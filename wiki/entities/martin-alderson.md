---
title: Martin Alderson
type: entity
created: 2026-04-09
updated: 2026-04-10
tags:
  - person
  - blogger
  - hn-popular
  - ai
  - product
  - developer-tooling
  - economics
  - company
sources: []
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

- [[concepts/ai-economics]] — Martin's analysis of AI cost structures and compute constraints
-  — The "$285 billion markdown files" thesis
-  — Two kinds of AI users
-  — Open source vulnerability cascades- [[anthropic]] — Claude Code, Cowork, and the knowledge-work-plugin

## Sources

- [Wall Street just lost $285 billion because of 13 markdown files](https://martinalderson.com/posts/wall-street-lost-285-billion-because-of-13-markdown-files/) (Feb 2026)
- [Two kinds of AI users are emerging. The gap between them is astonishing.](https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/) (Feb 2026)
- [Telnyx, LiteLLM and Axios: the supply chain crisis](https://martinalderson.com/posts/telnyx-litellm-axios-supply-chain-crisis/) (Mar 2026)
- [The Coming AI Compute Crunch](https://martinalderson.com/posts/the-coming-ai-compute-crunch/) (Jan 2026)
- [No, it doesn't cost Anthropic $5k per Claude Code user](https://martinalderson.com/posts/anthropic-5k-per-user/) (Mar 2026)
- [Which web frameworks are most token-efficient for AI agents?](https://martinalderson.com/posts/web-frameworks-token-efficiency/) (Feb 2026)
- [martinalderson.com/archive/](https://martinalderson.com/archive/)

## References

- martinalderson.com--posts-ai-agents-are-starting-to-eat-saas--37d8652e
- martinalderson.com--posts-anthropic-found-500-zero-days--e16d62a3
- martinalderson.com--posts-are-we-dismissing-ai-spend-before-the-6x-lands--0aadfca9
- martinalderson.com--posts-are-we-in-a-gpt4-style-leap-that-evals-cant-see--7696618b
- martinalderson.com--posts-are-we-really-repeating-the-telecoms-crash-with-ai-dat--e40dbebb
- martinalderson.com--posts-attack-of-the-clones--1a69c778
- martinalderson.com--posts-building-a-tax-agent-with-claude-code--72e6cc36
- martinalderson.com--posts-claude-code-static-analysis--2a4b4efb
- martinalderson.com--posts-excel-agents-could-unlock-1t-in-economic-value--2fb910d0
- martinalderson.com--posts-figmas-woes-compound-with-claude-design--f8915a52
- martinalderson.com--posts-google-ai-studio-api-unreliable-for-two-weeks--8a7a82ba
- martinalderson.com--posts-has-mythos-just-broken-the-deal-that-kept-the-internet--290ac35f
- martinalderson.com--posts-has-the-cost-of-software-just-dropped-90-percent--d6e9e325
- martinalderson.com--posts-how-i-make-cicd-much-faster-and-cheaper--006d75ad
- martinalderson.com--posts-how-i-use-claude-code-to-manage-sysadmin-tasks--82cdaf85
- martinalderson.com--posts-how-to-make-great-looking-consistent-reports-with-clau--3d6f1578
- martinalderson.com--posts-how-to-use-qwen-3-5-to-ocr-documents--f3719003
- martinalderson.com--posts-i-finally-found-a-use-for-ipv6--d17a28d3
- martinalderson.com--posts-is-the-ai-compute-crunch-here--3df57c24
- martinalderson.com--posts-mcp-support-across-ai-apis--c5e1cf4b
- martinalderson.com--posts-minification-isnt-obfuscation-claude-code-proves-it--89931401
- martinalderson.com--posts-moe-expert-routing-visualization--a70dde30
- martinalderson.com--posts-no-it-doesnt-cost-anthropic-5k-per-claude-code-user--77319d6f
- martinalderson.com--posts-non-technical-cfo-shipping-better-code-than-agencies--35095076
- martinalderson.com--posts-notes-from-mcp-europe--22c3c8bd
- martinalderson.com--posts-ported-photoshop-1-to-csharp-in-30-minutes--e5438a32
- martinalderson.com--posts-self-improving-claude-md-files--ac9dfa7e
- martinalderson.com--posts-telnyx-litellm-axios-supply-chain-crisis--1cf34d19
- martinalderson.com--posts-the-coming-ai-compute-crunch--de305311
- martinalderson.com--posts-tracking-mcp-server-growth--d7da3712
- martinalderson.com--posts-travel-agents-developers--03e9ba7f
- martinalderson.com--posts-turns-out-i-was-wrong-about-tdd--df116d72
- martinalderson.com--posts-two-kinds-of-ai-users-are-emerging--409d6535
- martinalderson.com--posts-using-agents-and-wine-to-move-off-windows--85a78b28
- martinalderson.com--posts-using-opencode-in-cicd-for-ai-pull-request-reviews--1b4f7bf3
- martinalderson.com--posts-wall-street-lost-285-billion-because-of-13-markdown-fi--69ec5d77
- martinalderson.com--posts-welcome--6aca66b2
- martinalderson.com--posts-what-happens-when-coding-agents-stop-feeling-like-dial--d2aad4ef
- martinalderson.com--posts-what-next-for-the-compute-crunch--d8f87332
- martinalderson.com--posts-which-programming-languages-are-most-token-efficient--9c9c84db
- martinalderson.com--posts-which-web-frameworks-are-most-token-efficient-for-ai-a--a83d9cfe
- martinalderson.com--posts-why-claudes-new-1m-context-length-is-a-big-deal--294e4983
- martinalderson.com--posts-why-im-building-my-own-clis-for-agents--08080178
- martinalderson.com--posts-why-on-device-agentic-ai-cant-keep-up--5a080ee7
- martinalderson.com--posts-why-sandboxing-coding-agents-is-harder-than-you-think--4d65588c
