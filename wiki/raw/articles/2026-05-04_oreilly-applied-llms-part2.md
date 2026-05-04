---
title: "What We Learned from a Year of Building with LLMs (Part II): Operations"
source: "https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-ii/"
authors: ["Eugene Yan", "Bryan Bischof", "Charles Frye", "Hamel Husain", "Jason Liu", "Shreya Shankar"]
date: 2024-06-17
tags: [llm, production, data-ops, model-management, product-design, team-building, oreilly]
---

# What We Learned from a Year of Building with LLMs (Part II): Operations

Published by O'Reilly Media, June 2024. Co-authored by **Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, and Shreya Shankar**.

Covers the operational aspects of building LLM applications: **Data, Models, Product, and People.**

---

## 1. Data Operations
The quality of input data constrains performance; output data is the only metric for success.

### Development-Prod Skew
- **Structural Skew:** Formatting discrepancies (JSON vs. list), casing, typos, fragments.
- **Semantic Skew:** Shifts in topics or user intent the model hasn't encountered.
- **Actionable Advice:** Measure skew via input/output length and formatting checks. Use embedding clusters to detect semantic drift. Ensure holdout datasets include production "noise" like typos.

### Daily Data Review ("Vibe Checks")
Developers must look at samples of LLM inputs/outputs every day to identify unpredictable failure modes.
- **Criteria Drift:** Developers' perceptions of "good" vs. "bad" change as they see more data.
- **Operationalize:** Log all pairs, add manual review to on-call rotations. When a failure is found, immediately write a code assertion or evaluation for it.

---

## 2. Working with Models
Managing dependencies on external APIs requires strategies for versioning and integration.

### Structured Output for Integration
"This application pattern is an extreme version of Postel's law: be liberal in what you accept (arbitrary natural language) and conservative in what you send (typed, machine-readable objects)."
- Use Instructor for LLM APIs; Outlines for self-hosted models.

### Model Versioning and Migration
- **Pinning:** Always pin specific model versions (e.g., `gpt-4-turbo-1106`).
- **Migration Pain:** Expect a 10% performance drop when even upgrading within the same family.
- **Shadow Pipelines:** Run a parallel pipeline with the latest model version to test stability before switching.

### Model Selection
Choose the **smallest model** that gets the job done. A smaller model (Claude Haiku) with 10-shot prompt can outperform a zero-shot larger model (GPT-4). For classification, lightweight DistilBERT/DistilBART achieve 0.84 ROC-AUC at <5% cost of LLM.

---

## 3. Product Design
LLM products should be centered on the "job to be done," not the technology.

### Human-in-the-Loop (HITL) UX
- **The Suggestion Pattern:** Instead of full automation, have the LLM suggest and let the user validate/edit.
- **Implicit Feedback:** Accepting a suggestion = strong positive; regenerating = strong negative.

### Prioritization and Risk
- **Hierarchy of Needs:** Prioritize Reliability and Harmlessness first. Accept imperfection in Usefulness and Cost initially.
- **Risk Calibration:** Internal tools allow faster experimentation with lower risk than customer-facing medical/financial bots.

---

## 4. Team and Roles
Building AI products requires a mix of traditional engineering and new specialized skills.

### Process Over Tools
Avoid "LLM Evaluation in a Box" tools offering generic metrics. Focus on **EvalGen principles:**
1. Define domain-specific tests (assertions or LLM-as-a-Judge)
2. Align tests with human judgment
3. Iterate tests as the system changes

### The Evolution of Roles
1. **Product Focus:** AI Engineers for rapid prototyping and UX
2. **Foundations:** Data/Platform Engineers to instrument systems and collect data
3. **Optimization:** ML Engineers to design metrics, optimize RAG, debug stochastic systems

Note: Hiring an MLE too early is a common waste of resources.

### Culture of Experimentation
- Teach the whole team prompt engineering basics.
- Hackathons can accelerate roadmaps via paradigm-shifting UX patterns.
- Set aside specific time for building evals and running offline experiments.
