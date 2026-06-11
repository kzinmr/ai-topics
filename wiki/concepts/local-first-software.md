---
title: "Local-First Software"
type: concept
created: 2026-04-13
updated: 2026-04-13
status: draft
tags:
  - architecture
  - developer-tooling
related:
  - martin-kleppmann
  - automerge
  - bluesky-at-protocol
  - local-llm
sources:
  - "https://martin.kleppmann.com/papers/local-first.pdf"
  - "https://localfirst.fm"
  - "https://electric-sql.com"
---

# Local-First Software

A software design philosophy that makes the user's device the **primary authoritative copy** of data, limiting servers to synchronization, backup, and discovery assistance.

Proposed as a research paper by Ink & Switch in 2019. It is an antithesis to the cloud-centric architecture (REST API + server-authoritative model) and its problems of "network dependency," "lack of data ownership," "privacy risks," and "vendor lock-in."

---

## The 7 Ideals of Local-First Software

| # | Ideal | Core Principle |
|---|-------|----------|
| 1 | **No Spinners** | Instant UI response via local disk I/O. Network latency hidden by background sync |
| 2 | **Multi-Device** | Seamless cross-device sync. Server is secondary copy, authority is local |
| 3 | **Network Optional** | Full functionality offline. Sync later via internet/BT/WiFi |
| 4 | **Seamless Collaboration** | Real-time co-editing + async workflows. Automatic conflict resolution |
| 5 | **The Long Now** | Data persists even after vendor disappears. Prevents "digital dark age" |
| 6 | **Security & Privacy** | E2E encryption default. Eliminates centralized data honey pots |
| 7 | **Ultimate Ownership** | User can copy, modify, back up, delete data (not bound by API/ToS) |

---

## Analysis of Existing Architectures

| Technology | Strengths | Weaknesses |
|------|------|------|
| **Files + Email** | Full ownership, offline-capable, long-term preservation, fast | Real-time collaboration impossible, manual merging, version chaos |
| **Web Apps** (Google Docs, Trello) | Seamless real-time collaboration, zero install | No offline reliability, zero ownership, vendor lock-in |
| **Cloud Sync** (Dropbox, Drive) | Good offline support, easy backup | Conflict copies during real-time collaboration, mobile is server-dependent |
| **Git/GitHub** | Excellent async collaboration, offline-first, full control | Real-time fine-grained editing impossible, weak with non-text formats |
| **BaaS** (Firebase, CloudKit, Realm) | Easy sync, good offline caching | Proprietary lock-in, no privacy/long-term guarantees |
| **CouchDB/PouchDB** | Multi-master replication, philosophically aligned | Manual conflict resolution impractical, steep learning curve |

---

## CRDTs: The Foundational Algorithm of Local-First

**Conflict-free Replicated Data Types (CRDTs)** are multi-user data structures designed for distributed, concurrent editing.

### How They Work
- Multiple devices can independently update data, and it is deterministically merged on sync
- No manual merging like Git. Conflicts are resolved automatically through mathematics
- Transport-agnostic (server/P2P/Bluetooth/USB)
- Fine-grained (from keystroke-level real-time editing to batch async workflows)

### Kleppmann's Positioning
> *"Just as packet switching was an enabling technology for the Internet... CRDTs may be the foundation for collaborative software that gives users full ownership of their data."*

### Ink & Switch Prototype Findings
1. **CRDTs worked practically** — automatic merging was seamless
2. **Offline UX was overwhelmingly superior** — users felt true ownership
3. **Conflicts were rare** — minimized by fine-grained tracking + human coordination
4. **History visualization is important** — distributed systems need "time travel" UI
5. **URLs enable sharing** — Web-style URLs ideal for document discovery
6. **P2P networks are immature** — NAT traversal lacks reliability
7. **CRDT history bloat** — storing all keystrokes degrades memory/performance. GC/compression unsolved
8. **Servers have a role too** — not as authority but as "cloud peer" (discovery, backup, bridging offline users, burst computation)

---

## Ecosystem Development (2019-2026)

### Key Projects

| Project | Role | Notes |
|-------------|------|------|
| **Automerge** | CRDT library | Led by Kleppmann. JSON CRDT |
| **Yjs** | CRDT library | Proven in rich text collaboration |
| **ElectricSQL** | Postgres sync engine | Works with PGlite (WASM Postgres in browser). v1.0-beta in 2024 |
| **RxDB** | Local-first DB | OPFS/IndexedDB-based. Web-compatible |
| **TinyBase** | Reactive data store | Specialized for local state management |
| **PGlite** | WASM Postgres | Developed by ElectricSQL. DB running in browser |
| **Replicache** | Real-time sync | Immediate confirmation of local writes |
| **Vlcn/cr-sqlite** | SQLite CRDT | Relational CRDT |
| **Ditto** | P2P sync | Offline-first DB |

### Kleppmann's 2024 Update

At Local-First Conference 2024 (Berlin), he stated that **"Local-First has moved from research phase to practical stage."**

In particular, he proposed the **Generic Sync Server** concept — an approach that dramatically reduces development costs by **generalizing only synchronization** without placing app-specific code on the server.

> *"So much work in building a web app goes into reinventing this backend infrastructure that every single company has to reinvent again. And so if we can make the data sync generic... That I think is part of the economic value proposition of local-first software."*

---

## Large-Scale Local-First Implementation: Bluesky / AT Protocol

Kleppmann, as a Bluesky core developer, applies Local-First principles to social networking.

