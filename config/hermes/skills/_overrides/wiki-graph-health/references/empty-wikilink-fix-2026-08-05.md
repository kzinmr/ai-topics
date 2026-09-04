# Empty-Wikilink Safe Fix — Session 2026-08-05

## Context

`wiki-health-fix` cron run. Health digest reported no index corruption and 24
orphan candidates (all false positives: 22 `_index.md` + 2 `concepts/gpt/_archive/`
+ 1 redirect `entities/tim-sherratt` → `[[entities/tim-sh]]`). The real issue
found during verification: **362 empty wikilinks** (`- — description` lines with
the `[[slug]]` anchor lost) across 189 files.

## Raw script traps (fix_broken_wikilinks.py)

1. **Stale KNOWN_MAPPINGS — 73% broken proposals.** Dry-run proposed 107 fixes;
   78 pointed to non-existent files. Two failure classes:
   - Wrong namespace: `concepts/google`/`concepts/nvidia`/`concepts/meta`/
     `concepts/nous-research` → real pages are `entities/*`.
   - Flat-path myth: subdirectory-organized concepts are NOT at
     `concepts/<slug>.md`:
     - `concepts/ai-evals` → `concepts/evaluation/ai-evals.md` (7 refs)
     - `concepts/ai-safety` → `concepts/security-and-governance/ai-safety.md` (7 refs)
     - `concepts/agentic-coding` → `concepts/coding-agents/agentic-coding.md` (1 ref)
     - `concepts/chatgpt-memory-bitter-lesson` → `concepts/gpt/chatgpt-memory-bitter-lesson.md` (2 refs)
2. **Double-space format bug.** 352 of 362 broken lines use `-  — ` (dash, TWO
   spaces, em-dash); only 9 use `- — `. The raw script's
   `line.replace('- — ', f'- [[{slug}]] — ', 1)` only matches the single-space
   form → it counts "fixed" lines without changing the file (phantom fix).
3. **Flag semantics footgun.** `dry_run = '--dry-run' in sys.argv or '-n' in
   sys.argv` — running with NO flags APPLIES changes. `--apply` is not parsed but
   also results in apply. Never run bare.
4. **Runtime.** Needs PyYAML; system python3 (3.13) lacks it. Use
   `/opt/data/.hermes/venv/bin/python`.

## Safe procedure (result: 83 fixes / 70 files, 0 broken links introduced)

1. Scan with regex `^(\s*)-\s+—\s+(.*)$` (handles both space forms).
2. For each broken line, get the base slug from `find_slug_for_description`,
   apply OVERRIDES, then **resolve against the filesystem**: target exists as
   flat file OR as a directory (subdirectory org, e.g. `concepts/context-engineering/`).
3. Bare entity slugs (e.g. `simon-willison`, `teknium`, `xeiaso-net`) resolve to
   `entities/<slug>` and are emitted PREFIXED (`[[entities/simon-willison]]`),
   matching the dominant wiki convention; do NOT emit bare `[[simon-willison]]`.
4. Skip anything without a verifiable target — report it, don't guess. Residual
   after safe fix: 279 (descriptions below mapping threshold; includes
   multi-line merged artifacts like `- — X- [[slug]] — Y` where the anchor
   merged into the description).
5. Verify after apply: extract every `[[...]]` from `git diff wiki/` added lines
   and assert each target exists:
   ```python
   diff = subprocess.run(["git", "diff", "wiki/"], capture_output=True, text=True).stdout
   added = set()
   for line in diff.split('\n'):
       if line.startswith('+') and not line.startswith('+++'):
           for m in re.findall(r'\[\[([^\]|]+)', line):
               added.add(m)
   missing = [l for l in added if not os.path.exists(f"wiki/{l}.md") and not os.path.isdir(f"wiki/{l}")]
   # 2026-08-05: added 52 unique links, missing 0
   ```
6. `validate_index.py` exit 0, commit `wiki: auto-fix health issues (N empty wikilinks)`,
   push. Scope `git add wiki/` only — never stage unrelated `config/` changes
   from other pipelines.

## Override map (verified real paths)

| KNOWN_MAPPINGS slug | Correct target |
|---|---|
| `concepts/ai-evals` | `concepts/evaluation/ai-evals` |
| `concepts/ai-safety` | `concepts/security-and-governance/ai-safety` |
| `concepts/agentic-coding` | `concepts/coding-agents/agentic-coding` |
| `concepts/chatgpt-memory-bitter-lesson` | `concepts/gpt/chatgpt-memory-bitter-lesson` |
| `concepts/google` | `entities/google` |
| `concepts/nvidia` | `entities/nvidia` |
| `concepts/meta` | `entities/meta` |
| `concepts/nous-research` | `entities/nous-research` |

Truly missing (skip — no reliable page): `blog`, `git`, `attention-mechanism`,
`newsletter`, `benchmark`, `gan`, `differential-privacy`, `distillation`,
`quantization`, `vim`.

## Script locations

- Raw script: `/opt/data/scripts/fix_broken_wikilinks.py` AND
  `~/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_broken_wikilinks.py`
  (NOT `~/ai-topics/scripts/`).
- Safe fixer: `scripts/fix_empty_wikilinks_safe.py` in this skill
  (`--apply` to write, dry-run default, `--verify` to recount).
