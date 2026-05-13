# AGENTS.md — ai-topics リポジトリ

> **このファイルは、このリポジトリで作業する Hermes Agent（およびサブエージェント）のための**単一の真実源（Single Source of Truth）**です。
> リポジトリの構成、自動化パイプライン、規約、落とし穴をカバーしています。

---

## リポジトリ概要

このリポジトリは **LLM / AI Agent 技術の wiki 知識ベース** です。Andrej Karpathy の [LLM Wiki パターン](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) に基づき、AI/ML エコシステムのモデル・ツール・フレームワーク・人物・概念を継続的にドキュメント化しています。

- **GitHub**: `kzinmr/ai-topics`
- **Canonical root**: `~/ai-topics`
- **Wiki root**: `~/wiki` → symlink to `~/ai-topics/wiki`

---

## ディレクトリ構成

```
~/ai-topics/
├── AGENTS.md                        ← このファイル
├── wiki/                            ← 知識ベース本体（3層アーキテクチャ）
│   ├── SCHEMA.md                    ← Wiki規約・タグ分類学・ページ閾値
│   ├── index.md                     ← 全Wikiページのインデックス（section別・アルファベット順）
│   ├── log.md                       ← 全Wiki操作の時系列ログ（append-only）
│   ├── raw/                         ← Layer 1: 不変のソース素材
│   │   ├── articles/                ← Web記事、ブログポスト、クリッピング
│   │   ├── papers/                  ← arXiv論文、テクニカルレポート
│   │   └── newsletters/             ← ニュースレターダイジェスト
│   ├── entities/                    ← Layer 2: 人物・組織・製品ページ
│   ├── concepts/                    ← Layer 2: 概念・トピックページ
│   ├── comparisons/                 ← Layer 2: 横断比較ページ
│   ├── queries/                     ← Layer 2: 再利用可能な調査・回答
│   └── events/                      ← Layer 2: 重要イベント・リリース
├── config/
│   ├── feeds/
│   │   ├── x-accounts.yaml          ← 追跡対象X/Twitterアカウント一覧
│   │   └── blogs.opml               ← 追跡対象ブログRSSフィード（84 blogs）
│   ├── hot-topics.yaml              ← 自動クローリングのトピック設定
│   └── hermes/skills/               ← リポジトリ管理のHermesスキル
├── scripts/                         ← 自動化スクリプト（28個）
├── .githooks/                       ← Git pre-commit hooks
│   ├── pre-commit                   ← index.md validate + tag validation を実行
│   └── pre-commit-tag-validator.py  ← タグ分類学違反ブロッカー
└── inbox/                           ← ニュースレターダイジェスト保存先
```

---

## Wiki 3層アーキテクチャ

| 層 | ディレクトリ | 変更可能？ | 内容 |
|---|---|---|---|
| **Layer 1** | `raw/` | ❌ 不変 | ソース記事・論文・トランスクリプト |
| **Layer 2** | `entities/` `concepts/` `comparisons/` `queries/` `events/` | ✅ Agentが管理 | 構造化Wikiページ |
| **Layer 3** | `SCHEMA.md` `index.md` | ✅ 規約更新時のみ | スキーマ・ナビゲーション |

### 重要規約
- **全WikiページにYAML frontmatter必須**: `title`, `created`, `updated`, `type`, `tags`, `sources`
- **タグは必ず `SCHEMA.md` の分類学から**: 新規タグは必ずSCHEMA.mdに追加してから使用
- **最低2つの外部wikilink**: 新規ページは最低2つの他ページへリンク
- **index.md 即時更新**: ページ作成・更新後は必ずindex.mdに反映
- **log.md 即時追記**: 全操作をappend-onlyで記録
- **`raw/` 内のファイルを編集しない**: ソース素材は不変
- **200行以上で分割**: 長大ページはサブページに分割
- **既存ページ優先**: 重複ページを作る前に `index.md` と関連ページを確認し、原則として既存ページへ統合
- **矛盾を消さない**: 新情報が旧情報と衝突する場合は、古い解釈を削除せず日付・出典つきで contested / superseded として残す

---

## 知識ベース運用原則

セットアップ時ドラフトにあった抽象的な運用憲章は、現行 `SCHEMA.md` と upstream 版 `AGENTS.md` に合わせて以下のルールとして統合する。

### Primary Objective
このWikiは、raw source と最終回答のあいだにある **durable, inspectable synthesis layer** である。作業の目的は、一回限りの回答ではなく、あとから検証・再利用できる知識として残すこと。

