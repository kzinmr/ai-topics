---
title: "Self-Evolving Agents"
tags:
  - self-improving
  - coding-agents
  - harness-engineering
  - architecture
created: 2026-04-13
updated: 2026-05-28
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


## Related

- [[concepts/agents-that-build-themselves]] — Agents That Build Themselves (concrete implementation of Level 5)
- [[concepts/memory-systems-design-patterns]] — Memory Systems Design Patterns
- [[concepts/agent-team-swarm/agent-team-swarm]] — Agent Team / Swarm
- [[concepts/harness-engineering]] — Harness Engineering
- [[concepts/evaluation-flywheel]] — Evaluation Flywheel
- [[entities/ivan-leo]] — Ivan Leo (co-creator of self-extending agent workshop)
- [[entities/pi]] — Pi coding agent — concrete implementation of Level 5 self-modification with session trees, hot reload, extension state
- [[entities/openclaw]] — OpenClaw — always-on self-evolving agent with markdown memory compaction
- [[concepts/hermes-agent-architecture]] — Hermes Agent — capability accumulation system that grows stronger over time through skill/memory accumulation
