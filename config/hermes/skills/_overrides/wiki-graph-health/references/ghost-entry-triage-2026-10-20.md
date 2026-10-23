# Ghost Entry Triage & Frontmatter Backfill (wiki-health-fix run, 2026-10-20)

Session: `wiki-health-fix` cron. 7 ghost entries + 15 frontmatter gaps found, all fixed, pushed as `a32fde1f` (18 files), pre-commit validate_index + tag validator passed.

Companion to `watchdog-healthy-baseline.md` section 2 (ghost false positives) and section 5 (auto-fix thresholds). This file covers what to do with ghosts that ARE genuine.

## 1. The 4-way ghost triage - do NOT blanket-delete

The digest / `wiki_health.py` reports ghosts; the naive move is deleting every index line. Wrong in one of four cases, and that case is the expensive one.

Three cheap checks per ghost:

```bash
grep -rn "<slug>" wiki/ --include=*.md -l | grep -v 'wiki/index.md'   # inbound wikilink?
git log --oneline --all -- wiki/<path>                                  # ever a real file?
ls wiki/raw/articles/ | grep -i "<topic>"                               # source material?
```

| Case | Signal | Action |
|---|---|---|
| A. Never created, no inbound links, no source | all three empty | **Delete the index line** (6/7 in this run) |
| B. Never created but a live `[[wikilink]]` targets it | inbound link from a rich page | **CREATE the page** from the raw article - do NOT delete |
| C. Was a real file, deleted upstream | git log shows a deletion | Delete the index line |
| D. `_archive/` or `_index` path | path contains `_archive` | Skip - intentionally unindexed (false positive) |

**Case B is the trap.** Deleting the index line looks clean and silently strands a real cross-reference. Check inbound wikilinks BEFORE deleting anything.

Case B worked example (2026-10-20): `concepts/outer-harness` had no file, but `entities/third-moment-research.md` carried it in both `related:` frontmatter and body prose (`See [[concepts/outer-harness]]`). Raw sources existed (`raw/articles/2026-10-14_openai_third-moment-research-10000-agents.md`, `2026-05-08_anthropic-engineering_effective-harnesses-for-long-running-agents.md`) so a sourced concept page was written (inner-vs-outer harness comparison table, concrete Third Moment implementation, open questions, 3 See-Also links) rather than removing the entry.

This is the **only** exception to the section-5 "never auto-create" rule: creating a page to satisfy a ghost that a live wikilink targets is in scope for a health-fix run.

Case A removals this run: `entities/claude-haiku-5-5`, `entities/popcar`, `concepts/agentic-software-factory-hierarchy-of-needs`, `concepts/llm-decompilation-and-software-recovery`, `concepts/openai/gpt-5-6-codex-model-card-2026`, `queries/wiki-graph-analysis-weekly-2026-10-09`.

Note `wiki/queries/2026-10-11-uncommitted-wip-snapshot.md` *documented* these very ghosts - an earlier run noticed the missing pages and wrote a note instead of fixing them. Ghosts reported in a query page do not mean resolved; verify live.

## 2. Canonical ghost-detection snippet

```python
import os, re
wiki='wiki'
existing=set()
for r,d,fs in os.walk(wiki):
    for f in fs:
        if not f.endswith('.md'): continue
        rel=os.path.splitext(os.path.relpath(os.path.join(r,f),wiki))[0]
        existing.add(rel)
        if rel.endswith('/_index'): existing.add(rel.rsplit('/',1)[0])  # [[concepts/post-training]] is VALID when _index.md exists
idx=open('wiki/index.md').read()
links=set(re.findall(r'\[\[((?:entities|concepts|comparisons|queries|events)/[^\]\|#|]+)', idx))
print('GHOSTS', [l for l in links if l not in existing])
```

Two omissions that produce garbage: (a) dropping the `_index` line means every directory-style link reports missing; (b) using `os.path.splitext(f)[0]` on `os.walk` paths keeps the `wiki/` prefix while slugs are `entities/foo` - that gave 6,260 phantom refs / 0 real in a past run.

## 3. Header recount after ghost removal

Removing ghosts drops section counts by exactly the number removed. Recompute from **section entry lines**, not filesystem:

```python
import re
c=open('wiki/index.md').read()
for name,nxt,pre in [('## Entities','## Concepts','entities/'),('## Concepts','## Comparisons','concepts/'),
                     ('## Comparisons','## Events','comparisons/'),('## Events','## Queries','events/'),
                     ('## Queries','## RSS Scans','queries/')]:
    s=c.index(name); e=c.index(nxt,s)
    n=len(re.findall(r'^[-|]+\s+\[\['+re.escape(pre), c[s:e], re.M))
    print(c[s:c.index(chr(10),s)], 'actual=', n)
```

