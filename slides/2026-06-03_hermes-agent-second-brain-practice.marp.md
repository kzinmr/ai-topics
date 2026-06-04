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

# 拡張の2チャネル: `_overrides` と `_custom`

スキルは <strong style="color:#2f7d6b">🟩 公式の機構</strong>の上に、2通りで足す。

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

設定の置き場所〔🟧〕: `AGENTS.md`（＝指示書 / Makefile+README）・`config/feeds/`・`hot-topics.yaml`・`SOUL.md`

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

# 失敗トレースを改善資産にする

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
