# Section Boundary Corruption Fix

## What Happens

The `## Concepts` and `## Events` section headers in `index.md` drift so that ~1,160 concept entries are misplaced under the Events section. This was discovered on 2026-06-19 when the Concepts section showed only 11 entries while Events showed 1,170.

## Root Cause

Index.md has a non-standard structure:

```
## Concepts (NNNN pages)
                      ← empty! Header immediately followed by Events header
## Events (N pages)
- [[events/...]]      ← 11 event entries
- [[concepts/...]]    ← ~1,160 concept entries spilled here!
## Comparisons (31 pages)
```

The `## Concepts` header is immediately followed by `## Events` instead of by concept list items. This means any script using `content.find('\n## ', concepts_header_end)` to find the Concepts section boundary finds Events instead. The actual concept entries sit BETWEEN Events entries and the Comparisons section.

Any manual edit or script that shifts the Events header, event entries, or the concept block boundaries without awareness of this quirk can break the separation.

## Analysis from 2026-06-19 Session

The corrupted state was:
```
## Concepts (1736 pages): 11 entries     # Wrong! Should be ~1170+
## Events (11 pages): 1170 entries       # Wrong! Should be 11
## Comparisons (31 pages): 31 entries    # Correct
```

The 11 correctly-placed concept entries were under Concepts header. The ~1,159 remaining concept entries were inside the Events section, starting after the 11 event entries and their following blank lines.

## Fix Procedure

Use terminal() with a Python heredoc — DO NOT use patch() for this, as pipe characters in markdown content cause patch() to add `|` prefixes to every line.

```bash
cd ~/ai-topics && python3 << 'PYEOF'
import re

with open('wiki/index.md') as f:
    content = f.read()

# 1. Find document boundaries
before_concepts = content[:content.index('## Concepts')]

concepts_match = re.search(
    r'(## Concepts.*?\n)(.*?)(?=\n## Events)', content, re.DOTALL
)
concepts_header = concepts_match.group(1)
concepts_initial = concepts_match.group(2).rstrip()  # 11 correct entries

events_match = re.search(
    r'(## Events.*?\n)(.*?)(?=\n## Comparisons)', content, re.DOTALL
)
events_header = events_match.group(1)
events_content = events_match.group(2)  # 11 event entries + blank lines + ~1159 concept entries

# 2. Find the boundary between event entries and spilled concept entries
lines = events_content.split('\n')
boundary = 0
for i, line in enumerate(lines):
    if line.strip().startswith('- [[concepts/'):
        # Find the last event entry before this concept line
        for j in range(i-1, -1, -1):
            if lines[j].strip():
                if lines[j].strip().startswith('- [[events/']):
                    boundary = i
                break
        if boundary == 0:
            boundary = i
        break

event_lines = lines[:boundary]
concept_spilled = lines[boundary:]

# 3. Clean trailing empty lines from event section
while event_lines and not event_lines[-1].strip():
    event_lines = event_lines[:-1]
event_lines.append('')  # one blank line before next section

# 4. Clean leading/trailing empty lines from spilled concept section
while concept_spilled and not concept_spilled[0].strip():
    concept_spilled = concept_spilled[1:]
while concept_spilled and not concept_spilled[-1].strip():
    concept_spilled = concept_spilled[:-1]

# 5. Rebuild the document
after_events = content[content.index('\n## Comparisons'):]

new_content = (
    before_concepts +
    concepts_header.rstrip('\n') + '\n' +
    concepts_initial + '\n\n' +
    '\n'.join(concept_spilled) + '\n\n' +
    events_header.rstrip('\n') + '\n' +
    '\n'.join(event_lines) +
    after_events
)

with open('wiki/index.md', 'w') as f:
    f.write(new_content)
print('✅ Section boundaries restored')
PYEOF
```

## Verification

After the fix, count entries per section:

```bash
cd ~/ai-topics && python3 << 'PYEOF'
import re
with open('wiki/index.md') as f:
    content = f.read()
sections = {}
for m in re.finditer(r'^## ([^\n]+)\n', content, re.MULTILINE):
    start = m.end()
    next_section = content.find('\n## ', start)
    if next_section == -1:
        next_section = len(content)
    section_text = content[start:next_section]
    entry_count = len(re.findall(r'^\s*-\s*\[\[', section_text, re.MULTILINE))
    sections[m.group(1)] = entry_count
for s, c in sections.items():
    print(f'{s}: {c}')
print(f'Total: {sum(sections.values())}')
PYEOF
```

Expected results:
- `## Concepts`: ~1170 entries (matching the restored count; ~546 more need separate index regeneration)
- `## Events`: 11 entries (matching 11 event files on disk)
- `## Comparisons`: 31 entries (no change)
- All entry counts from `find` counts on disk: pipe corruption 0, line prefix corruption 0

## Pitfalls

- **Pipe character corruption**: After any patch() that writes markdown list items, check for `|- `, `||- `, or `|---` artifacts. Fix with targeted sed as documented in the main SKILL.md.
- **Entry count verification**: The concept entry count after fix will be ~1170, not the full ~1716 on disk. The remaining ~546 are genuinely missing from index.md and need a separate batch-insertion pass (not a watchdog job).
- **Section header counts**: Update both the section header (`## Concepts (NNNN pages)`) and the summary line (`Total pages: NNNN | Concepts: NNNN`). The section header count reflects files on disk (not index entries), while the summary line's `Indexed entries` reflects index entries. They can differ.
- **The total indexed entries should not change** after this fix — only the distribution across sections changes.
