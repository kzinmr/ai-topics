---
marp: true
theme: default
paginate: true
size: 16:9
title: "Hermes Agent: 実運用の設定・スキル・定期実行"
description: "ソフトウェア開発者向けのHermes Agent実運用ガイド——Second BrainとしてのLLM Wiki運用の実際"
style: |
  section {
    font-family: "Hiragino Sans", "Yu Gothic", "Noto Sans CJK JP", "Helvetica Neue", sans-serif;
    background: #fbfaf4;
    color: #18241f;
    padding: 54px 66px;
    letter-spacing: 0;
  }
  h1, h2, h3 {
    color: #10251c;
    letter-spacing: 0;
  }
  h1 {
    font-size: 42px;
    line-height: 1.18;
  }
  h2 {
    font-size: 34px;
    line-height: 1.2;
  }
  p, li {
    font-size: 25px;
    line-height: 1.46;
  }
  ul, ol {
    margin-top: 0.5em;
  }
  strong {
    color: #b45f06;
  }
  code {
    background: #efe7d0;
    color: #243326;
    border-radius: 4px;
    padding: 0.04em 0.24em;
  }
  pre {
    font-size: 18px;
    line-height: 1.4;
  }
  table {
    font-size: 19px;
    border-collapse: collapse;
  }
  th {
    background: #17352b;
    color: #fffaf0;
  }
  td, th {
    padding: 0.42em 0.55em;
  }
  blockquote {
    border-left: 8px solid #c47f2c;
    color: #31423a;
    background: #f2ead8;
    padding: 0.4em 0.8em;
  }
  section.lead {
    background: #10251c;
    color: #fffaf0;
  }
  section.lead h1,
  section.lead h2,
  section.lead h3 {
    color: #fffaf0;
  }
  section.lead strong {
    color: #f1b35d;
  }
  section.section {
    background: #26372f;
    color: #fffaf0;
  }
  section.section h1,
  section.section h2 {
    color: #fffaf0;
  }
  .kicker {
    font-size: 18px;
    color: #b45f06;
    font-weight: 700;
    text-transform: uppercase;
  }
  .small {
    font-size: 18px;
    line-height: 1.38;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
  }
  .box {
    border: 1.5px solid #d5c8ac;
    border-radius: 8px;
    padding: 18px 20px;
    background: #fffdf7;
  }
  .box h3 {
    margin-top: 0;
    font-size: 24px;
  }
  .big {
    font-size: 30px;
  }
  .mono {
    font-family: "SFMono-Regular", Menlo, Consolas, monospace;
    font-size: 20px;
    line-height: 1.35;
  }
---

<!-- _class: lead -->

<div class="kicker">Software Engineer's Guide</div>

# Hermes Agent を Second Brain として回す

## 設定・スキル・定期実行の実運用

<br />

<div class="small">
2026年6月3日<br />
kzinmr (AI Engineer)
</div>

---

# 今日のゴール

前回（5/19 LLM勉強会）では **Harness Engineering の理論** を紹介した。
今回はその続き——**実際にどう動いているか** を具体的に見せる。

- 設定ファイル (`AGENTS.md`, `SCHEMA.md`) はどんな構造か
- Pre-commit hook で何を防いでいるか
- 28個の Cron ジョブはどう連携しているか
- スキルはどのように自動生成されるか
- 1日のワークフローはどんな姿か

<!-- _footer: "前回スライド: slides/2026-05-14_harness-engineering-llm-wiki.marp.md" -->

---

<!-- _class: section -->

# Part 1: 設計——ファイルに、実行はAgentに

---

# 3層アーキテクチャ

Karpathy の LLM Wiki パターンをそのまま適用。ファイルシステムが永続化層。

<div class="grid">
<div class="box">

### Layer 1: raw/ (不変)
- `raw/articles/` — Web記事
- `raw/papers/` — arXiv論文
- `raw/newsletters/` — ニュースレター
- **Agentは読むが、編集しない**

</div>
<div class="box">

### Layer 2: wiki ページ (Agent管理)
- `entities/` — 751ページ
- `concepts/` — 1,550ページ
- `comparisons/` — 26ページ
- **合計 2,327 ページ**

</div>
</div>

<div class="box">

### Layer 3: スキーマ (規約更新時のみ)
- `SCHEMA.md` — タグ分類学・ページ閾値
- `index.md` — 全ページのインデックス

</div>

<!-- _footer: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f" -->

---

# AGENTS.md: リポジトリの Single Source of Truth

人間のドキュメントではなく、**Agentへの指示書**。CI/CDでいう `Makefile` + `README`。

