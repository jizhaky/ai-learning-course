# Week 13: AI Agents — What They Are and How They Work

Welcome to Module 2. You've built neural nets, trained GPT, called APIs, and built a RAG system. Now you're going to build something that actually *does things* on its own: an AI agent.

---

## What is an AI Agent?

An AI agent is just three things in a loop:

1. **An LLM** (like Claude) that reads a situation and decides what to do
2. **Tools** that the LLM can call (search, calculate, read files, etc.)
3. **A loop** that keeps going until the LLM says "I'm done"

That's it. The LLM thinks, picks a tool, gets the result, thinks again, picks another tool (or answers). This loop is what makes it an "agent" instead of a one-shot chatbot.

---

## The ReAct Pattern

The most common agent pattern is called **ReAct** (Reasoning + Acting). It works like this:

1. **Thought**: The LLM reasons about what to do next
2. **Action**: The LLM calls a tool
3. **Observation**: The tool returns a result
4. **Repeat** until the LLM has enough info to answer

Read this blog post from Anthropic — it's the best explanation of agent patterns out there:

**[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)** — Read at least the first half. You'll come back to it later.

---

## Setup

You need the Anthropic Python SDK. If you don't have it yet:

```bash
pip install anthropic
```

Create a `.env` file in this folder with your API key:

```bash
cp .env.example .env
```

Then open `.env` and paste your key:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

> **Don't have an API key?** Go to [console.anthropic.com](https://console.anthropic.com), sign in (your parent set this up), go to API Keys, and create one. Keep it secret — never commit it to git.

---

## Run the Starter Code

```bash
python react_loop.py
```

This runs a minimal ReAct agent with 3 simple tools. Watch what happens:

- You type a question
- Claude thinks about which tool to use
- The tool runs and returns a result
- Claude thinks again
- Eventually Claude gives you a final answer

Try these questions:
- "What is 42 * 67 + 13?"
- "What is the date today?"
- "Tell me about the Python programming language"

---

## Tasks

1. **Run the agent** with the questions above. Watch the tool calls in the output.
2. **Read the code**. Understand the loop. Where does Claude decide to use a tool vs. give a final answer?
3. **Add a new tool**. Ideas: `get_random_number`, `reverse_string`, or `count_words`. Follow the pattern of the existing tools.
4. **Try to break it**. Ask something none of the tools can help with. What happens?
5. **Read the Anthropic blog post** linked above. Write one thing you learned in your reflection.

---

## Deliverables

- `react_loop.py` with at least one new tool you added
- `reflection.md` filled in
- Screenshot or copy-paste of one interesting agent run

---

## Stuck?

Copy your error message and paste it into Claude or ChatGPT:

> "I'm building a ReAct agent with the Anthropic Python SDK. I got this error: [paste error]. Here's my code: [paste code]. How do I fix it?"

This is the same pattern from Module 1 — use AI to debug AI.
