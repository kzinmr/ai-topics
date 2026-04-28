---
title: "Critique Shadowing"
tags: [llm-as-judge-evaluation-methodology-human-in-the-loop]
created: 2026-04-12
updated: 2026-04-24
type: concept
---

# Critique Shadowing

A 7-step iterative methodology for building aligned LLM-as-Judge evaluators, coined by **Hamel Husain**. The core insight: the process of building an LLM judge forces domain experts to carefully examine data and articulate evaluation criteria, which creates value even beyond the judge itself.

> "The real value of this process is looking at your data and doing careful analysis. Creating an LLM judge is a nice 'hack' I use to trick people into carefully looking at their data!" — Hamel Husain

## The 7-Step Process

### Step 1: Find The Principal Domain Expert
- Identify the one (maybe two) key individuals whose judgment is crucial for the AI product's success
- Examples: psychologist for mental health AI, lawyer for legal AI, customer service director for support bots
- They set the standard and capture unspoken expectations
- **Never skip this step** — developers acting as their own domain experts leads to biased evaluation

### Step 2: Create a Dataset
- Build a dataset capturing the problems the AI will encounter in production
- Define **dimensions** relevant to your use case (Features, Scenarios, User Personas)
- Use a mix of real user interactions and LLM-generated synthetic inputs
- Generate **inputs, not outputs** — prevents inheriting model biases
- Ground synthetic data in real constraints (actual DBs, business rules)
- Continue generating until you stop seeing new failure modes (theoretical saturation)

### Step 3: Domain Expert Reviews Data (Pass/Fail + Critiques)
- Expert makes **binary pass/fail** judgments on each interaction
- Expert writes **detailed critiques** explaining their reasoning
- Critiques must be detailed enough that a new employee could understand them
- Present all context on a single screen (user metadata, system info, resources)
- Start with ~30 examples, continue until no new failure modes emerge
- **Don't stray from binary judgments** — Likert scales are not actionable early on

### Step 4: Fix Errors
- Address obvious errors found during review before building the judge
- If pervasive errors exist, fix them and return to Step 3
- Every fixed error should become a test case

### Step 5: Build Your LLM as A Judge, Iteratively
- Create a judge prompt using expert examples as few-shot demonstrations
- Each example includes: the input (in `<input>` tags), the AI output (in `<output>` tags), and the expert's critique + outcome (in `<critique>` tags)
- Test the judge against expert judgments on held-out data
- Refine the prompt until agreement is satisfactory (>90% in Hamel's Honeycomb case, achieved in 3 iterations)
- Use **precision and recall** for imbalanced datasets, not raw agreement
- The process of building the judge helps the domain expert standardize their own criteria ("criteria drift")

### Step 6: Perform Error Analysis
- Calculate error rates across different dimensions (persona, scenario, feature)
- Classify traces by root cause (e.g., Missing User Education, Authentication Issues, Poor Context Handling)
- Use spreadsheets or custom tools for classification
- Focus on the most prevalent root causes first

### Step 7: Create Specialized LLM Judges (if needed)
- After identifying specific failure patterns, create targeted evaluators
- Some errors may only need code-based assertions, not LLM judges
- **Don't jump to specialized judges** until you've gone through the full critique shadowing process

## Criteria Drift

A phenomenon identified by Shankar et al. where the process of grading LLM outputs helps domain experts define and refine their evaluation criteria. The judge and the judged co-evolve.

> "To grade outputs, people need to externalize and define their evaluation criteria; however, the process of grading outputs helps them to define that very criteria."

## Common Pitfalls

1. **Overscoped AI**: Chatbots that promise to do anything are impossible to evaluate
2. **Not following the process**: Skipping the domain expert, not writing proper critiques
3. **Unrealistic alignment expectations**: Sometimes human annotations are still needed
4. **Terse critiques**: Judge prompts need detailed, explanatory critiques as examples
5. **Missing external context**: Examples must include the same information used to evaluate (user metadata, system info)
6. **Lack of diversity**: Need wide variety of examples to ensure the judge works across inputs

## When to Skip Steps

For independent developers who are also domain experts, working with test data that's already available, and where looking at data is not costly — you can jump directly to Step 3 and start reviewing data immediately. However, **you can never completely eliminate looking at your data**.

## Related Concepts

- [[concepts/ai-evals]] — Main evaluation framework
- [[concepts/llm-as-judge]] — Using LLMs to evaluate AI outputs
-  — Systematic categorization of failure modes

## Sources

- [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/) — Hamel Husain (October 29, 2024)
- [LLM Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) — Hamel Husain
- ["Who Validates the Validators?" — Shankar et al.](https://arxiv.org/abs/2409.09148) — Paper on criteria drift
