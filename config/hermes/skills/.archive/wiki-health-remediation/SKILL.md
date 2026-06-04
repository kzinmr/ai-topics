---
name: wiki-health-remediation
category: wiki
description: "Decision-matrix-driven remediation of wiki health issues: duplicate resolution, skeleton expansion, thin-page cleanup, and redirect creation."
---

# Wiki Health Remediation Workflow

Systematic remediation of wiki health check findings. Use after `wiki-graph-health` analysis identifies issues.

## Health Issue Categories & Decision Matrix

### Category 1: Duplicate Pages

**Detection:** Same topic exists at multiple paths (e.g., `concepts/X.md` + `concepts/harness-engineering/X.md`).

**Decision matrix:**

| Factor | Action |
|--------|--------|
| Partner file is **skeleton stub** (<500 chars) | Delete stub, partner = canonical |
| Partner file has **richer content** | Merge unique content into richer partner, delete stub |
| Partner file is **more specialized** (e.g., system-architecture subfolder) | Merge unique content into partner, replace stub with redirect |
| Both files have **comparable depth** | Keep more specific path (subdirectory), redirect root-level |

**Example from 2026-04-24:**
```
linear-walkthroughs:
  concepts/ (115 chars, stub) → DELETED
  harness-engineering/agentic-workflows/ (2,913 chars, rich) → CANONICAL

agentic-engineering:
  concepts/ (1,090 chars, stub) → DELETED
  harness-engineering/ (7,209 chars, rich) → CANONICAL

claude-code-best-practices:
  concepts/ (12,118 chars, 305 lines) → MERGED into harness version
  harness/system-architecture/ (5,394 chars, 115 lines) → CANONICAL
  Result: 18,423 bytes unified file
```

**Merge procedure:**
1. Read both files
2. Identify unique sections in each
3. Create merged file at partner path with combined content
4. Delete the lesser file
5. Verify no broken wikilinks remain

### Category 2: Skeleton Pages (`status: skeleton`)

**Decision matrix (in priority order):**

| Condition | Action |
|-----------|--------|
| **Partner file exists** with rich content | Replace with redirect: `status: complete`, `## See Also` → partner |
| **Referenced by many other pages** (≥3) | Expand with web search, add comparison tables, set `status: complete` |
| **Has >200 chars of real content** but still skeleton | Check partner, then expand or redirect |
| **<100 chars, no real content** | Delete (too thin to be useful) |

**Expansion approach for important concepts:**
1. Read partner/harness files for cross-reference
2. Search web for latest info on the topic
3. Write comprehensive page with: definition, key points, comparison table, sources
4. Update `status: skeleton` → `status: complete`

### Category 3: Thin Pages (No skeleton marker but very short)

**Decision matrix:**
| Size | Action |
|------|--------|
| <300 chars | Check for partner → redirect, else delete |
| 300-1000 chars | Check if referenced → redirect if partner exists, else expand |
| >1000 chars | Keep, review frontmatter |

### Category 4: Tag Consolidation (Occasional)

When a health report shows **500+ unique tags** or hundreds of mis-formatted tags that deviate from the SCHEMA taxonomy (~20 canonical tags).

**Common issues:**
- **Malformed YAML**: `- [[rag]]`, `- concepts/rag`, `"[rag]"` instead of `- rag`
- **Case variants**: `rAG`, `Rag`, `RAG` → normalize to canonical casing
- **Mixed delimiter**: `person`, `person,` (trailing comma), `- person` (YAML artifact)
- **Wiki-style references**: `[[person]]` inside the tags list instead of plain text
- **Typos / spelling**: `achitecure`, `mlops` (should be `ml-ops`)
- **Whitespace issues**: `rag , core` (space before comma)

**Fix procedure:**

