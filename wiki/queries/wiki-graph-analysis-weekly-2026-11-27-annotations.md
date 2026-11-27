---
title: Weekly Wiki Graph Analysis — Adjudicated Annotations
created: 2026-11-27
updated: 2026-11-27
type: query
tags: [wiki]
sources:
  - queries/wiki-graph-analysis-weekly-2026-11-27.md
---

# Weekly Graph Analysis — Adjudicated Annotations (2026-11-27)

Companion to `queries/wiki-graph-analysis-weekly-2026-11-27.md`. Raw report numbers are
adjudicated below with an independent recursive resolver + direct page reads. No wiki
mutations were made this run except report/annotations/index/log bookkeeping.

## WoW trend (deep-audit ground truth)

| Metric | 11-13 | 11-27 | Δ |
|---|---|---|---|
| L2 pages | 3,456 | 3,541 | +85 |
| Orphans | 460 | 493 | +33 |
| Broken links (raw) | 2,581 | 3,574 | +993 |
| Dup groups | 17 | 17 | 0 (same set) |
| Oversized | 330 | 335 | +5 |
| Stale (>90d) | 2,558 | 2,566 | +8 (baseline drift) |
| Tag violations | 0 | 0 | 0 |

Page growth +85 in 2 weeks. Orphan growth (+33) tracks new-page creation — stable graph.
Broken-link jump is mostly generator counting (see below), not a real regression.

## 1. Duplicate groups — verdict table (17 groups, 0 merges)

Measured `wc -l` + redirect frontmatter THIS session.

| Group | Verdict | Evidence |
|---|---|---|
| eugeneyan / eugene-yan | ✅ handled | eugeneyan=11L `redirect: "eugene-yan"` |
| giles-thomas / gilesthomas | ✅ handled | giles-thomas=11L `redirect: "gilesthomas"` (228L) |
| lilianweng / lilian-weng | ✅ handled | lilianweng=11L `redirect: "lilian-weng"` |
| martin-fowler / martinfowler | ✅ handled | martin-fowler=17L `redirect: "[[entities/martinfowler]]"` |
| samuelcolvin / samuel-colvin | ✅ handled | samuelcolvin=14L `redirect: samuel-colvin` |
| nvidia-openshell | ✅ handled | concepts side=43L `redirect:` to entity |
| alpha-proof-nexus / alphaproof-nexus | ✅ handled | alphaproof-nexus=39L `redirect:` |
| deer-flow / deerflow | ✅ handled | deerflow=45L `redirect: deer-flow` |
| dspyrlm / dspy-rlm | ✅ handled | dspyrlm=18L `status: redirect` (keep 697L dspy-rlm) |
| llm-integration-patterns | ✅ handled | concepts side=18L `status: redirect` (keep 273L comparison) |
| open-claw-ecosystem / openclaw-ecosystem | ✅ handled | concepts/open-claw-ecosystem=18L `status: redirect` |
| cline (entities/concepts) | ✅ legit split | mutual cross-links present (10/7 refs) |
| qwen (entities/concepts) | ✅ legit split | mutual cross-links present (26/5) |
| omnara (entities/concepts) | ✅ legit split | mutual cross-links present (8/4) |
| agent-harnesses (concepts/comparisons) | ✅ legit split | mutual cross-links (2/7) |
| _index pair | ❌ false positive | different namespaces |
| deliberate-coder / deliberatecoder | ❌ false positive | DIFFERENT PEOPLE (Ben Ilegbodu vs Steve Shogren) |

**Action: none.** Same 17-group ledger as 11-13/11-20; all either redirect stubs, verified
legit namespace splits, or known false positives.

## 2. Index reconciliation — real gaps

Generator reported "17 not indexed / 29 not on disk". Independent resolver (dir-hub aware):

- **Not-indexed (real): 0.** Loose-basename resolver finds all concepts pages reachable from index.
- **Missing-on-disk (real): 2 + 1 ambiguous:**
  - `queries/wiki-graph-analysis-weekly-2026-11-20` + `-annotations` — deleted by report rotation;
    fixed by this run's index swap (contiguous dangling lines → today's report + annotations).
  - `concepts/training` — index links a dir-hub with NO `index.md`/`_index.md` (contains only `trl.md`).
    Candidate: either fold `concepts/training/trl` reference elsewhere or create the hub. Low priority.
  - `concepts/browser-agent` — dir exists with content pages but no index.md → **needs hub page** (or
    child links in parent index). 1 entry, low priority.
  - `concepts/gpt/_archive/...` — correctly excluded from disk scan; index cleanup candidate only.

## 3. Broken links — interpretation

Raw 3,574 is inflated vs the 11-13 deep-audit number (2,581) because the generator counts bare
and namespaced missing targets separately and does not do a nested `endswith('/'+base)` resolution
pass. Real signals that survive nested resolution:

- **Empty `[[]]` links: essentially resolved.** Only 1 stray occurrence remains outside raw/ (in
  log.md itself) vs the 47–278 backlog flagged since 2026-08 — the sibling watchdog pipeline
  appears to have drained this queue. **Downgrade the standing "needs human review (1)" item.**
- **Persistent missing-page queue (4+ weeks, escalate):** `entities/cursor` (14 refs),
  `concepts/claude-opus-4-7` (10 refs), `concepts/intelligence-explosion` (8 refs, zero resolvable
  targets). Previously suggested `entities/huggingface`, `entities/ben-clavie` also still uncreated.
- **Borderline hub candidates (covered by child pages, no action needed):** enterprise-ai,
  ai-adoption, agent-architecture, agent-framework, ai-coding, inference-optimization, world-models,
  ai-governance — each has 2+ topical child pages; the bare targets are dangling shorthand.
- **Top fixable queue:** 150 bare→namespaced / cross-namespace auto-fixes — route to
  `wiki-health-fix` (17:50 UTC daily job); do not hand-fix in this cron.

## 4. Orphans (493, +33 WoW)

Growth is 1:1 with new-page creation; not a structural regression. Top content-rich orphans
worth connecting first (high value, cheap inbound-link fixes):
`concepts/multi-objective-policy-distillation`, `concepts/symphony`, `concepts/ai-benchmarks/skillspector`,
`comparisons/codex-app-server-vs-claude-agent-sdk`, `concepts/reasoning-trace-extraction-vulnerability`.
10 skeleton orphans remain (skeleton-enrich-daily covers these).

## 5. Other

- Stale 2,566 (+8): near-static bulk-import baseline; no action.
- Oversized 335 (+5): no urgency; largest actionable = `concepts/agentic-search` (1,212L),
  `entities/harvey` (1,133L) per 200-line SCHEMA rule.
- Tag violations: 0 (report + tag_audit agree).

## Recommendations (prioritized)

1. **Escalate missing-page queue** — 4–5 pages with 8+ refs unresolved for 4+ weeks:
   `entities/cursor`, `concepts/claude-opus-4-7`, `concepts/intelligence-explosion`,
   `entities/huggingface`, `entities/ben-clavie`. Route to skeleton-enrich or active-crawl.
2. **Create 2 dir-hub index pages**: `concepts/browser-agent/index.md`, `concepts/training/index.md`
   (or fold children into parent index) — clears 2 of the 4 real index gaps.
3. **Close the empty-`[[]]` review item** — backlog appears drained (278→1).
4. Defer the 150 auto-fixable links to the daily `wiki-health-fix` job.
5. No duplicate merges, no index deletions, no stale-page actions this run.
