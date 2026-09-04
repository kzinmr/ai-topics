# MOC (Map of Content) Page Creation Pattern

A MOC page is a concept-type wiki page that serves as a **navigational hub** for a thematic cluster of wiki pages. Unlike regular concept pages that dive deep into a single topic, MOC pages organize cross-references across multiple related pages.

## When to Create a MOC Page

- User asks for a "checkpoint" or "overview" of a thematic investigation
- A concept has spawned 10+ related wiki pages across entities/concepts/raw articles
- The cluster lacks a single entry point for navigation
- Example: Baudrillard/Simulacra cluster spawned 15 pages across 5 sub-themes

## MOC Page Template

```yaml
---
title: "Theme Name — Map of Content"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [concept, ...domain-specific-tags]
aliases: [theme-moc]
description: "Map of Content for [theme]. Navigational hub connecting N wiki pages across M thematic clusters."
related:
  - "[[concepts/central-page]]"
  - "[[concepts/related-1]]"
  - "[[concepts/related-2]]"
sources:
  - "raw/articles/key-source.md"
  - "https://external-source"
---
```

## Body Structure

MOC pages should be organized by **thematic clusters**, not by page type:

1. **The Core Framework** — central concept page + key source articles
2. **Cluster N: [Thematic Group Name]** — table of pages with their relationship to the theme
3. **Cross-Cutting Connections** — how this theme connects to other wiki areas
4. **Source Articles** — raw articles that feed the cluster
5. **Entity Pages** — people who contributed key perspectives

Each cluster section uses a table format:

```markdown
## Cluster Name — Description

| Page | Relationship to Theme | Summary |
|------|----------------------|---------|
| `[[concepts/page-1]]` | How it connects | One-line summary |
| `[[concepts/page-2]]` | How it connects | One-line summary |
```

## Post-Creation Steps

1. Add MOC link to **2-3 key related pages** (not just one central page):
   - The most closely related concept page (e.g., `ai-evaluation.md`)
   - Any overview/series page that feeds into the MOC (e.g., `ai-benchmarks-evals-overview.md`)
   - Use `patch` to add a line under `## Related Pages` or similar section
2. Update `index.md` — replace stub description with rich MOC summary covering thematic clusters and page count
3. Append to `log.md`
4. Commit and push

## Example

`concepts/baudrillard-moc.md` (2026-06-08) — 9.5KB MOC connecting 15 wiki pages across 5 clusters: philosophical framework, hyperreality, map-and-territory, illusions, counter-strategies. Cross-references raw articles, blog articles, entity pages, and concept pages.

## Upgrading an Existing Stub to a MOC

When a stub page already exists for the theme (e.g., `ai-benchmarks-and-community.md` with just a TODO), upgrade it rather than creating a new file. Workflow:

1. **Confirm it's a stub**: `read_file` — look for `status: stub` and minimal body content
2. **Multi-pass inventory search**: MOCs require comprehensive coverage. Search in waves:
   - `search_files(pattern="keyword", target="content", path="wiki/concepts/")` — content matches
   - `search_files(pattern="*keyword*", target="files", path="wiki/concepts/")` — filename matches
   - `search_files(pattern="  - tag-name", target="content", path="wiki/concepts/", context=1)` — tag-based discovery
   - Search for specific sub-topic filenames: `*swe-bench*`, `*arena*`, `*eval*`
3. **Read discovered pages** (at least frontmatter + first 25 lines) to understand each page's scope
4. **Write the full MOC** with `write_file` — this replaces the stub entirely
5. **Bidirectional cross-links**: Add MOC links to 2-3 key related pages (not just the central one):
   ```python
   # In ai-evaluation.md, ai-benchmarks-evals-overview.md, etc.
   patch(old_string="existing link section",
         new_string="- [[concepts/theme-moc]] — Theme MOC (navigation hub)\n- existing links...")
   ```
6. **Update index.md**: Replace the stub description with a rich MOC description
7. **Standard**: `git add` → commit → push

## Adding an Evolution Timeline

