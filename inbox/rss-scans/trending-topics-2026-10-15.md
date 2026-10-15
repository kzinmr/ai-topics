# Trending Topics — 2026-10-15 (12:00 UTC)

> HN front-page scan（2日窓・≥80pts）＋ keyword scan（4日窓・≥80pts / 13語）＋ 今朝の sibling pipelines（blog-ingest / active-crawl / newsletter / hot-post / x-bookmarks）との突合。
> 本レポートは **inbox/ 配下のみ**（ウィキ本文は未編集）。ウィキ作業は末尾の推奨アクション表に集約。

---

## トップトレンド（重要度順）

### 1. 「AIエージェントは暴走していない、フロンティアラボがセキュリティ基本をサボっている」— 今週最大の論争
- HN **916pts/551c**（10-14）。CSO Online の専門家コメント記事。最近の「AIハッキング報道」はエージェントの rogue 化ではなく **containment（封じ込め）と monitoring（監視）の実装不備**が原因だとする反論。
-NJスコア 4/5（Trend Surfing + Contrarian Insight + In-Group Signal）。既存の rogue-agent 言説（`concepts/rogue-ai-agent-activity`, `concepts/agent-collusion-public-infrastructure`「The Wiki Incident」, `concepts/security-and-governance/agent-containment`, `concepts/frontier-rl-safety-cases`）への **直接の反論軸** を加える記事で、ハブ追記に最適。
- ext: https://www.csoonline.com/article/4234854/ai-agents-arent-going-rogue-frontier-labs-are-skipping-security-basics.html ｜ hn: https://news.ycombinator.com/item?id=50091788
- 関連する法的論点として「Why aren't AI companies being charged for hacking?」（mortoray.com, 335pts/371c, 10-12, hn 50057278）も同時進行。

### 2. Cohere「フロンティア・コーディングエージェントのチーム運用」— 今日の raw、ウィキ未反映
- 今日の blog-ingest が `wiki/raw/articles/2026-10-15_cohere_lessons-from-scaling-teams-of-frontier-coding-agents.md` を保存済みだが **ウィキ本文には未反映**。
- 論旨: エージェント・チームは ProgramBench で単一エージェント比 **+10pt** だがコスト **3〜7倍**。「強い lead ＋ 安い worker（Sol lead ＋ Luna worker ×16）」で全 Sol チーム並みの性能を **70%減コスト**（$510→$155、reward 61.8% vs 63.2%）で達成。**エージェントの配置先（探索・計画のみに委任）が総数より効く**。
- 既存 `concepts/multi-agents/` hub・`concepts/ai-benchmarks/programbench` と直結。追記 or 小ページ新設が正当。
- ext: https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents

### 3. Codex CLI がデフォルトで永続・自己更新バックグラウンドデーモンをインストール（問題化）
- HN **606pts/292c**（10-12）。OpenAI Codex の GitHub issue #48195。coding agent のデフォルト挙動として「常駐・自動更新する裏プロセス」を入れることへの同意性（supply-chain / consent）批判。
- 既存 `entities/codex` / `concepts/codex/codex-safety` / `concepts/codex/codex-harness-controls` / `concepts/agent-skill-supply-chain-attacks` へ追記候補。NJスコア 3/5（In-Group + Pattern Interrupt）。
- ext: https://github.com/openai/codex/issues/48195 ｜ hn: https://news.ycombinator.com/item?id=50060694

### 4. OpenCode 2.0 リリース
- HN **669pts/264c**（10-14）。オープンソース coding agent harness の大型アップデート。既存 `entities/opencode`（updated 10-09、OpenCode fork である `entities/kilo` も隣接）に **追記で足りる**（新設不要）。
- ext: https://anoma.ly/notes/opencode-2-0/ ｜ hn: https://news.ycombinator.com/item?id=50094994