1. **Audit first** — scan all frontmatter for unique tags:
```python3
import os, re
tags_seen = {}
tag_re = re.compile(r'^\s*-\s+(.+)$', re.MULTILINE)
for root, dirs, files in os.walk('.'):
    if 'raw' in root or '.git' in root: continue
    for f in files:
        if not f.endswith('.md'): continue
        path = os.path.join(root, f)
        try: content = open(path, errors='ignore').read()
        except: continue
        if not content.startswith('---'): continue
        _, fm, _ = content.split('---', 2)
        in_tags = False
        for line in fm.split('\n'):
            if line.strip() == 'tags:': in_tags = True
            elif line.startswith('---'): in_tags = False
            elif in_tags:
                if line.strip().startswith('- '):
                    tag = line.strip()[2:]
                    tags_seen[tag] = tags_seen.get(tag, 0) + 1

for tag, count in sorted(tags_seen.items(), key=lambda x: -x[1]):
    print(f'{count:4d}x  {repr(tag)}')
```

2. **Fix malformed tags** — use regex over each source file:
   - `"[[concepts/llama]]"` → `llama`
   - `- [[person]]` → `person`
   - `rAG` → `rag`
   - Remove trailing commas, whitespace, quotes

3. **Consolidate synonyms** — map to canonical names:
   - `llms` → `llm`
   - `mlops` → `ml-ops`
   - `data-enginering` → `data-engineering`

4. **Update SCHEMA.md** — if you discover useful new tag categories that warrant expansion (e.g., "llm-inference" was missing from the original taxonomy), add them to `SCHEMA.md` under `## Tag Taxonomy`

5. **Verify** — re-run the audit and confirm no malformed tags remain

### Category 5: Entity Skeletons

All entity skeleton files from `build_x_wiki.py` should be treated differently:
- **>500 chars of content** → `status: complete` (has real research)
- **<200 chars** → Enrich via `x-account-enrichment` or mark `status: skeleton` for later
- **Already has `type: entity`** → Never delete without checking `build_x_wiki.py` source

### Category 6: Post-Bulk-Ingest Cleanup & Backlog Resolution

When a bulk ingest script (e.g., newsletter-wiki-ingest, blog-ingest, arXiv pipeline, X bookmark pipeline) generates a batch processing record at `~/wiki/bulk-processing/bulk-*.md`, two scenarios arise:

1. **Generated files need cleanup** — duplicates, malformed YAML, empty stubs
2. **Files were NEVER created** — items listed as `❌ ファイル未作成` need systematic resolution

#### Part A: Generated File Cleanup

**Common issues:**
- Bulk generates files for entries that don't actually exist on disk
- Bulk creates duplicates with existing entity pages
- Frontmatter YAML is malformed (description placed as free text between `title:` and `type:`)
- Concept pages are generated as empty stubs (frontmatter only, no content)

**Procedure:**

1. **Read the bulk record** — open `~/wiki/bulk-processing/bulk-<commit>.md`. Note the list of "新規作成Entity" and any TODO items.

2. **Audit what exists** — scan each listed file in `entities/` and `concepts/`. Only a fraction may exist.

3. **Deduplicate against existing entities** — for each entity skeleton found:
   - Search for the real person/company name in existing entities (`grep -i`)
   - Check if the URL/domain is already tracked in another entity
   - If duplicate: merge unique References (raw article crosslinks) into the existing entity, delete the skeleton
   - Even if the existing page has `## Sources` with human-readable links, add `## References` with raw article filenames for machine processing

4. **Fix malformed YAML frontmatter** — a common bulk-process bug puts the description as plain text:
   ```yaml
   # BAD — description has no YAML key:
   title: dragas
   
   Italian sysadmin and FreeBSD advocate...
   
   type: entity

   # GOOD:
   title: dragas
   description: Italian sysadmin and FreeBSD advocate...
   url: https://example.com
   type: entity
   status: skeleton
   ```
   Add `description:`, `url:`, `status: skeleton` keys.

5. **Delete empty concept stubs** — concept pages under 12 lines (frontmatter only, no meaningful content) should be deleted.

6. **Update the bulk-processing record** — mark each entry with its disposition:
   - `✅ 新規保持` — genuinely new entity, keep
   - `🗑️ 重複: merged into X.md` — duplicate merged into existing
   - `✅ concepts/X.md` — moved to concepts/ with content
   - `🗑️ 空のため削除` — empty concept stub deleted
   - `❌ ファイル未作成` — listed but never created on disk → proceed to Part B
   Update the TODO checklist as completed.

