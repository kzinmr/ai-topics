# Ghost Entry Resolution: Directory Hubs & Case Variants (Session 2026-11-16)

Watchdog-fix run: 9 ghost candidates in index.md all resolved without deletions. Two distinct sub-patterns beyond the known `_index.md` / `|Display` / `→ redirect` / `_archive/` FPs.

## Sub-pattern 1: Directory-hub links use `index.md`, NOT `_index.md`

**Symptom**: Ghost candidates like `concepts/gpt`, `concepts/openai`, `concepts/anthropic`, `concepts/claude`, `concepts/gemini`, `concepts/ai-benchmarks`, `concepts/browser-agent`, `concepts/training` — referenced from 30+ L2 pages (`grep -rn '[[concepts/gpt]]' wiki/ --include='*.md' | grep -v raw/`) but no `wiki/concepts/<slug>.md` and no `wiki/concepts/<slug>/_index.md`.

**Root cause**: This wiki's directory-hub pages are named `index.md` (e.g. `concepts/gpt/index.md`, title "GPT Models", 43 child pages), NOT `_index.md`. Ghost scanners that only check `f'{slug}.md'` and `f'{slug}/_index.md'` falsely flag every dir-hub link.

**Correct ghost existence check**:
```python
exists = (os.path.exists(f'wiki/{s}.md')
          or os.path.exists(f'wiki/{s}/_index.md')
          or os.path.exists(f'wiki/{s}/index.md'))   # <- dir hub
```

**Fix = REGISTER, don't delete**: add one index.md line per dir hub, alphabetically within the Concepts section:
`- [[concepts/gpt]] — GPT Models — hub index for GPT model-family pages (43 pages under concepts/gpt/)`
Then bump the `## Concepts (N pages)` header by the inserted count (recount via `grep -c '^- \[\[concepts/' wiki/index.md`).

Verified dirs with `index.md` hubs (2026-11-16): ai-benchmarks (122 files), anthropic, claude (27), gemini (14), gpt (43), openai (23). `browser-agent/` and `training/` had NO hub file at all — their child pages were already individually indexed (`[[concepts/browser-agent/deep-research]]` etc.), so the bare dir link was a dangling reference from body text; registering a hub line for them still resolves the link (index entry acts as the anchor) — alternatively create the hub `index.md`.

## Sub-pattern 2: Case-variant slug → display-text fix

`[[entities/met]]` ghost while the real file is `entities/metR.md` (case-sensitive path check fails; index line was `- [[entities/metR]] — METR ...`).

**Fix**: rewrite the index entry to Obsidian display-text syntax so BOTH slugs resolve:
`- [[entities/met|entities/metR]] — METR (Model Evaluation & Threat Research) — ...`
Do NOT rename metR.md (git history, incoming `[[entities/metR]]` links elsewhere) and do NOT add a duplicate line.

## Tooling pitfalls hit this session

- `grep -c '[[foo]]' file` fails with "Unmatched [ — use `grep -F '[['` or Python. Bracket-literal counting: prefer Python `str.count` / `re`.
- Mixing shell grep checks and Python `re.findall` index-membership checks gave contradictory results on the same slug; converge on ONE Python-based verifier (`pat.findall(idx)` → set membership) for all indexed/not-indexed judgments.
- `log.md` prepend via `open().write(entry + content)` re-buries `# Wiki Log` below the new entry whenever the file's top isn't already header+blank+italic line — run `python3 ~/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py` LAST before commit (header was buried at line 11 this session).
- SKILL.md 100K hard limit: net-growing patches to this umbrella FAIL. Put new knowledge in `references/` and add only a one-line pointer, or net-shrink existing text.

## Commit hygiene used
`git add wiki/index.md wiki/log.md` (only touched files; other dirty skills files left alone) → pre-commit hook (validate_index.py + tag validator) passes → push. Commit msg: `wiki: auto-fix health issues — register 8 dir-hub links, fix met ghost entry`.
