# Trending Topics Report — 2026-10-26 (12:00 UTC)

データ源: blog_ingest (10:03 UTC, 16件), newsletter-ingest (4通/20記事), HN Algolia (front page + AI keyword, 2日分), 本日午前のパイプラインコミット履歴。

## 📰 上位トレンド (Newsjacking スコア付き)

### 1. LLM価格崩壊 — OpenAI/Anthropicが数か月で最大80%値下げ (NJ 4/5)
- Max Woolf (minimaxir) の分析。HN 344pts/333c。キャッシュ読み取りがエージェント支出の96-99%を占めており、実際の戦場は cache-read 価格。29プロバイダの OpenRouter  commodity 化チェックと IPO タイミングの逆説も。
- 今朝の active-crawl で `concepts/llm-price-collapse-2026` として収録済み ✅
- HN: https://news.ycombinator.com/item?id=50236102

### 2. Gheist: 盗難GitHubトークンによる CI/CD シークレット大規模抜き取り (NJ 4/5)
- Wiz のレポート。`toJSON(secrets)` を base32 でエンコードしてログマスキングを回避、environment マトリクスで本番シークレットまでダンプ。抜き取りは GitHub 自身の API 経由なので遮断点が無い。
- 2026-07-28 からの「公開リポジトリの承認保留」は機能したが、**プライベートリポジトリと GHES は無防備**（CloudTrail でのみ検出可能）。
- セルフホストランナーの掃討ジョブは **Anthropic/Hugging Face/Groq/NVIDIA の AI プロバイダ鍵を明示的に収集** — エージェント時代ならではの標的。
- → 新規 `concepts/github-actions-secrets-exfiltration.md` 作成 ✅ (raw 保存済み)
- HN: https://news.ycombinator.com/item?id=50235010

### 3. IBM CEO「オープンウェイトはオンプレで抗しがたく安く良い」 (NJ 3/5)
- Arvind Krishna: フロンティアの約90%の性能を10%の価格で、2〜3ラックで。HN 291pts/199c (10/26)。企業側のオープンウェイト採用経済性の公言という需要側シグナル。
- → `concepts/open-weight-vs-closed-llm-gap` にセクション追加 ✅
- HN: https://news.ycombinator.com/item?id=50238088

### 4. 10年前の CNN がフロンティア LLM を皮膚がん診断で上回る (NJ 4/5)
- lynchlab.net。HN 581pts/246c (10/25)。特定ドメインでは古い専用モデルが汎用フロンティアに勝つ代表例 — 専用モデル優位トレンド（今朝収録の specialist-model superiority）と直結。
- raw は本日 blog パイプラインが保存済み (`2026-10-26_lynch_CNN-vs-LLM-skin-cancer-diagnosis.md`)。
- HN: https://news.ycombinator.com/item?id=50233779

### 5. 「认知重商主義」— AI パニックは初期資本主義への恐怖の写像 (NJ 4/5)
- Venkatesh Rao (Contraptions)。富→知能の4項対応（固定資源論/認知エリート支配/供給側偏重/「无用な頭脳」誤謬）。農業革命が「无用な口」予測を否定した歴史的反例。
- → 新規 `concepts/cognitive-mercantilism.md` 作成 ✅。`creative-class-job-loss`（実証的置换脅威）と対立する反証ペアとして位置づけ。
- HN: https://news.ycombinator.com/item?id=50239027

### 6. Cerebras が兆パラメータモデル運用の技術詳細を公開 (NJ 3/5)
- Kimi K3 (~3T) を WSE-3T 59ウェハで、4-bit/層16GB、RDMA パイプライン、1000-2000+ tok/s。HN 356pts/135c。
- → 今朝 active-crawl が `concepts/cerebras-cs4` に追記済み ✅
- HN: https://news.ycombinator.com/item?id=50227356

### 7. テリー・タオが OpenAI 数学証明のコミュニティ訂正ハブ「oai-math-revised」開設 (NJ 3/5)
- LLM 生成数学に対するコミュニティピアレビューという品質管理モデル。9月の「Severe Misalignment Declaration」の延長線上。
- → `entities/terry-tao.md` 更新 ✅ (本文は本文未取得だったが HN 52pts と過去記事から文脈補完)
- HN: https://news.ycombinator.com/item?id=50222283

### 8. Microsoft Decision-1: Qwen3.5-9B ベースの「決定特化」9Bモデル (NJ 3/5)
- チャットしない。固定選択肢に単一 forward pass で較正付き確率を返すだけ。$0.042/1M input、出力無料。ルーティング/分類/検証用。ベースが中国製オープンウェイト（Microsoft は将来 MAI/OpenAI に rebase 予定と明言）という構造が興味深い。
- ⚠️ 未収録 — shattering.io 二次情報。次インジェスト候補。
- HN: https://news.ycombinator.com/item?id=50238620

## 📊 ウィクション推奨アクション

| トピック | NJ | ステータス | 対象 |
|---|---|---|---|
| LLM価格崩壊 80% | 4 | ✅ 済み (active-crawl) | concepts/llm-price-collapse-2026.md |
| Gheist シークレット抜き取り | 4 | ✅ 今回作成 | concepts/github-actions-secrets-exfiltration.md |
| IBM オープンウェイト発言 | 3 | ✅ 今回追記 | concepts/open-weight-vs-closed-llm-gap.md |
| CNN vs LLM 皮膚がん | 4 | raw 済み / 概念ページ未収録 | 次候補: specialist-model superiority に追記 |
| 认知重商主義 | 4 | ✅ 今回作成 | concepts/cognitive-mercantilism.md |
| Cerebras 3T 運用 | 3 | ✅ 済み (active-crawl) | concepts/cerebras-cs4.md |
| oai-math-revised | 3 | ✅ 今回追記 | entities/terry-tao.md |
| MS Decision-1 | 3 | ⚠️ 未収録 | 次インジェスト候補 |

## 📋 その他の観察
- r/opensource が LLM 使用プロジェクトとソロプロジェクトを全面禁止 (HN 88pts/111c) — OSS コミュニティの LLM 疲れの象徴事例。HN: https://news.ycombinator.com/item?id=50231722
- UC バークレー数学教授、AI 普及で「宿題を採点する意味がない」 (HN 220pts/320c) — 教育評価の再設計議論。HN: https://news.ycombinator.com/item?id=50233304
- ニュースレター4通処理（Kimi K3.1 Pro 中心、今朝の hot-post で収録済み）。
- 本日午前パイプライン: active-crawl 4概念、blog triage 9件、Kimi K3.1 Pro 収録済み — 重複作成なし。

## 変更ファイル
- NEW: concepts/github-actions-secrets-exfiltration.md, concepts/cognitive-mercantilism.md
- NEW raw: wiz.io Gheist, contraptions cognitive-mercantilism (sha256 計算済み)
- UPD: concepts/open-weight-vs-closed-llm-gap.md, entities/terry-tao.md, SCHEMA.md (tags: secrets-exfiltration, github-actions, ai-panic), index.md, log.md
