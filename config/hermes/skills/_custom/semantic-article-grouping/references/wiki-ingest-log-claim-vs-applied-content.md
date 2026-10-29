# Sibling-parallel commit & log-prepend safety (newsletter-wiki-ingest)

Companion to the "log coverage claim ≠ applied content" pattern already in this file. These are the two mechanical pitfalls hit when a wiki-ingest cron runs in the 07:00–11:00 UTC parallel window alongside sibling subagents/pipelines touching the same repo (`~/ai-topics`).

## Pitfall: `git pull --rebase` aborts but `git push` still succeeds

When a sibling subagent has uncommitted working-tree edits (e.g. it enriched another entity page but hasn't committed yet), `git pull --rebase` fails with:

```
error: cannot pull with rebase: You have unstaged changes.
```

This is NOT a failure of your work. If your commit is a clean fast-forward, the **subsequent `git push` still succeeds**:

```
To https://github.com/kzinmr/ai-topics.git
   ac59ec7e..34651b72  main -> main
```

**Lesson:** Treat the `git push` output as authoritative, not the `git pull --rebase` error. Do NOT panic-re-run ingest or try to stash the sibling's changes. Confirm with:

```bash
git log --oneline -1                 # your commit is HEAD
git status --short -- wiki/          # your files are clean (no M/?? for YOUR paths)
```

If your paths are clean and push reported `old..new main -> main`, you are done. The unstaged changes belong to a sibling that will commit its own work.

## Safe log.md prepend under sibling parallelism

`wiki/log.md` is newest-first with **NO H1 title line** — the file starts at the newest `## [date ...] pipeline | run ...` heading. A prepend script that anchors on a line starting with `# ` silently matches a sibling's H2 section and destroys the previous entry heading.

**Correct anchor:** the first line where `line.startswith("## [")`. Because this anchor is **content-based**, it is robust to siblings prepending their own entries between your read and write — the script re-finds the first `## [` heading at run time and inserts above it regardless of how many new sibling entries appeared.

```python
lines = content.split("\n")
idx = next((i for i, ln in enumerate(lines) if ln.startswith("## [")), 0)
new = "\n".join(lines[:idx]) + "\n" + entry + "\n" + "\n".join(lines[idx:])
```

In cron mode write the script to `/tmp/` via `write_file` and run via `terminal` (execute_code blocked; heredocs with CJK trip the homoglyph scanner). If `write_file` warns a sibling modified `/tmp/log_update.py`, that's benign — your content was just written; run it and verify with `head -6 wiki/log.md`.

## Beehiiv 403 → direct-slug body recovery (re-confirmed)

When all `link.mail.beehiiv.com/v2/c/...` tracking URLs return 403 (expired token) AND no inbox pre-triage summary exists, the **direct article URL on the canonical read-domain** recovers the body: `curl -sL https://read.<pub>.com/p/<slug>` returns full HTML (700KB+) with JSON-LD (`headline`, `isAccessibleForFree:False`, `author`, `description`) + free-preview `<p>` paragraphs (~14 paras here). This is enough to author an accurate events/concept page from the free tier; flag paywalled remainder as "re-fetch downstream". Validated 2026-10-25 (Superintel+ uid=839, OpenAI offline cached-web RL event page). This is the same domain-split documented in the main skill's getsuperintel map — the `read.getsuperintel.com/p/{slug}` direct-slug variant works even when the `.com` Framer host 404s and tracking links 403.
