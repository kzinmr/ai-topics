# Research Infrastructure Buildout Pattern

## When to Use

When the user asks you to "ingest an article and build research infrastructure" or "make research on X easier," or when you discover an entity page with broken `[[wikilinks]]` to concept pages that don't exist yet.

## The Pattern

### 1. Audit Existing Links

Before enriching the entity page, audit EVERY wikilink in it:

```bash
# Find all wikilinks in the entity page
search_files(path="/opt/data/wiki/entities", pattern="\[\[concepts/", target="content")
# For each linked concept page, check if it exists
search_files(path="/opt/data/wiki/concepts", pattern="<slug>")
```

Pay special attention to:
- `related:` frontmatter entries — these are explicit design intents for the knowledge graph
- `[[wikilinks]]` in body text — indicate conceptual dependencies
- Cross-references to other entities

### 2. Classify Broken Links

| Broken Link Type | Action |
|-----------------|--------|
| Core concept (2+ pages reference it) | **Create** a new concept page |
| Niche concept (only this page references) | Either create if substantial, or fold into entity page |
| Comparable to existing concept | Add section to existing concept page instead |
| Out of scope | Remove the link |

### 3. Create Concept Pages Before Enriching Entity

**Order matters**: Create missing concept pages FIRST, then enrich the entity. Why:
- Entity enrichment naturally references the new concepts with fresh wikilinks
- The concept pages provide semantic context that shapes entity enrichment
- Prevents a situation where entity is enriched but links still broken

### 4. Cross-Source Synthesis

When enriching, search for OTHER raw articles about the same topic:

```bash
search_files(path="/opt/data/wiki/raw/articles", pattern="<topic>")
```

Multiple sources on the same entity → richer entity page with multiple perspectives.

### 5. Verify Connected Graph

After all updates:
- Every wikilink in the entity page should resolve
- Every `related:` entry should point to an existing page
- The entity page should link TO the concept pages, and concept pages should link BACK

## Example: Palantir (2026-05-25)

```
Before:
  entities/palantir.md (164 lines)
  → wikilinks to concepts/agent-ontology ❌ (broken)
  → wikilinks to concepts/decision-centric-architecture ❌ (broken)
  → wikilinks to concepts/enterprise-agents ❌ (broken)
  → Bert Hubert raw article existed but not incorporated

After:
  entities/palantir.md (253 lines, +FDE +Government sections)
  + concepts/decision-centric-architecture.md (103 lines) ✅
  + concepts/enterprise-agents.md (141 lines) ✅
  + concepts/agent-ontology.md (138 lines) ✅
  → All links resolve, bidirectional cross-references
  → Bert Hubert synthesis added government dependency perspective
```
