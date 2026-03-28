# Week 16: Memory — Agents That Remember

Every agent you've built so far has amnesia. When you restart the script, it forgets everything. Ask it about something you discussed two minutes ago in a previous run — blank stare.

This week you fix that.

---

## Why Agents Forget

LLMs are stateless. Each API call is independent — Claude doesn't remember previous conversations unless you send them in the messages array. When you restart your script, that messages array is gone.

There are two kinds of memory you can give an agent:

### 1. Conversation Memory
The messages list you already know. As long as you keep appending to it, the agent remembers the current conversation. But it has limits — Claude's context window is large but not infinite.

### 2. Knowledge Memory (Persistent)
Save information to a file or database so it survives between runs. This is what you built in Week 10 with RAG — retrieve stored knowledge before answering. This week we do a simpler version: a note-taking system.

---

## This Week's Code

Two files:

- **`memory_store.py`** — A simple file-based note system. Functions: `save_note(key, content)`, `get_note(key)`, `list_notes()`. Stores everything in a JSON file.
- **`memory_agent.py`** — An agent that can save and retrieve notes, plus full conversation history within a session.

---

## Setup

```bash
cp .env.example .env
```

Install deps:

```bash
pip install anthropic python-dotenv
```

---

## Run It

```bash
python memory_agent.py
```

Try this sequence:
1. "Remember that my favorite programming language is Python"
2. "Remember that I'm working on a school project about climate change"
3. "What do you know about me?"
4. Quit and restart the agent
5. "What do you know about me?" — it should still remember!

Then try:
- "Save a note called 'todo' with: finish math homework, read chapter 5, practice guitar"
- "What's on my todo list?"
- "List all my notes"

---

## Tasks

1. **Run the agent** and test the save/retrieve flow above.
2. **Quit and restart**. Verify notes persist but conversation history is lost.
3. **Read `memory_store.py`**. It's short. Understand how notes are stored.
4. **Add a `delete_note` tool**. Add the function to `memory_store.py` and wire it into the agent.
5. **Add a `search_notes` tool** that finds notes containing a keyword.
6. **Think about limits**. What happens if you save 1000 notes? 1 million? How would you handle that?
7. **Fill in `reflection.md`**.

---

## How This Connects to RAG

In Week 10 you built a RAG system that retrieved relevant chunks from a document before answering. That's the same idea as knowledge memory — look up stored info before generating a response. The difference is scale:

- **This week**: Simple key-value notes in a JSON file
- **Week 10 RAG**: Embedded chunks with similarity search
- **Production systems**: Vector databases, semantic search, thousands of documents

They're all the same pattern: **retrieve, then generate**.

---

## Deliverables

- `memory_agent.py` and `memory_store.py` with your improvements
- `reflection.md` filled in
- The `agent_notes.json` file with at least 3 saved notes

---

## Stuck?

> "I'm building a memory system for an AI agent. Notes save fine but when I restart the agent, [describe problem]. Here's my memory_store.py: [paste code]. What's wrong?"
