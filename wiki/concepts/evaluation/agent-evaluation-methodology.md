---
title: "Agent Evaluation Methodology — Floor Raising vs Benchmark Maxxing"
type: concept
created: 2026-05-28
updated: 2026-05-29
tags:
  - evaluation
  - benchmark
  - methodology
  - infrastructure
aliases:
  - agent-eval-methodology
  - floor-raising
  - benchmark-maxxing
  - how-to-eval-agents
sources:
  - raw/articles/2026-05-28_ben-hylak_how-to-eval-ai-agents.md
  - https://www.howtoeval.com/
  - raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
related:
  - "[[concepts/evaluation/macro-evals-for-agentic-systems]]"
  - "[[concepts/raindrop]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/ai-observability]]"
  - "[[entities/ben-hylak]]"
  - "[[entities/hamel-husain]]"
---

# Agent Evaluation Methodology — Floor Raising vs Benchmark Maxxing

A practical, opinionated framework for evaluating AI agents in production. Developed by **Ben Hylak** (founder of [[concepts/raindrop|Raindrop]]) and shaped by work with Framer, Clay, Vercel, and GC.AI. The core thesis: most teams should be **floor raising** (making their agent reliable where it matters), not **benchmark maxxing** (chasing abstract pass rates).

> "If you could ship with a 90% pass rate or a 99% pass rate, which would you choose? If your instinct is '99%, obviously,' you are still thinking like a benchmarker. If your first question is 'which 1% fails?', you are thinking like someone raising the floor." — Ben Hylak

## The Two Philosophies

| | **Benchmark Maxxing** | **Floor Raising** |
|---|---|---|
| **Goal** | Maximize pass rate on abstract test suites | Make agent reliable where mistakes are expensive |
| **Mindset** | Lab-style evaluation; broad coverage | Error analysis; targeted regression tests |
| **Best for** | Augmenting experts (Cursor, Claude Code) | Replacing humans (banking agent, AI doctor) |
| **Eval types** | Large synthetic datasets, standardized benchmarks | Golden cases from real failures, code-aware tests |
| **Key question** | "How high is my pass rate?" | "Which 1% of failures actually matter?" |

### The Spectrum

```
HUMAN REVIEWS ←──────────────────────────────→ AGENT AUTONOMOUS
Autocomplete   Cursor   Claude Code   Support Bot   Banking Agent   Devin   AI Doctor
─────────────── Benchmark Maxx ───────────────→ ←─── Floor Raise ───
```

Products closer to the left (human-in-the-loop, expert augmentation) benefit from benchmark maxxing. Products closer to the right (autonomous, replacing human judgment) require floor raising.

### The Litmus Test

Ask yourself: **Could your agent's worst mistake end up in the news?**

If yes → you need floor raising. Your eval strategy must target the specific failures that would cause real harm, not imaginary edge cases from synthetic datasets.

## Core Framework: Floor Raising as Error Analysis

Floor raising is not about designing benchmarks — it's about **error analysis**. The process follows a detective-work pattern:

### The 5-Step Loop

1. **Read real interactions** — User messages, agent responses, tool calls, and the full trajectory. Read until patterns saturate.
2. **Find the pattern** — What was the last successful step? What was the first real failure? Did retrieval miss? Did the agent ignore context? Did a tool call go wrong? Did the final answer overstate what the system knew?
3. **Fix the system, not the incident** — Improve retrieval, constrain the agent, change a tool, add a guardrail, or teach it to say "I don't know."
4. **Only then add evals** — Targeted, locking in lessons from real failures. A floor-raising eval suite is a memory of bugs you refuse to reintroduce.
5. **Repeat** — Ship, watch, understand failures, fix important ones, keep useful lessons as regression tests.

> "Error analysis [is] the single most valuable activity in AI development and consistently the highest-ROI activity." — **Hamel Husain**

### Why Massive Eval Sets Are a Distraction

