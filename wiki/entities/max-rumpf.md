---
title: Max Rumpf
type: entity
aliases: [Maximilian-David Rumpf, maxrumpf]
created: 2026-05-13
updated: 2026-08-15
status: L3
sources: [https://maxrumpf.com/, https://www.sid.ai/, https://www.sid.ai/research/sid-1, https://www.sid.ai/research/sid-1-technical-report, https://x.com/maxrumpf, https://ycombinator.com/companies/sid, https://maxrumpf.com/writing/2026-07-04-only-one-superintelligence.html, raw/articles/2026-07-04_maxrumpf_only-one-superintelligence.md]
tags:
  - person
  - lab
  - search
  - reinforcement-learning
  - training
  - blogger
  - x-account
  - ycombinator
  - superintelligence
related:
  - concepts/agentic-search
  - concepts/post-training/grpo
  - entities/sid
  - entities/turbopuffer
  - concepts/retrieval-augmented-generation

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

### Will There Be Only One Superintelligence? (July 2026)
Questions the "winner-take-all" singularity narrative: the story that the first superintelligence compounds its lead until it alone controls everything assumes the leader can predict the future well enough to pick optimal research directions. But superintelligence is itself the largest and most irreducible source of uncertainty about the future — a lesser intelligence cannot predict a greater one, including its own descendants and its rivals' future versions. Uncertainty doesn't make a maintained lead impossible, but it's not a foregone conclusion. Notable for coming from a hard-nosed RL/search practitioner rather than an AI-safety theorist.

> "A lesser intelligence cannot predict a greater one. Its own descendants will be smarter than it is now, so it cannot know what they will do or which strategy is optimal for producing them."

## SID-1 Training Infrastructure & SID-2 (2026)

In May 2026, Rumpf and SID researcher Sam Dauncey published a detailed guest post on the turbopuffer blog describing how SID-1 was trained at scale — and disclosed that **SID-2 is already in training**. Key facts:

- **RL rollout scale**: 256 questions × 16 attempts = 4,096 rollouts per training step, >1,000 steps, up to ~81,920 searches per step with 1k+ QPS bursts in the opening ~10s window of each step
- **Corpora**: 10M+ document indexes spanning finance, science, legal, email, and general knowledge (5,000 curated abstracts to internet scale)
- **Search backend**: SID migrated to [[entities/turbopuffer]] because search latency bottlenecked GPU utilization — its stateless query tier over object storage absorbs bursty RL traffic
- **Emergent tool preferences**: SID-1 learned to prefer ANN over BM25, uses HyDE (hypothetical document embeddings) natively, issues parallel overdetermined/underdetermined keyword mixes, and never fully abandons BM25
- **SID-2**: In training as of May 2026, expected to extend SID-1's speed and recall advantages beyond the current frontier LLM generation

Rumpf frames the meta-lesson: "If RL makes a model prefer some tool, it is likely a better tool" — an AlphaGo-style argument that learned tool preferences can outperform expert-designed pipelines. See [[concepts/agentic-search]] for the full RL infrastructure analysis and [[entities/sid]] for the company entity.

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

- [[concepts/sid-1]] - SID first agentic retrieval model
- [[concepts/post-training/grpo]] - Group Relative Policy Optimization
- [[concepts/agentic-retrieval]] - Agentic information retrieval
- Magistral - Developer of the modified GRPO used for SID-1 training (no wiki page yet)
- Moravec's Paradox - Foundation concept for "Robots Might Be 1000x Harder" (no wiki page yet)
- Amdahl's Law - Theoretical foundation for Amdahl's Argument for AI (no wiki page yet)
- [[concepts/retrieval-augmented-generation]] - Retrieval-Augmented Generation where Max has deep expertise
- [[entities/sid]] - SID AI company entity (SID-1, SID-2, platform)
- [[entities/turbopuffer]] - Search backend used for SID-1 RL training
- [[concepts/agentic-search]] - Full agentic search concept (SID-1 as core reference implementation)

## Sources

- [maxrumpf.com](https://maxrumpf.com/) — Personal site and essays
- [Will There Be Only One Superintelligence?](https://maxrumpf.com/writing/2026-07-04-only-one-superintelligence.html) (July 2026) — [[raw/articles/2026-07-04_maxrumpf_only-one-superintelligence]]
- [Training SID-1 to beat GPT-5 at search with 1k+ QPS RL rollouts](https://turbopuffer.com/blog/reinforcement-learning-sid-ai) (May 2026, with Sam Dauncey) — [[raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai]]
- [SID-1 research page](https://www.sid.ai/research/sid-1) — [[raw/articles/2025-12-04_sid-1-agentic-retrieval]]
- [SID-1 Technical Report](https://www.sid.ai/research/sid-1-technical-report)
- [X: @maxrumpf](https://x.com/maxrumpf)
