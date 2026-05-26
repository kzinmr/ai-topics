---
title: Martin Kleppmann
type: entity
created: 2026-04-13
updated: 2026-05-12
aliases:
  - martin.kleppmann
tags:
  - person
  - architecture
  - developer-tooling
  - lab
  - open-source
related:
  - concepts/local-first-software
  - entities/automerge
  - entities/bluesky-at-protocol
sources:
  - https://martin.kleppmann.com
  - https://martin.kleppmann.com/papers/local-first.pdf
  - https://github.com/automerge/automerge
---
# Dr. Martin Kleppmann

Associate Professor at the University of Cambridge Department of Computer Science and Technology. Researches distributed systems, local-first collaborative software, and cryptographic protocols.

**Best-selling author of *Designing Data-Intensive Applications*** (2017, 2nd ed. 2026) — the authoritative text on distributed data system architecture. Over 200,000 copies sold, translated into 8 languages.

---

## Biography

| Period | Role |
|------|------|
| 2022–present | University of Cambridge, Associate Professor (Concurrent and Distributed Systems, Cryptography and Protocol Engineering) |
| 2022–2023 | TU Munich Research Fellow (Systems Research Group) |
| 2015–2022 | University of Cambridge Research Fellow (Systems Research Group) |
| 2012 | Co-founded Rapportive → acquired by LinkedIn |
| 2009 | Co-founded Go Test It → acquired by Red Gate Software |

---

## Research: Local-First Software and CRDTs

### Local-First Software (2019)

Published the paper **"Local-First Software: You Own Your Data, in Spite of the Cloud"** at Ink & Switch research lab. Proposes a design philosophy where user devices are the primary authority, countering cloud-centric architecture.

**7 Ideals**: No Spinners, Multi-Device, Network Optional, Seamless Collaboration, The Long Now, Security & Privacy, Ultimate Ownership

Positions **CRDTs (Conflict-free Replicated Data Types)** as the foundational technology, enabling mathematical guarantees for distributed collaborative editing.

### Automerge

A JavaScript CRDT library. Implements a JSON data model as an operation-based CRDT.

- Multiple devices can update independently → deterministic merge on sync
- Enables both offline operation and real-time collaboration
- Transport-agnostic (P2P, server, Bluetooth, etc.)
- Formally verified (Strong Eventual Consistency)

**Key Papers**:
- "A Conflict-free Replicated JSON Datatype" (IEEE TPDS, 2017)
- "Verifying strong eventual consistency in distributed systems" (PACMPL, 2017)
- "Automerge: Real-time data sync between edge devices" (MobiUK, 2018)
- "Interleaving anomalies in collaborative text" (PaPoC, 2019)

### Generic Sync Server (2024)

Proposed at the Local-First Conference 2024. An approach to **generalize sync** without placing application-specific code on the server. Has the potential to dramatically reduce development costs.

> *"So much work in building a web app goes into reinventing this backend infrastructure that every single company has to reinvent again. And so if we can make the data sync generic... That I think is part of the economic value proposition of local-first software."*

---

## Bluesky / AT Protocol

Kleppmann is a core Bluesky developer, involved in designing the decentralized social network.

**AT Protocol's Local-First Elements**:
- **Personal Data Server (PDS)**: User data's primary copy lives on "your server"
- **Account Portability**: Data can migrate when changing servers (prevents vendor lock-in)
- **Self-Certifying Data**: Cryptographically verifiable data
- **"Big World" Design**: Large-scale indexing via Relay + lightweight PDS

Paper: "Bluesky and the AT Protocol: Usable Decentralized Social Media" (arXiv:2402.03239, DIN '24)

---

## Publications

| Title | Year | Notes |
|----------|-----|------|
| Designing Data-Intensive Applications | 2017 | O'Reilly. Seminal work on distributed systems/databases |
| Designing Data-Intensive Applications (2nd ed.) | 2026 | Co-authored with Chris Riccomini |
| Secret Colors: A Gentle Introduction to Cryptography | 2020 | Co-authored with Mitch Seymour (children's cryptography primer) |

---

## Talks & Media

- ACM Tech Talks (2023): "Creating local-first collaboration software with Automerge"
- RainbowFS Workshop (2022): "Automerge: CRDTs meet version control"
- Distributed Computing and Analytics Workshop (2018): "Automerge: Replicated Data Structures for Peer-to-Peer Collaboration"
- [localfirst.fm Podcast #4](https://localfirst.fm/4): CRDTs, Automerge, generic syncing servers & Bluesky
- Crowdfunding via [Patreon](https://patreon.com)

---

## Local-First and AI Agent Technical Bridges (From Kleppmann's Context)

> **Note**: Kleppmann himself does not directly address AI Agents. The following organizes points where his research **could technically connect** to AI agent development.

### 1. Event Sourcing → Agent Audit Logs

**CRDTs** record all changes as immutable events and merge on sync. This approach is directly applicable to agent session management:
- CAST (Claude Agent Specialist Team) records all agent actions in SQLite WAL mode
- Claude Code session history is saved to local files
- Both follow the pattern of "recording changes as events → reconstructible later"

**Difference**: CRDTs have mathematical convergence guarantees; agent decision chains have no equivalent guarantee.

### 2. Generic Sync Server → MCP

Kleppmann's approach of "generalizing only sync" aligns with **[[concepts/mcp]]** design philosophy:
- ElectricSQL: Abstracts Postgres → client synchronization
- MCP: Standard protocol connecting 3000+ external services
- Both provide a "standardization layer requiring no app-specific code"

### 3. CRDT History Growth → Context Window Management

CRDTs' unresolved problem (storing every keystroke → memory degradation) is structurally identical to agent **context window bloat**:
- Both face unbounded append-only log growth
- Both have immature GC/compaction
- Both struggle with "what to keep, what to discard"

### 4. Remaining Essential Gaps

| Aspect | Local-First (Resolved/In Progress) | AI Agent (Unresolved) |
|------|------------------------------|------------------|
| Conflict resolution | Mathematically guaranteed via CRDTs | No guarantees for multi-agent decision conflicts |
| Sync abstraction | Practical via ElectricSQL/Generic Sync | Agent reasoning pipelines are heavily task-dependent |
| Data ownership | Clear for static data | Ownership and verification of LLM-generated content is immature |
| P2P sync | NAT traversal is a challenge but progressing | Agent-to-agent direct communication (A2A) similarly unresolved |

---

## Links

- Website: https://martin.kleppmann.com
- Bluesky: @martin.kleppmann.com
- Mastodon: @martin@nondeterministic.computer
- GitHub: https://github.com/automerge/automerge
- Papers: https://martin.kleppmann.com/papers/
- Email: firstname at lastname dot com

## See Also

- [[entities/daniel-van-strien]] — Co-author on local-first papers and related CRDT research
- [[entities/_index]]
- [[lance-martin]]
- [[entities/martin-alderson]]