#### Part B: Resolving ファイル未作成 (Items Never Created)

When items are marked `❌ ファイル未作成` in the bulk record, systematically categorize and resolve each one.

**Step 1 — Full Audit**

Read the bulk record and build a complete list of ❌ items. For each, determine:

| Category | Description | Action |
|----------|-------------|--------|
| **Already exists (different slug)** | Entity exists under a different filename (e.g., `wheresyoured-at` → `ed-zitron-s-where-s-your-ed-at`) | Mark as ✅ mapped in progress table |
| **Already exists as concept** | Topic is covered by an existing concept page (e.g., `llamacpp` → `concepts/llama-cpp.md`) | Mark as ✅ concept exists |
| **News/media outlet** | General news site (e.g., `cnn`, `fortune`, `9to5google`) | Skip — not AI-specific |
| **Platform/company (non-AI)** | Generic tech platform not core to AI wiki focus (e.g., `github`, `cisco`, `auth0`) | Skip |
| **arXiv-only paper (no peer review)** | Paper on arXiv without peer-reviewed venue | Skip per source rules |
| **Genuinely needs creation** | Important person, company, tool, or concept missing from wiki | Create full page |

**Techniques for auditing at scale:**
- Use `grep -l` / `search_files` to check if existing entities reference the domain/topic
- Check for aliases: `entities/sero.md` may be the entity for `0xsero`
- Check raw articles: existing entities may already have the URL in their References section
- For news outlets: generally skip all major media brands (the-verge, cnn, cnbc, fortune, etc.)
- For tools/concepts: check `concepts/` first, then check if topic is AI-core

**Step 2 — Batch-Create Missing Pages (in parallel)**

Use `delegate_task` with max 3 concurrent subagents. Follow `wiki-entity-enrichment-from-article` for page structure (8-12KB target with frontmatter, overview, core topics, cross-references, sources).

Recommended batching:
- **Batch 1** — 3 entity pages for important people/companies (e.g., shuvendu, kimi, devin)
- **Batch 2** — 3 remaining entity pages (e.g., lenny, databricks, agentcraft)
- **Batch 3** — remaining concepts and special cases (e.g., korean-ai concept)

Each subagent prompt must include:
- Exact file path (`~/wiki/entities/name.md`)
- Raw article paths to reference
- Any existing concept/entity pages for cross-referencing
- Explicit instruction: DO NOT include `status: skeleton`

**Step 3 — Batch-Enrich Existing Skeletons (in parallel)**

If the bulk record also has skeleton entities that need enrichment (e.g., `refactoring-english`, `gilesthomas`, `mahadk`), batch-enrich them via `delegate_task`:
- 2-3 skeletons per subagent
- Provide the existing file path and raw article paths
- Instruct: remove `status: skeleton`, add `updated: YYYY-MM-DD`, target 8-12KB
- Include cross-reference research (find the real person behind the blog)

**Step 4 — Update the Bulk Record**

Rewrite the progress section at the bottom of `bulk-*.md` with final counts:

| Category | Count | Examples |
|----------|-------|---------|
| ✅ New entity/concept created | N | List page names |
| ✅ Mapped to existing entity | N | old → new mappings |
| ✅ Existing concept covers | N | Topic names |
| ✅ Skeleton enriched | N | Page names |
| 🗑️ Skip (news/media/etc) | N | Count only |
| 🗑️ Already deleted | N | Count only |
| 🗑️ arXiv-only skip | N | Paper names |

Also:
- Update the table for each individual entry (replace `❌` with the correct status)
- Replace `## 改善が必要な点（TODO）` items with completed checkboxes
- Update `## 進捗サマリー` section date and counts
- Add "### 残課題: （なし）" if fully resolved

**Step 5 — Update index.md and log.md**

- Update `wiki/index.md`: add new entity/concept entries in the correct alphabetical positions. Update page counts in the header (entity count, concept count, total).
- Update `wiki/log.md`: prepend a single entry summarizing the batch (date, what was resolved, new pages created).

