--- 
name: wiki-concept-from-research
description: Create a new wiki concept page from scratch via web research (not from raw articles), OR rebuild/expand an existing concept page with fresh research. Includes explicit differentiation from related pages.
trigger: "When asked to create a new concept page from research, when the user provides a URL (Notion page, blog post, technical article, Google Slides, YouTube talk, X/Twitter thread) and says \"wikiに取り込んで\" (ingest this into wiki), when the user provides a survey paper or project page that proposes a novel taxonomy/classification framework (e.g., ETCLOVG, layered architecture models), when the user provides one URL and research reveals a related/prequel article by the same author that also needs ingestion (multi-article author arc), when a trending topic has no wiki page yet, when a similar but distinct concept should be separated from an existing page, when expanding an existing page with a new external source that reveals structural parallels with another wiki concept (cross-concept synthesis, horizontal), when multiple official/docs sources naturally form a vertical hierarchy (API mechanism → architectural pattern → implementation), when the user provides a prioritization table (trending-topics output) directing a full rebuild or expansion of an existing concept page, when the user provides a GitHub PR URL alongside a blog post/docs page and asks to understand the development history (「このPRの内容も開発経緯として理解して」), when the user provides a URL to an already-ingested topic and says \"論じて\" or \"絡めて\" (discuss in relation to other articles) — triggering cross-article causal-chain synthesis (see references/cross-author-causal-chain-synthesis.md), OR when the user challenges an existing concept framing with a historical counter-reference (\"Xというけど、それはY時代にはすでに始まっている\") — triggering historical baseline reframing (see references/historical-baseline-reframing.md), OR when the user asks for 「構造的対比」(structural comparison) between related concepts/paradigms — triggering multi-axis structural analysis (see references/multi-axis-structural-analysis.md), OR when the user proposes a novel framing/thesis during conversation and asks to wiki-fy it (「wikiにまとめて」「wiki追加してください」) without providing an external source — the user is the origin of the framing. Decompose their claim, validate via parallel research across independent technology domains, and synthesize into a concept page (see references/conversation-driven-synthesis.md)."
---

# Wiki Concept Page Creation from Research

## Purpose
Create a new wiki concept page when: (1) a trending topic has no wiki page yet (e.g. from a `trending-topics`  report); (2) the user provides an external resource and says "wikiに取り込んで" (ingest this into the wiki); or (3) a similar but distinct concept needs separation.

Do NOT use this skill when: the user provides a raw article already saved in `wiki/raw/articles/` — for article-driven enrichment, use `wiki-entity-enrichment-from-article` instead.

## Before You Start
When the user says "wikiに取り込んで" and provides a URL, ALWAYS load this skill first. The web_extract result from an external URL is NOT a "raw article" — treat it as source research, save it to `wiki/raw/articles/` alongside the final concept page.

## Research Phase

### Step 1: Scan for existing coverage
Before creating or expanding a page, search the wiki to understand what already exists. This prevents duplication and identifies cross-references.

For trending topics (from a prioritization table):
- Check `wiki/index.md` — Concepts section for the topic or similar pages
- Check `wiki/concepts/` and `wiki/entities/` for related pages
- Check `wiki/raw/articles/` for any prior raw-article coverage

For external-resource ingestion:
- Check the same locations. Identify which wiki pages will link to the new or expanded page.

When the user asks to map a deployment architecture from one cloud provider to another (e.g., "Fly.io + Modal → AWS"), see `references/cloud-infrastructure-mapping-research.md` for the full multi-source research pattern: find existing implementations → identify hardest component → extract service docs → structure as tiered comparison → cross-reference design principles.

**Stub detection — check if the raw article file has actual content.** When a `raw/articles/` file exists for the source URL, open it and verify it contains real article body text, not a placeholder. The presence of `*[Full article content to be scraped and inserted here]*` or a near-empty body (under ~30 lines) means the file is a **stub** — the article was scraped but never populated. You must populate the stub with full content before creating concept pages from it. Use the extraction methods in Step 2 (web_extract → curl → browser_navigate) to get the full article, then overwrite the stub with `write_file`. The stub's frontmatter (date, author, source_url) is usually correct — preserve it and add `updated:`.

