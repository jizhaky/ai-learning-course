"""
Week 16: Simple File-Based Memory Store
=========================================
Stores notes as key-value pairs in a JSON file.
Notes persist between runs — this is the agent's long-term memory.
"""

import json
import os

NOTES_FILE = "agent_notes.json"


def _load_notes() -> dict:
    """Load notes from disk. Returns empty dict if file doesn't exist."""
    if not os.path.exists(NOTES_FILE):
        return {}
    try:
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def _save_notes(notes: dict) -> None:
    """Save notes to disk."""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


def save_note(key: str, content: str) -> str:
    """
    Save a note with a given key.

    Args:
        key: The name/key for the note (e.g., "todo", "favorites", "project_ideas")
        content: The content of the note

    Returns:
        Confirmation message
    """
    notes = _load_notes()
    notes[key] = content
    _save_notes(notes)
    return f"Saved note '{key}' successfully."


def get_note(key: str) -> str:
    """
    Retrieve a note by key.

    Args:
        key: The name/key of the note to retrieve

    Returns:
        The note content, or an error message if not found
    """
    notes = _load_notes()
    if key in notes:
        return notes[key]
    return f"No note found with key '{key}'. Use list_notes to see all saved notes."


def list_notes() -> str:
    """
    List all saved note keys and a preview of each.

    Returns:
        A formatted list of all notes, or a message if none exist
    """
    notes = _load_notes()
    if not notes:
        return "No notes saved yet."

    result = "Saved notes:\n"
    for key, content in notes.items():
        preview = content[:80] + "..." if len(content) > 80 else content
        result += f"  - {key}: {preview}\n"

    return result


# TODO: Add these functions:
#
# def delete_note(key: str) -> str:
#     """Delete a note by key."""
#     ...
#
# def search_notes(keyword: str) -> str:
#     """Search all notes for a keyword."""
#     ...


# Quick test — run this file directly to test the store
if __name__ == "__main__":
    print("Testing memory store...")
    print(save_note("test", "This is a test note"))
    print(get_note("test"))
    print(list_notes())
    print("Done! Check agent_notes.json")
