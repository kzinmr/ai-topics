---
title: Weekly Wiki Graph Analysis — Adjudicated Annotations
created: 2026-10-23
updated: 2026-10-23
type: query
tags: []
sources:
  - wiki/queries/wiki-graph-analysis-weekly-2026-10-23.md
---

# Weekly Wiki Graph Analysis — Adjudicated Annotations (2026-10-23)

Companion to [[queries/wiki-graph-analysis-weekly-2026-10-23]]. Raw report numbers are
inflated by known generator quirks (see `wiki-graph-health` skill). This page records the
adjudicated verdicts after reading the actual pages.

## 1. Duplicate groups — verdicts (16 raw groups)

| Group | Verdict | Evidence |
|---|---|---|
| `entities/_index` vs `concepts/_index` | FALSE POSITIVE | Different namespaces, both legit hub pages |
| `entities/cline` vs `concepts/cline` | BORDERLINE | Both rich (128 vs 98 lines); ensure mutual cross-link, do not merge |
| `entities/deliberate-coder` vs `entities/deliberatecoder` | FALSE POSITIVE | **Different people**: Ben Ilegbodu ("Deliberate Coder") vs Steve Shogren ("Deliberate Software"). Merging = data loss |
| `entities/eugene-yan` (352) vs `entities/eugeneyan` (220) | REAL DUP | Keep `eugene-yan` (richer this run), convert `eugeneyan` to `status: redirect` |
| `entities/giles-thomas` (92) vs `entities/gilesthomas` (228) | REAL DUP | Keep `gilesthomas` (richer this run), redirect `giles-thomas` |
| `entities/lilian-weng` (202) vs `entities/lilianweng` (156) | REAL DUP + CONTESTED | Keep `lilian-weng`; when merging keep BOTH career claims (OpenAI Preparedness VP vs Thinking Machines co-founder) with dates/sources, set `contested: true` |
| `entities/martin-fowler` vs `entities/martinfowler` | ALREADY HANDLED | `martin-fowler` is a 17-line redirect stub → `martinfowler`. Detector should skip redirect stubs |
| `entities/qwen` (145) vs `concepts/qwen` (88) | BORDERLINE | Entity (company/product) vs concept (model family) split is defensible; ensure cross-links |
| `entities/samuel-colvin` vs `entities/samuelcolvin` | ALREADY HANDLED | `samuelcolvin` is a 14-line `redirect: samuel-colvin` stub |
| `concepts/agent-harnesses` vs `comparisons/agent-harnesses` | BORDERLINE | Concept (157) vs comparison (412); legit namespace split if cross-linked |
| `concepts/alpha-proof-nexus` (142) vs `concepts/alphaproof-nexus` (52) | REAL DUP | Keep hyphenated, redirect the other |
| `concepts/deer-flow` (92) vs `concepts/deerflow` (51) | REAL DUP | Keep `deer-flow`, redirect `deerflow` |
| `concepts/dspy-rlm` (697, `status: complete`) vs `concepts/dspyrlm` (25, `status: stub`) | REAL DUP | Redirect the stub |
| `concepts/evals-skills` (25, stub) vs `comparisons/evals-skills` (69) | REAL DUP | April-stub family; redirect the concept stub |
| `concepts/llm-integration-patterns` (25, stub) vs `comparisons/llm-integration-patterns` (275) | REAL DUP | April-stub family; redirect the concept stub |
| `concepts/open-claw-ecosystem` (25, stub) vs `concepts/openclaw-ecosystem` (138, `status: complete`) | REAL DUP | April-stub family; redirect the stub |

**Net: 8 real dupes to consolidate, 2 already redirect stubs, 3 false positives, 3 borderline (cross-link only).**

## 2. Index gap — ground truth (independent resolver)

