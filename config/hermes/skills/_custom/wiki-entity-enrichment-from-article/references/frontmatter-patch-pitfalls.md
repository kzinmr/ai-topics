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
