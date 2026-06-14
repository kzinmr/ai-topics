# Post-Relocation Enrichment Pattern

Pattern for enriching relocated pages with content from past sessions and splitting focused content into new concept pages.

## Context

After relocating a page (e.g., `death-of-browser/_index.md` → `browser-agent/death-of-browser.md`), the user may want to:
1. **Enrich** the relocated page with related content from past sessions
2. **Split** enriched content into focused concept pages

## Pattern 1: Enriching from Past Sessions

### Step 1: Find Related Content via session_search
```python
session_search(query="o3 deep research system cards browser agent", limit=5)
# Returns: session IDs with matching content
```

### Step 2: Scroll to Relevant Context
```python
session_search(session_id="<found_session_id>", around_message_id=<match_id>, window=10)
# Retrieves: detailed content from past session
```

### Step 3: Add Context to Relocated Page
- Add new technical approaches, player entries, or comparison rows
- Update Key Player Map if applicable
- Add links to related concept pages (e.g., `[[concepts/gpt/gpt-deep-research-system-card]]`)

## Pattern 2: Splitting into Focused Concept Pages

When a page grows too large or covers multiple distinct topics:

### Step 1: Create New Focused Page
```bash
# Create new page with focused content
write_file(path="~/wiki/concepts/browser-agent/deep-research.md", content="...")
```

### Step 2: Add Cross-Reference from Parent
```python
# In parent page, add link to new focused page
patch(mode="replace", path="...", 
      old_string="**Key insight**: Deep Research represents...",
      new_string="**Key insight**: Deep Research represents...\n\n→ See [[concepts/browser-agent/deep-research]] for detailed analysis.")
```

### Step 3: Register in index.md
```python
# Add new page entry after parent page entry in index.md
patch(mode="replace", path="~/wiki/index.md",
      old_string="- [[concepts/browser-agent/death-of-browser|...",
      new_string="- [[concepts/browser-agent/death-of-browser|...\n- [[concepts/browser-agent/deep-research|...")
```

### Step 4: Log All Operations
```markdown
## [YYYY-MM-DD] Post-relocation enrichment and page splitting
**Action**: Enriched relocated page with content from past session. Split enriched content into new concept page.
**Updated pages**:
- `concepts/browser-agent/death-of-browser.md` — Added Deep Research context
- `concepts/browser-agent/deep-research.md` — New concept page
- `index.md` — New page registered
```

## Real Example: Deep Research Split

### Context
- **Parent page**: `browser-agent/death-of-browser.md` (browser agent trends)
- **New page**: `browser-agent/deep-research.md` (Deep Research as agentic browsing pattern)
- **Source**: Content from past session about Deep Research System Card

### Execution
1. Found `gpt-deep-research-system-card.md` content via session_search
2. Added "Agentic Browsing Loop (Research-First)" to death-of-browser.md
3. User suggested splitting into focused page
4. Created `browser-agent/deep-research.md` with detailed analysis
5. Added cross-reference from parent page
6. Registered in index.md

### Result
- Two complementary pages with different focus:
  - `death-of-browser.md`: Browser agent trends and technical approaches
  - `deep-research.md`: Deep Research as agentic browsing pattern
- Cross-references enable navigation between related concepts

## Key Insights

1. **session_search is powerful**: Use it to find related content from past sessions for enrichment
2. **Split when focused**: When a page covers multiple distinct topics, split into focused pages
3. **Cross-reference always**: Add bidirectional links between related pages
4. **Log everything**: Record all operations in log.md before committing
