---
title: "AI Evals (AI Evaluation Systems)"
tags: [[evaluation-llm-as-judge-error-analysis-ai-engineering-ai-systems]]
created: 2026-04-12
updated: 2026-04-24
---

# AI Evals (AI Evaluation Systems)

Product-specific evaluation systems for measuring whether an AI application works correctly on real tasks with real data. **Not** foundation model benchmarks like MMLU, HELM, or GPQA.

## Core Thesis

> "Unsuccessful AI products almost always share a common root cause: a failure to create robust evaluation systems." — Hamel Husain

Success in AI product development hinges on **iteration speed**, which is bottlenecked by evaluation quality. A robust eval system creates a virtuous cycle:

1. **Evaluate Quality** (tests, metrics)
2. **Debug Issues** (logging, trace inspection)
3. **Change Behavior** (prompt engineering, fine-tuning, code updates)

Focusing only on #3 leads to "demo-only" products that plateau. The key metric for AI development isn't features shipped — it's **experiments run**.

## The 3 Levels of Evaluation

### Level 1: Unit Tests (Fast & Cheap)
- Run on every code change to catch regressions
- Break LLM capabilities into features/scenarios, write reusable assertions
- Use LLMs to synthetically generate diverse, challenging inputs
- Track pass/fail rates in CI/CD pipelines with dashboards (e.g., Metabase)
- **Unlike traditional unit tests, you don't necessarily need a 100% pass rate** — your pass rate is a product decision, depending on the failures you are willing to tolerate

