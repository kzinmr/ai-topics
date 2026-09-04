# Stale Page Count Inflation in `wiki_health.py` Output

## Discovery
**Date**: 2026-07-15 — confirmed during `wiki-health-fix` cron run.

## Symptom
The human-readable health digest reports a stale page count that is **10-12x higher** than the real value when verified independently.

| Source | Claimed stale | Verified stale | Ratio |
|--------|---------------|----------------|-------|
| 2026-07-15 | 1,627 / 2,772 (59%) | 138 / 2,772 (5%) | ~12x |

## Root Cause
The health script's stale detection uses a broad filesystem walk that likely includes `raw/articles/`, `transcripts/`, and other non-Layer-2 content when counting "stale pages." However the "Total Layer 2 pages" header only counts `entities/` + `concepts/` + `comparisons/`. The numerator and denominator come from different scan scopes, producing a misleading percentage.

## Verification Procedure
Always run an independent stale scan before acting on the health digest's number:

```python
import os, time
wiki = "wiki"
now = time.time()
stale = []
for root, dirs, files in os.walk(wiki):
    if "/raw/" in root or "/_archive/" in root:
        continue
    for f in files:
        if not f.endswith(".md"): continue
        if f in ("_index.md",): continue
        path = os.path.join(root, f)
        age = (now - os.path.getmtime(path)) / 86400
        if age > 30:
            stale.append((age, path))
print(f"Real stale count: {len(stale)}")
for age, path in sorted(stale, reverse=True)[:5]:
    print(f"  {age:.0f}d  {path}")
```

## Expected Behavior
- If health digest claims 1,000+ stale but independent scan shows <200 → stale number is inflated. Report the real number.
- If health digest and independent scan agree → stale is real and needs remediation.

## Affected Metrics
- Stale page count in the health digest overview
- Any downstream pipelines that gate on stale count (skeleton-enrich, dream-cycle prioritization)

## Related
- `references/watchdog-healthy-baseline.md` — full verification checklist
