---
title: 'Databricks'
type: entity
created: 2026-04-30
updated: 2026-04-30
tags: [company, platform, data-ai, mlops]
aliases:
  - databricks-inc
  - databricks-engineering
  - databricks-data-intelligence-platform
sources:
  - raw/articles/crawl-2026-04-29-databricks-memory-scaling.md
  - "https://www.databricks.com/company/about-us"
  - "https://www.databricks.com/blog/memory-scaling-ai-agents"
  - "https://www.databricks.com/blog/open-sourcing-unity-catalog"
  - "https://www.databricks.com/blog/introducing-agent-bricks"
  - "https://www.databricks.com/blog/2018/06/05/introducing-mlflow-an-open-source-machine-learning-platform.html"
---

# Databricks

> **Databricks** is the data and AI company, headquartered in San Francisco. Founded in 2013 by the original creators of Apache Spark™, Delta Lake, MLflow, and Unity Catalog, Databricks provides the **Data Intelligence Platform** — a unified, open lakehouse architecture for data engineering, data science, machine learning, and AI. Over 15,000 organizations worldwide (including 60%+ of the Fortune 500) rely on Databricks.

## Company Overview

### Founding & History

Databricks was founded in 2013 by the original creators of Apache Spark: **Matei Zaharia**, **Ali Ghodsi**, **Reynold Xin**, **Ion Stoica**, **Patrick Wendell**, and **Arsalan Tavakoli-Shiraji** — all from the AMPLab at UC Berkeley. The company pioneered the **lakehouse architecture**, combining data lake functionality with data warehouse capabilities on a single unified platform.

| Year | Milestone |
|------|-----------|
| 2013 | Founded by UC Berkeley AMPLab researchers |
| 2014 | Open-sourced Apache Spark |
| 2018 | Announced **MLflow**, open source ML lifecycle platform |
| 2020 | Introduced **Databricks SQL** (formerly SQL Analytics) |
| 2021 | Reached $1B+ annual revenue run rate |
| 2023 | Acquired **MosaicML** for ~$1.3B; launched Lakehouse AI |
| 2024 | Open-sourced **Unity Catalog**; announced Mosaic AI platform |
| 2025 | Launched **Agent Bricks** and **Lakebase** OLTP database |
| 2026 | Published **Memory Scaling** research with **MemAlign** framework |

### Funding & Valuation

Databricks is one of the most valuable private enterprise software companies globally:

- **December 2024:** Raised $10B at a **$62B valuation** from Thrive Capital, Andreessen Horowitz, T. Rowe Price, and others — one of the largest private funding rounds in tech history.

### Scale

- **15,000+** customers globally (Block, Comcast, Condé Nast, Rivian, Shell)
- **60%+** of the Fortune 500 use Databricks
- **1,200+** global cloud, ISV, and consulting partners
- **~7,000** employees

### Strategic Partnerships

- **March 2025:** Five-year partnership with **Anthropic** ($100M deal) — integrating Claude models into the platform
- **June 2025:** Four-year partnership with **Google / Alphabet** to integrate **Gemini** models

---

## Key Contributions to AI

### Apache Spark

The foundational open-source unified analytics engine for large-scale data processing. Databricks was founded by Spark's original creators and continues to be the primary steward and contributor to the project. Spark enables distributed data processing for ML workloads at scale.

### MLflow

**MLflow** is the largest open-source AI engineering platform for agents, LLMs, and ML models. Launched in 2018, it provides:
- Experiment tracking and model registry
- LLM evaluation and tracing (GenAI observability)
- AI Gateway for cost and access management
- Over **30 million monthly downloads**

MLflow is managed by the Linux Foundation and serves as the industry standard for MLOps lifecycle management. Databricks provides a fully managed, enterprise-grade version integrated with Unity Catalog.

### Unity Catalog

**Unity Catalog** is the industry's first open-source unified catalog for data and AI governance. Open-sourced in June 2024 and hosted at **LF AI & Data**, it provides:
- Fine-grained access control across data, models, and AI assets
- Data lineage and versioning
- Format-agnostic governance across clouds and data formats
- Integration with MLflow for model governance

Unity Catalog serves thousands of customers in production and is the backbone of Databricks' governance model.

### Databricks Runtime for ML / AI Runtime

**Databricks Runtime for Machine Learning (MLR)** provides pre-configured, optimized ML environments with popular frameworks (TensorFlow, PyTorch, scikit-learn, XGBoost), AutoML capabilities, and GPU-optimized distributed training via HorovodRunner. In 2025-2026, this evolved into **AI Runtime (AIR)** — a serverless, on-demand GPU compute service with NVIDIA A10/H100 support, RDMA networking, and deep integration with MLflow and Unity Catalog.

