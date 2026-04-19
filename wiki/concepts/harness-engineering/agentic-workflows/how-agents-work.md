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

## Plan Mode vs Conversational Planning

> *"Plan mode feels like a hack that was necessary for older generations of models that were not great at adhering to prompts... Instead of 'plan mode', I simply start a conversation with the model, ask a question, let it google, explore code, create a plan together, and when I'm happy with what I see, I write 'build'."*
> — Peter Steinberger

従来の「Plan Mode」（事前に計画を立ててから実行）は、モデルの指示遵守能力が低かった時代のハック。最新のモデルでは**会話形式で計画を作り、"build"と書くだけで実行に移れる**。

### 会話的計画の利点
- モデルがコードを探索しながら計画を立てる → 精度向上
- 人間のフィードバックをリアルタイムで反映できる
- 計画モードのオーバーヘッドが不要

## Claude CodeのTask Toolアーキテクチャ

SankalpによるClaude Code 2.0の分析から、サブエージェントの構造が明らかになっている：

### サブエージェントの種類

| 種類 | コンテキスト | 用途 |
|------|------------|------|
| `general-purpose` | 全コンテキスト継承 | 一般的なタスク委任 |
| `plan` | 全コンテキスト継承 | 計画作成 |
| `Explore` | 新規セッション | ファイル検索・コードリーディング（読取専用） |

### Task Toolの重要パラメータ

```json
{
  "required": ["description", "prompt", "subagent_type"],
  "properties": {
    "description": "3-5語のタスク概要",
    "prompt": "タスク指示",
    "subagent_type": "general-purpose | Explore | Plan",
    "model": "sonnet | opus | haiku (親エージェントと同じモデルがデフォルト)",
    "run_in_background": "長時間スクリプト用にtrue",
    "resume": "以前のセッションから再開するエージェントID"
  }
}
```

### Exploreエージェントの制約

```markdown
=== CRITICAL: READ-ONLY MODE - NO FILE MODIFICATIONS ===
STRICTLY PROHIBITED: Creating, modifying, deleting, moving files.
USE: GLOB, GREP, READ tools only
BASH: ONLY for read-only ops (ls, git status, cat, find). NEVER mkdir, rm, npm install, etc.
```

Exploreエージェントは**読取専用**で設計されており、ファイル変更は一切できない。これにより、探索中にコードベースを壊すリスクを排除している。

## 関連概念

- [[../agentic-engineering]] — 上位概念
- [[subagents]] — エージェントの階層化
- [[using-git-with-agents]] — バージョン管理統合
- [[context-window-management]] — Task Toolはコンテキストを分割する
- [[cli-first-development]] — エージェントのツール呼び出しパターン

## 参照

- [[simon-willison]] — How Coding Agents Work概念提唱者
- [[sankalp]] — Claude Code 2.0 Task Tool分析
- [[steipete]] — Plan Mode不要論
- [Agentic Engineering Patterns — How Agents Work](https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/)
- [A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
- [Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
