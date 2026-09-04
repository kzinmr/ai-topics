# Frontmatter Patch Pitfalls (★★★☆☆)

Lessons from real frontmatter corruption events when using `patch` on YAML frontmatter. These are distinct from the index-file pitfalls already documented in the main SKILL.md.

---

## Pitfall 1: Duplicate Frontmatter Fields

**When**: Both `old_string` and `new_string` contain the same YAML key (e.g., both have `created: 2026-05-18`).

**What happens**: The patch tool treats the existing value as matched context AND injects the key from `new_string` as an addition — producing duplicate YAML keys (e.g., two `created:` lines).

**Real-world case**: `forward-deployed-engineering.md` — patch contained `created: 2026-05-18` in both old and new strings, resulting in:
```yaml
created: 2026-05-18
created: 2026-05-18  # DUPLICATE
updated: 2026-05-22
```

**Detection**: After every frontmatter patch, immediately `read_file` the top 30 lines and scan for duplicate YAML keys (`created:`, `updated:`, `type:`, `tags:`, `sources:`).

**Fix**: Use a corrective `patch` that includes the duplicate key in `old_string` (both copies + context) and the deduplicated version in `new_string`.

**Prevention**: When updating `updated:` date only, use `old_string` that starts from `updated:` not `created:`, or use `replace_all` for the date value.

---

## Pitfall 2: Fuzzy Matching Corrupts Adjacent Fields

**When**: The patch tool's fuzzy matching finds a partial match in adjacent YAML fields when exact bytes differ.

**What happens**: Fields like `aliases`, `status`, or `related` can be silently dropped — the patch replaces them with content from `new_string` meant for a different location.

**Real-world case**: `agent-skills.md` — the patch was targeting `created:`/`updated:` fields but matched against `aliases:` and `status: active`, dropping those fields and replacing them with `created:`/`updated:`.

**Detection**: After every frontmatter patch, `read_file` the top 30 lines and verify ALL expected frontmatter fields are present. Compare against what you remember from the pre-patch state.

**Fix**: If fields were dropped, use another `patch` to restore them with correct values. Use a `write_file` as last resort (only when you know the full correct content).

**Prevention**: Use longer `old_string` with more surrounding context (2-3 lines before and after the target) to reduce fuzzy-matching ambiguity. The more context you include, the less likely the tool matches elsewhere.

---

## Pitfall 4: Old-String Context Creep — Silent Field Deletion

**When**: `old_string` includes more YAML frontmatter lines than intended (e.g., wraps `updated:` with adjacent fields like `tags:`, `status:`, `aliases:`), and `new_string` omits some of those fields.

**What happens**: The omitted fields are silently deleted from the file. No error is raised — the patch succeeds, the file is saved, but critical frontmatter metadata (tags, sources, aliases) is gone.

**Real-world case (June 24, 2026)**: `entities/perplexity-comet.md` — patching `updated:` date from `2026-04-13` to `2026-06-24`:

```python
# old_string (TOO WIDE — includes adjacent fields):
"updated: 2026-04-13
tags:
- entity
- product
- browser-agent
status: active"

# new_string (omits tags):
"updated: 2026-06-24
type: entity
status: active"
```

Result: `tags:` was replaced with `type: entity`, silently dropping `- entity`, `- product`, `- browser-agent`. The `type: entity` line was already present earlier in the frontmatter, creating a duplicate.

**Detection**: After every frontmatter patch, `read_file` the top 15 lines and check ALL expected fields: `created`, `updated`, `type`, `tags`, `aliases`, `status`, `sources`, `related`. Use a mental checklist or a script.

**Fix**: 
1. Read the current (corrupted) file
2. If `tags:` was dropped, add it back with its original values: `patch(old_string="aliases:\n...", new_string="tags:\n- entity\n- product\n- browser-agent\naliases:\n...")`
3. If duplicate `type:` lines exist, remove one with another patch

**Prevention**:
- **Always patch single lines when possible**: `patch(old_string="updated: 2026-04-13", new_string="updated: 2026-06-24")` — never include adjacent fields in `old_string` unless you intend to modify them
- **After patching `updated:` date, immediately read the file to verify**: the tiny effort of a 30-line read prevents silent data loss
- **If you must include context for uniqueness, minimize it**: include the one line above and one line below the target, nothing more than necessary

---

## Pitfall 3: Non-Canonical Tags Block Git Commit

**When**: Using tags not in `SCHEMA.md` taxonomy.

**What happens**: The pre-commit hook (`pre-commit-tag-validator.py`) validates all tags against SCHEMA.md and blocks `git commit` with a list of violating files and offending tags.

**Real-world cases**:
| Wrong tag | Correct SCHEMA tag |
|-----------|-------------------|
| `devtools` | `developer-tooling` |
| `applied-ai` | `enterprise-ai` |
| `career` | (no equivalent — use `enterprise-ai` or skip) |

**Detection**: The hook outputs: `🚨 TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED` with violating files and tags.

**Fix**: 
1. Map non-canonical tags to their SCHEMA equivalents
2. OR add the new tag to `SCHEMA.md` if truly novel and necessary
3. Fix tags in files, `git add`, re-commit

**Prevention**: Always `grep` SCHEMA.md for a tag name before using it on a new page. See `scripts/tag_normalization.py` for existing mappings.

## Pitfall 5: Sources-List Update Cascading Into Adjacent Fields

**When**: Adding a new entry to a YAML `sources:` list in frontmatter, where the `old_string` includes the closing `]` and the next line (e.g., `updated:` or `tags:`).

### Sub-pitfall 5a: YAML Closing `---` Delimiter Consumed