```
AGENTS.md に含まれるもの:
├── ディレクトリ構成と役割
├── Wiki 3層アーキテクチャのルール
├── ページ作成・更新の手順
├── Cron パイプライン全体図 (28ジョブ)
├── 主要スクリプト一覧
└── よくある失敗と対処法
```

Agent はこのファイルを読んで、リポジトリの構造とルールを理解する。
**設定を変更したければ、このファイルを編集する。**

---

# SCHEMA.md: タグ分類学とページ閾値

知識ベースの品質を保つための規約。

<div class="grid">
<div class="box">

### タグ分類学 (10カテゴリ)
- Models: `model`, `reasoning`, `llm`
- People: `company`, `lab`, `open-source`
- Products: `tool`, `platform`, `coding-agent`
- Techniques: `inference`, `fine-tuning`, `rag`
- Engineering: `agentic-engineering`, `python`
- AI Agents: `multi-agent`, `orchestration`
- ... etc.

</div>
<div class="box">

### ページ閾値
- **作成**: 2+ソースで言及された場合
- **追加**: 既存ページがあれば更新
- **分割**: 200行超
- **廃棄**: 内容が完全にsuperseded

### frontmatter必須
`title`, `created`, `updated`,
`type`, `tags`, `sources`

</div>
</div>

---

# Pre-commit Hook: Agentのミスをブロックする

`.git/hooks/pre-commit` に2つのバリデータを設置。

<div class="grid">
<div class="box">

### 1. index.md 検証
- ページ作成後に `index.md` が更新されているか
- 新しいページがインデックスに反映されていなければ **commit をブロック**

</div>
<div class="box">

### 2. タグ検証
- frontmatter の `tags` が SCHEMA.md の分類学に含まれているか
- 新規タグを SCHEMA.md に追加し忘れた Agent の commit を **ブロック**

</div>
</div>

> Agent が新しいページを作ったとき、タグを新規作成して SCHEMA.md に追加し忘れることがあった。
> この hook がそのミスを git commit 前にブロックする。

---

<!-- _class: section -->

# Part 2: Cron パイプライン——28ジョブの連携

---

# 日次データ収集: 3パイプライン並列

毎日 UTC 07:00 頃に3つのパイプラインが並列走行。

```
ブログ (07:00→07:30→07:50):
  blog-ingest ──→ blog-triage ──→ blog-wiki-ingest
  (RSS取得)      (分類・優先順位)   (Wiki生成・更新)

ニュースレター (07:10→07:20→07:40):
  newsletter-ingest ──→ newsletter-triage ──→ newsletter-wiki-ingest
  (Gmail IMAP取得)     (内容分類)            (Wiki生成・更新)

Sitemap監視 (06:00):
  sitemap-monitor (企業ブログの新記事検出)
```

各パイプラインは **script → triage → ingest** の3段階。
中間結果はJSONチェックポイントとして保存される。

---

# X/Twitter とアクティブクロール

<div class="grid">
<div class="box">

### X/Twitter
- **x-bookmarks-ingest** (1日2回)
  自分のブックマークから記事を取り込む
- **x-accounts-scan** (2日毎)
  追跡対象アカウントの新規投稿をスキャン
- `config/feeds/x-accounts.yaml` でアカウント管理

</div>
<div class="box">

### アクティブクロール
- **active-crawl** (毎日 UTC 11:00)
  `config/hot-topics.yaml` ベースの
  プロアクティブ知識探索
- **trending-topics** (毎日 UTC 12:00)
  トレンドリサーチ
- **raw-backlog-ingest** (4時間毎)
  未処理 raw 記事の段階的処理
  (5記事/バッチ × 6回/日 = 30記事/日)

</div>
</div>

---

# 夜間統合: Dreaming パイプライン

UTC 18:00 頃、日中に集めた知識を統合する。

```
dreaming-collect (18:00)    ← 知識断片の収集
  → dreaming-group (18:10)  ← テーマ別グループ化
    → dreaming-wiki-ingest (18:20)  ← Wiki ページへの統合
```

- 日中にバラバラに収集された記事・論文・投稿を
  テーマごとに束ねる
- 重複や矛盾を検出し、統合された Wiki ページを生成
- 人間が翌朝見るときには、整理された知識ベースが待っている

---

# Wiki 健全性パイプライン

<div class="grid">
<div class="box">

### 日次 (毎日)
- **wiki-watchdog-fix** (17:35 UTC)
  構造的問題をスキャン
- **wiki-health-fix** (17:50 UTC)
  自動修正 + 修正後レポート

