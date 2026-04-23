---
title: LLM Integration Patterns — A Comparative Taxonomy
description: LLMをシステムに統合する主要なアプローチの分類と比較。Orchestration, Declarative Programming, Recursive Execution, Agentic Workflows, Genetic Optimizationの5つのパラダイムを、制御構造、最適化タイミング、コンテキスト管理、適用シナリオの観点から相対化する。
aliases:
  - llm-system-integration-patterns
  - llm-programming-paradigms
status: complete
depth_tracking:
  created: 2026-04-13
  last_updated: 2026-04-13
  target_depth: concept-level comparative analysis
  key_sources:
    - "DSPy: Compiling Declarative Language Model Calls (Khattab et al., ICLR 2024)"
    - "Recursive Language Models (Zhang, Kraska, Khattab, arXiv 2025)"
    - "GEPA: Reflective Prompt Evolution (Khattab et al., 2025)"
    - "Anthropic Building Effective Agents (2025)"
    - "LangChain/LangGraph Architecture (2024-2025)"
    - "LlamaIndex RAG Patterns (2024-2025)"
related:
  - dspy
  - rlms
  - gepa
  - agentic-engineering
  - langchain
  - langgraph
  - llamaindex
---

# LLM Integration Patterns: A Comparative Taxonomy

LLMをプロダクションシステムに統合するアプローチは、2023年から2025年にかけて急速に進化した。本ページは主要なパターンを**制御構造**、**最適化タイミング**、**コンテキスト管理**の3つの次元で分類し、相対化する。

---

## 5つの統合パラダイム

### パラダイムマップ

```
                  制御の主体
              開発者 ←———————→ LM自身
              │                   │
  最  │   LangChain           RLMs
  適  │   LlamaIndex          (Recursive)
  化  │   OpenAI Agents       Anthropic Workflows
  タ  │       SDK
  イ  │                   │
  ミ  │     DSPy              GEPA
  ン  │   (Declarative)       (Genetic)
  グ  │
  │
  V
  最適化の次元
```

### 1. Orchestration Patterns (LangChain, LangGraph, LlamaIndex)

**哲学:** 開発者がLLM呼び出しのフローを明示的に制御する。

| 側面 | 詳細 |
|------|------|
| **制御主体** | 開発者（Pythonコード） |
| **プロンプト** | 手動で作成・保守 |
| **最適化** | なし（開発者の試行錯誤に依存） |
| **コンテキスト** | 固定ウィンドウ＋外部検索 |
| **長所** | 直感的、豊富な統合、即座に動作 |
| **短所** | プロンプト保守が高い、モデル依存 |
| **適用** | プロトタイピング、ツール統合、既存ワークフロー |

**LangChain**は「チェーン」という概念でLLM呼び出しを連結する。**LangGraph**は状態機械によるエージェントループを追加。**LlamaIndex**はデータ取得とインデックス構築に特化。

**根本的限界:** プロンプトが「魔法の文字列」のまま。モデルを変更すると、プロンプトの書き直しが必要。品質は開発者のプロンプト設計スキルに直接依存。

### 2. Declarative Programming (DSPy)

**哲学:** LLMを**最適化可能なモジュール**として宣言的にプログラミングする。

| 側面 | 詳細 |
|------|------|
| **制御主体** | optimizer（コンパイル時） |
| **プロンプト** | 自動生成（訓練データから） |
| **最適化** | コンパイル時（Teleprompter） |
| **コンテキスト** | 固定（デモンストレーション埋め込み） |
| **長所** | モデル非依存、自動最適化、再現性 |
| **短所** | 訓練データが必要、学習曲線が急 |
| **適用** | 反復的パイプライン（RAG, QA, 分類） |

DSPyの革新的洞察は、**プロンプトをハイパーパラメータとして扱う**こと。開発者は「何をしたいか」（Signature）だけを宣言し、「どうするか」（プロンプト文本体）はoptimizerが決定する。

**PyTorchとの類似性:**
```
PyTorch: nn.Linear → optimizer (SGD) → 重み
DSPy:    Signature → optimizer (MIPROv2) → プロンプト
```

### 3. Recursive Execution (RLMs)

