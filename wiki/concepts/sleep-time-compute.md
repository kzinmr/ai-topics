---
title: "Sleep-Time Compute — Offline Reasoning Before the Query Arrives"
created: 2026-09-23
updated: 2026-09-23
type: concept
tags: [test-time-scaling, token-economics, inference, context-engineering, ai-agents, agent-memory, arxiv]
sources:
  - raw/articles/2026-09-23_arxiv_2504.13171_sleep-time-compute.md
related:
  - "[[concepts/test-time-compute]]"
  - "[[concepts/token-economics]]"
  - "[[concepts/continual-learning]]"
  - "[[concepts/kv-cache-compaction]]"
---

# Sleep-Time Compute — Offline Reasoning Before the Query Arrives

## Definition

**Sleep-time compute** is the practice of letting a model "think" *offline*, before a
user query ever arrives — anticipating what questions might be asked and pre-computing
useful quantities about a context so that far less work is needed at test time. It was
introduced by Lin, Snell, et al. (Letta / UC Berkeley, arXiv:2504.13171, Apr 2025) as a
fourth axis of compute, distinct from pretraining, RL post-training, and
[[concepts/test-time-compute|test-time compute]].

The analogy is biological: a brain consolidates and pre-processes memories during sleep,
so that waking recall is cheap. Sleep-time compute moves the expensive reasoning out of
the latency-critical, cost-critical request path and into idle periods.

## Why It Matters

Test-time compute improves accuracy but at high **latency and inference cost** — every
extra reasoning token is paid for on the user's clock. Sleep-time compute breaks this by
amortizing reasoning across the *context* rather than the *query*:

- On Stateful GSM-Symbolic and Stateful AIME, it cut the test-time compute needed to hit
  the same accuracy by **~5×**.
- Scaling the sleep budget further raised accuracy by up to **+13%** (GSM-Symbolic) and
  **+18%** (AIME).
- The authors introduced **Multi-Query GSM-Symbolic** (several related queries over one
  context) to show the pre-computed state amortizes across queries: the more questions you
  expect about a given context, the more sleep-time compute pays off.

## Relationship to Other Ideas

Sleep-time compute is the *proactive* counterpart to reactive
[[concepts/test-time-compute|test-time scaling]] — instead of spending more tokens when the
query arrives, it spends tokens *ahead* of the query. It shares territory with
[[concepts/continual-learning|continual learning]] and the "machine dreaming" idea (a model
rehearsing skills on its own experience), but differs in mechanism: sleep-time compute
produces pre-computed *artifacts* (notes, summaries, inferred facts) attached to a context,
not necessarily weight updates.

Economically it reframes the budget in [[concepts/token-economics]] terms: idle GPU cycles
are far cheaper than request-path cycles, so shifting reasoning off the critical path is an
arbitrage on latency-critical compute. Conceptually it also sits near
[[concepts/kv-cache-compaction|context compaction]] — both pre-digest context to make the
live turn cheap — but compaction *compresses*, sleep-time compute *derives new understanding*.

## Open Questions

- How do you decide *what* to pre-compute when the query distribution is unknown or adversarial?
- For agentic memory, does a sleep pass that revisits an [[concepts/ai-agent-memory|agent's
  accumulated context]] produce genuinely new capability, or just re-summarization?
- What is the correct scheduler — how much "sleep" budget before diminishing returns,
  echoing the [[concepts/attention-bottleneck|context capacity]] limits it is partly designed to dodge?

## Sources

- Sleep-time Compute: Beyond Inference Scaling at Test-time — arXiv:2504.13171 (2025-04-17), Lin, Snell, Wang, Packer, Wooders, Stoica, Gonzalez (Letta / UC Berkeley)
