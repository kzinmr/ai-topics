---
type: blog_post
author: Jason Liu
author_handle: "@jxnlco"
author_url: "https://jxnl.co"
url: "https://jxnl.co/writing/2026/05/18/six-levels-of-complexity-of-an-ai-powered-morning-brief-with-codex/"
date: 2026-05-18
tags: [codex, morning-brief, automation, agents-file, memory-vault, onboarding]
---

# Six levels of complexity in a Codex morning brief

Title: Six levels of complexity in a Codex morning brief - Jason Liu

URL Source: https://jxnl.co/writing/2026/05/18/six-levels-of-complexity-of-an-ai-powered-morning-brief-with-codex/

This is the easiest way I know to teach someone how to use AI.

Not by starting with models, agents, or some abstract taxonomy of what the technology can do. Start with a job people already understand, then make that job quietly more powerful.

The morning brief works because almost everyone already has one. They just assemble it badly.

I think the morning brief is the first Codex workflow that normal people actually understand.

You wake up, open Slack, check your calendar, click into email, forget why you opened email, go back to Slack, then realize you have a meeting in seven minutes and no idea what happened yesterday.

The appeal is simple: help me remember what is going on.

When we were talking about Codex onboarding, this was the first workflow that felt both boring enough to teach and strong enough to matter. It starts as a dumb little orientation prompt. If you keep pushing it, it turns into a pretty good model for how people actually graduate into using Codex seriously.

Start with the thing a beginner can understand. Then add one real capability at a time until the shape of the whole system becomes obvious.

I think there are six real levels.

## Level 1: ask your actual day what is going on

The first version is almost embarrassingly small.

Connect Slack, Gmail, and Calendar, then ask:

> Using Slack, Gmail, and Calendar, what do I have going on today?

Just see whether Codex can look across the three places your work usually hides and tell you something you actually care about.

## Level 2: add an agents file

The second level is adding a little bit of persistent instruction.

You already have enough raw surface area for Codex to be useful. Now you need to stop it from being generically helpful every single morning. This is where an agents file becomes useful.

## Level 3: ask it to keep an eye on this

The third level is adding recurrence, but I do not think I would teach it as "create an automation." I would say: Keep an eye on this every weekday morning.

## Level 4: split it into multiple project-level briefs

Eventually one brief gets mushy. I do not really want one universal daily assistant forever. I usually have multiple project threads, and each one gives me its own morning brief.

## Level 5: let the brief draft the work

At this level, the morning brief should not only tell me what happened. It should draft the obvious work that follows from the brief.

## Level 6: save what matters in a memory vault

The sixth level is where the brief stops being only a morning ritual and starts feeding a memory system.

If the morning brief keeps finding the same people, same projects, same open loops, and same decisions, some of that should leave the thread and become durable.

The smallest useful version might look like:
vault/
├── TODO.md
├── people/
├── projects/
├── daily/
├── notes/
└── AGENTS.md

## Why I like this ladder

Each level teaches a more serious way of using Codex without asking the user to jump straight into some grand agent architecture.

Level 1 teaches the connectors.
Level 2 teaches defaults through an agents file.
Level 3 teaches recurrence by asking Codex to keep an eye on this.
Level 4 teaches project-level briefs in durable threads.
Level 5 teaches the trust boundary I actually care about: draft the work, do not impersonate me.
Level 6 teaches the part that compounds: save durable context in a vault so tomorrow's brief starts smarter than today's.

That is why I would teach Codex through the morning brief. It begins as a simple summary and ends as a miniature operating system for your work.

