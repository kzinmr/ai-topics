---
title: Newsjack (Agent PR Skills)
created: 2026-06-17
updated: 2026-06-17
type: concept
tags: [ai-agents, go, developer-tools, open-source, product]
aliases: ["newsjack", "newsjack.sh", "agent pr skills"]
sources:
  - "https://newsjack.sh"
  - "https://github.com/elvisun/newsjack"
  - "https://x.com/elvissun/status/2067037758296580296"
related:
  - "elvis-sun"
  - "hermes-agent"
  - "claude-code"
  - "harness-engineering"
---

# Newsjack — Agent PR Skills

**Creator:** [[elvis-sun|Elvis Sun]] (@elvissun)  
**Website:** https://newsjack.sh  
**GitHub:** https://github.com/elvisun/newsjack  
**License:** MIT  
**Language:** Go + Markdown skills  
**Stars:** 428 ★ (as of 2026-06-17)

> "The open-source skills that turn your agent into a full PR team." — newsjack.sh tagline

## Overview

Newsjack is an open-source framework that equips AI coding agents (Claude Code, Codex, Hermes, OpenClaw) with PR (Public Relations) capabilities. It consists of plain-Markdown skill instructions plus a small Go CLI. Instead of treating agents as mere code generators, Newsjack makes them capable of media monitoring, journalist outreach, pitch crafting, and PR strategy — essentially turning a solo developer's agent into a full PR department.

## Architecture: Three Lanes

Newsjack organizes its 20+ skills into three operational lanes:

### 🛰️ Detect — Surface What Matters
- **Industry monitoring** — find newsjacking opportunities: fresh stories you have standing to jump on before the wave breaks
- **Coverage tracking** — Google Alerts-style keyword tracking with LLM filtering
- **Competitor tracking** — launches, funding rounds, stumbles
- **Story freshness verification** — who broke it, who owns it, what oxygen's left

### 🚀 Act — Turn Signal Into Output
- **Angle generation** — turn one update into hooks framed for different beats
- **Journalist fit-check** — will *this* reporter actually care?
- **Source query response** — triage inbound HARO-style requests
- **Pitch roasting** — honest critique against the rubric editors actually use
- **Fact-checking** — extract claims, verify each, flag shaky ones
- **Voice extraction** — fingerprint real writing style, kill AI tells
- **Media list building** — targeted reporters, not scraped contact dumps

### 🧭 Strategize — Figure Out What Your Story Is
- **PR strategy walkthrough** — audience first, positioning second, news pegs third
- **Newsworthiness scoring** — cold read on whether it clears the bar

## Platform Compatibility

| Agent Platform | Detect | Act | Strategize |
|---|---|---|---|
| **Claude Code** | ✅ | ✅ | ✅ |
| **Codex (OpenAI)** | ✅ | ✅ | ✅ |
| **Hermes** | ✅ | ✅ | ✅ |
| **OpenClaw** | ✅ | ✅ | ✅ |
| **Claude.ai** | ✅ (⚡Limited) | ✅ (⚡Limited) | ✅ |
| **ChatGPT** | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited |
| **Medialyst** | ✅ (🔧 API) | ✅ (🔧 API) | ✅ |

Legend: ✅ = full local state, ⚡ = limited mode (no saved state between sessions), ⚠️ = best-effort one-shot, 🔧 = external API required

## Key Design Decisions

### Skills as Plain Markdown
Each skill is a standalone Markdown file that the agent reads as instructions. This means:
- **Platform-agnostic** — works with any agent that can read files
- **Auditable** — humans can review what the agent will do
- **Hackable** — users can modify skills without code

### CLI as Thin Orchestrator
The Go CLI handles:
- Scheduling (cron-style monitoring)
- State persistence (saved voice fingerprints, monitoring profiles)
- External API connections (Medialyst for journalist enrichment)

Heavy lifting is delegated to the agent via skills.

### Separation of Concerns
"Detect" skills collect signal. "Act" skills produce output. "Strategize" skills frame the problem. Each lane is independently useful but designed to compose.

## Relationship to Elvis Sun's Ecosystem

Newsjack is the latest in Elvis Sun's PR/agent toolchain:

| Tool | Purpose | Status |
|---|---|---|
| **Newsjack** | Agent PR skills (open-source) | Launched May 2026 |
| **Medialyst.ai** | Journalist discovery platform | Beta |
| **PressPulse.ai** | PR opportunity listening | $100k+ revenue |
| **Solar Flare PR** | Search-first PR agency | Active |
| **ismypitchshit.com** | AI pitch roaster | Viral tool |

## Relevance to Agent Ecosystem

Newsjack is a notable example of the **"agent as department"** pattern — using AI agents not just for coding but for specialized business functions (PR, marketing, sales). It demonstrates:

1. **Skill composability** — 20+ independently useful skills that compose into workflows
2. **Agent-as-harness** — the agent becomes the execution environment, not just the tool
3. **Solo founder leverage** — one person + agent = full PR team
4. **Open-source skills** — skills as distributable, versionable assets (like npm packages for agent capabilities)

## See Also

- [[elvis-sun]] — Creator of Newsjack
- [[concepts/newsjacking-framework]] — The viral content strategy behind the name
- [[concepts/harness-engineering]] — Agent-as-harness pattern
- [[entities/hermes-agent]] — Supported agent platform
- [[concepts/vibe-coding]] — Related philosophy of rapid iteration with AI
