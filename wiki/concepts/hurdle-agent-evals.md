---
title: "Hurdle (Together AI agent evals)"
created: 2026-11-27
updated: 2026-11-27
type: concept
tags:
  - agent-evaluation
  - evals
  - llm-as-judge
  - coding-agents
  - agent-skills
  - sandbox
  - open-source
  - together-ai
sources:
  - "raw/articles/2026-11-25_together-ai_introducing-hurdle-agent-evals.md"
  - "https://www.together.ai/blog/introducing-hurdle-run-agent-evals-on-your-api-skills-and-docs"
related:
  - "[[entities/together-ai]]"
  - "[[concepts/llm-evaluation]]"
  - "[[concepts/agent-skills]]"
  - "[[concepts/evaluation/agent-evaluation-methodology]]"
---

# Hurdle (Together AI agent evals)

**Hurdle** is an open-source npm library released by [[entities/together-ai]] on 2026-11-25 for running **agent evaluations of a company's own developer platform** — its API, SDK, docs, and agent skills. It drives Claude Code and Codex against real-world "task" prompts, records each session, and scores runs with a mix of deterministic code checks, runtime guards, and an LLM judge, then reports pass rates by model and condition.

## Why it exists

Coding agents have become one of the main ways developers consume an API or SDK, so "how agent-friendly is our platform?" is now a first-class DX question. Together started doing this internally in spring 2026, found hand-orchestration "extremely tedious," and spent six months building Hurdle. The pitch: benchmark your platform's agent experience across a representative sample of models, harnesses, and conditions — the same way Together does.

## Core primitives

| Primitive | What it does |
|---|---|
| **Task** | A prompt a developer would hand an agent (plus starter files) |
| **Checks** (`defineChecks`) | Post-run assertions: required API requests (method/path/status), files or data the agent must produce |
| **Guards** (`defineGuard`) | In-flight blocks: e.g. deny `POST /v1/compute/clusters` so an eval agent can't spin up a real GPU cluster; blocked request gets a 403 and counts as failure |
| **Judge** (`run.judge`) | Rubric handed to an LLM judge over the recorded session |
| **Suite** (`defineSuite`) | Matrix of tasks × agents (runner + model) × conditions × repeats; `verdict: "hybrid"` requires both code checks and judge to pass |
| **Conditions** | A/B arms like `baseline` vs `with-skill` (injects an agent-skill directory) — direct measurement of whether your docs/skill actually improve agent pass rates |

Run with `npx hurdle run --view`; results persist to `.hurdle/`. Example suite in the launch post: 1 task × 2 models (claude-opus-4-8, claude-sonnet-4-6) × 2 conditions × 15 repeats = 60 runs.

## Sandboxing and key safety (Guardian)

Two run modes:

- **Local**: Hurdle launches the `claude`/`codex` CLI in a temp workspace with a clean config. Caveats: no guards/request checks (Hurdle can't see API traffic), and the agent runs *as you* with your real keys — only for trusted tasks.
- **Sandboxed** (production): each run gets a fresh **Together Sandbox**. A local proxy, **Guardian**, intercepts all traffic: the agent only ever holds *random stand-in keys*; Guardian swaps in the real key (Authorization header only) when forwarding to your API or the model provider. This routing is what enables request checks, guards, and transcript-safe key handling ("if a stand-in leaks into the transcript, it's nbd"). macOS/Linux only for now.

Default sandboxing does not restrict *which* endpoints the agent can hit — the launch post explicitly advises a dedicated low-balance eval key plus guards for dangerous operations.

## Assessment

Hurdle packages several 2026 agent-eval orthodoxy points into one tool: evals belong in the *agent harness* (not just model outputs), pass rates need repeats because single runs pass/fail by chance, skill/doc effectiveness should be A/B-tested as eval *conditions*, and guard-based scoring (an agent that *attempts* a forbidden action fails even if it recovers) is a distinct signal from output checks. It complements model-benchmark suites by targeting the platform-under-test.

## Open questions

- Judge cost at scale (hybrid verdicts run an Opus-class judge per scored run)
- Guardian currently swaps keys only into the `Authorization` header — APIs with other auth schemes can't be sandbox-tested
- Runner support is Claude Code + Codex only (no generic ACP harness yet)

## Related

- [[entities/together-ai]] — vendor; also ships Post-Training and Sandbox APIs used by Hurdle
- [[concepts/agent-skills]] — Hurdle conditions formalize "does this skill help agents?"
- [[concepts/llm-evaluation]] — broader eval methodology context
- [[concepts/sandbox]] — isolation substrate for risky agent workloads
