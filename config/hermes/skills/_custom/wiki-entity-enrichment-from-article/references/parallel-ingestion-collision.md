# Parallel Ingestion Collision Detection

## Problem

The wiki has autonomous cron pipelines (`raw-backlog-ingest`, `newsletter-wiki-ingest`, `dreaming-wiki-ingest`) that run independently. When a user asks you to ingest a paper or article, a parallel cron job may have already ingested it moments earlier. Your `write_file` calls succeed but produce content identical to what's already committed — `git diff --stat` shows nothing.

## Detection

After writing wiki pages and running `git add wiki/`:

```bash
# If git diff shows nothing for your files, check whether they're already in HEAD
git show HEAD:wiki/entities/<file>.md | head -5
git log --oneline -3 -- wiki/entities/<file>.md
```

**If the files exist in HEAD with content matching yours**: a parallel agent already committed them. This is GOOD — no duplicate work needed. Verify the committed content is adequate and move on.

**If the files DON'T exist in HEAD but git diff is empty**: the files may be outside the git tree or in a symlink target that git doesn't see. Check `realpath` and `git rev-parse --show-toplevel`.

## Handling

| Scenario | Action |
|----------|--------|
| Content identical to HEAD | No commit needed. Verify quality, explain to user, done. |
| Your version has better content | `patch` to add your improvements, commit the diff. |
| Neither version exists (but files written) | Debug git tree issue, `git add -f` if needed. |

## Real Case (2026-05-29)

SIRA paper (arXiv 2605.06647) was being ingested manually via user request on Discord. Simultaneously, the DCI paper cron job (`7e22a2d0`) bundled SIRA into the same commit. When the manual ingestion wrote `entities/sira.md`, `raw/papers/sira-2605.06647.md`, and patched `information-retrieval.md`, `git diff --stat` showed zero changes for all wiki files. Investigation with `git show HEAD:wiki/entities/sira.md` confirmed the file was already committed with identical content. No second commit was needed.

## Prevention

Before starting ingestion, check if the target was recently committed:

```bash
git log --oneline -5 --diff-filter=A -- wiki/entities/ wiki/raw/papers/ | head -5
```

This catches papers ingested in the last few minutes by cron jobs. If the paper is already there, skip the write phase and go directly to verification + user explanation.
