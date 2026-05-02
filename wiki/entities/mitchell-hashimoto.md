---
title: Mitchell Hashimoto
type: entity
handle: "@mitchellh"
created: 2026-04-13
updated: 2026-04-27
depth: 22000
status: L3
tags:
  - agentic-engineering
  - ai
  - ai-agents
  - blogger
  - building-block-economy
  - developer-tooling
  - ghostty
  - harness-engineering
  - hashicorp
  - hn-popular
  - libghostty
  - person
  - terminal-emulator
  - terraform
  - vibe-coding
  - x-account
  - zig
aliases:
  - mitchellh
  - mitchellh.com
sources: []
---

# Mitchell Hashimoto

| | |
|---|---|
| **X/Twitter** | [@mitchellh](https://x.com/mitchellh) |
| **Blog** | [mitchellh.com](https://mitchellh.com/writing/) |
| **RSS** | https://mitchellh.com/feed.xml |
| **GitHub** | [mitchellh](https://github.com/mitchellh) |
| **Role** | Co-founder of HashiCorp; creator of Ghostty terminal emulator |
| **Known for** | Terraform, Vagrant, Packer, Vault; "Harness Engineering" terminology; Ghostty terminal |
| **Bio** | Infrastructure engineer and entrepreneur who built the tools powering modern cloud infrastructure. Co-founded HashiCorp (Terraform, Vault, Consul, Nomad, Packer), which went public in 2021. Now focused full-time on Ghostty, a next-generation terminal emulator written in Zig. Pioneered the term "Harness Engineering" for systematic prevention of AI agent mistakes. FAA licensed private pilot (PPL ASEL IR), flies a Cirrus SF50 Vision Jet. |

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

### Skill Formation Concerns

Mitchell has expressed concern about AI's impact on junior developers:

> "The skill formation issues particularly in juniors without a strong grasp of fundamentals deeply worries me."

He believes that outsourcing too much too early prevents developers from building the intuition needed to evaluate AI output quality.

## Key Work

- **[[mitchell-hashimoto-hashicorp]]** — Co-founded HashiCorp (2012–2021); built Terraform, Vagrant, Packer, Vault, Consul, Nomad. IPO in 2021.
- **[[mitchell-hashimoto-ghostty]]** — Created Ghostty terminal emulator (2023–present); GPU-accelerated, Zig-based, with libghostty embeddable library; non-profit sponsorship via Hack Club.
  - **Ghostty as Non-Profit** — Mitchell made Ghostty a non-profit organization, believing that terminal emulators (and developer tools more broadly) should not be driven by profit incentives. This reflects his broader philosophy that infrastructure software should serve users, not shareholders.
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

> "Adopting a tool feels like work, and I do not want to put in the effort, but I usually do in an effort to be a well-rounded person of my craft."

> "Don't try to 'draw the owl' in one mega session." — on breaking AI tasks into clear, actionable chunks

> "I felt more efficient, but even if I wasn't, the thing I liked the most was that I could now focus my coding and thinking on tasks I really loved while still adequately completing the tasks I didn't."

## Related People

- **[[ryan-lopopolo]]** — Both independently arrived at "Harness Engineering"
- **[[boris-cherny]]** — Both work on AI-assisted developer workflows
- **[[concepts/karpathy]]** — Shared interest in making AI accessible to individual developers
- **[[simon-willison]]** — Covers agentic engineering patterns
- **Richard Feldman** — Zed engineer who hosted Mitchell's agentic engineering session
- **Gergely Orosz** — Pragmatic Engineer podcast host
- **[[armon-dadgar]]** — HashiCorp co-founder
- **[[akira-realmcore]]** — Random Labs/Slate; swarm orchestration pioneer
- **[[steve-blank]]** — Lean Startup creator; AI startup methodology
- **[[daniel-de-laney]]** — Designer/PM; structured development and AI tools
- **[[drmaciver]]** — Hypothesis creator; property-based testing and AI reliability

## Sources

- [mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey)
- [Zed Blog: Agentic Engineering in Action](https://zed.dev/blog/agentic-engineering-with-mitchell-hashimoto)
- [The Pragmatic Engineer Podcast](https://podscan.fm/podcasts/the-pragmatic-engineer/episodes/mitchell-hashimotos-new-way-of-writing-code)
- [Ghostty GTK Rewrite](https://mitchellh.com/writing/ghostty-gtk-rewrite)
- [Ghostty Zig Patterns Talk](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Building Block Economy](https://mitchellh.com/writing/building-block-economy)
- [Vibing a Non-Trivial Feature](https://mitchellh.com/writing/vibing-a-non-trivial-feature)
- [GitHub: mitchellh](https://github.com/mitchellh)
- [Ghostty is Now Non-Profit](https://mitchellh.com/writing/ghostty-is-now-non-profit)
- [mitchellh.com/about](https://mitchellh.com/about)

## References

- mitchellh.com--writing-abandoning-rubygems--19dfb3a0
- mitchellh.com--writing-advice-for-tech-nonprofits--b542e9d1
- mitchellh.com--writing-ai-through-a-cloud-lens--3f1b526f
- mitchellh.com--writing-apple-the-key-to-my-success--03eacf7c
- mitchellh.com--writing-as-code--96c16db1
- mitchellh.com--writing-automation-obsessed--4b50858e
- mitchellh.com--writing-building-block-economy--42ecbe77
- mitchellh.com--writing-building-large-technical-projects--f20898d1
- mitchellh.com--writing-comparing-filesystem-performance-in-virtual-machines--5f8718ad
- mitchellh.com--writing-contributing-to-complex-projects--2ccea0b6
- mitchellh.com--writing-feel-it--41d63145
- mitchellh.com--writing-ghostty-1-0-reflection--8911499a
- mitchellh.com--writing-ghostty-and-useful-zig-patterns--2c6cc976
- mitchellh.com--writing-ghostty-devlog-001--805e600e
- mitchellh.com--writing-ghostty-devlog-002--c03371c1
- mitchellh.com--writing-ghostty-devlog-003--3a33d9ab
- mitchellh.com--writing-ghostty-devlog-004--11955a17
- mitchellh.com--writing-ghostty-devlog-005--bcaf2306
- mitchellh.com--writing-ghostty-devlog-006--b32ca05d
- mitchellh.com--writing-ghostty-gtk-rewrite--ed802785
- mitchellh.com--writing-ghostty-is-coming--d5b6626b
- mitchellh.com--writing-ghostty-leaving-github--89eae6ee
- mitchellh.com--writing-ghostty-memory-leak-fix--77e9020e
- mitchellh.com--writing-ghostty-non-profit--0165e454
- mitchellh.com--writing-ghostty-subsystem-maintainers--1fdea173
- mitchellh.com--writing-github-changesets--22a84be6
- mitchellh.com--writing-grapheme-clusters-in-terminals--f0bdf237
- mitchellh.com--writing-libghostty-is-coming--41b28239
- mitchellh.com--writing-my-ai-adoption-journey--cece43d7
- mitchellh.com--writing-my-startup-banking-story--d25e12ac
- mitchellh.com--writing-nix-with-dockerfiles--43acb322
- mitchellh.com--writing-non-trivial-vibing--14c72bcf
- mitchellh.com--writing-packer--8b47a3b5
- mitchellh.com--writing-polar--92dee336
- mitchellh.com--writing-prompt-engineering-transactional-prompting--dfc3c1a0
- mitchellh.com--writing-prompt-engineering-vs-blind-prompting--30b88011
- mitchellh.com--writing-simdutf-no-libcxx--dc1de051
- mitchellh.com--writing-the-new-normal--556edb1a
- mitchellh.com--writing-the-tao-of-vagrant--ae329a5b
- mitchellh.com--writing-tripwire--6021fe64
- mitchellh.com--writing-zig-and-swiftui--809b71e5
- mitchellh.com--writing-zig-builds-getting-faster--68f59a10
- mitchellh.com--writing-zig-comptime-conditional-disable--069575c8
- mitchellh.com--writing-zig-comptime-tagged-union-subset--2930fd29
- mitchellh.com--writing-zig-donation--1dc5f3e4
- mitchellh.com--zig-astgen--13b49ec8
- mitchellh.com--zig-build-internals--1c5eee2b
- mitchellh.com--zig-parser--fd85cbd7
- mitchellh.com--zig-sema--1dd9defd
- mitchellh.com--zig-tokenizer--17b5a33d
