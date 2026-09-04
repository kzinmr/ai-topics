# Newsletter Triage Workflow

## URL Resolution Techniques

### Substack Newsletters
The raw newsletter files contain tracking/redirect URLs, NOT canonical article URLs. Use these patterns to find the real article:

**Pattern 1 — Canonical post URL** (most reliable):
Look for `open.substack.com/pub/{publication}/p/{slug}` in the raw file (typically Link 7 or Link 9).
Example: `https://open.substack.com/pub/bensbites/p/building-gets-easier`
→ Canonical form: `https://www.bensbites.com/p/building-gets-easier`
→ Also works: `https://open.substack.com/pub/{publication}/p/{slug}` directly with web_extract

**Pattern 2 — Redirect links** (`substack.com/redirect/2/eyJlIj...`):
These resolve to the Substack app download page, NOT the article. **Do NOT use these.**

**Pattern 3 — App-link URLs** (`substack.com/app-link/post?publication_id=...`):
These are email tracking links. Extract `publication_id` and `post_id`, then construct:
`https://open.substack.com/pub/{publication}/p/{slug}`

To determine `{publication}` (the unique slug):
- From the newsletter source_name (e.g., "The Signal" → `thesignal`, "Ben's Bites" → `bensbites`)
- From `open.substack.com/pub/{publication}/p/...` URLs elsewhere in the same raw file (Pattern 1)
- As fallback: `web_extract` the app-link URL directly — it redirects to the post which reveals the publication slug in the final URL
- Use the `next=` parameter if present in redirect URLs (e.g., `next=https://thesignal.substack.com/p/how-to-run-claude-cowork-from-your` reveals both publication and slug)

**Pattern 4 — Newsletter body extraction** (CRITICAL when raw digests only have tracking URLs):
Raw newsletter files from cron/process_email.py contain only extracted link URLs, NOT the newsletter body text. The real article links shared in the newsletter are inside the post body ON substack. After resolving the newsletter post URL (Pattern 1/3), call `web_extract` on it to get the full post text — this reveals the actual article links the author curated, with their titles and descriptions.

**Pattern 5 — Schema.org metadata extraction** (fast triage without full scrape):
When you only need metadata (title, description, author, paywall status) for classification, extract schema.org JSON-LD from the HTML without parsing the full page body. This works even for paywalled articles where the body isn't in the initial HTML.

```bash
# Download the page
curl -sL "https://open.substack.com/pub/{publication}/p/{slug}" -o /tmp/article.html

# Extract key fields (works for all Substack pages)
grep -oP '"description":"[^"]*"' /tmp/article.html | head -1
grep -oP '"headline":"[^"]*"' /tmp/article.html | head -1
grep -oP '"name":"[^"]*"' /tmp/article.html | head -3  # Author + publication
grep -oP '"isAccessibleForFree":[a-z]*' /tmp/article.html | head -1
grep -oP '"datePublished":"[^"]*"' /tmp/article.html | head -1
grep -oP '"userInteractionCount":[0-9]+' /tmp/article.html | head -3  # Likes, shares, comments
```

The `description` field is especially valuable for triage — it's the author's own summary, typically 1-2 sentences. The `isAccessibleForFree` field tells you whether to expect full body text or a paywall.

**Known limitation**: Fully paywalled Substack pages may have schema.org metadata but no body content in the HTML. Classify based on title + description alone. This was sufficient for accurate triage in 12/12 cases (July 2026 newsletter batch).

### Beehiiv Newsletters
Beehiiv uses `link.mail.beehiiv.com/v1/c/...` tracking URLs that encode the destination.

**Resolution method — `curl` with browser headers (preferred, fast)**:
```bash
curl -sS -L -o /dev/null -w "%{url_effective}" --max-time 8 \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml" \
  "https://link.mail.beehiiv.com/v1/c/..."
```
This resolves tracking redirects to canonical URLs (e.g., `getsuperintel.site/p/...`). Without browser-like headers, bare `curl` gets HTTP 403 from Cloudflare — the headers are essential.

**Fallback — Newsletter web version** (when Cloudflare blocks tracking links):
As of July 2026, Cloudflare's bot protection escalated — even full browser headers may return HTTP 403 with `cf-mitigated: challenge`. When this happens:

1. Find the `hp.beehiiv.com/{uuid}` link in the raw newsletter file — this is the public web version
2. Also check for `{publication}.site/p/{slug}` or `{publication}.com` web archive URLs
3. Scrape the web version instead — it contains the full newsletter body text with article titles, author analysis, and source references

