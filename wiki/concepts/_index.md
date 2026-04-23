# Concepts

AI and LLM concept pages organized by topic.

## Overview

## Harness-Engineering

- [[concepts/harness-engineering/agentic-engineering-patterns]] — Simon Willisonが2026年2月23日に開始したガイドプロジェクト。コーディングエージェント（Claude Code、OpenAI Codex、Gemini CLI等）から最高の結果を得るための実践パターンを体系化したもの。
- [[concepts/harness-engineering/agentic-engineering]] — Based on the concept popularized by Simon Willison's [Agentic Engineering guide](https://simonwillison.net/2025/Apr/11/agentic-engineering/).
- [[concepts/harness-engineering/agentic-workflows/agent-first-design]] — コードベースを「人間がナビゲートしやすい」のではなく「AIエージェントが作業しやすい」ように設計する哲学。
- [[concepts/harness-engineering/agentic-workflows/agentic-manual-testing]] — コーディングエージェントによる探索的テスト。自動テストがパスしても見逃される問題（クラッシュ、UI欠落、エッジケース）を発見するために、エージェントの手動テスト能力を活用する。
- [[concepts/harness-engineering/agentic-workflows/anti-patterns]] — Simon Willisonが警告するコーディングエージェント使用時のアンチパターン。特に「レビューされていないコードを他者に押し付ける」行為は深刻な問題。
- [[concepts/harness-engineering/agentic-workflows/cli-first-development]] — ソフトウェア開発をCLI（コマンドラインインターフェース）から始めるアプローチ。エージェント時代の開発ワークフローの核心パターン。
- [[concepts/harness-engineering/agentic-workflows/code-hoarding]] — Simon Willisonが提唱する、開発者が学んだスキルや解決策を意図的に蓄積し、再利用するプラクティス。
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — AIエージェントが生成したコードの動作理解を失うことで蓄積する認知的負債。技術的負債の認知版。[[vibe-coding]]によって加速度的に増加する。
- [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Simon Willisonが提唱する、AIコーディングエージェントと人間開発者の協調による反復的改善サイクル。
- [[concepts/harness-engineering/agentic-workflows/context-window-management]] — コーディングエージェントのコンテキストウィンドウを効果的に管理し、品質とコストを最適化するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/)で詳述。
- [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] — コーディングエージェントにプロジェクトを渡した際の最初の4単語プロンプト。Simon Willisonが提唱する、エージェントをテスト思考に切り替える最小限の指示。
- [[concepts/harness-engineering/agentic-workflows/hoard-things-you-know]] — Simon Willisonが提唱する知識の貯蔵と再利用の概念。エージェント時代において、個人が「どのように行うか知っているか」を記録・蓄積することが強力な武器になる。
- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] — コーディングエージェントの内部仕組みを理解するための概念モデル。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/)で詳述。
- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] — コーディングエージェントに対話的アニメーションやビジュアライゼーションを生成させ、アルゴリズムや概念を直感的に理解するパターン。
- [[concepts/harness-engineering/agentic-workflows/karpathy-rl-agents]] — Andrej Karpathyが提唱する自律的研究ループ（Autonomous Research Loop）のパターン。2026年3月の[AutoResearch](https://github.com/karpathy/autoresearch/)プロジェクトと[No Priors podcast](https://www.youtube.com/watch?v=kwSVtQ7dziU)での発言
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — コーディングエージェントにコードベースの構造化された解説を生成させるパターン。既存コードの理解、忘れかけた自分のコードの復習、Vibe Codingしたコードの仕組み理解に有効。
- [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]] — Simon Willisonが提唱するプロンプトを中心としたソフトウェア開発手法。AIコーディングエージェントに対して、詳細な仕様をプロンプトとして記述し、それを実装させるワークフロー。
- [[concepts/harness-engineering/agentic-workflows/red-green-tdd]] — コーディングエージェントとの開発において、テストファースト開発を適用するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)の中核概念。
- [[concepts/harness-engineering/agentic-workflows/rodney]] — Simon Willisonが開発したChrome DevTools ProtocolベースのCLIブラウザ自動化ツール。コーディングエージェントがWeb UIをテスト・検証するために設計。
- [[concepts/harness-engineering/agentic-workflows/showboat]] — Simon Willisonが開発した、コーディングエージェントに「自分の作業を示させる」ためのドキュメンテーション/成果物生成ツール。
- [[concepts/harness-engineering/agentic-workflows/subagents]] — メインのAIエージェントが独立したサブエージェントを並列に起動し、それぞれが隔離されたコンテキストとターミナルセッションでタスクを実行するパターン。
- [[concepts/harness-engineering/agentic-workflows/throw-away-draft-pattern]] — エージェントに最初に捨て台本（throw-away draft）を書かせ、それを自分のメンタルモデルと比較してから、改めて反復する開発パターン。
- [[concepts/harness-engineering/agentic-workflows/using-git-with-agents]] — コーディングエージェントとGitを統合するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)で詳述。
- [[concepts/harness-engineering/agentic-workflows/vibe-coding]] — Simon Willisonが定義する、「コードに一切注目せずにLLMでコードを書く」開発スタイル。
- [[concepts/harness-engineering/context-engineering]] — コンテキストウィンドウを効果的に活用し、LLMの性能を最大化する体系的アプローチ。Harness Engineeringの横断技術コンポーネントとして位置づけられる。
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — AnthropicがClaude Developer Platformでリリースした、大規模ツール使用を可能にする3つの新機能。
- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — LLMエージェントが自律的にタスクを完了させるための実行ループ構造。モデルがアクションを提案し、プラットフォームが実行し、結果をモデルにフィードバックする循環プロセス。
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — エージェントが外部システムと安全に相互作用するためのセキュリティ制御パターン。OpenAI Responses APIのコンテナ環境で実装されている。
- [[concepts/harness-engineering/system-architecture/agent-skills]] — エージェントが再利用可能なワークフローパターンをSKILL.md bundlesとしてパッケージ化する仕組み。同じマルチステップパターンを毎回再発見・再計画するコストを削減する。
- [[concepts/harness-engineering/system-architecture/ai-memory-systems]] — AIアシスタント・エージェントにおける「メモリ（記憶）」システムの設計哲学の比較。OpenAI、Anthropic、Cognition（Devin）がそれぞれ異なるアプローチを採用しており、これは製品ターゲット（コンシューマー vs 技術者）とアーキテクチャ思想（自動 vs 明示的）の違いを反映している。
- [[concepts/harness-engineering/system-architecture/anthropic-memory-tool-cognition]] — 2025年10月、AnthropicはClaude APIにMemory Toolを正式に導入した。これは6つのファイル操作（view, create, str_replace, insert, delete, rename）をモデルにネイティブに提供するという、非常に「opinionated（意見が明確な）」設計だった。Cognition（Devinの開発元）はこの動きをいち早くキャッチし、An
- [[concepts/harness-engineering/system-architecture/building-effective-agents]] — Anthropicが数十社のチームとの協働から得た、LLMエージェント構築の実践的ガイドライン。
- [[concepts/harness-engineering/system-architecture/claude-code-best-practices]] — Anthropic公式のClaude Code（エージェント型コーディングツール）使用ベストプラクティス。
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — MCP（Model Context Protocol）サーバーをコードAPIとして公開し、エージェントがコードを書いてツールを呼び出すパターン。Cloudflareの「Code Mode」と同じ核心洞察。
- [[concepts/harness-engineering/system-architecture/container-context]] — エージェントに永続的な実行環境を提供するホスト型コンテナ。ファイルシステム、データベース、ネットワークアクセスを統合した「モデルの作業スペース」。
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Discovered during Cognition's integration of Claude Sonnet 4.5 into Devin.
- [[concepts/harness-engineering/system-architecture/context-compaction]] — 長期実行エージェントがコンテキストウィンドウの限界に達した際、重要な情報を保持しつつ不要なデータを圧縮する仕組み。OpenAI Responses APIのネイティブ機能。
- [[concepts/harness-engineering/system-architecture/effective-harnesses-for-long-running-agents]] — AnthropicがClaude Agent SDKで開発した、長時間実行エージェント用の2エージェント・ハーネスパターン。
- [[concepts/harness-engineering/system-architecture/evals-for-ai-agents]] — Anthropicが提唱する、AIエージェントの評価（Evals）の体系化ガイド。
- [[concepts/harness-engineering/system-architecture/harness-design-long-running-apps]] — Anthropicが長時間実行のアプリケーション開発向けに設計したエージェントハーネス（枠組み）のパターン。GAN（生成的敵対ネットワーク）のGenerator-Evaluatorループに着想を得た。
- [[concepts/harness-engineering/system-architecture/infrastructure-noise]] — エージェント型コーディングベンチマークにおいて、インフラ設定のみがスコアに与える影響を定量化した調査。
- [[concepts/harness-engineering/system-architecture/multi-agent-research-system]] — Anthropicが構築した、複数のClaudeエージェントを並列に動作させるリサーチシステム。
- [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]] — Anthropicが実践した、AIエージェント向けのツール設計方法论。「エージェントのためにツールを書き、エージェントを使ってツールを最適化する」アプローチ。

