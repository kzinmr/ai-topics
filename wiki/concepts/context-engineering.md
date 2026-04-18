---
title: "Context Engineering"
created: 2026-04-13
updated: 2026-04-13
source: 
  - "OpenAI Cookbook — Context engineering patterns"
  - "Andrej Karpathy, X/Twitter, June 25, 2025"
  - "Anthropic — Effective context engineering for AI agents"
  - "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines (Khattab et al., 2023)"
tags: [context-management, prompt-engineering, optimization, karpathy, dspy]
status: active
---

# Context Engineering

コンテキストウィンドウを効果的に活用し、LLMの性能を最大化する体系的アプローチ。Karpathyは「コンテキストエンジニアリングは、次のステップに最適な情報でコンテキストウィンドウを満たす繊細な芸術と科学」と定義している。

## Karpathyによる定義とSoftware 2.0との関係

Andrej Karpathyは2025年6月25日のX投稿で以下のように述べている：

> "People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step."

Karpathyは「Software 2.0」（2017年）において、ニューラルネットワークを「最適可能なパラメータ」として扱うパラダイムシフトを提唱した。この考え方は、LLM時代の「コンテキストエンジニアリング」に直接接続している：

| パラダイム | プログラミング対象 | 最適化手法 |
|------------|-------------------|-----------|
| Software 1.0 | 明示的なコード（Python, C++等） | 手書きロジック |
| Software 2.0 | ニューラルネットワーク重み | 勾配降下法 |
| Software 3.0 | LLMへのプロンプト/コンテキスト | コンテキストエンジニアリング |

### Autoresearchとの関係

Karpathyのautoresearch（2026年3月）は、評価可能な目標があればAIエージェントがパラメータを自律的に最適化するパターンを示している：

1. 不変の評価器（prepare.py）を固定
2. エージェントが1つの編集可能なファイル（train.py）を変更
3. 一晩中実行し、改善を保持、後退を破棄

このパターンは、DSPyの「プロンプトをハイパーパラメータとして最適化」と構造的に同一である。

## DSPyとの関係性

DSPy（Declarative Self-improving Python）は、プロンプトを学習パラメータとして扱い、最適化によって自動的に改善するフレームワークである。KarpathyのContext EngineeringとDSPyは根本的に同じ方向を向いている：

| 観点 | KarpathyのContext Engineering | DSPy |
|------|------------------------------|------|
| 焦点 | コンテキスト全体の設計 | プロンプトの最適化 |
| 手法 | 情報の選択・整理・圧縮 | 宣言的プログラミング・コンパイル |
| 目的 | LLMの性能最大化 | 自己改善パイプライン |
| パラダイム | Software 3.0 | Software 2.0の延長 |

DSPyの最適化パターン：
- **MIPROv2**: ベイズ最適化によるプロンプト改善
- **BootstrapFewShot**: 自己生成によるデモ例の最適化
- **GEPA**: 反映的進化によるプロンプト最適化

## Core Techniques

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
- **Prompt-only Focus**: プロンプトのみを最適化し、コンテキスト全体を軽視する


## Prerequisites & Supporting Concepts

Effective context engineering requires understanding several foundational concepts:

- **[[token-economics]]** — Cost per million tokens optimization determines how much context you can afford
- **[[attention-mechanism-variants]]** — Different attention mechanisms affect context window efficiency (KV cache, compute scaling)
- **[[context-compression]]** — Techniques for reducing context size while preserving information
- **[[context-window-management]]** — Organizing context for maximum effectiveness


- [[token-economics]] — Inference cost analysis
- [[attention-mechanism-variants]] — KV cache and attention efficiency
- [[context-compression]] — Reducing context window size
- [[concepts/ai-agent-engineering/context-compaction]] — Agent-specific compaction techniques
- [[dspy]] — Declarative LM programming for automated context optimization
- [[concepts/context-window-management]] — Context Window Management
- [[concepts/context-compaction]] — Context Compaction
- [[concepts/long-context-coding-agents]] — Long-Context via Coding Agents
- [[concepts/dspy]] — DSPy: Declarative Self-improving Python
- [[entities/andrej-karpathy]] — Andrej Karpathy