Independent recursive resolver (not the report's generator):

- index.md wikilinks: 3294
- missing-on-disk: **6** — ALL are prior weekly reports deleted by the report rotation
  (2026-08-28, 2026-08-28-annotations, 2026-09-18, 2026-09-25, 2026-10-02, 2026-10-16).
  The report's "27 stale index entries" is generator false-positive inflation; no other
  index cleanup needed. Fix: replace the dangling entries with today's report + annotations.
- not-on-disk-not-indexed (real): **0 beyond today's own report file**. The report's
  "22 not indexed" concepts are sibling-agent WIP (55 dirty wiki files from active-crawl /
  blog pipelines uncommitted at run time) — defer reconciliation to those pipelines.

## 3. Broken links — adjudication (4223 reported)

Top "missing" targets are mostly resolvable via nested paths; the naive resolver only
checks top-level dirs:

| Target | Actual location |
|---|---|
| `concepts/claude-code/claude-code` (36 refs) | `entities/claude-code.md` (namespace mismatch) |
| `concepts/ai-safety` (35 refs) | `concepts/security-and-governance/ai-safety.md` |
| `grpo` (22 refs) | `concepts/post-training/grpo.md` |
| `gaia-benchmark` (20 refs) | `concepts/ai-benchmarks/gaia-benchmark.md` |
| `reinforcement-learning` (19 refs) | `concepts/post-training/reinforcement-learning.md` |
| `tau-knowledge` (14 refs) | `concepts/ai-benchmarks/tau-knowledge.md` |
| `agentdojo` (14 refs) | `concepts/ai-benchmarks/agentdojo.md` |
| `concepts/swe-bench` (14 refs) | `concepts/ai-benchmarks/swe-bench.md` |
| `hal-leaderboard` (16 refs) | `concepts/ai-benchmarks/hal-leaderboard.md` |

GENUINELY missing (worth creating or de-linking): `agent-evaluation` (26 refs, no page at
any depth — closest: `concepts/evaluation/agent-evaluation-methodology`),
`concepts/agent-memory` (16 refs — closest: `concepts/harness-engineering/system-architecture/ai-memory-systems`),
`concepts/rag` (15 refs — closest: `concepts/rag-systems`), plus 38 refs of empty `[[]]`
wikilinks (malformed links; strip).

## 4. Orphans (491 reported / 485 content-rich)

Known inflation: ~20 are referenced only via bare (non-namespaced) wikilinks — namespacing
those links fixes orphan status + broken links in one pass. Top actionable content-rich
orphans to give inbound links:

1. `concepts/harness-engineering/system-architecture/claude-code-best-practices` (385 L)
2. `concepts/ai-energy` (317 L)
3. `concepts/multi-objective-policy-distillation` (279 L)
4. `entities/openenv` (234 L)
5. `concepts/claude/system-card-milestones` (231 L)
6. `entities/ibrahim-diallo` (227 L)
7. `concepts/symphony` (208 L)

(`queries/2026-10-04-uncommitted-wip-snapshot-query`, 3680 L, is a WIP snapshot artifact —
ignore, candidate for `_archive/`.)

## 5. Stale pages / tag violations

- 2385 stale (>90d) is dominated by bulk-import `updated` dates (April cohorts) — "never
  touched", not "degraded". No action beyond size+staleness prioritized review.
- Report's "1 tag violation" is an undercount: a SCHEMA-vs-frontmatter scan finds many
  page-slug self-tags that aren't in the taxonomy (e.g. `concepts/nixos` tagged `nixos`).
  Route to the `tag-audit-weekly` job, not this run.

## 6. Action list (prioritized)

1. [HIGH] Consolidate 8 real dup pairs (add `status: redirect` to the thinner page).
2. [HIGH] Strip 38 empty `[[]]` links.
3. [MEDIUM] Namespace-fix top broken targets per §3 table (9 targets ≈ 200 refs).
4. [MEDIUM] Create or alias `agent-evaluation`, `agent-memory`, `rag` to nearest pages.
5. [MEDIUM] Add inbound links to top 7 content-rich orphans (§4).
6. [LOW] Fix index.md dangling report entries (done in this run).
7. [BACKLOG] Generator bugs in `_weekly_graph_report.py`: skip redirect stubs in dup
   detector; resolve `foo/_index.md`; stop dangling index entries on report rotation.
