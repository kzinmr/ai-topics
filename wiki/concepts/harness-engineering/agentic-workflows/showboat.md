---
title: "Showboat"
type: concept
aliases:
  - showboat
  - agent-documentation-tool
created: 2026-04-12
updated: 2026-05-27
tags:
  - tool
  - agentic-engineering
  - developer-tooling
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/"
---

# Showboat

A documentation/output generation tool developed by Simon Willison to **make coding agents "show their work"**.

## Purpose

> "Forces agents to 'show their work' by creating verifiable, auditable testing artifacts."

Records the agent's reasoning, testing, and implementation process as verifiable Markdown documentation.

## Key Commands

| Command | Description |
|---------|------------|
| `showboat note` | Record observations in Markdown |
| `showboat exec` | **Most important.** Records the executed command and its output — prevents hallucination |
| `showboat image` | Capture screenshots (used with Rodney for UI verification) |

### Importance of `showboat exec`
> "Records the exact command run + its output. Prevents hallucination by proving what actually happened."

Prevents agents from falsely reporting what they executed by embedding actual output in the documentation, making it verifiable after the fact.

## CLI Design Philosophy

> "Design CLIs for agents. Structure `--help` outputs to be self-documenting for LLMs."

Showboat's `--help` output is structured so that LLMs can immediately understand and use the tool. This is a typical example of **agent-first CLI design**.

## Usage Examples

### Linear Walkthrough
```
Read the source and then plan a linear walkthrough of the code that explains how it all works in detail.
Then run "uvx showboat --help" to learn showboat - use showboat to create a walkthrough.md file in the repo
and build the walkthrough in there, using showboat note for commentary and showboat exec plus sed or grep
or cat or whatever you need to include snippets of code you are talking about.
```

→ With this prompt, Claude Code automatically generates detailed documentation explaining six Swift files.

### API Documentation
```
Run `uvx showboat --help` and then create a `notes/api-demo.md` showboat document and use it to test and document that new API.
```

## Related Tools

- [[concepts/harness-engineering/agentic-workflows/rodney]] — Browser automation CLI (works with Showboat for screenshots)
- [swiftui-slides](https://github.com/simonw/swiftui-slides) — SwiftUI slide app (code explanation generated with Showboat)

## Related Concepts

- [[concepts/agentic-manual-testing]] — Primary use case for Showboat
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — Code explanation generation pattern
- [[concepts/harness-engineering/agentic-engineering]] — Higher-level concept

## References
- [[entities/simon-willison]] — Developer
