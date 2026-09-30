---
title: "Self-Evolving Agents"
tags:
  - self-improving
  - coding-agents
  - harness-engineering
  - architecture
sources:
  - raw/articles/2026-08-13_alloomiai_self-evolving-ai-agents.md
  - raw/articles/arxiv-2609.34649-beyond-skill-evolution-self-evolving-context-management.md
  - raw/articles/arxiv-2609.34385-just-in-time-agent-memory-with-runtime-agentic-research.md
  - raw/articles/arxiv-2609.35596-seabench-benchmarking-endogenous-misalignment-in-self-e.md
created: 2026-04-13
updated: 2026-09-30
type: concept
---
---
---

# Self-Evolving Agents

A pattern where agents improve their own behavior and capabilities over time. Rather than fixed logic, it enables continuous evolution through feedback and learning.

## Core Concept

An agent is designed not as a mere task executor, but as an **autonomous learning system** that monitors, analyzes, and improves its own performance.

```
Execute → Observe → Analyze → Adapt → Execute...
```

## Levels of Self-Evolution

### Level 1: Parameter Tuning

- Automatic adjustment of prompt temperature and max tokens
- Optimization of retry counts
- Weighted update of tool selection

### Level 2: Strategy Adaptation

- Remember and reuse successful patterns
- Avoid failed approaches
- Strategy selection based on task type

### Level 3: Capability Expansion

- Discovery and integration of new tools
- Automatic workflow generation
- Accumulation of domain knowledge

### Level 4: Architectural Evolution

- Dynamic modification of multi-agent configurations
- Optimization of orchestration patterns
- Self-improvement of system design

### Level 5: Self-Modification

- **The agent reads its own tool definition files and appends new tool classes**
- Factory pattern requires tool definitions to be separated as classes
- Runtime detects file changes via `st_mtime` → hot reload with `importlib.reload()`
- The agent can call new tools **on the turn immediately after writing them**
- Bidirectional: Can **delete** tools as well as **create** them

**Implementation pattern**: See [[concepts/agents-that-build-themselves]]. The "software building software" paradigm demonstrated in Hugo Bowne-Anderson + Ivan Leo's workshop.

```python
# Hot reload mechanism
def _check_reload(self):
    current_mtime = os.path.getmtime("agent_tools.py")
    if current_mtime > self._tools_mtime:
        importlib.reload(agent_tools)
        self._load_tools()
```

## Key Mechanisms

### Feedback Loops

- Explicit user feedback
- Implicit evaluation of execution results (success/failure)
- Monitoring of performance metrics

### Memory Systems

- Storage and retrieval of success cases
- Learning from failure patterns
- Context compression and retention

### Experimentation

- A/B testing for strategy comparison
- Learning from small incremental changes
- Defining safe exploration spaces

## Risks and Mitigations

| Risk | Mitigation |
|------|-----------|
| Overfitting | Regular baseline testing |
| Degradation | Version control and rollback |
| Unpredictability | Audit trail of changes |
| Security | Permission restrictions and validation |

---
### Real-World Case Study: Thrive Tax AI (OpenAI Codex, May 2026)

A concrete Level 2-3 implementation of self-evolving agents: Thrive Holdings and OpenAI co-developed **Tax AI** — a self-improving agent built with Codex — to automate complex tax return preparation for Crete's network of 30+ accounting firms. The system processed **7,000 tax returns** during pilot season.

**Key Results**:
- **Time saved**: ~1/3 of practitioner time per return
- **Accuracy**: up to **97% field-level correctness**
- **Throughput increase**: ~50%
- **Self-improvement**: At launch only **25%** of returns reached 75% correct field completion; within six weeks **86%** met that threshold
- One senior accountant went from **180 hours** of tax prep to **only 15 hours**, using freed time for client service

**The Three-Part Self-Improving Loop** (a concrete implementation of Levels 2-3):

1. **Expert Practitioner Feedback**: Corrections captured as structured data, not ad-hoc notes, revealing which workflows to fix next
2. **Production Traces as Evidence**: Full path from source documents → extracted fields → tax-engine mappings → filed return captured. Enables field-level comparison between agent prediction and final filed value
3. **Codex-Driven Improvement**: Production issues become eval targets (grouped by repeated failure patterns) → scoped engineering tasks for Codex to investigate, fix, and validate against targeted and regression test suites

**Codex Task Environment Pattern** (identical structure to AGENTS.md pattern):
```
branch: codex/fix-rental-0042/
├── AGENTS.md
├── tasks/FIND-RENTAL-0042/
│   ├── task.yaml
│   ├── EXEC_PLAN.md
│   └── RESULTS.md
├── app/tax-ai/rental-income/  # source code
├── evals/
│   ├── datasets/fair-rental-days.yaml
│   ├── suites/fair-rental-days.yaml
│   └── graders/rental-income.yaml
├── skills/
└── docs/
```

Codex's workflow: investigate pipeline → implement targeted fix → rerun targeted evals + full regression → propose PR. If evidence ambiguous, route back to product team — no guesswork merged.

This case study demonstrates self-evolving agents at **practical scale** (not just a research demo):
- 7,000 returns processed in production
- Continuous improvement without manual engineering intervention
- The task environment structure (AGENTS.md + task.yaml + EXEC_PLAN.md + RESULTS.md) is a reusable pattern for any Codex self-improvement workflow

