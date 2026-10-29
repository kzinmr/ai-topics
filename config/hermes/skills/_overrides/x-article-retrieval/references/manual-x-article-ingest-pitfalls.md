# Manual X Article Ingest Pitfalls (2026-10-17, E2B "Sandboxes are dead")

User-requested ingest (X URL + 「wikiに取り込んで」) on top of the main SKILL.md workflow.

## 1. log.md prepend formatting

Naive `entry + log` (Python string concat) glues the new entry's last bullet to the next `## [` heading because the log has no trailing structure guarantee. Symptoms: `## [2026-10-16] skeleton-enrich...` appears immediately after your last bullet with no blank line.

Correct pattern:
```python
entry = "...bullets...\n\n"   # MUST end with blank line
log = open('wiki/log.md').read()
open('wiki/log.md','w').write(entry + log)
```
Then verify: `sed -n '1,14p' wiki/log.md`.

If a retry caused a duplicate entry, dedupe: find the second occurrence of your heading, cut from there to the next `\n## [`:
```python
first = log.find(marker); second = log.find(marker, first+1)
nxt = log.find('\n## [', second+10)
log = log[:second].rstrip() + '\n' + log[nxt+1:]
```

## 2. Contradiction-with-existing-takeaways pattern

When the new source directly contradicts a Key Takeaway already on a concept page (case: E2B CEO's "cold-start competition is the wrong answer for wave 3" vs `concepts/sandbox/infrastructure.md` takeaway #3 "cold start 90-200ms is now acceptable"), do NOT edit or delete the old takeaway. Per the AGENTS.md contradiction rule:

- Add a NEW dated section that names the conflict explicitly ("This thesis directly challenges takeaway #3 above…")
- Label vendor-self-reported claims in the same section (e.g. "vendor-reported; no independent verification")
- Note when the thesis is also a commercial repositioning (E2B critiques the cold-start race it itself competes in) — this keeps the wiki neutral

## 3. Pre-commit tag verification (before writing, not after failure)

Tags must exist in `wiki/SCHEMA.md` taxonomy. Quick check before authoring pages:
```bash
python3 -c "
import re; s = open('wiki/SCHEMA.md').read()
tags = set(re.findall(r'[a-z0-9]+(?:-[a-z0-9]+)*', s))
for t in ['agent-infrastructure','x-article']: print(t, t in tags)"
```
Known: `agent-infrastructure`, `ai-infrastructure`, `platform`, `serverless`, `sandbox` valid; `x-article` NOT valid. The pre-commit hook checks ALL staged files, so a bad tag in a brand-new entity page blocks the whole commit.

## 4. Two-call xurl fetch is enough (also patched into x-article-retrieval)

The metadata call requesting `tweet.fields=note_tweet,created_at,author_id,public_metrics&expansions=author_id&user.fields=name,username,description` returns `article.title` too (unrequested) — detection + metrics + author in ONE call. Then one `tweet.fields=article` call for the body. Skip a third metadata call.

## 5. New-entity cross-link discovery

When creating a first entity page (e.g. `entities/e2b.md`), grep existing concept pages for the entity name (`grep -rn "E2B" wiki/concepts/`) — mentions often already exist in comparison tables (it was in sandbox/infrastructure.md's platform table). Wikilink the new entity FROM those pages back, and update the concept page's `updated:` + `sources:` frontmatter in the same commit.