**Dangling wikilink detection (critical):** Before creating a new concept page, search for existing `[[wikilinks]]` to that concept slug across ALL wiki page types. Run:
```bash
cd ~/ai-topics && grep -rn 'concepts/<proposed-slug>' wiki/ --include='*.md' -l
```
If wikilinks exist (e.g., `[[concepts/langgraph]]` already referenced in `human-in-the-loop.md`, `entities/langchain.md`), creating the new concept page **immediately fulfills all dangling references** — no entity-page edits needed. Use the exact slug the existing wikilinks expect. This is one of the highest-value outcomes of creating a new concept page: it resolves broken navigation with zero follow-up work.

### Step 2: Gather external sources and raw articles
For a green-field concept page (no prior wiki page):
1. Search the web with the concept name + relevant keywords for reliable external sources. Prioritize: official docs > research papers > technical blog posts > news articles
2. **Always** use **web_extract** to fetch full content from any site that supports it. If web_extract returns nothing or an error, fall back to **web_read** for sites that require JavaScript rendering
   - **Summary trap (broad)**: `web_extract` on many company/marketing blogs (LangChain, Anthropic, OpenAI, company blogs using CMS-generated summaries) often returns a pre-existing machine-generated **summary** rather than the raw essay body. Similarly for Substack and LessWrong. Do NOT trust web_extract output as the full article — always verify by checking whether the extracted text reads like a third-party summary ("In this essay, the author explores...") vs the author's actual voice, or is suspiciously short relative to the page's metadata (e.g., 20-min read returns only 30 lines).
   - **Truncation fallback (curl)**: When `web_extract` times out with `LLM summarization timed out` (content exceeds 5,000 chars), try `curl -sL '<URL>'` in terminal to fetch the raw HTML. The HTML can then be manually converted to markdown: read the `<article>` or main content `<div>`, strip tags, and reconstruct headings/paragraphs. This is simpler than `browser_navigate` and works for most static blogs (Astro, Hugo, Jekyll, etc.) that serve full content in the HTML source. Use this before attempting the heavier browser fallback. See `references/curl-html-to-markdown-extraction.md` for a reusable Python execute_code pattern.
   - **LinkedIn is pure JS-rendered — curl won't help.** LinkedIn Pulse articles serve NO article body in static HTML. `web_extract` gets the first ~5,000 chars of rendered content (often sufficient for short articles). `curl` only returns JSON-LD metadata (title, author, datePublished, headline blurb) and navigation chrome — zero article body text. The JSON-LD `headline` field gives you the article's meta description, which can supplement the truncated web_extract output. If the combined content is still too thin, accept the partial extraction and proceed — for well-known technical topics (like Adam optimizer), your own knowledge can fill gaps in the concept page. The raw article file should note that content is partial: add `extraction: partial` to the frontmatter.
   - **Google Slides — use `/htmlpresent` endpoint.** `web_extract` on `docs.google.com/presentation/d/ID/edit` returns only navigation chrome (no slide content). Instead, replace `/edit` with `/htmlpresent`: `https://docs.google.com/presentation/d/ID/htmlpresent`. This server-rendered view returns structured markdown (titles, bullets, code blocks, tables) cleanly via `web_extract`. No browser needed. See `references/google-slides-extraction.md` for details. If the presentation has images/diagrams you need, fall back to `browser_navigate` + `browser_vision`.
   - **Full-text extraction (when web_extract gives a summary)**: Use `browser_navigate(url)` → `browser_snapshot(full=true)` to get the page DOM. If the snapshot truncates, use `browser_console` with `document.body.innerText.substring(start, end)` in chunks (e.g., 0..8000, 8000..16000, 16000..24000) to extract the full plain text. Combine all chunks into a single raw article file. This works across all blog platforms — LangChain, Substack, LessWrong, and most JS-rendered content.
3. For each external source, **save a raw article** to `wiki/raw/articles/` with complete frontmatter (source, title, author, publication, date, tags)
4. Group and deduplicate source material before writing the concept page

### Step 2b: Multi-article author ingestion (tripartite structure)
When an author has **multiple related articles** forming an arc (e.g., one experiential/prequel and one theoretical), don't just create a concept page — create all three layers:

```
raw/articles/  ──  entities/<author>.md  ──  concepts/<idea>.md
(sources)           (person)                 (ideas)
```

Workflow:
1. **Raw articles first**: Save each article with its actual publication date
2. **Entity page second**: Create `entities/<author>.md` connecting the articles to the person. Include a comparison table showing how the articles relate (e.g., experiential vs theoretical, early vs mature)
3. **Concept page(s) third**: Create `concepts/<idea>.md` from the synthesized material. Cross-link back to the entity page and raw articles
4. **Link both ways**: Each page should reference the others in its `related:` frontmatter

