---
title: "IFEval (Instruction-Following Evaluation)"
type: concept
created: 2026-05-08
tags:
sources: []
  - benchmark
  - evaluation
related_concepts:
  - concepts/ai-benchmarks-and-evals
  - concepts/codeif-bench
  - concepts/ifeval-fc
  - concepts/logic-ifeval
related_entities:
  - entities/google-research
  - entities/yale-university
  - entities/florian-brand
---

# IFEval (Instruction-Following Evaluation)

## Overview

IFEval (Instruction-Following Evaluation) is a benchmark introduced by Google Research and Yale University in November 2023 that evaluates how well large language models follow natural language instructions. It takes a deliberately simple approach: instead of relying on expensive human evaluation or potentially biased LLM-as-judge methods, IFEval uses **verifiable instructions** — constraints that can be checked deterministically by a program.

The core insight is elegant: by focusing on instructions with objective, programmatically verifiable criteria (e.g., "write at least 400 words," "include the keyword 'AI' at least 3 times," "end your response with 'Goodbye'"), the evaluation becomes completely automated, reproducible, and immune to LLM-judge biases.

Since its release, IFEval has become one of the most widely adopted LLM benchmarks, integrated into major evaluation frameworks like EleutherAI's lm-evaluation-harness. It has also spawned derivative benchmarks: CodeIF-Bench (instruction following in code generation), IFEval-FC (instruction following in function calling), and LogicIFEval (complex logical instruction following).

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Instruction following — a core LLM capability |
| **Task type** | Generate text responses that satisfy one or more verifiable constraints |
| **Format** | Text prompt with embedded instructions → response checked against deterministic rules |
| **Evaluation** | 100% deterministic, programmatic — each instruction type has a dedicated verifier function |
| **Metric** | Strict accuracy (all instructions in a prompt must be satisfied) and loose accuracy (proportion of individual instructions satisfied) |

### The 25 Verifiable Instruction Types

IFEval defines 25 categories of verifiable instructions. These are grouped into several families:

**Content constraints:**
- Include specific keywords (e.g., "mention 'artificial intelligence' at least once")
- Keyword frequency (e.g., "use the word 'data' exactly 3 times")
- Exclude specific words or phrases

**Format constraints:**
- Word count (minimum, maximum, or exact range)
- Sentence count
- Paragraph count
- Response structure (e.g., "start with 'Introduction:'", "end with 'Conclusion'")

**Stylistic constraints:**
- Write entirely in uppercase/lowercase
- Use specific punctuation requirements
- Avoid certain punctuation marks

**Structural constraints:**
- Number of sections or bullet points
- Presence of specific sections (introduction, body, conclusion)
- Ordered list with specific items

**Language constraints:**
- Respond in a specific language
- Code block formatting
- JSON output format

Each prompt contains one or more of these instructions. A response is scored as "correct" only if ALL instructions in the prompt are satisfied simultaneously — making this a strict test of multi-constraint instruction following.

### Example Prompts

> "Write a summary of climate change in exactly 3 paragraphs. Mention the word 'carbon' at least twice. End your response with '---'."

> "Explain quantum computing in more than 200 words but fewer than 400 words. Include the keywords 'superposition' and 'entanglement'. Do not use the word 'classical'."

> "Write a poem about autumn. The poem must have exactly 4 stanzas. Each stanza must have exactly 4 lines. The word 'leaf' must appear at least 3 times."

## Data Sourcing

| Detail | Value |
|--------|-------|
| **Total prompts** | ~500 (541 in the original release) |
| **Instruction types** | 25 distinct verifiable instruction categories |
| **Instructions per prompt** | 1 or more (typically 2–4) |
| **Creation method** | Manual construction by the research team |
| **Release date** | November 14, 2023 |
| **Paper** | "Instruction-Following Evaluation for Large Language Models" (arXiv:2311.07911) |
| **Code** | Open-source: `github.com/google-research/google-research/tree/master/instruction_following_eval` |
| **License** | Creative Commons Attribution 4.0 (CC-BY 4.0) |
| **Integration** | Available in EleutherAI's lm-evaluation-harness as the `ifeval` task |

The prompts were manually constructed to cover diverse combinations of instructions. Unlike benchmarks that use crowd-sourced or web-scraped data, the IFEval prompts are entirely synthetic and purpose-built — each one is a carefully designed test of specific instruction-following capabilities.

## Key Numbers

### Human Baseline
Humans would trivially score near 100% on IFEval — the instructions are simple to follow (e.g., "write 400 words," "mention X 3 times"). The benchmark is designed to expose LLM weaknesses, not human ones. There is no formal human baseline published.

### Original Paper Baselines (November 2023)
| Model | Strict Accuracy | Loose Accuracy |
|-------|----------------|----------------|
| GPT-4 | ~83% | ~88% |
| PaLM 2 (L) | ~53% | ~63% |
| PaLM 2 (M) | ~41% | ~52% |

