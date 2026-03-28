"""
Week 16: Memory Agent
======================
An agent with two types of memory:
1. Conversation history (within a session)
2. Persistent notes (survives restarts via JSON file)

Run it: python memory_agent.py
"""

import os
import json
from dotenv import load_dotenv

load_dotenv()

import anthropic

from memory_store import save_note, get_note, list_notes

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-20250514"

# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "save_note",
        "description": "Save a note to persistent memory. Use this when the user asks you to remember something, save information, or store a note. The note will survive even if the conversation ends.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "A short name for the note, like 'todo', 'favorites', 'user_info'. Use snake_case.",
                },
                "content": {
                    "type": "string",
                    "description": "The content to save.",
                },
            },
            "required": ["key", "content"],
        },
    },
    {
        "name": "get_note",
        "description": "Retrieve a saved note by its key. Use this when the user asks about something that was previously saved.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "The key of the note to retrieve.",
                }
            },
            "required": ["key"],
        },
    },
    {
        "name": "list_notes",
        "description": "List all saved notes with previews. Use this when the user asks what you know or remember, or to see all saved information.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    # TODO: Add delete_note and search_notes tool definitions here
]

TOOL_FUNCTIONS = {
    "save_note": lambda args: save_note(args["key"], args["content"]),
    "get_note": lambda args: get_note(args["key"]),
    "list_notes": lambda args: list_notes(),
    # TODO: Add your new tools here
}

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a helpful assistant with persistent memory.

You have tools to save and retrieve notes. When the user tells you something worth remembering (preferences, facts about themselves, tasks, etc.), save it as a note.

When the user asks what you know about them or asks about something previously discussed, check your notes first.

Key behaviors:
- Proactively save important information the user shares
- When asked "what do you know about me?", list your notes
- Use descriptive keys for notes (e.g., "favorite_language", "current_project")
- If a note already exists with the same key, updating it replaces the old content
"""

# ---------------------------------------------------------------------------
# Agent loop with conversation memory
# ---------------------------------------------------------------------------


def run_agent():
    """Run the agent with persistent conversation history."""
    print("Memory Agent — Week 16")
    print("This agent remembers things between messages AND between restarts.")
    print("Try: 'Remember that my favorite color is blue'")
    print("Then quit, restart, and ask: 'What's my favorite color?'")
    print("Type 'quit' to exit.\n")

    # Conversation history — persists within this session
    conversation: list[dict] = []

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye! Your notes are saved in agent_notes.json.")
            break
        if not user_input:
            continue

        # Add user message to conversation
        conversation.append({"role": "user", "content": user_input})

        try:
            # Agent loop — may take multiple iterations if tools are called
            messages = list(conversation)  # Copy so we can add tool results
            max_iterations = 10

            for _ in range(max_iterations):
                response = client.messages.create(
                    model=MODEL,
                    max_tokens=1024,
                    system=SYSTEM_PROMPT,
                    tools=TOOLS,
                    messages=messages,
                )

                if response.stop_reason == "tool_use":
                    tool_results = []

                    for block in response.content:
                        if block.type == "text":
                            pass  # Claude's thinking, don't print yet
                        elif block.type == "tool_use":
                            func = TOOL_FUNCTIONS.get(block.name)
                            if func:
                                result = func(block.input)
                            else:
                                result = f"Unknown tool: {block.name}"

                            print(f"  [{block.name}: {json.dumps(block.input)}]")

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
                    # Final text response
                    final_text = ""
                    for block in response.content:
                        if hasattr(block, "text"):
                            final_text += block.text

                    print(f"\nAssistant: {final_text}")

                    # Save assistant response to conversation history
                    conversation.append(
                        {"role": "assistant", "content": final_text}
                    )
                    break

        except anthropic.APIError as e:
            print(f"\nAPI Error: {e}")
            # Remove the failed user message from history
            conversation.pop()
        except Exception as e:
            print(f"\nError: {e}")
            conversation.pop()


if __name__ == "__main__":
    run_agent()
