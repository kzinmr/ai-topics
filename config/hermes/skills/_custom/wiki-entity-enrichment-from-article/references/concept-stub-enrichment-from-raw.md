# Enriching Concept Stubs from Raw Article Mentions

When a concept page exists as a stub (status: stub, ~24 lines), enrich it by mining `wiki/raw/` for articles that mention the concept — rather than web-searching from scratch.

## Trigger

User asks to enrich an existing concept page. The page has TODO markers or minimal content.

## Workflow

### 1. Discover Raw Mentions

Search broadly across raw/ for the concept term (include variants, abbreviations):

```python
search_files(path="~/wiki", pattern="sycophancy|sycophant", target="content", limit=50)
```

This returns hits in `raw/articles/`, `raw/papers/`, `raw/inbox/`, and existing wiki pages. Focus on `raw/` hits — wiki hits show cross-reference opportunities.

### 2. Check for Duplicate/Sibling Stubs

Search `index.md` for the concept slug AND aliases. Common pattern: two stubs covering the same topic with different names (e.g., `ai-sycophancy` and `sycophancy-in-llms`).

Decision:
- **One is clearly canonical** (better name, more stubs referencing it) → enrich that one, convert the other to a `status: redirect` page
- **Both are equally good** → pick the one that better matches the concept's natural scope, merge aliases into its frontmatter

### 3. Read the Richest Existing Page First

If there's already a rich page on a sub-topic (e.g., `anti-sycophancy.md` at 92 lines), read it first. It often contains:
- Sources that also mention the parent concept
- Cross-references you'll need to maintain
- Structure you can mirror or contrast

### 4. Read Relevant Raw Articles

For each raw article hit, read enough context (20-40 lines around the match) to understand how the concept is discussed. Prioritize articles where the concept is a **primary topic** over casual mentions.

Key categories of raw sources to look for:
- **Technical reports/papers** → formal definitions, benchmarks, evaluation methodology
- **Blog posts/analysis** → practical implications, industry observations
- **Newsletter digests** → brief mentions that point to deeper sources

### 5. Build the Enriched Page

Structure for a concept page (adjust based on concept type):

```markdown
## Definition and Taxonomy
- What it is, key distinctions (hard vs soft, etc.)

## Root Causes
- Training methodology contributions (RLHF, etc.)
- Mechanistic interpretability findings
- Architectural factors

## Manifestations in Practice
- In specific domains (coding agents, user-facing, multi-agent)
- Real-world examples from raw articles

## Measurement and Evaluation
- Benchmarks table (name, focus, key finding)
- Industry metrics (company internal evaluations)

## Model-Specific Observations
- Per-model differences if available from raw sources

## Mitigation
- Brief overview + wikilink to dedicated mitigation page if one exists

## Open Questions
- From raw sources or gaps in coverage

## Related
- Minimum 2 wikilinks (SCHEMA.md requirement)
- Link to sub-topic pages, related concepts, entities
```

### 6. Handle the Redirect Stub

For the consolidated duplicate:
```markdown
---
title: "Old Name"
type: concept
aliases: [old-slug]
status: redirect
---

# Old Name

> **Redirect**: This page has been consolidated into [[concepts/canonical-name]].
```

Add the old slug to the canonical page's `aliases:` frontmatter.

### 7. Update Cross-References

If an existing rich page (like `anti-sycophancy.md`) should link back to the enriched page, add the back-reference via `patch`. Check the rich page's `## Related` section.

### 8. Update index.md + log.md + Commit

Standard wiki update flow. For the redirect page, add an entry in index.md:
```
- [[concepts/old-slug]] — → [[concepts/canonical-slug]]
```

## Pitfalls

- **Don't overwrite rich pages**: If a sub-topic page already has 40+ lines, don't rewrite it — just add back-references
- **Tag validation**: Check SCHEMA.md before committing. Tags like `safety`, `alignment`, `ai-safety` must already exist in the taxonomy
- **Source attribution**: List all raw articles referenced in frontmatter `sources:` field
- **CJK detection**: English-only wiki pages. Check for accidental CJK in quoted material
