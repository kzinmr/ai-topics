# Companion Analysis Pages Pattern

When an index page lists a series of related documents (system cards, model releases, product versions), a companion chronological/trend analysis page adds significant value.

## Trigger
- User asks to analyze milestones, evolution, or trends across a series of indexed documents
- An index page exists but lacks temporal/analytical perspective
- User wants "時系列分析" or "milestone analysis" of a document series

## Pattern: Index Page + Companion Timeline

### Index Page (`system-cards.md`)
Lists all documents with metadata (date, version, links). Factual, reference-oriented.

### Companion Timeline Page (`system-card-milestones.md`)
Chronological analysis with:
- **Phases** — group milestones by structural shifts (not just date ranges)
- **Per-milestone detail** — what changed, why it matters, significance
- **Trend analysis** — escalation patterns, co-evolution of capabilities and safety, sophistication growth
- **Structural innovations table** — first appearance of each new pattern

## Structure Template

```markdown
## Phase N: [Phase Name] (Date Range)

### N. [Milestone Title] — [Model/Product] (Date)

Description of what changed.

- **Key innovation**: The structural shift
- **Significance**: Why it matters in the larger arc
- **Cross-reference**: See [[related-page]]

## Trend Analysis

### [Dimension] Escalation
```  (ASCII timeline showing progression)

### Capability-Safety Co-evolution
| Capability Advance | Safety Response |
|---|---|

### Evaluation Sophistication Growth
- **Period**: What was measured
```

## Cross-Referencing
- Link companion page FROM index page (add to index's `## See Also`)
- Link companion page TO related pages (other providers' milestone pages for comparison)
- Ensure frontmatter `sources:` references the index page

## Naming Convention
- Index: `{provider}-system-cards.md` or `{series-name}.md`
- Companion: `{provider}-system-card-milestones.md` or `{series-name}-milestones.md`

## Example
- `concepts/claude/system-cards.md` (index, 17 cards)
- `concepts/claude/system-card-milestones.md` (companion, 12 milestones, 5 phases)
- `concepts/gpt/gpt-system-card-milestones.md` (GPT equivalent for cross-provider comparison)

## Pitfalls
- Don't duplicate the index — the companion adds ANALYSIS, not just reordering
- Each milestone should have a "Significance" that connects to the larger narrative
- Trend analysis sections should use tables or ASCII timelines, not prose lists
- Cross-reference to other providers' milestone pages for comparison context
