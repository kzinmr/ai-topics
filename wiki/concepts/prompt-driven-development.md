---
title: "Prompt-Driven Development"
type: concept
created: 2026-04-25
updated: 2026-11-19
tags:
  - concept
  - agentic-engineering
  - methodology
  - prompting
  - ai-coding
aliases:
  - prompt-driven-development
  - prompt-driven design
sources:
  - https://simonwillison.net/guides/agentic-engineering-patterns/#prompt-driven-development
  - raw/articles/2026-01-14_openai-codex-prompting-guide.md
related:
  - "[[concepts/harness-engineering/agentic-workflows/prompt-driven-development]]"
  - "[[concepts/spec-driven-development]]"
status: active
---

# Prompt-Driven Development

**Prompt-Driven Development (PDD)** is a software methodology in which the *prompt* — not the code — is the primary artifact the developer authors and iterates on. The developer writes a detailed prompt describing intent, constraints, and acceptance criteria; a coding agent implements it; the developer reviews the diff and feeds corrections back. Prompts accumulate into reusable assets (guides, `AGENTS.md` rules, prompt libraries) that encode team knowledge in a form agents can execute.

> Note: a detailed workflow-level treatment lives at [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]] (Simon Willison's pattern, 5 key steps). This top-level page positions PDD among neighboring methodologies and captures its durable ideas.

## The Workflow

1. **Express intent** — describe what/why, constraints, examples, and definition of done in natural language.
2. **Agent implements** — the harness runs the agent loop ([[concepts/how-coding-agents-work]]).
3. **Review as code review** — inspect the diff, run tests; do not accept unverifiable output.
4. **Feed back** — corrections go back as *more prompt context*, ideally promoted into durable instructions rather than one-off chatter.
5. **Harvest prompts** — successful prompts become templates, skills, or `AGENTS.md` rules; this is the compounding asset.

## Why It Works

- Prompts are the only interface where **domain intent survives** translation to implementation; specs and code drift, but a well-tended prompt corpus keeps re-expressing the intent to each new agent run.
- It matches how frontier models are trained: instruction-following quality improves faster than any compensation trick, so expressing intent directly exploits the model's best-trained skill ([[concepts/rich-suttons-bitter-lesson]], [[concepts/just-large-models]]).
- Iteration on prompts is *cheap and inspectable* — unlike fine-tuning, the "training data" is versionable text under review.

## Positioning Among Neighboring Methodologies

| Methodology | Primary artifact | Human role | Typical tooling |
|-------------|-----------------|-----------|-----------------|
| Vibe coding | Conversation momentum | Direct, low oversight | Chat with agent |
| **Prompt-driven development** | **The prompt / prompt corpus** | **Author + reviewer of prompts & diffs** | Agents + reusable prompts |
| Spec-driven development | Formal spec (often EARS/Gherkin) | Spec author; agent derives code & tests from spec | [[concepts/spec-driven-development]] (Kiro-style) |
| Harness engineering | The harness itself | Build tools/loops/feedback around agents | [[concepts/harness-engineering]] |

PDD vs. vibe coding: PDD keeps **review discipline and prompt craftsmanship**; vibe coding removes them. PDD vs. spec-driven development: specs are heavier, more formal artifacts; PDD treats prose prompts + accumulated guidance as sufficient and lets formality scale with risk.

## Anti-Patterns

- **Prompt sprawl**: thousands of one-off prompts, nothing promoted to durable instructions — knowledge leaks.
- **Unreviewed acceptance**: skipping diff review turns PDD into vibe coding with extra steps (ai generated code risks).
- **Prompt-as-code-substitute**: writing million-word prompts to micromanage implementation instead of stating intent + letting the model choose mechanics.
- **No verification hooks**: prompts that never say "run the tests" leave the loop open ([[concepts/harness-engineering/agentic-workflows/first-run-the-tests]]).

## Related

- [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]] — Willison's 5-step operational version
- [[concepts/prompt-engineering]] — techniques for writing effective prompts
- [[concepts/agents-md-evaluation]] — evaluating durable instruction files
- [[concepts/vibe-coding]] / [[concepts/vibe-coding-vs-agentic-engineering]] — the contrast cases
- [[concepts/harness-engineering/system-architecture/context-engineering]] — the discipline of assembling everything the model sees

## Sources

- Simon Willison, "Prompt Driven Development" — Agentic Engineering Patterns, https://simonwillison.net/guides/agentic-engineering-patterns/#prompt-driven-development
- OpenAI Codex prompting guide — `raw/articles/2026-01-14_openai-codex-prompting-guide.md`
