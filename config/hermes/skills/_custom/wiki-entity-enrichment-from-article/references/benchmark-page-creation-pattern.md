# Benchmark Page Creation Pattern

When adding a new AI benchmark to `concepts/ai-benchmarks/`, follow this pattern.

## Directory Structure

- Benchmark pages go under `wiki/concepts/ai-benchmarks/<slug>.md`
- Sub-index at `wiki/concepts/ai-benchmarks/index.md` — organized by category sections
- Raw sources go under `wiki/raw/articles/`

## Frontmatter Template

```yaml
---
title: "<Benchmark Name> (<Full Name>)"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active
tags:
  - benchmark
  - evaluation
  - <domain-specific-tags>
aliases:
  - <short-name>
  - "<Alt Name>"
sources:
  - https://arxiv.org/abs/XXXX.XXXXX
  - https://huggingface.co/datasets/<org>/<dataset>
  - raw/articles/<raw-file>.md
related_entities:
  - entities/<author>.md
related_concepts:
  - concepts/ai-benchmarks-and-evals.md
  - <related-concept-pages>
---
```

## Standard Sections

1. **What It Measures** — what the benchmark evaluates, why it exists
2. **Data/Methodology** — construction pipeline, data sourcing
3. **Key Results** — scores, comparisons, leaderboards
4. **Related Benchmarks** — comparison with similar/preceding benchmarks
5. **Connections to Other Wiki Concepts** — wikilinks to related pages

## Workflow

1. Fetch arXiv abstract (use `r.jina.ai` or `curl` + meta tags)
2. Fetch announcement post (X/blog) if available
3. Create raw article in `wiki/raw/articles/`
4. Create benchmark page in `wiki/concepts/ai-benchmarks/`
5. Update `concepts/ai-benchmarks/index.md` — add to appropriate category section
6. Update `wiki/index.md` — insert alphabetically
7. Update `wiki/log.md` — append entries
8. `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: add <name>" && git push`

## Sub-Index Category Sections

Current sections in `concepts/ai-benchmarks/index.md` (as of 2026-06-26):
- Xeophon Series (18 Parts) — subdivided by domain
- τ-bench Ecosystem
- SWE-bench Ecosystem
- Web & OS Agent Benchmarks
- Agent & Game Environments
- Science, Research & Enterprise
- Safety & Adversarial
- Reward & Judge Evaluation
- Agent Evaluation Infrastructure
- Domain-Specific
- Coding (non-xeophon)
- Metrics
- Search & Retrieval
- Benchmark Methodology & Meta

Add new sections as needed.

## Bulk Ingestion from "Awesome" Lists

When a curated GitHub list (awesome-evals, awesome-llm, etc.) contains dozens of benchmarks/tools not yet in the wiki, use this batch workflow:

### Step 1: Extract and diff
1. Download the README (`curl -sL <raw-url> > /tmp/source.md`)
2. Extract all benchmark/tool names with URLs via regex: `\*\*\[([^\]]+)\]\(([^)]+)\)\*\*`
3. List existing wiki pages: `ls wiki/concepts/ai-benchmarks/*.md | sed 's/.md$//'`
4. Fuzzy-match extracted names against existing slugs (common aliases: τ→tau, τ²→tau-squared)
5. Output: list of new benchmarks to create

### Step 2: Batch create via delegate_task
- Group new benchmarks into 3-4 thematic batches (e.g., Web/OS, Coding/SWE, Science, Safety)
- Launch parallel delegate_task calls, each creating 10-15 pages
- Pass each subagent: the benchmark list, the raw article path, allowed tags, and template format
- Each subagent uses `write_file` to create pages

### Step 3: Update indexes
- **ai-benchmarks/index.md**: Add new category sections as needed, insert entries under correct section
- **wiki/index.md**: For bulk additions (20+), add a sub-index pointer + 5-10 representative entries rather than all individual entries
- **wiki/log.md**: Single summary entry describing the batch operation

### Step 4: Tag validation and commit
- Run `git add wiki/ && git commit` to trigger pre-commit tag validation
- Fix any tag violations (common: invented tags like `contamination` → use `benchmark-optimization`)
- `git push`

## Pitfalls

- **Sub-index is separate from main index**: Both need updating — the sub-index (`concepts/ai-benchmarks/index.md`) AND the main wiki index (`wiki/index.md`)
- **Don't duplicate in sub-index**: Add the entry once under the appropriate section, not in multiple sections
- **related_concepts should include ai-benchmarks-and-evals**: This is the MOC page
- **Tags must exist in SCHEMA.md**: Check before creating pages; add new tags to SCHEMA.md first if needed
- **r.jina.ai for arXiv HTML**: Use `curl -s "https://r.jina.ai/https://arxiv.org/html/<id>v<N>"` for full paper content when PDF extraction is needed
- **Tag `contamination` not in SCHEMA.md**: Use `benchmark-optimization` instead for contamination-aware benchmarks (e.g., LiveBench)
- **Bulk index.md strategy**: For 20+ new pages, don't add all to main wiki/index.md — add a sub-index pointer (`[[concepts/ai-benchmarks/index]]`) + 5-10 representative entries. The sub-index has the full catalog.
- **Subagent tag compliance**: Subagents may invent tags not in SCHEMA.md. Always run `git commit` (which triggers pre-commit tag validation) before pushing. Fix violations by replacing invented tags with canonical ones.
- **related_concepts wikilinks**: Subagents sometimes use bare `[[wikilinks]]` in body text instead of proper `related_concepts` frontmatter. Verify frontmatter has `related_concepts:` list with actual page paths.
