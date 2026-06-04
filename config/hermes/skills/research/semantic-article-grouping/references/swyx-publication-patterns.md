# swyx / Latent Space Publication Patterns

**Publication ID**: 1084089
**Author**: Shawn "swyx" Wang (@swyx)
**Domains**: open.substack.com/pub/swyx/p/{slug}, www.latent.space

## Dual Content Types

Publication 1084089 produces TWO distinct content types from the same substack:

### Type A: AINews (Daily AI News Roundup)
- Format: Aggregated news bulletin with curated X/Twitter embeds, arXiv papers, GitHub repos
- Frequency: Daily (weekdays)
- Source URL construction: `open.substack.com/pub/swyx/p/{slug}` where slug contains `ainews-`
- Paywall: Most content behind free preview; full body requires subscription
- Content density: 30-80 external links per post
- Sections: Qwen updates, AI Twitter recap, tool releases, model announcements
- **Triage approach**: The free preview gives section headings and table of contents — enough for triage. Link 2 (post title) is the canonical URL. UUID redirects (links 8-20) are track-only.
- **Paywalled <article> extraction**: Even when `isAccessibleForFree: false` in JSON-LD, the raw HTML `<article>` tag still yields ~25K chars of usable content (model names, X/Twitter embeds with quotes, benchmark numbers, section headers). The paywall gate is rendered on top via CSS — the content is in the HTML. Always attempt `<article>` tag extraction via curl as a fallback before concluding a post is opaque.

### Type B: Latent Space Podcast (Interview Episodes)
- Format: Long-form interviews with AI researchers and practitioners
- Frequency: Weekly
- Source URL construction: `open.substack.com/pub/swyx/p/{slug}` — slug matches podcast topic
- Paywall: Usually **fully accessible** (no paywall); audio/video embedded
- Content density: 1-2 external links (podcast player, shownotes)
- Examples: "ESMFold2: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub"
- **Triage approach**: Full transcript/summary accessible. Content is narrative interview — assess topic relevance for wiki inclusion.
- **Internal anchor link noise**: The podcast page contains 22+ internal anchor links like `https://www.latent.space/i/{post_id}/introduction-...` pointing to transcript sections. These are NOT external articles — they are internal navigation. Filter them out during external link extraction. The podcast intro paragraph and section headings ARE the content to assess. Zero external article yield from the link extraction pass is normal for podcast episodes.

## Distinguishing Types from Subject Line

| Signal | Likely Type |
|--------|------------|
| Starts with emoji (🔬, 🧠, 🎙️) + descriptive title | **Podcast episode** (Type B) |
| "AINews" in subject, date-based (e.g., "May 27, 2026") | **Daily news roundup** (Type A) |
| Author name in subject ("Alex Rives, BioHub") | **Podcast episode** (Type B) |
| Brief, topic-focused ("GPT-5.5 Instant") | Podcast or short form |
| Multiple links, "New AI Infra decacorns" | **News roundup** (Type A) |

## URL Resolution

Both types use the same substack infrastructure:
```
open.substack.com/pub/swyx/p/{slug}  →  www.latent.space/p/{slug}
```

The `open.substack.com` URL gives the full content (or free preview for Type A). Custom domain `latent.space` redirects to the same.

## See Also
- `references/substack-publication-patterns.md` — AINews-specific section
