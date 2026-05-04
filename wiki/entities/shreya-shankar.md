---
title: "Shreya Shankar"
tags: [person]
created: 2026-04-24
updated: 2026-04-13
type: entity
---


# Shreya Shankar — Berkeley AI Evals Researcher & DocETL Creator

| | |
|---|---|
| **Role** | PhD Candidate, UC Berkeley EECS (Aditya Parameswaran lab) |
| **Research Areas** | Data management, human-computer interaction, LLM-powered data systems |
| **Known For** | Co-creator of world's #1 AI evals course (with Hamel Husain), DocETL framework, SPADE/EvalGen, PROMPTEVALS dataset |
| **Education** | UC Berkeley — PhD Computer Science; NDSEG Fellowship recipient |
| **Notable Achievements** | Trained 2,000+ PMs and engineers across 500+ companies (including OpenAI, Anthropic teams) |
| **X/Twitter** | [@sh_reya](https://x.com/sh_reya) |
| **LinkedIn** | [shrshnk](https://www.linkedin.com/in/shrshnk/) |
| **Website** | [sh-reya.com](https://www.sh-reya.com/) |
| **Years Active** | 2017 – Present |

## Overview

Shreya Shankar is a **PhD candidate at UC Berkeley EECS** (advised by Aditya G. Parameswaran) and one of the most influential voices in **AI evaluation methodology**. Alongside Hamel Husain, she co-created the world's most popular AI evals course on Maven, training 2,000+ product managers and engineers — including large teams at OpenAI and Anthropic.

Her research bridges **data management systems** and **human-computer interaction**, with a focus on building reliable, production-grade LLM pipelines. She is on the 2026 computer science faculty job market.

Shankar's work is distinguished by its **systematic, data-driven approach** to AI quality — she has repeatedly demonstrated that "vibes-based" development is insufficient for production AI, and that rigorous error analysis and evaluation frameworks are the highest-leverage activity for AI product teams.

> *"To build great AI products, you need to be really good at building evals. It's the highest ROI activity you can engage in."*

## Timeline

| Date | Event |
|------|-------|
| 2017 | NIPS paper: "No Classification without Representation" — geodiversity issues in open datasets (Google) |
| 2020 | NeurIPS paper: Memory-efficient semidefinite programming for neural network verification |
| 2022 | ICLR paper: "Rethinking Streaming Machine Learning Evaluation" |
| 2022 | "Operationalizing ML: An Interview Study" — challenges faced by ML engineers in production |
| 2023 | CIKM paper: "Automatic and Precise Data Validation for Machine Learning" |
| 2023 | CIDR paper: "Revisiting Prompt Engineering via Declarative Crowdsourcing" (with Aditya Parameswaran) |
| 2024 | VLDB paper: **SPADE** — Synthesizing Data Quality Assertions for LLM Pipelines |
| 2024 | UIST 2024 paper: **"Who Validates the Validators?"** — EvalGen, aligning LLM-assisted evaluation with human preferences |
| May 2024 | O'Reilly Radar Part I: Co-authored "What We've Learned From A Year of Building with LLMs" (with Eugene Yan, Hamel Husain, Jason Liu, Bryan Bischof, Charles Frye) |
| Jun 2024 | O'Reilly Radar Part III: Co-authored strategic section of Applied LLMs guide |
| Aug 2024 | SIGMOD Demo: "Building Reactive LLM Pipelines with Motion" |
| Oct 2024 | VLDB paper: **DocETL** — Agentic Query Rewriting and Evaluation for Complex Document Processing (3.7K GitHub stars) |
| Sep 2025 | **Lenny's Podcast** — "Why AI evals are the hottest new skill for product builders" (101.5K+ YouTube views) |
| Nov 2025 | HILDA Workshop: "Why Is Dataset Search Still So Hard?" |
| 2025 | NAACL 2025 (Oral): **PROMPTEVALS** — Dataset of Assertions and Guardrails for Production LLM Pipelines (co-first author with mentee Reya Vir) |
| 2026 | On CS faculty job market — Research Statement on LLM-powered data systems |

## Core Philosophy

### Systematic Evals Over Vibes-Based Development

Shankar is the leading advocate for moving AI product development away from intuition-based ("vibes") assessment toward **systematic, measurable evaluation**:

> *"You can't improve what you can't measure. Building solid evals should be the starting point for any LLM-based system or product."*

Her argument is not that human judgment is irrelevant — rather, that **human judgment must be structured, documented, and repeated** before it can be automated:

> *"The real value is looking at your data. Creating an LLM judge is a nice 'hack' to trick people into carefully examining their data."*

### The Error Analysis Process (Open Coding)

Shankar developed a rigorous methodology for discovering failure modes in AI systems:

1. **Pull 100 production traces** — real user interactions, not synthetic test cases
2. **Open coding** — manually review each trace, write freeform notes on the first upstream error encountered
3. **Theoretical saturation** — continue until no new failure mode types are being discovered
4. **Axial coding with AI** — use LLMs to categorize open codes into actionable failure modes
5. **Prioritize by frequency** — create pivot tables to count occurrences, focus on most prevalent issues

> *"The highest ROI activity involves looking at actual user interaction data, which most teams neglect by jumping straight to hypothetical test cases without grounding in real problems."*

> *"There's actually a term in data analysis and qualitative analysis called theoretical saturation. When you do all of these processes of looking at your data, when do you stop? It's when you are saturating — you're not uncovering any new types of notes, new types of concepts, or nothing that will materially change the next part of your process."*

### The "Benevolent Dictator" Principle

Shankar argues that evaluation taxonomy should be maintained by a single domain expert, not a committee:

> *"Assign one domain expert with product taste to conduct error analysis rather than forming committees. This person should be the product manager for most applications, keeping the process tractable and avoiding expensive consensus-building that prevents teams from executing systematic evaluation workflows."*

This principle emerged from observing that teams who tried to build evals democratically ended up with bloated, contradictory taxonomies that no one could maintain.

### LLM-as-Judge: Binary Over Likert

Shankar advocates for **pass/fail** evaluation criteria rather than subjective rating scales:

> *"Binary LLM judges are more actionable than Likert scales. Build automated evaluators that output pass/fail for specific failure modes, not 1-5 ratings."*

Her reasoning: binary criteria force clarity about what constitutes "good" vs. "bad" output, which in turn forces teams to articulate their actual requirements.

### Human-in-the-Loop is Non-Negotiable

Despite building tools that automate evaluation, Shankar insists that **humans cannot be skipped from the initial error analysis step**:

> *"LLMs can't replace humans in the initial error analysis. AI-driven tools can transform chaos into prioritized problems, but they cannot replace the initial human error analysis step."*

This aligns with her broader view that **evaluation is a team process problem**, not a tooling problem:

> *"Evals are the most important thing to get an agent working, yet no one is doing it. We're planning a webinar on evals, and the industry has embraced AI for every possible problem — but operations will eventually need to catch up."*

## Key Publications

### DocETL (VLDB 2025) — Agentic Query Rewriting and Evaluation
- **Co-authors:** Tristan Chambers, Tarak Shah, Aditya G. Parameswaran, Eugene Wu
- **GitHub:** 3,700+ stars
- **Impact:** Framework for complex document processing with agentic rewriting and evaluation. One of the first real-world uses of LLM systems in courtroom proceedings.

### EvalGen (UIST 2024) — Aligning LLM-Assisted Evaluation with Human Preferences
- **Co-authors:** J.D. Zamfirescu-Pereira, Björn Hartmann, Aditya G. Parameswaran, Ian Arawjo
- **Key innovation:** Mixed-initiative approach where LLMs suggest evaluation criteria, humans grade outputs, and the system iteratively aligns.
- **Embedded in:** ChainForge (open-source prompt engineering and auditing interface)

### SPADE (VLDB 2024) — Synthesizing Data Quality Assertions for LLM Pipelines
- **Co-authors:** Haotian Li, Parth Asawa, Madelon Hulsebos, Yiming Lin, J.D. Zamfirescu-Pereira, Harrison Chase, Will Fu-Hinthorn, Aditya G. Parameswaran, Eugene Wu
- **Key innovation:** Fully automated algorithm for generating Python assertions from the revision history of a prompt

### PROMPTEVALS (NAACL 2025, Oral) — Dataset of Assertions and Guardrails
- **Co-authors:** Reya Vir (co-first author, mentee), Harrison Chase, William Hinthorn, Aditya Parameswaran
- **Dataset:** 2,087 LLM pipeline prompts with 12,623 corresponding assertion criteria
- **Key finding:** Fine-tuned Mistral and Llama 3 models outperform GPT-4o by 20.93% on assertion generation

### "No Classification without Representation" (NIPS 2017)
- **Co-authors:** Yoni Halpern, Eric Breck, James Atwood, Jimbo Wilson, D. Sculley (Google)
- **Topic:** Geodiversity issues in open datasets for developing world applications
- **Significance:** Early work on bias in ML datasets

### Applied LLMs Guide (O'Reilly Radar, 2024)
- **Co-authors:** Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu
- **Impact:** The definitive practical guide for engineering teams building LLM products
- **Structure:** Three parts — Tactical (prompting, RAG, evals), Operational (team building), Strategic (business alignment)

## Teaching & Speaking

### Maven AI Evals Course (with Hamel Husain)
- **Students:** 2,000+ PMs and engineers
- **Companies trained:** OpenAI, Anthropic, and 500+ organizations
- **Format:** Hands-on course covering error analysis, open coding, axial coding, LLM-as-judge, and evaluation pipeline construction
- **Course page:** https://bit.ly/4myp27m

### Lenny's Podcast (September 2025)
- **Episode:** "Why AI evals are the hottest new skill for product builders"
- **Views:** 101.5K+ on YouTube, 1.6K+ likes
- **Topics covered:** Evals definition, error analysis methodology, open coding, axial coding, LLM-as-judge, vibes vs. systematic evals

### Conferences
- UIST 2024, UIST 2025 (HCI — Human-Computer Interaction)
- VLDB 2024, VLDB 2025 (Data Management)
- NAACL 2025 (NLP — Oral presentation)
- SIGMOD 2024 (Demo)
- ICLR 2022, NIPS 2017, CIDR 2024, CIKM 2023, HILDA 2025

## Mentorship & Impact

Shankar actively mentors undergraduate and junior researchers:
- **Current mentees:** Andrew Cheng, Ruiqi Chen, Siyona Sarma, Sasha Singh, Lindsey Wei
- **Past mentees:** Parth Asawa (now PhD @ Berkeley), Ankush Garg (now Senior Data Scientist), Rachel Lin
- **Co-first author model:** Her NAACL 2025 paper lists mentee Reya Vir as co-first author

Her research has been adopted by **OpenAI and Anthropic teams** for their evaluation pipelines, and her tools (DocETL, EvalGen, SPADE) are used in production by companies building LLM-powered applications.

## Research Funding

- **NDSEG Fellowship** (National Defense Science and Engineering Graduate Fellowship)
- **Bridgewater AI Labs** sponsorship
- **Modal Labs** compute credits
- **EPIC Lab** sponsors at UC Berkeley

## Key Quotes

> *"To build great AI products, you need to be really good at building evals. It's the highest ROI activity you can engage in."*

> *"The highest ROI activity involves looking at actual user interaction data, which most teams neglect by jumping straight to hypothetical test cases without grounding in real problems."*

> *"LLMs can't replace humans in the initial error analysis. AI-driven tools can transform chaos into prioritized problems, but they cannot replace the initial human error analysis step."*

> *"Assign one domain expert with product taste to conduct error analysis rather than forming committees."*

> *"Binary LLM judges are more actionable than Likert scales."*

> *"There's actually a term in data analysis and qualitative analysis called theoretical saturation. When do you stop? It's when you're not uncovering any new types of notes, new types of concepts, or nothing that will materially change the next part of your process."*

## Related Entities

- [[hamel-husain]] — Co-creator of AI evals course, collaborator on Applied LLMs guide
- [[eugene-yan]] — Co-author on Applied LLMs guide, shared evals philosophy
- [[concepts/ai-evals]] — The evaluation framework they teach
- [[concepts/llm-as-judge]] — Core evaluation technique
-  — Foundational practice- [[concepts/harness-engineering]] — Connected philosophy
- [[concepts/eval-tools-comparison]] — Tool selection framework
- [[concepts/critique-shadowing]] — Husain's methodology (complementary)
- [[drmaciver]] — Property-based testing applied to LLM evaluation (`foundational-llm-evals`); PBT methodology for eval design

## Related Concepts

- [[concepts/llm-patterns-eugene-yan]] — Co-author of the O'Reilly Applied LLMs Guide (What We Learned from a Year of Building with LLMs)
- [[entities/eugene-yan]] — Lead author of the Applied LLMs Guide

## Sources

- [Personal Website](https://www.sh-reya.com/) — Research statement, publications, mentees
- [Papers Page](https://sh-reya.com/papers/) — Complete publication list
- [Lenny's Podcast](https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill) — 101.5K+ views
- [DocETL GitHub](https://github.com/ucbepic/docetl) — 3.7K stars
- [UIST 2024 Paper — EvalGen](https://people.eecs.berkeley.edu/~bjoern/papers/shankar-validators-uist2024.pdf)
- [O'Reilly Radar — Applied LLMs Guide](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/)
- [Papers With Code — Shreya Shankar](https://paperswithcode.com/search?q=author%3AShreya+Shankar)
- [ACL Anthology — Shreya Shankar](https://aclanthology.org/people/shreya-shankar/)
