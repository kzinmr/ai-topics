---
title: "Hamel Husain"
tags: [- person]
created: 2026-04-24
updated: 2026-04-13
type: entity
---


# Hamel Husain — AI Engineering & Evaluation Expert

| | |
|---|---|
| **Role** | Independent Consultant (Parlance Labs), R&D at AnswerAI, Scout at Bain Capital |
| **Previous** | Staff ML Engineer at GitHub (Copilot), Senior DS at Airbnb, EIR at fast.ai |
| **Known For** | "Critique Shadowing" methodology, AI Evals course (w/ Shreya Shankar), nbdev, CodeSearchNet |
| **Education** | Georgia Tech — MS Computer Science (Machine Learning) |
| **Newsletter** | [hamel.dev/blog](https://hamel.dev) (Substack/O'Reilly Radar) |
| **X/Twitter** | [@HamelHusain](https://x.com/HamelHusain) |
| **GitHub** | [hamelsmu](https://github.com/hamelsmu) |
| **Years Active** | 2004 – Present |

## Overview

Hamel Husain is a veteran **AI Engineer and Consultant** with over 20 years of experience, currently operating as an independent consultant through **Parlance Labs**, an R&D member at **AnswerAI** (Jeremy Howard's venture), and a Scout for **Bain Capital**.

He is a leading voice in the **AI Evaluation** and **Harness Engineering** movements. Husain co-created the world's most popular AI evals course (with Shreya Shankar), training 2,000+ engineers and PMs at companies like OpenAI and Anthropic.

His career spans **GitHub** (where he contributed to the precursors of Copilot and led CodeSearchNet), **Airbnb**, **Accenture**, and **fast.ai**. He is the creator of **nbdev** (literate programming for notebooks) and **evals-skills**, a plugin set for AI coding agents.

> *"The real value is looking at your data. Creating an LLM judge is a nice 'hack' to trick people into carefully examining their data."*

## Timeline

| Date | Event |
|------|-------|
| 2004–2008 | Consultant at **Accenture** (CRM data analysis for Fortune 500 telecom) |
| 2008–2016 | Data Scientist roles in credit modeling and optimization |
| 2016–2017 | Senior Data Scientist at **Airbnb** (Growth marketing) |
| 2017–2022 | Staff Machine Learning Engineer at **GitHub** |
| 2019 | O'Reilly AI Conference Speaker: "Build, train, and deploy ML with Kubeflow" |
| 2020 | Launched **CodeSearchNet** (representation learning of code, precursor to Copilot) |
| 2020 | Created **nbdev** (notebook-enabled software development) with Jeremy Howard |
| Jan 2022–Aug 2022 | Head of ML Data Science at **Outerbounds** (Metaflow) |
| Aug 2022–May 2023 | Entrepreneur in Residence at **fast.ai** |
| May 2023–Present | Independent Consultant at **Parlance Labs** |
| Oct 2024–Present | R&D at **AnswerAI** (Jeremy Howard's new AI venture) |
| 2024 | Published "Your AI Product Needs Evals" (Hamel.dev) |
| Oct 2024 | Published "Using LLM-as-a-Judge For Evaluation: A Complete Guide" |
| May 2024 | Co-authored **"What We've Learned From A Year of Building with LLMs"** (O'Reilly Radar, Parts I, II, III) |
| 2025 | Published "Selecting The Right AI Evals Tool" |
| 2025 | Published **"A Field Guide to Rapidly Improving AI Products"** |
| 2025 | Released **evals-skills** (OSS plugins for coding agents) |
| Sep 2025 | **Lenny's Podcast** (w/ Shreya Shankar): "Why AI evals are the hottest new skill" (100K+ views) |

## Core Philosophy

### Process First, Tools Second
Husain argues that the industry's obsession with evaluation *tools* (LangSmith, Braintrust, etc.) misses the point. The value lies in the **process of error analysis**.

> *"When everything is important, nothing is."* — On the danger of generic metrics vs. specific failure modes.

### Critique Shadowing
A signature methodology for building aligned LLM-as-Judge evaluators, described in detail in his 2024 blog series:
1.  **Find the Principal Domain Expert**: The person with the "taste" to judge quality.
2.  **Create a Dataset**: Features × Scenarios × Personas.
3.  **Domain Expert Reviews Data**: Pass/fail judgments with detailed critiques.
4.  **Fix Errors**: Iterate on the prompt or data.
5.  **Build LLM Judge**: Use expert examples as few-shot prompts.
6.  **Perform Error Analysis**: Classify errors by root cause.
7.  **Create Specialized Judges**: If needed, break down into multiple judges.

> *"Documentation tells the agent what to do. Telemetry tells it whether it worked. Evals tell it whether the output is good."*

### Harness Engineering
Husain is a proponent of **Harness Engineering** — the practice of building systems that constrain and guide LLMs to ensure reliability.
-   **60-80% of dev time** should be spent on error analysis and evaluation.
-   **Binary over Likert**: Pass/fail judgments are more actionable than 1-5 scales.
-   **Synthetic Data Strategy**: Generate inputs, not outputs, to prevent inheriting model biases.

### The "LLM Judge" Skepticism
While he teaches how to build LLM judges, he is skeptical of their standalone value without human-in-the-loop grounding.
> *"LLM judges are themselves models with biases and limitations. The real differentiator is the process of building, testing, and iterating."*

## Key Publications & Works

### "What We've Learned From A Year of Building with LLMs" (O'Reilly, 2024)
Co-authored with **Eugene Yan, Shreya Shankar, Jason Liu, Bryan Bischof, Charles Frye**.
-   **Part I (Tactical):** Prompting, RAG, Evals.
-   **Part II (Operational):** Team building, Iteration processes.
-   **Part III (Strategic):** Business alignment, Product-market fit.
-   **Impact:** The definitive industry reference for production LLM engineering.

### "A Field Guide to Rapidly Improving AI Products" (2025)
-   Practical advice on moving from prototype to production.
-   Emphasizes that "scale makes everything harder" and "execution is everything".

### evals-skills (Open Source)
-   A set of plugins for AI coding agents to perform evaluations: `eval-audit`, `error-analysis`, `generate-synthetic-data`, `write-judge-prompt`.
-   Connects to the Harness Engineering philosophy by automating the "check" step in the agent loop.

### Lenny's Podcast (Sep 2025)
-   Appeared with Shreya Shankar to discuss the "Evals" course.
-   Key takeaway: "Evals are the most important thing to get an agent working, yet no one is doing it."

## Open Source Contributions
-   **nbdev**: Literate programming environment for Python notebooks (co-creator).
-   **fastcore**: Extensions to Python for fast.ai.
-   **ghapi**: Python client for GitHub API.
-   **CodeSearchNet**: Dataset and models for searching code (GitHub).
-   **Inspect AI**: Notes and contributions to the evaluation library.

## Career & Background
-   **Industrial Engineering**: Started in optimization and credit modeling before moving to data science.
-   **GitHub**: Worked on the internal tools that became **Copilot**. Led the **CodeSearchNet** project, which was one of the first large-scale attempts to train models on code repositories.
-   **fast.ai**: Worked closely with **Jeremy Howard** on democratizing deep learning and building developer tools.
-   **AnswerAI**: Joined the R&D team for Howard's new venture, focusing on next-gen AI product development.
-   **Bain Capital**: Serves as a Scout, evaluating early-stage AI companies.

## Key Quotes

> *"The real value is looking at your data. Creating an LLM judge is a nice 'hack' to trick people into carefully examining their data."*

> *"Documentation tells the agent what to do. Telemetry tells it whether it worked. Evals tell it whether the output is good."*

> *"When everything is important, nothing is."*

> *"Evals are the most important thing to get an agent working, yet no one is doing it."*

> *"60-80% of dev time should be spent on error analysis and evaluation."*

## Related Entities

-   [[shreya-shankar]] — Co-creator of AI evals course, collaborator on Applied LLMs guide.
-   [[eugene-yan]] — Co-author on Applied LLMs guide, shared evals philosophy.
-    — Mentor/collaborator at fast.ai and AnswerAI.
-   [[concepts/ai-evals]] — The evaluation framework he teaches.
-   [[drmaciver]] — Property-based testing applied to LLM evaluation (`foundational-llm-evals`); PBT methodology for eval design.
-   [[shreya-shankar]] — Co-creator of AI evals course, collaborator on Applied LLMs guide.
-   [[concepts/harness-engineering]] — His core engineering philosophy.
-   [[concepts/critique-shadowing]] — His signature methodology.
-   [[concepts/llm-as-judge]] — Core evaluation technique he critiques and teaches.

## Sources

-   [Hamel.dev](https://hamel.dev) — Personal blog and portfolio.
-   [LinkedIn](https://www.linkedin.com/in/hamelhusain) — Career history.
-   [O'Reilly Radar](https://www.oreilly.com/people/hamel-husain/) — Author profile.
-   [Lenny's Podcast](https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill) — Episode summary.
-   [GitHub](https://github.com/hamelsmu) — Open source projects.
-   [Parlance Labs](https://parlance-labs.com) — Consulting firm.
-   [AnswerAI](https://www.answer.ai/) — R&D role.
