---
title: Weekly Wiki Graph Analysis — Adjudicated Annotations (2026-11-13)
created: 2026-11-13
updated: 2026-11-13
type: query
tags: [wiki]
sources: []
---

# Weekly Graph Analysis — Adjudicated Annotations (2026-11-13)

Companion to [[queries/wiki-graph-analysis-weekly-2026-11-13]]. All counts below are
re-verified THIS session via `deep_link_audit.py` + an independent inline resolver;
the raw report's numbers are inflated by known generator bugs (see Backlog).

## Ground-truth metrics (this session)

| Metric | Raw report | Verified | Note |
|---|---|---|---|
| Pages scanned (L2) | 3450 | 3456 | deep audit |
| Orphans (no inbound) | 491 | 460 (≥20 lines) | deep audit, excl. index pages |
| Broken wikilinks | 3449 | 2581 true | 448 bare + 463 raw + 438 entity-ns unresolved |
| Duplicate groups | 17 | 0 actionable | all adjudicated below |
| Tag violations | 1 | 0 | tag_audit.py: "Tags NOT in taxonomy: 0" |
| Not indexed | 23 | 1 (today's report) | sibling WIP (4 raw newsletters) deferred to newsletter pipeline |
| Stale index entries | 27 | 3 | = deleted prior reports + `_archive` entry |
| Stale >90d | 2558 | 2558 | bulk-import dates; low urgency |
| Oversized >200L | 330 | 330 | unchanged vs last week (326) |

## Dup-group verdict table (17 groups)

| Group | Verdict | Evidence |
|---|---|---|
| entities/_index vs concepts/_index | FALSE POSITIVE | different namespaces, meta-pages |
| entities/cline vs concepts/cline | LEGIT SPLIT | product page vs "Autonomous Coding Agent Paradigm" concept |
| entities/deliberate-coder vs entities/deliberatecoder | FALSE POSITIVE | Ben Ilegbodu vs Steve Shogren — different people (known trap) |
| entities/eugene-yan vs entities/eugeneyan | ALREADY HANDLED | eugeneyan = `status: redirect` stub (11L) → eugene-yan (352L) |
| entities/giles-thomas vs entities/gilesthomas | ALREADY HANDLED | giles-thomas = `status: redirect` (11L) → gilesthomas (228L) |
| entities/lilian-weng vs entities/lilianweng | ALREADY HANDLED | lilianweng = `status: redirect` (11L) → lilian-weng (202L) |
| entities/martin-fowler vs entities/martinfowler | ALREADY HANDLED | martin-fowler has `redirect: [[entities/martinfowler]]` (17L) → martinfowler (171L) |
| entities/nvidia-openshell vs concepts/nvidia-openshell | LEGIT SPLIT | org/product (128L) vs agent-runtime concept (43L) |
| entities/omnara vs concepts/omnara | LEGIT SPLIT | company (51L) vs platform concept (114L) |
| entities/qwen vs concepts/qwen | LEGIT SPLIT | product org (152L) vs model family (89L) |
| entities/samuel-colvin vs entities/samuelcolvin | ALREADY HANDLED | samuelcolvin has `redirect: samuel-colvin` (14L) → samuel-colvin (233L) |
| concepts/agent-harnesses vs comparisons/agent-harnesses | LEGIT SPLIT | concept (158L) vs 9-harness comparison (412L) |
| concepts/alpha-proof-nexus vs concepts/alphaproof-nexus | ALREADY HANDLED | alphaproof-nexus has `redirect: alpha-proof-nexus` (39L) |
| concepts/deer-flow vs concepts/deerflow | ALREADY HANDLED | deerflow has `redirect: deer-flow` (45L) |
| concepts/dspy-rlm vs concepts/dspyrlm | ALREADY HANDLED | dspyrlm = `status: redirect` (18L) → dspy-rlm (697L) |
| concepts/llm-integration-patterns vs comparisons/llm-integration-patterns | ALREADY HANDLED | concept side = `status: redirect` (18L) → comparison (275L) |
| concepts/open-claw-ecosystem vs concepts/openclaw-ecosystem | ALREADY HANDLED | hyphen side = `status: redirect` (18L) → openclaw-ecosystem (138L) |

**Total merges needed: 0.** Same verdict distribution as 2026-11-06 (17 groups, 0 merges).

## Index reconciliation (verified)

- missing-on-disk = 3 REAL: the two 2026-11-06 report/annotations entries (rotated out by
  the generator) + `concepts/gpt/_archive/2026-04-24-news-aggregation` (intentionally
  archived but still linked — cleanup candidate, low priority).
- not-indexed = 1 REAL: today's own report page (fixed by this run's index edit).
- The report's "23 not indexed" = 4 untracked sibling-pipeline raw newsletters (defer to
  newsletter-wiki-ingest) + resolver keying artifacts.

