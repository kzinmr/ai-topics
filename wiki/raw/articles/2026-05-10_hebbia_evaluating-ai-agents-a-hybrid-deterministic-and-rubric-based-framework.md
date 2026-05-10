---
title: "Evaluating AI Agents: A Hybrid Deterministic and Rubric-Based Framework"
source: "Hebbia Blog"
url: "https://www.hebbia.com/blog/evaluating-ai-agents-a-hybrid-deterministic-and-rubric-based-framework"
scraped: "2026-05-10T01:27:04.046202+00:00"
lastmod: "2026-05-08"
type: "sitemap"
---

# Evaluating AI Agents: A Hybrid Deterministic and Rubric-Based Framework

**Source**: [https://www.hebbia.com/blog/evaluating-ai-agents-a-hybrid-deterministic-and-rubric-based-framework](https://www.hebbia.com/blog/evaluating-ai-agents-a-hybrid-deterministic-and-rubric-based-framework)

Engineering
By Joseph Renner
03.26.26
Evaluating AI Agents: A Hybrid Deterministic and Rubric-Based Framework
How Hebbia measures agent quality at scale with a hybrid evaluation methodology.
End-to-end evaluations are valuable to capture emergent behaviors and system-level quality for AI agents that take on increasingly complex orchestration, analysis, and reasoning tasks. However, there is a vacuum of AI industry standards for subagent testing, and existing methods often rely on anecdotal assessment, rather than quantitative evidence.
When an agent generates a visualization, summarizes a document, or coordinates a multi-step analysis, there's rarely a single "correct" answer. Concrete insight into where agents fail is what makes targeted architectural improvements possible.
Hebbia’s approach to agent evaluation combines traditional deterministic checks with rubric-based LLM grading. This robust and systematic architecture, principled rubric design, and holistic scoring results in faster and more effective agent development.
The Hybrid Evaluation Approach
Our subagent evaluation methods target agents’ discrete behaviors and capabilities. We use rubric-based LLM graders alongside deterministic checks to produce focused, interpretable results that diagnose exactly where quality issues originate.
Deterministic checks handle verifiable properties of agent outputs such as schema validation, required field presence, data type correctness, and formatting compliance to produce fast, reliable, and consistent results.
Rubric-based evaluations by LLMs assess either outcomes or processes for properties like coherence, completeness, and domain-appropriateness. Outcome-focused evaluation is appropriate for agents with constrained scope and minimal reasoning. For multi-step agents utilizing complex tools, process-focused criteria evaluate the entire reasoning path, not just the destination.
This hybrid approach allows for exact matches to test factual correctness while assessing open-ended properties that require model-based judges.
LLM Grader System Architecture
Our LLM graders apply rubric criteria to agent outputs on many sets of test cases with precision. To achieve this, we’ve invested heavily in two often-underestimated requirements that have proven to be essential for effective evaluation results: dataset construction and variance control.
Dataset Construction
We construct test cases that approximate production distributions without using actual user data. Though synthetic, these datasets are anything but arbitrary.
Building effective test inputs requires partnership with expert data providers — including data labeled by domain experts — and bootstrapping from existing ground truth. Depending on the subagent, we leverage labeled examples, known correct outputs, and documented edge cases to seed our test distributions.
To validate coverage, we pass test case profiles to our in-house financial domain experts to identify gaps and failure modes. As Hebbia power users, they have unique insight into the gap between what financial professionals expect and what our agents produce and ensure our synthetic dataset reflects what agents will actually encounter in production.
Output Variance Control
Given static inputs, agent outputs can vary across runs even with low temperatures. We pass multiple data samples through our agents to return several sets of responses for evaluation. This allows us to differentiate systematic failures (the agent consistently gets something wrong) from stochastic failures (the agent sometimes gets it wrong by random chance).
LLM-graders are subject to the same stochasticity as agents, potentially returning different output scores across runs with consistent inputs. To control for this, we also run multiple grading passes per evaluation and aggregate results. This reduces noise from grader non-determinism and surfaces rubric ambiguity—if graders frequently disagree on a criterion, that criterion needs refinement, not more grading passes.
Rubric Design Principles
Our rubrics are specifically designed for answering questions like:
Is this visualization choice appropriate for the data?
Is the summary accurate and complete?
Does the response match what a domain expert would expect?
We’ve converged on several design constraints to make rubrics more reliable and actionable in our financial workflow context:
One Criterion, One Failure Mode:
Each criterion targets a single, diagnosable issue. This atomicity makes LLM graders more consistent, accurate, and allows for tractable debugging.
Pass/Fail Only:
Binary decisions are faster for LLM graders to converge on and easier to validate against human judgment. If we need more granularity, we add more criteria rather than adding more score levels.
Grounded in Specifics:
Financial workflows demand precision. For example, rather than asking "is this chart type appropriate?", our criteria specify exact mappings: LINE for continuous trends, BAR for discrete comparisons, STACKED BAR for part-to-whole over multiple periods. "Good title" means nothing actionable. "Title is descriptive, specific, 5-10 words, without units or scale information" can be consistently applied.
Distinct Coverage:
Redundant criteria distort scores and waste evaluation compute. If two criteria tend to pass or fail together, they're probably measuring the same underlying capability. In such a case criteria are either removed or revised for narrower scopes to ensure distinct measurements.
Criteria are able to distinguish good from great:
Criteria are designed at two levels, required criteria represent SLAs of the agent, while additional criteria represent conditions that represent advanced capabilities but would not lead to failure.
Hebbia's advantage is that we engage in-house financial domain experts throughout rubric development. Our experts define what constitutes correct, high-quality outputs and identify common error modes. We use these insights to generate initial rubric criteria with LLM assistance, then pass them back to our experts to review for accuracy, weighting, clarity, and completeness.
We then apply rubrics to diverse outputs and have our specialists validate results across quality levels. Rubrics are iteratively refined as new failure modes surface in production, requirements evolve based on user feedback, or agent capabilities improve.
Extracting Insights From Rubric Scores
A common reaction when first seeing a 60% rubric score is to assume that the agent is broken. This intuition comes from academic grading, where 60% means you missed almost half the material. Rubric-based evaluation works differently.
Our rubrics are designed to be aspirational and hill-climbable, capturing not just minimum acceptability but the full spectrum of quality up to expert-level excellence. A response that passes all required criteria and hits some additional criteria is doing its job well, even if the percentage looks modest. Additional criteria exist to give us room to measure improvement over time — if agents routinely scored 95%, we'd have no signal for optimization and no way to distinguish good from great.
This framework generates detailed diagnostics rather than flat test scores.
Why Agent Evaluation Requires Quantitative Evidence
End-to-end evaluations capture emergent behaviors and system-level quality, but they don't tell you
why
an agent failed or
where
to fix it. For AI agents taking on increasingly complex tasks, that diagnostic gap matters. Subagent testing often relies on anecdotal evidence rather than quantitative measurement — especially when there's rarely a single "correct" answer to evaluate against.
Hebbia's approach combines deterministic checks with rubric-based LLM grading to fill this gap. Domain expert-driven rubric design, variance-controlled scoring, and granular pass/fail criteria give us concrete, actionable insight into each subagent's strengths and weaknesses. The result is faster diagnosis, targeted architectural improvements, and agent development grounded in evidence rather than intuition.
