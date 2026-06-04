# Multi-Provider Comparison Ingestion Pattern

When the user provides multiple URLs about the **same product/integration/standard** from **different providers**, the emergent wiki structure is: comparison page + entity pages + concept enrichment. This pattern is distinct from single-article ingestion or multi-article author-arc ingestion.

## Trigger

User says something like:
- 「self-hosted sandboxes to Claude Managed Agents に対する対応sandboxサービスの記事群をwikiに取り込んで関連付けて」
- 「MCPサーバー実装の比較記事をwikiに取り込んで」
- Any request containing 2+ URLs about the same topic from different companies/providers

## Workflow

### Phase 1: Extract All Articles in Parallel

1. Call `web_extract` on all URLs simultaneously (up to 5 per call)
2. Check if web_extract returned summaries vs full body text (word count < ~500 for a long page → summary trap)
3. For summary-truncated articles, fall back to `execute_code` with curl + HTML strip (see `references/curl-html-to-markdown-extraction.md`)
4. Save each as a raw article: `wiki/raw/articles/YYYY-MM-DD_{provider}_{topic}.md` with proper frontmatter

### Phase 2: Scan Existing Coverage

Before creating pages:
1. `search_files` for the topic slug across wiki to find existing concept/entity pages
2. Check if a parent concept page already exists (e.g., `concepts/claude-managed-agents.md`)
3. Check if entity pages exist for each provider (e.g., `entities/cloudflare.md` may exist but `entities/cloudflare-sandbox.md` may not)
4. If a provider has an existing parent entity page and you're creating a product-specific one, use distinct names: `{provider}-sandbox.md` vs `{provider}.md`

### Phase 3: Create Pages via Parallel Subagents

Deploy two subagent tasks in parallel:

**Subagent A: Comparison Page**
- Goal: Create `wiki/comparisons/{topic}-providers.md`
- Route to `comparisons/` per `wiki-comparison-page-routing` (3+ items = comparison)
- Include: summary table (all providers × 8-10 dimensions), per-provider detailed sections, architecture diagrams, decision guidance
- Must link to entity pages for each provider

**Subagent B: Entity Pages**
- Goal: Create one entity page per provider: `wiki/entities/{provider}-{product}.md`
- Each entity covers: product description, key CMA integration features, [[wikilinks]] to comparison + concept pages
- If a parent entity already exists (e.g., `entities/cloudflare.md`), the product-specific page should cross-link to it

**⚠️ Critical: Provide entity page naming conventions to BOTH subagents.** Tell Subagent A exactly what entity page slugs Subagent B will use, so wikilinks are consistent. See pitfall below.

### Phase 4: Enrich Parent Concept Page

If a parent concept page exists (e.g., `concepts/claude-managed-agents.md`):
1. Add a "Provider Options" subsection with a compact comparison table
2. Cross-link to the new comparison page: `[[comparisons/{topic}-providers]]`
3. Add new raw article sources to frontmatter
4. Bump `updated` date if needed

### Phase 5: Index, Log, Commit

1. Insert each new page into `wiki/index.md` alphabetically under its section
2. Update section header counts: Entities (N→N+4), Comparisons (N→N+1)
3. Update top-level counts: Total pages, Indexed entries
4. Append log entry to `wiki/log.md`
5. Commit once: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push`

## Pitfalls

### Subagent wikilink coordination failure (RECURRING)
When the comparison subagent and entity subagent run in parallel, they may use inconsistent entity page names:
- Comparison subagent wikilinks `[[entities/cloudflare]]` (the parent company page)
- Entity subagent creates `entities/cloudflare-sandbox.md` (the product-specific page)

**Fix**: In the `context` field of BOTH subagents, explicitly specify the entity page slugs they should use:
```
Entity pages will be at:
- wiki/entities/cloudflare-sandbox.md
- wiki/entities/daytona-sandbox.md
- wiki/entities/modal-sandbox.md
- wiki/entities/vercel-sandbox.md
```

After both subagents complete, verify consistency:
```bash
grep -o 'entities/[a-z-]*' wiki/comparisons/{topic}.md | sort -u
ls wiki/entities/{provider}*.md
```

If there's a mismatch, redirect wikilinks to the actual entity page paths before committing.

### Index.md patch removes unrelated entries
When using `patch` on `wiki/index.md`, the `old_string` must be precise. A too-broad match (e.g., matching across non-adjacent lines with an implicit wildcard) can silently drop entries between matched lines. Always verify the surrounding N lines after each index.md patch.

### Existing parent entity pages
Providers like Cloudflare, Vercel, Modal may already have `entities/{company}.md`. The product-specific pages (`{company}-sandbox.md`) should cross-link to these parent entities, not replace them. Check with `search_files` before creating.
