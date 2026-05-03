     1|---
     2|title: "Concepts"
     3|tags:
     4|  - training
     5|  - concept
     6|  - ai-agents
     7|  - model
     8|  - local-llm
     9|  - prompting
    10|  - rag
    11|  - evaluation
    12|  - inference
    13|created: 2026-04-24
    14|updated: 2026-04-24
    15|---
    16|
    17|# Concepts
    18|
    19|AI and LLM concept pages organized by topic.
    20|
    21|## Overview
    22|
    23|## AI Agent Architecture Patterns
    24|
    25|- [[concepts/functional-core-imperative-shell]] — Architecture pattern separating deterministic, pure-functional processing (core) from side-effect-heavy decision making (shell). In AI agents, the functional core handles mechanical, verifiable tasks while the imperative shell manages validation, evaluation, and strategic decision-making.
    26|- [[concepts/reasoning-compression]] — The principle that software complexity and reasoning requirements will be compressed over time as models improve, eliminating the need for extensive exploration and reducing the imperative shell to validation/evaluation only.
    27|- [[concepts/agent-serverless]] — Serverless deployment pattern for AI agents — managed environments with built-in SaaS integration, permissions, and security. Includes enterprise tiers with persistent logs, audit trails, and turnkey agent infrastructure.
    28|- [[concepts/agent-iam]] — Agent IAM / Non-Human Identity Security for managing permissions and access control for AI agents interacting with enterprise systems.
    29|- [[concepts/automation-series]] â 10-part series by Antoine Buteau on automation architecture: three kinds of work (deterministic/probabilistic/accountable), bounded agents, the automation boundary (code vs model vs human), HITL as design pattern, state/idempotency/queues, observability/replay, failure modes/blast radius, and an architecture worksheet.
    30|- [[concepts/bitter-lesson-harnessing]] — How model intelligence evolution affects the importance of harness engineering — as models get smarter, harness complexity becomes less critical.
    31|- [[concepts/generative-app-evolution]] — Generative App Evolution pattern: UI → Stateless App → Stateful App progression in AI-driven applications.
    32|
    33|## Harness-Engineering
    34|
    35|- [[concepts/harness-engineering/agentic-engineering-patterns]] — Simon Willisonが2026年2月23日に開始したガイドプロジェクト。コーディングエージェント（Claude Code、OpenAI Codex、Gemini CLI等）から最高の結果を得るための実践パターンを体系化したもの。
    36|- [[concepts/harness-engineering/agentic-engineering]] — Based on the concept popularized by Simon Willison's [Agentic Engineering guide](https://simonwillison.net/2025/Apr/11/agentic-engineering/).
    37|- [[concepts/harness-engineering/agentic-workflows/agent-first-design]] — コードベースを「人間がナビゲートしやすい」のではなく「AIエージェントが作業しやすい」ように設計する哲学。
    38|- [[concepts/harness-engineering/agentic-workflows/agentic-manual-testing]] — コーディングエージェントによる探索的テスト。自動テストがパスしても見逃される問題（クラッシュ、UI欠落、エッジケース）を発見するために、エージェントの手動テスト能力を活用する。
    39|- [[concepts/harness-engineering/agentic-workflows/anti-patterns]] — Simon Willisonが警告するコーディングエージェント使用時のアンチパターン。特に「レビューされていないコードを他者に押し付ける」行為は深刻な問題。
    40|- [[concepts/harness-engineering/agentic-workflows/cli-first-development]] — ソフトウェア開発をCLI（コマンドラインインターフェース）から始めるアプローチ。エージェント時代の開発ワークフローの核心パターン。
    41|- [[concepts/harness-engineering/agentic-workflows/code-hoarding]] — Simon Willisonが提唱する、開発者が学んだスキルや解決策を意図的に蓄積し、再利用するプラクティス。
    42|- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — AIエージェントが生成したコードの動作理解を失うことで蓄積する認知的負債。技術的負債の認知版。[[concepts/vibe-coding]]によって加速度的に増加する。
    43|- [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Simon Willisonが提唱する、AIコーディングエージェントと人間開発者の協調による反復的改善サイクル。
    44|- [[concepts/harness-engineering/agentic-workflows/context-window-management]] — コーディングエージェントのコンテキストウィンドウを効果的に管理し、品質とコストを最適化するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/)で詳述。
    45|- [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] — コーディングエージェントにプロジェクトを渡した際の最初の4単語プロンプト。Simon Willisonが提唱する、エージェントをテスト思考に切り替える最小限の指示。
    46|- [[concepts/harness-engineering/agentic-workflows/hoard-things-you-know]] — Simon Willisonが提唱する知識の貯蔵と再利用の概念。エージェント時代において、個人が「どのように行うか知っているか」を記録・蓄積することが強力な武器になる。
    47|- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] — コーディングエージェントの内部仕組みを理解するための概念モデル。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/)で詳述。
    48|- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] — コーディングエージェントに対話的アニメーションやビジュアライゼーションを生成させ、アルゴリズムや概念を直感的に理解するパターン。
    49|- [[concepts/harness-engineering/agentic-workflows/karpathy-rl-agents]] — Andrej Karpathyが提唱する自律的研究ループ（Autonomous Research Loop）のパターン。2026年3月の[AutoResearch](https://github.com/karpathy/autoresearch/)プロジェクトと[No Priors podcast](https://www.youtube.com/watch?v=kwSVtQ7dziU)での発言
    50|- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — コーディングエージェントにコードベースの構造化された解説を生成させるパターン。既存コードの理解、忘れかけた自分のコードの復習、Vibe Codingしたコードの仕組み理解に有効。
    51|- [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]] — Simon Willisonが提唱するプロンプトを中心としたソフトウェア開発手法。AIコーディングエージェントに対して、詳細な仕様をプロンプトとして記述し、それを実装させるワークフロー。
    52|- [[concepts/harness-engineering/agentic-workflows/red-green-tdd]] — コーディングエージェントとの開発において、テストファースト開発を適用するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)の中核概念。
    53|- [[concepts/harness-engineering/agentic-workflows/rodney]] — Simon Willisonが開発したChrome DevTools ProtocolベースのCLIブラウザ自動化ツール。コーディングエージェントがWeb UIをテスト・検証するために設計。
    54|- [[concepts/harness-engineering/agentic-workflows/showboat]] — Simon Willisonが開発した、コーディングエージェントに「自分の作業を示させる」ためのドキュメンテーション/成果物生成ツール。
    55|- [[concepts/harness-engineering/agentic-workflows/subagents]] — メインのAIエージェントが独立したサブエージェントを並列に起動し、それぞれが隔離されたコンテキストとターミナルセッションでタスクを実行するパターン。
    56|- [[concepts/harness-engineering/agentic-workflows/throw-away-draft-pattern]] — エージェントに最初に捨て台本（throw-away draft）を書かせ、それを自分のメンタルモデルと比較してから、改めて反復する開発パターン。
    57|- [[concepts/harness-engineering/agentic-workflows/using-git-with-agents]] — コーディングエージェントとGitを統合するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)で詳述。
    58|- [[concepts/harness-engineering/agentic-workflows/vibe-coding]] — Simon Willisonが定義する、「コードに一切注目せずにLLMでコードを書く」開発スタイル。
    59|- [[concepts/harness-engineering/context-engineering]] — コンテキストウィンドウを効果的に活用し、LLMの性能を最大化する体系的アプローチ。Harness Engineeringの横断技術コンポーネントとして位置づけられる。
    60|- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — AnthropicがClaude Developer Platformでリリースした、大規模ツール使用を可能にする3つの新機能。
    61|- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — LLMエージェントが自律的にタスクを完了させるための実行ループ構造。モデルがアクションを提案し、プラットフォームが実行し、結果をモデルにフィードバックする循環プロセス。
    62|- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — エージェントが外部システムと安全に相互作用するためのセキュリティ制御パターン。OpenAI Responses APIのコンテナ環境で実装されている。
    63|- [[concepts/harness-engineering/system-architecture/agent-skills]] — エージェントが再利用可能なワークフローパターンをSKILL.md bundlesとしてパッケージ化する仕組み。同じマルチステップパターンを毎回再発見・再計画するコストを削減する。
    64|- [[concepts/harness-engineering/system-architecture/ai-memory-systems]] — AIアシスタント・エージェントにおける「メモリ（記憶）」システムの設計哲学の比較。OpenAI、Anthropic、Cognition（Devin）がそれぞれ異なるアプローチを採用しており、これは製品ターゲット（コンシューマー vs 技術者）とアーキテクチャ思想（自動 vs 明示的）の違いを反映している。
    65|- [[concepts/harness-engineering/system-architecture/anthropic-memory-tool-cognition]] — 2025年10月、AnthropicはClaude APIにMemory Toolを正式に導入した。これは6つのファイル操作（view, create, str_replace, insert, delete, rename）をモデルにネイティブに提供するという、非常に「opinionated（意見が明確な）」設計だった。Cognition（Devinの開発元）はこの動きをいち早くキャッチし、An
    66|- [[concepts/harness-engineering/system-architecture/building-effective-agents]] — Anthropicが数十社のチームとの協働から得た、LLMエージェント構築の実践的ガイドライン。
    67|- [[concepts/harness-engineering/system-architecture/claude-code-best-practices]] — Anthropic公式のClaude Code（エージェント型コーディングツール）使用ベストプラクティス。
    68|- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — MCP（Model Context Protocol）サーバーをコードAPIとして公開し、エージェントがコードを書いてツールを呼び出すパターン。Cloudflareの「Code Mode」と同じ核心洞察。
    69|- [[concepts/harness-engineering/system-architecture/container-context]] — エージェントに永続的な実行環境を提供するホスト型コンテナ。ファイルシステム、データベース、ネットワークアクセスを統合した「モデルの作業スペース」。
    70|- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Discovered during Cognition's integration of Claude Sonnet 4.5 into Devin.
    71|- [[concepts/harness-engineering/system-architecture/context-compaction]] — 長期実行エージェントがコンテキストウィンドウの限界に達した際、重要な情報を保持しつつ不要なデータを圧縮する仕組み。OpenAI Responses APIのネイティブ機能。
    72|- [[concepts/harness-engineering/system-architecture/effective-harnesses-for-long-running-agents]] — AnthropicがClaude Agent SDKで開発した、長時間実行エージェント用の2エージェント・ハーネスパターン。
    73|- [[concepts/harness-engineering/system-architecture/evals-for-ai-agents]] — Anthropicが提唱する、AIエージェントの評価（Evals）の体系化ガイド。
    74|- [[concepts/harness-engineering/system-architecture/harness-design-long-running-apps]] — Anthropicが長時間実行のアプリケーション開発向けに設計したエージェントハーネス（枠組み）のパターン。GAN（生成的敵対ネットワーク）のGenerator-Evaluatorループに着想を得た。
    75|- [[concepts/harness-engineering/system-architecture/infrastructure-noise]] — エージェント型コーディングベンチマークにおいて、インフラ設定のみがスコアに与える影響を定量化した調査。
    76|- [[concepts/harness-engineering/system-architecture/multi-agent-research-system]] — Anthropicが構築した、複数のClaudeエージェントを並列に動作させるリサーチシステム。
    77|- [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]] — Anthropicが実践した、AIエージェント向けのツール設計方法论。「エージェントのためにツールを書き、エージェントを使ってツールを最適化する」アプローチ。
    78|
    79|## Fine-Tuning
    80|
    81|- [[concepts/fine-tuning/axolotl]] — Axolotl is a YAML-configured fine-tuning framework supporting 100+ models with LoRA/QLoRA, DPO/KTO/ORPO/GRPO, and multimodal capabilities.
    82|- [[concepts/fine-tuning/grpo-rl-training]] — Group Relative Policy Optimization — a reinforcement learning approach for fine-tuning language models that compares multiple completions within a group to learn preferred behaviors without requiring 
    83|- [[concepts/fine-tuning/peft-lora-qlora]] — Full fine-tuning of a 70B model requires hundreds of GBs of GPU memory. PEFT methods reduce this dramatically by:
    84|- [[concepts/fine-tuning/pytorch-fsdp]] — FSDP enables distributed training of large models by sharding model parameters, gradients, and optimizer states across multiple GPUs.
    85|- [[concepts/fine-tuning/quantization-overview]] — Quantization reduces model precision (FP32 → FP16 → INT8 → INT4) to decrease memory requirements and improve inference speed with minimal accuracy loss.
    86|- [[concepts/fine-tuning/rlhf-dpo-preference]] — After Supervised Fine-Tuning (SFT), preference optimization methods align models with human values and desired behaviors. These methods differ in data requirements, complexity, and training stability.
    87|- [[concepts/fine-tuning/trl]] — TRL is HuggingFace's library for fine-tuning language models with reinforcement learning and preference optimization methods.
    88|- [[concepts/fine-tuning/unsloth]] — Unsloth is a fine-tuning optimization library providing 2-5x faster training with 50-80% less memory usage through custom Triton kernels and LoRA/QLoRA optimization.
    89|
    90|## Local-Llm
    91|
    92|- [[concepts/local-llm/dgx-spark-nim]] — 2台のDGX SparkをQSFPケーブル（ConnectX-7, 200 Gbps）で接続し、分散推論が可能。RoCE（RDMA over Converged Ethernet）経由でMPI + NCCL v2.28.3による並列推論を実行。
    93|- [[concepts/local-llm/gguf]] — GGUF is the quantization format used by llama.cpp for efficient CPU/Apple Silicon inference.
    94|- [[concepts/local-llm/inference-hardware]] — Hardware options for running LLMs locally, from consumer GPUs to edge devices.
    95|- [[concepts/local-llm/model-distillation]] — 1. Model compression: Creating smaller, efficient models suitable for consumer hardware
    96|- [[concepts/local-llm/model-quantization]] — Without quantization, most open-weight models would not fit in consumer GPU VRAM (24 GB on RTX 4090) or even the DGX Spark's 128 GB unified memory.
    97|- [[concepts/local-llm/ollama]] — (content needed)
    98|- [[concepts/local-llm/self-hosting-ai-development]] — The core tension: control and cost predictability vs. convenience and performance.
    99|- [[concepts/local-llm/server-dgx-spark]] — Complete setup guide for running a local LLM server on NVIDIA DGX Spark, with focus on NemoClaw integration for secure AI agent development.
   100|
   101|## Openclaw
   102|
   103|- [[concepts/openclaw/anthropic-conflict]] — 2026年4月、AnthropicはClaudeのサブスクリプションプラン（Pro/Max）からサードパーティAIエージェントフレームワーク（OpenClawなど）のアクセスをブロックした。この決定は、プラットフォーム管理、開発者アクセス、AIエージェントインフラの経済学をめぐる重大な論争を引き起こした。
   104|- [[concepts/openclaw/architecture-comparison]] — elvis（@elvis_）が2026年4月に行った9時間のHermes Agent vs OpenClawの並列ソースコード研究に基づくアーキテクチャ比較分析。
   105|- [[concepts/openclaw/ecosystem-tools]] — Peter Steinberger（@steipete）が開発したMCP-first開発者ツールエコシステム。OpenClawを中核とし、複数のCLI/MCPサーバーが相互連携する構造。
   106|- [[concepts/openclaw/five-tier-precedence]] — OpenClawのスキルロードシステムが採用する階層的優先度モデル。Hermes Agentのself-authoring（自己作成）アプローチとの対比において、最も重要なアーキテクチャ上の差異の一つ。
   107|- [[concepts/openclaw/philosophy]] — OpenClawの設計哲学の中核は「Primitives over Defaults」（デフォルトではなくプリミティブを提供する）。これはLinuxカーネルやKubernetesの設計思想に近い。
   108|
   109|## Ai-Organization
   110|
   111|- [[concepts/ai-organization/ai-org-context-as-moat]] — AIが実行レイヤーを代替する時代において、企業の競争優位は「何をどのように判断するか」という独自の文脈(context)に収斂する。McKinseyのAgentic Organizationフレームワーク、ReworkedのDiamond Org Chart議論、そしてAgile Leadership Dayの実践的組織図モデルを統合する。
   112|- [[concepts/ai-organization/ai-org-from-hierarchy-to-intelligence]] — Jack Dorseyが2024年にBlock（旧Square）で実践したHierarchy to Intelligenceモデル。従来のヒエラルキー型意思決定を廃し、「文脈駆動の自律実行 + 透明性ベースの監視」への移行を宣言。AIを単なる生産性向上ツールではなく、「協調メカニズムそのものの再設計」として捉える。
   113|- [[concepts/ai-organization/ai-org-solo-founder-and-super-ic]] — AIツールスタックが成熟するにつれ、「1人 = 従来の10人チーム」というパラダイムが現実化している。Reddit r/ClaudeCodeコミュニティとFourWeekMBAの議論を統合し、ソロ創業者の台頭、スーパーICの登場、そしてその限界と課題を整理する。
   114|
   115|## Inference
   116|
   117|- [[concepts/inference/llama-cpp]] — llama.cpp is a C/C++ inference engine for running LLMs efficiently on consumer hardware, created by Georgi Gerganov.
   118|- [[concepts/inference/sglang]] — SGLang's signature optimization. Builds a tree-structured KV cache across requests sharing common prefixes:
   119|| [[concepts/inference/vllm]] — vLLM is a high-throughput LLM serving engine with PagedAttention optimization.
   120||- [[concepts/tensorrt-llm]] — NVIDIA's optimized inference engine with TensorRT compiler, FP8/FP4 quantization, Triton integration. Highest throughput on NVIDIA GPUs.
   121|
   122|## Ai-Infrastructure-Engineering
   123|
   124|- [[concepts/ai-infrastructure-engineering/_index]] — Parent page: AI Infrastructure Engineering. GPU/VRAM fundamentals, distributed training, model serving, observability, cost optimization.
   125|- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPU memory hierarchy, VRAM requirement calculation, roofline model, batching economics, quantization effects. ⬜ L1
   126|- [[concepts/ai-infrastructure-engineering/distributed-training]] — DDP → FSDP → DeepSpeed ZeRO stages, 3D parallelism (TP/PP/EP), strategy selection guide. ⬜ L1
   127|- [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — Deployment architectures, autoscaling strategies (HPA, predictive, serverless), load balancing, cost optimization. ⬜ L1
   128|- [[concepts/ai-infrastructure-engineering/llm-observability]] — Inference metrics (TTFT, TPOT, ITL), GPU/VRAM monitoring, cost attribution, production patterns, vLLM OTel integration. ⬜ L1
   129|
   130|## Web-Filesystem.Md
   131|
   132|- [[concepts/web-as-filesystem]] — Webの全ドキュメントをUnixファイルシステムとしてマウントする抽象化。エージェントに`tree`、`grep`、`cat`、`find`を自然に使い、コード幻覚を解消。Nia (Nozomio Labs) による実装。
   133|
   134|## Sandbox
   135|
   136|- [[concepts/sandbox/in-process]] — In-process sandboxing isolates LLM-generated code execution within the host process using language-level security boundaries — without requiring Docker, cloud accounts, or external infrastructure. Thi
   137|- [[concepts/sandbox/infrastructure]] — Infrastructure-level sandboxing refers to OS/hypervisor-level isolation technologies used to safely execute AI agent code — particularly LLM-generated or user-supplied code — without compromising the 
   138|- [[concepts/sandbox/js-runtime]] — JavaScript/TypeScript runtimes form a critical layer of the AI agent stack. Unlike Python's single CPython implementation, the JS ecosystem offers three competing runtimes with fundamentally different
   139|
   140|## Agent-Loop-Orchestration.Md
   141|
   142|- [[concepts/agent-loop-orchestration]] — OpenAI Responses API patterns for orchestrating agent loops. See harness-engineering/system-architecture/agent-loop-orchestration.md for full content.
   143|
   144|## Agent-Sandboxing.Md
   145|
   146|- [[concepts/agent-sandboxing]] — Agent Sandboxingは、AIエージェントの動的コード実行を安全に隔离する技術譜。gVisor、FirecrackermicroVM、WASM等の隔离技術を整理。標準コンテナは共有カーネルのため不十分。
   147|
   148|## Agent-Survival-Benchmark.Md
   149|
   150|- [[concepts/agent-survival-benchmark]] — LLMエージェントの生存能力とPvP（プレイヤー対プレイヤー）圧力下での性能を測定するオープンソースベンチマーク。
   151|
   152|## Agent-Team-Swarm.Md
   153|
   154|- [[concepts/agent-team-swarm]] — Agent team swarm refers to coordination patterns where multiple AI agents work together in distributed, emergent structures rather than rigid hierarchies.
   155|
   156|## Agent-Team-Swarm
   157|
   158|- [[concepts/agent-team-swarm/managed-devins]] — Cognition's evolved approach to multi-agent coordination, introduced in Devin 2.2.
   159|
   160|## Agentic-Alternative-To-Graphrag.Md
   161|
   162||- [[concepts/agentic-alternative-to-graphrag]] — A November 2025 paper by Contextual AI (George Halal, Jackie Zhang, Sheshansh Agrawal) proposing that the reference traversal problem in RAG pipelines should be solved via agentic tool-use rather than
   163|
   164|## Agentic-Browsing.Md
   165|
   166||- [[concepts/agentic-browsing]] — Agentic Browsing refers to AI agents that autonomously navigate websites, click buttons, fill forms, and execute multi-step web tasks without human intervention. Tools like Browser Use, Playwright MCP, and Puppeteer enable agents to interact with web UIs as humans do — clicking, scrolling, typing, and reading structured and unstructured content.
   167|
   168|## Agentic-Engineering.Md
   169|
   170|- [[concepts/agentic-engineering]] — This stub exists for backwards compatibility while content is organized into the harness-engineering/ subdirectory structure.
   171|
   172|## Agentic-Manual-Testing.Md
   173|
   174|- [[concepts/agentic-manual-testing]] — Manual testing enhanced with AI agent assistance. See harness-engineering/agentic-workflows/agentic-manual-testing.md for full content.
   175|
   176|## Agentic-Pbt.Md
   177|
   178|- [[concepts/agentic-pbt]] — Anthropic + Hypothesis共同研究（NeurIPS 2025 DL4C Workshop）。Claude Codeエージェントが型注釈、docstring、関数名、コメントからコードの不変条件（properties）を自律的に推論し、HypothesisフレームワークでPBTを生成・実行する。
   179|
   180|## Agentic-Rag.Md
   181|
   182||- [[concepts/agentic-rag]] — Agentic RAG integrates autonomous AI agents into the RAG pipeline, enabling dynamic retrieval, iterative context refinement, and adaptive workflow orchestration. It addresses limitations of traditiona
   183|
   184|## Agentic-Security.Md
   185|
   186||- [[concepts/agentic-security]] — Agentic Security encompasses the security patterns, protocols, and tools for protecting AI agents, MCP servers, and the broader agent ecosystem. Covers authentication, authorization, data exfiltration prevention, MCP server security, prompt injection defense, and sandboxing strategies for agentic systems.
   187|
   188|## Agentic-Scaffolding.Md
   189|
   190|- [[concepts/agentic-scaffolding]] — エージェントを本番環境で安全に動作させるための「足場」パターン。エージェントの力を最大化しつつ、リスクを管理するインフラストラクチャ設計。
   191|
   192|## Agentic-Theory.Md
   193|
   194|- [[concepts/agentic-theory]] — Sean Goedecke's analysis applying Peter Naur's 1985 "theory building" concept to AI-assisted programming.
   195|
   196|## Agentic-Web.Md
   197|
   198|- [[concepts/agentic-web]] — (content needed)
   199|
   200|## Agentic-Workflow-Patterns.Md
   201|
   202|- [[concepts/agentic-workflow-patterns]] — (content needed)
   203|
   204|## Ai-Addiction-Burnout.Md
   205|
   206|- [[concepts/ai-addiction-burnout]] — AI coding tools trigger a compulsion loop similar to slot machines:
   207|
   208|## Ai-Agent-Memory-Middleware.Md
   209|
   210|- [[concepts/ai-agent-memory-middleware]] — AIエージェントが状態を永続化し、セッション間でコンテキストを共有し、複数エージェントパイプラインで協調するためのストレージインフラストラクチャの横断分析。
   211|
   212|## Ai-Agent-Memory-Two-Camps.Md
   213|
   214|- [[concepts/ai-agent-memory-two-camps]] — Classification of AI memory/context tools into two fundamentally different paradigms: Memory Backends vs Context Substrates.
   215|
   216|## Ai-Agent-Traps.Md
   217|
   218|- [[concepts/ai-agent-traps]] — A systematic framework from Google DeepMind (2026) for understanding how the open web can be weaponized against autonomous AI agents. Defines six categories of adversarial content engineered to exploi
   219|
   220|## Ai-Autonomy-Debate.Md
   221|
   222|- [[concepts/ai-autonomy-debate]] — The AI Autonomy Debate centers on whether AI agents should operate fully autonomously or maintain human oversight in the loop. What started as a niche technical discussion has become one of the most c
   223|
   224|## Ai-Bubble-Economics.Md
   225|
   226|- [[concepts/ai-bubble-economics]] — The AI Bubble Economics concept encompasses the growing body of analysis questioning whether the unprecedented capital flowing into artificial intelligence infrastructure is backed by real economic va
   227|
   228|## Ai-Coding-Agent-Criticism.Md
   229|
   230|- [[concepts/ai-coding-agent-criticism]] — Armin Ronacher (lucumr.pocoo.org) identified a structural asymmetry in how AI coding agents are debated:
   231|
   232|## Ai-Coding-Reliability.Md
   233|
   234|- [[concepts/ai-coding-reliability]] — The central tension: AI tools can write code faster than any human, but writing code is not the same as shipping reliable software. The industry is discovering this distinction at scale in 2026.
   235|
   236|## Ai-Digital-Nato.Md
   237|
   238|- [[concepts/ai-digital-nato]] — In April 2026, OpenAI, Anthropic, and Google began sharing threat intelligence through the Frontier Model Forum (founded with Microsoft in 2023) to detect and counter what they term "adversarial disti
   239|
   240|## Ai-Evals.Md
   241|
   242|- [[concepts/ai-evals]] — Product-specific evaluation systems for measuring whether an AI application works correctly on real tasks with real data. Not foundation model benchmarks like MMLU, HELM, or GPQA.
   243|
   244|## Ai-Index-Report-2026.Md
   245|
   246|- [[concepts/ai-index-report-2026]] — スタンフォード大学HAI（Human-Centered AI Institute）が発表した年次AI指数レポート。AIの研究開発、技術性能、経済影響、倫理・ガバナンスなど包括的なデータを収録。
   247|
   248|## Ai-Memory-Systems.Md
   249|
   250|- [[concepts/ai-memory-systems]] — OpenAIのChatGPT Memory、AnthropicのClaude Memory（開発中）、CognitionのDevin Memoryは、それぞれ異なる設計哲学に基づいている。このページは3つのアプローチを比較し、コーディングエージェントにおけるメモリシステムの最適設計を探る。
   251|
   252|## Ai-Military.Md
   253|
   254|- [[concepts/ai-military]] — Coverage of AI systems (particularly Claude) outperforming US military teams in wargame simulations, and the subsequent Pentagon-Anthropic dispute over military use of AI.
   255|
   256|## Ai-Observability.Md
   257|
   258|- [[concepts/ai-observability]] — AI observability extends traditional software observability (metrics, logs, traces) to cover the unique challenges of LLM-powered applications: non-deterministic outputs, token usage, agent decision t
   259|
   260|## Ai-Privacy-Tools.Md
   261|
   262|- [[concepts/ai-privacy-tools]] — In early 2026, the AI security community identified a novel technique dubbed "Slingshot" — a CORS-based attack vector that allows AI agents and browser automation tools to bypass traditional web secur
   263|
   264|## Ai-Safety.Md
   265|
   266|- [[concepts/ai-safety]] — AI Safety encompasses the technical and philosophical work of ensuring that increasingly capable AI systems behave as intended, remain aligned with human values, and can be understood and controlled b
   267|
   268|## Ai-Subprime.Md
   269|
   270|- [[concepts/ai-subprime]] — Ed Zitron's analysis drawing parallels between the 2008 subprime mortgage crisis and the current AI industry economics.
   271|
   272|## Anthropic-Managed-Agents.Md
   273|
   274|- [[concepts/anthropic-managed-agents]] — Anthropic Managed Agentsは、AI Agentのプロトタイプから本番運用までを10倍速く実現するプラットフォーム。インフラ構築（サンドボックス、認証、権限管理、チェックポイント、エラーリカバリー）をClaudeに委譲し、開発者はタスク定義・ツール・ガードレールの設計に集中できる。
   275|
   276|## Anthropic-Openclaw-Conflict.Md
   277|
   278|- [[concepts/anthropic-openclaw-conflict]] — In April 2026, Anthropic blocked third-party AI agent frameworks (including OpenClaw) from accessing Claude models through flat-rate subscription plans (Pro/Max). This decision triggered a significant
   279|
   280|## Attention-Mechanism-Variants.Md
   281|
   282|- [[concepts/attention-mechanism-variants]] — Modern transformer architectures use different attention mechanisms to optimize the trade-off between modeling capacity, compute efficiency, and context length. A prerequisite concept for [[context-engineering]]
   283|
   284|## Back-Of-House-Multi-Agent-Patterns.Md
   285|
   286|- [[concepts/back-of-house-multi-agent-patterns]] — 厨房のメタファーを用いたマルチエージェント・ワークフローパターン。Sarah Chieng ([[concepts/@milksandmatcha]]) と [@0xSero] によって2026年4月に提唱。
   287|
   288|## Back-Of-House-Patterns.Md
   289|
   290|- [[concepts/back-of-house-patterns]] — プロの厨房（Back of House）のメタファーを用いたマルチエージェント・ワークフローパターン。単一エージェントの限界（[[concepts/single-agent-ceiling]]）を解決するための実践的フレームワーク。
   291|
   292|## Base-Consistency.Md
   293|
   294|- [[concepts/base-consistency]] — BASE is an alternative consistency model to ACID, designed for distributed systems that prioritize availability over strict consistency. It stands for:
   295|
   296|## Behavioral-Trait-Transmission.Md
   297|
   298||- [[concepts/behavioral-trait-transmission]] — Language models that share initialization can transmit behavioural traits through training data that is semantically unrelated to those traits — a phenomenon discovered by Anthropic and academic resea
   299|
   300|## Blogwatcher.Md
   301|
   302||- [[concepts/blogwatcher]] — Blogwatcher is a CLI-based blog and RSS feed monitoring tool (written in Go) for tracking technical blogs and newsletters. It periodically scans configured RSS/Atom feeds, detects new posts, and can be integrated into automated workflows for content discovery and curation.
   303|
   304|## Building-Effective-Agents.Md
   305|
   306|- [[concepts/building-effective-agents]] — Anthropic's guide to building effective AI agents. See harness-engineering/system-architecture/building-effective-agents.md for full content.
   307|
   308|## Caid-Coordination.Md
   309|
   310|- [[concepts/caid-coordination]] — A coordination framework from CMU (2026) for running multiple coding agents in parallel on complex software engineering tasks. Uses git operations as the core coordination primitive.
   311|
   312|## Capabilities-Based-Security.Md
   313|
   314|- [[concepts/capabilities-based-security]] — Security model starting from zero access, explicitly granting capabilities. See sandbox patterns for full content.
   315|
   316|## Causal-Backbone-Conjecture.Md
   317|
   318|- [[concepts/causal-backbone-conjecture]] — The conjecture proposes that agent-like structures emerge naturally from resource constraints, not from the need to model "a sufficiently rich set of tasks." In environments with finite resources (com
   319|
   320|## Chaos-Engineering.Md
   321|
   322|- [[concepts/chaos-engineering]] — Chaos Engineering is the discipline of experimenting on a system to build confidence in its ability to withstand turbulent conditions in production. For microservices, this means intentionally injecti
   323|
   324|## Chatgpt-Memory-Bitter-Lesson.Md
   325|
   326|- [[concepts/chatgpt-memory-bitter-lesson]] — Analysis of ChatGPT's memory system through the lens of Rich Sutton's Bitter Lesson — arguing that the best way to build agent memory is not to build one at all, but to embrace stateless, context-wind
   327|
   328|## Chief-Of-Staff-Agent-Patterns.Md
   329|
   330|- [[concepts/chief-of-staff-agent-patterns]] — Anthropic cookbook: [The Chief of Staff Agent](https://platform.claude.com/cookbook/claude-agent-sdk-01-the-chief-of-staff-agent)
   331|
   332|## Claude-47-Tokenizer.Md
   333|
   334|- [[concepts/claude-47-tokenizer]] — 2026年4月16日にClaude Opus 4.7がリリースされ、初めてトークナイザーが変更された。この変更により、同じ入力テキストが40%多いトークンにマッピングされる。
   335|
   336|## Claude-Agent-Sdk-Sre-Patterns.Md
   337|
   338|- [[concepts/claude-agent-sdk-sre-patterns]] — Anthropic cookbook: [The Site Reliability Agent](https://platform.claude.com/cookbook/claude-agent-sdk-03-the-site-reliability-agent)
   339|
   340|## Claude-Code-Best-Practices.Md
   341|
   342|- [[concepts/claude-code-best-practices]] — Practical patterns and techniques for effective Claude Code usage, synthesized from experienced users' real-world workflows. These complement the internal patterns found in  — March 2026 incident where Anthropic's Claude Code source code was leaked via npm package.
   343|
   344|## Claude-Code-Source-Patterns.Md
   345|
   346|- [[concepts/claude-code-source-patterns]] — Analysis of tactical engineering patterns found in Claude Code's leaked source code (March 2026). Reveals how Anthropic builds production-grade coding agents with emphasis on prompt composition, cache
   347|
   348|## Claude-Memory-Tool.Md
   349|
   350|- [[concepts/claude-memory-tool]] — Analysis of how Cognition (makers of Devin) is adopting Claude's memory approach — and what this reveals about competitive dynamics in the coding agent space.
   351|
   352|## Claude-Memory.Md
   353|
   354|- [[concepts/claude-memory]] — Analysis of Claude's memory system design — how Anthropic uses filesystem-based memory (`CLAUDE.md`, `.agent/` directories) instead of proprietary databases, treating the filesystem as the single sour
   355|
   356|## Claude-Mythos-Glasswing.Md
   357|
   358|- [[concepts/claude-mythos-glasswing]] — The model was revealed via a CMS misconfiguration leak on March 26, 2026, when security researchers discovered ~3,000 unpublished Anthropic assets publicly accessible. Anthropic confirmed the leak was
   359|
   360|## Claude-Mythos-Preview.Md
   361|
   362|- [[concepts/claude-mythos-preview]] — Anthropic did not release Claude Mythos publicly. The preview is restricted to frontier red team research and select partners. This decision was characterized by The Signal Newsletter as a "lockdown" 
   363|
   364|## Cli-Over-Mcp-Pattern.Md
   365|
   366|- [[concepts/cli-over-mcp-pattern]] — Standard CLIs like `gh`, `vercel`, `psql` have:
   367|
   368|## Closing-Agent-Loop.Md
   369|
   370|- [[concepts/closing-agent-loop]] — Cognition's philosophy for autonomous development: Devin doesn't just write code — it handles the entire development loop.
   371|
   372|## Coala.Md
   373|
   374|- [[concepts/coala]] — CoALA (Cognitive Architectures for Language Agents) is a unified conceptual framework that maps modern LLM-based agents to the 50-year lineage of cognitive science and symbolic AI. It addresses the pr
   375|
   376|## Code-Mode.Md
   377|
   378|- [[concepts/code-mode]] — CodeMode is the paradigm where LLMs write code (typically Python) for batch execution rather than making sequential tool calls. Coined by Cloudflare and independently developed by Anthropic, Pydantic,
   379|
   380|## Cognition-Ai-Data-Analyst.Md
   381|
   382|- [[concepts/cognition-ai-data-analyst]] — Cognitionチームが提唱する、AIソフトウェアエンジニア（Devin）を24/7オンデマンドデータサイエンティストとして活用するアプローチ。SQL専用ツールではなく、コードベースの文脈理解+データ分析+可視化を統合したエージェント設計。
   383|
   384|## Cognition-Devin-Philosophy.Md
   385|
   386|- [[concepts/cognition-devin-philosophy]] — Cognition Labs（CEO: Scott Wu @ScottWu46）の Devin チームが発信する、AI coding agent に関する一貫した哲学。
   387|
   388|## Cognitive-Cost-Of-Agents.Md
   389|
   390|- [[concepts/cognitive-cost-of-agents]] — In April 2026, [[simon-willison]] published a deeply personal reflection after using Claude Code intensively for a full month. The post, "The cognitive impact of coding agents," challenged the prevail
   391|
   392|## Cognitive-Debt.Md
   393|
   394|- [[concepts/cognitive-debt]] — The accumulated mental overhead of understanding and maintaining complex AI-generated code. See harness-engineering/agentic-workflows/cognitive-debt.md for full content.
   395|
   396|## Cognitive-Load-Software-Development.Md
   397|
   398|- [[concepts/cognitive-load-software-development]] — Artem Zakirullinの "Cognitive load is what matters" — GitHubで12,000+スターを獲得したソフトウェア設計における認知負荷の体系的フレームワーク。
   399|
   400|## Compute-Scaling-Bottlenecks.Md
   401|
   402|- [[concepts/compute-scaling-bottlenecks]] — The concept was most thoroughly articulated by Dylan Patel of SemiAnalysis, particularly in his March 2026 Dwarkesh Podcast appearance, where he traced the entire AI compute stack from silicon atoms t
   403|
   404|## Context-Compression.Md
   405|
   406|- [[concepts/context-compression]] — Methods for reducing the size of context windows while preserving task-relevant information. Critical prerequisite for [[concepts/context-engineering]] — addresses the fundamental constraint that LLMs have fin
   407|
   408|## Context-Engineering.Md
   409|
   410|- [[concepts/context-engineering]] — This stub exists for backwards compatibility while content is organized into the harness-engineering/ subdirectory structure.
   411|
   412|## Context-Fragments.Md
   413|
   414|- [[concepts/context-fragments]] — Vivek Trivedy (@vtrivedy10) が2026年4月に提唱した概念。コンテキストウィンドウを「harnessが選択的にロードするオブジェクトの集合」として捉えるフレームワーク。
   415|
   416|## Context-Graph.Md
   417|
   418|- [[concepts/context-graph]] — Living record of decision traces stitched across entities and time — the foundational architecture for AI agent decision-making in enterprise workflows
   419|
   420|## Context-Routing.Md
   421|
   422|- [[concepts/context-routing]] — 多ドメインエージェントは、すべてのクエリに対してすべてのドメインの知識、ツールセット、指示を読み込む。これはコンテキストの浪費であり、注意力の分散を招く。
   423|
   424|## Context-Window-Management.Md
   425|
   426|- [[concepts/context-window-management]] — The core challenge: LLMs have a fixed context window, but software projects have unbounded complexity. Effective management is the difference between a productive AI session and a confused, expensive 
   427|
   428|## Critique-Shadowing.Md
   429|
   430|- [[concepts/critique-shadowing]] — A 7-step iterative methodology for building aligned LLM-as-Judge evaluators, coined by Hamel Husain. The core insight: the process of building an LLM judge forces domain experts to carefully examine d
   431|
   432|## Cybersecurity-Proof-Of-Work.Md
   433|
   434|- [[concepts/cybersecurity-proof-of-work]] — A concept coined by Drew Breunig in April 2026, observing that as LLMs like Claude Mythos become increasingly effective at finding security vulnerabilities, cybersecurity transforms into an economic e
   435|
   436|## Dark-Factory-Software-Factory.Md
   437|
   438|- [[concepts/dark-factory-software-factory]] — 「Dark Factory（暗黒工場）」とは、人間がコードを一切書かず、レビューもしないソフトウェア開発の最高自動化レベル。Fanucの無人工場（ロボットが稼働する工場は照明が不要＝暗い）に由来する比喻。
   439|
   440|## Death-Of-Browser.Md
   441|
   442|- [[concepts/death-of-browser]] — 1. 認知負荷の限界: 人間は多数のタブ、ポップアップ、SEOスパムに疲弊
   443|
   444|## Decoder-Only-Gpt.Md
   445|
   446|- [[concepts/decoder-only-gpt]] — The decoder-only GPT (Generative Pre-trained Transformer) is the dominant architecture behind modern large language models (ChatGPT, Claude, Gemini, etc.). Andrej Karpathy's microgpt project (February
   447|
   448|## Deep-Agents.Md
   449|
   450|- [[concepts/deep-agents]] — Deep agents are autonomous AI agents that combine multiple architectural patterns to handle complex, multi-step tasks with minimal human intervention. They feature:
   451|
   452|## Direct-Prompting-Philosophy.Md
   453|
   454|- [[concepts/direct-prompting-philosophy]] — The core thesis: "Don't waste your time on stuff like RAG, subagents, Agents 2.0 or other things that are mostly just charade. Just talk to it. Play with it. Develop intuition." — Peter Steinberger
   455|
   456|## Dspy-Rlm.Md
   457|
   458|- [[concepts/dspy-rlm]] — Recursive Language Model — 大規模コンテキストをsandobx Python REPLでプログラム的に探索するDSPyモジュール
   459|
   460|## Dspy.Md
   461|
   462|- [[concepts/dspy]] — DSPyはOmar Khattab率いるStanford NLPが開発した、LLMを「プロンプト」ではなく「最適化可能なモジュール」として宣言的にプログラミングするフレームワーク。Signature/Module/Teleprompterの抽象化により、手動プロンプトエンジニアリングをコンパイル時の自動最適化に変換する。
   463|
   464|## Ecs-Fargate-Scaling.Md
   465|
   466|- [[concepts/ecs-fargate-scaling]] — AWS ECS FargateをLambdaのようにスケーリングさせる実験的検証。SQSワークロードでのバーストハンドリング性能を最適化する。
   467|
   468|## Elixir-Beam-Agent-Orchestration.Md
   469|
   470|- [[concepts/elixir-beam-agent-orchestration]] — Elixir/BEAM（Erlang仮想マシン）をAIエージェントオーケストレーションに活用するパターン。[[concepts/openai-symphony]] のRyan Lopopoloが採用したアプローチ。
   471|
   472|## Evaluation-Flywheel.Md
   473|
   474|- [[concepts/evaluation-flywheel]] — OpenAIのcookbookで示される、評価と改善を循環させる開発パターン。
   475|
   476|## Event-Driven-Architecture.Md
   477|
   478|- [[concepts/event-driven-architecture]] — Event-Driven Architecture (EDA) is a software design pattern where services communicate asynchronously through events rather than synchronous API calls. Services publish events to a central event bus 
   479|
   480|## Exec-Plans.Md
   481|
   482|- [[concepts/exec-plans]] — エージェントにタスクを実行させる際、事前に計画（プラン）を立ててから実行するパターン。計画と実行を分離することで、透明性・再現性・デバッグ性を向上させる。
   483|
   484|## Experiential-Memory.Md
   485|
   486|- [[concepts/experiential-memory]] — Vivek Trivedy (@vtrivedy10) が2026年4月に提唱した概念。エージェントが相互作用を通じて蓄積する「経験的記憶」を、エージェント間で共有・フォーク・再利用するフレームワーク。
   487|
   488|## Flashattention-Pytorch-Educational.Md
   489|
   490|- [[concepts/flashattention-pytorch-educational]] — [shreyansh26/FlashAttention-PyTorch](https://github.com/shreyansh26/FlashAttention-PyTorch) は、FlashAttentionアルゴリズム（FA1からFA4まで）をPyTorchで教育的・アルゴリズム的明晰さのために実装したプロジェクト。
   491|
   492|## Formal-Verification-Llm-Agents.Md
   493|
   494|- [[concepts/formal-verification-llm-agents]] — Formal verification is the practice of mathematically proving that code always satisfies its specifications—including all edge cases. AI is poised to bring this from a fringe academic pursuit into the
   495|
   496|## Functional-Emotions-Llms.Md
   497|
   498|- [[concepts/functional-emotions-llms]] — The discovery that Large Language Models develop internal representations of emotion concepts that causally influence model behavior, including alignment-relevant outcomes. Based on Anthropic's 2026 i
   499|
   500|## Gemini.Md

- [[concepts/gemini]] — (content needed)

## Autonomous-Component-Optimization.Md

- [[concepts/autonomous-component-optimization]] — Daniel Miesslerが提唱する汎用的自己改善サイクル（Map→Execute→Log→Collect→Optimize→Update）。Karpathy LoopのML超パラメータチューニングを任意の知識ワークフローに拡張した概念。

## Intent-Based-Engineering.Md

- [[concepts/intent-based-engineering]] — AI開発における新たなボトルネック「articulation gap（表明のギャップ）」を特定した概念。エンジニアリングが「どう作るか」から「良い状態をどう記述するか」へ移行することを示す。Daniel Miessler提唱。   501|