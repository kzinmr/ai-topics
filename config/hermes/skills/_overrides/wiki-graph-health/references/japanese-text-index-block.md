# Japanese Text in Index Entries — Pre-Commit Block

## Problem

The pre-commit hook blocks commits when Japanese characters are introduced to previously-clean wiki files. This blocks `index.md` changes when new entries reference Japanese-language page titles or descriptions.

**Symptom:**
```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW Japanese introduced to clean file: wiki/index.md
```

## Root Cause

Orphan pages with Japanese-language content (titles, descriptions, aliases) get added to index.md with their original Japanese text preserved in the description line:

```
- [[concepts/context-routing]] — Context Routing — クエリ別コンテキスト振り分け — Query-aware...
```

## Fix

Patch the index entry to use only the English portion of the description.

**Before:**
```markdown
- [[concepts/context-routing]] — Context Routing — クエリ別コンテキスト振り分け — Query-aware context routing strategies
- [[concepts/continual-learning]] — Continual Learning — 継続的学習 — Continuous improvement through web research
```

**After:**
```markdown
- [[concepts/context-routing]] — Context Routing — Query-aware context routing strategies
- [[concepts/continual-learning]] — Continual Learning — Continuous improvement through web research and feedback loops
```

## Prevention

When building index entries for orphan pages, check the page's `title:` frontmatter field for Japanese characters before constructing the description. If it has both JP and EN text, use only the English portion. Detection:

```bash
# Check for Japanese in the title field
grep -P '[\x{3000}-\x{9FFF}\x{F900}-\x{FAFF}]' ~/wiki/concepts/<slug>.md
```

## Patching

```bash
# Find the offending line
grep -nP '[\x{3000}-\x{9FFF}]' ~/wiki/index.md

# Patch to remove Japanese text
patch(
    old_string="- [[concepts/context-routing]] — Context Routing — クエリ別コンテキスト振り分け — Query-aware",
    new_string="- [[concepts/context-routing]] — Context Routing — Query-aware context routing strategies",
    path="~/wiki/index.md"
)
```

## Re-commit

After fixing all Japanese text in index entries:
```bash
git add wiki/index.md && git commit -m "..."
```
