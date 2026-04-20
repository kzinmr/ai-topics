---
title: Martin Alderson
created: 2026-04-09
updated: 2026-04-10
tags:
  - person
  - blogger
  - hn-popular
  - ai
  - saas
  - developer-tools
  - economics
  - startup
---


# Martin Alderson

| | |
|---|---|
| **Blog** | [martinalderson.com](https://martinalderson.com) |
| **RSS** | https://martinalderson.com/feed.xml |
| **Role** | Writer at the intersection of software engineering and economics; AI transformation analyst |
| **Bio** | Software engineer and blogger focused on the economics of AI, the future of SaaS, agentic coding tools, and supply chain security. Known for data-driven analysis that cuts through AI hype — particularly on SaaS disruption, compute economics, and the widening productivity gap between AI power users and casual users. |

## Core Ideas

### The "$285 Billion Markdown Files" Thesis (Feb 2026)

Martin's most viral essay documented how **13 markdown files (~156KB)** in Anthropic's `knowledge-work-plugin` repository on GitHub triggered a **$285 billion selloff** in SaaS stocks on February 3, 2026 — roughly **$1M in market cap erased per byte of markdown**. The analysis cuts through media panic to identify a genuine structural shift:

> *"Instead of SaaS being replaced by 'agentically-built' SaaS, what if people just don't need (as much) SaaS?"*

Key insight: AI agents operate at a **higher abstraction level** than traditional SaaS. Instead of navigating dashboards and clicking through UIs, users prompt agents that directly execute tasks using raw source material (markdown, text files, APIs). This means:
- Professional services firms face disruption — their expertise is being codified into structured markdown
- Legacy SaaS platforms with poor API support are vulnerable; "headless" API-first platforms will win
- The future belongs to **API-first infrastructure** that treats agents as first-class consumers

### Two Kinds of AI Users: The Bifurcation (Feb 2026)

Martin identified a dramatic productivity divide that is accelerating:

**Power Users** — Often surprisingly non-technical (finance directors, marketers, operations staff) who use Claude Code in the terminal, build custom Python scripts, chain MCPs together, and achieve **10x–100x productivity gains**. One non-technical executive converted a 30-sheet Excel financial model to Python in 2–3 prompts using Claude Code.

**Casual Users** — Stuck with M365 Copilot and web-based chatbots, generating meeting agendas and summaries. Martin's assessment: *"One extremely jarring realisation was just how poor Microsoft Copilot is."*

The structural driver: **enterprise IT lockdown** prevents agentic tooling (no local script execution, no terminal access, locked-down laptops), while smaller companies with fewer legacy constraints are "absolutely flying with AI."

> *"I don't think there's ever been a time in history where a tiny team can outcompete a company one thousand times its size so easily."*

### The Open Source Supply Chain Crisis (Mar 2026)

Martin documented the cascading **TeamPCP supply chain attack** that compromised Trivy → LiteLLM (~22M weekly downloads) → Telnyx → Axios (~100M weekly downloads) in under two weeks. Key contribution: identifying **LLMs as an accelerant** for supply chain attacks:

1. LLMs lower the barrier to finding vulnerabilities — even non-experts can discover zero-days in minutes
2. Attackers use AI to craft more sophisticated payloads
3. The cascading credential theft creates a "vicious cycle of compromises"

Proposed solutions include AI-powered pre-publish scanning by frontier labs and OS-level sandboxing for package managers (restricting `npm install` to designated directories, blocking unexpected network calls from CI/CD pipelines).

### AI Compute Economics

Martin consistently applies rigorous arithmetic to debunk AI hype and uncover genuine constraints:

- **"No, it doesn't cost Anthropic $5k per Claude Code user"** — demonstrated the viral claim doesn't survive basic math, analyzing token costs, caching, and amortization
- **"The Coming AI Compute Crunch"** — argued DRAM shortages (not capital expenditure) will define AI infrastructure growth through 2027
- **"Are we really repeating the telecoms crash with AI datacenters?"** — compared token demand growth and capacity utilization to the 2000s telecom bubble, finding the economics don't match
- **"Are OpenAI and Anthropic Really Losing Money on Inference?"** — deconstructed real costs, suggesting economics may be far more profitable than commonly claimed

### Agentic Coding Tool Analysis

- **"Which web frameworks are most token-efficient for AI agents?"** — benchmarked 19 frameworks; minimal frameworks cost up to 2.9x fewer tokens than full-featured ones
- **"Minification isn't obfuscation — Claude Code proves it"** — used ASTs and AI agents to reverse-engineer minified JavaScript
- **"How to generate good looking reports with Claude Code, Cowork or Codex"** — practical guide to brand extraction and report generation
- **"Using agents and Wine to move off Windows"** — documented using Claude Code to fix Linux desktop issues and get garbage-rated Windows apps working in Wine

### AI-Discovered Zero-Days

Martin wrote about Anthropic's red team finding **500+ critical vulnerabilities** in abandoned software and asked: *"Who fixes the zero-days AI finds?"* This is a genuinely hard coordination problem — AI makes vulnerability discovery cheap and fast, but remediation still requires human effort on projects that may have no active maintainers.

## Blog Themes

- **AI economics** — Cost analysis, compute constraints, market dynamics
- **SaaS disruption** — How agentic AI is reshaping enterprise software
- **Developer productivity** — Agentic coding tools, MCPs, token efficiency
- **Supply chain security** — Open source vulnerability cascades, LLM-accelerated attacks
- **Enterprise adoption** — The bifurcation between power users and casual users

## Key Quotes

> *"Instead of SaaS being replaced by 'agentically-built' SaaS, what if people just don't need (as much) SaaS?"*

> *"I don't think there's ever been a time in history where a tiny team can outcompete a company one thousand times its size so easily."*

> *"The bifurcation is real and seems to be, if anything, speeding up dramatically."*

> *"While the world's been watching physical supply chains, a different kind of supply chain attack has been escalating in the open source ecosystem."*

## Related

- [[ai-economics]] — Martin's analysis of AI cost structures and compute constraints
- [[saas-disruption]] — The "$285 billion markdown files" thesis
- [[agent-bifurcation]] — Two kinds of AI users
- [[supply-chain-security]] — Open source vulnerability cascades
- [[anthropic]] — Claude Code, Cowork, and the knowledge-work-plugin

## Sources

- [Wall Street just lost $285 billion because of 13 markdown files](https://martinalderson.com/posts/wall-street-lost-285-billion-because-of-13-markdown-files/) (Feb 2026)
- [Two kinds of AI users are emerging. The gap between them is astonishing.](https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/) (Feb 2026)
- [Telnyx, LiteLLM and Axios: the supply chain crisis](https://martinalderson.com/posts/telnyx-litellm-axios-supply-chain-crisis/) (Mar 2026)
- [The Coming AI Compute Crunch](https://martinalderson.com/posts/the-coming-ai-compute-crunch/) (Jan 2026)
- [No, it doesn't cost Anthropic $5k per Claude Code user](https://martinalderson.com/posts/anthropic-5k-per-user/) (Mar 2026)
- [Which web frameworks are most token-efficient for AI agents?](https://martinalderson.com/posts/web-frameworks-token-efficiency/) (Feb 2026)
- [martinalderson.com/archive/](https://martinalderson.com/archive/)