**When**: The `sources:` list is the **last** field in the YAML frontmatter (right before the `---` closing delimiter), and `old_string` includes the `---` line along with the sources tail.

**What happens**: The `---` delimiter is in `old_string` but omitted from `new_string`, so the patch removes it silently. The file ends up with no YAML closing delimiter — the frontmatter bleeds into the body content. No error or warning is raised.

**Real-world case (July 20, 2026)**: Enriching `entities/sam-altman.md` — adding a second source to the `sources:` list:

```python
# old_string includes the --- delimiter and blank line:
"  - raw/newsletters/2026-05-10-...md\n---\n\n# Sam Altman"

# new_string omits ---:
"  - raw/newsletters/2026-05-10-...md\n  - raw/articles/...md"
```

Result:
```yaml
sources:                         # YAML frontmatter
  - raw/newsletters/2026-05-10-...md
  - raw/articles/...md
# Sam Altman                     # Now parsed as YAML key!
```

**Detection**: After every frontmatter patch, run `head -5 wiki/<file>.md` and verify the YAML closing `---` is present between the last frontmatter field and the body heading.

**Fix**: Re-patch to restore the `---` delimiter:
```python
old_string = "  - raw/articles/...md\n# Sam Altman"  # current corrupt state
new_string = "  - raw/articles/...md\n---\n\n# Sam Altman"  # add --- back
```

**Prevention**:
- **Never include the `---` closing delimiter in `old_string`** when patching frontmatter fields. Patch only up to the last YAML field line.
- If you must include context lines for uniqueness, stop before `---`.
- After ANY frontmatter patch, immediately `head -5` the file to confirm the `---` is still intact.
- If the `sources:` list is the last field, construct `old_string` that ends at the last source item entry (before `---`), not including the delimiter.

**What happens**: The patch replaces the `sources:` tail AND the adjacent field, creating:
1. A duplicate `updated:` line (one from old context, one from new context)
2. Then fixing the duplicate with another patch can corrupt `tags:` spacing (removing the space after `tags:` → `tags:[value]`)

**Real-world case (June 26, 2026)**: `entities/simon-willison.md` — adding two new sources to the `sources:` list:

```python
# Patch 1: added sources + updated: in new_string
old_string = "...porting-moebius--6904f00e.md]"
new_string = "...porting-moebius--6904f00e.md, ...ai-and-liability--dc57f9f0.md, ...scrutineer-html--2ad1fbbe.md]\n updated: 2026-06-26"
# Result: duplicate updated: line (original + new with leading space)

# Patch 2: tried to remove duplicate, corrupted tags:
old_string = "...scrutineer-html--2ad1fbbe.md]\n  updated: 2026-06-26\ntags:"
new_string = "...scrutineer-html--2ad1fbbe.md]\ntags:"
# Result: tags:[person, blogger] (missing space after colon)
```

**Detection**: After every frontmatter patch, `read_file` the top 15 lines and check: (1) no duplicate YAML keys, (2) all field spacing correct (`tags: [value]` not `tags:[value]`), (3) `updated:` appears exactly once.

**Prevention**:
- When adding to `sources:` list, include ONLY the last source entry + closing `]` in `old_string`. Do NOT include `updated:` or `tags:` lines.
- Use a separate patch for the `updated:` date change.
- After EACH patch, `read_file` the top 15 lines before making the next patch.

---

## Pitfall 6: Body `Source:` Wikilink Makes Frontmatter Sources Anchor Ambiguous

**When**: Enriching via Python string replacement (or patch) — adding a new entry to a frontmatter `sources:` list, using an anchor that ends with the last source filename + closing `]` (e.g., `raw/articles/foo--bar.md]`).

**What happens**: The same raw-article filename appears in TWO places in the page: (1) the frontmatter `sources:` list ending with `md]` (single bracket), and (2) the body's `Source: [[raw/articles/...md]]` wikilink ending with `md]]` (double bracket — the `md]` substring also matches the first bracket of `]]`). A naive `.replace()` corrupts the body wikilink or silently hits the wrong location; a count check (`content.count(anchor)`) returns 2.

**Real-world case (Aug 11, 2026)**: `entities/simon-willison.md` — adding `raw/articles/simonwillison.net--2026-aug-10-introducing-muse-glimmer--d8fd569f.md` to the frontmatter `sources:` list. The anchor `raw/articles/simonwillison.net--2026-aug-9-sqlite-text-history-prototype--40d193a4.md]` matched twice: once in frontmatter (line 10, `...40d193a4.md]` + newline) and once in the body's `Source: [[raw/articles/...40d193a4.md]]` wikilink (line 822). The script's ambiguity guard (`count > 1 → SystemExit`) caught it before any corruption.

**Fix**: Disambiguate with the trailing newline: use `...40d193a4.md]\n` as the anchor — the frontmatter line ends `md]\n` but the body wikilink is `md]]\n`, so `md]\n` only matches frontmatter.

**Prevention**:
- Use count-checking helpers in enrichment scripts: `replace_once(path, old, new)` that raises on `count == 0` (anchor missing) and `count > 1` (ambiguous) instead of bare `.replace()`. The ambiguity guard is what saved this run — always include it.
- When the anchor is a raw-article filename, append the closing context: `]\n` for frontmatter sources lists (distinct from body wikilink `]]`).
- **simon-willison.md quirk**: this page has TWO `sources:` lines in frontmatter — a legacy indented `  sources: [...]` (older entries, ends `--6340f228.md]`) and the canonical `sources: [...]` (ends `--40d193a4.md]`). `grep -c` on a filename returns 3 (2 frontmatter + 1 body Source). The canonical line is the second one; the legacy line is the pre-`status: L3` era and should NOT be extended — always target the canonical line, or you'll create a divergent third sources list.
