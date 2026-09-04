# Subagent Enrichment Source Format Pitfall

When using `delegate_task` to enrich wiki entity or concept pages in parallel, subagents may add the new article's URL to the frontmatter `sources` array with **incorrect formatting** — typically backtick-wrapped raw paths (`` `raw/articles/...` ``) instead of proper markdown links (`[Title](url)`) or plain unformatted paths (`raw/articles/...`).

## Error Pattern

```yaml
# ❌ SUBAGENT PRODUCES THIS:
sources:
  - `raw/articles/simonwillison.net--2026-jul-14-pedalican--5bb96ce4.md`

# ✓ CORRECT FORMAT (markdown link, preferred):
sources:
  - [Simon Willison: Codex Desktop pets (Pedalican)](https://simonwillison.net/2026/Jul/14/pedalican/)

# ✓ CORRECT FORMAT (bare path, acceptable):
sources:
  - raw/articles/simonwillison.net--2026-jul-14-pedalican--5bb96ce4.md
```

## Detection

After subagent enrichment, verify source formatting:
```bash
head -15 wiki/<namespace>/<file>.md | grep -A5 "sources:"
```

## Observed Fix (2026-07-15)

Blog-wiki-ingest subagent enriched `concepts/codex/codex-superapp.md`. Backticked raw path discovered during post-enrichment verification. Fix applied via `patch()`:

```yaml
old_string: '`raw/articles/simonwillison.net--2026-jul-14-pedalican--5bb96ce4.md`'
new_string: '[Simon Willison: Codex Desktop pets (Pedalican)](https://simonwillison.net/2026/Jul/14/pedalican/)'
```

## Prevention

In `delegate_task` context, explicitly tell subagents: "Add source entries as markdown links with proper titles, not as backtick-wrapped raw paths."
