---
title: Stanford CS336 — Language Modeling from Scratch
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags: [course, curriculum, implementation, llm-training, triton, scaling-laws, alignment]
aliases: [cs336, language-modeling-from-scratch, hashimoto-liang-course]
sources:
  - https://stanford-cs336.github.io/spring2025/
  - raw/articles/2026-05-04_stanford-cs336-syllabus.md
---

# Stanford CS336: Language Modeling from Scratch

> **Tatsunori Hashimoto & Percy Liang** による Stanford の実装集中型コース（5 units）。OS系コースに触発され、学生が**ゼロから完全な言語モデルを構築**する。講義ではなく**5つの大規模実装課題**が主役。2025年春開講。

---

## なぜこのコースが特別か

Yoav Goldberg のガイドの中で唯一「技術/MLクラスだが、LLM訓練のニッチな詳細をカバーしている」として特別扱いされたコース。特筆すべき点：

1. **ゼロビルド哲学** — トークナイザ実装からTransformer構築、Tritonカーネル記述、Common Crawl処理、RLアライメントまで。OSコースの「全部自分で作る」アプローチ
2. **最新技術スタック** — TritonによるFlashAttention2、uvパッケージ管理、AGENTS.md/CLAUDE.mdを含むCI/CD。2025年のベストプラクティスが反映
3. **GPU費用ガイド付き** — RunPod $1.99-2.99/h、Lambda Labs $2.49-3.29/hの実践的コスト情報
4. **オープンソース課題** — 全5課題がGitHub公開、1.6k〜56 ⭐

---

## カリキュラム詳細とWikiマッピング

### Assignment 1: Basics（Transformer一からの実装）

| 実装項目 | 学べること | 関連Wiki概念 |
|---------|-----------|-------------|
| BPE Tokenizer | サブワード分割の完全理解 | `concepts/decoder-only-gpt`（トークナイゼーション節） |
| Transformerアーキテクチャ | Attention, Feed-Forward, LayerNorm, Positional Encoding | `concepts/decoder-only-gpt`, `concepts/transformer-architecture`, `concepts/attention-mechanism-variants` |
| Optimizer (AdamW) | 学習率スケジューリング, weight decay | — |
| 訓練ループ | forward/backward, loss計算, perplexity評価 | `concepts/llm-core` |
| データ: TinyStories + OpenWebText | GPT-4生成データと実Webデータの比較 | `concepts/local-llm`（データ関連） |

> **独自の価値:** トークナイザを自分で実装することで、BPEの動作と語彙選択がモデル品質に与える影響を**体感**できる。TinyStories（GPT-4生成の子供向けストーリー）とOpenWebText（実Webスクレイプ）の両方で訓練し、データ分布の影響を比較。

### Assignment 2: Systems（GPU最適化と分散訓練）

| 実装項目 | 学べること | 関連Wiki概念 |
|---------|-----------|-------------|
| GPUプロファイリング | メモリ帯域幅、計算バウンドの診断 | `concepts/ai-infrastructure-engineering/gpu-vram-fundamentals` |
| **Triton FlashAttention2** | カスタムCUDAカーネル記述 | `concepts/flashattention-pytorch-educational` |
| メモリ効率の良いTransformer | アクティベーションチェックポインティング、再計算 | `concepts/context-compression` |
| Distributed Data Parallel (DDP) | マルチGPU訓練の基礎 | `concepts/ai-infrastructure-engineering/distributed-training` |

> **独自の価値:** **Tritonカスタムカーネル**を実際に書ける。FlashAttentionをブラックボックスとして使うのではなく、Tritonで独自実装する経験は、業界でこのスキルセットを持つエンジニアが極めて少ない中で、**最大の差別化要因**。

### Assignment 3: Scaling（スケーリング則の実験検証）

| 実装項目 | 学べること | 関連Wiki概念 |
|---------|-----------|-------------|
| Scaling Law fitting | Chinchilla Optimal Model Sizeの実データ検証 | —（概念ページ未作成） |
| API Training Runner | 分散訓練APIの呼び出しと結果収集 | — |
| 損失予測モデル | IsoFLOP contours, パラメータ予測 | — |