**哲学:** LLMに**自身のコンテキストアクセス**を制御させる。

| 側面 | 詳細 |
|------|------|
| **制御主体** | LM自身（REPL環境） |
| **プロンプト** | コード生成で自己制御 |
| **最適化** | 推論時（実行中の自己適応） |
| **コンテキスト** | 外部環境（無制限） |
| **長所** | 任意長のコンテキスト、コンテキストrot回避 |
| **短所** | 非決定性、デバッグ困難 |
| **適用** | 超長文理解（10M+トークン）、深層推論 |

RLMsの根本的洞察は、**コンテキストは外部変数である**ということ。従来のLLMはプロンプト内に全てのコンテキストを詰め込むが、RLMsはREPL環境を通じて必要な情報にアクセスする。

### 4. Agentic Workflows (Anthropic, OpenAI Agents SDK)

**哲学:** LLMを自律的なエージェントとしてツールと連携させる。

| 側面 | 詳細 |
|------|------|
| **制御主体** | orchestrator + LM |
| **プロンプト** | システム指示＋ツール定義 |
| **最適化** | 実行時（ツール選択、エラー処理） |
| **コンテキスト** | 固定＋ツール出力 |
| **長所** | 複雑なワークフロー、動的対応 |
| **短所** | 予期せぬ動作、制御困難 |
| **適用** | 自律タスク実行、複数ツール連携 |

Anthropicの **「Building Effective Agents」** は、エージェントを「hardcoded workflows」と「autonomous agents」に分類し、前者を推奨する。これはDSPyの宣言的アプローチに近い。

### 5. Genetic Optimization (GEPA)

**哲学:** プロンプトを**遺伝的アルゴリズムで進化**させる。

| 側面 | 詳細 |
|------|------|
| **制御主体** | 進化アルゴリズム |
| **プロンプト** | 自動進化（世代間） |
| **最適化** | 世代間（Pareto最適選択） |
| **コンテキスト** | 固定（親プロンプト） |
| **長所** | RLベース最適化を上回る場合がある |
| **短所** | 計算コストが高い |
| **適用** | プロンプト最適化、戦略発見 |

GEPAはDSPyのTeleprompterを**さらに一般化**したもの。DSPyがデモンストレーションを選択するのに対し、GEPAはプロンプト文本体を進化させる。

---

## 比較マトリクス

### 次元別比較

| 次元 | Orchestration | DSPy | RLMs | Agentic | GEPA |
|------|--------------|------|------|---------|------|
| **制御主体** | 開発者 | optimizer | LM自身 | orchestrator | 進化algo |
| **最適化timing** | なし | コンパイル時 | 推論時 | 実行時 | 世代間 |
| **コンテキスト** | 固定 | 固定 | 無制限 | 固定＋ツール | 固定 |
| **データ要件** | なし | 訓練例 | なし | なし | 評価メトリクス |
| **モデル依存** | 高い | 低い | 中程度 | 中程度 | 低い |
| **再現性** | 高い | 高い | 低い | 低い | 中程度 |
| **保守性** | 低い | 高い | 中程度 | 中程度 | 高い |
| **学習曲線** | 低い | 高い | 高い | 中程度 | 高い |
| **適用スコープ** | 汎用 | パイプライン | 超長文 | 自律タスク | 最適化 |

### パフォーマンス特性

| パターン | フレームワークオーバーヘッド | トークン効率 | 品質向上潜力 |
|----------|----------------------------|-------------|-------------|
| LangChain | ~10ms/call | 中 | 開発者依存 |
| LangGraph | ~14ms/call | 中 | 開発者依存 |
| LlamaIndex | ~6ms/call | 高 | 中 |
| **DSPy** | **~3.5ms/call** | **高** | **大** |
| Haystack | ~5.9ms/call | 高 | 中 |

DSPyが**最も低いフレームワークオーバーヘッド**を示す（AIMultiple 2025ベンチマーク）。これは、抽象化がコンパイル時に解決されるため、実行時のオーバーヘッドが最小限になる。

---

## 進化の系譜

### Khattabの研究トレイル

Omar Khattabの研究は、LLM統合パラダイムの進化を体現している：