## Fine-Tuning

- [[concepts/fine-tuning/axolotl]] — Axolotl is a YAML-configured fine-tuning framework supporting 100+ models with LoRA/QLoRA, DPO/KTO/ORPO/GRPO, and multimodal capabilities.
- [[concepts/fine-tuning/grpo-rl-training]] — Group Relative Policy Optimization — a reinforcement learning approach for fine-tuning language models that compares multiple completions within a group to learn preferred behaviors without requiring 
- [[concepts/fine-tuning/peft-lora-qlora]] — Full fine-tuning of a 70B model requires hundreds of GBs of GPU memory. PEFT methods reduce this dramatically by:
- [[concepts/fine-tuning/pytorch-fsdp]] — FSDP enables distributed training of large models by sharding model parameters, gradients, and optimizer states across multiple GPUs.
- [[concepts/fine-tuning/quantization-overview]] — Quantization reduces model precision (FP32 → FP16 → INT8 → INT4) to decrease memory requirements and improve inference speed with minimal accuracy loss.
- [[concepts/fine-tuning/rlhf-dpo-preference]] — After Supervised Fine-Tuning (SFT), preference optimization methods align models with human values and desired behaviors. These methods differ in data requirements, complexity, and training stability.
- [[concepts/fine-tuning/trl]] — TRL is HuggingFace's library for fine-tuning language models with reinforcement learning and preference optimization methods.
- [[concepts/fine-tuning/unsloth]] — Unsloth is a fine-tuning optimization library providing 2-5x faster training with 50-80% less memory usage through custom Triton kernels and LoRA/QLoRA optimization.

## Local-Llm

- [[concepts/local-llm/dgx-spark-nim]] — 2台のDGX SparkをQSFPケーブル（ConnectX-7, 200 Gbps）で接続し、分散推論が可能。RoCE（RDMA over Converged Ethernet）経由でMPI + NCCL v2.28.3による並列推論を実行。
- [[concepts/local-llm/gguf]] — GGUF is the quantization format used by llama.cpp for efficient CPU/Apple Silicon inference.
- [[concepts/local-llm/inference-hardware]] — Hardware options for running LLMs locally, from consumer GPUs to edge devices.
- [[concepts/local-llm/model-distillation]] — 1. Model compression: Creating smaller, efficient models suitable for consumer hardware
- [[concepts/local-llm/model-quantization]] — Without quantization, most open-weight models would not fit in consumer GPU VRAM (24 GB on RTX 4090) or even the DGX Spark's 128 GB unified memory.
- [[concepts/local-llm/ollama]] — (content needed)
- [[concepts/local-llm/self-hosting-ai-development]] — The core tension: control and cost predictability vs. convenience and performance.
- [[concepts/local-llm/server-dgx-spark]] — Complete setup guide for running a local LLM server on NVIDIA DGX Spark, with focus on NemoClaw integration for secure AI agent development.

## Openclaw

- [[concepts/openclaw/anthropic-conflict]] — 2026年4月、AnthropicはClaudeのサブスクリプションプラン（Pro/Max）からサードパーティAIエージェントフレームワーク（OpenClawなど）のアクセスをブロックした。この決定は、プラットフォーム管理、開発者アクセス、AIエージェントインフラの経済学をめぐる重大な論争を引き起こした。
- [[concepts/openclaw/architecture-comparison]] — elvis（@elvis_）が2026年4月に行った9時間のHermes Agent vs OpenClawの並列ソースコード研究に基づくアーキテクチャ比較分析。
- [[concepts/openclaw/ecosystem-tools]] — Peter Steinberger（@steipete）が開発したMCP-first開発者ツールエコシステム。OpenClawを中核とし、複数のCLI/MCPサーバーが相互連携する構造。
- [[concepts/openclaw/five-tier-precedence]] — OpenClawのスキルロードシステムが採用する階層的優先度モデル。Hermes Agentのself-authoring（自己作成）アプローチとの対比において、最も重要なアーキテクチャ上の差異の一つ。
- [[concepts/openclaw/philosophy]] — OpenClawの設計哲学の中核は「Primitives over Defaults」（デフォルトではなくプリミティブを提供する）。これはLinuxカーネルやKubernetesの設計思想に近い。

## Ai-Organization

- [[concepts/ai-organization/ai-org-context-as-moat]] — AIが実行レイヤーを代替する時代において、企業の競争優位は「何をどのように判断するか」という独自の文脈(context)に収斂する。McKinseyのAgentic Organizationフレームワーク、ReworkedのDiamond Org Chart議論、そしてAgile Leadership Dayの実践的組織図モデルを統合する。
- [[concepts/ai-organization/ai-org-from-hierarchy-to-intelligence]] — Jack Dorseyが2024年にBlock（旧Square）で実践したHierarchy to Intelligenceモデル。従来のヒエラルキー型意思決定を廃し、「文脈駆動の自律実行 + 透明性ベースの監視」への移行を宣言。AIを単なる生産性向上ツールではなく、「協調メカニズムそのものの再設計」として捉える。
- [[concepts/ai-organization/ai-org-solo-founder-and-super-ic]] — AIツールスタックが成熟するにつれ、「1人 = 従来の10人チーム」というパラダイムが現実化している。Reddit r/ClaudeCodeコミュニティとFourWeekMBAの議論を統合し、ソロ創業者の台頭、スーパーICの登場、そしてその限界と課題を整理する。

