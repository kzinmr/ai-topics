---
title: "LLM Patterns (Eugene Yan)"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - llm-patterns
  - evals
  - rag
  - fine-tuning
  - production-llm
aliases:
  - "7 patterns for building LLM systems"
  - "yan-llm-patterns"
  - "llm-based-systems-patterns"
sources:
  - https://eugeneyan.com/writing/llm-patterns/
  - raw/articles/2026-05-04_eugeneyan-llm-patterns.md
status: Level2
---

# LLM Patterns (Eugene Yan's Framework)

**Eugene Yan** が提唱する、LLMをプロダクションシステムに統合するための7つの実践的パターン。2023年7月の記事「[Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/)」で初めて体系的に整理され、その後O'Reilly共著「[What We've Learned From a Year of Building with LLMs](https://oreilly.com)」で発展・改訂された。

このフレームワークは、LLMアプリケーション開発における「評価なき開発は盲目」という哲学に基づき、データ中心の改善からユーザー向け設計までをカバーする。

---

## フレームワークの全体像

7つのパターンは **データ中心 → インフラ → ユーザー対面** のスペクトラムを形成する：

```
データ/内部        インフラ            ユーザー対面
  Evals     RAG     Caching      Guardrails      Defensive UX
  ↓         ↓         ↓             ↓                ↓
  Fine-tuning       (Infrastructure)          User Feedback
```

| パターン | 目標 | 焦点 | カテゴリ |
|---------|------|------|---------|
| **Evals** | パフォーマンスの測定 | データ/内部 | 🔵 評価基盤 |
| **RAG** | 外部知識の注入 | データ/内部 | 🔵 知識拡張 |
| **Fine-tuning** | タスク特化 | データ/内部 | 🔵 モデル適応 |
| **Caching** | レイテンシ・コスト削減 | インフラ | 🟢 効率化 |
| **Guardrails** | 品質・安全性の確保 | インフラ | 🟢 品質保証 |
| **Defensive UX** | エラーの優雅な処理 | ユーザー対面 | 🟡 UX設計 |
| **User Feedback** | 改善のためのデータ循環 | ユーザー対面 | 🟡 フィードバック |

**Evalsはすべての基盤** — 測定なしに改善は不可能。

---

## 各パターンの詳細

### 1. Evals — パフォーマンス測定

LLMエンジニアリングの基盤。評価なしに「飛び回る」ことになる。

**主要指標:**
- **BLEU/ROUGE** — n-gramベースの精度/再現率。創造的タスクでは人間の判断と相関が低い
- **BERTScore/MoverScore** — 埋め込みを使って同義語や意味的類似性を考慮
- **LLM-as-a-Judge (G-Eval)** — 強力なモデル（GPT-4）で他モデルを評価。GPT-4は人間評価者と~85%一致

**実装のヒント:**
- **Eval Driven Development (EDD)** — エンジニアリングの前にタスク固有のプロンプトと「正解」参照を収集
- **LLMバイアスの緩和:** LLMは最初の回答（Position bias）、長い回答（Verbosity bias）、自身の出力（Self-enhancement bias）を好む。評価時に回答順序を入れ替えてPosition biasを対策

**関連Wikiページ:**
- [[concepts/evals-for-ai-agents]] — AIエージェント向け評価（要拡充）
- [[eugene-yan--core-ideas]] — Eugene YanのEDD哲学とAlignEval

---

### 2. RAG (Retrieval-Augmented Generation) — 外部知識の注入

モデルを外部の最新データに基づかせ、幻覚（ハルシネーション）とコストを削減。

**主要概念:**
- **Dense Passage Retrieval (DPR)** — クエリと文書を同じベクトル空間にマッピングするデュアルエンコーダ
- **Hybrid Search** — キーワード検索（BM25）+ 意味検索（Embeddings）の組み合わせ。単独より優れる
- **HyDE (Hypothetical Document Embeddings)** — クエリに対してLLMが仮想的な文書を生成し、その埋め込みで検索

**ベクトルインデックス:**
- **FAISS** — 数十億ベクトルに対して効率的なメモリ使用
- **HNSW** — 高速な階層的検索のためのグラフ構造
- **ScaNN** — Googleのアプローチ。最高の再現率-レイテンシトレードオフ

**関連Wikiページ:**
- [[concepts/agentic-rag]] — エージェント型RAGの進化系
- [[concepts/modern-retrieval-toolkit]] — 最新の検索ツールキット

---

### 3. Fine-tuning — タスク特化

パフォーマンス向上、制御、モジュール化（小さな専門モデルの使用）のために。

**主要手法:**
- **LoRA (Low-Rank Adaptation)** — 学習可能な低ランク分解行列を注入し、少数のパラメータのみ更新
- **QLoRA** — 4ビット量子化モデルをファインチューニング。65Bモデルを48GB GPU 1台で調整可能
- **Instruction Fine-tuning** — (指示, 出力) ペアでベースモデルを学習し、役立つアシスタントに

**関連Wikiページ:**
- [[concepts/fine-tuning/peft-lora-qlora]] — LoRA/QLoRAの詳細
- [[concepts/fine-tuning/instruction-fine-tuning]] — 指示チューニング
- [[concepts/fine-tuning/axolotl]] — ファインチューニングフレームワーク
- [[concepts/fine-tuning/unsloth]] — 高速ファインチューニング

---

### 4. Caching — レイテンシ・コスト削減

以前計算したLLM応答をキャッシュし、将来の同一・類似リクエストに再利用。

**戦略:**
- **Semantic Caching** — 入力の埋め込みをキャッシュキーにする
- **Safe Caching** — 自然言語ではなくItem IDや制約付き入力（ドロップダウン選択など）を使用。誤った「類似」回答を防ぐ
- **Pre-computation** — 人気クエリの応答をオフラインで事前生成。レイテンシを秒からミリ秒に

---

### 5. Guardrails — 品質保証

LLMの出力を構文、安全性、事実正確性の観点から検証。

**ツールと方法:**
- **Structural Guidance** — 定型表現（Guidance、Outlinesなど）を使ってモデルに特定の文法（JSONなど）を強制
- **統語的/意味的チェック:**
  - *統語的:* SQLコードが実行可能か、値が定義済みリストに含まれるか
  - *意味的:* LLMで要約がソーステキストと矛盾していないか確認（SelfCheckGPT）
- **Input Guardrails** — 敵対的・NSFWプロンプトがモデルに到達する前にブロック

**関連Wikiページ:**
- [[concepts/structured-outputs]] — 構造化出力の手法
- [[concepts/ai-coding-reliability]] — AIコーディングの信頼性

---

### 6. Defensive UX — エラーの優雅な処理

LLMが失敗することを前提とし、インターフェースを優雅に設計。

**核となる原則:**
- **期待値の設定:** 「AIは不正確な情報を生成する可能性があります」という注意書きで信頼を調整
- **効率的な却下:** 提案を無視しやすくする（GitHub Copilotのゴーストテキストなど）
- **帰属性の提供:** 引用や「社会的証明」を含めてユーザーが情報を検証できるように
- **親しみやすいUI:** すべてをチャットボックスに詰め込むのではなく、標準的なUI要素（ボタン、リスト）を使用

---

### 7. User Feedback — データフライホイール

フィードバックはLLMプロダクトの主要な「堀（moat）」であり、将来の評価とファインチューニングを促進。

- **明示的フィードバック:** いいね/よくない、「再生成」ボタン、星評価
- **暗黙的フィードバック:**
  - *Copilot:* ユーザーがTabを押してコードを受け入れたか？
  - *Midjourney:* ユーザーが画像をアップスケール・ダウンロードしたか？
  - *検索:* 結果をクリックしたか、クエリを修正したか？

---

## フレームワークの進化

Yanの7パターンはコミュニティとの共進化により複数バージョンが存在する：

| バージョン | 出典 | パターン | 違い |
|-----------|------|---------|------|
| **v1 (2023.07)** | 本記事 | Evals, RAG, Fine-tuning, Caching, Guardrails, Defensive UX, User Feedback | オリジナル。Caching/Guerdrails/Defensive UX/User Feedbackを含む |
| **v2 (2024)** | O'Reilly共著 | Evals, RAG, Fine-tuning, Prompting, UX, LLM-as-Judge, Cascade | Prompting/LLM-as-Judge/Cascadeが追加。Caching/Guerdrails/User Feedbackはサブトピックに統合 |

**O'Reilly版v2の新パターン:**
- **Prompting** — 効果的な指示設計。タスク固有の出力のための体系的なプロンプト設計
- **LLM-as-Judge** — 注意深いキャリブレーションのもとでモデルを使って他モデルを評価
- **Cascade** — 複雑なタスクを単純なサブタスクに分割し、各タスクに最適なモデルを割り当て

---

## 関連Wikiページ

- [[entities/eugene-yan]] — フレームワークの提唱者
- [[entities/eugene-yan--core-ideas]] — Yanのコアアイデアとフレームワーク一覧
- [[concepts/evals-for-ai-agents]] — AIエージェント評価（要拡充）
- [[concepts/agentic-rag]] — RAGのエージェント型進化
- [[concepts/fine-tuning/peft-lora-qlora]] — PEFT/LoRA/QLoRA
- [[concepts/fine-tuning/instruction-fine-tuning]] — 指示チューニング
- [[concepts/structured-outputs]] — 構造化出力
- [[concepts/ai-coding-reliability]] — AIコーディングの信頼性とガードレール
