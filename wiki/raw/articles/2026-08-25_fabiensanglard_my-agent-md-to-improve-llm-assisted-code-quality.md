---
title: "My agent.md to improve LLM-assisted code quality"
source: fabiensanglard.net
url: https://fabiensanglard.net/agent.md/index.html
date: 2026-08-21
date_ingested: 2026-08-25
tags: [raw, coding-agents, code-quality, developer-tooling, methodology]
type: article
in: "HN front page 2026-08-25 (405 pts)"
---

# My agent.md to improve LLM-assisted code quality

**Author:** Fabien Sanglard (fabiensanglard.net)
**Published:** 2026-08-21
**Source:** https://fabiensanglard.net/agent.md/index.html
**Captured:** 2026-08-25 via active-crawl (full text scraped)

## Context

The first time the author used an LLM to speed up coding was in mid-2025 (working on `libadbmdns`, an mDNS implementation in Rust); the code produced wouldn't compile. He revisited LLMs in January 2026: the model wrote a complex indexed-binary heap class and pinpointed an obscure bug in the `polling` crate due to the Windows IOCP implementation — but the code quality was "abysmal... spaghetti code with no comments and no structure." In March 2026 he tried agentic IDEs (Antigravity, VS Code's Claude Code plugin) and found himself "reviewing the code of an infinitely patient junior CS major," repeating suggestions like "don't use magic numbers," "add a short comment," "use short function names" in every new session.

**Key insight**: when a coding session starts, the coding harness loads a file named `agent.md` and injects it into the prompt. That is the perfect location to persist coding-style preferences. When he caught himself repeating the same suggestion, he added it there. (Note: he writes `agent.md`; the broader ecosystem also uses `AGENTS.md`, `claude.md`, `gemini.md` — he says those can be symlinked toward `agent.md` to have it active anywhere.)

## FAB's AGENT.MD (the full rule set, abridged here; full text at the source URL)

### Style rules

- When writing something intended for human consumption (comment, commit message, reply to prompt), use as few words as possible. Pick every word meticulously. Be down to the point. Less is more.
- Avoid superlatives and praise. Stop telling me I am absolutely right. Give me the cold hard truth.
- Avoid magic numbers and strings by extracting recurring or meaningful values into descriptive constants or enums. Keep self-explanatory one-off values inline. If a value comes from a spec (e.g. HTTP 200 OK), use a constant regardless.
- Reduce code indentation. Avoid Arrow Anti-Pattern. Leverage early return and continue.
- Keep function names short. Less than 30 characters.
- Use enums instead of booleans for function parameters.
- Let the reader of the code breathe. Add empty lines between logical blocks of code.
- Add a small, to-the-point comment to explain *what* the block does and *why*. Use examples when possible. Propose ASCII drawings to explain complete systems.
- Treat member visibility changes as a breaking design shift. Keep all fields and functions private unless external access is strictly required. Prompt the user for explicit approval before changing any access modifier from private to internal or public.
- Program to levels of abstraction. Lower-level mechanics (raw hardware I/O, sector parsing, direct socket streams) must be encapsulated in a dedicated driver/abstraction layer. Expose clean, high-level APIs so calling code works with domain concepts, not raw implementation details.
- Don't touch blocks of code unrelated to the feature you implement. Minimize the number of changed lines.
- Strictly adhere to the layered boundary hierarchy: each layer may only communicate with its immediate neighbor directly below it. Never "punch holes" through layers.
- Always use `{}`, even on a one-line "if" statement.

### Commit message rules (7 rules)

1. Separate the subject line from the body with a single blank line.
2. Limit the subject line to 50 characters (72 absolute hard limit).
3. Capitalize the first letter of the subject line.
4. Do not end the subject line with a period.
5. Use the imperative mood in the subject line ("Fix bug," not "Fixed"). Test: "If applied, this commit will [subject]."
6. Wrap the body text manually at 72 characters.
7. Use the body to explain *what* and *why*, not *how* (the code explains the how).

### Bug-fix rule

- If the prompt indicates a bug is being fixed, don't write the fix right away. First write the test. Observe it failing. Then write the fix. Observe the test passing. (i.e., enforce TDD in the agent loop.)

## Caveats and mitigations from the post

- "This is not a magic bullet that lets me avoid reading the code. LLMs constantly hallucinate and cannot be trusted. I still have to verify and iterate a lot, but now I usually focus on **architecture and design** instead of code style."
- **Context dilution** (Lost in the Middle): as context grows, models pay less attention to instructions in the middle. Mitigations found: (1) keep the context short — start a new session per feature; (2) explicitly ask the harness to **reload agent.md** when code quality drops.
- **Auto-update**: he now asks the agent itself to update `agent.md` with new rules instead of hand-editing.

## HN community discussion (2026-08-25, 405 pts)

- "A bunch of these should be enforced with linting, that way people who still hand-craft code get the same feedback."
- "Just this one line in AGENTS.md has given better results to reduce if not eliminate verbosity and grandeur: Always use ASD-STE100 Simplified Technical English."
- "The most powerful change I've run into is 'Positive phrasing' as a default: prefer to tell the model what it should do, and why, not a prohibition. When you say 'don't do x' you are just pre-seeding the model with 'x'."
- "Since we're sharing our AGENTS.md, here's my own: Convergence rule — every substantial task must end in exactly one of three states: Success / ... (truncated)"