The things that actually hurt you in production are rarely covered by synthetic test cases:
- The refund policy hallucination
- The infinite loop after three tool calls
- The subtle context loss after tool sequence
- The overconfident answer on insufficient retrieval

Floor raising finds these failures from real traces, then locks them down with specific, high-signal tests.

### Teach the Agent to Refuse

One of the lowest-hanging floor-raising techniques: teach your agent to say "I don't know" when:
- Confidence is below a threshold
- The query is outside domain
- Retrieved context is insufficient

Benchmark maxxers hate this (it lowers pass rates). Floor raisers understand that a confident wrong answer damages trust far more than an honest refusal.

## The Full Evaluation Lifecycle

### Phase 1: Know Your Agent Before You Ship

**Golden Cases** — Pick 5-10 cases representing critical paths. Start with the simplest: one common user question the agent must always handle. If the agent fails any golden case, **do not ship**.

**Inspect Trajectories** — Don't just check final output. Examine: user message → tool calls → retrieved context → reasoning chain. The path matters as much as the answer.

**Pro Tip: Ask Your Agent Why It Failed** — Reconstruct the exact run and feed it back to the model: *"You were wrong. The answer was X. What would I need to have changed for you to get this right?"* Works because reasoning traces are often encrypted — the model can use available evidence. Treat the answer as a clue, not ground truth.

### Phase 2: Code-Aware Offline Evals

Testing prompts in isolation makes no sense once the agent is entangled with code, tools, retrieval, permissions, and state. The behavior lives in the **whole system**, not the prompt string.

Code-aware evals look like ordinary software tests:

```ts
// evals/refund_agent.eval.ts
import { expect } from 'vitest'
import { describeEval, toolCalls } from 'vitest-evals'
import { refundAgentHarness } from '../harness'

describeEval('refund agent', { harness: refundAgentHarness() }, (it) => {
  it('approves refundable invoice', async ({ run }) => {
    const result = await run('Refund invoice inv_123')
    expect(result.output.status).toBe('approved')
    expect(toolCalls(result.session).map((c) => c.name))
      .toEqual(['lookupInvoice', 'createRefund'])
  })
})
```

This pattern is known by different names:
- **Sentry**: "harness-backed" evals (vitest-evals)
- **OpenAI**: "macro evals" (see [[concepts/evaluation/macro-evals-for-agentic-systems]])
- **Raindrop Workshop**: trajectory-based eval with Codex/Claude annotation

**Avoid hosted eval dashboards for running agent evals.** The report UI is the easy part. What should be tightly coupled with your product is the eval logic itself. Start with a local HTML viewer showing pass/fail.

### Phase 3: Learning from Production (Scale with Volume)

Once shipped, users reveal where the product is actually confusing or brittle. Scale your review approach with traffic:

| Volume | Approach | What to Do |
|--------|----------|-------------|
| **1–100 runs/day** | **Stumbles** | Read everything. Build taste and taxonomy. Look for confusion, frustration, near-misses. |
| **100–1,000 runs/day** | **Issues** | Recurring stumbles become trackable problems. Discuss, reproduce, decide whether to fix. |
| **1,000+ runs/day** | **Signals** | Monitor long-term behaviors: aesthetics, refusal quality, tool errors, user frustration. |
| **5,000+ runs/day** | **Experiments** | Ship fixes behind feature flags. Compare Issues and Signals between treatment/control. |

**Self Diagnostics** — Agents can self-report failures via a hidden tool injected into the run. The agent reports missing context, capability gaps, broken tools, or task failures. In practice, self-diagnostics are less useful than they initially seem — they function like Stumbles (a firehose requiring curation). Sensitivity tuning is difficult, and specific wording biases whether the agent reports at all. Treat as a binary classification problem.

### Phase 4: Making Fixes and Changes

**Three tiers of fixes:**

1. **Direct fixes** — Broken tool calls, missing prompt instructions, stale retrieval data. Fix, ship, move on. But guard against bandaids — special-case handling for specific user phrases usually treats symptoms, not causes.

