# Codex SQLite feedback logs can write ~640 TB/year and rapidly consume SSD endurance

**Source:** https://github.com/openai/codex/issues/28224
**Published:** 2026-06-14 (updated 2026-06-23)
**Author:** 1996fanrui (GitHub Issue)
**Archived:** 2026-06-24

---

## Summary

A GitHub issue (#28224) on the openai/codex repository reported that Codex CLI continuously writes large amounts of data to local SQLite feedback log databases, resulting in approximately 640 TB/year of SSD writes. On a consumer 1 TB SSD rated at ~600 TBW (terabytes written), this could exhaust the drive's warranted write endurance in less than one year.

## Key Findings

### Evidence 1: Write Amplification

After approximately 21 days of uptime, the reporter's SSD had written about 37 TB. Process/file-level checks confirmed Codex SQLite logs as the primary continuous writer.

| Metric | Value |
|--------|-------|
| Current logs_2.sqlite file size | 1.2 GiB |
| Current retained rows | 506,149 |
| Total allocated row IDs | 5,543,677,486 |

The database retains only ~0.5M rows while the SQLite AUTOINCREMENT counter has advanced past 5.5B IDs — a ~10,000x gap between retained and historical inserted row IDs.

### Evidence 2: Log Level Distribution

| Level | Estimated MiB | Byte % |
|-------|---------------|--------|
| TRACE | 732.5 | 70.7% |
| INFO | 266.5 | 25.7% |
| DEBUG | 30.6 | 3.0% |
| WARN | 5.9 | 0.6% |

Top sources:
- `codex_api::endpoint::responses_websocket` TRACE: 527.4 MiB
- `codex_otel.log_only` INFO: 141.2 MiB
- `codex_otel.trace_safe` INFO: 121.2 MiB
- `log` TRACE: 97.4 MiB
- `codex_client::transport` TRACE: 60.1 MiB

### Root Cause

The primary sources are global TRACE logs, mirrored telemetry logs, and raw WebSocket/SSE payloads being persisted to SQLite at extremely high volume. The TRACE-level logging essentially records every event including noisy targets that should never be persisted.

## Resolution

Three PRs were merged (by June 23, 2026) that eliminated approximately 85% of the excessive logging:

1. **Stop logging every Responses WebSocket event** (#29432, released in 0.142.0)
2. **Filter noisy targets from persistent logs** (#29457, released in 0.142.0)
3. **Stop persisting bridged log events** (#29599, to be released in 0.143.0)

### Workaround

A simple workaround from @beskay:

```sql
sqlite3 ~/.codex/logs_2.sqlite "CREATE TRIGGER IF NOT EXISTS block_log_inserts BEFORE INSERT ON logs BEGIN SELECT RAISE(IGNORE); END;"
```

## Related Issues

- #17320: Excessive SQLite WAL writes during streaming due to TRACE logs ignoring RUST_LOG
- #24275: Codex Desktop rapidly grows logs_2.sqlite/WAL during normal active use
- #26374: app-server feedback log sqlite grows unbounded (~0.75 GB/day), no retention/rotation
- #22444: logs_2.sqlite-wal grows indefinitely after deletion due to stale/suspended Codex TUI processes
- #20563: Heavy I/O activity from idle codex processes
- #27020: Severe disk I/O / 100% disk active time on Windows WSL2
- #27911: goals_1.sqlite write amplification: ~11 MB/s sustained writes (11 GB lifetime) on a 4 KB database
- #21134: Codex Desktop becomes unusable on long active threads due to memory and TRACE log churn
- #12969: app-server source /feedback logs from sqlite at trace level

## Impact

This bug class represents a significant infrastructure reliability concern for AI coding agents. Agent software that persists excessive telemetry to local storage can cause real hardware damage (SSD wear-out), system instability (disk exhaustion), and degraded user experience. The incident highlights the need for careful log volume management in always-running agent processes.

Raw source from GitHub Issue #28224, openai/codex repository (93.3K stars, 13.8K forks).
