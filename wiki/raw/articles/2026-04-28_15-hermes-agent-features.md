---
title: "15 Hermes Agent features you've never touched"
type: x-article
date: 2026-04-28
source: twitter
tweet_id: 2049139067359568032
author: Hermes Agent
url: https://x.com/i/article/2049139067359568032
bookmark_count: see_metadata
---

# 15 Hermes Agent features you've never touched

Most people install Hermes and treat it like a smarter ChatGPT. They wire up Telegram, point it at a model, type a request, get a response. Then they close the window and call it a day.
If that's you, you're using roughly 8% of what Hermes can actually do.
Here are 15 features, ranked by how much they change your output. Most people who've been running Hermes for months have never touched a single one on this list.
THE SETUP MOST PEOPLE SKIP ENTIRELY
1. /personality + SOUL.md
Hermes reads a single file at boot called SOUL.md. Whatever you put in there becomes your agent's voice forever. Across every session, every platform, every backend. Use /personality to switch between named personas mid-conversation.
Define how it talks. What it refuses. Who it thinks it's writing for. Write it once. Stop typing "you are a senior X expert" at the top of every conversation.
Most people retype the same role primer every single session.
 
2. MEMORY.md + USER.md
Two persistent files Hermes reads on every session. MEMORY.md is the agent's notebook on what's true about your projects. USER.md is what it knows about you specifically: your role, your tone, your context, your tradeoff preferences.
Indexed with FTS5 and an LLM summarizer so the agent can pull a relevant memory from 8 weeks ago into a session today.
Most people re-explain who they are every time they open a new chat.
3. /insights [days]
Analytics across every session you've ever run. Which projects ate the most tokens. Which providers cost what. What the agent stalled on. What you keep coming back to.
/insights 30 shows you the last month at a glance.
Most people open a new session blind because they didn't know /insights exists.
 
4. /snapshot
Save the entire Hermes config and state as a snapshot before you do anything risky. Experiment, break things, /snapshot restore <id> to get back to the known-good state.
The "I'm about to refactor my SOUL.md and I might regret it" command.
Most people don't know rollbacks exist for the agent itself.
 
