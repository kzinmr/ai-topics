# Trending batch run — 2026-11-18 (weekday noon, ~30 calls, 1 commit 17 files, BOTH hooks green FIRST try)

Clean run, zero hook round-trips. Recipe from 11-13/11-17 held exactly: frontmatter-driven `grep -cw` tag verification before `git add`, staged page bodies via write_file, heading-anchored appends, two-pass sha256, scoped git add.

New/confirmed details:
- `github.com/microsoft/onnxruntime` returned 404 to plain urllib fetch — because the repo itself had vanished from GitHub (that WAS the story, HN 350p). When a GitHub-primary fetch 404s on a trending story, check whether the disappearance is the news before assuming fetcher failure. Comment tree (Intel fork, SourceForge mirror, Phrack 73 ORT parser flaw) carried the whole fact chain.
- `hn_algolia_supplement.py` foreground terminal call gets killed at the 60s tool timeout even with `timeout 150` inside the command — run via `terminal(background=true, notify_on_complete=true)` writing to a file, then read in two sed passes.
- Report typo class re-appeared inside the write_report.py script: `遠測` (for テレメトリ), `銀行_run` (for バンクラッシュ), `チャネルサングラス` (channel-sungging corruption), `ウィクション` (for ウィキ, second instance after 11-13). Fix route that worked: patch the SOURCE write_report.py with an `assert a in s` substitution list, re-run it (never just sed the output — the script is re-runnable).
- Han-grep eyeball gate output for a clean JP report is a long list of legitimate 漢字 compounds (日窓/一次/突然消滅...) — the gate only needs a quick scan for simplified-only forms; zero Hangul + balanced 「」 (17/17) was the real pass signal.
- Wiki target gotcha: `concepts/weight-provenance` and `concepts/model-attestation` are SCHEMA tags but NOT pages; real pages are `concepts/artifact-provenance-gates.md` / `concepts/pace-provenance-aware-capability-enforcement.md`. Tag-in-SCHEMA ≠ wikilink-target-exists; still run the `[ -f ]` sweep on every Related bullet.
- SCHEMA minted 15 tokens in one batch (java, metr, runta, protein-models, harness-evaluation, openjdk, ai-overviews, publisher-economics, safety-washing, revolving-door, ai-regulation, vendor-benchmark, model-telemetry, avx-512, memory-corruption) via the add_tag whole-word regex helper — no hook fire.
- Index counts verified post-commit directly (entities 972/972, concepts 2372/2372) — the two-step check is cheap enough to fold into the push call.
