---
title: Mitchell Hashimoto
type: entity
created: 2026-04-09
updated: 2026-04-10
tags:
- person
- blogger
- hn-popular
- developer-tools
- ai-agents
- harness-engineering
aliases:
- mitchellh
- mitchellh.com
sources: []
---

# Mitchell Hashimoto

| | |
|---|---|
| **Blog** | [mitchellh.com](https://mitchellh.com) |
| **RSS** | https://mitchellh.com/feed.xml |
| **X/Twitter** | [@mitchellh](https://x.com/mitchellh) |
| **Role** | Founder & CEO of Ghostty (non-profit), co-founder of HashiCorp |
| **Known for** | Vagrant, Packer, Consul, Terraform, Vault, Nomad, Waypoint, Ghostty terminal emulator |
| **Bio** | Developer living in Los Angeles. Previously co-founded HashiCorp (CEO ~4 yrs, CTO ~5 yrs). Left in 2023. Now focuses on Ghostty. FAA licensed private pilot (PPL ASEL IR), flies a Cirrus SF50 Vision Jet. |

## Core Ideas

Mitchell is a **software craftsman** who approaches AI with a pragmatic, iterative methodology. Unlike hype-driven adopters, he forces himself through an initial "friction phase" to build first-principles understanding of AI capabilities. His most influential writing is about **developer tooling**, **infrastructure**, and **AI adoption workflows**.

### The Building Block Economy

Mitchell predicts a shift from monolithic applications to a "building block economy" — small, composable AI-powered components that developers can assemble. He sees AI not as a replacement for developers, but as a force multiplier that changes *how* software is built. Key insight: the value shifts from writing code to orchestrating intelligent components and defining the right constraints.

### AI Adoption Journey (6-Step Framework)

Mitchell documented his personal AI adoption process in a widely-shared essay. The framework:

1. **Drop the Chatbot** — Web chatbots are inefficient for coding. Switch to **agents** (LLMs that can read files, execute programs, and self-correct in a loop).
2. **Reproduce Your Own Work** — Manually complete a task, then force an agent to produce identical results without seeing the solution. This reveals AI's edges and builds prompt intuition.
3. **End-of-Day Agents** — Block the last 30 minutes of the workday to queue tasks for agents to run overnight. Use for deep research, parallel ideation, and issue/PR triage.
4. **Outsource the Slam Dunks** — Delegate high-confidence, low-judgment tasks. **Critical rule: turn off desktop notifications** to prevent context switching. Human controls interruption timing.
5. **Engineer the Harness** — Systematically prevent recurring agent mistakes via `AGENTS.md` files and custom verification scripts. Each line in a harness config represents a learned failure mode.
6. **Always Have an Agent Running** — Maintain a background agent (preferring slower, thoughtful models) for continuous work. Effective ~10-20% of the workday currently.

### Harness Engineering

Mitchell coined the concept of **"Harness Engineering"** — treating AI agent configuration as a living document of failure modes. His Ghostty project's `AGENTS.md` file has become a reference implementation. Each rule in the file was added after an agent made a specific mistake. The philosophy: *don't blame the AI, fix the harness.*

### Skill Formation Concerns

Mitchell has expressed concern about AI's impact on junior developers:
> *"The skill formation issues particularly in juniors without a strong grasp of fundamentals deeply worries me."*

He believes that outsourcing too much too early prevents developers from building the intuition needed to evaluate AI output quality.

### Ghostty as Non-Profit

Mitchell made Ghostty a non-profit organization, believing that terminal emulators (and developer tools more broadly) should not be driven by profit incentives. This reflects his broader philosophy that **infrastructure software should serve users, not shareholders**.

## Key Quotes

> *"Adopting a tool feels like work, and I do not want to put in the effort, but I usually do in an effort to be a well-rounded person of my craft."*

> *"Don't try to 'draw the owl' in one mega session."* — on breaking AI tasks into clear, actionable chunks

> *"I felt more efficient, but even if I wasn't, the thing I liked the most was that I could now focus my coding and thinking on tasks I really loved while still adequately completing the tasks I didn't."*

## Related

- [[concepts/harness-engineering]] — Mitchell's methodology for preventing recurring agent mistakes
-  — Terminal emulator project, now non-profit
- [[concepts/agentic-engineering]] — Agent-first development workflows
-  — Infrastructure-as-code company Mitchell co-founded

## Sources

- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) (Feb 2026)
- [The Building Block Economy](https://mitchellh.com/writing/the-building-block-economy)
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
