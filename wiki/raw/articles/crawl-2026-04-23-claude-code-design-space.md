---
title: Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems
category: other
status: active
---

# Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems

**Source:** arXiv:2604.14228v1  
**Date:** April 2026  
**URL:** https://arxiv.org/html/2604.14228v1  
**Authors:** Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen (VILA Lab, MBZUAI & UCL)  
**Crawled:** 2026-04-23  

## 🔑 Core Thesis & Architecture Overview
- **Core Loop:** A simple `while-true` async generator (`queryLoop()`) that calls the model, dispatches tools, and repeats. Follows the **ReAct pattern**.
- **Infrastructure Dominance:** Only **~1.6%** of the codebase is AI decision logic; **~98.4%** is deterministic operational infrastructure (permissions, context management, recovery, tool routing).
- **7-Component Flow:** `User → Interfaces → Agent Loop → Permission System → Tools → State & Persistence → Execution Environment`
- **5-Layer Decomposition:**
  1. **Surface:** Entry points & rendering (CLI, SDK, IDE)
  2. **Core:** Agent loop & 5-layer compaction pipeline
  3. **Safety/Action:** Permission system, hooks, extensibility, sandbox, subagents
  4. **State:** Context assembly, runtime state, append-only JSONL persistence, CLAUDE.md memory
  5. **Backend:** Shell execution, MCP clients, remote tools

## 🎯 Four Recurring Design Questions
| Design Question | Claude Code's Answer |
|----------------|----------------------|
| **Where does reasoning live?** | Model reasons; harness executes. Model only outputs structured `tool_use` blocks. |
| **How many execution engines?** | Single `queryLoop()` engine. Only the rendering/interaction layer varies. |
| **Default safety posture?** | **Deny-first with human escalation** + defense-in-depth (7 independent safety layers). |
| **Binding resource constraint?** | **Context window** (200K–1M tokens). Managed via a graduated 5-layer compaction pipeline. |

## 🧭 13 Design Principles
1. **Human Decision Authority** — Users retain ultimate control; system supports observation, approval, interruption, and audit.
2. **Safety, Security, & Privacy** — Protects users/code/infra even when humans are inattentive.
3. **Reliable Execution** — Faithful interpretation, long-horizon coherence, environmental ground-truth verification.
4. **Capability Amplification** — Enables qualitatively new workflows (~27% of tasks would not have been attempted otherwise).
5. **Contextual Adaptability** — Fits user/project context; trust evolves over time (auto-approve rates rise from ~20% to >40% across 750 sessions).
6. Deny-first with human escalation
7. Graduated trust spectrum
8. Defense in depth (layered)
9. Externalized programmable policy
10. Context as scarce resource
11. Append-only durable state
12. Minimal scaffolding, maximal harness
13. Values over rules
14. Composable multi-mechanism extensibility
15. Reversibility-weighted risk
16. Transparent file-based config/memory
17. Isolated subagent boundaries
18. Graceful recovery & resilience

## ⚙️ Core Subsystems Breakdown
### Turn Execution (Query Loop)
- **Pipeline:** Settings resolution → State init → Context assembly → 5 pre-model shapers → Model call → Tool dispatch → Permission gate → Execution → Stop condition.
- **Streaming Execution:** Concurrent read-only tools; serializes state-modifying tools. Uses sibling abort controllers & progress signals.
- **Recovery Mechanisms:** Max output token escalation (up to 3 retries), reactive compaction, prompt-too-long fallback, streaming fallback.

### Context Compaction
- **5-layer graduated pipeline** as tokens approach limits:
  1. Light truncation (drop old messages)
  2. Summarize older turns
  3. Compress tool outputs
  4. Summarize entire conversation
  5. Switch to smaller model for compaction

### Safety Architecture
- **7 independent safety layers** providing defense-in-depth.
- **Deny-first default:** Unrecognized actions blocked and escalated to human.
- **Permission model:** Granular allow/deny per tool + per path.

### State Management
- **Append-only JSONL logs** for auditability.
- **CLAUDE.md memory:** Persistent project context managed via PRs.
- **File-based config:** Transparent, version-controllable.

## 🔍 Key Insights
- **Agent reliability comes from the harness, not the model.** The model provides intelligence; the harness provides reliability through deterministic control flow.
- **Trust is earned over time.** Auto-approval rates naturally increase across sessions as the agent proves itself.
- **The agent loop is embarrassingly simple.** The complexity is all in the surrounding infrastructure.
- **Context compaction is a critical subsystem.** Without it, agents cannot operate in long-horizon tasks.
