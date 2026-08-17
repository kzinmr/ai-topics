---
title: "xAI Releases Grok 4.6 + Grok Bot — AI Teammates Enter the Frontier"
created: 2026-08-13
updated: 2026-08-17
type: event
tags:
  - xai
  - model
  - coding-agents
  - agent-team-swarm
  - event
sources:
  - raw/newsletters/2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md
  - raw/newsletters/2026-08-13-xai-s-grok-4-6-released-frontier-intelligence-at-insane-pricing.md
  - raw/newsletters/2026-08-13-grok-bot-is-not-what-you-think.md
  - raw/newsletters/2026-08-14-ben-s-session-2.md
  - raw/newsletters/2026-08-14-grok-bot.md
  - raw/newsletters/2026-08-16-anthropic-s-trust-equation-google-s-show-of-hands-and-grok-never-logs-off.md
---

# Event: xAI Releases Grok 4.6 + Grok Bot

**Date**: August 13, 2026
**Type**: Model Release + Agent Product Launch
**Significance**: xAI released **Grok 4.6**, a frontier model positioned on price/performance (Artificial Analysis Intelligence Index ~61, "arguably the second best knowledge work model in the world"), alongside **Grok Bot** — xAI's first entry into the [[concepts/multi-agents/agent-team-swarm|AI teammate]] category ("AI teammates that do real work for you... sign in to your tools, use them just like you do, and come back with finished work"). The AI teammate/multiplayer/multiagent space is described by AINews as "the next big AI battleground," and Grok Bot is its most significant new entrant yet.

## Overview

On August 13, 2026, xAI announced Grok 4.6 as a major step up from [[events/grok-4-5-launch|Grok 4.5]] at the same price. The release landed on what AINews called a "Frontier Model Day" — the same day as Qwen3.8-Max open weights, DeepSeek V4 Pro GA, and Microsoft's MAI-Thinking-1. Grok Bot (early beta) is powered by Grok 4.6 and marks xAI's entry into agentic knowledge work, competing with Claude Tag/[[entities/claude-code|Claude Code]]-style teammates for a category that AINews says "was still open for a new category leader."

## Key Details — Grok 4.6

- **Confirmed 1.5T parameter model**, a step up from Grok 4.5
- **Artificial Analysis Intelligence Index: 61**, exactly level with GPT-5.6 Sol and two points off Claude Opus 5 (Superintel+ Aug 2026 reporting); behind Claude Opus/Fable but with strong agentic results; near GPT-5.6 Sol and Claude Fable on webdev tasks
- **API pricing**: **$2 per million input tokens, $6 per million output tokens** — vs Sol's $5 input (Superintel+, Aug 2026). Grok 4.5 measured 56 on the Intelligence Index in early July 2026, making 4.6 a five-point jump
- **AA-Briefcase Elo 1577** — second only to Claude Opus 5 (1715), above Claude Fable 5 (1574) and clearly above GPT-5.6 Sol (1502) ([[concepts/ai-benchmarks/aa-briefcase]], Artificial Analysis agentic knowledge work benchmark, "at substantially lower cost than other leading models")
- **Training disclosure**: longer supplemental training run than Grok 4.5, using curated model-generated data for reasoning and advanced technical concepts; Grok 4.5 was used to regenerate SFT trajectories across reasoning efforts, agent harnesses, STEM, software engineering, and knowledge work, with model-based checks filtering problematic traces
- **⚠️ Cursor data contamination**: Cursor disclosed that an earlier snapshot of its own codebase was accidentally included in Grok 4.6's training data; CursorBench is being rebuilt as a result (Superintel+, Aug 2026)
- **Agentic RL**: trained on a wide range of agentic RL tasks — knowledge work, general coding, and domain-specific environments for kernel optimization, web development, and computer-aided design (CAD)
- **Pricing**: materially below frontier peers (per Artificial Analysis); practitioners immediately framed it as "the new default for coding and bug-finding workloads"
- **Reported behavior**: more self-testing behavior during long tasks
- **Roadmap**: Grok 4.7 initial training complete, with supplemental training on SpaceX internal data planned; Ben's Bites reported 4.7 expected within weeks (Aug 2026)

## Key Details — Grok Bot