### AT Protocol's Local-First Elements
- **Personal Data Server (PDS)**: User's data has their "own server" as primary copy (Ideal #2/#7)
- **Account Portability**: Data can be migrated when changing servers (Ideal #5/#7)
- **Self-Certifying Data**: Data with cryptographic verification (Ideal #6)
- **"Big World" Design**: Relay handles large-scale indexing, PDS stays lightweight (balancing scalability + ownership)

Paper: [arXiv:2402.03239](https://arxiv.org/abs/2402.03239) — "Bluesky and the AT Protocol: Usable Decentralized Social Media"

---

## Local-First and AI Agents: Concrete Technical Bridges and Honest Gap Analysis

> **Note**: Local-First and AI Agents address different problem domains. The following organizes **actually existing technical connection points**, not conceptual similarities.

### Bridge 1: Event Sourcing → Agent Audit Logs

**Local-First side**: CRDTs record all changes as events and merge them on sync (event sourcing).

**AI Agent side**:
- CAST (Claude Agent Specialist Team) records all agent actions in SQLite WAL mode
- Claude Code session history is saved to local files
- 3-layer memory: Daily notes → Long-term MEMORY.md → Knowledge graph (PARA structure)

**Connection point**: Both have an architecture of "recording changes as immutable events, enabling later reconstruction." Agent "cross-session memory" can be interpreted as applying Local-First event sourcing to context management.

### Bridge 2: Local Authority Model → Local Agent Execution

**Local-First side**: The primary authoritative copy of data is local. Servers only handle sync.

**AI Agent side**:
- Claude Code runs locally as a Node.js CLI (~10.5 MB)
- Filesystem, shell, tools are all local
- Only model inference uses API communication. Workspace context is saved locally
- OpenClaw: Mac Mini 24/7 autonomous operation. Data on local filesystem

**Connection point**: The model of "agent executes locally, external API is limited to inference only" matches Local-First's structure of "local is primary, cloud is complementary." From a privacy/compliance perspective (medical/financial/legal), the prohibition on data exfiltration directly corresponds to Local-First Ideals #6/#7.

### Bridge 3: Generic Sync Server → MCP (Model Context Protocol)

**Local-First side**: Kleppmann's proposed approach of "not placing app-specific code on the server, generalizing only sync." ElectricSQL abstracts Postgres → client sync.

**AI Agent side**:
- MCP connects 3000+ external services via standard protocol
- Claude Code defines MCP servers in `.mcp.json`
- No app-specific integration code needed. Tool connections via standard interface

**Connection point**: The design philosophy of "abstracting via standard protocol, separating the infrastructure layer from the application layer" is common to both. MCP applies Local-First's Generic Sync Server concept to "AI tool connections."

### Bridge 4: Edge Inference → Network Optional

**Local-First side**: Full functionality without network (Ideal #3).

**AI Agent side**:
- [[concepts/local-llm/_index]] — Local inference via Ollama + llama.cpp/GGUF
- RTX 4090 24GB runs 70B models (quantized)
- Phi-4-Reasoning 14B beats o1-mini in math
- Apple MLX for fastest M-series chip inference
- TTFT: 7B at 50ms (local) vs 200-400ms (cloud)

**Connection point**: "Escape from network dependency" is a shared goal for both. In AI Agents, edge inference dominates on both latency (TTFT reduction) and privacy (no data exfiltration). Cost-wise, dual RTX 5090s ($4K) are comparable to H100 ($25K+).

### Bridge 5: CRDTs → CRDT for AI

**Local-First side**: CRDTs guarantee automatic merging of data structures.

**AI Agent side**:
- Research is underway applying CRDTs to AI context management
- Treat local knowledge graphs as CRDTs, merging cross-device sessions
- SQLite CRDT (Vlcn/cr-sqlite) usable as AI Agent session store

**Connection point**: Attempts to apply CRDTs' "distributed state convergence" concept to AI Agent "state management." However, this is still at the research stage.

### Honestly Remaining Gaps

| Local-First solved/in-progress | AI Agent unsolved |
|----------------------|-----------------|
| Mathematical conflict resolution via CRDTs | No mathematical guarantees for multi-agent "decision conflicts" |
| Generic Sync Server abstraction | Agent inference pipelines have strong task-specific dependencies |
| Static data ownership/permanence | Concepts of ownership, verification, and permanence for LLM-generated content are immature |
| P2P sync (NAT traversal is a challenge) | Inter-agent direct communication (A2A protocol) similarly unsolved |
| CRDT history bloat (GC/compression unsolved) | Agent context bloat (compaction immature) |

---

## 2026 Trends

- **EU AI Act (effective August 2026)** makes local deployment a regulatory requirement
- **Local models matching Sonnet-class quality** predicted by end of 2026
- **Dual RTX 5090s ($4K)** comparable to H100 ($25K+) — 75% cost reduction
- **Hybrid architecture** (local for speed/privacy + cloud for frontier reasoning) becomes standard

---

## References

- Kleppmann, M. et al. (2019). ["Local-First Software: You Own Your Data, in Spite of the Cloud"](https://martin.kleppmann.com/papers/local-first.pdf). Ink & Switch.
- Kleppmann, M. (2024). ["The past, present, and future of local-first"](https://martin.kleppmann.com/2024/05/30/local-first-conference.html). Local-First Conference, Berlin.
- Kleppmann, M. et al. (2024). ["Bluesky and the AT Protocol: Usable Decentralized Social Media"](https://arxiv.org/abs/2402.03239). arXiv:2402.03239 [cs.DC].
- [localfirst.fm](https://localfirst.fm) — Podcast series on local-first development
- [ElectricSQL Blog](https://electric-sql.com/blog/2024/07/17/electric-next) — "A new approach to building Electric"
- [RxDB](https://rxdb.info/articles/local-first-future.html) — "Why Local-First Software Is the Future and its Limitations"
- [CAST Project](https://github.com/ek33450505/claude-agent-team) — Claude Agent Specialist Team
- [OpenClaw](https://openclaw.ai) — Self-hosted AI agent framework
