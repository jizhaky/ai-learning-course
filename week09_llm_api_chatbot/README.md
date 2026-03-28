# Week 9: LLM API Chatbot

## Objective

Build a command-line chatbot that uses an API key from a local environment file instead of hardcoding secrets in code.

## Required Videos

- Official API quickstart video or docs from your chosen provider
- Optional: a short prompt design talk after the first working version

## Tasks

1. Copy `.env.example` to `.env`.
2. Add your API key locally.
3. Run `python week9_chatbot.py`.
4. Try at least three prompts and then change the system prompt style.

## Deliverables

- A working CLI chatbot
- A local `.env` file that is not committed to git
- One note about how the prompt changed the behavior

## Checkpoint Questions

- Why should API keys stay outside source code?
- What is the system prompt doing?
- What should you log carefully when using external APIs?
- How would you make this bot more useful for a student?
