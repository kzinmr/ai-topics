---
title: "10 Things Senior AI Engineers Stopped Wasting Tokens On"
date: 2026-05-12
type: x_note_tweet
url: https://x.com/deronin_/status/2054255152555545079
author: Ronin (@DeRonin_)
author_id: "1414948050817196037"
engagement:
  likes: 421
  bookmarks: 1012
  reposts: 34
  replies: 16
  quotes: 4
  impressions: 47391
quotes: https://x.com/DeRonin_/status/2054235707791778034
tags:
  - ai-coding
  - cost-optimization
  - token-economics
  - model-routing
  - prompt-caching
  - context-engineering
  - vibe-coding
---

# 10 Things Senior AI Engineers Stopped Wasting Tokens On

> Andrej Karpathy: "90% of your AI coding bill is paying for context you didn't need to send"

Here are 10 things senior AI engineers stopped wasting tokens on:

1. **Auto-context loading 50 files for a 30-line fix**: $1.20/turn for tokens you'll never read. 80% input waste, every session

2. **Running Opus on lint, format, and rename tasks**: $0.60 for what Haiku nails at $0.02. 30x overpay on the cleanup tier

3. **Tool call loops that re-send the full repo on every retry**: 5x context cost per agentic flow. fixing these alone cuts 30-50% of bills

4. **Sonnet as the default model**: Kimi 2.6 matches its quality on most coding tasks at 1/6 the cost. defaulting to Sonnet in 2026 is leaving 60-70% on the table

5. **Streaming responses on stable-prefix workflows**: kills your prompt cache. you pay 10x for tokens that should have cost cents

6. **"Just in case" file includes**: 80,000-token prompts that should be 3,000. context bloat is the silent budget killer

7. **Per-session knowledge rebuilding**: 10 min writing a SKILL.md once vs paying agents to re-figure out your environment every run. $4 vs $0.30 per execution

8. **Single-model setups**: premium tier on every task is the most expensive mistake in AI coding right now

9. **Asking 10 small questions one at a time**: 10 separate input prefix charges vs one batched call. 70-90% savings on routine workflows

10. **Buying Claude Pro + ChatGPT Plus + Cursor Pro**: you seriously use one. the other two are habit, not utility

**What actually compounds instead:**

- context discipline (grep before fetching, always)
- prompt caching on every stable prefix
- multi-model routing (Kimi 2.6 default, Opus for the 10%)
- graduated skills via SKILL.md files
- profiling tool calls before optimizing prompts
- the routing mindset (right model for right task)

> in 12 months, the gap between developers shipping on $200/month and $4,000/month budgets won't be skill — it'll be how well they route

**Full guide quoted**: [How To Cut Your AI Coding Bill by 80% (FULL GUIDE)](https://x.com/i/article/2053183959341711361)
