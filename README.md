# AI Topics — Hermes Knowledge Base

Hermes Agent が管理する AI/ML トピックの知識ベースリポジトリ。

## ディレクトリ構成

```
ai-topics/
├── README.md               # このファイル
├── .gitignore
│
├── inbox/                  # 受信データ (パイプライン出力、トリアージ待ち)
│   ├── newsletters/        # emailパイプラインの日次ダイジェスト
│   └── rss-scans/          # blogwatcher-cliの日次スキャンレポート
│
├── wiki/                   # llm-wiki スキル準拠の知識ベース
│   ├── SCHEMA.md           # [Layer 3] 構造ポリシー・更新ルール
│   ├── index.md            # 全ページの索引
│   ├── log.md              # 更新履歴
│   │
│   ├── raw/                # [Layer 1] 不変のソース素材 (Hermesは読み取り専用)
│   │   ├── articles/       # スクレイプ済み記事
│   │   ├── papers/         # arXiv論文
│   │   ├── transcripts/    # ポッドキャスト文字起こし
│   │   └── assets/         # 画像・図表
│   │
│   ├── concepts/           # [Layer 2] 概念・手法・技術 (how/why)
│   ├── entities/           # [Layer 2] 人物・企業・プロダクト (who/what)
│   ├── comparisons/        # [Layer 2] ツール/モデル比較 (vs)
│   └── queries/            # [Layer 2] 調査クエリ結果
│
├── config/
│   ├── feeds/              # 購読ソース定義
│   │   ├── blogs.opml      # HN人気ブログ 84件
│   │   └── x-accounts.yaml # X/Twitter追跡アカウント定義
│   └── hermes/             # Hermes Agent 設定 (skills.external_dirs 経由で読み込み)
│       ├── SOUL.md         # エージェントの人格・責務定義
│       └── skills/         # プロジェクト固有のlocalスキル
│           ├── wiki/       # wikiエンティティ強化・アカウントエンリッチ
│           └── research/   # ブログ分析・記事グルーピング
│
├── scripts/                # 自動化スクリプト
│   ├── process_email.py    # メール→raw/articles 変換パイプライン
│   ├── email_watcher.sh    # Maildir監視 (systemd経由)
│   ├── check_mail.sh       # メール手動確認CLI
│   ├── build_blog_wiki.py  # OPML→entities ページ生成
│   ├── build_x_wiki.py     # x-accounts→entities ページ生成
│   ├── wiki_server.py      # Wikiブラウザサーバー (port 8000)
│   └── cache/              # スクレイプキャッシュ (.gitignore、再生成可能)
│
├── systemd/                # systemd ユニットファイル
│   ├── email-watcher.service
│   ├── hermes-gateway.service
│   └── wiki-server.service
│
└── docs/                   # プロジェクトドキュメント
│   ├── SETUP.md            # セットアップガイド
│   └── email-receiving-docs.md  # exe.dev メール受信設定
│
├── shelley/                # Shelley (exe.dev コーディングエージェント) 作業領域
│   ├── README.md           # この領域の説明
│   ├── hermes-o11y-strategy.md           # LLM o11y 戦略
│   ├── braintrust-logging-api-reference.md # Braintrust API リファレンス
│   └── phoenix_research.md               # Arize Phoenix 調査
```

## サービス構成

| サービス | systemd unit | ポート | 役割 |
|----------|-------------|--------|------|
| Email Watcher | `email-watcher` | — | Maildir監視→newsletter自動処理 |
| Hermes Gateway | `hermes-gateway` | — | Discord bot (Hermes Agent) |
| Wiki Server | `wiki-server` | 8000 | Wikiブラウザ |

## データフロー

```
═══ 購読 & 受信 ═══

config/feeds/                  購読先の定義 (設定)
  │
  ├─ Newsletter Email → Maildir → process_email.py
  │    ├→ inbox/newsletters/*.md     日次ダイジェスト
  │    └→ wiki/raw/articles/*.md     リンク先記事スクレイプ
  │
  └─ RSS feeds → blogwatcher-cli (cron)
       └→ inbox/rss-scans/*.md       日次スキャンレポート

═══ llm-wiki Layer 1 → Layer 2 (キュレーション) ═══

Hermes Agent (Discord) が inbox/ + wiki/raw/ から知識を抽出・構造化:
  inbox/*          トリアージ (重要記事を特定し raw/ に取り込み)
  wiki/raw/*   →  wiki/concepts/      技術概念
                   wiki/entities/      人物・企業
                   wiki/comparisons/   ツール比較
                   wiki/queries/       調査結果
                   index.md, log.md 更新 → git push
```

## シンボリックリンク

旧パスとの互換性のため以下のシンボリックリンクが存在:
- `~/wiki` → `~/ai-topics/wiki/`
- `~/scripts/*` → `~/ai-topics/scripts/*` (各スクリプト個別)
- `~/hn-popular-blogs-2025.opml` → `~/ai-topics/config/feeds/blogs.opml`
- `~/x-accounts.yaml` → `~/ai-topics/config/feeds/x-accounts.yaml`
- `~/SETUP.md` → `~/ai-topics/docs/SETUP.md`
- `~/.hermes/SOUL.md` → `~/ai-topics/config/hermes/SOUL.md`
- `~/.hermes/config.yaml` の `skills.external_dirs` → `~/ai-topics/config/hermes/skills/`
