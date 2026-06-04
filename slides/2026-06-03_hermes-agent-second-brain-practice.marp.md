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
2026年6月4日<br />
kzinmr (AI Engineer)
</div>

---

# 今日のゴール

前回（5/15 Product Jam）では **Harness Engineering の概要** を紹介した。
今回はその続き——**実際にどう動いているか** を具体的に見せる。

- 設定ファイル (`AGENTS.md`, `SCHEMA.md`) はどんな構造か
- Pre-commit hook で何を防いでいるか
- 28個の Cron ジョブはどう連携しているか
- スキルはどのように自動生成されるか
- 1日のワークフローはどんな姿か

<!-- _footer: "前回スライド: slides/2026-05-14_harness-engineering-llm-wiki.marp.md" -->

---

<!-- _class: section -->

# Part 1: 構成と設定
## 公式ハーネス × ai-topics 拡張

---

# 公式 × 拡張 の地図

<strong style="color:#2f7d6b">🟩 Hermes 公式</strong>＝機構、<strong style="color:#b45f06">🟧 ai-topics 拡張</strong>＝ドメイン。以降このパートは**この2色で対照**する。

<div class="grid">
<div class="box">

### 🟩 Hermes 公式（機構）
- `AGENTS.md` 読み込み規約
- スキル機構（agentskills.io）
- cron スケジューラ / メモリ
- permission・承認・sandbox
- 同梱 `llm-wiki` skill ほか

</div>
<div class="box">

### 🟧 ai-topics 拡張（ドメイン）
- `wiki/` 3層構造 ＋ `SCHEMA.md`
- `_overrides/` ＋ `_custom/` スキル
- `config/feeds/` ・ `hot-topics.yaml`
- 4× git pre-commit validator
- `config/hermes/SOUL.md`（人格）

</div>
</div>

公式の上に拡張を載せる。**ハーネスを替えても、ドメイン資産（wiki・config）は git に残る。**

---

# llm-wiki の構成 — Karpathy LLM-Wiki

<strong style="color:#2f7d6b">🟩</strong> `llm-wiki` skill **自体は Hermes 公式**（MIT, v2.0.0）。<strong style="color:#b45f06">🟧</strong> それを `~/wiki` に向け、`SCHEMA.md` と規約で**このドメインへ固有化**する。

| 層 | ディレクトリ | 変更可否 |
|---|---|---|
| **Layer 1** | `raw/` | ❌ 不変（ソース素材） |
| **Layer 2** | `entities/` `concepts/` `comparisons/` … | ✅ Agent が管理（**2,327ページ**） |
| **Layer 3** | `SCHEMA.md` `index.md` | ✅ 規約更新時のみ |

> RAG と違い、知識を**一度コンパイルして最新に保つ**。相互参照は既に張られ、矛盾は既にフラグ済み。

<!-- _footer: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f" -->

---

# Guardrails は多層 — まず skills に宿る

<div class="grid">
<div class="box">

### ① skills 内の検証 〔🟩機構＋🟧内容〕
trigger / 手順 / 落とし穴 / **検証ステップ** を skill に焼き込む（例: `skill-archive-safety`）

### ② Hermes 公式 built-in 〔🟩〕
permission・承認フロー・sandbox

</div>
<div class="box">

### ③ AGENTS.md / SCHEMA.md 規約 〔🟧〕
frontmatter必須 / タグはSCHEMAから / **リッチページ上書き禁止** / 矛盾を消さない

### ④ git pre-commit 〔🟧・決定的〕
ステージ時に機械チェック（次スライド）

</div>
</div>

**柔らかい層**（skills・規約・確率的）→ **硬い層**（git hook・決定的）を重ねる。

---

# pre-commit: 4つの決定的バリデータ 〔🟧〕

`git config core.hooksPath .githooks` で有効化。ステージされた wiki ページを検査する。

<div class="grid">
<div class="box">

### 1. index.md 破損検出
`validate_index.py` — pipe corruption 等

### 2. タグタクソノミー
`SCHEMA.md` に無いタグを**ブロック**

</div>
<div class="box">

### 3. コンテンツ退行
リッチページの**50%超の縮小をブロック**（スケルトン上書き防止）

### 4. 日本語混入
英語 wiki への JP 混入をブロック

</div>
</div>