### Manual Wiki Workflow
1. `wiki/SCHEMA.md`、`wiki/index.md`、関連する既存ページを先に読む
2. `wiki/raw/` のソースを参照するが、編集しない
3. 新規ページより既存ページ更新を優先する
4. ページ作成時は `SCHEMA.md` の Page Thresholds を満たすか確認する
5. frontmatter の `updated`、`tags`、`sources`、本文中の `[[wikilinks]]` を同時に更新する
6. `wiki/index.md` と `wiki/log.md` を同じ作業単位で更新する
7. 新旧情報が矛盾する場合は、出典・日付・不確実性を本文に明示する

### Query / Analysis Workflow
1. 調査回答はまず `wiki/index.md` から関連ページを探す
2. Wikiページだけで根拠が薄い場合は、ページの `sources` から raw source も確認する
3. 回答が再利用可能な調査・比較・判断なら、`wiki/queries/` か該当する `concepts/` / `comparisons/` に保存する
4. 新しい query / summary ページを作った場合は、`type: query` または `type: summary` を使い、`index.md` と `log.md` に反映する

### Generated Artifact Governance
- 生成されたツール、ワークフロー、UI、スクリプトの仕様・検証結果は、必要に応じて `wiki/queries/` または関連 `concepts/` ページへ記録する
- `wiki/workflows/` や `factory/` のような未定義ディレクトリは、`SCHEMA.md` と `index.md` の構造を更新するまでは新設しない
- 外部副作用を持つ処理（投稿、通知、cron変更、push、deploy）は、既存ポリシーかユーザー明示依頼がある場合のみ実行する
- 検証なしで生成物を production 相当に昇格しない。最低限、実行条件・検証結果・残リスクを記録する

### Quality Checks
編集後は必要に応じて以下を確認する:
- orphan pages
- duplicate pages
- missing or broken wikilinks
- stale pages
- unsupported claims
- contradictions without source/date context
- generated artifacts without owning spec or validation notes

---

## Cron パイプライン全体像（26ジョブ）

### 日次データ収集パイプライン（07:00 UTC / 16:00 JST）

```
blog-ingest (07:00) ──→ blog-triage (07:30) ──→ blog-wiki-ingest (07:50)
                          ↑ script: blog_checkpoint.py
                          ↑ script: blog_triage_checkpoint.py
                          ↑ script: blog_ingest.py

newsletter-ingest (07:10) ──→ newsletter-triage (07:20) ──→ newsletter-wiki-ingest (07:40)
                                ↑ script: process_email.py
                                ↑ script: newsletter_checkpoint.py
                                ↑ script: newsletter_triage_checkpoint.py

sitemap-monitor (06:00) ← no_agent, sitemap_monitor.py
```

### 日中パイプライン

```
active-crawl (11:00 UTC / 20:00 JST) — hot-topics.yaml ベースのプロアクティブ知識探索
trending-topics (12:00 UTC / 21:00 JST) — トレンドリサーチ
x-bookmarks-ingest (11:30, 23:30 UTC) — Xブックマークからの記事取り込み
x-accounts-scan (22:30, 2日毎) — 追跡Xアカウントの新規投稿スキャン
skeleton-enrich-daily (19:00 UTC) — スケルトンページの強化
```

### 夜間ナレッジ統合（18:00 UTC / 翌03:00 JST）

```
dreaming-collect (18:00) ──→ dreaming-group (18:10) ──→ dreaming-wiki-ingest (18:20)
                                ↑ script: dreaming_collect.py
                                ↑ script: dreaming_checkpoint.py
                                ↑ script: dreaming_group_checkpoint.py
```

### Wiki健全性パイプライン（17:50 UTC / 翌02:50 JST）

```
wiki-health-fix (17:50) ──→ wiki-watchdog-fix (17:35)
  ↑ script: wiki_health_json.py → wiki_health.py --json
  ↑ スキャン → 自動修正 → 修正後レポート（1ジョブに統合）
```

### 週次メンテナンス

```
wiki-graph-analysis (金 15:00 UTC) — グラフ分析・重複検出
tag-audit-weekly (月 10:00 UTC) — タグ監査・自動修正
check-skill-inventory (日 16:00 UTC) — スキル棚卸し
```

### 配信パイプライン

```
ai-topics-slack-hot-posts (00:30, 06:30, 12:30 UTC) ──→ ai-topics-discord-hot-posts (00:45, 06:45, 12:45 UTC)
  ↑ script: ai_topics_slack_hot_posts_context.py            ↑ script: discord_slack_relay.py (no_agent relay)

Weekly AI digest (月 00:00 UTC) → Telegram
```

