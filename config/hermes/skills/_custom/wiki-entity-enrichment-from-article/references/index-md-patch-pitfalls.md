# index.md Patch Pitfalls — Concepts Section

The Concepts section in `wiki/index.md` uses simple `- ` prefix format (no embedded line numbers), so in theory `patch` should work. In practice, it often doesn't.

## Pitfall 1: Patch Fails on Long Description Lines

**Symptom**: `patch` returns "Could not find a match for old_string" even though the text looks correct.

**Cause**: Concept entries often have very long description text (200–500+ chars). The byte-level matching is fragile — any difference in line wrapping, Unicode encoding, or truncation prevents `old_string` from matching. This happens even when `read_file` shows the text looks identical.

**Reproduction**: From 2026-05-26 session:
```
old_string = "- [[concepts/societal-shadow]] — Concept proposed by QC..."
```
Failed twice with "Could not find a match" despite the text visibly matching the file content. The `societal-shadow` description was ~600 chars long.

**Fix**: When `patch` fails twice on a concept entry, fall back to Python `list.insert()` immediately. The Concepts section doesn't need line renumbering (no embedded numbers), so a simple insert suffices:

```python
with open('/opt/data/wiki/index.md', 'r') as f:
    lines = f.readlines()

# Find insertion point by content
for i, line in enumerate(lines):
    if '[[concepts/societal-shadow]]' in line and not 'linguistic-vertigo' in line:
        insert_idx = i + 1
        break

new_line = '- [[concepts/new-concept]] — Description.\n'
lines.insert(insert_idx, new_line)

with open('/opt/data/wiki/index.md', 'w') as f:
    f.writelines(lines)
```

**Key**: Include a disambiguator in the match condition (e.g., `and not 'linguistic-vertigo' in line`) because concept descriptions often wikilink to other concepts, causing false matches.

## Pitfall 2: execute_code Partial-Write Hazard

**Symptom**: A Python script in `execute_code` modifies a file in-memory, crashes before writing, and leaves the file in an inconsistent state on disk — but the NEXT `execute_code` call sees the stale on-disk state and makes wrong assumptions.

**Cause**: The pattern `lines.pop(i)` → later computation → `open().writelines()` means if the later computation throws (e.g., TypeError from NoneType + int), the mutation is lost but the program state is dirty.

**Reproduction**: From 2026-05-26 session:
```python
lines.pop(i)  # Removed entry
# ... later ...
print(f"{concept_start+1}")  # TypeError: NoneType + int
# File was never written — entry still on disk
```
This caused a chain of 3 execute_code calls to fix the index: one to insert (wrong position), one to remove+revert (crashed, didn't write), one to fix properly.

**Fix**: Structure execute_code scripts with a strict ordering:
1. Read file
2. Compute ALL values (indices, counts, new lines)
3. Mutate list
4. Write immediately — NO computation between mutation and write
5. Print verification (separate read, no mutation)

```python
# ✅ Correct pattern
lines = open(path).readlines()

# Step 1-2: Compute everything
insert_idx = None
for i, line in enumerate(lines):
    if condition:
        insert_idx = i + 1
        break

if insert_idx is None:
    print("ERROR: target not found")
else:
    # Step 3: Mutate
    new_line = '...\n'
    lines.insert(insert_idx, new_line)
    
    # Step 4: Write immediately (no computation after this)
    with open(path, 'w') as f:
        f.writelines(lines)
    
    # Step 5: Verify (fresh read, no mutation)
    verify = open(path).readlines()
    print(f"Verified: {verify[insert_idx]}")
```

## Pitfall 3: Pre-Commit Tag Validator Blocks Commit

**Symptom**: `git commit` fails with "TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED" for a new custom tag not in SCHEMA.md.

**Fix**: Map the tag to an existing SCHEMA.md tag. Check `wiki/SCHEMA.md` for the nearest available tag with:
```bash
grep "economics\|industry\|business" ~/wiki/SCHEMA.md
```

Example: `software-economics` → `economics` (already in SCHEMA.md Meta category).