> 4つとも「Agent が実際にやらかした失敗」から生まれた。**失敗 → 決定的ガードレール**（Ratchet）。

---

<!-- _class: section -->

# Part 2: Cron パイプライン
## 28ジョブを「構造」で捉える

---

# cron に何を登録できるか — 3モード

`hermes cron` は LLM だけでなく、script と skill も登録できる。

| モード | 指定 | 挙動 |
|---|---|---|
| **LLM** | `prompt` | 自然言語タスクを agent が実行（既定） |
| **script** | `no_agent` + `script` | **LLM を起こさず**実行、stdout をそのまま配信（決定的・安価） |
| **skill** | `skills: [...]` | <strong style="color:#b45f06">レポジトリ管理🟧</strong>の skill を名前で呼び出し、context に注入 |

ジョブの大半は **prompt + script + skills のハイブリッド**。
skill モードは Part 1 の `_overrides`/`_custom`（git管理）を**外部呼び出し** → <strong style="color:#2f7d6b">公式同梱skill🟩</strong>と棲み分け。

---

# cron × script: 決定的な実行/コンテキスト収集

- script 事後処理ではなく **pre-run（事前実行）**

```
script 実行 → stdout を "## Script Output" として
              agent の prompt に注入 → LLM が分析
```

- 必要な時だけ高価な LLM を起こす: 変更検知・差分収集を**決定的に安く**実行
  - 動的: script の最終行が `{"wakeAgent": false}` なら **LLM をスキップ**
  - 静的: `no_agent` なら script が全て（stdout を verbatim 配信、LLM 不在）

> 例：`sitemap-monitor` / `pipeline-watchdog` は script 主導。新着・異常があるときだけ agent を起こす。

---

# cron × AGENTS.md — workdir でポリシーを一元管理

cron ジョブに `workdir` を設定すると、**その配下の `AGENTS.md` が system prompt に自動注入**

<div class="grid">
<div class="box">

### 仕組み
- `workdir` → `TERMINAL_CWD`
- agent 起動時に `AGENTS.md` / `CLAUDE.md` を
  **workdir から**ロード
- first-match-wins・トップレベルのみ

</div>
<div class="box">

### 効果
- **作業ディレクトリ単位でポリシー一元管理**
- ai-topics の運用規約：「全wiki書き込み系 cron は `workdir: /opt/data/ai-topics` 必須」
- → wiki作業のグローバルポリシーが、全てのwiki系 cron セッションに届く

</div>
</div>

---

# cron の進化 — read-only から自動適用へ

action の確定性が高いと判断されるに従い、**提案→手動** から **自動適用** へ。

```
[read-only / 提案]                  [自動適用]
wiki-health (paused)      ───►      wiki-health-fix (active)
チェック＆修正提案→人間が反映        スキャン→自動修正→修正後レポート
```

- 安全のため **read-only（提案のみ）から始める**
- 提案の確度が高いと確認できたら、確定的な action を **自動適用へ昇格**
- 最終ゲートは pre-commit（Part 1）— 自動適用でも決定的チェックが効く

> 自動化の Ratchet：信頼できると分かった範囲だけ、人間の手を外す。

---

# ジョブカタログ① — ingest（受動）/ crawl（能動）

<div class="grid">
<div class="box">

### 📥 ingest（passive）— 来たものを取り込む
- `blog-ingest → triage → wiki-ingest` (RSS x blogwatcher cli)
- `newsletter-ingest → triage → wiki-ingest` (Substack由来)
- `x-bookmarks-ingest` (手で追加した新着bookmarksを取得)
<!-- - `raw-backlog-ingest`（5件×6回/日） -->

</div>
<div class="box">

### 🔭 crawl（active）— 自分から取りに行く
- `active-crawl`
  （`hot-topics.yaml` ベースの
  プロアクティブ知識探索）
- `trending-topics`
  （トレンドリサーチ）
- `sitemap-monitor`（RSS非対応サイトの監視）
- `x-accounts-scan` (`x-accounts.yaml`内アカウントの新着投稿)

</div>
</div>

ingest=RSS/NL/Xの**受動収集**、crawl=ギャップを埋める**能動探索**。

各段は script(pre-run)＋skill のハイブリッド。

NOTE: X API は4月から従量課金に対応。月の最低利用料 $200 から $20 程度に