### Level 2: Human & Model Evaluation (Debugging & Alignment)
- Requires **trace logging** (grouped LLM interactions)
- Build custom labeling UIs (Gradio, Streamlit, Shiny, Panel) to reduce friction
- Start with **binary** (pass/fail) labels, not granular scoring
- Use LLM-as-Judge: a more powerful model critiques outputs, track correlation with human labels
- **Critical metric**: Use precision/recall for imbalanced datasets, not raw agreement
- Track inter-annotator agreement (Cohen's Kappa) when multiple reviewers exist

### Level 3: Online Evaluation (Production Monitoring)
- A/B testing, user feedback, behavioral metrics
- Monitor for drift in real-world performance
- Use production traces to continuously expand eval datasets
- Alert on metric anomalies, not just absolute thresholds

## The Iteration Flywheel

```
Error Analysis → Build Eval Dataset → Create Judges → Run Experiments → Fix Errors → Repeat
```

Each cycle makes the system more reliable. Most teams skip error analysis and jump straight to building, which is the single biggest mistake.

## Key Principles

### Binary Over Likert Scales
- Use **pass/fail** judgments, not 1-5 scales
- Likert scales introduce subjectivity, inconsistency, and middle-value bias
- "If someone says they need 8 dimensions on a 1-5 scale, they don't know what they're looking for"
- Track gradual improvements via sub-component binary checks

### Error Analysis > Metrics
- **Bottom-up approach** (recommended): Examine actual data, annotate failures, let metrics emerge naturally
- **Top-down approach** (avoided): Starts with generic metrics (hallucination, toxicity), misses domain-specific issues
- Generic metrics are worse than useless — they create false confidence and fragment attention
- **Case study**: NurtureBoss annotated conversation logs, discovered 3 issues accounting for **>60% of all problems**, date handling success improved from **33% → 95%**

### The Principal Domain Expert
- Every AI product needs one (maybe two) key individuals whose judgment is crucial
- Examples: a psychologist for mental health AI, a lawyer for legal AI, a customer service director for support bots
- They set the standard, capture unspoken expectations, ensure consistency
- In small companies, this might be the CEO/founder; for indie devs, it's themselves (but must be honest about expertise)

### Pass Rate Warning
> "Be wary of optimizing for high eval pass rates. If you're passing 100% of your evals, you're likely not challenging your system enough. A 70% pass rate might indicate a more meaningful evaluation that's actually stress-testing your application."

### Budget & Time Allocation
- Evals are part of development (like debugging)
- Expect to spend **60-80% of dev time** on error analysis & evaluation
- Don't sell "evals" to stakeholders — show data stories: top failure modes, error frequency, fixed bugs
- Review cadence: re-run after major changes (2-4 week cycles, 100+ fresh traces). Between cycles: 10-20 weekly, focusing on outliers

### Process > Tools
- No single "best" eval tool exists — selection depends on team's skillset, technical stack, and maturity
- The tool should enable a rigorous evaluation workflow, not replace it
- "Process first, tools second" — avoid treating evals as an off-the-shelf solution

## Synthetic Data Strategy

### When to Use
- Cold-start problem: you need data to improve AI, but need AI to get users
- LLMs are surprisingly good at generating diverse, realistic user inputs

### How to Generate
1. Define **dimensions** relevant to your use case (Features, Scenarios, User Personas)
2. Create 20 tuples manually first, then scale with LLM generation
3. Two-step process: (a) LLM generates structured tuples, (b) Separate prompt converts tuples to natural language queries
4. **Generate inputs, not outputs** — prevents inheriting model biases
5. Ground in real constraints (actual DBs, schedules, business rules, local regulations)
6. Verify scenario coverage (ensure queries actually trigger intended edge cases)

### When Synthetic Fails
- Complex domain content, low-resource languages, high-stakes domains
- Underrepresented user groups, or when validation is impossible

## Human Annotation Process

### The 4-Step Error Analysis Process
1. **Create Dataset**: Gather representative traces (real or synthetic)
2. **Open Coding**: Human annotator journals issues. Focus on the *first* upstream failure
3. **Axial Coding**: Group notes into a failure taxonomy. Count occurrences per category
4. **Iterative Refinement**: Review until theoretical saturation (~100 traces minimum)

### Outsourcing Warning
- Usually a mistake — breaks feedback loops, causes superficial labeling, loses tacit knowledge
- Exceptions: purely mechanical tasks, tasks without product context, or hiring external SMEs

### Surfacing Problematic Traces
- Random sampling → stress testing → existing evals → efficient sampling
- Outlier detection, metric sorting, stratified sampling, embedding clustering

## Trace Definition

A **trace** is the complete record of all actions, messages, tool calls, and data retrievals from initial query to final response. Vendor definitions vary significantly. Traces are the fundamental unit of eval analysis.

## Minimum Viable Setup

1. Start with **error analysis**, not infrastructure
2. Manually review 20-50 outputs per significant change
3. Use a single domain expert as a **"benevolent dictator"** for quality decisions
4. Build a simple data viewer (spreadsheet → custom web app)
5. Show all context in one place (no system-hopping)
6. Enable trivial feedback capture (1-click correct/incorrect)

## Key Mistakes to Avoid

1. **The Tools Trap**: Buying complex eval platforms before doing error analysis
2. **Metric Sprawl**: Too many metrics fragment attention — "When everything is important, nothing is"
3. **Skipping Domain Experts**: Not involving people who understand the subject matter deeply
4. **Unvalidated Metrics**: Using measurements that don't truly reflect what matters to users or business
5. **Arbitrary Scoring**: Using uncalibrated 1-5 scales where the difference between scores is unclear
6. **Eval-Driven Development**: Writing evaluators for imagined errors rather than discovered ones (exception: strict, known constraints like "never mention competitors")

## Related Concepts

- [[llm-as-judge]] — Using LLMs to evaluate AI outputs
- [[critique-shadowing]] — 7-step process for building aligned LLM judges
-  — Systematic categorization of failure modes
- [[harness-engineering]] — OpenAI's approach to AI-assisted development
- [[eval-tools-comparison]] — LangSmith vs Braintrust vs Phoenix vs Inspect AI
- [[evals-skills]] — Evals skills for coding agents
-  — PBT methodology applied to LLM evaluation (MacIver)

## Related People

- [[drmaciver]] — Created `foundational-llm-evals` applying property-based testing to LLM evaluation
- [[shreya-shankar]] — Co-creator of AI evals course, DocETL/EvalGen/SPADE researcher
- [[hamel-husain]] — Co-creator of AI evals course, Critique Shadowing methodology pioneer

## Sources

- [Why AI Evals Are the Hottest New Skill](https://open.substack.com/pub/lenny/p/why-ai-evals-are-the-hottest-new-skill) — Lenny's Newsletter (2025) featuring Hamel Husain
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — Hamel Husain
- [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/) — Hamel Husain (October 29, 2024)
- [LLM Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) — Hamel Husain
- [Selecting The Right AI Evals Tool](https://hamel.dev/blog/posts/eval-tools/) — Hamel Husain
- [Evals Skills for Coding Agents](https://hamel.dev/blog/posts/evals-skills/) — Hamel Husain
- [A Field Guide to Rapidly Improving AI Products](https://hamel.dev/blog/posts/field-guide/) — Hamel Husain
- [Inspect AI](https://hamel.dev/notes/llm/evals/inspect.html) — Hamel Husain
