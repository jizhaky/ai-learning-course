# Week 0: GitHub Setup

Before you start the course, you need a place to save your work. That place is GitHub.

**Git** is a tool that tracks changes to your files. **GitHub** is a website that stores your project online so you can access it from anywhere and show your work to others.

Why bother? Every week you'll write code, fill in reflections, and run experiments. Without Git, that work lives on one computer and nowhere else. With Git, it's backed up, versioned, and visible.

---

## Step 1: Create a GitHub account

1. Go to [github.com](https://github.com)
2. Click **Sign up**
3. Pick a username (this is public — keep it professional)
4. Use a real email address you check
5. Create a password
6. Verify your email when GitHub sends you a confirmation

That's it. You have a GitHub account.

---

## Step 2: Create your course repo from the template

1. Go to this link: [https://github.com/izhaky/ai-learning-course/generate](https://github.com/izhaky/ai-learning-course/generate)
2. You'll see a page that says "Create a new repository from ai-learning-course"
3. Under **Repository name**, type `ai-learning-course` (or whatever you want to call it)
4. Make sure **Public** is selected
5. Click the green **Create repository** button

You now have your own copy of all the course files.

---

## Step 3: Install Git

Git is a command-line tool. You need it on your computer to download and upload your work.

**Mac:**
Open Terminal (search for "Terminal" in Spotlight) and paste:
```bash
xcode-select --install
```
A popup will ask you to install developer tools. Click **Install** and wait for it to finish.

**Windows:**
1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the installer
3. Run it — click **Next** on every screen (the defaults are fine)
4. When it's done, open **Git Bash** from your Start menu

**Linux:**
Open a terminal and paste:
```bash
sudo apt install git
```

### Stuck?

If any step doesn't work on your machine, copy the error message and paste it into ChatGPT, Claude, or any AI assistant. Tell it what you were trying to do and what happened. Something like:

> "I'm trying to install Git on my Mac. I ran `xcode-select --install` and got this error: [paste error here]. How do I fix this?"

This is a real skill — learning to debug with AI is something you'll use throughout this course and beyond.

---

## Step 4: Tell Git who you are

Open your terminal (Terminal on Mac, Git Bash on Windows) and run these two commands. Replace the name and email with yours:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

This is how Git signs your work. Use the same email you used for GitHub.

---

## Step 5: Clone your repo

This downloads your repo to your computer. In your terminal, paste this command — but replace `YOUR-USERNAME` with your actual GitHub username:

```bash
git clone https://github.com/YOUR-USERNAME/ai-learning-course.git
```

Then move into the folder:

```bash
cd ai-learning-course
```

You should now see all the course files on your computer.

---

## Step 6: Make your first commit

Open the `README.md` file in any text editor. At the very top, add a line with your name:

```
# My AI Learning Course - [Your Name]
```

Save the file. Then run these three commands:

```bash
git add README.md
git commit -m "Add my name to README"
git push
```

What just happened:
- `git add` — stages the file (tells Git "I want to save this change")
- `git commit` — saves the change with a label
- `git push` — uploads it to GitHub

**save, label, upload.** That's Git in three commands.

---

## Step 7: Verify

Go to your repo on GitHub: `https://github.com/YOUR-USERNAME/ai-learning-course`

You should see your name in the README. If you do, you're set. Week 0 is done.

---

## After each week

When you finish a week's work, save it to GitHub:

```bash
git add .
git commit -m "Complete week 1"
git push
```

Replace the number with whatever week you just finished. That's it — three commands, every time.

Your commit history becomes your progress log. Anyone looking at your repo (including future you) can see exactly what you did and when.
