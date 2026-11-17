---
title: "SEO Skill"
type: entity
created: 2026-11-05
updated: 2026-11-05
tags: [tool, mcp, agent-native, developer-tooling]
aliases:
  - seoskill
  - seoskill.dev
description: "Open-source SEO tool by Ian Nuttall for 'agent-native teams' — gives a team's AI coding agents (Claude Code, Codex, any MCP client) access to real Search Console, Google Analytics, and Bing data plus Google algorithm-update dates and site crawls, via a free hosted MCP server and an open-source CLI, so agent answers about search come from your own numbers."
sources:
  - "https://seoskill.dev"
  - "https://github.com/iannuttall/seo"
---

# SEO Skill

**SEO Skill** ([seoskill.dev](https://seoskill.dev), [github.com/iannuttall/seo](https://github.com/iannuttall/seo)) is an **open-source SEO tool for "agent-native teams"** built by **Ian Nuttall** ([@iannuttall](https://x.com/iannuttall)). Its thesis: instead of an AI agent *guessing* about your search performance, connect it to your **real** Search Console, Google Analytics and Bing data so every answer about traffic comes from your own numbers.

## What it is

- **Distribution:** a free **hosted MCP server** (`https://seoskill.dev/mcp`) and an **open-source CLI** (`npm i -g seo && seo start`). Works with **Claude Code, Codex, or any MCP client** (`claude mcp add --transport http seoskill …`).
- **Data sources:** Google Search Console, Google Analytics, Bing, plus **Google algorithm-update dates** and a **site crawl**. Some pieces (site crawls, Bing) run locally on your own machine because Bing blocks the hosted server.
- **Use cases:** "find out why traffic moved" — the agent pulls clicks/impressions vs. the prior period, the affected pages and queries, matching GA sessions, and the Google updates that fall between the dates.

## Positioning

SEO Skill is part of the broader **"agent-native" / MCP-for-real-data** pattern — exposing a domain (SEO) as a first-class tool surface that coding agents call directly, rather than a human-oriented dashboard. Ian Nuttall frames it within his stack of agent-run business workflows (he also recommends **Amp** as a Conductor replacement for running customer support, SEO, GitHub issues, iOS builds, and product planning through an agent — see [[entities/amp]] and [[entities/ian-nuttall]]).

## `seo lint` — AI-writing-pattern detection (November 2026)

`seo lint` is a CLI subcommand that "find[s] the lines in a blog post, landing page, title
or meta description that read as AI-written, with a fix for each"
([docs](https://seoskill.dev/docs/lint)), demonstrated in the author's own
"AI slop" explainer ([seoskill.dev/blog/ai-slop](https://seoskill.dev/blog/ai-slop)): "AI
slop is AI-made content published without a careful read. The writing patterns that give it
away, the research behind them, and a free check for your drafts."

Announced by Nuttall on Nov 11, 2026 as work in progress
([tweet](https://x.com/iannuttall/status/2120449713426354623)). The strategic oddity is
that an **agent-native SEO tool now includes an AI-text detector**: the same agent that
drafts the page runs the lint that proves it doesn't read as AI-written. Content generation
and content audit are being bundled into one toolchain, with the
"publish without a careful read" failure mode named explicitly as the thing to machine-check.

## Go-to-market: public teardown series (November 2026)

SEO Skill is marketed through **public SEO teardowns of named SaaS products**, each posted
as a reply to the target's founders — the teardown is simultaneously the sales pitch and a
worked demo of the tool's output:

| Date | Target | Angle |
|---|---|---|
| Nov 9 | **Dub** (link shortening) | "higher Domain Rating than Rewardful, 399 affiliate programs and payout data from $20 million. Here's how I'd use them." [post](https://seoskill.dev/blog/how-id-grow-dub) |
| Nov 10 | **TypingMind** (AI chat app for your own API keys) | "The pricing, API key and comparison pages it has, and why they don't rank." [post](https://seoskill.dev/blog/how-id-grow-typingmind) |
| Nov 15 | **Loops** (SaaS email platform) | "some SEO ideas that won't cost you 10k" — priced against agency spend. [post](https://seoskill.dev/blog/how-id-grow-loops) |

Also promoted around Google core-algorithm rollouts, where the **Google update-date
dataset** is the differentiator for the "did this update do this to me?" question
([tweet](https://x.com/iannuttall/status/2120227530896732273), Nov 10).

**Monetization open question (Nov 13):** in a reply to @michael_chomsky, Nuttall said he is
"considering just making it free and finding another way to sustain it"
([tweet](https://x.com/iannuttall/status/2121160175759302767)) — consistent with the
agent-native-tools pattern of the free tool feeding an audience/course business.

## Related

- [[entities/ian-nuttall]] — author (Practical Programmatic; URL Monitor sold for $250k);
  see his [[entities/ian-nuttall#X Activity Log (November 2026)|November 2026 activity log]]
- [[entities/keep]] — Nuttall's companion Markdown capture tool for agent context
- [[entities/amp]] — the coding agent Nuttall pairs it with
- [[concepts/mcp]] — the integration protocol it exposes
