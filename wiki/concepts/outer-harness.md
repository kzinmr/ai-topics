---
title: "Outer Harness"
type: concept
created: 2026-10-20
updated: 2026-10-20
tags:
  - concept
  - ai-agents
  - agent-harness
  - long-horizon
  - agent-orchestration
  - architecture
sources:
  - raw/articles/2026-10-14_openai_third-moment-research-10000-agents.md
  - raw/articles/2026-05-08_anthropic-engineering_effective-harnesses-for-long-running-agents.md
confidence: medium
related:
  - "[[concepts/long-horizon-agents]]"
  - "[[concepts/harness-engineering/agent-harness]]"
  - "[[entities/third-moment-research]]"
  - "[[entities/openai]]"
---

# Outer Harness

## Definition

An **outer harness** is a supervisory control layer that sits *above* an agent's own harness
(the "inner harness") and manages the agent as a subagent rather than participating in the
task itself. Where the inner harness supplies tools, prompts, sandboxing and the tool-call
loop, the outer harness observes trajectories from the outside and makes lifecycle decisions:
inspect unfinished work, retry, terminate, or escalate to a human.

The term was popularized by OpenAI's October 2026 account of running ~10,000 coding agents
for 36+ hours at [[entities/third-moment-research]], where a frontier reasoning model
(GPT-6 Sol / GPT-6.1 Sol) supervises the **Codex harness** running as a subagent inside Docker.

## Inner vs outer harness

| Layer | Responsibilities | Failure mode it addresses |
|---|---|---|
| **Inner harness** | Tool loop, prompts, sandbox, context management, filesystem abstraction | Agent cannot do the task well |
| **Outer harness** | Trajectory inspection, retry/terminate/escalate, fleet scheduling, budgeting | Agent silently stalls, loops, or drifts at fleet scale |

The distinction matters because at fleet scale the bottleneck shifts from "can one agent solve
this?" to "which of ten thousand running sessions should be killed, restarted, or handed to a
person?" That triage decision cannot be made from inside the agent's own context window.

## Concrete implementation (Third Moment Research, Oct 2026)

- **Inner:** default Codex harness in Docker; ~1 TB of data, docs and a research repo per agent.
- **Outer:** GPT-6 Sol / GPT-6.1 Sol inspecting unfinished trajectories — retry, terminate, or
  escalate to humans. GPT-6.1 Sol is their most-used supervisor model because it matches Astra's
  reasoning quality at the fewest tokens, which matters when supervising thousands of sessions.
- **Pre-flight safety:** agents penetration-test their own sandbox via the Daybreak platform
  before launching simulations, so the outer harness does not have to discover escapes at runtime.

## Relationship to prior harness work

The outer harness is the fleet-scale descendant of Anthropic's "effective harnesses for
long-running agents" guidance: both treat the agent as a stateful, resumable process needing
external checkpoints rather than a single-shot completion. The new element is that the supervisor
is itself a frontier model with judgment about *task quality*, not just a deterministic
watchdog enforcing timeouts and retries.

## Open questions

- Supervisor cost/latency overhead at fleet scale — an outer model reasoning over every stalled
  trajectory can dominate token spend if the retry policy is loose.
- Escalation semantics: what makes a trajectory "unfinished" enough to terminate is still
  heuristic, and mis-terminations are invisible unless logged.
- Attribution: when a supervisor rewrites or retries an agent's work, it becomes unclear which
  model produced the accepted result — relevant for eval and safety claims.

## See Also

- [[concepts/long-horizon-agents]] — the workload class that motivates outer supervision
- [[concepts/harness-engineering/agent-harness]] — the inner harness layer
- [[entities/third-moment-research]] — reference deployment