## Broken-link triage: genuine missing-page queue

Report top targets MINUS nested-resolvable ones (resolved this session:
`agent-evaluation`→concepts/evaluation/agent-evaluation-methodology,
`bitter-lesson`→concepts/rich-suttons-bitter-lesson,
`inference-optimization`→concepts/llm-inference-optimization-performance,
`ai-governance`→concepts/security-and-governance/agentic-ai-governance, etc.):

| Target | Refs | Status |
|---|---|---|
| `[[]]` (empty links) | 47 | mechanical syntax fix |
| concepts/claude-opus-4-7 | 10 | GENUINE — create page or alias to concepts/claude |
| entities/cursor | 14 | GENUINE entity (only nested arch pages exist) |
| entities/ben-clavie | 9 | GENUINE entity |
| entities/huggingface | 10 | GENUINE entity |
| concepts/enterprise-ai | 13 | borderline (scaling-patterns/deployment pages exist; needs hub) |
| concepts/ai-adoption | 11 | borderline (ai-adoption-barbell/failures exist; needs hub) |
| concepts/agent-architecture | 10 | borderline (ai-agent-architecture exists — could alias) |
| concepts/agent-framework | 9 | borderline (microsoft-agent-framework exists) |
| concepts/ai-coding | 9 | borderline (ai-coding-effectiveness-debate exists) |

Creation queue (HIGH→LOW): claude-opus-4-7, entities/cursor, entities/huggingface,
entities/ben-clavie, then hub-vs-alias decisions for the 5 borderline targets.

## Orphans — content-rich linking priorities

Top content-rich orphans (deep audit, ≥20L, no inbound). Each is referenced only by
index.md; recommend adding a wikilink from the thematically nearest hub page:

1. queries/2026-10-04-uncommitted-wip-snapshot-query (3680L) — WIP snapshot artifact;
   consider archiving instead of linking.
2. concepts/multi-objective-policy-distillation (279L) → link from post-training hub
3. entities/ibrahim-diallo (237L), entities/openenv (234L), entities/shuvendu (175L)
4. concepts/claude/system-card-milestones (231L) → concepts/claude hub
5. concepts/symphony (208L), concepts/spine-swarm-agents (187L),
   concepts/hegel-property-based-testing (187L)
6. concepts/ai-benchmarks/skillspector (188L) → ai-benchmarks index
7. comparisons/codex-app-server-vs-claude-agent-sdk (185L),
   comparisons/openclaw-pi-hermes-state-management (183L) → comparisons hub
8. concepts/reasoning-trace-extraction-vulnerability (181L) → security-and-governance hub

## Week-over-week trend

| Metric | 2026-11-06 | 2026-11-13 | Δ |
|---|---|---|---|
| L2 pages | 3404 | 3456 | +52 |
| True orphans (≥20L) | 457 | 460 | +3 |
| True broken links | 2598 | 2581 | −17 |
| Dup groups / merges | 17 / 0 | 17 / 0 | 0 |
| Oversized | 326 | 330 | +4 |
| Stale >90d | 2491 | 2558 | +67 |
| Tag violations | 0 | 0 | 0 |

Graph is stable; new orphans track new-page creation 1:1.

## Generator bug backlog (open, do not re-discover)

1. Index reconciliation should resolve `foo/_index.md` → slug `foo`, skip `_archive/`.
2. Dup detector should skip `redirect:`-frontmatter and `index`/`_index` slugs (all 17
   groups this week were already-handled/false-positive/legit-split).
3. Report rotation deletes last week's file but leaves dangling index.md entries.

## Actions taken this run

- Replaced dangling 2026-11-06 index entries with today's report + annotations.
- Appended log.md entry. No page merges (0 needed), no tag fixes (0 violations).
