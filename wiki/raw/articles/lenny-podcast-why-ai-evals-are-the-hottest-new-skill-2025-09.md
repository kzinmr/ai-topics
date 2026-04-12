---
title: "Why AI evals are the hottest new skill for product builders"
source: "Lenny's Podcast"
date: 2025-09-25
authors: ["Shreya Shankar", "Hamel Husain"]
url: "https://open.substack.com/pub/lenny/p/why-ai-evals-are-the-hottest-new-skill"
tags: [ai-evals, evaluation, ai-agents, methodology]
---

# Why AI evals are the hottest new skill for product builders

Shreya Shankar and Hamel Husain teach the world's most popular course on AI evals and have trained over 2,000 PMs and engineers (including many teams at OpenAI and Anthropic). In this conversation, they demystify the process of developing effective evals, walk through real examples, and share practical techniques that'll help you improve your AI products.

## What you'll learn

1. WTF evals are
2. Why they've become the most important new skill for AI product builders
3. A step-by-step walkthrough of how to create an effective eval
4. A deep dive into error analysis, open coding, and axial coding
5. Code-based evals vs. LLM-as-judge
6. Tips and tricks for implementing evals effectively
7. The time investment
8. Insight into the debate between "vibes" and systematic evals

## Key Points

### What are evals?

Evals are systematic methods to measure AI product quality. They replace subjective "vibes-based" assessment with measurable, reproducible checks.

### Error Analysis First

**Always start with error analysis (don't jump into writing evals).** Before writing a single eval, manually review real user interaction traces. The highest ROI activity involves looking at actual user interaction data, which most teams neglect by jumping straight to hypothetical test cases without grounding in real problems.

### Open Coding & Axial Coding

1. Review 100 production traces manually
2. Write freeform notes on the first errors you observe
3. Use LLMs to categorize notes into actionable failure modes
4. Continue until "theoretical saturation" — when no new categories emerge

### The "Benevolent Dictator" Approach

Assign one domain expert with product taste to conduct error analysis rather than committees. This maintains consistency in taxonomy development.

### Code-based Evals vs. LLM-as-Judge

- **Code-based evals:** Deterministic, fast, cheap. Use for structured tasks with clear pass/fail criteria.
- **LLM-as-judge:** Can evaluate subjective, open-ended outputs. Use binary pass/fail, not Likert scales. Test your LLM judge against human judgment.

### Strategic Eval Investment

Write 4-7 LLM judge evaluators for persistent, ambiguous failure modes that resist prompt fixes. Skip evals for obvious engineering errors.

### Evals are the New PRDs

Well-crafted eval prompts effectively become living product requirements documents.

### The Truth About Claude Code's "No Evals" Claim

The popular "you don't need evals" stance is misleading—and how rigorous evals remain essential.

### Dogfooding Isn't Enough

Why dogfooding isn't enough for most AI products.

## Real-World Example

A demonstration revealed how a real estate AI assistant told a prospective tenant no apartments with studies were available, then said thanks and goodbye—completely missing the lead nurturing opportunity. This failure only became visible through systematic error analysis of production traces.

## Timestamps

- (00:00) Introduction to Hamel and Shreya
- (04:57) What are evals?
- (09:56) Demo: Examining real traces from a property management AI assistant
- (16:51) Writing notes on errors
- (25:16) The concept of a "benevolent dictator" in the eval process
- (28:07) Theoretical saturation: when to stop
- (54:45) Testing your LLM judge against human judgment
- (01:00:51) Why evals are the new PRDs for AI products
- (01:05:09) How many evals you actually need
- (01:07:41) What comes after evals
- (01:09:57) The great evals debate
- (1:15:15) Why dogfooding isn't enough for most AI products
- (1:22:28) Tips and tricks for implementing evals effectively
- (1:30:37) The time investment
- (1:33:38) Overview of their comprehensive evals course

## Where to Find Them

### Shreya Shankar
- X: [@sh_reya](https://x.com/sh_reya)
- LinkedIn: [shrshnk](https://www.linkedin.com/in/shrshnk/)
- Website: [sh-reya.com](https://www.sh-reya.com/)
- Maven course: https://bit.ly/4myp27m

### Hamel Husain
- X: [@HamelHusain](https://x.com/HamelHusain)
- LinkedIn: [hamel](https://www.linkedin.com/in/hamelhusain/)
- Website: [hamel.dev](https://hamel.dev/)
- Maven course: https://bit.ly/4myp27m

## Referenced
- Building eval systems that improve your AI product: https://www.lennysnewsletter.com/p/building-eval-systems-that-improve
- Mercor: https://mercor.com/
- Andrew Ng on X: https://x.com/andrewyng
