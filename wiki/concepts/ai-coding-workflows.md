---
title: "AI Coding Workflows"
type: concept
created: 2026-04-29
updated: 2026-04-30
tags:
  - agentic-engineering
  - developer-tooling
  - security
  - workflow
  - concept
  - multi-llm
sources:
  - "raw/articles/timsh.org--claude-inside-docker--6842418e.md"
  - "raw/articles/timsh.org--how-i-created-an-ethereum-proof-of-stake-demo-entirely-with---3d132b24.md"
---

# AI Coding Workflows

> Structured patterns for using AI coding assistants (Claude Code, Cursor, Codex) in production — from isolated containers to credential management. Focus on the *how* of agent-assisted development: security boundaries, cost tradeoffs, and environment setup.

## Why Isolate AI Agents

Running AI coding tools with unrestricted access to your local filesystem, terminal, and secrets is inherently risky. As [[concepts/cognitive-debt]] shows, when you work at a higher level of abstraction, you lose direct understanding of what the tool is doing — and that's exactly when security vulnerabilities matter most.

Common failure modes observed in the wild:
- AI agents deleting entire project directories (`rm -rf` incidents)
- Bypassing built-in command blacklists in "Yolo mode"
- MCP (Model Context Protocol) vulnerabilities exposing host systems
- Unrestricted access to SSH keys and API credentials

## Docker Dev Container Pattern

The most accessible isolation strategy: run Claude Code inside a Docker container via VSCode's Dev Container feature.

### Architecture

```
┌─────────────────────────────┐
│  Host Machine               │
│  ├── VSCode (GUI)           │
│  └── Docker Engine          │
│      └── Container          │
│          ├── Claude Code    │
│          └── Project Files  │
└─────────────────────────────┘
```

### Benefits

| Property | Without Docker | With Docker Container |
|----------|---------------|----------------------|
| Filesystem access | Full host access | Container-only + mounted volumes |
| Secrets exposure | SSH keys, credentials accessible | None unless explicitly provided |
| Blast radius | System-wide damage possible | Container isolation |
| Reproducibility | Machine-dependent | Deterministic environment |

### Setup

1. Create a `.devcontainer/devcontainer.json` in your project root
2. VSCode prompts "Reopen in Container" — click it
3. Claude Code is installed inside the container
4. Work proceeds normally in VSCode, but all agent execution happens in the sandbox

