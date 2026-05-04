---
title: "GenAI Handbook (William Brown)"
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags: [curriculum, meta-knowledge, roadmap, llm-education, generative-ai]
aliases: [willccbb-handbook, genai-roadmap]
sources:
  - https://genai-handbook.github.io
  - https://github.com/genai-handbook/genai-handbook.github.io
  - raw/articles/2026-05-04_genai-handbook.md
---

# GenAI Handbook (William Brown)

**William Brown ([@willccbb](https://x.com/willccbb))** が2024年6月に作成したGenAI学習リソースの**知識マップ**。これは個別の技術概念そのものではなく、Generative AI全体を学ぶための**リソースロードマップ**であり、散在する優れた解説リソース（ブログ、動画、論文）を教科書スタイルに整理したもの。

> **これはメタ知識（知識マップ）である。** ハンドブック自体が知識のソースではなく、「どこに何があるか」を案内するナビゲーションツール。各リソースの実際の内容はリンク先を直接参照すること。
>
> **注意：** 本ハンドブックは2024年6月時点のものであり、約2年経過している。特にSection V（Agents, DSPy）やSection VI（vLLM, llama.cpp）は大きく進化しているため、最新情報との突き合わせが必要。

---

## 🛠️ 全体構造

GenAI Handbookは9セクションで構成される：

```text
Section I:   Foundations of Sequential Prediction（前提知識）
    ↓
Section II:  Neural Sequential Prediction（ニューラルネット→Transformer）
    ↓
Section III: Foundations for Modern LM（トークン化、MoE、スケーリング則）
    ↓
Section IV:  Finetuning Methods（LoRA, RLHF, DPO）
    ↓
Section V:   Evaluations & Applications（ベンチマーク、RAG、エージェント）
    ↓
Section VI:  Performance Optimization（量子化、FlashAttention、vLLM）
    ↓
Section VII: Sub-Quadratic Context Scaling（SSM、Mamba、RWKV）
    ↓
Section VIII: Generative Modeling Beyond Text（GANs、拡散モデル）
    ↓
Section IX:  Multimodal Models（VLM、VQ-VAE）
```

**ハンドブックを提供するブロガー・教育者：**
- **Andrej Karpathy** (ゼロからGPT, トークン化, 逆伝播)
- **Lilian Weng** (RL, エージェント, 拡散, プロンプト, GAN)
- **3Blue1Brown** (微積, 線形代数, ニューラルネット可視化)
- **Chip Huyen** (RLHF, LLMエンジニアリング, マルチモーダル)
- **Sebastian Raschka** (LoRA実践, モデル評価)
- **Tim Dettmers** (量子化, LLM.int8())
- **Neel Nanda** (機械的解釈可能性の入門)
- **Jay Alammar** (Transformer, Word2Vecの可視化)
- **StatQuest** (統計/MLの基本動画シリーズ)
- **Maxime Labonne** (LLM Courseコンパニオン)

---

## 🧩 Wikiカバレッジマッピング

### Section I: Foundations of Sequential Prediction

**カバレッジ率:** ~5%（参照している前提知識であり、Wikiのスコープ外）

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| 微積分・線形代数 (3Blue1Brown) | — | Wikiのスコープ外（プログラミング/エンジニアリング前提知識） |
| 教師あり学習 | — | 同上 |
| 時系列分析 / ARIMA | — | 同上 |
| オンライン学習・後悔最小化 | — | 同上 |
| 強化学習 (MDP, Policy) | [[concepts/reinforcement-learning]] | 「古い」RLの基礎（Sutton & Barto）もカバーされているが、LLMアライメントRLとは異なる文脈 |
| マルコフモデル | — | 同上 |

**リソース評価：** このセクションは前提知識の整理が目的。Lilian Wengの [RL Overview](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) は今でも優れた入門記事。Sutton & Bartoの教科書は古典だが、LLMアライメントには直接つながらない。

---

### Section II: Neural Sequential Prediction

**カバレッジ率:** ~20%

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| ニューラルネット基礎 | [[concepts/deep-learning]] | 高レベルカバレッジのみ |
| RNNs | — | 欠落 |
| LSTMs / GRUs | — | 欠落 |
| Embeddings / Word2Vec | [[entities/embeddings]] | エンティティページに埋め込みの概要あり |
| Transformer (Encoder-Decoder) | [[concepts/transformer-architecture]] | カバー済み |
| Decoder-Only Transformers | [[concepts/decoder-only-gpt]] | カバー済み |

**リソース評価：**
- 🟢 **Karpathy「Let's build GPT」** — 2時間でTransformer全体像を掴める最高のリソース。2026年現在も価値不変。
- 🟢 **3Blue1Brown「But what is a GPT?」** — 視覚的に美しい。基礎を固めるのに最適。
- 🟢 **Jay Alammar「The Illustrated Transformer」** — 直感的理解に優れた古典。必読。
- 🟡 **d2l.ai** — コード付き教科書。理論：実践のバランスが良い。ただし最新のLLM技術（RLHF, vLLM）はカバー外。
- ⚪ **Goodfellow「Deep Learning」** — 古典だが2016年発行。Transformer未収録。歴史的価値のみ。

---

### Section III: Foundations for Modern Language Modeling

**カバレッジ率:** ~50%

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| トークン化 (BPE) | [[concepts/claude-47-tokenizer]] | Claude 4.7のトークナイザ変更を中心的に扱う。汎用BPE解説は不足 |
| Positional Encoding (RoPE) | [[concepts/transformer-architecture]] | Transformerアーキテクチャページ内で一部カバー |
| Mixture-of-Experts | [[concepts/mixture-of-experts]] | カバー済み |
| Scaling Laws | [[concepts/scaling-laws]] | カバー済み |
| Pretraining Recipes | [[concepts/llm-training-fundamentals]] | カバー済み |
| 分散学習 / FSDP | [[concepts/pytorch-fsdp]], [[concepts/fsdp-qlora]] | 両方とも充実 |

**リソース評価：**
- 🟢 **Karpathy「Tokenization」動画** — トークン化を深く理解したいなら必見。独特の思考フレームを与えてくれる。
- 🟢 **Eleuther AI「Rotary Embeddings」ブログ** — RoPEの説明として今でもベスト。
- 🟢 **Hugging Face「Mixture of Experts Explained」** — 概念説明として十分。
- 🟢 **Answer.AI「FSDP + QLoRA Deep Dive」** — 実践的なFSDP解説。wikiの[[concepts/fsdp-qlora]]に取り込み済み。
- 🟡 **Meta公式FSDPブログ** — やや古いが基本を理解するには良い。
- 🟡 **Chinchilla Scaling Laws**ブログ群 — 基本概念を知るには良いが、2024年以降のScaling Laws議論（小さなモデルへのシフト）はカバー外。
- ⚪ **「The Novice's LLM Training Guide」** — レンタルサーバー上の非公式ガイド。内容は有用だが出典不明確。

---

### Section IV: Finetuning Methods for LLMs

**カバレッジ率:** ~80%（Wikiで最も充実したセクション）

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| Instruct Fine-Tuning | [[concepts/fine-tuning]], [[concepts/post-training]] | 両方ともカバー済み |
| LoRA | [[concepts/peft-lora-and-qlora]], [[concepts/qlora]], [[entities/lora-fine-tuning]] | 3つもページあり充実 |
| RLHF | [[concepts/rlhf]], [[concepts/ai-safety-alignment-rlhf-scalable-oversight-interpretability]] | カバー済み |
| DPO | [[concepts/rlhf-dpo-orpo-kto-preference-optimization]] | カバー済み（KTO/ORPO含む） |
| Context Scaling (YaRN) | — | 欠落 |
| Distillation | [[concepts/model-distillation]] | カバー済み |
| Model Merging | — | 欠落（SLERP mergingは未カバー） |

**リソース評価：**
- 🟢 **Sebastian Raschka「Practical Tips for Finetuning LLMs Using LoRA」** — 実践的な知見が豊富。ハイパーパラメータの選択基準など貴重。
- 🟢 **Hugging Face「Illustrating RLHF」** — RLHFの定番入門。2026年現在も基本は変わらず。
- 🟢 **Hugging Face「DPO with TRL」** — コード付きで実践的。
- 🟡 **Chip Huyen「RLHF」** — 理論と実践のバランスが良い。
- 🟡 **Maxime Labonne「Merge Large Language Models with mergekit」** — モデルマージの事実上の標準ガイド。wikiに未取り込み。

---

### Section V: LLM Evaluations and Applications

**カバレッジ率:** ~80%

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| Benchmarking / Evals | [[concepts/ai-evals]], [[concepts/ai-evaluation]], [[concepts/open-llm-leaderboard]] | カバー済み |
| Sampling / Structured Outputs | [[concepts/sampling-strategies]], [[concepts/structured-outputs]] | カバー済み |
| Prompting | [[concepts/prompt-engineering]] | カバー済み |
| Vector Databases | [[concepts/vector-search]], [[concepts/rag-systems]] | カバー済み |
| RAG | [[concepts/rag-systems]], [[concepts/retrieval-augmented-generation]], [[concepts/agentic-rag]] | カバー済み |
| Agents / Tool Use | 多数のページ | 最も充実したセクション |
| DSPy | [[concepts/dspy]], [[concepts/dspy-architecture]] | カバー済み |
| Synthetic Data | [[concepts/synthetic-data]] | カバー済み |
| Representation Engineering | — | 欠落 |
| Mechanistic Interpretability | [[concepts/mechanistic-interpretability]] | カバー済み |

**リソース評価：**
- 🟢 **Lilian Weng「LLM Powered Autonomous Agents」** — エージェントの網羅的サーベイ。2026年現在でも最も引用される記事の一つ。ただし実装は2023年時点。
- 🟢 **Chip Huyen「Building LLM Applications for Production」** — 2023年の記事だが、システム設計の原則は色褪せない。
- 🟢 **Neel NandaのMIリソース** — 機械的解釈可能性の入門として最高。特にGlossaryとQuickstart Guideは必読。
- 🟢 **Anthropic「Scaling Monosemanticity」** — Claude 3 Sonnetの特徴抽出。MIの実際の応用例として重要。
- 🟡 **LangChain「Deconstructing RAG」** — 基本は良いが、2026年現在のRAG実践とは乖離あり。
- 🟡 **Pinecone Learning Series** — ベクトルDBの概念説明として秀逸。2026年でも通用する。
- ⚪ **Microsoft「Generative AI for Beginners」** — 入門レベルとしては良いが、このハンドブックのターゲット層（技術者）には浅すぎる。

---

### Section VI: Performance Optimizations for Efficient Inference

**カバレッジ率:** ~85%

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| Quantization | [[concepts/model-quantization]], [[concepts/gguf-quantization]], [[concepts/gguf]] | カバー済み |
| Speculative Decoding | [[concepts/speculative-decoding]] | カバー済み |
| FlashAttention | [[concepts/flashattention-pytorch-educational]] | カバー済み |
| KV Caching | [[concepts/kv-cache]], [[concepts/attention-mechanism-variants]] | カバー済み |
| vLLM / PagedAttention | [[concepts/vllm]], [[concepts/serving-llms-vllm]] | カバー済み |
| CPU Offloading / llama.cpp | [[concepts/llama-cpp]], [[entities/ollama]] | カバー済み |

**リソース評価：**
- 🟢 **Tim Dettmers「LLM.int8()」ブログ** — 量子化の基礎理論として今でもベスト。 emergent featuresの概念は必須知識。
- 🟢 **Tri DaoのFlashAttention講演** — 考案者による解説。tilingとrecomputationの理解に最適。
- 🟢 **NVIDIA「Mastering LLM Techniques: Inference Optimization」** — 俯瞰に最適な短いブログ。
- 🟡 **Jay Mody「Speculative Sampling」** — 理論のウォークスルーとして良い。ただしvLLMなどでの実装状況は追記が必要。
- 🟡 **vLLMオリジナルブログ** — 2023年のものだが、PagedAttentionの基本は変わらず。
- ⚪ **Datacamp「llama.cpp Tutorial」** — 入門レベル。深い理解には不足。

---

### Section VII: Sub-Quadratic Context Scaling

**カバレッジ率:** ~5%

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| Sliding Window Attention | — | 欠落 |
| Ring Attention | — | 欠落 |
| Linear Attention / RWKV | — | 欠落 |
| SSMs / Mamba | — | 欠落。S4→Mambaの歴史が未カバー |
| HyperAttention | — | 欠落 |

**リソース評価：**
- 🟢 **「The Annotated S4」** — SSMの最も優れた解説。コードと理論の橋渡し。
- 🟢 **Maarten Grootendorst「Visual Guide to Mamba」** — 視覚的に理解しやすい。Mamba入門に最適。
- 🟢 **Tri Dao「Mamba-2 State Space Duality」シリーズ** — Mamba-2の全4部作。SSMとLinear Attentionの関係を理論的に示した重要な成果。
- 🟡 **RWKVブログ（Hugging Face, Johan Wind）** — RWKVの概念説明。実用性は限定的だがアーキテクチャの多様性を知るのに有用。

**⚠️ このセクションはWikiの大きなギャップ。特にMamba系SSMは現在も活発に研究されており、概念ページ作成が推奨される。**

---

### Section VIII: Generative Modeling Beyond Sequences

**カバレッジ率:** ~5%

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| VAEs | — | 欠落 |
| GANs | — | 欠落（一部の言及のみ） |
| Conditional GANs / VQGAN-CLIP | — | 欠落 |
| Diffusion Models | [[concepts/ai-image-generation]], [[skills/stable-diffusion-image-generation]] | スキルとして存在。概念ページとしては欠落 |
| Normalizing Flows | — | 欠落 |

**リソース評価：**
- 🟡 **Lilian Weng「What are Diffusion Models?」** — 拡散モデルの理論的入門として今でも良い。ただし2年経過して多くの資料が出ている。
- 🟡 **Hugging Face「The Annotated Diffusion Model」** — コード付き解説。実装ベースで学びたい人向け。
- ⚪ **GANs関連（Paperspace, Analytics Vidhya）** — 2024年時点でもGANsは「やや時代遅れ」とハンドブック自身が認めている。2026年の現在ではさらに古く、DiffusionとVAEに集中すべき。

---

### Section IX: Multimodal Models

**カバレッジ率:** ~15%

| Topic | Wiki Coverage | 備考 |
|-------|-------------|------|
| VQ-VAE | — | 欠落 |
| Vision Transformers | [[concepts/vision-models]] | カバー済み |
| Multimodal 全般 | [[concepts/multimodal]] | カバー済み |

**リソース評価：**
- 🟢 **Chip Huyen「Multimodality and LMMs」** — マルチモーダルLLMの俯瞰に最適。
- 🟢 **Lilian Weng「Generalized Visual Language Models」** — 様々なVLMアプローチを整理。
- 🟡 **Distill「Multimodal Neurons」** — 視覚的に魅力的。概念理解に役立つが学術的な深さは限定的。
- ⚪ **Apple MM1論文** — 2024年の大規模実験。実用的だが2026年ではやや古い。

---

## 📊 総合カバレッジ

| Section | Wiki Coverage | 備考 |
|---------|-------------|------|
| I. Foundations | **~5%** | Wikiのスコープ外（前提知識）。参照リソースは有用。 |
| II. Neural Sequential | **~20%** | RNN/LSTMの概念ページが欠落 |
| III. Modern LM | **~50%** | トークン化の汎用ページが不足。FSDP/MoEは充実。 |
| IV. Finetuning | **~80%** | Wikiで最も充実。Context Scaling (YaRN) と Model Mergingが欠落。 |
| V. Evaluations & Apps | **~80%** | Agents/RAGは充実。Representation Engineeringが欠落。 |
| VI. Inference Optimization | **~85%** | 最も充実したセクション。全てカバー。 |
| VII. Context Scaling | **~5%** | 最大のギャップ。SSM/Mamba/RWKVの概念ページが全くない。 |
| VIII. Beyond Text | **~5%** | Diffusion/VAE/GANsが未カバー。ただしWikiのスコープ外に近い。 |
| IX. Multimodal | **~15%** | VQ-VAEが欠落。VLMはカバー済み。 |

---

## 🏆 おすすめ優先順位

### 🅰️ エンジニア / 実務者 — LLMアプリケーション開発者向け

Section V（Evals & Applications）とSection VI（Inference Optimization）に集中。VII（Context Scaling）はMambaを理解したい場合のみ。

```text
1. Section V: Agents / RAG / DSPy — 実務に直結
2. Section VI: vLLM / Quantization — デプロイに必須
3. Section IV: LoRA / RLHF / DPO — ファインチューニング実践
```

### 🅱️ 研究者 / 深掘りしたい人

Section III（Modern LM）から始め、Section VII（SSM/Mamba）とSection V後半（MI, RepE）へ。

```text
1. Section III: Scaling Laws / MoE — 基盤理論
2. Section VII: Mamba / SSM — 最先端アーキテクチャ
3. Section V: MI / RepE — 解釈可能性
4. Section I: Time-Series / RL — 理論的基礎
```

### 🅲️ 初学者 — 初めてGenAIを学ぶ人

ハンドブックの構造をそのまま追うのが最適。Section IIのTransformerまでは必須。Section III以降は興味に応じて選択。

```text
1. Section I: Math (3Blue1Brown) + RL基礎
2. Section II: Karpathy「Let's build GPT」(最優先)
3. Section III: Tokenization + Scaling Laws
4. Section IV: LoRA（実践から入る）
5. Section V: Prompting → RAG
```

---

## 🗺️ ギャップ分析 — Wikiに追加すべき概念

| 優先度 | 欠落概念 | 該当Section | 理由 |
|--------|---------|------------|------|
| 🔴 | **SSM / Mamba** | VII | アーキテクチャの重要な代替パラダイム。現在も活発な研究分野。 |
| 🔴 | **Representation Engineering** | V | AI安全とモデル制御の新しいパラダイム。実用性が高い。 |
| 🟡 | **Model Merging (mergekit / SLERP)** | IV | オープンソースモデル活用の実践的手法として普及。 |
| 🟡 | **Context Scaling (YaRN / RoPE拡張)** | IV | 長期コンテキスト処理の実装テクニックとして重要。 |
| 🟢 | **RNN / LSTM** | II | 歴史的価値。ただし優先度低（Transformer前提の時代）。 |
| 🟢 | **FlashAttention（詳細概念ページ）** | VI | 現在はスキルとして存在。概念ページ化する価値あり。 |
| 🟢 | **Diffusion Models（概念ページ）** | VIII | 画像生成の基盤。スキルはあるが概念ページがない。 |

---

## 🔗 関連Wikiページ

- [[entities/will-brown]] — ハンドブック作成者
- [[concepts/llm-course-roadmap]] — Maxime Labonne（類似のメタ知識マップ）
- [[concepts/learning-llms-in-2025]] — Yoav Goldberg（類似のメタ知識マップ）
- [[concepts/transformer-architecture]] — Transformerの中核概念
- [[concepts/scaling-laws]] — スケーリング則
- [[concepts/rlhf-dpo-orpo-kto-preference-optimization]] — 選好最適化
- [[concepts/rag-systems]] — 検索拡張生成
- [[concepts/model-quantization]] — 量子化
- [[concepts/mechanistic-interpretability]] — 機械的解釈可能性
- [[entities/andrej-karpathy]] — ハンドブックで最も引用される教育者
- [[entities/lilian-weng]] — 2番目に多く引用されるブロガー
- [[entities/maxime-labonne]] — コンパニオンリソース（LLM Course）の作成者

---

> **このページはメタ知識（知識マップ）であり、William Brown の GenAI Handbook が参照する各リソースを評価し、既存Wiki概念にマッピングしたものである。個別の技術概念の解説は各リンク先を参照すること。**
