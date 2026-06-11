---
title: "Production-Ready Agent Engineering: From MCP to RL"
type: concept
created: 2026-06-10
updated: 2026-06-11
tags:
  - ai-agents
  - reinforcement-learning
  - mcp
  - ai-agent-engineering
  - education
  - grpo
  - agentic-rl
  - evaluation
  - context-engineering
  - tool-calling
sources:
  - raw/articles/2026-06-10_maven_agents-mcp-rl-course-overview.md
  - raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning.md
  - raw/articles/2025-06-10_willbrown_training-agents-with-rl-lightning.md
  - raw/articles/2025-06-19_willbrown_agents-mcp-rl-lesson2.md
  - raw/articles/2025-06-24_willbrown_agents-mcp-rl-lesson3.md
  - raw/articles/2025-06-26_willbrown_agents-mcp-rl-lesson4.md
  - raw/articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours.md
  - raw/articles/2026-06-10_semianalysis_scaling-rl-environments-reward-hacking.md
  - raw/articles/2024-10-11_corbt_founders-guide-to-fine-tuning.md
  - raw/articles/2024-10-28_corbt_hacker-news-rlhf-part1.md
  - raw/articles/2024-12-30_corbt_openai-reinforcement-fine-tuning.md
  - raw/articles/2025-01-14_corbt_deterministic-vs-freeform-tasks.md
  - https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
  - https://maven.com/p/193c6f/build-your-own-ai-research-agent
  - https://maven.com/p/c3950c/training-agents-with-reinforcement-learning
  - https://newsletter.semianalysis.com/p/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data
---

# Production-Ready Agent Engineering: From MCP to RL

A live, cohort-based training course on **[Maven](https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl)** taught by [[entities/will-brown]] (Research Lead, [[entities/prime-intellect]]) and [[concepts/corbett-kyle-corbitt|Kyle Corbitt]] (CTO, OpenPipe). Covers the full stack of production agent engineering — from tool design via Model Context Protocol to reinforcement learning optimization with GRPO.

**Schedule:** June 17 – July 2025 (2x weekly lectures)
**Time Commitment:** 4–6 hours/week | **Price:** $1,400

## Course Overview

The course bridges the gap between agent prototyping and production-ready agent systems. It covers three major pillars:

1. **Agent Design & Tool Integration** — Modern LLM agent patterns, MCP-based tool building, and research agent implementation
2. **Evaluation & Feedback** — Formulating evaluation metrics that enable learning from reward feedback
3. **RL Optimization** — Applying reinforcement learning (GRPO and related algorithms) to train agents that outperform frontier models on specific tasks

### Learning Objectives

| # | Topic | Description |
|---|-------|-------------|
| 1 | Agent Design Patterns | Choose the right approach for your use case from modern LLM agent architectures |
| 2 | MCP Tool Building | Build portable, reliable tools for agents using Model Context Protocol |
| 3 | Research Agents | Implement research agents with custom format instructions and data access |
| 4 | RL Fundamentals | Understand how reinforcement learning applies to LLM agents |
| 5 | Agentic RL Formulation | Frame agentic tasks as RL problems with proper evaluation metrics |
| 6 | GRPO Training | Use Group-Relative Policy Optimization to train task-specific agents |
| 7 | Holistic Integration | Design production-ready agents end-to-end with RL optimization |

## Instructors