MOC pages benefit from an ASCII timeline showing how the domain evolved:

```markdown
## Evolution Timeline

\```
2020-2022: Static benchmark golden age (MMLU, GSM8K, HumanEval)
    ↓
2023: SWE-bench arrives → first agentic benchmark
    ↓
2024: Benchmark saturation (MMLU→MMLU Pro, ARC→ARC-AGI 2)
    ↓
2025: Evals culture rises (Langfuse Academy, eval vs monitoring debate)
    ↓
2026: Agent evaluation matures (Agent Arena, causal tracing, macro evals)
\```
```

This helps readers quickly understand the trajectory without reading every linked page.

## External Documentation Hub Pattern

When the source URL is itself an **index/hub page** pointing to multiple documents (e.g., a company's safety documentation portal, a research lab's publication index), the ingestion pattern is:

1. **Fetch the hub** — extract the full list of linked items (titles, URLs, dates, excerpts)
2. **Create a concept page** as the hub, using `type: concept` — this IS the MOC for the external site
3. **Create a raw article** for the hub page itself (the index page is a source too)
4. **Full item index** — include ALL items in a table with date, title, URL, and key theme/category
5. **Structural analysis** — identify patterns across items (e.g., safety level escalation, capability progression)
6. **Bidirectional cross-links** — link to existing related wiki pages AND update those pages to link back
7. **Tag taxonomy check** — domain-specific framework tags (e.g., `preparedness-framework` for OpenAI, `responsible-scaling-policy` for Anthropic) may need adding to SCHEMA.md before commit

Example: `concepts/openai-deployment-safety-hub.md` (2026-06-10) — ingested deploymentsafety.openai.com as a hub for 19 OpenAI system cards. Bidirectional links to `anthropic-system-cards` and `model-cards-system-cards`. Required adding `preparedness-framework` tag to SCHEMA.md.

## Directory-Based MOC Restructuring

When a MOC grows to cover 15+ individual pages in a single category, consider restructuring into a directory hierarchy. See `references/wiki-directory-restructuring.md` for the full workflow (merge pages → create `concepts/<topic>/` directory → batch backlink updates → sub-index).

Key decision: Whether to move existing enriched pages depends on user preference.

**Option A — Link only (keep in place)**: Less disruptive, no backlink updates needed. The sub-index links to pages at their current location. Works when pages are scattered across different concerns.

**Option B — Move everything (2026-06-10 benchmark pattern)**: User explicitly requested ALL benchmark pages be consolidated under `concepts/ai-benchmarks/`. This required moving 34 files, updating 60+ backlinks via batch sed, and handling duplicates from concurrent sessions. The benefit is a clean, self-contained directory where every page belongs. Use this when the user wants a unified namespace for the topic.

When moving enriched pages, always check for duplicates (files at both old and new locations) and keep the richer version.

## Pitfalls

- **Don't duplicate content** — MOC pages are navigational, not analytical. Link to the deep page rather than reproducing its content.
- **Same frontmatter rules** — must have `type: concept`, valid tags from SCHEMA.md, minimum 2 outbound wikilinks (trivially satisfied by MOCs).
- **Keep it current** — add a "Last updated" note at the bottom. MOCs become stale as new pages are added.
- **Blog articles live at repo root** — `~/ai-topics/blog/`, NOT `~/wiki/blog/`. When searching for blog content, search both locations.
- **⚠️ Language policy applies**: ALL non-raw/ wiki content must be English — including MOC table headers, section titles, and cell content. Even when the user communicates in Japanese, write the wiki page in English. This is the #1 commit-blocker for MOC pages because they have many table cells and section headers where Japanese slips in naturally. See `references/precommit-pitfalls.md` section 3.
- **⚠️ Tag validation before commit**: MOC pages tend to use broad conceptual tags. Verify every tag exists in SCHEMA.md before committing. Common trap: `evaluation-methodology` (not in SCHEMA) vs `evaluation` (in SCHEMA). Run `grep "tag-name" wiki/SCHEMA.md` for any tag you're unsure about.
