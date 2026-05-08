---
title: "Anthropic Infrastructure Postmortems (2025-2026)"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - anthropic
  - infrastructure
  - postmortem
  - incident-analysis
aliases:
  - Claude quality degradation
  - Anthropic postmortem
  - Claude Code quality issues
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_a-postmortem-of-three-recent-issues.md
  - raw/articles/2026-05-08_anthropic-engineering_april-23-postmortem.md
  - https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
  - https://www.anthropic.com/engineering/april-23-postmortem
related:
  - infrastructure-noise-agent-evals
  - anthropic
---

# Anthropic Infrastructure Postmortems (2025-2026)

Anthropicが公表した2つの大規模品質低下インシデントの詳細な事後分析。インフラバグ（2025年8-9月）とプロダクト変更（2026年3-4月）の2部構成。

---

## Part 1: 2025年8-9月 インフラバグ3連発

> "We never reduce model quality due to demand, time of day, or server load."

### Bug 1: コンテキストウィンドウルーティングエラー

- **期間**: 2025年8月5日〜9月16-18日
- **影響**: Sonnet 4リクエストの最大16%（最悪時）。Claude Codeユーザーの30%が1回以上影響
- **原因**: 短いコンテキストのリクエストが1Mトークンコンテキスト用サーバーに誤ルーティング
- **悪化要因**: 「スティッキー」ルーティング（一度誤ルーティングされると後続も同じ）
- **修正**: ルーティングロジック修正（9月4日〜18日）

### Bug 2: 出力破損

- **期間**: 2025年8月25日〜9月2日
- **影響**: Opus 4.1/4, Sonnet 4 — 英語プロンプトにタイ語や中国語文字が混入、コードに構文エラー
- **原因**: TPUサーバーのランタイムパフォーマンス最適化によるミスコンフィグ。低確率トークンに誤って高確率が割り当てられた
- **修正**: 変更ロールバック + 予期せぬ文字出力の検出テスト追加

### Bug 3: XLA:TPU 近似top-k誤コンパイル

- **期間**: 2025年8月25日〜9月4-12日
- **モデル**: Haiku 3.5（確認済み）、Sonnet 4/Opus 3（可能性）
- **原因**: 近似top-k操作が特定のバッチサイズとモデル構成で完全に誤った結果を返すXLAコンパイラの潜在バグ
- **複雑性**: 2024年12月のワークアラウンドが誤って除去されバグが露出。bf16/fp32混合精度の不一致
- **修正**: 近似top-k → 正確top-k + fp32標準化

### 検出の困難さ

- 各バグが異なるプラットフォーム・異なる頻度で異なる症状 → 「ランダムで一貫性のない劣化」に見えた
- 社内評価がユーザーの報告する劣化を捕捉できず（Claudeは単独ミスからの回復が上手い）
- プライバシー制約がユーザーインタラクション調査を阻害

---

## Part 2: 2026年3-4月 Claude Code品質低下

> 3つの独立した変更が「広範で一貫性のない劣化」として現れた。

### Issue 1: デフォルト推論努力の誤設定

- **変更**: 3月4日 — reasoning effortを `high` → `medium` に変更
- **理由**: `high` モードでの極端な長レイテンシ（UIフリーズ）対策
- **結果**: Claude Codeが「賢くなくなった」という報告殺到
- **修正**: 4月7日 — Opus 4.7は `xhigh`、他は `high` に設定
- **教訓**: レイテンシより知能を優先すべき（ユーザーは低速でも高品質を選ぶ）

### Issue 2: 推論履歴消失バグ

- **変更**: 3月26日 — 1時間以上アイドル状態のセッションで古い思考をクリアする最適化
- **バグ**: 1回だけのはずがセッション終了まで毎ターンクリアし続ける
- **症状**: 忘却・反復・奇妙なツール選択。「なぜその判断をしたか」の記憶喪失
- **副次的影響**: キャッシュミス連発 → 使用制限の消耗加速
- **修正**: 4月10日
- **発見経緯**: Opus 4.7のCode ReviewがPRから発見（Opus 4.6は見逃した）

### Issue 3: 冗長性削減システムプロンプト

- **変更**: 4月16日 — 「ツール間テキスト≤25語、最終応答≤100語」の指示を追加
- **結果**: コーディング品質3%低下（Opus 4.6/4.7両方）
- **修正**: 4月20日即時ロールバック
- **教訓**: システムプロンプト変更の影響評価が不十分。より広範な評価スイートが必要

### 再発防止策

- より多くの内部スタッフが公開ビルドと同一のClaude Codeを使用
- システムプロンプト変更に対するモデル別広範評価 + ソーク期間 + 段階的ロールアウト
- Code Reviewツールの改善（追加リポジトリをコンテキストとしてサポート）
- @ClaudeDevs（X）でプロダクト判断の詳細説明を公開

---

## 共通パターン

1. **検出の遅れ**: 複数の独立した変更が重なり「ランダムな劣化」に見える
2. **社内評価の限界**: 既存の評価スイートがユーザー体験の劣化を捕捉できない
3. **プライバシー vs 調査**: ユーザーデータへのアクセス制限が根本原因特定を遅らせる
4. **ユーザーフィードバックの重要性**: `/feedback`, `/bug`, ソーシャルメディアでの具体的報告が最終的な解決の鍵

## See Also

- [[entities/anthropic]] — Anthropic entity
- [[concepts/infrastructure-noise-agent-evals]] — Infrastructure noise in agent evals
- [[concepts/ai-resistant-evaluations]] — AI-resistant evaluation design
