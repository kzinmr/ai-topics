---
title: "Lint Rules as the Agent Feedback Loop (Anti-Slop Factory)"
type: concept
created: 2026-10-13
updated: 2026-10-13
confidence: medium
tags:
  - coding-agents
  - agentic-engineering
  - code-quality
  - developer-tooling
  - software-engineering
  - agent-harness
  - case-study
  - anti-pattern
aliases: ["lint-as-agent-feedback", "anti-slop software factory", "slop compounds"]
sources:
  - raw/articles/x.com--sarahfim--anti-slop-software-factory--2026-10-12.md
related:
  - concepts/agents-md-code-quality
  - concepts/dark-factory-software-factory
  - concepts/agentic-software-factory-hierarchy-of-needs
  - concepts/agent-slop
  - concepts/coding-agents/closing-agent-loop
  - concepts/coding-agents/ai-code-quality
  - concepts/agent-first-codebase-design
  - concepts/agent-harness-primitives
---

# Lint Rules as the Agent Feedback Loop (Anti-Slop Factory)

Practitioner framework from **Sarah (@sarahfim)**, lead product engineering at [[entities/composio|Composio]], from her X Article *"How to build an anti-slop software factory for teams of 30+"* (2026-10-12). She designed the Composio dashboard repo from scratch in Feb 2026 (right after Claude Code's breakout) for ~50 contributors spanning engineering, product, and marketing — all bringing their own personal agents — and reports most changes became "one-shot-able and really easy to approve."

## Core thesis: the repository is the factory, not the agent

Contrary to the common "software factory = agent swarms + Kanban boards" mental model, Sarah argues a good factory is defined by the **repository and its machinery** (CI, lint rules, type system, tests), so that *anyone* can bring *any* agent/harness/model and it becomes "almost impossible for that agent to write bad code." This inverts the [[concepts/agentic-software-factory-hierarchy-of-needs]] emphasis on the harness: the repo substrate sits below even the harness.

## Slop compounds

The failure mode she names: if a cloud agent works in a repo full of slop, it is asked to *slop a plan → slop an implementation from that plan → self-review its own slop*. Repeated at scale, "the slop is exponential" — PRs become slower to approve and velocity decays over time. This is the repo-level counterpart to [[concepts/agent-slop]] (which measures the marketing-vs-capability gap at the model level); here the slop originates in the codebase, not the model.

## Lint rules > skills (the mechanism claim)

The page's most citable argument — why deterministic enforcement beats instructional guidance:

- **Agents ignore instructions.** "You have to assume that every rule you write in a skill will be broken by someone's agent, if not your own."
- **Skills rot.** Models improve; each model's pitfalls differ from the next model's. Every skill she ever wrote eventually became tech debt / "context debt" for other agents.
- **Lint closes the loop.** A skill *tells* an agent a rule; a lint rule tells the agent it *broke* the rule, immediately, with exactly how to fix it — and it closes the loop for *everyone's* agents, not just the skill's author's.
- Operational rule of thumb: **"every time an agent gets something wrong, you lint it away."** Composio's dashboard ended up with 38 custom lint rules — including theming, global-primitive enforcement, banning `lib/`/`utils/`, and even banning `useState`/`useEffect` outright (use requires a justification comment pointing to React Query / React Hook Form / nuqs instead).
- She is optimistic about automation of rule authoring itself: **React Doctor** (automatic React best-practice checks) and "anti-slop" linters that detect common agent anti-patterns.

This is the strongest published articulation of the counter-position in the HN debate on [[concepts/agents-md-code-quality]] ("a bunch of these should be enforced with linting") — taken to its extreme: instructions are advisory, lint is enforceable, so prefer enforceable.

## The seven repo-level practices (summary)

| # | Practice | Anti-slop mechanism |
|---|----------|--------------------|
| 1 | **Co-location** (feature owns its components/helpers/tests; `lib/`/`utils/` banned) | Less grep/ls → less context flooding; PR scope is visible at a glance |
| 2 | **End-to-end type safety** (tRPC, OpenAPI) | Schema change → compiler shows the agent every call site that must change |
| 3 | **Duplication is OK** (except global primitives, which are lint-enforced) | Codegen is cheap; shared abstractions for near-duplicates cost more than they save (Tailwind precedent) |
| 4 | **Lint rules** | Deterministic, immediate, self-correcting feedback — see above |
| 5 | **End-to-end tests** (Meticulous session replay; MCPJam for MCP servers) | Global visual/protocol regression signal no single agent can self-verify |
| 6 | **Bugbots last** (BUGBOT.md best practices per repo) | Only for nondeterministic bugs; high false positives, slower loop than lint |
| 7 | **Fast CI** (Blacksmith: some checks −50%, some −70%+) | Non-engineers live in preview deployments; build+checks *is* their whole loop |

Cloud agents (their internal **Zen**: 1,300+ merged PRs since Feb 2026, 245 in Sep alone, triggered from Slack/Linear/Datadog/cron) come *after* the seven — made effective by context access (Datadog logs, PostHog sessions, Linear tickets) through Composio's managed auth, which lets prompts stay vague.

## Positioning among factory case studies

Added to the [[concepts/dark-factory-software-factory]] case-study lineage as the **mid-scale (30–50 people, cross-functional)** datapoint: StrongDM (3-person team), Warp (startup memo), Uber (Fortune-500, cost curves) — Composio contributes the "mixed-skill contributors with BYO agents" scenario, where enforcing quality *structurally* matters most because reviewers can't be domain experts everywhere.

## Related

- [[concepts/dark-factory-software-factory]] — levels-of-automation framing; this page adds the mid-scale case study
- [[concepts/agentic-software-factory-hierarchy-of-needs]] — harness-first thesis; Sarah's repo-first claim is a counterweight
- [[concepts/agents-md-code-quality]] — the instruction-side of the same debate
- [[concepts/agent-harness-primitives]] — "encode constraints as tooling (custom linters with remediation)" is the same primitive
- [[concepts/coding-agents/closing-agent-loop]] — Cognition's catch/fix loop; lint is the cheapest loop-closer
- [[concepts/coding-agents/ai-code-quality]] — slop-cannon vs quality-first framing
- [[concepts/agent-first-codebase-design]] — co-location / duplication are instances of designing for agent retrieval

## Sources

- Sarah (@sarahfim), "How to build an anti-slop software factory for teams of 30+", X Article, 2026-10-12 — https://x.com/sarahfim/status/2109736893198016898 (raw: `raw/articles/x.com--sarahfim--anti-slop-software-factory--2026-10-12.md`)
