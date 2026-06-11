---
title: Codex Prompting
type: concept
created: 2026-05-12
updated: 2026-05-26
tags:
  - prompting
  - coding-agents
  - harness-engineering
  - metaprompting
  - openai
sources:
  - raw/articles/2026-01-14_openai-codex-prompting-guide.md
  - https://github.com/openai/codex
---

# Codex Prompting

Prompt design patterns and best practices for OpenAI [[entities/openai-codex]] (gpt-5.3-codex), based on the OpenAI Cookbook's "Codex Prompting Guide."

## Core Principles

### 1. Bias for Action

The most important principle in Codex prompt design. Instructions that make the model explicitly output plans or request user confirmation significantly degrade performance.

- ❌ **Anti-pattern**: "First make a plan, then execute it"
- ❌ **Anti-pattern**: "Get user confirmation before each step"
- ✅ **Recommended**: "Do not stop until the task is complete or you hit a blocker"

Reason: Explicit plan output causes early stopping in the model. The model plans internally, so making it write out the plan is unnecessary.

### 2. Concise, Direct Instructions

Eliminate "assistant speak" and provide only the minimum necessary context.

- ❌ **Anti-pattern**: Verbose role descriptions and personality settings
- ❌ **Anti-pattern**: "You are a kind, intelligent, and diligent AI assistant..."
- ✅ **Recommended**: Only specific action instructions and constraints

### 3. Concrete Examples

When expecting specific behavior, concrete examples (few-shot) are more effective than abstract instructions. However, for general coding tasks and standard formats, they are not always necessary.

### 4. Systematic Testing

Always test prompt changes with Eval (evaluation tasks). Use both pass/fail evaluation and preference-based evaluation.

## Standard System Prompt Structure

The standard Codex CLI prompt consists of the following sections:

```
# General — Basic policy for tool selection
# Autonomy and Persistence — Autonomy and persistence
# Codebase Exploration — Codebase exploration strategy
# Tool Use — Tool use best practices
# Frontend Quality — UI quality standards
# Coding Standards — Coding conventions
# Communication — Communication style
```

Key snippets from each section:

| Section | Most Important Snippet |
|-----------|----------------|
| General | "When searching for text or files, prefer using grep/rg/locate over find/ls" |
| Autonomy | "Never wait for user confirmation unless you encounter an error you cannot resolve" |
| Exploration | "Read relevant files fully before editing them" |
| Tool Use | "Parallelize independent tool calls" / "Use patch for targeted edits" |
| Frontend | "Make UIs functional — buttons and forms should work" |
| Communication | "Write concise responses without preambles. Don't list out what you're about to do — just do it" |

## Anti-Patterns (Instructions to Remove)

| Anti-Pattern | Problem | Fix |
|-------------|------|------|
| Explicit request for plans | Triggers early stopping | Rely on internal planning |
| Request for confirmation | Unnecessary interaction increase | Confirm only on errors |
| Verbose role descriptions | Token waste, instruction dilution | Minimal, concise instructions |
| Contradictory instructions | Combining "be thorough" with "be concise" | Provide concrete definitions for each concept |

## Metaprompting (Self-Improving Prompts)

A powerful feature of Codex: having the model itself improve its prompt through "metaprompting."

### Basic Metaprompt

```
<instructions>
Analyze the saved conversation and identify improvements in the assistant's behavior patterns.
Propose specific changes to the system prompt.

## Pattern Analysis
- What went well
- Mistakes or missed opportunities
- Recurring issues across multiple turns
- Places where instructions were not followed

## Change Proposals (per proposal)
1. Exact text to add/modify/remove
2. Justification for the change
3. Expected improved behavior after the change

## Rules
- Propose generalizable changes, not specific to this conversation
- Prioritize changes with significant impact on task completion
- State downsides if any
</instructions>
```

### Effective Use of Metaprompting

1. **Iterative execution**: Run the metaprompt multiple times on the same conversation and adopt suggestions that appear consistently (a single run risks overfitting to conversation-specific details)

2. **Validation with Eval**: Always measure the effect of improvements obtained from metaprompting with Eval. Some changes that look like improvements may actually degrade performance

3. **Purpose-specific metaprompts**:
   - **Overthinking mitigation**: "Suggest instruction changes that reduce time to first tool call"
   - **Verbose preamble mitigation**: "Rewrite the user update instructions to match preference constraints"

4. **Proactive prompt generation**: After successfully completing a task with minimal prompting, ask "Based on this success pattern, write a better system prompt"

## Tool Design and Prompt Interaction

The effectiveness of prompts depends heavily on tool implementation:

- **apply_patch**: With fuzzy matching implementation, the model can edit without worrying about exact string matches. Prompt accordingly: "Use patch for targeted edits rather than rewriting entire files"
- **Terminal parallelization**: When background execution + completion notification mechanisms exist, "Parallelize independent terminal calls" becomes effective
- **Browser tools**: Prompt the model to use them for visual verification of UI work

## Related Topics

- [[entities/openai-codex]] — OpenAI Codex agent
- [[concepts/metaprompting]] — Metaprompting
- [[concepts/harness-engineering/agent-harness]] — Agent harness design
- [[concepts/prompt-engineering]] — General prompt engineering
- [[concepts/coding-agents/coding-agents]] — Coding agent comparison