A minimal template is available at [github.com/tim-sha256/claude-in-docker](https://github.com/tim-sha256/claude-in-docker).

## Secure Credential Management

Inside an isolated container, you need a controlled way to give the agent access to version control and external services.

### GitHub Fine-Grained PATs (Recommended)

Instead of sharing your primary SSH key with the container, use a dedicated fine-grained Personal Access Token:

1. Create token at `github.com/settings/personal-access-tokens/new`
2. Grant **only** `Contents: Read and write` repository permission
3. Clone repos using: `git clone https://<USER>:<TOKEN>@github.com/<USER>/<REPO>.git`
4. Save credentials: `git remote set-url origin https://<USER>:<TOKEN>@github.com/<USER>/<REPO>.git`

**Why not SSH keys?** SSH keys are difficult to scope — a key that grants access to one repo often grants access to many. PATs can be limited to specific repositories and permission types.

### General Credential Rules

- **Never mount host `.ssh/` or `.config/` directories** into agent containers
- Use **scoped credentials** — each agent gets the minimum permissions it needs
- **Rotate tokens regularly** — treat them as temporary, not permanent
- **Audit what agents can access** — if you wouldn't give it to a freelance dev, don't give it to an agent

## Cost Comparison: Claude Code vs Cursor

| Factor | Claude Code + Docker | Cursor Pro |
|--------|---------------------|------------|
| Monthly cost | $20 (Claude subscription) | $20 (Cursor subscription) |
| Rate limits | Reasonable, transparent | Aggressive post-unlimited update |
| Token visibility | Clear spending indication | Obscured |
| Security | Docker isolation | Full host access by default |
| IDE experience | VSCode Dev Container (seamless) | Native Cursor IDE |
| CLI preference | For terminal-oriented workflows | For GUI-oriented workflows |

## When to Use This Pattern

- Working on **multiple projects** where isolation matters
- Using AI agents with **third-party code** you don't fully trust
- **Corporate environments** where filesystem access needs restrictions
- Developers who prefer **CLI-native workflows** over GUI tools

## Multi-LLM Role Separation Pattern

A practical workflow pioneered by [[entities/tim-sh]]: using **two different LLMs** for distinct roles in the development process. This addresses a key limitation of single-LLM coding — a single model with a single chat context tends to lose architectural perspective over time and struggles with both high-level design and low-level implementation simultaneously.

### The Pattern: PM + Coder

| Role | Tool | Responsibility |
|------|------|---------------|
| **Project Manager** | ChatGPT-4o | Architecture, design, requirements, UX, instruction writing, code review |
| **Coder** | Cursor / Claude Code | File implementation, syntax, compiler errors, debugging |

The key insight: **the "Project Manager" LLM writes instructions for the "Coder" LLM**, similar to how a human tech lead writes tickets for a junior developer. This creates a self-reinforcing loop where the PM LLM forces architectural rigor and the Coder LLM ensures implementation quality.

### Key Techniques

| Technique | Description |
|-----------|-------------|
| **Always Commit** | Commit after every meaningful change (100+ commits/project). Enables easy rollback and creates a recoverable audit trail |
| **localStorage.json** | Externalize all data structures (variables, schemas, API shapes) into a JSON file both LLMs can read. Avoids hallucinated variable names across sessions |
| **SVG over Libraries** | Use raw SVG for data visualization — both LLMs share a common understanding of SVG. Third-party chart libraries are opaque to the "wrong" LLM |
| **Template First** | Define layout and component templates upfront before creating the first page. Both LLMs reference the same template |
| **Single Chat Context** | Keep all project discussions in one ChatGPT chat. When context degrades, re-send the latest `localStorage.json` and template definitions |
| **Debug vs Design Split** | Debug code issues with Coder LLM (it sees the actual files). Design/UX problems take back to PM LLM (it knows the architecture) |
| **Resend Source** | Re-send reference material when context windows degrade mid-project |

### When to Use This Pattern

- **Non-developer practitioners** who need architectural guidance from one LLM and implementation from another
- **Complex projects** where a single LLM chat context degrades over time
- **Projects requiring both deep UX and clean implementation** — rarely available from one model
- **Anyone working across tool boundaries** (ChatGPT web vs IDE-native agent)

### Risks

- Requires maintaining **two separate workflows** and two sets of context
- The PM LLM's instructions may become stale if the Coder LLM diverges
- If instructions are too vague, the Coder LLM produces disconnected code
- If instructions are too specific, the Coder LLM loses autonomy and cannot adapt

### Related: The Instruction Mismatch Anti-Pattern

An instructive failure case from the field: a developer asking for PHP code and getting 5,000 lines of Next.js spaghetti because the LLM's system prompt defaulted to a different stack. Documented in [[concepts/abstraction-costs#Spaghetti Code from Stack Mismatch]]. The lesson: **the LLM's "mental model" of your stack must be explicitly set** — don't rely on defaults.

## Related Patterns

- [[concepts/vibe-coding]] — Self-hosting is the natural deployment target for vibe-coded apps
- [[concepts/cognitive-debt]] — Isolation mitigates the risk of agents operating beyond your understanding
- [[concepts/ai-abstraction-costs]] — Containers restore a level of visibility that high-level abstractions remove
- [[concepts/self-hosting-ai-development]] — Deploy your isolated dev environment alongside your production apps
- [[concepts/anthropic-managed-agents]] — Enterprise-grade agent isolation (Anthropic's approach)

## References

- [Switching to Claude Code + VSCode inside Docker](https://timsh.org/claude-inside-docker/) — Tim Sh (April 2026)
- [Claude Code bypassing Cursor built-in command blacklist](https://reddit.com/r/ClaudeAI/) — Community reports (2026)
