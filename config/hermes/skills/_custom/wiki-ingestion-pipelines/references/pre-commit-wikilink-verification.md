# Pre-commit wikilink verification (blog-ingest cron, 2026-10-30)

`.githooks/pre-commit` validates `index.md` and the tag taxonomy, but **does NOT check
that `[[wikilinks]]` resolve**. A page full of links to nonexistent pages commits
clean. Verify links yourself before `git add wiki/`.

## The check

Run from `wiki/` over only the files you touched:

```bash
cd /opt/data/ai-topics/wiki && for f in entities/x.md concepts/y.md; do
  grep -o "\[\[[^]|]*" "$f" | sed 's/\[\[//' | sort -u | while read l; do
    [ -f "$l.md" ] || echo "DANGLING in $f: $l"
  done
done
```

`[^]|]*` stops at the first `|`, so `[[target|display]]` yields `target`.

## Filtering the noise (critical — otherwise you chase ghosts)

Raw output is dominated by **false positives**. Four categories are pre-existing or
structural and must NOT be "fixed":

1. **Directory links.** `[[concepts/context-engineering]]` and `[[concepts/claude-code]]`
   resolve to *directories* containing `index.md`, not `foo.md`. Test
   `ls -d concepts/foo` before calling it dangling.
2. **Section anchors.** `[[concepts/synthid#C2PA Limitations]]` — strip at `#` and check
   only the file part.
3. **Same-page anchors.** `[[#Software Is Slow Because of Bad Design]]` — starts with
   `#`, always a local heading reference, never a file.
4. **Pre-existing breakage from other pipelines.** Check the file's `git diff` — if *you*
   did not add the line, it is not yours to fix. Repairing unrelated dangling links in a
   rich page risks clobbering a sibling writer's work.

Practical filter: `[ -f "$l.md" ] || [ -d "${l%%#*}" ] || echo "CHECK: $l"`, then confirm
each survivor appears on a `+` line in your own diff.

## What this caught (2026-10-30)

Four genuinely bad links, all invented from plausible-sounding memory rather than checked
against the tree:

| Written | Reality |
|---|---|
| `concepts/ai-mathematical-discovery` | `concepts/ai-mathematics-theorem-proving` |
| `concepts/effort-control` | `concepts/claude/effort-control` (nested dir) |
| `concepts/chain-of-thought-monitoring` | `concepts/chain-of-thought` |
| `concepts/emergent-abilities` | does not exist — nearest are `concepts/scaling-hypothesis` / `concepts/scaling-laws` |

**Lesson:** every `[[link]]` you type should come from a directory listing you just read,
not recall. When a link fails, `ls concepts/ | grep -i <keyword>` before deciding whether
to rename or drop it. Dropping is correct when no near neighbour exists — a dangling link
is worse than none, because it renders as a broken placeholder and misleads later ingest
runs into thinking the page is merely pending.

## Also verify raw-article citations

Pages cite sources two ways — `[[raw/articles/<file>.md]]` wikilinks and `sources:`
frontmatter entries. Both silently accept a mistyped filename:

```bash
cd /opt/data/ai-topics && git show --stat HEAD | grep raw/articles/
```

Saved-article filenames are long and hash-suffixed
(`simonwillison.net--2026-oct-29-how-i-built-the-most-ai-pilled-company-in-the-wo--a0c59133.md`).
The 60-char path truncation means the filename frequently does **not** match what the
title suggests, so never reconstruct it from memory — copy it from the checkpoint's
`saved_articles[].raw_path` or from `ls`.

## Ordering

Run this **before** `git add wiki/`. Fixing links post-commit needs a second commit, and
if a sibling writer has since touched the same page the fix can collide.

## Companion: log.md prepend traps (moved here from SKILL.md, which is at its 100k cap)

If you also wrote a log entry this session, verify the header survived. Three rules,
expanded in `log-prepend-header-repair.md` and `log-prepend-no-header-variant.md`:

- **Never assert `content.count("# Wiki Log") == 1`.** It false-fires on quoted history
  inside log *entry bodies* (recovery notes literally quote the header). Use the
  structural check: `lines[0] == "# Wiki Log"` plus a substring check for your own entry.
- **The header block is not stable across pipelines** — some write a bare `# Wiki Log`
  with no italic blurb. Locate the boundary with
  `next(k for k, l in enumerate(lines) if l == "# Wiki Log")` rather than slicing past a
  hardcoded three-line constant, which is how duplicate headers and swallowed entries get
  produced.
- **Assert before mutating, and require a pure insertion after.** `assert
  lines[0].startswith('## [')` before you write turns a silent sibling-cron clobber into a
  loud stop. After repairing, `git diff --stat wiki/log.md` must report N insertions and
  **0 deletions**; any deletions mean you dropped entries — restore with
  `git show HEAD:wiki/log.md` and redo. Do the whole repair in ONE script; chaining two
  mutating log scripts is what produced the 4002→3988-line data loss recorded in
  `log-prepend-header-repair.md`.

## Note on the 100,000-char SKILL.md cap

`wiki-ingestion-pipelines/SKILL.md` is at ~100k and **rejects any edit whose resulting
size exceeds 100,000 chars** — including pure additions. Failed attempts report the
resulting size, so you can read the overflow off the error and shrink accordingly. To add
content: write it as a `references/*.md` file (no cap) and either point to it tersely from
SKILL.md or fold it into an existing reference. If SKILL.md genuinely must grow, a
verbose passage elsewhere has to be condensed into a reference first.

