---
title: "Ryan Lopopolo — Core Ideas & Philosophy"
type: entity
parent: ryan-lopopolo
created: 2026-04-28
updated: 2026-04-28
tags:
  - person
  - harness-engineering
  - ai-agents
  - agentic-engineering
  - elixir
  - symphony
sources: []
---

# Ryan Lopopolo: Core Ideas & Philosophy

Back to main profile: [[ryan-lopopolo]]

## Harness Engineering — The System, Not the Prompt

Ryan's defining contribution is the distinction between *prompting* and *harness engineering*:

> "Prompting is asking an LLM to write code. Harness engineering is building the systems, feedback loops, and constraints that let agents operate autonomously at scale."

Key principles:

1. **Constraint-Driven Development** — Ryan deliberately refused to write any code himself in the Frontier experiment, forcing the team to build complete end-to-end agent capability. "If we're deploying agents into enterprises, they should be able to do all the things I do."

2. **Systems Over Prompting** — When agents fail, don't just prompt harder. Ask: "What capability, context, or structure is missing?"

3. **Fast Build Loops** — Enforced <1 minute inner loop. Progressively swapped build systems (Makefile → Bazel → Turborepo → Nx) to maintain speed.

4. **Human Bottleneck Shift** — Humans moved from code review to building systems, observability, and context. Post-merge review is now statistical sampling/auditing.

5. **Code is Disposable** — Worktrees and merge conflicts matter less when agents resolve them autonomously.

## Symphony — Multi-Agent Orchestration Layer

Ryan built **Symphony**, an internal Elixir-based orchestration system for managing AI coding agents:

**Why Elixir/BEAM?** Native process supervision (gen_server), fault tolerance, and massive concurrency map perfectly to task-driven agent daemons.

**How Symphony Works:**
1. Spins up isolated git worktrees per ticket
2. Coordinates parallel coding agents (Codex instances)
3. Handles CI, flaky tests, and merge queues
4. **Rework State:** If PR fails review, Symphony trashes the entire worktree and restarts from scratch. Humans only intervene to fix systemic context gaps.

## The $land Skill — Autonomous PR Lifecycle

Full delegation via a custom `$land` skill:

```bash
$land → push PR → wait for human/agent review → wait for CI → fix flakes → merge upstream → resolve conflicts → merge to main
```

- **Review Agents** bias toward merging. Only flag issues >P2
- **Author Agents** can defer or push back on scope-creeping review comments
- Agents attach compressed trajectory videos (FFmpeg screen recordings) to PRs, proving work completion without human shoulder-surfing

## Agent Utilization Is the New Performance Ceiling

> "A billion tokens per engineer per day is a utilization target. It asks how much of the software lifecycle the agents are actually allowed to do."

> "Writing patches is a small slice of the job. Most of the software lifecycle is reading logs, checking traces, diffing behavior across releases, chasing down performance regressions, inspecting crash dumps, following analytics, tightening invariants, and proving that a fix actually worked."

Numbers from Ryan's own data:
- **3-5 PRs/engineer/day** on GPT-5.2 *without* Symphony
- **~75 PRs/engineer/week** *with* Symphony

> "Utilization drops anywhere the agent cannot see or act."

## Stop Treating Code as the Artifact

> "Once agents write most of the code, stop treating the source files as the artifact. The durable thing is everything upstream of them: the repo-owned spec, the guardrails, the typed boundaries, and the operator surface that determines what code is allowed to exist."

> "Symphony is a ghost library: the implementation is downstream of the spec."

## Software Work Is No Longer Scheduled

> "Backlogs, roadmaps, sprint planning, quarterly prioritization: all of that evolved in a world where the truly scarce resource was human time and attention."

> "Full Japanese support in an alpha app for internal users in our Tokyo office should have been a project. In my day-to-day work, it was a background task."

> "The truly scarce resource is still human time and attention. Spend it on bets and ambiguity, not on scheduling the known-good engineering that agents can clear in the background."

## The Production Function Changed

> "For decades, software output scaled roughly with human engineering time. That mental model is deeply ingrained: planning, staffing, prioritization, and risk management all assume it. That model is now wrong."

