---
title: Peter Steinberger
type: entity
entity_type: person
status: L3
created: 2026-04-13
updated: 2026-06-21
sources: [https://steipete.me/, https://www.thewantrepreneurshow.com/blog/peter-steinberger-built-a-100m-dev-tool-burned-out-then-came-back-to-code-with-ai-agents-and-never-looked-back/, https://github.com/steipete, raw/articles/2026-05-30_steipete_my-agent-stack-for-automating-my-personal-life.md, raw/articles/2026-06-07_steipete-design-loops-dont-prompt.md, raw/articles/2026-06-02_microsoft-build_brk245-build-the-thing.md, raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering.md]
tags:
  - person
  - ai-agents
  - agentic-engineering
  - openclaw
  - developer-tooling
  - mcp
  - coding-agents
  - personal-ai

---


# Peter Steinberger

Austrian software developer, creator of **OpenClaw** (originally "Clawdbot"), founder of PSPDFKit (exited to Apple ecosystem). Known as **@steipete** on GitHub/Twitter. A pioneer of **AI-native development workflows** — orchestrating 5-10 AI agents in parallel to ship at the velocity of a 30-person team.

## Bio

Peter Steinberger grew up in rural Austria and bootstrapped **PSPDFKit**, a mobile PDF framework used internally by Apple and deployed on **1B+ devices**. After 13 years, the CEO role led to burnout — "As a CEO, you're the trash bin. Everything others can't solve, you have to fix." He sold his shares in 2020, took a 3-year tech hiatus, and returned in early 2023 to discover AI-assisted development. This sparked his evolution from elite iOS engineer to **AI-native solo builder** who ships 600+ commits per day by orchestrating Claude Code, Codex, and custom MCP servers.

## Timeline

| Period | Role | Key Events |
|--------|------|------------|
| ~2007-2020 | Founder/CEO, PSPDFKit | Bootstrapped mobile PDF framework to millions in ARR; 1B+ device deployments |
| 2020 | Exit & Burnout | Sold shares after 13 years; took 3-year tech hiatus |
| 2023 | Return to Development | Discovered Claude Code; "holy f--- mind-blowing moment" |
| 2024-2025 | AI Agent Builder | Created OpenClaw (Clawdbot); 135,000+ instances at peak |
| 2025 | Trademark Conflict | Renamed Clawdbot → Moltbot → OpenClaw after Anthropic complaint |
| Feb 2026 | Joined OpenAI | Sam Altman welcomed him to "drive next generation of personal agents" |
| Apr 2026 | Anthropic-OpenClaw Conflict | Anthropic blocked third-party tools; Steinberger's account suspended then restored |
| 2026 | Prolific Open-Source | 15k+ GitHub stars across projects; 46k+ GitHub followers |

## Core Ideas

### "Design Loops, Don't Prompt Agents" (Jun 2026)
> "Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — @steipete, June 7, 2026

Steinberger's progression from manual prompting to loop authoring mirrors Boris Cherny's three-stage evolution: from manual + autocomplete → parallel sessions → loop author. The key insight: **the reusable unit inside the loop is a skill, not a prompt**. A loop with no reusable skills is `while(true)` around a stranger. A loop that calls a library of sharp, tested, named skills is a system that compounds. This connects directly to his "Skills > Loops" thesis and [[concepts/harness-engineering/agentic-loop|the broader loop evolution spectrum]].

Saravia's DAIR.AI Academy article (Jun 19, 2026) provides a comprehensive synthesis of this paradigm, covering the six building blocks of loop engineering, the five meanings of 'loop', and concrete patterns such as the PR babysitter.

### Token Privilege & The Loop Access Gap (Jun 2026)

In June 2026, a prominent tech commentator quoted Steinberger's loop thesis and added a structural observation: **perspectives on AI usage differ dramatically depending on whether you are token-rich or token-poor.** The idea of designing loops — running agents continuously on infrastructure time — comes from a place of incredible privilege: unlimited token budgets, AI startup access, and the freedom to let agents run indefinitely. For developers operating under tight token budgets or enterprise cost controls, loops are a luxury, not a default. This introduces a **loop access gap** that may stratify the developer community as agent infrastructure matures.

### "Ship Beats Perfect" — The AI-Native Developer Philosophy
> "I don't read code anymore. I weave it."

Steinberger's most provocative claim. He shifted from **line-by-line coding** to **system architecture and prompt engineering**. Where he once obsessed over spacing, naming, and architecture details, he now focuses on:
- **Outcome over syntax** — does the system work correctly?
- **Architecture and taste** — what should be built and how it should feel
- **Verification** — code is verifiable; compile, run, test

### The Closed Loop Principle
> "Code works well with AI because it's verifiable. You can compile it, run it, test it. That's the loop. You have to close the loop."

The key insight enabling high-quality AI-generated code: build CLI test runners and synthetic user flows so agents can **validate their own work**. This forces systems to be structured for testability rather than aesthetics.

### PRs = "Prompt Requests"
Reframed the pull request concept: instead of reviewing code line-by-line, review the **prompts and architecture decisions** that generated the code. The bottleneck shifts from typing speed to **structuring thought clearly**.

### Polyagentmorous Development
> "Powered by Vienna coffee culture" — steipete GitHub bio

Runs **5-10 AI agents in parallel** simultaneously (Claude Code, Codex, various MCP servers). Each agent is a specialist: file operations, web scraping, terminal automation, screenshot analysis. He orchestrates them like a conductor, not a coder.

### Agent Tooling Ecosystem
Current projects demonstrate a systematic approach to building **MCP-first developer tools**:

| Tool | Description | Stars |
|------|-------------|-------|
| **OpenClaw** | Personal AI agent framework with WhatsApp/Discord integration | 135k+ instances |
| **VibeTunnel** (vt.sh) | Turn any browser into terminal; command agents remotely | — |
| **CodexBar** | Usage stats for OpenAI Codex and Claude Code (no login needed) | 9.9k |
| **Peekaboo** | macOS CLI + MCP server for AI agent screenshot capture | 3.1k |
| **mcporter** | Call MCPs via TypeScript, package as CLI | 3.8k |
| **gogcli** | Google Suite CLI (Gmail, GCal, GDrive, GContacts) | 6.7k |
| **agent-rules** | Rules and knowledge for working with Claude Code/Cursor | 5.7k |
| **Aspects** | AOP for Objective-C and Swift (legacy) | 8.4k |
| **tokentally** | Tiny lib for LLM token + cost math | — |
| **Terminator MCP** | "I'll be back... with your terminal output!" | — |

## OpenClaw Architecture & Skill Governance

### Five-Tier Skill Precedence Model
OpenClaw implements a strict hierarchical skill loading system:
1. **Workspace skills** (highest priority)
2. **User global skills**
3. **Managed skills**
4. **Bundled skills** (baseline only)
5. **Extra skills** (lowest priority)

This ensures deterministic behavior: "When something breaks at 3am, you can trace it in one grep instead of guessing which skill the agent triggered."

### Anti-Bloat Policy
From OpenClaw VISION.md: "Bundled skills are baseline only. New skills go to ClawHub first. Core additions should be rare and require a strong product or security reason."

**Discovery bounds:** byte caps, candidate caps, symlink rejection, verified file opens only. Eligibility checks are separate from discovery — different agents can see different subsets of skills.

### Product Philosophy: Primitives Over Defaults
> "You're not getting defaults, you're getting guarantees. OpenClaw does exactly what you told it to do, nothing more, nothing less. Boring in the best way." — elvis analysis

Steinberger's approach prioritizes **legibility and scope control** over autonomous self-improvement. The governance model means the skill corpus doesn't rot over time because nothing gets added without user intention.

## The Anthropic-OpenClaw Conflict (April 2026)

Steinberger became the public face of the **open-source vs. platform risk** debate when Anthropic blocked third-party tools (including OpenClaw) from Claude subscriptions:

> "First they copy some popular features into their closed harness, then they lock out open source."

Key events:
- **April 4, 2026**: Anthropic blocked third-party tools
- **Negotiation**: Steinberger and Dave Morin secured a 1-week delay
- **April 12, 2026**: Steinberger's own Claude account suspended ("suspicious signals"), restored within hours
- **Public criticism**: Framed the issue as platform risk for open-source AI frameworks

This conflict validated his core thesis: **open-source tooling should not depend on a single platform's goodwill**.

## Contributions to Open Source

- **15k+ GitHub stars** across 173 public repositories
- **PSPDFKit**: Industry-standard mobile PDF SDK (exited 2021)
- **OpenClaw**: Open-source personal AI agent framework (135k+ running instances at peak)
- **MCP Server Ecosystem**: Multiple production-ready MCP servers for developer tooling
- **Aspects**: Delightful AOP library for Objective-C/Swift (8.4k stars)
- **InterposeKit**: Modern Swift method swizzling library

## Quotes and Philosophy

| Quote | Context |
|-------|---------|
| "I don't read code anymore. I weave it." | On AI-assisted development |
| "Ship beats perfect" | GitHub bio philosophy |
| "Code works well with AI because it's verifiable." | The closed loop principle |
| "Building stuff almost felt like playing a computer game." | On his origin story in rural Austria |
| "As a CEO, you're the trash bin." | Why he burned out and sold PSPDFKit |
| "First they copy some popular features into their closed harness, then they lock out open source." | On Anthropic's OpenClaw blocking |

## Personal Agent Stack (May 2026)

In a May 2026 X article, Steinberger documented his personal agent stack for automating daily life — the first comprehensive public account of a **personal agent operating across communication channels** (WhatsApp, Telegram, Gmail, iMessage, Google Drive, Calendar).

**Core thesis:** The agent-operated computer replaces the app-operated computer. You state intent → the agent gathers context → proposes action → waits for approval → executes → reports back.

### Agent: Codex + GPT-5.5
Previously used Claude Code; migrated to Codex because GPT-5.5 is better for personal automation work. The switch itself is not the story — the story is wiring the model into existing life data.

### Tool Hierarchy (from most to least preferred)
1. **APIs and CLIs** — `gogcli` for Google Workspace, `wacli` for WhatsApp, `imsg` for iMessage/SMS
2. **Local files** — Markdown/CSV files in Google Drive (agent-readable source of truth)
3. **Browser automation** — for web apps without APIs
4. **Screen automation** — last resort (AppleScript/macOS UI scripting)

### Data Layer Design
Moved knowledge from Notion to Google Drive because Notion's UI-native structure (nested pages, databases, properties, permissions) is "pleasant for humans and annoying for models." Google Drive holds Markdown files, CSVs, and provides a clean CLI surface via `gogcli`.

Key insight: **"You should not organize your knowledge only for the human UI. You should organize it for the agent's tool path."**

### Skills as Operational Taste
Skills are text-based operating manuals for recurring tasks (e.g., inbox-zero: list Gmail, auto-archive vs needs-review, draft replies, wait for approval, send, sign as "Nicolas"). Mistakes become instructions — the agent compounds improvement over time.

### Approval Gates
Multi-tier trust model: read-only scanning → drafting → sending → high-stakes actions. The agent does the tedious work but asks at the right moments. This is what makes personal agents **personal** — not by having a cute voice, but by accumulating operational taste.

### Killer Workflow: "What Did I Miss?"
The highest-value workflow is life inbox triage: scan WhatsApp, Telegram, Gmail, SMS, Calendar, and Drive changes every few hours → identify who needs a reply, what is urgent, what is stale → present a summary. This is context-heavy, repetitive, cross-tool, and full of small decisions — perfect for agents.

[[raw/articles/2026-05-30_steipete_my-agent-stack-for-automating-my-personal-life.md]]

## What Model is Peter Using?

Steinberger maintains a live blurb at **whatmodelispeterusing.com** — tracking which models he's currently using for different tasks. This reflects his **evaluation-first** approach: he doesn't commit to a single model, but chooses based on the task.

## Media Appearances

### Talks & Interviews

- **"Build the Thing That Builds the Thing"** (Jun 2026, Microsoft Build BRK245): 45-min breakout on the meta-development philosophy behind OpenClaw's automation ecosystem — ClawSweeper (auto-closing 15K issues), Octopus (API token balancing), Crab Box (isolated cloud test infra), Auto Review (iterative agent self-review), Core Patch (parallel audits), Crab Fleet (multiplayer agent dev). [[raw/articles/2026-06-02_microsoft-build_brk245-build-the-thing]]
- **"Builders Unscripted: Ep. 1 — Peter Steinberger, Creator of OpenClaw"** (Feb 2026): 31-min interview with Romain Huet (OpenAI). Covers OpenClaw's viral growth, building with Codex, "vibe coding" critique, and open source philosophy. Recorded prior to joining OpenAI. [[raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger]]

## Sources

- [[raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering]] — Elvis Saravia (DAIR.AI), "From Prompting Agents to Loop Engineering" (Jun 19, 2026). Synthesizes Steinberger's loop thesis across six building blocks, five loop taxonomies, and concrete patterns.

## Related

- [[concepts/openclaw-ecosystem]] — The framework he created
- [[concepts/anthropic/openclaw-conflict]] — The April 2026 policy dispute
- [[concepts/agentic-engineering]] — AI-assisted software development patterns
-  — The protocol his tooling ecosystem is built on
- [[concepts/skill-architecture-patterns]] — Skill governance model (OpenClaw's primitives-first approach)
- [[entities/boris-cherny]] — Anthropic's Head of Claude Code
- [[entities/simon-willison]] — Fellow opinion leader on agentic engineering
- [[entities/xeiaso-net]] — Infrastructure engineer; creator of Anubis anti-scraper
- [[entities/anildash]] — Tech commentator; agentic engineering and coding culture
- [[concepts/harness-engineering/agentic-workflows/vibe-coding]] — The coding approach Steinberger evolved into "AI-native development"
