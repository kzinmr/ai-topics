---
title: "DSPy — Declarative Self-improving Python for LMs"
tags: [training, concept, ai-agents, llm, prompting, rAG, evaluations]
created: 2026-04-24
updated: 2026-04-24
---

# DSPy: Declarative Self-improving Language Systems

**DSPy** (Declarative Self-improving Python for LMs, "dee-spai")は、Stanford NLP Group（Omar Khattab, Arnav Singhviら）が開発した**宣言的LMプログラミングフレームワーク**。

## Core Philosophy: Prompting is Not Programming

> *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."*
> — Omar Khattab, PhD Dissertation (2024)

DSPyの根本的な主張は以下の通り：

**従来のアプローチ（プロンプトエンジニアリング）:**
1. 問題をステップに分解する
2. 各ステップに対して試行錯誤でプロンプトを書く
3. モデルが変わればプロンプトも書き直す
4. パイプラインの品質はプロンプトの品質に直接依存

**DSPyのアプローチ（宣言的プログラミング）:**
1. **Signature**で入出力の契約を宣言する
2. **Module**で推論パターンを構成する
3. **Metric**で成功基準を定義する
4. **Teleprompter**が自動的に最適化する

> *"It's actually better to think of language models as modules in programs, not end products."*
> — Omar Khattab, Cohere talk (2024)

このパラダイムシフトは、**PyTorchがニューラルネットワークにもたらしたもの**と類似している：

| 時代 | 深層学習 | LLM |
|------|---------|-----|
| Before | NumPyで手動重み調整 | 手動プロンプトエンジニアリング |
| After | PyTorchで宣言的モジュール構成 | DSPyで宣言的Signature構成 |
| Key insight | 逆伝播が重みを自動最適化 | Teleprompterがプロンプトを自動最適化 |

---

## Architecture: The Three Abstractions

### 1. Signatures — 入出力の契約

Signatureは「LLMに何をしたいか」を**宣言的に**記述する。実装の詳細（プロンプト文本体）は含まない。

```python
class AnswerQuestion(dspy.Signature):
    """Answer questions with short, factual responses."""
    question = dspy.InputField()
    answer = dspy.OutputField()

class GenerateSearchQuery(dspy.Signature):
    """Generate a search query for a retrieval tool."""
    context = dspy.InputField(desc="Available background information")
    question = dspy.InputField()
    query = dspy.OutputField()
```

**設計原則:**
- **Docstring** = タスクの説明（optimizerがプロンプト生成に使用）
- **InputField/OutputField** = 型付きインターフェース
- **desc** = フィールドの意味論的制約
- Signatureは**モデル非依存** — 同じSignatureがGPT-4, Claude, Llamaで動作

### 2. Modules — 推論パターン

ModulesはSignatureを実行に結びつける。PyTorchの`nn.Module`に相当。

| Module | 用途 | PyTorch相当 |
|--------|------|------------|
| `dspy.Predict` | 基本的な予測 | `nn.Linear` |
| `dspy.ChainOfThought` | 段階的推論 | — |
| `dspy.ReAct` | 推論＋行動ループ | — |
| `dspy.ProgramOfThought` | コード生成＋実行 | — |
| `dspy.MultiChainComparison` | 複数推論パスの比較 | — |

```python
# Moduleの定義
class RAG(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_query = dspy.ChainOfThought(GenerateSearchQuery)
        self.retrieve = dspy.Retrieve(k=3)
        self.answer = dspy.ChainOfThought(AnswerQuestion)
    
    def forward(self, question):
        query = self.generate_query(question=question).query
        context = self.retrieve(query).passages
        return self.answer(context=context, question=question)
```

**重要な洞察:** Moduleはプロンプトを**含まない**。プロンプトはコンパイル時にoptimizerによって生成される。

### 3. Teleprompters — 自動最適化エンジン

Teleprompter（現在は「optimizer」と呼称）は、**訓練データとメトリクスを与えると、パイプライン全体のプロンプトを自動最適化する**アルゴリズム。

| Optimizer | アルゴリズム | 特徴 |
|-----------|-------------|------|
| `BootstrapFewShot` | 正解例の自動収集 | 最小限の最適化、高速 |
| `BootstrapFewShotWithRandomSearch` | 正解例＋ランダム探索 | 安定した品質向上 |
| `MIPROv2` | ベイズ最適化＋CoT | 最先端の品質、高コスト |
| `COPRO` | 勾配ベースのプロンプト進化 | 中間コスト/品質 |
| `Ensemble` | 複数Moduleの投票 | 推論時スケーリング |

