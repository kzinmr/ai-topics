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

**⚠️ PITFALL — Singular vs Plural tag variants**: SCHEMA.md often has plural forms (`scaling-laws`, `evaluations`, `agents`). Writing the singular (`scaling-law`, `evaluation`, `agent`) silently fails. Before using a tag, `grep` for it in SCHEMA.md to confirm exact spelling. Common traps:

| Written (wrong) | SCHEMA has (correct) |
|---|---|
| `scaling-law` | `scaling-laws` |
| `test-time-compute` | `test-time-scaling` |
| `gpu-optimization` | `gpu` + `performance` |
| `persistent-kernel` | `fused-kernels` |
| `latency` | `real-time` |
| `compiler` | `optimization` |

**⚠️ PITFALL — YAML `sources` field as single-line array**: The `sources:` frontmatter field must use multi-line YAML format, NOT a single-line array. The pre-commit hook parses `sources: [raw/articles/..., raw/articles/...]` and treats the array value as a tag, causing violations like:
```
wiki/entities/xiaomi-mimo.md:  sources: [raw/articles/2026-04-23_xiaomi-mimo-v2.5-pro.md, raw/articles/2026-06-08_xiaomi-mimo-tilert-1000tps.md]
```
**Correct format**:
```yaml
sources:
  - raw/articles/2026-04-23_xiaomi-mimo-v2.5-pro.md
  - raw/articles/2026-06-08_xiaomi-mimo-tilert-1000tps.md
```
**Wrong format** (causes tag violation):
```yaml
sources: [raw/articles/2026-04-23_xiaomi-mimo-v2.5-pro.md, raw/articles/2026-06-08_xiaomi-mimo-tilert-1000tps.md]
```

**Fix — Option A (PREFERRED): Map to existing canonical tags.** Many non-canonical tags have close equivalents already in SCHEMA.md. Replacing them avoids taxonomy bloat and is faster than editing SCHEMA.md. Examples:

| Offending Tag | Canonical Replacement | Why |
|---|---|---|
| `model-training` | `model` + `training` | SCHEMA has both separately |
| `ai-researcher` | `researcher` | `researcher` exists in People/Orgs |
| `production-ml` | _(remove)_ | Covered by `reinforcement-learning` + `coding-agents` context; no unique concept |
| `online-learning` | `continual-learning` (alias) or `training` | Check if a close alias exists first |
| `scaling-laws` | `scaling` | SCHEMA has `scaling` (not `scaling-laws`) |
| `pre-training` | `training` | SCHEMA has `training`; `pre-training` is not a tag |
| `claude` | `model` | No `claude` tag; use `model` (or `claude-fable-5` for the specific product) |
| `system-card` | `system-card` | Meta (added 2026-06-10 as canonical); also `ai-safety` or `evaluations` for narrower focus |
| `model-evaluation` | `evaluations` | SCHEMA has `evaluations` (plural); `model-evaluation` is not a tag |
| `data-curation` | `datasets` or `synthetic-data` | SCHEMA has `datasets` and `synthetic-data` but not `data-curation` |
| `sparse-retrieval` | `retrieval` | SCHEMA has `retrieval`; `sparse-retrieval` is not a tag |
| `tracing` | `trace-analysis` or `observability` | SCHEMA has `trace-analysis` (ML pipelines) and `observability` (monitoring); `tracing` is not a tag |
| `icml` | _(remove)_ | Bare conference acronyms are NOT canonical. SCHEMA uses year-suffixed forms: `iclr-2026`, `neurips-2024`, `recsys-2025`. If no year-suffixed form exists for your conference, just drop the tag — the conference reference is already in `sources:` frontmatter |
| `iclr` | `iclr-2026` (or remove) | Same rule: bare acronyms blocked; use year-suffixed form or omit |
| `neurips` | `neurips-2024` (or remove) | Same rule |
| `culture` | `ai-organization` | Use for org culture topics |
| `product-development` | `product` | Use the shorter form |
| `personalization` | `personal-ai` | Use for personalization/AI assistant topics |
| `competitive-dynamics` | `strategy` | Use for competitive analysis |
| `healthcare` | `biotech` or `ai-safety` | No dedicated healthcare tag |
| `research-funding` | `research` + `philanthropy` | Use both tags together |
| `realtime-api` | `api` | Use the broader `api` tag |