## Inference

- [[concepts/inference/llama-cpp]] — llama.cpp is a C/C++ inference engine for running LLMs efficiently on consumer hardware, created by Georgi Gerganov.
- [[concepts/inference/sglang]] — SGLang's signature optimization. Builds a tree-structured KV cache across requests sharing common prefixes:
- [[concepts/inference/vllm]] — vLLM is a high-throughput LLM serving engine with PagedAttention optimization.

## Sandbox

- [[concepts/sandbox/in-process]] — In-process sandboxing isolates LLM-generated code execution within the host process using language-level security boundaries — without requiring Docker, cloud accounts, or external infrastructure. Thi
- [[concepts/sandbox/infrastructure]] — Infrastructure-level sandboxing refers to OS/hypervisor-level isolation technologies used to safely execute AI agent code — particularly LLM-generated or user-supplied code — without compromising the 
- [[concepts/sandbox/js-runtime]] — JavaScript/TypeScript runtimes form a critical layer of the AI agent stack. Unlike Python's single CPython implementation, the JS ecosystem offers three competing runtimes with fundamentally different

## Agent-Loop-Orchestration.Md

- [[concepts/agent-loop-orchestration]] — OpenAI Responses API patterns for orchestrating agent loops. See harness-engineering/system-architecture/agent-loop-orchestration.md for full content.

## Agent-Sandboxing.Md

- [[concepts/agent-sandboxing]] — Agent Sandboxingは、AIエージェントの動的コード実行を安全に隔离する技術譜。gVisor、FirecrackermicroVM、WASM等の隔离技術を整理。標準コンテナは共有カーネルのため不十分。

## Agent-Survival-Benchmark.Md

- [[concepts/agent-survival-benchmark]] — LLMエージェントの生存能力とPvP（プレイヤー対プレイヤー）圧力下での性能を測定するオープンソースベンチマーク。

## Agent-Team-Swarm.Md

- [[concepts/agent-team-swarm]] — Agent team swarm refers to coordination patterns where multiple AI agents work together in distributed, emergent structures rather than rigid hierarchies.

## Agent-Team-Swarm

- [[concepts/agent-team-swarm/managed-devins]] — Cognition's evolved approach to multi-agent coordination, introduced in Devin 2.2.

## Agentic-Alternative-To-Graphrag.Md

- [[concepts/agentic-alternative-to-graphrag]] — A November 2025 paper by Contextual AI (George Halal, Jackie Zhang, Sheshansh Agrawal) proposing that the reference traversal problem in RAG pipelines should be solved via agentic tool-use rather than

## Agentic-Engineering.Md

- [[concepts/agentic-engineering]] — This stub exists for backwards compatibility while content is organized into the harness-engineering/ subdirectory structure.

## Agentic-Manual-Testing.Md

- [[concepts/agentic-manual-testing]] — Manual testing enhanced with AI agent assistance. See harness-engineering/agentic-workflows/agentic-manual-testing.md for full content.

## Agentic-Pbt.Md

- [[concepts/agentic-pbt]] — Anthropic + Hypothesis共同研究（NeurIPS 2025 DL4C Workshop）。Claude Codeエージェントが型注釈、docstring、関数名、コメントからコードの不変条件（properties）を自律的に推論し、HypothesisフレームワークでPBTを生成・実行する。

## Agentic-Rag.Md

- [[concepts/agentic-rag]] — Agentic RAG integrates autonomous AI agents into the RAG pipeline, enabling dynamic retrieval, iterative context refinement, and adaptive workflow orchestration. It addresses limitations of traditiona

## Agentic-Scaffolding.Md

- [[concepts/agentic-scaffolding]] — エージェントを本番環境で安全に動作させるための「足場」パターン。エージェントの力を最大化しつつ、リスクを管理するインフラストラクチャ設計。

## Agentic-Theory.Md

- [[concepts/agentic-theory]] — Sean Goedecke's analysis applying Peter Naur's 1985 "theory building" concept to AI-assisted programming.

## Agentic-Web.Md

- [[concepts/agentic-web]] — (content needed)

## Agentic-Workflow-Patterns.Md

- [[concepts/agentic-workflow-patterns]] — (content needed)

## Ai-Addiction-Burnout.Md

- [[concepts/ai-addiction-burnout]] — AI coding tools trigger a compulsion loop similar to slot machines:

## Ai-Agent-Memory-Middleware.Md

- [[concepts/ai-agent-memory-middleware]] — AIエージェントが状態を永続化し、セッション間でコンテキストを共有し、複数エージェントパイプラインで協調するためのストレージインフラストラクチャの横断分析。

## Ai-Agent-Memory-Two-Camps.Md

- [[concepts/ai-agent-memory-two-camps]] — Classification of AI memory/context tools into two fundamentally different paradigms: Memory Backends vs Context Substrates.

## Ai-Agent-Traps.Md

- [[concepts/ai-agent-traps]] — A systematic framework from Google DeepMind (2026) for understanding how the open web can be weaponized against autonomous AI agents. Defines six categories of adversarial content engineered to exploi

## Ai-Autonomy-Debate.Md

- [[concepts/ai-autonomy-debate]] — The AI Autonomy Debate centers on whether AI agents should operate fully autonomously or maintain human oversight in the loop. What started as a niche technical discussion has become one of the most c

## Ai-Bubble-Economics.Md

- [[concepts/ai-bubble-economics]] — The AI Bubble Economics concept encompasses the growing body of analysis questioning whether the unprecedented capital flowing into artificial intelligence infrastructure is backed by real economic va

## Ai-Coding-Agent-Criticism.Md

- [[concepts/ai-coding-agent-criticism]] — Armin Ronacher (lucumr.pocoo.org) identified a structural asymmetry in how AI coding agents are debated:

## Ai-Coding-Reliability.Md

- [[concepts/ai-coding-reliability]] — The central tension: AI tools can write code faster than any human, but writing code is not the same as shipping reliable software. The industry is discovering this distinction at scale in 2026.

## Ai-Digital-Nato.Md

- [[concepts/ai-digital-nato]] — In April 2026, OpenAI, Anthropic, and Google began sharing threat intelligence through the Frontier Model Forum (founded with Microsoft in 2023) to detect and counter what they term "adversarial disti

## Ai-Evals.Md

- [[concepts/ai-evals]] — Product-specific evaluation systems for measuring whether an AI application works correctly on real tasks with real data. Not foundation model benchmarks like MMLU, HELM, or GPQA.

## Ai-Index-Report-2026.Md

- [[concepts/ai-index-report-2026]] — スタンフォード大学HAI（Human-Centered AI Institute）が発表した年次AI指数レポート。AIの研究開発、技術性能、経済影響、倫理・ガバナンスなど包括的なデータを収録。

## Ai-Memory-Systems.Md

