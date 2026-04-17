# Changelog — Hermes Agent System

Hermes Agent のインフラ・スクリプト・設定・スキルなどシステム側の変更履歴。
wiki コンテンツの変更は `wiki/log.md` で管理。

書式: `## YYYY-MM-DD — 概要` / 項目は箇条書き / 新しいものが上

---

## 2026-04-12 — スキルライフサイクル基盤

- `scripts/check_new_skills.py` 新規作成 — unmanaged local skill の差分検出
- Hermes cron 「Skill Inventory Check」登録 (毎週月曜 08:00 UTC → Slack)
- `shelley/skill-lifecycle-roadmap.md` 新規作成 — Phase 1→4 ロードマップ

## 2026-04-12 — Hermes 設定のレポ管理

- `config/hermes/SOUL.md` 追加 (`~/.hermes/SOUL.md` → symlink)
- `config/hermes/skills/` 追加 — プロジェクト固有スキル5個を `skills.external_dirs` 経由で管理
  - wiki: wiki-entity-upgrade, x-account-enrichment
  - research: blog-author-thought-analysis, opinion-leader-depth-analysis, semantic-article-grouping
- `claude-mythos-model` スキル削除 (one-off)
- `~/.hermes/config.yaml` に `skills.external_dirs: [~/ai-topics/config/hermes/skills]` 設定

## 2026-04-12 — ビルドキャッシュ整理

- `blog_authors.json`, `x_accounts.json` → `scripts/cache/` に統合 (.gitignore)
- `wiki/raw/x_accounts.json` 削除 (Layer 1 の定義に合致しないため)
- スクリプトのパス参照を `Path(__file__).resolve().parent / "cache"` に統一

## 2026-04-12 — inbox/ 導入 (受信データの分離)

- `inbox/newsletters/` — email パイプライン日次ダイジェスト (旧 `wiki/raw/newsletters/`)
- `inbox/rss-scans/` — blogwatcher-cli 日次スキャンレポート (旧 `wiki/raw/rss-scans/`)
- `wiki/raw/` を llm-wiki スキル本来の定義 (不変ソース素材) に復元
- `process_email.py` 出力先を `inbox/newsletters/` に変更
- データフロー: `config/feeds/` (設定) → `inbox/` (受信) → `wiki/raw/` (トリアージ済み) → `wiki/Layer 2` (キュレーション)

## 2026-04-12 — 購読設定の移動・リネーム

- `feeds/` → `config/feeds/`
- スクリプト・symlink 追従

## 2026-04-12 — Shelley 作業領域

- `shelley/` 新規作成 — Shelley の調査・設計ドキュメント置き場
- `docs/` から o11y 戦略・Braintrust API ref・Phoenix 調査を移動

## 2026-04-12 — レポ構成の初期整理

- `scripts/` — 自動化スクリプトをレポに統合 (`~/scripts/*` → symlink)
- `docs/` — SETUP.md, email-receiving-docs.md をレポに統合
- `systemd/` — service ファイルをレポに統合
- `README.md`, `.gitignore` 新規作成
- `hermes-o11y-strategy.md` をレポルートから移動
- 全サービス (email-watcher, wiki-server, hermes-gateway) の symlink 互換性確保
