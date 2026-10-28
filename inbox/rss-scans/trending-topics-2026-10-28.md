# AI トレンドトピックスレポート — 2026-10-28 (12:00 UTC)

## スキャン概要

- **RSS ブログスキャン**: 36件新規検出 / 20件セーブ（blog_ingest 10:00 UTC）
- **ニュースレター**: 3通（「Was Kimi's Hype Secretly Paid For?」等）— newsletter-triage 済み（take 7件、本日朝パイプラインで処理済）
- **HN Algolia**: front page 30件（2日分）+ AIキーワード検索（3日分、80pts以上）の2パス
- 午前パイプライン（blog-ingest 10:00 / newsletter-triage 10:10 / active-crawl 11:00 UTC）で Anthropic S-1・ETH反証・GPT-6.1 Terra・Survival LLM・Anthropic創薬・価格崩壊・ abliterated DeepSeek は既に収録済み。本レポートは未収録ハイライトの発掘と収録状況の棚卸しが主目的。

## トップトピック（Newsjacking スコア付き）

### 1. 【本日新規収録】Google DeepMind「Genie 4」発表 — ネイティブ音声付きリアルタイム世界モデル 🔥 NJ 5/5
- HN **920pts/532c** — 2026-10-27発表（Raia Hadsell ら）。DeepMind の第4世代ワールドモデル
- 4つの前進: ①フォトリアル+リアルタイム対話的シミュレーション ②物理・人間動作の現実性（最大の飛躍はキャラクター）③**ネイティブ音声生成**（環境音・音楽・リアルタイム対話話者を同時生成する初のリアルタイム世界モデルと主張）④自然言語による実行中の世界へのリアルタイム介入
- アーキテクチャが要点: **Gemini 3.8 Flash がループ内の guide agent** として場景観察→目標分解→フレーム検証→再計画を担い、Gemini Omni が実世界の外観・挙動を接地。プランナー（LLM）+ レンダラー（Genie）への分離は「ハイブリッド世界モデル」路線そのもの
- Gemini 4 Argon + Gemini Robotics 実験（Apptronik Apollo がチェッカーをする課題分解シミュレーション）→ ロボットの学習環境としての明示的なポジション
- 配布は trusted tester + Google AI Ultra（Project Genie）+ Gemini API/AI Studio早期アクセスのresearch preview。ベンダー選定プロンプトのみなので定性的主張は confidence: medium
- **収録**: ✅ 本レポート作成時に新規収録 — `concepts/genie-4.md` 作成、`entities/deepmind.md` にセクション追記、raw記事保存

### 2. 【本日新規収録】Anthropic、スタンフォード教授陣の書を海賊版で学習 — Bartz後の「脱退組」訴訟 Cruz v. Anthropic 🔥 NJ 5/5
- HN **529pts/277c** — Stanford Daily 10/27報道。連邦判決（2026年5月）で Anthropic がスタンフォード教授10名超の書を無許諾スクレイプ・海賊版でClaude学習に使用と認定
- Bartz $1.5B和解（約$3,000/冊、約50万タイトル）から**脱退**した Tobias Wolff・Chang-rae Lee らが2026年5月に提起した非クラス訴訟。**法定賠償 最大$150,000/冊**（和解額の約50倍）と恒久差止を求める
- 主張はBartzと同一構造: LibGen / PiLiMi 等のシャドーライブラリからのダウンロード+恒久的中央ライブラリ構築（Alsup判事が海賊版側で違法とした行為）。勝訴なら対象作品のClaude学習への恒久使用差止
- 背景: AI企業に対する侵害訴訟は70件超（NYT、Getty含む）、Authors Guild は OpenAI/Microsoft 訴訟と並行して連邦議会でのライセンス立法を推進。Goldstein（スタンフォード法学部）は「取引費用」問題として構造化
- **収録**: ✅ 本レポート作成時に新規収録 — `concepts/cruz-v-anthropic.md` 作成、`concepts/anthropic-copyright-settlement.md` にセクション追記、raw記事保存、SCHEMAタグ+1（`cruz-v-anthropic`）

### 3. Claudeの学習データ利用ポリシー確認ページがHN上位 — 「商用はデフォルト非学習、フィードバックは5年保存」 NJ 2/5
- HN **219pts/105c** — privacy.claude.com の公式ポリシーページが話題化
- 商用（Claude for Work / API / Gov）はデフォルトで入力・出力を学習に使用しない。ただし**thumbs up/down フィードバック送信中は会話全体を最長5年保存**し学習に使える（ユーザー・顧客IDからはデリリンク）。コネクタ由来の生コンテンツは含まれないが、会話はがコピーされていれば含まれうる
- 企業側は Rate chats 設定でメンバーのフィードバック送信自体を無効化可能。単なるポリシー原文だが、S-1提出期とStanford海賊版報道の直後に「自社データの扱い」がHNで上位化した点に注目価値
- **収録**: 独立ページの閾値未満のためスキップ → 本レポートに記録のみ（既存 `concepts/ai-code-provenance-in-open-source` / プライバシー系ページと関連）

