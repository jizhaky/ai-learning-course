# Week 17: OpenClaw Basics — Your Own AI Agent in the Cloud

You've been building agents on your laptop. Now you deploy one to a real server that runs 24/7.

**OpenClaw** is an open-source AI agent platform. You give it a personality (SOUL.md), tell it what it can do (skills), connect it to chat channels (like Telegram), and it runs on its own.

This week: get it running, understand the file structure, and write your first skill.

---

## Step 1: Deploy OpenClaw on DigitalOcean

> **Get a parent for this step — you'll need a credit card for DigitalOcean ($12/month).**

1. Go to [https://marketplace.digitalocean.com/apps/openclaw](https://marketplace.digitalocean.com/apps/openclaw)
2. Click **Create Droplet**
3. Choose your settings:
   - **Region**: Pick the datacenter closest to you (e.g., New York, San Francisco, London)
   - **Size**: The cheapest option ($12/mo) is fine
   - **Authentication**: Choose **SSH Key** (more secure than password)
     - If you don't have an SSH key, click "New SSH Key" and follow the instructions
     - Or choose Password if your parent prefers (make it strong)
4. Click **Create Droplet**
5. Wait about 1 minute for it to provision
6. Copy the IP address from your DigitalOcean dashboard

---

## Step 2: SSH into Your Server

Open your terminal and connect:

```bash
ssh root@YOUR_IP_ADDRESS
```

Replace `YOUR_IP_ADDRESS` with the actual IP from Step 1.

If it asks about fingerprint authenticity, type `yes`.

> **Stuck?** If SSH doesn't work, paste the error into Claude: "I'm trying to SSH into my DigitalOcean droplet and got this error: [paste]"

---

## Step 3: Run the OpenClaw Setup

Once you're SSH'd in, run the setup wizard:

```bash
/opt/openclaw-tui.sh
```

This opens a text menu. Follow the prompts:

1. **Pick your AI provider**: Choose **Anthropic**
2. **Paste your API key**: The same `sk-ant-...` key you've been using
3. **Set a name**: Give your agent a name (e.g., "Atlas", "Nova", whatever you want)

Test it with a message:

```bash
openclaw chat "Hello, are you working?"
```

You should get a response. Your agent is alive.

---

## Step 4: Understand the Workspace Files

Your OpenClaw agent lives in `/opt/openclaw/workspace/`. Let's look at what's there:

```bash
ls /opt/openclaw/workspace/
```

Key files:

### `SOUL.md`
This is your agent's personality and core instructions. It's like the system prompt but permanent. OpenClaw reads this file every time it handles a message.

```bash
cat /opt/openclaw/workspace/SOUL.md
```

### `IDENTITY.md`
Your agent's name, who it is, how it should introduce itself.

```bash
cat /opt/openclaw/workspace/IDENTITY.md
```

### `TOOLS.md`
Documents what built-in tools the agent has access to.

```bash
cat /opt/openclaw/workspace/TOOLS.md
```

### Skills folder
Skills are modular abilities you add to your agent. Each skill is a folder with a `SKILL.md` file.

```bash
ls /opt/openclaw/workspace/skills/
```

---

## Step 5: Write Your First Skill

A skill is just a markdown file that tells OpenClaw how to do something. Let's make one.

Pick a topic you know about — a school subject, a hobby, a game, anything.

Create the skill folder:

```bash
mkdir -p /opt/openclaw/workspace/skills/my_first_skill
```

Create the skill file:

```bash
nano /opt/openclaw/workspace/skills/my_first_skill/SKILL.md
```

Use this template (also available in this repo as `my_first_skill/SKILL.md`):

```markdown
# My First Skill: [Topic Name]

## Purpose
Answer questions about [your topic] clearly and accurately.

## When to Use
When the user asks about [your topic].

## Behavior
- Answer in a friendly, clear way
- If you're not sure about something, say so
- Give examples when they help

## Knowledge
[Write 5-10 facts or pieces of information about your topic here.
The agent will use these when answering questions.]

1. ...
2. ...
3. ...
```

Save the file (in nano: Ctrl+O, Enter, Ctrl+X).

Test it:

```bash
openclaw chat "Tell me about [your topic]"
```

---

## Step 6: Edit the Soul

Make your agent yours. Open the SOUL.md:

```bash
nano /opt/openclaw/workspace/SOUL.md
```

Add some personality:
- How should it talk? (casual, formal, funny?)
- What does it care about?
- What should it refuse to do?

Save and test:

```bash
openclaw chat "Who are you and what can you help with?"
```

---

## Tasks

1. **Deploy OpenClaw** following the steps above.
2. **Write your first skill** about a topic you choose.
3. **Customize SOUL.md** with a personality you like.
4. **Test at least 5 messages** with your agent.
5. **Fill in `reflection.md`**.

---

## Deliverables

- Screenshot of `openclaw chat` working
- Your `SKILL.md` file (copy it to this folder in your repo too)
- `reflection.md` filled in

---

## Stuck?

> "I'm setting up OpenClaw on DigitalOcean. I got to [step] and [what happened]. The error is: [paste]. How do I fix this?"

Also check the OpenClaw docs: [https://github.com/openclawai/openclaw](https://github.com/openclawai/openclaw)
