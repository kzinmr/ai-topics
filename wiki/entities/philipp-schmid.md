---
title: Philipp Schmid
handle: "@_philschmid"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ai
  - huggingface
  - google-deepmind
  - deployment
  - llm-ops
  - fine-tuning
  - agent-harnesses
  - mcp
  - gemini
---


# Philipp Schmid (@_philschmid)

| | |
|---|---|
| **X** | [@_philschmid](https://x.com/_philschmid) |
| **Blog** | [philschmid.de](https://www.philschmid.de) |
| **GitHub** | [philschmid](https://github.com/philschmid) |
| **Role** | Senior AI Developer Experience Engineer @ Google DeepMind; prev: Tech Lead @ Hugging Face; AWS ML Hero |
| **Known for** | Hugging Face deployment guides, LLM fine-tuning tutorials, agent harness architecture, MCP server best practices, Gemini developer documentation |
| **Bio** | AI developer experience engineer at Google DeepMind, where he is building the first AI DevRel team to bring Google DeepMind's AI research to every developer. Previously served as Technical Lead at Hugging Face, helping grow revenue from $0 to ~$100M in 4 years through cloud and hardware partnerships. Recognized as the first German AWS Machine Learning Hero (2021). Prolific technical writer and educator with hundreds of blog posts and tutorials. |

## Overview

Philipp Schmid is one of the most prolific and influential technical educators in the AI ecosystem. His blog at philschmid.de has been a go-to resource for developers since 2021, covering everything from BERT optimization to the latest in LLM deployment, fine-tuning, and agent engineering. With over 150,000 followers on LinkedIn and a substantial presence across X, GitHub, and the developer community, Schmid has established himself as the definitive voice on practical AI engineering.

At **Hugging Face**, Schmid served as Technical Lead for strategic cloud and hardware partnerships, working with AWS, Google Cloud, Azure, Cloudflare, DigitalOcean, and Dell. He was instrumental in creating **Hugging Face Inference Endpoints** — a user-friendly, production-ready solution for deploying machine learning models as APIs. His work helped bridge the gap between cutting-edge research and practical deployment, making models like Falcon, LLaMA, StarCoder, and BLOOM accessible to developers worldwide. He frequently shared optimization techniques like Q-LoRA, speculative decoding with Medusa, and AWQ quantization that dramatically reduced inference costs.

In early 2025, Schmid joined **Google DeepMind** as a Senior AI Developer Experience Engineer, where he is building the first AI DevRel team. His mission: "Enable every developer to build with AI in a responsible, ethical and successful way." He works alongside notable colleagues including Mat Velloso, Paige Bailey, Logan Kilpatrick, and Omar Sanseviero. At DeepMind, he has been deeply involved in **Gemini** developer documentation, the **Gemma** open model family guides, and the emerging agent ecosystem including the Gemini Interactions API and MCP (Model Context Protocol) servers.

Schmid's GitHub presence is equally impressive — with 3,700+ followers and 247 public repositories, his projects include:
- **deep-learning-pytorch-huggingface** (1.4k stars) — Comprehensive deep learning tutorials
- **gemini-samples** (1.4k stars) — Practical Gemini API examples
- **clipper.js** (617 stars) — HTML to Markdown converter and crawler
- **easyllm** (474 stars) — Simplified LLM integration library
- **huggingface-sagemaker-workshop-series** (242 stars) — Enterprise-scale NLP workshops

## Core Ideas

### 2026: The Year of Agent Harnesses

Schmid's most influential framing of 2026 centers on **Agent Harnesses**:

> *"If 2025 was the beginning of agents, 2026 will be around Agent Harnesses. An Agent Harness is the infrastructure that wraps around an AI model to manage long-running tasks. It is not the agent itself. It operates at a higher level than agent frameworks."*

He argues that harnesses provide three critical functions:
1. **Validating Real-World Progress** — Allowing users to easily test and verify agent behavior
2. **Creating Feedback Loops** — Shared, stable environments where improvements compound over time
3. **Building Durability** — Systems that get more reliable over time instead of more brittle

> *"Harnesses often act as the set of opinions that turns a model into a product."*

This framing directly parallels work by [[varun-trivedy]] (DeepAgents harness engineering) and [[thariq-shihipar]] (Claude Agent SDK architecture), establishing a consensus view across the AI engineering community.

### MCP Server Best Practices

In "MCP is Not the Problem, It's your Server: Best Practices for Building MCP Servers" (Jan 2026), Schmid delivered one of the most practical guides on Model Context Protocol implementation:

- MCP servers are often poorly designed, not the protocol itself
- Key patterns for reliable tool discovery, execution, and error handling
- The importance of idempotent operations and proper authentication
- How to design servers that gracefully handle model hallucination and tool misuse

This post reflected Schmid's signature approach: take an emerging technology, identify the common pitfalls, and provide concrete, actionable guidance.

### Fine-Tuning in the Age of Prompting

Schmid's 2025 guide "How to fine-tune open LLMs in 2025 with Hugging Face" became one of the most referenced resources on practical model customization:

> *"Fine-tuning still matters for specialized use cases despite better models — especially for consistency, domain expertise, controlling output style, or reducing costs."*

Key techniques covered:
- **Q-LoRA** for efficient 4-bit training
- **Spectrum method** for selective layer fine-tuning
- **Flash Attention and Liger Kernels** for training speedups
- **DeepSpeed and accelerate** for multi-GPU scaling
- Evaluation harnesses for testing fine-tuned models

### Deployment Optimization Philosophy

Throughout his work, Schmid emphasizes a consistent philosophy:

> *"Reduce cost, accelerate performance, and maintain quality — you can achieve all three with the right optimization stack."*

His notable optimization achievements:
- **Mixtral 8x7B + Medusa + AWQ**: 3x cost reduction on SageMaker (g5.12xlarge with 4×A10G instead of g5.48xlarge) with up to 2x speed increase
- **BERT on Inferentia2**: Significant latency improvements through ONNX conversion and static quantization
- **Falcon 40B on Inference Endpoints**: Production-ready deployment with SOC2 Type 2 compliance

### Distillation and Model Size

Schmid is a strong advocate for **knowledge distillation** as the practical path to deployable AI:

> *"You take a giant teacher model and train a smaller student model to mimic it. Same brainpower for your use case, but in a body you can actually deploy."*

He argues that without distillation, most teams end up running demos rather than production systems. With it, models become small enough for single-GPU or edge deployment with real-time inference.

## Key Work

### Hugging Face Inference Endpoints

Schmid was the technical lead for this product, which democratized LLM deployment:
- User-friendly interface for deploying any Hugging Face model as a production API
- Support for Falcon 40B, LLaMA, X-Gen, StarCoder, RedPajama, and hundreds more
- SOC2 Type 2 compliance and Business Associate Agreements for healthcare
- Automatic scaling and cost optimization
- Integration with AWS, GCP, Azure, and other cloud providers

### Google DeepMind AI DevRel Team

Since joining in 2025, Schmid has been central to:
- **Gemini API developer skills** — A "Gemini API developer skill" that provides agents with live documentation, boosting success rates from 28.2% to 96.6%
- **Gemini 3 developer guides** — Comprehensive documentation for the latest Gemini model family
- **Gemma 3 introduction** — Developer guide for Google's open model family
- **Agent framework collaborations** — Working with ADK, Agno, Browser Use, Eigent, Letta, and mem0
- **Closing the knowledge gap** — Bridging static model knowledge with rapidly evolving software practices

### Blog and Technical Writing

Schmid's blog has been continuously updated since 2021 with hundreds of posts covering:
- LLM deployment and optimization
- Fine-tuning methodologies
- Agent architecture and harnesses
- Cloud infrastructure for AI
- Open model ecosystem analysis

### Open Source Contributions

| Repository | Stars | Description |
|------------|-------|-------------|
| deep-learning-pytorch-huggingface | 1,364 | Comprehensive deep learning tutorials with PyTorch and Hugging Face |
| gemini-samples | 1,361 | Practical Gemini API examples and guides |
| clipper.js | 617 | HTML to Markdown converter and web crawler |
| easyllm | 474 | Simplified LLM integration library |
| document-ai-transformers | 394 | Document AI with Hugging Face Transformers |
| huggingface-sagemaker-workshop-series | 242 | Enterprise-scale NLP workshop materials |

### AWS ML Hero Recognition

Schmid was recognized as the **first German AWS Machine Learning Hero** in 2021, acknowledging his contributions to making ML accessible on AWS through:
- SageMaker integration tutorials
- Inferentia and Trainium optimization guides
- Cost-effective deployment strategies using Spot Instances
- Multi-container endpoint architectures

## Blog / Recent Posts

| Date | Title | Summary |
|------|-------|---------|
| 2026-03-28 | How Kimi, Cursor, and Chroma Train Agentic Models with RL | Analysis of how leading AI companies use RL for agent training |
| 2026-03-24 | Combine Built-in Tools and Function Calling in Gemini Interactions API | Guide to tool integration in Google's agent framework |
| 2026-03-16 | Developer Guide: Nano Banana 2 with Gemini Interactions API | Practical deployment guide for multimodal models |
| 2026-03-10 | How Autoresearch will change Small Language Models adoption | Impact of automated research on SLM ecosystems |
| 2026-03-04 | Practical Guide to Evaluating and Testing Agent Skills | Comprehensive evaluation framework for agent capabilities |
| 2026-02-24 | Writing a Good AGENTS.md | Best practices for agent context files |
| 2026-02-20 | Agents: Inner Loop vs Outer Loop | Architecture patterns for agentic systems |
| 2026-02-17 | Can We Close the Loop in 2026? | Predictions on agent feedback loop maturity |
| 2026-02-13 | Multimodal Function Calling with Gemini 3 and Interactions API | Guide to multimodal agent development |
| 2026-02-01 | The Agent Client Protocol Overview | Framework for agent-client communication |
| 2026-01-21 | MCP is Not the Problem, It's your Server | Best practices for building reliable MCP servers |
| 2025-12 | How to fine-tune open LLMs in 2025 with Hugging Face | Comprehensive guide covering Q-LoRA, Spectrum, Flash Attention, DeepSpeed |

## Related People

- **[[varun-trivedy]]** — Both work on agent harness engineering; Schmid's "2026 will be around Agent Harnesses" framing aligns with Trivedy's DeepAgents work
- **[[thariq-shihipar]]** — Both contribute to the Claude Agent SDK ecosystem; complementary perspectives on harness design and agent architecture
- **[[florian-brand]]** — Both focus on open model deployment and evaluation; Brand on benchmark analysis, Schmid on deployment optimization
- **[[logan-kilpatrick]]**, **[[omar-sanseviero]]**, **[[paige-bailey]]**, **[[mat-velloso]]** — Colleagues on the Google DeepMind AI DevRel team
- **[[nathan-lambert]]** — Both active in the open model ecosystem; Lambert at Ai2, Schmid at DeepMind

## X Activity Themes

Schmid's X activity (@_philschmid) typically covers:

1. **Agent harness architecture** — Deep analysis of how infrastructure around models determines real-world performance
2. **Deployment optimization** — Practical guides on reducing costs, improving latency, and scaling LLM inference
3. **Fine-tuning techniques** — Q-LoRA, distillation, Spectrum methods, and when fine-tuning beats prompting
4. **Gemini and Google AI ecosystem** — Updates on Gemini API, Interactions API, Gemma models, and developer tools
5. **MCP server design** — Best practices for building reliable, production-grade Model Context Protocol servers
6. **Developer education** — Tutorials, guides, and workshop materials for the broader AI development community
7. **Industry commentary** — Thoughts on the shift from model-centric to infrastructure-centric AI development, the economics of AI deployment
