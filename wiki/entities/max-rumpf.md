---
title: Max Rumpf
type: entity
aliases: [Maximilian-David Rumpf, maxrumpf]
created: 2026-05-13
updated: 2026-05-13
status: L2
sources: [https://maxrumpf.com/, https://www.sid.ai/, https://www.sid.ai/research/sid-1, https://www.sid.ai/research/sid-1-technical-report, https://x.com/maxrumpf, https://ycombinator.com/companies/sid]
tags:
  - person
  - lab
  - search
  - reinforcement-learning
  - training
  - blogger
  - x-account
  - ycombinator

---

# Max Rumpf

Max Rumpf (Maximilian-David Rumpf) is CEO and Co-founder of SID.ai. He leads an AI search and information retrieval research lab and led the development of SID-1. He began his career researching AI accelerator design at ETH Zurich and founded SID during the YC S23 batch. SID-1 is the first end-to-end RL-trained model for agentic retrieval, gaining attention as a search-specialized model using GRPO.

## Profile

| Field | Details |
|------|------|
| Name | Maximilian-David "Max" Rumpf |
| Role | CEO / Co-founder, SID.ai |
| Location | San Francisco, CA |
| X | [@maxrumpf](https://x.com/maxrumpf) (1,125 posts, ~2,456 followers) |
| LinkedIn | [/in/maximiliandavid](https://linkedin.com/in/maximiliandavid) |
| Personal Site | [maxrumpf.com](https://maxrumpf.com/) |

## Career

### ETH Zurich (2020-2023)
As a researcher at SAFARI Research Group, worked on AI accelerator design under a professor who developed Google's TPU architecture. Also served as a Teaching Assistant for the information security and cryptography research group. Co-founded SID while pursuing his CS Master's degree.

### Studienstiftung des deutschen Volkes (2018-2023)
Awarded the German National Academic Foundation scholarship (awarded to top 0.5% of German students).

### SID.ai (2022-present)
Co-founded SID in 2022 with Lotte Seifert (COO) and Lukas Ruflair. Accepted into YC S23 batch. An AI search research lab with offices in San Francisco and Zurich.

## SID.ai

An AI research lab with the motto "Solving retrieval one model at a time." Raised $500K in pre-seed funding in May 2023. Investors include Y Combinator, Canaan, Rebel, and General Catalyst. Individual investors/advisors include researchers from Anthropic, DeepMind, OpenAI, MIT, Cognition, Cursor, Applied Compute, Prime Intellect, Standard Intelligence, and Jeff Dean.

### Pivot History
- **Early 2023**: B2C personal data search "Sid Search" (positioned as "Stripe for data")
- **Mid 2023 (around YC)**: Pivoted to RAG / data connectors - "Serverless RAG to connect AI to company, industry, or person-specific data"
- **Late 2025**: SID-1 announced - transition from general RAG provider to retrieval-specialized model research lab

## SID-1 (December 2025)

SID-1 is the first model trained end-to-end with reinforcement learning (RL) for **agentic retrieval**, using a modified version of Magistral's GRPO without SFT.

**Difference from traditional search pipelines**: Rather than a fixed pipeline of query rewriting, search, and reranking, SID-1 iteratively searches, reads results, and refines queries like a human - repeating as many times as needed.

### Performance Comparison

| Model | Recall | Time | Cost/Query |
|--------|--------|----------|------------|
| **SID-1 (4x)** | **0.84** | 5.5s | $0.0014 |
| SID-1 | 0.77 | 5.5s | $0.00062 |
| GPT-5.1 (high) | 0.78 | 131s | $0.24 |
| Gemini 3 Pro | 0.66 | 156s | $0.12 |
| Sonnet 4.5 | 0.64 | 35s | $0.54 |
| Reranker @10 | 0.45 | 0.78s | $0.00061 |
| Vector only @10 | 0.44 | 0.15s | $0.0000098 |

**Key Metrics**:
- **24x faster** than GPT-5.1 (5.5s vs 131s), **3-4 orders of magnitude lower cost**
- **~2x recall** vs traditional reranking pipelines (0.45 to 0.84)
- **Drop-in compatible** with existing search systems, operates as a frontier model sub-agent
- Available via API, AWS Bedrock, and self-hosting

## Notable Essays

### Robots Might Be 1000x Harder Than Superintelligence (October 2024)
A reinterpretation of Moravec's Paradox. The human brain has optimized object manipulation and spatial movement over millions of years, but mathematics has only about 1,000 years of history. In ML terms, 'math is out-of-distribution for the monkey brain.' Foundational tasks like navigation and object manipulation may be 1,000x harder than math, but humans are so good at them that the complexity is invisible.

> "A good razor is that if our ancestors were doing it millions of years ago, it could be hard for AI. If the task is only thousands of years old, it's most likely pretty easy."

### Just-In-Time Coding (August 2024)
Extends the concept of JIT compilation to AI code generation, envisioning a world where code is written during program execution. A React button is ~100 tokens; on Groq, TTFT 200ms + 500 tokens/s = ~400ms. Faster than a Salesforce button. Scalable from buttons to pages to full applications.

> "The code only gets written during the execution of the program."

### N-of-1 Software (August 2024)
A vision of AI transforming software from "n-of-1-billion" to "n-of-1." Excel's advantage over SaaS is customizability - AI brings that to all software.

> "AI lets us create n-of-1 software: Software that only serves a single person."

### Amdahl's Argument for AI (April 2024, X Thread)
Applies Amdahl's Law to AI productivity. The productivity ceiling of AI apps is bounded by the portion of workflow requiring human intervention. Human processing speed is ~1-3 tokens/sec and practically cannot be accelerated.

### Arxiv Might Kill Small Universities and Labs (May 2024, X Thread)
While acknowledging arXiv's open access value, questions the secondary impact of unfiltered publishing on academia's trust structures.

## Quotes & Ideas

### RL Framework Instability (December 2025, Pinned Post)
> "Most RL frameworks are fundamentally unstable. We wasted more H100 hours on debugging this than any other issue for our multi-turn, multi-env RL run. When using OpenAI-style messages for env interactions, parsing and retokenizing leads to subtly different tokens."

Practical challenges faced during SID-1's GRPO multi-turn RL training, noting how subtle tokenization differences undermine training stability.

### Enterprise AI and Search
On Lukas Petersson's Audio Tokens podcast, in relation to the debate about horizontal AI replacing vertical AI, argued that effective search systems are essential for autonomous AI to access private data.

## Podcast Appearances

| Date | Show | Topic |
|------|------|--------|
| July 2024 | High Agency: The Podcast for AI Builders (Ep.6) | Advanced RAG systems, chunking strategies, hybrid search, knowledge graph limits, reranking |
| March 2025 | Audio Tokens (Ep.9, Lukas Petersson) | AI agent bottlenecks, enterprise AI adoption, Europe vs SF |
| May 2023 | Before They Change The World | Stripe for data, pre-YC founding story |

## Related Pages

- [[sid-1]] - SID first agentic retrieval model
- [[grpo]] - Group Relative Policy Optimization
- [[agentic-retrieval]] - Agentic information retrieval
- [[magistral]] - Developer of the modified GRPO used for SID-1 training
- [[moravecs-paradox]] - Foundation concept for "Robots Might Be 1000x Harder"
- [[amdahls-law]] - Theoretical foundation for Amdahl's Argument for AI
- [[rag]] - Retrieval-Augmented Generation where Max has deep expertise
