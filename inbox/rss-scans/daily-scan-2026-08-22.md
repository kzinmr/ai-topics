# Daily RSS Scan — 2026-08-22

- **Scan run**: 2026-08-22 07:00 UTC (blog_ingest, run_id `20260822T100051Z`)
- **New articles total**: 20 (18 saved to `wiki/raw/articles/`, 2 unsaved — paywall/JS)
- **Blogs scanned with new posts**: simonwillison.net (4), daringfireball.net (8), garymarcus.substack.com, matklad.github.io, seangoedecke.com, johndcook.com, dfarq.homeip.net, pluralistic.net, filfre.net, shkspr.mobi
- **Checkpoint**: `/opt/data/.hermes/cron/data/blog_ingest/latest.json`

## Triage Table

| ソース | タイトル | NJスコア | アクション | 対象 |
|--------|----------|----------|------------|------|
| garymarcus.substack.com | Data center madness | 4/5 | wiki更新（概念+人物） | `concepts/ai-bubble-economics`, `concepts/subprime-data-center-crisis`, `entities/gary-marcus` |
| matklad.github.io | Rust Glancer | 4/5 | wiki更新（人物） | `entities/matklad-github-io` |
| simonwillison.net | Stop Making TUIs | 4/5 | wiki更新（人物） | `entities/simon-willison` |
| simonwillison.net | llm 0.32.1 / llm-openrouter 0.7 | 2/5 | wiki更新（リリースノート、人物に併記） | `entities/simon-willison` |
| seangoedecke.com | You should never be angry at work | 2/5 | wiki更新（人物） | `entities/seangoedecke-com` |
| simonwillison.net | Quoting Matt Webb | 1/5 | スキップ（リンク集、短文） | — |
| johndcook.com | How would you know whether an ancient culture had zero? | 0/5 | スキップ（非AI・数学雑学） | — |
| dfarq.homeip.net | Microsoft QuickBasic remembered | 0/5 | スキップ（非AI・懐古） | — |
| filfre.net | A Need for Speed (Digital Antiquarian) | 0/5 | スキップ（非AI） | — |
| pluralistic.net | Born on technology's third base | 0/5 | スキップ（非AI・SF） | — |
| shkspr.mobi | Book Review: An Immense World (Ed Yong) | 0/5 | スキップ（非AI・書評） | — |
| daringfireball.net | The Fourth Horseman… (Microsoft MD in SharePoint) | 0/5 | スキップ（非AI・ファイル形式）※未保存 | — |
| corporate.walmart.com | Tap to Pay at Walmart / Sam's Club | 0/5 | スキップ（非AI・決済） | — |
| techcrunch.com | Bluesky's active user base is shrinking | 0/5 | スキップ（非AI・SNS） | — |
| daringfireball.net | When New DF Posts Drop in a Forest | 0/5 | スキップ（メタ論考） | — |
| bsky.app | Bluesky Is Full of Anti-AI Zealots | 0/5 | スキップ（非AI・SNS） | — |
| timmarinin.net | How Bluesky & Threads Sneak Logos Into Screenshots | 0/5 | スキップ（非AI・UI） | — |
| daringfireball.net | Apple / EC DMA app payment terms | 0/5 | スキップ（非AI・規制） | — |
| Bloomberg | Gurman: No camera AirPods until 2027 | 0/5 | スキップ（非AI・ハード）※未保存 | — |

## AI-Relevant Ingest Summary

Today's scan had **4 clearly AI-relevant articles** (plus a release-note pair bundled into the Simon Willison page). All were ingested as **enrichments to existing pages** — no new entity/concept pages were created, since each article extended a topic already well-covered in the wiki:

1. **Gary Marcus — "Data center madness" (Aug 21)** → the day's highest-signal article.
   - Added an **"August 2026 Update: Data Center Madness"** section to `concepts/ai-bubble-economics.md` with two independent revenue-requirement estimates (Berezin **~$10T**, Williams **~$2.5T**) against a projected **$1T 2027 hyperscaler capex**, and Marcus's new **political-economy** angle (Republican-aligned communities "abandoning data centers").
   - Cross-linked `concepts/subprime-data-center-crisis.md` ↔ `concepts/ai-bubble-economics.md` and bumped both `updated` fields.
   - Added a post-analysis section + frontmatter source to `entities/gary-marcus.md`.

2. **matklad — "Rust Glancer" (Aug 21)** → `entities/matklad-github-io.md`.
   - New **"Rust Glancer: A Three-Tier Analyzer Architecture"** section: critique of rust-analyzer's rowan+Salsa-over-all-dependencies model, the IntelliJ PSI three-backend template (syntax trees / Stub Trees / `.rmeta`), the "rmeta-transparent" prerequisite, a Sorbet-style plugin to avoid running proc macros, and the "half-drawn horse" framing. Cross-referenced his LSP and query-based-compiler essays.

3. **Simon Willison — "Stop Making TUIs" + release notes (Aug 21)** → `entities/simon-willison.md`.
   - **"Stop Making TUIs"**: Thomas Ptacek's argument that coding agents have driven the cost of a usable GUI to near-zero, so the CLI/TUI cheap-default economics no longer hold. Explicitly contrasted with matklad's "lower to plain text" IDE philosophy (the two bracket the UI-cost frontier).
   - **llm 0.32.1 / llm-openrouter 0.7** release notes (httpx/openai<3 stopgap; OpenRouter reasoning traces).

4. **Sean Goedecke — "You should never be angry at work" (Aug 21)** → `entities/seangoedecke-com.md`.
   - New section framing the post as the **emotional-regulation** corollary to his recurring "name the specific friction" pattern (just-say-no engineer = institutional, keep-thinking = cognitive, angry-at-work = emotional), and to his "AI isn't the root cause of most engineering pain" thesis.

**Index & log**: `wiki/index.md` (6 entries updated) and `wiki/log.md` (1 dated entry appended) both updated.

## Unsaved Articles
- **Bloomberg** — "Gurman Says No Camera-Equipped AirPods Until 2027" (paywall).
- **Microsoft Tech Community** — "Introducing markdown support in SharePoint and OneDrive" (JS-heavy, scrape failed).
