# AI Topics — Hermes Knowledge Base

Hermes Agent が管理する AI/ML トピックの知識ベースリポジトリ。

## ディレクトリ構成

```
ai-topics/
├── README.md               # このファイル
├── .gitignore
│
├── hermes/                 # Newsletter ダイジェスト (日次自動生成)
│   └── YYYY-MM-DD-newsletter.md
│
├── wiki/                   # 知識ベース本体
│   ├── SCHEMA.md           # 構造ポリシー・更新ルール
│   ├── index.md            # 全ページの索引
│   ├── log.md              # 更新履歴
│   ├── concepts/           # 概念・手法・技術 (how/why)
│   ├── entities/           # 人物・企業・プロダクト (who/what)
│   ├── comparisons/        # ツール/モデル比較 (vs)
│   ├── queries/            # 調査クエリ結果 (予約)
│   └── raw/                # 生の情報源
│       ├── articles/       # newsletter記事の自動取り込み
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
    ├── SETUP.md                          # セットアップガイド
    ├── hermes-o11y-strategy.md           # LLM o11y 戦略
    ├── braintrust-logging-api-reference.md # Braintrust API リファレンス
    ├── phoenix_research.md               # Arize Phoenix 調査
    └── email-receiving-docs.md           # exe.dev メール受信設定
```

## サービス構成

| サービス | systemd unit | ポート | 役割 |
|----------|-------------|--------|------|
| Email Watcher | `email-watcher` | — | Maildir監視→newsletter自動処理 |
| Hermes Gateway | `hermes-gateway` | — | Discord bot (Hermes Agent) |
| Wiki Server | `wiki-server` | 8000 | Wikiブラウザ |

## データフロー

```
Newsletter Email → Maildir → email_watcher → process_email.py
  → raw/articles/*.md (生記事)
  → hermes/YYYY-MM-DD-newsletter.md (日次ダイジェスト)
  → git push

Hermes Agent (Discord) → wiki/concepts/, entities/, comparisons/
  → index.md, log.md 更新
  → git push

Cron (blogwatcher-cli) → daily RSS scan → ~/.blogwatcher-cli/
```

## シンボリックリンク

旧パスとの互換性のため以下のシンボリックリンクが存在:
- `~/wiki` → `~/ai-topics/wiki/`
- `~/scripts/*` → `~/ai-topics/scripts/*` (各スクリプト個別)
- `~/hn-popular-blogs-2025.opml` → `~/ai-topics/feeds/hn-popular-blogs-2025.opml`
- `~/x-accounts.yaml` → `~/ai-topics/feeds/x-accounts.yaml`
- `~/SETUP.md` → `~/ai-topics/docs/SETUP.md`
