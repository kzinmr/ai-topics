# Wiki Health Audit Patterns

Learned patterns from large-scale wiki health audits (1000+ pages).

## Key Metrics at Scale

| Metric | 1500-page wiki baseline | Action needed |
|--------|------------------------|---------------|
| Broken wikilinks | ~170 | High - fix genuinely missing targets |
| Invalid tags | ~470 (30%+ of usage) | Medium - taxonomy expansion + decomposition |
| Oversized pages | ~100 | Low - split only if >400 lines |
| Missing frontmatter | ~3 | Low - quick fix |
| Orphan pages | ~2 | Low - add to index |
| Index count drift | 795 reported vs 1539 actual | Medium - update header |

## Tag Taxonomy Drift Patterns

### Always-Error Tags (Composite Kebab-CASE)
These are single tags containing multiple words joined by hyphens. **Always decompose:**
- `cognition-devin-memory-tool-claude-code-competitive-analysis` → `memory`, `context-management`, `competitive-analysis`
- `background-agent-orchestration-linear-github-workflow-automation-graph-based` → `agent-orchestration`, `github`, `automation`
- `llm-output-formatting-json-pydantic-reliability-type-safety-function-calling` → `structured-output`, `pydantic`, `function-calling`
- `ai-safety-alignment-rlhf-scalable-oversight-interpretability` → `alignment`, `rlhf`, `interpretability`

**Detection regex:** `tags:\s*\[.*[a-z]+-[a-z]+-[a-z]+-[a-z]+-[a-z]+.*\]` (5+ hyphenated words)

### Legitimate Tags Not in Taxonomy
Common additions needed for AI/ML wiki:
- **Orgs/Platforms**: `microsoft`, `google`, `openai`, `anthropic`, `github`, `telegram`, `raspberry-pi`
- **Concepts**: `long-context`, `human-in-the-loop`, `privacy`, `enterprise`, `cloud`, `cli`, `debugging`, `monitoring`
- **Technical**: `neurosymbolic`, `vision-language`, `moe`, `token-efficiency`, `fault-tolerance`

### Tag Cleanup Strategy
1. **Decompose** composite kebab-case tags (always errors)
2. **Add** frequent legitimate tags to SCHEMA.md taxonomy
3. **Remove** tags used <3 times unless conceptually important
4. **Target**: <50 unique canonical tags for 500-2000 page wiki

## Index Health Patterns

### Common Discrepancies
- `Total pages: N` in header becomes stale within days of active ingest
- Section counts (Entities/Concepts) are rarely updated
- Pages created by scripts (`build_x_wiki.py`, `build_blog_wiki.py`) often skip index updates
- Subdirectory pages (`concepts/harness-engineering/...`) may not be counted

### Auto-Correction Script
```python
# Quick index count verification
import os
wiki = "~/ai-topics/wiki"
actual = sum(1 for r, d, f in os.walk(wiki) 
             if not any(s in r for s in ['raw', '.git', '_archive'])
             for fn in f if fn.endswith('.md') and fn not in ['SCHEMA.md', 'index.md', 'log.md'])
# Compare with index.md header
with open(f"{wiki}/index.md") as f:
    header_count = int(re.search(r'Total pages:\s*(\d+)', f.read()).group(1))
print(f"Discrepancy: {actual - header_count} pages unaccounted")
```

## Case Sensitivity Issues

### Common Patterns
- `[[concepts/mooncake]]` → file is `concepts/Mooncake.md` (capital M)
- `[[entities/OpenAI]]` → file is `entities/openai.md` (lowercase)
- Linux filesystems are case-sensitive; macOS may mask this locally

### Detection
```python
import os
wiki = "~/ai-topics/wiki"
# Find all wikilinks and their targets
links = re.findall(r'\[\[([^\]|]+)', content)
for link in links:
    target = link.strip()
    # Check exact match
    if not os.path.exists(os.path.join(wiki, target + '.md')):
        # Check case-insensitive
        base = os.path.basename(target)
        for root, dirs, files in os.walk(os.path.join(wiki, os.path.dirname(target))):
            for f in files:
                if f.lower() == base.lower() + '.md':
                    print(f"Case mismatch: {target} -> {f}")
```

## _index.md Special Handling

### Why They're Different
- Serve as synthesis hubs for subdirectories
- May lack full frontmatter (legitimate)
- Often exceed 200 lines (by design)
- Should be excluded from standard lint checks

### Recommended Frontmatter
```yaml
---
title: "Topic Synthesis"
type: index
status: synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [synthesis, overview]
---
```

## Raw Articles Reference Links

Links like `[[raw/articles/2026-04-daniel-miessler...]]` are **valid source references**, not broken links. These point to immutable source material in Layer 1 of the wiki architecture.

### Detection
```python
# These are valid - don't flag as broken
valid_source_patterns = ['raw/articles/', 'raw/papers/', 'raw/transcripts/']
if any(link.startswith(p) for p in valid_source_patterns):
    continue  # Skip - this is a source reference
```

## Health Check Workflow

1. **Run scan** → collect all metrics
2. **Filter false positives** → raw/articles/, _index.md, case variants
3. **Fix critical** → genuinely broken wikilinks, missing frontmatter
4. **Address warnings** → tag taxonomy, index counts, case sensitivity
5. **Document changes** → update log.md, commit

## Automation Candidates

- `scripts/tag_audit.py` → scan all tags, flag composites, suggest taxonomy additions
- `scripts/index_sync.py` → compare filesystem vs index.md counts, auto-update
- `scripts/case_fix.py` → find and fix case mismatches in wikilinks