---

# ジョブカタログ② — lint（健全性）/ report（配信）

<div class="grid">
<div class="box">

### 🩺 lint（health-check）
- `wiki-health-fix`（スキャン→自動修正）
- `wiki-watchdog-fix`（修正後の検証）
- `wiki-graph-analysis`（重複・リンク）
- `tag-audit-weekly` / `check-skill-inventory`
- `pipeline-watchdog`（no_agent 監視）

</div>
<div class="box">

### 📣 report（delivery）
- `ai-topics-slack-hot-posts`
- `ai-topics-discord-hot-posts`（relay）
- `Weekly AI digest` → Telegram

</div>
</div>

lint=知識ベースの**自己修復**、report=結果を**メッセンジャーへ配信**（ダッシュボードを開かせない）。

---

# アドバンスト: dreaming — コンテンツの横断統合

夜間バッチ（JST 03:00 頃）で、その日の断片を**テーマ横断で統合**する。

```
dreaming-collect → dreaming-group → dreaming-wiki-ingest
  (断片収集)        (意味的グループ化)   (統合・相互参照・統廃合)
```

- **⚠️ Claude Code の dreaming とは別物**
  - Claude Code: セッション横断で**作業改善**を提案
  - ai-topics: **wiki コンテンツ**のクロスリファレンス・統廃合・横断分析
- 重複や矛盾を検出し、点在する知識を結び直す
- こうした**横断分析は夜間バッチが効く**（日中の対話を止めない）

---

<!-- _class: section -->

# Part 3: スキル
## 経験をコードにする — 公式を土台に、自分で育てる

---

# スキルとは — agentskills.io 標準の「手順メモリ」

`~/.hermes/skills/` 以下の SKILL.md（YAML frontmatter、<strong style="color:#2f7d6b">agentskills.io 互換🟩</strong>）。

| 要素 | 内容 |
|---|---|
| トリガー条件 | いつこのスキルを使うか |
| 手順 | 具体的なコマンド・ファイルパス |
| 落とし穴 | よくある失敗と対処法 |
| 検証ステップ | 成功を確認する方法 |

- タスク実行時に関連スキルを**自動ロード**（progressive disclosure）
- **harness engineering の核心**：失敗を手順に変換し、二度と繰り返さない

---

# 自律拡張・整理・回収 — 主体もトリガーも別の3つ

スキルの生成・修正はセッション内実行、Curator/Cron のbackground検証で補完

| 仕組み | 主体・タイミング | 何をするか |
|---|---|---|
| **① 自律拡張・修正** | <strong style="color:#2f7d6b">Hermes 本体🟩</strong> ／ セッション内 | 決定論ゲート（既定10反復）→ **LLM が create / patch / none** |
| **② 整理（Curator）** | <strong style="color:#2f7d6b">Hermes 公式🟩</strong> ／ 非活動時 | スキルGC：30日 stale / 90日 archive（**削除しない**） |
| **③ 回収（check-skill-inventory）** | <strong style="color:#b45f06">ai-topics カスタム cron🟧</strong> ／ 週次 | `~/.hermes/` の新規skillを検出 → **git backup** |

① は「使いながら育つ」Hermes 自身の学習ループ。② 増殖の整理、③ カスタム資産のbackup

---

# 公式 × カスタム — スキルバックアップの3層構成

<strong style="color:#b45f06">カスタム3層🟧</strong>を `external_dirs` で公式に重ねる。カスタムには **2つの役割** — ① 使用 と ② 更新耐性のバックアップ。

| 層 | 中身 | 主な使われ方 | Git |
|---|---|---|---|
| `_overrides/`🟧 | 公式の改変版 | **cron が名前で参照** | ✅必須 |
| `_custom/`🟧 | 完全新規 | **cron が名前で参照** | ✅必須 |
| `_adhoc/`🟧 | 日常作業用 | **Hermes が自律ロード**（cron非参照） | ✅推奨 |
| <strong style="color:#2f7d6b">公式🟩</strong> | `~/.hermes/skills/` | Hermes が自律ロード | ❌（自動更新） |

cron が名前で叩く＝**決定的**に使う層と、Hermes が状況判断で**自律的**に使う層に分解、前者の保守を重視。
公式スキルの改変か、完全新規拡張かも区別。
3層とも git バックアップ＝**Hermes 更新でも消えない**（read-only・ローカル優先でマウント）。

