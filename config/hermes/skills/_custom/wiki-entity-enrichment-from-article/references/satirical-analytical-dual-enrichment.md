# Satirical / Analytical Article Dual Enrichment (Entity + Concept)

When an expert's **satirical or analytical article** makes a substantive point about a topic that already has a concept page, the optimal enrichment pattern is a **dual split**: the author's entity page gets the full satirical analysis, while the concept page gets a condensed cross-reference.

This differs from:
- **Entity enrichment cascade** (entity-enrichment-cascade-pattern.md → 4-5 pages, equal depth) — for substantive new frameworks and multi-sub-page cascades
- **Cross-cutting article ingestion** (cross-cutting-article-ingestion.md → equal-depth sections per page) — for articles with multiple distinct technical domains
- **Opinion leader policy essays** (cross-cutting-article-ingestion.md sub-pattern) — for serious policy proposals, not satire

## When This Applies

- The article is satirical, analytical, or darkly humorous — not a policy proposal or technical how-to
- A concept page for the article's topic ALREADY EXISTS with real-world incidents/cases
- The satire's value is in demonstrating systemic vulnerabilities through a fictional scenario that the author designs as a stress test of their own analytical framework

## Decision Rules

| Question | If YES | If NO |
|----------|--------|-------|
| Does the author already have a rich entity page? | Full analysis goes on entity page | Create entity page first, then enrich |
| Does the concept page exist with real-world cases? | Condensed cross-reference only | May need full concept section instead |
| Does the satire map specific elements to real-world equivalents? | Add a parallelism mapping table on the entity page | Entity page gets descriptive analysis only |
| Does the article introduce a genuinely new conceptual angle not on the concept page? | Add a brief subsection to the concept page too | Concept page gets only a "Related" cross-ref |

## Workflow

### 1. Read the Article Body (MANDATORY)
Fully understand the satirical mechanism before deciding placement. A satirical piece's value often lies in its **mapping accuracy** — which real-world patterns each fictional element represents.

### 2. Entity Page: Full Analysis
Add to the author's entity page as a new Core Ideas subsection:
- **Article title and context** (publication date, format, subject)
- **The satirical mechanism** (e.g., "seven independent AI-powered security gates fail for different reasons")
- **Detailed enumeration** of each satirical element with real-world mapping
- **Parallelism mapping table** — col 1: satirical target, col 2: real-world parallel
  ```
  | Satirical target | Real-world parallel |
  |---|---|
  | creats.io registry | npm/PyPI registries |
  | OpenClaw-4.2 | Claude Code (Anthropic) |
  ```
- **Analytical insight** — what the satire reveals that a non-satirical analysis would not
- **Key quote** from the article if it crystallizes the thesis
- Cross-references to the relevant concept page(s)

### 3. Concept Page: Condensed Cross-Reference
Add a brief item to the concept page:
- A single paragraph covering what the satire demonstrates
- A forward link to the entity page (`[[entities/author]]`) for full analysis
- Do NOT duplicate the parallelism table from the entity page
- Timestamp and update the `updated` frontmatter date and `sources`

### 4. Conditional: Full Concept Section
Only add a full new section to the concept page if the satire reveals a **failure mode not documented by any real incident** already on the page. In practice this is rare — satirical pieces compress existing vulnerabilities into a single narrative rather than identifying genuinely new ones. When it does happen, precede with a "Satirical case study" subheading and note the article's fictional nature.

## Example (June 2026)

**Article**: Andrew Nesbitt, "Incident Report: CVE-2026-LGTM" (nesbitt.io)

| Target | Enrichment type | Content size |
|--------|----------------|-------------|
| `entities/andrew-nesbitt.md` | Full subsection | ~30 lines (7-gate enumeration + parallelism table + analytical insight) |
| `concepts/ai-supply-chain-security.md` | Condensed item in case study list | ~5 lines (paragraph + entity wikilink) |

## Pitfalls

- **Do not over-enrich the concept page**: The concept page documents real incidents. Adding a full satirical analysis to it dilutes the factual signal. The satire is primarily a demonstration of the author's analytical style, which belongs on their entity page.
- **Do not skip the parallelism table**: The mapping between fiction and reality is the core intellectual contribution of a well-executed AI satire. A bare summary (e.g., "7 AI gates fail") without the mapping loses most of the article's value.
- **Check if the concept page's existing incidents already cover the same failure modes**: If every satirical failure mode maps to an existing concept page incident, the concept page enrichment should be minimal (just a note that the author's satire independently arrives at the same conclusions). Only add a new case study if the satire identifies a failure mode not yet documented.
- **Update both `updated` dates and `sources`**: Both the entity page and concept page need their frontmatter updated.