</div>
<div class="box">

### 週次
- **wiki-graph-analysis** (金 15:00 UTC)
  ページ間リンクのグラフ分析、重複検出
- **tag-audit-weekly** (月 10:00 UTC)
  タグ分類学の監査
- **check-skill-inventory** (日 16:00 UTC)
  スキルの棚卸し

</div>
</div>

検出される問題: orphan pages, duplicate pages,
broken wikilinks, stale pages, missing tags

---

# 配信パイプライン: 知識を届ける

```
ai-topics-slack-hot-posts (1日3回: 00:30, 06:30, 12:30 UTC)
  → ai-topics-discord-hot-posts (15分後: 00:45, 06:45, 12:45 UTC)
    ↑ script: discord_slack_relay.py (no_agent relay)

Weekly AI digest (毎週月曜 00:00 UTC) → Telegram
```

- 注目記事を Slack / Discord に自動配信
- 週次ダイジェストを Telegram に送信
- **pipeline-watchdog** (6時間毎) で全体ヘルスを監視

---

<!-- _class: section -->

# Part 3: スキル——経験をコードにする

---

# スキルとは何か

`.hermes/skills/` 以下に SKILL.md として保存される**手順のメモリ**。

| 要素 | 内容 |
|---|---|
| トリガー条件 | いつこのスキルを使うか |
| 手順 | 具体的なコマンドやファイルパス |
| 落とし穴 | よくある失敗と対処法 |
| 検証ステップ | 成功したことを確認する方法 |

- 現在 **30カテゴリ、100+スキル** が存在
- Agent がタスクを実行するたびに、関連スキルを自動ロード
- ユーザーは `skill_view()` で内容を確認・編集できる

---

# スキルはどのように生まれるか

典型的な流れ:

```
1. Agent が複雑なタスクに取り組む
   (例: 新しいブログの RSS フィードを追加する)

2. 最初の試行で失敗や非効率に遭遇する
   (例: OPML のパースで文字化け)

3. 手動で修正し、成功する
   (例: エンコーディング指定を追加)

4. 「この手順をスキルとして保存して」と依頼
   または Agent が自ら提案する

5. SKILL.md が作成される
```

**harness engineering の核心**: 失敗をスキルに変換し、
同じ失敗を繰り返さないようにする。

---

# 実例: llm-wiki スキル

最も重要なスキル。**1,400行超** の SKILL.md。

<div class="grid">
<div class="box">

### 6つのコア操作
1. **Ingest** — 記事・論文の取り込み
2. **Query** — 知識の引き出し
3. **Lint** — 品質検査
4. **Active Crawl** — プロアクティブ探索
5. **Synthesize** — 知識の統合
6. **JP→EN Translation** — 翻訳

</div>
<div class="box">

### 記録されている内容
- 3層アーキテクチャの詳細仕様
- 記事のスコアリング・優先順位付け
- JP→EN 翻訳ワークフローと落とし穴
- サブディレクトリパターン
- タグ付けの具体例

</div>
</div>

---

# スキルの爆発と整理

運用を続けるとスキルが増殖。

<div class="grid">
<div class="box">

### 問題
- 2026年5月時点で **100+スキル / 30カテゴリ**
- 重複するスキルが増える
- 古いスキルが更新されない

</div>
<div class="box">

### 対策
- **Curator** による重複検出・統合提案
- **check-skill-inventory** 週次ジョブ
- `absorbed_into` で統合先を指定して削除
- スキル管理自体が harness の対象に

</div>
</div>

---

<!-- _class: section -->

# Part 4: 日々のワークフロー

---

# 1日の流れ

```
06:00  sitemap-monitor         新記事を検出
07:00  blog-ingest             RSS から記事取得
07:10  newsletter-ingest       ニュースレター取得
07:20  newsletter-triage       分類
07:30  blog-triage             分類
07:40  newsletter-wiki-ingest  Wiki 更新
07:50  blog-wiki-ingest        Wiki 更新
  ↓
[人間が起床]
  ↓
08:00  Slack / Discord に注目記事が届いている
       → 興味のあるトピックがあれば Agent に深掘り依頼
  ↓
日中   Agent と対話:
       - ナレッジクエリ (「○○について整理して」)
       - 記事取り込み (URL を渡す → raw → wiki)
       - 新しい追跡対象の追加
  ↓
18:00  dreaming パイプライン: 日中の知識を統合
22:00  x-accounts-scan: X アカウントの新着チェック
```

---

# ナレッジクエリの実際

