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

### Type B: Latent Space Podcast (Interview Episodes)
- Format: Long-form interviews with AI researchers and practitioners
- Frequency: Weekly
- Source URL construction: `open.substack.com/pub/swyx/p/{slug}` — slug matches podcast topic
- Paywall: Usually **fully accessible** (no paywall); audio/video embedded
- Content density: 1-2 external links (podcast player, shownotes)
- Examples: "ESMFold2: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub"
- **Triage approach**: Full transcript/summary accessible. Content is narrative interview — assess topic relevance for wiki inclusion.

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
