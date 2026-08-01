---
title: "LLM Evaluation"
type: concept
aliases:
  - llm-evaluation
created: 2026-04-25
updated: 2026-08-01
tags:
  - concept
  - evaluation
  - benchmark
sources:
  - raw/articles/simonwillison.net--2026-jul-31-smevals--e6e7fe34.md
status: active

---

# LLM Evaluation

Evaluation of LLMs covers benchmarks, evals, grading, and harnesses used to measure model capabilities. This page documents evaluation tools and methodology; individual benchmarks live under [[concepts/ai-benchmarks]].

## smevals — Small Eval Suite (July 2026)

**smevals** is a small eval framework for evaluating models, prompts, and harnesses, built by [[entities/simon-willison|Simon Willison]] in collaboration with Jesse Vincent's Prime Radiant applied AI research lab. Simon describes it as his "third iteration" on eval tooling.

### Usage

```bash
uvx smevals run path-to-eval/ -m gpt-5.5 -m claude-opus-4.6
uvx smevals grade path-to-eval/        # grade runs against defined checks
uvx smevals serve path-to-eval/        # localhost web server to explore results
uvx smevals build path-to-eval/        # static HTML report
```

An eval is a directory of YAML files; `uvx smevals docs` outputs the README so a coding agent can learn the tool.

### Vocabulary

| Term | Definition |
|------|-----------|
| **eval** | A collection of challenges designed to answer a question about a model (e.g., "how good is that model at generating SVGs?") |
| **task** | A specific challenge within an eval (e.g., "Generate an SVG of a pelican riding a bicycle") |
| **config** | A model (plus optional other parameters: system prompts, model params, agent harnesses) to evaluate |
| **run** | What happened when a specific config executed a specific task |
| **runner** | The script that executes a run |
| **grader** | Produces a grade for runs against the defined checks |
| **checks / checkers** | Simple operations (string matching, XML validation) or custom scripts — including using other models to judge runs |

The separation of **runs from grading** is a core design choice: collect runs first, grade later, and explore results via the web server or static report.

Source: [[raw/articles/simonwillison.net--2026-jul-31-smevals--e6e7fe34.md]]

## Related Pages

- [[concepts/ai-benchmarks]] — individual benchmark pages
- [[entities/simon-willison]] — smevals author
- [[concepts/evaluation/llm-evaluation-harness]] — lm-eval-harness
- [[concepts/evaluation/ai-evaluation]] — evaluation methodology
