# Wikilink Validation & Tag Verification Patterns

## Wikilink Validation

**Problem**: When creating or enriching wiki pages, agents often generate wikilinks to files that don't exist yet, creating broken links.

**Verification Command**:
```bash
# Check all wikilinks in a page point to existing files
grep -oP '\[\[\K[^\]]+' wiki/path/to/page.md | sort -u | while read -r link; do
  if [ -f "wiki/${link}.md" ] || [ -f "wiki/${link}" ]; then
    echo "OK: $link"
  else
    echo "BROKEN: $link"
  fi
done
```

**Common Pitfalls**:
- Linking to `concepts/on-device-ai` when only `concepts/on-device-rag.md` exists
- Linking to `concepts/claude-code` when the actual file is `concepts/claude-code/claude-code.md`
- Linking to `entities/apple` when only `concepts/apple.md` exists (wrong directory type)
- Creating links in batch without verifying target files exist

**⚠️ Person entity pages carry descriptive suffixes (2026-08-14)**: When enriching with a person wikilink, the natural-name slug often does NOT exist. Observed in blog-wiki-ingest: `[[entities/john-d-cook]]` was BROKEN — the real page is `entities/john-d-cook-applied-mathematics-consulting.md` (suffix from the site/brand). Before linking any person, `ls wiki/entities | grep -i '<surname>'` — the suffix is usually the site domain or role description. Same trap applies to company/organization pages with qualifiers.

**⚠️ Concept remapping when no standalone page exists (2026-08-14)**: A topic mentioned in the body may have NO dedicated page — the coverage lives inside an umbrella concept. Observed: `[[concepts/leiden-declaration-ai-mathematics]]` was BROKEN; the Leiden Declaration is covered in `concepts/ai-mathematics-theorem-proving.md`. Grep the concept dir for the topic name first (`grep -rli 'topic' wiki/concepts/`), then link to the umbrella page with an anchor if helpful: `[[concepts/ai-mathematics-theorem-proving|Leiden Declaration]]`.

**⚠️ Benchmark/evaluation pages live in subdirectories (2026-08-02)**: Naive links to `[[concepts/ai-evaluation]]` are BROKEN — the page is at `concepts/evaluation/ai-evaluation.md` (evaluation methodology pages sit under `concepts/evaluation/`). `[[concepts/ai-benchmarks]]` is valid only as a directory link (individual benchmarks live under `concepts/ai-benchmarks/<name>.md`). When enriching an entity page with benchmark/eval topic context, always `find wiki/concepts -name '*evaluation*'` / `ls wiki/concepts/ai-benchmarks` first, then link to the actual subdirectory path. Pattern: `[[concepts/ai-benchmarks]]` + `[[concepts/evaluation/ai-evaluation]]`.

**Fix Pattern**:
1. Run verification command above
2. For each BROKEN link, find the closest existing file:
   ```bash
   find wiki/ -name '*similar-name*' 2>/dev/null
   ```
3. Replace broken links with existing file paths
4. Re-run verification until all links are OK

## Tag Verification

**Problem**: Adding tags that don't exist in SCHEMA.md taxonomy, causing pre-commit hook failures.

**Verification Command**:
```bash
# Check if a tag exists in SCHEMA.md
grep -q "tag-name" wiki/SCHEMA.md && echo "VALID" || echo "INVALID"
```

**Common Tag Errors**:
- Using `on-device-ai` when only `on-device` exists in taxonomy
- Using `claude-sdk` when only `claude-code` and `agent-sdk` exist
- Inventing new tags without adding them to SCHEMA.md first
- Using singular forms when taxonomy uses plural (`memory-systems` not `memory-system`)

**Fix Pattern**:
1. Before adding any tag, verify it exists in SCHEMA.md
2. If tag doesn't exist, either:
   - Use existing canonical tag from same category
   - Add new tag to SCHEMA.md taxonomy first (if justified)
3. Run tag validation: `grep -oP '  - \K[a-z-]+' wiki/path/to/page.md | while read tag; do grep -q "$tag" wiki/SCHEMA.md || echo "INVALID: $tag"; done`

## Rich Page Protection

**Rule**: Pages >40 lines in `wiki/entities/` or `wiki/concepts/` must be PATCHED, not overwritten with `write_file`.

**Verification**:
```bash
wc -l wiki/path/to/page.md
```

**Workflow**:
1. If >40 lines: Use `patch` tool with targeted string replacement
2. If <40 lines (skeleton): Can use `write_file` for full replacement
3. Always read first 30 lines to understand current structure before patching

## Session Example

Apple Foundation Models page was 171 lines → required patch approach, not write_file. Had 6 broken wikilinks that needed fixing to existing files. Used 2 non-canonical tags that needed correction.

---

*Generated from session: 2026-06-15 Apple Foundation Models concept page enrichment*
*Author: Hermes Agent*
