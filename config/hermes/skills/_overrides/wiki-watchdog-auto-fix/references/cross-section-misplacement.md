# Cross-Section Misplacement in index.md

## What Happens

Entries from one namespace (e.g., `concepts/`) appear under a different section header in `index.md` (e.g., `## Entities`). Unlike the Concepts→Events spill (where entries physically sit between the Events block and Comparisons header due to the non-standard section ordering), cross-section misplacement happens because batch orphan-insertion scripts sort entries **globally** without checking which section they belong in.

## Root Cause

The index has independently sorted sections:

```
## Entities (834 pages)
- [[entities/aakash-gupta]]    ← correct
- [[concepts/ai-benchmarks/lighteval]]  ← WRONG: concept entry in Entities section!
- [[entities/apertus]]          ← correct
```

When a batch-insertion script processes orphan concept pages and inserts them alphabetically across the entire document without pausing at section boundaries, concept entries like `concepts/ai-benchmarks/lighteval` land in the Entities section because they sort between `entities/aakash-gupta` (a) and `entities/apertus` (a).

This is caused by the **alphabetic sorting ignoring namespace prefixes** — `concepts/ai-benchmarks/` sorts before `entities/apertus`.

## Detection

```bash
cd ~/ai-topics

# Concept entries in Entities section
concepts_in_entities=$(sed -n '/^## Entities/,/^## Concepts/p' wiki/index.md | grep -cP '^- \[\[concepts/' || echo "0")
echo "Concept entries in Entities section: $concepts_in_entities"

# Entity entries in Concepts section
entities_in_concepts=$(sed -n '/^## Concepts/,/^## Events/p' wiki/index.md | grep -cP '^- \[\[entities/' || echo "0")
echo "Entity entries in Concepts section: $entities_in_concepts"

# Event entries in Concepts section
events_in_concepts=$(sed -n '/^## Concepts/,/^## Events/p' wiki/index.md | grep -cP '^- \[\[events/' || echo "0")
echo "Event entries in Concepts section: $events_in_concepts"
```

Expected: all three counts should be 0.

## Severity Assessment

| Count | Severity | Action |
|-------|----------|--------|
| 1-5 | Low | Move manually with `patch()` |
| 5-50 | Medium | Batch operation via Python script |
| 50+ | High | Report for human review — large restructure needed |

## Root Cause Prevention

When writing batch-insertion scripts for orphans, the insertion loop must:

1. **Know which section to insert into** — read the current section header context
2. **Sort only within the correct section** — do not use global alphabetical merge
3. **Check the first character of the wikilink target** — `concepts/` entries belong under `## Concepts`, `entities/` under `## Entities`

Example guard (Python):

```python
section_map = {
    'entities/': '## Entities',
    'concepts/': '## Concepts',
    'events/': '## Events',
    'comparisons/': '## Comparisons',
    'queries/': '## Queries',
}

def get_target_section(wikilink_target: str) -> str:
    """Determine which section header a wikilink belongs under."""
    for prefix, section in section_map.items():
        if wikilink_target.startswith(prefix):
            return section
    return None
```

## Relationship to Concepts→Events Spill

The **Concepts→Events spill** (documented in `section-boundary-fix.md`) is a different defect caused by the non-standard index.md ordering where `## Concepts` header is immediately followed by `## Events` instead of by concept list items. That defect moves ~1,160 entries into the Events section.

**Cross-section misplacement** (this document) is smaller in scale (70 entries in this run) and caused by batch scripts lacking namespace-aware section targeting, not by the structural ordering quirk.

Both defects can coexist. Detection should check for both.