> "I haven't written code by hand in months. My laptop hums with its lid half closed at night, running `caffeinate -sdi` so a PR or three can get authored, pushed, reviewed and merged while I'm asleep."

> "Any time I catch myself thinking 'I wish …', I instead say '@codex please …'. I am more than happy to throw away 80% of these! But those rejections are learnings."

## What Does It Mean to Do a Good Job?

Ryan's deepest philosophical post on verification as the central problem of AI-assisted development:

> "Verification was always the problem. AI makes that obvious because every real task is downstream of a question we almost never write down. What does it mean to do a good job?"

> "Producing an artifact and reviewing it both require hundreds of small decisions about non-functional requirements: tone, taste, risk tolerance, how much polish is enough, what shortcuts are acceptable, what counts as done. Historically, teams wrote almost none of that down."

> "You do not get to run your AI through a hiring pipeline."

> "Without that guidance, the reviewers endlessly bully the implementer and nothing converges. Human reviewers usually know to unblock while still providing high-signal feedback. The models do not unless you say it."

> "If you want the models and agents to do a good job, write down what that means, then add nuance only when the coarse instruction starts to overfit."

## Context Engineering for Agent Legibility

Ryan's approach to making codebases agent-friendly:

- **AGENTS.md as Table of Contents** — Keep it to ~100 lines with pointers to deeper docs in a structured docs/ directory.
- **Inverted Dev Workflow** — Spawn the agent first (Codex), then give it scripts/skills to boot the local observability stack on demand.
- **Encoding Engineering Taste** — Non-functional requirements, guardrails, and team preferences persisted in markdown: `core_beliefs.md`, `tech_tracker.md`, `quality_score.md`.
- **Self-Improving Loops** — Agent session logs, PR comments, and failed builds are slurped into blob storage. Daily agent loops distill learnings back into repo context.

## The Frontier Enterprise Vision

Ryan's work at OpenAI Frontier points to safe, observable, governable agent deployment at enterprise scale:

- Native IAM, security tooling, and workspace integrations
- **Safety Specs** that prevent data exfiltration and respect internal code names
- **Data Ontology/Semantic Layer** — critical for business-aware agents (aligning definitions of "revenue," "active user," etc.)

## Key Quotes

> "Prompting is asking an LLM to write code. Harness engineering is building the systems, feedback loops, and constraints that let agents operate autonomously at scale."

> "A billion tokens per engineer per day is a utilization target. It asks how much of the software lifecycle the agents are actually allowed to do."

> "Writing patches is a small slice of the job. Most of the software lifecycle is reading logs, checking traces, diffing behavior across releases, chasing down performance regressions, inspecting crash dumps, following analytics, tightening invariants, and proving that a fix actually worked."

> "Once agents write most of the code, stop treating the source files as the artifact. The durable thing is everything upstream of them: the repo-owned spec, the guardrails, the typed boundaries, and the operator surface that determines what code is allowed to exist."

> "Symphony is a ghost library: the implementation is downstream of the spec."

> "Planning systems are bad at background tasks. The work is too small to look strategic, too cross-cutting to have a clean owner, and too easy to postpone because nothing is fully on fire yet."

> "I haven't written code by hand in months. My laptop hums with its lid half closed at night, running `caffeinate -sdi` so a PR or three can get authored, pushed, reviewed and merged while I'm asleep."

> "My job these days is to teach the machine how to do more and more of the work that I used to do."

> "Verification was always the problem. AI makes that obvious because every real task is downstream of a question we almost never write down. What does it mean to do a good job?"

> "You do not get to run your AI through a hiring pipeline."

> "Without that guidance, the reviewers endlessly bully the implementer and nothing converges. Human reviewers usually know to unblock while still providing high-signal feedback. The models do not unless you say it."

> "If you want the models and agents to do a good job, write down what that means, then add nuance only when the coarse instruction starts to overfit."

> "Build things. Even weird things. Even things that might not last forever. The act of building changes you."

## See Also

- [[ryan-lopopolo--timeline|Timeline & Career]]
- [[ryan-lopopolo--writings|Writings & Speaking]]
