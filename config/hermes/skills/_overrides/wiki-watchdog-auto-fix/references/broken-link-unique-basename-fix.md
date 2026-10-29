# Broken-Link Unique-Basename Resolution (path/nesting drift)

Session: `wiki-watchdog-fix` cron, 2026-10-29. Cut broken wikilinks **3,348 → 2,464 refs (−884, −26%)** and targets **1,590 → 1,465** in one pass: 123 mappings / 874 replacements / 252 files.

This is the class of broken link that `fix_wikilinks.py` and `wiki_graph.py`'s `bare-wikilink`/`cross-namespace` categories do **not** cover: the link's final segment is correct, the directory prefix is wrong.

## Why the documented fixers miss it

| Class | Example | Covered by |
|---|---|---|
| bare → prefixed | `[[openai]]` → `[[entities/openai]]` | `fix_wikilinks.py` |
| namespace swap | `[[entities/scc]]` → `[[concepts/scc]]` | `fix_wikilinks.py` |
| **path/nesting drift** | `[[grpo]]` → `[[concepts/post-training/grpo]]` | **this recipe** |
| redundant segment | `[[concepts/claude-code/claude-code]]` → `[[entities/claude-code]]` | **this recipe** |
| dir-hub flattening | `[[concepts/post-training/post-training-distributional-view]]` → `[[concepts/post-training-distributional-view]]` | **this recipe** |
| sub-agent page | `[[concepts/rlm]]` → `[[entities/omar-khattab/rlm]]` | **this recipe** |

The migration that moved benchmarks under `concepts/ai-benchmarks/`, post-training under `concepts/post-training/`, and evaluation under `concepts/evaluation/` left thousands of pre-migration links pointing at the old flat paths.

## The scanner

Save to `/tmp/broken_scan.py` and run via `terminal('python3 /tmp/broken_scan.py')` (execute_code is blocked in cron mode).

```python
import os, re, collections
wiki = 'wiki'                      # run from ~/ai-topics
bybase = collections.defaultdict(list); existing = set()
for r, dirs, fs in os.walk(wiki):
    for f in fs:
        if not f.endswith('.md'): continue
        rel = os.path.splitext(os.path.relpath(os.path.join(r, f), wiki))[0]
        existing.add(rel); bybase[os.path.basename(rel)].append(rel)
        # dir links [[concepts/foo]] are VALID when foo/_index.md or foo/index.md exists
        if rel.endswith(('/index', '/_index')):
            existing.add(rel.rsplit('/', 1)[0])

link = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
refs = collections.Counter()
for r, dirs, fs in os.walk(wiki):
    if '_archive' in r or '/raw/' in r: continue
    for f in fs:
        if not f.endswith('.md'): continue
        for m in link.findall(open(os.path.join(r, f), encoding='utf-8', errors='replace').read()):
            m = m.strip()
            if not m or m.startswith(('raw/', 'queries/')): continue
            if m.startswith('[') or '::' in m: continue   # [[:alnum:]], [[gnu::packed]]
            if m not in existing: refs[m] += 1

fixmap = {}
for m, n in refs.items():
    if n < 3: continue                          # threshold: skip one-off noise
    cands = bybase.get(m.split('/')[-1], [])
    if len(cands) != 1: continue                # UNIQUE only — never guess
    if cands[0] != m: fixmap[m] = cands[0]

print('FIXMAP', len(fixmap), 'refs', sum(refs[m] for m in fixmap))
```

## Four mandatory correctness rules

1. **Build `existing` with `relpath` from the walk root.** `os.path.splitext(f)[0]` keeps a `wiki/` prefix while slugs are `entities/foo` → *every* prefix link falsely reports missing (6,260 phantom refs / 0 real, seen 2026-08-06).
2. **Register `_index.md` / `index.md` as their directory.** Without `existing.add(rel.rsplit('/',1)[0])`, every valid `[[concepts/post-training]]` hub link is a false positive. Both `index` and `_index` occur in this wiki.
3. **Unique basename only.** `context-engineering` matched two files (`harness-engineering/` and `harness-engineering/system-architecture/`) — excluded, reported, not guessed. Ambiguity is the escalation signal, not the file count.
4. **Skip artifacts and out-of-scope namespaces**: `[[:alnum:]]`, `[[:space:]]`, `[[gnu::packed]]`, `[[fallthrough]]`, `[[wikilinks]]`; skip `raw/`, `queries/`, `_archive/` while scanning.

