# Triage Builder Script: ASCII-Quote SyntaxError (Nov 2026)

## The failure

`write_file` → `/tmp/build_blog_triage_20261106.py` returned:

```
lint: SyntaxError: unterminated string literal (detected at line 132) (line 132, column 80)
```

Line 132 was a **pure-ASCII English** `body_excerpt` field quoting article text:

```python
"We usually call them "rows" or "records" instead, but they're definitionally global variables..."
```

The existing skill warning frames this as a *Japanese-literal* problem ("embedded ASCII double-quotes inside Japanese string literals give a misleading `SyntaxError: invalid decimal literal`"). It is **not** Japanese-specific: any ASCII `"` inside a double-quoted Python literal is a syntax error, regardless of the surrounding language. `body_excerpt` is the most common offender precisely because it quotes source articles, which are full of `"..."`.

The error message is unhelpful (`unterminated string literal` / `invalid decimal literal` depending on what follows the stray quote) and the character is hard to spot in a 15–20 KB builder script with CJK scattered through it.

## The fix (apply always, not just on failure)

In triage builder scripts, **never** put ASCII `"` inside string literals:

| Content | Do this |
|---|---|
| Quotes from the source article | Drop the quotation marks, or wrap the phrase in `'...'` / 「」 |
| Japanese terms / labels | 「」 (already skill guidance) |
| Star ratings | Build as `"*" * stars` from an `mk(...)` helper, not a literal `"★★★★☆ ..."` |
| Emoji in titles (🫧, 🖱️) | Describe in words: `"Breaking: Mayhem in the market (bubble emoji)"` |
| Shell-y fragments in `body_excerpt` | Fine — only `"` and the literal's own delimiter matter |

`body_excerpt` is REQUIRED for every decision and must quote the article, so this is not avoidable-by-omission — it's an authoring convention.

## Workflow that caught it cheaply

`write_file` runs `ast.parse` lint automatically. Writing the builder to `/tmp/` **first** surfaced the SyntaxError at write time, so `terminal python3` never ran a broken script. Sequence:

1. `write_file` → `/tmp/build_blog_triage_{run_id}.py` (unique filename per pipeline — sibling subagent race, see SKILL.md)
2. Read the lint output. If `SyntaxError`, fix the quote characters and re-write (don't try to run it).
3. `terminal` → `python3 /tmp/build_blog_triage_{run_id}.py`
4. Verify with the no-pipe `python3 -c` one-liner over the hardcoded triage path — check decision count, take/ref/skip split, **and** that no `body_excerpt` / `reason_ja` is empty.

Step 4 caught nothing this time but is the guard against the `null`/`None` and duplicate-decision pitfalls.

## Related hygiene from the same run (Nov 6 2026, blog-triage, 20 candidates)

- **Same-day dedup is the dominant skip signal.** Dwarkesh's 24.5 KB Clocktower article looked like the batch's biggest take, but `concepts/ai-benchmarks/blood-on-the-clocktower-dwarkesh.md` had been created *earlier the same morning* by the blog-ingest commit (`git log --oneline -- wiki/log.md` → `wiki: blog-ingest 2026-11-06 — 20 raw articles ... Clocktower benchmark concept`). Checked `head -40` + `tail` of the page and the entity page's `sources` frontmatter before deciding skip. Always run the `git log` / log.md same-day check **before** reading big articles in depth — it reorders the work.
- **`entities/openai.md` covered GPT-6 Cyber's headline numbers but the model had no dedicated page** — the "fresh `updated:` date ≠ full coverage" pattern. The take was an *existing-page-adjacent new page* (`concepts/gpt/gpt-6-cyber.md`), justified by concrete unrecorded specifics (RemoteExploitBench 100%-refuse-vs-95%-complete, Preparedness High→Critical, Dragos xOT, PSP). Grep the umbrella entity page for the article's *specific* benchmark names, not the model name.
- **`archive_triage.py` prints `/opt/data/.hermes/home/ai-topics/...`** — looks like the nested-path trap, is a symlink. `readlink -f` → `/opt/data/ai-topics`. Do not relocate. (Already noted in SKILL.md; reconfirmed.)
- Batch-skip entries (6 non-AI blogs collapsed into one decision) keep the decisions array at 15 for a 20-candidate batch without losing per-article `body_excerpt` evidence — concatenate the individual excerpts with ` | ` separators inside the single batch entry.