THE MID-FLIGHT CONTROL NOBODY USES
5. /branch (alias /fork)
Branch the current session to explore a different path without losing the original. Like git for conversations. Try a riskier approach without burning
your good context, come back if it doesn't work.
Most people start a new session and lose every byte of context they just built up.
---
6. /rollback
Filesystem checkpoints. Agent ran a destructive edit and broke your code? Don't reach for git, just /rollback. Hermes keeps checkpoints of every file it
touched and you can restore any of them.
Most people learn this exists the hard way, after the agent eats their work.
---
7. /btw
Ephemeral side question that uses session context but doesn't call any tools and doesn't get persisted. The "quick gut check, don't pollute my main
thread" command.
Most people open a whole new session for a one-off question, then lose all their context when they come back.
---
8. /steer and /queue
You're 3 tool calls into a long agentic task and you realize the agent is using the prod API when it should be using staging. Don't kill the run.
/steer use the staging API not prod. The next tool call sees your note. The current turn doesn't get interrupted. The prompt cache stays warm.
Pair with /queue to line up the next turn without interrupting the current one.
Most people kill the run and start over.
---
9. /yolo, /fast, /reasoning
Three power toggles most users never touch. /yolo skips all dangerous-command approvals (use it carefully). /fast switches the session to OpenAI
Priority Processing or Anthropic Fast Mode for lower latency. /reasoning sets the reasoning effort level for o-style models.
Most people accept the defaults forever and wonder why their sessions feel slow.
---
THE PROVIDER LOCK-IN THAT ISN'T
---
10. /model [--provider] [--global]
Hermes is provider-agnostic by design. One command swaps the model behind your agent without restarting. Anthropic Opus 4.7, OpenAI Codex (GPT-5.5 via
OAuth, no API key needed), OpenRouter, NVIDIA NIM, Kimi, Gemini, AWS Bedrock, Vercel AI Gateway, Xiaomi MiMo, Step Plan, Arcee.
/model anthropic:claude-opus-4-7 to switch to Opus. /model openrouter:kimi-k2.6 to drop to a cheaper option for grunt work. The agent state carries
over.
Most people get locked into one provider because they don't realize Hermes was built portable from day one.
---
11. Auxiliary models
The agent does more than answer your prompts. It also compresses context, summarizes sessions, generates titles, runs vision tasks. Hermes lets you
assign a different model to each side task.
Run Opus 4.7 as your main brain, Haiku 4.5 for compression, a tiny model for title generation. Configure once via hermes model and the auxiliary screen
handles the rest.
Most people pay Opus rates for Haiku-grade work, every single session.
---
THE REACH NOBODY ACTIVATES
---
12. The 17-platform gateway
Telegram, Discord, Slack, WhatsApp, Signal, Email, SMS, Matrix, Mattermost, Feishu, WeCom, DingTalk, BlueBubbles, Home Assistant, QQBot, plus CLI and
voice. One Hermes process drives every one of them.
Run hermes gateway and you're broadcasting to every platform your team actually lives on. Pair via DM, gate by allowlisted users, rate-limit per
channel.
Most people stop after Telegram and never wire up the other 16.
---
13. /voice (real-time voice on 4 platforms)
Real-time voice in the CLI, in Telegram DMs, in Discord channels, and in Discord voice channels. Type /voice and just talk.
Useful when you're walking, driving, or away from a keyboard. Useful when typing is slower than talking, which is most of the time.
Most people only ever type at it.
---
14. Cron + /webhook-subscriptions
Hermes ships with a built-in cron scheduler. You write the schedule in plain language and tell it where to deliver the result.
"Every Friday at 5pm, summarize this week's GitHub commits and post to my Slack #standups channel." Hermes parses, runs unattended, delivers wherever
you said.
Pair it with /webhook-subscriptions for the inverse: external services (GitHub, Vercel, Stripe, uptime checks) push payloads directly to your DMs with
zero LLM cost. Zero tokens spent. Zero latency.
Most people pay for a Zapier sub to do exactly this.
---
THE THING THAT SEPARATES SERIOUS USERS
---
15. Skills are slash commands
This is the one most people never figure out. Hermes ships with 100+ skills out of the box and every single one is a slash command. Type / and they
autocomplete.
/architecture-diagram for SVG architecture art. /excalidraw for hand-drawn diagrams. /manim-video for 3Blue1Brown-style animations.
/research-paper-writing for end-to-end ML paper drafts. /linear for issue management. /google-workspace for Gmail and Calendar and Drive and Docs and
Sheets. /imessage for sending texts. /youtube-content for transcripts to threads. /codex and /claude-code to delegate to other agents.
/test-driven-development to enforce RED-GREEN-REFACTOR. /systematic-debugging for 4-phase root-cause analysis.
The kicker: you can write your own. I have a custom skill called /sage-x. It spots outliers in my niche, scouts trends, recommends what to post, drafts
reactive QTs and threads, batches my daily output in my voice. I built it once. Type /sage-x in any of my Hermes sessions on any of my platforms and it
runs. Forever.
Most people use slash commands once a week. Real users have built their entire workflow into them.
---
THE IRONY THAT SHOULD BOTHER EVERYONE
You paid for an agent with persistent memory, 100+ pre-built skills, filesystem rollback, session branching, mid-flight steering, 17-platform messaging
reach, voice mode, native multi-provider routing, auxiliary model routing, cron automation, webhook integration, and the ability to write your own slash
commands.
And you've been using it as a fancier Telegram bot.
The tool wasn't underdelivering. You never gave it the instructions it was waiting for.
 
If you found this useful, follow me @sharbel on X.
And if you run a business, we build content systems for founders in order to attract the right audience for you, and convert it into revenue. If you want to have these same systems installed for you, book a call with us at FounderFunnel.com.
