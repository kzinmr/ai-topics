---
title: "Linear Walkthroughs"
type: concept
aliases:
  - linear-walkthroughs
  - code-walkthrough
created: 2026-04-12
updated: 2026-05-27
tags:
  - concept
  - agentic-engineering
  - code-intelligence
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/"
---

# Linear Walkthroughs

A pattern for having a coding agent **generate structured explanations of a codebase**. Useful for understanding existing code, reviewing code you've half-forgotten, and understanding how Vibe Coded code works.

## Definition

> "Sometimes it's useful to have a coding agent give you a structured walkthrough of a codebase. Maybe it's existing code you need to get up to speed on, maybe it's your own code that you've forgotten the details of, or maybe you vibe coded the whole thing and need to understand how it actually works."

## How It Works

A frontier model plus an appropriate agentic harness can construct detailed code explanations.

## Practical Example: SwiftUI Presentation App

Simon needed to understand his own code after Vibe Coding a macOS SwiftUI slide presentation app with Claude Code + Opus 4.6.

### Prompt
```
Read the source and then plan a linear walkthrough of the code that explains how it all works in detail.
Then run "uvx showboat --help" to learn showboat - use showboat to create a walkthrough.md file in the repo
and build the walkthrough in there, using showboat note for commentary and showboat exec plus sed or grep
or cat or whatever you need to include snippets of code you are talking about.
```

### Key Techniques
- **Use `showboat exec` + `sed/grep/cat`** → Eliminates the risk of the agent manually copying code snippets (hallucination errors)
- **Record with Showboat** → Remains as a verifiable, auditable artifact

### Results
> "I learned a great deal about how SwiftUI apps are structured and absorbed some solid details about the Swift language itself just from reading this document."

Detailed documentation for 6 Swift files was automatically generated.

## Paying Down Cognitive Debt

> "If you are concerned that LLMs might reduce the speed at which you learn new skills I strongly recommend adopting patterns like this one. Even a ~40 minute vibe coded toy project can become an opportunity to explore new ecosystems and pick up some interesting new tricks."

Vibe Coding → Linear Walkthrough can be **transformed into a learning opportunity**.

## Related Concepts

- [[concepts/showboat]] — Documentation tool used for generating walkthroughs
- [[concepts/interactive-explanations]] — More intuitive understanding methods (animations)
- [[concepts/vibe-coding]] — The main scenario where walkthroughs become necessary
- [[concepts/harness-engineering/agentic-engineering]] — Higher-level concept

## References
- [[entities/simon-willison]] — Pattern originator
