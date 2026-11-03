# Trending Topics — 2026-11-03 (12:00 UTC)

HN front-page + keyword + points>100 sweep（24h）、朝のパイプライン（newsletter-wiki-ingest, blog-ingest, active-crawl なし=本日ログ未见）と重複確認済み。

## 主要トピック（NJスコア順）

### 1. Weight-Space Programming — LLMがニューラルネット重みを「素読み・素書き」 (HN 2751pts/834c) NJ 5/5 ✅ wiki化済み
- MIT CSAIL（Takehi, Teoh, Zhang, Khattab）「Sparks of Weight-Space Programming」(11/02)。GPT-6 Astra が重み17,253個だけで学習ゲームを99%精度で当てる、環境フィードバックなしでPPO 100M步相当のゲーム用ネットを自作、Qwen3.5-0.8B の重み 0.016% を勾配なしで編集し MATH-500 7.9%→48.1%、IFEval 3倍。
- HN の争点: (a) RSI 再燃（「コード書き換えではなく重み手術で特異点経路が開いた」kristiandupont）(b) 明示的学習 vs 創発 (c) ツール使用の有無 (d) jailbreak/ablation との连续性（swiftcoder）。
- → 新規: [[concepts/weight-space-programming]]、raw 保存済み（HNコメント付き）。[[concepts/agi-declaration-controversy-2026]]・[[concepts/rome-weight-tampering-attacks]] 追記。
- 出典: https://rikiyat.github.io/blog/weight-space-programming/ · HN https://news.ycombinator.com/item?id=50341174

### 2. Anthropic IPO 財務開示ラッシュ — S-1修正・$895Bコミット・SECブロック論争 NJ 4/5 ✅ entities/anthropic 追記
- 修正S-1: Q3売上 $17B、Q3純損失 $23.3B（転換社債fair-value起因、恒常的との指摘）、**$895B の.compute/infraコミットメント** (HN 233pts)。ARR QoQ +47%（上半期100%+から減速、Blodget「成長が横ばいに」HN 213pts）。
- 社内AI使用量、小売価格換算で従業員給与総額超（Business Insider, HN 334pts）— リテール換算であって現金支出ではない、というツッコミ多数。「フロンティア企業は従業員1人あたり$300kの計算機会費用」論争。
- SECにIPOブロックを求める寄稿（Matt Scherer「Brace for Impact」共著、TechPolicy.Press, HN 366pts）— 循環取引・注記レベルの財務エンジニアリングが根拠。HN多数派は.blocking反対、少数派がインデックス強制買い歪みを指摘。
- → [[entities/anthropic]] 新セクション、[[concepts/ai-bubble-financial-crisis]] に11/2-3市場セクション（Oracle $20B社債+株式 HN 190pts・ピーク比-60%、Intel株崩壊/$3.5Tチップ安 HN 213pts）。
- 出典: HN 50337439 / 50344958 / 50344919 / 50339494 / 50342284 / 50346153

### 3. Agentic Backdoors via Pretraining Poisoning — 事前学習データ0.1%汚染でエージェントにRCEバックドア (HN 102pts) NJ 4/5 ✅ wiki化済み
- arXiv:2610.37741（Carlini, Jagielski ら、10/27提出）。Qwen3 をスクラッチ事前学習→クリーンな後処理でCLIエージェント化。汚染率0.1%で**ASR 92%（4B）**、0.0005%でも有意。トリガー出現時に攻撃者指定コマンド実行、通常入力は正常動作。
- HN: 「HFダウンロードは新版warez」（yodon）、「.weight-space programming が検出/植入の両輪になる」、「Anthropic系のプロパガンダ」vs「査読可能リサーチ」、ROI懐疑 vs ス턱スネット反論。防御はサンドボックス+オブザーバビリティに収束。
- → 新規: [[concepts/agentic-backdoors-via-pretraining-poisoning]]、raw 保存済み。
- 出典: https://arxiv.org/abs/2610.37741 · HN https://news.ycombinator.com/item?id=50341334