### 5. Liquid AI LFM2.5-24B-A2B — on-device エージェント向け疎モデル
- HN **232pts/54c**（10-14）。既存 `entities/liquid-ai` / `entities/liquid-ai-lfm2-5-retrievers` 家系の新型。A2B（active-2B）MoE で高速オンデバイス・エージェント推論を狙う。`entities/liquid-ai` に追記。
- ext: https://www.liquid.ai/blog/lfm2-5-24b-a2b ｜ hn: https://news.ycombinator.com/item?id=50097369

### 6. Linus Torvalds の初の LLM 支援パッチシリーズ（LWN）
- HN **116pts/98c**（10-14）。カーネル界の重鎮が LLM 支援パッチを初めて出したという象徴的事件。既存 hub `concepts/ai-coding-effectiveness-debate` / `concepts/ai-coding-reliability` の論点（Linus の「AI が諦めない debug session」発言は `entities/simon-willison` に既収録）へ追記で吸収可能。
- ext: https://lwn.net/Articles/1100449/ ｜ hn: https://news.ycombinator.com/item?id=50090842

### 7. OpenAI 幹部会議室の盗聴事件 — 技術外だが業界ノイズ大
- HN「OpenAI engineer arrested in bugging of executive conference room」**648pts/538c**（10-13）＋「OpenAI finds recording device」**85pts**。技術トレンドではないためウィキ対象外（provenance bar で drop）。記録のみ。
- hn: https://news.ycombinator.com/item?id=50078141

### 8. AI 企業ボイコット論・ misc
- 「Just say no to OpenAI and Anthropic」（micahflee, 171pts/170c, hn 50060500）は既存 `entities/micahflee` の論点。
- 「TV4 postpones show after AI agent erases edited material」（148pts/84c, hn 50085323）は事故案例として `concepts/coding-agents/ai-coding-reliability` の逸話候補（低優先）。
- TypeSafe Jev 1.14.0（306pts, hn 50095353）は「dreamers」実験的機能。既存 `entities/typesafe-ai` / `concepts/system-one-models` に追記で足りる。

---

## 📊 ウィキ推奨アクション（priority 順）

| # | トピック | 新設/追記 | 対象ページ | 状態 |
|---|----------|-----------|-----------|------|
| 1 | AIエージェント「暴走」は封じ込め不備（CSO） | 追記 | `concepts/security-and-governance/agent-containment` + `concepts/rogue-ai-agent-activity` | ⚠️ 未収録（新論点） |
| 2 | Cohere エージェントチーム 30%コスト | 新設 or 追記 | `concepts/multi-agents/`（新小ページ候補） + `concepts/ai-benchmarks/programbench` | ⚠️ 未収録（raw は保存済） |
| 3 | Codex CLI 常駐デーモン問題 | 追記 | `concepts/codex/codex-safety` + `entities/codex` | ⚠️ 未収録 |
| 4 | OpenCode 2.0 | 追記 | `entities/opencode` | ⚠️ 未収録（updated 10-09） |
| 5 | LFM2.5-24B-A2B | 追記 | `entities/liquid-ai` | ⚠️ 未収録 |
| 6 | Linus LLM支援パッチ | 追記 | `concepts/ai-coding-effectiveness-debate` | ⚠️ 未収録 |
| — | Gemini 4 Argon / Karpathy 能力ギャップ / Ars「more code not software」 | — | `events/2026-10-01-gemini-4-argon-release` 他 | ✅ 昨日分レポートで既整理・ hubs 存在 |
| — | Scion / Modal mixed-precision RL / code-as-graph / 今朝の Canva-Go・Expedia-Go・ElevenLabs deepfake | — | 今朝の active-crawl / blog-ingest 収録済 | ✅ 済み |

**今週の新規ウィキ推奨は上表 1〜6。ただし trend-report cron の慣例どおり本 run では wiki/ 本文を編集せず、ingest pipelines（active-crawl 20:00 JST / blog-wiki-ingest）およびユーザー判断に委ねる。** 優先度 1・2・3 が最も actionability 高い。
