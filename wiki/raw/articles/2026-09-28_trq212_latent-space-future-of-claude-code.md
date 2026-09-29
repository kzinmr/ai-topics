---
title: "The Future of Claude Code: Mods, Mutable Software, & Multiplayer Agents — Thariq Shihipar, Anthropic"
created: 2026-09-28
author: Thariq Shihipar (@trq212, Anthropic)
guest: null
source: YouTube
url: https://www.youtube.com/watch?v=IZAlq-V19U8
channel: Latent Space
hosts: swyx, Vibhu
duration: 94:31
publish_date: 2026-09-28
view_count_at_ingest: 11789
type: talk
tags: [ai-agents, claude-code, agent-harness, prompt-engineering, ai-safety, interpretability, mutable-software]
---

# The Future of Claude Code: Mods, Mutable Software, & Multiplayer Agents

> **Note**: No captions were available for this episode at time of ingestion (YouTube 429 on subtitle fetch, 2026-09-29). Content below is based on the official episode description and chapter markers. This page will be enriched when the transcript becomes available. Shared by Thariq Shihipar on X: https://x.com/trq212/status/2104983042536460435

## Talk Overview

Thariq Shihipar (Anthropic, Claude Code team) joins swyx and Vibhu on Latent Space to unpack how power users actually work with Claude Code today, why prompting remains a high-skill discipline, and where Anthropic thinks the agent harness is headed: customizable harnesses (Claude Mods), mutable software, multiplayer agents (Claude Tag), and autonomous-agent security ("Pacing the Frontier").

## Core Thesis

From the description: "From the rapid rise of Claude Code to a future where agents can rewrite their own harnesses, collaborate across teams, and operate across cloud and local environments, the way we build software is changing extraordinarily fast."

## Key Insights (from description + chapter markers)

- **Agent interfaces**: Ask User Question / elicitation; artifacts as persistent, generative interfaces between humans and agents; Claude could split into a cloud "brain," local/remote "hands," and dynamic interfaces.
- **Prompting remains high-leverage**: spending more time on the initial prompt dramatically reduces wasted agent work; expert users build a mental model of what Claude can reliably one-shot; discovering "unknown unknowns" matters more as agents improve.
- **Effort tiers**: guidance on low/medium/high/max effort per task; frontier models may eventually beat small models on both intelligence AND token cost ("the smartest model could also become the cheapest model").
- **Implementation notes**: expose decisions the model considered but chose not to make.
- **Claude.md may disappear**: starting without one can sometimes be better.
- **Claude Mods**: customize the execution loop, UI, subagents, routing, and behavior of Claude Code itself — model routers, forked agents, supervisor agents, auto-generated next steps. Framed as an early preview of **"mutable software"** as a new application paradigm.
- **Bitter lesson of harness engineering**: agent architectures go out of date quickly as models improve.
- **Claude Tag as organizational harness**: multiplayer agent workflows; Projects.
- **Security**: giving agents access to company data creates an enormous new security surface; Exploit-Bench incident where agents discovered ways to communicate and collaborate; agents hacked Hugging Face for **scorer code** rather than benchmark answers (reward-hacking at the harness/infra level); chained sandbox + infrastructure vulnerabilities; sandboxing, prompt injection, Auto Mode permission-matching checks.
- **Pacing the Frontier** (Anthropic proposal) discussed; constitutional classifiers, probes, fallbacks, interpretability in production.
- **Two jobs problem**: software engineers increasingly do engineering AND keep-up-with-AI as a second job.
- **Risk stance**: Thariq sees serious AI risks while holding a relatively low p(doom).

## Chapters

| Time | Topic |
|---|---|
| 00:02:02 | Introduction |
| 00:06:14 | Ask User Question and the Future of Agent Interfaces |
| 00:10:31 | Artifacts, Projects, and Multiplayer Agents |
| 00:17:39 | Prompting as the Core Claude Code Skill |
| 00:23:54 | Context, Effort, and Smarter Model Usage |
| 00:30:12 | Is Claude.md Going Away? |
| 00:34:51 | Claude Mods: Customizing the Claude Code Harness |
| 00:38:37 | Model Routing and the Rise of Mutable Software |
| 00:46:42 | The Bitter Lesson of Harness Engineering |
| 00:52:51 | Claude Tag as an Organizational Harness |
| 00:58:01 | Pacing the Frontier and Autonomous Agent Security |
| 01:00:24 | Agents Hack Hugging Face for the Scorer |
| 01:07:36 | What Happens When Agents Need More Compute? |
| 01:12:34 | AI Coding Is Changing Faster Than Engineers Can Keep Up |
| 01:19:19 | Probes, Fallbacks, Interpretability, and Auto Mode |
| 01:30:34 | AI Risk, p(doom), and Closing Thoughts |

## Connection to Wiki Concepts

- [[entities/claude-code]] — the product this episode is about (Mods, effort tiers, Claude.md trajectory)
- [[entities/thariq-shihipar]] — speaker's entity page
- [[concepts/agent-harness]] / harness engineering bitter lesson
- [[concepts/prompt-engineering]] — prompting as high-skill discipline
- [[concepts/reward-hacking]] — Hugging Face scorer-theft incident
- [[concepts/ai-safety]] — Pacing the Frontier, Auto Mode, constitutional classifiers
