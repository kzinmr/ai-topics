---
title: Eugene Yan
type: entity
handle: "@eugeneyan"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ml-engineering
  - recsys
  - llm-systems
  - production-ai
sources: []
---


# Eugene Yan (@eugeneyan)

| | |
|---|---|
| **X** | [@eugeneyan](https://x.com/eugeneyan) |
| **Blog** | [eugeneyan.com/writing](https://eugeneyan.com/writing) |
| **GitHub** | [eugeneyan](https://github.com/eugeneyan) |
| **Role** | Member of Technical Staff, Anthropic (formerly Principal Applied Scientist, Amazon) |
| **Known for** | "Applied LLMs" guide, LLM production patterns, recommender systems expertise, practical ML writing |
| **Bio** | Eugene Yan (Ziyou Yan) is a Member of Technical Staff at Anthropic, where he works to bridge the field and the frontier in building safe, reliable AI systems at scale. Previously a Principal Applied Scientist at Amazon, he built real-time retrieval, bandit rankers, and recommendation systems. He is the lead author of the widely-read "What We've Learned From A Year of Building with LLMs" guide and maintains one of the most practical ML blogs in the industry. |

## Overview

Eugene Yan is among the most pragmatic and grounded voices in applied machine learning. His career spans e-commerce ML at Alibaba/Lazada, healthtech at a Series A startup, recommendation systems at Amazon, and now AI safety and production at Anthropic. This breadth of experience — from building ML systems in emerging markets to working at the frontier of AI development — gives him a uniquely practical perspective on what works and what doesn't in production AI.

Yan's writing is distinguished by its emphasis on *shipping*. While many AI thought leaders focus on model capabilities or theoretical advances, Yan consistently brings the conversation back to production reality: evaluation, monitoring, data pipelines, cost management, and team organization. His blog at eugeneyan.com is a masterclass in applied ML, with over 200 posts spanning recommender systems, LLM engineering, leadership, and career development.

His most influential contribution is arguably the ["Applied LLMs"](https://applied-llms.org/) guide — "What We've Learned From A Year of Building with LLMs" — co-authored with Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, and Shreya Shankar. This comprehensive document, published in mid-2024, became the de facto reference for engineering teams looking to move beyond AI demos into production systems. It is organized into three layers: tactical (prompting, RAG, evals), operational (team building, iteration processes), and strategic (business alignment, product-market fit).

Yan currently writes a newsletter reaching 11,800+ readers on RecSys, LLMs, and engineering lessons. He has spoken at major conferences including the AI Engineer World's Fair, Netflix PRS Workshop, and numerous others.

## Core Ideas

### Seven Patterns for Building LLM Systems

In his landmark July 2023 post ["Patterns for Building LLM-based Systems & Products"](https://eugeneyan.com/writing/llm-patterns/), Yan identified seven key patterns, organized along two axes: improving performance vs. reducing cost/risk, and closer to data vs. closer to user:

1. **Evals** — The foundation: "Building solid evals should be the starting point for any LLM-based system or product (as well as conventional machine learning)." You can't improve what you can't measure.
2. **RAG (Retrieval-Augmented Generation)** — Adding recent, external knowledge to ground LLM outputs and reduce hallucinations
3. **Fine-tuning** — Getting better at specific tasks when prompting and RAG aren't sufficient
4. **Caching** — Reducing latency and cost for repeated or similar queries
5. **Guardrails** — Ensuring output quality, safety, and compliance
6. **Defensive UX** — Anticipating and managing errors gracefully at the user interface level
7. **Feedback Collection** — Continuously gathering user signals to improve the system

> 詳細は [[concepts/llm-patterns-eugene-yan]] を参照 — 各パターンの実装詳細、フレームワークの進化（v1→v2）、既存Wikiページへのマッピングをカバー。

These patterns map to Yan's broader philosophy that LLM applications succeed or fail based on system design, not model capability alone.

### Evals as the Foundation

> *"Evals help us understand if our prompt engineering, retrieval augmentation, or finetuning is on the right track. Consider it eval-driven development, where your evals guide how you build your system and product."*

In his October 2023 AI Engineer Summit keynote, Yan argued that annotation guidelines — the documents that guide human labelers — are one of the most valuable assets an ML team can build. Well-crafted guidelines improve both human consistency and model instructions, and can later seed fine-tuning datasets.

> *"Eyeballing doesn't scale — it's good as a final vibe check, but it doesn't scale."*

This insight has proven increasingly important as teams discover that their intuition about model quality diverges sharply from systematic evaluation.

### The Demo-to-Production Reality Gap

> *"There is a large class of problems that are easy to imagine and build demos for, but extremely hard to make products out of. For example, self-driving. It's easy to demo a car self-driving around a block but making it into a product takes a decade."* (citing Andrej Karpathy)

Yan consistently emphasizes that production ML is about much more than model accuracy:
- **Don't underestimate the effort it takes to go from demo to production**
- **Scale makes everything harder** — Each 10x increase in traffic uncovers new bugs
- **LLM economics depend on scale** — "Even the most expensive LLMs are not that expensive for B2B scale; even the cheapest LLMs are not that cheap for consumer scale." (citing Will Larson)
- **The real bottlenecks aren't cost — they're trust, reliability, security**

### Product Evals in Three Simple Steps

In his November 2025 post ["Product Evals in Three Simple Steps"](https://eugeneyan.com/writing/product-evals/), Yan distilled the eval process:

1. **Labeling a small dataset** — Start with real defects that actually affect users, not synthetic examples
2. **Aligning LLM evaluators** — Ensure automated judges correlate with human judgment
3. **Running the eval harness** — Create a reproducible pipeline for continuous measurement

> *"I recently observed a team invest ~4 weeks into building their eval dataset and LLM-as-judge pipeline. That investment paid off by tightening the feedback loop and helping them iterate faster. That is the benefit of having product evals; not just to measure and improve the quality of the product, but to tighten the feedback loop."*

### LLM-as-Judge Won't Save The Product—Fixing Your Process Will

In his April 2025 post, Yan challenged the industry's over-reliance on automated evaluation:

- LLM judges are themselves models with biases and limitations
- The real differentiator is the *process* of building, testing, and iterating
- Human evaluation remains essential, even when expensive
- Evaluation should drive product decisions, not just model selection

### Recommender Systems in the Age of LLMs

In his March 2025 post ["Improving Recommendation Systems & Search in the Age of LLMs"](https://eugeneyan.com/writing/recsys-llm/), Yan explored how LLMs are transforming recommendation systems:

- **LLM/multimodal-augmented model architectures** — Combining language models with traditional recsys approaches
- **Scaling laws** — Performance consistently improves as model and dataset size expand
- **Knowledge distillation** — Transferring insights from large models to smaller, efficient ones
- **Cross-domain transfer learning** — Handling limited data scenarios
- **Parameter-efficient fine-tuning** — Techniques like LoRAs for domain adaptation
- **Semantic IDs** — Using semantically meaningful tokens instead of random hash IDs, enabling LLM-recommender hybrids that can both converse and recommend

### 39 Lessons on Building ML Systems

In his November 2024 post, Yan synthesized lessons from multiple ML conferences:

**Building effective ML systems:**
1. The real world is messy — define reward functions, handle edge cases
2. You don't always need machine learning — heuristics and SQL are valuable baselines
3. Set realistic expectations — many problems have a ceiling, especially those involving human behavior
4. Don't overlook time — user preferences change, inventory gets drawn down
5. Evals are a differentiator and moat
6. Build with an eye toward the future — flexibility beats specialization
7. It takes a village — infra, engineering, data, ML, design, product, business

**Production and scaling:**
- Each 10x-ing of scale uncovers new bugs
- Execution is everything — navigating from legacy systems to high velocity
- Start simple and iterate

## Key Work

### Applied LLMs Guide

["What We've Learned From A Year of Building with LLMs"](https://applied-llms.org/) (June 2024) — Co-authored with Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, and Shreya Shankar. Published on O'Reilly Media in three parts (Tactical, Operational, Strategic). The guide covers:

- **Tactical:** Prompting, RAG, flow engineering, evals, monitoring
- **Operational:** Team building, iteration processes, organizational challenges
- **Strategic:** Business alignment, product-market fit, competitive positioning

### Notable Blog Posts (eugeneyan.com/writing)

| Date | Title | Topic |
|---|---|---|
| Dec 2025 | "2025 Year in Review" | Annual reflection and lessons |
| Nov 2025 | "Product Evals in Three Simple Steps" | Building evaluation pipelines |
| Nov 2025 | "Advice for New Principal Tech ICs" | Career guidance for senior engineers |
| Sep 2025 | "Training an LLM-RecSys Hybrid for Steerable Recs with Semantic IDs" | Prototype combining LLMs with recommendation |
| Jun 2025 | "Evaluating Long-Context Question & Answer Systems" | LLM evaluation methodology |
| May 2025 | "Exceptional Leadership: Some Qualities, Behaviors, and Styles" | Engineering leadership |
| Apr 2025 | "An LLM-as-Judge Won't Save The Product—Fixing Your Process Will" | Evaluation philosophy |
| Mar 2025 | "Improving Recommendation Systems & Search in the Age of LLMs" | RecSys + LLM integration |
| Aug 2024 | "Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)" | Automated evaluation analysis |
| Jul 2024 | "How to Interview and Hire ML/AI Engineers" | Hiring best practices |
| May 2024 | "What We've Learned From A Year of Building with LLMs" | Applied LLMs guide |
| May 2024 | "Prompting Fundamentals and How to Apply them Effectively" | Prompt engineering |
| Nov 2024 | "39 Lessons on Building ML Systems, Scaling, Execution, and More" | Conference takeaways |
| Jul 2023 | "Patterns for Building LLM-based Systems & Products" | The seven-pattern framework |

### Speaking Engagements

- **AI Engineer World's Fair 2024** — Keynote: "What We Learned from a Year of LLMs"
- **AI Engineer 2025** — "Improving RecSys & Search with LLM techniques"
- **Netflix PRS Workshop 2024** — "Applying LLMs to Recommendation Experiences"
- **AI Engineer Summit 2023** — Keynote: "Building Blocks for LLM Systems"
- Multiple other conference talks on ML engineering and LLM production

### Open Source Projects

- **applied-llms.org** — The Applied LLMs guide
- **applyingml.com** — Papers, guides, and interviews on applying ML effectively
- **applied-ml** — Curated papers on real-world ML systems in industry

### Prototypes

- **Semantic IDs:** Training an LLM-RecSys hybrid for steerable recommendations
- **News Agents:** Automating daily news via agentic workflows
- **AI Reading Club:** Prototyping an AI-powered reading experience
- **LLM UXs:** Interacting with LLMs with minimal chat interfaces

## Blog / Recent Posts

Eugene Yan's blog at [eugeneyan.com/writing](https://eugeneyan.com/writing) has published 209+ posts totaling 420,000+ words. Key themes include:

- **ML Engineering** — Practical guidance on building, deploying, and scaling ML systems
- **LLM Production** — Patterns, anti-patterns, and lessons from building with foundation models
- **Recommender Systems** — Architecture, evaluation, and LLM integration
- **Engineering Leadership** — Hiring, team building, career development for tech ICs
- **Evaluation & Quality** — Evals, LLM-as-judge, annotation guidelines
- **Career & Writing** — Reflections on professional growth and the craft of technical writing

## Related People

- **Chip Huyen** — Both focus on production ML and engineering; Huyen more on systems design, Yan on LLM application patterns
- **Ethan Mollick** — Both write about practical AI usage; Mollick from business/education, Yan from engineering/production
- **Lilian Weng** — Both address LLM capabilities and production; Weng from research, Yan from applied engineering
- **Bryan Bischof** — Co-author on the Applied LLMs guide
- **Hamel Husain** — Co-author on the Applied LLMs guide
- **Shreya Shankar** — Co-author on the Applied LLMs guide; shares focus on ML evaluation
- **Andrej Karpathy** — Both cite Karpathy's "demo to production" insight; both value practical engineering
- **Samuel Colvin** — Both work on production-grade AI tools; Colvin on type safety, Yan on evaluation and patterns

## X Activity Themes

Eugene Yan's X/Twitter activity focuses on:

- **ML Engineering Best Practices** — Practical advice from years of production experience
- **LLM System Patterns** — Sharing insights on RAG, evals, fine-tuning, and guardrails
- **Recommender Systems** — Updates on RecSys research and LLM integration
- **Engineering Leadership** — Advice for senior tech ICs and engineering managers
- **Career Development** — Lessons on hiring, growth, and navigating the tech industry
- **Technical Writing** — Reflections on the craft of writing about ML and AI
- **Conference Takeaways** — Summarizing key lessons from ML conferences
- **Prototype Updates** — Sharing experimental work on LLM-RecSys hybrids and agentic workflows

## See Also

- [[entities/_index]]