```
ColBERT (2020) → 検索の「late interaction」
     ↓
Baleen (2021) → 複数ホップ推論
     ↓
DSPy (2023) → 宣言的LMプログラミング
     ↓
DSPy Assertions (2023) → 実行時検証
     ↓
GEPA (2025) → 遺伝的プロンプト進化
     ↓
RLMs (2025) → 再帰的コンテキスト処理
```

**一貫したテーマ:**
> *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."*

各段階で、**より多くの制御を開発者/LMに移譲**し、**より少ない手動チューニング**で**より高い品質**を達成することを目指している。

### DSPy → RLMs: パラダイムの継承と差異

| 継承点 | DSPy | RLMs |
|--------|------|------|
| **LMをモジュールとして扱う** | ✓ (Signature/Module) | ✓ (REPLコマンド) |
| **コンテキスト管理の自動化** | ✓ (Teleprompter) | ✓ (環境変数) |
| **モデル非依存** | ✓ | ✓ |
| **最適化のタイミング** | コンパイル時 | 推論時 |
| **訓練データ** | 必要 | 不要 |

RLMsはDSPyの**「コンパイル時最適化」を「推論時適応」に置き換えた**ものと見なせる。両者とも**LMをプログラマブルなコンポーネント**として扱うが、最適化のタイミングが異なる。

---

## 実践的選択ガイド

### シナリオ別推奨パターン

| シナリオ | 推奨パターン | 理由 |
|----------|-------------|------|
| プロトタイプ開発 | Orchestration | 高速、直感的 |
| 本番RAGパイプライン | **DSPy** | 自動最適化、モデル非依存 |
| 超長文理解（100K+ tokens） | **RLMs** | コンテキストrot回避 |
| 自律エージェント | Agentic | ツール連携、動的対応 |
| プロンプト品質向上 | **GEPA** | 遺伝的最適化 |
| コスト最適化 | DSPy → RLMs | 小モデルで高品質 |

### ハイブリッドアプローチ

実際のパイプラインは複数のパターンを組み合わせる：

```
LangChain (Orchestration)
  ├── DSPy Module (QA pipeline)
  │     └── Teleprompter optimized prompts
  ├── RLM (Long document processing)
  │     └── REPL environment for 10M+ tokens
  └── Agentic workflow (Tool use)
        └── Error handling, retries
```

**設計原則:**
1. **安定したパイプライン** → DSPyで最適化
2. **動的なコンテキスト** → RLMsで処理
3. **外部ツール連携** → Agenticで管理
4. **プロトタイプ** → Orchestrationで構築

---

## 重要な洞察

### 1. 「プロンプトはコードである」

DSPyの最も重要な洞察は、プロンプトを**コードと同じように扱う**こと。バージョン管理、テスト、最適化、デバッグの全てが適用可能。

### 2. 「最適化はタイミングが重要」

| タイミング | メリット | デメリット |
|-----------|---------|-----------|
| コンパイル時 (DSPy) | 再現性、安定性 | 訓練データ必要 |
| 推論時 (RLMs) | 動的適応 | 非決定性 |
| 世代間 (GEPA) | 大域的最適解探索 | 計算コスト |

### 3. 「制御の移譲が進化の方向性」

```
開発者完全制御 → optimizer制御 → LM自己制御
    (LangChain)     (DSPy)         (RLMs)
```

この方向性は、**より少ない人間の介入**で**より高い品質**を達成することを示している。

### 4. 「モデル非依存が本質的」

DSPy、RLMs、GEPAの共通点は、**特定のプロンプト文本体に依存しない**こと。モデルが進化しても、宣言的インターフェースはそのまま有効。

---

## See Also

- [[dspy]] — 宣言的LMプログラミング
- [[rlms]] — 再帰的言語モデル
- [[gepa]] — 遺伝的プロンプト最適化
- [[concepts/agentic-engineering.md]] — エージェントワークフローパターン
- [[omar-khattab]] — DSPy/GEPA/RLMsの創作者
- [[alex-zhang]] — RLMsの第一著者
- [[colbert]] — 検索のlate interactionパラダイム