```bash
# Find the web version link
grep -oP 'https://hp\.beehiiv\.com/[a-f0-9-]+' /path/to/raw/newsletter.md

# Scrape it
curl -sL 'https://hp.beehiiv.com/{uuid}' -o /tmp/beehiiv_page.html
python3 -c "
import re
with open('/tmp/beehiiv_page.html') as f:
    html = f.read()
html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
html = re.sub(r'<[^>]+>', ' ', html)
html = re.sub(r'\s+', ' ', html)
print(html[:8000])
"
```

**Known gotcha**: `hp.beehiiv.com` pages may also be paywalled — you'll get the free section (typically the intro + first 2-3 sections) but the rest requires a subscription. This is usually enough for triage classification.

**When all resolution fails**: If even `curl` with headers returns 403 and no web version exists, mark the newsletter as `manual_review_beehiiv_links_unresolvable` in triage output — downstream wiki-ingest should NOT attempt to scrape these.

**Historical note**: `curl` with headers worked for beehiiv from June 2026 until ~July 2026 when Cloudflare escalated protection. The web version fallback became the primary resolution path.

## Classification Criteria

| Level | Criteria | Examples |
|-------|----------|----------|
| **Critical** | Direct AI agent/LLM relevance, comprehensive landscape updates, major product launches | Codex SuperApp pivot, SemiAnalysis value capture analysis, frontier model benchmarks |
| **High** | Specific tooling/workflow coverage, industry context with wiki actionability | Claude Dispatch mobile patterns, hyperscaler capex analysis |
| **Medium** | Weekly roundups with 1-2 relevant items, single-topic coverage | True Positive Weekly, single blog post |
| **Low** | Noise, marketing fluff, no wiki actionability | — |

## Triage Output Format

### Ideal Schema (for manual triage)
```json
{
  "triage_timestamp": "ISO8601",
  "run_id": "from_cron",
  "newsletters": [
    {
      "message_id": "email_message_id",
      "subject": "newsletter_subject",
      "source": "Publication / Author",
      "date": "YYYY-MM-DD",
      "canonical_url": "resolved_canonical_url",
      "classification": "critical|high|medium|low",
      "summary": "3-5 sentence summary of key points",
      "wiki_relevance": "comma-separated wiki topic tags",
      "recommended_action": "specific wiki action (create page, enrich entity, etc.)"
    }
  ],
  "summary": {
    "total_newsletters": N,
    "critical": N,
    "high": N,
    "medium": N,
    "low": N,
    "key_themes": ["theme1", "theme2"],
    "recommended_wiki_updates": ["action1", "action2"]
  }
}
```

### Actual Cron Pipeline Format (as of July 2026)
The cron triage jobs produce a different shape than the ideal schema above. The real `triage_latest.json` uses:

```json
{
  "checkpoint_run_id": "20260703T071110Z",
  "summary_ja": "12ニュースレターをトリアージ。...(Japanese summary)...",
  "decisions": [
    {
      "item_id": "<email_message_id>",
      "source": "newsletter",
      "source_name": "Newsletter subject line",
      "title": "Short descriptive title for the triage item",
      "url": "https://resolved/canonical/url",
      "raw_path": "/opt/data/ai-topics/wiki/raw/newsletters/...",
      "recommended_action": "take|reference|skip",
      "reason_ja": "★★★★☆ Japanese explanation with star rating...",
      "candidate_wiki_path": "concepts/target-page.md",
      "body_excerpt": "Japanese summary of article content..."
    }
  ]
}
```

Key differences from ideal schema:
- **`decisions` array** instead of `newsletters` array
- **`recommended_action`** uses `take|reference|skip` (not `critical|high|medium|low`)
- **Star ratings** embedded in `reason_ja` text (★★★★★ = new concept page, ★★★★☆ = update existing, ★★★☆☆ = entity/reference, ★★☆☆☆ = marginal, ★☆☆☆☆ = skip)
- **`summary_ja`** (Japanese) instead of structured `summary` object
- **`candidate_wiki_path`** and `body_excerpt` are included for downstream wiki-ingest
- **`reason_ja`** is in Japanese — the triage agent writes explanations in Japanese

The `recommended_action` values map to wiki-ingest behaviors:
- `take`: Create new wiki page (★★★★★) or significant update (★★★★☆)
- `reference`: Enrich existing entity/concept page (★★★☆☆)
- `skip`: No wiki action (★★☆☆☆ or lower)

## Save Location
- Triage report: `/opt/data/.hermes/cron/data/triage/newsletter-triage-{timestamp}.json`
- Inbox copy: `/opt/data/ai-topics/wiki/raw/inbox/newsletter-ingest/{timestamp}.json`
