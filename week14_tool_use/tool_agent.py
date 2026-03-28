"""
Week 14: Tool Use Agent
========================
An agent with real tools: web search, file reading, and math.
Run it: python tool_agent.py
"""

import os
import json
from dotenv import load_dotenv

load_dotenv()

import anthropic

from tools import web_search, read_file, calculate

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-20250514"

# ---------------------------------------------------------------------------
# Tool definitions — Claude reads these to decide which tool to use
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "web_search",
        "description": "Fetch a web page and return its text content. Use this to look up information online. Pass a full URL starting with http:// or https://.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The full URL to fetch, e.g. 'https://example.com'",
                }
            },
            "required": ["url"],
        },
    },
    {
        "name": "read_file",
        "description": "Read the contents of a local file. Use this when the user asks about a file on disk.",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, e.g. 'tools.py' or '/home/user/notes.txt'",
                }
            },
            "required": ["file_path"],
        },
    },
    {
        "name": "calculate",
        "description": "Evaluate a mathematical expression. Supports +, -, *, /, ** (power), and parentheses.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The math expression to evaluate, e.g. '2**10 + 3**10'",
                }
            },
            "required": ["expression"],
        },
    },
]

# TODO: Add your new tool definition here! Match the format above.

# Map tool names to functions
TOOL_FUNCTIONS = {
    "web_search": lambda args: web_search(args["url"]),
    "read_file": lambda args: read_file(args["file_path"]),
    "calculate": lambda args: calculate(args["expression"]),
}

# TODO: Add your new tool to TOOL_FUNCTIONS too.

# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a helpful assistant with access to tools.
Use your tools when you need to look up information, read files, or calculate things.
Always explain what you're doing and why you chose a particular tool.
If a tool returns an error, explain what went wrong and try a different approach."""


def run_agent(user_message: str) -> str:
    """Run the agent loop until Claude gives a final answer."""
    print(f"\n{'='*60}")
    print(f"User: {user_message}")
    print(f"{'='*60}")

    messages = [{"role": "user", "content": user_message}]
    max_iterations = 10  # Safety limit — don't loop forever

    for i in range(max_iterations):
        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        print(f"\n--- Step {i+1} (stop_reason: {response.stop_reason}) ---")

        if response.stop_reason == "tool_use":
            tool_results = []

            for block in response.content:
                if block.type == "text":
                    print(f"  Thinking: {block.text}")
                elif block.type == "tool_use":
                    print(f"  Tool: {block.name}({json.dumps(block.input)})")

                    # Execute the tool
                    func = TOOL_FUNCTIONS.get(block.name)
                    if func:
                        result = func(block.input)
                    else:
                        result = f"Unknown tool: {block.name}"

                    # Show a preview of the result
                    preview = result[:200] + "..." if len(result) > 200 else result
                    print(f"  Result: {preview}")

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
            # Final answer
            final_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_text += block.text

            print(f"\nFinal answer:\n{final_text}")
            return final_text

    print("\nAgent hit the iteration limit. Something might be wrong.")
    return "Agent stopped after too many iterations."


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Tool Use Agent — Week 14")
    print("This agent can fetch web pages, read files, and do math.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break
        if not user_input:
            continue

        try:
            run_agent(user_input)
        except anthropic.APIError as e:
            print(f"\nAPI Error: {e}")
            print("Check your .env file and make sure your API key is correct.")
        except Exception as e:
            print(f"\nError: {e}")
