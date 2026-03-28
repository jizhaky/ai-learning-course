# Week 14: Tool Use — Teaching Claude to Do Real Things

Last week your agent had mocked tools. This week you give it real ones.

The key idea: Claude doesn't *run* tools. Claude *asks* you to run them. Your code runs the tool and sends the result back. Claude just picks which tool to call and what arguments to pass.

---

## How Tool Schemas Work

When you call Claude with tools, you send a JSON schema for each tool. The schema tells Claude:

- **name**: What to call it
- **description**: When to use it (Claude reads this to decide)
- **input_schema**: What arguments it needs (JSON Schema format)

Claude reads these descriptions and decides which tool fits the situation. Better descriptions = better tool selection.

---

## How the Flow Works

```
You: "What's on the front page of Hacker News?"
 |
 v
Claude: "I should use web_search to check Hacker News"
        → tool_use: web_search(url="https://news.ycombinator.com")
 |
 v
Your code: fetches the URL, returns the HTML text
 |
 v
Claude: "Here are the top stories: ..."
```

The stop_reason in Claude's response tells you what happened:
- `"end_turn"` = Claude is done talking, here's the answer
- `"tool_use"` = Claude wants to use a tool, run it and send the result back

---

## This Week's Code

Open `tools.py` — this has three real tool functions:
- **web_search**: Fetches a URL and returns the text content
- **read_file**: Reads a local file
- **calculate**: Evaluates math expressions

Open `tool_agent.py` — this is the agent that uses those tools in a loop.

---

## Setup

Same as last week. Make sure you have your `.env` file:

```bash
cp .env.example .env
```

Install dependencies:

```bash
pip install anthropic python-dotenv
```

---

## Run It

```bash
python tool_agent.py
```

Try these:
- "Read the file tools.py and tell me what functions are in it"
- "What is 2**10 + 3**10?"
- "Fetch https://httpbin.org/json and summarize what you get"

---

## Tasks

1. **Run the agent** with the examples above. Watch how Claude picks tools.
2. **Read `tools.py`**. Understand each function. What could go wrong with each one?
3. **Add a new tool**. Ideas:
   - `list_directory(path)` — lists files in a folder using `os.listdir()`
   - `write_file(path, content)` — writes content to a file
   - `get_weather(city)` — fetch weather from a free API like wttr.in: `https://wttr.in/{city}?format=3`
4. **Improve the descriptions**. Change a tool's description and see if Claude uses it differently.
5. **Fill in `reflection.md`**.

---

## Deliverables

- `tool_agent.py` and `tools.py` with at least one new tool
- `reflection.md` filled in
- Copy-paste of one run showing the agent using multiple tools

---

## Stuck?

Same pattern as always — paste your error into Claude or ChatGPT:

> "I'm building a tool-use agent with the Anthropic SDK. My tool returns [X] but Claude doesn't seem to understand it. Here's my tool definition: [paste]. What's wrong?"
