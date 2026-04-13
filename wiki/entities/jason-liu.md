---
title: "Jason Liu"
handle: "@jxnlco"
created: 2026-04-13
updated: 2026-04-13
tags: [person, x-account, ai, structured-outputs, pydantic, instructor, llm-engineering, developer-tools, rag, context-engineering, evals]
aliases: ["jxnlco", "jason liu instructor", "jason liu pydantic", "567 studios", "jason liu rag"]
---

# Jason Liu (@jxnlco)

| | |
|---|---|
| **X** | [@jxnlco](https://x.com/jxnlco) |
| **Blog** | [jxnl.co](https://jxnl.co) |
| **GitHub** | [jxnl](https://github.com/jxnl) |
| **Role** | Founder, 567 Studios; creator of Instructor; former Staff MLE at Stitch Fix |
| **Known for** | Instructor library (11K+ stars, 6M+ monthly downloads), "Pydantic is all you need" keynote, structured outputs for LLMs |
| **Bio** | Staff ML Engineer and open source creator with 10+ years building AI systems at scale. Creator of Instructor, cited by OpenAI as inspiration for their structured output feature. Works with Seed to Series B companies on AI best practices including RAG, Context Engineering, and Evals. |

## Overview

Jason Liu is one of the most influential practitioners in the space of **structured LLM outputs** — the problem of getting reliable, typed, validated data from language models rather than loose text. His open source library **Instructor** (python.useinstructor.com) has become a de facto standard for this pattern, with 11,000+ GitHub stars, 6M+ monthly downloads, and explicit citation by OpenAI as the inspiration for their Structured Outputs feature.

Liu's career spans the full production ML stack: Data Scientist at Meta (2017), Staff MLE at Stitch Fix (2018–2023) where he built multimodal embedding systems handling 350M+ daily requests, and now Founder of 567 Studios (2023–present) where he consults for companies including Zapier, HubSpot, Limitless, Weights & Biases, Modal Labs, Timescale, and Pydantic. He also runs training programs on Maven attended by engineers from OpenAI, Anthropic, Google, Microsoft, Amazon, and Netflix.

His intellectual signature is the thesis that **"we're not changing the language of programming — we're relearning how to program with data structures."** This positions structured outputs not as a new paradigm but as a return to classical software engineering rigor, making LLM integration backwards-compatible with existing codebases and tooling.

## Core Ideas

### "Pydantic is All You Need" — Structured Outputs as the Foundation

Liu's keynote at the **AI Engineer Summit 2023** ("Pydantic is all you need") crystallized his core philosophy: the problem with LLM integration isn't the models — it's the interface between probabilistic outputs and deterministic software.

> "Imagine hiring an intern to write an API that returns a string you have to JSON load into a dictionary and pray the data is still there. You'd probably fire them and replace them with GPT. Yet, many of us are content using LLMs in the same way."

His argument has three pillars:

1. **Schema-first design** — Define what you want as a Pydantic model, not as a prompt template
2. **Validation as self-correction** — Treat LLM errors as validation failures with clear error messages the model can use to retry
3. **Backwards compatibility** — Make Software 3.0 work with existing paradigms (type hints, dataclasses, ORM patterns)

Instructor's API is intentionally minimal:

```python
from instructor import from_openai
from pydantic import BaseModel
from openai import OpenAI

class User(BaseModel):
    name: str
    age: int

client = from_openai(OpenAI())
response = client.create(model="gpt-4o", response_model=User,
    messages=[{"role": "user", "content": "John is 25 years old"}])
# response is a validated User(name="John", age=25)
```

### Validation Errors as a Feature, Not a Bug

Liu reframes the LLM reliability problem through the lens of **classical software validation**:

> "Instead of framing 'self-critique' or 'self-reflection' in AI as new concepts, we can view them as validation errors with clear error messages that the system can use to self-correct."

Instructor implements a **reasking mechanism** that automatically:
1. Parses the LLM's raw output
2. Validates it against the Pydantic schema
3. On failure, sends the validation error back to the model as context for retry
4. Repeats until valid output is produced or max retries is reached

This turns the probabilistic LLM into a deterministic function from the caller's perspective — a critical requirement for production systems.

### Multi-Language, Multi-Provider Structured Outputs

Since the original Python release, Instructor has expanded to **5 languages** (Python, TypeScript, Ruby, Go, Elixir) plus a **Rust** implementation, and supports every major LLM provider:

- OpenAI, Anthropic, Google, Vertex AI, Cohere
- Ollama, llama-cpp-python (local/offline models)
- Any provider with function calling capabilities

The cross-language strategy reflects Liu's belief that **structured outputs are a universal need**, not a Python-specific convenience.

### Software 3.0 — Classical Engineering Meets LLMs

Liu's vision of "Software 3.0" is that structured outputs allow developers to:
- **Own the objects we define** — typed models, not loose JSON
- **Control the functions we implement** — explicit tool contracts
- **Manage the control flow** — retries, validation, error handling
- **Own the prompts** — declarative schema definitions that generate prompts automatically

> "This approach makes Software 3.0 backwards compatible with existing software, demystifying language models and returning us to a more classical programming structure."

### RAG Philosophy — Data-First, Evaluation-Driven

Through his consulting work with dozens of startups and his free 6-week email course on RAG, Liu has developed a distinctive philosophy on building and improving RAG systems. His approach can be summarized in three core theses:

**1. "RAG is the feature, not the benefit."**

> "RAG systems suck because the value you derive is time saved from finding an answer. This is a one-dimensional value, and it's very hard to sell any value beyond that. Meanwhile, a report is a higher-value product because it is a decision-making tool that enables better resource allocation."

Jason predicts RAG will shift from question-answering to **report generation** — from delivering answers to enabling decisions. This reframes the success metric from "did the user get an answer?" to "did the user make a better decision?"

**2. "Look at your data at every step of the pipeline."**

His single most repeated principle. A typical RAG pipeline has six stages (Data Collection → Extraction/Enrichment → Indexing → Retrieval → Re-ranking → Generation), and problems can emerge at any of them. Teams that skip evaluation at intermediate stages are flying blind:

> "The mistake is increasing system complexity without proper evaluation. About 90% of the time, teams implement complex retrieval paths and re-ranking systems when the real problem was bad input data."

**3. "Good search is the ceiling on your RAG quality."**

> "If recall is poor, no prompt engineering or model upgrade will save you." Jason argues that teams obsess over the generation step (which LLM to use, prompt templates) while the retrieval step — fundamentally an information retrieval problem — is the actual bottleneck.

This philosophy manifests in his **RAG Master Series** on jxnl.co — 12+ interconnected articles covering everything from fundamentals to advanced optimization, anti-patterns, and enterprise implementation.

## Key Work

### Instructor Library
The flagship open source project — a thin wrapper around LLM APIs that adds:
- **response_model parameter** — specify a Pydantic model, get validated objects back
- **Automatic retries** — configurable max retries with validation error feedback
- **Streaming with structure** — partial objects as tokens arrive, maintaining type safety
- **Multi-provider support** — same API across OpenAI, Anthropic, Google, local models
- **Multi-language ports** — TypeScript, Ruby, Go, Elixir, Rust implementations
- **11,000+ GitHub stars, 6M+ monthly PyPI downloads**
- **Cited by OpenAI** as inspiration for their Structured Outputs API feature

### Structured Outputs By Example
A hands-on educational site (github.com/jxnl/structuredoutputsbyexample) showcasing extraction patterns across:
- Basic data extraction
- Classification tasks
- Streaming responses
- Multiple LLM providers
- Real-world use cases (search queries, content moderation, data transformation)

### Stitch Fix — Multimodal Embedding System (2018–2023)
As Staff MLE, Liu:
- Built multimodal embedding systems using ResNet-50 and CLIP+GPT-3 integration
- Designed the **Flight framework** handling 350M+ daily requests with 80% internal adoption
- Led a team of 6–7 engineers and data scientists
- Applied structured output patterns to product recommendation and personalization pipelines

### Meta (Facebook) — Data Scientist (2017)
- Built real-time monitoring dashboards, reducing escalation time by 50%
- Early work on production ML systems at scale

### Maven Training Programs
Liu runs advanced training courses on Maven for engineers from top AI companies, covering:
- RAG architecture and implementation
- Context engineering patterns
- Evaluation frameworks for LLM systems
- Structured outputs and validation

### Consulting Practice (567 Studios)
Works with Seed to Series B companies on AI best practices:
- RAG system design and optimization
- Context engineering strategies
- Evaluation framework construction
- Developer adoption and tooling

### RAG Master Series (jxnl.co)
A comprehensive 11+ article series on RAG, distilling years of consulting experience into a systematic framework:

**Foundation Posts:**
- [What is RAG?](https://jxnl.co/writing/2024/11/07/what-is-retrieval-augmented-generation/) — Core components: knowledge base, retrieval, generation, re-ranking. Key insight: RAG systems must be optimized as interconnected pipelines, not isolated parts
- [Levels of RAG Complexity](https://jxnl.co/writing/2024/02/28/levels-of-complexity-rag-applications/) — 7-tier framework from basic chunk+embed (Level 1) through structured processing with reranking (Level 2), observability and wide event tracking (Level 3), to image/table processing and query routing (Levels 6–7). Core philosophy: *"Most teams jump straight to Level 4 complexity and wonder why everything break*"

**Implementation & Improvement Posts:**
- [Systematically Improving Your RAG](https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/) — Data-first improvement runbook: synthetic data for baselines, hybrid search (BM25 + vector), metadata utilization, query clustering for capability gap analysis
- [The RAG Playbook: Building a Data Flywheel](https://jxnl.co/writing/2024/08/19/rag-flywheel/) — Continuous improvement cycle: synthetic data → fast evaluations → production monitoring → user feedback → classification → system improvements. *"The teams who can make that loop go as fast as possible are the ones who win"*
- [Low-Hanging Fruit for RAG Search](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/) — Seven quick wins: date filters, user feedback copy, cosine distance tracking, full-text search, making chunks look like questions at ingestion time, file/document metadata inclusion
- [Six Proven Strategies for Improving RAG](https://jxnl.co/writing/2025/09/11/rag-series-index/) — Portfolio approach: flywheels, query segmentation, specialized indices, routing, feedback loops, response optimization

**Production & Monitoring Posts:**
- [Systematically Improving RAG with Monitoring](https://jxnl.co/writing/2025/09/11/rag-series-index/) — AI monitoring must detect subtle degradation, not just explicit errors. Track implicit signals (frustration patterns) alongside explicit ones (thumbs up/down)
- [RAG Anti-Patterns with Skylar Payne](https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/) — Top mistakes: increasing complexity without evaluation (~90% of failures), naive embedding usage, chunking too small, ignoring query routing. *"About 90% of the time, teams implement complex retrieval paths and re-ranking systems when the real problem was bad input data"*

**Evaluation Posts:**
- [The Only 6 RAG Evaluations You Need](https://jxnl.co/writing/2025/09/11/rag-series-index/) — Overcomplicated frameworks fail. Six core evals: retrieval quality, generation accuracy, relevance, citation validation, latency, user satisfaction

**Advanced & Enterprise Posts:**
- [RAG++: The Future Beyond Question Answering](https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/) — RAG will shift from Q&A to **report generation**. *"A report is a higher-value product because it is a decision-making tool that enables better resource allocation"*
- [Authority in RAG Systems](https://jxnl.co/writing/2025/03/06/authority-in-rag-systems-the-missing-piece-in-your-retrieval-strategy/) — Relevancy, freshness, AND authority are all critical signals. Proposes learning-to-rank approaches combining semantic similarity with PageRank-style authority
- [RAG Enterprise Implementation Process](https://jxnl.co/writing/2025/09/11/rag-series-index/) — Scaling RAG across organizations with governance, compliance, and multi-team coordination
- [Text Chunking Strategies with Anton from ChromaDB](https://jxnl.co/writing/2025/09/11/text-chunking-strategies-for-rag-applications/) — Two rules in tension: (1) fill the embedding model's context window, (2) don't group unrelated information. *"There's no one-size-fits-all chunking strategy"*

## Blog / Key Writings

### Structured Outputs
- **AI Engineer Keynote: Pydantic is all you need** (Nov 2023) — The talk that launched his public profile, arguing that structured outputs via Pydantic solve the fundamental LLM integration problem
- **Pydantic is Still All You Need: Reflections on a Year of Structured Outputs** (Sep 2024) — One-year retrospective: "nothing's really changed in the past year. The core API is still just one function call." Covers 40% month-over-month growth, multi-language expansion, and the case for validation-first design
- **Bridging Language Models with Python with Instructor, Pydantic, and OpenAI's Function Calls** (Medium, 2023) — Technical deep-dive into why Pydantic is the right abstraction between LLMs and traditional software
- **Structured Outputs By Example** (github.com/jxnl/structuredoutputsbyexample) — Living documentation of extraction patterns across providers and use cases

### RAG (Retrieval-Augmented Generation) — 12+ articles

Jason maintains the most comprehensive practitioner's guide to RAG on his blog, organized as a multi-part series with a [RAG Master Series Index](https://jxnl.co/writing/2025/09/11/rag-series-index/). His approach is distinctive for its **data-first, evaluation-driven methodology** rather than architecture-first thinking.

**Core RAG philosophy:**

> "Rag is the feature, not the benefit." — Jason argues that RAG as question-answering delivers only time-saved value, while RAG as report-generation delivers decision-making value, which is fundamentally more valuable to businesses.

> "Look at your data at every step of the pipeline." — His single most repeated principle. Teams that examine data inputs, intermediate results, and outputs, then iterate fast, "are invariably the ones who succeed."

**Key RAG articles:**

- **[What is Retrieval Augmented Generation?](https://jxnl.co/writing/2024/11/07/what-is-retrieval-augmented-generation/)** — Foundational overview of RAG components (query understanding, retrieval, generation, re-ranking) and why RAG matters over pure parametric knowledge
- **[Levels of Complexity: RAG Applications](https://jxnl.co/writing/2024/02/28/levels-of-complexity-rag-applications/)** — Framework classifying RAG systems into levels from basic chunk+embed→search (Level 0) through query enhancement (Level 2), observability/wide events (Level 3), async and caching (Level 4), advanced search/ranking (Level 5), to image/table processing and routing (Level 6+)
- **[Systematically Improving Your RAG](https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/)** — Comprehensive improvement runbook based on consulting experience. Core thesis: start with synthetic data for baseline metrics, use hybrid search (BM25 + vector), cluster and model topics to find capability gaps
- **[Low-Hanging Fruit for RAG Search](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/)** — Seven quick wins: synthetic baseline data, date filters, improved user feedback copy, tracking cosine distance/reranking scores, adding full-text search, making chunks look like questions at ingestion time, including file/document metadata
- **[The RAG Playbook](https://jxnl.co/writing/2024/08/19/rag-flywheel/)** — Systematic flywheel: iterate → user feedback → production monitoring → system improvements → classification → real-world data collection → fast evaluations → synthetic data generation
- **[Predictions for the Future of RAG](https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/)** — RAG will shift from question-answering to report generation. "A report is a higher-value product because it is a decision-making tool that enables better resource allocation." Predicts a marketplace of report-generating templates
- **[Authority in RAG Systems](https://jxnl.co/writing/2025/03/06/authority-in-rag-systems-the-missing-piece-in-your-retrieval-strategy/)** — Relevancy, freshness, AND authority are all critical signals. Embedding search ignores authority; proposes learning-to-rank approaches combining semantic similarity with PageRank-style authority signals
- **[Text Chunking Strategies](https://jxnl.co/writing/2025/09/11/text-chunking-strategies-for-rag-applications/)** — Guest session with Anton from ChromaDB. Two rules of thumb in tension: (1) fill the embedding model's context window, (2) don't group unrelated information. "There's no one-size-fits-all chunking strategy."
- **[RAG Anti-Patterns with Skylar Payne](https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/)** — Interview with Skylar (ex-Google, ex-LinkedIn). Top anti-patterns: increasing complexity without evaluation (~90% of mistakes), naive embedding usage (trained for semantic similarity, not Q&A), chunking too small, ignoring query routing (simple metadata lookups instead of full RAG for straightforward queries)
- **[Beyond Chunks: Why Context Engineering is the Future of RAG](https://jxnl.co/writing/2025/08/27/facets-context-engineering/)** — First post in a Context Engineering series. Core thesis: "In agentic systems, how we structure tool responses is as important as the information they contain." Four levels of context engineering: minimal chunks → chunks with source metadata → multi-modal content → facets and query refinement. Predicts tool results become prompt engineering for agents.

**RAG 6-week email course:** Jason runs a free 6-week email course on RAG covering everything from his consulting work, available at improvingrag.com.

### Context Engineering

Jason is developing Context Engineering as a natural evolution beyond RAG for agentic systems:

> "The breakthrough came when we realized chunks themselves were the limitation. When search results showed multiple documents, agents couldn't strategically decide which to load or how to explore further."

- Four levels: Minimal Chunks → Source Metadata → Multi-Modal → Facets & Query Refinement
- Predicts: "Tool results become prompt engineering" — metadata teaches agents how to use tools in future calls
- First post in series (Aug 2025) focuses on faceted search as the lowest-hanging fruit

## Related People

- **[[pydantic]]** — Samuel Colvin's data validation library; the foundation of Instructor's approach
- **[[eugene-yan]]** — Fellow practitioner in production ML evaluation; both emphasize systematic validation over benchmarking
- **[[shreya-shankar]]** — Overlapping focus on evaluation and validation rigor in LLM systems
- **[[bryan-bischof]]** — Shared philosophy of production-first ML engineering over demo-centric approaches
- **Weights & Biases** — Consulting client; shared community around ML engineering best practices
- **Modal Labs** — Consulting client; serverless GPU infrastructure for running structured output pipelines
- **Zapier, HubSpot, Limitless, Timescale** — Consulting clients across the AI application stack

## X Activity Themes

- **Structured outputs patterns** — Practical examples of extracting typed data from LLMs
- **Pydantic tips and tricks** — Validation techniques, schema design, error handling
- **Instructor library updates** — New features, multi-language ports, provider support
- **AI engineering best practices** — Production patterns, evaluation frameworks, RAG optimization
- **Conference talks and workshops** — Maven course updates, keynote announcements, community engagement
- **Software 3.0 philosophy** — Arguments for classical engineering rigor in LLM applications
- **Consulting insights** — Real-world patterns observed across startups and enterprises
