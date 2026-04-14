---
tags: [person]
---


# Eugene Yan (Ziyou Yan)

**URL:** https://eugeneyan.com
**Blog:** eugeneyan.com
**Twitter/X:** @eugeneyan
**GitHub:** https://github.com/eugeneyan (4.8K followers, 80 public repos)
**Position:** Member of Technical Staff @ Anthropic (2026–Present)
**Education:** BSc Psychology & Organisation Behaviour (Singapore Management University); MSCS (Georgia Tech OMSCS)
**Notable Projects:** applied-ml (28.7K stars), open-llms (12.7K stars), ml-surveys (2.9K stars)

## Overview

Eugene Yan (Ziyou) is a practitioner-scholar who has become one of the most influential voices on building production machine learning systems and, more recently, on applying large language models at scale. His journey is unconventional: a psychology graduate who self-taught programming and data science, rose through IBM, Lazada/Alibaba, a healthtech startup, and Amazon (Principal Applied Scientist), before joining **Anthropic as a Member of Technical Staff** in 2026.

Yan's work is defined by its practical, hands-on orientation. Unlike many AI researchers who work in academic isolation, Yan has shipped ML systems that serve real customers at scale across e-commerce, healthcare, workforce analytics, and AI products. His blog at eugeneyan.com — over 209 posts, 31 talks, 19 prototypes, and 420K+ words — is widely regarded as one of the most valuable resources for ML practitioners, bridging the gap between cutting-edge research and production engineering.

His GitHub repositories have become essential community resources: **applied-ml** (28.7K stars) curates papers and tech blogs from companies sharing their real-world ML work; **open-llms** (12.7K stars) tracks commercially usable open-source language models. Both are go-to references for engineering teams building ML products.

Yan's influence extends through his newsletter (11,800+ readers) and his consistent focus on what he calls the "ghost knowledge" of applied ML — the practical, unwritten lessons that only emerge from shipping systems in production. His 2025 transition to Anthropic positions him at the frontier of AI research while maintaining his commitment to practical, customer-serving systems.

His career philosophy centers on three principles: continuous self-learning, delivering tangible value, and empathic communication — all of which he developed while navigating an unconventional path from psychology graduate to principal applied scientist at one of the world's largest tech companies.

## Timeline

| Date | Event |
|------|-------|
| ~2013 | Graduated from Singapore Management University with BSc in Psychology & Organisation Behaviour |
| 2013–2014 | Data Scientist at IBM — built workforce analytics, fraud detection, and job forecasting systems |
| 2015–2017 | Data Scientist at Alibaba/Lazada — ranking systems, ML automation, MLOps |
| 2017 | Published "My Journey from Psych Grad to Leading Data Science at Lazada" — widely shared story of non-traditional career path |
| 2017 | Gave talk at Singapore Management University on data analytics for non-technical students |
| 2017 | Started Georgia Tech's Online Master of Science in Computer Science (OMSCS) program |
| 2017–2018 | VP, Machine Learning at Alibaba/Lazada — product ranking (+5–20% conversion), push notifications (+10% CTR), product/review classification (-90% cost) |
| 2018 | Published "OMSCS CS7642 (Reinforcement Learning) Review and Tips" — detailed course analysis |
| 2018–2019 | ML Lead at Healthtech Series A startup — shipped ML system for Southeast Asia's largest healthcare provider (disease detection, cost estimation); delivered 4 hospital cost-predictor models in 3 months |
| 2020 | Joined Amazon as Principal Applied Scientist |
| 2020 | Published "Georgia Tech's OMSCS FAQ (based on my experience)" — became one of the most-read guides for the program |
| 2020–2025 | Principal Applied Scientist at Amazon — built real-time retrieval, bandit rankers, and recommendation systems for search; developed AI products for summarization, translation, and Q&A |
| 2023 | Published "LLM-powered Biographies" — early experiment with LLMs generating biographical content, highlighting their limitations |
| 2023 | Published "Patterns for Building LLM-based Systems & Products" — comprehensive framework covering evals, RAG, fine-tuning, UX, and more; became one of his most-read posts (62.4K views) |
| 2023 | Created "What We've Learned From a Year of Building with LLMs" with collaborators — published on O'Reilly as a book and technical series |
| 2024 | Published "How to Generate and Use Synthetic Data for Finetuning" |
| 2024 | Published "Task-Specific LLM Evals that Do & Don't Work" |
| 2024 | Published "Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)" |
| 2024 | Published "Prompting Fundamentals and How to Apply them Effectively" |
| 2024 | Built and released **AlignEval** — an app to make LLM evaluations easy, fun, and semi-automated |
| 2024 | Published "2024 Year in Review" — detailed analysis of shipping ML/LLM systems at scale |
| 2024 | eugeneyan.com reached 11,800+ newsletter subscribers and 10.5% YoY increase in unique visitors despite 27% Google Search decline |
| 2025 | Published "Evaluating Long-Context Question & Answer Systems" |
| 2025 | Published "An LLM-as-Judge Won't Save The Product—Fixing Your Process Will" |
| 2025 | Published "Advice for New Principal Tech ICs (Notes to Myself)" — distilling observations on effective principal engineering |
| 2025 | Published "Training an LLM-RecSys Hybrid for Steerable Recs with Semantic IDs" |
| 2025 | Published "AI Engineer 2025 - Improving RecSys & Search with LLM techniques" |
| 2025 | Published "2025 Year in Review" |
| 2025 | Built AI Coach prototype — talk to "Tara," an AI coach at +1 (206) 558-8782 |
| 2025 | Transitioned from Amazon to **Anthropic** as Member of Technical Staff |
| 2026–Present | Member of Technical Staff at Anthropic — working to bridge the field and the frontier, building safe, reliable AI systems at scale |

