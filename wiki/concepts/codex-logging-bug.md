---
title: "Codex Logging Bug (SQLite SSD Wear Incident)"
created: 2026-06-24
updated: 2026-06-24
type: concept
tags:
  - coding-agents
  - sqlite
  - incident
  - infrastructure
  - optimization
  - agent-safety
  - vulnerability
  - feedback-loop
  - bug
  - openai
sources:
  - raw/articles/2026-06-14_openai-codex_logging-tb-ssd.md
---

# Codex Logging Bug (SQLite SSD Wear Incident)

The Codex logging bug (GitHub Issue #28224) was a significant infrastructure incident involving OpenAI's [[entities/codex|Codex CLI]] agent, where excessive SQLite feedback logging caused approximately 640 TB/year of SSD writes — enough to exhaust consumer SSD write endurance in under one year. The incident was reported on June 14, 2026, and resolved through three merged PRs by June 23, 2026.

## Incident Overview

### The Problem

Codex CLI continuously wrote large volumes of telemetry and debug data to local SQLite databases (`~/.codex/logs_2.sqlite` and associated WAL/SHM files). On the reporter's machine, after approximately 21 days of uptime, the SSD had accumulated 37 TB of writes attributable primarily to Codex SQLite log operations.

Extrapolated to a full year: **~640 TB/year**.

On a consumer 1 TB SSD with a typical **600 TBW** (terabytes written) endurance rating, this rate would consume the drive's full warranted write lifetime in less than 12 months.

### Severity

This is not merely a performance issue — it represents **physical hardware damage risk** from AI agent software. The incident exposed a class of failure modes unique to always-running agent processes that generate continuous telemetry:

| Risk Category | Impact |
|---------------|--------|
| **SSD wear-out** | Premature drive failure, data loss |
| **Disk exhaustion** | System instability when disk fills with log data |
| **I/O contention** | Degraded system performance for all applications |
| **Write amplification** | SQLite WAL + filesystem overhead multiplies logical writes |
| **Silent degradation** | Problem accumulates over weeks before user notices |

## Technical Analysis

### Root Cause: Unfiltered TRACE-Level Logging

The primary culprits were global TRACE-level log statements that persisted enormous volumes of internal event data to SQLite:

| Source | Level | Size |
|--------|-------|------|
| `codex_api::endpoint::responses_websocket` | TRACE | 527.4 MiB |
| `codex_otel.log_only` | INFO | 141.2 MiB |
| `codex_otel.trace_safe` | INFO | 121.2 MiB |
| `log` | TRACE | 97.4 MiB |
| `codex_client::transport` | TRACE | 60.1 MiB |

**70.7% of logged data was at TRACE level** — the most verbose logging tier, typically intended for transient debugging rather than persistent storage.

### SQLite Write Amplification

The incident revealed severe write amplification in SQLite:

| Metric | Value |
|--------|-------|
| Database file size | 1.2 GiB |
| Retained rows | ~506,000 |
| Total allocated row IDs | 5,543,677,486 |

The **10,000x gap** between retained rows and historical inserted row IDs indicates massive log churn. SQLite's AUTOINCREMENT counter advanced past 5.5 billion while the database retained only half a million rows — meaning virtually all logged data was inserted and then pruned, with the writes still hitting the SSD.

Additional amplification sources:
- **WAL (Write-Ahead Log)**: Double-writes for every transaction
- **Index updates**: B-tree index modifications for each insert
- **Pruning/checkpoint operations**: Rewriting pages during VACUUM or auto-checkpoint
- **Filesystem-level amplification**: Journaling, copy-on-write filesystem overhead

### Related Codex SQLite Issues

The logging bug was not isolated — it connected to a constellation of SQLite-related performance issues in the Codex codebase:

| Issue | Description |
|-------|-------------|
| #17320 | Excessive SQLite WAL writes during streaming due to TRACE logs ignoring RUST_LOG |
| #24275 | Codex Desktop rapidly grows logs_2.sqlite/WAL during normal active use |
| #26374 | app-server feedback log sqlite grows unbounded (~0.75 GB/day) |
| #22444 | logs_2.sqlite-wal grows indefinitely after deletion (stale TUI processes hold file handles) |
| #20563 | Heavy I/O from idle codex processes |
| #27020 | Severe disk I/O on Windows WSL2 |
| #27911 | goals_1.sqlite write amplification: ~11 MB/s sustained |
| #21134 | Codex Desktop unusable on long threads due to memory and TRACE log churn |
| #12969 | app-server sources feedback logs at trace level |

This pattern suggests a systematic engineering gap: Codex's observability infrastructure was designed for cloud/server environments (where TRACE logs go to centralized log aggregation) rather than local desktop agents (where they go to SQLite on consumer SSDs).

## Resolution

Three PRs were merged between June 14-23, 2026, eliminating approximately 85% of the excessive logging:

| PR | Description | Release |
|----|-------------|---------|
| #29432 | Stop logging every Responses WebSocket event | 0.142.0 |
| #29457 | Filter noisy targets from persistent logs | 0.142.0 |
| #29599 | Stop persisting bridged log events | 0.143.0 (planned) |

### Workaround

For users affected before the fix shipped, a SQLite trigger could block log inserts:

```sql
sqlite3 ~/.codex/logs_2.sqlite "
  CREATE TRIGGER IF NOT EXISTS block_log_inserts
  BEFORE INSERT ON logs
  BEGIN
    SELECT RAISE(IGNORE);
  END;
"
```

## Broader Implications

### Agent Software and Local Storage

This incident highlights a fundamental tension in AI agent architecture: agents that run continuously on user machines need **different logging strategies** than server-side services:

| Environment | Logging Model | Storage Target |
|-------------|---------------|----------------|
| Cloud/server | Verbose, centralized | Object storage, log aggregation (unlimited) |
| Desktop agent | Filtered, capped | Local SSD (finite endurance) |
| Mobile agent | Minimal, sampled | Flash storage (very limited endurance) |

Agent platforms adopting cloud-native logging patterns on consumer hardware risk creating similar incidents. This applies not just to Codex but to [[entities/claude-code]], [[entities/cursor-ai]], [[entities/devin]], and any agent that runs persistently on user devices.

### The "Always-On Agent" Problem

Traditional developer tools (editors, compilers, linters) are I/O-bound on user actions. AI agents introduce a new pattern: **continuous background I/O** from:
- Telemetry and feedback logging
- Context indexing and file watching
- Conversation persistence
- Agent state checkpointing
- Sub-agent communication logging

Without explicit write budgets and log rotation policies, these continuous writes can silently degrade hardware.

### [[concepts/software-supply-chain-security]] Implications

The incident intersects with supply chain security concerns: agent software with excessive disk I/O can:
- Mask malicious I/O patterns (attackers could hide exfiltration in noisy log streams)
- Create denial-of-service vectors (triggering TRACE-level logging on user machines)
- Accelerate hardware failure in CI/CD environments (shared runners, cloud dev machines)

### Agent Safety Lessons

From an [[concepts/agent-safety]] perspective, the incident demonstrates that:

1. **Unbounded resource consumption is a safety failure**: Agents that can exhaust local storage without user awareness violate the principle of bounded resource usage
2. **Observability must be cost-aware**: Logging infrastructure must account for the storage medium (SSD vs. cloud) and set appropriate defaults
3. **Telemetry should be opt-in at verbose levels**: TRACE-level logging should never be a default for persistent storage on consumer devices
4. **Agent health monitoring needs disk-aware metrics**: Agent platforms should surface SSD write rates and disk health in their monitoring dashboards

### Industry-Wide Relevance

This is not a Codex-specific problem. Any AI coding agent with local telemetry persistence faces similar risks. Recommended practices for agent platform developers:

- **Default log level caps**: Never persist TRACE or DEBUG to local storage by default
- **Write budgets**: Implement configurable daily/monthly write limits
- **Retention policies**: Auto-prune logs older than N days with configurable retention
- **Disk health awareness**: Monitor SSD TBW and warn users before approaching endurance limits
- **Opt-in telemetry**: Verbose logging should require explicit user opt-in

## Timeline

| Date | Event |
|------|-------|
| 2026-06-14 | Issue #28224 opened by 1996fanrui, reporting 640 TB/year writes |
| 2026-06-14 | Workaround posted by @beskay (SQLite trigger) |
| 2026-06-23 | Three PRs merged (#29432, #29457, #29599), 85% reduction confirmed |
| 2026-06-23 | Issue closed by reporter |

## Related Pages

- [[entities/codex]] — OpenAI Codex coding agent (primary entity page, detailed)
- [[entities/openai-codex]] — OpenAI Codex overview (alternate entity page)
- [[concepts/agent-safety]] — Agent safety concepts and practices
- [[concepts/software-supply-chain-security]] — Software supply chain security
- [[concepts/ai-agent-safety-incidents]] — AI agent safety incidents
- [[concepts/agent-safety-incidents-open-source]] — Open-source agent safety incidents
