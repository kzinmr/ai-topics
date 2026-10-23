# Alphabetical Drift in index.md — Why "Sort by Slug" Breaks

> **Load this BEFORE any batch index.md insertion.** Referenced from
> `references/orphan-index-insertion.md` and `SKILL.md` Section A4c Approach B.

Discovered 2026-10-19 (`wiki-health-fix` run). The main `SKILL.md` Section A4c and
`references/orphan-index-insertion.md` both tell you to insert by **slug string
comparison**. In the real index.md that produces **misplaced entries**.

## The failure mode

The Entities section has drifted out of alphabetical order — accumulated from later
pipeline runs appending entries at the wrong place. Observed live:

```
- [[entities/aaron-rosenthal]] — ...
- [[entities/abridge]] — Abridge — AI-powered medical conversation summarization
- [[entities/jan-leike]] — Jan Leike — Anthropic co-lead of agentic safety ...
- [[entities/adam-mastroianni]] — Adam Mastroianni — ...
- [[entities/adam-rosenthal]] — Redirect: ...
```

`jan-leike` sits between `abridge` and `adam-mastroianni`. Alphabetically it belongs
much later. This is **not corruption** — `validate_index.py` passes, the section
renders, nothing is broken. It is accumulated insertion drift, and it is the
status quo you must insert *into*.

**What "first slug > target" does**: it stops at the FIRST line whose slug sorts
after the target. Inserting `indra-ocr-agent` stops at `jan-leike` (`j` > `i`) →
entry lands at line 17 in the `a*` neighbourhood. **Wrong.**

**What "last slug <= target, then stop on first >" does**: same thing, wrong
neighbourhood, because the scan terminates on the out-of-order line before it
reaches the real `i*` cluster.

Both naive approaches put `indra-ocr-agent` and `apple-onnx-mlx-modelscope` after
`abridge`, hundreds of lines away from their true alphabetical homes. This is exactly
what happened on the first attempt of the 2026-10-19 run — it was reverted.

## The fix: physical-position insertion, not slug-sort

Anchor on file position, treating drift as fact:

```python
def slug_of(line):
    m = re.match(r'^\|?-\s+\[\[(?:entities|concepts|comparisons|events|queries)/([^\]|]+)', line)
    return m.group(1) if m else None

def last_le(lines, lo, hi, slug):
    """Last physical index in [lo+1, hi) whose slug <= target, scanning until the
    first entry that sorts AFTER target. Drift-tolerant in the sense that matters:
    the anchor is what a reader of this section actually sees."""
    prev = None
    for i in range(lo + 1, hi):
        s = slug_of(lines[i])
        if s is None:
            continue
        if s <= slug:
            prev = i
        else:
            break
    return prev
```

Insert bottom-up (reverse sort planned ops by index) so earlier inserts don't shift
later anchors.

## Do NOT merge-sort rebuild the Entities section

`references/orphan-index-insertion.md` recommends, as "preferred for cron mode",
reading all section entries, sorting by slug, and rebuilding the whole section.

**For Concepts that's fine. For Entities it is destructive**: it silently reorders
~950 lines, moving entries like `jan-leike` hundreds of lines down. A 3-entry
insertion becomes a ~1,900-line diff, which:
- makes the change unauditable,
- risks clobbering a concurrent pipeline's insertion,
- risks tripping the pre-commit rich-page shrink detector,
- and buries the 3 lines anyone actually reviews.

| Section | Drift observed | Merge-sort rebuild? |
|---|---|---|
| Concepts | low | OK |
| Entities | **high** (`jan-leike` case) | **NO — physical-position insertion** |
| Comparisons / Events / Queries | small, low | OK |

If you genuinely want to re-sort Entities, that is its own dedicated, separately
committed change — never smuggled into an orphan-registration commit.

## Mandatory backup + diff-verify for batch index writes

Batch insertion rewrites index.md via `open('w')`, not `patch`, so there is no
built-in safety net:

```bash
cd ~/ai-topics
cp wiki/index.md /tmp/index.bak      # BEFORE the script
python3 /tmp/orphan_reg.py
python3 scripts/validate_index.py    # must exit 0
git diff wiki/index.md               # EYEBALL IT — this is the real check
```

`validate_index.py` does **not** catch misplacement — it checks structural corruption
(pipe prefixes, baked-in numbers, truncation artifacts) and passes happily on 7
entries in the wrong neighbourhood. If the diff shows lines landing away from their
visible neighbours, restore and redo:

```bash
cp /tmp/index.bak wiki/index.md && python3 /tmp/orphan_reg_v2.py
```

Rewriting the script (v2) beats hand-patching v1's output back into shape.

## Verifying an insertion happened (grep gotcha)

Namespace-prefixed patterns give **false zeros** under BRE:

```bash
grep -c "\[\[concepts/aauth" wiki/index.md   # 0  ← WRONG, looks like it failed
grep -c "aauth" wiki/index.md                # 1  ← correct
```

The stored wikilink is `[[concepts/aauth]]`; the leading `[[` needs escaping. Safer:
use `grep -F`, or treat the `git diff` output as the source of truth.

Related: `git status --porcelain --cached` is **not a valid git invocation**
(`--cached` is a `git diff` flag, not a `git status` flag). To list staged files:

```bash
git diff --name-only --cached
```

## Header recount: compute, never increment

Recount section headers from actual line counts rather than adding the insertion
count — the declared numbers drift independently:

```python
n = sum(1 for l in section_lines if re.match(r'^\|?-\s+\[\[entities/', l))
```

2026-10-19: Entities declared 946 (recounted 952), Concepts declared 2207 (recounted
2211) — both headers were already stale *before* this run's 7 additions. Also refresh
`> Total pages:` and `> Last updated:` in the same write.

## Digest orphan claims still need live verification

The pre-run digest reported 9 orphans; filesystem verification found 7 real gaps and
2 false positives (`concepts/gpt/_archive/*` — archived, intentionally unindexed).
Standard rule, reconfirmed: never act on digest orphan counts without an
`os.path.exists` check per slug.

## Report-only classes seen this run (do not auto-fix)

- **`queries/` run-snapshot notes without frontmatter** — `2026-10-04-uncommitted-wip-snapshot.md`
  (244 KB), `2026-10-11-uncommitted-wip-snapshot.md`, `2026-10-17-skeleton-enrich-empty.md`,
  `wiki-graph-analysis-weekly-2026-08-28-annotations.md`. These are auto-generated
  pipeline run notes, not durable knowledge pages. Adding frontmatter to a 244 KB
  dump is churn; flag for deletion or relocation instead.
- **Empty-wikilink residual ~278** — matches the known stable count (~279, 0 fixable,
  see `watchdog-session-2026-08-13`). Do not chase.
