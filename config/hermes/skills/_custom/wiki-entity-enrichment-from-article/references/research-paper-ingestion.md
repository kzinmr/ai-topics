# Research Paper Ingestion Pattern

When a user provides a URL to a research paper, project page, or benchmark dataset, use this multi-source workflow to create a comprehensive wiki ingestion.

## Trigger Signals
- User shares an arXiv link, conference paper URL, or research project page
- URL points to a `.github.io` project site with associated paper + code
- User says "ingest this article" and the source is academic/research

## Multi-Source Research Strategy

Fetch from **3 sources in parallel** (when available):

1. **Project page** (the user-provided URL) — pipeline overview, use case narrative, high-level findings
2. **GitHub README** (same org/user, same repo name) — technical details, installation, dataset info, config examples
3. **arXiv abstract** (search by paper title) — formal abstract, author list, affiliation

Use `curl -sL <url>` for each. For arXiv, extract metadata from `<meta>` tags:
```bash
curl -sL "https://arxiv.org/abs/XXXX.XXXXX" | grep -oP '(?<=<meta name="citation_author" content=")[^"]+'
curl -sL "https://arxiv.org/abs/XXXX.XXXXX" | grep -oP '(?<=<meta property="og:description" content=")[^"]+'
```

## Page Creation Pattern

### When to create paired pages (concept + entity)
Create **both** a concept page and an entity page when:
- The paper introduces a **named pipeline/method/framework** (→ concept page)
- AND the paper introduces a **named dataset/benchmark/tool** (→ entity page)
- Example: "Retrieve, Merge, Predict" (concept) + "YADL" (entity)

### When to create a single concept page only
- Paper proposes a technique or methodology without a distinct benchmark entity
- Example: a paper on a new attention mechanism

### When to create a single entity page only
- Paper is primarily about building a tool/system/dataset
- Example: a paper introducing a new LLM or framework

## Workflow Steps

1. **Fetch all sources** (project page, GitHub README, arXiv) in parallel
2. **Save raw article** to `wiki/raw/articles/<descriptive-slug>.md`
   - Include YAML frontmatter with `url`, `arxiv`, `github`, `fetched` fields
   - Combine abstract + pipeline overview + key findings from all sources
3. **Check SCHEMA.md** for existing tags — add new tags to taxonomy BEFORE creating pages
4. **Create concept page** at `wiki/concepts/<method-name>.md`
   - Tags: include technique tags (e.g. `automl`, `feature-engineering`) + domain tags
   - Cross-link to related existing concepts (RAG, vector-search, etc.)
   - Include "Open Questions" section for future research directions
5. **Create entity page** (if applicable) at `wiki/entities/<dataset-or-tool-name>.md`
   - Tags: `datasets`, `benchmark`, `open-data` as applicable
   - Link back to the concept page via `[[wikilinks]]`
6. **Update `wiki/index.md`**:
   - Insert entries alphabetically in correct sections
   - Bump page count in section headers
7. **Update `wiki/log.md`**:
   - Prepend entry (newest first) with bullet points for each file created/modified
8. **Commit and push**:
   ```bash
   cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ingest <paper-name>" && git push
   ```

## Pitfalls

- **Don't forget SCHEMA tag updates**: Pre-commit hook blocks pages with tags not in taxonomy. Always check/add tags first.
- **arXiv search may return multiple results**: Verify the correct paper by checking the abstract matches.
- **GitHub README may diverge from project page**: Use the project page as primary narrative, README for technical details.
- **Don't create an entity page for generic knowledge bases** (e.g. YAGO, Wikidata) — only for purpose-built datasets/benchmarks that are the paper's contribution.
- **Concept page cross-links**: Always include at minimum 2 outbound `[[wikilinks]]` — link to related concepts, the benchmark entity, and upstream concepts (RAG, embeddings, etc.).

## Example Session (Retrieve, Merge, Predict)

Input: `https://soda-inria.github.io/retrieve-merge-predict/`

Created:
- `raw/articles/retrieve-merge-predict.md` (raw source with arXiv abstract + GitHub README)
- `concepts/retrieve-merge-predict.md` (3-stage pipeline concept)
- `entities/yadl.md` (benchmark data lake entity)
- SCHEMA.md: added `automl`, `feature-engineering`, `data-lakes` tags
- index.md: 2 new entries, entity count bumped
- log.md: prepended ingestion entry
