# Substack Publication URL Resolution Patterns

Known substack publication URL behaviors discovered during newsletter-triage sessions. Use this when resolving newsletter post URLs from substack `app-link/post` patterns.

## URL Resolution Patterns by Publication

| Publication | Substack Handle | Post URL Pattern | Resolves To | Notes |
|------------|----------------|------------------|-------------|-------|
| **The Signal** | `thesignal` | `open.substack.com/pub/thesignal/p/{slug}` | `thesignal.substack.com/p/{slug}` | Direct redirect, no domain change. Text content accessible. |
| **AINews** | `swyx` | `open.substack.com/pub/swyx/p/{slug}` | `www.latent.space/p/{slug}?triedRedirect=true` | **Domain change**: redirects to `latent.space` (swyx's domain). Content behind paywall. |
| **NLP News** | `nlpnews` | `open.substack.com/pub/nlpnews/p/{slug}` | `nlpnews.substack.com/p/{slug}` | Direct redirect, standard behavior. |
| **Gary Marcus** | `garymarcus` | `open.substack.com/pub/garymarcus/p/{slug}` | `garymarcus.substack.com/p/{slug}` | Direct redirect. |

## Finding the Post URL from the Checkpoint

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

If no `open.substack.com` URL is available, construct:
```
https://{handle}.substack.com/p/{post_id}
```

But you need to know the handle. Map known publication_ids to handles:
- `publication_id=1084089` → handle=`swyx` (AINews → latent.space)
- `publication_id=293154` → handle=`thesignal` (The Signal → thesignal.substack.com)

For unknown publication_ids, extract the handle from any other link in the checkpoint that has a known pattern (e.g., the `/@{handle}` author link).

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
