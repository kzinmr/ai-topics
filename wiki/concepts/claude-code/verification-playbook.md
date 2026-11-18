---
title: "Claude Code Verification Playbook"
type: concept
created: 2026-11-18
updated: 2026-11-18
tags: [claude-code, coding-agents, verification, testing, developer-tooling, anthropic]
sources:
  - raw/articles/2026-11-16_claude-dev_claude-code-team-verification.md
confidence: medium
related:
  - "[[concepts/claude-code/_index]]"
  - "[[concepts/code-review-bottleneck]]"
  - "[[concepts/formal-verification-llm-agents]]"
  - "[[concepts/coding-agents/ai-coding-reliability]]"
---

# Claude Code Verification Playbook

How the Claude Code team verifies agent-written code — Addy Osmani's post "How the Claude Code team thinks about verification" (claude.dev, Nov 16 2026, HN 282p). Context: **~90% of the team's code is written and reviewed by Claude**; verification loops are what allow running dozens-to-hundreds of agents in parallel instead of one or two.

> Internal Anthropic claims ("up to 10 points" grader gains, reliability-checklist mechanics) are self-reported, hence confidence: medium.

## Why verification loops

- Separate grader against a rubric improved task success **by up to 10 points** over a standard prompting loop in internal testing on structured file generation, largest gains on the hardest problems.
- Tests/benchmarks/specs are now cheap to *generate* and then run as software without many extra tokens — closing the loop feeds failures back as hooks or CLAUDE.md rules.
- Failure modes: **flaky tests train the agent to re-run instead of fix**; slow tests shrink batch coverage — save heavy tests for pre-commit.

## Three test types worth investing in

1. **E2E tests** — hardest to fool, definitive done criteria; give the agent "hands and eyes" on the running app via CDP, simulators, or API harnesses; a feature map doubles as grading rubric.
2. **Property tests** — invariants that can't break (round-trip encoding, non-negative balance, idempotency, optimized≡naive equivalence) via fast-check / Hypothesis / proptest; generated edge cases don't share the coding agent's bias — especially useful for rewrites when the spec has drifted from production.
3. **Differential tests** — old system as oracle for migrations; random or production-sample inputs, normalize irrelevant factors, maintain an approved-differences list.

## Team process rules

- **Verification means running the change** — a `verify` skill in `.claude/skills/` that boots and smoke-tests the app; Claude iterates on the skill itself.
- **Failing tests → human** after three fix rounds.
- **Code owners write their own checks**; checks must say *why* they pull a reviewer in.
- **39-item reliability checklist** with diff-readable triggers (e.g. "--resume loads old transcripts"); Claude checks only the 3–10 matching items.
- **One reviewer, multiple rounds** — tuning a primary reviewer with a REVIEW.md beats stacking a second expensive reviewer; rounds build on earlier-round context.
- **Changes can't modify their own checks** — REVIEW.md read from the base branch, never the PR; reviews pinned to commits.
- **Cheap checks first** — tests/build/lint before opening a PR, enforced via hook or `/goal`.
- **Commit gates with verify stamps** — off/observe/enforce modes; blocked twice → let the next through so the agent doesn't deadlock.
- **Review the reviewers** — eval built from past incidents/reverts (repo restored to review-time state, one-sentence answer key), separate recall tracking for raw findings / post-verification / final review, Important/Nit/Pre-existing tags, recall tuned only up to the overfitting point.

## Position

The direct prescription side of the [[concepts/code-review-bottleneck]] thesis: if human review is the binding constraint, the leverage is *machine-checkable evidence attached to every change* — the same conclusion [[concepts/coding-agents/ai-coding-reliability]] and the Harvard Chen–Stratton study point to. Contrast formal methods in [[concepts/formal-verification-llm-agents]]; team-wide review mechanics in the earlier "how code review works at Anthropic" post.

## See Also

- [[concepts/claude-code/claude-code-skills]] — the skill system the `verify` skill uses
- [[concepts/claude-code/claude-md-rules]] — where closed-loop failures get codified
