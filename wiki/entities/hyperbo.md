---
title: hyperbo
tags: [entity, person, agent-engineering, software-engineering]
type: entity
status: active
updated: 2026-07-18
sources:
  - raw/articles/hyperbo.la--w-code-reds-need-maintenance-loops--83920e0a.md
  - raw/articles/hyperbo.la--w-token-mandates--2d279dd2.md
---

# hyperbo

hyperbo.la is a blog authored by a Stripe engineer (referenced in the Stripe Code Yellow anecdote) covering software engineering, AI coding agents, and organizational practices. The writing is known for its pragmatic, engineering-first perspective on agentic infrastructure, maintenance loops, and the changing production function of software work.

## Overview

Hyperbo's writing sits at the intersection of **agent engineering**, **software engineering culture**, and **organizational design**. The author draws on direct experience at Stripe (including the company's first Code Yellow) and other hypergrowth technology companies to analyze how AI agents change the cost equation of durable software maintenance, the role of individual contributors, and how organizations discover and deploy reasoning compute.

Two major themes in recent writing are the **Code Red / maintenance loop** operating model and **token mandates** as organizational discovery mechanisms.

## Code Reds and Maintenance Loops

The core thesis: most code reds (emergency cross-functional efforts to fix critical metrics) leave behind postmortems and tired ICs — but not durable maintenance. The metric returns to being nobody's job and drifts again until the next crisis.

At Stripe, the first Code Yellow built Adaptive Acceptance for a lighthouse customer threatening to churn — a cross-functional team of ~20 from engineering, data science, marketing, bizops, card policy, and partnerships worked for two months. Unlike most code reds, this one left behind a product. The usual pattern is:

1. A concerned IC or leader flags the situation to an executive.
2. The executive declares a code red; a team scrambles together, disrupting in-flight work.
3. The team executes until metrics match exit criteria.
4. The code red ends, the team disbands, and the metric returns to being unmanaged.

Hyperbo argues that **green is not done** — every code red reveals that some metric is more important than previously believed. The real output should be a durable maintenance loop that keeps the invariant healthy without requiring another tiger team.

## `/Goal` Infrastructure

Agents make maintenance loops cheap enough that teams no longer need to permanently staff every newly discovered invariant. The key innovation is the `/goal` infrastructure:

- `/goal` is **different from asking an agent to do a task** (e.g. "fix this flaky test").
- A goal is a **process that spawns tasks** — it keeps observing metrics, generating interventions, testing them, and asking for human review when it needs authority.
- Example goals: "keep p95 CI latency under N minutes," "reduce customer-visible incidents in this subsystem," "find and remove the top sources of onboarding churn."
- Mechanically, this can look like a text box that accepts a prompt, spawns 50 persistent cloud agents, and passes that `/goal` to agent sessions continuously.

The IC role moves up a level: during the code red, the job is not only to fix the metric but to understand *why* it was able to drift, what human adaptation kept it healthy, what signals those humans were watching, what actions were available, and which parts of that loop can be made durable. The agentic discovery process replaces ad hoc social escalation with a named, inspectable, improvable process.

Code red success: used to require indefinitely staffed teams; now agents change the cost equation so that durable ownership is achievable without permanently borrowing humans from their roadmaps.

## Token Mandates

Token mandates (requiring minimum AI usage across an organization) are rational, not cargo culting. They serve as organizational discovery mechanisms for learning how to deploy reasoning compute.

The steel case:

- AI is a transformative technology; no one knows how to use it or what good practitioners look like.
- **Intelligence is a result of high token consumption** — deploying AI with suitable context, harness, tools, and access enables high token consumption, which is the required recipe for extracting value from reasoning models.
- The existing performance system was built to identify excellence in the old production function; it is almost orthogonal to identifying who can build the new one.
- Roughly **~5% of every org** has the skills and vision to build the machine that builds the machine.
- A small central AI team is fraught because leadership doesn't yet know which practitioners belong on it — it might pick the best brand marketer and miss the person quietly automating campaign production.

Token mandates enable randomized hill climbing to discover what patterns are possible. Last mile deployment is not yet handled by models themselves (as of July 2026), so this discovery must be done by the existing set of expert humans in the business.

## Agent Engineering Connections

Hyperbo's writing connects directly to core agent engineering concepts:

- **Harness engineering**: the "loop that builds the loop" — manufacturing execution capacity through persistent agent fleets maintaining SLOs.
- **Code Red → Maintenance Loop pipeline**: transforming emergency response into durable agentic processes.
- **Token mandates as discovery**: finding the 5% who can build agentic infrastructure and empowering them.
- **`/goal` infrastructure**: the process abstraction that separates goal-setting from task execution, enabling scalable agentic maintenance.

## References

- hyperbo.la--w-agents-agents-agents--79613a0d
- hyperbo.la--w-artichoke-pernosco--58217cbc
- hyperbo.la--w-aws-org-chart--3b38899e
- hyperbo.la--w-cactus-harvesting--5378d197
- hyperbo.la--w-chatgpt-4000--06a17be6
- hyperbo.la--w-code-is-not-the-artifact--7b35d138
- hyperbo.la--w-codex-copypasta--1fc0b1f9
- hyperbo.la--w-coding-agents-for-technical-non-engineers--46484b05
- hyperbo.la--w-debazeling--d1a27bd5
- hyperbo.la--w-do-the-simplest-thing--0638d00b
- hyperbo.la--w-engineering-finance-partnership--1cde771d
- hyperbo.la--w-feedback-windows--4b7adc2e
- hyperbo.la--w-harness-engineering-the-blog-build--bd93b74d
- hyperbo.la--w-iterator-destiny--bcee6a14
- hyperbo.la--w-latex-escapism--d9f50dc7
- hyperbo.la--w-lazy-prompt-rustsec--611207ec
- hyperbo.la--w-nemawashi--03eb1ace
- hyperbo.la--w-production-function-changed--0406b7d8
- hyperbo.la--w-reflections-on-learning-rust--8253a636
- hyperbo.la--w-robot-vacuum-canary-tailscale--53c675e6
- hyperbo.la--w-scaling-impact-senior-staff--0181fa4e
- hyperbo.la--w-secrets-in-parameter-store-postmortem--7b808c31
- hyperbo.la--w-service-mesh--bd9d0e18
- hyperbo.la--w-social-coding-2018--a491bede
- hyperbo.la--w-software-work-not-scheduled--a91959e4
- hyperbo.la--w-source-level-polymorphism--6d4881e0
- hyperbo.la--w-sprint-log-2019-03-08--cdde4413
- hyperbo.la--w-synthesis--6af16823
- hyperbo.la--w-terraform-blue-green--8b8f9b11
- hyperbo.la--w-the-conjoined-villages--f31c5fec
- hyperbo.la--w-tool-discovery--3c3beb28
- hyperbo.la--w-what-does-it-mean-to-do-a-good-job--3ccf2ed2
- hyperbo.la--w-winding-down-artichoke-ruby--844efee4

## See Also

- [[entities/substack]] — Newsletter and content publishing platform.
- [[concepts/coding-agents/coding-agents]] — Topics covered in hyperbo's writing on AI and software engineering.
- [[concepts/software-engineering]] — Software development practices and engineering culture.
