---
title: "Fred K. Schott (@FredKSchott)"
type: entity
handle: "@FredKSchott"
created: 2026-05-10
updated: 2026-08-16
tags:
  - person
  - harness-engineering
  - coding-agents
  - open-source
aliases:
  - "fred-schott"
  - "Fred Schott"
  - "FredKSchott"
sources:
  - "https://x.com/FredKSchott"
  - "https://github.com/fredkschott"
  - "https://x.com/FredKSchott/status/2050274923852210397"
  - "raw/articles/2026-05-09_addyosmani-agent-harness-engineering.md"
  - "raw/newsletters/2026-08-15-react-for-agents-astro-creator-brings-hooks-to-his-meta-harness-flue.md"
  - "https://www.latent.space/p/flue-2"
related:
  - "[[concepts/harness-engineering/agent-harness]]"
  - "[[entities/addy-osmani]]"
  - "[[entities/vtrivedy10]]"
---

# Fred K. Schott (@FredKSchott)

| | |
|---|---|
| **X** | [@FredKSchott](https://x.com/FredKSchott) |
| **GitHub** | [fredkschott](https://github.com/fredkschott) |
| **Role** | Creator of **Astro** (web framework) and **Flue** (agent harness framework) |
| **Known for** | Building foundational developer infrastructure — from static site generators to agent harnesses |

## Bio

Fred K. Schott is a developer tools creator best known as the co-creator of **Astro**, the modern web framework (islands architecture, zero-JS by default). In May 2026, he launched **Flue** — the first dedicated **agent harness framework** for TypeScript.

Schott identifies as "CEO of HTML" — a playful nod to his focus on building practical, developer-first infrastructure that abstracts away complexity.

## Flue: The Agent Harness Framework

Flue is a TypeScript-native agent harness framework released in May 2026. Its key design principles:

| Principle | Implementation |
|-----------|---------------|
| **100% headless, programmable** | No TUI/GUI assumptions — deploy anywhere |
| **Markdown-driven logic** | Skills, roles, and AGENTS.md define agent behavior |
| **Built-in harness** | Sessions, sub-agents, sandboxing, loop orchestration shipped OOTB |
| **Zero-config sandboxing** | Isolated execution without manual setup |
| **Node.js, Cloudflare, GitHub Actions** | Deploy on multiple runtimes |

Flue was the first framework to frame itself explicitly as an **agent harness framework** rather than an AI SDK or chat wrapper. As Addy Osmani noted, "Flue... was apparently inspired by an earlier version of [the Agent Harness Engineering] post."

**Python port**: PyFlue, created by Shashikant Jagtap, brings the same Markdown-skills, persistent sessions, sandboxed FS/shell, and pluggable backends (DeepAgents, OpenAI Agents SDK, Google ADK, PydanticAI) to Python.

Flue was featured by Render for one-click deployment.

## Core Ideas

### Harness-as-a-Service (HaaS)

Flue embodies the HaaS paradigm: instead of wiring agent loops, context management, and sandboxes from scratch, developers select Flue, configure skills/prompts/hooks, and focus purely on domain logic.

### Agent = Model + Harness

Schott's framing aligns perfectly with Vivek Trivedy's definition. Flue explicitly separates the model (interchangeable, via any provider) from the harness (Flue's runtime).

## Flue 2 & the "React for Agents" Thesis (Aug 2026)

In a [Latent Space interview with Richard MacManus](https://www.latent.space/p/flue-2) (Aug 15, 2026), Schott detailed Flue 2 (first stable release, built on React-style Agent Hooks):

- **"Maybe no one has even built the React for agents"** — he initially pitched Flue as "the Astro for agents or the Next.js for agents," then pivoted to React-style hooks after early users (especially "bigger customers, their whole company is one agent") showed file-based routing was the wrong abstraction.
- An agent in Flue is a **JavaScript function that re-renders every turn**; 16 built-in hooks (`useSkill()`, `useTool()`, `useSubagent()`) plus custom hooks enable dynamic runtime configuration — "real support bots, real triage bots."
- **"There is no agent without a harness"** — Flue 2 is built on Pi, an open-source minimal harness (Pi to Flue = Vite to Astro); harness is fundamental, not a feature.
- **Host portability**: "The best tools are the ones that float above the host" — Flue is an open-source framework for every host (Cloudflare is Schott's employer, but Flue is not Cloudflare-bound). Contrasted with Vercel's eve, "the most directly competitive," which is optimized for Vercel's platform.
- **On meta-harnesses** (Databricks Omnigent, Exo): he's played with Exo and finds the discussion fascinating, but argues "the framework and the harness are very intertwined" — one API across all harnesses would muddle Flue's story.
- **On LangChain Managed Deep Agents**: not on Flue's roadmap — "It's so early for us, we're just focused on building the best harness."
- Onboarding is **agent-first**: "pass this prompt to your agent, it's gonna guide you through it" — the docs have markdown support, and many users (including MacManus) set up Flue agents via Claude Code.

The interview connects his v1 framing ("like Claude Code, but 100% headless and programmable") to the broader [[concepts/harness-engineering]] and [[concepts/agent-team-swarm|meta-harness]] landscape. Flue's origin: an issue-triage system inside the Astro repo that grew into a headless, hostable Claude Code experience. See [[entities/flue]] for the full framework detail.

## Related

- [[entities/addy-osmani]] — Cited Flue as a HaaS exemplar in "Agent Harness Engineering"
- [[entities/vtrivedy10]] — Coined "Agent = Model + Harness"
- [[concepts/harness-engineering/agent-harness]] — Comprehensive harness architecture reference
- [[concepts/why-harness-development-boom]] — Structural forces driving harness development
