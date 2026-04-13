---
title: "Alex L. Zhang"
handle: "@a1zhang"
created: 2026-04-13
updated: 2026-04-13
tags: [person, rlm, ml-systems, gpu-programming, inference-scaling, scaffolds]
aliases: ["alexzhang13", "altzhang"]
status: complete
---

# Alex L. Zhang (@a1zhang)

| | |
|---|---|
| **X** | [@a1zhang](https://x.com/a1zhang) |
| **Sub Alt** | [@lateinteraction](https://x.com/lateinteraction) (Omar Khattabのアカウント) |
| **Blog** | [alexzhang13.github.io](https://alexzhang13.github.io/) |
| **GitHub** | [alexzhang13](https://github.com/alexzhang13) |
| **Role** | PhD Student, MIT CSAIL (advisors: Omar Khattab, Tim Kraska) |
| **Known for** | Recursive Language Models (RLMs), GPU MODE, KernelBench |
| **Bio** | MIT CSAILのPhD学生。Princeton CS学部首席卒。Sakana AI、VantAI、Snap Inc.、Appleでの研究・開発経験。MLシステムと推論時スケーリングを専門とする。 |

## Overview

Alex ZhangはMIT CSAILのPhD学生で、Omar KhattabとTim Kraskaに師事している。Princeton大学でコンピュータサイエンスの首席卒業生として卒業し、Karthik Narasimhan、Ofir Press、Khanh Nguyenらに師事した。

研究の中心テーマは**「言語モデルが十分に活用されていない領域」**。具体的には、推論時スケーリング(inference-time scaling)、GPUカーネル最適化、そして**言語モデルとスキャフォールドの境界線の曖昧化**を探求している。

GPU MODEコミュニティの運営メンバーとして、NVIDIA、AMD、Jane Streetと協力し、GPUプログラミングコンペティションを開催。KernelBench(ICML 2025)ではベストペーパー受賞。

## Core Ideas

### 1. Recursive Language Models (RLMs) — コンテキストを環境として扱う

RLMはAlex Zhangの代表的な研究で、2025年10月のブログ記事と2025年12月のarXiv論文(2512.24601)で発表された。

> "We propose Recursive Language Models (RLMs), a general inference strategy where language models can decompose and recursively interact with input context of unbounded length through REPL environments."

**核心的なアイデア:**
- 言語モデルが自らを再帰的に呼び出すことで、無制限の長さの入力コンテキストを処理する
- コンテキストウィンドウを拡張するのではなく、**コンテキストをREPL環境内の変数として扱う**
- モデルがコードを生成し、コンテキストをpeek/grep/partitionして、短いスニペットに対して再帰的にサブクエリを実行
- `rlm.completion(prompt, model)` が `gpt5.completion(prompt)` のドロップイン代替となる

**Context Rotへのアプローチ:**
> "Anthropic defines context rot as '[when] the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases', but many researchers in the community know this definition doesn't fully hit the mark... it's almost like, as the conversation goes on, the model gets…dumber?"

RLMはcontext rotを根本的に回避する — ルートLM(depth=0)は全文を一度に見ないため、ウィンドウ詰まりが起きない。

**実証結果:**
| ベンチマーク | 結果 |
|---|---|
| **OOLONG (trec_coarse)** | RLM(GPT-5-mini)がGPT-5を132kコンテキストで**>34pts上回る**(~114%改善) |
| **BrowseComp-Plus** | 1000ドキュメントで**完璧なパフォーマンス**を維持 |
| **RLM-Qwen3-8B** | ベースQwen3-8Bを平均**28.3%上回り**、3つの長期コンテキストタスクでGPT-5に迫る |

**RLMとエージェントの違い:**
> "Agents are designed based on human / expert intuition on how to break down a problem to be digestible for an LM. RLMs are designed based on the principle that fundamentally, LMs should decide how to break down a problem to be digestible for an LM."

### 2. Language Models will be Scaffolds (2026年2月)

2026年2月のブログ記事「Language Models will be Scaffolds」で、RLMの思想的延長を表明。

> "I have been somewhat convinced since before I started my PhD that the language models we interact with in the (near) future will be what we call scaffolds today."

**核心的な主張:**
- 「言語モデル」と「スキャフォールド」の境界線が曖昧になっている
- 前半の10年: スケール一辺倒(データ、コンピュート、モデル容量)
- 後半の10年: 既存のニューラル言語モデルは**深刻に過小評価**されている
- Claude Code、Codex、Cursor、Antigravityの違いを「vibes」以外でどう評価するか? — 評価指標の欠如が問題
- 本来の「言語モデル」の定義(Attention is All You Need以前): テキストからテキストへの確率関数
- RLMのタイトルで誤解されるのは「Language Model」の部分ではなく、提案の本質が**タスク非依存のスキャフォールド**であること

> "A powerful class of language models with near-infinite input, output, and reasoning context are scaffolds around neural language models that can call themselves recursively inside of a REPL."

### 3. RL for RLMs — 再帰的推論の学習

RLMの次のマイルストーンとして、**明示的に再帰的推論を学習したRLM**を提唱。

> "We think that RLMs trained explicitly to recursively reason are likely to represent the next milestone in general-purpose inference-time scaling after CoT-style reasoning models and ReAct-style agent models."

- RLMの軌跡(trajectory)は完全に学習可能でRL化可能
- テスト時コンピュートスケーリングの新しい軸を提供
- アーキテクチャ変更なしで超大規模コンテキストに対応

### 4. GPU効率化とMLシステム

MLシステム分野での一貫した貢献:
- **KernelBench**: LLMが効率的なGPUカーネルを書けるか評価するベンチマーク(ICML 2025, Best Paper)
- **KernelBot**: GPUコードのコンペティションプラットフォーム(GPU MODE)
- **Tritonカーネル**: OSS AlphaFold3用(1k+ ⭐)
- **Neo-1**: Sakana AIでの研究
- **Project Popcorn**: GPUプログラミング関連

### 5. 推論時スケーリングの哲学

> "The field is generally resistant to 'out-there' ideas, but the ability to produce novel, state-of-the-art systems without expensive training is at a peak."

- 高コストなトレーニングではなく、**既存モデルをどう活用するか**に重点
- スケールは死んでいないが、**新しい軸の探索**が重要
- 「low-hanging fruit」という表現を嫌う — 「怠惰な漸進的アイデアを追求すべきだという意味になるから」
- 革新的なアイデアが分野の方向性に大きな影響を与える時期

## Key Work

### Research Papers & Projects
| Year | Title | Venue/Status |
|---|---|---|
| 2025 | Recursive Language Models | arXiv:2512.24601 (with Omar Khattab, Tim Kraska) |
| 2025 | KernelBot: Competition Platform for Heterogeneous GPU Code | CODEML @ ICML 2025 (Spotlight) |
| 2025 | VideoGameBench: Can VLMs Complete Popular Video Games? | Under review |
| 2025 | KernelBench: Can LLMs Write Efficient GPU Kernels? | ICML 2025, DL4C (Best Paper) |
| 2025 | Neo-1 | Sakana AI |
| 2025 | KernelLLM-8B | — |
| 2024 | SWE-bench Multimodal | ICLR 2025 |
| 2024 | Triton kernels for OSS AlphaFold3 | 1k+ ⭐ GitHub |
| 2024 | Language-guided World Models | SpLU-RoboNLP @ ACL 2024 (Oral) |
| 2023 | Building Scalable Video Understanding Benchmarks through Sports | DMLR Workshop @ ICLR 2024 |
| 2023 | Transaction Fee Mining and Mechanism Design | arXiv |
| 2019 | Adaptive Tremor Suppression Orthoses | Intel ISEF 2nd Place |

### Open Source
| Repository | Stars | Description |
|---|---|---|
| [alexzhang13/rlm](https://github.com/alexzhang13/rlm) | 3.3k+ | RLM推論エンジン (OpenAI, Anthropic, OpenRouter, Portkey対応) |
| [gpu-mode/kernelbot](https://github.com/gpu-mode/kernelbot) | 90+ | GPU MODEコンペティションプラットフォーム |
| [alexzhang13/rlm-minimal](https://github.com/alexzhang13/rlm-minimal) | — | RLM最小実装 |

## Blog Posts

| Date | Title | Summary |
|---|---|---|
| 2026-02-25 | [Language Models will be Scaffolds](https://alexzhang13.github.io/blog/2026/scaffold/) | LMとスキャフォールドの境界線が曖昧化する未来を提唱。RLMの思想的延長。 |
| 2025-10-15 | [Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/) | RLMの提案と実証。OOLONGとBrowseComp-Plusでの結果、REPL環境の設計原則。 |
| 2024-10-30 | [A Meticulous Guide to Advances in Deep Learning Efficiency](https://alexzhang13.github.io/blog/2024/deep-learning-efficiency/) | DLアルゴリズム、ハードウェア、ライブラリ、コンパイラの効率化の包括的ガイド。 |
| 2023-12 | [The Annotated Kolmogorov-Arnold Network (KAN)](https://alexzhang13.github.io/blog/2023/kan/) | KANの注釈付きガイド。 |
| 2023-12 | [Highlights of NeurIPS 2023 from Reading All 3584 Abstracts](https://alexzhang13.github.io/blog/2023/neurips-2023/) | NeurIPS 2023の全3584アブストラクトを読み込んだ分析。 |

## GPU MODE Community

GPU MODEの運営メンバーとして活動:
- NVIDIAとのNVFP4 Blackwellコンペティション
- AMDとの$100k-$1Mコンペティション(3回)
- Jane Streetとのモデル最適化コンペティション
- KernelBotプラットフォームの開発と運用
- Discordコミュニティ(gpu-mode)のモデレーション

## Related People

| Person | Relationship | Wiki Link |
|---|---|---|
| [[Omar Khattab]](@lateinteraction) | PhD advisor, RLM共著者, DSPy開発者 | — |
| [[Tim Kraska]] | PhD advisor, MIT CSAIL | — |
| [[Karthik Narasimhan]] | Princetonでのメンター | — |
| [[Ofir Press]] | Princetonでのメンター | — |
| [[Mark Saroufim]] | GPU MODE, KernelBot共著者 | — |
| [[Simran Arora]] | KernelBench共著者, Sakana AI | — |
| [[Anne Ouyang]] | KernelBench共著者 | — |
| [[Simon Willison]] | スキャフォールド関連の議論で言及 | [[simon-willison]] |
| [[Andrej Karpathy]] | スケール vs スキャフォールド議論の文脈で関連 | [[andrej-karpathy]] |

## X Activity Themes

| Theme | Content |
|---|---|
| **RLM** | RLMの提案、実証結果、再帰的推論の学習。Omar Khattabとの共同ツイート。 |
| **Scaffold Philosophy** | "Language Models will be Scaffolds" の思想的展開。LMとスキャフォールドの境界。 |
| **GPU MODE** | コンペティションの告知、KernelBotの運用、コミュニティ活動。 |
| **Inference-Time Scaling** | CoT、ReActに続く次のマイルストーンとしてのRLM。 |
| **ML Systems** | GPUカーネル最適化、ベンチマーク、効率化。 |

## Connection to Harness Engineering & Agentic Engineering

RLMは[[Harness Engineering]]の文脈で重要な含意を持つ:
- Harness = スキャフォールドの一種
- RLMは**タスク非依存の汎用スキャフォールド**として、特定のタスクに最適化されたharnessとは対照的
- Harnessが人間の手で設計されるのに対し、RLMは**モデル自身がコンテキストを分解する方法を決定する**
- Agentic Engineeringの観点では、RLMはReActエージェントのパラダイムを超える可能性を示唆

> "RLMs are not agents, nor are they just summarization. The idea of multiple LM calls in a single system is not new — in a broad sense, this is what most agentic scaffolds do."

## Future Bets

Alex Zhangが示唆している今後の方向性:
1. **RLMのトレーニング**: 明示的に再帰的推論を学習したモデル
2. **インフェレンスエンジンの再考**: 非同期実行、KVキャッシュ再利用
3. **スキャフォールドの多様化**: RLM以外の革新的スキャフォールドの探索
4. **評価指標の整備**: スキャフォールド間の比較可能なベンチマーク
5. **コスト/速度の最適化**: 現在のRLM実装はブロッキングでプレフィックスキャッシュなし
