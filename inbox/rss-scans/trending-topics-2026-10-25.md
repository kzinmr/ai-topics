# Daily Trending Topics Report — 2026-10-25

> 生成: 2026-10-25 12:00 UTC (trending-topics cron)
> 入力: blogwatcher RSSスキャン (24h: 55記事 / 24ブログ), HN Algolia (front page + keyword, 2-3日窓), ニュースレター1通 (OpenAI offline RL), 追跡Xアカウント (10/23スキャン分)
> 午前パイプライン (blog-triage 0takes/7refs, newsletter-wiki-ingest, active-crawl 4概念) は済み。本レポートは HN 側の未収録トピックを重点抽出。

## 🏆 本日のトップピック

### 1. Apollo首席エコノミスト「Tech業界の外にAIのリターンはゼロ」— 今月最大のマクロ懐疑データ
- **ソース**: Apollo / Torsten Slok (Chief Economist), The Daily Spark 2026-10-24
- **HN**: 562pts / 596c — https://news.ycombinator.com/item?id=50224463
- **要点**: 従業員一人あたり売上・利益率は Mag 7 だけ上昇、**S&P 493 は横ばい**。TFP (SF Fed Fernald系列) にもAI由来の生産性向上は未検出。企業はトークン支出を「成長源でなくマージンを削るコストセンター」と再定義し始め、VC系企業以外の支出が鈍化。「AIは優れた計算機だが、ビジネスでの知能の本体は judgment (文脈・説明責任・信頼・暗黙のルール)。AIストーリーは Mag 7 ではなく S&P 493 で決着する」
- **意義**: AIバブル論争の経験的ブックエンド。capex/トークン支出は爆増するも需要側がP&Lに転換できていない。
- **Wiki**: ✅ 本日収録 → `concepts/ai-economics.md` (S&P 493 Test セクション新規)

### 2. アメリカの「クリエイティブ階級」20万人減 — 後退する雇用とAIの相関
- **ソース**: Apricitas Economics (Joseph Politano)「AI and the Fall? of the Creative Class」
- **HN**: 384pts / 396c — https://news.ycombinator.com/item?id=50226419
- **要点**: 4年間でメディア・映画・芸術関連の雇用が **20万人以上減少** (この1年で約5万人)。映画・音声録音 (ハリウッド) は **10万人超 = セクターの約1/3**、出版は7万人減。対照的に **リアル体験型エンタメは堅調に成長** — 生成AIが代替可能な「デジタルプロデュース可能」職種のみが縮小しているのがAI帰属の最強根拠。帰属留保: メディア各社は **著作権の法的根拠保全** のためAI利用を秘匿する誘因を持つ。
- **意義**: 「コストライン (解雇) にはAIが見えるが、売上ラインにはまだ見えない」— トピック1と対で読むべき先行指標。
- **Wiki**: ✅ 本日新規作成 → `concepts/creative-class-job-loss.md`

### 3. 「なぜAI生成文は読みにくいのか」— 心理言語学が初めて定量測定
- **ソース**: arXiv:2610.29162 (cs.CL)
- **HN**: 209pts / 172c — https://news.ycombinator.com/item?id=50223647
- **要点**: 人間の処理負荷と相関する言語特徴 (目的関係節、長い統語依存、低頻度n-gram、非生主语+生物動詞) を9つのフロンティア/ニアフロンティアモデルで測定。**全モデルが人間執筆より難しい特徴を多用** (往復訳パラフレーズより多い)。仮説: 人間の言語は「伝達」に最適化されるが、LLMは math/code/reasoning の目的関数下で **information density (情報密度)** に最適化される → 長さペナルティ微调で人間的挙動から乖離する PoC を実証。モデルファミリー間の差も大きい。
- **意義**: 「AIスロップは読みにくい」という体感不満の初の系統的測定。post-training目的の設計課題として定式化。
- **Wiki**: ✅ 本日新規作成 → `concepts/ai-generated-language-readability.md`、`concepts/ai-slop.md` にも追記

### 4. Cerebrasが万亿パラメータ展開の中身を全公開 — Kimi K3 (3T) は WSE-3T 59枚
- **ソース**: Cerebras 公式ブログ「How we deploy Trillion-parameter frontier models」(Oct 22)
- **HN**: 204pts / 65c — https://news.ycombinator.com/item?id=50227356 (10/25アゲイン)
- **要点**: WSE-3T 1枚 = 44GBオンチップSRAM。Kimi K3 (~3T, 69 linear-attn + 24 dense層) を4-bit量子化すると **約16GB/層** → dense層はKVキャッシュと同居のため1層/ウェハ、linear層は固定サイズ状態なので2層/ウェハ → **計59ウェハ**をパイプライン接続。ウェハ間はアクティベーションのみ **RDMA (~2µs/hop)**、重みは移動せず。マイクロバッチ充填で **1000-2000+ tok/s**。Cerebras側ベンチ: Terminal-Bench 2.1 88.3% / BrowseComp 91.2% (GPT-5.6 Solに拮抗)。
- **意義**: 「ウェハスケール×オープンウェイト×最速サーブ」ポジションの技術的裏付け公開。
- **Wiki**: ✅ 本日更新 → `concepts/cerebras-cs4.md` (+59ウェハ算術セクション)、`concepts/kimi-k3.md`

