# Tag Audit Session — 2026-08-03

## Key Learnings

### 1. Normalization Dry-Run ≠ Audit Violations (CRITICAL)

`tag_audit.py` reported **0 non-SCHEMA tags** (only 2 one-offs, deleted), yet
`tag_normalization.py --dry-run` listed **39 pages** "would modify". Root cause:
the `TAG_NORMALIZATION` dict contains mappings for tags that are ALREADY valid
SCHEMA.md taxonomy tags (present in the bold-category lines, not just backtick format):

| Source (valid SCHEMA tag) | Mapped to |
|---|---|
| `gpu` | `hardware` |
| `retrieval` | `rag` |
| `ai-safety` | `agent-safety` |
| `cybersecurity` | `security` |
| `mixture-of-experts` | `model` |
| `long-context` | `context-management` |
| `speculative-decoding` | `inference` |
| `mathematics` | `education` |
| `google-deepmind` | `google` |
| `chatgpt` | `openai` |

These are **preference rewrites, not violation fixes** — and several DEGRADE tag
specificity on a knowledge wiki (`mixture-of-experts`→`model`, `long-context`→
`context-management`, `mathematics`→`education` are all information loss). For a
violation-fix job (tag-audit-weekly), **skip normalization entirely when the audit
is clean**. Only run it when genuine non-SCHEMA multi-use tags need mapping.

### 2. Verification Technique — Per-Page Diff Simulation

Before deciding whether to run normalization, import the module and print the
actual per-page tag diffs (this revealed the true nature of the 39 dry-run pages):

```python
import importlib.util, os
spec = importlib.util.spec_from_file_location(
    "tn", "/opt/data/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/tag_normalization.py")
tn = importlib.util.module_from_spec(spec); spec.loader.exec_module(tn)
wiki = os.path.expanduser("~/wiki")
for root_dir in ['entities', 'concepts', 'comparisons', 'events', 'queries']:
    for root, dirs, files in os.walk(os.path.join(wiki, root_dir)):
        for f in files:
            if not f.endswith('.md'): continue
            content = open(os.path.join(root, f)).read()
            m = tn.re.match(r'^(---\n)(.*?)(\n---)', content, tn.re.DOTALL)
            if not m: continue
            tags = tn.extract_tags_from_frontmatter(m.group(2))
            if not tags: continue
            mapped = [tn.TAG_NORMALIZATION.get(t, t) for t in tags]
            if mapped != tags:
                diffs = [(a, b) for a, b in zip(tags, mapped) if a != b]
                print(os.path.relpath(os.path.join(root, f), wiki), diffs)
```

### 3. Verify Source Tags Against SCHEMA Bold-Category Lines

The audit parser is permissive: any lowercase token in a `- **Category**: ...`
line counts as valid — backtick-quoted format is NOT the only valid format.
`grep -c '\`gpu\`' wiki/SCHEMA.md` returns 0 even when `gpu` is a valid tag
(bold-line format). Use word-boundary grep instead:

```bash
grep -o "\b<tag>\b" wiki/SCHEMA.md   # >0 = valid tag → mapping is a preference rewrite, not a violation fix
```

### 4. Concurrent Job Sweeps Your log.md Entry

While the audit ran, `blog-triage` committed (`git add wiki/` + commit) and
**swept my prepended log.md entry into its own commit** (`00b3e5ba`). This is
safe — the entry lives in the repo. Verify, don't re-commit:

```bash
git log --oneline -- wiki/log.md        # find the commit that carries your entry
git show <hash>:wiki/log.md | head -20  # confirm your entry is present
```

Then commit only your own files with explicit pathspec:

```bash
git add wiki/queries/your-page.md
git commit -m "..." -- wiki/queries/your-page.md   # pathspec limits to your files only
git push
```

This avoids both (a) double-committing log.md and (b) sweeping other jobs'
staged/untracked files into your commit.

### 5. Log Header-Burial Byte Pattern

When restructuring a buried `# Wiki Log` header, the intro line is followed by
`\n` DIRECTLY (no blank line before the first entry). Searching for
`"# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n\n"` fails
with "header not found". Use the exact single-trailing-newline form:

```python
header = "# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n"
idx = content.find(header)
```

Also expect the file to be concurrently modified between read and write — if the
first prepend script errors or the structure looks different on re-read, re-read
the file and adjust before rewriting (the concurrent `blog-triage` entry landed
mid-operation and was captured correctly by the restructure).

### 6. Pre-Commit Hook Passed Without --no-verify

After fixing the 2 one-off tags, `git commit` passed the tag validator on its own
(1 file, all tags in SCHEMA). `--no-verify` was NOT needed. Consistent with the
2026-07-27 session — the hook passes when normalization mappings are complete and
no violations remain.

### 7. Category-Line Prefix Variant — `|- **Category**:` (2026-08-08)

SCHEMA.md category lines appear in TWO prefix forms: `- **Category**: ...` AND
`|- **Category**: ...` (e.g. the Meta line is `|- **Meta**: search, relevance, ...`).
An ad-hoc parser using `^- \*\*` silently misses the pipe-prefixed lines, falsely
reporting valid tags (`search`, `automation`) as "MISSING". Detection regex must
handle both: `^(?:-|\|-) \*\*.*?\*\*:` — or better, just call `scripts/tag_audit.py`,
which is authoritative. Quick-verify a suspected tag with word-boundary grep:

```bash
grep -o "\bsearch\b" wiki/SCHEMA.md | head -1   # >0 = valid, parser was at fault
```

### 8. Never Regex Whole File Bodies for Tag Violations (2026-08-08)

An ad-hoc scanner that mis-slices frontmatter (`c.split('---')[1]` on a page whose
frontmatter doesn't parse as expected) or scans body text produces THOUSANDS of
false "violations" from URLs, wikilinks, and prose. Observed: 7,901 false positives
vs 6 real violations from `tag_audit.py` in the same run. Rules:
- **Quantify drift only with `scripts/tag_audit.py`** — its counts are trustworthy.
- Ad-hoc Python is fine ONLY to LIST specific files matching a known frontmatter
  defect (e.g. misplaced tag-list), never to measure taxonomy compliance.
