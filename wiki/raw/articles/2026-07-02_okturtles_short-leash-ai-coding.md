---
title: "The Short Leash AI Coding Method For Beating Fable"
url: "https://blog.okturtles.org/2026/07/short-leash-ai-method/"
date: 2026-07-02
date_ingested: 2026-07-05
source: "okturtles"
type: article
authors: ["Greg Slepak", "taoeffect", "okTurtles team"]
tags: [article, raw, ai-coding, coding-agents, human-in-the-loop, code-quality]
---

# The Short Leash AI Coding Method For Beating Fable

Source: https://blog.okturtles.org/2026/07/short-leash-ai-method/

## Problems Identified

- AI agents go "off the rails" during sessions
- "Vibe engineering" (12 parallel agents, no human oversight) produces slop
- Even Fable 5 produces inefficient, ugly code in niche areas without training data

## The Short Leash Method (12 Principles)

1. **Planning phase**: Research the task, formulate a plan, use a tasks tracker to break into steps
2. **Never use YOLO mode** (no "dangerously skip permissions")
3. **AI never works while you're away** (no "play video games while it codes")
4. **Use a coding agent that shows diffs** via permissions prompts
5. **Actually analyze proposed changes**: Sit there and review every diff
6. **Keep yourself in the loop** at all times (opposite of YouTuber trends)
7. **Use diff permissions as a leash**: Keeps your understanding current, keeps AI constrained
8. **DENY permissions** any time AI is about to do something unwanted
9. **Intervene frequently** to prevent derailment
10. **AI is always "kept on a short leash"**
11. **Commit after every subtask**: Protects against AI deleting previous work
12. **Review phase**: Both human and AI review

## AI Review Protocol

- Every PR reviewed by both human AND AI (better than either alone)
- AI acts as a "linter" catching common mistakes; human catches high-level issues
- PR description must include **AI Disclosure** heading listing exact models used
- The PR author **must review their own AI-assisted PR** line-by-line before submission
