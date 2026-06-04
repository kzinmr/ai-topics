# Tag Taxonomy Pitfalls — Pre-Commit Hook Reference

When editing any wiki page (entity, concept, comparison, event, query), the `pre-commit` hook in `ai-topics/.githooks/pre-commit-tag-validator.py` blocks commits that contain tags not registered in `wiki/SCHEMA.md`'s canonical taxonomy.

## The Hook

Hook path: `ai-topics/.githooks/pre-commit`
Validator: `ai-topics/.githooks/pre-commit-tag-validator.py`
Taxonomy source: `wiki/SCHEMA.md`

On commit, the hook:
1. Scans all staged `.md` files in `wiki/` for YAML frontmatter `tags:`
2. Validates each tag against the canonical list in SCHEMA.md
3. Prints a detailed error listing: file path, invalid tag name
4. Blocks the commit (exit code 1) if any violation found

## Prevention Checklist

**Before every `git commit` that modifies wiki pages:**

1. **Identify all new tags** you added to page frontmatter
2. **Search SCHEMA.md** for each tag: `search_files(pattern="tagname", path="wiki/SCHEMA.md")`
3. **If tag is missing**, add it to the appropriate category:

| Category | Examples | Common new additions |
|---|---|---|
| Products | tool, platform, service, framework, product | `openrouter`, new IDE/tool names |
| People/Orgs | company, lab, anthropic, openai | `siliconflow`, new company names |
| Models | model, llm, moe, text-generation | New model family names |
| Techniques | prompting, rag, kv-cache, fine-tuning | New technique names |
| AI Agents | ai-agents, coding-agents, agent-safety | New agent-related concepts |
| Infrastructure | cloud, gpu, security, architecture | New infra technologies |

4. **Add missing tags** to SCHEMA.md, preserving the comma-separated format
5. **Verify placement**: SCHEMA.md categories are long comma-separated lines — `patch` fuzzy matching has been known to insert tags into the WRONG category. Re-read the line after editing.
6. **Stage both files**: `git add wiki/SCHEMA.md` alongside your page changes

## When the Hook Blocks Your Commit

The error output is precise. Example:

```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (1):
   wiki/entities/tencent-hy3.md:  openrouter

   Fix options:
   1. Add 'openrouter' to SCHEMA.md taxonomy
   2. Map it to an existing canonical tag
   3. Use an existing SCHEMA tag instead
```

**Response**: Add `openrouter` to the Products category in SCHEMA.md, `git add`, retry commit.

## Common Patterns

### New Product/Platform Name
```markdown
# In SCHEMA.md, Products line:
..., obsidian, openrouter

# In page frontmatter:
tags: [entity, model, llm, openrouter, ...]
```

### New Company/Lab
```markdown
# In SCHEMA.md, People/Orgs line:
..., mit, palantir, tencent, siliconflow

# In page frontmatter:
tags: [entity, company, llm-proxy, siliconflow, ...]
```

### Pricing-related Tag for Models
The `pricing` tag already exists in SCHEMA.md under Products. Use it directly — no SCHEMA.md change needed.

## Historical Incidents

- **2026-05-27**: Agent added `openrouter` tag to `entities/tencent-hy3.md` without registering it in SCHEMA.md. Pre-commit hook blocked commit. Fixed by adding `openrouter` to Products category.
- **2026-05-13 (batch-person-entity)**: Tags `researcher` and `pseudonymous` added to person pages without SCHEMA.md registration. Hook blocked commit. Also: `llm-proxy` was inserted into Engineering AND Infrastructure categories due to `patch` fuzzy matching on long lines.