### Top Model Scores (as of May 2026)

| Model | Score |
|-------|-------|
| Qwen3.5-27B | 0.950 |
| Qwen3.6 Plus | 0.943 |
| o3-mini | 0.939 |
| Qwen3.5-122B-A10B | 0.934 |
| Claude 3.7 Sonnet | 0.932 |
| Qwen3.5-397B-A17B | 0.926 |
| Llama 3.3 70B Instruct | 0.921 |
| Nova Pro | 0.921 |
| GPT-4.1 | 0.874 |
| DeepSeek-V3 | 0.861 |

**Key statistics:**
- Average score across 63 evaluated models: **0.843**
- Best score: **0.950** (Qwen3.5-27B)
- Standard deviation: ~0.05
- The benchmark is approaching saturation at the top end, with several models above 0.92.

The progression from GPT-4's ~83% (Nov 2023) to Qwen3.5-27B's 95% (2026) shows significant improvement in instruction-following capabilities across the industry. The relatively narrow spread at the top (0.921–0.950 for the top 10) suggests IFEval may be approaching its useful differentiation ceiling for frontier models.

## @xeophon's Key Insight

> IFEval is a cool, super simple eval. It tests one specific aspect of LLMs — instruction following — and does it elegantly. The evaluation is trivially easy because every instruction is programmatically verifiable. No LLM-as-judge, no human raters, no ambiguity. It's a pure capability check that every model developer should run.

## Strengths

1. **Completely deterministic evaluation**: No LLM judge bias, no human subjectivity — every instruction is checked by a verifier program. Results are 100% reproducible.
2. **Fast and cheap to run**: No API calls needed for evaluation; just run the verifier programs on model outputs.
3. **Simple and interpretable**: It's immediately clear what each prompt is testing and why a model passed or failed.
4. **Widely adopted**: Integrated into lm-evaluation-harness and used by virtually all major model developers.
5. **Spawned a family of benchmarks**: CodeIF-Bench, IFEval-FC, LogicIFEval, and others extend the verifiable-instruction paradigm to new domains.
6. **Tests multi-constraint following**: Prompts with multiple simultaneous instructions test a model's ability to satisfy competing constraints.

## Weaknesses

1. **Narrow scope**: Only tests surface-level constraint following, not semantic instruction understanding. A model could pass IFEval with perfect scores while completely misunderstanding the intent of more nuanced instructions.
2. **Approaching saturation**: Top models are scoring above 0.92, and the best (0.950) is within 5 points of perfection. The benchmark may soon lose its ability to differentiate frontier models.
3. **Synthetic prompts**: Manually constructed prompts test for specific patterns that models can learn to recognize without developing general instruction-following ability.
4. **No real-world task integration**: Instructions are isolated ("write 400 words about X") rather than embedded in realistic use cases ("write a 400-word executive summary of this earnings report").
5. **Ignores response quality**: A model can satisfy all verifiable constraints while producing nonsensical or low-quality content. IFEval explicitly does not evaluate the semantic quality of responses.
6. **Fixed instruction types**: The 25 categories, while diverse, don't cover all aspects of instruction following (e.g., tone, politeness, role-playing consistency).

## Related Wiki Pages

- `concepts/ai-benchmarks-and-evals` — Overview of the AI benchmarks and evals landscape
- `concepts/codeif-bench` — CodeIF-Bench, extending verifiable instruction evaluation to code generation
- `concepts/ifeval-fc` — IFEval-FC, verifiable instruction following in function calling
- `concepts/logic-ifeval` — LogicIFEval, complex logical instruction following
- `entities/florian-brand` — @xeophon, author of the AI Benchmarks & Evals analysis series
- `entities/google-research` — Google Research, co-creators of IFEval
- `entities/yale-university` — Yale University (Jeffrey Zhou), co-creator of IFEval

## Sources

1. Zhou, J., Lu, T., Mishra, S., Brahma, S., Basu, S., Luan, Y., Zhou, D., Hou, L. (2023). "Instruction-Following Evaluation for Large Language Models." arXiv:2311.07911. https://arxiv.org/abs/2311.07911
2. IFEval on GitHub (Google Research). https://github.com/google-research/google-research/tree/master/instruction_following_eval
3. IFEval in EleutherAI lm-evaluation-harness. https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ifeval/README.md
4. LLM Stats — IFEval Leaderboard. https://llm-stats.com/benchmarks/ifeval
5. Scale Labs — Instruction Following Leaderboard. https://labs.scale.com/leaderboard/instruction_following
6. Wang, P., et al. (2025). "CodeIF-Bench: Evaluating Instruction-Following Capabilities of LLMs in Interactive Code Generation." arXiv. (Derivative benchmark)
7. Skripko, N. (2025). "Instruction-Following Evaluation in Function Calling for Large Language Models." arXiv. (IFEval-FC)