### ヘルスモニタリング

```
pipeline-watchdog (2時間毎) ← no_agent, パイプラインヘルスチェック
```

---

## 主要スクリプト一覧

| スクリプト | 用途 | Cronジョブ |
|---|---|---|
| `blog_ingest.py` | blogwatcher RSS取得＋raw記事保存 | blog-ingest |
| `process_email.py` | Gmail IMAP経由ニュースレター取得 | newsletter-ingest |
| `fetch_x_bookmarks.py` | Xブックマーク取得＋URLスクレイピング | x-bookmarks-ingest |
| `fetch_x_accounts.py` | 追跡Xアカウントの新規投稿スキャン | x-accounts-scan |
| `sitemap_monitor.py` | 企業ブログのsitemap監視 | sitemap-monitor |
| `build_x_wiki.py` | x-accounts.yaml → エンティティスケルトンページ生成 | 手動 |
| `build_blog_wiki.py` | blogs.opml → ブログエンティティページ生成 | 手動 |
| `dreaming.py` / `dreaming_collect.py` | 夜間ナレッジ統合 | dreaming-* |
| `wiki_health.py` | Wiki健全性スキャン（--json対応、0.28秒） | wiki-health-fix |
| `wiki_health_json.py` | wiki_health.py --json ラッパー | wiki-health-fix |
| `wiki_graph.py` | Wikiグラフ分析（重複・壊れリンク） | wiki-graph-analysis |
| `validate_index.py` | index.md バリデーション | pre-commit |
| `trending_topics.py` | トレンドトピックリサーチ | trending-topics |
| `papers_index.py` | arXiv論文インデックス管理 | 手動 |
| `youtube_meta.py` | YouTube動画メタデータ取得 | 手動 |
| `cloudflare_email.py` | Cloudflare Email Routing経由配信 | 手動 |

---

## Git 規約

### Pre-commit Hooks

```bash
# hooks有効化（clone後一度だけ必要）
cd ~/ai-topics && git config core.hooksPath .githooks
```

2つのバリデーターがコミットをブロックする可能性あり:

1. **`validate_index.py`**: `wiki/index.md` の構造的破損を検出 — baked-in line numbers, `|-` corruption, `[[[` triple brackets, truncation artifacts
2. **`pre-commit-tag-validator.py`**: 全ステージングWikiページのタグが `SCHEMA.md` 分類学に従っているか検証

### ブロックされた場合の対応

- **タグ違反**: `SCHEMA.md` に正規タグを追加 → `git add wiki/SCHEMA.md` → 再コミット
- **Index破損**: `wiki-graph-health` スキルの修復手順を参照
- **`--no-verify` は最終手段**: タグ分類学に追加できない残存ノイズのみ許容

### コミットメッセージ規約

```bash
git commit -m 'wiki: <簡潔な要約>'
```

- メッセージに `&` を含む場合はシングルクォート必須（shell展開防止）
- `&&` チェーンは避け、`git add` `git commit` `git push` を分割実行

### プッシュ手順

```bash
cd ~/ai-topics && git pull --rebase && git add wiki/ && git commit -m 'wiki: <summary>' && git push
```

---

## Hermes Agent スキルシステム

このリポジトリの運用は以下のHermes Agentスキルに依存しています:

| スキル | 役割 |
|---|---|
| `llm-wiki` | Wikiの読み書き・検索・保守の中核スキル |
| `wiki-ingestion-pipelines` | 全インジェストパイプラインの包括的ガイド |
| `wiki-graph-health` | Wiki健全性チェック・修復 |
| `wiki-daily-report` | 日次Wiki変更レポート生成 |
| `cron-job-management` | Cronジョブの作成・監視・デバッグ |
| `blogwatcher-db` | blogwatcher SQLite DBクエリ |
| `semantic-article-grouping` | 記事のセマンティックグループ化・トリアージ |
| `hermes-report-quality` | Gwern品質技術（Anti-Examples, MoS等） |
| `raw-article-filename-policy` | raw記事ファイル命名規約 |

---

## 絶対に守るべき重要なルール

### ファイルパス
- **Canonical wiki path**: `~/wiki/` → `~/ai-topics/wiki/` （実パス: `/opt/data/ai-topics/wiki/`）
- **使ってはいけないパス**: `/opt/data/home/wiki/`, `/opt/data/.hermes/home/wiki/` など
- **サブエージェントには絶対パスを明示**: `delegate_task` のcontext では `/opt/data/ai-topics/wiki/...` と書く

