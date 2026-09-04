### Pitfall: Duplicate Tags from `replace_all` (2026-07-31)

When fixing tag violations by replacing a non-canonical tag with an existing canonical one using `patch(replace_all=true)`, **check whether the canonical tag already exists in the file**. If it does, `replace_all` replaces the invalid tag in-place but leaves the pre-existing canonical tag intact, creating a duplicate.

**Real failure (2026-07-31)**: `session-portability.md` had tags `provider-sealed-state` and `vendor-lock-in`. Replaced `provider-sealed-state` → `vendor-lock-in` with `replace_all=true`, resulting in two `vendor-lock-in` entries. Had to do a second patch to remove the duplicate.

**Prevention**: Before replacing a non-canonical tag, check if the replacement target already exists:
```bash
grep -c 'vendor-lock-in' wiki/concepts/session-portability.md
# If > 0, DELETE the non-canonical tag instead of replacing:
# old_string: "  - provider-sealed-state\n  - vendor-lock-in"
# new_string: "  - vendor-lock-in"
```

**Alternative**: When multiple tags need fixing, delete the invalid ones entirely and add new canonical tags to SCHEMA.md if needed. Avoid `replace_all` on tags when the target might already be present.
