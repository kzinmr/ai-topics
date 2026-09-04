# Index Dedup Variant: Bare Entry + Described Entry in Drifted Position

Session: 2026-08-10 wiki-watchdog-fix run.

## The Pattern

`grep -n '\[\[concepts/model-welfare\]\]' wiki/index.md` returned **2 hits**:

```
2211:- [[concepts/model-welfare]]                                    ← BARE, alphabetically-correct position
2835:- [[concepts/model-welfare]] — Model Welfare — Engineering ...  ← DESCRIBED, drifted position (after wheelhouse)
```

This is a genuine duplicate, but Section 9's naive "remove the second occurrence"
would DELETE the described entry and leave a bare entry with no summary — losing
the description that the drifted copy carried.

## The Fix (description-preserving)

1. **Patch the bare entry at the correct position** — add the description from the
   drifted entry:
   ```
   old: - [[concepts/model-welfare]]
   new: - [[concepts/model-welfare]] — Model Welfare — Engineering discipline for AI agent well-being: ...
   ```
   Use a 2-line anchor (the bare line + the next entry) to guarantee uniqueness when
   the bare line alone appears twice.
2. **Delete the drifted duplicate** with a 3-line anchor (one above + duplicate + one below).
3. Verify: `grep -c '\[\[concepts/model-welfare\]\]' wiki/index.md` == **1** and
   `python3 scripts/validate_index.py` exits 0.

Result: one described entry at the correct alphabetical spot; drift removed.

## Same-run pattern: coverage-gap registration

`concepts/modelcrafting` existed on disk (95-line page) but was absent from index.md.
Inserted at its alphabetical position (between `model-welfare` and
`modern-retrieval-toolkit`) with a one-line summary, using the surrounding entries as
the patch anchor. This is the A4c orphan-index-registration pattern applied to a
concept page.

## Verification trap: grep on shared action prefixes

After prepending a log entry, `grep -c 'watchdog | Auto-fix' wiki/log.md` returned **13**,
which looked like a duplicate-entry bug. It was not: dozens of historical watchdog
entries share the `watchdog | Auto-fix` prefix. Only matching the FULL title with date
confirmed the single new entry:

```bash
grep -c '^## \[2026-08-10\] watchdog | Auto-fix: index dedup' wiki/log.md   # == 1
```

**Rule**: to verify a log/index entry was added exactly once, grep the full
`^## \[YYYY-MM-DD\] <action> | <subject>` line, never the `<action> |` prefix alone.

## Headers in the same run

Entities header 889 vs 890 section entries; Concepts 1963 vs 1964 — both corrected to
the entry count per baseline §4b (authoritative = count of `- [[dir/slug]]` lines in
the section, not flat file count, not recursive count).

## Escalated (unchanged policy)

- 26 pages missing `created:` frontmatter field → human-directed batch (10+ files).
- 6 known entity duplicate pairs (samuel-colvin/samuelcolvin, lilian-weng/lilianweng,
  martin-fowler/martinfowler, eugene-yan/eugeneyan, giles-thomas/gilesthomas,
  deliberate-coder/deliberatecoder) → dedup merge needs human canonical-slug decision.
