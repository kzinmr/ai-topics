---
title: Architect Loop (Cross-Vendor Agent Pattern)
created: 2026-06-14
updated: 2026-06-14
type: concept
tags:
  - coding-agents
  - agent-harness
  - agent-loop
  - prompting
  - tool-use
  - cost-optimization
  - multi-agent
  - agent-orchestration
  - vendor-lock-in
  - agent-architecture
sources:
  - raw/articles/2026-06-14_danmcinerny_architect-loop-fable-codex.md
  - https://github.com/DanMcInerney/architect-loop
---

## Overview

**Architect Loop** is an open-source, cross-vendor agent loop pattern that pairs [[concepts/claude/fable-5|Claude Fable 5]] as the architect/planner with [[entities/codex|OpenAI Codex]] (GPT-5.5) as the builder. By splitting planning from execution across two different AI labs, it reduces token costs by ~58–74% compared to running a top model end-to-end, while adding cross-model review that reduces same-model review bias.

The repo functions as the only persistent memory — not in the repo = didn't happen. Two Claude Code skills drive the loop: `/architect` for building and `/architect-research` for discovery-scale research.

## Architecture

The system separates concerns across three roles:

| Role | Model | Effort | Owns |
|------|-------|--------|------|
| Architect | Claude Fable 5 (via Claude Code, `effort: high`) | Minutes per work block | Arbitration, judging raw evidence against frozen gates, next-slice specs, kill/continue decisions |
| Builder | GPT-5.5 (via `codex exec`, `xhigh` reasoning) | Hours per slice | Implementation, lane agents, raw-results reporting |
| Memory | The repo: `docs/HANDOFF.md`, `docs/gates/`, git history | Permanent | Everything |

**Two commands:**

- **`/architect`** — The build loop: one Fable session per work block judges the last run, specs the next slice, dispatches builders. Fable never writes code — it specifies, judges, and integrates.
- **`/architect-research <topic>`** — The research loop: for when you're still deciding *what* to build. Scout-first decomposition produces a cited decision report that feeds the build loop's PRD.

## Loop Mechanics

### `/architect` — The Build Loop

Each work block follows a strict sequence:

1. **Ground**: Read `CLAUDE.md`/`AGENTS.md` → verification gate → `docs/HANDOFF.md`
2. **Arbitrate**: Resolve every open disagreement (ACCEPT/REJECT/MODIFY + one-line reason)
3. **Judge**: Run gates yourself against verbatim frozen text (PASS/FAIL/INVALID per gate → kill/continue)
4. **Spec next slice**: Objective + output format + tool guidance + boundaries; freeze gates to `docs/gates/<slice>.md` *before* any builder starts; commit the freeze
5. **Dispatch**: 1–4 parallel `codex exec` lanes, each in its own git worktree with fresh context. Builders must surface disagreements before building (silent compliance = defect), build only their declared files, report raw results — they never commit
6. **Post-flight**: Architect verifies builder claims directly — runs gate commands, reads diffs against spec intent, checks for gate tampering and boundary violations, then commits/merges passing lanes

**Key properties:**
- Fable judges in a *later* session than the one that dispatched — always fresh-context review
- `docs/gates/` are read-only to builders. Any builder edit to a gate file = automatic slice FAIL
- Multi-hour builder runs are normal (community reports: 6.5h runs at ~20% of a weekly Codex quota)
- Supervision built in: liveness checks, stall triage, explicit timeouts on long commands

### `/architect-research` — The Research Loop

Scout-first decomposition mirrors production deep-research systems (OpenAI DR, Anthropic, Gemini, Perplexity, Kimi):

