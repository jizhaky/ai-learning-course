"""Final project template for a small local AI tool."""

from __future__ import annotations

from pathlib import Path

from config import PROJECT_NAME, PROJECT_GOAL


def load_sample_data() -> str:
    return Path(__file__).with_name("sample_data.txt").read_text()


def main() -> None:
    print(f"Project: {PROJECT_NAME}")
    print(f"Goal: {PROJECT_GOAL}\n")

    sample_text = load_sample_data()
    print("Loaded sample data:\n")
    print(sample_text)
    print()

    # TODO: Replace this section with the core logic of your project.
    # Examples:
    # - retrieve useful notes
    # - summarize input
    # - score reflections
    # - generate step-by-step help
    print("TODO: implement your project logic here.")

    # TODO: Add a simple command-line loop or function-based workflow.
    print("TODO: decide what the user types in and what your tool returns.")

    # TODO: Add one improvement idea based on your own feedback from the course.
    print("TODO: connect the project to a real user need.")


if __name__ == "__main__":
    main()
