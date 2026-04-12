---
title: "AI Agent Engineering"
aliases:
  - ai-agent-engineering
  - agent system design
  - agent architecture
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-design
  - anthropic
status: L2
sources:
  - "https://www.anthropic.com/engineering/building-effective-agents"
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills"
  - "https://www.anthropic.com/engineering/advanced-tool-use"
  - "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
  - "https://www.anthropic.com/engineering/claude-code-sandboxing"
  - "https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
---

# AI Agent Engineering

Anthropic Engineeringが提唱する、**AIエージェントシステムの設計・構築方法论**。Agentic Engineering（個人の開発手法）とは異なり、エージェントアーキテクチャ、ワークフローパターン、ツール設計、セキュリティ、評価システムなどのシステム設計に焦点を当てる。

## Core Philosophy

> *"Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."*

- **Start Simple**: 単一LLM呼び出しを最適化し、必要な場合のみマルチステップ複雑性を追加
- **Trade-offs**: エージェントシステムは通常、**レイテンシとコスト**を犠牲にして**タスク性能**を向上させる
- **Transparency**: エージェントの計画ステップを明示的に表面化し、デバッグと信頼を確保

## Architecture: Workflows vs Agents

| Type | Definition | Best For |
|------|------------|----------|
| **Workflows** | LLMとツールを**事前定義されたコードパス**でオーケストレーション | 予測可能で明確に定義されたタスク |
| **Agents** | LLMが自身のプロセスとツール使用を**動的に指示** | 柔軟性とモデル駆動の意思決定が必要な開かれた問題 |

## Key Workflow Patterns

### 1. Prompt Chaining
- 連続したステップ。各LLM呼び出しが前の出力を処理
- 固定のサブタスクに分解可能なタスクに適す
- プログラム的な「ゲート」を検証用に追加

### 2. Routing
- 入力を分類 → 専門的なダウンストリームタスク/モデルに振り分け
- 明確な入力カテゴリで関心の分離が必要な場合

### 3. Parallelization
- **Sectioning**: 独立したサブタスクを同時実行
- **Voting**: 同じタスクを複数回実行し、多様な出力/信頼性を取得

### 4. Orchestrator-Workers
- 中央LLMがタスクを動的に分解、ワーカーLLMに委任、結果を統合
- 予測不可能なサブタスクに適す（サブタスクは**事前定義されない**）

### 5. Evaluator-Optimizer
- 生成LLM + 評価LLMの継続的フィードバックループ
- 明確な評価基準があり、反復的改善が測定可能な価値をもたらす場合

## Long-Running Agents

### Core Challenge
エージェントは離散的なコンテキストウィンドウで動作し、セッション間にメモリがない。

### Two-Fold Solution
1. **Initializer Agent**: 初回セッションで環境をセットアップ
   - `init.sh`（開発サーバー起動、ベースラインE2Eテスト）
   - `claude-progress.txt`（セッションごとの作業ログ）
   - `feature_list.json`（構造化された要件分解）
2. **Coding Agent**: 以降のセッションで増分的な進捗
   - 1機能ずつ実装、テスト、gitコミット
   - 次のセッションのために構造化された状態を残す

### Session Workflow
```
1. Orient: pwd で作業ディレクトリ確認
2. Review: claude-progress.txt と git log で最近の状態把握
3. Select: feature_list.json から最高優先度の未完了機能を選択
4. Verify Baseline: init.sh 実行、基本E2Eテスト
5. Implement & Commit: 1機能実装、テスト、コミット、進捗更新
```

## Agent Skills

> *"Building a skill for an agent is like putting together an onboarding guide for a new hire."*

- **Progressive Disclosure**（3段階読み込み）:
  1. Level 1: YAML frontmatter（name, description）をシステムプロンプトに事前ロード
  2. Level 2: タスク識別時にSKILL.md本文をフルロード
  3. Level 3+: 必要に応じて追加ファイル（reference.md, forms.md）をオンデマンドロード
- **Open Standard**（2025年12月）: クロスプラットフォーム移植性のために公開
- **Execution Model**: スキルはネイティブコード実行（Python, Bashなど）をトリガー可能

## Advanced Tool Use

### Tool Search Tool
- ツール定義をオンデマンドで発見（85%のトークン使用量削減）
- 50+ MCPツールで~72Kトークン → ~8.7Kトークンに削減

### Programmatic Tool Calling
- コード実行環境内でツールを呼び出し（中間結果をコンテキストから除外）
- 大規模データ処理に最適

### Tool Use Examples
- JSONスキーマだけでなく、使用パターンからの学習
- 1-5つの例で最小限、部分的、完全指定パターンを示す

## Sandboxing

> *"In our internal usage, we've found that sandboxing safely reduces permission prompts by 84%."*

- **Filesystem Isolation**: カレントディレクトリへのアクセス制限
- **Network Isolation**: Unixドメインソケット → 外部プロキシ経由
- **OS Primitives**: Linux bubblewrap & macOS seatbelt
- **Open Source**: サンドボックス化されたbashランタイムを研究プレビューとして公開

## Evals for Agents

### Types of Graders
- **Code-based**: 文字列マッチ、バイナリテスト、静的解析、結果検証
- **Model-based**: LLM判定（ファジールールベース）
- **Human**: 専門家レビュー

### Capability vs Regression Evals
- **Capability**: 「このエージェントは何ができるか？」— 低い合格率から開始
- **Regression**: 「既存の機能を壊していないか？」— 高い合格率を維持

## Context Engineering

> *"Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information."*

- **Just-in-Time Context**: 実行時にデータを動的に取得
- **Context Rot**: コンテキストウィンドウが埋まるにつれモデルの注意力が低下
- **Self-Managed Context**: エージェントが理解を層別に構築

## Related Concepts
- [[agentic-engineering]] — Simon Willisonの開発者中心アプローチ
- [[context-window-management]]
- [[agent-skills]]
- [[long-running-agents]]
- [[advanced-tool-use]]
- [[sandboxing]]
- [[evals-for-agents]]
- [[agent-loop]]
- [[multi-session-workflows]]

## Related Entities
- [[anthropic]] — Claude Agent SDK, Claude Code, Claude Platform
- [[simon-willison]] — 実践的Agentic Engineeringパターン

## Sources
- [Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
- [Effective Harnesses for Long-Running Agents (Anthropic)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Agent Skills (Anthropic)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Advanced Tool Use (Anthropic)](https://www.anthropic.com/engineering/advanced-tool-use)
- [Demystifying Evals (Anthropic)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Claude Code Sandboxing (Anthropic)](https://www.anthropic.com/engineering/claude-code-sandboxing)
- [Building Agents with Claude Agent SDK (Anthropic)](https://www.anthropic.com/engineering/building-agents-with-the-claai-agent-sdk)
- [Effective Context Engineering (Anthropic)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
