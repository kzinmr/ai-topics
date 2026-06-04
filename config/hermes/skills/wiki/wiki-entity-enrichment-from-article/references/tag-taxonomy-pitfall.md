# Tag Taxonomy Validation Pitfall

## Problem

The pre-commit hook (`pre-commit-tag-validator.py`) blocks commits containing tags not in `wiki/SCHEMA.md`. New entity pages commonly trip this when using descriptive tags that seem natural but aren't in the canonical taxonomy.

## Common Non-Canonical → Canonical Mappings

| Non-Canonical (BLOCKED) | Canonical (SCHEMA.md) |
|--------------------------|----------------------|
| `ai-researcher` | `researcher` |
| `cli-design` | `cli` |
| `chinese-ai` | `china` |
| `ai-engineer` | `engineer` |
| `devtools` | `developer-tooling` |
| `ai-coding` | `ai-coding` (exists) |
| `agent-design` | `agent-design-patterns` or split into `agent-architecture` + `design-patterns` |
| `ml-researcher` | `researcher` |
| `web-developer` | `web-development` |
| `javascript` | `web-development` or `programming-language` |
| `accessibility` | omit — no SCHEMA equivalent; if essential, add to SCHEMA.md first |

## Prevention

Before writing frontmatter, verify tags exist in SCHEMA.md:

```bash
grep -w "tag-name" ~/wiki/SCHEMA.md
```

Or check all tags at once:

```bash
for tag in tag1 tag2 tag3; do
  grep -q "\b$tag\b" ~/wiki/SCHEMA.md || echo "MISSING: $tag"
done
```

## Recovery (when commit is blocked)

1. Read the error output — it lists the violating tags and their source files
2. Map each non-canonical tag to the nearest SCHEMA.md canonical tag
3. Use `patch()` to replace tags in the affected frontmatter
4. Re-commit

## When a new tag is genuinely needed

Add it to `wiki/SCHEMA.md` first, then use it. The SCHEMA.md has categorized tag lists — add the new tag to the appropriate section.
