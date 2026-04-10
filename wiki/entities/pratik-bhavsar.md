---
entity: pratik-bhavsar
aliases:
  - ptkbhv
  - bhavsarpratik
url: https://pakodas.substack.com
blog: https://pakodas.substack.com
twitter: "@ptkbhv"
github: https://github.com/bhavsarpratik
linkedin: https://www.linkedin.com/in/bhavsarpratik
role: AI Engineer at Galileo; author of Eval Engineering books
type: person
tags:
  - AI-evaluation
  - agent-leaderboard
  - hallucination-index
  - LLM-as-a-judge
  - RAG
  - multi-agent-systems
updated: 2026-04-10
---

# Pratik Bhavsar

**URL:** https://pakodas.substack.com
**Blog:** pakodas.substack.com (Eval Engineering newsletter)
**Twitter/X:** @ptkbhv
**GitHub:** https://github.com/bhavsarpratik
**LinkedIn:** https://www.linkedin.com/in/bhavsarpratik
**Company:** Galileo (AI Engineer, Employee #26 at Series A)
**Former:** Enterpret (Founding Engineer), Jina AI, Morningstar, Maxpool (Founder)
**Education:** M.Tech, Indian Institute of Technology (IIT) Bombay (9.15/10 GPA)
**Location:** India

## Overview

Pratik Bhavsar is an AI Engineer at Galileo, where he leads the Agent Leaderboard and Hallucination Index initiatives — two of the most prominent open benchmarks for evaluating generative AI systems. He is the author of four widely-read ebooks: "Mastering Multi-Agent Systems," "Mastering RAG," "Mastering Agents," and "Mastering LLM-as-a-Judge."

Bhavsar's work focuses on a critical gap in the AI ecosystem: **how do you evaluate AI systems when there's no ground truth?** His Agent Leaderboard benchmarks LLM-based agents on real-world enterprise tasks across multiple domains, providing the industry's first standardized evaluation framework for agentic AI. The Hallucination Index, featured in Andrew Ng's newsletter, tracks the frequency and impact of hallucinations across different models and tasks.

His career spans the full AI stack: from building low-latency semantic search engines at Morningstar and Enterpret, to contributing to the open-source neural search framework at Jina AI, to now leading evaluation infrastructure at Galileo. He holds an M.Tech from IIT Bombay (one of India's most prestigious engineering institutions) and has consistently ranked in the top 20 nationally in AI competitions, including Microsoft's Search Ranking Challenge and the SEMEVAL Sentimix competition.

Bhavsar is also the founder of **Maxpool**, a community and nonprofit focused on agents, evaluation, RAG, and the business of AI. Maxpool has built "Max," a custom AI assistant integrated into the community, and serves as a hub for AI professionals sharing evaluation best practices.

## Timeline

| Date | Event |
|------|-------|
| 2013–2015 | M.Tech at Indian Institute of Technology (IIT) Bombay, Energy Science and Engineering (9.15/10 GPA) |
| ~2015–2018 | Data Science/ML roles at various companies (Reckrut.com, Book Lovers Society) |
| ~2018 | Completed Stanford CS229, CS231n, CS224n, CS224d courses via online certifications |
| 2019 | Founded Maxpool — community of AI professionals focused on agents and evaluation |
| 2019–2021 | Data Science roles at Morningstar and TaskHuman — built low-latency semantic search, personalized notification systems, and recommendation engines |
| 2019 | Secured 1st place in Microsoft AI Challenge (internal) and top 20 nationally in Microsoft's Search Ranking Challenge |
| 2020 | Top 10 nationally at SEMEVAL Sentimix (sentiment analysis competition) |
| Sep–Dec 2020 | AI Engineer at Jina AI — contributed to open-source neural search framework, NER for intent extraction on social media |
| Feb 2021–May 2023 | Founding Engineer at Enterpret — built semantic search, reranking, text generation, and zero/few-shot NLP pipelines for enterprise AI |
| Jun 2023–Present | AI Engineer at Galileo (Employee #26 at Series A) — leading Agent Leaderboard and Hallucination Index |
| Feb 2025 | Launched Agent Leaderboard v1 on Hugging Face — benchmarking 30+ LLMs across agentic tasks |
| Jul 2025 | Launched Agent Leaderboard v2 — enterprise-grade benchmark across 5 industries with Klarna case study context |
| 2025 | Published "Mastering Agents" ebook |
| 2025 | Published "Mastering Multi-Agent Systems" ebook |
| 2025 | Published "Mastering RAG" ebook |
| 2025 | Published "Mastering LLM-as-a-Judge" ebook |
| 2025 | Galileo's Hallucination Index featured in Andrew Ng's newsletter |
| 2026 | 1st place in every internal hackathon at Galileo (continuous record) |
| 2026 | Active contributor to evaluation frameworks and open-source AI benchmarks |

## Core Ideas

### What We Measure Shapes AI

Bhavsar's foundational philosophy for evaluation work:

> "What we measure shapes AI."
> — Agent Leaderboard v2 announcement

This echoes Goodhart's Law (when a measure becomes a target, it ceases to be a good measure) but applies it constructively: the benchmarks we create define the direction the entire field moves. If we only measure token accuracy, models optimize for token accuracy. If we measure action completion in realistic enterprise scenarios, models optimize for actually solving user problems.

### Action Completion Over Token Metrics

A key insight driving Agent Leaderboard v2: traditional NLP metrics (BLEU, ROUGE, exact match) are inadequate for evaluating agentic AI. Agents don't just generate text — they take actions, interact with tools, navigate interfaces, and complete multi-step workflows.

Agent Leaderboard v2 measures:
- **Action Completion (AC):** Did the agent complete every user goal in the scenario, providing clear confirmation or a correct answer?
- **Domain-specific performance:** Across 5 critical industries (customer support, travel, finance, etc.)
- **Realistic scenarios:** Based on real enterprise workflows rather than synthetic benchmarks

The first results showed GPT-4.1 leading with an average Action Completion score of 62% across all domains — meaning even the best models fail to complete user goals nearly 40% of the time.

### The Klarna Lesson: Why Evaluation Matters

Agent Leaderboard v2 was explicitly motivated by Klarna's infamous decision to replace 700 customer-service reps with AI, which backfired so severely that they had to rehire humans. Bhavsar's team wrote:

> "Klarna's decision to replace 700 customer-service reps with AI backfired so much that they're now rehiring humans. That's precisely the problem Agent Leaderboard v2 is built to solve. Rather than simply testing whether an agent can answer a question, we test whether it can complete real enterprise tasks."
> — Agent Leaderboard v2 blog, July 2025

This real-world example grounds his evaluation philosophy: AI systems need to be evaluated on the same criteria businesses use to evaluate human employees. Can they complete the task? Can they handle edge cases? Can they provide appropriate escalation when uncertain?

### LLM-as-a-Judge

Bhavsar's "Mastering LLM-as-a-Judge" ebook and the associated open-source tools address one of the hardest problems in AI evaluation: **how do you score AI outputs when there's no objective ground truth?**

The LLM-as-a-judge approach uses a strong language model to evaluate the outputs of weaker models, providing:
- Rubric-driven scoring (not just binary right/wrong)
- Consistency across evaluators (LLMs don't have bad days)
- Scalability (can evaluate thousands of outputs in minutes)
- Explainability (the judge model can justify its scores)

His work includes production-ready LLM evaluation tools with TypeScript implementation and 19 passing tests in the open-source `llm-as-judge-skills` project.

### Hallucination Tracking at Scale

The Galileo Hallucination Index, which Bhavsar leads, tracks hallucination frequency and impact across different models and tasks. Featured in Andrew Ng's newsletter, the Index has become one of the industry's most-cited resources for understanding model reliability.

His approach to hallucination measurement goes beyond binary "hallucinated/not hallucinated" — it considers:
- **Severity:** How impactful is the hallucination? (Minor factual error vs. dangerous medical misinformation)
- **Frequency:** How often does the model hallucinate on a given task type?
- **Domain-dependence:** Do hallucination rates vary by industry or use case?
- **Model-dependence:** Which models hallucinate least on which types of tasks?

### Building Evaluation Infrastructure, Not Just Benchmarks

Bhavsar distinguishes between creating a benchmark (a static dataset with scores) and building evaluation infrastructure (tools, frameworks, and processes that enable continuous improvement):

- **Agent Leaderboard** is not just a ranking — it's an open framework for benchmarking LLM-based enterprise agents that anyone can extend
- **Hallucination Index** is not just a report — it's an ongoing tracking system that updates as new models and tasks emerge
- His open-source tools on GitHub (including the `galileo-ai/agent-leaderboard` repository) provide reusable evaluation pipelines

This infrastructure-first approach ensures that evaluation keeps pace with the rapidly evolving capabilities of AI systems.

## Key Quotes

> "What we measure shapes AI."
> — Agent Leaderboard v2 announcement

> "I've spent my career working across the AI stack, evaluating agents without ground truth, building continual improvement systems for transformers, and making search systems that actually work in production."
> — GitHub profile

> "Klarna's decision to replace 700 customer-service reps with AI backfired so much that they're now rehiring humans. That's precisely the problem Agent Leaderboard v2 is built to solve."
> — Agent Leaderboard v2 blog, July 2025

> "Rather than simply testing whether an agent can answer a question, we test whether it can complete real enterprise tasks."
> — Agent Leaderboard v2 blog

## Key Projects

### Agent Leaderboard (galileo-ai/agent-leaderboard)
Open framework for benchmarking LLM-based enterprise agents. v1 (Feb 2025) tested 30+ LLMs. v2 (Jul 2025) expanded to 5 industries with realistic enterprise scenarios. Hosted on Hugging Face with 1,280+ views and active community contributions.

### Hallucination Index
Open-source index tracking hallucination frequency and impact across models and tasks. Featured in Andrew Ng's newsletter. Repository: github.com/rungalileo/hallucination-index.

### Mastering GenAI Series (4 ebooks)
- **Mastering Multi-Agent Systems** — Architecting production-grade multi-agent workflows
- **Mastering RAG** — Retrieval-augmented generation best practices
- **Mastering Agents** — Building and deploying AI agents
- **Mastering LLM-as-a-Judge** — Evaluation without ground truth
All published via Galileo (galileo.ai/ebook).

### Maxpool
Community and nonprofit founded in 2019 for AI professionals. Focus on agents, evaluation, RAG, and the business of AI. Built "Max," a custom AI assistant integrated into the community platform.

### Search Ranking at Morningstar and Enterpret
Built low-latency core semantic search using transformers for autocompletion and search, unsupervised deep learning-based recommendation engines, and personalized notification systems.

## Honors & Recognition

- 🥇 **1st place** in every internal hackathon at Galileo, Morningstar, and Enterpret
- 📈 **Top 20 nationally** in Microsoft's Search Ranking Challenge
- 📝 **Top 10 nationally** in SEMEVAL Sentimix 2020
- 🏆 **1st place** in Microsoft AI Challenge 2018 (internal)
- 📰 **Featured in Andrew Ng's newsletter** for the Hallucination Index
- 📚 **4 published ebooks** on AI evaluation, RAG, multi-agent systems, and LLM-as-a-judge
- 🎓 **9.15/10 GPA** at IIT Bombay (M.Tech, Energy Science and Engineering)
- 👥 **25K+ LinkedIn followers**, 3K+ on X

## Related Concepts

- [[AI-Evaluation]] — Bhavsar's primary domain
- [[Agent-Leaderboard]] — His flagship benchmarking project
- [[Hallucination-Index]] — His industry-cited hallucination tracking
- [[LLM-as-a-Judge]] — His approach to evaluation without ground truth
- [[RAG]] — Retrieval-augmented generation, covered in his ebooks
- [[Multi-Agent-Systems]] — His architectural expertise
- [[Galileo-AI]] — His current company
- [[Semantic-Search]] — His earlier engineering work

## Sources

- Substack: https://pakodas.substack.com
- GitHub: https://github.com/bhavsarpratik
- LinkedIn: https://www.linkedin.com/in/bhavsarpratik
- Hugging Face: https://huggingface.co/pratikbhavsar
- Agent Leaderboard v2: https://huggingface.co/blog/pratikbhavsar/agent-leaderboard-v2
- Agent Leaderboard collection: https://huggingface.co/collections/pratikbhavsar/agent-leaderboard-67c03062f856fd8ddbca2b80
- Galileo blog: https://galileo.ai/blog/agent-leaderboard-v2
- Galileo ebooks: https://www.galileo.ai/ebook-mastering-agents
- Hallucination Index: https://github.com/rungalileo/hallucination-index
- Maxpool: https://maximalists.ai/
- IIT Bombay profile: https://www.ese.iitb.ac.in/student/pratik-bhavsar
