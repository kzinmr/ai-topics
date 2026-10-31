# SKILL.md Size Ceiling — Patching the dreaming Skill (discovered 2026-10-29)

`skill_manage(action='patch', name='dreaming', ...)` on the **SKILL.md** body
fails with:

```
SKILL.md content is 101,014 characters (limit: 100,000).
Consider splitting into a smaller SKILL.md with supporting files in references/ or templates/.
```

## Consequences for maintenance

1. **New learnings must go into `references/*.md`**, not SKILL.md. Every
   validated pattern this cycle (and future ones) should be written as a dated
   reference file (e.g. `references/dreaming-render-failure-2026-10-29.md`) and
   referenced from the existing prose with a one-line `📖 See references/...`
   pointer added *inside a reference file* or via an equal-length in-place
   replacement in SKILL.md.
2. **SKILL.md is effectively read-only for additions.** Only equal-length or
   shortening replacements will pass validation. If you need SKILL.md text to
   change, either (a) shorten another paragraph in the same patch so the net
   size does not grow, or (b) move a large dated narrative block out to
   `references/` first (that shrinks SKILL.md and creates room), then add the
   new pointer.
3. **Do not "fix" this by deleting validated pitfalls** to make room — the
   pitfalls are load-bearing. The right consolidation is moving verbose
   "Validated <date>" case narratives into reference files and leaving a
   one-line rule + pointer in SKILL.md.

## Correct tool-call shapes (the failure modes waste iterations)

- ✅ `skill_manage(action='write_file', name='dreaming', file_path='references/<x>.md', file_content=...)`
  — `name` AND `file_path` AND `file_content` are all required; omitting `name`
  yields `Skill '' not found in active profile 'default'`, omitting `file_path`
  yields `file_path is required for 'write_file'`.
- ✅ `skill_manage(action='patch', name='dreaming', file_path='references/<x>.md', old_string=..., new_string=...)`
  — patching a reference file works.
- ❌ `skill_manage(action='patch', ..., file_path='SKILL.md')` →
  `File must be under one of: assets, references, scripts, templates`. To edit
  SKILL.md itself, omit `file_path` (it defaults to SKILL.md) — but then you hit
  the 100k limit above.
- ⚠️ When patching a reference file, `old_string` must be copied from THAT file
  (the tool shows a `file_preview` + "Did you mean" list on a miss — use it to
  re-anchor rather than guessing).

## Suggested future trim (when someone has budget to do it carefully)

The Pattern E "Validated <date>" narrative blocks and the multi-variant
Deep Sleep commit-detection prose are the largest chunks. Moving two or three of
them into reference files would create the headroom that normal patching needs.
Verify with `read_file` after any such move that no rule text was dropped.