### Step 3: Differentiate from related concepts
Identify and document what makes the new concept distinct from similar existing pages. This differentiation is critical — without it, the wiki accumulates redundant pages. If the concept cannot be clearly differentiated, consider merging into an existing page instead.

## Writing Phase

### Step 3.25: Proactive tag taxonomy check (BEFORE writing the page)
**Do this before you write a single line of frontmatter.** The pre-commit hook validates ALL tags against `wiki/SCHEMA.md`. Don't wait for it to fail — check proactively:

1. Read `wiki/SCHEMA.md` and identify the canonical tags you plan to use. **Check EVERY tag individually** — don't assume a tag exists just because a related one does (e.g., `aws` exists ✓ but `bedrock` does not ✗ — both are AWS-specific). Use `search_files` or `execute_code` with `open()` to grep for each tag candidate in SCHEMA.md.
2. For any tag NOT in the taxonomy, **add it to SCHEMA.md first** (in the correct category: Models, People/Orgs, Products, Techniques, Engineering, AI Agents, Infrastructure, Meta, or Domain Concepts), then use it in your page
3. Common additions: company names go under People/Orgs; infrastructure concepts (like `llm-proxy`) go under Engineering; product names (like `bedrock`, `fly-io`) go under Products; domain-specific concepts (like `biotech`, `sports-analytics`) go under Domain Concepts
4. Verify spelling: tags are lowercase kebab-case, prefer plural forms (`coding-agents` not `coding-agent`)

This prevents the round-trip of: write page → commit blocked → fix tags → recommit. Adding tags to the taxonomy is an intentional act of curation, not a violation to be caught.

### Step 3.5: Route to correct directory (COMPARISON CHECK — load `wiki-comparison-page-routing`)
**Before you create the page file**, determine the correct wiki directory using the comparison routing skill:

> Load `wiki-comparison-page-routing` skill and apply the decision tree:
> - 3+ items compared → `wiki/comparisons/` (NOT `wiki/concepts/`)
> - 2 items (head-to-head) → `wiki/comparisons/`
> - Single concept/technique → `wiki/concepts/`
> - Person/org/tool → `wiki/entities/`
>
> **Litmus test**: Remove all comparison tables from the page. Does it still work as a concept explanation? YES → concepts/. NO (the page IS the comparison) → comparisons/.
>
> Use `type: comparison` in frontmatter for comparison pages. This prevents the cleanup debt pattern where comparison pages accumulate in concepts/ and need `moved_from` entries later.

### Step 4: Create the concept page
Write the page to `wiki/concepts/<name>.md` (or `wiki/comparisons/<name>.md` if routed there by Step 3.5) with:
- A lowercase, hyphenated filename matching the concept name
- Complete YAML frontmatter (title, type: concept, aliases, created/updated dates, tags, related pages, sources linking to saved raw articles)
- A discriminative summary describing what this concept is (and optionally what it is not)
- A discriminative summary describing what this concept is (and optionally what it is not)
- **CRITICAL: Tags MUST be in SCHEMA.md taxonomy** — pre-commit hook blocks commits for any tag not listed in `wiki/SCHEMA.md` lines 32-40. Common pitfall: using similar but non-canonical names (e.g., `codeact` vs `code-act`). Check the taxonomy first. If a genuinely new tag is needed, add it to SCHEMA.md in the appropriate category before using it.
- Use `[[wikilink]]` syntax for cross-references (not markdown links)

### Step 5: Update existing pages
After creating the new page, enrich related pages — a single article often warrants updates to multiple targets:

1. **Author entity page** — Add a section or work entry for the article. If the article introduces a new framework/thesis, create a structured subsection.
2. **Parent/company entity page** — If the article comes from or about a company (e.g., LangChain), add it as a source reference.
3. **Related comparison pages** — If the article introduces a new comparison dimension, update the relevant comparison page.
4. **Existing concept pages** — Add related-page wikilinks and/or new subsections to concept pages that are related to the new page.
5. **Update `wiki/index.md`** — add the new page under the correct section (Concepts or Entities), alphabetically

### Step 6: Commit and push
```bash
cd ~/ai-topics
git add wiki/
git commit -m "wiki: <short description of what was added>"
git push
```

