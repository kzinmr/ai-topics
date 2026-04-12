# AI Topics — Hermes Knowledge Base

Hermes Agent が管理する AI/ML トピックの知識ベースリポジトリ。

## ディレクトリ構成

```
ai-topics/
├── README.md               # このファイル
├── .gitignore
│
├── wiki/                   # 知識ベース本体
│   ├── SCHEMA.md           # 構造ポリシー・更新ルール
│   ├── index.md            # 全ページの索引
│   ├── log.md              # 更新履歴
│   │
│   ├── concepts/           # [Layer 2] 概念・手法・技術 (how/why)
│   ├── entities/           # [Layer 2] 人物・企業・プロダクト (who/what)
│   ├── comparisons/        # [Layer 2] ツール/モデル比較 (vs)
│   ├── queries/            # [Layer 2] 調査クエリ結果 (予約)
│   │
│   └── raw/                # [Layer 1] 取り込み前の生データ (情報源)
│       ├── articles/       # newsletter記事の自動スクレイプ結果
│       ├── newsletters/    # newsletter日次ダイジェスト (自動生成)
│       ├── rss-scans/      # RSSスキャン日次レポート
│       ├── papers/         # arXiv論文 (予約)
│       ├── transcripts/    # ポッドキャスト文字起こし (予約)
│       ├── assets/         # 画像・図表 (予約)
│       └── x_accounts.json # X/Twitter追跡アカウント (処理済みデータ)
│
├── feeds/                  # 情報ソース定義
│   ├── hn-popular-blogs-2025.opml  # HN人気ブログ 84件
│   └── x-accounts.yaml    # X/Twitter追跡アカウント定義
│
├── scripts/                # 自動化スクリプト
│   ├── process_email.py    # メール→raw/articles 変換パイプライン
│   ├── email_watcher.sh    # Maildir監視 (systemd経由)
│   ├── check_mail.sh       # メール手動確認CLI
│   ├── build_blog_wiki.py  # OPML→entities ページ生成
│   ├── build_x_wiki.py     # x-accounts→entities ページ生成
│   └── wiki_server.py      # Wikiブラウザサーバー (port 8000)
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
═══ Layer 1: 取り込み (wiki/raw/) ═══

Newsletter Email → Maildir → email_watcher → process_email.py
  → wiki/raw/articles/*.md       (個別記事スクレイプ)
  → wiki/raw/newsletters/*.md    (日次ダイジェスト)
  → git push

RSS Feeds → blogwatcher-cli (cron) → wiki/raw/rss-scans/*.md

═══ Layer 2: キュレーション (wiki/{concepts,entities,comparisons}/) ═══

Hermes Agent (Discord) が raw/ から知識を抽出・構造化:
  → wiki/concepts/    ▒ 技術概念
  → wiki/entities/     ▒ 人物・企業
  → wiki/comparisons/  ▒ ツール比較
  → index.md, log.md 更新
  → git push
```

## シンボリックリンク

旧パスとの互換性のため以下のシンボリックリンクが存在:
- `~/wiki` → `~/ai-topics/wiki/`
- `~/scripts/*` → `~/ai-topics/scripts/*` (各スクリプト個別)
- `~/hn-popular-blogs-2025.opml` → `~/ai-topics/feeds/hn-popular-blogs-2025.opml`
- `~/x-accounts.yaml` → `~/ai-topics/feeds/x-accounts.yaml`
- `~/SETUP.md` → `~/ai-topics/docs/SETUP.md`