### read_file の罠
- **`read_file` の出力をファイルに貼り付けない**: 行番号プレフィックス `N|` が baked-in corruption を引き起こす
- **patch の old_string に `read_file` 出力を使わない**: `sed -n 'N,Np'` か `head -N` で生の内容を確認する

### タグ
- **タグ分類学（SCHEMA.md Tag Taxonomy）を最初に読む**
- **新規タグは必ずSCHEMA.mdに追加してから使用**
- **複合kebab-caseタグ（5語以上）は常にエラー**: 分解して個別タグに
- **Pre-commit hookは全ステージングファイルを検査する**: 自分が変更したページ以外の違反も修正する

### index.md
- **行フォーマットを確認してからpatch**: `- [[slug]]` か `NNN|- [[slug]]` か
- **pipe corruption (`|-`) を検出したら即修復**
- **アルファベット順を維持**: 大規模indexでは順序が崩れている可能性あり → `read_file` で正確な位置確認
- **ヘッダーカウントを更新**: `Total pages`, section counts

### log.md
- **`write_file` で上書きしない**: log.mdはappend-only → `cat /tmp/new.md log.md > /tmp/merged.md && mv /tmp/merged.md log.md`
- **logのローテーション**: 500行以上で `log-YYYY.md` にアーカイブ

### delegate_task
- **完了後は必ずファイル存在確認**: サブエージェントは嘘をつくことがある
- **subagent context には絶対パスを書く**
- **並列処理は最大3つ**: `max_concurrent_children=3`

### Git
- **`git commit` のメッセージに `&` を含める時はシングルクォート**: `git commit -m 'wiki: agents & tools'`
- **heredoc に `&` を含めない**: シェル展開スキャンがブロックする → `write_file` でテンポラリファイル作成
- **`sed -i` のたびに `grep -n` し直す**: 行番号がずれる

### web_extract
- **複数URLはバッチ取得**: `web_extract(urls=[url1, url2, ...])` で効率的に
- **切り詰め（LLM summarization timeout）されたら `execute_code` + httpx/BS4 にフォールバック**
- **ボットプロテクション（Anubis等）を検出したらスキップ**

---

## 環境変数とパス

| 変数/パス | 値 | 用途 |
|---|---|---|
| `HERMES_HOME` | `/opt/data/.hermes` | Hermes Agent設定ルート |
| `EMAIL_IMAP_HOST` | (`.env`から) | ニュースレターIMAP |
| `EMAIL_ADDRESS` | (`.env`から) | ニュースレター取得アカウント |
| `SLACK_BOT_TOKEN` | (`.env`から) | Slack API |
| `AI_TOPICS_SLACK_BOT_USER_ID` | `U0AS46GSGFN` | Slack Dedup用 |
| Canonical scripts | `~/ai-topics/scripts/` | Git追跡 |
| Cron実行scripts | `~/.hermes/scripts/` | cronから実行（ai-topics/scriptsと同期要） |
| blogwatcher DB | `~/.blogwatcher/blogwatcher.db` | RSS記事DB |
| xurl | `/opt/data/bin/xurl` | X API CLI |
| Python venv | `/opt/data/.hermes/venv/bin/python3` | cronジョブPython環境 |

---

## スキルの修正

リポジトリ内のカスタムスキルは `config/hermes/skills/` にあります。修正する場合:
1. `config/hermes/skills/<category>/<name>/SKILL.md` を編集
2. テスト: `/skill <name>` でロード確認
3. Commit: `git add config/hermes/skills/ && git commit -m 'wiki: update skill <name>' && git push`

---

## 緊急時対応フローチャート

1. **Pre-commit block** → エラーメッセージを読む → 違反ファイルを特定 → SCHEMA.mdのタグを追加 or ページのタグを修正
2. **Cronジョブ失敗** → `cronjob list` で `last_status` 確認 → `last_delivery_error` 確認 → 出力ログ確認
3. **Index破損** → `validate_index.py` 実行 → 破損パターン特定 → `wiki-graph-health` スキルの修復手順適用
4. **サブエージェントがファイルを作成しなかった** → `git status` 確認 → 手動で `delegate_task` 再実行 or ファイル手動作成

---

> **最終更新**: 2026-05-13
> **メンテナー**: Hermes Agent (kzinmr)
