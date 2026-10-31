# Batch Wikilink Target Verifier (dreaming / wiki-ingest post-write gate)

Verifies every `[[target]]` in the pages you just created/edited resolves to a
real file, and flags ghost links before commit. The pre-commit hooks do NOT
check wikilink targets, so this is the only gate.

## Usage

```bash
cd ~/ai-topics/wiki && bash ../config/hermes/skills/_custom/dreaming/scripts/check_wikilinks.sh \
  concepts/llm-expertise-amplification.md entities/sakana-ai.md entities/modal-labs.md
```

Pass page paths relative to `wiki/` (no leading `wiki/`, no `.md`). Run it from
the `wiki/` directory so the `[ -f ]` test resolves correctly.

## Why not `find -e`

`find wiki -e "wiki/$t.md"` does **not** test existence — `-e` is parsed as a
predicate/option, so every link reports MISSING even when all files exist. Use
the plain bash `[ -f "$t.md" ]` loop below.

## Why alias-stripping matters

`grep -o "\[\[[^]|]*"` strips both the `[[` and any `|alias` in one pass. The
older `sed 's/\]\]//'` variant leaves stray brackets and mis-tests every aliased
link. (Same bug class as the hermes-report-quality checker's `[[a|b]]` MISS
flood.)

## Ghost-link recovery

When a target reports MISSING, do NOT create a stub to satisfy it. Sweep for the
real page and retarget:
```bash
cd ~/ai-topics/wiki && find concepts entities -iname '*<kw>*'
```
Common ghost → real mappings (validated 2026-10-29):
- `concepts/ai-copyright-and-fair-use` → `concepts/ai-music-copyright.md`, `concepts/anthropic-copyright-settlement.md`
- `concepts/quantization` → `concepts/model-quantization.md` (+ `gguf-quantization`, `post-training/quantization-overview`, `local-llm/model-quantization`)
- `concepts/alignment-faking` / `concepts/ai-transparency` → `concepts/evaluation/llm-evaluation-harness.md`, `concepts/ai-sycophancy.md`, `concepts/ai-content-transparency.md`
- `concepts/alignment` → `concepts/ai-alignment`; `concepts/ai-safety` → `concepts/security-and-governance/ai-safety`

Always sweep RECURSIVELY from the wiki root — pages live under `concepts/coding-agents/`,
`concepts/evaluation/`, `concepts/post-training/`, `concepts/ai-benchmarks/`,
`concepts/local-llm/`, `concepts/sandbox/`, and a top-level-only scan falsely
reports them missing.