2026-10-20: Entities 952 to 950, Concepts 2217 to 2214, Queries 36 to 35 (then 37 after 2 orphan registrations).

Note the `^[-|]+\s+` - the entities/concepts sections mix `- ` and `|- ` prefixes. A regex anchored on `^- ` alone returns 0 for whole sections (observed: all five sections reported `actual=0` on the first attempt).

Always finish with a section-header integrity check (`c.count(s)==1` for each of Entities/Concepts/Comparisons/Events/Queries) - batch index edits can silently drop a header, and `validate_index.py` does NOT catch that.

## 4. Frontmatter gaps: what the population actually looks like

`os.walk` scan over entities/concepts/comparisons/queries/events, skipping `_index*` **and** `_archive/`. (For locating the closing delimiter use the line-based loop in `watchdog-healthy-baseline.md` section 7 item 6 - raw filenames contain `---`.)

2026-10-20 results and the fix per class:

| Class | Count | Fix |
|---|---|---|
| `redirect:` stubs missing `sources:` | 8 of 9 | `re.sub(r'^(redirect: .*)$', 'sources: []\n\1', c, count=1, flags=re.M)` - insert before `redirect:` to keep field order |
| `queries/` page missing `sources:` | 1 | insert before `confidence:` |
| `queries/<date>-*-snapshot.md` with NO frontmatter | 5 | prepend full block (see section 5) |
| entity missing `updated:` | 1 | insert after the `tags:` line |

`redirect:` stubs are the dominant `sources:`-gap population - they carry `title/type/created/updated/tags/redirect` and simply omit `sources:`. Deterministic fix, and the pre-commit validator accepts `sources: []`.

## 5. `queries/` run-snapshot pages - the recurring offender

`skeleton-enrich-daily` writes `queries/<date>-skeleton-enrich-empty.md` and `queries/<date>-uncommitted-wip-snapshot.md` as **bare `# heading` files**: no frontmatter, not in index.md. Every week they re-dirty both the frontmatter-gap metric and the orphan-index metric.

One-pass fix:

1. Prepend `title` / `type: query` / `created: <date parsed from filename>` / `updated: <today>` / `tags: [query, knowledge-management]` / `sources: []`.
2. Register in `## Queries`, then **sort the whole date-prefix block** - do not trust adjacent-line anchors, that section is already drifted:
   ```python
   i = next(n for n,l in enumerate(lines) if l.startswith('- [[queries/2026-10-05-authority'))
   j = next(n for n,l in enumerate(lines) if l.startswith('- [[queries/agent-capability-set-hyperbo'))
   block = lines[i:j]; block.sort(key=lambda l: l.split('[[queries/')[1]); lines[i:j] = block
   ```
3. Bump `## Queries (N pages)`.

**Durable fix for the curator (not yet done)**: change where `skeleton-enrich-daily` writes these, or make it emit frontmatter + self-index. Re-fixing them weekly is wasted health-run budget. Related open escalations from the same report: 6,629 unprocessed raw articles (mostly `xeiaso.net` CVE short-form notes, non-AI-core junk, `raw-backlog-ingest` is paused) and 2,944 stale pages (92% of the wiki - the 30-day rule likely needs redefining: metadata-touch age vs content age).

## 6. Tag gotchas hit while writing a new page (2026-10-20)

- `multi-agents` **fails** the pre-commit validator. Canonical: **`agent-orchestration`** (siblings `agent-swarms`, `agent-team-swarm`, `orchestration`, `subagents`).
- `concept` IS valid, but only via the SCHEMA **Core Types backtick line** (backtick-quoted `concept`, `entity`, `comparison`, `query`, `summary`, ...), not a bold category line. A parser reading only `- **Category**: ...` reports `concept` as unknown - grep the raw file for the backticked tag before adding anything to the taxonomy.
- `ai-agents`, `agent-harness`, `long-horizon`, `architecture`, `query`, `knowledge-management` all verified valid.
- Validate tags *before* writing the page: build the valid set from both parser branches, then assert each tag is in the set.

## 7. Report framing that worked

The digest claimed 2 orphans - both `concepts/gpt/_archive/*`, reported as false positives with no action. Digest stale/unprocessed numbers were reported as escalations, not fixed. The digest said **nothing** about frontmatter gaps or ghost entries - those were found only by independent `os.walk` scans. Confirms the standing rule: `wiki_health.py` output covers index corruption only; ghosts, frontmatter gaps, and index-to-filesystem gaps require your own scan.
