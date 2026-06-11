---

title: Browserbase
type: entity
aliases:
- browserbase-hq
- stagehand
created: 2026-04-13
updated: 2026-05-26
tags:
  - entity
  - developer-tooling
  - browser-agent
  - infrastructure
sources:
  - raw/articles/2026-05-18_browse-sh-browserbase_agent-skills-catalog.md
  - https://www.browserbase.com/
  - https://www.browserbase.com/blog/stagehand-v3
  - https://docs.browserbase.com/introduction/stagehand
  - https://www.browserbase.com/blog/introducing-the-stagehand-api

---

# Browserbase

**Browserbase** is a platform providing reliable browser automation infrastructure for AI agents. It handles "the where" (where to execute) and builds an integrated three-layer architecture with Stagehand (the what) and Stagehand API (the how).

## Overview

| Item | Details |
|---|---|
| Valuation | $300M (Series B) |
| Key Customers | Vercel, Perplexity, Clay |
| Open Source | Stagehand (22k+ GitHub stars, 700k+ weekly downloads) |
| Core Value | Secure browser fleet management, scalability |

## Three-Layer Platform Architecture

```
┌─────────────────────────────────────────────┐
│  Stagehand (the what)                          │
│  Open-source AI automation framework                │
│  Natural language commands: act(), extract(), observe()│
├─────────────────────────────────────────────┤
│  Stagehand API (the how)                       │
│  Hosted intelligence engine                          │
│  Prompt → CDP action conversion and optimization     │
├─────────────────────────────────────────────┤
│  Browserbase (the where)                       │
│  Cloud browser infrastructure                        │
│  Secure, scalable, stealth                           │
└─────────────────────────────────────────────┘
```

## Stagehand v3 (October 2025)

### Graduation from Playwright
- Eliminated Playwright dependency, operates at protocol level
- Modular driver system introduced
- Native operation across multiple environments including Bun
- Enhanced iframes/shadow DOM traversal

### Performance Improvements
- 44%+ faster across all benchmarks vs v2
- Notable improvements in deeply nested iframes/shadow DOM
- CI/CD integration optimization

### Supported Languages
- **TypeScript/Node.js**: `npx create-browser-app`
- **Python**: `uv run` + stagehand SDK
- **Java / Go / Ruby**: SDK supported

## Key Features

1. **Host Browser Fleet**: Secure browser environments at scale
2. **Session Inspector**: Visualize and debug all AI decisions
3. **Model Gateway**: Route LLM requests via Browserbase API key
4. **Browse.sh** (May 2026): Catalog of 100+ browser skills. AI-driven skill generation via Autobrowse. `npm i -g browse`. Reduces agent site rediscovery cost by 45%
5. **MCP Server**: Run directly on infrastructure (March 2026)
6. **Fetch API**: Browser-based data fetching (March 2026)
7. **Search**: In-browser search functionality (March 2026)
8. **Concurrency**: Expanded from 1 to 3 on free plan (March 2026)
9. **Prime Intellect Integration**: Browser agent training and evaluation (March 2026)

## Differences from browser-use

| Dimension | Browserbase | browser-use |
|---|---|---|
| Focus | Infrastructure (hosting) | Framework (operation logic) |
| Stagehand | Natural language commands | Agent loop |
| Offering | Managed browsers | Local/cloud both |
| OSS | Stagehand only | Entire core library |
| Complement | Can be used together | Can integrate with Browserbase Cloud |

## Related Entities

- [[entities/browse-sh]] — Browser skill catalog
- [[entities/browser-use]] — Open-source browser automation
- [[concepts/browser-agent/death-of-browser]] — The dehumanization of the browser
- [[entities/webmcp]] — Standardization protocol
- [[entities/anthropic-computer-use]] — Screenshot-based approach

## Sources

- [Stagehand v3 Announcement](https://www.browserbase.com/blog/stagehand-v3)
- [Stagehand API](https://www.browserbase.com/blog/introducing-the-stagehand-api)
- [Stagehand Documentation](https://docs.browserbase.com/introduction/stagehand)
