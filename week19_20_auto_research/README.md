# Weeks 19-20: Auto Research Agent (2-Week Project)

This is your first multi-week project. You're going to build a **research agent** — an OpenClaw skill that takes a question, searches the web, reads pages, and writes a report with sources.

This combines everything from the last 6 weeks:
- Agent loops (Week 13)
- Tool use (Week 14)
- Multi-step planning (Week 15)
- Memory (Week 16)
- OpenClaw skills (Weeks 17-18)

---

## What You're Building

A skill that works like this:

```
You (via Telegram): Research: What are the pros and cons of nuclear energy?

Agent: I'll research that for you. Let me search for information...

[Agent searches the web, reads several pages, takes notes]

Agent: Here's what I found:

## Nuclear Energy: Pros and Cons

### Pros
- Low carbon emissions compared to fossil fuels (source: ...)
- High energy density (source: ...)
- Reliable baseload power (source: ...)

### Cons
- Radioactive waste storage (source: ...)
- High upfront construction costs (source: ...)
- Risk of accidents (source: ...)

### Sources
1. [URL 1]
2. [URL 2]
3. [URL 3]
```

---

## Week 19: Build the Skill

### Step 1: Understand the Research Pattern

The research agent follows this loop:

1. **Question** → User asks something
2. **Search** → Agent uses `web_search` to find relevant pages
3. **Read** → Agent uses `web_fetch` to read promising pages
4. **Extract** → Agent pulls out key facts and saves the source URL
5. **Synthesize** → Agent writes a report combining all facts
6. **Cite** → Agent includes source URLs

### Step 2: Create the Skill on Your Server

SSH into your server:

```bash
ssh root@YOUR_IP_ADDRESS
```

Create the skill folder:

```bash
mkdir -p /opt/openclaw/workspace/skills/research_skill
```

Copy the template from this repo (`research_skill/SKILL.md`) or create it:

```bash
nano /opt/openclaw/workspace/skills/research_skill/SKILL.md
```

The skill file tells OpenClaw:
- When to activate (user says "research:" or "look up:")
- What tools to use (web_search, web_fetch)
- How to format the output (sections, bullet points, sources)

### Step 3: Test Basic Searches

Try simple queries first:

```bash
openclaw chat "Research: What is the tallest building in the world?"
```

Watch the output. Does it search? Does it cite sources?

### Step 4: Iterate

The first version won't be perfect. Common issues:
- Agent doesn't search enough sources → Update SKILL.md to say "search at least 3 sources"
- Sources aren't cited → Add explicit instructions about including URLs
- Report is too short → Ask for "at least 200 words with specific facts"

---

## Week 20: Improve and Polish

### Make It Better

1. **Better search queries**: Add instructions for the agent to rephrase the question as a good search query
2. **Multiple perspectives**: Tell the agent to search for different viewpoints
3. **Fact checking**: Add a step where the agent verifies key claims across sources
4. **Better formatting**: Use headers, bullet points, and bold for key terms

### Test with Harder Questions

Try the questions in `example_queries.md`. These are designed to test different aspects:
- Questions that need multiple searches
- Questions with controversial answers
- Questions that need recent information

### Share It

Send research questions to your agent via Telegram. Share the bot with a friend and have them try it.

---

## Tasks

### Week 19:
1. Create the research skill on your OpenClaw server
2. Test with 3 simple research questions
3. Iterate on the SKILL.md at least twice based on results

### Week 20:
1. Test with the questions in `example_queries.md`
2. Improve the skill based on what you learned
3. Have someone else try it and get feedback
4. Fill in `reflection.md`

---

## Deliverables

- Your `research_skill/SKILL.md` (copy it to this repo folder)
- Screenshots of 3 research runs (including one from `example_queries.md`)
- `reflection.md` filled in

---

## Stuck?

> "I'm building a research skill for OpenClaw. The agent [searches but doesn't synthesize / doesn't cite sources / gives shallow answers]. Here's my SKILL.md: [paste]. How can I improve it?"

Remember: most problems with OpenClaw skills are solved by making the SKILL.md instructions clearer and more specific.
