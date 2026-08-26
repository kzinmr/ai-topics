---
title: "AGENTS.md Code-Quality Conventions (Sanglard)"
type: concept
created: 2026-08-25
updated: 2026-08-25
tags:
  - coding-agents
  - code-quality
  - developer-tooling
  - prompt-injection
  - methodology
  - case-study
sources:
  - raw/articles/2026-08-25_fabiensanglard_my-agent-md-to-improve-llm-assisted-code-quality.md
---

# AGENTS.md Code-Quality Conventions (Sanglard)

Fabien Sanglard's public `agent.md` (published 2026-08-21; HN 405 pts, Aug 25) — a curated set of code-quality rules written *for* LLM agents, placed in the repo root so that the coding harness loads it at session start and injects it into the prompt (he writes `agent.md`; `claude.md`/`gemini.md` can be symlinked to it). The thesis: most "AI code smell" is not a model-capability problem but a **conventions-problem** — the model defaults to verbose, over-commented, over-abstracted code unless you explicitly tell it not to.

## The rules (from the actual file)

Sanglard's `AGENT.MD` has ~13 style rules + 7 commit-message rules + 1 TDD rule:

**Style**
1. **Minimal human-facing text.** Comments/commit messages/replies use as few words as possible; "less is more."
2. **No superlatives or praise.** "Stop telling me I am absolutely right. Give me the cold hard truth."
3. **No magic numbers/strings.** Extract recurring or spec-derived values into constants or enums; keep self-explanatory one-offs inline.
4. **Reduce indentation; avoid the Arrow Anti-pattern.** Leverage early return and continue.
5. **Short function names.** Under 30 chars. (HN example of what this prevents: `draw_image_with_html_image_element_and_sw_and_sh_and_dx_and_dy_and_dw_and_dh`.)
6. **Enums over booleans** for function parameters.
7. **Whitespace between logical blocks** - let the reader breathe.
8. **Comments explain what+why**, with examples; ASCII drawings for whole systems.
9. **Visibility changes require approval.** Keep fields/functions private; ask before widening access.
10. **Abstraction layers.** Raw I/O/sockets/hardware sit in a dedicated driver layer; upper layers use domain concepts.
11. **Minimal diffs.** Don't touch unrelated blocks; minimize changed lines.
12. **Strict layering.** Each layer talks only to its immediate neighbor below; never punch holes.
13. **Braces always**, even for one-line if blocks.

**Commit messages** - 7 rules: blank line between subject/body; subject 50 chars max (72 hard cap); capitalize first letter; no trailing period; imperative mood ("Fix bug" not "Fixed"); wrap body at 72 cols; body explains what+why, not how.

**TDD rule**: when the prompt indicates a bug fix, first write the test, watch it fail, then write the fix, watch it pass.

## Why it works (the mechanism, per the post + HN)

- **The harness loads `agent.md` at session start** and injects it into the prompt - the cheapest universal place for persistent style constraints. Sanglard notes `gemini.md`/`claude.md` can be symlinked to a shared `agent.md`.
- **Positive phrasing > negative phrasing** (the most-cited HN lesson). Telling the model what to do biases sampling toward it; "don't do X" still puts X in context.
- **Specificity beats generality.** "Function names under 30 chars" is checkable; "reasonable names" is not.
- **Context-dilution mitigation**: Lost-in-the-Middle effects degrade mid-context instructions. His two countermeasures: (1) new session per feature (short context), (2) explicitly ask the harness to **reload `agent.md`** when quality drops.
- **Agent-maintained rules**: he asks the agent to update `agent.md` itself with new rules, instead of hand-editing.
- **Explicit caveat**: "not a magic bullet... I still have to verify and iterate a lot, but now I usually focus on architecture and design instead of code style."

## HN community response (2026-08-25)

- **Pro**: "The most powerful change I've run into is positive phrasing." Multiple users reported that a 2-line `AGENTS.md` with "Always use ASD-STE100 Simplified Technical English" eliminated 90% of verbose comments.
- **Con**: "A bunch of these should be enforced with linting, so that humans who still hand-craft code get the same feedback." (The counter-argument: linting catches *what*, `AGENTS.md` shapes *how* — style, naming, abstraction level — which linting can't easily encode.)
- **Meta**: "This is just a code-of-conduct for the model." The file is effectively a lightweight, machine-readable style guide.

## Relationship to existing pages

- This is a **practical instantiation** of [[concepts/coding-agents/ai-code-quality]] — that page discusses the problem; this page is one specific, public, working solution.
- It sits adjacent to [[concepts/agents-md-evaluation]] (the empirical question: do context files actually help coding agents?) — Sanglard's file is a strong "yes, at least for code quality" data point.
- It is **not** the same as `AGENTS.md` for *architecture* (system design, module boundaries) — this file is specifically about *code style and quality*.

## Open questions

- Does the effect decay? (Does the model "forget" the rules after 50 edits in a long session?)
- Is there a measurable cost? (Tokens spent on the `AGENTS.md` context vs. the value of the code-quality improvement.)
- How does this interact with model-specific defaults? (Does Claude Code already do most of this? Does Codex need more explicit rules?)

## Related Pages

- [[concepts/coding-agents/ai-code-quality]] — the problem this file addresses
- [[concepts/agents-md-evaluation]] — empirical evidence on context files
- [[concepts/coding-agents/coding-agents]] — coding agent overview
- [[concepts/prompt-injection]] — `AGENTS.md` is also a (benign) prompt-injection vector if the repo is untrusted
- [[concepts/harness-engineering]] — the harness layer that reads `AGENTS.md`