## Core Ideas

### Bridging the Field and the Frontier

Yan's defining philosophy is his commitment to **connecting practical, production-tested ML work ("the field") with cutting-edge research ("the frontier").** He doesn't see these as separate domains but as a continuum: the best practitioners understand research deeply, and the best researchers understand production constraints. His move to Anthropic in 2026 was motivated by this desire to bridge the two — bringing production experience to frontier model development and bringing frontier capabilities back to practical application.

> "I work to bridge the field and the frontier, and help build safe, reliable AI systems that serve customers at scale."

This philosophy manifests in everything he does: his blog posts are written by practitioners for practitioners, his GitHub repositories curate real-world production lessons, and his prototypes (AI Coach, AlignEval, News Agents) test ideas in production-like settings before formalizing them.

### The Seven Patterns for LLM-Based Systems

Yan's most influential framework organizes practical LLM integration into seven key patterns, mapped along two axes: **improving performance vs. reducing cost/risk** and **closer to data vs. closer to user**:

1. **Evals** — Measuring performance through systematic evaluation, not just benchmarks
2. **RAG** — Adding recent, external knowledge through retrieval-augmented generation
3. **Fine-tuning** — Adapting models to specific domains and tasks
4. **Prompting** — Effective instruction design for task-specific outputs
5. **UX** — Designing user interfaces that account for LLM capabilities and limitations
6. **LLM-as-Judge** — Using models to evaluate other models (with careful calibration)
7. **Cascade** — Breaking complex tasks into simpler sub-tasks, each handled by the most appropriate model

His framework emphasizes that **evals are the foundation** — without measurement, you can't improve. RAG is positioned as the most cost-effective way to add knowledge, since updating retrieval indices is cheaper than retraining models.

### Eval-Driven Development (EDD)

Yan advocates for a development methodology modeled on test-driven development: **write evals first, then build systems that pass them.** He argues that many teams fail at AI products because they skip the evaluation step and jump straight to prompting or fine-tuning.

> "Product evals are misunderstood. Some folks think that adding another tool, metric, or LLM-as-judge will solve the problems and save the product. But this sidesteps the core problem and avoids the real work. Evals aren't static artifacts or quick fixes; they're practices that apply the scientific method."

His approach to evals is deeply practical:
- **Look at the data first** — observe inputs, outputs, and user interactions before writing criteria
- **Align to human preferences** — the key insight is that building effective evals requires understanding what humans actually want, not what benchmarks measure
- **Work backward from data** — understand what the LLM actually produces, not what you expect it to produce
- **Use the scientific method** — observe, hypothesize, test, iterate

