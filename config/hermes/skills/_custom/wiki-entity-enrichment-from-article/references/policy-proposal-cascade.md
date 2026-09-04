# Policy Proposal Article Cascade (★★★★☆)

When a major AI figure publishes a detailed regulatory/governance proposal as a standalone article (X Article, blog post, essay), the correct action is a **multi-page cascade** rather than a single-page enrichment.

## Detection

- The article is by a leading AI executive (CEO, Chief Scientist) or prominent policy voice
- The content is a **specific institutional proposal** (not general commentary): names a model (FINRA, FAA, CAISI), defines thresholds, proposes mechanisms
- The proposal enters a landscape with **existing competing proposals** already documented in the wiki
- The author already has a rich entity page (>100 lines)
- An umbrella regulation/governance concept page already exists (e.g., `ai-regulation-2026`)

## Cascade Steps

### Step 1: Save Raw Article
Save with proper date-author-slug naming.

### Step 2: Create New Concept Page (write_file)
The proposal deserves its own concept page with:
- Full frontmatter (aliases, related, sources)
- The institutional model and mechanics
- Comparison table against existing competing proposals
- Key philosophical positions / quotes from the author
- Criticism & open questions section
- Cross-references to umbrella regulation page and competing proposals

### Step 3: Enrich Author Entity Page (patch)
Add a dedicated subsection (e.g., "On AI Governance (July 2026)") under their philosophy/views section:
- 8-10 bullet points summarizing the proposal
- Wikilink to the new concept page
- Update frontmatter: `updated` date, `sources` array
- Add to `## Related` and `## Sources` sections
- The entity page gets a THUMBNAIL of the proposal — the concept page has the full detail

### Step 4: Enrich Umbrella Regulation Page (patch)
Add a dedicated subsection to the regulation hub (e.g., `ai-regulation-2026`):
- The author/proposal name and date as heading
- Key elements as bullet points
- **Comparison table** against competing proposals already documented on the page (Amodei, OpenAI, etc.)
- Positioning statement: how this proposal differs from others
- Wikilink to the new concept page
- Source reference to the raw article
- Update frontmatter: `updated` date, `sources` array

### Step 5: Cross-Reference Competing Proposals (patch)
For each competing proposal page already in the wiki (e.g., `frontier-safety-blueprint`):
- Add a bullet point in "Broader Context" section noting the new proposal
- Add a wikilink in "Related Concepts" section

### Step 6: Update index.md and log.md
- Insert new concept alphabetically in Concepts section
- Increment concept count
- Single log entry summarizing all page changes

## Comparison Table Template

When adding the proposal to the umbrella regulation page, use a comparison table:

```markdown
| Element | New Proposal (Model) | Existing A (Model) | Existing B (Model) |
|---------|---------------------|-------------------|---------------------|
| Institutional model | ... | ... | ... |
| Pre-release review | ... | ... | ... |
| International scope | ... | ... | ... |
| Slowdown authority | ... | ... | ... |
| Open-source representation | ... | ... | ... |
```

## Working Examples

- **Demis Hassabis "A Framework for Frontier AI" (Jul 2026)**: Created `concepts/frontier-ai-standards-body`, enriched `entities/demis-hassabis`, `concepts/ai-regulation-2026`, `concepts/frontier-safety-blueprint`
- **Dario Amodei "Policy on the AI Exponential" (Jun 2026)**: Already ingested into `concepts/ai-regulation-2026` with FAA-model comparison
- **Nathan Lambert "Welcome to the AGI Era of AI Governance" (Jun 2026)**: Already ingested into `concepts/ai-regulation-2026` with geopolitical trigger analysis

## Pitfalls

- **Don't create a new regulation umbrella page**: The proposal is one voice in a broader landscape. Add it to the existing regulation hub, don't create a competing hub.
- **Comparison table must reflect already-documented proposals**: Read the umbrella page first to see which frameworks are already described — your comparison table should reference those exact ones.
- **Entity page gets a thumbnail, not a duplicate**: The author's entity page should have a brief summary + wikilink. The concept page has the full depth.
- **Search for author's entity page before creating**: Major figures almost always have existing entity pages. Use `ls` and `grep` on the entities directory, not `search_files(target="files")` which returns false negatives with symlinks.
