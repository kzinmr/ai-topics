# Ops 作業領域

Hermes Agent の運用基盤に関する調査・検討・設計ドキュメントを管理するディレクトリ。

## 目的

Hermes の運用改善 (o11y、インフラ、ツール選定など) に関する調査・設定作業などのメタ作業の成果物置き場。
wiki/ や hermes/ はHermesが管理する知識資産であり、この領域はそれとは別の「運用者側の作業ノート」に相当する。

## 命名規則

- 調査メモ: `<topic>_research.md` (例: `phoenix_research.md`)
- 戦略・設計: `<topic>-strategy.md` (例: `hermes-o11y-strategy.md`)
- API リファレンス: `<tool>-api-reference.md`
- 作業ログ: `<topic>-worklog.md`

## 現在のドキュメント

| ファイル | 内容 |
|---|---|
| `hermes-o11y-strategy.md` | LLM o11y 連携戦略 (Braintrust 主系 + Arize Phoenix 待機系) |
| `braintrust-logging-api-reference.md` | Braintrust Python SDK Logging/Tracing API リファレンス |
| `phoenix_research.md` | Arize Phoenix トレース取り込み調査 |
| `skill-lifecycle-roadmap.md` | スキルライフサイクル管理ロードマップ (Phase 1–4) |
