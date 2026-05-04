---
title: Jason Liu
type: entity
handle: "@jxnlco"
created: 2026-04-13
updated: 2026-04-27
tags:
  - person
  - x-account
  - ai
  - structured-outputs
  - pydantic
  - instructor
  - model
  - developer-tooling
  - rag
  - context-engineering
  - evaluation
sources: []
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

### [[jason-liu--instructor|Instructor Library & Structured Outputs]]
Liu's core philosophy — "Pydantic is All You Need" — argues the problem with LLM integration isn't the models but the interface between probabilistic outputs and deterministic software. His library enables schema-first design, validation as self-correction via automatic reasking, and backwards compatibility with existing paradigms. Instructor now spans 5 languages, every major LLM provider, and was cited by OpenAI as inspiration for their Structured Outputs API feature. Includes the **Software 3.0** vision of classical engineering rigor applied to LLM systems. See the full details → [[jason-liu--instructor]]

### [[jason-liu--rag-framework|RAG Philosophy & Framework]]
Liu's systematic practitioner framework for RAG, organized around the thesis that "RAG is the feature, not the benefit." Key contributions include: the **Twin Biases** of RAG development (Absence Bias, Intervention Bias), the **RAG Playbook** continuous improvement flywheel, the **"Only 6 RAG Evals"** framework (Q/C/A conditional relationships), the **7-Step Quick-Win Runbook**, **RAG Levels of Complexity** (0–6), and **Authority in RAG Systems** (proposing Learning to Rank to address semantic search's neglect of authority signals). See the full framework → [[jason-liu--rag-framework]]

### [[jason-liu--context-engineering|Context Engineering — Beyond RAG for Agentic Systems]]
Liu extends RAG into agentic systems with a **four-level context engineering** framework (from minimal chunks to facets/query refinement), the concept of **agent peripheral vision** (agents need to know what they don't know), and form-factor decision frameworks. Also includes the **"In Distribution" theory** about sandbox engineering in the OpenAI Agents SDK. See the full framework → [[jason-liu--context-engineering]]

## Key Work

### [[jason-liu--instructor|Instructor Library]]
A thin wrapper around LLM APIs adding response_model parameter, automatic retries with validation feedback, streaming with type safety, and multi-provider support. **11K+ GitHub stars, 6M+ monthly downloads.** Cited by OpenAI as inspiration for their Structured Outputs feature. See [[jason-liu--instructor]] for full details.

### [[jason-liu--key-work|Career, RAG Master Series, & Consulting]]
Includes his work at **Stitch Fix** (multimodal embedding systems, Flight framework), **Meta**, **Maven training programs**, and his **567 Studios consulting practice**. The **RAG Master Series** is a comprehensive 12+ article series on jxnl.co covering everything from fundamentals to enterprise implementation, plus a detailed **Speaker Series** table and **RAG Anti-Patterns** analysis. See the full career and article listing → [[jason-liu--key-work]]

## Related People

- **[[concepts/pydantic]]** — Samuel Colvin's data validation library; the foundation of Instructor's approach
- **[[samuel-colvin]]** — Pydantic creator; collaborated on structured outputs patterns and Pydantic AI
- **[[concepts/structured-outputs]]** — Liu's primary technical domain; cited by OpenAI as inspiration for their feature
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

## Related Concepts

- [[concepts/llm-patterns-eugene-yan]] — Co-author of the O'Reilly Applied LLMs Guide (What We Learned from a Year of Building with LLMs)
- [[entities/eugene-yan]] — Lead author of the Applied LLMs Guide

## References

- jason-liu-sandboxes-agents-sdk-2026-04
