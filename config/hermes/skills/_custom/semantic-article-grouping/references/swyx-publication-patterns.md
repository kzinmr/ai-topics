# swyx / Latent Space Publication Patterns

**Publication ID**: 1084089
**Author**: Shawn "swyx" Wang (@swyx)
**Domains**: open.substack.com/pub/swyx/p/{slug}, www.latent.space

## Rebranding Note (July 2026)

As of July 2026, **AINews is now officially a section of Latent Space**. The newsletters continue to publish under swyx's Substack (pub_id=1084089) and the same open.substack.com distribution, but the canonical publication is `latent.space`. The newsletter post body includes: "AINews is now a section of Latent Space. You can opt in/out of email frequencies!" This does not affect URL resolution: `open.substack.com/pub/swyx/p/{slug}` still works and redirects to `www.latent.space/p/{slug}`.

## Dual Content Types

Publication 1084089 produces TWO distinct content types from the same substack:

### Type A: AINews (Daily AI News Roundup)
- Format: Aggregated news bulletin with curated X/Twitter embeds, arXiv papers, GitHub repos
- Frequency: Daily (weekdays)
- Source URL construction: `open.substack.com/pub/swyx/p/{slug}` where slug contains `ainews-`
- Paywall: **Variable — mostly behind free preview but occasional free issues.** Daily news roundups are usually paywalled (`isAccessibleForFree: false`) with ~1K char free preview. However, breaking AI safety/policy events (e.g., the June 13 Fable/Mythos export control directive issue) may be made fully accessible (`isAccessibleForFree: true`) with full 70+ paragraph body retrievable from `open.substack.com`. Always check `isAccessibleForFree` in JSON-LD before assuming paywall; if true, the full body is accessible.
- Content density: 30-80 external links per post
- Sections: Qwen updates, AI Twitter recap, tool releases, model announcements
- **Triage approach**: The free preview gives section headings and table of contents — enough for triage. Link 2 (post title) is the canonical URL. UUID redirects (links 8-20) are track-only.
- **Paywalled `<article>` extraction**: Even when `isAccessibleForFree: false` in JSON-LD, the raw HTML `<article>` tag still yields ~25K chars of usable content (model names, X/Twitter embeds with quotes, benchmark numbers, section headers). The paywall gate is rendered on top via CSS — the content is in the HTML. Always attempt `<article>` tag extraction via curl as a fallback before concluding a post is opaque.
- **Typical yield**: 1-3 takes, 2-4 references, many skips (most topics already covered by sitemap-monitor and blog-ingest pipelines)

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

## AINews Section Anchor Navigation (July 2026)

AINews daily newsletters use **section anchor links** for targeted content extraction. Each major section has a stable anchor at:
```
https://www.latent.space/i/{post_id}/{section-slug}
```

### Observed Section Slugs

| Slug | Content |
|------|---------|
| `core-facts-and-specs` | Model size, modality, licensing, context window |
| `training-and-release-details` | Training data, timeline, release info |
| `architecture-details-surfaced-in-reactions` | Technical architecture from community analysis |
| `variants` | Model family variants (e.g., Inkling-Small 276B-A12B) |
| `performance-and-benchmarks` | Benchmark overview |
| `specific-benchmark-numbers-cited` | Concrete benchmark scores (Intelligence Index, Elo, task-specific) |
| `qualitative-performance-takes` | Community qualitative assessments |
| `inference-systems-and-launch-ecosystem` | Serving stacks, infrastructure partners |
| `pricing-and-availability` | API/hosting pricing |
| `facts-vs-opinions` | Distinction between confirmed facts and interpretations |

### Usage Pattern

1. Extract `post_id` from the app-link URL in the newsletter candidate (`publication_id=1084089&post_id=NUM`)
2. Build section URLs: `https://www.latent.space/i/{post_id}/{slug}`
3. Use `web_extract` or curl on individual section URLs for targeted content when the full page is too large
4. **Advantage**: Section pages contain only the relevant section's content, not the full newsletter with UI chrome
5. **Verified**: July 2026, post_id=207247810 (Inkling release). Section anchors returned clean, focused text.

### Limitations
- Section slugs are not guaranteed for every post — newer posts (first week?) may lack some sections
- The `facts-vs-opinions` section is especially useful for distinguishing confirmed claims from speculation (common in AINews curation style)
- Not all post_ids have all sections; the sections present depend on content type (model release posts are the most richly structured)

## See Also
- `references/substack-publication-patterns.md` — AINews-specific section
- `references/pure-podcast-substack-patterns.md` — distinction from pure-podcast publications
