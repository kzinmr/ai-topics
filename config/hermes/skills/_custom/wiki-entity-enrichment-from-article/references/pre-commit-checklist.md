# Pre-Commit Checklist for Wiki Page Creation

When creating new wiki pages (entity or concept), run this checklist BEFORE `git commit`.

## 1. Tag Validation

The pre-commit hook (`pre-commit-tag-validator.py`) blocks commits containing tags NOT in `wiki/SCHEMA.md`.

**Before committing:**
- Scan your frontmatter `tags:` against `wiki/SCHEMA.md`
- If a tag is missing, FIRST check for an existing canonical tag that covers the same concept:
  - `workflow-automation` → `workflow` (exists under **Engineering**)
  - `voice-input` → `voice-ai` (exists under **Techniques**)
  - `agent-memory-system` → `memory-systems` (exists under **AI Agents**)
- Only add a NEW tag to SCHEMA.md if no existing canonical tag fits — add it to the appropriate category, then `git add wiki/SCHEMA.md`
- Example: `ycombinator` → no existing tag, added to **People/Orgs** category

**Error when blocked:**
```
🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (1):
   wiki/entities/max-rumpf.md:  ycombinator
```

**Fix:** `patch` SCHEMA.md to add the tag, `git add wiki/SCHEMA.md`, re-commit.

## 2. YAML Quoting (x-accounts.yaml)

When adding entries to `config/feeds/x-accounts.yaml`, the `notes` field uses **single-quoted** YAML strings.

- ✅ Escape literal single quotes with `''` (two single quotes): `Amdahl''s Argument`
- ❌ Do NOT use `\'` (backslash-escape) — invalid YAML, breaks parsing

**Verify after adding:**
```python
import yaml
with open("/opt/data/ai-topics/config/feeds/x-accounts.yaml") as f:
    yaml.safe_load(f)  # throws ParserError if quoting is wrong
```

## 3. sed Insertion Direction

`sed -i 'N r /tmp/file' target.md` inserts content **AFTER** line N.

To insert **BEFORE** line T, insert after line `T-1`:
```bash
sed -i 'T-1 r /tmp/file' target.md  # appears BEFORE line T
```

**After every sed insertion**, re-grep to verify placement — line numbers shift.

## 4. index.md and log.md Update Order

1. Create wiki pages first (entity/concept)
2. Update x-accounts.yaml if adding a person
3. Insert into index.md (use sed, verify placement)
4. Prepend to log.md (use `patch`, NOT `write_file` — see `references/log-md-handling-pitfall.md`)
5. Run tag check: scan new pages' tags against SCHEMA.md
6. If new tags needed: patch SCHEMA.md, `git add wiki/SCHEMA.md`
7. `git add` all changed files
8. `git commit`
9. If blocked by pre-commit hook: fix per above, re-commit
10. `git push`

## 6. CJK/Japanese Content Check

The pre-commit hook blocks non-`raw/` wiki pages containing CJK characters (Chinese, Japanese, Korean).

**Before committing:**
- `search_files(pattern="[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]", path="wiki/entities/your-new-page.md")` — run on every new entity page
- If any matches found: romanize names, remove CJK parentheticals, translate quotes
- See `references/wiki-language-cjk-pitfall.md` for details

**Error when blocked:**
```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW FILE with Japanese content: wiki/entities/jina-ai.md
```

**Fix:** Remove CJK characters from the page, `git add`, re-commit.

## 7. web_extract Fallback for Long Technical Pages

When `web_extract` returns only the abstract/first paragraph of a long technical page (e.g., arXiv-style reports), try the **announcement/summary page** instead.

Example: `sid.ai/research/sid-1-technical-report` → only returned abstract. Used `sid.ai/research/sid-1` (the launch announcement) which had the full performance comparison table and architectural details.
