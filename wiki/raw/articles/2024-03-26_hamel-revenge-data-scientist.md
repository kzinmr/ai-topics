# The Revenge of the Data Scientist

- **URL:** https://hamel.dev/blog/posts/revenge/
- **Author:** Hamel Husain
- **Date:** March 26, 2024
- **Scraped:** 2026-04-30

---

## Core Thesis

While LLM APIs allow engineers to ship AI without traditional data scientists, the "harness" required to make these systems reliable—evaluations, metrics, and debugging—is fundamentally a data science problem. The role is not in decline; it is becoming more critical as systems become more stochastic.

---

## The Definition of a Data Scientist

> Data Scientist (n.): Person who is better at statistics than any software engineer and better at software engineering than any statistician.
> — *Josh Wills*

Historically, data scientists were on the "critical path" for shipping AI. With the rise of foundation models, many feel sidelined. Husain argues this is a misconception: training models was never the bulk of the work; the real work is **setting up experiments, debugging stochastic systems, and designing metrics.**

---

## The "Harness" is Data Science

Modern AI agents (like OpenAI's Codex or Karpathy's auto-researcher) operate within a "harness" of tests, specifications, and observability stacks. Husain posits that a large portion of this harness is actually data science.

### The Current Problem: "Vibe-based" Engineering

Engineers are currently building on "vibes," using off-the-shelf metrics without looking at data. This leads to five major pitfalls.

---

## 5 Major Eval Pitfalls (and the Data Science Fix)

### 1. Generic Metrics

- **The Pitfall:** Using off-the-shelf scores (helpfulness, coherence, hallucination) that are too generic to diagnose specific application failures.
- **The Fix:** **Look at the data.** Read traces, code custom trace viewers, and perform error analysis to find application-specific metrics (e.g., "Calendar Scheduling Failure" vs. a generic "Coherence" score).

### 2. Unverified Judges

- **The Pitfall:** Using an LLM as a judge without knowing if the judge itself is accurate.
- **The Fix:** Treat the judge like a **classifier**.
  - Get human labels.
  - Partition data into train/dev/test.
  - Measure **Precision and Recall** rather than just Accuracy (which hides failures in imbalanced data).

### 3. Bad Experimental Design

- **The Pitfall:** Generating synthetic test sets by simply asking an LLM for "50 queries," resulting in unrepresentative data.
- **The Fix:**
  - Ground synthetic data in **real production logs**.
  - Replace subjective 1-5 Likert scales with **binary pass/fail** criteria tied to business outcomes.

### 4. Bad Data and Labels

- **The Pitfall:** Outsourcing labeling or treating it as a low-value task.
- **The Fix:** Data scientists are skeptics. They insist on **domain experts** for labeling.
  - **Criteria Drift:** Users often don't know what they want until they see the LLM's output. The act of labeling helps define the requirements.

### 5. Automating Too Much

- **The Pitfall:** Trying to automate the "looking at data" step.
- **The Fix:** LLMs can write the plumbing and boilerplate, but they cannot decide if an output is "good" for your specific business context—only a human looking at the data can do that.

---

## Summary Mapping: Old Skills, New Names

Husain argues that modern LLM workflows map directly to classic Data Science fundamentals:

| Modern LLM Task | Data Science Fundamental |
| :--- | :--- |
| Reading traces/categorizing failures | **Exploratory Data Analysis (EDA)** |
| Validating an LLM judge | **Model Evaluation** |
| Building test sets from logs | **Experimental Design** |
| Expert labeling | **Data Collection** |
| Monitoring production performance | **Production ML** |

---

## Actionable Takeaways

- **Highest ROI Activity:** Look at the data (read the traces).
- **Tooling:** Python remains the best toolset for data exploration.
- **Resource:** Husain developed an open-source plugin [evals-skills](https://github.com/hamelsmu/evals-skills) to help identify errors in evaluation pipelines.
- **Metric Design:** Move away from vague similarity scores (ROUGE/BLEU) toward metrics that measure specific failure modes.
