---
title: AI Benchmarks & Evals Overview (xeophon Series)
type: concept
created: 2026-05-08
updated: 2026-05-08
status: active
featured: true
tags:
  - benchmark
  - evaluation
  - model
  - ai-metrics
  - comparison
  - coding-benchmarks
  - knowledge-benchmarks
  - reasoning-benchmarks
  - multimodal-benchmarks
  - agent-benchmarks
  - game-based-benchmarks
sources:
  - https://x.com/xeophon/status/1917175899948020203
  - https://x.com/xeophon/status/1925513059281305612
  - https://x.com/xeophon/status/1925870415173300350
  - https://x.com/xeophon/status/1927325298011287757
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
author: Florian Brand (@xeophon)
related_entities:
  - entities/florian-brand.md
related_concepts:
  - concepts/llm-evaluation.md
  - concepts/swe-bench.md
---

# AI Benchmarks & Evals Overview

> Florian Brand (@xeophon) による「Popular Benchmarks / Evals」18部構成シリーズの包括的まとめ。
> 各ベンチマークの設計思想、データソーシング方法、強み・弱点を解説。

---

## シリーズ概要

| Part | Date | Benchmark | Category | Key Insight |
|------|------|-----------|----------|-------------|
| 1 | 2025-04-29 | **GPQA** | Knowledge (Science) | Bio/Physics/Chemistry only. Diamond set > main set. |
| 2 | 2025-04-30 | **LiveCodeBench** | Coding | Rolling problems stay fresh. Easy tasks bore modern LLMs. |
| 3 | 2025-05-01 | **Aider Polyglot** | Coding (Multi-lang) | 6 languages, not just Python. Rarer than expected. |
| 4 | 2025-05-02 | **MMLU Pro** | Knowledge (Multi-domain) | 43% new questions vs MMLU. LLM-assisted filtering. |
| 5 | 2025-05-05 | **MMMU** | Multimodal | Broad topics, college-level. Hand-crafted by students. |
| 6 | 2025-05-06 | **MRCR** | Long-context | Multiple needles. Improvements over NIAH. |
| 7 | 2025-05-07 | **SimpleQA** | Knowledge (Factual) | Sanity check. Important for RL-trained models. |
| 8 | 2025-05-08 | **Vibe-Eval** | Personalized | Custom prompts. Everyone should have their own. |
| 9 | 2025-05-09 | **BFCL V3** | Function Calling | Multi-turn, multi-step. Human-validated. |
| 10 | 2025-05-13 | **IFEval** | Instruction Following | Simple, tests one aspect. Easy to evaluate. |
| 11 | 2025-05-14 | **ChartQA** | Multimodal (Charts) | Noisy test data. Brand recommends retirement. |
| 12 | 2025-05-15 | **Tau-Bench** | Function Calling (Agent) | LLM simulates users. Small but powerful. |
| 13 | 2025-05-19 | **HLE** | Knowledge + Reasoning | Hardest MMLU-style. Strict filtering. |
| 14 | 2025-05-20 | **CountBenchQA** | Counting | Ultra-simple. Tests one thing well. |
| 15 | 2025-05-21 | **ARC-AGI (1)** | Abstract Reasoning | Fluid intelligence. Chollet's classic. |
| 16 | 2025-05-22 | **ARC-AGI 2** | Abstract Reasoning | Human-validated improvement. Non-human perf tanks. |
| 17 | 2025-05-23 | **SWE-Bench Verified** | Software Engineering | 3 annotators/issue. Models stuck at 80-85%. |
| 18 | 2025-05-27 | **Factorio LE** | Game-based Agent | Code+REPL interface. No vision needed. |

---

## ベンチマーク分類

