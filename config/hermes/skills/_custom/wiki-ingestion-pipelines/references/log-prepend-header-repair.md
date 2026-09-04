# Log.md Prepend & Header Repair (validated Aug 2026)

When prepending a new entry to `wiki/log.md` (newsletter-wiki-ingest, blog-wiki-ingest,
dreaming-wiki-ingest, raw-backlog-ingest, etc.), the file has a **multi-line header that
must stay at line 1**:

```
# Wiki Log

_Log of all wiki changes. Newest entries at top._

## [YYYY-MM-DD] ...
```

## Failure mode 1: duplicate `# Wiki Log` headers

The naive re-order fix `rest[len(header):]` **silently keeps the original header**
when the on-disk header block does not exactly match the `header` constant — e.g. the
file's header is followed directly by `## [date]` with no blank line, or the trailing
`\n\n` spacing differs. Result: `grep -c '^# Wiki Log' wiki/log.md` = 2.

## Failure mode 2: new entry dropped entirely

If the log ALREADY had a displaced header (a previous pipeline prepend put an entry
ABOVE the header — a recurring state, the log is a shared append-only file written by
many pipelines), then a follow-up "fix" that slices `content[header_idx:]` discards
everything before the header — **including the entry just prepended**. Symptom:
`total_lines` shrank, and the new entry never appears in `head -40`.

## Robust pattern (validated Aug 2026)

Strip ALL header variants from the body, then rebuild `header + new_entry + body`:

```python
LOG_PATH = "/opt/data/ai-topics/wiki/log.md"
new_entry = "## [YYYY-MM-DD] pipeline | ...\n- ...\n\n"
header = "# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n\n"

with open(LOG_PATH) as f:
    content = f.read()
# Remove every occurrence of the header block, including variants without trailing blank
for variant in ('# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n\n',
                '# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n',
                '# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._'):
    content = content.replace(variant, '')
body = content.strip('\n')
result = header + new_entry + '\n' + body + '\n'
with open(LOG_PATH, 'w') as f:
    f.write(result)
```

## Verify 3 invariants after ANY log write

Cheap, catches both failure modes:

```python
lines = open(LOG_PATH).read().splitlines()
assert lines[0] == '# Wiki Log', 'header not at line 1'
assert sum(1 for l in lines if l.strip() == '# Wiki Log') == 1, 'duplicate header'
assert any('pipeline-name' in l for l in lines[:40]), 'new entry missing'
```

Also confirm prior entries survived (e.g. `grep -c 'blog-wiki-ingest' wiki/log.md` still
> 0) — the drop-failure mode removes data silently.

## Session trace (2026-08-05 newsletter-wiki-ingest)

- First prepend script used the skill's documented re-order + prepend → header ended at
  line 15 (entry above header), then a second "fix" script sliced from `header_idx` and
  **deleted the new entry** (4002 → 3988 lines) while leaving a duplicate header at line 18.
- Final repair: strip-all-variants + rebuild → header at line 1, exactly 1 `# Wiki Log`,
  entry present, prior entries intact (blog-wiki 1, raw-backlog 45).
- Lesson: never chain two mutating log scripts. Do the whole repair in ONE script and
  assert the 3 invariants before exiting.
