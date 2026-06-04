# Research Page as Single Listing

When a research lab or company publishes findings as summary cards on a single page with no individual post URLs accessible.

## Detection Signals

- `/research/` page returns a list of titled summaries (e.g., "Super-4096 — Loss keeps improving while routing collapses...")
- Individual post URLs 404 (e.g., `/research/super-4096/` not found)
- Page is likely a static site or SPA where content is rendered client-side from a data blob
- `web_extract` gets all summaries but `browser_navigate` is unavailable or impractical

## Pattern

### 1. Extract All Summaries

Use `web_extract` on the research page URL. Capture every post's title, type tag (research result / methodology / systems / hypothesis), and one-line description.

### 2. Find Supplementary Sources

The summaries alone are thin. Search for:
- **GitHub README**: The lab's open-source repos often contain the detailed technical narrative behind the summaries
- **Blog posts**: HuggingFace, Medium, or Substack posts where the lab explains their approach in depth
- **Web search**: Author names + project names to find talks, interviews, or third-party coverage
- **X/Twitter**: The author's profile and recent posts for additional context

### 3. Thematic Grouping

Don't create one wiki page per summary — they'd be too thin. Instead:
- Group summaries by theme (e.g., methodology posts together, results posts together, systems posts together)
- Identify the **core narrative arc** across all summaries (e.g., "We built a speedrun methodology → applied it to MoE training → discovered routing collapse ≠ quality collapse")
- Create **1-3 concept pages** that synthesize the full research program

### 4. Page Structure

For the synthesis concept page:
- **Core Philosophy** section: distill the lab's approach from framing posts
- **Key Findings** section: one subsection per major result, with the summary as the claim and supplementary sources as evidence
- **Systems Innovation** section: any novel infrastructure (e.g., RDEP)
- Cross-reference the entity page, related concepts, and any people pages

### 5. Create Entity Page

The lab/company gets an entity page covering:
- Overview and philosophy
- Workstreams (from supplementary sources)
- Key people (from GitHub org, X profiles)
- Research program summary with links to concept pages
- Roadmap (if available from the main site)

## Example: Noumena Network (2026-05-08)

**Input:** `https://noumena.com/research/` — 12 summary cards, all dated Mar 14, 2026

**Supplementary sources:**
- `github.com/Noumena-Network/nmoe` — README with RDEP architecture, configs, speedrun workflow
- `huggingface.co/blog/Noumena-AI/skill-is-all-you-need` — Agent systems blog post
- `x.com/_xjdr` — Founder's X profile (bio, pinned tweet, project links)
- `github.com/xjdr-alt/entropix` — Founder's other major project

**Output:**
- `entities/noumena-network.md` — entity page
- `concepts/moe-training-noumena-methodology.md` — 7 thematic findings from 12 summaries
- `concepts/rdep.md` — systems innovation concept page
- `entities/xjdr.md` — key person enrichment (stub→full)

## Pitfalls

- **Don't try to scrape individual post pages** that don't exist. The URLs 404 because the site is a single-page listing.
- **Don't create 12 thin concept pages.** Synthesize into 1-3 rich ones.
- **Summaries are claims, not evidence.** Cross-reference with GitHub READMEs and blog posts to add technical depth.
- **The research page may be the lab's only public output.** Build the entity page from what's available — the main site, GitHub org, X account, and any referenced repos.
- **Check for existing stubs.** The lab or its people may already have skeleton pages in the wiki from blog author scraping.
