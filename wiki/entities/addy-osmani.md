---
title: Addy Osmani
created: 2026-05-10
updated: 2026-05-18
type: entity
tags:
  - person
  - google
  - web-development
  - coding-agents
  - harness-engineering
aliases:
  - Addy Osmani
  - addyosmani
sources:
  - raw/articles/2026-05-09_addyosmani-agent-harness-engineering.md
  - raw/articles/2026-05-05_addyosmani_cognitive-surrender.md
  - raw/articles/2026-05-17_addy-osmani_dont-outsource-learning.md
  - https://addyosmani.com/bio/
description: "Director at Google Cloud AI, formerly Chrome Developer Experience lead. Published comprehensive Agent Harness Engineering framework (May 2026) and Cognitive Surrender concept (May 2026). Author of several books on software engineering and AI."
---

# Addy Osmani

**Addy Osmani** is an Irish software engineering leader and director at Google Cloud AI, focused on helping developers and businesses succeed with Gemini, Vertex AI, and the Agent Development Kit (ADK). He bridges Google DeepMind, engineering, product, and developer relations teams for Cloud AI.

## Career

### Google Chrome (2012–2025)
Osmani spent nearly 14 years leading developer experiences in Chrome, working on:
- **Chrome DevTools** — Developer tools for the web platform
- **Lighthouse** — Automated auditing for performance, accessibility, SEO
- **Core Web Vitals** — Google's performance metrics initiative
- **Speedometer 2** — Browser benchmark, collaborated with Apple's Safari team
- **Puppeteer / Chrome Headless** — Browser automation tooling
- **Aurora** — Framework optimization (React, Next.js, Angular, Nuxt)

### Google Cloud AI (2025–present)
Transitions to Google Cloud AI as a director, focusing on enterprise AI adoption:
- **Gemini** — Google's AI model family
- **Vertex AI** — Enterprise ML platform
- **Agent Development Kit (ADK)** — Agent building framework

## Open-Source Contributions

Osmani is known for leading Chrome's open-source philanthropy, sponsoring projects including Webpack, RollUp, Vite, Vue, Nuxt, Svelte, and Astro. His own open-source projects include:
- **TodoMVC** — Framework comparison project
- **Yeoman** — Scaffolding tooling
- **Critical** — Critical-path CSS extraction
- **Quicklink** — Prefetching library
- **Workbox** — Service worker library (contributor)
- **Material Design Lite** — 32K GitHub stars

## Publications

Osmani is a published author of several books:
- *Web Performance Engineering*
- *The Effective Software Engineer*
- *Effective Software Engineering Management*
- *Product Engineering with AI*
- *Success at Scale*
- *Developer Experience*

## Harness Engineering Contributions (May 2026)

On May 9, 2026, Osmani published a comprehensive synthesis codifying **Agent Harness Engineering** under the framing **Agent = Model + Harness**. Key contributions:

- **The Ratchet** — Every agent mistake becomes a permanent rule (AGENTS.md → hook → reviewer subagent)
- **Working Backwards from Behavior** — Design methodology: behavior → component
- **Harnesses Don't Shrink, They Move** — Model improvements shift harness requirements rather than eliminating them
- **Claude Code Architecture** — Mapped Fareed Khan's architecture diagram to harness engineering concepts
- **HaaS (Harness-as-a-Service)** — Industry shift from LLM APIs to Harness APIs providing runtime

His post synthesized contributions from @Vtrivedy10 (term coiner), @dexhorthy (emergent patterns), HumanLayer ("skill issue"), Anthropic Engineering (long-running apps), and Birgitta Böckeler (user-side experience).

## "Don't Outsource the Learning" (May 2026)

On May 17, 2026, Osmani published a follow-up piece expanding the cognitive surrender thesis with fresh research findings and practical countermeasures:

- **Anthropic 2026 Randomized Trial** — Engineers learning a new Python library showed AI users scored 50% vs 67% on comprehension quizzes, despite equal task completion speed. Conceptual questioners scored >65%; copy-pasters scored <40%.
- **MIT "Your Brain on ChatGPT"** — EEG showed reduced brain connectivity with LLM use; 83% of LLM users couldn't quote a single line of what they produced.
- **CHI 2026 Anchoring Effect** — LLM framing at task start produced measurably worse decisions even when humans did the rest independently.

Osmani advocated for **Learning Mode** features (Anthropic, OpenAI, Google have shipped them but adoption is near-zero for production work) and proposed concrete strategies: form a hypothesis before asking, request explanation before code, and treat "ship" and "learn" as separate metrics.

## Related Pages

- [[concepts/harness-engineering]] — The discipline he helped codify
- [[concepts/cognitive-surrender]] — Concept he explored in depth (May 2026): individual mechanism behind simulacrum and comprehension debt
- [[entities/vtrivedy10]] — Vivek Trivedy, who coined the term "harness engineering"
- [[entities/hamel-husain]] — Early popularizer of harness engineering from evals perspective
- [[concepts/agentic-engineering]] — Related engineering practice
- [[entities/simon-willison]] — Fellow developer experience leader and AI practitioner
