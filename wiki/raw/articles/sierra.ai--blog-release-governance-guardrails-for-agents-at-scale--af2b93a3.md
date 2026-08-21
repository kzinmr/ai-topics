---
title: "Release governance: guardrails for agents at scale"
url: "https://sierra.ai/blog/release-governance-guardrails-for-agents-at-scale"
fetched_at: 2026-08-21T10:01:07.386033+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# Release governance: guardrails for agents at scale

Source: https://sierra.ai/blog/release-governance-guardrails-for-agents-at-scale

Some of the world’s largest companies build their agents on Sierra: hundreds of people working inside a single agent, across hundreds of journeys, serving millions of customers. A small change to the agent can instantly reshape how it behaves with every customer. At that scale, releasing an agent safely can’t rely on an informal check or on someone remembering to double-check a change.
That’s why we built release governance directly into the Sierra platform: the checks, approvals, and rollout strategies that move a change safely from a builder’s
Workspace
to a live customer conversation. It’s the same discipline that carried software teams from a few developers to thousands — automated testing, code review, and staged rollouts — applied to the
Agent Development Lifecycle
. In practice, that means Agent Checks and Simulations catching problems proactively, merge approval workflows putting a person in the loop, and split traffic releases rolling changes out gradually.
Catch problems before customers do
The best time to find a problem is before you’ve made it. Long before a change is ready to ship, Sierra is already checking your work.
Agent Checks
is a linter for your agent, surfacing warnings as you build based on your journeys and the conversations they generate.
It catches the issues that are easy to miss and expensive to ship: a tool your prompt references but never made available, conflicting instructions to the agent, a lookup tool doing an action tool’s job, a response that works on screen but falls apart on a call, or a sensitive-data lookup with insufficient authentication. Checks are prioritized by severity, helping teams distinguish issues likely to impact customers from lower-priority quality improvements, and most come with a suggested fix from
Ghostwriter
that can be applied in place.
While Agent Checks catch problems in how an agent is built, some issues only show up in conversations. That’s why teams can also require
Simulations
to pass before moving toward production. Together, they provide automated quality gates built directly into the platform, reducing the risk of a change slipping through unchecked.
Not every decision can be automated
Automated gates catch what’s broken, but they can’t tell you whether a change should ship.
That’s why we introduced
merge approval workflows
. Organizations can now require peer review before any change releases, just as software teams require approval before a pull request lands. A dedicated
Reviewer role
lets you decide exactly whose sign-off is needed: a CX lead, a compliance stakeholder, an engineering manager, or another domain expert.
Reviewers can inspect line-by-line diffs, leave contextual comments, and request changes before a merge is approved. Builders can work alongside Ghostwriter to address that feedback and even request another review before a human signs off.
Ship gradually, not all at once
Once a change has sign off, the next question is whether you should ship it to all your customers at once. Usually, the answer is no.
Our new
split traffic releases
let organizations incrementally roll out a release to a portion of customer traffic before expanding it to everyone — the same canary strategy software teams have relied on for years. If you’ve upgraded your model, redesigned authentication, or made a sweeping behavioral change, you can verify the release behaves as expected before rolling it out more broadly. A large airline, travel marketplace, and fintech company are already using split traffic to control how rollouts reach their customers.
For teams already using Experiments, split traffic releases serve a different purpose: Experiments help you determine which variation performs best, while split traffic releases help you safely deploy the winning one.
And because every release is an immutable snapshot, rolling back is just as fast if something unexpected appears.
Governance for scale
Software teams didn’t invent code review, CI/CD, and canary deployments because they enjoyed process. They adopted them because they’re the only way hundreds of people can safely ship software together.
Enterprise agents have reached that same point. As the Agent Development Lifecycle matures, release governance stops being overhead and becomes the thing that lets teams move quickly without holding their breath. These controls earn their keep with a single builder on a single journey, and become non-negotiable once hundreds of people are building in parallel for an agent talking to customers around the clock.
