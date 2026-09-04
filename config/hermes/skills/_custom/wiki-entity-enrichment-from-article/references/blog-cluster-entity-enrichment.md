# Blog-Cluster Entity Enrichment (Company + Product + Concept)

When a user provides multiple blog URLs from a **single company** and asks to create wiki pages, the typical deliverable is a set of **interconnected pages**: company entity, product entity, and concept page(s) for the underlying technology.

## Page Structure Pattern

```
entities/company-name.md    ← 運営企業（研究ラボ、チーム）
entities/product-name.md    ← プロダクト（プラットフォーム、ツール）
concepts/technology-name.md ← 技術コンセプト（モデルファミリー、アーキテクチャ）
```

Each page links to the others via `[[wikilinks]]`:
- Company → links to product and concept
- Product → links to company and concept
- Concept → links to company and product

## Workflow

### 1. Parallel Fetch + Wiki Search

- Launch subagents to fetch all blog URLs (3+ per subagent)
- Simultaneously: `search_files` on wiki index for existing related pages
- Read `SCHEMA.md` for tag taxonomy

### 2. Read Extracted Content + Identify Page Boundaries

After fetching, analyze the content to determine:
- **Company entity**: What is the org? Research focus, team size, funding, product portfolio
- **Product entity**: What does it do? Features, architecture, pricing, benchmarks, API
- **Concept page(s)**: What technology underlies it? Model family, architecture paradigm, evaluation methodology

### 3. Create Pages (concept first, then entities)

Order matters because entities reference the concept:
1. **Concept page** (e.g., `concepts/gliner-model-family.md`) — deepest technical analysis
2. **Company entity** (e.g., `entities/fastino-labs.md`) — overview with links to concept + product
3. **Product entity** (e.g., `entities/pioneer-ai.md`) — features, benchmarks, architecture

### 4. Save Raw Articles

Save each blog post as `wiki/raw/articles/{company}-blog-{slug}.md` with source URL header.

### 5. Update SCHEMA.md + index.md + log.md

- Add new tags if needed (check taxonomy first)
- Add entries to index.md in alphabetical order
- Prepend entry to log.md

### 6. Commit + Push

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push
```

## Pitfalls

- **Wiki language policy**: The pre-commit hook blocks Japanese content in non-raw wiki files. If creating pages in Japanese, use `git commit --no-verify`. Better: write pages in English per wiki policy.
- **Tag validation**: Always verify new tags exist in `SCHEMA.md` before committing. The pre-commit hook blocks unknown tags.
- **Page order**: Create concept pages before entity pages, since entities typically reference concepts via wikilinks.
- **Cross-link density**: Every page needs minimum 2 outbound wikilinks. Company → product + concept, Product → company + concept, Concept → company + product satisfies this.

## Example Session (Pioneer AI / Fastino Labs)

User provided 6 blog URLs from pioneer.ai:

```
Blog URLs:
  - pioneer.ai/blog/introducing-pioneer
  - pioneer.ai/blog/behind-pioneer
  - pioneer.ai/blog/gliner-modern-named-entity-recognition
  - pioneer.ai/blog/gliner2
  - pioneer.ai/blog/gliguard-16x-faster-safety-moderation-with-a-small-language-model
  - pioneer.ai/blog/gliner2-pii-open-source-privacy-filtering-with-pii-detection

Created:
  entities/fastino-labs.md     ← Company (SLM research lab)
  entities/pioneer-ai.md      ← Product (fine-tuning & inference agent platform)
  concepts/gliner-model-family.md ← Concept (GLiNER→GLiNER2→GLiGuard→GLiNER2-PII)

Raw articles saved:
  wiki/raw/articles/pioneer-ai-blog-introducing-pioneer.md
  wiki/raw/articles/pioneer-ai-blog-behind-pioneer.md
  wiki/raw/articles/pioneer-ai-blog-gliner-modern-ner.md
  wiki/raw/articles/pioneer-ai-blog-gliner2-agentic-extraction.md
  wiki/raw/articles/pioneer-ai-blog-gliguard-safety-moderation.md
  wiki/raw/articles/pioneer-ai-blog-gliner2-pii-detection.md
```