### MosaicML Acquisition ($1.3B, 2023)

Databricks acquired **MosaicML** in June 2023 for ~$1.3B, bringing in a leading generative AI platform known for:
- **MPT (Mosaic Pretrained Transformers)** — state-of-the-art open-source LLMs (MPT-7B, MPT-30B)
- Efficient model training with 2-7x speed improvements
- Enterprise-grade LLM fine-tuning and deployment

Post-acquisition, MosaicML's technology formed the foundation of **Mosaic AI** (announced 2024), enabling:
- Custom model training and fine-tuning on customer data
- DBRX foundation model
- AI Vector Search for RAG
- AI Model Serving for deployment and monitoring

### Lakebase

**Lakebase** is a fully managed OLTP database integrated with the Databricks Data Intelligence Platform. Built on serverless PostgreSQL, it supports structured queries, full-text search, and vector similarity — notably serving as the scalable storage pillar for Databricks' memory scaling research.

### Agent Bricks

Launched at the 2025 Data + AI Summit, **Agent Bricks** is a development platform for building, evaluating, and deploying AI agents. Key features:
- Auto-optimized agents using enterprise context (schemas, business rules)
- Multi-agent orchestration with Supervisor Agent pattern
- LLM-as-judge evaluation and human feedback loops
- Integration with MCP servers, Unity Catalog, and MLflow tracing

---

## Recent AI Research & Agent Work

### Memory Scaling for AI Agents (April 2026)

Published on the Databricks Engineering Blog, the **Memory Scaling** paper introduces a new axis for AI agent improvement — where agent performance scales with the accumulation of external memory stores rather than model size or inference-time reasoning. This work is detailed in the full article at [[concepts/memory-scaling]].

**Key Insights:**
- **Third scaling axis** alongside parametric scaling (larger models) and inference-time scaling (chain-of-thought)
- **Memory Taxonomy:** Episodic (raw logs), Semantic (generalized skills), Personal (user-specific), Organizational (shared business context)
- Core thesis: *"The differentiator for enterprise agents will increasingly be what memory they have accumulated rather than which model they call"*

### MemAlign Framework

Databricks' **MemAlign** framework distills episodic memories into semantic rules for agents:

| Method | Result |
|--------|--------|
| **Labeled Data** | Accuracy rose from near zero to 70%, surpassing expert-curated baselines by ~5%; reasoning steps dropped from ~20 to ~5 |
| **Unlabeled Logs** | Using LLM-as-judge to filter raw logs, surpassed expert baseline (33%) after only 62 records; reached 50%+ accuracy |

**Takeaway:** Uncurated user interactions can substitute for costly hand-engineered domain instructions — a significant finding for enterprise agent deployment.

### Infrastructure for Memory Scaling

Databricks identified three pillars for production memory systems:
1. **Scalable Storage:** Serverless PostgreSQL (Lakebase/Neon) for structured queries, full-text search, and vector similarity
2. **Memory Management:** Bootstrapping (cold-start from existing docs), Distillation (compress raw logs), Consolidation (deduplicate, resolve conflicts)
3. **Security & Governance:** Identity-aware access control, lineage tracking

### Known Challenges

- **Quality Degradation:** Agents risk amplifying their own errors by citing past mistakes
- **Staleness:** Outdated schemas or renamed entities in memory can mislead agents
- **Discovery Gap:** Agents must learn *when* to query memory — a meta-cognitive challenge

### Future Vision: The Agent as Memory

Databricks envisions a future where an agent's identity is defined by its **memory store** rather than its model weights:
- Swappable reasoning engines (the LLM becomes a commodity)
- Competitive advantage through accumulated memory
- *"A smaller model with a rich memory store can outperform a larger model with less memory"*

---

## Related Wiki Pages

- [[concepts/memory-scaling]] — The core concept introduced by Databricks
- [[concepts/ai-agent-memory]] — Overview of AI agent memory systems
- [[concepts/ai-agent-memory-middleware]] — Storage infrastructure for agentic AI (references Databricks' memory scaling work)
- [[concepts/supermemory]] — Supermemory Filesystem (SMFS), an adjacent approach to agent memory
- [[entities/claude-perfect-memory]] — Claude Code's memory architecture
- [[concepts/agent-memory]] — Redirect page consolidating to [[concepts/ai-agent-memory]]
