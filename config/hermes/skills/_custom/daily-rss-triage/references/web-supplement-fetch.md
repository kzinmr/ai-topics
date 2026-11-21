# Web Supplement Fetch — robust recipes for Phase 1b supplementation

Verified 2026-08-10 (trending-topics cron run). Use when the RSS scan yields few
AI-relevant articles, or when you need breaking headlines beyond the pipeline
(model releases, security incidents, HN front-page signals).

## 1. Verify delegated web_search actually ran

When using `delegate_task` with `toolsets: ['web']`, the subagent may return its
*plan* ("I'll search for X...") instead of executed results. Check the result object:

- `tool_trace: []` + only 1 API call → no searches were executed → discard and fall back.
- Do not burn turns retrying delegation blindly; go straight to direct fetch below.

## 2. Direct fetch pattern (works in cron; execute_code is blocked)

Write a Python script to `/tmp/` with `write_file`, run with `python3 /tmp/xxx.py`
via `terminal`. No shell pipes involved.

**Pitfall**: `curl ... | python3 -c ...` pipes are BLOCKED by the Hermes security
scanner (`tirith:curl_pipe_shell`, HIGH — "Downloaded content will be executed without
inspection"). Two safe alternatives:
  a) `curl -s -o /tmp/out.json URL` then read/parse the file in a separate step.
  b) Python urllib inside the script (no pipe at all — preferred).

**Pitfall (verified 2026-08-23)**: the security scanner also blocks `cat file.json |
python3 -c "import json,sys; ..."` on ANY local file — even a small checkpoint JSON
under `~/.hermes/cron/data/`. Pattern key: `tirith:pipe_to_interpreter` (HIGH, "Pipes
output from 'cat' directly to interpreter"). The 2026-08-16 warning that "even
`cat latest.json | python3 -c` is blocked" is not theoretical — it fired on a live
`~/.hermes/cron/data/blog_ingest/latest.json` read this run. Do NOT use cat-pipes for
checkpoint parsing. Use one of:
  - `json.load(open(...))` inside a script written to `/tmp/` with `write_file` (preferred),
  - read the file with `read_file`,
  - or `curl -s -o /tmp/out.json` / plain file copy, then parse in a separate step.

The scanner fires on the pipe syntax itself regardless of whether the input is remote
or local. The rule generalizes: never pipe anything into an interpreter; fetch/copy
to a file first, then parse it in a separate step.

## 3. Hacker News front-page recipe (top trending tech signal)

```python
import json, urllib.request, time

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode())

since = int(time.time()) - 3*86400
d = fetch(f"https://hn.algolia.com/api/v1/search?tags=front_page&numericFilters=created_at_i%3E{since}")
for h in d.get("hits", [])[:30]:
    print(f"- {h.get('points')} | {h.get('title','')[:110]} | {h.get('url') or '(ask)'}")
```

CRITICAL: the `>` in `numericFilters` must be URL-encoded as `%3E`. A raw `>` in the
URL (especially with shell expansion) → `400 Bad Request` from hn.algolia.com.

## 4. Generic page fetch (get article body when titles aren't enough)

```python
import urllib.request, re, html

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", errors="replace")

def strip_html(s):
    s = re.sub(r"<script[\s\S]*?</script>", " ", s)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()
```

Nav-heavy sites (claude.com, research.meta.ai) return navigation menus in the first
~2500 chars of stripped text — the article body follows the page title; read past the
menu (print `text[:2500]`, and the meaningful content starts after the title line).

**Pitfall (verified 2026-08-27, OpenAI post-mortem): the "filter lines > N chars" body
extraction silently returns 0 chars when the whole article is one text blob.** Some
sites (OpenAI, most JS-rendered SPA-style posts) strip to a single long line — the
header + entire article body are concatenated with no `\n`. A pattern like:

```python
lines = [l.strip() for l in t.split("\n") if len(l.strip()) > 40]
```

…produces a 1-element list and any `find("In July 2026")` against it returns -1 →
you write a 168-byte raw file with just the header. **Diagnosis:** if your
post-strip line count is < 5 and `len(body) < 500`, the article is a single blob.
**Fix:** use `str.find` on the raw stripped text (NOT on the line-filtered list) and
slice between the body-start marker and the footer marker:

```python
idx = text.find("In July 2026")          # first body sentence
end = text.find("2026 Alignment Authors") # footer / author line
body = text[idx:end]
```

The raw-file byte count should be ≥ 5KB for a substantial article; anything under
2KB is a near-certain extraction failure — re-extract before saving to
`wiki/raw/articles/`.

## 6. Substack newsletter triage: fetch the post body from the CUSTOM DOMAIN

Validated 2026-11-11 (newsletter-triage, 5 newsletters / 74 candidates). When a Substack
newsletter checkpoint's links are all email chrome (`submitLike`, `action=post-comment`,
`action=share`, `restack-comment`, `email-read-in-app`, `@author`, `subscribe-widget`,
`redirect/2/eyJ...` OAuth, `redirect/<uuid>`), do NOT resolve any token URL. The post slug is
already in the checkpoint's Link 7/8 URLs (`open.substack.com/pub/<pub>/p/<slug>?utm_...`) —
swap the host to the publication's custom domain and curl once:

```
https://www.lennysnewsletter.com/p/<slug>
https://www.bensbites.com/p/<slug>
https://www.hyperdimensional.co/p/<slug>
```

Batch 3-4 publications in one script (see §2: `write_file` → `terminal python3`):

```python
import subprocess, re
r = subprocess.run(["curl","-sL","--max-time","25",url], capture_output=True, text=True)
art = re.search(r'<article[^>]*>(.*?)</article>', r.stdout, re.DOTALL)
ps = [re.sub(r'<[^>]+>','',p).strip()
      for p in re.findall(r'<p[^>]*>(.*?)</p>', art.group(1), re.DOTALL)]
body = " ".join(p for p in ps if len(p) > 40)
```

- These Substack pages have **no `<title>` tag** — use the checkpoint `source_name` (for
  single-article Substack emails it IS the article title) plus the extracted `<article>` text.
- Custom-domain 404 / "Page not found" is itself a triage verdict (nothing substantive at that
  slug — e.g. `aiweekly.co` Hundred-Page RL book promo = chrome only) → reference/skip, don't
  chase tokens.
- "∙ Paid" posts still render 30+ free-preview `<p>` paragraphs with headline numbers. **Read the
  free preview before accepting an inbox summary's `importance: low` on a data-bearing essay.**
  Lenny's "State of the tech job market: late 2026" was inbox-classified "peripheral/perishable
  skip"; the preview's PM-openings +75%, +56% vs engineers +43%, PM hiring share 16%→21% made it a
  ★★★★☆ take.
- Beehiiv counterpart: if the inbox pre-triage summary already lists `resolved_links` +
  `existing_coverage`, do NOT re-resolve the ~20 `link.mail.beehiiv.com/v2/c/` URLs — trust it for
  topic ID, verify coverage on disk (saved ~17 `web_extract` calls).

## 7. Coverage ladder for a model/product release (triage-side)

grep across `entities/ concepts/ events/`, then:

1. Page exists **with the article's specific numbers** → `reference` (sibling pipeline won).
2. Only **sibling generations** exist (`muse-spark`/`muse-glimmer`/`meta-muse-spark` present,
   `muse-ember` absent) → **take**. Family-name grep hits are false-positive coverage.
3. `log.md` hit **+ tag already minted in `wiki/SCHEMA.md`** (e.g. `muse-ember` minted 2026-11-10)
   but **zero page bodies anywhere** → strongest take signal: a prior run registered the taxonomy
   and never made the page. Check `grep -n "<kw>" wiki/SCHEMA.md` alongside log.md.
4. Zero hits → take only if a raw article body exists (blog-ingest's
   `raw/articles/<blog>--<date>--<slug>--<hash>.md` often carries the full body when the
   newsletter's own raw is chrome-only).

Honour an "already ingested by sibling pipeline" claim only after grepping the section heading
**and** its figures (`grep -n "5.2" concepts/claude/fable-5.md` → FrontierCode 2.0 49.1%;
`grep "8tx" entities/google-tpu.md` → dedicated Nov 9 section). A fresh `updated:` date alone never
justifies downgrading a lead story to `reference`.

`archive_triage.py <pipeline> --keep-reference` prints a nested-looking
`/opt/data/.hermes/home/ai-topics/wiki/raw/archived/...` path — it is a symlink;
`readlink -f` → `/opt/data/ai-topics`. Commit the archive file + `archive_index.json` as-is.

## 5. Cross-referencing before wiki work

The wiki-ingest pipelines (newsletter-wiki-ingest ~07:40, blog-wiki-ingest ~07:50,
x-bookmarks-ingest, active-crawl) usually run BEFORE trending-topics (~12:00 UTC).
Before proposing new wiki pages, grep the index for today's topics:

```bash
cd /opt/data/ai-topics/wiki && grep -inE "topic|entity" index.md | head -20
```

If the entry exists with today's date, reference the existing page in the report
instead of creating a duplicate.
