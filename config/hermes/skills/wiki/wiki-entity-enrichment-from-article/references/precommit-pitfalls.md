# Pre-Commit Hook Pitfalls for Wiki Ingestion

> Common commit failures and their fixes when ingesting articles/papers into the wiki.

## 1. Tag Taxonomy Violations

**What it looks like:**
```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (N):
   wiki/concepts/some-page.md:  new-tag-name
```

**Root cause**: Tags in page frontmatter must exist in `wiki/SCHEMA.md` tag taxonomy.

**Fix — Option A (PREFERRED): Map to existing canonical tags.** Many non-canonical tags have close equivalents already in SCHEMA.md. Replacing them avoids taxonomy bloat and is faster than editing SCHEMA.md. Examples:

| Offending Tag | Canonical Replacement | Why |
|---|---|---|
| `model-training` | `model` + `training` | SCHEMA has both separately |
| `ai-researcher` | `researcher` | `researcher` exists in People/Orgs |
| `production-ml` | _(remove)_ | Covered by `reinforcement-learning` + `coding-agents` context; no unique concept |
| `online-learning` | `continual-learning` (alias) or `training` | Check if a close alias exists first |
| `scaling-laws` | `scaling` | SCHEMA has `scaling` (not `scaling-laws`) |
| `pre-training` | `training` | SCHEMA has `training`; `pre-training` is not a tag |
| `data-curation` | `datasets` or `synthetic-data` | SCHEMA has `datasets` and `synthetic-data` but not `data-curation` |

**Rule of thumb**: Before adding a new tag, search SCHEMA.md for partial matches. `model-training` → try `model`, `training`. `ai-researcher` → try `researcher`. If a canonical tag covers 80%+ of the meaning, use it. Only add to SCHEMA.md when the concept is genuinely novel and re-usable across many pages.

**Common trap — org/company names as tags**: When creating entity pages for people who founded or work at a specific company (e.g., `exolabs`, `anthropic-fellow`, `openai-alumni`), do NOT use the org name as a tag unless it's already in the SCHEMA taxonomy. Map to broader tags instead: `founder`, `entrepreneur`, `ceo`, `researcher`, etc. The taxonomy has ~560 tags — check before inventing new ones.

**Fix — Option B: Add to SCHEMA.md.** When no existing tag fits, add the new tag(s) to the appropriate category. Most new tags go under **Techniques** (line ~35). Example additions:
- `niah, needle-in-haystack, context-rot, context-degradation, query-expansion`
- `position-interpolation, context-extension, rope, position-encoding`

**Pattern**: Check `grep -n "tag-name" wiki/SCHEMA.md` *before* writing page frontmatter. Prefer mapping to existing tags over expanding the taxonomy.

## 2. Japanese/CJK Language Block

**What it looks like:**
```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW FILE with Japanese content: wiki/entities/some-page.md
```

**Root cause**: Wiki language policy is **English-only** for all non-raw/ content. The hook detects CJK Unicode ranges: `[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]`.

**Fix**: Remove non-English characters. Common triggers:
- Chinese characters in names (e.g., `Han Xiao (肖涵)` → `Han Xiao`)
- Japanese text in summaries or quotes
- CJK punctuation or symbols

**Note**: The CJK range catches Chinese names too, not just Japanese. Be aware when adding Asian researcher names.

## 3. Duplicate Index Sections

**What it looks like**: `Found 2 matches for old_string. Provide more context to make it unique.`

**Root cause**: `wiki/index.md` has duplicated concept sections. Both copies need the same update.

**Fix**: Use `replace_all=true` in the patch call:
```python
patch(path="wiki/index.md", old_string="...", new_string="...", replace_all=True)
```
This updates both copies simultaneously. Verify the diff shows both sections updated.

## 5. Sibling-Agent Tag Contamination

**What it looks like**: Your pages have valid tags, but commit is blocked with violations in files you didn't touch:
```
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (3):
   wiki/concepts/other-page.md:  some-new-tag
   wiki/entities/other-entity.md:  another-tag
```

**Root cause**: A sibling agent (another concurrent cron job or delegate_task) staged files to the same repo with new tags that aren't in SCHEMA.md yet. Since `git commit` commits everything in staging, your commit inherits their tag violations.

**Fix — Option A (preferred when you own the fix)**: Fix the offending tags directly in the sibling files. If a tag like `html` is clearly wrong, replace it with a canonical tag (`html` → `frontend`). This is faster than expanding the taxonomy for one-off tags.

**Fix — Option B**: Add the missing tags to `wiki/SCHEMA.md` to unblock the commit for everyone:
- Map each tag to the correct category (Techniques, Engineering, People/Orgs, AI Agents, etc.)
- Common sibling tags to expect: `model-training` → Techniques, `production-ml` → Engineering, `ai-researcher` → People/Orgs

**Prevention**: When you see `git status --short` showing files from other agents before committing, proactively check: `grep -r "^tags:" wiki/concepts/ wiki/entities/ | grep -v "tags: \[" ` for any unrecognized tags, and pre-add them to SCHEMA.md before the commit.

**Alternative — individual staging**: Instead of `git add wiki/` (which stages everything), stage only your own files:
```bash
git add wiki/concepts/your-page.md wiki/entities/your-entity.md wiki/raw/articles/your-article.md wiki/index.md wiki/log.md wiki/SCHEMA.md
```
This avoids inheriting tag violations from other sessions' pending changes.

**Near-duplicate tag triage**:
1. First check if a canonical tag already covers the concept (search SCHEMA.md for partial matches)
2. If yes, fix the concept page to use the canonical tag
3. If the variant is genuinely distinct (e.g. `ai-content-detection` = detection tech vs `ai-detection` = meta concept), add the variant to SCHEMA.md
4. If uncertain, add the variant — tag dedup can be done later by `tag-audit-weekly`

## Commit Retry Flow

After fixing any of the above:
```bash
cd /opt/data/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push
```
The pre-commit hook re-runs and will validate tags + language. Repeat until clean.

## 4. Missing Wikilinks in Cross-Referenced Pages

**What it looks like**: New pages link to `[[concepts/reward-hacking]]` or `[[concepts/on-policy-distillation]]` that may not exist yet.

**Root cause**: When creating a concept page, it's easy to add `related:` wikilinks to pages that don't exist. The pre-commit hook doesn't catch this.

**Fix**: Before adding a `[[wikilink]]` in a new page, verify the target exists with `search_files`:
```python
search_files(pattern="target-page-slug", target="files_only", path="wiki/")
```
If it doesn't exist, either (a) create it in the same batch, (b) drop the link, or (c) add it as plain reference without wikilink syntax (e.g., "reward hacking" instead of `[[concepts/reward-hacking]]`). Broken wikilinks degrade the wiki graph and will be caught later by `wiki-graph-analysis`.