---

# 拡張の2チャネル: `_overrides` と `_custom`

カスタムskillを足す2通り。<strong style="color:#2f7d6b">🟩 公式の機構</strong>の上に重ねる。

<div class="grid">
<div class="box">

### 🟧→🟩 `_overrides/`
公式skillを**ドメイン向けに上書き**
- `llm-wiki` ・ `blog-post-writing`
- `cron-job-management`
- `wiki-graph-health`

</div>
<div class="box">

### 🟧 `_custom/`
**完全独自**のドメインskill
- `dreaming` ・ `daily-rss-triage`
- `semantic-article-grouping`
- `wiki-ingestion-pipelines`

</div>
</div>

`_overrides` は公式を**上書き＝drift管理が要る**: Hermes 更新で公式が変わっても保全するのに必要

`_custom` は新規＝自由。どちらも cron が名前で参照する。

`check_skill_drift.py`で週次レビュー

---

# 実例: llm-wiki — 公式を分析し、ドメインに適合

<strong style="color:#2f7d6b">🟩 公式</strong> `skills/research/llm-wiki`（**507行**）を起点に、<strong style="color:#b45f06">🟧 約3倍へ拡張</strong>（**1,405行**）。

<div class="grid">
<div class="box">

### 公式の Core Operations
1. **Ingest** 2. **Query** 3. **Lint**

（Karpathy LLM-Wiki の3操作）

</div>
<div class="box">

### ai-topics が足した適合
- **4. Active Crawl**（ギャップ探索）
- **5. Synthesize**（原稿生成）
- **6. JP→EN Translation**（英語化）
- 記事スコアリング / subagent batch
- path解決・index破損リカバリ手順

</div>
</div>

公式の骨格はそのまま、**このドメインの作法（収集・採点・英語wiki化）を上乗せ**した。

---

<!-- _class: section -->

# Part 4: 日々のワークフロー・活用方法
## 狭義RAG（取り込み→クエリ）から、広義RAG（文脈注入→生成）へ

---

# 1日の流れ

```
03:00  dreaming           未明: 日中の知識を統合 → 翌朝には整理済み
07:00  x-accounts-scan    朝: X アカウントの新着をチェック
  ↓
[ 起床 ]
  ↓
09:30  配信               Slack / Discord に注目記事が届く (1日3回)
       → 深掘りしたいトピックは Agent に依頼
  ↓
日中   Agent と対話:
       - ナレッジクエリ (「○○について整理して」)
       - 記事取り込み (URL を渡す → raw → wiki)
       - 新しい追跡対象の追加
  ↓
15:00  sitemap-monitor    新記事を検出
16:00  blog / newsletter  ingest → triage → wiki 更新 (〜16:50)
21:30  配信               その日の収集分を Slack / Discord へ
```

<div class="small">※ 時刻はすべて <strong>JST（UTC+9）</strong>。cron 定義自体は UTC。</div>

---

# 活用の全体像：狭義RAG → 広義RAG

取り込み→クエリ（狭義RAG）は一機能にすぎない。wiki は **文脈の基盤**であり、**文脈注入 → 生成操作の拡張**（広義RAG）のインパクトが大。

<div class="grid">
<div class="box">

### 狭義RAG（取り込み→クエリ）
- 記事を ingest → wiki に compile
- 質問に対し関連ページを引く

</div>
<div class="box">

### 広義RAG（文脈注入→生成）
- wiki を文脈として注入し…
- レポート / blog / slides / コード文脈
  を**生成・拡張**する

</div>
</div>

「検索して答える」だけでなく、**蓄積した文脈で生成を駆動する**。

---

# 外部エージェントから wiki を使う — CLI と MCP

Claude Code / Codex など外部エージェントへも、wiki を**読み取り専用で文脈注入**できる。

<div class="grid">
<div class="box">

### `scripts/wiki` CLI 〔🟧〕
- shell-native・ripgrep 全文検索・メタデータ絞り込み
- `wiki search / show / meta / links`（**read-only**）
- shell が使える agent（Claude Code / Codex）向き

</div>
<div class="box">

