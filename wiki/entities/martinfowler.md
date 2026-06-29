---
title: "Martin Fowler"
created: 2026-06-21
updated: 2026-06-23
type: entity
tags:
  - person
  - thoughtworks
  - software-engineering
  - ai-software-engineering
  - consultant
  - methodology
  - rag
  - text-to-sql
sources:
  - "[[raw/articles/2026-06-19_martinfowler_reliable-agentic-ai-systems]]"
  - https://martinfowler.com
related:
  - thoughtworks
  - refactoring
  - enterprise-architecture
status: active
---

# Martin Fowler

Martin Fowler is a renowned software architect, author, and thought leader in the software engineering community. He serves as Chief Scientist (formerly Principal Scientist) at [[entities/thoughtworks|Thoughtworks]], a global technology consultancy, and publishes extensively on his website [martinfowler.com](https://martinfowler.com) — one of the most widely-read technical blogs in the industry.

## Background

Fowler has been a prominent voice in software engineering for decades, contributing foundational works on refactoring, patterns of enterprise application architecture, domain-specific languages, and continuous delivery. His writing spans both deeply technical topics and broader reflections on engineering practices. He maintains a **bliki** (blog + wiki) format on martinfowler.com that serves as a primary reference for software engineering patterns and practices.

## Key Contributions

- **Refactoring**: Authored the seminal book *Refactoring: Improving the Design of Existing Code* (1999, 2nd ed. 2018), which popularized the concept and practice of code refactoring as a disciplined technique.
- **Enterprise Patterns**: Wrote *Patterns of Enterprise Application Architecture* (2002), cataloging design patterns for enterprise software systems including the widely-adopted **Repository**, **Unit of Work**, and **Data Mapper** patterns.
- **UML Distilled**: Wrote *UML Distilled* (1997, 3rd ed. 2003), a concise guide to the Unified Modeling Language that became a standard reference.
- **DSLs**: Advanced domain-specific languages with *Domain-Specific Languages* (2010), co-authored with Rebecca Parsons.
- **Microservices**: Co-authored the foundational essay *Microservices* (2014) with James Lewis, which shaped the modern understanding of microservice architectures.
- **Continuous Delivery**: Co-author of the *Continuous Delivery* essay series with Jez Humble and contributing editor to the field.

## Bliki Publication Platform

Martin Fowler's website (martinfowler.com) is organized as a **bliki** — a hybrid of blog and wiki. Articles are presented as permanent reference documents rather than time-bound blog posts. This format is curated by Fowler and a rotating set of contributors from Thoughtworks. Key features of the bliki model:

- Articles are treated as living documents that can be updated
- Each article has a clear author attribution (typically a Thoughtworks consultant)
- Content spans software architecture, engineering practices, Agile, DevOps, and increasingly AI systems engineering
- The platform has a distinctive design aesthetic with clear diagrams and structured prose

## Role in AI Systems Engineering

Through Thoughtworks and his platform, Fowler has increasingly covered AI and LLM engineering topics. The bliki model has proven well-suited for AI content, where the field evolves rapidly and articles benefit from being treated as living documents. In June 2026, martinfowler.com published **"Building Reliable Agentic AI Systems"**, a comprehensive case study of Bayer AG's PRINCE platform co-authored with Sarang Sanjay Kulkarni, a Principal Consultant at Thoughtworks.

This article applies Fowler's long-standing emphasis on engineering discipline — [[concepts/context-engineering|context engineering]] and [[concepts/harness-engineering|harness engineering]] — to the emerging domain of agentic AI, demonstrating practical patterns for building production-reliable AI agents.

## PRINCE Case Study: Building Reliable Agentic AI Systems (June 2026)

In June 2026, martinfowler.com published "Building Reliable Agentic AI Systems" — a detailed case study of the **PRINCE (Preclinical Information Center)** platform developed by Bayer AG in collaboration with [[entities/thoughtworks|Thoughtworks]]. Authored by Sarang Sanjay Kulkarni (Principal Consultant at Thoughtworks) and hosted on Fowler's bliki, the article documents how pharmaceutical preclinical research was transformed from keyword-based search into an intelligent agentic research assistant.

### Background and Motivation

Preclinical drug discovery at Bayer faced significant challenges: data silos across disparate systems, limited keyword-based search capabilities unable to handle complex preclinical terminology, and time-consuming manual analysis of decades of study reports. The PRINCE platform was conceived as a unified gateway to address these challenges.

### Evolution: Search → Ask → Do

PRINCE evolved through three distinct phases:

1. **Search**: Consolidated thousands of nonclinical study reports from multiple in-house data silos into a unified searchable format, primarily leveraging structured metadata.
2. **Ask**: Introduced an AI-powered question-answering system using Retrieval-Augmented Generation (RAG), enabling researchers to query unstructured data including scanned historical PDF reports in natural language.
3. **Do**: The current phase positions PRINCE as an active research assistant capable of executing complex tasks through multi-agent orchestration, including drafting regulatory documents.

### System Architecture

PRINCE's architecture is orchestrated using **LangGraph** and served via a **FastAPI** backend with a **React** conversational UI:

- **Vector Store**: OpenSearch stores vector representations of all study reports
- **Structured Data**: Amazon Athena provides access to curated structured data from ETL pipelines
- **State Management**: PostgreSQL (LangGraph checkpointer) + DynamoDB for application state
- **LLM Backends**: Internal GenAI platforms hosting models from OpenAI, Anthropic, Google, and open-source providers via unified OpenAI-compatible endpoints

### Multi-Agent Workflow

The system employs three specialized agents working in coordination:

1. **Researcher Agent**: The primary information gatherer, using a hybrid retrieval approach:
   - **Agentic RAG** ([[concepts/agentic-rag]]) for unstructured data — a multi-stage pipeline with keyword extraction, metadata filter generation, query expansion (n=5), weighted hybrid search (semantic 0.7 + keyword 0.3), and reranking (bge-reranker-large, top-k=7)
   - **Text-to-SQL** ([[concepts/text-to-sql]]) for structured data — using dynamic few-shot prompting with vector-similarity-based example retrieval for Athena SQL generation

2. **Reflection Agent**: Validates data completeness and sufficiency, providing feedback loops for additional research when needed. Performs **data validation** rather than process reflection.

3. **Writer Agent**: Synthesizes verified information into formatted, citation-linked responses ensuring transparency and explainability.

### Context Engineering

A key design principle in PRINCE is **context discipline**. Rather than stuffing all available information into one large prompt, the system provides different context at each stage:

- **Planning context** (Think & Plan phase)
- **Retrieval context** (Researcher Agent phase)
- **Evidence context** (Reflection Agent phase)
- **Synthesis context** (Writer Agent phase)

This approach, reflecting [[concepts/context-engineering]], reduces context pollution and makes the system easier to debug, evaluate, and improve. Context engineering shaped what information each model received, what it did not receive, and how context moved between specialized steps.

### Harness Engineering

The reliability scaffolding around the models — [[concepts/harness-engineering]] — included:

- **Orchestration**: LangGraph-based multi-stage workflow controlling intent clarification → thinking/planning → research → validation → response generation
- **Retry Mechanisms**: Two-level retry (individual LLM call level and logical node level); agents receive error context to chart alternative trajectories
- **Fallback Strategies**: Automatic failover to alternative models or platforms when a specific LLM fails
- **Observability**: Langfuse for production tracing and evaluation datasets, RAGAS for RAG pipeline quality assessment, CloudWatch for system health monitoring
- **Evaluation Methodology**: Daily live traffic evaluation + dataset evaluation on core workflow/prompt/model changes

### Transparency and Explainability

PRINCE prioritizes trust through:
- **Automatic citations** linking responses back to specific source chunks
- **Human-in-the-Loop** at the Clarify User Intent stage, where AI recommends data sources but the user retains final decision authority
- **Explainable agent decisions** through traceable reasoning paths

### Ongoing Evolution

The Researcher Agent is evolving from a monolithic architecture into a hierarchy of domain-specific sub-agents (toxicology, pharmacology, etc.), each owning its own toolset and prompt instructions. This reflects Fowler's long-standing emphasis on **cohesion and separation of concerns** in system design.

## Significance for the AI Engineering Community

The PRINCE case study published on martinfowler.com is significant for several reasons:

- It demonstrates that established software engineering principles (context discipline, separation of concerns, observability, retry with backoff) apply directly to agentic AI systems
- It provides a concrete reference architecture for production-grade Agentic RAG and Text-to-SQL systems
- It shows how large enterprises (Bayer AG) can successfully build and deploy multi-agent AI systems with governance and compliance requirements
- It validates context engineering and harness engineering as distinct engineering disciplines for AI systems
- It exemplifies the bliki publication model's suitability for emerging, fast-evolving technical domains

## Related Pages

- [[concepts/agentic-rag]] — Agentic RAG architecture, comprehensively illustrated by PRINCE
- [[concepts/context-engineering]] — Context engineering discipline, demonstrated in PRINCE's multi-stage context design
- [[concepts/harness-engineering]] — Harness engineering discipline, shown in PRINCE's orchestration, retry, and observability patterns
- [[entities/thoughtworks]] — Thoughtworks, the consultancy where Fowler serves as Chief Scientist
- [[concepts/reliable-agent-patterns]] — Catalog of reliability patterns extracted from the PRINCE case study
