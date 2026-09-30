# X/Twitter bookmarks & account-posts scan — 2026-09-30

Sources: `xurl bookmarks -n 80` (deduped against processed bookmarks), cross-checked
against existing wiki coverage.

## Summary

**No new wiki-worthy articles.** All 80 bookmarked tweets resolve to material that is
already ingested or represented in the wiki. 0 new raw articles saved, 0 new/updated
wiki pages required (only this scan report).

## Findings

### Previously ingested (dedup hits — 3)
| Date | Item | Existing coverage |
|---|---|---|
| 2026-07-29 | Unsloth — "Kimi K3 can now be run locally" (1-bit Dynamic GGUF, 1.56TB→594GB, ~78.9% accuracy, Mac Studio + 128GB RAM) | `raw/articles/2026-07-29_unsloth_kimi-k3-local-inference.md`, [[concepts/kimi-k3]] "Local Inference" section, [[concepts/unsloth]] |
| 2026-08-02 | @wafer_ai — Kimi K3 on single 8×AMD MI355X node (952 tok/s total vs 16×B200 across two NVIDIA servers) | `raw/articles/2026-08-01_wafer-ai_kimi-k3-amd-mi355x-serving-benchmark.md`, [[entities/wafer-ai]], [[entities/amd]] |
| 2026-07-12 | Prime Intellect — verifiers v1 release (taskset / harness / runtime decomposition) | `raw/articles/2026-07-12_primeintellect_verifiers-v1.md`, [[entities/prime-intellect]] |

### Already represented, no new content to add
- **Qwen-MM-Plugins launch** (2026-08-10) — [[entities/qwen-mm-plugins]] exists with full capability table (core, video-memory, video-edit, blender, FreeCAD, edu-agent).
- **Meta open-weight release discussion** (2026-08-11, "first open-weight since the Llama days") — covered by [[entities/meta]] Open Source History / MSL sections.

### Not wiki-worthy
Remaining ~75 bookmarks are pre-dedup-window items already processed in prior runs
(context-engineering, harness, RLM, agentic-RL, tooling articles already in
[[concepts/...]] / [[entities/...]] pages).

## Decisions
- No entity/concept enrichment warranted: the three dedup-hit items each already carry
  the exact metrics from the tweets (594GB/78.9%; 952 tok/s; taskset-harness-runtime).
- No new SCHEMA.md tags needed. No index.md/log.md page changes required.

## Caveat
`xurl /2/timelines/home.json` (24h home timeline pull) returned an empty/error
response, so this run relied on bookmarks only. Account-posts dedup ledger
(`~/.hermes/processed_x_accounts.json`) shows the x-accounts-scan job (last run
2-day cadence) covers tracked accounts separately.
