# Pure-Podcast Substack Publication Patterns

Not all Substack publications with podcast content follow the Latent Space model (standalone article + audio). Some are **pure-podcast** — the email contains only audio player UI links, and the post page has no substantive body text beyond bullet-point show notes.

## Distinguishing Pure-Podcast from Hybrid

| Dimension | Pure-Podcast (Lenny's Podcast) | Hybrid (Latent Space, AINews) |
|-----------|-------------------------------|-------------------------------|
| Email links | 100% audio UI (play_card, play_button, progress_bar, duration) | Mixed: article title links + some audio UI |
| Post page body | Audio player + guest bio + topic preview. Variable: some episodes have 30+ paragraphs of standalone body text including intro Q&A summary, bullet-point topic list, embedded YouTube, and extensive reference links | Full article body (25-54 paragraphs) with research analysis |
| `isAccessibleForFree` | `false` (gated behind paywall), but body may still be fully accessible via `<article>` extraction | Often `false` despite full body being accessible |
| Primary content format | Audio (1-2 hour podcast episode) + optional standalone intro text (varies by guest) | Written article (standalone research/analysis) |
| Transcript | NOT in post body (may exist separately) | NOT in post body (also separate) |
| Post-paragraph extraction yield | 0-5 meaningful paragraphs for typical episodes; **30-34 paragraphs for high-profile AI guests** (June 2026: Fiona Fung episode had 34 substantive paragraphs) | 20-54 substantive paragraphs |

## Known Pure-Podcast Publications

### Lenny's Podcast (`publication_id=10845`) — Hybrid (two content types)
- **Host**: Lenny Rachitsky
- **Focus**: Product management, startups, career, business strategy
- **Email format**: Every email link is an audio-player variant (play_card, play_button, progress_bar, duration, show_logo, show_title, post_title, preview_link, listen_now). No external article curation.
- **Post URL**: `https://open.substack.com/pub/lenny/p/{slug}`
- **Post page content (variable)**: 
  - **Typical episode**: Audio player UI (~1.5 hours), 3-5 bullet-point show notes, sponsor mentions, transcript link
  - **High-profile AI guest episodes** (observed June 2026: Fiona Fung, Anthropic; July 2026: Dianne Penn): 30-70+ `<p>` tags and 80K+ chars of body text, but the text is **predominantly metadata/UI/sponsor/links** — not standalone article content
- **isAccessibleForFree**: `false`, but body text may still be fully accessible via `<article>` tag extraction (34+ paragraphs observed despite false flag)
- **AI relevance**: Generally low for wiki content extraction — the substantive content is in the audio. HOWEVER, intro text for AI-figure episodes can yield wiki-worthy entity discovery content (org charts, role descriptions, key statistics like "8x code shipping", management methodology).
- **Detection pattern for high-body-content episodes**: Post page will have a `<h1>` headline + guest intro paragraph + bullet-point topic list (Look for: "What she's learned about...", "Which roles...", "Specific ways..." patterns) before the audio player chrome. **However, paragraph count alone is misleading** — the content may consist entirely of single-line topic headings, sponsor ads (WorkOS, Mercury), and reference link lists (LinkedIn, anthropic.com, amazon.com book links) with zero substantive analysis text.
- **Content-structure heuristic (critical)**: When a Lenny's Podcast episode shows 30+ `<p>` tags, read the **first 10 paragraphs** before drawing any conclusion. The text falls into three categories:
  1. **Substantive** (3+ sentences/paragraph, technical claims, data points, methodology) → wiki-worthy entity discovery
  2. **Single-line topic headings** ("How exactly Claude got so good at coding", "What Anthropic's early days were like") → metadata, not content — skip unless you have a transcript
  3. **Sponsor/UI/reference links** (WorkOS, Mercury ads; Amazon book links; YouTube/Spotify embeds; production credits) → noise, always skip
  - **Confirmed pattern** (July 2026): Dianne Penn episode had 70+ `<p>` tags and 81K chars. Zero substantive paragraphs. The topic bullet points were all single-line headings, the remaining ~60 paragraphs were sponsor ads, platform links, Amazon book URLs, and production credits.
- **Recommended triage action**: **Do NOT skip based on paragraph count alone.** Curl the post URL and extract `<article>` paragraph text. Read the first 10 paragraphs to check category distribution. If every "topic" paragraph is a single-line heading (<30 words) with no follow-up analysis, skip — the substantive content is only in the audio transcript, which is not available in the post body. Only extract for entity discovery if you find 5+ paragraphs of 3+ sentence analytical text.

### "How I AI" (Spinoff, `publication_id=10845`) — Substantive hybrid (DO NOT auto-skip)
- **Produced by**: Lenny's Podcast Network
- **Format**: Weekly podcast-article hybrid, but **consistently produces 90+ paragraphs of standalone body text** — NOT a pure-podcast publication despite sharing pub_id=10845
- **Focus**: AI tools, workflows, and builder practices (GPT-5.6 reviews, local AI fleets, agent harnesses)
- **Email format**: Same audio UI variants as Lenny's Podcast (play_card, play_button, etc.) — cannot distinguish from standard Lenny's at the email-link level. Slug detection is required.
- **Post page**: Always has extensive standalone article body (90+ paragraphs observed) with:
  - Sponsored tools embedded in body (Bolt.new, Customer.io, Runway, Jira Product Discovery)
  - Full podcast transcript excerpts as article paragraphs
  - Multiple external links to builder workflows (chatprd.ai/how-i-ai/workflows/)
  - YouTube/Spotify/Apple Podcasts embed links
- **isAccessibleForFree**: `true` (fully accessible)
- **Content density**: 3-4 distinct wiki-worthy topics per issue (e.g., GPT-5.6 Sol benchmark, Alex Finn's local AI fleet, Claire's agent harness build)
- **Detection**: `open.substack.com/pub/lenny/p/how-i-ai-{slug}` — slug always contains `how-i-ai`
- **Triage action**: **Never auto-skip.** Treat as a full article newsletter. Extract all 90+ paragraphs via curl JSON-LD + `<article>` tag. The body contains substantive technical claims, model comparisons, and workflow descriptions suitable for wiki ingestion.
- **Yield expectation**: 1-3 takes, 1-2 references per issue (validated Jul 2026)

## Triage Guidance

When you encounter a Substack publication where **all email links are audio UI variants**:

1. **Identify it immediately**: If 20/20 email links contain `play_audio=true`, `play_card`, `play_button`, `listen_now`, `progress_bar`, `duration` — this is a pure-podcast publication.
2. **Check the post page before skipping**: Do NOT immediately skip. Curl the post URL and check `<article>` paragraph count. If 10+ substantive paragraphs exist (guest bio, bullet-point topic previews, embedded media links beyond player chrome, reference links), extract them for entity discovery. The intro standfirst may be enough for entity creation even without the full transcript.
3. **Skip only when confirmed low-yield**: If the post page's `<article>` tag yields <5 meaningful paragraphs (only audio player chrome, 2-3 show-note bullets, no guest bio), then skip.
4. **Exception**: If the podcast post page has a **transcript** link that resolves to substantive text, *and* the topic is directly AI/LLM/agent-relevant (not general business/product strategy), treat as a normal newsletter candidate.

## Comparison Table

| Publication | pub_id | Type | Article Body? | Wiki Yield |
|-------------|--------|------|---------------|------------|
| Lenny's Podcast | 10845 | Pure podcast | Variable (0-34 paragraphs; varies by guest) | ★★☆☆☆ (entity discovery only, not technical content) |
| Latent Space | 1084089 | Hybrid | Yes (full analysis articles) | ★★★★☆ |
| AINews (swyx) | 1084089 | Written bulletin | Yes (full daily bulletin) | ★★★☆☆-★★★★★ |