**Step 6 — Commit and Push**

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: bulk-<commit> resolution - N new pages, M skeleton enrichments, K skip items categorized, L existing mappings verified" && git push
```

**Key decisions for ファイル未作成:**

| Situation | Action |
|-----------|--------|
| Already mapped to existing entity (different slug) | Mark as ✅ mapped, no new file needed |
| Already covered by existing concept page | Mark as ✅ concept exists |
| General news/media outlet | 🗑️ Skip — not AI-specific |
| Non-AI platform/company | 🗑️ Skip |
| arXiv-only paper (no peer review) | 🗑️ Skip per source rules |
| Important person, company, tool, or concept | ✅ Create full page (8-12KB via delegate_task) |
| Existing skeleton needs enrichment | ✅ Enrich in parallel (remove `status: skeleton`) |

## Execution Order

Always execute in this order:

1. **Duplicate resolution first** — prevents orphaned references after redirects
2. **Skeleton expansion/redirect** — fix content depth issues
3. **Thin page cleanup** — delete or redirect the dregs
4. **Frontmatter batch update** — only after structure is stable

## Git Strategy

After each category completion, stage changes:
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: remediate <category>" && git push
```

Or batch all changes in one commit at the end.

## Common Pitfalls

- **Don't merge files where one is a redirect stub** — the stub already says "moved to X". Just verify X exists and update status.
- **Don't delete harness-engineering files** — they are often the canonical location. The `concepts/` root-level versions are often stubs.
- **Check `log-2026.md` separately** — it contains legacy-format references, skip for wikilink fixes.
- **Entity skeletons from `build_x_wiki.py`** — these are intentional placeholders. Enrich them, don't auto-delete.
- **`_index.md` files are intentionally large** (500+ lines) — they are hubs, not candidates for deletion.

## Large-Scale Health Remediation Patterns

### Pattern 1: Corrupted filenames with embedded special characters
Some files get corrupted with newlines or control characters in the filename. Python `glob` or `os.listdir` finds them; use file size to identify the corrupted variant.

```python
# Delete corrupted file — use Python for filenames with special chars
import os, glob
d = '/opt/data/ai-topics/wiki/concepts'
for f in glob.glob(os.path.join(d, 'context-en*')):
    if os.path.getsize(f) == 107:  # known small size for corrupted variant
        os.remove(f)
```

### Pattern 2: Missing `type` field across many pages
When 100+ pages are missing the `type:` frontmatter field, auto-detect from directory structure:

```python
# Determine type from path prefix
if rel.startswith('entities/'): type = 'entity'
elif rel.startswith('concepts/'): type = 'concept'
elif rel.startswith('comparisons/'): type = 'comparison'
# Append type line to existing frontmatter
```

### Pattern 3: Systematic broken wikilinks due to missing directory prefix
The most common broken-link pattern: links to pages inside `concepts/` subdirectories (e.g., `harness-engineering/`, `fine-tuning/`) lack the `concepts/` prefix. Build a complete slug-to-path map and fix in bulk.

```python
# Strategy:
# 1. Build all_paths dict: {slug: rel_path} for ALL wiki .md files
# 2. Scan every file for [[wikilinks]]
# 3. For each link, check if slug exists in all_paths
# 4. If not, try prepending 'concepts/' to the slug
# 5. If that resolves, record the (old_link, new_slug) fix pair
# 6. Apply fixes with regex — handle [[link]], [[link | desc]], [[link — desc]]
```

### Pattern 4: Rebuilding index.md from scratch
When `index.md` has far fewer entries than actual pages, regenerate it:

```python
# 1. Scan all wiki pages, extract frontmatter (title, description, type, status)
# 2. Skip stub/skeleton pages from index
# 3. Group by type (entity, concept, comparison)
# 4. Generate markdown with one line per page: - [[slug]] — description
# 5. Total pages often 1000+; index.md can be 50-70KB
```

## Verification After Remediation

1. **No dangling `status: skeleton`** in files you touched
2. **All redirects point to existing files**
3. **No broken wikilinks** introduced by merges
4. **File sizes reasonable** — redirects should be <2KB, expanded pages should be >1KB
5. **index.md page count** matches actual wiki page count (minus stubs/skeletons)
