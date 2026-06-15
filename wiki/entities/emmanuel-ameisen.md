---
title: "Emmanuel Ameisen"
tags:
  - person
  - anthropic
  - fine-tuning
  - post-training
  - training
  - evaluation
  - interpretability
  - ml-education
  - applied-ml
created: 2026-06-15
updated: 2026-06-15
type: entity
aliases:
  - "@hundredblocks"
sources:
  - raw/articles/2024-01-24_emeisen_why-fine-tuning-is-dead.md
  - https://github.com/hundredblocks
  - https://github.com/hundredblocks/ml-powered-applications
  - https://www.oreilly.com/library/view/building-machine-learning/9781492045106/
  - https://www.youtube.com/watch?v=ctss0hcD9SE (Chai Time Data Science, ~2020)
  - https://www.youtube.com/watch?v=NxiqmQwKir8 (ZenML, ~2022)
  - https://hamel.dev/blog/posts/workshops/ (ML/LLM workshop series)
---

# Emmanuel Ameisen

**Emmanuel Ameisen** (GitHub: [@hundredblocks](https://github.com/hundredblocks)) is an ML practitioner, author, and researcher currently working at **Anthropic** on fine-tuning and interpretability. He is the author of *Building Machine Learning Powered Applications* (O'Reilly, January 2020), a practical guide to training and deploying ML models that has become a standard reference in applied ML. He is based in San Francisco, CA.

Ameisen's career spans ~10 years across data science, ML education, applied ML at **Stripe**, and research at **Anthropic**. He is known for his pragmatic, data-first approach to ML engineering and his skepticism toward "cool" techniques in favor of boring but effective solutions — a philosophy he articulates most clearly in his widely-discussed 2024 talk "Why Fine-Tuning is Dead."

## Career Timeline

### Zipcar (~2014–2016)
Early ML engineering work at the car-sharing company. Focused on practical, production-oriented ML solutions for operational problems. This period established his reputation for building end-to-end ML systems rather than just models.

### Insight Data Science / Insight Fellows (~2016–2018)
Transitioned into ML education, leading programs that helped PhDs and professionals transition into data science careers. This experience directly informed his book and his focus on teaching practical, production-ready ML. The program covered common pitfalls in ML development, MVP design patterns, and the gap between academic ML and production reality.

### Stripe — Staff Manager, ML (~2018–2023)
At Stripe, Ameisen led ML teams working on some of the most demanding production ML problems:
- **Credit card fraud detection**: Built systems that had to operate at massive scale with strict latency and accuracy requirements
- **Parental control ML systems**: Applied ML to safety-critical content filtering
- **ML infrastructure**: Focused on making ML accessible and reliable across the organization

During his time at Stripe, he gave talks at ZenML and Chai Time Data Science, sharing lessons from production ML deployment. His Stripe work reinforced his philosophy that 80% of ML work is data work — collection, labeling, cleaning — and that model choice is secondary to data quality.

### Anthropic — Research/Engineering (~2023–Present)
At Anthropic, Ameisen works on:
- **Fine-tuning**: Developing and evaluating fine-tuning approaches for Claude models
- **Interpretability**: Understanding how LLMs work internally, contributing to Anthropic's broader interpretability research program

His work at Anthropic has given him a unique vantage point: he fine-tunes frontier models for a living, yet argues that fine-tuning is becoming less necessary. This tension — being an expert in a technique while publicly questioning its importance — is central to his credibility on the topic.

## Writing: Building Machine Learning Powered Applications

**Book**: *Building Machine Learning Powered Applications: Going from Idea to Product*
**Publisher**: O'Reilly Media (January 2020)
**Pages**: 257
**Level**: Beginner to intermediate
**Companion repo**: [github.com/hundredblocks/ml-powered-applications](https://github.com/hundredblocks/ml-powered-applications) (714 stars)

### Book Structure
The book follows a case study approach — building an ML-powered writing assistant — through four major parts:

**Part I: Find the Correct ML Approach**
- From product goal to ML framing
- Estimating what's possible with models vs. rules
- Creating a plan: measuring success, handling distribution shift
- The importance of starting simple

**Part II: Build a Working Pipeline**
- End-to-end scaffolding and prototyping
- Dataset acquisition and exploration
- Iterative feature engineering from patterns

**Part III: Iterate on Models**
- Training and evaluation: looking beyond accuracy
- Debugging ML: wiring, training, generalization
- Using classifiers for writing recommendations
- Feature importance and model interpretability

**Part IV: Deploy and Monitor**
- Deployment options: server-side, streaming, batch, client-side
- Safeguards: handling failures, adversarial inputs, bias
- Monitoring: performance metrics, CI/CD for ML, A/B testing

### Key Themes from the Book
These themes prefigure his later "fine-tuning is dead" argument by several years:
- **Always start with the simplest approach** that could work
- **Data work dominates** — most ML time is spent on data, not modeling
- **Feedback loops are critical** — production models need monitoring and continuous improvement
- **Deployment considerations should drive design** — think about scale, latency, and failure modes from the start

## Speaking & Education

### Podcasts & Talks
| Venue | Title | Year | Focus |
|-------|-------|------|-------|
| [Chai Time Data Science](https://www.youtube.com/watch?v=ctss0hcD9SE) | Building ML Powered Apps | ~2020 | Career journey, Zipcar → Insight → Stripe, common ML pitfalls |
| [ZenML](https://www.youtube.com/watch?v=NxiqmQwKir8) | Practical Production ML | ~2022 | Failure modes, metrics, AutoML, feature stores, shadow infrastructure |
| [TWIML AI Podcast #349](https://www.youtube.com/watch?v=nibkQOX7GPs) | Turning Ideas into ML Products | ~2020 | Product-focused ML development |
| Hamel Husain's ML/LLM Workshop | Why Fine-Tuning is Dead | Jan 2024 | The fine-tuning vs. RAG/prompting debate |

### Education Philosophy
Ameisen's approach to ML education is characterized by:
- **Concrete examples over abstract theory** — every concept is illustrated with code and real datasets
- **Progressive complexity** — start with the simplest possible solution, iterate only when needed
- **Production-first mindset** — teach what works in production, not what's novel in papers
- **Interviewing practitioners** — the book includes interviews with industry leaders (Chris Harland, Chris Moody, Robert Munro, Bruno Guisard)

## Open Source Projects

| Repository | Stars | Description |
|------------|-------|-------------|
| [concrete_NLP_tutorial](https://github.com/hundredblocks/concrete_NLP_tutorial) | 1.1k | NLP workshop about concrete solutions to real problems |
| [ml-powered-applications](https://github.com/hundredblocks/ml-powered-applications) | 714 | Companion repo for the O'Reilly book |
| [transcription_demo](https://github.com/hundredblocks/transcription_demo) | 261 | Speech-to-text demonstration |
| [semantic-search](https://github.com/hundredblocks/semantic-search) | 203 | Semantic search for images and text using neural networks |
| [large-model-parallelism](https://github.com/hundredblocks/large-model-parallelism) | 95 | Functional local implementations of model parallelism approaches |
| [insight-accent](https://github.com/hundredblocks/insight-accent) | 6 | Voice transformation demo |

## Key Positions

### "Fine-Tuning is Dead" (2024)
In a widely-discussed talk at [Hamel Husain's ML/LLM workshop](https://hamel.dev/blog/posts/workshops/), Ameisen argued that fine-tuning is becoming less necessary as a primary tool for adapting LLMs:

**Core argument structure:**
1. **Fine-tuning is not for adding knowledge** — if the model doesn't know about your business, the solution is to tell it (via RAG or prompting), not to fine-tune it
2. **RAG dominates knowledge tasks** — papers comparing fine-tuning vs. RAG show RAG delivers ~90% of the improvement; fine-tuning adds marginal gains (e.g., 63.13 → 63.29)
3. **The "moving target" problem** — domain-specific models (like BloombergGPT) get overtaken by next-gen frontier models within months
4. **Price/context trends eliminate the advantage** — model prices dropped from ~$60/M tokens (2021) to ~$0.50/M tokens (2024); context windows grew from 2K to 1M+. If trends continue, most fine-tuning becomes unnecessary
5. **Fine-tuning's remaining niche**: extreme context requirements, style/format enforcement, latency-constrained applications

**Nuance:** The "fine-tuning is dead" headline is deliberately provocative. Ameisen's actual position is more precise: fine-tuning goes from being 50% of the effort to 5% of the effort for most use cases. It's not dead — it's marginalized to specific niches where prompting and RAG can't reach.

### Practical ML Philosophy
Across his book, talks, and workshop presentations, Ameisen consistently advocates:
- **"Be afraid of anything that sounds cool"** — the boring thing almost always delivers more value in production
- **Evals → prompts → dynamic few-shot → RAG → (maybe) fine-tuning** — this is the correct order of operations, not the reverse
- **80% of ML work is data work** — collection, labeling, cleaning — regardless of whether you fine-tune
- **Start simple, iterate** — the simplest model that works is the best model
- **People skip data work and go straight to fine-tuning as a "side quest"** — this is the most common mistake he sees

### Anthropic Perspective on Fine-Tuning
Working at Anthropic gives Ameisen a unique vantage point: he fine-tunes frontier models professionally while publicly questioning their necessity. This tension is productive — it means his "fine-tuning is dead" argument comes from someone who knows fine-tuning intimately and still concludes it's overused.

Key insights from his Anthropic work:
- **Prefix caching** (Anthropic's implementation) changes the cost equation — if fine-tuning data can be a cached prefix, the advantage of weight-encoding diminishes
- **Fine-tuning larger models seems to get less effective** — an anecdotal but consistent observation across practitioners
- **Dynamic few-shot examples** (RAG over a database of examples) is an increasingly common pattern that replaces fine-tuning for many use cases

## Professional Profile

| Attribute | Detail |
|-----------|--------|
| **Name** | Emmanuel Ameisen |
| **GitHub** | [@hundredblocks](https://github.com/hundredblocks) |
| **Location** | San Francisco, CA, United States |
| **Current Role** | Research/Engineering at Anthropic (fine-tuning + interpretability) |
| **Previous** | Staff Manager at Stripe (ML), ML Education at Insight Data Science |
| **Book** | *Building Machine Learning Powered Applications* (O'Reilly, 2020) |
| **GitHub Followers** | 418 |
| **Years Active** | ~2014 – Present |
| **Key Topics** | Fine-tuning, RAG, ML education, production ML, interpretability |

## Related Entities & Concepts

- [[entities/hamel-husain|Hamel Husain]] — hosted the workshop where Ameisen gave the "Why Fine-Tuning is Dead" talk
- [[entities/chip-huyen|Chip Huyen]] — fellow ML educator and author of *Designing Machine Learning Systems*
- [[entities/anthropic|Anthropic]] — current employer, working on fine-tuning and interpretability
- [[entities/stripe|Stripe]] — previous employer, led ML teams for fraud detection and safety
- [[concepts/post-training/_index|Post-Training]] — comprehensive fine-tuning coverage
- [[concepts/rag|RAG]] — the primary alternative to fine-tuning for knowledge tasks
- [[concepts/context-engineering|Context Engineering]] — prompting, few-shot, and RAG as alternatives to weight updates

## Sources

- "Why Fine-Tuning is Dead" talk, Hamel Husain's ML/LLM workshop (Jan 24, 2024) — [[raw/articles/2024-01-24_emeisen_why-fine-tuning-is-dead]]
- *Building Machine Learning Powered Applications*, O'Reilly Media (January 2020) — [oreilly.com](https://www.oreilly.com/library/view/building-machine-learning/9781492045106/)
- GitHub profile: [github.com/hundredblocks](https://github.com/hundredblocks) (418 followers, 9 repos, Arctic Code Vault Contributor)
- Chai Time Data Science interview: [youtube.com/watch?v=ctss0hcD9SE](https://www.youtube.com/watch?v=ctss0hcD9SE)
- ZenML interview: [youtube.com/watch?v=NxiqmQwKir8](https://www.youtube.com/watch?v=NxiqmQwKir8)
- TWIML AI Podcast #349: [youtube.com/watch?v=nibkQOX7GPs](https://www.youtube.com/watch?v=nibkQOX7GPs)