```python
# 最適化の例
metric = dspy.evaluate.answer_exact_match  # 成功基準
tp = dspy.MIPROv2(metric=metric, num_candidates=5)
optimized_rag = tp.compile(RAG(), trainset=train_examples)
```

**Teleprompterの動作原理:**
1. **Candidate generation:** 訓練例からデモンストレーションを自動収集
2. **Evaluation:** 各候補をメトリクスで評価
3. **Selection:** Pareto最適解（品質 vs トークンコスト）を選択
4. **Compilation:** 選択されたデモンストレーションをプロンプトに埋め込み

---

## DSPy Assertions — 計算的制約

DSPy v2.3で導入されたAssertionsは、**プロンプト出力に対する実行時検証**を提供する。

```python
@dspy.assert
def validate_answer(answer):
    assert len(answer) < 100, "Answer too long"
    assert not any(word in answer.lower() for word in ["i don't know", "unknown"]), "No uncertainty allowed"
```

**動作:**
1. Assertion違反を検出すると、DSPyは自動的に**再推論**を試みる
2. 違反情報を含むフィードバックをLMに提供
3. 最大N回まで再試行（設定可能）
4. それでも失敗する場合は例外を送出

これは**従来のバリデーション**（出力後のチェック）と異なり、**自己修正ループ**をパイプラインに組み込む。

---

## Fine-Tuning + Prompt Optimization: Two Steps

2024年7月の論文 *"Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together"* は重要な洞察を提供：

**発見:**
- Prompt optimization alone → +15% improvement
- Fine-tuning alone → +12% improvement
- **Combined** → +23% improvement（相加効果ではなく相乗効果）

**理由:** Fine-tuningはモデルの基本的な推論能力を向上させ、prompt optimizationはタスク固有の戦略を最適化する。両者は**異なる次元**を改善するため、組み合わせると相乗効果が生まれる。

---

## DSPy vs Other Approaches: Paradigm Comparison

### 統合パタームの分類

| パターン | 代表例 | 制御の主体 | プロンプト | 最適化 |
|----------|--------|-----------|-----------|--------|
| **Orchestration** | LangChain, LangGraph | 開発者 | 手動 | なし |
| **Data-centric** | LlamaIndex | 開発者 | 半自動 | 検索最適化 |
| **Declarative** | **DSPy** | optimizer | 自動生成 | **コンパイル時** |
| **Recursive** | **RLMs** | LM自身 | REPL環境 | **推論時** |
| **Agentic** | OpenAI Agents SDK | orchestrator + LM | 手動＋ツール | 実行時 |
| **Genetic** | **GEPA** | 進化アルゴリズム | 自動進化 | **世代間最適化** |

### DSPy vs LangChain/LangGraph

| 次元 | DSPy | LangChain/LangGraph |
|------|------|---------------------|
| **設計思想** | 宣言的（what） | 命令的（how） |
| **プロンプト** | コンパイル時に自動生成 | 開発者が手動で記述 |
| **モデル切替** | 再コンパイルで自動適応 | プロンプトの書き直しが必要 |
| **最適化** | Teleprompterがデータ駆動 | 手動チューニング |
| **抽象化レベル** | Signature/Module | Chain/Agent/Tool |
| **コード量** | 最小限（宣言のみ） | 詳細な制御フロー |
| **学習曲線** | 急（新しいパラダイム） | 緩い（既存のパターンに近い） |
| **エコシステム** | 研究志向、小規模 | 大規模、多様な統合 |

### DSPy vs RLMs

| 次元 | DSPy | RLMs |
|------|------|------|
| **最適化のタイミング** | コンパイル時（訓練データが必要） | 推論時（実行中に自己最適化） |
| **コンテキスト管理** | 固定プロンプト（デモンストレーション埋め込み） | REPL環境（再帰的コンテキストアクセス） |
| **制御の主体** | Teleprompter（外部optimizer） | LM自身（コード生成で自己制御） |
| **データ要件** | 訓練例（10-50以上） | なし（ゼロショット） |
| **再計算可能性** | 高い（コンパイル結果は決定論的） | 低い（推論時の非決定性） |
| **適用シナリオ** | 反復的パイプライン（QA, RAG, 分類） | 超長文コンテキスト（10M+トークン） |
| **共通の洞察** | **LMをモジュールとして扱え** | **LMが自身のコンテキストを管理させろ** |

### DSPy vs GEPA

