# Appending rows to existing markdown tables via `patch`

When ingesting a new model/product/release into an entity page that already has a
summary table (e.g. a "Model Family Overview" table on `entities/kimi.md`), the
`patch` replace-mode edit is error-prone because of how leading `|` is handled.

## The pitfall (hit live on 2026-10-25, kimi.md K3.1 Pro ingest)

Replacing a single existing table row with "that row + a new row" by copying the
original `| **X** | ... |` line and appending a second line is easy to fumble:

- If you accidentally start `new_string` rows with `||` (double pipe) — e.g. by
  prefixing a copy of the original line that already began with `|` — you produce
  `|| **Kimi K3.1 Pro** | ...` which renders as an empty first cell and breaks the
  table.
- Adding a stray `> Note:` blockquote directly under a table can also detach the
  table from following content.

## The reliable pattern

1. **Anchor on a multi-line block, not one row.** Put several existing table rows
   (verbatim, single-pipe) in `old_string` so the match is unambiguous, then in
   `new_string` reproduce those rows EXACTLY and append the new row after them.
   This forces you to retype every pipe consistently.
2. **Every table line starts and ends with a single `|`.** No `||` anywhere.
3. **Prefer a dedicated section over a table row for big releases.** A new frontier
   model usually earns its own `## <Model> — <hook> (Mon YYYY)` section (pricing
   table, benchmarks, open-weight status, availability) rather than living only as a
   one-line table row. Do both: add the family-table row AND a full section.
4. **Always update frontmatter `updated:` + append to `sources:`** in the same edit
   unit, plus `wiki/log.md`. index.md only needs touching for NEW pages.
5. After patching a table, re-read the region (the patch tool returns a diff —
   eyeball the pipes in it) before committing. The pre-commit hook checks tag/size
   but NOT table integrity.

## Self-check before commit

`git diff -- wiki/entities/<page>.md` and confirm no line begins with `||` and no
table row lost its trailing `|`.
