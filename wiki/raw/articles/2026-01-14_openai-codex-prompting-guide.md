---
title: "Codex Prompting Guide"
source: "OpenAI Cookbook"
url: "https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide"
date_published: 2026-01-14
date_updated: 2026-03-05
model_family: "GPT-5 Codex (gpt-5.3-codex)"
tags: ["codex", "prompt-engineering", "openai", "coding-agent", "gpt-5", "metaprompting", "agent-harness"]
---

# **Codex** Prompting Guide

Codex models advance the frontier of intelligence and efficiency and our recommended agentic coding model. Follow this guide closely to ensure you're getting the best performance possible from this model. This guide is for anyone using the model directly via the API for maximum customizability; we also have the [Codex SDK](https://developers.openai.com/codex/sdk/) for simpler integrations.

In the API, the Codex-tuned model is `gpt-5.3-codex` (see the [model page](https://platform.openai.com/docs/models#codex)).

## Recent improvements to Codex models

- **Faster and more token efficient**: Uses fewer thinking tokens to accomplish a task. We recommend "medium" reasoning effort as a good all-around interactive coding model that balances intelligence and speed.
- **Higher intelligence and long-running autonomy**: Codex is very capable and will work autonomously for hours to complete your hardest tasks. You can use high or xhigh reasoning effort for your hardest tasks.
- **First-class compaction support**: Compaction enables multi-hour reasoning without hitting context limits and longer continuous user conversations without needing to start new chat sessions.
- Codex is also much better in PowerShell and Windows environments.

## Getting Started

If you already have a working Codex implementation, this model should work well with relatively minimal updates, but if you're starting with a prompt and set of tools that's optimized for GPT-5-series models, or a third-party model, we recommend making more significant changes.

The best reference implementation is our fully open-source [codex-cli](https://github.com/openai/codex) agent, available on GitHub. Clone this repo and use Codex (or any coding agent) to ask questions about how things are implemented. From working with customers, we've also learned how to customize agent harnesses beyond this particular implementation.

**Key steps to migrate your harness to codex-cli:**

1. **Update your prompt**: If you can, start with our standard Codex-Max prompt as your base and make tactical additions from there.
   - a) The most critical snippets are those covering autonomy and persistence, codebase exploration, tool use, and frontend quality.
   - b) You should also remove all prompting for the model to communicate an upfront plan, preambles, or other status updates during the rollout, as this can cause the model to stop abruptly before the rollout is complete.

2. **Update your tools**, including our apply_patch implementation and other best practices below. This is a major lever for getting the most performance.

## Prompting

### Recommended Starter Prompt

This prompt began as the default GPT-5.1-Codex-Max prompt and was further optimized against internal evals for answer correctness, completeness, quality, correct tool usage and parallelism, and bias for action. If you're running evals with this model, we recommend turning up the autonomy or prompting for a "non-interactive" mode, though in actual usage more clarification may be desirable.

The standard Codex system prompt includes the following structure:

```
You are Codex, based on GPT-5. You are running as a coding agent in the Codex CLI on a user's computer.

# General
- When searching for text or files, prefer using grep/rg/locate over find/ls
- Use the terminal for file operations, git, builds, and package management
- Use read/write/patch tools for file I/O
- Be thorough but terse where possible
- If you make a plan, write it to a Markdown file

# Autonomy and Persistence
- You are allowed to run long sequences of operations without asking for permission
- Never wait for user confirmation unless you encounter an error you cannot resolve
- Don't stop until you have completed the task or hit a blocker
- If you encounter a bug, try multiple approaches to fix it before asking

# Codebase Exploration
- When working in a new codebase, start by understanding the structure
- Use tree, ls, and grep to explore before making changes
- Read relevant files fully before editing them
- Understand the project's build system, linting, and testing conventions

# Tool Use
- Use the right tool for each job
- Parallelize independent tool calls
- Use patch for targeted edits rather than rewriting entire files
- Use terminal for build/test/format/lint commands
- Use browser/Bing search tools for documentation lookup

# Frontend Quality
- When building UIs, aim for polished, complete designs
- Test across multiple breakpoints
- Make UIs functional (not just visually polished — buttons and forms should work)
- Use the browser tool to visually verify your work

# Coding Standards
- Follow existing code style and conventions in the project
- Use language idioms, not just syntactically correct code
- Write tests when appropriate
- Handle edge cases and errors

# Communication
- Write concise responses without preambles
- Don't list out what you're about to do — just do it
- Use markdown formatting in messages to the user
```

### Guiding Principles for Writing Codex Prompts

- **Be concise and straightforward**: Give the model permission to be concise and avoid "assistant speak". Give the model the exact context it needs. It's easy to lose performance by adding many specific behavioral instructions, especially if they are contradictory or overly complex.
- **Use concrete examples**: If you want the model to think or behave in a particular way, provide examples that illustrate the desired patterns. However, also note that examples are not always required for common coding tasks or formats, use your discretion only when you've observed the model not having the right context.
- **Test changes systematically**: Run your prompts against evaluation tasks to determine whether improvements are real. Use both pass/fail and preference-based evaluation.
- **Use metaprompting to self-improve**: GPT-5 models are very good at self-improvement. Use metaprompting: ask the model to analyze its own behavior and suggest prompt improvements. See the metaprompting section below.

### Anti-patterns to Remove

Things that harm Codex performance:

- **Prompting for an explicit plan**: The model will still plan, but asking it to write out or say what the plan is often causes it to stop early or be less effective.
- **Asking for confirmation**: If you let the model ask before doing things, it will often ask the user before taking useful actions. Discourage this.
- **Verbose role descriptions**: Don't use flowery language describing the model's personality. Simple, clear instructions work best.
- **Contradictory instructions**: Avoid saying both "be thorough" and "be concise" unless you define specifically what thoroughness means vs. verbosity.

## Tools

### Key Tools and Best Practices

The article provides detailed tool implementation guidance including:

- **apply_patch**: A critical tool for editing files. The implementation should use fuzzy matching heuristics and allow the model to specify the exact old string to replace. Open-source reference: `apply_patch.py` in the codex-cli repo.
- **Terminal tool**: Should support background execution with notification for long-running commands. The model should be prompted to parallelize terminal calls when possible.
- **File read/write/patch**: Direct file I/O tools that are faster than terminal commands.
- **Browser tool**: For documentation lookup and visual verification of UI work.
- **Search tools**: grep/rg for content search, locate/find for file search.

## Metaprompting

The article includes a metaprompting section with this recommended prompt:

```
# Evaluating and Improving System Prompts

<instructions>
Analyze this preserved conversation. Identify patterns in the assistant's behavior that could be improved. Then, propose specific, concrete changes to the system prompt.

## Pattern Analysis
- What did the assistant do well?
- Where did the assistant make mistakes or miss opportunities?
- Are there recurring issues across multiple turns?
- Did the assistant follow all instructions correctly?

## Proposed Changes
For each proposed change:
1. The exact text to add, modify, or remove from the system prompt
2. A brief justification for why this change would help
3. An example of the improved behavior you expect

## Rules
- Propose changes that are generalizable, not specific to this one conversation
- Prioritize changes that would have the biggest impact on task completion
- Be specific about what to change and where in the prompt
- If a change might have downsides, note them
</instructions>
```

The article recommends:
- Running the metaprompt on past conversations to iterate on prompt design
- Testing prompt changes with evals before deploying
- Asking the model to generate the prompt proactively after seeing a few examples
- Running metaprompting a few times and looking for common elements across generated improvements

### Metaprompting Examples from the Article

| Problem | Suggested Metaprompt |
|---------|---------------------|
| Overthinking / slow starts | Ask it to propose instruction changes that reduce time-to-first-tool-call |
| Overly wordy preambles | Ask it to rewrite user-updates instructions to satisfy your preference constraints |

## Write Your Own Prompt (Self-Writing Prompts)

Codex is capable of writing its own prompt after seeing examples of successful interactions. The article suggests:
1. Give Codex a task with a minimal prompt
2. After success, ask it to write a better system prompt based on what worked
3. Iterate: use the new prompt, test, refine

This can produce prompts that are more tailored to your specific workflow than the general-purpose starter prompt.
