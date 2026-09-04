# Entity Research Fallback: Direct-Domain Curl When Delegated Research & Search Engines Fail

Validated 2026-08-07 while creating `entities/taalas.md` (AMD acquisition of Taalas) from a newsletter take.

## The failure cascade

1. **Delegated research subagent output truncation**: `delegate_task` with `toolsets: ["web"]` returned a 253K-char response that was truncated in the sandbox — the fact sheet never made it back intact. The subagent also dumped raw HTML into its summary instead of a condensed fact sheet.
2. **Subagent /tmp work does not persist**: the subagent created `taalas_research/` with fetched HTML, but the directory was gone when the parent checked (`find / -maxdepth 4 -name taalas_research` → empty). **Never rely on files a research subagent claims to have written — only its summary is guaranteed to survive.**
3. **Search engines all bot-blocked**: DuckDuckGo HTML endpoint returned a CAPTCHA/anomaly page; Bing returned a challenge; Google returned a 107-byte stub; TechCrunch URL guess 404'd; TechCrunch WP-JSON search API returned empty.

## The working fallback: curl the entity's own domain directly

The company's own homepage is usually NOT bot-blocked (it wants visitors). Sequence that worked:

```bash
curl -sL --max-time 25 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36" "https://taalas.com" -o /tmp/taalas_home.html
```

Then strip HTML to text with Python (NOT `curl | grep` — the pipe-to-interpreter scanner blocks it):

```python
import re, html
h = open('/tmp/taalas_home.html', encoding='utf-8', errors='ignore').read()
text = re.sub(r'<script.*?</script>', '', h, flags=re.DOTALL)
text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', text)
text = html.unescape(text)
text = re.sub(r'\s+', ' ', text)
# find the meaningful section past the Lottie animation JSON blob
idx = text.find('<company-name> is creating')
print(text[idx:idx+4000])
```

**Pitfall**: marketing homepages embed a huge Lottie animation JSON blob (`{"v":"5.7.12","fr":30,...}`) in a `<script>` — the naive text-strip prints thousands of chars of animation keyframes first. Search for the company-name anchor phrase (e.g. `text.find('Taalas is creating')`) rather than printing from the top.

**Yield**: taalas.com homepage alone gave the tagline ("The Model is The Computer"), the product concept (Hardcore Models, ~1000× efficiency claim, Taalas Foundry, fine-tuning support) — combined with the newsletter body excerpt (acquisition announcement + official X quote), this was sufficient to build a quality entity page. The homepage is a *primary source* for the entity's own claims, which is exactly what an entity page needs.

## Guidelines for entity-page creation with blocked research

1. Try `delegate_task` research first, but **instruct the subagent to return a compact structured fact sheet (≤ ~1-2KB), explicitly forbidding raw HTML dumps** in the summary. 253K-char truncation loses the result.
2. If search engines are bot-blocked, **skip them entirely** — go straight to `curl` of the entity's own domain (homepage, /products/, /about/, /blog/).
3. Supplement with the article/newsletter body excerpt already in the triage (the newsletter often quotes the official announcement verbatim — Taalas's official X post was quoted in full in AINews).
4. Mark uncertain facts (financial terms, founder details) as "not disclosed in the announcement" rather than guessing — an entity page with verified tagline + verified acquisition event + explicitly-unknown terms is better than fabricated details.
5. For a brand-new entity page, keep it to a verified core (~30-50 lines): overview, official positioning, the acquisition/event, significance, related pages. Depth can come later via enrichment.

## Related
- Prefer this fallback over repeated `curl` attempts at search engines — DDG/Bing/Google challenges do not resolve on retry.
- The homepage text-strip recipe also works for `/products/`, `/about/`, and other static pages on the same domain.