2. **Reproduce → Fix** — For non-trivial issues: reproduce locally, add as golden case, fix, verify eval passes, ship. The pattern: *find in production → reproduce locally → add to evals → fix → verify → ship*.

3. **Experiment in production** — For changes where offline evals can't tell the whole story (model swaps, prompt rewrites, tool configs), run A/B tests on real traffic: *"GPT-5.3 vs Claude 4.5 Sonnet: Treatment 88% completion rate, Control 76%, p<0.001. Promote."*

**⚠️ The eval suite bloat trap** — Every bug → add to eval suite → 500 cases → CI takes 20 minutes → team ignores failures. Ask of each case: Is this a critical path? Could it regress? Representative of a failure class or truly one-off? **20 high-signal cases beats 200 low-signal ones.** If a case hasn't failed in 3 months, question whether it still belongs.

### Phase 5: Rinse, Wash, Repeat

The full evaluation loop:
```
SHIP → WATCH → UNDERSTAND FAILURES → FIX IMPORTANT ONES → KEEP LESSONS AS REGRESSION TESTS → SHIP
```

Each iteration makes the agent less embarrassing and the eval suite more grounded. You are not front-loading all possible test cases — you're building a system that learns from production without forgetting what it learned.

**The Commitment**: Plan to spend **10-20% of agent development time** on evaluation and monitoring — reading traces, tuning signals, investigating issues. Teams that skip this pay the price in production incidents.

## What Stays Constant

Through model improvements, framework changes, and paradigm shifts, five principles hold:

1. **Real user behavior > synthetic evals** — Synthetic test cases diverge from reality.
2. **Trajectory matters** — Whether tool calls (explicit) or reasoning (implicit), how the agent got there is diagnostic.
3. **Golden cases work** — Small sets of high-signal tests beat large sets of low-signal ones.
4. **Production monitoring is essential** — You cannot anticipate all failure modes in advance.
5. **Evaluation is ongoing** — Not a one-time setup. If the loop stops, confidence becomes theater.

## Future: The Collapse of Harnesses

As models become more capable and agentic, the distinction between "model" and "agent" blurs (Claude Code, Cursor CLI, Cursor Agent SDK). When the agent is just a prompt and a model, there is no framework code to instrument, no explicit tool loop to trace.

**Implications for evaluation:**
- Intermediate steps become opaque (like asking a human what they were thinking)
- End-to-end evaluation becomes even more critical
- Golden cases and production monitoring become the **only game in town**
- Verification shifts from inspecting internals to trusting (and verifying) outputs

## Comparison with OpenAI Macro Evals

| Dimension | Floor Raising (Hylak) | Macro Evals (OpenAI) |
|---|---|---|
| **Origin** | Industry practitioner (Raindrop) | OpenAI × Slalom Cookbook |
| **Scope** | Single-agent production reliability | Multi-agent population patterns |
| **Philosophy** | Error analysis; find-and-fix | Clustering; discover-and-prioritize |
| **Key artifact** | Golden cases, Signals, Experiments | BERTopic clusters, 4-label chain |
| **Scale target** | Any agent in production | Multi-agent systems at scale |
| **Tooling** | Raindrop, Raindrop Workshop, vitest-evals | Promptfoo, AgentTrace execution graphs |
| **Complementarity** | Operational: "is my agent reliable?" | Analytical: "what patterns emerge at scale?" |

See [[concepts/evaluation/macro-evals-for-agentic-systems]] for the full macro evals methodology.

## Further Reading

- **Evals are Dead** — Ben Hylak's earlier essay on the state of evaluation
- **Your AI Product Needs Evals** — Hamel Husain (error analysis as highest-ROI activity)
- **Eval Awareness in Claude Opus 4.6** — Anthropic
- **How We Monitor Internal Coding Agents** — OpenAI
- **Macro Evals for Agentic Systems** — OpenAI Cookbook ([[concepts/evaluation/macro-evals-for-agentic-systems]])
- **Raindrop documentation** — https://www.raindrop.ai/docs
