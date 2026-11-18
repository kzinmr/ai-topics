# Non-AI / non-substantive content to skip

Moved from SKILL.md "Key Patterns to Recognize" (2026-11-15 slim-down). Full skip
criteria, including the podcast / link-digest nuances and their counter-nuances.

## Skip outright (no URL resolution needed)
- **Business strategy podcasts** (e.g., Lenny's Podcast with Evan Spiegel on distribution moats) — unless they discuss AI specifically.
- **Pure-podcast newsletters** (e.g., Lenny's Podcast Tony Fadell): 100% audio UI links in email, post page has no standalone article body. Skip immediately without URL resolution. Does NOT apply to hybrid publications (e.g., Latent Space) that write standalone articles alongside audio. See `pure-podcast-substack-patterns.md` for full detection criteria.
- **Pure link digest newsletters** (e.g., AI Weekly / True Positive Weekly): post body is a shallow bullet list of article titles with 1-line descriptions and no editorial analysis. Skip the digest, but GAP-CHECK its curated URLs and take gap-filling primaries (`tpw183-curate-link-take-pattern.md`). Also `newsletter-triage-2026-10-21-batch-patterns.md` ("noted, not ingested" = take).
- **General tech news** without AI/agent relevance.
- **Company financial results** without AI product implications.

## ⚠️ Nuance: Podcast post pages WITH substantial body text
Even when the primary format is audio, the Substack post page for a podcast episode may
contain 50+ paragraphs of explanatory text (free, `isAccessibleForFree: true`). This is
especially common with AI/Science podcasts (Latent Space AI for Science, etc.). The post
page JSON-LD + `<article>` tag extraction can yield wiki-worthy conceptual content
(training methodologies, research framing, technical claims). Check the post page body
before assuming a podcast link has no wiki value. In June 2026, a Latent Space podcast
post about Axiom Math ("Scaling Past Informal AI") had 54 significant paragraphs without
any audio transcription — the author wrote a standalone article alongside the podcast.

## ⚠️ Counter-nuance: Pure-podcast pubs
e.g., Lenny's Podcast: email is 100% audio UI links with no standalone article body —
BUT high-profile AI guests can produce 30-70+ `<p>` tags. DO NOT auto-skip based on email
pattern; read the first 10 `<article>` paragraphs and check for substantive analysis vs.
single-line topic headings. See `pure-podcast-substack-patterns.md` for the
content-structure heuristic.