### 知識・サイエンス系 (Knowledge)
- **GPQA** — 大学院レベルのGoogle-proofなQ&A。専門家（PhD保有/取得中）が作成。Diamond setが最も信頼性の高いサブセット。
- **MMLU Pro** — MMLUの改良版。10択に拡張、トリビアルな問題を除外。43%が新規問題。
- **SimpleQA** — ニッチな事実知識のチェック。RL学習後のモデルの知識喪失検出に有用。
- **HLE (Humanity's Last Exam)** — 人類最後の試験。最も難しいMMLU形式のベンチマーク。厳格なフィルタリングと高い参加インセンティブ。

### コーディング系 (Coding)
- **LiveCodeBench** — LeetCode/AtCoder/CodeForcesから定期的に新問題を収集。汚染のないコード生成評価。
- **Aider Polyglot** — Pythonだけでなく6言語対応。多言語コーディング能力をテスト。

### ソフトウェア工学系 (Software Engineering)
- **SWE-Bench Verified** — 実際のGitHub issueを解決するエージェント的ベンチマーク。Ofir Press / OpenAIによる人間検証済みサブセット（500タスク）。1 issueあたり3名のアノテーター。モデルは80-85%で頭打ち。

### マルチモーダル系 (Multimodal)
- **MMMU** — 大学レベルのマルチモーダル理解。6分野30科目183サブフィールド。大学生による手作業のデータ作成。
- **ChartQA** — チャート理解。データは良いがテストセットのノイズが多い。引退推奨。

### 関数呼び出し・指示追従系 (Function Calling / Instruction Following)
- **BFCL V3** — Berkeley Function Calling Leaderboard V3。マルチターン・マルチステップの関数呼び出し。人間検証済み。
- **IFEval** — シンプルな指示追従評価。一つの側面だけをテストし評価が容易。
- **Tau-Bench** — 別のLLMでユーザーをシミュレートする関数呼び出しテスト。

### 長文コンテキスト系 (Long Context)
- **MRCR** — Multi-Round Coreference Resolution。複数のneedleを使用し、NIAHを改善。

### 抽象的推論系 (Abstract Reasoning)
- **ARC-AGI (1)** — François Cholletによるfluid intelligenceテスト。抽象的な視覚パターン推論。今でも最も重要なベンチマークの一つ。
- **ARC-AGI 2** — 多数の人間によるタスク検証で初版を改善。初版と類似タスクだが非人間のパフォーマンスが急落（人間が得意でAIが苦手な抽象推論のギャップを示す）。

### カウンティング系 (Counting)
- **CountBenchQA** — 超シンプルなカウンティング。一つのことを一つのレベルでテスト。

### パーソナライズド系 (Personalized)
- **Vibe-Eval** — 個人の興味に基づくプロンプトセット。誰でも独自に持つべきeval。

### ゲームベース・エージェント系 (Game-based Agent)
- **Factorio Learning Environment (FLE)** — Factorioゲームを模した環境で、モデルがコードを書いてREPL経由で操作。ビジョン不要。楽しいが中毒性あり。

---

## 主要な学び (Key Takeaways)

### 1. ベンチマークは相対的な強みを示す
Brand の一貫したメッセージ：「ベンチマークは額面通りに受け取るべきではなく、モデルの相対的な強みと各分野の全般的な進歩を示すもの」。絶対的なモデル品質を測定するものではない。

### 2. データ品質が全て
- **良い例**: GPQA（専門家が作成・検証）、HLE（厳格なフィルタリング）、SWE-Bench Verified（3名のアノテーター）
- **悪い例**: ChartQA（ノイジーなテストデータ、不整合）

### 3. サチュレーション（飽和）への対応
多くのベンチマークが飽和しつつある：
- LiveCodeBench: easy/medium LeetCode問題はLLMにとって簡単すぎる
- MMLU: 改善の余地が少ないためMMLU Proが開発された
- SWE-Bench Verified: モデルが80-85%で頭打ち — 残り15-20%が本当に難しい
- 定期的な問題更新（LiveCodeBench方式）が一つの解決策

### 4. 新しいeval設計のトレンド
- **マルチターン・マルチステップ**: BFCL V3が示すように、単一ターンの関数呼び出しから複雑な対話へ
- **LLM-as-judge の活用**: Tau-Benchのように別のLLMでユーザーをシミュレート
- **パーソナライゼーション**: Vibe-Evalのような個人化された評価
- **ゲーム環境**: Factorio LEのような没入型環境でのエージェント能力テスト
- **人間ベースラインの重視**: ARC-AGI 2のように多数の人間参加者で難易度を検証

### 5. ベンチマークの「引退」判断
ChartQAのように、データの質が低いベンチマークは積極的に引退させるべき。コミュニティとして健全なベンチマークエコシステムを維持するために重要。

### 6. エージェントベンチマークの台頭
SWE-Bench Verifiedを「最初の（？）エージェント的ベンチマーク」と位置づけ。コードを書くだけでなく、実環境でissueを解決する能力をテストする方向へのシフトを示唆。

---

## 全18パートのリンク

| Part | Tweet URL | Benchmark |
|------|-----------|-----------|
| 1 | [link](https://x.com/xeophon/status/1917175899948020203) | GPQA |
| 2 | (in thread) | LiveCodeBench |
| 3 | (in thread) | Aider Polyglot |
| 4 | (in thread) | MMLU Pro |
| 5 | (in thread) | MMMU |
| 6 | (in thread) | MRCR |
| 7 | (in thread) | SimpleQA |
| 8 | (in thread) | Vibe-Eval |
| 9 | (in thread) | BFCL V3 |
| 10 | (in thread) | IFEval |
| 11 | (in thread) | ChartQA |
| 12 | (in thread) | Tau-Bench |
| 13 | (in thread) | HLE |
| 14 | (in thread) | CountBenchQA |
| 15 | (in thread) | ARC-AGI (1) |
| 16 | [link](https://x.com/xeophon/status/1925513059281305612) | ARC-AGI 2 |
| 17 | [link](https://x.com/xeophon/status/1925870415173300350) | SWE-Bench Verified |
| 18 | [link](https://x.com/xeophon/status/1927325298011287757) | Factorio LE |

---

## Related Pages

- [[entities/florian-brand]] — Florian Brand (@xeophon) の人物ページ
- [[concepts/llm-evaluation]] — LLM評価全般
- [[concepts/swe-bench]] — SWE-bench詳細
- 各ベンチマークの個別コンセプトページ（必要に応じて作成）
