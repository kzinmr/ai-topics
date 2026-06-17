---
title: "Agent Evaluation Methodology — Floor Raising vs Benchmark Maxxing"
type: concept
created: 2026-05-28
updated: 2026-06-17
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
  - raw/articles/leehanchung.github.io--blogs-2026-06-13-hidden-technical-debt-agent-evaluation-infr--f05320f3.md
  - https://leehanchung.github.io/blogs/2026/06/13/hidden-technical-debt-agent-evaluation-infra/
related:
  - "[[concepts/evaluation/macro-evals-for-agentic-systems]]"
  - "[[concepts/evaluation/raindrop]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/ai-observability]]"
  - "[[entities/ben-hylak]]"
  - "[[entities/hamel-husain]]"
  - "[[entities/lee-han-chung]]"
---

# Agent Evaluation Methodology — Floor Raising vs Benchmark Maxxing

A practical, opinionated framework for evaluating AI agents in production. Developed by **Ben Hylak** (founder of [[concepts/evaluation/raindrop|Raindrop]]) and shaped by work with Framer, Clay, Vercel, and GC.AI. The core thesis: most teams should be **floor raising** (making their agent reliable where it matters), not **benchmark maxxing** (chasing abstract pass rates).

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

## Lee Han-chung: Agent Evaluation Infrastructure as Technical Debt

A framework by **Lee Han-chung** (Han, Not Solo) that reframes agent evaluation as a durable infrastructure layer — the part that outlives model updates, harness rewrites, and runtime refactors. Drawing on reinforcement learning abstractions, the core thesis is that agent evaluation looks less like a metric library and more like an **experimental control plane**.

> "Agents need worlds. Agentic evaluation infra needs multiverses." — Lee Han-chung

### The RL 5-Tuple: Eval Infrastructure as Control Plane

Lee formalizes the evaluation infrastructure as an extended RL 5-tuple:

\[
I_{eval} = \{T, A, M, S, C, R, \tau\}
\]

| Component | Meaning |
|-----------|---------|
| **T** | Task suites, task distributions, verifiers, rubrics, judges, human review |
| **A** | Harness — the scaffolding that wraps the agent loop |
| **M** | Model |
| **S** | Initial state, checkpoints, memory, state deltas |
| **C** | Configuration — skills, tools, stopping rules, token budgets |
| **R** | Runtime — sandbox, execution environment |
| **τ** | Trace schema and trace store |

The purpose of this system is to produce a **data-driven decision** for next steps: ship, rollback, retrain, change harness, fix runtime, or curate more tasks. This framing turns evaluation into a normalized, auditable, replayable experiment record.

### From Spreadsheet to System

Evaluating a single-turn chat assistant fits in a spreadsheet: prompt, response, label, score. Agentic systems break every assumption:

| Concern | Single-turn chat eval | Agentic system eval |
|---------|----------------------|---------------------|
| **Unit of work** | Prompt and response | Episode and trajectory |
| **Main artifact** | Output text | Output, trace, state delta |
| **Failure modes** | The final answer | Any step in the rollout |
| **Environment** | Static prompt set | Mutable runtime, tools, memory |
| **Verification** | Score the answer | Score outcome, process, and state |
| **Reproducibility** | Seed and prompt | Seed, state, runtime, tools, memory, clocks, APIs |
| **Cost** | Inference tokens | Inference, tools, runtime, human review |
| **Safety** | A bad answer | A bad action |

### Rollouts, Episodes, Traces

Key vocabulary for agent evaluation:

- **Episode** — A bounded attempt from initial state to terminal condition
- **Rollout** (or **trajectory**) — Running the agent through one episode
- **Trace** — The recorded observability artifact: messages, tool calls, state changes, latency, cost

A single aggregated score provides very sparse reward signal. Lee argues that final-output-only evals are insufficient because **agents change the environment**. A coding agent may end with a patch that passes tests, but the trace might show it deleted tests it couldn't pass, removed unrelated files, leaked a token, or looped on the same failing command. The trace is what lets you evaluate process — not just outcome.

### Five Evaluation Surfaces

Lee identifies five surfaces for evaluating agent behaviors:

1. **Output** — Did the agent complete the task? Verifiable tasks (math, coding) vs open-ended tasks (analysis, research). Use rubrics and matrices rather than single scores.
2. **Trace** — Process questions: Did the agent use the right tools? Retry failing calls? Inspect files before editing? Validate after changes? A minimal trace record includes run id, task id, step index, model/harness version, tool calls with argument/observation hashes, latency, cost, state delta pointer, checkpoint id, verifier result, and failure labels.
3. **Memory** — Conversation context, scratchpads, skills files, vector-store entries. Memory pollution changes agent behavior silently — a bad episode becomes a durable preference (analogous to the YouTube dark hole of recommendation systems).
4. **Environment** — State deltas at each step: files added/deleted, DB rows updated, git refs changed, secrets accessed. Capturing per-step state deltas makes failure attribution possible.
5. **Mechanistic interpretability** — Sparse autoencoders, transcoders, cross-layer transcoders. Not available to teams using proprietary API endpoints; for most builders, extrinsic trace/state instrumentation must be comprehensive.

