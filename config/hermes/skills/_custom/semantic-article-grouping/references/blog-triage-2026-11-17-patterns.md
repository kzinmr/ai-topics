# Blog Triage Patterns — 2026-11-17 (run 20261117T100008Z)

20 candidates, all `source: blog`, all read in full. Yield: take 4 / reference 2 / skip 14 (collapsed into 2 batch entries + 3 individual). Archive: 7 items.

## 1. CJK builder script: three blockers hit in one file, one pass

First `write_file` attempt to `/tmp/blog_triage_<runid>.py` failed lint with:

```
SyntaxError: invalid syntax. Perhaps you forgot a comma? (line 76, column 5)
```

Two independent causes in the same file:

1. **Star glyph in a helper default/arg**: `make(..., "★" * stars + " " + reason)` inside a dict literal. The `★` itself is fine as data, but combined with the adjacent CJK strings the parser/lint surface produced the misleading "forgot a comma" error. Fix: `"*" * stars` (ASCII asterisks). The `★` rating display is cosmetic — downstream reads `recommended_action`, not the glyph.
2. **ASCII double quotes inside Japanese literals** when quoting English headlines verbatim (`"Nvidia's Days as an Open Checkbook for the AI Economy Are Numbered"`). Fix: drop the quotes and let the English run inline, or wrap in 「」.

Working sequence (all cron-safe, no heredoc, no `execute_code`):
```
write_file /tmp/blog_triage_<runid>.py
terminal: python3 -c "import ast;ast.parse(open('/tmp/...',encoding='utf-8').read())"
terminal: python3 /tmp/blog_triage_<runid>.py
terminal: python3 -c "import json; d=json.load(open('<hardcoded path>')); ..."   # no pipe
```
Lint clean on rewrite → ran first try, 11 decisions, zero missing `body_excerpt`/`reason_ja`.

## 2. `search_files target='files'` false negative on stub pages

Checked `concepts/` for "Superintelligence" with `target='files'` → **0 matches**, yet `concepts/superintelligence.md` existed (title "Superintelligence"). Cause: `target='files'` runs a regex over file CONTENTS, and the 20-line stub is a frontmatter-heavy skeleton whose body never repeats the term.

Discipline adopted this session — for every coverage check use BOTH:
- `find <dir> -maxdepth 1 -iname "*keyword*"` (true filename glob)
- `grep -c "" <file>` + `grep -n "^## " <file>` (line count + section map, distinguishes stub from substantive)

A ~20-line page with `updated:` months old = stub → **take signal (★★★★★ new page)**, not an absence signal.

## 3. Person-interview coverage-gap shortcut (dwarkesh.com podcast transcripts)

For a long-form interview raw (this session: `www.dwarkesh.com--p-paul-christiano-2`, 114KB transcript), the decisive gap test is on the **guest**, not the host:

1. `find entities concepts events queries -iname "*<guest-slug>*"` — 0 hits → no person page
2. `grep -ril "<Guest Full Name>" entities/ concepts/ events/` — hits only as an incidental citation (Christiano appeared solely as a 2016 "Concrete Problems in AI Safety" coauthor in `concepts/security-and-governance/ai-safety.md`) → does NOT count as coverage
3. `grep -ril "<guest's org>" entities/ concepts/` — "Alignment Research Center" appeared only inside two GPT system cards → still a gap
4. Check the nearest adjacent concept pages' actual section list (`recursive-self-improvement.md`, `superintelligence.md`, `ai-alignment.md`) for the SPECIFIC claims, not the topic umbrella

All four weak → new concept page (★★★★★). Host entity page (`entities/dwarkesh-patel.md`) having dated episode sections is NOT coverage of the guest's thesis.

## 4. Recurring source-specific verdicts (reuse next time)

- **George Hotz "the singularity is nearer" series**: `entities/george-hotz.md` is 379 lines and accumulates every essay with per-date subsections + a Key Writings list. Always check whether the specific DATE entry exists — the page being rich is not coverage of a new post. Nov 13 "First Strike" ≠ Nov 17 "My Empire of Dirt". Test: does the page contain the specific thesis? (Nov 17's Anthropic-singleton critique + long-war resource thesis were absent → take.)
- **Daring Fireball-linked Apple/macOS items**: 5/20 candidates this run were Full Disk Access / iPhone Duo / App Store links — zero LLM/agent content, batch-skip. DFG batches skew heavily Apple; expect it and batch them.
- **Gary Marcus bubble posts**: check `concepts/ai-bubble-economics.md` (617 lines) section list — it stops at the Nov 12 Economist editorial + Anthropic S-1; each new Marcus bubble post adds concrete numbers (Oracle −61%, WSJ Kress "open checkbook") → ★★★★☆ existing-page update, never a new page.
- **Simon Willison micro-posts**: sub-1KB release notes (llm 0.37.3 SQLite 3.54.1 `json_object` regression + D. Richard Hipp spec ruling) → reference (one-line timeline entry), not take. Sub-500B quote-posts (Go Proverbs) → skip.

## 5. Same-day freshness check that actually decided it

`grep "2026-11-17" wiki/log.md` returned exactly one line: `## [2026-11-17] blog-ingest | 20 raw articles`. That is raw SAVING only, never triage consumption. `triage_latest.json` carried the 20261115 run id → batch confirmed fresh before any analysis. Cost: one grep.

## 6. archive_triage.py path cosmetic trap (re-confirmed)

`scripts/archive_triage.py blog --keep-reference` printed `/opt/data/.hermes/home/ai-topics/wiki/raw/archived/...` — looks like the nested docker-home path, is a symlink to the canonical repo. `git add` the canonical `wiki/raw/archived/triage/blog/<date>_<runid>.json` + `archive_index.json` only; the pre-existing unrelated modified entity pages in `git status` were left unstaged (targeted add, per `references/archive-commit-targeted-git-add.md`). Commit `5b53659a` pushed clean, no pre-commit hook violations.
