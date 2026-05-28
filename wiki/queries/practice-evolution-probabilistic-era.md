---
title: "Practice Evolution in the Probabilistic Era — TDD, Evals, A/B Testing, Monitoring, Observability"
type: query
created: 2026-05-28
updated: 2026-05-28
tags:
  - methodology
  - agent-evaluation
  - probabilistic-systems
  - comparison
  - survey
  - reliability
aliases:
  - practice-evolution
  - eval-practices-portal
  - tdd-evals-monitoring-trajectory
related:
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

# Practice Evolution in the Probabilistic Era

> **A portal tracking how professional practices — TDD, evals, A/B testing, monitoring, observability — are being redefined as software shifts from deterministic to probabilistic.**

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

| Classical Era | Probabilistic Era |
|---|---|
| Write test → watch it fail → write code → watch it pass | Cannot write tests before behavior is known |
| Tests document expected behavior deterministically | Expected behavior is a probability distribution |
| Binary pass/fail assertions | Statistical evaluation; trajectory-based analysis |
| Tests are spec-first; refactoring is safe | "Every new model drop invalidates all assumptions" (Segato) |
| Hallmark of disciplined engineering | "Actively harmful when applied to AI agents" (Segato) |

**Key insight:** TDD assumes you know the input space *X* and output space *Y* beforehand. With AI agents, both are unbounded. "Not knowing the full scope of what you want ahead of time" — the classic critique of TDD — applies perfectly to agent development.

**Transition path:** TDD → **Eval-Driven Development** (Chase) → **Error Analysis** (Husain) → **Floor Raising** (Hylak). The eval suite becomes "a memory of bugs you refuse to reintroduce," built *after* you discover failures in production, not *before* you write code.

**Wiki pages:**
- [[concepts/ai-evals]] — Hamel Husain's 3-level eval framework
- [[concepts/testing-ai-agents]] — Non-determinism challenges
- [[concepts/evaluation-flywheel]] — OpenAI's continuous improvement cycle

### 2. Evals (Offline Evaluation)

| Classical Era | Probabilistic Era |
|---|---|
| Evals = comprehensive test suites | Evals = adversarially selected known-issue collection |
| Goal: maximize pass rate | Goal: lock in lessons from real failures |
| Large synthetic datasets | Small high-signal golden cases |
| Static, infrequently updated | Continuously sampled from production traces |
| Measures: "how good is my product?" | Measures: "did I regress on critical paths?" |

**Key insight:** The "evals are dead" debate (see [[concepts/evals-vs-monitoring-debate]]) is not about killing evals — it's about their proper scope. Chase (LangChain) bridges the positions: evals and production monitoring are complementary layers in the agent improvement loop.

**The 6-definitions problem:** Hylak identified that "eval" has at least 6 meanings — from human-reviewed inputs to frontier model benchmarks — making the debate slippery. The word has become so vague that it obscures decisions rather than clarifying them.

**Transition path:** Synthetic evals → **Code-aware evals** (test the full agent path, not just prompts) → **Trace-based evals** (datasets from production) → **Complementary layers** (offline for regression, online for discovery).

**Wiki pages:**
- [[concepts/evals-vs-monitoring-debate]] — The defining intellectual conflict
- [[concepts/agent-evaluation-methodology]] — Floor raising framework
- [[concepts/macro-evals-for-agentic-systems]] — OpenAI's population-level analysis
- [[concepts/infrastructure-noise-agent-evals]] — Segato on eval reliability
- [[concepts/eval-awareness-browsecomp]] — When models detect they're being evaluated
- [[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]] — Tool comparison
- [[concepts/ai-evaluation]] — General evaluation landscape

### 3. A/B Testing & Experimentation

| Classical Era | Probabilistic Era |
|---|---|
| Funnel optimization (conversion, retention) | Trajectory analysis (user paths through possibility fields) |
| Known success metrics | Success metrics are ambiguous ("better software" = ?) |
| Weeks for statistically significant results | Hours via semantic signal comparison |
| Separate from evals and monitoring | Collapses into one holistic feedback system |
| Tools: Optimizely, LaunchDarkly | Tools: Raindrop experiments, production signal comparison |

