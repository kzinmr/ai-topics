# Newsletter Take Body Fetch Pattern (cron-mode)

When `newsletter-wiki-ingest` processes a `take`, the raw newsletter digest
(`wiki/raw/newsletters/*.md`) contains only tracking/redirect URLs — NOT the article body.
The triage JSON's `url` field usually already holds the **canonical article URL** resolved by
the triage agent (substack post URL, or beehiiv-hosted article URL like
`read.getsuperintel.com/p/{slug}`). The ingest agent must fetch the body itself before enriching.

Validated 2026-08-16 (Flue 2 Latent Space interview + Superintel+ GLM-5.3 deepdive) and
2026-08-20 (AINews "Death of Params" GLM 5.3 post, 42 paras).

## Working Pattern

Cron mode blocks `execute_code` with subprocess and heredoc scanners block inline Japanese —
use the standard `write_file` → `/tmp/script.py` → `terminal python3` path. Use a **unique
filename** (pipeline + date); sibling subagents race on `/tmp/` in the 07:00-07:50 parallel
window. If `write_file` warns the file was modified by a sibling, verify your content is intact
(`head -5`) before running — `bytes_written` matching your input is a good check.

Script: curl with a browser User-Agent → JSON-LD title + `<article>`/`<p>` paragraph extraction
→ save JSON → print first ~25 paragraphs → read the rest from the saved JSON. Never read a
600KB HTML file directly; read the extracted JSON instead.

```python
#!/usr/bin/env python3
import subprocess, re, html, json

def fetch(url, timeout=20):
    r = subprocess.run(["curl", "-sL", "-A",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
        url], capture_output=True, text=True, timeout=timeout)
    return r.stdout

def extract_article(html_text):
    out = {"title": None, "article_paras": []}
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html_text, re.DOTALL):
        try:
            d = json.loads(m)
            if isinstance(d, dict) and d.get('headline'):
                out["title"] = d.get('headline')
        except Exception:
            pass
    art = re.search(r'<article[^>]*>(.*?)</article>', html_text, re.DOTALL)
    body = art.group(1) if art else html_text
    for p in re.findall(r'<p[^>]*>(.*?)</p>', body, re.DOTALL):
        t = html.unescape(re.sub(r'<[^>]+>', '', p)).strip()
        t = re.sub(r'\s+', ' ', t)
        if len(t) > 30:
            out["article_paras"].append(t)
    return out

targets = {"slug1": "https://..."}
results = {name: extract_article(fetch(url)) for name, url in targets.items()}
for name, ext in results.items():
    print(f"=== {name} === TITLE: {ext['title']} paras={len(ext['article_paras'])}")
    for i, p in enumerate(ext["article_paras"][:40]):
        print(f"[{i}] {p[:500]}")
with open("/tmp/fetch_out.json", "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
```

After the first pass, read paragraphs 25+ from the saved JSON
(`python3 -c "import json; ..."` or a second small script) before writing the wiki section.

## Domain Characteristics (Aug 2026)

| Domain | curl behavior | Extraction | Notes |
|--------|--------------|------------|-------|
| substack custom domain (`www.latent.space/p/{slug}`, `open.substack.com/pub/...`) | 200 with browser UA | `<article>` tag present; JSON-LD `headline` works | Flue 2 interview: 42 paras; AINews Death-of-Params: 42 paras. First para is chat UI noise (author / date / share buttons) — strip manually |
| beehiiv-hosted article domain (`read.getsuperintel.com/p/{slug}`) | 200, ~640KB | **NO `<article>` tag**; JSON-LD title works; free-preview `<p>` extraction works | Paywall marker: "Subscribe to Superintel+ to read the rest" after ~17 paras → mark the section `(mostly paywalled, free preview used)` and only use free-preview claims |

For other domains, the `content-extraction-fallbacks.md` chain (BS4, tagged-text-block,
Jina Reader `r.jina.ai`) applies.

## Enrichment Integration

- Write wiki sections with **concrete quotes** from the fetched body (e.g. Flue 2: "There is
  no agent without a harness", "The best tools are the ones that float above the host").
- For paywalled previews (GLM-5.3 Superintel+ deepdive): capture the free-preview claims
  (uneven-gain mechanism, vendor-only-numbers caveat, "post-training has quietly become the
  main event") and note paywalled sections explicitly — do NOT guess their content.
- **Stale-`updated:`-date = likely gap**: check target entity pages' `updated:` dates. May 2026
  dates for a v2-release article = genuine gap even though the page exists (both `flue.md` and
  `fred-schott.md` were v1-only). Inverse of the "fresh date ≠ full coverage" pitfall.
- Add the resolved canonical URL + raw newsletter digest path to the page frontmatter `sources`.

## Operational notes from the same run

- **Archive no-op**: `archive_triage.py newsletter --keep-reference` may print
  `"All items already archived (dedup)"` with `archived: 0` when a prior pipeline run already
  committed the archive (check `git log --oneline` for a "wiki: archive newsletter triage ..."
  commit). Treat as idempotent no-op — do NOT force re-archive.
- **`git pull --rebase` fails with unstaged changes** when unrelated files are dirty
  (e.g. sibling blog-wiki-ingest entity pages, or `config/hermes/skills/` touched by
  skill-drift). If `git push` then succeeds anyway (no remote divergence), no action needed.
  Always `git add` the specific wiki files explicitly (never `git add .`) to avoid sweeping
  sibling changes into your commit.
- **Aug 20 2026**: archive script printed path under `/opt/data/.hermes/home/ai-topics/...` —
  that is a **symlink** to the canonical repo; `readlink -f` before reacting, do NOT move files.