### 4. 「AGI & the City」11月クラスタ — Altman/Sutskever/Sahai/政府が同時AGI再定義 NJ 3/5 ✅ 新規ページ
- Altman「AI研究は主に経験科学に」（X経由・二手）／Sutskever「RLでは足りない、2027年に驚きが」／Sahai・Karthik・Xue「Egoless Mathematics in the AI Era」（Taoブログguest post、HN 167pts）／**EO 14434 で联邦AI表記が "Super Intelligence" に改称されCensus局が10/19調査から文言変更**（Simon Willison、HN 118pts）。
- 計測対象の名称を計測機器側に刷り込む構造的データインテグリティ問題（WillisonがApolloチャート更新で監視役）。
- → 新規: [[concepts/agi-and-the-city-agi-debate-2026]]、[[entities/terry-tao]] 追記。
- 出典: HN 50336840 / 50341736 · simonwillison.net / terrytao.wordpress.com

### 5. Revolut、セルフホストGLMへ移行 — $0.30/M tokens、Anthropic/OpenAIの1/10 (HN 103pts) NJ 3/5 ✅ 追記済み
- AI ops責任者David Abitbol: **Nvidia B200×56台**、ブレンド $0.30/M tokens ≈ 旧コストの1/10。企業ワークロードのうちフロンティア必須スライスの縮小、フロンティアラボの対抗（$2k/seatバルクプラン仮説）、B200減価リスク、データ主権動機。
- → [[concepts/self-hosting-ai-development]] 追記。
- 出典: HN https://news.ycombinator.com/item?id=50350004

### 6. OpenAI「Scaling Git」— エージェント起動コミット地獄か資産か (HN 239pts) NJ 3/5 △ 本文未取得(403)・関連ページ追記のみ
- openai.com/index/scaling-git-at-openai/ は urllib 403。HNスレッドから要約: Anthropic の「redesigning source control」への応答と読まれる。論争 = コード量増加はエージェント時代は資産（コードはエージェントが書きエージェントが読む）vs 負債（将来のコンテキスト汚染・AI slop）。
- → [[concepts/ai-agent-bureaucracy]] に共鳴セクション追記。本文は次回リトライ（GitHub/HN経由）。
- 出典: HN https://news.ycombinator.com/item?id=50345924

### 7. 昨日からのその他のAI関連ハイライト（レポーティングのみ）
- **Subvocal — 声を出さずに computer と対話する Show HN** (HN 721pts/345c) — サイレント音声入力の新UI経路。https://news.ycombinator.com/item?id=50340088 ⚠️ 未収録（候補）
- **Momentic (YC W24) Launch HN** — アプリを実際に使ってバグを拾うエージェント (HN 146pts)。https://news.ycombinator.com/item?id=50339913 ⚠️ 未収録（候補）
- **NVIDIA auto-ontology オープンソース化** (HN 108pts, 11/03)。https://news.ycombinator.com/item?id=50348962 ⚠️ 未収録（候補）
- **AIエージェントがマウスの脳外科手術を自律実施** (HN 137pts) — Exin Therapeutics、Opus 5が限界理解後に拒否したエピソードが好意的引用。https://news.ycombinator.com/item?id=50336138 ⚠️ 未収録（一次X投稿のみ・企業サイト起動せず）
- **Oracle $20B資金調達 / Intel株崩壊 $3.5Tチップ安** — 2項は上記#2のbubbleページに収録済み。

## ウィクション推奨アクション

| トピック | NJ | 状態 |
|---|---|---|
| Weight-Space Programming | 5/5 | ✅ 済み — concepts/weight-space-programming.md |
| Anthropic S-1/IPO争議 | 4/5 | ✅ 済み — entities/anthropic.md 追記 |
| Pretraining Poisoning バックドア | 4/5 | ✅ 済み — concepts/agentic-backdoors-via-pretraining-poisoning.md |
| AGI & the City クラスタ | 3/5 | ✅ 済み — concepts/agi-and-the-city-agi-debate-2026.md |
| Revolut GLM セルフホスト | 3/5 | ✅ 済み — concepts/self-hosting-ai-development.md 追記 |
| OpenAI Scaling Git | 3/5 | △ 関連追記のみ（本文403、次回リトライ） |
| Subvocal / Momentic / NVIDIA auto-ontology / マウス脳手術 | 2-3/5 | ⚠️ 未収録（候補） |

## 備考
- active-crawl は本日11:00ログ未见（log.md確認済み）。朝のnewsletter-wiki-ingestはRealtime-Bench・Figma PM OS・Duet 9-task benchmarkを収録済みで重複なし。
- openai.com 403 / X投稿2件は本文未取得を明記。Sutskever・Altman発言は二手情報としてconfidence注記済み。
- SCHEMA.md Models行に6タグ追加（weight-space-programming, model-editing, pretraining-poisoning, agentic-backdoor, anthropic-ipo, self-hosted-inference）。
