---
title: "Computer Use Agents"
created: 2026-05-31
updated: 2026-11-19
type: concept
tags:
  - ai-agents
  - automation
  - benchmark
  - pointer
  - google
sources:
  - https://www.pointer.ai/blog/sota
  - https://uncensoredhub.ai/news/2026-05-29-claude-opus-4-8-orchestrates-hundreds-of-parallel-subagents-hits-84-on-browser-a
  - raw/articles/2026-11-17_openai.com_computer-use-healthcare-teams.md
---

# Computer Use Agents

**Computer use agents** are AI systems that operate computers the same way humans do — clicking, typing, navigating — to accomplish tasks across multiple applications.

## OSWorld Benchmark

OSWorld is the standard benchmark for computer use agents, spanning 360+ tasks across:
- Web browsing (Chrome)
- Coding (VS Code)
- Photo editing (GIMP)
- Document/spreadsheet work (LibreOffice)
- Media playback (VLC)
- Email (Thunderbird)
- Operating system tasks

**Human baseline: 72.4%**

## Current State of the Art (May 2026)

| System | Model | OSWorld Score | Notes |
|---|---|---|---|
| [[entities/pointer-ai|Pointer AI]] | Claude Opus 4.7 | **83.6%** | Highest verified score |
| [[entities/pointer-ai|Pointer AI]] | Claude Sonnet 4.6 | 81.5% | Second place |
| [[entities/anthropic|Anthropic]] | Claude Opus 4.8 | 84% | Online-Mind2Web (browser) |
| Previous best | — | ~78% | Before Pointer results |

## Pointer AI Architecture

- **Lightweight task controller** + 3 specialized agents
- Generator-validator loop: one subsystem makes changes, another validates by reviewing diffs
- Different models excel at different domains (Opus > Sonnet on most, Sonnet > Opus on VS Code, Impress, VLC)
- Multi-apps category: +15 point jump with Opus 4.7
- Fully open source release

## Phantom Tools Phenomenon

5% of Opus 4.7 tool calls in OSWorld were to **tools that were never provided** — ingrained "computer use primitives" from heavy reinforcement during training. The model hallucinated tools it had been trained to use.

## Dynamic Workflows Impact

[[concepts/dynamic-workflows|Dynamic Workflows]] in [[concepts/claude/opus-4-8|Claude Opus 4.8]] extends computer use to codebase-scale migrations across hundreds of thousands of lines, with parallel subagent orchestration.

## Gemini 3.5 Flash Computer Use (June 2026)

In June 2026, [[entities/google|Google]] [[entities/deepmind|DeepMind]] announced built-in computer use as a native tool in **Gemini 3.5 Flash**, delivering what Google described as its best performance yet for agentic computer use tasks. Previously available only as a standalone capability, computer use is now integrated directly into the main Gemini Flash model.

### Key Capabilities

- **Native integration**: Computer use is a built-in tool in Gemini 3.5 Flash rather than a separate model or add-on, joining other built-in tools like Search and Maps grounding.
- **Multi-environment support**: Agents built on Gemini 3.5 Flash can see, reason, and take action across browser, mobile, and desktop environments.
- **Long-horizon tasks**: Improved performance for extended automation tasks such as continuous software testing and knowledge work across professional applications.
- **Enterprise automation**: Demonstrated use cases include analyzing the Gemini app to return a categorized list of features, and auditing its own documentation for accessibility compliance.

### Safety Architecture

Google implemented several safety measures specifically for computer use agents operating in live environments:

- **Targeted adversarial training**: Gemini 3.5 Flash received specific adversarial training for computer use to mitigate prompt injection risks.
- **Enterprise safeguard systems**: Two optional systems were released — (1) requiring explicit user confirmation for sensitive or irreversible actions, and (2) automatic task termination when indirect prompt injection is detected.
- **Defense-in-depth recommendation**: Google encourages developers to combine these with secure sandboxing, [[concepts/human-in-the-loop|human-in-the-loop]] verification, and strict access controls.

### Platform Access

Developers and enterprises can access computer use in Gemini 3.5 Flash via the Gemini API and [[concepts/gemini/gemini-enterprise-agent-platform|Gemini Enterprise Agent Platform]].

See [[concepts/gemini-computer-use]] for the Android-specific implementation guide with the complete screenshot→model→function_call→ADB loop, 10 mobile actions, and ADBBridge class (Philipp Schmid, June 2026).

## OpenAI Computer-Use for Healthcare Teams (Nov 17, 2026)

OpenAI's *"Advancing computer-use agents for healthcare teams"* (HN 53 pts) reports GPT-6 Astra operating clinical and administrative workflows in real EHR/insurer software — clicking, typing, and moving between apps for prior authorizations, referrals, discharge planning, and inter-visit outreach (HN ids 50535898, 50519201).

**Evaluation (all OpenAI-reported):**
- **Clinical EHR-inbox tasks** shaped by physicians: **99% of 325 reviewed tasks rated safe** (reviewers checked whether inaccuracies/omissions could plausibly cause patient harm); physicians rated **93% of 646 helpfulness assessments** "very" or "extremely helpful."
- **HealthAdminBench** (independent Stanford benchmark for administrative workflows): **GPT-6 Astra 94.3%** of rubric points, **GPT-6 Luna 91.8%** at **98% lower cost — 8.5¢/task** — both at maximum reasoning effort. A clean model-routing data point: a near-matching cheaper model for high-volume admin work.

**Deployment partners:** CVS Health (cleared a months-long document-sending backlog over one weekend; tens of thousands of consult steps/day; open-sourcing its **Agent Kit** built on OpenAI's Agents SDK), Abridge (inpatient discharge-barrier coordination), Cigna Healthcare, and Ambience. Access via OpenAI API, ChatGPT for Healthcare, and ChatGPT for Clinicians, with HIPAA-compliant workflows, configurable approvals, and audit logs.

**Confidence caveat:** safety/helpfulness figures are OpenAI's own review methodology; the one genuinely third-party number is Stanford's HealthAdminBench. The "99% safe" rating is on a curated 325-task sample, not production-wide safety.

This is the most concrete *regulated-industry* deployment of [[concepts/computer-use]] yet, contrasting with the consumer/desktop demos above — and CVS's open-sourced CUA agent kit is an early reusable pattern for production computer-use.

## Related Pages
- [[entities/pointer-ai]] — Pointer AI, SOTA computer use agent developer
- [[concepts/dynamic-workflows]] — Dynamic Workflows for parallel subagent orchestration
- [[entities/anthropic]] — Anthropic's Claude Opus 4.8 computer use capabilities
- [[concepts/multi-agents/agent-orchestration]] — Agent orchestration patterns
- [[entities/google]] — Google, developer of Gemini models
- [[entities/deepmind]] — Google DeepMind, AI research lab behind Gemini
- [[concepts/gemini/gemini-enterprise-agent-platform]] — Enterprise platform for Gemini agents