| 次元 | DSPy Teleprompters | GEPA |
|------|-------------------|------|
| **アルゴリズム** | ブートストラップ＋選択 | 遺伝的アルゴリズム＋Pareto最適 |
| **探索空間** | デモンストレーションの選択/順序 | プロンプト文本体の進化 |
| **最適化対象** | プロンプト＋few-shot例 | プロンプト文本体＋推論戦略 |
| **計算コスト** | 中程度 | 高（世代を跨ぐ評価） |
| **品質** | 安定した改善 | 場合によりRLベース最適化を上回る |
| **統合可能性** | DSPyパイプライン内 | 独立した最適化フェーズ |

---

## DSPyのパイプライン構成パターン

### Pattern 1: Retrieve-then-Answer

```python
class RAG(dspy.Module):
    def forward(self, question):
        docs = Retrieve(query=question)
        return Answer(context=docs, question=question)
```

### Pattern 2: Generate-Search-Refine

```python
class MultiHop(dspy.Module):
    def forward(self, question):
        q1 = GenerateQuery(question=question)
        d1 = Retrieve(query=q1)
        q2 = GenerateNextQuery(question=question, prev=d1)
        d2 = Retrieve(query=q2)
        return Answer(context=d1+d2, question=question)
```

### Pattern 3: Multi-Agent Debate

```python
class Debate(dspy.Module):
    def forward(self, question):
        a1 = Expert1(question=question)
        a2 = Expert2(question=question)
        a3 = Expert3(question=question)
        return CompareAndSelect(answers=[a1, a2, a3])
```

**重要な洞察:** DSPyのパイプラインは**モデル非依存**。同じパイプライン定義がGPT-4、Claude、Llamaで動作し、各モデルに対してoptimizerが最適なプロンプトを自動生成する。

---

## 設計哲学の進化

### Phase 1: DSP (2022) — Denotative Suggestion Pipelines
- 手動プロンプトテンプレートのラッパー
- 基本的なモジュール構成
- 最適化なし

### Phase 2: DSPy v1 (2023) — Declarative Self-improving Python
- Telepromptersによる自動最適化導入
- Signature/Module抽象化
- ICLR 2024 Spotlight

### Phase 3: DSPy v2 (2024) — Assertions & Fine-tuning Integration
- DSPy Assertions（実行時検証＋自己修正）
- Fine-tuning + Prompt Optimizationの相乗効果
- MIPROv2 optimizer

### Phase 4: DSPy v3 (2025+) — Towards Foundation Model Programming
- GEPA統合（遺伝的プロンプト進化）
- マルチモジュールGRPO
- RLMsとの概念統合（Khattabの最新研究）

---

## 適用ガイドライン

### DSPyが有効な場合
- 同じタスクを**繰り返し実行**するパイプラインがある
- **評価メトリクス**が明確に定義できる
- 訓練例（10-50以上）が利用可能、または生成可能
- 複数のLLMで同じパイプラインを実行したい
- プロンプトの保守コストが高い

### DSPyが不向きな場合
- **一度きりの探索的クエリ**（評価データがない）
- 非常に**動的なタスク**（Signatureが頻繁に変更される）
- **リアルタイム最適化**が必要（推論時の適応が必須）→ RLMsを検討
- **統合エコシステム**が重要（多くの外部ツールと連携）→ LangChainを検討

---

## 重要な論文と発表

| 日付 | タイトル | 主要洞察 |
|------|---------|---------|
| Oct 2023 | DSPy: Compiling Declarative Language Model Calls (ICLR 2024) | Teleprompterによる自動最適化のパラダイム提示 |
| Dec 2023 | DSPy Assertions | 実行時制約による自己修正パイプライン |
| Jun 2024 | Prompts as Auto-Optimized Training Hyperparameters | プロンプトはハイパーパラメータである |
| Jul 2024 | Fine-Tuning and Prompt Optimization: Two Great Steps | 両者の組み合わせが相乗効果を生む |
| 2025 | GEPA: Reflective Prompt Evolution | 遺伝的アルゴリズムによるプロンプト進化 |
| 2025 | RLMs | 再帰的コンテキスト処理（DSPyの次なる進化） |

---

## See Also

- [[omar-khattab]] — DSPyの創作者
- [[gepa]] — 遺伝的プロンプト最適化（DSPy optimizerの進化系）
- [[rlms]] — 再帰的言語モデル（DSPyとは異なる最適化アプローチ）
-  — DSPyのエージェントパターン
-  — DSPy以前のKhattabの検索フレームワーク
