# Redirect-Stub Orphan False Positives (health-fix session 2026-10-28)

## Pattern
`wiki_health.py` digest reports orphan pages not in index.md (e.g. `entities/eugeneyan`, `entities/giles-thomas`, `entities/lilianweng`). Live check shows each is an 11-line stub:

```yaml
status: redirect
redirect: "<canonical-slug>"
```

created by a **same-day watchdog entity-dedup commit** (commit message pattern: `watchdog: entity dedup — X/Y/Z intentionally converted to redirects ... index dedup + header recount`).

## Verification recipe (do this BEFORE any index/delete action)
1. `cat wiki/entities/<slug>.md` — confirm `status: redirect` + tiny file (`wc -l` ≈ 11).
2. `git log --oneline -3 -- wiki/entities/<slug>.md` — confirm a recent watchdog dedup commit created the stub deliberately.
3. Canonical target check: `ls wiki/entities/<canonical>.md` exists AND `grep -n "\[\[entities/<canonical>\]\]" wiki/index.md` has at least 1 line.
4. Incoming-link check: `grep -rln '\[\[entities/<slug>\]\]' wiki/ --include='*.md' | grep -v raw/` — if empty, nothing links to the stub.

## Decision
If all four pass → **false positive; take NO file action**. Do not register the stub in index.md (the digest's orphan scanner just doesn't recognize redirect stubs), do not delete it (it preserves the old slug as a redirect target for legacy links). Record the verdict in a log.md entry so the next run doesn't re-litigate.

## Other same-session notes
- Digest claims can lag behind the live wiki: a later watchdog job may have already fixed reported issues (this session: 36 broken wikilinks fixed by watchdog commit 34ffd503 before the health-fix run). Always re-verify digest claims with live grep before acting (see Watchdog Pipeline Timing section).
- If `git pull --rebase` fails with unstaged changes from sibling pipelines (skills WIP, uncommitted raw newsletters), do NOT stash/reset them — the health-fix job can still commit its own log.md entry scoped via `git add wiki/log.md` only.
- `validate_index.py` clean + 0 corruption in Python scan = no-op run; report table with all zeros + COST_REPORT, commit only log.md.
- SKILL.md size: wiki-graph-health SKILL.md is at ~100.5K chars (over the 100K edit limit as of 2026-10-28) — skill_manage patch on SKILL.md fails with "limit: 100,000". Put new knowledge in references/ files instead; the curator should split SKILL.md.