### 4. Hob — Claude Cowork / ChatGPT のオンデバイスOSS代替がShow HN上位 NJ 3/5
- HN **170pts/42c** — FrigdeHQ/hob（GitHub）。クラウド不要のローカルAI同僚デスクトップ
- 昨今のローカル第一潮流（Survival LLM 384pts、Apple M6/M5 Ultra on-device、on-device 5 providers abliterated DeepSeek）と同系列のShow HN。まだリリース初期でページ閾値未満
- **収録**: スキップ（Show HN製品・閾値未満）→ 本レポートに記録のみ

### 5. IBM CEO「オープンウェイトモデルは十分に良く、安い」— オンプレ移行の経営層言及 NJ 3/5
- HN **423pts/335c** — The Register。Arvind Krishna CEOがオープンウェイトの実用性を経営層として公然評価
- 既存ページ `entities/ibm.md`・`concepts/open-weight-vs-closed-llm-gap`・`concepts/llm-price-collapse-2026` と直結する続報だが、単独ページ化ほどではない（CEO発言一件）。次回該当ページのエンリッチ候補
- **収録**: 記録のみ（既存ページ充実時に引用候補）

### 6. 昨日からの継続トピック（午前パイプラインで収録済み）✅
- **Anthropic S-1（SEC公開提出、Nasdaq "ANT"）**: HN 1,697pts — `entities/anthropic.md`「Public S-1 Filing」セクション収録済（active-crawl 11:00）
- **OpenAI 数学攻勢（ETH反証+3新発見）**: `concepts/openai-eth-refutation-verification-crisis.md` 収録済
- **GPT-6.1 Terra**: `entities/gpt-6-1-sol` / `entities/openai` に収録済、朝のhot-postでもcross-check済
- **Survival LLM / Anthropic創薬 / Liquid LFM3 / Benchmarking Crisis**: active-crawl 11:00 UTCで新規ページ化済
- **10年前のCNNが皮膚がん診断でfrontier LLM撃破**: `concepts/specialist-model-superiority.md` に収録済（昨日のレポート）
- **LLM価格崩壊（最大80%減）**: `concepts/llm-price-collapse-2026.md` 収録済

## その他ハイライト

- **r/opensource がLLM使用プロジェクトを全面禁止**（HN 90pts）— OSSのAIプロヴェナンス論争の続編。既存 `concepts/ai-code-provenance-in-open-source` の追記候補
- **Brown大学生がAIを支える見えないグローバル労働を地図化**（HN 182pts, Brown大学ニュース）— `concepts/labor` 系の続報候補
- **PaperPilot**（HN 236pts）— クラウドゼロのPure-Rust PDFエンジン+WASM+MCP。Show HN製品として記録のみ
- **Ghostty 1.4**（HN 1,083pts）— Mitchell Hashimoto のターミナル。開発者ツールだがAI文脈外。既存 `entities/mitchell-hashimoto-ghostty.md` あり

## ウィクション推奨アクション

| トピック | 状態 | 対象ページ |
|---|---|---|
| Genie 4 ワールドモデル | ✅ 本日収録 | `concepts/genie-4.md` + `entities/deepmind.md` |
| Cruz v. Anthropic 脱退訴訟 | ✅ 本日収録 | `concepts/cruz-v-anthropic.md` + `concepts/anthropic-copyright-settlement.md` |
| Claude 学習データポリシー | 📝 記録のみ | （閾値未満） |
| Hob on-device 代替 | 📝 記録のみ | （Show HN・閾値未満） |
| IBM CEO オープンウェイト発言 | 🔄 追記候補 | `entities/ibm.md` / `concepts/open-weight-vs-closed-llm-gap` |
| r/opensource LLM禁止 | 🔄 追記候補 | `concepts/ai-code-provenance-in-open-source` |
| Anthropic S-1 / ETH / Terra ほか | ✅ 午前パイプライン収録済 | （active-crawl・hot-post 参照） |

## 所感

本日の主役は二つとも「AIの材料をどこから持ってくるか」の問いだった。DeepMind は Genie 4 で世界そのものを生成しロボットの学習環境にすると宣言し、他方で Anthropic は学習材料の海賊版起源が司法に再認定された。生成側が「シミュレーションでデータを創る」方向へ進むほど、取得側の法的リスクが相対的に高まる対比。Cruz 訴訟の $150k/冊 要求は Bartz 和解で閉じたはずの負債の尾部がまだ開いていることを示すため、続報（陪審・差止）は優先度高でウォッチしたい。
