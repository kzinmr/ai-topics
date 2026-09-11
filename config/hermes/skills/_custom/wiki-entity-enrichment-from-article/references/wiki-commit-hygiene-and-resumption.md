---
title: "Selective Staging & Interrupted-Turn Resumption"
type: reference
created: 2026-09-05
sources:
  - session: 2026-09-05 pvncher X Article ingest
---

# Selective Staging & Interrupted-Turn Resumption

Two operational lessons from the pvncher X Article ingest (2026-09-05).

## 1. `git add wiki/` sweeps foreign files — stage selectively

Manual wiki ingests commit with `cd ~/ai-topics && git add wiki/ && git commit ...`. Cron pipelines (blog-wiki-ingest, x-bookmarks-ingest, raw-backlog, vendor-blog scrapes) frequently leave *their* raw articles uncommitted under `wiki/raw/`. Your `git add wiki/` then silently bundles them into your commit, and the commit message ("wiki: ingest X article by pvncher") misrepresents an 11-file change set.

**Pre-flight (30 seconds):**
```bash
cd ~/ai-topics && git status --short wiki/
```
- If only your files appear → proceed as usual.
- If foreign files appear → either:
  - **(a)** commit foreign raws separately first: `git add wiki/raw/articles/<foreign>...; git commit -m "wiki(raw): backlog files from cron pipelines"`, then commit yours; or
  - **(b)** stage selectively: `git add wiki/raw/articles/<yours>.md wiki/concepts/<page>.md wiki/entities/<page>.md wiki/log.md wiki/index.md` (explicit paths only, no directory).
- Do NOT `git stash` or discard foreign files — they're cron output that belongs in the repo.

## 2. Mid-task 503 → resume from filesystem state, not from scratch

If a turn aborts with `HTTP 503: Local LLM server is busy` (local provider busy) and the user replies 再試行 / "retry", the previous turn may have completed any prefix of the steps (raw save, page patches, log append). **Do not blindly redo the whole flow** — re-fetching wastes API calls and re-writing patched pages risks duplicate sections or fuzzy-patch mismatches.

**Resumption checklist (run first):**
1. `ls wiki/raw/articles/ | grep <slug>` — was the raw saved?
2. `grep -l "<new section heading>" wiki/concepts/*.md wiki/entities/*.md` — which pages already carry the new section?
3. `tail wiki/log.md` — was the log entry appended?
4. `git status --short wiki/` — is anything already committed vs staged?

Then resume at the first missing step. This also applies to any mid-turn interruption (user sends a new message, /stop), not just 503s.
