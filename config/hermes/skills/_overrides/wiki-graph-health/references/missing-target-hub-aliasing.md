# Missing-Target → Hub/Canonical Aliasing (Pattern D, 2026-10-28 watchdog)

When the weekly graph report lists genuinely-missing high-reference targets
(observed: `agent-evaluation` 26 refs, `agent-memory` 16, `rag` 15), prefer
**aliasing to an existing page/hub** over creating stubs. Proven on 36 refs /
26 files in one pass (commits `34ffd503` + log `ebf69c60`).

## Decision rule

| Situation | Rewrite target | Example |
|---|---|---|
| Missing slug has a rich indexed synonym page | that page's slug | `[[concepts/rag]]` → `[[concepts/retrieval-augmented-generation]]` |
| Missing slug is a sub-topic of an existing hub **directory** (has `_index.md`) | the DIRECTORY SLUG | `[[concepts/agent-evaluation]]` → `[[concepts/evaluation]]`; `[[concepts/agent-memory]]` → `[[concepts/context-engineering]]` |
| No synonym, no hub | create `status: stub` (old Pattern C) | — |

Before deciding, check: `ls wiki/concepts/<dir>/_index.md` (hub exists → dir-link
is valid), `ls wiki/concepts/ | grep -i <keyword>` (synonym candidates), and
`grep -n '<slug>' wiki/index.md` (is a variant already indexed?).

## 🛑 CRITICAL pitfall: directory SLUG, never `_index.md` file path

A naive `str.replace('[[concepts/agent-evaluation]]', '[[wiki/concepts/evaluation/_index.md]]')`
produces file-path-style wikilinks that do NOT resolve. Correct form is the bare
directory slug `[[concepts/evaluation]]`. Recovery pass if already emitted:

```python
bad = {
 '[[wiki/concepts/evaluation/_index.md]]': '[[concepts/evaluation]]',
 '[[wiki/concepts/context-engineering/_index.md]]': '[[concepts/context-engineering]]',
 '[[concepts/evaluation/_index.md]]': '[[concepts/evaluation]]',
 '[[concepts/context-engineering/_index.md]]': '[[concepts/context-engineering]]',
}
# walk wiki/, os.walk, skip _archive/raw, replace all four variants
```

Note the two-layer trap: the first bad replace may have produced the
`wiki/...` prefix AND a later cleanup may reintroduce `[[concepts/<dir>/_index.md]]`
— handle both variants in the recovery dict.

## Rewrite walk template

```python
import os
hubs = {'concepts/agent-evaluation': 'concepts/evaluation',
        'concepts/agent-memory': 'concepts/context-engineering'}
for root, dirs, files in os.walk('wiki'):
    if '_archive' in root or 'raw' in root: continue
    for f in files:
        if not f.endswith('.md'): continue
        p = os.path.join(root, f)
        # skip historical artifacts — keep their broken links as records
        if 'wiki-graph-analysis-weekly' in p or 'uncommitted-wip-snapshot' in p: continue
        c = open(p).read(); new = c
        for slug, hub in hubs.items():
            new = new.replace(f'[[{slug}]]', f'[[{hub}]]')
            new = new.replace(f'[[{slug}|', f'[[{hub}|')   # preserve display text
        if new != c: open(p,'w').write(new)
```

Also handle links inside frontmatter `related:`-style quoted strings
(`"[[concepts/agent-memory]]"` in context-repositories.md) — plain replace covers them.

## Verification & commit hygiene

1. `grep -rn '\[\[concepts/<old>\]\]' wiki/entities wiki/concepts --include='*.md'` → 0 residual.
2. Spot-check a nested-page edit (`sed -n '88,95p'` on a Related section) to confirm
   links read `[[concepts/evaluation]]` not file paths.
3. Stage ONLY touched files: `git diff --name-only -- wiki/ > /tmp/stage.txt && xargs git add -- < /tmp/stage.txt`.
   The working tree often carries 50+ dirty WIP files from sibling pipelines
   (hot-post/trending/dreaming) — NEVER `git add wiki/` wholesale; the watchdog
   commits only its own files.
4. Pre-commit tag validator runs automatically; a pure wikilink rewrite always passes.

## Report-staleness rule

The daily watchdog receives the `wiki_graph_analysis` context from the weekly
Friday job — ages of 4-8 days are normal (observed 122.5 h). Do NOT bulk-execute
its "~352 auto-fixable" / "~200 nested-namespace" link lists against a stale
resolver. Trust only adjudicated HIGH items (missing-target aliasing, empty
`[[]]` strip — verify count with `grep -rn '\[\[\]\]'` first; it was already 0
by watchdog time) and defer bulk sweeps to the next weekly run, re-verifying
each target's existence on the filesystem first.

## Pipeline-chain alert triage (same session)

`blog chain ingest_ok_but_triage_failed` / `newsletter triage_ok_but_wiki_ingest_failed`
in a 5-6 h old watchdog report were false alarms: same-day triage/ingest commits
had already landed (`fcc81418` etc.). Before acting on chain-break alerts, check
`git log --oneline --since='18 hours ago'` for the chain's expected commit
messages — if present, report as transient, no action.
