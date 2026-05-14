---
title: OpenAI Codex
type: entity
created: 2026-05-12
updated: 2026-05-14
tags:
  - product
  - coding-agent
  - openai
  - codex
  - agent-harness
  - autonomous-agents
aliases:
  - Codex CLI
  - codex-cli
  - GPT-5.3 Codex
  - gpt-5.3-codex
sources:
  - raw/articles/2026-01-14_openai-codex-prompting-guide.md
  - https://github.com/openai/codex
  - https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08
  - https://www.wsj.com/cio-journal/openai-is-working-with-consultants-to-sell-codex-f355b1b9
---

# OpenAI Codex

OpenAIのAIコーディングエージェント。CLI ベースの完全OSSエージェント（[GitHub](https://github.com/openai/codex)）として提供され、API経由でのカスタム統合も可能。モデルは `gpt-5.3-codex`。

コード生成・編集・コードベース探索・テスト・デプロイまで自律的に実行。コンパクション（会話圧縮）により数時間の自律実行が可能。

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | OpenAI |
| モデル | gpt-5.3-codex |
| 提供形態 | CLI（OSS）+ SDK + API |
| 特徴 | 自律実行、コンパクション、Windows/PowerShell対応 |
| 推論努力量 | medium（推奨）/ high / xhigh |

## 主要機能

- **長時間自律実行**: 数時間の自律タスク実行が可能。high/xhigh reasoning effort で最高難度タスクに対応
- **ファーストクラスコンパクション**: 会話履歴を圧縮し、コンテキスト制限を回避。長時間セッションでも新規チャット開始不要
- **Windows/PowerShell対応**: PowerShell環境での動作が大幅に改善
- **高速・トークン効率**: thinking tokens が削減され、medium reasoning effort でインタラクティブなコーディングに最適なバランスを実現

## アーキテクチャの特徴

- **apply_patch ツール**: ファジーマッチによるファイル編集。厳密な文字列置換ではなく、前後のコンテキストを考慮したマッチングを行う
- **バックグラウンドターミナル実行**: 長時間ビルドやテストをバックグラウンドで実行し、完了を通知
- **ツール並列化**: 独立したツール呼び出しを並列実行
- **ブラウザツール**: ドキュメント検索とUIの視覚的検証に使用

## プロンプト設計の特徴

[[concepts/codex-prompting]] 参照。主な特徴：

- **計画の明示的な出力を禁止**: モデルは内部的に計画するが、書き出させると早期停止の原因になる
- **確認不要の自律性**: エラー解決不能時以外はユーザー確認を待たない
- **簡潔なコミュニケーション**: preamble（前置き）やステータス更新を削除し、行動優先
- **メタプロンプティング**: モデル自身に過去の会話を分析させ、システムプロンプトの改善案を生成させる

## 成長指標（Growth Metrics）

| 日付 | WAU | ソース |
|------|-----|--------|
| 2026年3月中旬 | 200万 | Thibault Sottiaux（Codex責任者） |
| 2026年4月8日 | **300万** | Sam Altman 発表。Codex責任者Thibault Sottiauxが「1ヶ月弱前の200万から」と確認 |
| 2026年4月22日 | **400万** | WSJ報道。2週間で100万増加 |

2026年4月8日、Sam AltmanはCodexが週間アクティブユーザー300万人を突破したと発表し、利用制限のリセットを実施。さらに1,000万人に達するまで100万人増加ごとにリセットを繰り返す計画を表明した。Codex責任者Thibault Sottiauxは「1ヶ月弱前には200万人だった」と急成長を確認。

GPT-5.5ローンチ（2026年4月）以降、Codexの勢いは加速。4月22日にはWSJが400万WAU到達を報じ、2週間で100万人の純増を記録した。OpenAIはAccenture、Capgemini、PwCなどのコンサルティングファームと提携し、企業向けCodex販売を本格化。

Sources: [Business Today — Codex 3M WAU](https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08), [WSJ — OpenAI Working With Consultants to Sell Codex](https://www.wsj.com/cio-journal/openai-is-working-with-consultants-to-sell-codex-f355b1b9), [Gradually AI — Codex Statistics 2026](https://www.gradually.ai/en/codex-statistics/)


## 競合との比較

| 項目 | Codex | [[entities/claude-code]] | [[entities/cursor]] |
|------|-------|--------------------------|---------------------|
| モデル | gpt-5.3-codex | Opus 4.7 / Sonnet 4.6 | マルチモデル |
| OSS | ✅ 完全OSS | ❌ プロプライエタリ | ❌ |
| 自律性 | 高（数時間） | 高（Auto Mode） | 中 |
| コンパクション | ✅ ファーストクラス | — | — |

## 関連トピック

- [[concepts/codex-prompting]] — Codexプロンプト設計パターン
- [[concepts/agent-harness]] — エージェントハーネス設計
- [[concepts/metaprompting]] — メタプロンプティング（自己改善プロンプト）
- [[entities/openai]] — OpenAI
- [[concepts/coding-agents]] — コーディングエージェント全般
