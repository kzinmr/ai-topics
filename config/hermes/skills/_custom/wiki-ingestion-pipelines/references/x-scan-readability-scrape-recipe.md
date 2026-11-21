# X Accounts Scan — Raw Article Scrape Recipe (no web_extract)

When the `x-accounts-scan` cron delivers `new_posts` with `external_urls`, this profile has
NO `web_extract` tool. Save scraped articles to `wiki/raw/articles/` with this recipe
(verified 2026-11-13 x-accounts-scan run, 3/3 URLs succeeded).

## Recipe

`requests` + `readability-lxml` (`from readability import Document`) + `beautifulsoup4` are
installed in the profile venv. `trafilatura` is NOT. Do NOT write a new scraper — reuse this
pattern:

```python
import re, hashlib, datetime, requests
from readability import Document
from bs4 import BeautifulSoup

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) ... Chrome/120 Safari/537.36"}

def slugify(url, title):
    from urllib.parse import urlparse
    host = urlparse(url).netloc.replace("www.", "")
    t = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50]
    h = hashlib.md5(url.encode()).hexdigest()[:8]
    return f"{host}--{t}--{h}.md"   # matches existing raw/articles naming convention

r = requests.get(url, headers=UA, timeout=30); r.raise_for_status()
doc = Document(r.text)
soup = BeautifulSoup(doc.summary(), "html.parser")
text = soup.get_text("\n", strip=True)
# frontmatter: title / source_url / fetched (today) / type: raw-article
# save to /opt/data/ai-topics/wiki/raw/articles/<slugify(url,title)>
```

Write the script with `write_file` to `/tmp/scrape_x.py`, run via `terminal python3 ...`
(works fine here; no execute_code gate needed for this).

## Notes & pitfalls

- Filename convention `{host}--{slug}--{md5[:8]}.md` matches the existing corpus
  (e.g. `corbt.com--the-machine-starts--19c6639b.md`). Entity pages reference these via
  `[[raw/articles/<filename>]]`.
- The scan payload's `links[].title` already gives a good title, but re-deriving via
  `Document.short_title()` keeps title/filename consistent. Anthropic titles come with a
  trailing `" \\\\ Anthropic"` suffix — harmless, kept as-is.
- readability output may contain mojibake (`â` for em-dash/curly quotes) when the page
  charset isn't picked up. Acceptable for raw layer (immutable); clean quotes when writing
  the concept/entity page, not the raw file.
- Anthropic research posts and claude.dev blog posts scrape cleanly with readability
  (~18-21k chars). Fiction/long-form (corbt.com ~58k chars) also fine.
- After scraping: create/update concept + entity pages, update `index.md` (both the
  `> Total pages:` line AND the `## Concepts (N pages)` section header) and prepend a
  `log.md` entry, then `git add wiki/ && git commit && git push`.
  ⚠️ `git add wiki/` in a shared repo may sweep sibling cron output (observed: 12
  newsletter raw files got swept into the x-scan commit — not harmful, but write commit
  messages that match what was actually staged, or stage explicit paths).

## Index page-count bookkeeping

`wiki/index.md` line ~4 has `> Total pages: N` and each section header has
`## Concepts (N pages)`. Increment both by the number of NEW pages created (patch/replace
via sed is fine). The pre-commit hook validates index consistency but NOT wikilinks —
check `[[...]]` targets exist before committing (see
`references/pre-commit-wikilink-verification.md`).

## Dedup before creating concept pages

Before creating a new concept page from a scanned post, grep `wiki/index.md` and
`wiki/concepts/` for the topic — Anthropic posts often overlap existing pages
(`sleep-time-compute`, `agent-wikis`, `wiki-memory`, `claude/fable-5`, etc.). Prefer
linking new pages into that cluster via `related:` rather than duplicating; e.g. the Nov
2026 "components of agent memory" post became `concepts/components-of-agent-memory.md`
linked from `sleep-time-compute` territory, and the 1,000-agent FLT post became
`concepts/fable-5-2-1000-agent-flt-formalization.md` linked from `claude/fable-5`.
