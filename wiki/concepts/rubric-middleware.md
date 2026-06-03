---
title: "RubricMiddleware"
type: concept
created: 2026-06-03
updated: 2026-06-03
tags:
  - ai-agents
  - agent-evaluation
  - coding-agents
  - self-improving
  - middleware
  - langchain
  - deep-agents
  - llm-as-judge
aliases:
  - rubric-middleware
  - Rubric Middleware
  - agent rubrics
sources:
  - raw/articles/2026-06-02_langchain_rubric-middleware.md
  - https://x.com/i/article/2061868304654864384
  - https://docs.langchain.com/oss/python/deepagents/rubric
related:
  - concepts/deep-agents
  - concepts/agent-evaluation
  - entities/langchain
  - concepts/llm-as-judge
---

# RubricMiddleware

> **RubricMiddleware** is a LangChain [[concepts/deep-agents|Deep Agents]] middleware component that adds a self-correcting grader loop: define a rubric, and the agent self-evaluates and iterates until it satisfies every criterion or hits a configured cap. Introduced June 2026 by Seshadri (@sseshadri43) and Sydney Runkle (@sydneyrunkle).

## Core Idea

Agents often produce outputs that head in the right direction but don't fully land on the first attempt. RubricMiddleware automates the "inspect → correct → re-run" cycle that developers currently do manually:

```
Agent Run → Grader Review (per-criterion) → Pass? → Done
                                    ↓ Fail
                              Feedback injected → Agent runs again
```

If you're familiar with `/goal` in Claude Code or Codex, this is a similar pattern but more flexible — evaluation is handled by a **dedicated grader sub-agent** that can call tools, reason over the full transcript, and return per-criterion feedback.

## Architecture

### The Grader Sub-Agent

A separate LLM (often smaller/cheaper than the main agent model) reviews the agent's output against a rubric. Unlike generic self-reflection, the grader:

1. **Evaluates per criterion** — each rubric item gets its own verdict (pass/fail with specific reason)
2. **Can call tools** — gather hard evidence (run tests, lint, validate outputs) before producing a verdict
3. **Produces targeted feedback** — the agent knows exactly what to fix, not a generic "try again"
4. **Falls back to transcript reasoning** — when no tools are provided, the grader reasons from the conversation

### Loop Termination States

| State | Meaning |
|-------|---------|
| `satisfied` | All rubric criteria passed |
| `max_iterations_reached` | Hit the configured iteration cap |
| `failed` | Grader determined the task cannot be satisfied |
| `grader_error` | Grader itself encountered an error |

## Configuration

```python
from deepagents import RubricMiddleware

rubric_middleware = RubricMiddleware(
    model="anthropic:claude-haiku-4-5",     # grader model (cheaper/smaller)
    system_prompt="You are a code reviewer grading generated code against a rubric.",
    tools=[run_test_suite],                   # tools the grader can call
    max_iterations=5,                         # max fix → re-grade loops
)
```

Attach to a deep agent:

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="You are a careful Python engineer...",
    middleware=[rubric_middleware],
)
```

Invoke with a rubric passed at runtime:

```python
result = agent.invoke(
    {
        "messages": [HumanMessage(content="...")],
        "rubric": (
            "- All tests pass in run_test_suite\n"
            "- The function is named `find_duplicates` and accepts a single list argument\n"
        ),
    },
    config={"configurable": {"thread_id": "code-generation-session"}},
)
```

The rubric string is a **newline-delimited checklist**. If absent, the middleware does nothing — the agent runs normally.

## Design Decisions

### Cheaper Grader Model

The grader uses a smaller model (e.g., Claude Haiku 4.5) — grading is easier than generating. This keeps the self-correction loop cost-efficient.

### Tool-Equipped Grader

Rather than asking the grader to reason abstractly about correctness, it can call tools like `run_test_suite` to verify behavior directly. This gives the grader **hard evidence** rather than relying on guesswork.

### Per-Criterion Feedback

Unlike generic retry loops that say "try again," each rubric criterion gets its own verdict. The agent receives targeted feedback:
> "One test fails: test_unhashable. The function crashes with TypeError..."

## Example: Code Generation with Tests

In the LangChain example, the agent was asked to write a `find_duplicates(lst)` function. The rubric required all tests to pass.

- **First attempt**: Looked correct but failed `test_unhashable` (crashed with TypeError on lists within the input list)
- **Second attempt**: Revised implementation, passed all tests

The agent knew exactly which test failed and why — it didn't need to guess.

## Why It Matters

Agent outputs are **probabilistic**: the same prompt can succeed on one run and fall short on the next. RubricMiddleware shifts the burden of catching variance from the developer to the system.

| Before | After |
|--------|-------|
| Developer manually inspects outputs | Define "done" once, loop handles the rest |
| Re-run failed tasks blindly | Each retry is informed by per-criterion feedback |
| Compound errors as context grows | Grader catches errors before they snowball |

## Comparison with Related Patterns

| Pattern | RubricMiddleware | `/goal` (Claude Code/Codex) | Generic Self-Reflection |
|---------|-----------------|---------------------------|------------------------|
| Evaluator | Dedicated grader sub-agent | Same model self-evaluates | Same model reflects |
| Tool access | Yes (grader can call tools) | Varies | No |
| Feedback granularity | Per-criterion | Binary (pass/fail) | Free-form |
| Model for grading | Separate (cheaper) model | Same model | Same model |
| Iteration | Automatic loop | Usually manual re-prompt | Varies |

## Status

RubricMiddleware is in **beta** (June 2026) and the API may change.

## Related Concepts

- [[concepts/deep-agents]] — LangChain's autonomous agent framework that RubricMiddleware extends
- [[concepts/agent-evaluation]] — Broader evaluation patterns for AI agents
- [[concepts/llm-as-judge]] — LLM-as-judge: the evaluation paradigm RubricMiddleware formalizes into middleware
- [[entities/langchain]] — The company behind Deep Agents and RubricMiddleware

## Sources

- [Introducing Rubrics: Build Agents that Evaluate and Correct Their Work](https://x.com/i/article/2061868304654864384) — X Article by Seshadri & Sydney Runkle (Jun 2, 2026)
- [RubricMiddleware Documentation](https://docs.langchain.com/oss/python/deepagents/rubric)
- Raw article: `raw/articles/2026-06-02_langchain_rubric-middleware.md`
