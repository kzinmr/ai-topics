# Multi-Article Ingestion with Comparison

When the user provides 2+ articles on the same topic and asks to "ingest and compare," the deliverable is:
1. Individual raw article clippings in `wiki/raw/articles/`
2. A **concept page** that synthesizes the shared concept across all articles
3. A **comparison page** in `wiki/comparisons/` that highlights differences
4. Cross-links between the concept page and comparison page
5. Updates to any existing entity/concept pages that are related

## Workflow

### Step 1: Fetch all articles in parallel

Use `curl -sL` for each URL. If any return Cloudflare/JS challenge pages (~5-10KB of JS with no article content), immediately fall back to `delegate_task` with `browser` toolset for that URL while continuing to process others.

**Cloudflare detection heuristic**: If `wc -c` returns <15KB AND the HTML contains `challenge-platform` or `_cf_chl_opt`, it's a Cloudflare challenge — curl won't work.

### Step 2: Check existing wiki BEFORE writing

Search `index.md`, `concepts/`, `entities/`, and `comparisons/` for existing pages on the same topic. Use:
- `search_files` with content patterns (concept name, company names, key terms)
- `search_files` targeting files for slug matches

If an existing page partially covers the topic, update it with `patch` rather than creating a duplicate.

### Step 3: Create raw article clippings

Save to `wiki/raw/articles/YYYY-MM-DD_source_slug-title.md` with:
- Source URL
- Author (if available)
- Published date
- Structured summary (sections, key points, quotes)

### Step 4: Create the concept page

The concept page should:
- Define the shared concept abstractly (not vendor-specific)
- Describe the common architecture/pattern both articles converge on
- Include a "Two Implementations" (or N) section covering each article's approach
- Link to the comparison page for detailed differences
- Link to related existing wiki pages
- Use tags from SCHEMA.md taxonomy

### Step 5: Create the comparison page

Use `type: comparison`. Structure:
- Summary table (dimension × approach)
- Shared architecture/pattern section
- Approach differences (philosophy, implementation, scale)
- What A found that B didn't
- Synthesis section (complementary, not competing)
- Open questions

### Step 6: Update existing pages

Add cross-references to:
- Entity pages for mentioned companies/people
- Related concept pages (add a one-line link in Related section)
- The concept page itself (link to comparison)

### Step 7: Update index.md and log.md

Add new pages to appropriate sections in index.md with one-line descriptions.
Append to log.md with file list and brief descriptions.

## Example: OpenAI + Sierra Deployment Simulation (2026-06-18)

**Input**: Two URLs — OpenAI research framework blog, Sierra product blog
**Cloudflare**: OpenAI page blocked → delegate_task with browser fetched it in ~43s
**Output**:
- `raw/articles/2026-06-11_openai_deployment-simulation.md`
- `raw/articles/2025-08-19_sierra_simulations-the-secret-behind-every-great-agent.md`
- `concepts/deployment-simulation.md` — three-actor pattern (user simulator + agent + judge)
- `comparisons/openai-vs-sierra-agent-simulation.md` — research framework vs product platform
- Updated `entities/sierra.md` (Agent Simulation Platform section)
- Updated `concepts/scenario-based-simulation.md` (cross-link)
- index.md: +2 entries (1 concept, 1 comparison)
- log.md: +1 entry

## Pitfalls

- **Don't create comparison pages for unrelated articles.** If the articles don't share a clear common concept, create individual concept pages without a comparison.
- **Don't duplicate existing pages.** Always search first. If `concepts/tau-bench.md` already exists and one article is about τ-bench, update that page rather than creating a new one.
- **Comparison pages need a summary table.** Without it, the reader can't quickly see the differences.
- **Raw clippings go in raw/, not in concepts/.** The raw article is Layer 1 (immutable); the concept page is Layer 2 (agent-managed).
