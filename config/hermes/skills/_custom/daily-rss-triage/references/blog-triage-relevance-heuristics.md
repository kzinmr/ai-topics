# Blog Triage Relevance Heuristics

Decision framework for determining which blog articles from the RSS ingest are worth wiki page updates vs. raw-save-only. Developed from repeated blog-triage sessions.

## Triage Decision Tree

For each article from the blog-ingest checkpoint:

### 1. Source Signal Weight (who wrote it?)

| Source Tier | Examples | Bias |
|-------------|----------|------|
| **Tier 1 — AI thought leaders** | Simon Willison, geohot, Andrej Karpathy, swyx | Almost always worth triage; even "link blog" posts reveal market dynamics |
| **Tier 2 — Tech commentators with AI coverage** | Daring Fireball (Gruber), John Gruber, lcamtuf | Worth scanning; AI content is intermittent but often high-signal |
| **Tier 3 — Domain blogs** | John Cook (math), Jim Nielsen (design), Terence Eden (travel) | Skip unless directly AI-relevant; save as raw only |

### 2. Content Relevance Filter

**Wiki-worthy (create/update pages):**
- New substantive information about an existing wiki entity or concept
- Market dynamics / competitive positioning between tracked products (e.g., Fable vs GPT-5.6)
- New product capabilities, usage metrics, or pricing changes
- First-person takes from AI practitioners on LLM usage patterns
- Cross-entity competitive intelligence (e.g., OpenAI removing usage limits pressures Anthropic)

**Raw-save only (no wiki action):**
- Tool version releases (shot-scraper 1.11, sqlite-utils 4.1.1) — unless major feature
- Organizational theory / management concepts (DRI) — unless directly about AI agent governance
- Domain-specific content from non-AI blogs (travel, cooking, hardware)
- Paywalled content with no extractable substance

### 3. Wiki Page Action Type

| Article Content | Action |
|----------------|--------|
| New info about existing entity | `patch` entity page — add to Recent Themes, update `updated`, add source |
| New market dynamics between tracked products | `patch` both entity pages + relevant concept page |
| New concept not yet in wiki | Consider creating concept page if >2 independent sources |
| Tool release with AI implications | `patch` tool entity page if exists; otherwise raw-save |
| Quote-post revealing author's AI philosophy | `patch` author entity page |

### 4. Common Patterns from Simon Willison's Blog

Willison's link blog posts are the single highest-yield source for wiki updates. His post structure:
- **Tool release posts** (shot-scraper, sqlite-utils, datasette) — usually raw-save only
- **"Bump" / competitive dynamics posts** — wiki-worthy, updates multiple pages
- **Quote posts with AI commentary** — patch the quoted person's entity page
- **Directly AI posts** (LLM coding, agent engineering) — always wiki-worthy

### 5. Batch Triage Workflow

```
1. Read checkpoint JSON from blog-ingest
2. For each article:
   a. Check source tier (Tier 1 → always read; Tier 2/3 → scan title)
   b. Read raw article if Tier 1 or title suggests AI relevance
   c. Check wiki/index.md for existing entity/concept pages
   d. Decide: skip | raw-save-only | wiki-update
3. For wiki-update articles:
   a. Read existing page(s) before patching
   b. Patch with new information (never overwrite rich pages)
   c. Update `updated` date, add source link
4. Commit all changes in single git commit
5. Update log.md with triage summary
```

## Pitfalls

- **Over-triaging non-AI content**: A math blog post about Bayesian statistics is NOT AI-relevant just because ML uses Bayes. The threshold is "does this change our understanding of an AI entity, concept, or market?"
- **Under-triaging link blog posts**: Simon Willison's one-liner about Fable access extensions revealed competitive dynamics worth 3 wiki page updates. Don't skip link posts from Tier 1 sources.
- **Creating pages for single-source concepts**: Don't create a new concept page from a single blog post. Wait for corroborating sources unless it's a major product launch.
- **Missing cross-entity updates**: When an article mentions multiple tracked entities (e.g., "OpenAI removing limits pressures Anthropic"), update ALL relevant pages, not just the primary subject.
- **Bundle minor LLM-CLI dot-releases into the author's page-edit, don't triage them separately**: A dot-release like `llm 0.32.1` (fixes an `openai<3`/httpx transitive-dep break) or `llm-openrouter 0.7` (reasoning traces) is individually "raw-save only" per the rules above — but when the author (Simon Willison) has a rich entity page AND the same scan also has a higher-signal Willison post, it is cheaper and more coherent to fold the release note into the same page-edit as a short "release notes" bullet in the body rather than make a separate commit. Surfaced 2026-08-22: the `llm 0.32.1` + `llm-openrouter 0.7` notes were bundled into `simon-willison.md` alongside the "Stop Making TUIs" link post. Reserve a standalone commit for a release that is itself the day's lead story (e.g., a major LLM 0.33 feature release).
