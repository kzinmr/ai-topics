# Dreaming Pipeline Captured Blog Content Before Blog-Ingest (Overnight Gap)

> ⚠️ **SKILL.md size limit reached (100K+) — this file documents a cross-pipeline dedup pattern that couldn't be added inline. When SKILL.md is next trimmed/split, merge this content into the "Cross-pipeline dedup" subsection under §3. Coverage Gap Analysis.**

## The Pattern

The dreaming pipeline runs at **18:00-18:20 UTC** daily:
- dreaming-collect (18:00) → dreaming-group (18:10) → dreaming-wiki-ingest (18:20)

Blog-ingest runs at **07:00 UTC** the next morning.

Content published in the evening window (~**09:00-17:00 UTC**, after blog-ingest's daily RSS scrape but still within dreaming's `raw/articles/` backlog window) may be:

1. Scraped by blogwatcher and saved to `raw/articles/` (after 07:00 UTC RSS scrape)
2. **Not yet processed by blog-triage** (which runs at 07:30 UTC next day)
3. **But already picked up by dreaming** (which processes raw/articles backlog at 18:00 UTC)
4. Dreaming enriches the content into concept/entity pages
5. Blog-ingest scrapes the same article via RSS the next morning
6. Blog-triage finds it already processed

## Concrete Example (June 2026)

| Timestamp (UTC) | Event |
|----------------|-------|
| Jun 21 ~12:00 | Simon Willison publishes "Temporary Cloudflare Accounts for AI agents" |
| Jun 21 07:00 | Blog-ingest RSS scrape — misses the article (published after scrape) |
| Jun 21 18:10 | Dreaming-group processes `raw/articles/` backlog — finds the Cloudflare article |
| Jun 21 18:20 | Dreaming-wiki-ingest enriches `concepts/cloudflare-agents.md` with Cloudflare section |
| Jun 22 07:00 | Blog-ingest RSS scrape — now discovers the Cloudflare article |
| Jun 22 07:30 | Blog-triage runs — greps `log.md` for Jun 21, finds "Dreaming Wiki Ingest" with Cloudflare entry |

**Result:** The blog-triage correctly marked it as `skip` (already processed).

## Detection at Blog-Triage Time

```bash
# Step 1: Check yesterday's dreaming entries
grep "$(date -d 'yesterday' +%F)" ~/ai-topics/wiki/log.md | grep -i "dreaming" | head -5

# Step 2: Check for the specific topic keyword across all dreaming entries
grep -i "Dreaming Wiki Ingest" ~/ai-topics/wiki/log.md | grep -i "cloudflare\|topickeyword"

# Step 3: Verify the concept/entity page actually existed from yesterday
grep -i "topickeyword" ~/ai-topics/wiki/concepts/*.md ~/ai-topics/wiki/entities/*.md 2>/dev/null | head -5
```

## Action When Detected

1. **Default → mark blog version as `skip`**: The dreaming enrichment already created/updated concept/entity pages. No duplication needed.
2. **Exception — unique author commentary → mark as `reference`**: If the blog article contains **the author's personal hands-on commentary** not captured in the dreaming source (e.g., Simon Willison's GPT-5.5 xhigh test results vs a bare Cloudflare announcement), add the blog version as a `reference` entry to the author's entity page with a `[[concepts/concept-name]]` cross-wikilink. This captures the blog pipeline's unique value (author voice) without duplicating concept page enrichment.

## Distinction from Similar Patterns

| Pattern | Pipeline Window | Dedup Basis |
|---------|----------------|-------------|
| raw-backlog-ingest dedup | Runs at 0,4,8,12,16,20 UTC (6x/day) | Individual raw article processes logged separately |
| Dreaming overnight dedup | Runs once at 18:00-18:20 UTC | Deep enrichment (multiple entity/concept pages) logged as single large entry |
| Sitemap-monitor dedup | 06:00 UTC daily | Same-morning overlap with newsletter-triage |

Dreaming's enrichments are **deeper** than raw-backlog-ingest (multiple entity/concept pages updated per session) and appear as a single large log entry, not individual raw article processes.
