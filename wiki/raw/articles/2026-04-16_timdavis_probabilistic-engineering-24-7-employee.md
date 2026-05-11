---
title: "Probabilistic engineering and the 24-7 employee"
source: "Tim Davis Blog"
date: 2026-04-16
scraped: 2026-05-11
type: blog
url: https://www.timdavis.com/blog/probabilistic-engineering-and-the-24-7-employee
authors: ["Tim Davis"]
tags: [agentic-engineering, software-engineering, ai-agents, career, ai-infrastructure]
---

# Probabilistic engineering and the 24-7 employee

**Author**: Tim Davis (runs Modular, creator of Compound Loop)
**Published**: 2026-04-16
**URL**: https://www.timdavis.com/blog/probabilistic-engineering-and-the-24-7-employee

## Full Content

Software is quietly becoming a probabilistic system.

We built our profession around deterministic code. Write it, test it, ship it, know it works - but in my experience that contract is breaking. Inside the top few percent of operators at truly AI-native companies, the codebase has started to become something you _believe_ works, with a probability you can no longer precisely state. The workday is changing as a consequence, and so are the roles, the organizations, the training pipelines, and the nature of what it means to ship.

I noticed because I built one.

A few months ago, in the evenings after my day job running Modular, I started building a side project called Compound Loop - a system that orchestrates multiple frontier models against each other to write, review, and merge code more or less autonomously. I would set it running on a real problem before I went to bed, and I would wake up and triage a stack of pull requests that had not existed the night before. Some were excellent, some were wrong, and some surfaced a question I did not know to ask. By 8 a.m. I was not catching up on yesterday's work - I was deciding which of the overnight jobs to keep, while the system kept analyzing logs and adding more PRs. The continuous compounding nature of it was, and still is, infectious to watch.

For the first time in the history of knowledge work, the person who went home did not take the only copy of their brain with them. 9-9-6 as a concept is dead, and we are simply 24-7 employees now - but the 24-7 employee is not a person working 24 hours, it is a person whose agents work with enormous parallelization. Most teams in 2026 still bottleneck on coordination rather than typing, and most organizations have barely begun to restructure, but the frontier is always where the future shows up first, and the frontier is already here. This essay is not a description of the industry at large, but rather a description of what is already happening inside the most AI-native teams, and where I believe that pulls the rest of the industry.

## Roles are not just collapsing upward - they are splitting

Inside the most AI-native teams, the pattern is messier than the clean "everyone levels up" story most commentary is selling. Some operators really are moving up the stack: the best engineers are becoming more effective product managers, working at engineering's abstraction layer, the best product managers are becoming system architects, and the best architects are thinking about distribution, growth, and the shape of the market. For this group - maybe the top tier of any team - the work is more leveraged than it has ever been, and they are having the best years of their careers.

But that is not the whole picture. Alongside the upward shift, a downward pressure is fragmenting roles in ways the headlines are not covering. Plenty of engineers are not becoming architects - instead they are becoming spec writers, reviewers, and agent babysitters, operators who spend their days translating intent into machine-readable prompts and then grading the machine's work against standards they themselves might not fully possess. Some of that work is genuinely important, but some of it is the 2026 equivalent of data entry, dressed up in new terminology.

These fragmented roles will be paid less, valued less, and in many cases become career dead ends. The pay gap between the top tercile running fleets of agents effectively and the middle tier managing their exhaust will be wider than the pay gap between engineers and sales reps was in the previous era. That gap is already opening.

In AI infrastructure, kernel performance and compiler design and hardware abstraction remain deeply defensible moats, because there is still a high degree of determinism needed at the lowest levels. But at the level of building software on top of those moats, the center of gravity has shifted hard toward the human inputs a machine cannot yet replicate.

## Jevons was right about coal, and he is right about code

In 1865, economist William Stanley Jevons observed that more efficient steam engines led to _more_ coal consumption rather than less - efficiency expanded the set of things worth building engines for. We are living the software version of that same observation. As the unit cost of writing code approaches zero, we are not writing less, we are writing vastly more and shipping vastly more.

