# Single-Page Research Collection Ingestion

When a research lab/company publishes findings as a single listing page with
summaries but no individual post pages (all guessed URLs return 404), this
pattern handles extraction and enrichment.

## Recognition

Indicators of a single-page research collection:
- Research page shows list of posts with summaries, tags, dates
- All post titles on one page, no obvious individual links
- Guessing individual URLs (`/research/slug/`) returns 404
- Site may be SPA-based or statically generated without post subpages

## Procedure

1. **Extract the listing page** — use `web_extract` on the research URL.
   The summaries ARE your source material. Save to `raw/articles/`.

2. **Identify the organization** — extract from the main site (`/`), About page,
   or header. Know who you're dealing with before writing pages.

3. **Find supplementary sources** — single-page summaries are thin. Search for:
   - GitHub repos (often contain the implementation behind the research)
   - HuggingFace blog posts (many labs publish longer-form pieces there)
   - X/Twitter threads (search `"OrganizationName" research`)
   - ArXiv papers (if the lab publishes academically)

4. **Synthesize, don't just list** — 12 individual one-paragraph concept pages
   would be too thin. Instead:
   - One entity page for the organization
   - One comprehensive concept page that thematically groups all findings
   - Separate concept pages only for techniques that justify standalone treatment
     (e.g., RDEP — a named parallelism strategy with its own implementation)

5. **Cross-reference generously** — link to existing wiki pages for related
   concepts (e.g., `mixture-of-experts`, `deepseek` for MoE practitioners).

## Example: Noumena Network (2026-05-08)

- Listing page: `https://noumena.com/research/` — 12 posts, all 404 on individual URLs
- Supplementary: GitHub `Noumena-Network/nmoe` (RDEP implementation)
- Supplementary: HuggingFace blog "Skill is All You Need"
- Output: 1 entity + 2 concept pages (methodology synthesis + RDEP)
