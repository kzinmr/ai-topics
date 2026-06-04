# Newsletter Triage Workflow

## URL Resolution Techniques

### Substack Newsletters
The raw newsletter files contain tracking/redirect URLs, NOT canonical article URLs. Use these patterns to find the real article:

**Pattern 1 — Canonical post URL** (most reliable):
Look for `open.substack.com/pub/{publication}/p/{slug}` in the raw file (typically Link 7 or Link 9).
Example: `https://open.substack.com/pub/bensbites/p/building-gets-easier`
→ Canonical form: `https://www.bensbites.com/p/building-gets-easier`
→ Also works: `https://open.substack.com/pub/{pub}/p/{slug}` directly with web_extract

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

### Beehiiv Newsletters
Beehiiv uses `link.mail.beehiiv.com/v1/c/...` tracking URLs that encode the destination.
**Resolution method**: Call `web_extract` directly on the beehiiv tracking URL — the server follows the redirect chain and returns the actual article's title and full content body. This is more reliable than searching by subject line.
Fallback: Search the subject line + date via web_search to find the canonical article URL.
Example: Subject `$700 Billion AI Bet, One Earnings Night` → web_extract(beehiiv_url) → returns the full earnings analysis article

## Classification Criteria

| Level | Criteria | Examples |
|-------|----------|----------|
| **Critical** | Direct AI agent/LLM relevance, comprehensive landscape updates, major product launches | Codex SuperApp pivot, SemiAnalysis value capture analysis, frontier model benchmarks |
| **High** | Specific tooling/workflow coverage, industry context with wiki actionability | Claude Dispatch mobile patterns, hyperscaler capex analysis |
| **Medium** | Weekly roundups with 1-2 relevant items, single-topic coverage | True Positive Weekly, single blog post |
| **Low** | Noise, marketing fluff, no wiki actionability | — |

## Triage Output Format

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

## Save Location
- Triage report: `/opt/data/.hermes/cron/data/triage/newsletter-triage-{timestamp}.json`
- Inbox copy: `/opt/data/ai-topics/wiki/raw/inbox/newsletter-ingest/{timestamp}.json`
