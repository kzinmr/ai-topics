---
title: Princeton COS597R — Deep Dive into Large Language Models
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags: [course, curriculum, research, llm-papers, scaling, alignment, reasoning, interpretability]
aliases: [cos597r, princeton-llm, deep-dive-llm]
sources:
  - https://princeton-cos597r.github.io/
  - raw/articles/2026-05-04_princeton-cos597r-syllabus.md
---

# Princeton COS597R: Deep Dive into Large Language Models

> **Danqi Chen & Sanjeev Arora**（Princeton）による**論文ベースのLLM研究サーベイコース**。スケーリング則からデータキュレーション、アライメント、推論、RAG、ハードウェアまで、LLM研究の全スペクトラムをカバー。研究指向で、実装よりも**概念理解と批判的思考**を重視。2024年秋開講。

---

## なぜこのコースが特別か

1. **豪華インストラクター** — Chen（長文脈・知識編集の専門家）+ Arora（理論家）の組み合わせで理論・実践の両面をカバー
2. **論文ベースの深掘り** — 毎回1-2本の重要な論文を精読。Lectureship制度（学生が講義ノートを執筆）で議論を文書化
3. **Debate Panel形式** — Presenter + 2 Critics + 2 Proponentsの構造で、論文を批判的に評価する訓練
4. **2024年秋季のベストスナップショット** — GPT-4登場後、Llama 3公開後、DPO登場後のLLM研究の全体像を提供

---

## カリキュラム詳細とWikiマッピング

### フェーズ1: 事前学習とスケーリング（9月）

| 週 | トピック | キーペーパー | 関連Wiki概念 |
|----|---------|-------------|-------------|
| 1-2 | Pre-training | GPT-3 (*Language Models are Few-Shot Learners*), Llama 3 | `concepts/decoder-only-gpt`, `concepts/transformer-architecture` |
| 3 | Scaling Laws | Chinchilla (*Training Compute-Optimal LLMs*) | —（スケーリング則の概念ページ未作成） |
| 4 | Emergent Abilities | *Are Emergent Abilities a Mirage?* | —（未カバー） |

> **CS336との関係:** 同じスケーリング則を扱うが、COS597Rでは**論文を読んで概念を理解**するのに対し、CS336では**実験で検証**する点が対照的。両方をやると最も効果的。

### フェーズ2: データとポストトレーニング（9月末〜10月）

| 週 | トピック | キーペーパー | 関連Wiki概念 |
|----|---------|-------------|-------------|
| 4 | Data Curation | Dolma (3T tokens), Phi-1.5 (データ品質vs量) | —（データキュレーションの概念ページ未作成） |
| 5 | Instruction Tuning | FLAN, Tulu | `concepts/fine-tuning/instruction-fine-tuning` |
| 6 | Preference Learning | InstructGPT, DPO | `concepts/fine-tuning/rlhf-dpo-preference` |
| 7 | Constitutional AI | *Harmlessness from AI Feedback* | `concepts/ai-safety` |
| 7 | Weak-to-Strong | Weak-to-Strong Generalization | `concepts/ai-safety`（関連） |

> **独自の価値:** **DPOとRLHFの比較**を論文レベルで行えるのがこのコースの強み。InstructGPT（RLHFの原典）とDPO（その簡略化）を同じ週に読み、Debate Panelで議論する。

### フェーズ3: 高度な能力（10月〜11月）

| 週 | トピック | キーペーパー | 関連Wiki概念 |
|----|---------|-------------|-------------|
| 8 | Long Context | RoPE, Long-context training | `concepts/attention-mechanism-variants`, `concepts/kv-cache` |
| 9 | Reasoning | *Let's Verify Step by Step*, Test-Time Compute Scaling | `concepts/grpo-rl-training`（間接的）, `concepts/exec-plans` |
| 10 | Small Models | Sheared LLaMA, Gemma 2 | `concepts/model-quantization`, `concepts/fine-tuning/quantization-overview` |
| 11 | RAG | *Retrieval from trillions of tokens* | `concepts/agentic-rag` |
| 12 | Agents | LLM → Autonomous Agents の進化 | `concepts/agent-harness`, `concepts/agent-orchestration-frameworks` |

> **独自の価値:** **Test-Time Compute Scaling**（OpenAI o1の基盤論文）をカリキュラムに含む。2024年秋時点で、この画期的な論文をコースで取り上げた数少ない例。

### フェーズ4: 特殊トピック（11月）

| 週 | トピック | キーペーパー | 関連Wiki概念 |
|----|---------|-------------|-------------|
| 13 | Hardware | FlashAttention, Mamba | `concepts/flashattention-pytorch-educational`, `concepts/local-llm/gguf`（間接的） |
| 14 | Multimodal | Visual Grounding (Saining Xie) | `concepts/ai-image-generation` |
| 14 | Pruning/Distillation | — | — |

---

## このコースの限界

- **実装ゼロ** — コードを一切書かない。概念理解に集中するため、「手を動かしたい」人には不向き
- **2024年秋時点で固定** — GRPO、推論時計算の拡張（o1以降）、RLM、Agent Harness、Claude Mythos等はカバーされない
- **論文読解力が必要** — 毎週1-2本の論文を読む負荷。前提知識としてCOS484（深層学習）相当が必要
- **アクティブ参加が前提** — Pre-lecture form提出＋Debate Panel＋Lecture Scribing。独学ではScribeノート＋論文リストとしての活用に限定される

---

## 学習優先順位の中での位置づけ

| 側面 | COS597R | 代替コース |
|------|---------|-----------|
| 研究スキル | 🟢 **最高。論文精読＋批判的議論** | CS336: 実装スキルに集中 |
| LLM知識の幅 | 🟢 事前学習→展開まで全範囲 | CMU LLMs: 応用重視、理論は薄い |
| 実装経験 | ⚪ なし | CS336: 全部実装 |
| 参加ハードル | 🔵 論文読解力が必要 | CMU LLMs: 最も入門しやすい |
| アクセスのしやすさ | 🟢 全教材公開、Scribeノート充実 | — |

---

## 関連Wikiページ

- [[concepts/learning-llms-in-2025]] — Yoav Goldbergの全体ガイド
- [[concepts/stanford-cs336-language-modeling-from-scratch]] — 実装版の対抗馬
- [[concepts/decoder-only-gpt]] — コース全体の前提アーキテクチャ
- [[concepts/fine-tuning/rlhf-dpo-preference]] — 選好最適化（第6週）
- [[concepts/grpo-rl-training]] — 推論時計算の後続（第9週の発展）
- [[concepts/flashattention-pytorch-educational]] — FlashAttention（第13週）
- [[concepts/agentic-rag]] — RAG（第11週）
- [[concepts/ai-safety]] — Constitutional AI（第7週）
- [[concepts/kv-cache]] — 長文脈（第8週）
- [[concepts/attention-mechanism-variants]] — RoPE（第8週）

---

> **このページはメタ知識（知識マップ）です。** Princeton COS597Rのカリキュラム構造と論文ロードマップをWiki概念にマッピングしています。実際の講義ノートや論文はprinceton-cos597r.github.ioを参照してください。
