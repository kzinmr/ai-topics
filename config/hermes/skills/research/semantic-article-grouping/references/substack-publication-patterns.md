# Substack Publication URL Resolution Patterns

Known substack publication URL behaviors discovered during newsletter-triage sessions. Use this when resolving newsletter post URLs from substack `app-link/post` patterns.

## URL Resolution Patterns by Publication

| Publication | Substack Handle | Publication ID | Post URL Pattern | Resolves To | Notes |
|------------|----------------|---------------|------------------|-------------|-------|
| **The Signal** | `thesignal` | 293154 | `open.substack.com/pub/thesignal/p/{slug}` | `thesignal.substack.com/p/{slug}` | Direct redirect, no domain change. Text content accessible. |
| **AINews** | `swyx` | 1084089 | `open.substack.com/pub/swyx/p/{slug}` | `www.latent.space/p/{slug}?triedRedirect=true` | **Domain change**: redirects to `latent.space` (swyx's domain). Content behind paywall. |
| **Latent Space Podcast** | `swyx` | 1084089 | `open.substack.com/pub/swyx/p/{slug}` | `www.latent.space/p/{slug}` | Same pub_id as AINews. See `references/swyx-publication-patterns.md` for distinguishing types. |
| **NLP News** | `nlpnews` | (unknown) | `open.substack.com/pub/nlpnews/p/{slug}` | `nlpnews.substack.com/p/{slug}` | Direct redirect, standard behavior. |
| **Gary Marcus** | `garymarcus` | (unknown) | `open.substack.com/pub/garymarcus/p/{slug}` | `garymarcus.substack.com/p/{slug}` | Direct redirect. |
| **Simon Willison** | `simonw` | 1173386 | `open.substack.com/pub/simonw/p/{slug}` | `simonw.substack.com/p/{slug}` | Django co-creator's personal newsletter. Full content accessible free. Often cross-posts from simonwillison.net. |
| **Hyperdimensional (Dean Ball)** | `hyperdimensional` | 2244049 | `open.substack.com/pub/hyperdimensional/p/{slug}` | `hyperdimensional.substack.com/p/{slug}` | AI policy analysis by Dean W. Ball (FAI). Deep essays on physical AI, regulation. |
| **Ben's Bites** | `bensbites` | 4379299 | `open.substack.com/pub/bensbites/p/{slug}` | `bensbites.substack.com/p/{slug}` | Daily AI news by Ben Tossell. Short form, link-heavy, often includes sponsored content. |
| **AI by Aakash** | `aibyaakash` | 5747120 | `open.substack.com/pub/aibyaakash/p/{slug}` | `aibyaakash.substack.com/p/{slug}` | Weekly AI news by Aakash. Covers funding rounds, model releases, tool launches. Often promotes GBrain system. |
| **True Positive Weekly** | `aiweekly` | 61455 | `open.substack.com/pub/aiweekly/p/{slug}` | `aiweekly.substack.com/p/{slug}` | Curated AI/ML links by Andriy Burkov. Link-heavy format: headlines only with short descriptions. web_extract often returns truncated content (headlines visible, link URLs inaccessible). |
| **SemiAnalysis** | `semianalysis` | 6349492 | Sent as individual emails (one article per email) | `semianalysis.com/p/{slug}` | **Not a standard substack newsletter** — each article sends as its own email. Heavy paywall. See `references/semianalysis-paywall-patterns.md`. |

## Constructing Post URLs from Checkpoint Data

The newsletter-ingest pipeline extracts an `app-link/post` URL with `publication_id` and `post_id`:

```
https://substack.com/app-link/post?publication_id=1084089&post_id=196741175
```

Two construction strategies:

### Strategy A: Use the `open.substack.com` URL (from `redirect=app-store` link)

Checkpoint often contains a Link with pattern:
```
https://open.substack.com/pub/{handle}/p/{slug}?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app
```

Strip the `redirect=app-store` and query params to get the clean post URL:
```
https://open.substack.com/pub/{handle}/p/{slug}
```

This is the **most reliable** method — the slug is human-readable.

### Strategy B: Construct from publication_id/post_id (fallback)

If no `open.substack.com` URL is available, look up the handle from the table above and construct:
```
https://open.substack.com/pub/{handle}/p/{post_id}
```

Note: using the raw `post_id` as the slug sometimes works (Substack may auto-resolve), but the slug-based URL is preferred.

### Strategy C: substack.com/home/post/p-{post_id} (fallback when custom domain fails)

When both `open.substack.com/pub/{pub}/p/{slug}` AND the custom domain (e.g., `latent.space`) return `http_error`, try the Substack internal post page:

```
https://substack.com/home/post/p-{post_id}
```

This uses the **post ID** directly, bypassing slug matching and custom domain DNS resolution. In May 2026, the AINews post "Cerebras' $60B IPO" (`post_id=197953407`) returned `http_error` on both `open.substack.com/pub/swyx/p/...` and `www.latent.space/ainews-...` (404), but `substack.com/home/post/p-197953407` returned HTTP 200 with full HTML content (235KB).

**How to use**: Run `web_extract` on the `substack.com/home/post/p-{post_id}` URL. If `web_extract` fails, use the `curl + subprocess` HTML fallback approach from the main SKILL.md — the HTML response is typically large (200K+) and contains embedded external article links.

**Limitation**: This URL format has no browser JS rendering — content after paywall gate won't be visible. But the HTML will contain:
- The free preview text
- All embedded external link `<a>` tags (curated articles, X posts, YouTube embeds)
- Section anchor links (`/i/{post_id}/...` — filter these out)
- Sponsor/ad links

## Paid/Paywalled Detection

| Signal | Meaning |
|--------|---------|
| `∙ Paid` badge in post header | Full content behind paywall |
| `Subscribe Sign in` banner at top | Not authenticated; paywalled |
| "Paid" in post metadata (from web_extract) | Paywalled |
| Content truncated mid-sentence | Likely paywalled (free preview cutoff) |
| `isAccessibleForFree: false` in JSON-LD | Confirmed paywalled |

Paywalled substack posts still provide value:
- The **free preview** (first ~1000 chars) often contains the lede, thesis, and key framing
- Embedded X/Twitter links within the preview are visible and may contain substantive quotes
- The post title and subtitle provide framing for the topic
- Cross-reference claims against non-paywalled sources

## Common Patterns

### Link Naming in Checkpoints
- **Link 2** (or `post-email-title` link) = The newsletter post page itself (the email's title link)
- **Link 4** (or `@handle`) = Author profile → Skip
- **Link 5** (or `submitLike`) = Like/reaction → Skip
- **Link 6** (or `comments`) = Comment section → Skip
- **Link 7** (or `share`) = Share action → Skip
- **Link 8+** (UUID redirects) = Email tracking links → Skip (post body has content)
- **Link 9** (or `redirect=app-store` + `email-read-in-app`) = Read-in-app prompt → Skip BUT contains the clean post URL as a side-effect

### AINews Specific
- Publication is published by `swyx` (Shawn Wang / swyxio)
- Owns `latent.space` domain, which is the canonical home
- Also at `www.latent.space/s/ainews/`
- Heavy use of X/Twitter embeds for source curation
- Dario Amodei quotes and event recaps are common premium content
- Free preview typically covers: event summary, headline details, 2-3 embedded X posts with key quotes
- **Section anchor pattern**: Posts contain anchored sub-sections at paths like `/i/{post_id}/{n}-{slug}` (e.g., `/i/197305557/1-qwen-36-local-inference-advances`, `/i/197305557/ai-twitter-recap`). These are internal anchor links to parts of the same newsletter post, NOT separate articles. When extracting external links from the HTML, these can be filtered out by recognizing the `/i/{post_id}/` prefix pattern.
- **External link density**: A single AINews post typically contains 30-80 external links (X/Twitter posts, arXiv papers, GitHub repos, Reddit threads, YouTube videos). Most are embedded X posts. Prioritize articles with substantive external content (arXiv papers, blog posts, GitHub repos) over individual X post embeds.

### True Positive Weekly (Andriy Burkov) Patterns
- Publication: `aiweekly` on Substack (publication_id=61455)
- Format: Link-aggregation style — publishes ~20 curated AI/ML links per week, each with a 1-2 line description
- **web_extract limitation**: The Substack free preview often truncates at the headline level — individual article URLs are embedded in the HTML but NOT rendered in the web_extract markdown output. The page's table of contents shows headlines, but the actual `<a href>` links to external articles may be hidden behind Substack's UI framework.
- **Triage approach**: When web_extract returns only headlines without link URLs, use the curl+subprocess HTML fallback (from main SKILL.md) to extract the embedded `<a>` tags from the raw HTML. If that also fails (Cloudflare, etc.), triage at the headline/topic level only — most True Positive Weekly headlines are general enough to assess as skip (too broad) or reference (points to pre-existing wiki coverage).
- **Typical topics**: AI chips explained, agent patterns, Shazam internals, time series models, scientific paper maps — broad educational content that rarely adds specific wiki value.

### Ben's Bites (Ben Tossell) Patterns
- Publication: `bensbites` on Substack (publication_id=4379299)
- Format: Short daily newsletter with 1 main story + 5-10 link roundups + "Afters" (notable tweets) + sponsor
- **Content character**: Very informal, tool-oriented. Many links are tools/products (Clanker, Granite, Supermemory, Polar, Parse 2.0) that may or may not be wiki-worthy. 
- **Triage approach**: Focus on the main story section (usually substantive) and any links that mention specific technical claims (benchmarks, security findings, model releases). Skip the "tools roundup" section unless a specific tool has clear wiki relevance. Skip sponsored content.
- **Beware DeepSWE duplication**: Ben's Bites often links to the same benchmarks and releases that AINews covers the same day. Cross-check against the AINews post in the same batch before creating separate decisions.

### AI by Aakash (GBrain) Patterns
- Publication: `aibyaakash` on Substack (publication_id=5747120)
- Format: Weekly AI news recap + tool/funding roundup + prominent GBrain promotion (Garry Tan's persistent memory system)
- **Content character**: News aggregation with opinionated takes. Often covers xAI news (Grok Build), Anthropic funding/model releases, and startup tooling. The GBrain system (Herme Agent/OpenClaw-based persistent memory) is a recurring theme.
- **Triage approach**: The xAI Grok Build and GBrain sections are the highest-value content. Funding news (SpaceX IPO, Uber budget) is secondary. The newsletter is generally thorough enough to triage from the web_extract body without needing external URL resolution.

## Paywall Detection by Publication

| Publication | Paywall Status | Free Preview Length | Notes |
|------------|---------------|-------------------|-------|
| **AINews (swyx)** | Behind paywall | ~1,000 chars (section headings + 1-2 X embeds) | Headings sufficient for triage |
| **Latent Space Podcast** | Free | Full content | Podcast transcript/shownotes fully accessible |
| **The Signal** | Behind paywall | ~1,000 chars (lede + 1 quote) | Usually from lede only |
| **Simon Willison** | Free | Full content | Personal newsletter, cross-posts from blog |
| **Hyperdimensional** | Free | Full content (essay format) | Deep policy essays, fully readable |
| **Ben's Bites** | Free | Full content | Short format, fully readable |
| **AI by Aakash** | Free | Full content | News aggregation, fully readable |
| **True Positive Weekly** | Free | Full content (headlines visible) | Links embedded in HTML may be hidden |
| **SemiAnalysis** | Behind paywall | ~500 chars | Heavily paywalled |
