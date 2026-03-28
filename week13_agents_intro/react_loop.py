"""
Week 13: Minimal ReAct Agent
============================
This is a simple agent that uses Claude + tools in a loop.
Run it: python react_loop.py

The agent has 3 tools:
- search_wikipedia: Returns info about a topic (mocked for demo)
- calculate: Does simple math
- get_current_date: Returns today's date

Watch how Claude decides which tool to use and loops until it has an answer.
"""

import os
import json
from datetime import datetime

# Load API key from .env file
# If you don't have python-dotenv: pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

import anthropic

client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY from environment

MODEL = "claude-sonnet-4-20250514"

# ---------------------------------------------------------------------------
# Tools — these are the functions the agent can call
# ---------------------------------------------------------------------------


def search_wikipedia(topic: str) -> str:
    """
    Mocked Wikipedia search. In a real agent, this would hit an API.
    For now it returns hardcoded responses so you can see the pattern.

    TODO: Try replacing this with a real API call!
    You could use the Wikipedia API:
    https://en.wikipedia.org/api/rest_v1/page/summary/{topic}
    """
    fake_results = {
        "python": "Python is a high-level programming language created by Guido van Rossum in 1991. It emphasizes code readability and supports multiple programming paradigms including procedural, object-oriented, and functional programming.",
        "artificial intelligence": "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence displayed by animals and humans. AI research focuses on creating systems that can reason, learn, and act autonomously.",
        "neural network": "A neural network is a computing system inspired by biological neural networks in the brain. It consists of layers of interconnected nodes (neurons) that process information using mathematical functions.",
    }

    # Check if any key matches (case-insensitive)
    topic_lower = topic.lower()
    for key, value in fake_results.items():
        if key in topic_lower:
            return value

    return f"No Wikipedia article found for '{topic}'. Try a different search term."


def calculate(expression: str) -> str:
    """
    Evaluates a simple math expression.
    Only allows basic math — no imports or dangerous code.

    TODO: What happens if someone passes in something that isn't math?
    Try it and see. How would you make this safer?
    """
    # Only allow numbers and basic math operators
    allowed_chars = set("0123456789+-*/.() ")
    if not all(c in allowed_chars for c in expression):
        return f"Error: expression contains invalid characters. Only numbers and +-*/.() are allowed."

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def get_current_date() -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")


# ---------------------------------------------------------------------------
# Tool definitions — this is what we send to Claude so it knows what's available
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "search_wikipedia",
        "description": "Search Wikipedia for information about a topic. Returns a summary of the topic.",
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic to search for",
                }
            },
            "required": ["topic"],
        },
    },
    {
        "name": "calculate",
        "description": "Calculate a mathematical expression. Supports basic arithmetic: +, -, *, /, parentheses.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The math expression to evaluate, e.g. '42 * 67 + 13'",
                }
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_current_date",
        "description": "Get the current date and time.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
]

# Map tool names to functions so we can call them dynamically
TOOL_FUNCTIONS = {
    "search_wikipedia": lambda args: search_wikipedia(args["topic"]),
    "calculate": lambda args: calculate(args["expression"]),
    "get_current_date": lambda args: get_current_date(),
}

# TODO: Add your own tool here! Follow the pattern above:
# 1. Write a Python function
# 2. Add a tool definition dict to TOOLS
# 3. Add it to TOOL_FUNCTIONS


# ---------------------------------------------------------------------------
# The ReAct Loop — this is the core of the agent
# ---------------------------------------------------------------------------


def run_agent(user_message: str) -> str:
    """
    Runs the ReAct loop:
    1. Send user message + tools to Claude
    2. If Claude wants to use a tool → run it, send result back
    3. If Claude gives a text response → we're done
    """
    print(f"\n{'='*60}")
    print(f"User: {user_message}")
    print(f"{'='*60}")

    messages = [{"role": "user", "content": user_message}]

    # Loop until Claude gives a final text answer
    while True:
        # Call Claude with the conversation so far
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )

        print(f"\n--- Claude's response (stop_reason: {response.stop_reason}) ---")

        # Check if Claude wants to use a tool
        if response.stop_reason == "tool_use":
            # Process each content block
            tool_results = []
            for block in response.content:
                if block.type == "text":
                    print(f"Thinking: {block.text}")
                elif block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    tool_id = block.id

                    print(f"Tool call: {tool_name}({json.dumps(tool_input)})")

                    # Run the tool
                    if tool_name in TOOL_FUNCTIONS:
                        result = TOOL_FUNCTIONS[tool_name](tool_input)
                    else:
                        result = f"Error: unknown tool '{tool_name}'"

                    print(f"Tool result: {result}")

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_id,
                            "content": result,
                        }
                    )

            # Add Claude's response and tool results to the conversation
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})

        else:
            # Claude gave a final text answer — we're done
            final_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_text += block.text

            print(f"\nFinal answer: {final_text}")
            return final_text


# ---------------------------------------------------------------------------
# Main — run the agent interactively
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("ReAct Agent — Week 13")
    print("Type a question and watch the agent think + use tools.")
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
        except Exception as e:
            print(f"\nError: {e}")
            print("If this is an API error, check your .env file and API key.")
