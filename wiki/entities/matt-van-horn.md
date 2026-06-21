---
title: Matt Van Horn
created: 2026-05-09
updated: 2026-06-21
type: entity
tags:
  - person
  - community
  - ai-adoption
  - ai-agents
  - company
  - claude-code
aliases:
  - mvanhorn
  - '@mvanhorn'
  - Matt Van Horn
sources:
  - raw/articles/2026-04-19_mvanhorn_hermes-agent-use-cases-30days.md
  - raw/articles/2026-03-22_mvanhorn_claude-code-hacks.md
  - raw/articles/2026-06-02_mvanhorn_every-agentic-engineering-hack.md
  - raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering.md
  - https://x.com/mvanhorn/status/2045935785661349956
  - https://en.wikipedia.org/wiki/Matt_Van_Horn
  - https://www.linkedin.com/in/mattvanhorn/
  - https://en.wikipedia.org/wiki/June_(company)
related:
  - "[[entities/hermes-agent]]"
  - "[[concepts/hermes-agent-use-cases]]"
  - "[[concepts/reflexive-ai]]"
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/compound-engineering-every]]"
  - "[[entities/every-inc]]"
  - "[[entities/tobi-lutke]]"
  - "[[concepts/claude-code/claude-code-goal]]"
  - "[[concepts/loop-engineering]]"
---

# Matt Van Horn

**Matt Van Horn** (@mvanhorn) is an American entrepreneur who co-founded Zimride (which became Lyft) and June (maker of the June Intelligent Oven, acquired by Weber in 2021). He is currently building again and runs the @slashlast30days AI research tool. He is also known in the AI agent community for his systematic analysis of Hermes Agent use cases across multiple platforms.

## Overview

Matt Van Horn's career spans multiple startup waves — from the sharing economy (Lyft) through AI-powered hardware (June Intelligent Oven) to the current AI agent era. He has held leadership roles at Digg, Path, and Apple, and was Vice President of Business at Path. His June Oven company pioneered AI-driven smart kitchen appliances, using computer vision to identify and cook food. June was acquired by Weber Inc. in January 2021 for a nine-figure sum; today, JuneOS powers every smart product Weber sells.

Based in Seattle, WA, Van Horn now focuses on AI research and tooling. His recent work includes the @slashlast30days research tool and in-depth community analysis of Hermes Agent usage patterns.

## Career Timeline

| Year | Company | Role | Description |
|------|---------|------|-------------|
| 2007 | Zimride (→ Lyft) | Co-Founder | Co-founded ride-sharing service that became Lyft. Advised through August 2025. |
| ~2012 | Path | VP Business | Head of business development at the private social network. |
| ~2011 | Digg | Partnerships | Ran partnerships at the social news aggregator. |
| 2013–2021 | June | Co-Founder, CEO/President | Built AI-powered intelligent oven with computer vision. Acquired by Weber for 9 figures. |
| 2021–2024 | Weber-Stephen Products | President (June) + Indoor Products Lead | Led indoor products; JuneOS now powers all Weber smart products. |
| 2025– | Independent | Builder/Researcher | Building again. Runs @slashlast30days research tool. |

## Key Contributions

### Claude Code Workflow Philosophy (March -> June 2026)
Authored two widely-shared X Articles documenting his voice-driven, plan-first Claude Code workflow:

**"Every Claude Code Hack I Know" (March 2026)** -- 913K views:
- **Plan-first discipline**: `/ce:plan` for every idea, bug, or error immediately
- **Voice-driven development**: Using [[entities/monologue|Monologue]] voice app to talk to Claude Code
- **No-IDE philosophy**: "Just plan.md files and voice"
- **Parallel sessions**: 4-6 Claude Code sessions running concurrently
- **Granola MCP integration**: Meeting context flows directly into plan.md

