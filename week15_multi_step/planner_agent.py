"""
Week 15: Multi-Step Planning Agent
====================================
An agent that plans before it acts.

Phase 1: Claude breaks the question into steps
Phase 2: The agent executes each step with tools
Phase 3: Claude synthesizes all results into a final answer

Run it: python planner_agent.py
"""

import os
import json
import urllib.request
import urllib.error
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-20250514"

# ---------------------------------------------------------------------------
# Tools (same as Week 14, included here so this file runs standalone)
# ---------------------------------------------------------------------------


def web_search(url: str) -> str:
    """Fetch a URL and return text content."""
    try:
        if not url.startswith(("http://", "https://")):
            return f"Error: URL must start with http:// or https://"
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (Learning Agent)"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
        # Simple tag stripping
        import re

        text = re.sub(r"<[^>]+>", " ", raw)
        text = re.sub(r"\s+", " ", text).strip()
        return text[:5000] if len(text) > 5000 else text
    except Exception as e:
        return f"Error: {e}"


def read_file(file_path: str) -> str:
    """Read a local file."""
    try:
        blocked = [".env", "id_rsa", "id_ed25519", ".ssh"]
        if any(b in file_path.lower() for b in blocked):
            return "Error: cannot read sensitive files"
        if not os.path.exists(file_path):
            return f"Error: file not found: {file_path}"
        with open(file_path, "r") as f:
            content = f.read()
        return content[:5000] if len(content) > 5000 else content
    except Exception as e:
        return f"Error: {e}"


def calculate(expression: str) -> str:
    """Evaluate a math expression."""
    allowed = set("0123456789+-*/.() eE")
    if not all(c in allowed for c in expression):
        return "Error: invalid characters in expression"
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def get_current_date() -> str:
    """Get current date."""
    return datetime.now().strftime("%A, %B %d, %Y")


TOOLS = [
    {
        "name": "web_search",
        "description": "Fetch a web page by URL and return its text content.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Full URL to fetch"}
            },
            "required": ["url"],
        },
    },
    {
        "name": "read_file",
        "description": "Read the contents of a local file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Path to the file"}
            },
            "required": ["file_path"],
        },
    },
    {
        "name": "calculate",
        "description": "Evaluate a math expression. Supports +, -, *, /, **, parentheses.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Math expression to evaluate",
                }
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_current_date",
        "description": "Get today's date.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
]

TOOL_FUNCTIONS = {
    "web_search": lambda args: web_search(args["url"]),
    "read_file": lambda args: read_file(args["file_path"]),
    "calculate": lambda args: calculate(args["expression"]),
    "get_current_date": lambda args: get_current_date(),
}


# ---------------------------------------------------------------------------
# Phase 1: Planning
# ---------------------------------------------------------------------------


def create_plan(question: str) -> list[str]:
    """Ask Claude to break a question into numbered steps."""
    print("\n--- Phase 1: Planning ---")

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system="""You are a planning assistant. Given a question, break it into clear numbered steps.
Each step should be a single action that can be done with one of these tools: web_search, read_file, calculate, get_current_date.
Output ONLY the numbered steps, nothing else. Keep it to 5 steps or fewer.

Example:
Question: "What's the population of France and Germany, and which is larger?"
1. Search for the population of France
2. Search for the population of Germany
3. Compare the two numbers and determine which is larger""",
        messages=[{"role": "user", "content": question}],
    )

    plan_text = response.content[0].text
    print(f"\nPlan:\n{plan_text}")

    # Parse numbered steps
    steps = []
    for line in plan_text.strip().split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            # Remove the number prefix
            step = line.lstrip("0123456789.)")
            step = step.strip(" .")
            if step:
                steps.append(step)

    return steps


# ---------------------------------------------------------------------------
# Phase 2: Execution
# ---------------------------------------------------------------------------


def execute_step(step: str, previous_results: list[str]) -> str:
    """Execute a single step using the agent loop."""
    # Build context from previous steps
    context = ""
    if previous_results:
        context = "\n\nResults from previous steps:\n"
        for i, result in enumerate(previous_results, 1):
            context += f"Step {i} result: {result}\n"

    messages = [
        {
            "role": "user",
            "content": f"Execute this step: {step}{context}\n\nUse your tools to complete this step. Be concise in your response.",
        }
    ]

    # Run tool loop for this step (max 5 iterations per step)
    for _ in range(5):
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    func = TOOL_FUNCTIONS.get(block.name)
                    result = func(block.input) if func else f"Unknown tool: {block.name}"
                    print(f"    Tool: {block.name}({json.dumps(block.input)}) -> {result[:100]}...")
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
        else:
            # Got a text response — step is done
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return "No result"

    return "Step timed out after too many tool calls."


def execute_plan(steps: list[str]) -> list[str]:
    """Execute each step in the plan, collecting results."""
    print("\n--- Phase 2: Execution ---")
    results = []

    for i, step in enumerate(steps, 1):
        print(f"\n  Step {i}: {step}")
        result = execute_step(step, results)
        results.append(result)
        print(f"  Result: {result[:200]}{'...' if len(result) > 200 else ''}")

    return results


# ---------------------------------------------------------------------------
# Phase 3: Synthesis
# ---------------------------------------------------------------------------


def synthesize(question: str, steps: list[str], results: list[str]) -> str:
    """Ask Claude to combine all results into a final answer."""
    print("\n--- Phase 3: Synthesis ---")

    # Build the step-by-step results
    step_results = ""
    for i, (step, result) in enumerate(zip(steps, results), 1):
        step_results += f"\nStep {i}: {step}\nResult: {result}\n"

    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system="You are a helpful assistant. Synthesize the research results into a clear, complete answer to the original question. Be thorough but concise.",
        messages=[
            {
                "role": "user",
                "content": f"Original question: {question}\n\nResearch results:{step_results}\n\nPlease synthesize these results into a clear answer.",
            }
        ],
    )

    return response.content[0].text


# ---------------------------------------------------------------------------
# Main agent
# ---------------------------------------------------------------------------


def run_planner_agent(question: str) -> str:
    """Run the full plan-execute-synthesize pipeline."""
    print(f"\n{'='*60}")
    print(f"Question: {question}")
    print(f"{'='*60}")

    # Phase 1: Plan
    steps = create_plan(question)

    if not steps:
        print("Could not create a plan. Answering directly.")
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            messages=[{"role": "user", "content": question}],
        )
        return response.content[0].text

    # Phase 2: Execute
    results = execute_plan(steps)

    # Phase 3: Synthesize
    final_answer = synthesize(question, steps, results)

    print(f"\n{'='*60}")
    print(f"Final Answer:\n{final_answer}")
    print(f"{'='*60}")

    return final_answer


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Multi-Step Planning Agent — Week 15")
    print("Ask complex questions that need multiple steps to answer.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break
        if not user_input:
            continue

        try:
            run_planner_agent(user_input)
        except anthropic.APIError as e:
            print(f"\nAPI Error: {e}")
        except Exception as e:
            print(f"\nError: {e}")
