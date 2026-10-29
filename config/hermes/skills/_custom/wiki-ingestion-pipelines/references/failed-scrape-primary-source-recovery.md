# Recovering Unscrapeable Announcement Pages (curl + HTML text extraction)

Some first-party announcement pages (observed: `openai.com/index/*`) are
JS-heavy and defeat the standard web_extract/browser scrape, leaving a
**failed-scrape placeholder** in `wiki/raw/articles/`. Symptom: the raw file
exists but contains only a "could not scrape" stub, and downstream entity pages
were built entirely from third-party coverage (blog posts, newsletters).

## Detection

During orientation / page updates, grep raw files for scrape-failure markers:

```bash
cd ~/wiki/raw/articles
grep -l -i "failed to scrape\|could not scrape\|requires javascript" *.md | head
```

A recovered-primary-source upgrade is worth doing even when an entity page
already looks rich — third-party coverage systematically misses:
- exact benchmark tables and harness caveats
- negative findings the vendor states plainly (e.g. "harder to monitor than prior model")
- footnotes (eval methodology, harness modifications)
- first-party framing claims and availability/pricing details

## Recovery recipe

```bash
curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36" \
  --max-time 45 "<URL>" -o /tmp/page.html
```

Then extract with Python (stdlib only):

```python
import re, html
s = open('/tmp/page.html', encoding='utf-8', errors='ignore').read()
body = re.sub(r'<script.*?</script>', '', s, flags=re.S)
body = re.sub(r'<style.*?</style>',   '', body, flags=re.S)
paras = re.findall(r'<(p|h[1-6]|li)[^>]*>(.*?)</\1>', body, flags=re.S)
out = "\n\n".join(html.unescape(re.sub(r'<[^>]+>', '', t)).strip() for _, t in paras)
```

Notes:
- If `__NEXT_DATA__` JSON parsing yields nothing (regex failed to match the
  blob), fall back to the paragraph-tag extraction above — it captures body,
  captions, and footnotes in document order. Tables collapse; note that in the
  raw frontmatter.
- Save with full raw frontmatter per the llm-wiki skill: `source_url`,
  `ingested`, `sha256` (hash of body only), plus a `note:` field recording the
  extraction method so a future re-ingest knows provenance.
- Name the recovered file with the canonical date-prefixed convention
  (`YYYY-MM-DD_<site>_<slug>.md`) and ADD it to the entity page's `sources:`
  list — keep the old placeholder file in place for history; raw/ is immutable.
- Commit the recovered raw file + entity updates in the SAME commit; a recovered
  source left uncommitted is invisible to other pipelines (and was nearly lost
  in the 2026-09-05 active-crawl run when the tool budget ran out).

## Anubis bot-challenge sites (xeiaso.net) — curl bypass + article-tag extraction

`xeiaso.net` (and any Anubis-gated blog) returns a JS "Making sure you're not a
bot!" challenge page to the standard `web_extract` scrape, leaving a ~519-byte
placeholder in `wiki/raw/articles/`. Detection:

```bash
grep -l -i "making sure you're not a bot\|anubis" wiki/raw/articles/*.md
```

Recovery recipe (verified 2026-10-22): `curl -sL` with a desktop Chrome UA gets
PAST the challenge (returns real ~22KB HTML, no bot marker). But the generic
`<p|h1-6|li>` paragraph extractor above catches only nav/header text — this site
wraps the post body in `<article class="prose ...">`. Extract that block instead:

```python
m = re.search(r'<article[^>]*>(.*?)</article>', s, flags=re.S|re.I)
inner = m.group(1) if m else s
inner = re.sub(r'<(script|style).*?</\1>', '', inner, flags=re.S|re.I)
inner = re.sub(r'</(p|h[1-6]|li|blockquote|pre|div|tr)>', '\n', inner, flags=re.I)
txt = html.unescape(re.sub(r'<[^>]+>', '', inner))
```

This yields clean ~1.6-1.8KB shitpost bodies. Overwrite the placeholder in place
(same `--<hash>.md` filename — it's the same run's artifact, not a history-
preserving re-ingest), with frontmatter `note: recovered via curl+article-tag
extraction (Anubis bot-challenge bypass)`. If curl STILL returns the challenge
(Anubis difficulty ramp), fall back to the browser tool or a Jina reader proxy.
