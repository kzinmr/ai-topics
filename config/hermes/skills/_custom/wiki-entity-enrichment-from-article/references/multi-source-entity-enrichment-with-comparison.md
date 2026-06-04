# Multi-Source Entity Enrichment with Comparison Page Update

When a user provides multiple URLs (3+) about a single topic and asks to "deeply understand" and "incorporate into wiki," the workflow extends beyond single-article enrichment. The user often provides analytical framing (e.g., "this relates to our discussion about X") that must be captured as strategic significance, not just facts.

## Workflow

### 1. Parallel Fetch + Wiki Search (simultaneous)

Launch subagents to fetch all URLs while simultaneously searching wiki for existing content:

```python
# In parallel:
delegate_task(tasks=[
    {"goal": "Fetch URL1 and extract all content...", "toolsets": ["web", "browser"]},
    {"goal": "Fetch URL2 and extract all content...", "toolsets": ["web", "browser"]},
    {"goal": "Fetch URL3 and extract all content...", "toolsets": ["web", "browser"]},
])
# Simultaneously:
search_files(pattern="topic", path="/opt/data/wiki", target="content")
search_files(pattern="topic", path="/opt/data/wiki", target="files")
read_file(path="/opt/data/wiki/SCHEMA.md")
```

### 2. Read Existing Pages That Will Be Modified

Before writing, read ALL pages that will be touched:
- The entity page being enriched
- Any concept pages referenced in index but potentially missing
- Any comparison pages that may need updating
- The harness-backend-routing or protocol comparison pages if relevant

### 3. Create Raw Article First

Always save consolidated findings as a raw article before modifying wiki pages:

```
write_file("wiki/raw/articles/YYYY-MM-DD_topic-slug.md", consolidated_content)
```

### 4. Enrich Existing Entity Page

Add new section(s) to the existing entity page. Key patterns:
- Add new sources to frontmatter
- Add new tags if needed (verify in SCHEMA.md first)
- Add new section with `---` separator before existing "See Also"
- Include architecture diagrams, comparison tables, strategic analysis
- Add `→ [[wikilinks]]` to related pages at section end

### 5. Create Missing Concept Pages

When index.md references a concept page that doesn't exist on disk:
- Create the page with comprehensive content
- This is a "ghost entry" — the index was updated but the file was never created
- Include cross-references to related entity and comparison pages

### 6. Update Existing Comparison Pages

When the new information adds a system to an existing comparison:
- Update the title to include the new entrant
- Add the new system to the evaluation matrix (add column)
- Add a strengths section for the new system
- Update the ideal architecture diagram if applicable
- Update the decision guide
- Add new sources to frontmatter

### 7. Batch Update index.md + log.md + Commit

Update all index entries for modified pages, prepend log entry, commit and push.

## Pitfalls

- **Subagent fetch failures**: Browser-based subagents often time out on JS-heavy sites. If a subagent returns sparse results, retry with direct `curl` or `terminal` commands with a browser User-Agent header.
- **Multiple ACPs**: The same acronym can mean different things in different contexts (e.g., ACP = Agent Client Protocol vs Agent Control Plane vs Agent Context Protocol). Always verify which meaning applies.
- **Comparison page expansion**: When adding a 4th system to a 3-way comparison, update the title, verdict, all matrix rows, strengths section, architecture diagram, and decision guide — not just the matrix.
- **Analytical framing**: When the user provides analytical context (e.g., "this relates to our OpenClaw discussion"), capture it as a "Strategic Significance" section, not just factual content.

## Example Session

User: "Devin Desktopについて深く理解しwikiに取り込んで。[URLs] 特にagent-neutralな点が興味深い。我々のwikiでもACPを通じたagent orchestratorとしてのOpenClawの可能性について議論してきた。"

```
# Parallel fetch (3 subagents) + wiki search (simultaneous)
delegate_task → fetch devin.ai/download, blog post, ACP docs
search_files → existing Devin, ACP, Windsurf content
read_file → entities/devin.md, entities/cognition.md, comparisons/harness-backend-routing.md

# Raw article
write_file → raw/articles/2026-06-03_devin-desktop-windsurf-rebrand-acp-agent-neutral.md

# Enrich entity
patch → entities/devin.md (add Devin Desktop section with ACP integration)
patch → entities/cognition.md (add cross-reference)

# Create missing concept
write_file → concepts/agent-client-protocol.md (was in index but didn't exist)

# Update comparison
patch → comparisons/harness-backend-routing.md (add Devin Desktop as 4th system)
  - Title update
  - Verdict update
  - Matrix: add column
  - Strengths: add section
  - Architecture: 3-layer → 4-layer
  - Decision guide: add entry
  - Sources: add URLs

# Index + log + commit
patch → index.md (update 4 entries)
patch → log.md (prepend entry)
git add + commit + push
```
