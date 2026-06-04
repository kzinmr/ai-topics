# Tag Taxonomy Validation Pitfall

## The Problem

When creating or updating wiki pages, the Git pre-commit hook (`.githooks/pre-commit`) runs a tag taxonomy validator. If any page uses a tag **not listed in `wiki/SCHEMA.md`'s canonical taxonomy**, the commit is **blocked**.

Error message:
```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (N):
   wiki/path/to/page.md:  non-canonical-tag
```

## Common Violations

### 1. Plural vs Singular Mismatch
SCHEMA.md uses **singular** for some tags:
- ✅ `model` — NOT `models`
- ✅ `framework` — NOT `frameworks`

The skill guideline says "Prefer plural forms" but SCHEMA.md's actual tags may be singular. Always check SCHEMA.md.

### 2. Using descriptive tags not in taxonomy
Tags like `localization`, `honesty`, `funding` may feel natural but don't exist in SCHEMA.md. Use existing closest matches:
- `localization` → `translation`
- `honesty` → remove (or use `ai-safety`)
- `funding` → `vc`
- `models` → `model`

### 3. Forgetting to add to SCHEMA.md first
If a genuinely new tag is needed, **add it to `wiki/SCHEMA.md` first**, then use it in pages. The taxonomy must be updated before the page is committed.

## Prevention Checklist

Before committing wiki changes:
1. ❓ Did I use any tag not in SCHEMA.md?
2. ❓ Did I check singular/plural forms against the taxonomy?
3. ❓ If I need a new tag, did I add it to SCHEMA.md first?

## Quick Fix

```bash
# Check which tags will violate (if pre-commit hook exists)
cd ~/ai-topics
grep "^tags:" wiki/entities/*.md wiki/concepts/*.md | \
  grep -oP '[\w-]+(?=[,\]\s])' | sort -u > /tmp/page_tags.txt
grep -oP '^- `[\w-]+`' wiki/SCHEMA.md | sed 's/- `//;s/`//' | sort -u > /tmp/schema_tags.txt
comm -23 /tmp/page_tags.txt /tmp/schema_tags.txt
```

If blocked, fix tags then: `git add wiki/ && git commit ...`
