# YAML Frontmatter Corruption — 2026-08-15 Session

Full detail for Section N. Bulk frontmatter scripts silently corrupted 592+52 wiki pages;
`wiki_health.py` cannot see it (returns `{}` on YAML failure).

## Root cause
Commit `53227faf "wiki: add missing sources field to 752 pages"` inserted `sources: []`
BETWEEN `tags:` and its indented list items, producing invalid YAML in 592 files:

```yaml
tags:
sources: []      # ← inserted here
  - concept      # ← list now dangles under nothing
  - company
```

A later auto-fix commit (`4a8abef2 "add missing type/tags frontmatter to 42 L2 pages"`)
introduced merged-line corruption (`type: entitycreated:`) in a second batch.
**Lesson**: check `git log -- <file>` to find the single culprit bulk commit; the whole
file class usually shares one.

## Why health checks miss it
`scripts/wiki_health.py` `parse_frontmatter()`:
```python
try:
    data = yaml.safe_load(fm_text)
    return data if isinstance(data, dict) else {}
except Exception:
    return {}
```
Any YAML failure → `{}` → tags/created/updated/sources silently missing, zero report.
Independent full-wiki validation is mandatory (script below).

## Detection & classification
- `scripts/yaml_validate_frontmatter.py` → list of failing files + error line
- Classify by the offending line (regex over the error line):
  - `type: entity(created|url|handle|status):` → merged key line (Pattern 2)
  - `tags: \[\](type|description):` → merged inline tags (Pattern 2)
  - `- <tag>` non-indented after indented tags block → Pattern 3
  - `## Related Entities` before `title:` → body-in-frontmatter (Pattern 4)
  - `status: L3` + indented `sources:`/`tags:` → Pattern 5
  - `- [Title](url)` → markdown link in YAML list (Pattern 7)
  - `related: [[...]], ...` → wikilink value (Pattern 8)
  - `sources: [` mixed with `- ` items → flow+block mix (Pattern 9)
  - `aliases: [@x` or `- @x` → unquoted @ handle (Pattern 6)

## Fix recipes
### Generic batch (Patterns 1,2,3,6,7,8) — frontmatter-scoped, failing-only
Scoping is CRITICAL: whole-file regex hit 482 files (body `- @handle` + markdown links
quoted wrongly); scoping to frontmatter block AND only files failing `yaml.safe_load`
shrank the set to 35 with zero collateral. Key regexes:
```python
# A: type: entity<key>: merged
re.sub(r'^type: entity(created|url|handle|status):', r'type: entity\n\1:', fm, M)
# B: tags: []<key>: merged (double first)
re.sub(r'^tags: \[\]type: entitystatus: active', 'tags: []\ntype: entity\nstatus: active', fm, M)
re.sub(r'^tags: \[\]type: entity', 'tags: []\ntype: entity', fm, M)
re.sub(r'^tags: \[\]description:', 'tags: []\ndescription:', fm, M)
# C: non-indented dup tags after indented tags block
re.sub(r'(tags:\n(?:  - [^\n]*\n)+)((?:- [^\n]*\n)+)', keep_indented_only, fm)
# H/Z1: quote @-handles (frontmatter only!)
re.sub(r'aliases: \[(@[^\],]+)', r'aliases: ["\1"', fm)
re.sub(r'^(\s*)- (@[^\s\],]+)$', r'\1- "\2"', fm, M)
# F: markdown link in list → quote
re.sub(r'^(\s*)- (\[[^\]]+\]\([^)]+\))$', r'\1- "\2"', fm, M)
# G: wikilink value → quote
re.sub(r'^(related:\s*)(\[\[[^\n]+\])$', r'\1"\2"', fm, M)
```
Guard: only write when `yaml.safe_load(fm)` raised; re-verify after write.

### Pattern 1 (tags→sources order, 592 files)
Collect lines after `sources: []` while they are `  - `; rebuild as
`tags:\n` + tag lines + `sources: []\n`; skip consumed lines. Dry-run printed 590
(592 detected − 1 already manually fixed − 1 variant). Verify: re-run detector → 0.

### Pattern 4 (body-in-frontmatter, 10 files)
Find first `^key:` line in the frontmatter block; move everything before it to AFTER
the closing `---`. Sanity: pre-key lines must look like content (`#`, `##`, `- [[`, `*`).
Example steve-blank.md: `## Related Entities` + 2 links moved below frontmatter.

### Pattern 5 (L3 appended, simon-willison)
`status: L3` then indented `  sources:` (6 items) / `  tags:` then root `sources:`
(40 items). The indented sources were NOT in root — merge both, dedupe, restore
`tags: [person, blogger]` at root, drop indented lines. Verify count via
`yaml.safe_load` → sources 46, tags 2.

### Pattern 9 (flow+block mixed, anthropic/nvidia)
Regex `^sources: \[(.*?)\n\]` DOTALL; strip `,` and `- ` prefixes per line; dedupe;
emit block form `sources:\n  - item`. anthropic: 28 sources; nvidia same recipe.

### Em-dash URL lines (humanlayer/dex-horthy)
`- "https://…" — Y Combinator talk: "…"` fails because the unquoted em-dash tail after
the quoted URL creates a mapping. Fix: quote the WHOLE line including title:
`- "https://… — Y Combinator talk: Getting AI to Work in Complex Codebases (August 2025)"`.

## Table `||` in L2 pages (not wikilink corruption)
`grep '||-'` matched 3: two real (whole table `|| ` prefixed — agent paste artifact),
one false positive (`||---|---|---|` = valid GFM: `|` + separator cell). Real fix is
2-stage:
```bash
sed -i 's/^|| /| /' file.md                    # header + data rows
sed -i 's/^||-/-/' file.md && sed -i 's/^----------|/|----------|/' file.md  # separator rows
```
Then bump `updated:` in frontmatter for touched pages.

## Session counts
- Index corruption (pipe/line-number/triple-bracket/space): 0 — clean
- Ghost entries: 0 (all 2958 index targets resolve recursively)
- Orphan pages: 24 reported, ALL false positives (22 `_index.md` + 2 `gpt/_archive/`
  + 1 redirect `tim-sherratt` → `tim-sh`) — skip per A4c rule 6
- tags→sources inversion: 592 → 0
- YAML parse failures: 52 → 4 remaining (nvidia/harvey/unitree + re-verify)
  when session hit iteration cap — next run: `/tmp/fix_nvidia.py` recipe above.
