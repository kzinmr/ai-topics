---
title: "AI Coding Effectiveness Debate — If Coding Has Been Solved, Why Does Software Keep Getting Worse?"
created: 2026-07-27
updated: 2026-07-27
type: concept
tags:
  - coding-agents
  - code-quality
  - ai-skepticism
  - developer-tooling
sources:
  - raw/articles/2026-07-24_ptrchm-ai-coding-solved-debate.md
  - https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/
---

# AI Coding Effectiveness Debate — If Coding Has Been Solved, Why Does Software Keep Getting Worse?

The AI coding effectiveness debate is a central tension in the 2025–2026 software engineering landscape. On one side, AI [[concepts/coding-agents/coding-agents|coding agents]] such as [[entities/claude-code]] have demonstrated remarkable capabilities in generating, debugging, and deploying code at speed, leading to claims — both serious and hyperbolic — that "coding has been solved." On the other side, a growing body of anecdotal and empirical evidence suggests that software quality across the industry continues to decline, with major products exhibiting regression bugs, degraded UX, and brittle infrastructure. This paradox — powerful AI tools coexisting with worsening software — forms the core of the debate.

## The "Coding Has Been Solved" Narrative

Throughout 2025 and 2026, leaders at [[entities/anthropic]], [[entities/openai]], and other frontier labs have made increasingly ambitious predictions about AI's capacity to automate software engineering. Statements that "AI will write 100% of code by year's end" reflect a widespread belief that coding agents have crossed a capability threshold. Benchmarks such as SWE-bench show AI systems resolving real-world GitHub issues at competitive accuracy rates. Coding agents now operate as autonomous contributors in production workflows: they open PRs, run CI/CD pipelines, write tests, and deploy changes.

Proponents argue that:
- AI dramatically increases **developer throughput**, enabling small teams to ship features at the velocity of much larger organizations
- Coding agents lower the barrier to entry for non-engineers, democratizing software creation
- The combination of agentic loops, tool-use capabilities, and long-context windows means AI can reason about codebases holistically
- Management expectations have been reshaped: teams are now expected to produce more output with the same (or fewer) headcount

These productivity gains are real and measurable. Companies report shipping cycles shrinking from months to weeks. The promise of the "Agentic Era" is fundamentally about **more code, faster**.

## "Nothing Works" — The Skeptical Counterargument

In July 2026, a widely circulated essay by ptrchm titled "Nothing Works and Everyone Is Euphoric" captured the skeptical counter-narrative. The author argued that despite the proliferation of powerful AI coding tools, the lived experience of software users has been deteriorating:

- Banking apps require multiple authentication attempts before completing transactions
- Desktop applications steal focus and interfere with other workflows
- Warranty claim forms fail silently with JavaScript errors
- Car infotainment systems ship with bugs that affect driver safety
- OS updates have become a source of dread rather than excitement

The core argument is that AI tools are being used as **volume multipliers** rather than **quality multipliers**. The industry's KPI-driven culture incentivizes shipping features over fixing bugs, and AI tools amplify this tendency by making it even easier to produce code quickly. The result is what some call **AI debt** — a compounding accumulation of generated code that works superficially but lacks architectural coherence, proper error handling, and edge-case robustness.

## Code Generation vs. Code Quality — The Critical Distinction

A central insight of the debate is the distinction between **code generation** and **code quality**. AI coding agents are remarkably effective at the former — producing functionally correct code from prompts — but they do not inherently produce code that is:

- **Architecturally sound**: following separation of concerns, avoiding tight coupling
- **Maintainable**: documented, readable by humans, consistent with project conventions
- **Resilient**: handling error states, edge cases, and degradation gracefully
- **Minimal**: avoiding unnecessary abstractions or over-engineered solutions

This gap is explored in the related concept of [[concepts/coding-agents/ai-code-quality]], which documents the tension between "slop cannon" usage of AI tools versus deliberate, quality-oriented AI-assisted development. The distinction also connects to the [[concepts/coding-agents/normalization-of-deviance-in-ai-coding]], where the ease of AI generation erodes engineering discipline over time.

## Productivity Metrics vs. Quality Metrics

The debate exposes a fundamental misalignment between how organizations measure engineering effectiveness and what actually produces durable software:

| Metric Type | What It Measures | AI Impact | Software Quality Impact |
|---|---|---|---|
| **Productivity metrics** | PRs merged, story points completed, features shipped | Dramatic increase | Neutral or negative |
| **Velocity metrics** | Cycle time, deployment frequency | Significant reduction | Neutral |
| **Quality metrics** | Bug density, MTTR, regression rate, user satisfaction | Often unmeasured | Decline observed |
| **Business metrics** | Revenue, retention, churn | Lagging indicator | Long-term risk |

The essay's author points out that "making things more stable doesn't always have a direct effect on the numbers" and "doesn't look exciting in presentations." This creates a systemic incentive to prioritize AI-amplified feature velocity over AI-assisted quality engineering. The [[concepts/agent-productivity]] page explores related dynamics around the cognitive and organizational effects of AI tooling on development teams.

## Industry Responses and the AI Debt Cycle

The software industry is entering what some observers describe as an **AI debt cycle**: companies rush to adopt AI coding tools to stay competitive, produce large volumes of AI-generated code that passes basic tests but accumulates hidden quality costs, and then face mounting maintenance burdens that consume the productivity gains the tools initially promised.

Several counter-currents are emerging:

- **Individual developer rebellion**: As highlighted in the essay, solo developers are using AI tools to build software that would previously have been beyond their reach, potentially raising the baseline quality of independently developed software
- **Quality-focused AI workflows**: Some practitioners advocate using LLMs for systematic bug finding, test generation, and code review rather than raw code production (see also [[concepts/evaluation/agent-evaluation-methodology]])
- **Platform-level responses**: Growing frustration with degrading OS quality (macOS, Windows) is fueling interest in alternative platforms and "acts of rebellion" against mainstream software vendors

The [[concepts/ai-slop-productivity-paradox]] captures a related dynamic: AI enables more output with less effort, but the majority of that output may be low-quality "slop" that degrades the overall information and software ecosystem.

## The Infrastructure Fragility Problem

Beyond application-level bugs, the essay touches on a deeper concern about **infrastructure fragility**. The author notes that software has grown more complex over time through accumulated abstractions, frontend frameworks, and infrastructure layers. Each new abstraction adds fragility: "the bar for 'user experience' has kept rising, but everything has become increasingly fragile." AI coding agents, which excel at generating code within existing frameworks and abstractions, may inadvertently accelerate this complexity accumulation without addressing the underlying fragility.

This connects to broader concerns about [[concepts/software-supply-chain-security]], where the speed of AI-generated dependency additions amplifies the attack surface of modern software.

## Implications for Software Engineering

The AI coding effectiveness debate has several implications for the practice of software engineering:

1. **The role of the engineer shifts**: As AI handles more code generation, the engineer's value moves toward architecture, quality assurance, and systems thinking — skills that current AI tools do not replicate
2. **Organizational incentives must change**: Without structural changes to how engineering teams are evaluated and rewarded, AI tools will primarily amplify existing pathologies rather than improve outcomes
3. **Quality engineering becomes a differentiator**: Organizations that invest in AI-assisted quality (test generation, bug detection, code review) rather than AI-assisted volume may gain durable competitive advantage
4. **The "one-person unicorn" is real but limited**: Individual developers can now build software at unprecedented scale, but sustainable software still requires the discipline and infrastructure traditionally provided by teams

The essay's final note of optimism — that "everyday software will get better as a result of this frustration" — suggests that the debate itself is a productive force, driving awareness of the quality gap and motivating developers to use AI tools differently.

## Sources

- ptrchm, ["Nothing Works and Everyone Is Euphoric"](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/), July 24, 2026. HN: 878 points, #2 on Hacker News.
- Related: [[concepts/coding-agents/ai-code-quality]] — on using AI to write better code slowly vs. the "slop cannon" approach
- Related: [[concepts/coding-agents/normalization-of-deviance-in-ai-coding]] — on how AI coding erodes engineering standards
- Related: [[concepts/ai-slop-productivity-paradox]] — on the productivity/quality trade-off in AI-generated content
- Related: [[concepts/agent-productivity]] — on the cognitive and organizational effects of AI coding tools
