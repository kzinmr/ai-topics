# Tag Audit Session — 2026-10-26

## Outcome
Near-clean run: 3,371 pages scanned, 918 unique tags, **0 composite tags, 1 non-SCHEMA tag**. Fixed via one SCHEMA.md addition. Commit `8cc8a6ce` passed pre-commit tag validator WITHOUT `--no-verify` (contrary to the cron prompt's assumption that --no-verify is always needed — it's only needed when normalization touches pages the hook would block; a pure SCHEMA-addition commit passes cleanly).

## Violation and resolution
- `ai-control` (1x, `concepts/monitorability-metrics.md`).

**KEY JUDGMENT — do NOT blind-delete a 1x tag.** The Phase 2 rule says "one-off tags → DELETE as noise", but `ai-control` is the exact slug of an existing canonical concept page (`concepts/ai-control.md`, DeepMind AI Control roadmap). Deleting the tag would decouple the page from its own topic category. Resolution: **add the tag to SCHEMA.md** (AI Agents category, inserted after `agent-safety`), per the "frequent legitimate new tags with no canonical match → add to SCHEMA" branch — extended: a matching canonical *concept page* is itself justification even at 1x usage. Check `wiki/concepts/<tag>.md` (and `wiki/entities/<tag>.md`) existence before any one-off deletion.

## Technique: SCHEMA.md insertion via Python splice, not `patch`
SCHEMA.md Primary Category lines are single lines with 500+ comma-separated tags (Models line ~4,000 chars). Using `patch` requires reproducing a huge unique old_string. Instead:
```python
import re
s = open('wiki/SCHEMA.md').read()
m = re.search(r'^- \*\*AI Agents\*\*: (.+)$', s, re.MULTILINE)
tags = m.group(1).split(', ')
assert 'ai-control' not in tags
tags.insert(tags.index('agent-safety') + 1, 'ai-control')
new = '- **AI Agents**: ' + ', '.join(tags)
s = s[:m.start()] + new + s[m.end():]
open('wiki/SCHEMA.md', 'w').write(s)
```
Then re-run `tag_audit.py` to confirm 0 violations before committing.

## Git pitfall: sibling unstaged changes block rebase, not push
`git pull --rebase` failed with "cannot pull with rebase: You have unstaged changes" — the worktree had concurrent-pipeline modifications under `config/hermes/skills/` (sibling subagents). The staged commit itself was fine and `git push` succeeded directly (`46e13585..8cc8a6ce main -> main`). Do NOT stash sibling agents' work to force a rebase; if push succeeds, done. Only deal with the rebase if push is rejected as non-fast-forward — then `git stash` → pull --rebase → push → `git stash pop`.

## Other
- Bumped `updated:` on the tag-touched page (2026-08-17 convention).
- log.md prepend via `write_file /tmp` + `cat /tmp/entry.md log.md > merged && mv` (append-only rule).
- No TAG_NORMALIZATION changes needed.