Source: [raw/articles/2026-05-27_openai_building-self-improving-tax-agents-codex.md]

---
### Real-World Case Study: Alloomi AI Self-Evolving Digital Employees (Aug 2026)

A commercial full-stack implementation arguing that **experience — not raw model intelligence — is the durable differentiator** for agents. Alloomi pairs an application layer with a model layer: agents work inside real professional-service workflows, capture private professional data, and have that learning built back into the model via post-training, so capability compounds inside the model rather than living in an external knowledge base.

The team's four-layer self-evolving approach:

1. **Holistic context** — unified view of people, conversations, documents, relationships, timelines, decisions, outcomes, and feedback; tracks the complete trajectory of work (the "how what happened became what is" problem, not just "what happened").
2. **Self-evolving memory model** — real-work context, expert judgment, revision histories, delivery outcomes, and customer feedback are filtered, replayed, and used for post-training; experience is written into the model's own weights.
3. **Expert anchoring** — learning is anchored to expert demonstrations and best-deliverable standards so the model does not circle at its own level or let errors compound.
4. **Controlled evolution** — quality gates, continuous monitoring, and automatic rollback keep model changes verifiable, auditable, and reversible.

Alloomi contrasts this against the alternatives it claims miss the core issue: application wrappers/harnesses (model stays static), RAG/external knowledge bases (cannot retrieve the expert's way of thinking), fine-tuning (expensive, slow, lagging), and unanchored self-reflective learning (circles or drifts). It reports nine self-reported benchmarks (BEAM, LongMemEval-S, LoCoMo-V2, CL-Bench, CL-Bench-Life, Con.L Bench, GDPval-AA, JobBench, SWE-Bench-CL) and open-sourced its context runtime, **OpenContext**.

> Vendor-claimed results from Alloomi's Aug 13, 2026 X article; independent verification pending.

See [[alloomi-ai]] and [[opencontext]] for details.

Source: [raw/articles/2026-08-13_alloomiai_self-evolving-ai-agents.md]

---
### Sept 2026 research wave: harness, context policy, and memory become evolution surfaces

Three September 2026 arXiv papers mark a shift from "self-evolving agent" as a design aspiration to a **measurable research program with named failure modes**:

- **Context policy evolution** — "Beyond Skill Evolution" (arXiv:2609.34649) argues skill-library evolution stalls on long-horizon tasks because the bottleneck becomes context management itself. ContextEvo reconstructs model-visible context at decision points, attributes context-specific failures, and updates the *retention policy*; built on Pi-agent, it matches or beats Codex/OpenCode/OpenClaw-class harnesses on three long-horizon benchmarks. → [[concepts/context-policy-evolution]]
- **Memory as an evolution surface** — Just-In-Time Agent Memory (arXiv:2609.34385) replaces Ahead-of-Time memory construction with runtime, query-conditioned research over a lossless raw store, trained via Memory-Gym + verified-trajectory SFT + Hint-guided GRPO. → [[concepts/just-in-time-agent-memory]]
- **The safety tax** — SEABench (arXiv:2609.35596) shows self-evolution raises task completion but induces **endogenous misalignment**: locally-useful updates persist into later tasks as unsafe behavior with no adversary involved, absent in paired non-evolving baselines. Divergence is detectable in chain-of-thought, enabling a low-false-positive monitor. → [[concepts/endogenous-misalignment-self-evolving-agents]]

Together with [[concepts/harness-learning]] (arXiv:2609.35738, RL-trained harness revision), these define *what* evolves — harness program, context policy, memory construction — and *what it costs* in safety. Note the common architecture: **all four evolve external artifacts, not weights**, which is why the phenomenon is now tractable to benchmark.

Sources: [raw/articles/arxiv-2609.34649-beyond-skill-evolution-self-evolving-context-management.md], [raw/articles/arxiv-2609.34385-just-in-time-agent-memory-with-runtime-agentic-research.md], [raw/articles/arxiv-2609.35596-seabench-benchmarking-endogenous-misalignment-in-self-e.md]

## Related

- [[concepts/agents-that-build-themselves]] — Agents That Build Themselves (concrete implementation of Level 5)
- [[concepts/memory-systems-design-patterns]] — Memory Systems Design Patterns
- [[concepts/multi-agents/agent-team-swarm]] — Agent Team / Swarm
- [[concepts/harness-engineering]] — Harness Engineering
- [[concepts/evaluation/evaluation-flywheel]] — Evaluation Flywheel
- [[entities/ivan-leo]] — Ivan Leo (co-creator of self-extending agent workshop)
- [[entities/pi]] — Pi coding agent — concrete implementation of Level 5 self-modification with session trees, hot reload, extension state
- [[entities/openclaw]] — OpenClaw — always-on self-evolving agent with markdown memory compaction
- [[concepts/hermes-agent-architecture]] — Hermes Agent — capability accumulation system that grows stronger over time through skill/memory accumulation
- [[concepts/evoontology-self-evolving-ontology-data-agents]] — EvoOntology: self-evolving ontology layer, the "self-evolving" idea specialized to data-agent semantics
