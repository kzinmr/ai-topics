# Trending AI Topics — 2026-08-29

> 定期スキャン（HN Algolia Aug 26–29 全3スロット合算・blog_ingest/newsletter checkpoint・X bookmarks scan）。
> 大半は morning pipelines（active-crawl / blog-wiki-ingest / newsletter-ingest）で既に wiki 収録済み。
> 本レポートの新規ウィキアクション: **Terminal-Bench-Science 0.1**（下記1）。

## 📰 本日のトップトピック

### 1. Terminal-Bench-Science 0.1 — 科学者自作のエージェント科学ベンチマーク、最高得点わずか30% ⭐NEW
Stanford の Terminal-Bench チームが、ソフトウェア工学から**科学研究ワークフロー**へベンチマークを拡張（Aug 28、[HN 115pts](https://news.ycombinator.com/item?id=49472820)）。現役科学者が作成した70タスク（生命科学・物理・地球科学・数学・工学）、成果物（解析・シミュレーション・証明・コード）ベースの検証可能な採点、そして「論文リリースで放置」ではなく**連続的リリリース**を設計方針に掲げる点が特徴。
**リーダーボード**: Claude Opus 5 (Claude Code) **30.0%** / GPT-5.6 Sol (Codex) 22.4% / Claude Fable 5 21.4% — 最強モデルでも実研究タスクの1/3未満しか解けない。NanoGPT Speedrun と同じ harness×model レースの科学版。
→ ✅ 収録済み — `concepts/ai-benchmarks/terminal-bench.md`（新セクション）、raw: `2026-08-29_terminal-bench-science-0-1-announcement.md`

### 2. 「バグの噂だけでセキュリティエクスプロイトが見つかる時代」— Simon Willison
Cambridge 教授・OCaml メンテナ Anil Madhavapeddy の警告を Willison が紹介。AI エージェントによる噂レベルの情報からのエクスプロイト自動発見が現実化しつつある。
→ ✅ 収録済み — `concepts/security-in-the-ai-era.md`、`entities/simon-willison.md`（raw 保存済み）

### 3. Anthropic、NSA/DoD のブラックリスト化判断で claude.ai 個人利用を政府端末で解禁（WSJ）
政府のサプライチェーンリスク指定と個人利用解禁という矛盾した併存は、「エージェント経済圏」が政府調達枠組みと正面から衝突した象徴例。
→ ✅ 収録済み — `concepts/anthropic-dod-dispute.md`（2026-08-29 追記）

### 4. Anthropic Model Hardware Standard — 研究機器をエージェントが操作するための標準化プレビュー
HHMI Janelia 発祥、MCP 経由のモデル非標準ドライバ+読み書きプリミティブ。AWS Strands Robots、Universal Robots、Tecan 等がパートナー。物理世界の安全制約（Genentech の発泡事故例）も明文化。
→ ✅ 収録済み — `concepts/model-hardware-standard.md`（active-crawl が収録）

### 5. NanoGPT Speedrun 生中継で Fable 5 が記録更新（3:39、$74.35）— Opus 5 は 1000+ step で $753
Prime Intellect の公開中継セッション。同じ課題で**10倍のコスト差**という harness×model の効率的差が可視化。
→ ✅ 収録済み — `concepts/ai-benchmarks/nanogpt-speedrun.md`

### 6. AI データセンターバブル論争が金融メディアに本格拡散（WSJ/Bloomberg/Fortune/Business Insider）
OpenAI 830億ドル/monthly burn・Oracle の GPU リース解約・Nvidia の 7500億ドルバックログ論争・Nvidia の OpenAI 株 7.5% 留保・AMD-OpenAI 5GW・「Anthropic が今四半期初の黒字化」— 2008年危機类比・Minsky モーメント論・「AIバブルは実体経済に波及」まで。
→ ✅ 収録済み — `concepts/ai-data-center-crisis.md`、`concepts/openai-2026-revenue-growth.md`、`entities/nvidia.md`

### 7. GLM-5.2 が OpenRouter 米企業利用で首位に（SemiAnalysis）／AI 発明の特許性テストケース群（Ars Technica）
OpenRouter 公称利用の23%が米国企業＝Anthropic を除く全社合算超。米企業の実際のコモディティ化は重み付けなし推論マイグレーション。特許は Amaris v. Kaltura（CLI特許の抽象性）と Thaler DABUS 系の2軌跡で実務家向け整理が必要との評価。
→ ✅ 収録済み — `concepts/compute-and-hardware.md`、`concepts/patent-eligibility-ai-inventorship.md`

### 8. OpenAI、GPT-5.6 Sol の安全評価レポート公開 ／ arXiv: 推論モデルの RL 後訓練が safety 特性を侵食 ／ 隠れた思考のモニタリング劣化
OpenRouter で唯一 safety grade A 維持の GPT-5.6 Sol レポート、RL post-training による safety erosion、CoT monitoring の silent degradation — 推論モデル時代のアラインメント計測系トピックが一気に3本。
→ ✅ 収録済み — `concepts/model-reliability-and-safety-eval.md`

## 📊 ウィクション推奨アクション

| # | トピック | 状態 |
|---|----------|------|
| 1 | Terminal-Bench-Science 0.1 | ✅ 本レポートで収録（terminal-bench.md 更新 + raw 保存） |
| 2 | Willison / 噂からのエクスプロイト | ✅ 済み — security-in-the-ai-era.md |
| 3 | Anthropic-DoD 論争展開 | ✅ 済み — anthropic-dod-dispute.md |
| 4 | Model Hardware Standard | ✅ 済み — model-hardware-standard.md |
| 5 | NanoGPT Speedrun 更新 | ✅ 済み — nanogpt-speedrun.md |
| 6 | AI  data center バブル論争 | ✅ 済み — ai-data-center-crisis.md |
| 7 | GLM-5.2 / AI 特許 | ✅ 済み — compute-and-hardware.md, patent-eligibility-ai-inventorship.md |
| 8 | safety eval / CoT monitoring | ✅ 済み — model-reliability-and-safety-eval.md |

**未収録**: なし（本日の全 big topics は pipelines + 本レポートでカバー済み）。

## 📈 トレンド観察
- **harness×model リーダーボードの科学への拡張**（NanoGPT Speedrun → Terminal-Bench-Science）が今週の明確なメタトレンド。ベンチマークの「連続リリリース化」と「専門家による課題供給」が新潮流。
- **科学エージェント**（Station 数学発見、Molot Mol-Brake、DeepXiv、Terminal-Bench-Science）が週内で4件 — agents in science エリアの立ち上がり。
- **エージェント×物理機器**（Anthropic MHS、Factory 2.0 の robot foundation models、humanoid）も並行して太い流れ。

---
*Scan sources: HN Algolia (3 slots, Aug 26–29, ≥20pts), blog_ingest checkpoint (30 new articles), newsletter checkpoint (4 sources), X bookmarks (0 new). 本レポート: inbox/rss-scans/trending-topics-2026-08-29.md*
