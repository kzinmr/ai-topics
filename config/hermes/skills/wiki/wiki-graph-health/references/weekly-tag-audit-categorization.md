# Weekly Tag Audit: Result Categorization

When `tag_audit.py` produces a report with 1000+ non-SCHEMA tags, the raw number is
misleading. Most are one-off tags from rare pages. This reference helps the agent
categorize results into actionable buckets.

## Step 1: Separate Scan Scope from Real Drift

The `tag_audit.py` scan includes ALL directories under wiki/ including raw/ and queries/.
Run a **targeted scan** that excludes transient directories for an apples-to-apples count:

```python
import os, re
from collections import Counter

wiki = os.path.expanduser("~/ai-topics/wiki")
tag_counter = Counter()

for root, dirs, files in os.walk(wiki):
    rel = os.path.relpath(root, wiki)
    if rel.startswith(('.git', 'raw', 'queries', '_archive')):
        continue
    for f in files:
        if not f.endswith('.md') or f in ('index.md', 'log.md', 'log-2026.md', '_index.md', 'SCHEMA.md'):
            continue
        path = os.path.join(root, f)
        content = open(path).read()
        m = re.search(r'^tags:\s*\n((?:  - .+\n)*)', content, re.MULTILINE)
        if m:
            for line in m.group(1).split('\n'):
                line = line.strip()
                if line.startswith('- '):
                    tag = line[2:].strip().strip('"').strip("'")
                    if tag:
                        tag_counter[tag] += 1
```

## Step 2: Categorize Non-SCHEMA Tags

After loading valid tags from SCHEMA.md (see tag_audit.py's `load_valid_tags()`), categorize each non-SCHEMA tag:

| Usage Bucket | Count | Action |
|---|---|---|
| **≥10 uses** 🔥 | ~0-2 | Almost certainly belongs in SCHEMA.md |
| **5-9 uses** HIGH | ~5-15 | Add to SCHEMA.md taxonomy directly |
| **3-4 uses** MEDIUM | ~20-50 | Classify as "add to SCHEMA" vs "map via normalization" vs "entity-name" |
| **<3 uses** LOW | ~900-1000 | Mostly page-specific noise. Log total count, don't act. |

### Classification Rules for MEDIUM (3-4 uses)

| Type | Examples | Action |
|---|---|---|
| **Legitimate domain category** | `ai-benchmarks`, `agentic-rag`, `model-compression` | Add to SCHEMA.md |
| **Entity/company name** | `sierra`, `every-inc`, `searchcode` | Map via normalization: `sierra → company`, `every-inc → company` |
| **Broad synonym** | `programming → developer-tooling`, `deployment → devops`, `vision → multimodal` | Map via normalization |
| **Specific tool/method** | `lm-eval → evaluation`, `claude-mythos → anthropic` | Map via normalization |
| **Person-role tag** | `python-developer → developer-tooling`, `developer → developer-tooling` | Map via normalization |

## Step 3: Verify the `related:` Field Confusion

The grep pattern `^  - [[` matches BOTH `tags:` entries AND `related:` entries. If
running ad-hoc grep analysis, always check whether matched lines are under `tags:`
or under `related:` by looking at the file's frontmatter. The `tag_audit.py` script
only looks at the `tags:` YAML key, so it's immune to this confusion, but custom
analysis scripts may not be.

## Step 4: Check Pre-Commit Hook Effectiveness

Compare composite kebab counts from previous week vs current week. The hook blocks
new ones at commit time, so the trend should be:
- **Week 1**: 16 found → manual cleanup
- **Week 2**: 0 found → hook is working (verify this each week)

If composite kebab reappears (>0), the hook may have been deactivated:
```bash
cd ~/ai-topics && git config core.hooksPath .githooks && git config core.hooksPath
# Should output: .githooks
```

## Step 5: Suggest tag_normalization.py Run

If ≥10 frequent non-SCHEMA tags (≥3 uses) exist AND the tag_normalization.py
TAG_NORMALIZATION dict has mappings for most of them, recommend running:
```bash
python3 /opt/data/.hermes/skills/wiki/wiki-graph-health/scripts/tag_normalization.py --dry-run
# Review, then:
python3 /opt/data/.hermes/skills/wiki/wiki-graph-health/scripts/tag_normalization.py
```

If the dict is MISSING mappings for 5+ frequent tags, add them first (see `scripts/tag_normalization.py`
`TAG_NORMALIZATION` dict), then run.

## Worked Example (2026-05-11)

```python
# SCHEMA.md valid tags: 219
# Total unique tags in use: 1198
# Tags in SCHEMA: 167 (14%)
# Tags NOT in SCHEMA: 1031

# Breakdown:
#   Composite kebab errors: 0 (down from 16)
#   HIGH (5-9 uses): 5 tags → add to SCHEMA
#   MEDIUM (3-4 uses): 36 tags → 15 add to SCHEMA, 12 map via normalization, 9 skip (entity names or too specific)
#   LOW (<3 uses): 990 tags → noise, ignore
#   tag_normalization.py run recommended: YES (41 >= 10)
```
