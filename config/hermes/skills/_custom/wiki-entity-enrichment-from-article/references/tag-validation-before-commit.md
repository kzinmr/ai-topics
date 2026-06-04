# Tag Validation Before Commit

## The Problem

The wiki's git pre-commit hook (`ai-topics/.githooks/pre-commit`) validates **every frontmatter `tags` field** against `wiki/SCHEMA.md`'s canonical 375-tag taxonomy. Non-canonical tags **block the commit entirely**. This is the single most frequent commit failure when creating or updating wiki pages.

## The Fix: Always Check SCHEMA.md First

**Before writing any frontmatter with `tags`**, use `search_files` to find canonical equivalents:

```
search_files pattern="desired-tag" target="content" path="wiki/SCHEMA.md"
```

## Common Non-Canonical → Canonical Mappings

| You wrote | Canonical tag | Notes |
|-----------|--------------|-------|
| `prompt-engineering` | `prompting` | The canonical term in Techniques |
| `claude` | `anthropic` | Company tags are organization-level |
| `token-efficiency` | *remove* | No canonical equivalent exists |
| `deep-research-system` | `deep-research` | Use existing if close enough |
| `agent-framework` | `agent-framework` | Exists in AI Agents taxonomy |

## Procedure When Writing Frontmatter

1. Draft your tags
2. For each tag, run `search_files pattern="tagname" target="content" path="wiki/SCHEMA.md"`
3. If tag not found → check for close matches or synonyms
4. If genuinely new concept needs a new tag → **add it to SCHEMA.md first**, then use it
5. Then write the page

## Recovery if Commit is Blocked

```
# Option 1: Fix tags to use canonical equivalents
patch path="wiki/concepts/your-page.md" old_string="prompt-engineering" new_string="prompting"

# Option 2: Add the tag to SCHEMA.md (only for genuinely new concepts)
# Edit wiki/SCHEMA.md to add the tag to appropriate category

# Then re-add and commit
git add wiki/ && git commit -m "..." && git push
```
