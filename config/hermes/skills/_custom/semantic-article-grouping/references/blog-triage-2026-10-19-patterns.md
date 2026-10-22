# Blog Triage Patterns — 2026-10-19 (run 20261019T100541Z)

Batch: 14 saved candidates + 6 unsaved_articles → 1 take, 5 references, 14 skips. Typical low-yield day (single-source-dominated batch with heavy Daring Fireball opinion/hardware noise).

## 1. Sibling-pipeline same-day page touches are NOT a dedup signal for author-entity takes

**Case**: Sean Goedecke's "What requirements don't you have?" (seangoedecke.com, 6.1KB) — frontier models RLVR-trained as "Grader-obsessed high-achieving schoolchildren" that introduce *unsolicited requirements* (spurious mutexes, TOCTOU checks that don't prevent TOCTOU, "what if admin status is lost mid-request" edge cases), ballooning a 4-line change into a 1000-line monster; concrete "code review is dead" rebuttal (~half of large AI diffs contain an LLM-invented unnecessary requirement); mitigations (spell out staleness tolerance in prompts, first scan in Go reviews for unnecessary mutexes/indirection).

`concepts/code-review-bottleneck.md` had been modified the SAME day by a sibling pipeline. Tempting to skip as "covered today" — WRONG. Verification showed:
- code-review-bottleneck.md = telemetry-study framing (adoption → review bottleneck), zero overlap with Goedecke's practitioner claims
- concepts/prompt-optimizers-unscored-requirements.md = academic (arXiv:2610.13287, GEPA/MIPROv2 unscored requirements) — adjacent NAME ("unscored requirements") but completely different territory (prompt optimization vs code-generation behavior). Adjacent keyword ≠ adjacent content; grep matches can be false positives across subfields.
- entities/seangoedecke-com.md (559 lines, 15+ article sections) — article absent → genuine gap.

**Lesson**: coverage test is always per-page content ("does THIS page contain THIS article's specific claim/number/argument?"). Never use "some related page was touched today by another pipeline" as a skip reason. Keep `grep` hits as leads, not verdicts — read the hit's actual section before citing it.

## 2. Contentless-small raw files (reverse of contentless-large)

`troyhunt.com--weekly-update-526` was 504B — above the 500B soft threshold but containing ONLY frontmatter + boilerplate author bio, no article body. The skill's §1 warning covers contentless LARGE files (10-20KB nav chrome); the small-file counterpart exists too: newsletter "Weekly Update NNN" posts where the extractor captured only the header.

Handling: title-level reference only (stars=2), `body_excerpt` explicitly notes "本文未抽出 (504B の frontmatter + 著者バイオのみ)" and that take-ification requires re-fetch. Do NOT fabricate substance from the subject line ("Building HIBP AI/SI First" could be anything).

## 3. Cross-pipeline continuity clue worth a reference line

Simon Willison micro-release posts (496B llm-tools-datasette 0.1.1) looked dismissible, but body read revealed it is the *sequel* to an event already recorded at line ~930 of entities/simon-willison.md (llm 0.32.1 httpx transitive-dependency breakage → "forthcoming 0.33 switches to httpx2"). The new post confirms the predicted side-effect materialized (plugins depending on httpx indirectly broke). Before skipping tiny release notes, grep the author's entity page for the predecessor event — if the article closes a loop the entity page opened, it earns a one-line reference append, not a skip.

Similarly llm-echo 0.5 (908B): simulated token usage now accounts for tool calls / system prompts / reasoning tokens — framed as mock-harness token-accounting validation (harness-engineering angle) to justify reference over skip.

## 4. Cron-mode execute_code block — confirmed still default

`execute_code` returned "BLOCKED: execute_code runs arbitrary local Python... Cron jobs run without a user present" in this run. The skill's Option B (write_file /tmp/script_YYYYMMDD.py + terminal python3) is the only path; the batch-triage Python helper must be written via write_file from the start, not attempted inline.

## 5. Routine confirmations

- `archive_triage.py blog --keep-reference` output path prints `/opt/data/.hermes/home/ai-topics/...` — symlink, verified canonical via `readlink -f` (existing skill guidance, revalidated).
- `git status` showed sibling pipelines' uncommitted wiki changes (aauth concept, modal/workos raw articles) — targeted `git add` of only the two archive files kept the commit clean; no --no-verify needed.
- Daring Fireball opinion/hardware noise (Verizon press release, HomeView pricing musing, political X clip, comic, kernel release, retro-computing) produced 7/14 skips — when DF contributes 5+ candidates, most are non-AI relay content; still read each body (640B-18KB) for the excerpt, batch-skip only same-author/same-category series.