## Apply

```python
items = sorted(fixmap.items(), key=lambda kv: -len(kv[0]))   # longest key first
for r, dirs, fs in os.walk(wiki):
    if '_archive' in r or '/raw/' in r: continue
    for f in fs:
        if not f.endswith('.md'): continue
        p = os.path.join(r, f)
        c = open(p, encoding='utf-8', errors='replace').read(); orig = c
        for m, t in items:
            c = c.replace('[[' + m + ']]', '[[' + t + ']]')
            c = c.replace('[[' + m + '|', '[[' + t + '|')   # preserve display text
        if c != orig: open(p, 'w', encoding='utf-8').write(c)
```

`[[slug|Display]]` needs its own replace — a regex-free `str.replace` on `[[m]]` alone silently leaves display-text links broken.

## Verify targets before applying

For every mapping, sanity-check the destination is a real substantive page, not another stub:
```bash
for f in concepts/security-and-governance/ai-safety.md entities/claude-code.md \
         concepts/coding-agents/coding-agents.md entities/embeddings.md; do
  printf "%-55s %6sB %4sL " "$f" "$(wc -c <"$f")" "$(wc -l <"$f")"; grep -m1 '^title:' "$f"
done
```
Cross-namespace destinations occurred and were correct: `[[concepts/embeddings]]`→`entities/embeddings`, `[[entities/apple]]`→`concepts/apple`, `[[entities/company-ai-pilled]]`→`concepts/company-ai-pilled`, `[[concepts/coding-agents/bernstein]]`→`entities/bernstein`. Verify by content, never by which directory the *link* claims.

## Top remappings (2026-10-29, for pattern recognition next time)

`concepts/ai-safety`→`security-and-governance/` (38) · `concepts/claude-code/claude-code`→`entities/claude-code` (35) · `grpo`→`post-training/grpo` (22) · `gaia-benchmark`→`ai-benchmarks/` (20) · `reinforcement-learning`→`post-training/` (19) · `entities/coding-agents`→`concepts/coding-agents/coding-agents` (18) · `concepts/swe-bench`→`ai-benchmarks/` (18) · `hal-leaderboard`→`ai-benchmarks/` (16) · `tau-knowledge`/`tau-squared-bench`/`tau-voice`→`ai-benchmarks/` (39) · `llm-as-judge`→`evaluation/` (12) · `concepts/agent-team-swarm`→`multi-agents/` (12) · `rlvr`→`post-training/` (11)

The `ai-benchmarks/` cluster alone was ~150 refs — the AGENTS.md rule "all benchmark pages live under `concepts/ai-benchmarks/`" is the single biggest source of drift.

## Genuinely-missing residue (human review, NOT fixable by renaming)

After the pass, 59 targets had no unique file anywhere. Highest-ref: `agent-evaluation` (24), `concepts/agentic-rl` (14), `entities/cursor` (13), `concepts/ai-governance` (12), `concepts/enterprise-ai` (12), `concepts/ai-adoption` (10), `concepts/agent-architecture` (10), `concepts/agent-harness-comparison` (9), `entities/huggingface` (9), `concepts/bitter-lesson` (9), `concepts/inference-optimization` (9). These need page creation (`active-crawl` / a page-creation job) — report counts, do not fabricate stubs from the watchdog.

Also stable across runs: **278 empty wikilinks** in 153 files (0 auto-fixable — matches the documented residual in `wiki-graph-health` Pattern B; `fix_empty_wikilinks_safe.py` proposals all point at non-existent files).

## Re-running the scan

Deterministic and idempotent — re-run to confirm the count dropped and that no new breakage was introduced. A second healthy pass should show the same or lower total. If a number *grew*, a replace collided with a display-text link or a wrong-namespace target; check `git diff` before committing.