### The Scientific Method for AI Products (Apr 2025)

In *"An LLM-as-Judge Won't Save The Product—Fixing Your Process Will,"* Yan presents evals as the **scientific method in disguise**:

1. **Observation** — Audit real inputs, outputs, and user interactions to identify failure modes
2. **Annotation** — Label a balanced dataset (target: 50:50 pass/fail) across the full input distribution
3. **Hypothesis** — Diagnose root causes (poor retrieval, conflicting instructions, flawed reasoning traces)
4. **Experimentation** — Test changes with explicit baselines and quantifiable success metrics
5. **Measurement** — Use automated evaluators calibrated against human judgment
6. **Iteration** — Apply successful changes, refine hypotheses, repeat

> "Building product evals is simply the scientific method in disguise. That's the secret sauce. It's a cycle of inquiry, experimentation, and analysis."

### LLM-as-Judge: A Critical Survey (Aug 2024)

Yan synthesized **two dozen research papers** into the definitive practical guide to LLM-as-Judge evaluation. Key findings:

**Scoring Approaches:**
- **Direct Scoring** — Best for objective tasks (faithfulness, toxicity, instruction-following)
- **Pairwise Comparison** — More reliable for subjective tasks; yields smaller LLM-human gaps
- **Reference-Based** — Acts as sophisticated fuzzy-matching; requires gold references

**Metrics Skepticism:**
> "I'm skeptical of correlation metrics like Cohen's κ and Kendall's τ. They're overoptimistic and hard to translate to production. I prefer forcing binary outputs to use classification metrics (precision, recall)."

**Key Techniques Discovered:**
- **Cross-Examination (LM vs LM)** — Multi-turn Q&A between examiner and examinee models; majority voting across 3 rounds achieves Recall 0.75-0.84, Precision 0.82-0.87
- **Panel of LLMs (PoLL)** — Ensemble of 3 smaller models via max voting outperforms GPT-4 alone at 1/7th the cost; GPT-4 initially underperformed due to "over-reasoning" until given explicit "don't overthink" instruction
- **SelfCheckGPT** — Generate N=20 samples, measure consistency against target; prompt-based PR-AUC reaches 0.93 on NotFact, 0.67 on Factual datasets
- **Fairer Preferences** — Paraphrasing instructions to neutralize prompt bias improves correlation by +17% (Mistral) and +10% (Llama-3)

**Human Annotation Reality:**
> "Human annotators rarely exceed 90% accuracy (Kappa often 0.2-0.3, miss ~50% of defects due to fatigue). The true benefit [of LLM evaluators] isn't higher accuracy than humans—it's scalability: consistent, (super)human-level judgment across hundreds of samples in minutes, 24/7."

### Task-Specific Evals: What Actually Works (Mar 2024)

Yan argues that **off-the-shelf evals rarely correlate with application-specific performance** and aren't discriminative enough for production:

**Classification/Extraction:**
- Voiceflow's eval harness caught a **10% performance drop** when upgrading from `gpt-3.5-turbo-0301` to `gpt-3.5-turbo-1106`
- "Accuracy is too coarse a metric. We need recall and precision, ideally across thresholds."
- High ROC-AUC/PR-AUC ≠ production-ready if the positive/negative distributions overlap too much to cut a reliable threshold

**Summarization:**
- N-gram metrics (ROUGE, METEOR) and LLM-as-Judge (G-Eval) are **unreliable** for production
- NLI-based consistency detection: finetuning on ~300 samples boosts ROC-AUC from 0.56 (random) → 0.85
- "I seldom see grammatical errors from a decent LLM (maybe 1 in 10k). No need to invest in evaluating fluency and coherence."

**Translation:** Use chrF, BLEURT, COMET, COMETKiwi (pre-trained checkpoints)

### AlignEval: A Practical Tool (Oct 2024)

Yan built **AlignEval**, an open-source app to streamline the eval workflow:

> "It is impossible to completely determine evaluation criteria prior to human judging of LLM outputs." (citing *Who Validates the Validators* by Shankar et al.)

