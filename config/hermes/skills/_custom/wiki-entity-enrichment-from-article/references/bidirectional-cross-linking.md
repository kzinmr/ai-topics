# Bidirectional Cross-Linking for Concept Pages

## When to Apply

When creating a **concept page** that relates to existing sibling concepts in the wiki (e.g., MemEx relating to PTC and RLM, or a new RL algorithm relating to GRPO and RLHF), the new page is not complete until **bidirectional links** are established.

## The Pattern

### Step 1: Create the new concept page with outward links
Standard procedure — the new page links to related pages via `[[wikilinks]]` in body text and `related:` in frontmatter.

### Step 2: Update sibling pages with backlinks (REQUIRED, not optional)
For each closely-related existing page, add a reference to the new page:

1. **See Also / Related Concepts section** — add a one-line entry with a brief description of the relationship
2. **Landscape/comparison tables** — if the sibling page has a table comparing systems/paradigms (e.g., "Current Landscape", "Plan-then-Execute Landscape"), add the new entry

### Step 3: Verify index.md entry
The new page must appear in `index.md`. If the page fits alphabetically between two existing entries, insert it there.

## Relationship Description Patterns

The backlink description should explain **why** the new page relates, not just that it exists:

| Relationship Type | Example Description |
|-------------------|---------------------|
| Generalization | "MemEx generalizes RLM's `spawn_agent()` as a first-class parallel primitive" |
| Production variant | "PTC is Anthropic's production variant of code-as-action" |
| Same substrate, different axis | "RLM: same substrate (code execution), different problem (context management)" |
| Extension | "MemEx extends CodeAct with persistent scope, typed returns, sub-agents" |
| Complementary | "PTC (Function axis) + RLM (Data axis) are complementary" |

## Example: MemEx Ingestion (2026-06-12)

When creating `concepts/memex-scratchpad.md`:
1. New page linked to: CodeAct, PTC, RLM, dspy-rlm, context-management, Databricks
2. Updated `concepts/coding-agents/codeact.md` — added MemEx to Current Landscape table
3. Updated `concepts/programmatic-tool-calling.md` — added MemEx to See Also
4. Updated `concepts/rlm-recursive-language-models.md` — added MemEx to Related Concepts
5. Updated `concepts/dspy-rlm.md` — added MemEx to See Also

User explicitly requested: "ptcやrlmとも関連付けて" (also relate to PTC and RLM). This confirms bidirectional cross-linking is expected behavior, not optional.

## Comparative Analysis Sections

When a new concept sits in a **family of related paradigms** (code-as-action family, memory systems, RL algorithms), add a dedicated comparison section:

### 2-Axis Framework Pattern
If an existing framework already defines axes of comparison (e.g., PTC = Function axis, RLM = Data axis), position the new concept relative to those axes:

```markdown
## X × Y × NewConcept: Three-Way Relationship

### The Two Axes (established framework)
| Axis | Paradigm | What It Does | Core Problem |
|------|----------|-------------|--------------|
| Axis 1 | Existing A | ... | ... |
| Axis 2 | Existing B | ... | ... |

### Where NewConcept Sits
NewConcept operates on **both axes simultaneously**:
[ASCII diagram showing position]

### Capability Matrix
| Capability | A | B | NewConcept |
|------------|---|---|------------|
| ... | ✅/❌ | ✅/❌ | ✅/❌ |
```

This pattern is more valuable than prose descriptions because it lets readers immediately understand the new concept's position in the design space.

## Pitfalls

- **One-directional links are incomplete**: Creating a concept page that links to CodeAct but not updating CodeAct to mention the new page leaves orphaned references
- **Don't just add to Related Pages**: The relationship description should explain WHY, not just link
- **Update tables too**: If a sibling page has comparison tables (landscape, capability matrix), add the new entry there — not just in See Also
- **Don't wait for the user to ask**: Proactive cross-linking is the default; the user having to ask "also relate to X" means you missed a step
