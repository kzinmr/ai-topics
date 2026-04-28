---
title: Mitchell Hashimoto
type: entity
handle: "@mitchellh"
created: 2026-04-13
updated: 2026-04-27
depth: 22000
status: L3
tags:
  - person
  - x-account
  - ai
  - agentic-engineering
  - harness-engineering
  - ghostty
  - zig
  - hashicorp
  - terraform
  - terminal-emulator
  - building-block-economy
  - libghostty
  - vibe-coding
sources: []
---

# Mitchell Hashimoto

| | |
|---|---|
| **X/Twitter** | [@mitchellh](https://x.com/mitchellh) |
| **Blog** | [mitchellh.com](https://mitchellh.com/writing/) |
| **GitHub** | [mitchellh](https://github.com/mitchellh) |
| **Role** | Co-founder of HashiCorp; creator of Ghostty terminal emulator |
| **Known for** | Terraform, Vagrant, Packer, Vault; "Harness Engineering" terminology; Ghostty terminal |
| **Bio** | Infrastructure engineer and entrepreneur who built the tools powering modern cloud infrastructure. Co-founded HashiCorp (Terraform, Vault, Consul, Nomad, Packer), which went public in 2021. Now focused full-time on Ghostty, a next-generation terminal emulator written in Zig. Pioneered the term "Harness Engineering" for systematic prevention of AI agent mistakes. |

## Overview

Mitchell Hashimoto is one of the most influential infrastructure engineers of the modern era. As co-founder of HashiCorp (with [[armon-dadgar]]), he built **Terraform** (100M+ downloads), **Vagrant**, **Packer**, **Vault**, **Consul**, and **Nomad** — the foundational tooling stack for cloud-native infrastructure. See [[mitchell-hashimoto-hashicorp]] for details.

After HashiCorp's IPO in 2021, Mitchell stepped back to focus on building software, creating **Ghostty** — a terminal emulator written from scratch in Zig. See [[mitchell-hashimoto-ghostty]] for details.

In **February 2026**, Mitchell coined **"Harness Engineering"** in his post ["My AI Adoption Journey"](https://mitchellh.com/writing/my-ai-adoption-journey):

> "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.' It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that same mistake again."

OpenAI and Martin Fowler subsequently endorsed the term. [[ryan-lopopolo]] at OpenAI had independently arrived at the same concept.

## Core Ideas

### Harness Engineering — Systematizing Agent Improvement

Every agent mistake becomes a permanent system improvement. This differs from prompt engineering ("How do I ask better?") and context engineering ("What does the agent need to know?"). The harness includes custom linters, AGENTS.md rules, CI/CD guardrails, structured feedback loops, and architectural constraints.

> "I'm making an earnest effort whenever I see an agent do a Bad Thing to prevent it from ever happening again."

### Building Block Economy

In his April 2026 essay (written entirely by hand), Mitchell articulated a paradigm shift for the AI era:

> "The most effective way to build software and get massive adoption is no longer high quality mainline apps but via building blocks that enable and encourage others to build quantity over quality."

Key insight: AI agents excel at gluing together well-documented components. Agents prefer open/free software. Maintainers get outsourced R&D from community PoCs.

### Anti-Slop Pattern

1. **Plan first** — Save to spec.md
2. **Execute via agent** — Scaffold + TODO pattern
3. **Anti-slop session** — When stuck, manually restructure, force deep understanding
4. **Final manual review** — Never ship AI code without thorough manual review

### 6-Step AI Adoption Journey

1. Drop the chatbot — Chatbots lack tools and context
2. Reproduce your own work — Build intuition for agent capabilities
3. End-of-day agents — Let them work overnight
4. Outsource slam dunks — Boilerplate, refactoring, tests
5. **Engineer the harness** — Prevent repeated mistakes
6. Always have an agent running — Background delegation

### Other Concepts

- **Agent Competition** — Run different models/agents on the same task; cap at 2 competing agents
- **Architect, Not Coder** — "My value is higher when I'm thinking about the system as a whole rather than typing out individual functions"
- **Transcription as External Memory** — Uses Wispr Flow voice transcription to create searchable design decision logs
- **On Diminishing Returns** — "The delta between models is getting smaller... The biggest gains now come from workflow design rather than model capability"
- **Senior Quality Philosophy** — Agents struggle with team-readability, architectural judgment, and cross-cutting concerns

## Key Work

- **[[mitchell-hashimoto-hashicorp]]** — Co-founded HashiCorp (2012–2021); built Terraform, Vagrant, Packer, Vault, Consul, Nomad. IPO in 2021.
- **[[mitchell-hashimoto-ghostty]]** — Created Ghostty terminal emulator (2023–present); GPU-accelerated, Zig-based, with libghostty embeddable library; non-profit sponsorship via Hack Club.
- **[Zed Agentic Engineering Session](https://zed.dev/blog/agentic-engineering-with-mitchell-hashimoto)** (Jun 2025) — Walked Richard Feldman through actual AI-assisted workflow on a Ghostty commit. Demonstrated agents for refactoring while focusing human effort on architecture.
- **Vouch** ([github.com/mitchellh/vouch](https://github.com/mitchellh/vouch)) — Community trust management system based on explicit vouches. Written in Nushell, 4,000+ GitHub stars.

## Key Writings

- **[My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)** (Feb 2026) — Original "Harness Engineering" definition and 6-step adoption path
- **[The Building Block Economy](https://mitchellh.com/writing/building-block-economy)** (Apr 2026) — AI-era software composition paradigm
- **[Vibing a Non-Trivial Feature](https://mitchellh.com/writing/vibing-a-non-trivial-feature)** (Oct 2025) — Transparent account of shipping Ghostty feature with AI (16 sessions, $15.98, 3 days)
- **[We Rewrote the Ghostty GTK Application](https://mitchellh.com/writing/ghostty-gtk-rewrite)** (Aug 2025) — GObject/Zig interfacing, Valgrind verification
- **[Pragmatic Engineer Podcast](https://podscan.fm/podcasts/the-pragmatic-engineer/episodes/mitchell-hashimotos-new-way-of-writing-code)** (Feb 2026) — 2-hour deep-dive on HashiCorp, AI workflows, Ghostty

## Key Quotes

> "If an agent isn't running, I ask myself 'is there something an agent could be doing for me right now?'"

> "My approach is that I'm more or less the architect of the software project. I still like to come up with the code myself. But I've realized that my value is higher when I'm thinking about the system as a whole rather than typing out individual functions."

> "Most of the work I do right now with LLMs is just getting it to more of a senior quality point of view."

> "Git and GitHub may not survive the agentic era in their current form."

> "Open source is moving from 'default trust' to 'default deny.'"

> "I really don't care one way or the other if AI is here to stay, I'm a software craftsman that just wants to build stuff for the love of the game."

## Related People

- **[[ryan-lopopolo]]** — Both independently arrived at "Harness Engineering"
- **[[boris-cherny]]** — Both work on AI-assisted developer workflows
- **[[concepts/karpathy]]** — Shared interest in making AI accessible to individual developers
- **[[simon-willison]]** — Covers agentic engineering patterns
- **Richard Feldman** — Zed engineer who hosted Mitchell's agentic engineering session
- **Gergely Orosz** — Pragmatic Engineer podcast host
- **[[armon-dadgar]]** — HashiCorp co-founder

## Sources

- [mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey)
- [Zed Blog: Agentic Engineering in Action](https://zed.dev/blog/agentic-engineering-with-mitchell-hashimoto)
- [The Pragmatic Engineer Podcast](https://podscan.fm/podcasts/the-pragmatic-engineer/episodes/mitchell-hashimotos-new-way-of-writing-code)
- [Ghostty GTK Rewrite](https://mitchellh.com/writing/ghostty-gtk-rewrite)
- [Ghostty Zig Patterns Talk](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Building Block Economy](https://mitchellh.com/writing/building-block-economy)
- [Vibing a Non-Trivial Feature](https://mitchellh.com/writing/vibing-a-non-trivial-feature)
- [GitHub: mitchellh](https://github.com/mitchellh)
