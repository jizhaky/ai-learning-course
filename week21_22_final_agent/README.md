# Weeks 21-22: Final Project — Build Your Own AI Agent

This is it. Two weeks to build an AI agent that solves a real problem for you.

No templates. No step-by-step instructions. You decide what to build, how to build it, and how to make it good.

---

## Requirements

Your final project must have:

1. **2+ custom skills** — not copies of what you built before, but new skills that work together
2. **Connected to Telegram** — you (and others) can chat with it from a phone
3. **Solves a real problem** — something you'd actually use, not a toy demo
4. **Custom personality** — SOUL.md and IDENTITY.md that make it yours

---

## Timeline

### Week 21: Build
- Day 1-2: Pick your project and plan the skills
- Day 3-4: Write SOUL.md, IDENTITY.md, and your first skill
- Day 5-6: Write your second skill and test everything
- Day 7: Fix bugs, polish

### Week 22: Polish and Present
- Day 1-3: Test with real use, fix issues, improve skills
- Day 4-5: Have at least 2 other people try it and give feedback
- Day 6: Make final improvements based on feedback
- Day 7: Write your final reflection

---

## Getting Started

1. **Pick a project** from `project_ideas.md` or come up with your own
2. **Plan your skills** — what should each one do?
3. **Start with templates** — use the files in `project_template/` as a starting point
4. **Build on your server**:

```bash
ssh root@YOUR_IP_ADDRESS
```

Create your project:

```bash
# Back up your current workspace (just in case)
cp -r /opt/openclaw/workspace /opt/openclaw/workspace_backup

# Edit your soul
nano /opt/openclaw/workspace/SOUL.md

# Edit your identity
nano /opt/openclaw/workspace/IDENTITY.md

# Create skills
mkdir -p /opt/openclaw/workspace/skills/skill_one
nano /opt/openclaw/workspace/skills/skill_one/SKILL.md

mkdir -p /opt/openclaw/workspace/skills/skill_two
nano /opt/openclaw/workspace/skills/skill_two/SKILL.md
```

Test as you go:

```bash
openclaw chat "test message for skill one"
openclaw chat "test message for skill two"
```

---

## Deliverables

1. **Your SOUL.md** (copy to this repo)
2. **Your IDENTITY.md** (copy to this repo)
3. **Your skill files** (copy each SKILL.md to this repo)
4. **Screenshots** of at least 5 Telegram conversations showing both skills in action
5. **Feedback notes** — what did the 2+ people who tested it say?
6. **`reflection.md`** — your final reflection on the course

---

## Grading Yourself

Ask yourself:
- Would I actually use this agent? (If yes, you built something good)
- Do both skills work reliably? (Test each one 5+ times)
- Does the personality feel right? (Not generic, not annoying)
- Did other people find it useful or interesting?

---

## Stuck?

You have all the tools:
- Re-read your SKILL.md files from previous weeks for patterns
- Ask Claude for help: "I'm building an OpenClaw skill for [X]. It should [describe behavior]. Write me a SKILL.md."
- Check OpenClaw logs: `openclaw logs --tail 50`
- Re-read the Anthropic blog post from Week 13 for agent design ideas

This is your project. Make it something you're proud of.
