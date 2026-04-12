---
title: "How Coding Agents Work"
aliases:
  - how-agents-work
  - coding-agent-architecture
  - agent-internals
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - agent-architecture
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/"
---

# How Coding Agents Work

コーディングエージェントの内部仕組みを理解するための概念モデル。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/)で詳述。

## 構成要素

### 1. Large Language Models
- ベースとなるLLM（Claude Opus 4.6、GPT-4など）
- コード生成・理解・推論の中核エンジン

### 2. Chat Templated Prompts
- システムプロンプト、ユーザーメッセージ、アシスタント応答の構造化
- 会話履歴をテンプレート化してモデルに投入

### 3. Token Caching
- 繰り返し使用するプロンプト部分のキャッシュ
- コスト削減と応答速度向上

### 4. Calling Tools
- エージェントが外部ツール（ファイルシステム、シェル、ブラウザなど）を呼び出す機能
- コード実行、テスト、デバッグの自動化

### 5. The System Prompt
- エージェントの振る舞いを定義するメタ指示
- プロジェクト固有の制約やコーディング規約を含む

### 6. Reasoning
- モデルの内部推論プロセス
- Chain-of-thoughtやstep-by-step思考の顕在化

### 7. LLM + System Prompt + Tools in a Loop
- これらすべてが統合されたエージェントループ
- 生成→実行→検証→修正のサイクル

## なぜ理解が必要か

コーディングエージェントを効果的に使用するには、その内部仕組みを理解することが不可欠。特に：
- **デバッグ**: エージェントがなぜ特定のエラーを出力するかを理解
- **プロンプト設計**: エージェントの能力と制限に合わせた指示作成
- **コスト管理**: トークン使用量とキャッシングの最適化
- **セキュリティ**: エージェントのファイルシステムアクセスと外部通信の制御

## 関連概念

- [[agentic-engineering]] — 上位概念
- [[subagents]] — エージェントの階層化
- [[using-git-with-agents]] — バージョン管理統合
- [[token-caching]] — コスト最適化