- **Tag taxonomy compliance**: The pre-commit hook validates ALL tags against `wiki/SCHEMA.md`. If your commit is blocked with `TAG TAXONOMY VIOLATIONS`, you used tags not in the canonical taxonomy. Fix by: (1) opening `wiki/SCHEMA.md` to find the right canonical tags (`search_files` for keywords), (2) replacing non-canonical tags in your page frontmatter with ones from SCHEMA.md, or adding legitimate new tags to SCHEMA.md. Do NOT use `--no-verify` to bypass — the check exists to prevent tag sprawl.

## Pitfalls
- **Never fabricate company ownership, transfer, or acquisition claims.** When writing entity bios, timelines, or comparison tables, do NOT invent claims like "Company X acquired Product Y" or "Product moved from Company A to Company B." These fabrications propagate across multiple wiki pages and are hard to find. If you don't know who owns a product, don't guess — look it up or omit the claim.
- **Don't write a generic overview.** The wiki already has broad coverage. Every new page must add novel content, not rehash what's covered elsewhere.
- **Differentiation is mandatory.** If the concept is essentially the same as an existing page, don't create a new page. Expand the existing one.
- **web_extract summary trap (broad).** Many company/marketing blogs return pre-existing machine-generated summaries. Always verify web_extract output: if it reads like a third-party summary or is suspiciously short for the claimed read time, use `browser_navigate` + `browser_snapshot(full=true)`.
- **Pre-existing tag violations block your commit — and can take multiple rounds.** The pre-commit hook validates ALL staged files, not just yours. If files you didn't touch have non-canonical tags, `git commit` will fail listing them. Fix by adding the missing tags to `wiki/SCHEMA.md`. **Violations may surface incrementally**: after fixing one batch, the next `git commit` may report a NEW violation not in the first scan. Plan for 2-3 rounds. Fix each batch, `git add wiki/` again, and retry until clean.
- **`patch` replace_all=true can duplicate frontmatter.** When using `replace_all=true` on frontmatter lines, the tool may match and re-insert `type:` and `tags:` lines twice. Avoid `replace_all=true` on frontmatter. If duplication occurs, fix with a follow-up patch that removes the duplicate lines.
- **`write_file` overwrite risk — verify file existence immediately before writing.** The wiki is actively updated by 27 parallel cron jobs which can create or modify files between your search and your `write_file`. Always verify RIGHT BEFORE writing: `grep '[[<dir>/<slug>]]' wiki/index.md` for the exact slug, then `ls /opt/data/ai-topics/wiki/<dir>/<file>.md`. If either exists, use `patch` to enrich instead.
- **Don't `git add wiki/` until all edits are done.** Staging changes early means parallel cron jobs can commit your staged changes alongside theirs with an unrelated commit message. Stage only at commit time: `git add` → immediate `git commit` → immediate `git push`.
- **Wiki language enforcement — ALL non-raw content MUST be English.** The pre-commit hook blocks CJK characters in wiki pages (raw/ is exempt). When the user speaks Japanese, respond in Japanese but write ALL wiki pages in English.
- **Patch encoding trap with curly quotes/special characters.** When `patch` finds no match despite text appearing visually identical, the culprit is often Unicode smart quotes or em dashes. Use a shorter, ASCII-only anchor string as `old_string`.

## Supporting References

This skill ships with reference files under `references/`. Load them with `skill_view(name, file_path)` to get specialized guidance:

- `references/arxiv-paper-ingestion.md` — Full arXiv paper ingestion pipeline
- `references/cloud-infrastructure-mapping-research.md` — Multi-source research pattern for mapping deployment architectures between cloud providers (e.g., Fly.io → AWS). Find existing implementations → identify hardest component → extract service docs → tiered comparison → cross-reference design principles. Covers NAT Gateway cost pitfall.
- `references/conversation-driven-synthesis.md` — User proposes a novel framing/thesis during conversation
- `references/cross-author-causal-chain-synthesis.md` — Cross-author causal-chain synthesis
- `references/curl-html-to-markdown-extraction.md` — Python execute_code pattern for curl+regex HTML-to-markdown
- `references/cross-wiki-architecture-synthesis.md` — Cross-wiki architecture synthesis
- `references/github-pr-as-history-source.md` — GitHub PR as development history source
- `references/google-slides-extraction.md` — Google Slides extraction via `/htmlpresent`
- `references/historical-baseline-reframing.md` — Historical baseline reframing
- `references/multi-axis-structural-analysis.md` — Multi-axis structural analysis
- `references/stub-enrichment-separation-crossref.md` — Stub detection, concept separation, hierarchy enrichment
- `references/wiki-knowledge-synthesis-overview.md` — Comprehensive domain overview page