### Experimentation, Not Benchmarking

A benchmark is a frozen environment. Agent evaluation infrastructure should be **experimentation-driven**: treat every change (new model, reworded prompt, added tool) as a hypothesis and each eval run as a controlled experiment.

**Perturbation tests** — Hold the task fixed, vary the paths available to the agent (turn limit, skills.md, tool failure rates, stale conflicting docs). A performance change isolates whether the agent learned the task or just memorized one golden path.

**Ablation tests** — Remove one component at a time and measure the delta: long-term memory, semantic search, browser access, sub-agents, agent skills. If removing memory barely moves the score, the memory layer is theater.

**Guardrail tests** — Inject tool errors, increase response latency, revoke a permission mid-run, and watch whether the agent recovers or fails closed.

**Decouple task from harness** — What you measure (dataset, answer contract, scorer) must be a separate object from how you run it (model, tools, harness, sandbox). Otherwise a model change and a harness change land in the same number and you cannot tell which one moved it.

### Checkpoints, Branches, and Replay

Long-horizon agent evals need checkpointing for the same reason game engines need state snapshots — re-running from the beginning is too expensive and hides variance. A checkpoint must include: filesystem state, conversation state, retrieved memories, tool observations, model/harness version, random seeds, clocks, package versions, database state, network fixtures.

Three operations:

| Operation | Purpose |
|-----------|---------|
| **Resume** | Continue the same attempt from a checkpoint under the same configuration |
| **Replay** | Inspect or re-execute a known trajectory from a known state |
| **Branch** | Start from the same checkpoint but change one factor: model, harness, memory, tool availability, budget, or verifier |

Branching enables targeted experiments: "Same state, new model — did the upgrade help?" / "Same state, memory disabled — is memory helping or poisoning?" This is the practical version of experience replay for agent systems.

### State Infrastructure Is Evaluation Infrastructure

In productivity tasks, agents live in filesystems and databases. Evaluation infrastructure must include state infrastructure:

- **Filesystems**: git worktrees, copy-on-write directories, overlay filesystems, container layers, VM snapshots
- **Databases**: transaction snapshots, logical dumps, branchable databases, seeded fixtures
- **Browser agents**: profiles, cookies, local storage, network recordings, DOM snapshots
- **Enterprise agents**: branchable mock systems with access controls

> "Agents need worlds. Agentic evaluation infra needs multiverses."

### Evaluation Debt

Lee introduces **evaluation debt** as the accumulated cost of convenience infrastructure. Warning signs include:

- Notebooks with CSV task sets and judge prompts in a shared Excel file
- A model router with an ever-changing tool schema
- Production runtime that is "basically the same" as eval runtime
- Failures pasted into Slack as screenshots
- A green dashboard nobody can trace back to the run that produced it

The bill comes due at the next model upgrade: aggregate score improves, dashboard stays green, yet customers report the agent got worse — and the team cannot reproduce the regression because production ran with different memory state, tool timeout, browser profile, and system prompt than the eval ever saw.

A durable evaluation layer can: identify which slice regressed, attribute the cause to the right component (model, harness, runtime, memory, verifier, or state), distinguish the agent failing the task from the scorer failing the agent, replay the failure, promote it into the regression suite, and tie the outcome to a ship/rollback/retrain decision.

### Contrast with Floor Raising

| Dimension | Floor Raising (Hylak) | Eval Infrastructure (Lee) |
|-----------|----------------------|---------------------------|
| **Focus** | Error analysis; find and fix specific failures | Build the durable measurement system itself |
| **Core artifact** | Golden cases, Signals, Experiments | RL 5-tuple, traces, checkpoints, state deltas |
| **Evaluation model** | Detective work on production traces | Controlled experiments with perturb/ablate/branch |
| **Primary concern** | "Which 1% of failures matter?" | "Can I reproduce, attribute, and replay?" |
| **Debt** | Eval suite bloat (too many low-signal cases) | Infrastructure debt (convenience systems that aren't reproducible) |
| **Complementarity** | Operational methodology for finding what to fix | Infrastructure framework for building how to measure |

## Further Reading

- **Evals are Dead** — Ben Hylak's earlier essay on the state of evaluation
- **Your AI Product Needs Evals** — Hamel Husain (error analysis as highest-ROI activity)
- **Eval Awareness in Claude Opus 4.6** — Anthropic
- **How We Monitor Internal Coding Agents** — OpenAI
- **Macro Evals for Agentic Systems** — OpenAI Cookbook ([[concepts/evaluation/macro-evals-for-agentic-systems]])
- **Raindrop documentation** — https://www.raindrop.ai/docs