- [[concepts/ai-memory-systems]] — OpenAIのChatGPT Memory、AnthropicのClaude Memory（開発中）、CognitionのDevin Memoryは、それぞれ異なる設計哲学に基づいている。このページは3つのアプローチを比較し、コーディングエージェントにおけるメモリシステムの最適設計を探る。

## Ai-Military.Md

- [[concepts/ai-military]] — Coverage of AI systems (particularly Claude) outperforming US military teams in wargame simulations, and the subsequent Pentagon-Anthropic dispute over military use of AI.

## Ai-Observability.Md

- [[concepts/ai-observability]] — AI observability extends traditional software observability (metrics, logs, traces) to cover the unique challenges of LLM-powered applications: non-deterministic outputs, token usage, agent decision t

## Ai-Privacy-Tools.Md

- [[concepts/ai-privacy-tools]] — In early 2026, the AI security community identified a novel technique dubbed "Slingshot" — a CORS-based attack vector that allows AI agents and browser automation tools to bypass traditional web secur

## Ai-Safety.Md

- [[concepts/ai-safety]] — AI Safety encompasses the technical and philosophical work of ensuring that increasingly capable AI systems behave as intended, remain aligned with human values, and can be understood and controlled b

## Ai-Subprime.Md

- [[concepts/ai-subprime]] — Ed Zitron's analysis drawing parallels between the 2008 subprime mortgage crisis and the current AI industry economics.

## Anthropic-Managed-Agents.Md

- [[concepts/anthropic-managed-agents]] — Anthropic Managed Agentsは、AI Agentのプロトタイプから本番運用までを10倍速く実現するプラットフォーム。インフラ構築（サンドボックス、認証、権限管理、チェックポイント、エラーリカバリー）をClaudeに委譲し、開発者はタスク定義・ツール・ガードレールの設計に集中できる。

## Anthropic-Openclaw-Conflict.Md

- [[concepts/anthropic-openclaw-conflict]] — In April 2026, Anthropic blocked third-party AI agent frameworks (including OpenClaw) from accessing Claude models through flat-rate subscription plans (Pro/Max). This decision triggered a significant

## Attention-Mechanism-Variants.Md

