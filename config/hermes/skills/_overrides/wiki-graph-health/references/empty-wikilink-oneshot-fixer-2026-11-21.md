# Empty-wikilink one-shot fixer (2026-11-21 session)

## Claimed script is fictional
`scripts/fix_empty_wikilinks_safe.py` does NOT exist at
`~/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/`
(only `fix_log_header_burial.py` and tag scripts are there). Do not waste time
looking for it — write the one-shot fixer below.

## Procedure
For every non-`_index` .md under entities/, concepts/, comparisons/, queries/,
events/ (skip `_archive`), process lines matching `^(\s*)-\s+—\s+(.*)`:

1. If the remainder contains a buried wikilink start (regex
   `-\s+\[\[[^\]]+\]\]\s+—\s+`), keep the line from that split point onward
   (recovers links merged onto the artifact line, e.g.
   `-  — desc- [[entities/xania-org]] — desc2` → `- [[entities/xania-org]] — desc2`).
2. Otherwise DROP the line entirely (anchor unrecoverable; the description alone
   is noise).

Same applies to single-space `- — ` variant.

## 2026-11-21 run stats
283 artifacts / 156 files → 29 recovered, 254 dropped, 0 content loss.

## Verification
- `grep -rn '^-  — \|^- — ' wiki/entities/ wiki/concepts/ | grep -v _archive | wc -l` → 0
  (except `_index.md` files which the walk skips — fix those manually, e.g.
  `concepts/multimodal/_index.md` CLIP line → link to `[[concepts/vision-models]]`).
- Content-loss gate before commit:
  `git diff -- wiki/entities wiki/concepts | grep '^-[^-]' | grep -vP '^\-\s*-\s*—' | grep -vP '^\-\s+\[\[' | grep -v 'created:\|updated:'`
  must be empty.
- Residual special case: a bare artifact whose true target must be inferred from
  the description (CLIP → vision-models hub page, since no clip.md exists).

## Log prepend
Standard recipe: python `open()` prepend, then ALWAYS run
`config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py`
LAST before commit (this run: header buried at line 10, restored).
