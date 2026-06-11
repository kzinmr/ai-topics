---
title: "Practice Evolution in the Inverted Stack — How TDD, Evals, A/B Testing, Monitoring, and Observability Are Being Redefined"
type: query
created: 2026-05-28
updated: 2026-05-28
tags:
  - methodology
  - evaluation
  - probabilistic-systems
  - comparison
  - survey
  - infrastructure
aliases:
  - practice-evolution
  - eval-practices-portal
  - tdd-evals-monitoring-trajectory
  - practice-evolution-probabilistic-era
related:
  - "[[concepts/inverted-stack-trace-native-engineering]]"
  - "[[concepts/probabilistic-era-software]]"
  - "[[concepts/agent-evaluation-methodology]]"
  - "[[concepts/evals-vs-monitoring-debate]]"
  - "[[concepts/agent-observability-feedback]]"
  - "[[concepts/harness-engineering]]"
  - "[[entities/ben-hylak]]"
  - "[[entities/gian-segato]]"
  - "[[entities/harrison-chase]]"
  - "[[entities/ankur-goyal]]"
  - "[[entities/hamel-husain]]"
---

# Practice Evolution in the Inverted Stack

> **A portal tracking how professional practices are being redefined now that AI has become the primary substrate and code is merely the harness around it.**

> **Historical note:** "Probabilistic" isn't new — classic ML (Zayd Enam, 2016) already dealt with stochastic outputs, 4D debugging, and long feedback cycles. What IS new is the **architectural inversion**: the AI-agent relationship to software has inverted. The model was a component inside deterministic software; now deterministic code is a harness around the AI. Traces have replaced code as the canonical record of system behavior. See [[concepts/inverted-stack-trace-native-engineering|The Inverted Stack]] for the full framework.

This page aggregates wiki knowledge about the ongoing transformation in how practitioners think about and apply quality assurance practices to AI agents. It serves as both a map of the current intellectual landscape and a living index for tracking how these practices evolve.

## The Causal Chain

Three independently-arrived-at perspectives form a unified theory of *why* old practices break and *what* replaces them:

```
┌──────────────────────────┐    ┌───────────────────────────┐    ┌──────────────────────────────┐
│  ONTOLOGICAL SHIFT        │    │  OPERATIONAL SHIFT         │    │  EVALUATIVE SHIFT             │
│  (Segato, Aug 2025)       │ →  │  (Chase, Jan 2026)         │ →  │  (Hylak, Sep 2025/May 2026)   │
│                           │    │                            │    │                               │
│  F: X→Y  becomes  F'(?)   │    │  Code no longer documents  │    │  Evals can't capture           │
│  Input space → infinite    │    │  the app's actual behavior │    │  production truth              │
│  Outputs → stochastic      │    │  → traces are source       │    │  → floor raising via           │
│  Models are discovered,    │    │    of truth for debugging, │    │    production monitoring       │
│  not engineered            │    │    testing, and monitoring │    │    is the answer               │
└──────────────────────────┘    └───────────────────────────┘    └──────────────────────────────┘
```

