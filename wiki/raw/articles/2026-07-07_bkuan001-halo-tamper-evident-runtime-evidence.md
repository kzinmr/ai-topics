---
title: "Halo — Open-Source, Tamper-Evident Runtime Evidence for AI Agents"
source: "GitHub (bkuan001/halo-record)"
url: "https://github.com/bkuan001/halo-record"
author: "Brian Kuan (bkuan001)"
date: "2026-07-07"
date_ingested: "2026-07-08"
type: article
tags: [agent-security, observability, open-source, audit, transparency, tools]
---

Tamper-evident runtime records for AI agents: the audit trail the vendor runs but cannot edit.

Every action your agent takes (tool calls, model calls, data access, approvals) becomes one record in an append-only, hash-chained log. Any party can verify the log was never altered, without trusting whoever produced it. When a customer's security team asks "what did your agent do with our data?", you hand them a link instead of a paragraph.

## Technical Details

- **Zero runtime dependencies**: Standard library only. `pip install halo-record` installs exactly one package.
- **No network calls**: except the witness (opt-in), which receives only a record count and chain fingerprint
- **Raw inputs never enter a record**: Arguments are hashed and stored only as a redacted summary
- **~4,300 lines of Python**: small enough to audit in an afternoon
- **Apache-2.0 license**
- **Format**: Open and free to implement. Reference implementation includes recorder, verifier, witness client, and report server

## Limitations

- Proves integrity (nothing edited or reordered) but NOT completeness (operator can delete the bad day and re-seal the chain)
- Redaction is best-effort (regex over common secret and PII formats) — defense-in-depth, not a guarantee

## HN Discussion (35 points, 20 comments)
- "I'm currently working on an agent framework that has auditability as one of its core promises"
- "Could I monitor something like Claude Code or Codex with this?"
- "Why a Python library instead of a completions API proxy?"
- "The vendor uses the same technique that academic preregistration uses in experiments"

## Source
- GitHub: https://github.com/bkuan001/halo-record
- HN discussion: https://hn.algolia.com/api/v1/items/48818098
