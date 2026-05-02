---
title: "Context Window Management"
type: concept
aliases:
  - context-window-management
  - context-management
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - prompting
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/"
---

# Context Window Management

コーディングエージェントのコンテキストウィンドウを効果的に管理し、品質とコストを最適化するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/)で詳述。

## 核心原則

> "Context windows have a maximum size, and they have a cost. Every token in the context costs money and compute — and the more you put in, the harder it is for the model to pay attention to the right parts."

コンテキストウィンドウは有限のリソース。無制限に入れてよいわけではない。

## Drew Breunigの5つのコンテキストパターン

Willisonが[Drew Breunigの分析](https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/)を通じて紹介したコンテキスト管理の体系:

### 1. Context Poisoning（コンテキスト汚染）
> "When a hallucination or other error makes it into the context, where it is repeatedly referenced."

ハルシネーションやエラーがコンテキストに混入し、以降の応答全体に悪影響が連鎖する現象。

**対策**: エージェントの出力を検証し、誤った情報がコンテキストに定着する前にセッションをリセット。

### 2. Context Distraction（コンテキスト注意散漫）
> "When a context grows so long that the model over-focuses on the recent context, neglecting what it was originally told."

コンテキストが長くなると、モデルが最初の指示を忘れて最近の内容に注意を奪われる。

**対策**: Context Summarization（要約）、定期的なセッションリフレッシュ。

### 3. Context Quarantine（コンテキスト隔離）
> "The act of isolating contexts in their own dedicated threads."

Willisonはこれを**sub-agents**パターンと呼ぶ。各タスクを独立したスレッド/セッションで実行し、コンテキストの汚染や拡散を防ぐ。

**実装例**:
- Claude Codeの新規セッション起動
- 並列エージェントでの独立ワークスペース
- `plan.md`ファイルでの状態引き継ぎ

### 4. Context Pruning（コンテキスト剪定）
> "Removing irrelevant or otherwise unneeded information from the context."

不要な情報をコンテキストから削除し、モデルの注意を重要な部分に集中させる。

### 5. Context Summarization（コンテキスト要約）
> "Boiling down an accrued context into a condensed summary."

長時間のセッションで蓄積されたコンテキストを要約し、次のセッションに引き継ぐ。

### 6. Context Offloading（コンテキスト外部化）
> "The act of storing information outside the LLM's context."

最も実用的なパターンの一つ。エージェントが `plan.md` や `notes.md` などのファイルをリポジトリに書き込み、必要なときにファイルから読み込むことで、コンテキストウィンドウの制限を回避。

**実装例**:
- コーディングエージェントが作業中に `plan.md` を作成・更新
- 次回セッションでファイルを読み込んで状態を復元
- 永続的なメモリとして機能

## Tool Loadoutパターン

> "Selecting a subset of tools to enable for a prompt, based on research that shows anything beyond 20 can confuse some models."

エージェントに一度に与えるツールの数は20以下に抑えるのが効果的。多すぎるツールはモデルの注意を散漫にする。

## 有効コンテキストウィンドウは50-60%

> *"Context rot sets in as the window fills. Effective window is ~50-60% of max."*
> — Sankalp (Claude Code 2.0 Guide)

モデルの性能はコンテキストが埋まるにつれて低下する。最大トークン数の50-60%が実用的な限界。

| モデル | 最大コンテキスト | 実用的な限界 |
|--------|----------------|-------------|
| Opus 4.5 | 200K tokens | ~120K tokens |
| GPT-5.2 | 400K tokens | ~240K tokens |
| Gemini 3 Pro | 1M tokens | ~600K tokens |

**Sankalpの推奨**: コンテキスト使用率が60%に達したら、`/compact`または`/handoff`でセッションを整理する。

## コンテキスト管理の実践的戦略

| 戦略 | 手法 | 効果 |
|------|------|------|
| セッション分割 | Context Quarantine | 汚染・散漫の防止 |
| ファイル外部化 | Context Offloading | コンテキスト制約の回避 |
| 定期的要約 | Context Summarization | 長期セッションの維持 |
| ツール絞り込み | Tool Loadout | 注意の集中 |
| 不要情報削除 | Context Pruning | 品質向上 |
| 60%ルール | `/compact` at 60% | 性能劣化の防止 |

## 関連概念

- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] — エージェントの内部仕組み（token caching含む）
- [[concepts/subagents]] — Context Quarantineの実装パターン
- [[concepts/agentic-engineering]] — 上位概念
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — コンテキスト管理失敗の帰結

## 参照

- [[simon-willison]] — Agentic Engineering Patterns創始者
- [Drew Breunig — How to Fix Your Context](https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/)