- **Status**: Early beta, announced August 13, 2026
- **Positioning**: "Bots are AI teammates that do real work for you. They sign in to your tools, use them just like you do, and come back with finished work."
- **Category context**: AINews frames this as the AI teammate/multiplayer/multiagent space's most significant new entrant — coding agents "breaking containment into knowledge work" has been a recurring theme, and Grok Bot is xAI's answer to the teammate category
- **Requirement**: Grok Bot requires sign-in to user tools (agentic tool access), contrasting with Claude Tag which AINews says requires a more technical user
- **Hands-on (Ben's Bites, Aug 2026)**: Users "personify" their agents — each agent gets a system prompt such as "you are ben's money manager agent"; agents can send messages to one another and each has access to its own virtual computer (which the user can watch them use). Currently accessible only on the $200/month plan (Cursor or Grok). Powered by Grok 4.6, with 4.7 expected within weeks. Ben Tossell's comparison: "Codex or Claude can do the same things but require a few more steps."

### Grok Bot Follow-ups (Aug 14, 2026)

Two follow-up analyses the day after launch added architectural detail:

**Ben's Bites "session #2 — personal agents are just files and folders"** (Aug 14): Tossell demystified the category — "nothing special to being a personal bot — it's a file and folder system." Key points:

- **Architecture**: each agent gets its own thread, a **shared computer**, and **per-agent memory stored as text files**; a **teach** feature lets users instruct agents; **automation routines** (cron-style) handle recurring tasks.
- **Category framing**: OpenClaw, Hermes, and Grok Bot are "not different products, per se, they're just packaged like one. It's really just about the setup" — the same file-and-folder substrate, different packaging.
- **Compaction + file persistence**: Tossell discussed context compaction (the [[concepts/ai-agent-engineering|harness]] trick of summarizing conversation state) combined with filesystem persistence as the durable-memory mechanism — a notable contrast to vector-store "memory" hype.

**AI by Aakash "Grok Bot."** (Aug 14): Aakash Gupta's 7-day-trial hands-on review:

- **xAI's $60B acquisition of Cursor closed** the week of the launch, pairing the acquisition with "what some are calling the product launch of the year."
- **Multi-agent substrate**: each bot runs a **persistent cloud computer**, logs into your apps, and handles tasks across interfaces; it returns to the human **only for approvals**; multiple bots run at once and coordinate on their own.
- **Skill self-evolution**: bots can grow their own skills over time — an architecture similar to Hermes-style skill systems ([[concepts/ai-agent-engineering]]).
- **Chief of Staff coordination**: xAI positions a coordinating agent that directs the other bots.
- **Verdict**: better single products exist (Autoresearch, GBrain, Hermes, ChatGPT Work, Claude Design, Cowork), but Grok Bot is "xAI's strongest entry" into the AI teammate category.

**Distribution — GitHub Copilot (Aug 14, 2026)**: Grok 4.6 became available inside **GitHub Copilot** (github.blog changelog, Aug 14), extending the model's distribution beyond xAI's own products into the mainstream coding-agent ecosystem. Artificial Analysis published benchmark coverage of Grok 4.6 the same day. (Source: The Signal roundup, 2026-08-16.)

## Strategic Context

Grok 4.6 continues xAI's capability-per-dollar strategy established with Grok 4.5 (co-trained with [[concepts/spacex-cursor-acquisition|Cursor]] following SpaceX's acquisition of Anysphere). The same-price upgrade at frontier-adjacent quality, combined with the Grok Bot teammate product, positions xAI against Anthropic's Claude teammate/agent products, OpenAI's agent stack, and the broader [[concepts/ai-agent-engineering|AI agent engineering]] landscape.

The launch is notable for the **economics-first framing**: independent evaluation (Artificial Analysis) is treated as the reference point, and the pricing advantage is the headline — consistent with xAI's value-leader positioning in [[entities/xai]].

## Source

- AINews (swyx / Latent Space) newsletter, August 13, 2026 — "[SpaceXAI Grok 4.6 and Grok @Bot](https://www.latent.space/p/ainews-spacexai-grok-46-and-grok)"
- Superintel+ (Kim Isenberg), August 13, 2026 — "[xAI's Grok 4.6 Released: Frontier Intelligence At Insane Pricing](https://read.getsuperintel.com/p/xai-s-grok-4-6-released-frontier-intelligence-at-insane-pricing)" (API pricing, AA-Briefcase Elo, Cursor data contamination)
- Ben's Bites (Ben Tossell), August 13, 2026 — "[Grok Bot is not what you think](https://www.bensbites.com/p/grok-bot-is-not-what-you-think)" (hands-on review)
- Ben's Bites (Ben Tossell), August 14, 2026 — "[Ben's session #2](https://www.bensbites.com/p/bens-session-2)" (personal agents as file-and-folder systems; Grok Bot architecture)
- AI by Aakash (Aakash Gupta), August 14, 2026 — "[Grok Bot.](https://www.aibyaakash.com/p/grok-bot)" (7-day-trial review; $60B Cursor acquisition closed)

## Related Pages

- [[entities/xai]] — parent entity
- [[events/grok-4-5-launch]] — predecessor model launch (July 9, 2026)
- [[entities/grok-4-3]] — earlier Grok model specs
- [[concepts/multi-agents/agent-team-swarm]] — AI teammate / multi-agent orchestration category
- [[concepts/ai-benchmarks/aa-briefcase]] — agentic knowledge work benchmark