1. **Cheap Codex scout** maps the topic (~10 searches): canonical terminology, load-bearing systems, named people, natural fault lines
2. **Fable designs 3–6 topic-specific lanes** from the scout's map, drawing from a source-class tactics library — checked for overlap and gaps before dispatch
3. **Parallel Codex researchers** run under hard budgets: search caps, ≤5 subjects per lane, saturation stop, strict findings discipline (URL + date + quote + confidence tag; NOT FOUND beats inference; no recommendations)
4. **Fable verifies and writes**: ≥2 independent sources per load-bearing claim, adversarial falsification searches, citations only from URLs actually fetched — one author writes one decision-oriented report. Gathering parallelizes; synthesis never does

## The Twelve Design Rules

Each rule is mechanically enforced by the skill, not left as advice:

1. **R1: Repo as memory** — Not in `HANDOFF.md` = didn't happen. Architect refuses to judge results that exist only in chat output
2. **R2: Gates freeze before results** — Gates committed pre-dispatch in `docs/gates/`; any builder edit = automatic FAIL
3. **R3: Builder never grades its own work** — Three-stage review: builder's own reviewer lane (cheap first pass), architect runs gates itself, cross-model adversarial pass for high-stakes slices
4. **R4: Grade the outcome, not the path** — Per-gate verdicts (PASS/FAIL/INVALID), then slice-level kill/continue
5. **R5: Mandatory disagreement with citations** — Builder's PHASE 0 must surface every disagreement with the spec citing real files; silent compliance is a defect
6. **R6: Full delegation contract** — Every dispatch: objective + output format + tool guidance + boundaries
7. **R7: One slice per iteration, fresh builder context** — Every slice is a fresh `codex exec` process. No context stretching across slices
8. **R8: Architect-orchestrated parallelism** — 1–4 lanes, disjoint file sets, isolated git worktrees. Architect owns the fan-out, not Codex
9. **R9: Supervise asynchronously** — Never block on the builder. Fable 5 tuned for async dispatch and parallel subagent sustainment
10. **R10: Grounded progress claims** — Audit every status claim against tool output; raw tables/numbers/SHAs only, no interpretation
11. **R11: Ground before judging** — Read project docs, learn verification gate before any judgment. Not everything needs the loop; scale effort to task
12. **R12: Keep skills thin and declarative** — Push detail to referenced files; prune against each new model generation

## Cost Analysis

The cross-vendor split yields significant savings:

- **Architect (Fable 5)**: Paid Claude plan, minutes per work block, `high` effort
- **Builder (GPT-5.5)**: Paid ChatGPT plan flat-rate, hours per slice, `xhigh` effort (review-survival optimized: 88% semantic equivalence vs 69% at `high`)
- **Orchestrator/worker split**: 58–74% lower cost vs running the top model end-to-end (community measurements from the Fable 5 Orchestrator Playbook)
- **Research fan-out**: ~15× chat-level tokens — deliberately gated as a separate skill
- **No API keys required**: Both models run on consumer subscriptions by default. `CODEX_API_KEY` available for per-token billing on overnight loops

## Why Cross-Vendor

The pattern addresses three predictable single-agent failure modes:

1. **Context rot** — Performance degrades as the context window fills. Fresh builder context per slice + repo as memory
2. **Self-grading** — 47–74% of self-improvement runs show proxy gains without real gains. Cross-model review (different labs) reduces same-model bias
3. **Goalpost drift** — Frozen gates prevent criteria edits after results exist

The split aligns with available benchmarks: GPT-5.5 leads Terminal-Bench 2.0 (82.7%) for hands-on terminal work; Fable 5 excels at long-horizon judgment and persistent file-based memory.

## Related Concepts

- [[concepts/claude/fable-5|Claude Fable 5]] — The architect model used in this loop
- [[entities/codex|OpenAI Codex]] — The builder tool (GPT-5.5 via `codex exec`)
- [[concepts/coding-agents/coding-agents]] — Broader coding agent ecosystem
- [[concepts/token-economics]] — Cost optimization context
- [[concepts/codex/codex-agent-loop]] — Codex's native agent loop (single-model)
- Ralph Loop — Precursor pattern emphasizing always-fresh context [external: ghuntley.com/ralph]
