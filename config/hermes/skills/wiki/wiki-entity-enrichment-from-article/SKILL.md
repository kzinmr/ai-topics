---
name: wiki-entity-enrichment-from-article
description: Create or enrich wiki entity and concept pages from raw articles, multi-source web research, newsletters, and tool/project investigations. Supports both article-driven enrichment and from-scratch entity page creation via website + docs + X/Twitter + GitHub/NPM research.
trigger: When asked to explain an article, create concept pages from raw content, convert newsletter articles into wiki entries, ingest a lecture/workshop transcript (see references/transcript-ingestion.md), create a comprehensive entity page for a tool/project from scratch via multi-source research, create an AI model entity page from arXiv paper + project page + HuggingFace sources, enrich a status:skeleton entity page from scratch, batch-create company entity pages, batch-create person entity pages from X handles (see references/batch-person-entity-creation.md), ingest a conference/event summary article (see references/event-summary-article-workflow.md), ingest an X/Twitter post into the wiki (see references/x-note-tweet-ingestion.md), ingest a research paper with benchmark dataset (see references/research-paper-ingestion.md), OR cross-reference a newly ingested article with existing concept pages (connect/relate/link to PTC, RLM, SaC, etc.).
---

# Wiki Article Processing & Concept Creation

## Cross-Referencing with Existing Concepts

When a user asks to "connect" or "relate" a newly ingested article to existing wiki concepts (e.g. "最近追加したPTC, RLMの概念とも関連つけて"), follow this workflow:

### Step 1: Find Existing Concept Pages by Abbreviation

Users often reference concepts by abbreviation (PTC, SaC, RLM, DCI). **Do NOT search by file glob** — concept pages may have long names (`programmatic-tool-calling`) or live in unexpected locations. Instead:

```
search_files(pattern="PTC", target="content", path="wiki/index.md")
search_files(pattern="PTC", target="content", path="wiki/log.md")
```

The index.md and log.md are the authoritative lookup tables. Log.md often has richer context about what was added and when.

### Step 2: Read Each Concept Page and Identify Connection Points

Read the concept pages to understand:
- What problem does each concept solve?
- How does the new article's framework relate to that problem?
- Does the article validate, contradict, extend, or provide a different lens on the concept?

### Step 3: Write a Synthesis Section in the Main Concept Page

Add a section (e.g. "Beyond the Binary: Hybrid Architectures") that:
- Frames the article's core argument as a lens for understanding the concepts
- Creates a comparison table showing how each concept addresses the article's concerns
- Draws a structural diagram (ASCII or table) showing where concepts sit on a spectrum
- States a key insight that ties them together

### Step 4: Add Bidirectional Links

For each related concept page, add a one-line backlink in its Related Concepts section:
```markdown
- [[concepts/new-article-concept]] — One-line description of the relationship
```

Also add `related:` frontmatter to the main concept page.

### Example: "Build agents, not pipelines" × PTC/SaC/RLM

The article argued pipeline vs agent is binary. PTC, SaC, and RLM collapse that binary:
- **PTC**: Agent writes its own pipeline per-task (87-92% token reduction)
- **SaC**: PTC applied to search (composable SDK primitives)
- **RLM**: Recursive context management (small model + deep recursion ≈ large model)

Each got a comparison table row and a one-line backlink. The main page got a "Beyond the Binary" synthesis section with an ASCII spectrum diagram.

## Workflow

For X/Twitter Note Tweet ingestion specifically, see `references/x-note-tweet-ingestion.md` for the full end-to-end pipeline (xurl fetch → raw article → entity page → related page updates).

### 0. Page Placement Decision: New Page vs. Section in Existing Page

> **⚠️ MANDATORY**: Before any `write_file`, run `search_files` to check for existing pages. Overwriting 100-200+ line pages destroys curation work. See `references/pre-write-verification.md` for the full protocol and recovery procedure.

Before creating a new page, determine whether the article describes a **standalone concept** or a **sub-topic/extension of an existing concept**:
| A comparison or survey across multiple concepts | Create new concept page with cross-references | "Agent harness comparison" → new concept page |

> **Heads-up — Multi-target pattern for landmark articles:** When a landmark article by a major figure reframes an existing concept (rather than introducing a new one), the correct action is almost always a **three-part enrichment**: (1) enrich the existing concept page with a dedicated section, (2) create an entity page for the author if they're not in the wiki yet, and (3) enrich any related entity pages that the article prominently references (e.g., the person who coined a term the article popularizes). This avoids the trap of creating a "new concept" page from content that is really a commentary on an already-documented concept.

| Article describes... | Action | Example |
|---|---|---|
| A new standalone concept, tool, person, or entity | Create new page in `concepts/` or `entities/` | New agent harness, new researcher |
| A major extension, feature, or sub-topic of an existing concept | **Add a dedicated section to the existing concept page** | MCP Apps → section in `concepts/mcp.md` |
| A **landmark/commentary article** about an existing concept by a major figure — article reframes/popularizes/situates an already-documented concept historically without introducing a standalone new concept | **Enrich the existing concept page** (add dedicated section) **+ create entity page for the author** if not in wiki **+ enrich related entities** that the article references | Tim O'Reilly's "End of Programming" about vibe coding → enrich vibe-coding page + create tim-oreilly entity + enrich addy-osmani with 70% Problem |
| A minor update or product announcement for an existing entity | Add a timeline entry or brief note to the existing entity page | New Claude version → add to `entities/anthropic.md` |
| A comparison or survey across multiple concepts | Create new concept page with cross-references | "Agent harness comparison" → new concept page |

**Heuristic**: If the new content would be confusing or incomplete without the parent concept's full context, it belongs as a section within the parent page. Standalone pages should be independently understandable.

When adding a section to an existing concept page:
- Add context about **competing alternatives** (if applicable — e.g., MCP-UI vs MCP Apps)
- Update the page's `tags` and `sources` frontmatter
- Add cross-references in the "Related Concepts" section
- Add a **Source** subsection with `[[raw/articles/...]]` wiki-link to the raw article

### 1. Read Raw Article
- Check if already scraped to `wiki/raw/articles/`
- If not, scrape and save with descriptive filename
- **Filename format:** Always use the **actual publication date**, not the ingestion date. Follow the [[raw-article-filename-policy]] skill for the exact format.
- **Single-scoop principle:** If the article text fits in one well-structured block at the top of the file, keep the raw article as one block. Do NOT split long articles into separate files unless there are truly independent sub-articles with their own publication dates.
  - Sources to check in order: Substack article header, blog `<time>` tags, `article:published_time` meta, search result snippets, Wayback Machine, RSS feed `<pubDate>`
- **Reddit scraping fallback:** Modern Reddit UI (reddit.com) blocks `web_extract` via JS rendering. Use `old.reddit.com` instead — prefix the URL with `old.` (e.g., `old.reddit.com/r/LocalLLaMA/comments/...`). This returns clean HTML with full post text and top comments.
- **Paywalled blog scraping:** If `web_extract` returns paywall overlay, try Jina Reader API (`r.jina.ai/<URL>`), sitemap.xml paths, or RSS feeds
- **Massive single-page hypertext articles (gwern.net pattern):** When the source is a long-form hypertext essay (e.g., gwern.net, LessWrong sequences) where `web_extract` returns only an AI-generated summary or truncated content:
  1. Use `browser_navigate` to load the page first (the browser tool renders the full DOM)
  2. Extract full text via `browser_console` with `document.body.innerText.substring()` split into chunks of ~40,000 characters:
     ```
     browser_console(expression="document.body.innerText.substring(0, 40000)")
     browser_console(expression="document.body.innerText.substring(40000, 80000)")
     ```
  3. Extract the article structure info (title, publication date, tags) from the page metadata and rendered text
  4. Merge chunks into a single raw article — the first call includes the article title/date header; subsequent calls continue where the previous left off
  5. **Filename:** Use the actual publication date from the page metadata (check `<meta property="article:published_time">` or visible date text). These pages often have a date range (e.g., "2020-05-28–2022-01-02") — use the START date
  6. **Why this works:** The browser renders the full DOM even when `web_extract` collapses the content. The text is available client-side in `document.body.innerText`. Split into chunks because `browser_console` may truncate very long strings (>100K chars)

### 2. Analyze Content
- Extract key concepts, terminology, and claims
- Identify related existing wiki pages
- Note any people, projects, or tools mentioned
- **Detect author entity sub-page structure**: If the article author has dedicated sub-pages (e.g., `karpathy-writings`, `karpathy-ideas`, `karpathy-projects`, `karpathy-research`), plan to distribute the article's content across ALL relevant sub-pages — not just the main entity page. The writings sub-page gets the post-mortem/details, the ideas sub-page gets the high-level theses/insights, and the concept page gets the case study. A single article from a prolific author may touch 3+ pages simultaneously.
- **Detect subdirectory promotion candidates**: Check if a subdirectory concept page already exists (e.g., `concepts/fine-tuning/pytorch-fsdp.md`) that overlaps with the new page you're about to create. If the new page is richer and should be the canonical version, plan the promotion pattern (see Section: Subdirectory Promotion).

### 3. Create Concept Page (if doesn't exist)
```markdown
---
title: "Concept Name"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [concept, tag1, tag2]
aliases: [alias1, alias2]
related: [[related-page-1]], [[related-page-2]]
sources: [URL or path to raw article]
---

# Concept Name

## Summary
Brief overview of the concept (2-3 sentences)

## Key Ideas
- Idea 1
- Idea 2
- Idea 3

## Terminology
- **Term**: Definition

## Examples/Applications
- Example 1
- Example 2

## Graph Structure Query (for knowledge base traversal)
When designing concept pages for a wiki knowledge base that supports graph traversal queries, add this section to define explicit, typed relationship edges. This enables structured queries like "find all concepts by author X" or "which concepts contrast with graphrag."

```
[this-concept] ──author──→ [entity: creator-name]
[this-concept] ──contrasts──→ [concept: alternative-approach]
[this-concept] ──extends──→ [concept: broader-framework]
[this-concept] ──relates-to──→ [concept: adjacent-topic]
[this-concept] ──embodies──→ [concept: underlying-philosophy]
```

**Edge types to consider:**
| Edge Type | When to Use |
|-----------|-------------|
| `author` / `coauthor` | Article author(s) as entity pages |
| `contrasts` | Directly opposing or competing approach |
| `extends` | The concept adds to or builds on a broader framework |
| `relates-to` | Adjacent topic with meaningful connection but no direct dependency |
| `embodies` | This concept is a concrete instance or application of a philosophy/framework |
| `teaches` | The concept functions as a tutorial or methodology guide |
| `precedes` / `follows` | Chronological ordering between related concepts |
| `part-of` | Hierarchical inclusion (sub-concept of a larger concept) |

Include actual wikilinks in a prose description below the diagram, e.g.:
> This section informs graph queries: authored by [[entities/hamel-husain]], contrasts with [[concepts/agentic-alternative-to-graphrag]], embodies [[concepts/harness-engineering]].

## Related Concepts
- [[related-page-1]]
- [[related-page-2]]

## Sources
- [Article Title](URL)
```

### 4. Create/Update Entity Page — Pre-Creation Verification

**BEFORE creating any new entity file, run this pre-creation verification checklist. `search_files` alone is unreliable — it has false-negative issues where it returns 0 results for files that actually exist.**

#### Pre-Creation Checklist (Run ALL of these)

