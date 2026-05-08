---
title: "Mozilla Firefox AI-Assisted Security Hardening"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - concept
  - security
  - ai-assisted-development
  - firefox
  - mozilla
  - claude-mythos
aliases: ["firefox ai security audit", "mozilla mythos preview hardening"]
related:
  - concepts/claude-mythos-preview
  - concepts/ai-coding-reliability
  - concepts/harness-engineering/agentic-engineering
sources:
  - raw/articles/simonwillison.net--2026-may-7-firefox-claude-mythos--7d5ece52.md
  - https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/
---

# Mozilla Firefox AI-Assisted Security Hardening

In **May 2026**, Mozilla published detailed results from their AI-assisted security hardening effort for Firefox, using access to **Claude Mythos Preview** and other frontier models. The results demonstrate a dramatic shift in AI-assisted vulnerability discovery.

## Key Metrics

| Period | Monthly Security Bugs Fixed |
|--------|----------------------------|
| 2025 average | 20-30 bugs/month |
| Jan 2026 | 25 |
| Feb 2026 | 61 |
| Mar 2026 | 76 |
| **Apr 2026** | **423** |

The **423 bugs fixed in April 2026** exceeded the entire year's total for 2025.

## The Turning Point: "Suddenly, the bugs are very good"

Mozilla reported a fundamental shift in AI-generated security bug reports:

> "Just a few months ago, AI-generated security bug reports to open source projects were mostly known for being unwanted slop. Dealing with reports that look plausibly correct but are wrong imposes an asymmetric cost on project maintainers: it's cheap and easy to prompt an LLM to find a 'problem' in code, but slow and expensive to respond to it."

> "It is difficult to overstate how much this dynamic changed for us over a few short months. This was due to a combination of two main factors. First, the models got a lot more capable. Second, we dramatically improved our techniques for **harnessing** these models — steering them, scaling them, and stacking them to generate large amounts of signal and filter out the noise."

## Notable Discoveries

The AI-assisted audit found deeply buried vulnerabilities:

1. **20-year-old XSLT bug** (Bug 2025977): Reentrant calls causing hash table rehashing while pointers were in use
2. **15-year-old `<legend>` element bug** (Bug 2024437): Recursive stack depth and cycle collection issues
3. **JIT optimization errors**: WebAssembly GC struct generating fake-object primitives
4. **RLBox escapes**: Process-in-process sandbox validation logic gaps

## Defense-in-Depth Validation

Importantly, many attempted exploits by the AI harness were **blocked by Firefox's existing defense-in-depth measures**. This validates Mozilla's security architecture while also showing where improvements are needed.

## The Harness Engineering Approach

Mozilla's success wasn't just about having a better model — it was about building better **harnesses**:

- **Steering**: Guiding the model to focus on specific code areas and vulnerability patterns
- **Scaling**: Running multiple parallel instances across different code modules
- **Stacking**: Combining multiple model passes to filter noise and amplify signal
- **Integration**: Automatic deduplication and tracking via Bugzilla
- **Model-agnostic pipeline**: Easy migration from Claude Opus 4.6 to Mythos Preview

## Industry Implications

Mozilla recommends all software projects start using AI harnesses immediately:

> "There is a bug in this part of the code, please find it and build a testcase." — Start simple, then build orchestration and tooling around the discovery and verification "inner loop."

The planned next step is transitioning from **file-based scanning to patch-based CI scanning** — integrating AI vulnerability detection directly into the development workflow.

## Connection to AI Coding Reliability

This success story contrasts with the **AI coding reliability crisis** documented elsewhere. The key difference:

- **Security auditing**: AI as a focused tool for finding bugs in existing code → high success rate
- **Code generation**: AI as a tool for writing new code → reliability concerns, outages, review bottlenecks

The distinction suggests AI is currently more reliable as an **analysis tool** than as a **generation tool** for production systems.

## Related

- [[concepts/ai-vulnerability-detection-at-scale]] — General concept: LLM-driven vulnerability detection at industrial scale
- [[concepts/claude-mythos-preview]] — The model that enabled this hardening effort
- [[concepts/ai-coding-reliability]] — Contrast: AI generation vs AI analysis reliability
- [[concepts/harness-engineering/agentic-engineering]] — The methodology behind the success

## Sources

- [Mozilla Hacks: Behind the Scenes Hardening Firefox with Claude Mythos Preview](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/) (May 2026)
- [Simon Willison: Behind the Scenes Hardening Firefox with Claude Mythos Preview](https://simonwillison.net/2026/May/7/firefox-claude-mythos/) (May 7, 2026)