> **独自の価値:** 理論として知っているスケーリング則（Chinchilla, Kaplan et al.）を**実際に自分の訓練実行で検証**できる。Stanfordが提供する訓練API（hyperturing.stanford.edu）を使い、異なるモデルサイズ×データ量の組み合わせで損失を計測。

### Assignment 4: Data（Common Crawl処理）

| 実装項目 | 学べること | 関連Wiki概念 |
|---------|-----------|-------------|
| Common Crawlダウンロード・解析 | WARCフォーマット、大規模データパイプライン | — |
| フィルタリング（品質・重複・PII） | データ品質の自動判定 | `concepts/fine-tuning/quantization-overview`（データ品質関連） |
| 重複除去（MinHash, exact dedup） | 大規模データの重複除去アルゴリズム | — |
| フィルタ済みデータで訓練 | データ品質が最終モデル性能に与える影響の測定 | — |

> **独自の価値:** **「データ」が最も重要な要素**であるにもかかわらず、ほとんどのLLMコースではスキップされるCommon Crawl処理を実践できる。フィルタリング戦略の違いが最終的なモデル性能にどう影響するかを**定量比較**できるのがユニーク。

### Assignment 5: Alignment（SFT + RL + DPO）

| 実装項目 | 学べること | 関連Wiki概念 |
|---------|-----------|-------------|
| SFT (Supervised Fine-Tuning) | 数学推論データセットでの教師ありチューニング | `concepts/fine-tuning/instruction-fine-tuning`, `concepts/fine-tuning/trl` |
| RL for Math Reasoning | GRPOスタイルの強化学習 | `concepts/grpo-rl-training`, `concepts/fine-tuning/rlhf-dpo-preference` |
| DPO (オプション) | Direct Preference Optimization | `concepts/fine-tuning/rlhf-dpo-preference` |
| Safety Alignment (補足) | 命令チューニング、RLHFの安全確保 | `concepts/ai-safety` |

> **独自の価値:** **数学推論にRLを使う**という2025年時点で最先端のトピックを課題として実装できる。GRPO/PPOの違いをコードレベルで理解し、SFTだけでは達成できない推論能力の向上を体験。補足としてSafety AlignmentのPDFも提供。

---

## このコースの限界

- **講義が最小限** — 主に課題がカリキュラムの中心。理論的な背景は自力で補う必要がある
- **GPU費用がかかる** — 全課題を通して$50-200程度のGPU費用を見積もるべき
- **カバレッジの偏り** — RAG、エージェント、評価、マルチモーダルはカバーされない。LLMの「作り方」と「訓練法」に特化
- **2025年春時点** — 2026年時点の最先端（RLM, Mythos, Agent Harness等）は含まれない

---

## 学習優先順位の中での位置づけ

| 側面 | CS336 | 代替コース |
|------|-------|-----------|
| 実装の深さ | 🟢 **最高。全コンポーネントを自作** | Princeton COS597R: 論文ベースで実装なし |
| 理論の深さ | 🔵 実装を通して学ぶ（発見的） | Princeton COS597R: 論文ベースで体系的 |
| 応用範囲 | ⚪ LLM訓練に特化 | CMU LLMs: アプリケーション全般 |
| コスト | 🟡 GPU費用$50-200 | 無料（論文読むだけ） |
| 前提知識 | 🔵 Python習熟必須 | COS597R: DL基礎、CMU: Light |

---

## 関連Wikiページ

- [[concepts/llm-course-roadmap]] — Maxime LabonneのLLM Courseとの類似性（Part 2: The Scientistと重なる）
- [[concepts/learning-llms-in-2025]] — Yoav Goldbergの全体ガイド
- [[concepts/decoder-only-gpt]] — Assignment 1で実装するアーキテクチャ
- [[concepts/flashattention-pytorch-educational]] — Assignment 2で実装するFlashAttention
- [[concepts/grpo-rl-training]] — Assignment 5で実装するRL手法
- [[concepts/fine-tuning/rlhf-dpo-preference]] — Assignment 5で扱う選好最適化
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — Assignment 2の前提知識
- [[concepts/fine-tuning/trl]] — Assignment 5で使用するHuggingFace TRL

---

> **このページはメタ知識（知識マップ）です。** Stanford CS336のカリキュラム構造をWiki概念にマッピングし、各Assignmentの学習内容と既存Wikiページの対応関係を示します。実際の課題内容は各GitHubリポジトリを参照してください。
