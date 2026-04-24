---
title: "Vivek 'Varun' Trivedy (@vtrivedy10)"
type: entity
handle: "@vtrivedy10"
created: 2026-04-14
updated: 2026-04-14
tags: [person, langchain, harness-engineering, ai-agents, deep-agents]
aliases: ["vtrivedy10", "Vivek Trivedy", "Varun Trivedy"]
sources: []
---

# Vivek 'Varun' Trivedy (@vtrivedy10)

| | |
|---|---|
| **X** | [@vtrivedy10](https://x.com/vtrivedy10) |
| **Blog** | [vtrivedy.com](https://www.vtrivedy.com/) |
| **GitHub** | [vtrivedy](https://github.com/vtrivedy) |
| **LinkedIn** | [Vivek Trivedy](https://linkedin.com/in/vivek-trivedy-433509134) |
| **Role** | Product Lead, Agents & Harnesses @ LangChain |
| **Known for** | Deep Agents CLI, Harness Engineering, Agent Architecture |
| **Bio** | Researcher and engineer leading open-source agent development at LangChain. PhD in CS from Temple University. Focuses on the intersection of model intelligence and system design. |

## Overview

Vivek Trivedy (also known as Varun Trivedy or Viv) is the Product Lead for Agents & Harnesses at **LangChain**. He is a leading voice in the emerging field of **Harness Engineering** — the discipline of designing systems, tooling, and execution environments that surround Large Language Models to turn raw intelligence into reliable, autonomous agents.

Trivedy is the primary architect behind **Deep Agents**, LangChain's open-source (MIT), model-agnostic coding agent CLI. His work demonstrates that significant performance gains in agentic coding can be achieved by optimizing the harness (context management, self-verification loops, middleware) rather than just swapping the underlying model.

Prior to LangChain, he was a Senior Health AI Scientist at **AWS** and is completing his PhD in Computer Science at **Temple University**, where his research focused on computer vision and representation learning under Prof. Longin Jan Latecki.

## Core Ideas

### Harness Engineering
> *"Agent = Model + Harness. If you're not the model, you're the harness."*

Trivedy argues that a raw LLM is not an agent; it becomes one only when a harness provides state, tool execution, feedback loops, and enforceable logic. Harness Engineering is about systems — building tooling around the model to optimize for task performance, token efficiency, and latency.

Key components of a harness include:
*   **System Prompts & Tools:** MCPs, skills, and their descriptions.
*   **Bundled Infrastructure:** Filesystem, sandbox, browser, and shell access.
*   **Orchestration Logic:** Sub-agent spawning, handoffs, model routing.
*   **Hooks/Middleware:** Deterministic execution patterns like compaction, continuation, and lint checks.

### The "Reasoning Sandwich" & Compute Allocation
> *"The goal of a harness is to mold the inherently spiky intelligence of a model for tasks we care about."*

In optimizing the Deep Agents CLI for **Terminal Bench 2.0**, Trivedy developed the "reasoning sandwich" heuristic: use maximum reasoning (`xhigh`) for planning and verification, but switch to efficient reasoning (`high`) for implementation steps. This approach reduced timeouts and token burn while boosting scores from 52.8% to 66.5%.

### Self-Verification Loops
> *"Models are biased towards their first plausible solution. Prompt them to aggressively test and verify."*

Trivedy emphasizes that agents naturally want to "early exit" after generating a plausible-looking solution. The harness must force a `Build → Verify → Fix` cycle. The `PreCompletionChecklistMiddleware` intercepts the agent's exit attempt to ensure tests are run and results compared against the task spec.

### Context Engineering & Rot
> *"The more that agents know about their environment, constraints, and evaluation criteria, the better they can autonomously self-direct their work."*

Harnesses must actively manage **Context Rot** (degradation of reasoning as the context window fills) via:
*   **Compaction:** Intelligently summarizing old context.
*   **Tool Call Offloading:** Retaining head/tail tokens of large outputs and dumping the rest to the filesystem.
*   **Progressive Disclosure:** Loading tool front-matter only when needed.

### HaaS (Harness as a Service)
> *"As tasks require more autonomous behavior, the core primitive is shifting from the LLM API to the Harness API."*

Trivedy predicts a future where builders create custom harnesses (like Bolt or Claude Code) and users plug into them to edit further or use as a product. The Claude Code SDK is currently the most mature "batteries-included" way to build and expose usable agents.

## Key Work

### Deep Agents CLI (LangChain)
*   Open-source, model-agnostic terminal-powered coding agent.
*   Built on LangGraph with streaming, persistence, and checkpointing.
*   Scored ~42.5% on Terminal Bench 2.0 with Sonnet 4.5 (on par with Claude Code).
*   **Result:** Jumped from Top 30 to Top 5 on Terminal Bench 2.0 (52.8% → 66.5%) using GPT-5.2-Codex by optimizing the harness only.

### Harbor (Evaluation Framework)
*   Framework for evaluating agents in containerized environments at scale.
*   Orchestrates runs, spins up sandboxes (Daytona), interacts with the agent loop, and runs verification + scoring.
*   Used to run the Terminal Bench 2.0 evaluations for Deep Agents.

### Academic Research (Temple University)
*   PhD work in Computer Vision and Representation Learning.
*   Advisor: Prof. Longin Jan Latecki.
*   Published work on image retrieval with self-supervised divergence minimization.

### AWS Health AI
*   Senior Health AI Scientist at Amazon Web Services.
*   Focus on applying AI/ML to healthcare data and systems.

## Timeline

| Date | Event |
|------|-------|
| 2016–2019 | BS Mathematics & Computer Science, Temple University |
| 2019–2021 | MS Computational Data Science, Temple University |
| 2020 | AWS ML Specialty & Solutions Architect Associate certifications |
| 2021–Present | PhD in CS (AI/ML), Temple University (Latecki Group) |
| Dec 2023 – Jan 2025 | Senior Health AI Scientist, AWS |
| Sep 2025 | Published "The Claude Code SDK and the Birth of HaaS" |
| Oct 2025 | Published "The Modern Planning Agent is Really a Dynamic, Adaptive Workflow Generator" |
| Nov 2025 | Published "Agents Should Be More Opinionated" |
| Dec 2025 | Published "Evaluating Deep Agents CLI on Terminal Bench 2.0" |
| Feb 2026 | Published "Improving Deep Agents with Harness Engineering" |
| Dec 2025 – Present | Product Lead, Agents & Harnesses @ LangChain |
| Mar 2026 | Published "The Anatomy of an Agent Harness" |
| Mar 2026 | LangChain open-sourced Deep Agents (MIT License) |

## Blog / Recent Posts

*   **[The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)** (Mar 10, 2026): Defines what a harness is and derives core components (system prompts, tools, infrastructure, orchestration) by working backwards from desired agent behavior.
*   **[Improving Deep Agents with Harness Engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)** (Feb 17, 2026): How the coding agent went from Top 30 to Top 5 on Terminal Bench 2.0 by changing the harness only.
*   **[Agents Should Be More Opinionated](https://www.vtrivedy.com/posts/agents-should-be-more-opinionated/)** (Nov 25, 2025): The best agent products aren't the most flexible, they're the most opinionated.
*   **[The Claude Code SDK and the Birth of HaaS](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service/)** (Sep 23, 2025): Shift from LLM APIs to Harness APIs for autonomous behavior.
*   **[Evaluating Deep Agents CLI on Terminal Bench 2.0](https://www.langchain.com/blog/evaluating-deepagents-cli-on-terminal-bench-2-0/)** (Dec 5, 2025): Benchmark results establishing Deep Agents as a solid starting point.

## Related People

*   : CEO/Co-founder of LangChain; Deep Agents is a key strategic direction.
*   : Co-author on Deep Agents evaluation and Harness Engineering posts.
*   [[ryan-lopopolo]]: Also discusses Harness Engineering; complementary perspectives on agent systems.
*   [[simon-willison]]: Covers AI engineering and agent tools; often discusses similar themes.
*   : PhD Advisor at Temple University.

## X Activity Themes

*   **Harness Engineering:** Deep dives into system design for agents (middleware, context management).
*   **Agent Reliability:** Posts about evaluation, benchmarking (Terminal Bench), and self-verification.
*   **Open Source AI:** Advocating for open harnesses (Deep Agents) and model-agnosticism.
*   **Developer Tools:** Commentary on the evolution of IDEs, CLIs, and agent workflows.

## Harness, Memory, Context Fragments & the Bitter Lesson (Apr 2026)

Vivの2026年4月の投稿では、Harness Engineeringを**メモリ・検索・コンテキスト管理**の文脈に拡張し、エージェントの長期的進化についてのメンタルモデルを提示している。これは「v30+」と称され、HTML図解を用いて反復的に洗練された思考のダンプである。

### Context Fragments

> *"the context window is a precious artifact. Harnesses make decisions on how to populate, manage, edit, and organize it so agents can do work. Each loaded object can be thought of as a Context Fragment and represents an explicit decision by the user and harness designer of what needs a model needs to do work at any given time."*

Vivはコンテキストウィンドウを単なる「トークンの入れ物」ではなく、**harnessが選択的にロードする「Context Fragment」の集合**として捉える。各フラグメントは、ユーザーとharness設計者の明示的な意思決定を反映している。このアイデアは、@a1zhang（Alex L. Zhang）の[[rlm-recursive-language-models]]で提唱された「externalizing objects + loading into the context window」のパイオニア的仕事に由来する。

### Experiential Memory

> *"agent memory has a massive advantage as it can be accumulated across all agents which are easily forked and duplicated (unlike humans). @dwarkesh_sp does a good talking about this massive benefit of artificial systems"*

エージェントは相互作用ごとに大量のデータ（Traces）を生成する。Vivはこれを**Experiential Memory（経験的記憶）**として扱い、人間とは異なりエージェント間で**共有・フォーク・蓄積**できる点を最大の利点と位置づける。メモリは外部化されたオブジェクトとして扱われ、harnessの役割は「適切なタイミングで適切なデータを蓄積メモリから検索し、コンテキストウィンドウにロードすること」である。

### Search & The Bitter Lesson

> *"As we deploy agents in our world over year timescales, there is going to be a hyper-exponential in the amount of data produced by those agents."*

VivはRich Suttonの[[chatgpt-memory-bitter-lesson]]をエージェントメモリに適用する：

1. **データを所有する** — オープンエコシステムが重要
2. **データを使う** — 検索、蒸留、整理が必須

人間の脳は「経験から文脈的に検索し、意図的な練習で重要なものをメモリに定着させる」ことに優れている。エージェントシステムも同様の能力を持つ必要があるが、現在のインフラ・アルゴリズムはこの新しいデータ・レジームで破綻する可能性がある。

### Open Questions

Vivが提起した未解決の問い：

| 問い | 意味 |
|------|------|
| **Traces → Memory Primitives** | 経験（トレース）をどのように効率的に蒸留し、長期的なメモリプリミティブにするか？ |
| **JIT Search vs Weight Integration** | 検索はjust-in-timeで実行すべきか、モデルの重みに統合すべきか？ |
| **Self-Managing Context** | モデルが自身のコンテキストウィンドウを自己管理するにはどうすればよいか？外部オブジェクトを再帰的に操作する際のエラー率をどう下げるか？ |

### 既存のHarness Engineeringとの接続

この投稿は、Vivが以前に構築したHarness Engineeringフレームワークを**メモリと検索の次元**に拡張するものである：

| 既存の概念 | 今回の拡張 |
|-----------|-----------|
| Harness = Model + システム | Harness = Model + Context Fragment routing + Memory retrieval |
| Context Rot対策（compaction, offloading） | Context Fragments（各ロードオブジェクトは明示的意思決定） |
| 自己検証ループ | 経験的メモリの蒸留・蓄積・共有 |
| Terminal Bench最適化 | Bitter Lesson — compute leveraged search > human-curated knowledge |

## Related People

*   : CEO/Co-founder of LangChain; Deep Agents is a key strategic direction.
*   : Co-author on Deep Agents evaluation and Harness Engineering posts.
*   [[ryan-lopopolo]]: Also discusses Harness Engineering; complementary perspectives on agent systems.
*   [[simon-willison]]: Covers AI engineering and agent tools; often discusses similar themes.
*   : PhD Advisor at Temple University.
*   [[alex-zhang]]: MIT CSAIL PhD, RLM (Recursive Language Models). Context Fragment ideaの源流。
*   [[dwarkesh-patel]]: Agent memoryのフォーク・蓄積可能性についての議論。
*   [[richard-sutton]]: The Bitter Lesson — computation leveraged search > curated knowledge.
