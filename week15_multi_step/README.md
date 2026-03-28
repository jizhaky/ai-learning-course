# Week 15: Multi-Step Agents — Planning and Execution

Your agents so far answer questions in one or two steps. But real problems are harder than that. "Compare the GDP of Japan and Germany over the last 5 years" isn't a one-tool question. You need to:

1. Look up Japan's GDP
2. Look up Germany's GDP
3. Compare them
4. Summarize

This week you build an agent that **plans first, then executes**.

---

## The Planning Pattern

Instead of jumping straight to tools, the agent:

1. **Takes the question** from the user
2. **Asks Claude to make a plan** — break it into numbered steps
3. **Executes each step** using tools
4. **Synthesizes** all the results into a final answer

This is powerful because:
- Claude can see the whole plan before starting
- Each step builds on the last
- If a step fails, the agent can adjust

---

## This Week's Code

`planner_agent.py` has everything:
- A planning phase (Claude writes the steps)
- An execution phase (each step gets its own tool calls)
- A synthesis phase (Claude combines all results into an answer)

---

## Setup

```bash
cp .env.example .env
```

Make sure your API key is in `.env`.

---

## Run It

```bash
python planner_agent.py
```

Try these complex questions:
- "What are the top 3 programming languages in 2024 and what is each one best used for?"
- "Read the file planner_agent.py and explain the three phases of how it works"
- "What is 2^10, 3^10, and 4^10? Which is largest and by how much?"

Watch how the agent breaks each question into steps before executing.

---

## Tasks

1. **Run the agent** with the questions above. Pay attention to the planning phase.
2. **Try your own complex question** — something that needs 3+ steps.
3. **Read the code**. Find where the plan gets created vs. where it gets executed.
4. **Experiment with the planning prompt**. Change the system prompt for the planner and see how the plans change. Can you make it create better plans?
5. **Add error handling**. What happens if one step fails? Modify the code so the agent notices and tries a different approach.
6. **Fill in `reflection.md`**.

---

## Deliverables

- `planner_agent.py` with your improvements
- `reflection.md` filled in
- Copy-paste of one multi-step run showing plan + execution + synthesis

---

## Stuck?

> "I'm building a multi-step planning agent. The planning phase works but the execution phase [describe problem]. Here's my code: [paste]. What's going wrong?"
