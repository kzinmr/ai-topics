
# Wiki Comparison Page Update

## When to Use

When adding a new item (model, provider, tool) to an existing multi-section comparison page like `comparisons/llm-api-pricing.md`.

## Pre-Requisites

1. Read the FULL comparison page first (`read_file` without offset/limit) to understand all sections
2. Gather all pricing/spec data for the new item before editing
3. Check `concepts/` and `raw/articles/` for source data

## Workflow

### Step 1: Identify All Sections to Update

Multi-section comparison pages typically have:
- **Main table** (e.g., "Current Frontier Models") — add row with tier classification
- **Cache pricing section** — add cache read/write estimates if applicable
- **Batch pricing section** — add batch API pricing or mark "—" if unavailable
- **Tier analysis section** — add to appropriate tier with "Why it wins" column
- **Cost comparison section** — add to all workload tables (chat, code gen, etc.)
- **Key Trends** — add a trend if the new item represents a significant market shift
- **Legacy/older models** — only if displacing an existing model to legacy
- **Changelog** — always add entry
- **Related Pages** — add wikilink to the item's entity/concept page

### Step 2: Edit with Patch Tool

Use `patch` with mode `patch` for multi-file edits. Each hunk needs **unique context**.

### Step 3: Verify and Fix

After patching, `read_file` on the edited sections to verify:
- No duplicate YAML frontmatter fields
- Section numbering is consistent (### 1, ### 2, etc.)
- All tables have consistent column counts

### Step 4: Update Index and Log

- Update `wiki/index.md` description for the comparison page
- Append to `wiki/log.md` with action summary

### Step 5: Commit and Push

```bash
cd ~/ai-topics && git add wiki/ && git -c core.quotepath=false commit -m "wiki: <summary>" && git push
```

**⚠️ Shell variable trap**: If the commit message contains `$` (e.g., `$10/$50`), use single quotes or escape: `\$10/\$50`. Otherwise git interprets them as shell variables and shows `$0/$0`.

## Pitfalls

### 1. Duplicate Frontmatter Fields

When patching frontmatter `updated:` field, the old text may match a duplicate if the field already exists. **Always read lines 1-10 first** to check for duplicates before patching. If a duplicate exists, use `terminal` + `sed` to remove the extra line:

```bash
# Remove line 5 (the duplicate)
cd ~/ai-topics && sed -i '5d' wiki/comparisons/FILE.md
```

### 2. Non-Unique Patch Context

The `patch` tool fails if `old_string` matches multiple locations. For section headers that appear in multiple places (e.g., `### 3.`), include surrounding context lines to make the match unique. If that fails, use `terminal` + `sed` with line-specific commands:

```bash
# Fix section numbering
cd ~/ai-topics && sed -i 's/^### 3\. Cache Is/### 4. Cache Is/' wiki/comparisons/FILE.md
```

### 3. execute_code Blocked in Cron Contexts

`execute_code` is blocked when running as a cron job or background task. Use `terminal` + `sed`/`awk` for bulk edits that `patch` can't handle.

### 4. Section Numbering Cascade

When inserting a new section (e.g., Key Trends #2), renumber ALL subsequent sections. Missing the cascade creates duplicate numbers that break the document structure.

## Example: Adding a Model to LLM API Pricing

```yaml
Sections to update (8 total):
1. US Frontier table → new row with tier
2. Cache discount rates → new row
3. Cache read prices → new row
4. Anthropic cache break-even → new row
5. Batch pricing → new row (or — if unavailable)
6. Tier analysis → new row in appropriate tier
7. Cost comparison → rows in both Chat and Code Gen tables
8. Key Trends → new trend if significant market shift
```
