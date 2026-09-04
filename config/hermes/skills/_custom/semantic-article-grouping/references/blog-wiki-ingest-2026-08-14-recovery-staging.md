# Ingest-Side Staging Discipline After Triage Checkpoint Recovery

Validated 2026-08-14 (blog-wiki-ingest, recovered from blog-triage JSON render failure).

## Scenario

The triage agent failed to render its cron response (`"failed to parse JSON response from blog-triage output"`),
but had already:
1. Saved valid JSON to `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json`, AND
2. **Committed the archive + raw article files** before the render failed.

Evidence in `git log --oneline -5`:
```
7e6ba774 wiki: blog-triage 2026-08-14 - 3 takes (voyage-code-4, Gemini 3.7 Flash via llm-gemini 0.33, Alpoge Hadamard-668 via Claude); 2 refs; 15 skips archived
```

## What the ingest job must do (and NOT do)

- **DO NOT re-run `archive_triage.py`** — the triage commit already contains the archive JSON
  (`wiki/raw/archived/triage/blog/2026-08-14_*.json`) and `archive_index.json` updates.
- **DO NOT re-add the raw article files** — they are in the triage commit.
- **Verify the archive is in git** with `git show --stat <triage-commit>` and confirm the dated archive
  file + raw files appear in the diff. Then proceed to Post-Recovery Verification of the takes.
- **Stage ONLY the wiki page files your enrichment touched**: entities/concepts pages + `wiki/index.md` + `wiki/log.md`.

## Sibling-pipeline noise at the same moment

At the 07:00-07:50 UTC window (and catch-up runs), the working tree will show unrelated changes from
parallel pipelines. Observed 2026-08-14 while staging the enrichment commit:

```
 M wiki/raw/archived/triage/archive_index.json     ← newsletter triage ran after blog triage; NOT yours
?? wiki/raw/articles/2026-08-14_elevenlabs_*.md    ← sitemap-monitor scrapes; NOT yours
?? wiki/raw/newsletters/2026-08-13-*.md            ← newsletter ingest; NOT yours
```

**Never blanket `git add wiki/`** in this state — it sweeps the sibling `archive_index.json` modification
into your page-enrichment commit (and the sitemap/newsletter raw files too). Always list exact paths:

```bash
git add wiki/entities/voyage-ai.md wiki/concepts/gemini/index.md wiki/concepts/claude-fable-jacobian-conjecture.md \
        wiki/entities/andrew-nesbitt.md wiki/entities/simon-willison.md wiki/index.md wiki/log.md
git commit -m 'wiki: blog-wiki-ingest 2026-08-14 - ...'
```

Leave the sibling changes unstaged — their owning pipelines commit them. This is the ingest-side mirror
of `references/archive-commit-targeted-git-add.md` (triage side): that file's rule is targeted `git add`
for the archive; this one is targeted `git add` for the enrichment pages.

## Commit sanity check

Before pushing, confirm `git status --short -- wiki/` shows exactly your staged files and the sibling
files remain as unstaged/untracked noise. The pre-commit hook (tag + index validation) will validate
only staged content.
