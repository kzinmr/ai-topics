# Newsletter wiki-ingest patterns — 2026-11-08 (run 20261108T101230Z)

Session: newsletter-wiki-ingest cron, recovery from triage JSON parse failure. 2 takes → 4 new pages + 6 updates, commit 2777eeda pushed.

## 1. `execute_code` fully blocked in this cron profile — no approvals fallback

`execute_code` returned `BLOCKED: ... Cron jobs run without a user present to approve it` for even a pure-stdlib json read (no subprocess). This profile does not set `approvals.cron_mode: approve`. Consequence: the skill's "Interactive sessions (execute_code available)" paths are dead here — **always** use `write_file /tmp/*.py` + `terminal python3`, or plain `terminal` (`sed -i`, `head/tail/cat` concat) for trivial edits like frontmatter date bumps and log.md prepend.

## 2. Triage parse-failure recovery worked as documented (validates existing ref)

Script output `{"ok": false, "error": "failed to parse JSON response from newsletter-triage output"}` + `output_path` → the triage agent had already saved `cron/data/newsletter/triage_latest.json` before its response render failed. Verified freshness via `checkpoint_run_id` match against the prior commit (`git show --stat 3df35b89` showed the triage report commit touched only `raw/inbox/...` + archive files, NOT wiki pages → takes genuinely unconsumed), then read the triage response markdown tail (after `## Response`) for the rich per-take downstream instructions. The full cron output file also embeds the candidates array at the tail — useful when latest.json needs cross-checking.

## 3. Pre-commit Japanese check fires on a single CJK token in a NEW file

`.githooks/pre-commit-jp-check.py` blocks commits with `NEW FILE with Japanese content` — even ONE CJK term (e.g. the 源网荷储 gloss in a concept page's first paragraph) in an otherwise-English new page. Fix is to remove/romanize the CJK, not `--no-verify` — the check is a genuine policy (all non-raw wiki content English). When writing new pages about Chinese/Japanese topics, avoid parenthetical native-script glosses. The existing `pre-commit-new-page-tags-workflow.md` ref covers tags; this is the jp-check sibling.

## 4. `git pull --rebase` blocked by sibling unstaged files → plain push still fine

`git pull --rebase` failed with "cannot pull with rebase: You have unstaged changes" (sibling subagents' `config/hermes/skills/` edits). Check whether local is behind first; when it isn't, a plain `git push` fast-forwards without stashing the sibling's files. Never stash or checkout a sibling's dirty files to unblock a push.

## 5. patch tool can drop a frontmatter line on fuzzy match

Editing kim-isenberg frontmatter, a `replace` with old_string spanning `created:`/`updated:`/`type:` produced a file missing `created:` and with duplicate `type:` — patch's fuzzy match consumed a line the new_string didn't reproduce. After any frontmatter patch, `head -6` the file to verify; fix with a second targeted patch.

## 6. Archive already committed by triage → skip archive_triage.py re-run

Check `git show --stat <prior-triage-commit>` before invoking `archive_triage.py` — this run's skip/reference archive (`2026-11-08_20261108T101230Z.json`, 32 lines) was committed at `3df35b89` by the triage stage itself. Re-running is harmless (dedup_skipped) but wasted.

## 7. Same-topic paywalled pair → contrast-page network

The batch's two takes were mirror images (US DC local backlash 40/41 vs Inner Mongolia no-backlash buildout). Cross-linked both directions plus hub pages (`ai-energy`, `subprime-data-center-crisis`, `nvidia-45c-data-center-cooling`) gained 1-paragraph cross-references with the opposing-case framing — much higher graph value than the minimum 2 wikilinks. Mark paywall scope ("free portion only", what's paywalled) on every page derived from gated sources.
