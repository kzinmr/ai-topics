---
title: Peter Steinberger
type: entity
entity_type: person
status: L3
created: 2026-04-13
updated: 2026-04-13
sources: [https://steipete.me/, https://www.thewantrepreneurshow.com/blog/peter-steinberger-built-a-100m-dev-tool-burned-out-then-came-back-to-code-with-ai-agents-and-never-looked-back/, https://github.com/steipete]
tags:
  - person
  - ai-agents
  - agentic-engineering
  - openclaw
  - developer-tools
  - ios
  - mcp
  - vibe-coding
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

## What Model is Peter Using?

Steinberger maintains a live blurb at **whatmodelispeterusing.com** — tracking which models he's currently using for different tasks. This reflects his **evaluation-first** approach: he doesn't commit to a single model, but chooses based on the task.

## Related

- [[concepts/openclaw-ecosystem]] — The framework he created
- [[concepts/anthropic-openclaw-conflict]] — The April 2026 policy dispute
- [[concepts/agentic-engineering]] — AI-assisted software development patterns
-  — The protocol his tooling ecosystem is built on
- [[concepts/skill-architecture-patterns]] — Skill governance model (OpenClaw's primitives-first approach)
- [[boris-cherny]] — Anthropic's Head of Claude Code
- [[simon-willison]] — Fellow opinion leader on agentic engineering
- [[xeiaso-net]] — Infrastructure engineer; creator of Anubis anti-scraper
- [[anildash]] — Tech commentator; agentic engineering and coding culture
- [[concepts/harness-engineering/agentic-workflows/vibe-coding]] — The coding approach Steinberger evolved into "AI-native development"
