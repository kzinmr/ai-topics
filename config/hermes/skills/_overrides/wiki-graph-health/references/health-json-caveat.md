# `wiki_health.py --json` Output Caveat

The `--json` output of `wiki_health.py` **does not contain an `index_corruption` field**. It was removed during the 0.28s optimization (2026-05-13) when content-validation breadth was traded for speed.

## What `--json` actually returns

```json
{
  "date": "2026-06-28",
  "overview": { "entities": 838, "concepts": 1845, "comparisons": 31, "raw_articles": 7601, "total_l2": 2714, "skeleton_entities": 0 },
  "page_name_policy": { "violations": [], "error_count": 0, "warn_count": 0 },
  "orphan_count": 2556,
  "orphans": ["comparisons/llm-api-pricing", "..."]
}
```

Only four keys: `date`, `overview`, `page_name_policy`, `orphan_count`, `orphans`.

## How to detect index corruption

Use live shell commands instead:

```bash
python3 -c "
import re
lines=open('wiki/index.md').readlines()
print('Pipe prefix:', sum(1 for l in lines if re.match(r'^\\|-\$', l)))
print('Line# prefixed:', sum(1 for l in lines if re.match(r'^\s*\d+\|', l)))
print('Triple brackets [[[ :', open('wiki/index.md').read().count('[[['))
print('Space prefix:', sum(1 for l in lines if re.match(r'^ - \[\[', l)))
"
python3 scripts/validate_index.py
```

## Why this matters

The `wiki-health-fix` cron job's Phase 1 instructions reference `index_corruption.issues` which does not exist in the JSON. Always skip the JSON corruption check and go straight to live verification. The pre-run JSON is useful only for `page_name_policy` violations, orphan counting, and overview stats.