**Rule of thumb**: Before adding a new tag, search SCHEMA.md for partial matches. `model-training` → try `model`, `training`. `ai-researcher` → try `researcher`. If a canonical tag covers 80%+ of the meaning, use it. Only add to SCHEMA.md when the concept is genuinely novel and re-usable across many pages.

**Real example (2026-06-05, dsprrr entity)**:
- Invented tags: `r-language`, `llm-framework`, `code-execution`, `tidyverse` — ALL blocked by pre-commit
- Fix: Mapped to existing: `dspy`, `rlm`, `framework`, `structured-outputs`
- Lesson: When creating entity pages for tools/frameworks, default to the ecosystem tags (`dspy`, `rlm`, `framework`) rather than descriptive adjectives. SCHEMA has ~630 tags — check before inventing.

**Common trap — org/company names as tags**: When creating entity pages for people who founded or work at a specific company (e.g., `exolabs`, `anthropic-fellow`, `openai-alumni`), do NOT use the org name as a tag unless it's already in the SCHEMA taxonomy. Map to broader tags instead: `founder`, `entrepreneur`, `ceo`, `researcher`, etc. The taxonomy has ~560 tags — check before inventing new ones.

**Fix — Option B: Add to SCHEMA.md.** When no existing tag fits, add the new tag(s) to the appropriate category. Most new tags go under **Techniques** (line ~35). Example additions:
- `niah, needle-in-haystack, context-rot, context-degradation, query-expansion`
- `position-interpolation, context-extension, rope, position-encoding`
- `on-device, context-compression` (added 2026-06-04 for on-device RAG concept page)

**⚠️ PITFALL — SCHEMA.md must be staged after editing**: If you patch `wiki/SCHEMA.md` to add new tags, you MUST include it in the `git add` staging. The pre-commit hook reads the **staged/index** version of SCHEMA.md, not the working copy. A common failure sequence:
1. Commit blocked → missing tags in SCHEMA.md
2. Patch SCHEMA.md with new tags
3. Re-run `git add wiki/` + `git commit` → **STILL BLOCKED** because SCHEMA.md was already staged (from step 1) with the OLD content
4. Fix: explicitly `git add wiki/SCHEMA.md` to update the staging area, then commit

The safe one-liner after adding tags to SCHEMA.md:
```bash
cd ~/ai-topics && git add wiki/SCHEMA.md wiki/ && git commit -m "..." && git push
```
This re-stages SCHEMA.md with the updated content before committing.

**⚠️ PITFALL — SCHEMA.md has duplicate category lines**: As of 2026-06, SCHEMA.md has TWO lines starting with `- **Models**:` — one at line ~32 (correct, with `reasoning, reasoning-model, code-model, ...`) and one at line ~35 (actually Techniques content: `inference, fine-tuning, training, ...`). When adding model-related tags like `open-weight` or `gemma`, add them to the **first** Models line (line ~32) which has the correct model-specific taxonomy. If the patch tool matches the wrong line, use more context in `old_string` to target the right one.

**Pattern**: Check `grep -n "tag-name" wiki/SCHEMA.md` *before* writing page frontmatter. Prefer mapping to existing tags over expanding the taxonomy.