### MCP server 〔🟧〕
- `docs/wiki-mcp.md`：read-only な Filesystem MCP
  （Docker `,ro` で書き込み不可）
- MCP クライアント（Claude Code / Desktop 等）が
  markdown を直接ナビゲート

</div>
</div>

どちらも **wiki を壊さない**（read-only）。CLI と MCP は併用可。

---

# ナレッジクエリ

**例**：「GRPO の論文と実装の関係を整理して」「先週の ○○ 周りの議論をまとめて」

Agent の行動:
1. `wiki/index.md` から関連ページを特定（`concepts/` `entities/`）
2. 指示があれば `raw/` のソースまで遡る
3. 回答を返す
4. 議論から新規観点が見出されれば、記事に追記更新
5. 回答が再利用可能なら `wiki/queries/` に保存 (semantic cache)

Karpathy の言う **compiled knowledge** —— RAG の「都度再発見」とは違う。

---

# オンデマンドwiki取り込み (最頻出操作)

**例**：「この記事読んで wiki に追加して」＋URL ／ 「この一連の議論を既存概念に絡めて」

Agent の行動:
1. ソースを `raw/` に保存（不変）
2. `index.md` で既存ページを確認 → 更新 or 新規
3. frontmatter・最低2つの `[[wikilink]]`・`index.md`/`log.md` を整備
4. pre-commit を通して `git commit & push`

**人間の介入**: URL や指示を渡すだけ。あとは自律実行。取り込みも生成も、同じ wiki を介してつながる。

---

# wiki からコンテンツ生成 — 聴衆・媒体別の reporting / blog / slides

蓄積した wiki を文脈に、**媒体・聴衆に合わせて生成**する（広義RAG の出力側）。関連スキル:

<div class="grid">
<div class="box">

### reporting
- `wiki-daily-report` / `trending-topics-reporting`
- `hermes-report-quality`（Gwern品質：Anti-Examples 等）
- Slack / Discord / Telegram へ媒体別に整形

</div>
<div class="box">

### blog / slides
- `blog-writing` / `research-paper-writing`
- `humanizer`（機械臭の除去）

</div>
</div>

同じ知識ベースから、**聴衆（社内/一般）・媒体（blog/slides/X…）別に出し分ける**。※この資料も wiki から生成。

---

# 設定は対話的に・人間レビュー可能に

設定変更は**対話で修正**して運用。設定は**保守でき・人間がレビューできる形**（md/YAML/JSON + git）。

<div class="grid">
<div class="box">

### 対話的な設定修正
- 「追跡対象に `@x` を追加して」→ `config/feeds/*.yaml` 編集 → スケルトン生成
- Cron 失敗 → ログ分析 → スクリプト修正 → `git commit`
- **人間の介入は設計判断のときだけ**

</div>
<div class="box">

### 失敗は改善資産に
- 繰り返した失敗 → harness 側へ恒久対策（スキル / pre-commit / AGENTS.md）
- 「Agent makes a mistake → Engineer a solution → never again」

</div>
</div>

すべて **diff が残る**。設定もスキルも cron も、git で監査・巻き戻しできる。

---

# まとめ

2ヶ月程度運用して変わったのは、**「何を知っているか」ではなく「どう知識を扱うか」**。
知識ベースは静的repoでなく、**自律的に更新され続ける runtime 環境**になった。
LLM の外側の「設定・Skill・wiki」が資産——蓄積した文脈が生成を駆動。

<div class="grid">
<div class="box">

### ポイント
- 設定は **MD/YAML/JSON + git**（人間レビュー可）
- 失敗は **harness で恒久対策**
- スキルは**自動で生まれ**、自分で育てる
- **常駐・定期実行を前提**に設計

</div>
<div class="box">

| 指標 | 値 |
|---|---|
| Wiki ページ総数 | 2,327 |
| entities/ | 751 |
| concepts/ | 1,550 |
| Cron ジョブ | 25 active |
| スキル | 100+ |
| スクリプト | 28 |
| 日次処理記事数 | ~30 + 自動取得分 |

</div>
</div>

---

<!-- _class: lead -->

# Thank You

<div class="small">

**リポジトリ**: github.com/kzinmr/ai-topics
**Wiki**: ai-topics/wiki/ (2,327 pages)
**Hermes Agent**: hermes-agent.nousresearch.com

</div>
