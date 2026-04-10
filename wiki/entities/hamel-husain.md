---
title: "Hamel Husain"
handle: "@HamelHusain"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ai, llm-evals, mlops, open-source, fastai, nbdev, github]
aliases: ["@HamelHusain", "hamelhusain", "hamelsmu", "Hamel Husain GitHub"]
---

# Hamel Husain (@HamelHusain)

| | |
|---|---|
| **X** | [@HamelHusain](https://x.com/HamelHusain) |
| **Blog** | [hamel.dev](https://hamel.dev) |
| **GitHub** | [hamelsmu](https://github.com/hamelsmu) |
| **Role** | ML Engineer, Educator, Consultant; co-creator of nbdev |
| **Known for** | LLM evaluation methodology, nbdev, fastai contributions, AI Evals course |
| **Bio** | Hamel Husain is a machine learning engineer with over 20 years of experience at companies including GitHub and Airbnb. He co-created nbdev with Jeremy Howard, is a major contributor to the fastai ecosystem, and has emerged as a leading voice on practical AI evaluation. He co-teaches AI Evals for Engineers and PMs to 3,000+ students from 500+ companies and writes extensively on his blog and Substack about building reliable AI systems. |

## Overview

Hamel Husain occupies a unique position in the AI ecosystem as a practitioner-educator who bridges the gap between cutting-edge research and real-world product development. With over two decades of experience in machine learning engineering — including early work on LLMs at GitHub and data science infrastructure at Airbnb — Hamel has evolved into one of the most influential voices on **practical AI evaluation**.

His career trajectory reflects the evolution of the ML field itself. He started in traditional data science and ML engineering, became an early advocate for literate programming through **nbdev** (which he co-created with [[Jeremy Howard]]), contributed significantly to the **fastai** ecosystem, and then pivoted hard to LLMs when ChatGPT launched in late 2022. Since then, he has focused almost exclusively on helping teams debug, analyze, and measure their AI systems — a practice he simply calls "evals."

Hamel's influence in the AI evaluation space is substantial. He co-teaches **AI Evals for Engineers and PMs**, a course that has enrolled over 3,000 students from 500+ companies including OpenAI, Anthropic, and numerous startups. His blog at hamel.dev and Substack newsletter are essential reading for anyone building AI products, covering topics from LLM-as-a-judge methodology to synthetic data generation to selecting the right evaluation tooling. His March 2026 post "The Revenge of the Data Scientist" argues that as AI systems become more complex, the skills of traditional data scientists — careful analysis, experimental design, and statistical rigor — become more valuable, not less.

Before his focus on LLMs, Hamel was a key figure in the **nbdev** project — a revolutionary software development framework based on Jupyter notebooks that enables literate and exploratory programming. He worked on nbdev from 2020–2023 alongside Jeremy Howard and Wasim Lorgat, pushing the boundaries of developer tools. His reflections on the commercialization attempt ("On commercializing nbdev") are a candid and insightful look at the challenges of turning innovative open-source tools into sustainable businesses.

## Core Ideas

### AI Products Need Evals

Hamel's foundational thesis, articulated in his March 2024 post "Your AI Product Needs Evals," is that **every AI product requires a rigorous evaluation system** — not just academic benchmarks, but product-specific tests that measure whether the system actually works on real user tasks with real data.

He distinguishes between different levels of evaluation:
- **Level 1: Basic correctness** — Does the system produce syntactically valid, non-hallucinated outputs?
- **Level 2: Task-specific performance** — Does the system perform well on the specific tasks it's designed for?
- **Level 3: User satisfaction** — Do actual users find the system helpful and reliable?
- **Level 4: Business impact** — Does the system drive measurable business outcomes?

His key insight is that most teams skip directly to Level 4 without establishing the foundation. *"Ever spend weeks building an AI system, only to realize you have no idea if it's actually working?"* he wrote. This gap — between building and measuring — is what his evaluation methodology aims to fill.

### Critique Shadowing and the LLM-as-a-Judge Methodology

In his October 2024 post "Creating a LLM-as-a-Judge That Drives Business Results," Hamel introduced **Critique Shadowing** — a methodology for building reliable LLM evaluators by having domain experts first manually critique a diverse set of AI outputs, then using those critiques to train an LLM judge.

> *"The paper from Shankar et al., 'Who Validates the Validators?' summarizes this well: to grade outputs, people need to externalize and define their evaluation criteria; however, the process of grading outputs helps them to define that very criteria. We dub this phenomenon criteria drift."*

Critique Shadowing works because:
1. It forces domain experts to articulate their evaluation criteria through concrete examples rather than abstract principles.
2. It captures the natural evolution of criteria as experts see more examples (criteria drift).
3. It produces training data that reflects real-world judgment patterns, not synthetic labels.
4. It can be iteratively refined as the AI system improves and new failure modes emerge.

Hamel has helped over 50 companies implement this approach and found it consistently produces more reliable evaluators than teams writing judge prompts from scratch.

### Synthetic Data for Evaluation

A recurring theme in Hamel's work is the strategic use of **synthetic data** for building evaluation datasets. In his October 2024 post, he addresses the skepticism directly:

> *"You might be skeptical of using synthetic data. After all, it's not real data, so how can it be a good proxy? In my experience, it works surprisingly well. Some of my favorite AI products, like Hex, use synthetic data to power their evals."*

He argues that LLMs are "surprisingly good at generating excellent — and diverse — examples of user prompts," which can be used to create comprehensive test suites covering edge cases, diverse personas, and rare scenarios that would be difficult to collect from real user data alone. The key is to validate synthetic data against real user behavior and iterate on the generation process.

### Evals Skills for Coding Agents

In March 2026, Hamel published **evals-skills**, a set of MCP-compatible skills that teach AI coding agents how to perform evaluation tasks. This represents a meta-application of his evaluation philosophy: using agents to automate the evaluation pipeline itself.

The skills include:
- **eval-audit** — Inspects an existing eval setup (or lack thereof), runs diagnostic checks across six areas (error analysis, evaluator design, judge validation, human review, labeled data, pipeline hygiene), and produces a prioritized list of problems.
- **error-analysis** — Reads traces, categorizes failures, and builds a vocabulary of what's broken.
- **generate-synthetic-data** — Creates diverse test inputs when real data is sparse.
- **write-judge-prompt** — Designs binary Pass/Fail LLM-as-Judge evaluators.

> *"Coding agents now instrument applications, run experiments, analyze data, and build interfaces. I've been pointing them at my evals infrastructure. Documentation tells the agent what to do. Telemetry tells it whether it worked. Evals apply the same principle to AI output quality."*

### The Revenge of the Data Scientist

In his March 2026 post "The Revenge of the Data Scientist," Hamel argues that as AI systems mature, the skills of traditional data scientists — statistical analysis, experimental design, error analysis, and data curation — become increasingly valuable. The era of "just prompt an LLM" is giving way to an era where careful measurement, rigorous evaluation, and systematic improvement are the differentiators between successful and failed AI products.

This connects to his broader philosophy: **telemetry and evaluation are the new competitive advantage**. Teams that can measure their AI systems accurately and iterate quickly will outperform teams that rely on intuition or generic benchmarks.

### Why He Stopped Using nbdev

In his January 2026 post "Why I Stopped Using nbdev," Hamel provided a candid reflection on his relationship with the tool he co-created. He explained that while nbdev remains innovative and valuable, the shift in his focus from software development to AI evaluation, combined with the emergence of new tools (like AI-assisted coding), made nbdev less central to his workflow. He noted that LLMs have "profoundly changed the nature of software development, especially the kind of software development that nbdev was designed to support."

This honesty about evolving tool preferences is characteristic of Hamel's pragmatic approach — he's willing to abandon tools he helped create when they no longer serve his needs, and encourages others to do the same.

## Key Work

### Evaluation Tools & Frameworks

- **evals-skills** (2026) — MCP-compatible skills for AI coding agents to perform evaluation tasks including audit, error analysis, synthetic data generation, and judge prompt writing.
- **AI Evals for Engineers and PMs** — A comprehensive course teaching practical evaluation methodology. 3,000+ students from 500+ companies including OpenAI and Anthropic.
- **AI Evals FAQ** — A foundational guide to product-specific AI evaluation, distinguishing it from academic benchmarks like MMLU or HELM.
- **nbsanity** (2024) — A tool to share Jupyter notebooks as polished web pages in seconds.
- **Inspect AI** — Coverage and advocacy for Inspect AI, an open-source Python library for LLM evaluation.

### Open Source Projects

- **nbdev** (2020–2023) — Co-created with Jeremy Howard. A literate programming framework built on Jupyter notebooks that allows developers to write code, documentation, and tests in a single environment. Revolutionized the way many developers think about code organization and documentation.
- **fastai** — Major contributor to the fastai library and ecosystem. Helped build the educational infrastructure that has trained hundreds of thousands of ML practitioners.
- **ghapi** (2020) — A comprehensive third-party Python client for the GitHub API, enabling programmatic access to all GitHub API endpoints.
- **fastws** — WebSocket library for fast, efficient real-time communication.
- **dialoghelper** — Tool for building conversational AI interfaces.

### Blog Posts & Writing

| Date | Title | Topic |
|------|-------|-------|
| Mar 2026 | The Revenge of the Data Scientist | Why data science skills are becoming more valuable in the AI era |
| Mar 2026 | Evals Skills for Coding Agents | Teaching AI agents to perform evaluation tasks |
| Jan 2026 | Why I Stopped Using nbdev | Candid reflection on evolving tool preferences |
| Jan 2026 | LLM Evals: Everything You Need to Know | Comprehensive guide to LLM evaluation methodology |
| Oct 2025 | Selecting The Right AI Evals Tool | Comparison of evaluation tooling options |
| Jul 2025 | Stop Saying RAG Is Dead | Defending RAG as a viable architecture with proper evaluation |
| Jun 2025 | Inspect AI, An OSS Python Library For LLM Evals | Coverage of open-source evaluation infrastructure |
| Mar 2025 | A Field Guide to Rapidly Improving AI Products | Practical methodology for iterative AI product development |
| Oct 2024 | Using LLM-as-a-Judge For Evaluation: A Complete Guide | Comprehensive LLM-as-a-judge methodology including Critique Shadowing |
| Jul 2024 | An Open Course on LLMs, Led by Practitioners | Practical LLM education for engineers |
| Jun 2024 | What We've Learned From A Year of Building with LLMs | Lessons from early LLM product development |
| Apr 2024 | Debugging AI With Adversarial Validation | Using adversarial techniques to identify and fix AI failures |
| Mar 2024 | Your AI Product Needs Evals | Foundational post on evaluation for AI products |
| Mar 2024 | Is Fine-Tuning Still Valuable? | Analysis of fine-tuning vs. prompting trade-offs |
| Jan 2024 | Dokku: my favorite personal serverless platform | Infrastructure tooling for ML deployment |
| Dec 2023 | Tokenization Gotchas | Common pitfalls in LLM tokenization |
| Nov 2023 | Tools for curating LLM Data | Data curation methodology for LLM training |
| Oct 2023 | vLLM & Large Models | Inference optimization with vLLM |
| Oct 2023 | Optimizing LLM latency | Practical techniques for reducing inference latency |
| May 2023 | On commercializing nbdev | Reflections on the challenges of commercializing open-source tools |
| Jan 2023 | Why Should ML Engineers Learn Kubernetes? | Infrastructure literacy for ML practitioners |
| Jul 2022 | nbdev + Quarto: A new secret weapon for productivity | Combining literate programming with modern publishing |

### Speaking & Teaching

- **AI Evals Course Instructor** — Co-teaches with 3,000+ students across multiple cohorts.
- **Answer.AI Dev Chats** — Regular participant in Answer.AI's developer discussion series.
- **Vanishing Gradients Podcast** — "LLM and GenAI Accessibility with Johno Whitaker" — discussion on making LLMs accessible to broader audiences.
- **Agents at Work Podcast** — "AI Agents from First Principles" — conversation on nbdev, coding AI, and the future of autonomous agents.
- **SolveIt Demos** — Presented the SolveIt "Thinking Developer's Environment" alongside Jeremy Howard to Hamel's evals course.

### Professional Experience

- **GitHub** — Early LLM work, developer tools, API infrastructure.
- **Airbnb** — Machine learning engineering,
- **Answer.AI** — AI evaluation consulting and education
- **Independent Consultant** — ML evaluation, data infrastructure, and developer tooling

## Blog / Recent Posts

| Date | Title | Summary |
|------|-------|---------|
| Mar 2026 | The Revenge of the Data Scientist | Argues that as AI systems mature, traditional data science skills (statistical analysis, experimental design, error analysis) become more valuable, not less. |
| Mar 2026 | Evals Skills for Coding Agents | Introduces evals-skills: MCP-compatible tools that teach AI coding agents to perform evaluation tasks including audit, error analysis, and synthetic data generation. |
| Jan 2026 | Why I Stopped Using nbdev | Candid reflection on evolving away from a tool he co-created, as LLMs changed the nature of software development. |
| Jan 2026 | LLM Evals: Everything You Need to Know | Comprehensive guide covering evaluation methodology, tooling selection, and best practices for product-specific AI evaluation. |
| Oct 2024 | Using LLM-as-a-Judge For Evaluation: A Complete Guide | Introduces Critique Shadowing methodology and provides a complete framework for building reliable LLM evaluators. |
| Mar 2024 | Your AI Product Needs Evals | Foundational post arguing that every AI product requires rigorous, product-specific evaluation — not just academic benchmarks. |
| Jul 2024 | An Open Course on LLMs, Led by Practitioners | Launch of practical LLM education focused on real-world applications rather than theory. |

## Related People

- **[[Jeremy Howard]]** — fastai founder; nbdev co-creator; Hamel's long-time collaborator and mentor.
- **[[Jonathan Whitaker]]** — Answer.AI colleague; both teach AI education courses and contribute to the fastai ecosystem.
- **[[Daniel van Strien]]** — Both write practical guides on the HF ecosystem and contribute to open-source ML tooling.
- **Wasim Lorgat** — nbdev co-contributor alongside Hamel and Jeremy.
- **Simon Willison** — Fellow advocate for practical, accessible AI tooling and transparent evaluation.

## X Activity Themes

Hamel's X activity (@HamelHusain) centers on:

1. **AI Evaluation Methodology** — Sharing frameworks, tools, and best practices for evaluating LLM-powered products rigorously.
2. **Critique Shadowing** — Promoting his methodology for building reliable LLM-as-a-judge systems through expert-led iterative refinement.
3. **Open Source ML Tools** — Advocating for transparent, community-driven evaluation infrastructure over proprietary black-box solutions.
4. **Practical AI Engineering** — Real-world guidance on deploying, monitoring, and improving AI systems in production environments.
5. **nbdev & Literate Programming** — Reflections on the evolution of developer tools and the intersection of documentation, code, and testing.
6. **Data Science Renaissance** — Arguing that careful data analysis and experimental design are becoming more valuable in the AI era.
7. **Teaching & Education** — Promoting his AI Evals course and sharing learnings from teaching 3,000+ students across 500+ companies.
