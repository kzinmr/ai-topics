---
title: "Hermes Agentをソフトウェア開発者のSecond Brainとして回す——設定・スキル・定期実行の実運用"
date: 2026-06-03
author: Hermes (kzinmr's AI Topics)
tags: [hermes-agent, knowledge-management, second-brain, harness-engineering, llm-wiki, ai-agents, blog]
sources:
  - concepts/llm-augmented-knowledge-retrieval.md
  - concepts/harness-engineering.md
  - concepts/agent-control-plane.md
  - entities/hermes-agent.md
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://mitchellh.com/writing/my-ai-adoption-journey
  - https://hermes-agent.nousresearch.com/docs
---

# Hermes Agentをソフトウェア開発者のSecond Brainとして回す

## 1. はじめに: 情報洪水の中で何を捨てるか

AI Agent領域の情報量は、2025年後半から指数的に増え続けている。arXiv論文、ブログ記事、X/Twitterの投稿、ニュースレター、YouTubeの講演録——毎日数十本の新しいソースが流れてくる。手動でこれを追い、整理し、必要なときに引き出せる状態にしておくことは、もはや不可能に近い。

私はAI Engineerとして、Andrej Karpathyの[LLM Wikiパターン](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)をAI/Agent領域の情報追跡・知識管理に適用している。その実行基盤としてHermes Agentを使い、約半年間、毎日自動で知識ベースを運用し続けている。

この記事では、Hermes Agentを「ただのチャットボット」ではなく、**設定を保守し、スキルを自動生成し、定期的に作業を回し続ける自律的なSecond Brain**として活用している実際の方法を紹介する。ターゲットはソフトウェア開発者——CI/CDパイプラインやIaCに馴染みがある人を想定している。

---

## 2. 全体像: 3層アーキテクチャとAgentic ETL

知識ベースの構造はKarpathyのパターンをほぼそのまま採用している。ファイルシステムを永続化層とし、Markdownを中間表現として使う。

```
raw/         ← Layer 1: 不変のソース素材（記事、論文、ニュースレター）
entities/    ← Layer 2: 構造化Wikiページ（人物、組織、製品）
concepts/    ← Layer 2: 概念ページ
comparisons/ ← Layer 2: 横断比較
SCHEMA.md    ← Layer 3: ページ規約・タグ分類学
index.md     ← Layer 3: 全ページのインデックス
```

ポイントは2つある。1つ目は、`raw/`は不変だということだ。ソース記事を編集することはなく、Agentが読み込んでWikiページを生成・更新する。2つ目は、全WikiページにYAML frontmatterが必須で、`tags`はSCHEMA.mdの分類学に従うという制約がある。これは後述するpre-commit hookで強制される。

現在の規模は以下の通り:

| ディレクトリ | ページ数 |
|---|---|
| entities/ | 751 |
| concepts/ | 1,550 |
| comparisons/ | 26 |
| **合計** | **2,327** |

この量の知識を手動で管理することは現実的ではない。Hermes Agentは、この知識ベースの作成・更新・検索・品質管理を自律的に行う。

---

## 3. 環境のセットアップ: 設計はファイルに、実行はAgentに

### 3.1 AGENTS.md: リポジトリのSingle Source of Truth

Hermes Agentの設定は、基本的にMarkdownファイルに書く。最も重要なのが`AGENTS.md`で、リポジトリのルートに置く。これは人間のためのドキュメントではなく、**Agentへの指示書**だ。

`AGENTS.md`には以下が含まれる:

- ディレクトリ構成とその役割
- Wikiの3層アーキテクチャと変更可能/不可のルール
- ページ作成・更新の手順
- Cronパイプラインの全体図（28ジョブの依存関係）
- 主要スクリプト一覧と対応するCronジョブ
- よくある失敗とその対処法

CI/CDで例えれば、`AGENTS.md`はリポジトリの`Makefile`や`docker-compose.yml`に相当する。Agentはこのファイルを読んで、リポジトリの構造とルールを理解する。

### 3.2 SCHEMA.md: タグ分類学とページ閾値

知識ベースの品質を保つための規約が`SCHEMA.md`に書かれている。内容は:

- **タグ分類学**: 10のプライマリカテゴリ（Models, People/Orgs, Products, Techniques, Engineering, AI Agents, Infrastructure, Meta, Domain Concepts）と、各カテゴリの正規タグ一覧
- **ページ閾値**: いつ新しいページを作るか（2+ソースで言及された場合）、いつ既存ページに追加するか、いつ分割するか（200行超）
- **frontmatter必須フィールド**: `title`, `created`, `updated`, `type`, `tags`, `sources`

### 3.3 Pre-commit Hook: Agentのミスをブロックする

.git/hooks/pre-commitに以下のバリデータを設置している:

1. **index.md検証**: ページ作成後にindex.mdが更新されているか
2. **タグ検証**: frontmatterのtagsがSCHEMA.mdの分類学に含まれているか

Agentが新しいページを作ったとき、タグを新規作成してSCHEMA.mdに追加し忘れることがあった。このpre-commit hookがそのミスをgit commit前にブロックする。Mitchell Hashimotoの言葉を借りれば、これはまさに「harness engineering」——Agentが同じ失敗を繰り返さないようにする足場だ。

---

## 4. Hermes Agentとの実際の仕事の仕方

### 4.1 ナレッジクエリ: 「wikiに聞いてみる」

日常的な使い方の一つは、知識の引き出し。質問が来たら、まず`wiki/index.md`から関連ページを探し、Wikiページだけで根拠が薄い場合は`raw/`のソースまで遡る。

例えば「GRPOの論文と実装の関係を整理して」と聞けば、Agentは:

1. `wiki/index.md`からGRPO関連ページを特定
2. `concepts/grpo-rl-training.md`や`entities/trl.md`を参照
3. 必要に応じて`raw/articles/`のソース記事も確認
4. 回答を返す。もし再利用可能な調査なら、`wiki/queries/`に保存する

重要なのは、**回答が一回で消えない**ということだ。調査結果はWikiページとして保存され、次に同じ質問が来たときに即座に参照できる。これは従来のRAG（検索拡張生成）とは異なるアプローチで、Karpathyが言う「compiled knowledge」としてのWikiだ。

### 4.2 記事取り込み: document → raw → wiki

外部の記事を取り込むときは:

1. 記事のURLを渡す（またはRSS/newsletterから自動取得される）
2. Agentが記事を`raw/articles/`に保存する
3. 記事の内容を分析し、既存のWikiページがあるか確認する
4. 既存ページがあれば更新、なければ新規作成する
5. `index.md`と`log.md`を更新する
6. git commit & pushする

このフロー全体が、人間の介入なしに自律的に実行される。

---

## 5. スキルの自動作成と適用: 経験をコードにする

Hermes Agentのスキル（Skills）は、**成功した手順とその落とし穴を構造化して保存する仕組み**だ。`.hermes/skills/`以下にSKILL.mdファイルとして管理され、次回以降の同様のタスクで自動的に参照される。

### 5.1 スキルはどのように生まれるか

典型的な流れはこうだ:

1. Agentが複雑なタスクに取り組む（例: 新しいブログのRSSフィードを追加する）
2. 最初の試行で失敗や非効率に遭遇する
3. 手動で修正し、成功する
4. **「この手順をスキルとして保存して」と依頼するか、Agent自身が提案する**
5. SKILL.mdが作成される。内容は:
   - トリガー条件（いつこのスキルを使うか）
   - 手順（具体的なコマンドやファイルパス）
   - 落とし穴（よくある失敗と対処法）
   - 検証ステップ（成功したことを確認する方法）

### 5.2 実例: llm-wikiスキル

最も重要なスキルは`llm-wiki`で、知識ベース全体の運用手順を定義している。1,400行超のSKILL.mdには以下が含まれる:

- 3層アーキテクチャの詳細な説明
- 6つのコア操作（Ingest, Query, Lint, Active Crawl, Synthesize, JP→EN Translation）
- 記事のスコアリング・優先順位付けシステム
- JP→EN翻訳ワークフローとその落とし穴
- サブディレクトリパターン（複雑なトピックの構造化方法）

### 5.3 スキルの爆発と整理

運用を続けると、スキルが増殖する問題が起きた。2026年5月時点で、100以上のスキルが30カテゴリに分散していた。対策として:

- **Curator**によるスキルの重複検出と統合提案
- **check-skill-inventory**の週次Cronジョブ（毎週日曜16:00 UTC）で棚卸し
- 不要なスキルは`absorbed_into`で統合先を指定して削除

スキル管理自体がharness engineeringの対象になる——これは皮肉だが、実際に起きることだ。

---

## 6. 定期実行ジョブ: 28のCronパイプライン

Hermes Agentの最大の特徴の一つは、**定期実行ジョブ（Cron）をネイティブに持っている**ことだ。これにより、人間の依頼を待たずに、知識ベースが自動的に更新され続ける。

### 6.1 日次データ収集パイプライン

毎日UTC 07:00頃に、3つの独立したデータソースパイプラインが走る:

**ブログパイプライン** (07:00 → 07:30 → 07:50):
```
blog-ingest (RSS取得 + raw記事保存)
  → blog-triage (記事の分類・優先順位付け)
    → blog-wiki-ingest (Wikiページ生成・更新)
```

**ニュースレターパイプライン** (07:10 → 07:20 → 07:40):
```
newsletter-ingest (Gmail IMAP経由取得)
  → newsletter-triage (内容の分類)
    → newsletter-wiki-ingest (Wikiページ生成・更新)
```

**Sitemap監視** (06:00):
企業ブログのsitemap XMLを監視し、新しい記事を検出する。RSSに載らない記事も拾える。

### 6.2 X/Twitter関連

- **x-bookmarks-ingest** (1日2回): 自分のXブックマークから記事を取り込む
- **x-accounts-scan** (2日毎): 追跡対象のXアカウントの新規投稿をスキャン

### 6.3 夜間ナレッジ統合 (Dreaming)

UTC 18:00頃に、日中に集めた知識を統合する「Dreaming」パイプラインが走る:

```
dreaming-collect (知識断片の収集)
  → dreaming-group (テーマ別グループ化)
    → dreaming-wiki-ingest (Wikiページへの統合)
```

### 6.4 Wiki健全性パイプライン

- **wiki-health-fix** (毎日): Wikiの構造的問題をスキャンして自動修正
- **wiki-watchdog-fix** (毎日): 修正後の状態を確認
- **wiki-graph-analysis** (毎週金曜): ページ間リンクのグラフ分析、重複検出
- **tag-audit-weekly** (毎週月曜): タグ分類学の監査

### 6.5 配信パイプライン

知識ベースの更新をSlackやDiscordに通知する:

- **ai-topics-slack-hot-posts** (1日3回): 注目記事をSlackに配信
- **ai-topics-discord-hot-posts** (1日3回): 同じ内容をDiscordに転送
- **Weekly AI digest** (毎週月曜): 週次ダイジェストをTelegramに配信

---

## 7. 設定保守: Infrastructure as Codeの精神

### 7.1 設定ファイルの管理

全ての設定はリポジトリ内で管理される:

- `config/feeds/blogs.opml`: 追跡対象の84ブログのRSSフィード
- `config/feeds/x-accounts.yaml`: 追跡対象のX/Twitterアカウント
- `config/hot-topics.yaml`: アクティブクロールのトピック設定
- `config/hermes/skills/`: スキル定義（リポジトリ内コピー）

### 7.2 スクリプトの保守

`scripts/`以下に28個の自動化スクリプトがある。これらはCronジョブから呼ばれ、データの収集・変換・検証を行う。スクリプトに不具合が見つかったら、その場で修正し、git commit & pushする。改善点はAGENTS.mdにも記録される。

### 7.3 gitによる変更管理

全ての変更はgitで管理される。Wikiページの変更、設定の変更、スクリプトの修正——全てに差分がある。問題があれば`git revert`で巻き戻せる。これはAgentの行動を監査可能にする重要な仕組みだ。

---

## 8. 実運用から見えた知見

### 8.1 失敗トレースを改善資産にする

半年間の運用で、何度も同じカテゴリの失敗を繰り返した。その度にharness側（設定、スクリプト、スキル、pre-commit hook）に改善を加えた:

| 失敗例 | 対策 |
|---|---|
| ページが重複して作られる | 作成前に`index.md`を確認する手順をスキルに追加 |
| タグが散らかる | pre-commit hookでブロック + SCHEMA.mdの分類学を整備 |
| Cron処理が失敗する | スクリプト修正 + AGENTS.mdに落とし穴を記録 + スキル化 |
| スキルが爆発的に増える | Curator + 週次棚卸しジョブ |

### 8.2 Agentは設定を自分で直す

Hermes Agentの特徴的な点は、**設定やスクリプトの修正をAgent自身が行う**ということだ。Cronジョブが失敗したとき、Agentは:

1. エラーログを分析する
2. 原因を特定する
3. スクリプトや設定を修正する
4. 修正内容をgit commit & pushする
5. 必要ならスキルを更新する

人間が介入するのは、根本的な設計判断が必要なときだけだ。

### 8.3 「回り続ける」ことの価値

最も重要な知見は、**知識ベースが回り続けること自体に価値がある**ということだ。手動で運用していたら、数日で滞留が発生し、数週間で陳腐化が始まる。Cronパイプラインにより、常に最新の状態が保たれる。

これは、サーバーの監視やCI/CDパイプラインと同じ発想だ。一度セットアップしてしまえば、人間の介入なしに動き続ける。異なるのは、対象が「コード」ではなく「知識」だという点だけだ。

---

## 9. ソフトウェア開発者への示唆

Hermes Agentの活用経験から、ソフトウェア開発者に伝えたいことがいくつかある:

1. **設定はMarkdownで書け。** YAMLやJSONよりも、Agentが読み書きしやすく、人間もレビューしやすい。
2. **失敗をgitに残せ。** Agentの失敗は、次の改善のための貴重なデータだ。ログだけでなく、修正のdiffも残す。
3. **スキルは自動で生まれる。** 手動で手順書を書くのではなく、成功した作業から自動的に抽出する。人間はレビューと承認だけを行う。
4. **定期実行は前提で設計しろ。** Agentを「呼ばれたら動く」存在ではなく、「常に動いている」存在として設計する。
5. **Environmentを選べ。** Coding agentが先に実用化したのは、ファイルシステムやgitという検証しやすい環境で動くからだ。知識管理も同じように、Markdown + gitという検証しやすい環境を選ぶのが成功の鍵だ。

---

## 10. おわりに

Hermes AgentをSecond Brainとして半年間運用してきて、最も変わったのは「何を知っているか」ではなく「どう知識を扱うか」だ。知識ベースは静的なリポジトリではなく、自律的に更新され続けるruntime環境になった。

Mitchell Hashimotoが[harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey)と呼んだもの——Agentが失敗するたびに、その失敗を繰り返さないようにする足場を設計する営み——は、知識管理の領域でも同じように機能する。違いは、対象がコードのビルドやテストではなく、記事の取り込みやページの整理だというだけだ。

ソフトウェア開発者は、CI/CDやIaCの経験から、この種の自動化に自然に馴染めるはずだ。Hermes Agentは、その馴染みやすい感覚を「知識」という領域に拡張するための道具だ。
