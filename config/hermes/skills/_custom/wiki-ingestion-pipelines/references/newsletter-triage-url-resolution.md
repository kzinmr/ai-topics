# Newsletter Triage: URL Resolution & Classification Patterns

Practical patterns for resolving newsletter article URLs during the `newsletter-triage` cron job.

## URL Resolution by Newsletter Platform

### Substack (publication_id in URL)

Substack newsletters use two URL forms:

1. **Redirect links**: `substack.com/redirect/UUID?j=...` — opaque tracking redirects. Cannot be resolved via `curl -I` (return 403 or same URL). `web_extract` handles these natively.
2. **App links**: `substack.com/app-link/post?publication_id=...&post_id=...` — internal Substack app links. Also opaque.
3. **Direct post links**: `open.substack.com/pub/{author}/p/{slug}` — the canonical form. These resolve via HTTP redirect to the actual domain:
   ```
   open.substack.com/pub/swyx/p/flue-2  →  www.latent.space/p/flue-2 (200)
   ```
   Use `curl -sL -o /dev/null -w '%{url_effective}' <url>` to discover the actual domain.

**Resolution strategy**: Find the `open.substack.com` link in the article list (usually link 7 or 8), resolve it to get the actual publication domain, then use that domain for the raw article filename and entity page.

### Beehiiv (link.mail.beehiiv.com)

Beehiiv tracking links (`link.mail.beehiiv.com/v2/c/{hash}/{id}`) are **Cloudflare-challenged** — `curl` returns 403 with a JS challenge page. They cannot be resolved via CLI.

The main article URL is typically the second-to-last link in the newsletter, formatted as `hp.beehiiv.com/{uuid}`. This URL is also Cloudflare-blocked but may work in a browser.

**Resolution strategy**: Identify the `hp.beehiiv.com` link (usually the penultimate link), note it as the main article URL, but mark content retrieval as requiring browser-based fetch. For triage purposes, classify based on title and known newsletter source.

### ConvertKit / Mailchimp

Standard redirect links — `curl -sL` typically resolves them. No special handling needed.

## Classification Heuristics

### critical
- Article directly addresses wiki's core domain (AI agents, LLM infrastructure, coding agents)
- Existing wiki entity/concept page can be enriched with the new content
- Clear path to specific page creation or update
- Example: "Flue 2 adds React hooks" → `entities/flue.md` exists and needs v2 enrichment

### high
- Article is relevant to wiki scope (LLM scaling, model architecture, AI industry trends)
- May feed into existing concept pages or warrant new ones
- Content not yet fully verified (e.g., Cloudflare-blocked URLs)
- Example: "Nobody Built a Bigger Model" → LLM scaling trends, but content unverified

### low
- Tangentially related (general tech news with AI angle)
- Content is a link dump, Reddit noise, or social media round-up
- Already well-covered by existing wiki pages

## Pre-Triage Entity Check

Before classifying, check existing wiki pages to avoid duplicate work:
```bash
# Check for existing entity
search_files(pattern="entity-name", path="~/ai-topics/wiki/entities", target="files")

# Check for content mentions across entities
search_files(pattern="person name", path="~/ai-topics/wiki/entities", target="content")

# Check raw articles already ingested
search_files(pattern="topic-slug", path="~/ai-topics/wiki/raw/articles", target="files")
```

## Cron-Mode Pitfalls

- `execute_code` is blocked in cron — use `terminal()` + `write_file` for all processing
- `curl ... | python3 -c ...` is blocked by tirith security scanner — fetch to file first
- Substack article HTML is client-side rendered — `curl` returns CSS/font references, not article body. OG metadata (`<meta property="og:...">`) is the reliable extraction target for title/description/author.
