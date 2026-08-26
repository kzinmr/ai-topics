---
title: "Munder Difflin — Agent harness to run an office of your clones"
url: https://munderdiffl.in/
date: 2026-08-22
fetched_at: 2026-08-26
source: munderdiffl.in (product site, self-published)
tags: [agent-harness, multi-agent, cli-agents, clone-agents, local-first, e2e-encryption, open-source, agent-employees]
extraction: full (marketing site; vendor claims unverified)
---

# Munder Difflin — Agent harness to run an office of your clones

GitHub Trending **#1 Repository of the Day** (week of Aug 22, 2026). HN: 311 points, 146 comments.

Free, open source and performant multi-agent harness; works with your existing subscriptions (uses hourly limits).

## Core concept

Munder Difflin uses **CLI agents running on your computer** to "do anything you can do." It supports 12 CLI agent providers off the shelf: Claude Code, Codex, Grok, Kimi Code, Antigravity, Qwen, Gemini CLI, OpenCode, Crush, Pi, Copilot, Cursor. Agents can be monitored in an "'office'-themed simulation" or a cleaner fullscreen mode; the simulation is deterministic and does not consume tokens.

## Three-step model ("Three steps to a second you")

1. **Install your harness** — one download; wraps the agent CLI you already use and runs on your laptop. Your code, your keys, your existing subscription — nothing leaves your machine.
2. **It becomes you** — captures your workflow, tooling, and what you know. Every clone you run shares that memory, so the next one starts already knowing how you work.
3. **Your office gets to work** — clones work around the clock; when one needs something it messages another. They hand off work, share context, and unblock each other, all on your own machine.

## Architecture (per node)

- **GOD orchestrator** — reads, plans, routes
- Role agents — research (e.g., Claude Code), build (e.g., Codex), review (e.g., Claude Code), sell (Grok), draft (Kimi CLI)
- **git** — each agent in its own isolated worktree
- **MemPalace** — "their memory · their machine · nowhere else"
- Runs 24/7; kick off from anywhere (you, Slack inbox, triggers)

Clone-to-clone messaging is **E2E encrypted** (X25519 / AES-256-GCM per the site's wire diagram), same-org only. Clones ask each other questions at 3am, unblock each other overnight, and open PRs.

## Role coverage ("Not just for engineers")

Everything a computer does is reachable from the command line, and CLI agents can drive all of it:

- **Developer** — reviews PRs, fixes bugs, ships small features, babysits CI, keeps docs honest
- **Designer** — audits screens against the design system, exports assets, drafts specs and copy
- **Product manager** — writes specs, triages issues, keeps boards/docs in sync, preps standup summaries
- **Sales & GTM** — drafts outreach, preps call briefs, keeps the CRM honest, chases follow-ups
- **Everyone else** — reports, spreadsheets, files, scheduling, follow-ups — "anything scriptable. Which is everything."

## Security model ("Private by architecture, not just by promise")

- **Local-first** — each clone is a node on its owner's laptop; code, keys, and personal context never leave the machine (everything runs at 127.0.0.1)
- **End-to-end encrypted** — clone-to-clone messages encrypted on your node, decrypted only on your teammate's; nobody in between (including the vendor) can read them
- **Org context, your rules** — you decide what's shared team-wide vs personal; the shared knowledge base is provisioned once, versioned, and inherited by every new clone
- **Open source** — MIT licensed; every line of the node, the protocol, and the crypto is on GitHub for audit

## Commercial plans (vendor pricing)

- **PRO** (individual): from $20/month or $200/year; optional 24/7 shared sandbox from +$19/mo; first 100 Founding Supporters get 50% off + 1 month free
- **TEAMS / CLOUD+NETWORK**: from $39/seat/month; clones talk E2E, shared org knowledge; sandbox tiers from shared 1x CPU/1GB ($58/seat) to dedicated 4x CPU/16GB ($324/seat)
- **Founding Supporter**: $20 one-time; permanent plaque on the Founders' Wall; project "stays free for everyone"

## Notes

- Vendor-published marketing site; all performance/feature claims are self-reported and unverified.
- The "office of clones" framing + deterministic simulation UI is a distinctive differentiator vs. typical multi-agent harnesses (which usually expose raw agent logs, not a themed office).
- Memory-sharing-across-clones ("MemPalace") is closest in the wiki to agent-employees and personal-ai patterns.

**HN discussion**: https://news.ycombinator.com/item?id=49396002 (311 points, 146 comments, Aug 22 2026)