```bash
# 1. Filename search (most reliable — use this FIRST)
ls ~/wiki/entities/ | grep -i "partial-name\|@handle\|fullname"
find ~/wiki/ -name "*partial-name*" -o -name "*other-variant*" 2>/dev/null

# 2. Index check (catches alternate slugs and stubs)
grep -i "@handle" ~/wiki/index.md | head -5
grep -i "Full Name" ~/wiki/index.md | head -5

# 3. Content search for aliases (catches frontmatter aliases)
grep -ril "alias-name\|@handle" ~/wiki/entities/ --include="*.md" 2>/dev/null

# 4. Search under alternate slug patterns
# Known traps: GitHub handle vs real name (e.g., mitsuhiko vs armin-ronacher)
#               handle vs full-name (e.g., vtrivedy10 vs varun-trivedy)
#               first-last vs handle-first (e.g., zach-mueller vs the-zach-mueller)
for slug in "full-name-slug" "first-last" "@handle-stripped"; do
    ls ~/wiki/entities/"$slug".md 2>/dev/null && echo "FOUND: $slug"
done
```

**If ANY check finds a match, do NOT create a new file.** Update the existing page instead (patch frontmatter, add sections, update sources). This applies even if the existing slug differs from what you planned (e.g., `zach-mueller` already exists even if you planned `the-zach-mueller`).

**Duplicate cleanup workflow** (if you discover mid-session that you created a duplicate):
1. Delete the duplicate file: `rm ~/wiki/entities/your-duplicate-slug.md`
2. Fix index.md: replace any entry referencing the wrong slug with the correct slug
3. Fix cross-references: update any `related:` frontmatter or inline wikilinks that reference the wrong slug — use `patch` on each affected page
4. Enrich the canonical page: add sources, updated date, and cross-refs section via `patch`
5. Update log.md: correct any reference to the wrong slug
6. Ensure the duplicate file is NOT in git add (it was deleted before staging)

- Follow same format but focused on the person/entity
- Include bio, contributions, key ideas, notable works
- Cross-link to concepts and other entities

### 5. Multi-Source Tool/Project Entity Page (From Scratch)

Two variants — **article-driven** (has a raw article as starting point) and **pure-web** (no article, just URLs/handles):

| Variant | Starting Point | Target |
|---------|---------------|--------|
| **Article-driven** | Raw article exists but is insufficient alone | Conduct multi-source research to fill gaps |
| **Pure-web** | No article — just a website URL, GitHub repo, or tool name | Build entity page from zero via website scraping + docs + GitHub + X/Twitter + registries |

**For pure-web** (no article — tool discovered via website URL, GitHub, or X/Twitter mention):
1. **Extract the homepage** (`web_extract` the landing page) — identify the product category, pitch, supported platforms, key differentiator
2. **Extract documentation** (`web_extract` the docs root and 2-3 key subpages) — features, CLI reference, architecture, installation
3. **Extract GitHub README** — language breakdown, license, star count, contributor count, recent commits
4. **Search for ecosystem context** — tools that integrate with it, competitors, community adoption (via `web_search`)
5. **Check for arXiv or technical papers** — Many modern AI tools/projects publish accompanying technical papers. Search: `web_search "ProjectName" arxiv` and check the GitHub README's bottom sections (often links to papers). If found, scrape the arXiv abstract page (`web_extract arxiv.org/abs/XXXX.XXXXX`) as a key source for architecture details, benchmarks, and formal contributions. Add it to the entity page's sources and architecture/benchmark sections.
6. **Identify the underlying infrastructure technology** — e.g., Dolt is a product, but understanding it requires documenting Prolly Trees, Dolt MCP, the commit graph architecture. These deserve their own subsections within the entity page, not just external links.
7. **Proceed to step 2** (Scrape the website) below — but skip the "Read the raw article" step

**Common sub-steps (both variants):**
2. **Scrape the website** (`web_extract` the homepage and docs subpage) — extract features, architecture, supported agents, community links
3. **Search X/Twitter** — find the creator's pinned post / launch announcement (often contains key context like "v1 is live")
4. **Search GitHub profile** — discover related projects by the same creator (often builds an ecosystem)
5. **Search NPM/Package registries** — confirm package name, version, CLI command
7. **Search for installation guides** — third-party blogs may document setup steps and architecture
8. **Create person entity page for the creator** — If the creator (individual or team) doesn't have a wiki page yet, create one. The person entity page should include: professional background, related projects, their key theses/ideas, blog URL, social handles, and cross-references to the service/tool entity they created.
9. **Check speaker profiles** — conference speaker pages (Google Cloud Next, etc.) often contain professional bios

#### Entity Page Structure for Tools/Projects

```markdown
---
title: ProjectName
type: entity
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - devtools
  - ai-agent
  - orchestrator  # adapt to project type
  - open-source
aliases:
  - alias1
  - alias2
sources:
  - raw/articles/article-file.md
  - https://project-website.com/
  - https://project-website.com/docs
---

# ProjectName

**ProjectName** is a [one-sentence description]. Built by [[entities/creator-name|Creator Name]], it provides [core value proposition].

[2-3 sentence overview of how it works — architecture principle, supported agents, key differentiator]

## Getting Started

```bash
npx @npm-package/name
```

## Key Features

Use H3 sections with bullet points for each feature. Prefer subsections over a flat list:

### Feature 1 Title
Description of what this feature does and why it matters.

### Feature 2 Title
...

### Additional Features
- **Feature A** — Brief desc
- **Feature B** — Brief desc

## Supported Agents (for agent orchestration tools)

| Agent | Status | Description |
|-------|--------|-------------|
| **Agent A** | Primary | Full integration |
| **Agent B** | Supported | Details |

## Architecture

Describe the architecture layers (client-server, hook-based, etc.) followed by an ASCII diagram:

```
┌──────────────────────────────┐
│        Browser UI (Port)     │
└─────────┬────────────────────┘
          │ WebSocket / REST
┌─────────▼────────────────────┐
│         Server (Node.js)      │
│    Event Processing · State   │
└──┬──────────┬──────────┬─────┘
   ▼          ▼          ▼
┌──────┐  ┌────────┐  ┌──────┐
│Agent A│  │Agent B │  │Agent C│
└──────┘  └────────┘  └──────┘
```

## Related Tools

- [[entities/related-tool-A]] — Description
- [[entities/related-tool-B]] — Description

## Creator

Built by **Name** (@handle), [role]. Also known for [other projects]. [Brief professional background paragraph from conference bios, LinkedIn, etc.]

## Community

- **Website**: URL
- **Docs**: URL
- **App**: URL
- **Discord**: URL
- **X/Twitter**: URL

## Sources

- [Source Name](URL) — Note (e.g., "Scraped YYYY-MM-DD")
- [Source Name](URL)
```

### 5a. Concept Abstraction from Service/Tool Investigation

When investigating a service/tool that embodies a **broader paradigm or architectural concept** beyond the service itself, create separate concept pages and cross-link them:

**When to abstract:**
- The service is the **first/only canonical implementation** of a pattern worth documenting (e.g., searchcode.com → code-intelligence-for-llms, B2A)
- The service exemplifies a **named thesis or framework** from its creator (e.g., searchcode.com → "Marketing to the Machine" → B2A concept)
- Other services/projects could implement the same pattern (future-proofing the concept)

**Cross-referencing pattern:**
```
entity: service-example        →  "Canonical implementation of [[concept/p]]"
concept: paradigm/concept       →  "Representative implementation: [[entities/service-example]]"
entity: creator-person          →  "Author of the [[concept/paradigm]] thesis"
```

**Workflow order:** Raw article → entity page (service) → entity page (creator) → concept(s) → update entity page cross-references → index/log → commit

### 5b. Skeleton Entity Page Enrichment (From Scratch — No Article Source)

When a person/blogger entity page exists as a `status: skeleton` in `~/wiki/entities/` with no raw article to drive enrichment (just frontmatter + raw article references), enrich it from scratch via multi-channel web research:

1. **Read the existing page** — note the frontmatter (`title`, `url`, any references), current `status: skeleton`
2. **Check RSS feed for article inventory** — Try `/rss.xml`, `/feed.xml`, `/atom.xml` first. RSS gives all article URLs, titles, and dates in one call — much faster than scraping individual archive pages. Cross-reference RSS entries against the skeleton's reference list to map hash-based references (e.g., `mahadk.com--posts-arc-boost--1c8b9380`) to actual topics.
3. **Scrape the person's website/blog** (`web_extract` the about page, homepage, and 2-3 recent posts)
3. **Research professional background:**
   - `web_search` for name + biography / founder / educator / researcher
   - Check Wikipedia, LinkedIn, Crunchbase
   - Check GitHub profile, Hugging Face profile, social media bios
4. **Identify core content themes:** What specific topics do they write about? (smolagents, LLM from scratch, fine-tuning, etc.)
5. **Search for specific article series** that demonstrate depth (e.g., "LLM from scratch part 1", multi-part tutorials, comparisons)
6. **Analyze writing style** from sampled blog posts

#### Target Page Structure (Person/Blogger Entities)

```markdown
---
title: slug
description: One-line description covering who they are + what they write about + why they matter
url: https://theirblog.com
type: entity
updated: YYYY-MM-DD
aliases: [handle1, Full Name]
tags:
  - person
  - ml-researcher
  - educator
  - python-developer
  - [other-relevant-tags]
sources:
  - https://theirblog.com/about
  - [external-Bio-wiki-wikipedia-etc]
---

# Full Name

**Full Name** (handles: `handle`) is a [role descriptor]. [2-3 sentence intro covering background, major achievement, current focus]

## Overview

Detailed biographical paragraph covering:
- Programming/entrepreneurial background
- Notable projects or companies founded
- Current research/publishing focus
- Platform presence (GitHub, social media handles)

## Core Topics

Subsections for each major topic area they write about, with specific article titles and links:

### Topic Area 1 (e.g., smolagents Tutorials)
- **Article Title** (Month Year) — What it covers, why it matters
- **Article Title** (Month Year) — ...

### Topic Area 2 (e.g., LLM from Scratch Series)
Overview of the series scope, key experiments, model releases, and significant findings.

## Writing Style & Philosophy

Analysis of their writing approach — what makes their content distinctive. Characteristics to consider:
- Narrative voice (first-person, instructional, analytical)
- Transparency (sharing failures, uncertainties)
- Experimental grounding (code-driven claims)
- Comparative thinking (side-by-side evaluations)
- Breadth of perspective (cross-domain experience)

## [Entrepreneurial / Professional Background]

### Company/Project Name (YEAR–YEAR)
What they built, key milestones, acquisition/exit if any.
Use separate H3 subsections for each major venture.

## Cross-References

- **[[existing-entity-page]]** — Description of relationship and connection
- **smolagents** — (if no entity page exists yet, use plain text)

## References

- `references/mcp-apps-ingestion-2026-05-07.md` — Session reference for ingesting sub-topic articles as sections within existing parent concepts. Covers decision heuristic, workflow, and competing UI-over-MCP standards discovered during MCP Apps ingestion.


- `references/mcp-apps-session-2026-05-07.md` — Full session transcript for MCP Apps ingestion: decision to add as section within `concepts/mcp.md` rather than standalone page, comparison with competing UI-over-MCP standards, index/log update workflow.

All existing raw article references preserved from the original skeleton.
```

