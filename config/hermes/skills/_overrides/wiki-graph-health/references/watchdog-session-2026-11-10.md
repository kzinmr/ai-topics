# Watchdog session 2026-11-10 — digest false-positive + log prepend self-burial

## 1. Digest `pipe_prefix: 6899` is a permanent false positive — DO NOT "fix"

The pre-run `wiki_health.py` markdown digest renders its own tables as `| # | Page | ...`
and `| 1 | ...` rows. The digest-level corruption check (or whatever produced the
`pipe_prefix: 6899` number in the cron context block) counts **markdown table rows in
the digest itself**, not corruption in index.md.

**Verified procedure (trust this, not the digest number):**
```bash
cd ~/ai-topics && python3 -c "
import re
c=open('wiki/index.md').read()
print('pipe_prefix:', len(re.findall(r'^|- \[\[', c, re.M)))
print('line_number:', len(re.findall(r'^\s*\d+\|', c, re.M)))
print('triple_bracket:', c.count('[[['))
print('space_prefix:', len(re.findall(r'^ - \[\[', c, re.M)))
"
```
Live counts were all 0 while the digest claimed 6,899. `validate_index.py` exit 0
confirmed. Always run live grep/Python verification before acting on digest claims
(this session: digest claimed corruption → 0 real issues → report it as "already
clean / false positive" in the report, don't sed anything).

## 2. The `new_entry + content` log.md prepend buries the header ITSELF

The skill's "RIGHT" prepend recipe (`f.write(new_entry + content)`) assumes content
starts with the `# Wiki Log` header. But if it does, the prepend pushes the header to
line ~18 — a self-inflicted recurrence of the very header-burial bug the references
warn about. This session: first prepend put `## [2026-11-10] watchdog...` at line 1,
header at line 17. `count('# Wiki Log')==1` still "passed" — count is NOT the right
assertion.

**Correct prepend (insert entry directly under the header):**
```python
log_path = os.path.expanduser("~/ai-topics/wiki/log.md")
with open(log_path) as f: content = f.read()
marker = '# Wiki Log\n'
idx = content.find(marker)
rest = content[idx+len(marker):]
new = marker + '\n' + new_entry + rest.lstrip('\n')   # new_entry ends with '---\n\n'
with open(log_path,'w') as f: f.write(new)
```

**Positional verification (mandatory, replaces count-based check):**
```python
lines = open(log_path).read().splitlines()
assert lines[0] == '# Wiki Log'
assert lines[1] == ''
assert lines[2].startswith('## ['), lines[2]
```
Also: after the find/split repair, a stray blank line can land between `# Wiki Log`
and the first entry — check `lines[1]==''` and `lines[2]` starts with `## [`, strip
extra blanks if not.

## 3. Index orphan check: the only real gap class this cycle

Recursive unindexed scan (excluding `_index` hubs and nested subdir pages served by
hubs) found exactly 1 gap: `queries/2026-11-09-skeleton-enrich-empty` — the daily
`skeleton-enrich-daily` job writes dated snapshot query pages and sometimes forgets
the index.md registration. Pattern to check every run: `queries/<date>-skeleton-enrich-empty`
files vs index.md entries; register alphabetically after the newest sibling and bump
the `## Queries (N pages)` header. Scan recipe:

```python
import os, re
c=open('wiki/index.md').read()
indexed={m.group(1) for m in re.finditer(r'\[\[((?:entities|concepts|comparisons|events|queries)/[^\]\|]+)', c)}
for ns in ['entities','concepts','comparisons','events','queries']:
    for root,dirs,files in os.walk(f'wiki/{ns}'):
        for f in files:
            if f.endswith('.md') and not f.startswith('_index'):
                slug=os.path.splitext(os.path.relpath(os.path.join(root,f),'wiki'))[0].replace(os.sep,'/')
                if slug not in indexed: print(slug)
```
(Nested pages with extra `/` segments are hub-served — eyeball before "fixing".)

## 4. Sibling-subagent warning on patch is informational

`patch` returned `_warning: file modified by sibling subagent ... but this agent never read it`
on index.md. Concurrent pipelines (trending-topics etc.) touch index.md constantly.
Re-verify counts with grep immediately after patching; commit only `git add` the
specific files you touched (never `git add -A` — working tree carries other jobs' WIP).

## Outcome
Commit `0b19a59c` + follow-up blank-line fix; pre-commit tag validator + validate_index.py
both passed on the first try.
