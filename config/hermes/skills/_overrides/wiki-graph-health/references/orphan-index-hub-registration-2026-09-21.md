# Register subdirectory `_index` hub pages in index.md (kills the "23 orphan" false positive)

**Symptom**: `wiki_health.py --json` / digest reports a stable `orphan_count: 23`
(21 `concepts/<dir>/_index` + `entities/_index` + `concepts/_index`, plus any
`_archive` files it can never index). Count never drops across nightly runs.

**Root cause**: The orphan scanner (`section_orphan_pages`) does a substring check
of the full rel path (`concepts/inference/_index`) in index.md text. The index
links hubs by bare dir slug (`- [[concepts/inference]] — ...`), so the scanner
never finds the `_index` path → permanent false-positive orphans.

**Fix (applied 2026-09-21)**: For each hub line in index.md, append
` → [[<dir>/_index]]` to the entry, e.g.

```
- [[concepts/inference]] → [[concepts/inference/_index]] — Inference — LLM inference engine comparison; ...
```

Plus add two root-hub lines at the start of the Entities/Concept sections:
`- [[entities/_index]] — Entities directory hub` (same for concepts).

Both wikilink forms work in Obsidian; the scanner's substring check now passes.

**Script pattern** (idempotent, driven by filesystem):

```python
import re, subprocess
hubs = subprocess.run(["find","wiki/concepts","wiki/entities","-name","_index.md"],
                      capture_output=True, text=True).stdout.split()
# skip _archive hubs; rel = path without wiki/ prefix and .md suffix
# if rel not in index_text: rewrite line "- [[<parentslug]]" -> "- [[<parentslug]] -> [[<rel>]]"
# root hubs (entities/_index, concepts/_index): prepend line after section header
```

**Notes**:
- Do NOT delete or "fix" `_archive/` orphans — archived content is intentionally unindexed.
- After edit, run `python3 scripts/validate_index.py` (must pass) before commit.
- Verify: `wiki_health.py --json` orphan_count should drop to only `_archive` entries.