#### Section Requirements
- **Overview** — Must cover: background, blog age/scope, current focus
- **Core Topics** — Must capture their specific technical writing areas with concrete article titles
- **Writing Style & Philosophy** — Required for bloggers/educators; captures their distinctive voice
- **Cross-References** — Link to related wiki entities; use `[[wikilink]]` for existing pages, plain text for pages that don't exist yet
- **References** — Preserve all existing raw article references from the original skeleton

#### Frontmatter Cleanup
- Remove `status: skeleton` entirely
- Add `type: entity` (if missing)
- Add `updated: YYYY-MM-DD`
- Add `tags` array with relevant person/topic tags
- Add `aliases` for handles and full name
- Add `sources` array with URLs to about page, Wikipedia, social profiles

#### Research Sources to Check (in priority order)
1. Person's own website / about page
2. Wikipedia / Python wiki / other community wikis
3. GitHub profile (pinned repos, bio, followers)
4. Hugging Face profile (models, datasets, bio)
5. LinkedIn (professional background, education)
6. Social media bios (X/Twitter, Bluesky)
7. Search results for name + "founder" / "background" / "biography"
8. Crunchbase / RocketReach (for entrepreneurial backgrounds)
9. Conference speaker pages (for bios and talk titles)

#### Pitfalls
- Multiple people may share the same name — verify you have the right person by cross-referencing handles and blog URL
- Don't replace existing raw article references — preserve them in the References section
- Don't add wikilinks to pages that don't exist yet — use plain text for those
- Blog RSS feeds may not capture the full article archive — check the blog's archive pages too
- If blog articles return 404 (common with older URL schemes), search for cached versions or Wayback Machine
- If no cached version exists either, use the RSS feed metadata (title, date) to include a summary entry marked **(Archived)** — this preserves the article's place in the author's bibliography without fabricating content
- Target 8-12KB for the final enriched page, matching `antirez-com.md` / `simon-willison.md` depth

### 5d. Subdirectory Promotion Pattern

When you discover that a subdirectory concept page (e.g., `concepts/fine-tuning/pytorch-fsdp.md`) already exists but your new top-level page is richer and should become the canonical reference:

#### Detection

- `search_files` or `ls` reveals a `.md` file under `concepts/subdirectory/` (e.g., `concepts/fine-tuning/pytorch-fsdp.md`)
- The subdirectory page was created in a prior session with useful content but limited depth
- Your new page covers the same concept at higher depth, with more sources, comparisons, and cross-references

#### Workflow

1. **Create the new top-level page** (`concepts/your-concept.md`) with full content — this becomes the canonical reference
2. **Update the subdirectory page** — keep all existing content, but add:
   - A redirect notice at the top: `> **Canonical page moved up.** This subdirectory page was merged into [[concepts/your-concept]] for the comprehensive reference. Key content retained below.`
   - Updated frontmatter: bump `updated` date, add `aliases` if needed, add the new top-level page to `related:`, add the new raw article to `sources:`
   - Update `related:` frontmatter to include `concepts/fsdp-qlora`, `concepts/qlora`, and the new top-level page
3. **Update all cross-references**: Search for wikilinks to the OLD subdirectory path and add the NEW top-level path alongside them:
   ```bash
   grep -r "concepts/fine-tuning/pytorch-fsdp" ~/wiki/ --include="*.md" | grep -v ".md.swo\|.git"
   ```
4. **Update `concepts/_index.md`** if the subdirectory has an index page — add a note pointing to the new top-level page
5. **Update `wiki/index.md`** — add an entry for the new top-level page in the Concepts section (simple `- ` prefix format, no renumbering needed)
6. **Log the promotion**: In log.md, note both the creation of the new page AND the update of the subdirectory page as a pointer

#### Pitfalls
- Don't delete the subdirectory page — it may have inbound wikilinks from other pages. Preserve it as a redirect with retained content
- Don't forget to update `related:` frontmatter on BOTH pages (bidirectional cross-references)
- Check `index.md` for the subdirectory page's existing entry — update its description to note the redirect, don't remove it
- The subdirectory page's existing sources should remain in its frontmatter; the new top-level page gets its own sources array

#### Example

From this session: `concepts/fine-tuning/pytorch-fsdp.md` (100 lines, Axolotl-focused) → `concepts/pytorch-fsdp.md` (239 lines, comprehensive). Subdirectory page updated with redirect notice, new frontmatter fields, and cross-refs to the new top-level page.

When the user provides an **arXiv paper + official project page** (no blog article) and asks to create a wiki page for an AI model/system:

**Source triad**: arXiv paper → project page → HuggingFace model card. These three sources together provide architecture details, benchmarks, and deployment info that a single blog post wouldn't.