**Key insight:** A/B testing becomes *more* important in the probabilistic era, not less — contra Ankur Goyal's claim. Hylak's rebuttal: "Imagine GPT-5 drops. With Raindrop, you can route 1% of your users to GPT-5 and instantly see how it impacts frustration." The critical distinction: Braintrust's A/B tests measure latency; Raindrop's measure semantic behavior change.

**The success definition problem:** Segato identified the elephant in the room — "real-world live A/B testing assumes you know what to optimize for. In AI products, you basically can't." Longer message chains could mean better software or frustrated debugging. The solution: trajectory-based clustering, not binary metrics.

**Wiki pages:**
- [[concepts/evals-vs-monitoring-debate#claim-3-evals-are-good-for-rapid-iteration]] — Hylak's rebuttal on A/B speed
- [[concepts/probabilistic-era-software#data-is-the-new-operating-system]] — Trajectories over funnels

### 4. Monitoring

| Classical Era | Probabilistic Era |
|---|---|
| SLOs: uptime, p99 latency, error rates | Decision quality, reasoning effectiveness, tool efficiency |
| Catch: 500 errors, null pointers, crashes | Catch: silent failures, context loss, infinite loops, hallucinations |
| Tools: Datadog, Sentry, PagerDuty | Tools: Raindrop, LangSmith, Arize Phoenix |
| Alert on infrastructure failure | Alert on semantic failure (agent gave wrong info confidently) |
| "Is the system up?" | "Is the agent behaving correctly?" |

**Key insight:** "An agent can be 'up' (0 errors) but still fail" (Chase). Traditional monitoring sees no error when an agent confidently gives wrong information, forgets user context, or takes a suboptimal tool path. The monitoring surface shifts from infrastructure to intelligence.

**Transition path:** Infrastructure monitoring → **Semantic signals** (custom tiny models detecting problematic patterns) → **Self-diagnostics** (agents reporting their own failures) → **Holistic system view** (marketing attribution + observability + A/B testing collapsed into one).

**Wiki pages:**
- [[concepts/agent-observability-feedback]] — The feedback loop
- [[concepts/raindrop]] — "Sentry for AI Agents"
- [[concepts/ai-observability]] — Broader observability landscape

### 5. Observability (o11y)

| Classical Era | Probabilistic Era |
|---|---|
| Logs, metrics, traces (the three pillars) | Agent traces as the primary artifact |
| Debug by reading code and stack traces | Debug by replaying trace states in playgrounds |
| Observability = ops concern | Observability = the entire development workflow |
| Collaboration on code (GitHub PRs) | Collaboration on traces (observability platforms) |
| Product analytics and debugging are separate | They collapse — user behavior IS agent behavior |

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
3. [[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]] — Tool comparison

### Path C: Practitioner Perspectives
1. [[entities/ben-hylak]] — Raindrop founder's position
2. [[entities/harrison-chase]] — LangChain CEO's architecture
3. [[entities/gian-segato]] — Anthropic researcher's framework
4. [[entities/ankur-goyal]] — Braintrust CEO's counterpoint
5. [[entities/hamel-husain]] — Error analysis pioneer

### Path D: Technical Deep Dives
1. [[concepts/macro-evals-for-agentic-systems]] — Population-level eval patterns
2. [[concepts/infrastructure-noise-agent-evals]] — Eval reliability quantification
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
- [[concepts/infrastructure-noise-agent-evals]] — Eval reliability
- [[concepts/eval-awareness-browsecomp]] — Models detecting evaluation
- [[concepts/testing-ai-agents]] — Non-determinism testing
- [[concepts/evals-for-ai-agents]] — Anthropic's eval guide
- [[concepts/evaluation-coding-agents]] — Coding agent benchmarks
- [[concepts/llm-evaluation-harness]] — lm-eval-harness
- [[concepts/harness-engineering]] — The harness philosophy
- [[concepts/ai-observability]] — Observability landscape
- [[concepts/agent-observability]] — Enterprise observability

### Comparisons
- [[comparisons/eval-tools-comparison]] — Eval tools compared
- [[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]] — Major platform comparison
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
