# Podcast Transcript Ingestion

## Dual-Source Pattern
Podcasts have two URLs to consume simultaneously:
- **Episode/page URL** — The show's website page (summary, show notes, sponsor list, guest bio)
- **Transcript URL** — Full transcript text file (often a `.txt` or HTML link from the page)

Fetch **both** — the page provides metadata (host, guest, date, episode number), the transcript provides the technical content.

## Source Handling

1. Fetch both URLs with `web_extract()` simultaneously (they're independent)
2. Cross-reference guest name and company from both sources against existing wiki
3. Save a single raw article that merges both sources — include:
   - Episode metadata (episode number, host, guest, date)
   - Executive summary (from transcript)
   - Extracted key quotes with speaker attribution
   - Technical nuggets (architecture details, metrics, case studies)
4. Filename format: `YYYY-MM-DD_company-or-topic-podcast.md`
5. Sources frontmatter should include both URLs

## Entity Creation Pattern

Podcast transcripts typically require **simultaneous creation of person + company entity**:

| Entity | What to Extract | Example |
|--------|----------------|---------|
| **Person (guest)** | Role, background, key theses/insights from the conversation, company affiliation | Benny Chen (Co-Founder, Fireworks AI) |
| **Company (guest's org)** | Product category, scale metrics, technical differentiators, customer case studies | Fireworks AI (13T tokens/day, RFT, FireAttention) |

Create both in parallel — they cross-reference each other.

## Conversational Content Mining

Transcript text is conversational — technical details are spread across Q&A exchanges. Mining strategy:
1. Look for **case studies with metrics** (e.g., "Vercel achieved 40x faster code fixing via RFT")
2. Extract **named technologies** described by the guest (e.g., "FireAttention", "3D FireOptimizer", "Eval Protocol")
3. Identify **comparisons** the guest makes (e.g., "RFT vs SFT", "NVIDIA vs AMD strategy")
4. Extract **industry observations** (e.g., "the alpha is shrinking", "ROI barrier is eval not compute")
5. Create concept pages for major named techniques (e.g., RFT) and update related existing pages

## Podcast Enrichment for Existing Entities

When ALL guest/person/company entity pages already exist, shift from creation to **targeted enrichment**:

1. **Read all existing entity pages first** — understand current coverage to avoid duplicating content
2. **Distribute podcast insights across entities by speaker attribution**:
   - Person pages → timeline entries, blog/recent posts, project tool sections
   - Tool/project pages → dedicated "Podcast" subsection
   - Concept pages → named frameworks or terminology
3. **Enrich entity page Sources** — add podcast URL and raw article path to `sources:` frontmatter
4. **Always update `updated:` frontmatter date** on all enriched pages

## Comparison with Other Source Types

| Aspect | Blog Article | Podcast Transcript |
|--------|-------------|-------------------|
| URLs to fetch | 1 (article) | 2 (page + transcript) |
| Speaker attribution | Implicit by author | Explicit (Host vs Guest quotes) |
| Technical density | High, structured | Low-to-medium, conversational |
| Entity creation needed | 0-1 (author, if new) | 2 (guest person + company) |
| Named thesis extraction | Optional | Primary value-add |
| Concept page triggers | Technical terms | Guest's named frameworks + technical terms |
