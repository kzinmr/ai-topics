# Non-Technical / Philosophical Concept Ingestion

When the source material is a philosophical, political, or ideological essay (not a technical AI concept), adjust wiki ingestion accordingly.

## Frontmatter Tags

Use broader, cross-domain tags rather than purely technical ones:

```yaml
tags:
  - philosophy
  - technology-criticism
  - political-theory
  - civilization-decline
  # also include relevant technical tags if the essay intersects with AI
  - ai-skepticism
  - e-acc
```

## Structure Differences from Technical Concepts

| Dimension | Technical Concept | Philosophical Concept |
|-----------|------------------|-----------------------|
| **Core** | Mechanism, API, workflow | Thesis, argument, worldview |
| **Comparisons** | Tool A vs Tool B | Thinker A vs Thinker B (comparison table) |
| **Sections** | Installation, usage, configuration | Intellectual lineage, key arguments, implications |
| **Counterpoint** | Limitations, edge cases | Criticisms, controversies |

## Comparison Table Pattern

When the essay directly responds to another text (e.g., Yarvin's manifesto rebutting Andreessen's), include a structured comparison table:

| Dimension | Source A | Source B |
|-----------|----------|----------|
| Primary thinker | Name | Name |
| Core text | Title (year) | Title (year) |
| View of X | Perspective A | Perspective B |
| ... | ... | ... |

## Intellectual Lineage Section

For essays that draw on historical thinkers, create an "Intellectual Lineage" subsection:
- Identify each referenced thinker and their original work
- Explain HOW the author uses them (agreement, contrast, warning)
- Include direct quotes where available

## Raw Article Notes

- Substack URLs often redirect through substack.com/redirect/... hashes
- **Always use the original publication URL** (graymirror.substack.com/p/...) for the filename, NOT the redirect URL
- Save with full frontmatter including author, date, type, and tags
