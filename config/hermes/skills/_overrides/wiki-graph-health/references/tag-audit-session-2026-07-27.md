# Tag Audit Session — 2026-07-27

## Key Learnings

### 1. Normalization Script Scope Gap (Fixed)
`tag_normalization.py` historically only scanned `entities/`, `concepts/`, `comparisons/`. Tags in `events/` and `queries/` were untouched by normalization, causing persistent violations like `wiki-maintenance`, `graph-analysis`, and `acquisition`.

**Fix applied 2026-07-27**: Added `events` and `queries` to the `root_dir` list in the script's `main()` function.

**Pre-flight check**: Before running normalization, verify the scan scope matches your needs:
```python
for root_dir in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
```

### 2. SCHEMA.md `... [truncated]` Corruption Pattern

**Symptom**: Tag audit reports `ai-critic` as not in taxonomy even though `grep 'ai-critic' wiki/SCHEMA.md` returns 1 match.

**Root cause**: The actual file line contains `ai-critic... [truncated]` — a literal `... [truncated]` string baked into the file from a previous read_file truncation artifact. The tag parser extracts `ai-critic... [truncated]` which doesn't match `ai-critic`.

**Detection**:
```bash
grep -n '\.\.\. \[truncated\]' wiki/SCHEMA.md
```
Also check other wiki metadata files (index.md, pages with long frontmatter lines).

**Fix**: Remove the `... [truncated]` text from the affected line. The preceding content is intact — the truncation is an artifact from an earlier `read_file` output being written back to the file.

**Verification**: Re-run `tag_audit.py` — the previously-failing tag should now parse correctly.

### 3. One-Off Deletion from Inline-Format Tags

The normalization script only MAPS tags to canonicals (via TAG_NORMALIZATION). It does NOT delete tags. To remove a one-off tag that has no canonical mapping:

**For block format** (`  - badtag`): Use `patch` with a unique anchor line from below.
**For inline format** (`tags: [tag1, badtag, tag3]`): The normalization script converts inline to block format on any modification. After normalization, delete the surviving one-off tag from the block-format output manually.

### 4. Pre-Commit Hook Passed Without --no-verify

After the tag audit + normalization cycle, the pre-commit hook passed on its own (178 files, all tags validated). This is the expected healthy pipeline behavior — the `--no-verify` bypass should only be needed when normalization mappings are incomplete.
