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

- [[harness-engineering]] — Mitchell's methodology for preventing recurring agent mistakes
-  — Terminal emulator project, now non-profit
- [[agentic-engineering]] — Agent-first development workflows
-  — Infrastructure-as-code company Mitchell co-founded

## Sources

- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) (Feb 2026)
- [The Building Block Economy](https://mitchellh.com/writing/the-building-block-economy)
- [Ghostty is Now Non-Profit](https://mitchellh.com/writing/ghostty-is-now-non-profit)
- [mitchellh.com/about](https://mitchellh.com/about)