**Special case — files moved FROM raw/**: Files in raw/ subdirectories are often not validated by the pre-commit hook. When you move files OUT of raw/ to a tracked directory (e.g., raw/transcripts/ to transcripts/), their tags suddenly get validated. You may see 5-10 new tag violations in a single commit. Either add the missing tags to SCHEMA.md or map them to existing canonical tags before committing.

## 2. Duplicate Entity Detection (NEW — 2026-06-04)

**What it looks like**: You create `wiki/entities/ben-clavie.md` only to discover `wiki/entities/benjamin-clavie.md` (309 lines, comprehensive) already exists. Wasted effort + orphan file.

**Root cause**: Entity filenames use various conventions — full name, surname only, handle, abbreviation. Searching by one variant misses others.

**Prevention — mandatory before creating any new entity file**:
1. **Search index.md** for ALL name variants:
   - Full name (`benjamin-clavie`), surname-only (`clavie`), X handle (`bclavie`), GitHub username, org abbreviation
   - Use: `search_files(pattern="<variant>", target="content", path="~/wiki/index.md")`
2. **Search entity directory** for files:
   - `search_files(pattern="<surname>", target="files", path="~/wiki/entities")`
   - Also try: `search_files(pattern="<handle>", target="files", path="~/wiki/entities")`
3. **If found**: READ the existing file, then PATCH to add new info. NEVER overwrite with `write_file`.
4. **Index entry may exist without file** (orphan index entry): check both index AND filesystem.

**Real example (2026-06-04)**:
- Searched for `bclavie` and `mixedbread` → found nothing
- Missed `benjamin-clavie.md` (309 lines, comprehensive entity page)
- Created duplicate `ben-clavie.md` → had to delete it
- The index had `[[entities/benjamin-clavie]]` at line 173

## 3. Japanese/CJK Language Block

**What it looks like:**
```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW FILE with Japanese content: wiki/entities/some-page.md
```

**Root cause**: Wiki language policy is **English-only** for all non-raw/ content. The hook detects CJK Unicode ranges: `[\\u3040-\\u309F\\u30A0-\\u30FF\\u4E00-\\u9FFF\\uFF00-\\uFFEF]`.

**Fix**: Remove non-English characters. Common triggers:
- Chinese characters in names (e.g., `Han Xiao (肖涵)` → `Han Xiao`)
- Japanese text in summaries or quotes
- CJK punctuation or symbols

**Note**: The CJK range catches Chinese names too, not just Japanese. Be aware when adding Asian researcher names.

**⚠️ PITFALL — User communicates in Japanese but wiki pages must be English**: When the user writes in Japanese (common for this user), it's tempting to write section headers and table content in Japanese to match their style. ALL non-raw/ wiki content must be English — this includes comparison pages, concept pages, entity pages, and especially table cells and section headers. The user's Japanese request does NOT mean they want Japanese output in the wiki. Write wiki pages in English; respond to the user in Japanese.

## 4. Duplicate Index Sections

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
⚠️  TAGS NOT IN SCHEMA.md TAXONOMY (N):
   wiki/concepts/other-page.md:  some-new-tag
   wiki/entities/other-entity.md:  another-tag
```

**Root cause**: A sibling agent (another concurrent cron job or delegate_task) staged files to the same repo with new tags that aren't in SCHEMA.md yet. Since `git commit` commits everything in staging, your commit inherits their tag violations.

**Fix — Option A (preferred when you own the fix)**: Fix the offending tags directly in the sibling files. If a tag like `html` is clearly wrong, replace it with a canonical tag (`html` → `frontend`). This is faster than expanding the taxonomy for one-off tags.

**Fix — Option B**: Add the missing tags to `wiki/SCHEMA.md` to unblock the commit for everyone:
- Map each tag to the correct category (Techniques, Engineering, People/Orgs, AI Agents, etc.)
- Common sibling tags to expect: `model-training` → Techniques, `production-ml` → Engineering, `ai-researcher` → People/Orgs

**Prevention**: When you see `git status --short` showing files from other agents before committing, proactively check: `grep -r "^tags:" wiki/concepts/ wiki/entities/ | grep -v "tags: \["` for any unrecognized tags, and pre-add them to SCHEMA.md before the commit.

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

## 6. Sibling-Agent Commit Co-Bundling (NEW — 2026-06-08)

**What it looks like**: You create new files and patch existing ones (entities, concepts, raw articles). When you run `git add wiki/ && git status --short wiki/`, only `index.md` and `log.md` show as modified — your other files show nothing. `git diff` and `git diff --cached` return empty for your files. But `git log --oneline -1` shows a recent commit by another agent that includes your files.

**Root cause**: A sibling agent (cron job or concurrent session) ran `git add wiki/ && git commit && git push` between your file creation and your staging. Since `git add wiki/` stages all wiki changes, your new files and patches were staged by the sibling's `git add`, and got committed under their commit message. When you later run `git add wiki/`, your files are already staged and committed — nothing new to add.

**This is NOT tag contamination** (section 5). The commit succeeded; your files are in the repo. The confusion is about provenance, not correctness.

**Diagnosis sequence**:
```bash
# 1. Check if your files exist and have the expected content
cat wiki/concepts/your-new-page.md | head -5

# 2. Check git log — does the latest commit include your files?
git log --oneline -1
git show --stat HEAD

# 3. If HEAD includes your files with a different commit message → co-bundled
# Your changes are safe; the commit message is misleading but the content is correct.
```

**Fix**: If you want a clean commit history, reset and re-commit:
```bash
cd ~/ai-topics
# Soft-reset the co-bundled commit
git reset --soft HEAD~1
# Unstage everything
git reset HEAD
# Re-stage only the sibling's files (they need their own commit)
git add <sibling-files>
git commit -m "wiki: <sibling's original message>"
# Now stage and commit your files separately
git add <your-files> wiki/index.md wiki/log.md
git commit -m "wiki: <your message>"
git push --force-with-lease
```

**Prevention (recommended)**: Use **individual file staging** instead of `git add wiki/`:
```bash
# Instead of:
git add wiki/  # catches everything, including sibling work

# Stage only your files:
git add wiki/concepts/gte-moderncolbert.md \
        wiki/raw/articles/2025-04-30_lighton_article.md \
        wiki/entities/lighton.md \
        wiki/concepts/colbert.md \
        wiki/index.md wiki/log.md
```
This is the same prevention as section 5 (individual staging), but the symptom and severity differ: section 5 is about tag violations blocking your commit; this section is about your commit succeeding silently under the wrong message.

**Real example (2026-06-08, GTE-ModernColBERT ingestion)**:
- Created `wiki/concepts/gte-moderncolbert.md` and `wiki/raw/articles/2025-04-30_lighton_gte-moderncolbert-pylate.md`
- Patched `wiki/entities/lighton.md`, `wiki/concepts/colbert.md`, `wiki/concepts/pylate.md`
- Ran `git add wiki/ && git status --short wiki/` → only `index.md` and `log.md` showed as `M`
- `git diff --cached` on my concept/patched files returned empty
- Discovered HEAD commit (`dfcf2ef9 "wiki: ingest Spotify Research Semantic IDs article + concept page"`) included ALL my files (83-line concept page, 74-line raw article, entity patches)
- Solution: just committed the remaining index.md + log.md updates and pushed

**When NOT to reset**: If the co-bundled commit is already pushed and other agents may have pulled it, a force-push is dangerous. In that case, just add your remaining changes (index.md, log.md) in a follow-up commit and note the co-bundling in your log entry.

## 7. Missing Wikilinks in Cross-Referenced Pages

**What it looks like**: New pages link to `[[concepts/reward-hacking]]` or `[[concepts/on-policy-distillation]]` that may not exist yet.

**Root cause**: When creating a concept page, it's easy to add `related:` wikilinks to pages that don't exist. The pre-commit hook doesn't catch this.

**Fix**: Before adding a `[[wikilink]]` in a new page, verify the target exists with `search_files`:
```python
search_files(pattern="target-page-slug", target="files_only", path="wiki/")
```
If it doesn't exist, either (a) create it in the same batch, (b) drop the link, or (c) add it as plain reference without wikilink syntax (e.g., "reward hacking" instead of `[[concepts/reward-hacking]]`). Broken wikilinks degrade the wiki graph and will be caught later by `wiki-graph-analysis`.

## 8. Duplicate `write_file` from Parallel Sessions

**What it looks like**: You run `write_file` to create entity/concept pages, then `git add` and `git commit`. The commit shows only 1 file changed with a few insertions — your new files aren't in the diff. But `git ls-files` shows they're tracked, and `git log --oneline -1 -- FILE` shows a sibling agent committed identical content minutes earlier.

**Root cause**: Two sessions process the same source URL simultaneously. Both produce the same content via `write_file`. The first session's commit includes the files; the second session's `write_file` overwrites with identical content, so git sees no diff.

**Diagnosis**:
```bash
# Check if your new files were already committed
git log --oneline -1 -- wiki/entities/your-new-page.md
git show --stat HEAD
```

**Prevention**: Before creating new wiki pages from a URL, check if a recent commit already includes them:
```bash
git log --oneline -5 -- wiki/entities/ PAGE-SLUG.md
```

**When it happens**: The only net new change may be cross-references in existing pages (e.g., adding a "See Also" section to `openai.md` linking to the new foundation page). This is still valuable — commit it separately.

## 9. Wiki Directory Restructuring (git mv + bulk link updates)

When moving wiki pages between directories (e.g., flat `concepts/` → hierarchical `concepts/gpt/`), see **references/wiki-directory-restructuring.md** for the full procedure: move map planning, git mv, Python wikilink update script, entity→concept merges, MOC index creation, and pitfalls (git reset unstages mv, sibling co-bundling, duplicate index entries).

**User preference (2026-06-10)**: Files in vendor subdirectories should include the vendor prefix (`gpt/gpt-5-5.md` not `gpt/5-5.md`). Exception: files with distinctive prefixes like `chatgpt-*`.

**Platform split pattern**: When a vendor directory grows large, split model-centric pages (models, features, system cards) from platform pages (APIs, SDKs, business) into separate directories (e.g., `gpt/` + `openai/`, `claude/` + `anthropic/`).

## 10. Pipe-Prefix List Item Corruption (`|-` instead of `-`) on Any Wiki Page

**What it looks like**: After running `patch` on a wiki page with markdown list items, the pre-commit hook blocks with `|-` at line starts:
```
|- [[concepts/foo]] — some description
|- [[concepts/bar]] — another description
```
instead of the correct:
```
- [[concepts/foo]] — some description
- [[concepts/bar]] — another description
```

**Root cause**: The `read_file` tool displays lines with `N|` line-number prefixes (e.g., `337|- [[concepts/opus-4-8]]`). When constructing the `new_string` for a `patch` call, it's easy to copy the `|-` from this display — the pipe looks like it's part of the content rather than the display format. The `patch` tool faithfully writes whatever you pass, so `|-` becomes the actual line start.

This corruption can affect ANY wiki page — concepts, entities, comparisons, events — not just index.md or log.md.

**PITFALL — The pipe is invisible without `cat -A`**: The `|-` vs `-` difference is subtle and hard to spot visually. Always verify patched lines with:
```bash
sed -n 'N,Mp' path/to/page.md | cat -A
```
`cat -A` reveals `|-` as `|-$` (pipe, hyphen, dollar-sign) vs a clean `-$` (just hyphen).

**Fix**: A second `patch` call to replace the corrupted prefix:
```python
patch(path="wiki/concepts/some-page.md",
      old_string="|- [[concepts/foo]]",
      new_string="- [[concepts/foo]]")
```

**Prevention**: Before writing `new_string` for a patch:
1. Verify your content doesn't start with `|` — use terminal `cat` instead of `read_file` to see raw content without `N|` prefix
2. If building from `read_file` output, explicitly strip the leading `|` from any line that starts with `N|-`
3. After patching, immediately verify: `sed -n 'N,Mp' path/to/page.md | cat -A`

**Real example (2026-06-14)**: Patched `concepts/claude/fable-5.md` to add an Anthropic statement link. The `new_string` was constructed using the `read_file` display line `337|- [[concepts/opus-4-8]]` which included the `|-` prefix. Result: both the existing line AND the new link gained `|-` corruption. Fixed with a second patch.

### Variant: Baked-in Line Number Prefixes from Subagent Patches

**What it looks like** (more severe): The pre-commit hook blocks lines starting with numbers:
```
L387: baked-in line number prefix: 387|- [[entities/han-lee]] — Han Lee
L388: baked-in line number prefix: 388|- [[entities/hanchunglee]] — ...
```

The content on disk has `387|- ...` (line number `387|` + `- ` list marker) instead of just `- ...`.

**Root cause**: A **subagent** (delegate_task) constructed a `patch`'s `new_string` by using the full `read_file` display line `387|- [[entities/han-lee]] — ...` as-is. Both the `N|` line number prefix AND the `-` list marker were copied into the patch content. The existing Section 10 documentation covers the `|-` (pipe+hyphen) case, but subagents may copy the **full line-number prefix** (`387|`) as well, producing `387|- ` corruption.

This is worse than standard `|-` corruption because:
- `read_file` shows `387|- [[entities/han-lee]]` — the `387` is the line number, the `|` is the separator, the `-` is the markdown list marker
- A subagent may use this exact string in its `new_string`, introducing three characters to strip: `387`, `|`, and the distinction between `|-` and `-`

**Diagnosis**: Verify with cat -A — if a list line starts with digits followed by `|`, the line-number prefix leaked in:
```bash
sed -n 'LINES' wiki/index.md | cat -A
# Output like: 387|- [[entities/han-lee]] ...$
#                    ^^^ the 387| is a leaked line-number prefix
```

**Fix with sed** (line-number specific — target the exact line):
```bash
# For line 387: remove the baked-in "387|" prefix, leaving just "- "
sed -i '387s/^387|- /- /' wiki/index.md
# For line 388:
sed -i '388s/^388|- /- /' wiki/index.md
```
The `387s/.../.../` sed address ensures you only modify the corrupted line, not matching content on other lines.

**Fix with patch** (when sed line number is uncertain):
```python
# Read the corrupted line with cat first, then use the EXACT corrupted content:
patch(path="wiki/index.md",
      old_string="387|- [[entities/han-lee]]",
      new_string="- [[entities/han-lee]]")
```

**⚠️ PITFALL — Double-baked corruption**: If the initial patch already included `387|-` and you try `s/^387|387|- /387|- /` (trying to fix from the wrong assumption), you'll produce `387|-` again and the pre-commit hook will still block. The correct transformation is `387|-` → `- ` (strip everything down to bare markdown list marker), not `387|-` → `387|-` again. Always validate with `cat -A` before deciding the fix.

**Prevention — subagent context guard**: When using `delegate_task` to patch `wiki/index.md`, include explicit context in the subagent's instructions:
> "Read the file with read_file. When building the new_string for patch, do NOT use the N| line-number-prefixed display lines directly — use raw file content obtained via: sed -n 'LINE,LINEp' wiki/index.md | cat -A to see only the actual file bytes. Strip any leading number+|+hyphen pattern before writing a patch."

This prevents the subagent from accidentally baking line numbers into its patch content.

**Real example (2026-06-15, blog-wiki-ingest)**: A subagent patched `wiki/index.md` to update han-lee and hanchunglee descriptions. The subagent used `read_file` output `387|- [[entities/han-lee]]` as-is in its `new_string`. The patch succeeded but left `387|- [[entities/han-lee]]` on disk (leaked line number prefix). The validate_index script flagged both lines as "baked-in line number prefix." Fix required two `sed -i` calls targeting lines 387 and 388.

This corruption can also affect entity/concept pages when subagents build patch content from read_file output containing page numbers (though index.md is the most common victim because of its number-prefixed list structure).

## 11. Content Regression Detection from Sibling Agents

**What it looks like**:
```
🚫 CONTENT REGRESSION DETECTED — rich wiki pages would be overwritten!
   The following staged changes shrink existing pages by >50% or >50 lines.
   📄 wiki/concepts/some-page.md
      262 → 19 lines  (−243 lines, 7% of original)
```

**Root cause**: A sibling agent (cron job or concurrent session) ran `write_file` on an existing rich wiki page, replacing curated content with a skeleton or stub. Since `git add wiki/` stages everything, your commit inherits the regression.

**Fix**: Unstage the offending file(s) and re-commit with only your changes:
```bash
cd ~/ai-topics
git reset HEAD wiki/concepts/some-page.md
git commit -m "wiki: your message"
```

**Progressive unstage pattern**: Multiple sibling blocks may appear in sequence. Each `git commit` attempt may reveal a NEW blocker (tag violations → CJK content → content regression). Fix each one by unstaging the offending file and retrying:

```bash
# Attempt 1: blocked by sibling's tag violations
git reset HEAD wiki/concepts/sibling-bad-tags.md
git commit -m "wiki: ..."  # → new block

# Attempt 2: blocked by sibling's CJK content
git reset HEAD wiki/concepts/sibling-cjk-content.md
git commit -m "wiki: ..."  # → new block

# Attempt 3: blocked by content regression
git reset HEAD wiki/concepts/sibling-skeleton.md
git commit -m "wiki: ..."  # → success
```

**Do NOT use `--no-verify`**: The content regression check exists to protect curated pages. Bypassing it risks losing accumulated knowledge. Always unstage the specific offending files instead.

**Real example (2026-06-15, W&B entity creation)**:
- Staged files included sibling agent's `pytorch-fsdp.md` (262→19 lines, skeleton overwrite) and `llm-as-policy.md` (Japanese content)
- Three sequential `git reset HEAD` calls needed before clean commit
- Each reset revealed the next blocker in the pre-commit pipeline

## 12. Index Drift — Existing Pages Missing from index.md

**What it looks like**: You check `index.md` for existing pages before creating new ones, find nothing, and create duplicates. Or you discover mid-creation that `kv-cache.md`, `kv-cache-compaction.md`, and `flash-attention-4.md` all exist as files but have zero entries in `index.md`.

**Root cause**: Pages created in older sessions (before the index-update discipline was enforced) were never registered in `index.md`. The pre-commit hook validates `index.md` structure but does NOT check that every Layer 2 file has a corresponding index entry.

**Detection**: When doing cross-reference checks during article ingestion (e.g., grepping index.md for related pages), also check the **filesystem**:
```bash
# Find concept files NOT in index.md
comm -23 \
  <(ls wiki/concepts/*.md | sed 's|wiki/||;s|\.md||' | sort) \
  <(grep -oP '\[\[concepts/[^\]]+' wiki/index.md | sed 's|\[\[||' | sort)
```

**Fix**: Add the missing index entries in the same commit as your new ingestion. Alphabetical insertion in the Concepts section. This is a net positive — you're fixing pre-existing drift, not creating new work.

**Real example (2026-06-29, NVIDIA KV Cache Compression ingestion)**:
- `kv-cache.md`, `kv-cache-compaction.md`, `flash-attention-4.md` — all existed as files with rich content
- None appeared in `index.md`
- Discovered while cross-referencing during `triattention` and `kv-cache-compression` page creation
- Added all missing entries in the same commit alongside the new pages

**Prevention**: When ingesting an article that touches existing concept pages, verify those pages are in index.md. If not, add them — it takes 30 seconds and prevents future agents from creating duplicates.

## Commit Retry Flow

After fixing any of the above:
```bash
cd /opt/data/ai-topics && git add wiki/SCHEMA.md wiki/ && git commit -m "wiki: ..." && git push
```
The pre-commit hook re-runs and will validate tags + language. Repeat until clean.