- [[concepts/attention-mechanism-variants]] — Modern transformer architectures use different attention mechanisms to optimize the trade-off between modeling capacity, compute efficiency, and context length. A prerequisite concept for [[context-en

## Back-Of-House-Multi-Agent-Patterns.Md

- [[concepts/back-of-house-multi-agent-patterns]] — 厨房のメタファーを用いたマルチエージェント・ワークフローパターン。Sarah Chieng ([[@MilksandMatcha]]) と [@0xSero] によって2026年4月に提唱。

## Back-Of-House-Patterns.Md

- [[concepts/back-of-house-patterns]] — プロの厨房（Back of House）のメタファーを用いたマルチエージェント・ワークフローパターン。単一エージェントの限界（[[single-agent-ceiling]]）を解決するための実践的フレームワーク。

## Base-Consistency.Md

- [[concepts/base-consistency]] — BASE is an alternative consistency model to ACID, designed for distributed systems that prioritize availability over strict consistency. It stands for:

## Behavioral-Trait-Transmission.Md

- [[concepts/behavioral-trait-transmission]] — Language models that share initialization can transmit behavioural traits through training data that is semantically unrelated to those traits — a phenomenon discovered by Anthropic and academic resea

## Building-Effective-Agents.Md

- [[concepts/building-effective-agents]] — Anthropic's guide to building effective AI agents. See harness-engineering/system-architecture/building-effective-agents.md for full content.

## Caid-Coordination.Md

- [[concepts/caid-coordination]] — A coordination framework from CMU (2026) for running multiple coding agents in parallel on complex software engineering tasks. Uses git operations as the core coordination primitive.

## Capabilities-Based-Security.Md

- [[concepts/capabilities-based-security]] — Security model starting from zero access, explicitly granting capabilities. See sandbox patterns for full content.

## Causal-Backbone-Conjecture.Md

- [[concepts/causal-backbone-conjecture]] — The conjecture proposes that agent-like structures emerge naturally from resource constraints, not from the need to model "a sufficiently rich set of tasks." In environments with finite resources (com

## Chaos-Engineering.Md

- [[concepts/chaos-engineering]] — Chaos Engineering is the discipline of experimenting on a system to build confidence in its ability to withstand turbulent conditions in production. For microservices, this means intentionally injecti

## Chatgpt-Memory-Bitter-Lesson.Md

- [[concepts/chatgpt-memory-bitter-lesson]] — Analysis of ChatGPT's memory system through the lens of Rich Sutton's Bitter Lesson — arguing that the best way to build agent memory is not to build one at all, but to embrace stateless, context-wind

## Chief-Of-Staff-Agent-Patterns.Md

- [[concepts/chief-of-staff-agent-patterns]] — Anthropic cookbook: [The Chief of Staff Agent](https://platform.claude.com/cookbook/claude-agent-sdk-01-the-chief-of-staff-agent)

## Claude-47-Tokenizer.Md

- [[concepts/claude-47-tokenizer]] — 2026年4月16日にClaude Opus 4.7がリリースされ、初めてトークナイザーが変更された。この変更により、同じ入力テキストが40%多いトークンにマッピングされる。

## Claude-Agent-Sdk-Sre-Patterns.Md

- [[concepts/claude-agent-sdk-sre-patterns]] — Anthropic cookbook: [The Site Reliability Agent](https://platform.claude.com/cookbook/claude-agent-sdk-03-the-site-reliability-agent)

## Claude-Code-Best-Practices.Md

- [[concepts/claude-code-best-practices]] — Practical patterns and techniques for effective Claude Code usage, synthesized from experienced users' real-world workflows. These complement the internal patterns found in [[claude-code-source-patter

## Claude-Code-Leak.Md

- [[concepts/claude-code-leak]] — March 2026 incident where Anthropic's Claude Code source code was leaked via npm package.

## Claude-Code-Source-Patterns.Md

- [[concepts/claude-code-source-patterns]] — Analysis of tactical engineering patterns found in Claude Code's leaked source code (March 2026). Reveals how Anthropic builds production-grade coding agents with emphasis on prompt composition, cache

## Claude-Memory-Tool.Md

- [[concepts/claude-memory-tool]] — Analysis of how Cognition (makers of Devin) is adopting Claude's memory approach — and what this reveals about competitive dynamics in the coding agent space.

## Claude-Memory.Md

- [[concepts/claude-memory]] — Analysis of Claude's memory system design — how Anthropic uses filesystem-based memory (`CLAUDE.md`, `.agent/` directories) instead of proprietary databases, treating the filesystem as the single sour

## Claude-Mythos-Glasswing.Md

- [[concepts/claude-mythos-glasswing]] — The model was revealed via a CMS misconfiguration leak on March 26, 2026, when security researchers discovered ~3,000 unpublished Anthropic assets publicly accessible. Anthropic confirmed the leak was

## Claude-Mythos-Preview.Md

- [[concepts/claude-mythos-preview]] — Anthropic did not release Claude Mythos publicly. The preview is restricted to frontier red team research and select partners. This decision was characterized by The Signal Newsletter as a "lockdown" 

## Cli-Over-Mcp-Pattern.Md

- [[concepts/cli-over-mcp-pattern]] — Standard CLIs like `gh`, `vercel`, `psql` have:

## Closing-Agent-Loop.Md

- [[concepts/closing-agent-loop]] — Cognition's philosophy for autonomous development: Devin doesn't just write code — it handles the entire development loop.

## Coala.Md

- [[concepts/coala]] — CoALA (Cognitive Architectures for Language Agents) is a unified conceptual framework that maps modern LLM-based agents to the 50-year lineage of cognitive science and symbolic AI. It addresses the pr

## Code-Mode.Md

- [[concepts/code-mode]] — CodeMode is the paradigm where LLMs write code (typically Python) for batch execution rather than making sequential tool calls. Coined by Cloudflare and independently developed by Anthropic, Pydantic,

## Cognition-Ai-Data-Analyst.Md

- [[concepts/cognition-ai-data-analyst]] — Cognitionチームが提唱する、AIソフトウェアエンジニア（Devin）を24/7オンデマンドデータサイエンティストとして活用するアプローチ。SQL専用ツールではなく、コードベースの文脈理解+データ分析+可視化を統合したエージェント設計。

## Cognition-Devin-Philosophy.Md

- [[concepts/cognition-devin-philosophy]] — Cognition Labs（CEO: Scott Wu @ScottWu46）の Devin チームが発信する、AI coding agent に関する一貫した哲学。

## Cognitive-Cost-Of-Agents.Md

- [[concepts/cognitive-cost-of-agents]] — In April 2026, [[Simon Willison]] published a deeply personal reflection after using Claude Code intensively for a full month. The post, "The cognitive impact of coding agents," challenged the prevail

## Cognitive-Debt.Md

- [[concepts/cognitive-debt]] — The accumulated mental overhead of understanding and maintaining complex AI-generated code. See harness-engineering/agentic-workflows/cognitive-debt.md for full content.

## Cognitive-Load-Software-Development.Md

- [[concepts/cognitive-load-software-development]] — Artem Zakirullinの "Cognitive load is what matters" — GitHubで12,000+スターを獲得したソフトウェア設計における認知負荷の体系的フレームワーク。

## Compute-Scaling-Bottlenecks.Md

- [[concepts/compute-scaling-bottlenecks]] — The concept was most thoroughly articulated by Dylan Patel of SemiAnalysis, particularly in his March 2026 Dwarkesh Podcast appearance, where he traced the entire AI compute stack from silicon atoms t

## Context-Compression.Md

- [[concepts/context-compression]] — Methods for reducing the size of context windows while preserving task-relevant information. Critical prerequisite for [[context-engineering]] — addresses the fundamental constraint that LLMs have fin

## Context-Engineering.Md

- [[concepts/context-engineering]] — This stub exists for backwards compatibility while content is organized into the harness-engineering/ subdirectory structure.

## Context-Fragments.Md

- [[concepts/context-fragments]] — Vivek Trivedy (@vtrivedy10) が2026年4月に提唱した概念。コンテキストウィンドウを「harnessが選択的にロードするオブジェクトの集合」として捉えるフレームワーク。

## Context-Graph.Md

- [[concepts/context-graph]] — Living record of decision traces stitched across entities and time — the foundational architecture for AI agent decision-making in enterprise workflows

## Context-Routing.Md

- [[concepts/context-routing]] — 多ドメインエージェントは、すべてのクエリに対してすべてのドメインの知識、ツールセット、指示を読み込む。これはコンテキストの浪費であり、注意力の分散を招く。

## Context-Window-Management.Md

- [[concepts/context-window-management]] — The core challenge: LLMs have a fixed context window, but software projects have unbounded complexity. Effective management is the difference between a productive AI session and a confused, expensive 

## Critique-Shadowing.Md

- [[concepts/critique-shadowing]] — A 7-step iterative methodology for building aligned LLM-as-Judge evaluators, coined by Hamel Husain. The core insight: the process of building an LLM judge forces domain experts to carefully examine d

## Cybersecurity-Proof-Of-Work.Md

- [[concepts/cybersecurity-proof-of-work]] — A concept coined by Drew Breunig in April 2026, observing that as LLMs like Claude Mythos become increasingly effective at finding security vulnerabilities, cybersecurity transforms into an economic e

## Dark-Factory-Software-Factory.Md

- [[concepts/dark-factory-software-factory]] — 「Dark Factory（暗黒工場）」とは、人間がコードを一切書かず、レビューもしないソフトウェア開発の最高自動化レベル。Fanucの無人工場（ロボットが稼働する工場は照明が不要＝暗い）に由来する比喻。

## Death-Of-Browser.Md

- [[concepts/death-of-browser]] — 1. 認知負荷の限界: 人間は多数のタブ、ポップアップ、SEOスパムに疲弊

## Decoder-Only-Gpt.Md

- [[concepts/decoder-only-gpt]] — The decoder-only GPT (Generative Pre-trained Transformer) is the dominant architecture behind modern large language models (ChatGPT, Claude, Gemini, etc.). Andrej Karpathy's microgpt project (February

## Deep-Agents.Md

- [[concepts/deep-agents]] — Deep agents are autonomous AI agents that combine multiple architectural patterns to handle complex, multi-step tasks with minimal human intervention. They feature:

## Direct-Prompting-Philosophy.Md

- [[concepts/direct-prompting-philosophy]] — The core thesis: "Don't waste your time on stuff like RAG, subagents, Agents 2.0 or other things that are mostly just charade. Just talk to it. Play with it. Develop intuition." — Peter Steinberger

## Dspy-Rlm.Md

- [[concepts/dspy-rlm]] — Recursive Language Model — 大規模コンテキストをsandobx Python REPLでプログラム的に探索するDSPyモジュール

## Dspy.Md

- [[concepts/dspy]] — DSPyはOmar Khattab率いるStanford NLPが開発した、LLMを「プロンプト」ではなく「最適化可能なモジュール」として宣言的にプログラミングするフレームワーク。Signature/Module/Teleprompterの抽象化により、手動プロンプトエンジニアリングをコンパイル時の自動最適化に変換する。

## Ecs-Fargate-Scaling.Md

- [[concepts/ecs-fargate-scaling]] — AWS ECS FargateをLambdaのようにスケーリングさせる実験的検証。SQSワークロードでのバーストハンドリング性能を最適化する。

## Elixir-Beam-Agent-Orchestration.Md

- [[concepts/elixir-beam-agent-orchestration]] — Elixir/BEAM（Erlang仮想マシン）をAIエージェントオーケストレーションに活用するパターン。[[openai-symphony]] のRyan Lopopoloが採用したアプローチ。

## Evaluation-Flywheel.Md

- [[concepts/evaluation-flywheel]] — OpenAIのcookbookで示される、評価と改善を循環させる開発パターン。

## Event-Driven-Architecture.Md

- [[concepts/event-driven-architecture]] — Event-Driven Architecture (EDA) is a software design pattern where services communicate asynchronously through events rather than synchronous API calls. Services publish events to a central event bus 

## Exec-Plans.Md

- [[concepts/exec-plans]] — エージェントにタスクを実行させる際、事前に計画（プラン）を立ててから実行するパターン。計画と実行を分離することで、透明性・再現性・デバッグ性を向上させる。

## Experiential-Memory.Md

- [[concepts/experiential-memory]] — Vivek Trivedy (@vtrivedy10) が2026年4月に提唱した概念。エージェントが相互作用を通じて蓄積する「経験的記憶」を、エージェント間で共有・フォーク・再利用するフレームワーク。

## Flashattention-Pytorch-Educational.Md

- [[concepts/flashattention-pytorch-educational]] — [shreyansh26/FlashAttention-PyTorch](https://github.com/shreyansh26/FlashAttention-PyTorch) は、FlashAttentionアルゴリズム（FA1からFA4まで）をPyTorchで教育的・アルゴリズム的明晰さのために実装したプロジェクト。

## Formal-Verification-Llm-Agents.Md

- [[concepts/formal-verification-llm-agents]] — Formal verification is the practice of mathematically proving that code always satisfies its specifications—including all edge cases. AI is poised to bring this from a fringe academic pursuit into the

## Functional-Emotions-Llms.Md

- [[concepts/functional-emotions-llms]] — The discovery that Large Language Models develop internal representations of emotion concepts that causally influence model behavior, including alignment-relevant outcomes. Based on Anthropic's 2026 i

## Gemini.Md

- [[concepts/gemini]] — Announced by Sundar Pichai, Demis Hassabis, and Koray Kavukcuoglu, Gemini 3 represents the most significant iteration to date.

## Gepa.Md

- [[concepts/gepa]] — GEPAはDSPyに統合された遺伝的アルゴリズムベースのプロンプト最適化手法。Pareto最適化により品質とコストを同時に最適化し、GRPOより35倍少ないサンプルで6%高い性能を達成。ICLR 2026 Oral。

## Github-Copilot-Billing.Md

- [[concepts/github-copilot-billing]] — In April 2026, Microsoft announced a major shift in GitHub Copilot's pricing model from requests-based billing to token-based billing, alongside tightening rate limits across all tiers. This change re

## Gnu-Ai-Reimplementations.Md

- [[concepts/gnu-ai-reimplementations]] — During the 1980s and 1990s, the GNU project systematically reimplemented the UNIX userspace from scratch. Stallman directed developers to:

## Gold-Diff-Distillation.Md

- [[concepts/gold-diff-distillation]] — コーディング製品企業が開発した新しいRLトレーニング手法。ユーザーの最終的な「望ましい状態」をRLターゲットとして利用する。

## Gpt-Models.Md

- [[concepts/gpt-models]] — The GPT (Generative Pre-trained Transformer) series, developed by OpenAI, represents the evolution of decoder-only transformer language models from 117M parameters (2018) to frontier-scale reasoning s

## Halo-Loss-Attention-Sinks.Md

- [[concepts/halo-loss-attention-sinks]] — Transformerモデルにおける「Attention Sinks」（注意の沈み込み）現象と、これに対処するHALO損失関数の理論と歴史。

## Harness-Design-Long-Running-Apps.Md

- [[concepts/harness-design-long-running-apps]] — Anthropic Labs（Prithvi Rajasekaran）による長期自律エージェントの実践設計。GAN-inspiredループ（Generator ↔ Evaluator）をフルスタック開発にスケールさせたアーキテクチャ。

## Harness-Engineering.Md

- [[concepts/harness-engineering]] — Agent = Model + Harness. Environment design philosophy for agent-driven development. See harness-engineering/_index.md for full content.

## Headless-Ai-Services.Md

- [[concepts/headless-ai-services]] — Matt Webbが提唱した概念で、personal AIが直接API経由でSaaSサービスを操作し、GUIベースの操作（bot-controlled mouse）を排除するアプローチ。

## Helium-Crisis-2026.Md

- [[concepts/helium-crisis-2026]] — Semiconductor supply chain disruption caused by helium shortage, impacting chip manufacturing globally.

## Illusion-Of-Thinking.Md

- [[concepts/illusion-of-thinking]] — A series of research papers in 2025-2026 demonstrated that pure LLMs fail at logical planning tasks they appear to solve, and that neurosymbolic hybrids dramatically outperform Vision-Language-Action 

## Inference-Speed-Development.Md

- [[concepts/inference-speed-development]] — The core insight: when the bottleneck shifts from human typing/thinking time to AI inference time, development velocity becomes a function of how quickly you can prompt, review, and iterate.

## Inference.Md

- [[concepts/inference]] — LLM推論最適化のための概念ページ。

## Intent-Formalization.Md

- [[concepts/intent-formalization]] — 1. Scale without scrutiny — AI generates code faster than humans can review

## Interactive-Explanations.Md

- [[concepts/interactive-explanations]] — Interactive explanations provide step-by-step, participatory learning experiences where users engage with content through active exploration rather than passive reading.

## Karpathy-Loop.Md

- [[concepts/karpathy-loop]] — Named after Andrej Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) project (released March 6, 2026), which accumulated ~71,000 GitHub stars in weeks and became one of the fastest-g

## Karpathy.Md

- [[concepts/karpathy]] — Andrej Karpathy is a prominent AI researcher, educator, and entrepreneur known for his contributions to deep learning, computer vision, and AI education.

## Kimi-K2-6.Md

- [[concepts/kimi-k2-6]] — K2.6 refreshes the lead that K2.5 established in January 2026, maintaining Moonshot's position as the leading Chinese open model lab throughout 2026 to date.

## Knowledge-Graph-Memory-Agents.Md

- [[concepts/knowledge-graph-memory-agents]] — Knowledge graph memory stores facts as a structured graph of entities and typed relationships, enabling multi-hop reasoning and entity-centric queries that flat vector stores cannot express. It is the

## Lambda-Monolith-Lambdalith.Md

- [[concepts/lambda-monolith-lambdalith]] — A serverless architecture pattern where a single AWS Lambda function handles all API routes, rather than splitting into many small, route-specific Lambda functions.

## Linear-Walkthroughs.Md

- [[concepts/linear-walkthroughs]] — Linear walkthroughs are structured, step-by-step guides that walk users through processes in a sequential, predictable manner. In agentic contexts, they inform how agents should structure task complet

## Llm-As-Judge.Md

- [[concepts/llm-as-judge]] — LLM-as-JudgeはLLMを使用してLLM出力を評価するパラダイム。3つのバイアス类型（ルーブリック順序、スコアID、参照解答）と7つのベストプラクティスを整理。高リスク評価にはGPT-4oクラスが必要。

## Llm-Evaluation-Harness.Md

- [[concepts/llm-evaluation-harness]] — Frameworks and tools for systematically evaluating Large Language Models across standardized benchmarks and custom test suites.

## Llm-Training-Coherence-Evolution.Md

- [[concepts/llm-training-coherence-evolution]] — LLMのトレーニング過程で、モデルがどのように「意味のあるテキスト生成」を獲得するかを追跡した実験。Karpathyの2015年RNN実験を現代のGPT-2アーキテクチャで再現し、57チェックポイントにわたるコヒーレンスの進化を可視化した。

## Local-First-Software.Md

- [[concepts/local-first-software]] — ユーザーのデバイスをデータの第一権威コピー（primary authoritative copy）とし、サーバーは同期・バックアップ・発見支援に限定するソフトウェア設計思想。

## Local-Llm.Md

- [[concepts/local-llm]] — >

## Logfire.Md

- [[concepts/logfire]] — Logfire is an AI-native observability platform built by the Pydantic team. It provides OpenTelemetry-native monitoring for both traditional applications and AI/LLM systems, with a developer-first appr

## Long-Context-Coding-Agents.Md

- [[concepts/long-context-coding-agents]] — A 2026 approach that externalizes long-context processing from latent attention into explicit, executable interactions. Coding agents organize text in file systems and manipulate it using native tools

## Main-Branch-Development.Md

- [[concepts/main-branch-development]] — AI agents excel at atomic, focused work. When given a clear task scope, they produce self-contained changes that can be committed immediately. The traditional branching rationale (isolating incomplete

## Managed-Agents-Sre-Incident-Response.Md

- [[concepts/managed-agents-sre-incident-response]] — Anthropic cookbook: [Build an SRE Incident Response Agent with Claude Managed Agents](https://platform.claude.com/cookbook/managed-agents-sre-incident-responder)

## Memory-Systems-Design-Patterns.Md

- [[concepts/memory-systems-design-patterns]] — AIエージェントのメモリシステム設計における3つのアプローチと、業界が収束しつつあるパターンを整理。

## Meta-Harness.Md

- [[concepts/meta-harness]] — An outer-loop system from Stanford and MIT (2026) that automatically searches over harness code for LLM applications. Discovers optimal context management, retrieval, and presentation strategies.

## Meta-Muse-Spark.Md

- [[concepts/meta-muse-spark]] — Muse Spark represents a major strategic pivot for Meta. The company built its AI reputation on open-source Llama models. Muse Spark is closed-source, with no open weights, no local deployment, and no 

## Microservices-Vs-Monolith.Md

- [[concepts/microservices-vs-monolith]] — Rehan van der Merwe's architecture decision tree provides a pragmatic approach:

## Mismanaged-Geniuses-Hypothesis.Md

- [[concepts/mismanaged-geniuses-hypothesis]] — The hypothesis posits that frontier language models are severely underutilized due to sub-optimal use of scaffolding, not due to inherent limitations in model capability.

## Model-Context-Protocol-Mcp.Md

- [[concepts/model-context-protocol-mcp]] — MCP uses a client-server model:

## Monty-Sandbox.Md

- [[concepts/monty-sandbox]] — Monty is a sandboxing project built on Pydantic, designed to provide safe, structured execution environments for AI agents. It extends Pydantic's validation and serialization capabilities to create co

## Multi-Agent-Autonomy-Scale.Md

- [[concepts/multi-agent-autonomy-scale]] — Research testing how much autonomy multi-agent LLM systems can sustain at unprecedented scale: 25,000 tasks, 8 models, up to 256 agents, 8 coordination protocols.

## Multi-Agent-Consensus-Patterns.Md

- [[concepts/multi-agent-consensus-patterns]] — 分散型AIエージェントシステムにおける合意形成パターン。単一障害点を排除し、スケーラビリティと耐障害性を確保するための調整プロトコル。

## Neural-Garbage-Collection.Md

- [[concepts/neural-garbage-collection]] — Traditional KV-cache management uses heuristic eviction strategies (e.g., sliding window, attention sinks preservation, token importance scoring). Neural Garbage Collection replaces these handcrafted 

## Neurosymbolic-Ai.Md

- [[concepts/neurosymbolic-ai]] — Neurosymbolic AI is an architecture that combines neural networks (pattern recognition, learning from examples) with symbolic reasoning (rule-based logic, abstraction, causal chains). The thesis is th

## Newsjacking-Framework.Md

- [[concepts/newsjacking-framework]] — Newsjacking is the practice of identifying already-trending topics, conversations, or content waves, and strategically inserting yourself into them with a unique angle. Rather than building attention 

## Offline-Evaluation.Md

- [[concepts/offline-evaluation]] — Offline Evaluationは、本番環境にデプロイする前にLLMアプリケーションを体系的に評価するパイプライン。オフラインテスト、人間判定、プロダクションテレメトリの3層で構成。

## Open-Claw-Ecosystem.Md

- [[concepts/open-claw-ecosystem]] — The Open Claw ecosystem refers to the collection of tools, protocols, and implementations related to Anthropic's Claude agent tooling and open source alternatives.

## Open-Model-Consortium.Md

- [[concepts/open-model-consortium]] — The Open Model Consortium is a proposed organizational structure for funding and developing frontier-level open-weight AI models through shared investment from multiple companies, rather than relying 

## Open-Source-Ai-Destruction.Md

- [[concepts/open-source-ai-destruction]] — The term was popularized by Jeff Geerling (Raspberry Pi/Ansible maintainer, YouTuber) in his March 2026 blog post and video "AI is destroying Open Source, and it's not even good yet."

## Openai-Agents-Sdk.Md

- [[concepts/openai-agents-sdk]] — The OpenAI Agents SDK is a standardized, model-native framework for building production-ready AI agents. Version 0.14.0 introduced native sandbox execution, enabling agents to safely inspect files, ru

## Openai-Symphony.Md

- [[concepts/openai-symphony]] — OpenAI Symphonyは、プロジェクトの作業を独立した自律的な実行ランに変換し、チームがコーディングAgentを「監視」するのではなく「作業を管理」できるようにするサービス。

## Personal-Superintelligence.Md

- [[concepts/personal-superintelligence]] — 2025年後半から2026年にかけて、AI業界で最も重要な哲学的分岐が表面化している。それは「superintelligenceの行き先」をめぐる対立である。

## Project-Glasswing.Md

- [[concepts/project-glasswing]] — Anthropic's initiative to use [[claude-mythos]] for defensive security research — finding and patching vulnerabilities in critical software.

## Prompt-Caching.Md

- [[concepts/prompt-caching]] — LLM API呼び出しにおけるキャッシングの設計パターン。コスト削減とレイテンシ改善のために、どの部分をキャッシュし、いつ無効化するかを体系的に扱う。

## Pydantic-Ai.Md

- [[concepts/pydantic-ai]] — Pydantic AI is an open-source Python agent framework built by the Pydantic team. It brings the "FastAPI feeling" to GenAI development: validated outputs, dependency injection, structured tool contract

## Pydantic-Serializability.Md

- [[concepts/pydantic-serializability]] — Pydantic's serializability system provides structured output for AI models. Key innovations include:

## Pydantic.Md

- [[concepts/pydantic]] — Pydantic is a Python data validation library that uses type hints to validate, serialize, and document data. It has become the de facto standard for data validation in the Python ecosystem, with 27.3K

## Ram-Relative-Adoption-Metric.Md

- [[concepts/ram-relative-adoption-metric]] — The Relative Adoption Metric (RAM) is a time-varying, size-normalized metric developed by Nathan Lambert and Florian to evaluate whether a new language model is on track to be ecosystem-defining. It w

## Reasoning-Model-Cost-Transparency.Md

- [[concepts/reasoning-model-cost-transparency]] — A 2026 study revealing that listed API prices for reasoning language models are systematically misleading, with actual costs differing dramatically from advertised rates.

## Reasoning-Models.Md

- [[concepts/reasoning-models]] — LLM architectures designed for explicit step-by-step reasoning, including chain-of-thought, process supervision, and test-time compute scaling.

## Red-Green-Tdd.Md

- [[concepts/red-green-tdd]] — Red Green TDD (Test-Driven Development) is the practice of writing tests before code, following a cycle of: Red (write failing test), Green (write minimal code to pass), Refactor (improve code while k

## Reinforcement-Learning.Md

- [[concepts/reinforcement-learning]] — Reinforcement Learning (RL) is a paradigm of machine learning where agents learn to make decisions by taking actions in an environment to maximize cumulative reward signals. RL is foundational to trai

## Research-Agent-Fundamentals.Md

- [[concepts/research-agent-fundamentals]] — Anthropic cookbook: [The One-Liner Research Agent](https://platform.claude.com/cookbook/claude-agent-sdk-00-the-one-liner-research-agent)

## Resilient-Prompt-Engineering.Md

- [[concepts/resilient-prompt-engineering]] — OpenAIのcookbookで示される、単なるプロンプトテクニックではなく、堅牢なプロンプト設計の方法論。特定モデルに依存しない汎用的なパターン。

## Rlhf.Md

- [[concepts/rlhf]] — RLHF is a technique for training AI models to align with human preferences by using human feedback to shape reward signals. It combines reinforcement learning with supervised fine-tuning on human pref

## Rlm-Recursive-Language-Models.Md

- [[concepts/rlm-recursive-language-models]] — Recursive Language Models (RLMs) are a task-agnostic inference paradigm proposed by Alex Zhang, Tim Kraska, and Omar Khattab (MIT CSAIL/OASYS Lab) that allows language models to handle near-infinite l

## Rlms.Md

- [[concepts/rlms]] — RLMs（再帰的言語モデル）は、LLMが自身のコンテキストを再帰的に読み書きすることで推論時に自己最適化を行うパラダイム。DSPyとは異なり訓練データ不要で、10M+トークンコンテキスト處理が可能。

## Sandbox.Md

- [[concepts/sandbox]] — Sandbox environments provide isolated execution contexts for AI agents to run code, interact with tools, and perform tasks without risking harm to production systems.

## Scaling-Without-Slop.Md

- [[concepts/scaling-without-slop]] — Approach to scaling AI models while maintaining quality, avoiding the "slop" problem of low-quality outputs.

## Self-Evolving-Agents.Md

- [[concepts/self-evolving-agents]] — エージェントが自身の振る舞いや能力を時間とともに改善していくパターン。固定されたロジックではなく、フィードバックと学習による継続的な進化を可能にする。

## Serializability.Md

- [[concepts/serializability]] — Serializability in AI systems refers to the ability to reliably convert LLM outputs into structured, typed data formats (JSON, Pydantic models, etc.) that can be consumed by downstream systems.

## Session-Hierarchy-Management.Md

- [[concepts/session-hierarchy-management]] — The core insight: context bloat is inevitable at every scale, but each scale requires a different intervention.

## Showboat.Md

- [[concepts/showboat]] — A documentation tool concept for AI agents. See harness-engineering/agentic-workflows/showboat.md for full content.

## Single-Agent-Ceiling.Md

- [[concepts/single-agent-ceiling]] — AIコーディングエージェントを使用する全ての開発者が直面する限界。プロジェクトが単純なタスク（HTMLの蛇ゲームなど）から実用的な規模に成長した瞬間に顕在化する。

## Skill-Architecture-Patterns.Md

- [[concepts/skill-architecture-patterns]] — 1. Prompt Nudge: System prompt instructs agent to consider saving a skill every N tool calls

## Space-Gpus.Md

- [[concepts/space-gpus]] — The idea has moved from science fiction to active development in 2025–2026, with multiple companies and billionaires investing heavily in orbital AI infrastructure.

## Speculative-Decoding.Md

- [[concepts/speculative-decoding]] — A technique to accelerate LLM inference by using a smaller "draft" model to generate candidate tokens, which are then verified in parallel by a larger "target" model. Reduces per-token latency by 2-4x

## Speech

- [[concepts/speech/whisper]] — Whisper is OpenAI's general-purpose speech recognition model, released in 2022. It uses a Transformer encoder-decoder architecture trained on 680k hours of multilingual and multitask supervised data.

## Sqs-Lambda-Esm-Scaling.Md

- [[concepts/sqs-lambda-esm-scaling]] — AWS LambdaのEvent Source Mapping (ESM)はSQSキューからメッセージをPullし、Lambda関数を自動起動する仕組み。Rehan van der Merweが100回以上の実験で得た知見をまとめる。

## Structured-Outputs.Md

- [[concepts/structured-outputs]] — Structured outputs is the paradigm of constraining LLM generation to produce valid, machine-readable data (JSON, XML, Pydantic models) rather than free-form text. This enables reliable integration of 

## Subagents.Md

- [[concepts/subagents]] — Parallel agent delegation patterns. See harness-engineering/agentic-workflows/subagents.md for full content.

## Test-Case-Minimization.Md

- [[concepts/test-case-minimization]] — This article describes a minimal property-based testing (PBT) library in ~256 lines of Zig that uses binary search on entropy size to automatically minimize failing test cases.

## Token-Economics.Md

- [[concepts/token-economics]] — LLM inference cost analysis, optimization layers, and the economics of running language models at scale. A prerequisite concept for [[context-engineering]].

## Tokenmaxxing.Md

- [[concepts/tokenmaxxing]] — Post-AIE Miami (April 2026), AI leadership has shifted toward "Tasteful Tokenmaxxing" — maximizing AI adoption and ROI while avoiding wasteful, low-quality output cycles. The concept represents a cult

## Ungrounded-Meaning.Md

- [[concepts/ungrounded-meaning]] — Analysis of whether language meaning can be learned from textual form alone, based on Shunyu Yao's commentary on Merrill et al.'s [Provable Limitations of Acquiring Meaning from Ungrounded Form](https

## Vajra-Background-Agent.Md

- [[concepts/vajra-background-agent]] — Vajra is an open-source background coding agent that autonomously handles issue planning, implementation, review, and PR creation. Inspired by real-world validation from major tech companies (Coinbase

## Vector-Db-Agent-Memory.Md

- [[concepts/vector-db-agent-memory]] — Vector databases are the dominant infrastructure for AI agent long-term memory (LTM) and semantic memory, enabling agents to persist and retrieve information across sessions via dense embedding simila

## Vibe-Coding.Md

- [[concepts/vibe-coding]] — A loose, prompt-driven development approach where you describe what you want and let the AI generate code with minimal oversight. See harness-engineering/agentic-workflows/vibe-coding.md for full content.

## World-Models-Science.Md

- [[concepts/world-models-science]] — Using world models and agent loops to automate scientific research and discovery.