**4-Step Workflow:**
1. **Upload Data** — CSV with input, output, and binary labels
2. **Label Mode** — Human review with binary (0/1) pass/fail; 50-100 labels recommended for stable criteria
3. **Evaluation Mode** — Define single-dimension criteria, run against LLM (gpt-4o-mini or claude-3-haiku), view real-time metrics (recall, precision, F1, Cohen's κ, confusion matrix)
4. **Optimization Mode** — Semi-automated improvement using dev/test splits; runs n trials to maximize F1

**Architecture Decisions:**
- Binary labels over Likert scales (validated by DoorDash and Llama2 teams)
- Claude XML prompt template with `<sketchpad>` for step-by-step reasoning and `<prediction>` for structured output
- Zod (JS) and Pydantic (Python) for structured output constraints
- Built 5 prototypes across FastHTML, Next.js, SvelteKit, and FastAPI+HTML before finalizing stack
- Hosted on Railway (Postgres + Redis) — prioritized deployment speed over VPS complexity (YAGNI principle)

**Key Insight:**
> "Align AI to human. Calibrate human to AI. Repeat."

### Product Evals in Three Simple Steps (Nov 2025)

Yan distills eval engineering into a repeatable pipeline:

**Step 1: Label Some Data**
- Target: 50-100 fail cases out of 200+ samples
- Source fails from **smaller/less capable models** (organic failures), not strong models (synthetic failures that are often out-of-distribution)
- Use active learning: calibrated evaluator flags likely failures for targeted human annotation

**Step 2: Align Our LLM-Evaluator**
- **One evaluator per dimension** (faithfulness, relevance, etc.) — avoid "God Evaluators"
- Combine via simple heuristics (output passes only if all dimensions pass)
- Handle position bias: evaluate twice with swapped order using XML tags; if results flip, mark as tie
- Split 75% dev / 25% test to measure generalization, not overfitting

**Step 3: Run the Eval Harness with Each Change**
- Connect harness directly to experiment pipeline for tight feedback loop
- "Tweak a config... generate output, and immediately evaluate it... make a one-line config change, start the pipeline, get lunch, and check results."
- **ROI Anecdote:** 4-week upfront eval investment enabled dozens of experiments in 2 weeks, and hundreds over months

**Statistical Rigor:**
> "Standard error ∝ 1/√n. To halve the margin of error, you must quadruple the sample size."
- Target <5% defect rate requires 400 samples (not 200) for statistical confidence
- Diminishing returns mean sample sizing must be deliberate, not arbitrary

### Long-Context Q&A Evaluation (Jun 2025)

Yan identifies two **orthogonal dimensions** for long-context evaluation:

**Faithfulness (Groundedness):**
- Strict reliance on source document; no external knowledge or hallucinations
- Must know when to say "I don't know"
- Faithfulness ≠ correctness: an answer can be factually true but unfaithful if it contradicts the specific document
- Citation accuracy: do provided references actually support the answer?

**Helpfulness:**
- Relevance, comprehensiveness, and conciseness
- Domain experts prefer comprehensive + faithful answers; crowd-workers prioritize surface conciseness

**Dataset Construction:**
- Use LLMs to draft questions at scale, then humans refine/validate
- Avoid vague prompts; use specific, synthesis-driving instructions
- Include positional variance: evidence at start/middle/end
- Include multi-hop questions spanning sections/documents
- Include No-Info questions to test refusal capability

**Assessment Methods:**
- Break answers into atomic claims, verify each against source
- Use pairwise comparisons ("Which answer is more helpful?") instead of absolute ratings
- BLEU/ROUGE correlate poorly with human judgment on open-ended Q&A

### The Ghost Knowledge of Applied ML

Yan's blog consistently focuses on what he calls "ghost knowledge" — the practical, unwritten lessons about applying ML that don't appear in papers or documentation. This includes:
- How to handle messy production data
- When to use simpler models over complex ones
- How to communicate technical work to business stakeholders
- What actually works in recommendation systems vs. what papers claim
- The hidden costs and maintenance burden of ML systems

This focus stems from his own experience: as a psychology graduate entering data science, he lacked the formal CS background and had to learn everything through doing. This gave him a practitioner's perspective that values working systems over theoretical elegance.

### Simplicity Over Complexity

Like many great practitioners, Yan favors simple solutions that work in production over complex ones that work on paper. His post "Simplicity" (23.4K views) argues that the best ML systems are often the simplest ones that are well-maintained, well-monitored, and well-understood by the team.

This connects to his broader engineering philosophy: **design systems for the long term.** As his colleague YuXuan Tay noted: "He takes a long term view when designing engineering systems to ensure that complexity and maintenance efforts are minimized when in production."

### Self-Learning as a Core Competency

Yan's career trajectory — from psychology graduate to principal applied scientist at Amazon — is itself a case study in self-directed learning. He learned Python overnight to unblock a project, completed Georgia Tech's rigorous OMSCS program while working full-time, and consistently teaches himself new areas (RL, NLP, LLMs, RecSys) as his career demands it.

> "In almost all my roles and projects, continuous self-learning played a big role."

His OMSCS FAQ became one of the most-read guides for the program because it addresses practical concerns (cost, workload, admissions) from the perspective of someone who actually completed it while working.

### Recommendation Systems in the Age of LLMs

Yan's deep expertise in recommendation systems — built through years at Lazada and Amazon — positions him uniquely to analyze how LLMs are changing the recsys landscape. His work on **Semantic IDs** (training an LLM-RecSys hybrid for steerable recommendations) demonstrates how LLMs can be integrated into traditional recsys architectures to improve personalization and control.

His posts on improving RecSys and search with LLM techniques consistently rank among his most popular, with the 2025 "AI Engineer 2025" talk and "Improving Recommendation Systems & Search in the Age of LLMs" each attracting 30K+ views.

### From Principal IC to Frontier Research

Yan's "Advice for New Principal Tech ICs" (Oct 2025) distills his observations on what makes an effective principal engineer or scientist. Key themes include:

- **Different principals have different flavors** — some dive deep in one space, others excel horizontally
- **The work that made you successful is now the side task** — at this level, writing code is secondary to enabling others
- **You're part-time everything** — product, design, engineering, communication
- **Put yourself on the critical path, then remove yourself from it** — the org should benefit from you without depending on you
- **If you were promoted to principal, it's because you've been acting as one for a while**

This reflects his own career arc: at Amazon, he transitioned from hands-on IC work to enabling broader organizational impact, building systems that serve customers at scale while mentoring the next generation of ML engineers.

## Key Quotes

> "I work to bridge the field and the frontier, and help build safe, reliable AI systems that serve customers at scale."

> "Product evals are misunderstood. Some folks think that adding another tool, metric, or LLM-as-judge will solve the problems and save the product. But this sidesteps the core problem and avoids the real work."

> "Evals aren't static artifacts or quick fixes; they're practices that apply the scientific method, eval-driven development, and AI."

> "In almost all my roles and projects, continuous self-learning played a big role."

> "The key insight is that aligning AI to human preferences is only half the battle. To build effective evals, we must work backward from the data."

> "By the way, if you want to learn more about evals..." — his signature sign-off, always pointing to community resources

> "He takes a long term view when designing engineering systems to ensure that complexity and maintenance efforts are minimized when in production." — YuXuan Tay, Meta

> "When a barrier is placed in front of him, he doesn't stop, he pushes through." — Karen Midkiff, IBM (on Yan teaching himself Python overnight)

> "There is a large class of problems that are easy to imagine and build demos for, but extremely hard to make products."

> "Simplicity is the ultimate sophistication." (paraphrased from his writing philosophy)

## Recent Themes (2024–2026)

- **LLM evaluation methodology**: Systematic approaches to eval-driven development, LLM-as-judge calibration, and building tools like AlignEval
- **Long-context Q&A systems**: Evaluating how well LLMs handle documents beyond their effective context window
- **Recommendation systems + LLMs**: Integrating LLMs into traditional recsys architectures (semantic IDs, steerable recommendations)
- **AI-powered product development**: Patterns for building production AI systems, from RAG to fine-tuning to UX design
- **Principal engineering leadership**: Advice and frameworks for senior ICs transitioning to broader organizational impact
- **Career transition to Anthropic**: Moving from applied ML at Amazon to frontier AI research and development
- **Open-source ML resources**: Maintaining and curating community resources (applied-ml, open-llms, ml-surveys)
- **Public prototyping**: Building AI tools in public (AI Coach, News Agents, AlignEval, Obsidian-Copilot) as learning and sharing exercises
- **Synthetic data for fine-tuning**: Practical guidance on generating and using synthetic training data
- **Prompting fundamentals**: Systematic approaches to effective instruction design for LLMs

## Related Concepts

- [[machine-learning-in-production]] — His primary domain: shipping ML systems that work at scale
- [[recommendation-systems]] — His deep expertise from Lazada and Amazon
- [[llm-evaluation]] — His work on eval-driven development and LLM-as-judge
- [[retrieval-augmented-generation]] — One of his seven core LLM integration patterns
- [[applied-ml]] — His most-starred GitHub repository (28.7K stars)
- [[open-llms]] — His curated list of commercially usable open LLMs (12.7K stars)
- [[ai-agents]] — His work on AI-powered products and prototypes
- [[georgia-tech-omscs]] — His master's program and the FAQ he wrote for it
- [[eval-driven-development]] — His methodology for building AI products
- [[singapore-management-university]] — His undergraduate alma mater

## Influence Metrics

- **GitHub repositories**: applied-ml (28.7K stars), open-llms (12.7K stars), ml-surveys (2.9K stars), ml-design-docs (689 stars)
- **Blog**: 209 posts, 31 talks, 19 prototypes, 420K+ words published at eugeneyan.com
- **Newsletter**: 11,800+ subscribers; consistent YoY growth despite Google Search traffic decline
- **Most-read posts**: "Patterns for Building LLM-based Systems & Products" (62.4K views), "Simplicity" (23.4K views), "AI Engineer 2025" (30K+ views)
- **Career progression**: Psychology graduate → IBM → Lazada/Alibaba (VP ML) → Healthtech Series A (ML Lead) → Amazon (Principal Applied Scientist) → Anthropic (MTS)
- **O'Reilly publication**: "What We've Learned From a Year of Building with LLMs" — co-authored book/technical series
- **Community impact**: applied-ml is the go-to reference for production ML papers; open-llms is the standard for tracking commercially usable models
- **Speaking**: 31+ talks at conferences including AI Engineer 2025, DataScience SG Meetup, and others
- **Prototypes**: AI Coach (phone-based), AlignEval, Obsidian-Copilot, News Agents, Semantic IDs, LLM UX experiments

## Sources

- https://www.eugeneyan.com/about/ — About page and career timeline
- https://eugeneyan.com/ — Main blog
- https://github.com/eugeneyan/ — GitHub profile and repositories
- https://eugeneyan.com/writing/llm-patterns — Patterns for Building LLM-based Systems & Products
- https://eugeneyan.com/writing/aligneval/ — AlignEval: Building an App to Make Evals Easy, Fun, and Automated
- https://eugeneyan.com/writing/eval-process/ — An LLM-as-Judge Won't Save The Product—Fixing Your Process Will
- https://eugeneyan.com/writing/qa-evals/ — Evaluating Long-Context Question & Answer Systems
- https://eugeneyan.com/writing/principal/ — Advice for New Principal Tech ICs
- https://eugeneyan.com/writing/psych-grad-to-data-science-lead/ — My Journey from Psych Grad to Leading Data Science at Lazada
- https://eugeneyan.com/writing/georgia-tech-omscs-faq/ — Georgia Tech's OMSCS FAQ
- https://eugeneyan.com/writing/2024-review/ — 2024 Year in Review
- https://eugeneyan.com/writing/semantic-ids-recsys/ — Training an LLM-RecSys Hybrid for Steerable Recs with Semantic IDs
- https://eugeneyan.com/writing/llm-bio/ — LLM-powered Biographies
- https://eugeneyan.com/speaking/sharing-at-singapore-management-university-on-data-analytics-talk/ — SMU talk on data analytics