**"Every Agentic Engineering Hack I Know" (June 2026)** -- Major update covering the full agentic engineering stack:
- **Compound Engineering workflow**: `/ce-plan` -> `/ce-work` loop as the universal development pattern. `/ce-brainstorm` for fuzzy ideas. "Plan for the plan" for non-code deep work (strategy docs, competitive analysis, board updates). Internally, `/ce-plan` fans out parallel research agents that read codebase conventions, search past solutions, and research external docs simultaneously.
- **"Don't Read the plan.md"**: Plans are for agents, not humans. Skim the title, ask inline questions ("TLDR?", "eli5 this plan", "wait, why this approach?"), and trust the plan as a leash that prevents agent laziness.
- **Voice-Pilled**: Voice-to-LLM via Monologue or Wispr Flow on Mac, Apple dictation on phone. The transcription doesn't need to be perfect because the LLM fills gaps contextually.
- **Human Signal**: With 4-6 parallel agent sessions, the human's role shifts from doing to directing -- providing taste, judgment, and the "react-and-redirect" loop. "Be the taste. Let them be the hands."
- **Dual-engine setup**: Claude Code (reasoning xhigh, fast mode off, $200 Max plan) for planning; Codex (reasoning xhigh, fast mode on, $200 plan) for building. Work is handed to Codex via IDE extension or `/ce-work --codex` -- never opening the Codex CLI directly.
- **Knowledge base integration**: Bear CLI (decade of notes), gbrain (synced brain), supermemory (memory layer). The principle: pick a notes tool with CLI/API and point the agent at it for compounding context.
- **Remote work infrastructure**: Mosh for SSH responsiveness, Tmux for airplane sessions, Mac Mini for always-on compute. Agent Cookie syncs cookies/.envs between machines.
- **AI Psychosis warning**: Acknowledged the addiction risk -- "Building with agents is the greatest video game ever made." Advised taking breaks, talking to loved ones, and building things people want.

**OSS Contributions via this workflow (updated June 2026):**
- **last30days** -- 27K+ stars. Multi-platform research tool (Reddit, X, YouTube, TikTok, HN, Polymarket, GitHub, web in parallel)
- **Printing Press** -- 3.7K+ stars, 320+ merged PRs. Fleet of CLI wrappers for real-world services (Tesla, Instacart, ESPN, Alaska Airlines, Granola)
- **Agent Cookie** -- Just launched. Browser session delivery for CLIs so agents act as authenticated users
- **AgentMail** -- Open-sourced. Gives Claude Code an email address: daemon watches AgentMail inbox, spawns fresh Claude sessions per allowlisted email
- **Compound Engineering** -- #3 contributor behind core team
- **Top contributor rankings**: #3 Compound Engineering, Superpowers, Emdash; #4 GStack, Paperclip; #6 Vercel Agent Browser; #2 Camoufox. Also hundreds of PRs in Python, Go, OpenCV.

Related: [[raw/articles/2026-03-22_mvanhorn_claude-code-hacks.md]] (metadata-only, auth-walled X Article), [[raw/articles/2026-06-02_mvanhorn_every-agentic-engineering-hack.md]]

### Hermes Agent Community Analysis (April 2026)
Authored a comprehensive 30-day analysis of Hermes Agent use cases across 7 platforms:
- 90 Reddit threads, 80 X posts, 55 YouTube videos, 3.5M+ views analyzed
- Identified 7 canonical Hermes Agent workflows with supporting community data
- Documented the "Three Shared Properties" pattern (Scheduled / File-based / Push to messenger)
- Named as the definitive community landscape study for the Hermes Agent ecosystem

### AI Adoption & Reflexive AI
- Documented Shopifys Reflexive AI Baseline policy ([[concepts/reflexive-ai]])
- Published research on entrepreneurship trends grounded in Shopify's internal data science
- Case study referenced as a model for organizational AI adoption

## Key Theses
- **Human Signal / Agentic Engineering flow**: The human role shifts from coder to taste director — providing judgment, direction, and the react-and-redirect loop while agents do the mechanical work. The plan.md becomes the durable artifact that survives context loss.
- **Voice is the primary input**: Voice-to-LLM works because LLMs fill transcription gaps contextually. Monologue + Apple dictation + gooseneck mic forms the interface layer.
- **Plan-first discipline is universal**: /ce-plan → /ce-work applies equally to code and non-code deep work (strategy docs, meeting transcripts, competitive analysis). The "plan for the plan" trick forces LLMs to do thorough work.
- **Community-driven agent research**: Systematic analysis of real-world agent usage reveals patterns that product docs miss

## Writing & Research
Van Horn publishes analysis at the intersection of AI adoption, entrepreneurship, and agent ecosystems. His X presence (@mvanhorn, 25.2K followers) covers Hermes Agent use cases, AI-first company policies, and startup-building insights.

## See Also
- [[concepts/agentic-engineering]] — The disciplined practice Van Horn exemplifies and writes about
- [[concepts/compound-engineering-every]] — The methodology he is #3 contributor to
- [[entities/every-inc]] — The company behind Compound Engineering, Monologue, Proof
- [[entities/hermes-agent]]
- [[concepts/hermes-agent-use-cases]]
- [[concepts/reflexive-ai]]
- [[concepts/solo-founder-stack]]
