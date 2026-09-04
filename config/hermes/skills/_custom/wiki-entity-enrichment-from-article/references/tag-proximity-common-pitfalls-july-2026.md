# Tag Proximity Common Pitfalls — Additional Mappings

Discovered during x-bookmarks-ingest cron run (July 2026): 8 tag violations across 5 new wiki pages. These extend the existing tag proximity trap table in the main SKILL.md.

### New Mappings

| Invented tag | Correct SCHEMA.md tag(s) | Notes |
|---|---|---|
| `hybrid-search` | `lexical-search` + `vector-search` + `bm25` + `neural-reranking` | SCHEMA.md covers all hybrid retrieval components individually; combine them |
| `growth` | `devrel` | No standalone `growth` tag; `devrel` under "Engineering" |
| `developer-relations` | `devrel` | SCHEMA.md uses the shorter `devrel` |
| `ml-engineer` | `ml-engineering` | SCHEMA.md uses `ml-engineering` (Engineering category) |
| `metadata` | `metadata-retrieval` or omit | No bare `metadata` tag; use domain-specific variant or drop entirely |
| `qualcomm` | Not in SCHEMA — drop | Company tags only exist for orgs with multiple wiki mentions; omit |

### Pre-Commit Tag Check (Proactive Pattern)

After creating/enriching multiple pages in a cron run, run this BEFORE the first commit attempt to catch tag violations proactively rather than after the pre-commit hook blocks you:

```bash
# Extract all tags from staged wiki pages
grep -h "^tags:" wiki/concepts/*.md wiki/entities/*.md | \
  grep -oP '(?<=\[)[^\]]+' | tr ',' '\n' | sed 's/^ *//;s/ *$//' | sort -u > /tmp/all_tags.txt

# Extract all canonical tags from SCHEMA.md
grep -oP '(?<=`)[a-z][a-z-]*(?=`)' wiki/SCHEMA.md | sort -u > /tmp/schema_tags.txt

# Find tags in pages but not in SCHEMA.md
comm -23 /tmp/all_tags.txt /tmp/schema_tags.txt
```

If output is non-empty, those tags need:
1. Adding to SCHEMA.md (if they're valid new categories), OR
2. Replacing with existing canonical tags (see mapping table above), OR
3. Dropping entirely (if no equivalent exists)

This saves 2-3 rounds of commit-fix loops per ingestion batch.