**ユーザー**: 「GRPO の論文と実装の関係を整理して」

Agent の行動:
1. `wiki/index.md` から GRPO 関連ページを検索
2. `concepts/grpo-rl-training.md` を参照
3. `entities/trl.md` や `entities/unsloth.md` を確認
4. 必要なら `raw/articles/` のソース記事も参照
5. 回答を返す
6. 再利用可能な調査なら `wiki/queries/` に保存

**ポイント**: 回答が一回で消えない。
Wiki ページとして保存され、次回即座に参照できる。
Karpathy の言う **compiled knowledge**。

---

# 記事取り込みの実際

**ユーザー**: 「この記事読んで wiki に追加して」 + URL

Agent の行動:
1. 記事を `raw/articles/` に保存 (不変)
2. 既存の Wiki ページがないか `index.md` を確認
3. 既存ページがあれば更新、なければ新規作成
4. frontmatter (`tags`, `sources`, `updated`) を設定
5. 最低2つの他ページへ `[[wikilink]]` を追加
6. `index.md` と `log.md` を更新
7. `git commit & push`

**人間の介入**: URL を渡すだけ。あとは自律実行。

---

# 設定の変更: Infrastructure as Code

<div class="grid">
<div class="box">

### 追跡対象の追加
```yaml
# config/feeds/x-accounts.yaml
- handle: "@new_person"
  category: ai-researcher
  notes: "Exploring ..."
```
→ Agent に「追加して」と依頼
→ `build_x_wiki.py` でスケルトン生成
→ 後日エンリッチメント

</div>
<div class="box">

### スクリプトの修正
Cron ジョブが失敗 → Agent が:
1. エラーログを分析
2. 原因を特定
3. スクリプトを修正
4. `git commit & push`
5. スキルを更新 (必要なら)

**人間の介入**: 設計判断が必要なときだけ。

</div>
</div>

---

<!-- _class: section -->

# Part 5: 何が変わったか

---

# 失敗traceを改善資産にする

半年間の運用で繰り返された失敗と対策:

| 失敗例 | 対策 (Harness側) |
|---|---|
| ページが重複して作られる | 作成前に `index.md` 確認をスキルに追加 |
| タグが散らかる | pre-commit hook でブロック |
| Cron 処理が失敗する | スクリプト修正 + AGENTS.md に記録 |
| スキルが爆発的に増える | Curator + 週次棚卸し |
| JP→EN 翻訳が不自然 | 翻訳スキルに落とし穴を詳細記録 |

> Agent makes a mistake → Engineer a solution → Agent never makes that mistake again.
> — Mitchell Hashimoto

---

# 数字で見る現在の知識ベース

| 指標 | 値 |
|---|---|
| Wiki ページ総数 | 2,327 |
| entities/ | 751 |
| concepts/ | 1,550 |
| comparisons/ | 26 |
| 追跡ブログ RSS | 84 |
| 追跡 X アカウント | 30+ |
| Cron ジョブ | 28 (25 active, 2 disabled) |
| スキル | 100+ (30カテゴリ) |
| 自動化スクリプト | 28 |
| 日次処理記事数 | ~30 (raw-backlog) + 自動取得分 |

---

# ソフトウェア開発者への5つの示唆

1. **設定は Markdown で書け**
   Agent が読み書きしやすく、人間もレビューしやすい

2. **失敗を git に残せ**
   Agent の失敗は次の改善のための貴重なデータ

3. **スキルは自動で生まれる**
   手動で手順書を書くのではなく、成功した作業から抽出する

4. **定期実行は前提で設計しろ**
   Agent を「呼ばれたら動く」ではなく「常に動いている」として設計する

5. **Environment を選べ**
   Markdown + git という検証しやすい環境を選ぶのが成功の鍵

---

# まとめ

Hermes Agent を Second Brain として半年運用して変わったのは、
**「何を知っているか」ではなく「どう知識を扱うか」** だ。

知識ベースは静的なリポジトリではなく、
**自律的に更新され続ける runtime 環境** になった。

設定・スキル・定期実行——これらは LLM の外側にある雑多な周辺機能ではない。
**モデルが実行を継続し、失敗を記憶し、次回に活かすための境界** だ。

ソフトウェア開発者は、CI/CD や IaC の経験から、
この種の自動化に自然に馴染めるはずだ。

---

<!-- _class: lead -->

# Thank You

<div class="small">

**リポジトリ**: github.com/kzinmr/ai-topics
**Wiki**: ai-topics/wiki/ (2,327 pages)
**Hermes Agent**: hermes-agent.nousresearch.com

</div>