For the full framework, see [[concepts/probabilistic-era-software]] and [[concepts/agent-observability-feedback#the-three-articles-a-unified-framework]].

---

## Practice-by-Practice: What's Changing

### 1. TDD (Test-Driven Development)

| Classical Era | Classic ML Era (Zayd 2016) | Inverted Stack Era |
|---|---|---|
| Write test → watch it fail → write code → watch it pass | Add model-specific test dimensions (4D debugging) | Cannot write tests before behavior is known |
| Tests document expected behavior deterministically | Tests measure statistical accuracy on held-out data | Expected behavior is a probability distribution; known inputs→known outputs assumption broken |
| Binary pass/fail assertions | Confidence thresholds, precision/recall tradeoffs | Statistical eval; trajectory-based assertions |
| Tests are spec-first; refactoring is safe | Model retraining invalidates test assumptions | "Every new model drop invalidates all assumptions" (Segato) |
| Hallmark of disciplined engineering | ML engineering requires intuition + experimentation | "Actively harmful when applied to AI agents" — pre-spec is impossible |

**Key insight:** TDD assumes bounded input/output spaces. Classic ML stretched this (4D debugging) but still had defined tasks. In the Inverted Stack, the AI *is* the system — you cannot pre-specify behavior, only discover it from production traces.

**Transition path:** TDD → **Eval-Driven Development** (Chase) → **Error Analysis** (Husain) → **Floor Raising** (Hylak). The eval suite becomes "a memory of bugs you refuse to reintroduce," built *after* you discover failures in production, not *before* you write code.

**Wiki pages:**
- [[concepts/ai-evals]] — Hamel Husain's 3-level eval framework
- [[concepts/testing-ai-agents]] — Non-determinism challenges
- [[concepts/evaluation-flywheel]] — OpenAI's continuous improvement cycle

### 2. Evals (Offline Evaluation)

| Classical Era | Classic ML Era (Zayd 2016) | Inverted Stack Era |
|---|---|---|
| Evals = comprehensive test suites | Evals = accuracy on held-out test sets; cross-validation | Evals = adversarially selected known-issue collection |
| Goal: maximize pass rate | Goal: maximize accuracy/F1 on benchmark | Goal: lock in lessons from real failures |
| Large synthetic datasets | Curated benchmark datasets (ImageNet, SQuAD) | Small high-signal golden cases from production traces |
| Static, infrequently updated | Updated with new data; periodic retraining | Continuously sampled from production traces |
| Measures: "does it work?" | Measures: "how accurate is the model?" | Measures: "did I regress on critical paths?"

**Key insight:**

**The 6-definitions problem:** Hylak identified that "eval" has at least 6 meanings — from human-reviewed inputs to frontier model benchmarks — making the debate slippery. The word has become so vague that it obscures decisions rather than clarifying them.

**Transition path:** Synthetic evals → **Code-aware evals** (test the full agent path, not just prompts) → **Trace-based evals** (datasets from production) → **Complementary layers** (offline for regression, online for discovery).

**Wiki pages:**
- [[concepts/evals-vs-monitoring-debate]] — The defining intellectual conflict
- [[concepts/agent-evaluation-methodology]] — Floor raising framework
- [[concepts/macro-evals-for-agentic-systems]] — OpenAI's population-level analysis
- [[concepts/coding-agents/infrastructure-noise-agent-evals]] — Segato on eval reliability
- [[concepts/eval-awareness-browsecomp]] — When models detect they're being evaluated
- [[comparisons/eval-tools-comparison]] — Tool comparison
- [[concepts/ai-evaluation]] — General evaluation landscape

### 3. A/B Testing & Experimentation

| Classical Era | Classic ML Era (Zayd 2016) | Inverted Stack Era |
|---|---|---|
| Funnel optimization (conversion, retention) | A/B test model variants on offline metrics | Trajectory analysis (user paths through possibility fields) |
| Known success metrics | Accuracy/F1 as proxy for success | Success metrics are ambiguous ("better software" = ?) |
| Weeks for significant results | Hours-days per experiment (parallel runs) | Hours via semantic signal comparison |
| Separate from evals and monitoring | Offline evaluation separate from production | Collapses into one holistic feedback system |
| Tools: Optimizely, LaunchDarkly | Tools: ML experiment trackers (W&B, MLflow) | Tools: Raindrop experiments, production signal comparison |

**Key insight:** A/B testing becomes *more* important in the probabilistic era, not less — contra Ankur Goyal's claim. Hylak's rebuttal: "Imagine GPT-5 drops. With Raindrop, you can route 1% of your users to GPT-5 and instantly see how it impacts frustration." The critical distinction: Braintrust's A/B tests measure latency; Raindrop's measure semantic behavior change.

**The success definition problem:** Segato identified the elephant in the room — "real-world live A/B testing assumes you know what to optimize for. In AI products, you basically can't." Longer message chains could mean better software or frustrated debugging. The solution: trajectory-based clustering, not binary metrics.

**Wiki pages:**
- [[concepts/evals-vs-monitoring-debate#claim-3-evals-are-good-for-rapid-iteration]] — Hylak's rebuttal on A/B speed
- [[concepts/probabilistic-era-software#data-is-the-new-operating-system]] — Trajectories over funnels

### 4. Monitoring

| Classical Era | Classic ML Era (Zayd 2016) | Inverted Stack Era |
|---|---|---|
| SLOs: uptime, p99 latency, error rates | Model accuracy drift, data distribution drift | Decision quality, reasoning effectiveness, tool efficiency |
| Catch: 500 errors, null pointers, crashes | Catch: model degradation, concept drift | Catch: silent failures, context loss, infinite loops, hallucinations |
| Tools: Datadog, Sentry, PagerDuty | Tools: ML monitoring (Arize, WhyLabs) | Tools: Raindrop, LangSmith, Arize Phoenix |
| Alert on infrastructure failure | Alert on accuracy degradation | Alert on semantic failure (agent gave wrong info confidently) |
| "Is the system up?" | "Is the model still accurate?" | "Is the agent behaving correctly?" |

**Key insight:** "An agent can be 'up' (0 errors) but still fail" (Chase). Traditional monitoring sees no error when an agent confidently gives wrong information, forgets user context, or takes a suboptimal tool path. The monitoring surface shifts from infrastructure to intelligence.

**Transition path:** Infrastructure monitoring → **Semantic signals** (custom tiny models detecting problematic patterns) → **Self-diagnostics** (agents reporting their own failures) → **Holistic system view** (marketing attribution + observability + A/B testing collapsed into one).

**Wiki pages:**
- [[concepts/agent-observability-feedback]] — The feedback loop
- [[concepts/raindrop]] — "Sentry for AI Agents"
- [[concepts/ai-observability]] — Broader observability landscape

### 5. Observability (o11y)

| Classical Era | Classic ML Era (Zayd 2016) | Inverted Stack Era |
|---|---|---|
| Logs, metrics, traces (the three pillars) | Model metrics dashboard; experiment tracking | Agent traces as the primary artifact |
| Debug by reading code and stack traces | Debug by analyzing loss curves + dev set output | Debug by replaying trace states in playgrounds |
| Observability = ops concern | Observability = data science concern | Observability = the entire development workflow |
| Collaboration on code (GitHub PRs) | Collaboration on experiment results + notebooks | Collaboration on traces (observability platforms) |
| Product analytics and debugging are separate | Product analytics and model metrics are separate | They collapse — user behavior IS agent behavior |

**Key insight:** Chase's thesis — *"In software, the code documents the app; in AI, the traces do."* — is the operational translation of Segato's ontological shift. When decision logic moves from code to the model at runtime, every practice built around code (debugging, testing, profiling, monitoring, collaboration) must be rebuilt around traces.

**You can't set a breakpoint in reasoning.** Traditional breakpoints are meaningless because decisions happen inside the model. Instead: open a trace right before the bad decision, load that exact state into a playground, iterate on prompt/context, and see if the agent makes a better choice.

**Wiki pages:**
- [[concepts/agent-observability-feedback]] — Full feedback loop architecture
- [[concepts/agent-observability]] — Enterprise observability patterns
- [[concepts/observability-monitoring-ai-opentelemetry-python-production]] — OTel-based approach
- [[concepts/observability-monitoring-tracing-opentelemetry-llm-agents-debugging]] — Tracing for LLM agents

---

## Key Thinkers: Positions Map

| Figure | Affiliation | Core Position | Practice Emphasis |
|---|---|---|---|
| **[[entities/gian-segato|Gian Segato]]** | Anthropic (ex-Replit) | Ontological shift: `F→F'` | Engineering → Empiricism |
| **[[entities/ben-hylak|Ben Hylak]]** | Raindrop | Floor raising > benchmark maxxing | Production monitoring > offline evals |
| **[[entities/harrison-chase|Harrison Chase]]** | LangChain | Traces as the new documentation | Both evals + monitoring; feedback loop |
| **[[entities/ankur-goyal|Ankur Goyal]]** | Braintrust | "Evals are the future" | Offline evals as the primary quality tool |
| **[[entities/hamel-husain|Hamel Husain]]** | Independent (Parlance Labs) | "Error analysis is the highest-ROI activity" | Systematic trace analysis; harness engineering |
| **OpenAI** | — | Evaluation Flywheel; Macro Evals | Continuous eval cycle; population-level patterns |
| **Anthropic** | — | Infrastructure noise quantification | Rigorous eval methodology; harness collapse |
| **Sentry** | — | Harness-backed evals (vitest-evals) | Code-aware evals as ordinary software tests |

---

## The Trajectory: Where Practices Are Heading

### Phase 1: Hybrid Coexistence (Current — 2026)
- Teams maintain both eval suites AND production monitoring
- Traces feed eval datasets; evals feed monitoring signals
- Tool consolidation: LangSmith, Raindrop, Braintrust, Arize coexist
- No clear winner in the evals-vs-monitoring debate

### Phase 2: Trace-Centric Consolidation (Emerging)
- Observability platform becomes the IDE of agent development
- Product analytics, debugging, and monitoring collapse into one trace-based system
- "The observability platform becomes as fundamental to agent development as the IDE is to traditional software" (Chase)

### Phase 3: Harness Collapse (Speculative — post-2026)
- As models become more agentic, the harness (framework code) collapses into the model itself
- "When the agent is just a prompt and a model, there is no framework code to instrument" (Hylak)
- End-to-end evaluation becomes the only game in town
- Golden cases and production monitoring are all that remains
- Intermediate steps become opaque — like asking a human what they were thinking

---

## Reading Paths

### Path A: Why Old Practices Break
1. [[concepts/probabilistic-era-software]] — The ontological shift
2. [[concepts/agent-observability-feedback#the-three-articles-a-unified-framework]] — The causal chain
3. [[concepts/evals-vs-monitoring-debate]] — The defining conflict

### Path B: The New Toolbox
1. [[concepts/agent-evaluation-methodology]] — Floor raising framework
2. [[concepts/agent-observability-feedback]] — The feedback loop
3. [[comparisons/eval-tools-comparison]] — Tool comparison

### Path C: Practitioner Perspectives
1. [[entities/ben-hylak]] — Raindrop founder's position
2. [[entities/harrison-chase]] — LangChain CEO's architecture
3. [[entities/gian-segato]] — Anthropic researcher's framework
4. [[entities/ankur-goyal]] — Braintrust CEO's counterpoint
5. [[entities/hamel-husain]] — Error analysis pioneer

### Path D: Technical Deep Dives
1. [[concepts/macro-evals-for-agentic-systems]] — Population-level eval patterns
2. [[concepts/coding-agents/infrastructure-noise-agent-evals]] — Eval reliability quantification
3. [[concepts/eval-awareness-browsecomp]] — Models detecting evaluation
4. [[concepts/testing-ai-agents]] — Non-determinism testing challenges
5. [[concepts/ai-evals]] — Hamel Husain's 3-level framework

---

## Index: All Wiki Pages on This Topic

### Concepts — Eval Practices
- [[concepts/agent-evaluation-methodology]] — Floor raising vs benchmark maxxing
- [[concepts/evals-vs-monitoring-debate]] — Hylak vs Goyal
- [[concepts/probabilistic-era-software]] — The ontological shift
- [[concepts/agent-observability-feedback]] — Feedback loop architecture
- [[concepts/ai-evals]] — Husain's evaluation framework
- [[concepts/ai-evaluation]] — General evaluation landscape
- [[concepts/evaluation-flywheel]] — OpenAI's cycle
- [[concepts/macro-evals-for-agentic-systems]] — Population-level analysis
- [[concepts/coding-agents/infrastructure-noise-agent-evals]] — Eval reliability
- [[concepts/eval-awareness-browsecomp]] — Models detecting evaluation
- [[concepts/testing-ai-agents]] — Non-determinism testing
- [[concepts/evals-for-ai-agents]] — Anthropic's eval guide
- [[concepts/coding-agents/evaluation-coding-agents]] — Coding agent benchmarks
- [[concepts/llm-evaluation-harness]] — lm-eval-harness
- [[concepts/harness-engineering]] — The harness philosophy
- [[concepts/ai-observability]] — Observability landscape
- [[concepts/agent-observability]] — Enterprise observability

### Comparisons
- [[comparisons/eval-tools-comparison]] — Eval tools compared
- [[comparisons/eval-tools-comparison]] — Major platform comparison
- [[comparisons/agent-orchestration-frameworks]] — Framework landscape

### Entities
- [[entities/ben-hylak]] — Raindrop co-founder
- [[entities/harrison-chase]] — LangChain CEO
- [[entities/gian-segato]] — Anthropic research, ex-Replit
- [[entities/ankur-goyal]] — Braintrust CEO
- [[entities/hamel-husain]] — Error analysis pioneer
- [[entities/langchain]] — LangChain platform
- [[concepts/raindrop]] — Raindrop monitoring platform

### Raw Articles
- raw/articles/2025-08_gian-segato_probabilistic-era.md
- raw/articles/2025-09-05_ben-hylak_thoughts-on-evals.md
- raw/articles/2026-01-10_harrison-chase_code-documents-app-traces-do.md
- raw/articles/2026-05-28_ben-hylak_how-to-eval-ai-agents.md
- raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
- raw/articles/2026-05-08_anthropic-engineering_infrastructure-noise.md
