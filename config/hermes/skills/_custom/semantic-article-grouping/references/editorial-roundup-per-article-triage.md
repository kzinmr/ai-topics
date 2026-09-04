# Editorial Roundup: Per-Article Triage Pattern

When a newsletter is an **editorial roundup** (editor curates 10-20 article links with commentary), ALL checkpoint candidates are typically Substack/beehiiv platform noise (like/comment/share buttons, OAuth redirects, author profile links). The ACTUAL triage content lives in the newsletter post body.

## Detection Pattern (pre-resolution)

Identify editorial roundups from the **inbox pre-triage summary** or subject line:
- Subject mentions "AI Weekly", "Bites", "Roundup", "Today in AI", "Daily"
- `inbox_summary.action` = "fetch_full_article" or "skip" (roundups are often misclassified as skip when they contain editorial value)
- The newsletter's publication name is a known editorial curator (e.g., Ben's Bites, AINews, Interconnects, The Signal)

**⚠️ Exclusion: editorial essay variant** — If the subject line contains thesis language ("The good, the bad and the ugly of X", "Why X matters") rather than list language ("X things to know", "Top stories"), this is NOT a roundup. See `references/editorial-essay-primary-content.md` for the essay triage pattern (1 decision for the essay itself, not N for external links).

## Workflow

### Step 1: Resolve the newsletter post URL
- Substack: extract `publication_id` + `post_id` from the app-link URL → `open.substack.com/pub/{pub}/p/{slug}`
- Use curl + JSON-LD + `<article>` paragraph extraction to get the full body

### Step 2: Extract article topics from the body
From the extracted paragraphs:
- **Section headings** with emoji (e.g., "🖱️ DeepMind reimagines the mouse pointer") → identify the topic
- **First 1-2 sentences of each section** → assess depth and wiki relevance
- **External links** embedded in the body → these are the real article URLs
- Editor's commentary paragraphs → assess editorial value (does the editor add analysis or just link?)

### Step 3: Create decisions per article topic (NOT per candidate)

Each extracted article topic becomes its own triage decision. Since they don't map to checkpoint `item_id`s:

| Field | Value |
|-------|-------|
| `item_id` | `null` (not from checkpoint) |
| `source` | `"newsletter"` |
| `source_name` | The newsletter publication name |
| `title` | The article topic / linked article title |
| `url` | The resolved external URL (or `null` if topic-only, e.g., a Codex feature announced by Ben Tossell without a canonical URL) |
| `raw_path` | The newsletter raw path (if the article link was extracted from the newsletter body) or `null` if no standalone raw article exists |
| `recommended_action` | Per-article assessment |
| `candidate_wiki_path` | The existing wiki page that should be enriched / created |
| `body_excerpt` | **From the newsletter body paragraph** describing this article, NOT from a raw article file. Since the article hasn't been separately scraped yet, the newsletter editor's description is the best available source. |

### Step 4: Mixed star ratings within one newsletter

A single editorial roundup can produce **takes + references + skips across its body-extracted articles**:

| Rating | Count range (typical) | Description |
|--------|----------------------|-------------|
| ★★★★★ (Take) | 0-3 per roundup | New major essays (Armin Ronacher), new features not documented anywhere in wiki |
| ★★★★☆ (Take) | 0-3 per roundup | New features requiring existing page enrichment (Codex Record & Replay, Claude Code Artifacts) |
| ★★★☆☆ (Reference) | 2-5 per roundup | Minor updates to existing pages (benchmark numbers, product GA announcements) |
| ★★☆☆☆ (Skip) | 5-15 per roundup | Already-covered topics, non-AI content, too-brief mentions |

Use `recommended_action` for the group:
- `take`: ★★★★★ or ★★★★☆ — requires page creation or enrichment
- `reference`: ★★★☆☆ — minor note, can be added during enrichment
- `skip`: ★★☆☆☆ or ★☆☆☆☆ — not actionable

### Step 5: Deduplication across extracted articles

Multiple articles from the same roundup may cover the same entity/concept as the other newsletters in the batch. Before making a final decision for each extracted article:
1. **Check other newsletters' extracted topics** for overlap (e.g., Sakana Fugu appeared in both Ben's Bites and AI Weekly)
2. If the same topic appears in multiple sources, assess which source provides the best coverage
3. Use a single `reference` decision for shared topics (don't create duplicate takes)

## Concrete Example (June 24, 2026)

**Newsletter**: Ben's Bites "Record a skill" (publication_id=4379299)
**Checkpoint candidates**: 20 links, ALL Substack platform noise (like/comment/share/OAuth/subscribe)
**Body-extracted topics**: 16 article topics (Codex Record & Replay, Claude Code Artifacts, Armin Ronacher essay, Cursor /automate, Sakana Fugu Ultra benchmarks, Gemini Interactions API GA, Perplexity Computer Brain, etc.)

**Extraction technique**: curl + JSON-LD `<script type="application/ld+json">` for metadata (headline, author, `isAccessibleForFree`), then `<article>` tag + `<p>` paragraph extraction for body content. The JSON-LD `body_html` was empty (expected — Substack rarely populates it), but the raw HTML `<article>` extraction returned 30 substantive paragraphs with article descriptions and external links.

**Result**: 3 takes, 5 references, 8 skips — all from body extraction, none from checkpoint candidates.

**Notable**: The newsletter body's "Record a skill" title turned out to be about Codex's new Record & Replay feature, NOT about general skill recording. The per-article triage correctly identified this as a Codex-specific feature, not a general concept.
