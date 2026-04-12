---
title: "Context Engineering"
created: 2026-04-13
source: "OpenAI Cookbook — Context engineering patterns"
tags: [context-management, prompt-engineering, optimization]
status: draft
---

# Context Engineering

OpenAI Cookbookで示される、コンテキストウィンドウを効果的に活用するパターン。AnthropicのContext Engineeringとは異なり、**技術的実装**に焦点を当てている。

## Core Concept

限られたコンテキストウィンドウ内で、最も重要な情報を効果的に配置し、モデルの性能を最大化する。

## Key Techniques

### 1. Context Compression

- 冗長な情報の削除
- 重要な事実の抽出と要約
- キーワード/エンティティの優先順位付け

### 2. Context Ordering

- 重要な情報を最初と最後に配置（recency/primacy effect）
- 関連する情報をグループ化
- 時系列または論理構造で整理

### 3. Dynamic Context Management

- タスクの複雑さに応じたコンテキスト量の調整
- 不要な情報の動的排除
- コンテキスト使用量の監視と最適化

### 4. Context Chunking

- large documentsを意味のあるチャンクに分割
- 各チャンクにメタデータを付加
- 必要に応じてチャンクを組み合わせ

## Implementation Patterns

### Retrieval-Augmented Context

```python
def build_context(query, documents, max_tokens):
    relevant = retrieve_top_k(query, documents, k=5)
    compressed = compress_documents(relevant, target_size=max_tokens*0.8)
    instructions = load_system_instructions()
    return combine(instructions, compressed)
```

### Progressive Context Loading

1. 基本コンテキストで初期応答生成
2. ユーザーのフォローアップに応じて追加コンテキストロード
3. 会話の進行に伴いコンテキストを更新

## Anti-Patterns

- **Context Overflow**: 最大トークン数を超える情報投入
- **Context Dilution**: 無関係な情報で重要な事実が埋もれる
- **Static Context**: 会話の進行に伴うコンテキスト更新を怠る

## Related

- [[concepts/context-window-management]] — Context Window Management
- [[concepts/context-engineering]] — Context Engineering (Anthropic)
- [[concepts/context-compaction]] — Context Compaction
- [[concepts/long-context-coding-agents]] — Long-Context via Coding Agents
