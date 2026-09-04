# Tag Fix Duplicate Pitfall

When fixing tag taxonomy violations in frontmatter by replacing one tag with another, you can accidentally create duplicates if the replacement target already exists in the file.

## Symptom
- You ran `patch` to replace `- conference` with `- event` because `conference` is not in SCHEMA.md
- The file already had `- event` in its tags
- Result: two `- event` entries
- YAML linter passes (duplicate list items are valid YAML)
- Pre-commit tag validator counts one violation resolved and one duplicate — the commit still passes, but the duplicate is noise

## Fix
1. After running any tag-replacement `patch`, verify by searching for the replacement tag name in the file
2. If a duplicate exists, use `patch` to remove the duplicate line (not replace — just remove the redundant line)
3. `read_file` the complete file (not paginated) to confirm all tag lines before and after editing

## Prevention
Before any tag-replacement patch:
1. Identify the violating tag (e.g., `- conference`)
2. Search the file for the replacement tag (e.g., `- event`) — is it already present?
3. If yes: use `patch` to just **delete** the violating line instead of replacing it: `old_string: "\n  - conference", new_string: ""`
4. If no: replacement is safe — proceed normally

## Real-world example (July 2026)
- `events/ai-engineer-worlds-fair-2026.md` had tags: `[event, conference, ai-engineering]`
- Patched `conference` → `event`, resulting in `[event, event, ai-engineering]`
- Required a second patch to deduplicate: remove the extra `- event` line
