---
title: "Halo — Tamper-Evident Runtime Evidence for AI Agents"
created: 2026-07-08
updated: 2026-07-08
type: entity
tags:
  - agent-security
  - observability
  - open-source
  - audit
  - transparency
  - tool
  - agent-observability
sources:
  - https://github.com/bkuan001/halo-record
  - https://hn.algolia.com/api/v1/items/48818098
  - [[raw/articles/2026-07-07_bkuan001-halo-tamper-evident-runtime-evidence]]
---

# Halo — Tamper-Evident Runtime Evidence for AI Agents

**Halo** is an open-source tool (Apache-2.0) that provides tamper-evident runtime records for AI agents — the audit trail that the vendor runs but cannot edit. Every action an agent takes (tool calls, model calls, data access, approvals) becomes one record in an append-only, hash-chained log.

> **Core bet**: "Security reviews already ask AI questions next to the SOC 2 checklist, and today a written assurance still passes. The bet behind this project is that it won't for long." — Brian Kuan, author

## Technical Design

### Architecture
- **Append-only hash-chained log**: Each record links to the previous, forming a cryptographic chain
- **Recorder/Verifier/Witness/Report Server**: Four-component reference implementation
- **Zero runtime dependencies**: Standard library only. `pip install halo-record` installs exactly one package
- **No network calls** (except optional witness): Witness receives only a record count and chain fingerprint — record contents never leave infrastructure
- **~4,300 lines of Python**: Small enough to audit in an afternoon

### Privacy Design
- **Raw inputs never enter a record**: Arguments are hashed and stored only as a redacted summary
- **Redaction is best-effort**: Regex over common secret and PII formats — defense-in-depth, not a guarantee
- **Format is open and free**: Anyone can implement the record format independently

### Limitations
| Capability | Supported? |
|---|---|
| Integrity (nothing edited/reordered) | ✅ Yes |
| Completeness (nothing omitted) | ⚠️ No — the operator can delete records and re-seal |
| Non-repudiation | ✅ Hash-chained, verifiable by any party |
| Raw input protection | ✅ Hashed, never stored in plaintext |
| Secret/PII detection | ⚠️ Best-effort regex only |

> **Key limitation**: "A self-held chain proves integrity: nothing was edited or reordered after the fact. It cannot prove completeness: the operator of a recorder can delete the bad day and re-seal the chain, or never write a record in the first place." — project README

## Use Cases

### For AI Agent Vendors
- Provide customers with a verifiable audit trail of agent actions on their data
- Answer security review questions ("what did your agent do with our data?") with evidence instead of assurances
- Pre-commit to actions before execution (academic preregistration pattern)

### For AI Agent Customers
- Independently verify vendor claims about agent behavior
- Detect gaps (missing records) when expected actions don't appear in the log
- Integrate with existing SOC 2 and security review processes

## Community Reception

The HN community (35 points, 20 comments) was generally positive about the idea but raised several concerns:
- Why a Python library instead of an API proxy? (Author's answer: library integrates at the agent code level, not the network layer)
- Will large vendors host witnesses? (Key adoption bottleneck)
- Can it monitor Claude Code or Codex? (Yes, by instrumenting the agent's tool-call layer)

## Related Concepts
- [[concepts/agent-security-patterns]] — General security patterns for agent systems
- [[concepts/ai-agent-security]] — AI agent security overview
- [[concepts/ai-agent-safety-incidents]] — Real-world AI agent failures
- [[concepts/security-and-governance/agent-security-landscape-2026]] — 2026 agent security landscape
- [[concepts/evaluation/agent-observability]] — Agent observability and monitoring
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — Security patterns in agent architecture

## Repository
- **GitHub**: [bkuan001/halo-record](https://github.com/bkuan001/halo-record)
- **License**: Apache-2.0
- **Author**: Brian Kuan ([@brian_kuan](https://news.ycombinator.com/user?id=brian_kuan) on HN)
