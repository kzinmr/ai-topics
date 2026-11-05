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

## Related

- [[entities/ian-nuttall]] — author (Practical Programmatic; URL Monitor sold for $250k)
- [[entities/amp]] — the coding agent Nuttall pairs it with
- [[concepts/mcp]] — the integration protocol it exposes