### Will Brown
Research Lead at [[entities/prime-intellect]], leading open-source agentic RL research. Creator of the [verifiers](https://github.com/PrimeIntellect-ai/verifiers) library (~4,000 stars) and the viral GRPO demo gist (1,200+ stars). PhD in Computer Science from Columbia University (multi-agent learning, advisors: Christos Papadimitriou, Tim Roughgarden). Previously ML Researcher at Morgan Stanley and Applied Scientist at AWS. See [[entities/will-brown]] for full profile.

### Kyle Corbitt
CTO of **OpenPipe**, the RL post-training company that helps companies train custom models optimized for their specific tasks. Previous ML experience at Y Combinator and Google. See [[concepts/corbett-kyle-corbitt]] for details.

## Companion Resources

| Resource | Description |
|----------|-------------|
| [ai-agent-engineering](https://github.com/willccbb/ai-agent-engineering) | Course files (71+ stars) |
| [research-agent-lesson](https://github.com/willccbb/research-agent-lesson) | "Build Your Own AI Research Agent" lesson files |
| [prod_agents.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lectures-1-through-4/lec2-prod-agents/prod_agents.ipynb) | Lesson 2 notebook: production-grade agent patterns |
| [evals_optimization.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lectures-1-through-4/lec3-evals-optimization/evals_optimization.ipynb) | Lesson 3 notebook: evals, SFT, and GRPO |
| [grpo_intro.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec4-rl/grpo_intro.ipynb) | Lesson 4 notebook: multi-armed bandit + GRPO batch demo |
| [verifiers](https://github.com/PrimeIntellect-ai/verifiers) | RL environment library for training and evaluating LLMs |
| [mcp-client-server](https://github.com/willccbb/mcp-client-server) | MCP Server that's also an MCP Client |

## Lightning Lessons (Pre-Course Workshops)

Free, standalone workshops offered before the main course cohort begins. Each focuses on a single topic and can be watched independently.

| Date | Lightning Lesson | Resources |
|------|-----------------|-----------|
| Jun 10 | [[raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning\|Build Your Own AI Research Agent]] (Will Brown) | [[transcripts/2025-06-10_willbrown_build-your-own-research-agent-notebook\|Notebook]] · [GitHub](https://github.com/willccbb/agent-engineering/blob/main/lightning-lessons/agents.ipynb) · [Maven](https://maven.com/p/193c6f/build-your-own-ai-research-agent) |
| Jun 10 | [[raw/articles/2025-06-10_willbrown_training-agents-with-rl-lightning\|Training Agents with Reinforcement Learning]] (Will Brown) | [[transcripts/2025-06-10_willbrown_training-agents-with-rl-notebook\|Notebook]] · [GitHub](https://github.com/willccbb/agent-engineering/blob/main/lightning-lessons/search.ipynb) · [Maven](https://maven.com/p/c3950c/training-agents-with-reinforcement-learning) |

### Lightning Lesson 1: Build Your Own AI Research Agent

A ~75-minute workshop building a deep research agent from scratch. Covers:
- Agent definitions (LLM + tool calls in a while loop)
- V1 agent: regex-based XML parsing with search/fetch tools
- V2 agent: sub-models as tools (helper models for bulk reading)
- MCP crash course: client/server architecture, standardized tool interface
- Deep research via Claude Code with MCP servers
- Evaluating agent output and connecting to RL reward signals

**Key takeaway:** Agents and RL are two sides of the same coin. Building agents from scratch (without frameworks) teaches the core loop that RL optimizes.

### Lightning Lesson 2: Training Agents with Reinforcement Learning

A ~65-minute workshop bridging agent building and RL training. Builds a **Wikipedia search agent** end-to-end:
- Local search tools (ChromaDB + embeddings) for deterministic evaluation
- Synthetic QA dataset generation (trivia-style, GPT-4.1 Mini)
- Baseline evaluation with LLM judges via [verifiers](https://github.com/PrimeIntellect-ai/verifiers)
- Live GRPO training — group-relative advantage computation, no critic model needed
- Case study: Wordle-playing agent

**Key takeaway:** RL gives you tools for actually improving agent models to be performant and cost-effective without relying on closed-source APIs. GRPO is sample-efficient — training takes hours, not days.

## Lecture Schedule

The course runs 3 weeks with 6 lectures (Tuesdays & Thursdays). Lecture transcripts will be added as they become available.

| Date | Lecture | Transcript |
|------|---------|------------|
| Jun 17 | [[transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture\|Lesson 1: Agent Patterns & Principles]] | [[raw/articles/2025-06-17_willbrown_agents-mcp-rl-lesson1\|Summary]] |
| Jun 19 | [[transcripts/2025-06-19_willbrown_agents-mcp-rl-lesson2-lecture\|Lesson 2: MCP + Production-Grade Agents]] | [[raw/articles/2025-06-19_willbrown_agents-mcp-rl-lesson2\|Summary]] · [[raw/articles/2025-06-21_willbrown_agents-mcp-rl-lesson2-repeat\|Repeat]] |
| Jun 21 | [[raw/articles/2025-06-21_willbrown_agents-mcp-rl-office-hours-week1\|Office Hours (Week 1)]] | *Q&A transcript* |
| Jun 24 | [[transcripts/2025-06-24_willbrown_agents-mcp-rl-lesson3-lecture\|Lesson 3: Agent Evals and Optimization]] | [[raw/articles/2025-06-24_willbrown_agents-mcp-rl-lesson3\|Summary]] |
| Jun 26 | [[transcripts/2025-06-26_willbrown_agents-mcp-rl-lesson4-lecture\|Lesson 4: Introduction to Reinforcement Learning]] | [[raw/articles/2025-06-26_willbrown_agents-mcp-rl-lesson4\|Summary]] |
| Jun 27 | [[transcripts/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours|Office Hours with Kyle Corbitt]] | [[raw/articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours|Summary]] |
| TBD | Lecture 5 | *pending* |
| TBD | Lecture 6 | *pending* |

## Lesson Summaries

### Lesson 1: Agent Patterns & Principles (Jun 17)

Inaugural lecture establishing the central thesis: RL and agents are two sides of the same coin. Covers model ecosystem (DeepSeek V3, GPT 4.1, Claude Sonnet, Gemini 2.5 Pro), tool calling patterns, structured outputs via Pydantic, and multi-turn state management. Key insight: prioritize tool-use reliability over raw intelligence.

**Transcript:** [[transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture]] · **Summary:** [[raw/articles/2025-06-17_willbrown_agents-mcp-rl-lesson1]]

### Lesson 2: MCP + Production-Grade Agents (Jun 19)

Bridges prototyping to production. Covers type hints as defense against silent LM output bugs, async processing (`asyncio.gather` + semaphores for ~7-8x speedup), agentic RAG vs prefetch RAG, MCP architecture ("FastAPI but LM-shaped"), logging frameworks (Logfire, Weave, MLflow, Arize), security (sandboxing, codifying patterns as tools), and the N×M→N+M problem MCP solves. Strong stance: A2A is premature, MCP is the standard to build on. Repeat session added: reward hacking, read-only defaults, GRPO/KL penalty details, entropy collapse, structured generation during training, agent evaluation deep dive.

**Transcript:** [[transcripts/2025-06-19_willbrown_agents-mcp-rl-lesson2-lecture]] · **Summary:** [[raw/articles/2025-06-19_willbrown_agents-mcp-rl-lesson2]] · **Repeat:** [[raw/articles/2025-06-21_willbrown_agents-mcp-rl-lesson2-repeat]] · **Notebook:** [prod_agents.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lectures-1-through-4/lec2-prod-agents/prod_agents.ipynb)

### Lesson 3: Agent Evals and Optimization (Jun 24)

The third lecture focuses on **evaluation methodology** as the foundation for RL optimization. Covers the benchmark landscape (Artificial Analysis, BFCL v3, TAO Bench), **model spec** as the starting point for eval design, deterministic evals (format parsing, instruction following via IFEval, set-product test generation), LM judges (calibration across models, pairwise comparison with position bias randomization, confidence intervals), **supervised fine-tuning** (TRL/Axolotl/Unsloth/Torchtune, LoRA vs full fine-tuning, curriculum learning by difficulty sorting), and a deep dive into **GRPO** mechanics (reference models, KL divergence penalty in token space, on-policy vs off-policy tradeoffs, online reference model updates).

**Key insight:** SFT is the gateway to RL — it validates that your task is learnable before expensive RL runs. Write a model spec before writing evals; use deterministic evals first (format, tool calls, instruction following); calibrate LM judges by comparing multiple models; for GRPO, start slow and safe with online reference updates.

**Transcript:** [[transcripts/2025-06-24_willbrown_agents-mcp-rl-lesson3-lecture]] · **Summary:** [[raw/articles/2025-06-24_willbrown_agents-mcp-rl-lesson3]] · **Notebook:** [evals_optimization.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec3-evals-optimization/evals_optimization.ipynb)

### Lesson 4: Introduction to Reinforcement Learning (Jun 26)

Bridges RL theory and LLM agent training. Will Brown delivers a crash course on RL fundamentals — MDPs, policy gradient, advantage estimation — through a **multi-armed bandit demonstration** (100-action single-turn game), then maps these concepts directly to LLM token generation (state = context, action = next token, policy = next-token distribution). Introduces GRPO mechanics: group = multiple rollouts per prompt, advantage = reward normalized within group. Kyle Corbitt follows with a live-coding session building **Art E** — an agentic RAG email search agent using SQLite + FTS5, demonstrating tool design patterns (wrapper functions), agent loop architecture, synthetic QA data generation, and benchmarking methodology. Key result: agentic keyword search significantly outperforms vector RAG. Sets up GRPO training for the next lesson.

**Key insight:** RL is finicky — small changes in learning rate/batch size cause dramatically different outcomes. The LLM-as-policy mapping is natural but requires careful tool design as a foundation before RL can converge.

**Transcript:** [[transcripts/2025-06-26_willbrown_agents-mcp-rl-lesson4-lecture]] · **Summary:** [[raw/articles/2025-06-26_willbrown_agents-mcp-rl-lesson4]] · **Notebook:** [grpo_intro.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec4-rl/grpo_intro.ipynb)

### Office Hours with Kyle Corbitt (Jun 27)

Unscripted Q&A session. Deep dives on: reward hacking mitigation (iterative process, LM judge patching, checkpoint rollback), RLHF workflow for low-volume human feedback (sales quoting agent use case), custom reward model training (HN title predictor — Llama 3.1 8B, log-score prediction, Liger Kernel), RL vs prompt engineering decision criteria, agent framework tradeoffs, jailbreaking via SFT (~10 examples usually sufficient).

**Key insight:** "Much more bullish on not needing to do any of this stuff" — ungrounded LM judges work well as reward models for many tasks. For human feedback, start with context extraction before thinking about RL.

**Transcript:** [[transcripts/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours]] · **Summary:** [[raw/articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours]]

## Included Credits

- $100 in Prime Intellect GPU credits
- $100 in OpenPipe finetuning credits
- 1 year of Weights & Biases Pro

## Ecosystem Context

This course is not just educational content — it is a **strategic onboarding path** into the emerging RL-for-agents ecosystem built around two key platforms:

### Prime Intellect ↔ Verifiers
[[entities/prime-intellect]] provides open-source RL infrastructure for LLMs. The [verifiers](https://github.com/PrimeIntellect-ai/verifiers) library (~4,000 stars) is the core building block — it defines modular RL environments for training and evaluating agents. Will Brown created verifiers and leads its development. The course teaches the **background knowledge needed to use verifiers effectively**: environment construction, reward shaping, GRPO training loops, and multi-turn agent evaluation. Students receive $100 in Prime Intellect GPU credits to practice with real infrastructure.

### OpenPipe ↔ RL Post-Training
**OpenPipe** (Kyle Corbitt, CTO) provides RL post-training as a service — companies bring their tasks, and OpenPipe trains custom models that outperform frontier APIs on those specific workloads. The course teaches the **evaluation and reward engineering fundamentals** that OpenPipe's customers need to formulate their tasks as RL problems. Students receive $100 in OpenPipe finetuning credits.

### Weights & Biases ↔ Experiment Tracking
W&B Pro (1-year included) provides the **observability layer** — tracking RL training runs, comparing reward curves, and debugging agent behavior. The course integrates W&B as the standard experiment tracking tool.

### The RL-Harness Lifecycle
This course embodies the [[concepts/rl-harness-lifecycle]] thesis: strong agents emerge from a co-evolutionary cycle between harness engineering and RL training. The course teaches both sides — MCP tool design (harness) and GRPO optimization (RL) — as complementary skills, not separate disciplines.

### Connection to the Broader Ecosystem
- [[concepts/agentic-search]] — Search-as-agent paradigm (related course: [Cheat at Search](https://maven.com/softwaredoug/cheatatsearch))
- [[concepts/grpo-rl-training]] — The specific RL algorithm taught in this course
- [[concepts/agent-evaluation]] — Evaluation methodology for RL reward signals
- [[concepts/context-engineering]] — Agent context design patterns (MCP, tool schemas)

## Key Concepts Covered

- [[concepts/agentic-rl]] — Applying RL to train LLM agents
- [[concepts/grpo-rl-training]] — Group Relative Policy Optimization
- [[concepts/mcp]] — Model Context Protocol for tool integration
- [[concepts/agent-evaluation]] — Evaluating agent performance for RL reward signals
- [[concepts/context-engineering]] — Designing effective agent contexts
- [[concepts/reasoning-models]] — Models with extended reasoning capabilities

## Comparison with Similar Courses

| Course | Platform | Focus | Price |
|--------|----------|-------|-------|
| **This course** | Maven | Agent engineering + RL optimization | $1,400 |
| [Cheat at Search](https://maven.com/softwaredoug/cheatatsearch) | Maven | Search with LLMs and agents | $1,300 |
| [GenAI Handbook](https://genai-handbook.github.io/) | Self-paced | Broad generative AI learning roadmap | Free |

## Related

- [[entities/will-brown]] — Primary instructor
- [[concepts/corbett-kyle-corbitt]] — Co-instructor
- [[entities/prime-intellect]] — Will Brown's organization (verifiers, PRIME-RL)
- [[raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning]] — Lightning Lesson 1: Build Your Own AI Research Agent
- [[transcripts/2025-06-10_willbrown_build-your-own-research-agent-notebook]] — Lightning Lesson 1 notebook walkthrough
- [[raw/articles/2025-06-10_willbrown_training-agents-with-rl-lightning]] — Lightning Lesson 2: Training Agents with RL
- [[transcripts/2025-06-10_willbrown_training-agents-with-rl-notebook]] — Lightning Lesson 2 notebook walkthrough
- [[raw/articles/2025-06-19_willbrown_agents-mcp-rl-lesson2]] — Lesson 2: MCP + Production-Grade Agents
- [[transcripts/2025-06-19_willbrown_agents-mcp-rl-lesson2-lecture]] — Lesson 2 transcript
- [[raw/articles/2025-06-24_willbrown_agents-mcp-rl-lesson3]] — Lesson 3: Agent Evals and Optimization
- [[transcripts/2025-06-24_willbrown_agents-mcp-rl-lesson3-lecture]] — Lesson 3 transcript
- [[raw/articles/2025-06-26_willbrown_agents-mcp-rl-lesson4]] — Lesson 4: Introduction to Reinforcement Learning
- [[transcripts/2025-06-26_willbrown_agents-mcp-rl-lesson4-lecture]] — Lesson 4 transcript
- [[raw/articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours]] — Office Hours with Kyle Corbitt
- [[transcripts/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours]] — Office Hours transcript
- [[concepts/grpo-rl-training]] — Key RL algorithm taught in the course
- [[concepts/rl-harness-lifecycle]] — Brown's framework for agent-RL co-evolution
- [[concepts/agentic-search]] — Related: agentic retrieval patterns (see also [Cheat at Search](https://maven.com/softwaredoug/cheatatsearch))

## Supplementary Reading

### Semi Analysis: Scaling Reinforcement Learning (June 2026)

Dylan Patel's comprehensive report on RL infrastructure bottlenecks complements this course's curriculum with industry-scale context:

- **GRPO mechanics**: Detailed explanation of rollout-based RL, confirming the course's GRPO coverage from an infrastructure perspective
- **Reward function design ("dark art")**: AlphaChip case study (6.2% wirelength reduction on TPUv6) illustrating how even simple reward functions require extensive experimentation — directly relevant to the course's evaluation and reward engineering modules
- **Reward hacking as first-order bottleneck**: Claude 3.7 test-editing, o3 hallucinations, GPT-4o sycophancy — all traced to reward function design failures
- **Non-verifiable domains**: LLM judges with rubrics (OpenAI deliberative alignment, Qwen-3, HealthBench) — the frontier the course's RL optimization modules aim toward
- **Environment engineering**: Latency, fault tolerance, security, CPU vs GPU servers, computer use challenges — the infrastructure layer the course's MCP/harness design feeds into
- **RL shifts hardware balance**: NVL72 for batched reasoning, Prime Intellect Intellect-2 for distributed RL, decentralized inference for RL pipelines
- **Data as moat**: Quality > quantity for RL data; OpenAI RFT for enterprise customization; STEM PhDs recruited for rubric writing
- **Recursive self-improvement**: Already happening via compiler/kernel optimization RL; Claude 4 system card evaluations

See [[concepts/reward-hacking]] for the expanded reward hacking taxonomy including Semi Analysis examples.

**Source:** [Scaling RL: Environments, Reward Hacking, Agents, Scaling Data](https://newsletter.semianalysis.com/p/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data) (paywall — preview covers ~80% of content)

### Kyle Corbitt Blog Series: ART開発前の知的背景 (2024-10 ~ 2025-01)

Kyle Corbitt が OpenPipe/ART 開発前〜開発中にかけて発信したブログシリーズ。Fine-tuning → RLHF → RFT → タスク分類という思考の進化過程が見える。

- **[A Founder's Guide to AI Fine-Tuning](https://corbt.com/posts/a-founder-s-guide-to-ai-fine-tuning)** (2024-10-11) — Fine-tuning の意思決定フレームワーク。何时 fine-tuning すべきか（prompt engineering / few-shot / RAG を尽くしてから）、データ準備（品質 > 量、代表性、一貫性、重複排除）、学習プロセス（小規模開始、テストセット確保、データイテレーション）、よくある失敗（過学習、データ汚染、評価 neglect、時期尚早な fine-tuning）。[[raw/articles/2024-10-11_corbt_founders-guide-to-fine-tuning]]
- **[RLHF Part 1: Hacker News Ranking](https://corbt.com/posts/hacker-news-rlhf-part-1)** (2024-10-28) — HN コンテンツランキングに RLHF を適用した実践例。Prompt engineering → 特徴量追加 → RLHF パイプライン（500 件のペアワイズ比較、Bradley-Terry loss の報酬モデル、78% 精度）。CTR が 25% → 60% に改善。**教訓:** LLM は特徴量抽出器としては優秀だがランカーとしては不十分、少量の preference データで大きく改善、特徴量エンジニアリング > モデルアーキテクチャ。[[raw/articles/2024-10-28_corbt_hacker-news-rlhf-part1]]
- **[Analyzing OpenAI's RFT](https://corbt.com/posts/openai-rft)** (2024-12-30) — OpenAI の Reinforcement Fine-Tuning (RFT) の技術解説。検証可能な出力を持つタスク向け、PPO + partial credit の grading function（dense reward）、少数データ（数十件）で学習可能。RFT 適用条件: タスクが難しい、出力が検証容易、ラベルデータが少ない。RFT → SFT への蒸留パイプライン（50件 RFT → 20K SFT → 5M 推論）。**Open-source RFT の QwQ 向け実装も進行中。** [[raw/articles/2024-12-30_corbt_openai-reinforcement-fine-tuning]]
- **[Deterministic vs Freeform Tasks](https://corbt.com/posts/deterministic-vs-freeform-tasks)** (2025-01-14) — タスクを deterministic（正解一意: 分類、情報抽出）と freeform（正解複数: 要約、チャット）に分類するフレームワーク。OpenPipe データセット分析: 63% freeform / 37% deterministic（使用量上位では逆転）。**温度:** deterministic=0、freeform=0.7-1.0。**評価:** deterministic は golden dataset、freeform は vibe check / LLM-as-judge / user feedback。**Fine-tuning:** deterministic → RFT + 小モデル蒸留、freeform → DPO / RLHF。**この分類は course の evaluation 講義の理論的基盤。** [[raw/articles/2025-01-14_corbt_deterministic-vs-freeform-tasks]]
