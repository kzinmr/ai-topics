---
title: Agent Operator Patterns
created: 2026-05-20
updated: 2026-05-20
type: concept
tags:
  - ai-agents
  - agent-architecture
  - agent-ergonomics
  - orchestration
  - hermes-agent
  - governance
  - methodology
  - durable-execution
  - multi-agent
  - design-patterns
sources:
  - raw/articles/2026-05-15_shann_hermes-agent-operator.md
related:
  - "[[entities/shannhk]]"
  - "[[entities/hermes-agent]]"
  - "[[comparisons/hermes-vs-openclaw]]"
---

# Agent Operator Patterns

**Agent Operator Patterns** is a collection of design patterns and best practices for **operating, managing, and extending** autonomous AI agents. The pattern set systematized by Shann Holmberg (@shannhk) in "How to Become a Hermes Agent Operator" provides a practical framework for scaling from a single agent to a full agent fleet.

## Core Mental Model (4-Element Model)

Shann's operating model consists of 4 elements:

```
┌───────┐
│  YOU  │   the operator
└───┬───┘
    │
    ├── control path ────► Agent Control Room (management, config, docs)
    ├── direct path  ────► Specialist Agent (direct interaction, fastest)
    └── orchestrated ────► Orchestrator → Task Bus → Specialists (composition, distribution)
```

| Element | Role | Access Method |
|---|---|---|
| **You (Operator)** | Final decision-maker, direct access to all elements | All paths |
| **Agent Control Room** | Fleet-wide documentation, configuration, governance. Not a place to chat | Filesystem (`/root/vps-agents/`) |
| **Hermes Agents (Workers)** | Specialists performing actual work. Own brain/personality/skillset | Chat + cron |
| **Agent Task Bus (Optional)** | Task relay between Orchestrator ⇔ Specialists (Level 3+) | Orchestrator reads/writes |

## Pattern 1: Control Room (Side Control Plane)

### Principle
> "The control room is the brain that defines the system. The live runtime is the body that runs it. You can rebuild the body from the brain. You cannot rebuild the brain from the body."

The Control Room is a **management layer (brain) separated from the agent runtime (body)**.

```
/root/vps-agents/          → Control Room: docs, rules, runbooks, architecture
   README.md
   CLAUDE.md
   agents/<agent-name>/
     inventory.md           ← Agent inventory: what, where, how it runs
     docker.md              ← Docker configuration
     env-map.md             ← Referenced credentials/env vars (no raw secrets)
     runbook.md             ← Restart, log check, incident response procedures
     backup.md              ← Backup procedures
   shared/
     security.md            ← Common security rules
     commands.md            ← Common command set
   api-keys-sop.md          ← API key management SOP
   orchestrator-and-fleet-skills.md

/srv/<agent-name>/data/     → Live Runtime: secrets, memory, skills, sessions, crons
```

**Storage Split Value**:
- Git-manage the Brain (Control Room) and the entire body can be rebuilt
- No raw secrets ever in the Brain
- New operators can grasp the whole system by reading the Control Room

### Application to Wiki Management System

The current wiki management system consists of 27 cron jobs and 28 scripts, but the pipeline overview is scattered across AGENTS.md and skills. Applying the Control Room pattern:

```
~/wiki/control-room/
  README.md                    ← System overview, architecture diagram
  inventory.md                 ← All cron jobs, pipelines, scripts
  agents/
    hermes-wiki/
      runbook.md               ← Restart, log check, troubleshooting
      env-map.md               ← Referenced credentials (no real values)
  pipelines/
    newsletter-ingest.md
    blog-ingest.md
    x-bookmarks.md
    x-accounts-scan.md
    raw-backlog.md
    daily-report.md
    dreaming.md
    wiki-health.md
  shared/
    naming-conventions.md      ← Filename conventions, frontmatter conventions
    quality-standards.md       ← Entity page quality standards
    troubleshooting.md         ← Common issues and solutions
```

## Pattern 2: Brain Layers (Context Layering)

### Principle
> "The layers are not decoration. They are the reason the agent does not lose context as the work gets specialized. The company brain stays stable while the worker iterates. The brain layers make the worker disposable."

Shann's SEO agent's 5-layer structure:

```
Company Brain (stable)    ← vision, brand, audience, products
    ↓
Orchestrator            ← routing only
    ↓
SEO Brain (semi-stable)  ← ranking playbook, voice rules, content formats, style guide
    ↓
3 Sub-agents (variable):
  Research + Ideate      ← keyword seed, SERP, competitor extraction, gap analysis
  Production             ← angle brief, outline, draft, image gen, QA
  Distribution           ← publish prep, schema, internal linking, syndication, monitoring
```

**Key Point**: Company Brain and SEO Brain are stable; Sub-agents (workers) are disposable. Context is not lost because upper-layer Brains absorb lower-layer iteration.

### Application to Wiki Management System

Current Hermes memory has all context packed flat. Introducing Brain Layers:

| Layer | Content | Change Frequency |
|---|---|---|
| **Wiki Brain (stable)** | Wiki purpose, coverage range, quality standards, SCHEMA definitions | Very low |
| **Pipeline Brain (semi-stable)** | Per-pipeline specific knowledge (processing rules, judgment criteria) | Only at pipeline addition |
| **Session Context (temporary)** | Specific content of articles/papers being processed | Per session |

## Pattern 3: Agent Creation Heuristics

### Principle
> "Needs its own credentials → new agent. Needs its own long-term memory → new agent. Ongoing repeated work that is a separate role → new agent. Otherwise stay with what you have."

**Anti-pattern**: Stuffing all credentials and memory into one "mega-agent." Isolation is lost, access revocation becomes difficult, the agent gets confused about which voice to use.

## Pattern 4: 4-Level Fleet Operation Model

| Level | Configuration | Suitable For | Required Skills |
|---|---|---|---|
| **1: One Agent** | Single Hermes + Control Room (optional) | Initial setup, personal assistant | SOUL.md, MEMORY.md, USER.md |
| **2: Direct Specialists** | Multiple specialists, direct interaction, no Orchestrator | Role separation validation, credential scope separation | Docker, SSH, Control Room folder |
| **3: Orchestrator + Specialists** | Orchestrator as front door, + Task Bus | Cross-functional workflows, delegation and composition | Above + orchestrator skills |
| **4: Automated Agent Team** | Level 3 + cron + automated workflows | Weekly reports, health checks, recurring tasks | Above + cron design, monitoring |

**Level 2→3 Transition Judgment**: Don't introduce an Orchestrator until Specialists have proven useful through direct use. "Don't build an Orchestrator for agents you're not sure are useful yet."

## Pattern 5: Prototype → Production Methodology

Shann's 4-step process applied to every marketing workflow:

```
Prototype in Hermes
  → 2-3 real-data corrections
    → Fine-tune in dedicated workspace
      → Deploy on VPS with cron
```

| Step | Content | Duration |
|---|---|---|
| 1. Prototype | Describe and trial workflow in main Hermes. First attempts nearly always wrong | 1 day |
| 2. Iterate | Run 2-3 times on real work, correcting deviations each time. Harness learns corrections and skills them | 2-3 days |
| 3. Fine-tune | Refine prompts, finalize routing, add error handling in dedicated workspace (Claude Code, etc.) | 1 week |
| 4. Deploy | Dockerize → VPS → cron setup → let it run | 1 day |

**Core insight**: "You cannot write a production agent from scratch. You have to grow one."

### Application to Wiki Management System

This methodology directly applies when adding new wiki pipelines:

1. **Prototype**: Manually try processing in Hermes a few times (e.g., new RSS feed processing)
2. **Iterate**: Run on real articles 2-3 times, fix tagging/classification deviations
3. **Fine-tune**: Script it, finalize error handling and cron schedule
4. **Deploy**: Productionize as a cron job like `raw-backlog-ingest`

## Pattern 6: Agent Ergonomics

### Fleet Check-in
```
$ ssh hermes
$ docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"

NAMES                       STATUS         IMAGE
hermes-orchestrator         up 14 hours    hermes-runtime
hermes-seo-espressio        up 8 hours     hermes-runtime
hermes-cmo                  up 8 hours     hermes-runtime
hermes-life                 up 12 hours    hermes-runtime
```

### Runbook Example
```
# runbook: hermes-seo-espressio
restart:   docker compose restart hermes-seo-espressio
logs:      docker logs -f hermes-seo-espressio
shell:     docker exec -it hermes-seo-espressio bash
```

## Concrete Application to Our Wiki Management System

Applying Shann's pattern set to the current wiki management system (Hermes single agent + 27 cron jobs) in priority order:

### Priority High: Build Control Room
Create `~/wiki/control-room/` to consolidate operational knowledge scattered across AGENTS.md and skills. Becomes the reference point for new pipeline additions and speeds up incident isolation.

### Priority Medium: Apply Agent Creation Heuristics
Gain criteria for whether to split the current single agent:
- **Need own credentials?** → Currently not needed
- **Need own long-term memory?** → Research agent specialized in arxiv papers has value
- **Ongoing repeated work as a separate role?** → daily-report generation, wiki-health checking are split candidates

### Priority Low-Medium: Introduce Brain Layers
Layer memory/skills so pipeline additions don't pollute overall context.

### Already Achieved
- **Level 4-equivalent automation**: 27 cron job autonomous pipelines match Shann's Level 4 (Automated Agent Team)
- **Prototype → Production**: `raw-backlog-ingest`'s phased introduction aligns with this methodology

## Cross-References

- [[entities/shannhk]] — Proponent of these patterns. Based on practical experience at Espressio AI
- [[entities/hermes-agent]] — The agent framework these patterns assume
- [[comparisons/hermes-vs-openclaw]] — "Rails vs Linux" philosophical framing

## References

- [How to Become a Hermes Agent Operator](https://x.com/i/article/2055317817658900480) (2026-05-15, Shann/@shannhk, X article)
- [hermes-agent-control-room template](https://github.com/shannhk/hermes-agent-control-room)
