# Week 18: OpenClaw Channels — Connect to Telegram

Your agent runs on a server. But right now you can only talk to it via SSH. That's not useful for everyday use.

This week you connect it to **Telegram** so you can message your agent from your phone.

---

## Step 1: Create a Telegram Bot

1. Open **Telegram** on your phone or computer
2. Search for **@BotFather** (it has a blue checkmark)
3. Send it this message:

```
/newbot
```

4. BotFather asks for a **name** — this is the display name (e.g., "My AI Agent")
5. BotFather asks for a **username** — this must end in `bot` (e.g., `my_ai_agent_bot`)
6. BotFather gives you a **token** — it looks like `7123456789:AAHq...`

**Copy that token.** You'll need it in the next step.

> **Important**: Keep your bot token secret. Anyone with it can control your bot.

---

## Step 2: Connect OpenClaw to Telegram

SSH into your server:

```bash
ssh root@YOUR_IP_ADDRESS
```

Add the Telegram channel:

```bash
openclaw channels add --channel telegram --token YOUR_TELEGRAM_BOT_TOKEN
```

Replace `YOUR_TELEGRAM_BOT_TOKEN` with the token from BotFather.

Verify it's connected:

```bash
openclaw channels list
```

You should see Telegram listed.

---

## Step 3: Test It

1. Open Telegram
2. Search for your bot's username (the one ending in `bot`)
3. Click **Start**
4. Send a message: "Hello!"

Your agent should reply. You're now chatting with your own AI agent on Telegram.

Try asking it about the skill you wrote last week.

---

## Step 4: Write a Second Skill

Your agent needs more abilities. Pick one of these or make up your own:

### Idea 1: Daily Quote
A skill that shares an inspiring or interesting quote when asked.

### Idea 2: Homework Reminder
A skill that helps organize homework tasks and deadlines.

### Idea 3: Quick Facts
A skill about a subject you're studying — give it key facts and formulas.

Create the skill:

```bash
mkdir -p /opt/openclaw/workspace/skills/useful_skill
nano /opt/openclaw/workspace/skills/useful_skill/SKILL.md
```

Use the template in `useful_skill/SKILL.md` in this folder as a starting point.

Test it via Telegram — send a message that should trigger your new skill.

---

## Step 5: Customize the Experience

Make your agent more useful:

1. **Update IDENTITY.md** — give it a proper introduction
   ```bash
   nano /opt/openclaw/workspace/IDENTITY.md
   ```

2. **Test from your phone** — send it messages throughout the day. What's useful? What's missing?

3. **Share it** — send the bot username to a friend or family member. See what they ask it.

---

## Tasks

1. **Create the Telegram bot** and connect it to OpenClaw.
2. **Test at least 10 messages** via Telegram.
3. **Write a second skill** using one of the ideas above (or your own).
4. **Have someone else try it** — see what they think.
5. **Fill in `reflection.md`**.

---

## Deliverables

- Screenshot of a Telegram conversation with your bot
- Your second `SKILL.md` file
- `reflection.md` filled in

---

## Troubleshooting

**Bot doesn't respond?**
- Check that the channel is connected: `openclaw channels list`
- Check logs: `openclaw logs --tail 20`
- Make sure the bot token is correct

**Responses are slow?**
- This is normal — the agent is running on a small server and calling the Anthropic API
- Typical response time is 2-5 seconds

**Stuck?**

> "I connected OpenClaw to Telegram but [describe what happens]. The logs say: [paste log output]. What's wrong?"
