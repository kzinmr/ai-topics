# Subagent Content Quality Guardrails

When delegating wiki-enrichment tasks to parallel subagents, the single most common failure pattern is **content quality in index.md and frontmatter** — not logic errors. Subagents copy `read_file` display formatting, use the wrong tag pluralization, or introduce CJK characters. This reference provides copy-pasteable context blocks to prevent all three.

## Context Injection Template

Include this block verbatim in each subagent's `context` field when they are creating/editing wiki pages and index.md:

```
## CRITICAL CONTENT QUALITY RULES — READ CAREFULLY

### 1. index.md list format
The index.md uses `- ` (hyphen-space) as list-item prefixes. Do NOT copy read_file display format.
- CORRECT: `- [[entities/foo]] — description`
- WRONG: `|- [[entities/foo]] — description`  (pipe-hyphen from read_file)
- WRONG: `||- [[entities/foo]] — description` (double-pipe from read_file)

When inserting a new entry into index.md, find the adjacent lines and use `- ` prefix. After inserting, verify by re-reading the lines.

### 2. Tag taxonomy — exact case and number
Tags MUST match SCHEMA.md exactly. Common pluralization traps:
- SCHEMA has `open-weight` (singular). Do NOT write `open-weights` (plural).
- SCHEMA has `person` (singular). Do NOT write `people`.
- SCHEMA has `organization` not `org`.
- SCHEMA has `blog` not `blogs`.
- Always run `grep -i "<tag>" /opt/data/ai-topics/wiki/SCHEMA.md` before using a tag.

### 3. No CJK characters in wiki pages
The pre-commit hook blocks ANY Chinese/Japanese/Korean characters in non-raw/ files.
Even proper nouns (company names, person names) are blocked.
- CORRECT: `Z.ai (Zhipu AI)` — use Latin transcription
- WRONG: `Z.ai (智谱AI)` — CJK characters block commit
- Any kanji, hanzi, hiragana, katakana in entities/, concepts/, comparisons/, queries/, events/, index.md, log.md will be rejected.

### 4. Use patch, never write_file on pages >40 lines
Read the existing page first. If it has >40 lines, use patch to add content.
Only use write_file for NEW pages or pages <40 lines.

### 5. Wikilink format
Use [[entities/slug]] or [[concepts/slug]].
NOT [[Entity(name)]] or similar non-standard formats.
Verify each target exists before linking.
```

## Parent-Side Instruction Pitfall: Tag Instructions to Subagents

When writing subagent `context` fields that include instructions to add/modify tags in frontmatter, the parent agent must specify **canonical SCHEMA.md tags only** — never page paths, slugs, or freeform strings.

**WRONG** (this session, Aug 2026):
```
Add `concepts/prime-agent` tag
```
Result: subagent literally adds `concepts/prime-agent` as a YAML tag → pre-commit blocks commit with "TAGS NOT IN SCHEMA.md TAXONOMY."

**CORRECT**:
```
Add `coding-agents` tag (this is the canonical SCHEMA.md tag covering this concept)
```
The parent agent must check SCHEMA.md before formulating the instruction: `grep -i "keyword" /opt/data/ai-topics/wiki/SCHEMA.md`

**Why this happens**: The parent agent is thinking about page relationships (wikilinks) and accidentally uses page-path notation in tag instructions. Tags serve a different purpose than wikilinks — they're categorical metadata, not page pointers. The `related:` frontmatter field is the correct place for page-path references.

**Detection**: If a commit is blocked with a tag violation like `concepts/some-name`, the fix is usually replacing the page-path tag with a canonical category tag (e.g., `concepts/prime-agent` → `coding-agents` or `open-source`).

## Post-Subagent Verification Checklist

After all parallel subagents complete, ALWAYS run these checks before attempting `git commit`:

### 1. Pipe-prefix scan in index.md
```bash
grep -n '^|- \[' /opt/data/ai-topics/wiki/index.md
```
If any matches, fix with patch: remove the leading `|` from each line.

### 2. Tag validation against SCHEMA.md
```bash
grep -rh "^tags:" /opt/data/ai-topics/wiki/entities/*.md /opt/data/ai-topics/wiki/concepts/*.md 2>/dev/null | \
  perl -pe 's/tags:\s*\[(.*?)\]/\1/g; s/tags:\s*//g; s/\s+-\s+/\n/g; s/,\s*/\n/g' | \
  grep -v '^$' | sort -u | while read tag; do
  if ! grep -q "$tag" /opt/data/ai-topics/wiki/SCHEMA.md; then
    echo "UNKNOWN TAG: $tag"
  fi
done
```

### 3. CJK character scan
```bash
python3 -c "
import re, glob
paths = ['index.md', 'log.md'] + \
  glob.glob('entities/*.md') + \
  glob.glob('concepts/*.md') + \
  glob.glob('concepts/**/*.md', recursive=True)
for fname in paths:
    try:
        with open(fname) as f: lines = f.readlines()
        for i, line in enumerate(lines, 1):
            if re.search(r'[\u3000-\u9FFF\uF900-\uFAFF\u3040-\u309F]', line):
                print(f'CJK: {fname}:L{i}')
    except FileNotFoundError: pass
"
```

### 4. Staged diff check
```bash
git diff --staged | grep -E '^\+.*\|\- ' | head -5
```