### 5. Samsung TV が TensorFlow Lite で視聴者をトラッキングか (進行中・一次情報thin)
- **ソース**: X (@mike64_t) でのTXR55HモデルのTF Lite推論リバースエンジニアリング
- **HN**: 44pts (10/25、急上昇中) — https://news.ycombinator.com/item?id=50230181
- **要点**: 960×540画像入力のTensorFlow LiteモデルがTV側で人物/視聴追跡を実行している疑い。Edge AIのプライバシー問題の家庭機器への波及事例。本文はXスレッドのみで一次情報未取得 — 続報待ち。
- **Wiki**: ⚠️ 未収録 (続報確認後に agent-privacy / on-device 文脈で収録候補)

## 📌 その他の注目 (スコアリング済み・スキップ判定)

| ソース | タイトル | NJ | アクション | 理由 |
|--------|----------|----|------------|------|
| HN 1066p | Kimi K3.1 Pro / Highspeed | 5/5 | ✅ 済み | `concepts/kimi-k3` (K3.1 Proセクション, 10/24更新済み) |
| Anthropic | LLMで形式的検証が大規模に現実的に | 4/5 | ✅ 済み | `concepts/formal-verification-llm-agents` (10/22収録) |
| Block/Dessa | 音声のみで訓練した対話モデル | 4/5 | ✅ 済み | `concepts/dessa-speech-only-model` |
| NVIDIA | OpenShell (agent fleetランタイム) 499p | 4/5 | ✅ 済み | active-crawl が本日 `concepts/nvidia-openshell` 作成 |
| ModelCompare | 全モデルが人間について同じ「物議」見解 | 4/5 | ✅ 済み | `concepts/model-collapse-of-viewpoints` |
| OpenAI | フロンティア訓練環境のセキュリティ | 3/5 | ✅ 済み | `concepts/frontier-training-environment-security` (昨日収録) |
| Berget AI | 同じリクエストでTXはスウェーデンの8.5倍CO2 | 3/5 | ✅ 済み | `concepts/per-request-ai-carbon` |
| Swedish Radio | スウェーデン政府機関がChatGPT/Claude禁止 | 3/5 | 収録候補 | sovereign-ai 側で言及あり、個別ページは次回検討 |
| Aikido | Node2Shell→HTTP2Shell (CVE-2026-111497) 波及拡大 | 3/5 | 収録候補 | 本文がマーケ色の強いCMS描画のため次回 browser系で再取得 |
| AI Engineer | Bloomberg「実被害を受けたAIエージェント攻撃と防ぎ方」 (動画) | 3/5 | 収録候補 | `ai-agent-safety-incidents` の続報として字幕取得価値あり |
| GitHub GVS5H | Qwen3.8-27B 5種が Fable 5 に「対抗」 Claims | 2/5 | スキップ | ベンチ検証不能なコミュニティ主張 (benchmark-framing 注意) |
| seangoedecke.com | Don't anthropomorphize big tech companies | 2/5 | ✅ 済み | blog-wiki-ingest が10:00に収録済み |
| danluu.com | We should be more ambitious with the software we build (479p) | 2/5 | 非AI | 一般ソフト開発論。エンティティ danluu 更新候補 |

## 🗞️ ニュースレター / X
- **The Offline World (10/25)**: OpenAI がフロンティアモデルのRL訓練を「Webのオフラインキャッシュ内」で実施 — 昨日 `events/2026-10-23-openai-offline-frontier-rl-2026.md` として収録済み ✅
- **追跡X (10/23 scan)**: KURE-v3/Sparse 多言語retrievalツールキット公開、Hamza Farooq AI Powered Search登壇など。目立つ単発ニュースはなし。

## 📊 ウィクション推奨アクション
- ⚠️ 未収録 (次インジェスト候補): ①スウェーデン政府のChatGPT/Claude禁止 (sovereign-ai or ai-governance)、②HTTP2Shell (supply chain 拡散状況の続報)、③Samsung TV TF Lite追跡 (続報待ち)、④Bloomberg AIエージェント攻撃実例 (動画字幕)
- 午前パイプライン重複は確認済み — active-crawl の4概念 (Mistral Large 4 / OpenShell / ThinkingCap / persona-conditioned security degradation) とは冲突なし。

## 収録サマリー (本run)
- 新規: `concepts/creative-class-job-loss.md`, `concepts/ai-generated-language-readability.md`
- 更新: `concepts/ai-economics.md`, `concepts/cerebras-cs4.md`, `concepts/kimi-k3.md`, `concepts/ai-slop.md`
- raw記事: 4本 (cerebras / apollo-slok / apricitas / arxiv-2610.29162)
- SCHEMAタグ追加: wafer-scale-inference, pipeline-parallelism, information-density, psycholinguistics, ai-payoff, creative-class, labor-displacement