Agents are opening pull requests, reviewing each other's work, and closing them without a human ever touching the keyboard, with a continuously live log monitoring loop. Self-healing test suites rewrite themselves when the underlying code changes. Autonomous experimentation loops spin up, measure, and tear down a hundred hypotheses in the time a team once ran three. Documentation updates itself faster on merges.

The throughput gains are not subtle — teams that have genuinely restructured around agents are shipping three, five, or ten times what they shipped a year ago.

But Jevons' second lesson: when supply explodes, selection becomes everything. More coal made engines more valuable, but it also made the discipline of choosing what to burn dramatically more important. Cheap energy without judgment is just waste, and the same logic applies to code. The operator who can direct a fleet of agents toward the right problem, filter the outputs for what is actually valuable, and integrate the results into something coherent is doing the highest-leverage work in software right now.

## From deterministic engineering to probabilistic engineering

We are rapidly moving from deterministic engineering to probabilistic engineering, and our tools, training, and organizational instincts are still built for the old paradigm. Deterministic engineering: you wrote code, you tested it, you reviewed it, and you knew what it did. Failures were deterministic.

Probabilistic engineering is different. Large portions of the codebase were generated by stochastic systems, reviewed under time pressure against contexts too large to fully hold, and integrated into a whole that no single human ever designed end-to-end. The codebase still runs and still ships, but the confidence interval around "this works as intended" has widened.

**The core asymmetry**: generation has become cheap, but validation has not.

An agent can produce a plausible-looking 500-line pull request in under a minute, but catching a subtle bug in that same pull request - a concurrency issue, a silent misinterpretation of the spec - can take a senior engineer an hour of careful reading. Review scales worse than generation, and crucially, review scales worse than _linearly_ with output volume, because as more of your codebase is written by agents, the context you need to hold in your head grows.

At some scale, the system produces more than humans can reliably evaluate, and correctness becomes probabilistic rather than assured. The codebase stops being a thing you _know_ works and becomes a thing you _believe_ works, with a probability you can no longer precisely state.

The failure mode is not a dramatic collapse but a slow, silent degradation - generation rises, review quality falls, unnoticed defects accumulate, and trust in the system quietly erodes until a customer or an auditor or a production incident forces the issue.

We do not yet have the tooling to solve this properly. Culture helps - smaller merges, harder gates, ruthless skepticism toward polished output - but culture does not scale past a certain team size. The new CI/CD is not a tool yet - it is a culture of ruthless skepticism, and an honest admission that we are building the replacement for that culture in real time.

## Not every industry moves at the same speed

- **Deterministic tier**: Highly regulated, high-stakes domains (avionics, medical devices, financial trading, nuclear) will remain deeply deterministic. The cost of a silent correctness failure is lives.
- **Probabilistic tier**: Consumer software, internal tools, marketing systems, most SaaS, experimental product work - already running hot.
- **Convergence zone**: The frontier of "safe enough to do probabilistically" will keep moving. Domains that look deterministic today will find probabilistic methods creeping up on them from below.

## The agentic fleet

The right metaphor is not the "factory shift" but "the agentic fleet" - though with honesty that most operators are running a swarm of brittle contractors, not a well-drilled Navy. Agents are uneven in capability, stochastic in behavior, occasionally confidently wrong, and often expensive to run at scale.

A fleet has composition (different agents for different tasks), coordination (handoffs, dependencies, escalation paths), and a command structure (someone decides the mission, sets the rules of engagement, and owns the outcome).

## Three bets for the next decade

1. **The compound loop**: The teams building mechanisms for continuous, multi-agent work that compounds overnight while humans sleep will outpace teams still iterating in synchronous day-long cycles.
2. **Validation infrastructure**: Generation is solved; validation is the bottleneck. The tools that catch stochastic failures before they become production incidents will create a moat.
3. **The operator class**: The human operators who can point agent fleets at the right problems, filter outputs, and integrate results coherently will be the most valuable people in software — not because they type fastest, but because they see clearest.

## Related
- [[concepts/probabilistic-engineering]]
- [[entities/tim-davis]]
- [[concepts/compound-engineering-loop]]
- [[concepts/agentic-engineering]]
