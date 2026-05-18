---
title: Codex Prompting
type: concept
created: 2026-05-12
updated: 2026-05-12
tags:
  - prompting
  - coding-agents
  - harness-engineering
  - metaprompting
  - openai
sources:
  - raw/articles/2026-01-14_openai-codex-prompting-guide.md
  - https://github.com/openai/codex
---

# Codex Prompting

OpenAI [[entities/openai-codex]]（gpt-5.3-codex）向けのプロンプト設計パターンとベストプラクティス。OpenAI Cookbookの「Codex Prompting Guide」に基づく。

## コア原則

### 1. 行動優先（Bias for Action）

Codexのプロンプト設計で最も重要な原則。モデルに計画を明示的に出力させたり、ユーザー確認を促したりする指示はパフォーマンスを著しく低下させる。

- ❌ **アンチパターン**: 「まず計画を立ててから実行してください」
- ❌ **アンチパターン**: 「各ステップの前にユーザーに確認してください」
- ✅ **推奨**: 「タスクが完了するかブロッカーに当たるまで停止しないでください」

理由: 計画の明示的な出力はモデルの早期停止（early stopping）を引き起こす。モデルは内部的に計画しているため、書き出させる必要はない。

### 2. 簡潔でストレートな指示

「アシスタント語」（assistant speak）を排除し、必要最小限のコンテキストのみを与える。

- ❌ **アンチパターン**: 長大なロール説明や人格設定
- ❌ **アンチパターン**: 「あなたは親切で知的で勤勉なAIアシスタントです…」
- ✅ **推奨**: 具体的な行動指示と制約のみ

### 3. 具象例の提供

特定の振る舞いを期待する場合、抽象的な指示より具象例（few-shot examples）が効果的。ただし、一般的なコーディングタスクや標準フォーマットでは必ずしも必要ない。

### 4. システム的なテスト

プロンプト変更は必ずEval（評価タスク）でテストする。pass/fail評価とpreference-based評価の両方を使用。

## 標準システムプロンプト構造

Codex CLIの標準プロンプトは以下のセクションで構成される：

```
# General — ツール選択の基本方針
# Autonomy and Persistence — 自律性と永続性
# Codebase Exploration — コードベース探索戦略
# Tool Use — ツール使用のベストプラクティス
# Frontend Quality — UI品質基準
# Coding Standards — コーディング規約
# Communication — コミュニケーションスタイル
```

各セクションの重要スニペット：

| セクション | 最重要スニペット |
|-----------|----------------|
| General | "When searching for text or files, prefer using grep/rg/locate over find/ls" |
| Autonomy | "Never wait for user confirmation unless you encounter an error you cannot resolve" |
| Exploration | "Read relevant files fully before editing them" |
| Tool Use | "Parallelize independent tool calls" / "Use patch for targeted edits" |
| Frontend | "Make UIs functional — buttons and forms should work" |
| Communication | "Write concise responses without preambles. Don't list out what you're about to do — just do it" |

## アンチパターン（削除すべき指示）

| アンチパターン | 問題 | 修正 |
|-------------|------|------|
| 計画の明示的要求 | 早期停止を誘発 | 内部的計画に任せる |
| 確認の要求 | 不要なインタラクション増加 | エラー時のみ確認 |
| 冗長なロール説明 | トークン浪費、指示の希釈 | 最小限の簡潔な指示 |
| 矛盾する指示 | 「徹底的に」と「簡潔に」の併用 | 各概念の具体的な定義を提供 |

## メタプロンプティング（自己改善プロンプト）

Codexの強力な機能として、モデル自身にプロンプトを改善させる「メタプロンプティング」がある。

### 基本メタプロンプト

```
<instructions>
保存された会話を分析し、アシスタントの行動パターンの改善点を特定。
具体的なシステムプロンプトの変更案を提案してください。

## パターン分析
- うまくいった点
- ミスや見逃した機会
- 複数ターンにわたる再発的問題
- 指示に従えなかった箇所

## 変更提案（各提案につき）
1. 追加/修正/削除する正確なテキスト
2. 変更の正当化理由
3. 期待される改善後の振る舞いの例

## ルール
- この会話に固有でない、一般化可能な変更を提案
- タスク完了への影響が大きい変更を優先
- ダウンサイドがある場合は明記
</instructions>
```

### メタプロンプティングの効果的な使い方

1. **反復実行**: 同じ会話に対してメタプロンプトを複数回実行し、共通して現れる改善案を採用する（1回だけだと会話固有の過剰適合の可能性がある）

2. **Evalでの検証**: メタプロンプトから得た改善案は必ずEvalで効果を測定する。改善に見えて実際には悪化するケースがある

3. **目的別のメタプロンプト**:
   - **過剰思考（overthinking）対策**: 「最初のツール呼び出しまでの時間を短縮する指示変更を提案して」
   - **冗長な前置き対策**: 「ユーザー更新指示を好みの制約に合うように書き直して」

4. **プロアクティブなプロンプト生成**: 最小限のプロンプトでタスクを成功させた後、「この成功パターンに基づいて、より良いシステムプロンプトを書いて」と依頼する

## ツール設計とプロンプトの相互作用

プロンプトの効果はツール実装に大きく依存する：

- **apply_patch**: ファジーマッチ実装により、モデルは正確な文字列一致を気にせず編集できる。プロンプトで「Use patch for targeted edits rather than rewriting entire files」と指示
- **ターミナル並列化**: バックグラウンド実行 + 完了通知の仕組みがある場合、「Parallelize independent terminal calls」が効果的
- **ブラウザツール**: UI作業の視覚的検証に使用するようプロンプトで指示

## 関連トピック

- [[entities/openai-codex]] — OpenAI Codex エージェント
- [[concepts/metaprompting]] — メタプロンプティング
- [[concepts/agent-harness]] — エージェントハーネス設計
- [[concepts/prompt-engineering]] — プロンプトエンジニアリング全般
- [[concepts/coding-agents]] — コーディングエージェント比較