**Research steps** (modify section 5's general steps for this pattern):
1. `web_extract` the arXiv abstract page → paper summary (architecture, innovations, benchmarks)
2. `web_extract` the official project page → capabilities, features, demo links
3. `web_extract` the HuggingFace model card → model variants, training details, safety features, license
4. `web_search` the model name for third-party analysis (benchmarks against competitors, community reception)

**Entity page structure for AI models** (extends section 5's tool/project template):

```markdown
---
title: "Org ModelName"
type: entity
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - entity
  - model
  - [org-name]
  - tts / llm / speech / vision  # adapt to model type
  - diffusion / transformer / mamba  # adapt to architecture
  - open-source / proprietary
related:
  - [competitor-entity]
  - [broader-concept-page]
sources:
  - raw/articles/paper-summary.md
  - https://arxiv.org/abs/XXXX.XXXXX
  - https://org.github.io/ModelName/
  - https://huggingface.co/org/ModelName
status: skeleton  # optional — remove after enrichment
---

# Org ModelName

## Architecture

Break down into 2-3 core components with parameters:

### Component 1 (e.g., Tokenizer)
- Base technique (σ-VAE, flow-matching, etc.)
- Key specs: frame rate, compression ratio, parameter count
- Novelty vs prior art (e.g., "80× better than Encodec")

### Component 2 (e.g., Language Model)
- Base model / size
- Context length and training curriculum
- Role in the pipeline

### Component 3 (e.g., Decoder/Head)
- Layer count, parameter count
- Inference technique (DDPM, CFG, DPM-Solver)
- Latency characteristics

## Model Variants

| Variant | Base LLM | Params | Capability | Max Duration | Latency | Status |
|---------|----------|--------|-----------|-------------|---------|--------|
| Variant-A | ... | ... | Full | ... | ... | Released |
| Variant-B | ... | ... | Streaming | ... | ~Xms | Released |

## Key Capabilities

| Capability | Detail |
|-----------|--------|
| Max duration | ... |
| Max speakers / inputs | ... |
| Languages | ... |
| License | ... |

## Benchmark Performance

- Conference venue (e.g., ICLR 2026 Oral)
- Objective metrics vs competitors (WER, similarity, etc.)
- Subjective human evaluation results

## Safety & Limitations

### Safety Features
- Content filtering, watermarking, logging, disclaimers

### Out-of-Scope Uses
- Voice impersonation, real-time deep-fakes, etc.

### Known Limitations
- What the model cannot do (no overlapping speech, single language only, etc.)

## Comparison: ModelName vs CompetitorModel

| Aspect | This Model | Competitor |
|--------|-----------|-----------|
| Architecture | ... | ... |
| Size | ... | ... |
| Max output | ... | ... |
| Languages | ... | ... |
| License | ... | ... |

## Related Concepts
- [[entities/competitor-model]]
- [[concepts/broader-category]]

## TODO
- [ ] Monitor for updates
- [ ] Enrich with hands-on evaluation
</markdown>

**Key sections unique to model entities** (not in tool/project template):
- Architecture breakdown with parameters (tokenizer, LLM, decoder)
- Model variant table (sizes, capabilities, availability)
- Benchmark performance with venue (ICLR, NeurIPS)
- Safety & Limitations section (guardrails, out-of-scope uses)
- Comparison table with similar models (architecture-level, not just feature-level)

**Concept page competitive positioning update** (AFTER creating the entity):

This is a critical step that differs from tool/project ingestion:

1. Search for **broader concept pages** that categorize this type of model:
   ```bash
   grep -r "competitor-name\|similar-model" ~/ai-topics/wiki/concepts/ | grep -oP '\[\[concepts/[^\]]+' | sort -u
   ```
2. For each concept page found:
   - Check if it has a **Key Players** or **Competitive Positioning** section
   - If it has a **comparison table**, add the new model as a row
   - If it has a **"Open vs Closed"** / "Market Dynamics" section, add a mention
   - Update the concept page `sources:` frontmatter if appropriate
   - Add a wikilink in the concept page's **Related Concepts** section
3. Also update `concepts/speech.md` or the most general parent concept:
   - Add `[[entities/new-model]]` to the Related Concepts list

### 6. Update All Index Files

Tool/project entity pages require **three** index updates:

**Pitfall — stubs missing from index.md**: A concept or entity page may exist as a file (possibly created by an earlier cron job or bulk import) but be absent from `wiki/index.md`. Always verify the page appears in the index after creation or enrichment. If missing, add an entry in the alphabetically-correct location with a one-line summary.

1. **`wiki/entities/_index.md`** — Add entry with wikilink and one-line summary. Verify alphabetical sort order with `read_file` before patching.
2. **`wiki/index.md`** (top-level wiki index) — Add entry under Entities section with wikilink and shorter summary. Same alphabetical placement.
3. **`wiki/log.md`** — Prepend entry with date, entity wikilink, key features summary, and raw article path.

When patching `entities/_index.md`, `concepts/_index.md`, or `wiki/index.md`:
- Read the surrounding lines first with `read_file(offset, limit)` to find the exact insertion point
- Use `patch` with enough context to make the old_string unique (include surrounding lines)
- Verify the patch result by reading again — check for formatting issues (e.g., `|-` instead of `-`, or `||-` double-pipe)
- **PIPE PREFIX PITFALL**: The `patch` tool is fragile with pipe-prefixed list entries that appear in `entities/_index.md` and `concepts/_index.md`. When these files use `|- ` prefix format (because of markdown table syntax), and your old_string uses `- ` (without the pipe), the patch tool adds an extra `|` on every inserted line creating `||- ` artifacts. **Fix:** After every patch on `_index.md` files, immediately `read_file` the affected lines. If you see `||- ` artifacts, use `sed -i 'N,Ns/^|//' PATH` to strip the extra leading pipe. Then re-verify.
- **PARTIAL-MATCH CORRUPTION on patch**: When your `old_string` matches only a PREFIX of the target line (not its full content), the patch tool replaces the matched portion and appends the REMAINING original text onto your `new_string`. This creates corrupted entries where original line tail leaks into the new content. **Fix:** Always include enough trailing context in `old_string` to uniquely identify the ENTIRE line — read the file with `read_file(offset, limit)` and copy the exact bytes. After every patch on index files, immediately re-read the affected lines to detect appended garbage. If found, fix with a second `patch` that replaces the corrupted substring.
- **EMBEDDED LINE-NUMBER CORRUPTION in `_index.md` and `index.md` files**: Several index files (`entities/_index.md`, `concepts/_index.md`, AND the main `wiki/index.md`) have old line numbers embedded in the actual file content (e.g., `   169|- [[entities/jaya-gupta]]` where `169` is an embedded line number, not a `read_file` display artifact — it is literally in the file). The `patch` tool consistently fails on these files — it either cannot find a match or produces hybrids like `171|   169|- [[slug]]`. Additionally, the embedded number format varies: some lines have `NNN|- ` prefix, some have `- ` prefix, causing unpredictable patch behavior. **DO NOT use `patch` for any index files that show embedded line numbers in `read_file` output.** Always verify with `sed -n 'N,Np' PATH` to see the actual file bytes. Use Python for ALL insertions instead:

  #### CRITICAL: Sections have DIFFERENT formats — Know Which One You're Editing

The three index files use DIFFERENT formats depending on section. Accidentally applying the wrong method will corrupt the file.

| File / Section | Format | Example | Insertion Method |
|----------------|--------|---------|-----------------|
| **Entities** section in `wiki/index.md` | `NNN|- [[slug]]` (embedded line numbers + pipe-dash) | ` 256|- [[entities/phil-schmid]]` | **Python with renumbering** (never `patch`) |
| **Concepts** section in `wiki/index.md` | `- [[slug]]` (simple dash-space, NO line numbers) | `- [[concepts/accelerate]]` | **Simple `patch` or `list.insert()`** — no renumbering |
| **entities/_index.md** | `NNN|- [[slug]]` (embedded line numbers) | Same as Entities section | **Python with renumbering** |
| **concepts/_index.md** | `NNN|- [[slug]]` (embedded line numbers) | Same | **Python with renumbering** |

> **Entities section = `NNN|- ` format → use Python with renumbering. Concepts section = `- ` format → use simple `patch` or `insert`.**

To verify which format a section uses before editing:
```bash
# Check a few lines around your insertion target
sed -n '200,210p' ~/wiki/index.md | head -5  # Check format
```
If you see `NNN|- ` anywhere near your target, use Python.

#### Preferred approach: Python insertion with automatic renumbering
  ```python
  import re

  with open('/opt/data/wiki/entities/_index.md', 'r') as f:
      lines = f.readlines()

  # Find the insertion point by matching existing entries
  before_idx = None
  after_idx = None
  for i, line in enumerate(lines):
      if 'thorsten-ball' in line:     # <-- adjust to your anchor entry
          before_idx = i
      if 'tim-sh' in line:            # <-- adjust to next-after entry
          after_idx = i

  # Extract the embedded line number format from existing lines
  match = re.match(r'(\s*)(\d+)(\|)', lines[before_idx])
  indent = match.group(1)    # leading spaces
  base_num = int(match.group(2))  # embedded line number

  # Create the new line (increment line number by 1)
  new_line = f'{indent}{base_num + 1:3d}|- [[slug]] — One-line description.\n'
  lines.insert(after_idx, new_line)

  # Renumber all lines from before_idx onward
  current = base_num
  for i in range(before_idx, len(lines)):
      m = re.match(r'^(\s*)(\d+)(\|)', lines[i])
      if m:
          prefix, num, sep = m.group(1), int(m.group(2)), m.group(3)
          # Only renumber lines with the same indent pattern
          if m.group(1) == indent and num >= base_num:
              lines[i] = f'{prefix}{current:3d}{sep}{lines[i][m.end():]}'
              current += 1

  with open('/opt/data/wiki/entities/_index.md', 'w') as f:
      f.writelines(lines)
  ```

  **Key patterns in this approach:**
  - Uses `'slug' in line` to find anchor entries by content (reliable across sessions)
  - Extracts the embedded line number format from existing lines with regex
  - Creates the new line with correct `indent + line_num + `|- ` prefix + slug + description
  - Renumbers ALL subsequent lines in the same indent/format group to prevent gaps
  - No corruption, no escape-drift, no pipe prefix artifacts

  **If you need to patch a corrupted line instead:**
  Do NOT use `sed -i 'N,Ns/^|//'` — this strips the leading artifact but leaves content malformed. Use Python:
  ```python
  with open('PATH', 'r') as f:
      lines = f.readlines()
  lines[idx] = f'   {old_line_number:3d}|- [[slug]] — Description\n'
  with open('PATH', 'w') as f:
      f.writelines(lines)
  ```

## Hidden Entity-Concept Connection Discovery (★★★☆☆)

When creating an entity page for an organization, research group, or company from multi-source research, you may discover **hidden connections** to technologies that were previously documented from a different angle. The entity may have co-developed a technique that already exists as a concept page — but neither the entity page nor the concept page cross-references the other.

### Detection

This happens when:
- The entity page's research mentions a collaboration, co-authorship, or co-development that involved a technology already wiki-documented
- The existing concept page credits "collaboration between Organization A, Person B, and Company C" — but your new entity IS one of those collaborators
- Raw articles previously ingested from other sources (e.g., a tutorial by Person B) mention the collaboration but focused on the implementation rather than the organization

**Example from this session:** Creating [[entities/mobius-labs]] revealed they were a co-developer of FSDP+Q-LoRA (Answer.AI × Tim Dettmers × Hugging Face × Mobius Labs). The existing [[concepts/fsdp-qlora]] page credited "Answer.AI, Tim Dettmers, and Hugging Face" — Mobius Labs was missing from the cross-reference because none of the prior sources focused on them.

### Workflow

1. **Before writing the entity page**, while reading sources, note any named collaborations or co-development claims
2. **Run backward searches** for each collaboration mentioned:
   ```bash
   # Search concept pages for the collaboration name
   grep -r "Mobius\|HQQ\|FSDP.*QLoRA" ~/wiki/concepts/ --include="*.md" | head -20
   
   # Search existing concept pages for the entity name
   grep -r "mobius-labs\|Mobius Labs" ~/wiki/concepts/ --include="*.md" | head -20
   
   # Search raw articles for mentions
   grep -r "Mobius Labs" ~/wiki/raw/articles/ --include="*.md" | head -20
   ```
3. **If a connection is found**, add the entity to the concept page's `related:` frontmatter AND add a cross-reference section (e.g., "Key People & Organizations" or a note in "Related Concepts")
4. **Add the concept page to the entity page's `related:` frontmatter** with a wikilink
5. **Check raw articles** that were ingested from prior sessions — they may mention the entity but were never linked to it. For each raw article that references the entity:
   - Add the raw article path to the entity page's `sources:` frontmatter
   - Add `[[entities/new-entity]]` as a note in the raw article's tags or a comment
6. **Log the connection discovery** in the log.md entry — this turns a "created entity page" into a "created entity page + cross-linked 3 existing pages"

### Pitfalls
- Don't add the entity to concept pages solely from inference (e.g., "they must have worked on this because they do similar things") — only add when the sources explicitly state a collaboration
- The backward search on raw articles is especially important: existing raw articles may have mentioned the entity name in passing (e.g., "in collaboration with Mobius Labs") but the entity page didn't exist at the time of ingestion, so no wikilink was created
- When adding cross-references to existing concept pages, use `patch` (never `write_file`) to preserve existing content

### 7. Bulk Processing Record Update

If a bulk-processing record (e.g., `~/wiki/bulk-processing/bulk-*.md`) lists this entity as ❌ ファイル未作成, update it to ✅ 作成済み after creating the page.

### 8. Frontmatter Rules for Entity Pages

- **Do NOT include `status: skeleton`** — fresh entity pages based on multi-source research are complete, not skeletons. Only use `status: skeleton` for placeholder pages created during bulk processing or automatic blog/X account scraping.
- Include `type: entity` (not `type: person` or `type: concept`)
- Use `tags` from SCHEMA.md taxonomy: `devtools`, `ai-agent`, `orchestrator`, `open-source`, `product`, `coding-agents`, etc.
- `sources` array must include both raw article paths and external URLs (website, docs, etc.)

### 9. Commit & Push
```bash
cd ~/ai-topics
git add wiki/
git commit -m "wiki: <summary>"
git push
```

## Quality Standards
- Entity pages should match depth of `wiki/entities/antirez-com.md` or `wiki/entities/simon-willison.md`
- **Infrastructure deep-dive**: When a tool has a unique internal architecture (e.g., Prolly Trees for Dolt, Merkle DAG commit graph), document it inline rather than just linking to external docs. Dedicate subsections with architecture diagrams, comparison tables, and ASCII flowcharts. The entity page should be independently useful without requiring the reader to open external documentation.
- Concept pages should be self-contained but well cross-linked
- All internal `[[links]]` must resolve to existing pages
- YAML frontmatter must be complete and accurate
- Sources must be cited with URLs or file paths

## Pitfalls
- Don't create duplicate concept pages — always search `wiki/concepts/` first
- Don't over-abstract — keep concepts grounded in the source material
- Don't forget to update both `index.md` AND `log.md`

### Tag Taxonomy Violations From Other Files (CRITICAL)
The pre-commit hook validates ALL staged files, not just yours. If cron jobs (active-crawl, blog-wiki-ingest, etc.) created new concept pages with tags not yet in SCHEMA.md, your commit will be blocked even though your own changes are clean.

**Workflow when commit fails with tag violations:**
1. Read the error output — it lists the specific tags and files causing violations
2. Identify which SCHEMA.md category each tag belongs to (Models, Engineering, Meta, Domain Concepts, etc.)
3. Add missing tags to SCHEMA.md using `patch()` on the appropriate category line
4. Re-stage and re-commit: `git add wiki/ && git commit -m "..."`
5. If blocked again, repeat — there may be multiple rounds of missing tags

**This is NOT an `--no-verify` situation.** The tags are valid; they just need to be registered. Adding them to SCHEMA.md is the correct fix and takes ~30 seconds per batch.

### Entity Page Update: Already-Existing Raw Article
When the raw article already exists in `wiki/raw/articles/` and a concept page already references it, the entity page enrichment checklist is:
1. Add raw article path to `sources` frontmatter YAML list
2. Add to **Timeline** table (if person entity) — include date, article title, 1-sentence summary
3. Add to **Recent Articles** section with 1-2 sentence summary + `[[wikilink]]` to concept page
4. Add raw filename to **Sources** section (list format)
5. Add raw filename slug to **References** section (list format)
6. Update frontmatter `updated` date to today
7. If concept page `updated` date is stale, bump it too
8. Update `log.md` — prepend entry (file may be large; use `terminal` with `sed -i` to insert after line 3)
9. Verify `index.md` validation passes, then commit and push

### log.md Prepending for Large Files
`log.md` grows continuously and can exceed 100KB. The `patch()` tool requires reading the full file first, which fails for very large files. **Use `terminal` with `sed -i` to prepend entries:**
```bash
sed -i '4i\## [date] entry title\n\nContent here\n\n' log.md
```
Line 4 is typically right after the header (lines 1-3: title, description, blank line).
- If article references people not yet tracked, add them to appropriate config files
- **CRITICAL: Duplicate entity detection before creating new person pages** — See Step 4 above (Pre-Creation Verification Checklist). Run the full checklist before creating any new entity. Key commands:
  - `ls ~/wiki/entities/ | grep -i "partial-name"` — manual filename scan (most reliable)
  - `find ~/wiki/ -name "*partial-name*" 2>/dev/null` — broad filesystem search
  - `grep -ril "@handle\|Full Name" ~/wiki/entities/` — content/alias search
  - Known duplicate traps: Varun Trivedy = Vivek Trivedy (@Vtrivedy10), GitHub handles vs real names (e.g., `mitsuhiko` vs `armin-ronacher`), slug variants (e.g., `zach-mueller` vs `the-zach-mueller`). If an existing page is found under ANY slug, update that page — never create a new file.
- **Duplicate entity cleanup workflow** — See Step 4 above.
- When inserting multiple entries into `index.md`, always verify the section header first (Concepts vs Entities vs Comparisons) before patching. Each insertion needs its own `patch` call at the correct alphabetical position.
- **Subagent path trap**: When delegating entity/concept page creation to a subagent, the subagent may write files to `/opt/data/home/wiki/` instead of the canonical `~/wiki/` (which resolves to `/opt/data/wiki/` → `/opt/data/ai-topics/wiki/`). After delegation, **always verify** files landed in the git repo: `ls /opt/data/ai-topics/wiki/entities/NAME.md` and `ls /opt/data/ai-topics/wiki/concepts/NAME.md`. If missing, copy from the stale path: `cp /opt/data/home/wiki/entities/NAME.md /opt/data/ai-topics/wiki/entities/` and add to git.
- When inserting multiple entries into `index.md`, read the full file with `offset/limit` to find the correct insertion line for each entry, then apply `patch` for each one individually. Never assume alphabetical order without verifying.
- Total page count in index.md header must be updated after each batch (increment by number of new pages created).
- **Escape-drift on patch with quotes/Unicode**: When patching files with smart quotes, em-dashes, CJK characters, or other Unicode, `patch` may error with `Escape-drift detected`. This happens when the exact bytes in the file don't match what the tool serialized. The recommended verbatim re-read fix often still fails because Unicode gets re-serialized differently on each read. **Two fallback approaches** (try in this order):
  1. **Shorten old_string** — Trim `old_string` to only the unique line(s) that lack the problematic characters, avoiding smart quotes, `&`, em-dashes, and CJK. For example, if line 38 has smart quotes but line 37 is clean, write your patch to match just line 37 + the start of line 38. This is the fastest fix and preserves the `patch` workflow.
  2. **Use `sed`** — If shortening fails, use `sed` for line insertion: `sed -n 'N,Np' PATH` to check line numbers, then `sed -i 'Ni|- [[entities/slug]] -- Description' PATH`. Always verify with `sed -n 'M,Np'` afterward.
- **Two failure modes for Unicode in patches** — When the file contains Unicode (smart quotes `\u201c`/`\u201d`/`\u2019`/`\u2014`):
  1. **Escape-drift error** (handled above) — patch tool rejects the input entirely
  2. **Silent literal write** — passing `\u2019` as a literal backslash-escaped sequence in `new_string` writes the text `\u2019` into the file instead of the intended Unicode character. **Fix:** Always use plain ASCII equivalents instead: `'` (not `\u2019`/right single quote), `"` (not `\u201c`/`\u201d`), `--` (not `\u2014`/em-dash). Re-read the surrounding lines after every patch that touches a file with smart quotes to verify no escaped literals leaked in.
- **Patch prefix mismatch on index files**: All three index files (`wiki/index.md`, `entities/_index.md`, `concepts/_index.md`) may use variable prefix formats — some lines use `- ` (dash-space), others use `NNN|- ` (embedded line number + pipe-dash), and the format can change mid-file. **Never assume a uniform prefix.** Always verify with `sed -n 'N,Np' PATH` before patching to see the actual bytes. If ANY line in the target section has embedded line numbers, use the Python approach instead of `patch` (see EMBEDDED LINE-NUMBER CORRUPTION above).
- **Patch matching duplicate slugs across sections**: When the same slug appears in multiple locations within a file (e.g., `vibe-coding` exists under BOTH `harness-engineering/agentic-workflows/vibe-coding` AND as a top-level `vibe-coding` entry), `patch` matches the **first occurrence** — which may be in the wrong section. This can silently delete unrelated lines (e.g., `context-engineering` was dropped when the patch targeted the top-level listing but matched the harness-engineering subdirectory). **Fix**: Before patching, always `read_file(offset=X, limit=5)` at the intended target to get the EXACT surrounding context. Include 1-2 lines of surrounding context in `old_string` to disambiguate which occurrence you're targeting. If the slug is not unique, use more surrounding context or switch to a Python insertion.
- **Python batch entity insertion ordering bug**: When inserting multiple entity entries into the Entities section in one Python script, computing alphabetical insertion points against the **original file state** causes all insertions to land at the same index (since later entries don't see earlier insertions). **Fix**: Sort insertions by descending index before inserting (each `list.insert()` then doesn't shift unprocessed insertion points). Alternatively, insert one entry, re-read the file, then insert the next. The descending-sort approach is simpler and works for any number of insertions.
- **New concepts and concepts/_index.md**: The `concepts/_index.md` file does NOT list all concept pages (many like mismanaged-geniuses-hypothesis exist in filesystem but are absent from `_index.md`). Do NOT assume every new concept needs an `_index.md` entry. Only add entries there when updating a pre-existing bucketed section or when the pattern is clearly comprehensive. The main `wiki/index.md` IS the authoritative catalog -- always update that one.

## Backfilling a Previously-Referenced-but-Nonexistent Concept Page (★★★☆☆)

When a concept page is already referenced in the wiki (via wikilinks in entity pages, `related:` frontmatter, or an existing index.md entry) but the actual `.md` file doesn't exist:

*(Full section unchanged — see above)*

## Multi-Dimensional Concept Enrichment (★★★☆☆)

When an existing concept page covers dimension A (e.g., pretraining) and a new article covers dimension B (e.g., RLHF/alignment) on the same umbrella topic, enrich by adding parallel H2 sections rather than merging or creating a new page. See `references/multi-dimensional-concept-enrichment.md` for the full workflow, detection signals, and comparison with case studies/multi-paper expansion.

## X Article Auth Wall & Metadata-Only Fallback (x.com/i/article/...)
- index.md already has an entry for the concept slug
- Sub-pages may exist under `concepts/<slug>/` directory but no root page

**False-negative pitfall with search_files (target="files"):** The search_files tool can return 0 results for exact-name patterns even when the file exists -- glob/regex matching is unreliable. Always cross-verify suspected-non-existent files with a terminal command: `ls ~/wiki/concepts/SLUG.md 2>/dev/null || echo NOT FOUND`. If the file exists despite search_files returning 0, your task shifts from backfill to enrichment -- skip the backfill workflow and instead patch the existing file to add the content that the references expected.

### Workflow
1. **Search for all references first** — grep entity pages, concept pages, and index.md for the broken wikilink. This tells you what content the backfilled page *must* connect to (related entities, parent/child concepts).
2. **Check for sub-pages** — if `concepts/slug/sub-page.md` exists, the root page should reference them and structure itself as an umbrella.
3. **Do NOT add a new index.md entry** — the entry already exists. Just update its description with `patch`.
4. **Cross-reference from the backfill to existing sub-pages** — the root page links TO the sub-pages, not the other way around.
5. **Update all entity pages** that listed the concept in their `related:` frontmatter — the wikilink now resolves, so verify any linked descriptions still make sense.
6. **Add the backfill to log.md** — note it as a "backfilled" operation so future readers understand the page didn't exist before.

### Example
`concepts/harness-engineering` was referenced in `entities/hamel-husain.md` (related: section), had sub-pages under `concepts/harness-engineering/agentic-engineering/`, and had an index.md entry — but no `concepts/harness-engineering.md` existed. The article "The Revenge of the Data Scientist" served as the foundational source to backfill it.
## X Article Auth Wall & Metadata-Only Fallback (x.com/i/article/...)

X article URLs often return HTTP 500 (auth wall) OR succeed but contain only metadata (title, author, description) with no body content.

When scraping fails or returns incomplete content:

0. **Try GetXAPI first** — If `$GETXAPI_KEY` is set in the environment, fetch the article body via:
   ```bash
   curl -s -H "Authorization: Bearer <GETXAPI_KEY>" \
     "https://api.getxapi.com/twitter/tweet/article?id=<TWEET_ID>"
   ```
   This returns the full article as structured JSON (headings, paragraphs, lists, inline styles). Use the **parent tweet's ID** (from `x.com/user/status/NNN`), NOT the article entity ID. See [[social-media/x-article-getxapi-fallback]] for response structure and markdown conversion. If successful, save as full-content article with `getxapi: true` frontmatter and skip the mirror-search steps below.
1. Extract the article title and author handle from the bookmark metadata (from xurl's `article.title` field in the tweet response, NOT from trying to `xurl read <article_id>` which returns "Could not find tweet with id" — X Article IDs are not tweet IDs)
2. Check file size: if < 5KB, likely metadata-only — proceed to step 3
3. Run `web_search` with: `"<article title>" author "<handle>" site:substack.com` or `"<article title>" "<author name>"`
4. Also try: `site:twitter.com "<article title>"` (may find threads summarizing the article)
5. If found on Substack/arXiv/other platform, scrape that mirror instead
6. Note the fallback source in the article metadata: `source_fallback: true`
7. Common targets: Substack mirrors, personal blogs, arXiv preprints, GitHub gists
8. For well-known authors (e.g., Tobi Lütke, Andrej Karpathy, Simon Willison), search author name + title directly

### Reconstruction Technique (Auth-Walled Content)

When NO mirror exists but the article title points to a well-known author + known technical domain, you can reconstruct meaningful wiki content through multi-source synthesis:

1. **Harvest the title** — The article title is the key signal. In xurl's tweet response, it's in `data.article.title`.
2. **Search the author's broader body of work** — Their recent blog posts, tweets, papers, and podcast appearances often cover the same thesis from different angles.
3. **Find third-party commentary** — Other researchers may have analyzed or critiqued the same ideas.
4. **Search for related technical papers and benchmarks** — The article likely responds to or builds on published research (e.g., Qwen3 OPD results, GRPO papers).
5. **Synthesize a coherent section** from the supplementary sources, attributing the article as the trigger and the third-party findings as the substance.
6. **In the raw article frontmatter**, include both the original X article URL AND the supplementary sources used for reconstruction.
7. **In the concept page**, credit the original author's framing explicitly (e.g., "In his May 2026 X article 'X', Author provides a practitioner's framing...") even if the technical data comes from third-party sources.

## Existing Concept Page Updates — Production Case Studies (★★★★☆)
When a real-world article describes how a company/product used a technology:
1. **Search existing concept pages first** — find the page that already covers the technology
2. **Add a case study section** under the relevant heading (e.g., "Production Users" or a new "Case Studies" subsection)
3. **Include concrete metrics** (NMSE, speedup %, cost reduction) and **model names** (gpt-oss-120b, gemma-3-12b)
4. **Key code snippets** if the article provides them (feedback loops, config patterns)
5. **Pattern extraction**: name the technique (e.g., "GEPA reflection loop", "Instruction Library Layer")
6. **Update the concept page tags** if the case study introduces new relevant dimensions (e.g., adding `llm-as-judge` to dspy.md)
7. **Add the raw article to the concept page's `sources:` array** in frontmatter
8. **Update `llm-as-judge.md` or related pages** if the case study demonstrates evaluation patterns
9. Use `patch` to insert, not `write_file` (preserves existing content)
10. **Always verify with `read_file` after patching**

Example structure for a case study insertion:
```markdown
### Company X Use Case (Month Year)

Company X used TECHNOLOGY to solve PROBLEM.

**Three-stage approach:**

| Stage | Model | Technique | Result |
|-------|-------|-----------|--------|
| A | model-v1 | method-A | metric-A |
| B | model-v2 | method-B | metric-B |

**Key patterns:**
- Pattern 1: description
- Pattern 2: description

[Source: Company X Blog](URL)
[Source: Company X Blog](URL)

## Single-Experiment Multi-Page Distribution (★★☆☆☆)

When one article/blog post describes a single experiment with quantitative results that validates an existing concept, enrich multiple existing pages simultaneously at different granularity levels rather than creating a new page.

### Detection
- Article describes one controlled experiment with metrics (benchmarks, ablation, methodology)
- The experiment validates a named hypothesis or concept that already has a wiki page
- The same results are relevant to entity pages (author), sibling concept pages (technical mechanism), and sub-entity pages (project-specific benchmarks)

### Workflow: Descending Granularity

Distribute the experiment data across pages from most-general to most-specific:

| Level | Target | What to add | Example from this session |
|-------|--------|-------------|---------------------------|
| 1. Parent concept | The validated hypothesis/framework page | Full experiment section: methodology, results table, ablation, connection to thesis | MGH page: LongCoT Experiment with 3 failure modes, ablation proof |
| 2. Sibling concept | The technical mechanism page | Experiment section alongside parallel experiments on same benchmark, call out differences in approach | RLM page: Zhang LongCoT experiment positioned alongside Weitekamp results |
| 3. Author entity | The person page | Blog post entry + one-line proof bullet under relevant section | Alex Zhang: new row in Blog Posts table + proof bullet under MGH |
| 4. Sub-entity | The project sub-page | One-line benchmark result in the benchmark list | Omar Khattab RLM sub-page: LongCoT-mini 65.6% in benchmark list |

**Key rules:**
- Each page gets a DIFFERENT amount of detail: parent concept = fullest (methodology + results + interpretation), sibling concept = mid (results table + key insights), entity = minimal (blog entry + one bullet), sub-entity = one-liner (benchmark number)
- No new pages are created -- all enrichment is patch on existing pages
- The same raw article serves as source for all patches
- Always cross-reference between levels in the sibling concept section (e.g., See full analysis in [[concepts/parent-concept]])

## Multi-Part Series Incremental Expansion (★★★★☆)

When the user progressively adds individual parts/articles from a known **multi-part series** (blog series, talk series, video series, paper series) where a parent series overview page acts as a hub connecting all parts.

### Detection

- User says "I added [part N] from this series, also add [part M]"
- The new URLs follow a predictable pattern (`series-name/p2-xxx`, `series-name/p3-yyy`)
- The parent series page already exists as a concept page listing all parts
- Each part has its own distinct presenter/author with a specific concept contribution

### URL Discovery for Paywalled/Subscription Sites

When a blog is on a subscription platform (Ghost, Substack, etc.) that blocks homepage scraping with a paywall overlay:

1. **RSS first** — check `/feed.xml`, `/rss.xml`, `/atom.xml`
2. **If no RSS** — check the **sitemap**: `/sitemap.xml`, `/sitemap-posts.xml`, `/sitemaps.xml`. Ghost sites auto-generate `sitemap-posts.xml` with ALL post URLs and lastmod dates.
3. **Filter by series** — grep/parse the sitemap for the series URL pattern (e.g., `automation-series-`) to extract all parts at once
4. **Compare with sitemap lastmod** — the sitemap's `<lastmod>` field reveals whether parts are published in chronological order, useful for establishing series sequence
5. **Avoid homepage scraping** — subscription sites return only signup UI from the homepage, making `web_extract` useless for navigation

### Workflow

**First part of a new series:**
1. Create the **parent series overview concept page** — covers all parts with a table, key insights, and sources for the overview article
2. Create **individual sub-concept page** for the first part — captures the unique concept contribution of that part
3. Update entity pages for key people (host, presenters)
4. Set up the graph structure query with `part-of` and `includes` edges

**Each subsequent part:**
1. Save raw article
2. Create **new sub-concept page** for this part — independent concept page with its own aliases, sources, and graph edges
3. **Update the parent series concept page** — add the new part to the Parts table, Key Insights table, and Part Details section
4. Update entity pages for the presenter if needed (timeline entries, sources)
5. Cross-link the new sub-concept page to the series page and sibling parts
6. If a person entity is mentioned but hasn't been created yet, check for existing pages under different slugs first (see Batch Creation > Person Extraction)
7. Update index.md, log.md, and commit

### Key Differences from Multi-Paper Expansion (single concept)

| Aspect | Multi-Paper (single concept) | Series Expansion (hub + sub-pages) |
|--------|------------------------------|-------------------------------------|
| Page structure | Multiple sources → ONE concept page | Each part → OWN concept page + parent hub |
| Source relationship | Perspectives merged into levels | Parts are independent siblings under a parent |
| Cross-referencing | Internal level references | `part-of` / `includes` graph edges |
| Entity updates | Optional | Likely needed (host + presenters) |
| Index updates | May skip if description unchanged | Always needed (new sub-concept pages) |

### Pitfalls

- **Check for existing entity pages before creating** — the presenter may already have a page under a different slug (e.g., `benjamin-clavie` vs `ben-clavie`). Search filenames and content before creating duplicate entity pages.
- **Fix stale ben-clavie/benjamin-clavie type refs** — when editing the parent series page, check that all wikilinks point to the correct existing slug. The initial creation may have used a slug that doesn't match an existing entity page.
- **Don't rewrite the entire parent page** — only patch new sections in (Part Details, tables, sources). The parent page grows incrementally with each addition.
- **Re-read parent page before each addition** — structure may have changed since the previous part was added.
- **Audit existing wikilinks on the parent page** — when re-reading the parent page, check that all existing wikilinks (especially for earlier parts and related concepts) point to correct existing slugs. The initial creation may contain stale links (e.g., `context-graph` instead of `context-rot`). Fix them as part of the same patch session — don't defer to a separate cleanup run.
- **Index page count** — each new sub-concept page increases the count by 1. Track cumulative additions across the session.
- **Document unique intellectual style when presenters use distinctive terminology** — Some presenters (e.g., Bryan Bischof with "The Map is Not the Territory" / "Curving Space" / buzzword deconstruction, Kelly Hong with "Context Rot") bring a distinctive philosophical vocabulary. When detected, create a dedicated subsection in the concept page that:
  1. Labels the named metaphor/framework explicitly (e.g., `**"Curving Space"** — intention...`)
  2. Traces its intellectual lineage if applicable (e.g., Korzybski for map/territory, physics metaphors for curving space)
  3. Explains the **rhetorical intent** — what problem does this framing solve? (e.g., reframing index engineering from passive to active, stripping marketing language down to pipeline operations)
  4. Quotes the presenter's exact phrasing with context
[Source: Company X Blog](URL)

## Single-Experiment Multi-Page Distribution (★★☆☆☆)

When one article/blog post describes a single experiment with quantitative results that validates an existing concept, enrich multiple existing pages simultaneously at different granularity levels rather than creating a new page.

### Detection
- Article describes one controlled experiment with metrics (benchmarks, ablation, methodology)
- The experiment validates a named hypothesis or concept that already has a wiki page
- The same results are relevant to entity pages (author), sibling concept pages (technical mechanism), and sub-entity pages (project-specific benchmarks)

### Workflow: Descending Granularity

Distribute the experiment data across pages from most-general to most-specific:

| Level | Target | What to add | Example from this session |
|-------|--------|-------------|---------------------------|
| 1. Parent concept | The validated hypothesis/framework page | Full experiment section: methodology, results table, ablation, connection to thesis | MGH page: LongCoT Experiment with 3 failure modes, ablation proof |
| 2. Sibling concept | The technical mechanism page | Experiment section alongside parallel experiments on same benchmark, call out differences in approach | RLM page: Zhang LongCoT experiment positioned alongside Weitekamp results |
| 3. Author entity | The person page | Blog post entry + one-line proof bullet under relevant section | Alex Zhang: new row in Blog Posts table + proof bullet under MGH |
| 4. Sub-entity | The project sub-page | One-line benchmark result in the benchmark list | Omar Khattab RLM sub-page: LongCoT-mini 65.6% in benchmark list |

**Key rules:**
- Each page gets a DIFFERENT amount of detail: parent concept = fullest (methodology + results + interpretation), sibling concept = mid (results table + key insights), entity = minimal (blog entry + one bullet), sub-entity = one-liner (benchmark number)
- No new pages are created -- all enrichment is patch on existing pages
- The same raw article serves as source for all patches
- Always cross-reference between levels in the sibling concept section (e.g., See full analysis in [[concepts/parent-concept]])

## Multi-Part Series Incremental Expansion (★★★★☆)

When multiple research papers, technical reports, or blog posts share a common dataset/benchmark/context and are added to the SAME concept page over multiple separate user requests.

### Detection

- A user shares a paper or report about a topic you've already expanded
- The new source references the **same benchmark** (e.g., BrowseComp-Plus, Oolong, NQ)
- The new source presents a **complementary or contrasting approach** to existing content on the same concept page

### Organization Pattern: Multi-Level Framework

When 3+ sources cover the same topic from different angles, organize them into numbered levels or perspectives:

```
## Level 1: [Perspective A — e.g., Traditional IR Approach]
## Level 2: [Perspective B — e.g., Harness Engineering]
## Level 3: [Perspective C — e.g., Coding Agents as Interface]
```

Each level should be **self-contained** (readable standalone) but explicitly cross-reference the other levels:
- "This directly challenges the assumption from Level 1 that better retrievers are always beneficial."
- "See Level 3 for a contrasting approach using file-system tools."

### Incremental Update Checklist

For each new source added to an existing concept page:

1. **Read the full current concept page** — understand existing structure and find correct insertion point
2. **Create appropriate section** — H3 subsection under existing level, or new H2 level if it's a genuinely new paradigm
3. **Add comparison tables** where the new source contrasts with existing content (shared benchmarks make direct comparisons valuable)
4. **Update frontmatter**: bump `updated` date, add new `aliases`, new `sources` (both raw article/paper path and external URL)
5. **Update the `tags` array** — add new relevant tags (e.g., `rl-training` for RL-trained retrieval)
6. **Patch the Sources section** at the bottom — prepend new entry
7. **Update `index.md`** only if the concept page description changes significantly (not for every incremental expansion)
8. **Update `log.md`** — prepend new entry with source name, key findings, raw article path, and URL
9. **Commit each incrementally** — `git commit -m "wiki: add <source-name> to <concept-page>"`
10. When a source is arXiv-only with no peer-review venue, note `(arXiv-only, ingested per user request)` in log.md

### Pitfalls

- Don't rewrite the entire page — only patch the new section in. The user may add more sources later.
- When adding a contrasting perspective, preserve existing content verbatim. Add new sections, don't modify old ones unless fixing errors.
- If the new source comes from a company blog/tech report (not arXiv/peer-reviewed), save to `raw/articles/`. Only save to `raw/papers/` for arXiv or arXiv-like preprints.
- Always re-read the page before the second incremental addition — the structure may have changed since your first addition.
- Check for emerging structural patterns: when 2 sources exist, a third may complete a framework (e.g., IR vs File-System vs RL-Trained becomes a clean 3-level model). Design the structure with future expansion in mind.
- **Cross-link successive additions**: When adding source N+1, explicitly reference previously-added sources within the same page (e.g., "This mirrors the Level 1 finding (SID-1...)"). This turns a pile of sources into a coherent, cross-referenced framework.
- **Production implementation validates theory**: When adding a production/real-world source to a multi-level concept page, check if it validates ALL levels simultaneously. Call out each level's correspondence explicitly with a "Connection to the X-Level Framework" subsection. This is distinct from a normal case study (which validates one thing) — you need to enumerate each level separately.
|- **arXiv-only user override**: When the user explicitly requests an arXiv-only paper with no peer-review venue, note `(arXiv-only, ingested per user request)` in log.md AND add `status: blocked` + `blocked_reason: no_peer_review` in the raw paper's frontmatter. Run normal concept enrichment; the paper isn't cited as a primary source but its findings enrich the concept page.
|- **Add validated patterns table when 3+ sources converge**: After integrating 3+ sources, append a `#### Validated Patterns` table at the end of the newest section. Each row maps a finding back to the level/source that established it (e.g., | BM25 > embeddings for agents | Level 1: Query Mismatch). Serves as quick-reference summary of what each source contributed and how they interrelate.
|- **Frontmatter source dedup after each patch**: When patching the `sources:` frontmatter array multiple times, duplicate entries can accumulate silently. After each frontmatter patch, `read_file` to verify no duplicates exist. Clean up with `patch(replace_all=True)` if found.

## Blog Feed Discovery (RSS absent → sitemap.xml fallback)
When adding a blog to `blogwatcher-cli`, **verify RSS/Atom existence first** before adding:

1. Try common feed paths: `/feed`, `/feed.xml`, `/rss.xml`, `/atom.xml`, `/blog/feed`, `/blog?format=rss`
2. Use `curl -s -o /dev/null -w "%{http_code}" <url>` or Python `urllib.request.urlopen()` in `execute_code`
3. Check HTML `<head>` for `<link type="application/rss+xml">` or `<link type="application/atom+xml">` tags

**If RSS/Atom found** → Add with: `blogwatcher-cli add "Blog Name" https://example.com` (auto-discovers feed).

**If ALL feed paths return 404/empty AND no feed link in HTML** → Blog has **no RSS feed**. Do NOT rely on blogwatcher-cli scanning (it reports "No feed or scraper configured"). Instead:

1. **Try sitemap.xml**: Check `/sitemap.xml` and common variations (`/sitemaps.xml`, `/sitemap_index.xml`). Many static-site blogs (Astro, Hugo, Jekyll, Next.js) auto-generate sitemaps even without RSS feeds.
   ```python
   # Python snippet for probing
   import urllib.request, urllib.error, xml.etree.ElementTree as ET
   url = "https://example.com/sitemap.xml"
   try:
       resp = urllib.request.urlopen(url, timeout=10)
       if resp.status == 200:
           tree = ET.parse(resp)
           ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
           locs = tree.findall(".//sm:loc", ns)
           blog_urls = [l.text for l in locs if "/blog/" in (l.text or "")]
           print(f"Found {len(blog_urls)} blog posts in sitemap")
   except: print("No sitemap")
   ```
2. **Still add to blogwatcher-cli** with the base URL: `blogwatcher-cli add "Blog Name" https://example.com`. This registers it for tracking even though periodic RSS scans won't find articles. The entity page can note "no RSS feed."
3. **Scrape all recent articles** from the sitemap URLs using `web_extract()`. Save each as `wiki/raw/articles/YYYY-MM-DD_source-slug.md`.
4. **Create entity pages**: For org blogs, create both the **organization entity** (`entities/org-name.md`) and **flagship project entity** (`entities/project-name.md`) simultaneously — the blog likely covers both with cross-links between them.
5. **Create concept pages** for each technical innovation mentioned in the blog posts.
6. **Track via X/Twitter** if the org is active there — blog posts are often announced on X.
7. Record "RSS unavailable" in the entity page metadata.

#### Pitfall: Framer-hosted blogs (dynamic routing)
Framer-hosted blogs (detectable by "Powered by Framer" footer or framer.app references) use **client-side dynamic routing**: the blog index page displays article titles/URLs, but individual article URLs return 404 when fetched server-side by `web_extract()`. This is NOT the same as a paywall or access control — Framer simply doesn't SSR individual blog posts.

**Primary technique: Browser-based URL discovery** (use this FIRST, most reliable):
1. Navigate to the blog index in the browser: `browser_navigate(url="https://blog.example.com/blog")`
2. Click each blog article link in the browser to navigate to the article
3. Extract the actual URL: `browser_console(expression="window.location.href")` — this reveals the real Framer slug, which is often different from what the display text suggests (e.g., display text: "Rust zero-cost abstractions vs. SIMD" → real slug: `/blog/zero-cost`)
4. Once you have the real URL, use `web_extract()` with the discovered URL — it typically returns full content without needing the browser
5. For speed with many articles, extract all URLs at once via JS:
   ```javascript
   (function() {
     const links = document.querySelectorAll('a');
     const blogLinks = [];
     links.forEach(a => {
       if (a.href && a.href.includes('/blog/') && !a.href.endsWith('/blog')) {
         blogLinks.push({text: a.textContent.trim().substring(0,80), href: a.href});
       }
     });
     return JSON.stringify([...new Map(blogLinks.map(l => [l.href, l])).values()], null, 2);
   })()
   ```
   This deduplicates by href and returns all unique blog article URLs at once.

**Fallback approaches** (when browser is unavailable or too slow):
- Check `/sitemap.xml` — Framer often auto-generates sitemaps with all post URLs
- If individual posts on a Framer site return 404, **do not keep retrying** — move to sitemap.xml or browser URL discovery
- Search for the article title via `web_search` to find cross-posts or summaries on other platforms (Substack, Medium, dev.to)

**Example from session (turbopuffer blog):**
- Guessed slug `/blog/rust-zero-cost-abstractions-vs-simd` → 404
- Browser click → actual URL `/blog/zero-cost` → `web_extract()` succeeded
- All 11 blog post URLs extracted via JS querySelectorAll, revealing various non-obvious slugs: `zero-cost` (Rust), `fts-v2-postings` (inverted indexes), `bm25-latency-musings` (BM25 scaling), `ann-v3` (ANN v3), `fts-v2-maxscore` (MAXSCORE), `continuous-recall` (recall measurement), and talk URLs under `/blog/podcast-*`, `/blog/video-*`

## Podcast Transcript Ingestion (★★☆☆☆)
See `references/podcast-transcript-ingestion.md` for the full workflow.

## Comparison Article Decomposition (★★★★☆)

When a single source provides a **comparison/overview of N techniques** (benchmark comparison, architecture taxonomy, codec comparison, framework survey), decompose into:

1. **1 concept page** — the comparison framework itself (comparison table, axes, selection guide)
2. **N entity pages** — each technique/tool/framework being compared
3. **Updated parent concept page(s)** — add a section with links to the comparison and all new entities

### Detection

The source text has a clear "compare and contrast" structure:
- Side-by-side comparison table
- "How to choose" / practical selection guide
- Each technique described in its own section
- Identifies distinct architectures, design philosophies, or tradeoffs

### Workflow

1. **Analyze axis structure** — identify the comparison dimensions (e.g., codec quality vs LLM readiness, semantic separation, token rate, streaming)
2. **Create concept page**: frontmatter + compact comparison table + per-technique breakdown + selection guide + caveats section
3. **Create entity pages**: one per technique — each gets frontmatter with cross-links to sibling entities and the comparison concept, a summary, specs table, positioning statement
4. **Update parent concept page(s)**: add a short summary section (e.g., "Neural Audio Tokenizers") at the top of the nearest existing concept page, with links to both the comparison concept and all entity pages. Use a bullet list with one-line descriptions of each entity.
5. **Save raw article**
6. **index.md**: add concept page entry in Concepts section + each entity entry in Entities section (alphabetically sorted)
7. **log.md**: single entry describing the full decomposition — list all created pages and the parent concept update

### Example

SoundStream / EnCodec / DAC / SpeechTokenizer / Mimi comparison → `concepts/audio-tokenizer-comparison` + 5 entity pages + updated `concepts/speech-audio-asr-tts-voice` with "Neural Audio Tokenizers" section

### Key Difference from Product Launch Batch

| Aspect | Product Launch | Comparison Article |
|--------|---------------|-------------------|
| Concept page type | One concept (the product's paradigm) | The comparison framework itself |
| Entity count | 1–2 (tool + creator) | N (each compared item) |
| Parent concept update | Maybe (add to competitive positioning) | Always (add a summary section linking to comparison) |
| index.md insertion | 2–3 entries | 1 + N entries |

## Batch Creation from Single Article (Architecture Reviews, Product Launches)
When a single article introduces multiple new concepts and entities (e.g., a product launch covers architecture + company + tool):
1. Extract **all** concepts first, then **all** entities — don't interleave creation
2. Verify each concept/entity doesn't already exist via `search_files` before creating
3. **Disambiguation check**: Search for name collisions (e.g., "Rivet" → rivet.dev vs Ironclad Rivet). Add clarifying note in entity page if needed.
4. **Person extraction**: Create entity pages for article authors/key figures mentioned (e.g., CTO, founder) if they don't already exist.
   - **Before creating any new person entity, check for existing pages under different slugs:**
     - `ls ~/wiki/entities/ | grep -i "partial-name"` — search filenames for first/last name variants
     - `grep -li "full name\|@handle" ~/wiki/entities/*.md` — search frontmatter aliases/descriptions
     - `search_files(target="content", pattern="Full Name\|@handle", path="~/wiki/entities")` — catch loose mentions
     - If a pre-existing page is found (even under a different slug like `benjamin-clavie` vs `ben-clavie`), **do NOT create a new file**. Update the existing page with the new article content, sources, timeline entries, and cross-references instead.
5. Update `index.md` header counts AFTER all insertions (total = concepts + entities created)
6. For `index.md` entries: insert each at its correct alphabetical position, then re-verify with `search_files`
7. A single `log.md` entry summarizing the batch is sufficient
8. Cross-link all new pages bidirectionally (concept ↔ entity ↔ person)

## Trajectory-Repo Deep Dive: Extracting Embedded Prompts/Tips (★★☆☆☆)

When a blog post references but does not reproduce key content (prompts, tips, configuration), and states that content is in an accompanying GitHub repository of trajectories:

### Detection
- Blog post says: "The prompt/tips/config is found in the trajectories repository"
- The referenced repository contains `results.jsonl` files under domain-specific subdirectories
- Each JSONL line is a trajectory with an embedded `prompt` field containing the full system/user messages

### Extraction Pipeline

1. **Locate the GitHub repo** — often linked at the bottom of the blog post (e.g., `github.com/author/project-results`)

2. **Check repo structure** via GitHub API:
   ```bash
   curl -sL "https://api.github.com/repos/author/repo/contents/trajectories" | python3 -c "import sys,json; data=json.load(sys.stdin); [print(d['name'], d['type']) for d in data]"
   ```

3. **Find trajectory files** — look for `results.jsonl` in the domain subdirectories (math, cs, logic, etc.)

4. **Extract the raw prompt** using grep from the raw GitHub content. The embedded prompt often uses a custom tag (e.g., `<env_tips>`) for the experiment-specific instructions:
   ```bash
   curl -sL "https://raw.githubusercontent.com/author/repo/main/trajectories/domain/results.jsonl" | grep -oP '<env_tips>.*?(?=</env_tips>|$)' | head -c 5000
   ```
   - If no specific tag, extract the full user-message content from the first JSONL line
   - Use `grep -oP` for tag extraction; for full extraction, pipe through Python JSON parsing

5. **Classify the extracted content** into the blog post's claimed structure:
   - **Graph/benchmark structure description** — what the model needs to know about the problem format
   - **Worked workflow / step-by-step method** — explicit instructions for how to approach multi-part problems
   - **Anti-pattern / "don't brute-force" rules** — timeouts, error budgets, fallbacks

6. **Backfill the raw article** with the full extracted tips content — the blog post's summary is always thinner than the actual prompt. This makes the raw article the authoritative source.

### Why This Works
- AI research trajectory repos store the **exact prompt that was sent to the model**, including system prompt, user prompt, and any embedded `<env_tips>` sections
- The blog post is a human-readable narrative; the repo is the machine-readable ground truth
- The gap between them often contains the actual engineering insight (e.g., the two-pass workflow, the verification methodology, the anti-brute-force heuristics)

### Pitfalls
- GitHub API may time out on large repos; fall back to `raw.githubusercontent.com` URLs
- Some repos require authentication — check if the repo is public first
- Trajectory JSONL files can be large (hundreds of KB); grep with byte limits (`head -c 5000`) is safer than reading the full file
- The prompt may be split across system and user messages within the same trajectory — check both roles
- Not all repos store the prompt inline; some use a separate config file (check for `config.json`, `prompt.txt`, `system_prompt.md` in the repo root)

### Example

Blog post: "A Mini Exercise on the Mismanaged Geniuses Hypothesis (RLMs on LongCoT)" — says tips exist in the trajectories repo.

Extraction:
```bash
curl -sL "https://raw.githubusercontent.com/alexzhang13/longcot-mini-rlm-results/main/trajectories/math/results.jsonl" | grep -oP '<env_tips>.*?(?=</env_tips>|$)'
```

Result: ~4KB of detailed tips comprising (1) graph dependency directive catalog, (2) Two-pass workflow (Map & Solve → Independent Re-derivation), (3) General principles (timeout budgets, symbolic computation, verification culture). The blog post summarized as "descriptions of graph structure, fake problem example, tips for not brute-forcing" — the actual tips were an order of magnitude richer.

## Cross-Referencing After Updates
After adding a case study to a concept page:
1. **Search for related concept pages** that might benefit from a source link back to the case study
   - e.g., After adding Dropbox Dash case study to `dspy.md`, also add it as a source to `llm-as-judge.md`
2. **Update the concept page's `sources:` frontmatter array** with the raw article path
3. **Check `index.md` entries** — update the one-line summary for the modified concept page to mention the new case study
4. **Always update `log.md`** with date, key findings, and raw article path
When running skeleton enrichment as a cron job:
- Set explicit model: `{"provider": "deepseek", "model": "deepseek-v4-flash"}` — don't rely on `custom` provider default
- Manual test runs queue asynchronously — results deliver to the `deliver` target, not the current conversation
- Use `enabled_toolsets: ["web", "file", "terminal"]` to reduce token overhead
- 53+ skeleton pages require batched processing — expect 数十分〜数時間の実行時間
- Monitor with `cronjob(action="list")` and check `last_status`/`last_delivery_error`

## Multi-Source Same-Author Sequential Enrichment (★★★★☆)

When enriching wiki pages from **multiple sources by the same author** (e.g., a YouTube talk + a blog article + a paper), apply this progressive enrichment pattern to build a coherent framework instead of siloed additions:

### When to Use
- Processing a YouTube talk by an author, then later processing their blog article on the same topic
- Processing multiple blog posts by the same person that build on each other
- A talk is the "live recorded version" of a blog post thesis

### Pattern

**First source (e.g., Talk):**
1. Save raw article (video metadata extraction via `youtube-content` skill or `~/ai-topics/scripts/youtube_meta.py` — do NOT write a custom YouTube scraper)
2. Enrich entity **speaking page** — add to Conference Talks list with wikilink to raw article
3. Enrich main **concept page** — add dedicated subsection with the talk's framework
4. Update log.md

**Second source (e.g., Blog article by same author):**
1. Save raw article
2. Enrich the **same concept page** — but this time:
   - Add a cross-reference note in an EXISTING subsection (not a new one) linking the article as a precursor/successor to the talk
   - Add the article to the concept page's `sources:` frontmatter and Sources section
3. Enrich the entity's **core-ideas or philosophy page** — expand existing sections with new detail from this article (not add new sections)
4. Enrich the **main entity page** — add to Recent Blog Posts or similar summary section
5. Check for and **clean up duplicate entries** that may have been created by the previous patch
6. Update log.md — describe the enrichment and cross-referencing; can reference the first source's log entry

**Third source (and beyond):**
When enriching from a 3rd+ source by the same author (e.g., another YouTube talk, interview, or paper), the pattern shifts from "add" to **"integrate":**

1. Save raw article
2. Enrich the **same concept page** — integrate into the EXISTING framework:
   - If the source provides implementation details for a concept already discussed in earlier sources, add it as a subsection under the relevant level (e.g., "Practitioner Implementation" under Level 2 Harness)
   - If the source introduces a new dimension not covered, it may deserve its own subsection, but should explicitly cross-reference the framework created by sources 1+2
   - Do NOT create a duplicate of the existing framework structure
3. Enrich the entity's **core-ideas page** — unlike the second source, this time you may create NEW sections (not just expand existing ones):
   - New frameworks introduced by the source (e.g., a "passive→proactive→active spectrum")
   - New implementation patterns (e.g., code-level tool-calling loops)
   - New future directions (e.g., long-running agents, memory compaction)
   - These new sections should cross-reference the earlier sections they complement
4. Enrich the entity's **main page** if needed (Recent Blog Posts, speaking list)
5. Re-read files before patching — the structure may have shifted from passes 1+2
6. Update log.md — describe how this source integrates into and extends the framework

### Key Differences from Single-Source Enrichment

| Aspect | Single Source | Sequential (same author) |
|--------|-------------|-------------------------|
| Concept page insertion | New subsection | Cross-reference note in existing subsection |
| Entity enrichment | One page | Speaking + Core-Ideas + Main (potentially all 3) |
| Cross-referencing | Optional | Required — earlier source should link to later source |
| Duplicate detection | Not needed | Check after each patch — duplicates happen when patches append before existing content |
| Log entry | One entry per source | Each source gets its own entry; second entry can reference the first |

### Pitfalls
- When patching the same section twice (e.g., "Recent Blog Posts" or "Conference Talks"), verify you didn't create duplicates on the second pass
- Re-read files before the second patch — the structure may have shifted since the first pass
- The second source's enrichment is typically **deeper** on entity pages (more detail into core-ideas) and **lighter** on concept pages (cross-reference, not new full section)
- Update the concept page's frontmatter `updated` date on each enrichment

## Git Push Troubleshooting
See `references/git-commit-pitfalls.md` for common issues: tag taxonomy validation failures, `&` in commit messages, and SSH credential problems in sandbox environments.

### Common Failure: Tag Taxonomy Violation
The git commit hook checks all `tags:` arrays in wiki frontmatter against `SCHEMA.md`. If you invent a tag not in the taxonomy (e.g., `personal-agents` instead of `personal-ai`), the commit is BLOCKED. **Always check `SCHEMA.md` before adding new tags.** If hit mid-session: read `SCHEMA.md` for the correct tag, `patch` the entity file, then re-commit. The hook validates ALL staged files.

---

## Section: Project Investigation

See `references/project-investigation.md` for the full workflow.

## Section: Grokipedia Entity Enrichment (grokipedia-entity-enrichment)

Use Grokipedia (grokipedia.com) to enrich wiki entity pages with biographical data, career timelines, interview quotes, and quantitative metrics.

### How to Extract
Grokipedia is JS-heavy. Use Jina Reader API:
```bash
curl -s -L --max-time 30 "https://r.jina.ai/http://grokipedia.com/page/{Person_Name}"
```
Replace spaces with underscores (e.g., `Boris_Cherny`).

### What to Extract
1. Early Life & Education
2. Career Timeline (company transitions with dates)
3. Key Projects with dates
4. Quantitative Metrics (adoption numbers, benchmarks)
5. Interview Quotes with source attribution
6. Industry Impact
7. Philosophy/Worldview
8. References with numbered citations

### Enrichment Process
1. Extract via Jina Reader
2. Cross-reference with existing entity page
3. Add new sections for missing data
4. Add specific quotes with attribution
5. Add metrics and numbers
6. Update Sources section with Grokipedia URL
7. Update index.md and log.md
8. Commit

### Known Strengths: citation-numbered references, interview summaries, competitive context, quantitative data, timeline precision
### Known Weaknesses: AI-generated content (verify critical claims), may lag behind, JS rendering (MUST use Jina Reader)

---

## Section: AI Agent Memory Middleware Analysis (ai-agent-memory-middleware-analysis)

Analyze and integrate memory/storage technologies into wiki using 4-tier framework.

### 4-Tier Memory Architecture
| Tier | Concept | Example |
|------|---------|---------|
| L0 | Virtual Filesystem | ChromaFS (vector DB as FUSE interface) |
| L1 | In-Context Memory | Prompt caching, KV cache |
| L2 | Local File Memory | CLAUDE.md, SKILL.md patterns |
| L3 | Cloud Storage Memory | S3 Files, Tigris, LLMFS, Cognee |

### Workflow
1. Identify new technology announcement
2. Scrape article to raw/articles/
3. Survey existing related wiki pages
4. Analyze against 4-tier framework
5. Create/update `wiki/concepts/ai-agent-memory-middleware.md`
6. Update index.md and log.md
7. Commit

---

## Section: Concept Hierarchy Reference (harness-agentic-concept-hierarchy)

### Hierarchy
```
Harness Engineering (umbrella philosophy)
"Agent = Model + Harness"
├── Agentic Engineering (human-side usage patterns — Willison)
├── AI Agent Engineering (system-side build patterns — Anthropic/OpenAI)
└── Context Engineering (cross-cutting — Karpathy/DSPy)
```

### Structural Rules
1. Harness is the umbrella — "Agent = Model + Harness" contains all others
2. Agentic ≠ AI Agent — different granularity and audience
3. Context Engineering is cross-cutting — applies to both
4. Keep separation of concerns — Don't merge Agentic + AI Agent

### Key People
- Ryan Lopopolo (@rlopopolo) — Harness Engineering, Symphony
- Simon Willison — Agentic Engineering patterns
- Andrej Karpathy — Context Engineering (Software 3.0)
- DSPy team — Declarative context optimization

### When creating entity pages, always:
1. Link to Harness as parent concept
2. Specify whether person's work falls under Agentic or AI Agent
3. Note Context Engineering contributions separately
1. Verify the GitHub token is available in the current session environment
2. SSH may not be available in sandbox (no `ssh` binary)
3. Try passing the token via git credential helper inline
4. If still failing → token may be expired/revoked; save commits locally and notify user
5. Never lose committed work — the commits are still in local branch (ahead of origin)

### CRITICAL: `&` character in commit messages
The terminal tool interprets `&` as shell backgrounding. If your commit message contains `&` (e.g., `set_to_none=True`), use **single quotes**: `git commit -m 'wiki: safe message here'`. Double quotes with `&` inside fail silently (the tool blocks `&&` chaining AND hangs on `&` inside double-quoted strings). Split `git add`, `git commit`, `git push` into separate terminal calls when `&&` chaining fails.