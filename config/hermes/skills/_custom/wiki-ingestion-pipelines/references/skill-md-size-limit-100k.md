# SKILL.md Size Limit — the 100K Wall (hit 2026-11-09)

`skill_manage` rejects any SKILL.md over **100,000 characters**. Two long-lived wiki skills sit at
that ceiling:

| Skill | Chars (2026-11-09) | Status |
|---|---|---|
| `semantic-article-grouping` | ~102,800 | over — cannot add a single character |
| `wiki-ingestion-pipelines` | ~100,200 | at ceiling |

## Symptom

Any `action=patch` — even one that only *adds* a 300-char pointer line — fails:

```
SKILL.md content is 102,838 characters (limit: 100,000). Consider splitting into a
smaller SKILL.md with supporting files in references/ or templates/.
```

This is **not** an argument error and not a missing skill (contrast the separate
`Skill '' not found` error, which means the `name` parameter was dropped/malformed).
Adding text is impossible until an equal amount is removed.

## The one working procedure

**Two patches, in this order.** Net-negative first, then the pointer.

1. **Remove ≥ what you intend to add.** Best candidates, in order of safety:
   - A duplicated `> 📖 See references/...` hook — the same reference is often linked from two
     sections; keep one.
   - Redundant validation-date lists (`Validated: dreaming (Jun 17), newsletter (Jun 22), ...`)
     that the reference file already records.
   - Restated prose that duplicates a `references/` file's own summary.
   Do **not** delete a numbered workflow step or a pitfall that isn't mirrored elsewhere — these
   skills are heavily cross-referenced by cron jobs.
2. **Add the new pointer / pitfall.** Now under the cap.

A single combined replace (delete X + add Y in one `new_string`) also works when the deleted and
added text are in the same region — prefer it when possible, since it leaves no half-edited state.

## Do not do these

- **Do not retry the oversized patch with shorter text** hoping the counter is wrong. It isn't.
  Check the reported number and remove at least that much.
- **Do not "fix" it by rewriting the whole SKILL.md** with `action=edit`. These files are 100KB of
  cron-referenced procedures; a rewrite loses detail and the background curator's consolidation
  work.
- **Do not add more dated `references/newsletter-triage-2026-*.md` files without pruning.** That is
  how these skills reached the wall. New dated material → reference file (fine, unlimited). A
  pointer line in SKILL.md → must pay for itself.

## Structural note for the curator

Both skills have accumulated ~30 dated reference files each plus large in-body pattern sections
that duplicate reference summaries. The durable fix is moving the in-body "Key Patterns to
Recognize" prose into references and leaving SKILL.md as a router. Flagged for the curator rather
than restructured mid-session — a bulk restructure of a cron-referenced skill should be its own
reviewed change, not a side effect of trying to add one pitfall line.
