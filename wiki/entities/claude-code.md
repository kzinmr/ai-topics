---
title: Claude Code
type: entity
created: 2026-04-24
updated: 2026-06-04
tags:
  - product
  - coding-agent
  - anthropic
  - economics
aliases:
  - Claude Code CLI
  - Anthropic Coding Agent
  - Claude Code Desktop
sources:
  - https://x.com/ClaudeDevs/status/2054610152817619388
  - https://www.latent.space/p/ainews-codex-rises-claude-meters
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
  - https://code.claude.com/en/whats-new/2026-w15
  - https://code.claude.com/en/whats-new/2026-w14
  - https://code.claude.com/en/changelog
  - https://www.getaiperks.com/en/articles/claude-code-updates
  - https://arxiv.org/html/2604.14228v1
  - https://claude.com/blog/introducing-routines-in-claude-code
  - "[[raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions]]"
  - "[[raw/articles/2026-05-25_sairahul1_claude-code-software-factory-7-agents]]"
  - raw/newsletters/2026-05-28-i-signed-up-for-another-saas.md
  - "[[raw/articles/2026-06-03_anthropic_claude-code-feedback-loops]]"
---

# Claude Code

Anthropic's AI coding agent. Operates across multiple surfaces: CLI, desktop app, VS Code/JetBrains extensions, Web, iOS, and Slack. Developed by [[entities/boris-cherny]].

Achieves 72.7% on SWE-bench Verified. As of April 2026, the industry-leading coding agent records 7.6x deployment frequency improvement and 89% AI adoption rate.

## Basic Information

| Item | Detail |
|------|------|
| Developer | Anthropic |
| Creator | Boris Cherny |
| Initial release | May 2025 (GA) |
| Latest major | v2.1.119 (April 23, 2026) |
| Default models | Opus 4.7, Sonnet 4.6, Haiku 4.5 |
| Supported environments | CLI, Desktop, VS Code, JetBrains, Web, iOS, Slack |

## Sub-Pages

- **[[entities/claude-code--capabilities]]** — Key metrics, latest features (Ultraplan, Monitor, Auto Mode, Routines, CLI Computer Use, Fast Mode), and key capabilities (Subagents, MCP Integration, Slash Commands, Checkpointing, Skills System)
- **[[entities/claude-code--architecture]]** — 5-layer decomposition, 7-component flow, core loop, infrastructure dominance (98.4% deterministic infra)
- **[[entities/claude-code--history]]** — Origins, internal dogfooding, GA, Agent Teams GA, and the source code leak incident

## Key Metrics (2026)

| Metric | Value |
|--------|-------|
| SWE-bench Verified | 72.7% (vs Codex 69.1%) |
| Deployment frequency increase | **7.6x** |
| AI adoption across employees | **89%** |
| Feature delivery speed | **2x faster** |
| Incident investigation speed | **80% faster** |

## Comparisons

- **Cursor** — Competitor
- **OpenAI Codex** — Competitor (SWE-bench: 69.1% vs Claude Code 72.7%)

## Related

- [[entities/boris-cherny]] — Creator
- [[entities/anthropic]] — Developer
- [[concepts/claude/mythos]] — Withheld high-security model
- [[entities/project-glasswing]] — Safety initiative
- [[concepts/harness-engineering]]

## Sources

- [Claude Code What's New — Week 15 (Ultraplan, Monitor)](https://code.claude.com/en/whats-new/2026-w15) (Apr 2026)
- [Claude Code What's New — Week 14 (CLI Computer Use)](https://code.claude.com/en/whats-new/2026-w14) (Apr 2026)
- [Claude Code Changelog](https://code.claude.com/en/changelog)
- [Introducing Routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) (Apr 14, 2026)
- [Auto Mode Blog](https://claude.com/blog/auto-mode) (Mar 24, 2026)
- [GetAI Perks — Claude Code Updates 2026](https://www.getaiperks.com/en/articles/claude-code-updates) (Mar 26, 2026)
- [arXiv:2604.14228v1 — Dive into Claude Code Architecture](https://arxiv.org/html/2604.14228v1) (Apr 2026)
- [Claude Code Camp — How the team really works](https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works) (Feb 5, 2026)
- [The Register — Claude Code source code leak](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/) (Mar 31, 2026)
- [Anthropic — Measuring Agent Autonomy](https://www.anthropic.com/news/measuring-agent-autonomy) (Feb 2026)
- [Kuber Studio — Claude Code Source Code Leak Analysis](https://kuber.studio/blog/AI/Claude-Code's-Entire-Source-Code-Got-Leaked-via-a-Sourcemap-in-npm,-Let's-Talk-About-it) (Apr 2026)



### Agent View — Unified Session Management (Research Preview, May 2026)

Claude Code introduced **Agent View**, a research preview feature providing a unified list of all active Claude Code sessions:

| Feature | Detail |
|---------|--------|
| **Functionality** | Unified dashboard showing all active agent sessions |
| **Status** | Research preview |
| **Use case** | Monitor and manage multiple concurrent Claude Code sessions from a single interface |

**Related session control commands** (Claude Code team thread, May 2026):
- **`/goal`** — Define a high-level objective for the agent to work toward autonomously
- **`/loop`** — Run a task in a continuous improvement loop
- **`/schedule`** — Schedule recurring agent runs at specified intervals

**Significance**: Agent View addresses the growing need for multi-agent session management as developers increasingly run multiple Claude Code sessions in parallel (per Boris Cherny's parallel worktree pattern). Combined with `/goal`, `/loop`, and `/schedule`, these represent a shift from interactive coding agent to persistent, managed agent workforce.

Source: Aakash's Clicky newsletter (May 2026)

## References

- 2026-04-16-vivek-trivedy-harness-memory-context-fragments
- 2026-04-28_x-article-the-harness-is-the-backend
- 2026-04-30_willccbb-analysis-rl-harness-lifecycle
- 2026-04-30_willccbb-rl-harness-lifecycle
- 2026-04-viv-harness-memory-context-fragments-bitter-lesson
- 2039441705586602134_The-Trillion-Dollar-Loop-B2B-Never-Had
- 2042660310851449223_Latent-Briefing-Efficient-Memory-Sharing
- crawl-2026-04-23-build-harness-not-code
- crawl-2026-04-23-harness-engineering-discipline

- 2026-01-02_boris-cherny---my-claude-code-setup-(jan-2026)
- 2026-01-31_boris-cherny---10-tips-from-the-claude-code-team-(feb-2026)
- 2026-02-11_chernycode---boris-cherny's-claude-code-config-files
- 2026-03-19-claude-agents-disagree-experiment
- 2026-04-09-claude-managed-agents-guide
- 2026-04-26-claude-code-openclaw-harness-practice
- 2026-keep-your-claude-code-context-clean-with-subagents
- 2041927992986009773_Launching-Claude-Managed-Agents
- 2047720067107033525_Memory-in-Claude-Managed-Agents
- boris-cherny-im-boris-i-created-claude-code
- crawl-2026-04-23-claude-code-design-space
- how-claude-code-team-really-works

## Usage & Workflows

#### 7-Agent Software Factory Workflow (May 2026)

A pipeline methodology by @sairahul1 ([[entities/sairahul1|Rahul]]) that splits Claude Code into 7 specialized agents. Overcomes the limits of vibe coding by enabling structured software development:

```
Researcher → Story Writer → Spec Writer → Backend Builder → Frontend Builder → Test Verifier → Validator
  (Read)       (Read)         (Read)      (Backend only)    (Frontend only)    (Test files)        (Read)
```

**3 human checkpoints**: Story approval → Spec approval → PR review. Everything else is fully automated.

**Centrality of CLAUDE.md**: A 100-300 line repo-root Markdown file serves as the shared knowledge base for all agents. It grows as team collective memory, with each AI mistake triggering an update.

See: [[concepts/dark-factory-software-factory]] for full case study and StrongDM comparison.

Source: [[raw/articles/2026-05-25_sairahul1_claude-code-software-factory-7-agents]]

### Core Workflow Patterns

#### Parallel Agent Execution
Boris Cherny's most influential insight:
> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."

- One agent reads logs and runs queries (analysis worktree)
- Multiple agents implement features in parallel (feature worktrees)
- Human acts as coordinator and approver

#### Plan Mode → Auto-Accept
1. **Start in Plan Mode** (double `Shift+Tab`) — Claude outlines the approach
2. **Review and refine** — Iterate with Claude until the plan is solid
3. **Switch to Auto-accept** — Claude executes the plan, usually succeeding on the first try
4. **Verify** — Claude runs tests or checks via browser extension

#### CLAUDE.md as Team Memory
- Version-control the team-shared file in git
- Update CLAUDE.md with each mistake
- Use `@claude` in PRs to update guidelines

### Terminal Environment

#### Recommended Setup
- **Ghostty**: Team-recommended (sync rendering, 24-bit color, Unicode support)
- **tmux**: Color-code/name tabs per worktree
- Shell aliases (za, zb, zc) for instant worktree switching
- Number terminal tabs 1-5, enable system notifications

#### Mobile-to-Desktop Workflow (2026)
Supports the "Phone to PR" workflow: start a task on iOS, route it to the desktop for execution, and finish as a PR.

### Claude Design Integration

Claude Design (April 2026) creates a direct handoff pipeline to Claude Code. When a design is complete, Claude Design packages everything into a handoff bundle that Claude Code can receive with a single instruction.

### Pricing (April 2026)

| Plan | Price | Details |
|

### Programmatic Usage Metering (May 2026)

On May 13, 2026, Anthropic announced a major pricing change via [@ClaudeDevs](https://x.com/ClaudeDevs/status/2054610152817619388), effective June 15, 2026:

- **Every paid Claude subscription now includes a dedicated monthly credit for programmatic usage**, equal to the dollar amount of the plan (e.g., $200/mo plan = $200 API credits)
- **Programmatic usage** covers: Claude Agent SDK, `claude -p`, Claude Code GitHub Actions, and third-party apps built on the Agent SDK
- **Interactive usage** (Claude.ai, Claude Code CLI/Desktop) retains its own limits separate from the API credit pool
- Previously, programmatic usage via OpenClaw, OpenCode, and other third-party harnesses was effectively subsidized at 70-90% below API pricing — this change formalizes and meters it

The announcement was met with mixed reactions: framed as a "rug pull" by some users who relied on the historical subsidy, but viewed by Anthropic as rationalizing a pricing model that was never sustainable for third-party harness usage. OpenClaw and OpenCode had already been selectively targeted; the new policy makes metering universal and transparent.

**Context**: This coincides with OpenAI's launch of an [enterprise switch promo](https://x.com/OpenAIDevs/status/2054586214112780518) the same day. Anthropic is consolidating its most favorable pricing behind its own tools (Claude Code, Claude.ai) now that its brand is established, while OpenAI Codex as the challenger maintains more liberal usage policies. See [[concepts/coding-agents/mandate-equinox]] for the broader competitive cycle.

Sources: [@ClaudeDevs — May 13, 2026](https://x.com/ClaudeDevs/status/2054610152817619388), [AINews: Codex Rises, Claude Meters Programmatic Usage](https://www.latent.space/p/ainews-codex-rises-claude-meters)
| **Pro** | $17/mo annual or $20/mo monthly | Claude Code included; Sonnet 4.6 + Opus 4.7 |
| **Max 5x** | $100/mo | Larger codebases, more usage |
| **Max 20x** | $200/mo | Maximum access, power users |
| **Team** | $20/seat/mo (5–150 seats) | Self-serve seat management |
| **Enterprise** | Contact sales | Advanced security, data management |
| **API** | Pay-as-you-go | No per-seat fee, unlimited developers |

---

## Security Plugin (May 2026)

Claude Code introduced a real-time security checking plugin that monitors code as it is written, warning about:
- **Dangerous command execution** — Shell commands with security implications
- **Unsafe HTML handling** — Cross-site scripting and injection risks
- **Dangerous Python code** — Code execution patterns with security implications

The plugin operates during Claude Code's code generation, catching common risk patterns before they reach version control. It represents a shift from post-commit security scanning to **pre-commit, real-time security feedback** integrated into the agent's code generation loop.

## Self-Verification & Feedback Loops (June 2026)

Claude Code's approach to autonomous task completion relies on two layers of verification that reduce the need for human babysitting:

### Two-Layer Verification Architecture

| Layer | When | Who | What |
|-------|------|-----|------|
| **Layer 1: Agentic Loop** | During building | Claude (self) | Type errors, lint errors, failing tests, runtime errors, browser verification |
| **Layer 2: Review Gate** | Before merge | Second agent (fresh context) | Unbiased code review, multi-angle diff analysis |

**Layer 1 — In-loop verification:** Claude already self-verifies against deterministic signals (type errors, lint errors, failing tests, runtime errors). The key insight is that manual checks — running the dev server, opening a browser, checking for layout shift, clicking through user flows — can be encoded as reusable skills. The more of those checks you encode, the closer Claude's first response gets to the final result.

**Layer 2 — Pre-merge review by a second agent:** A fresh agent with no bias from the coding conversation reviews the diff before merge. Options range from built-in `/review` (single-pass terminal review), to `/code-review` plugin (parallel subagents reviewing from different angles), to managed Claude Code Review (automatic on every PR for Team/Enterprise plans).

### Skill Composition: Bundling Skills into Workflows

The Claude Code team bundles multiple skills into a single feature-development workflow:
- `/simplify` — clean up the diff
- Custom `/verify` — confirm end-to-end functionality
- Design check — if UI was touched
- Open and subscribe to a PR
- Watch CI and auto-fix failures

This pattern — skills that call other skills — enables Claude to verify and execute more work end-to-end without human intervention.

### Frontend Verification Example

A `frontend-verify` skill demonstrates the pattern: Step 1 runs a browser verification (embedded preview in desktop app, or Chrome DevTools MCP in CLI), Step 2 runs a mobile performance audit. Domain-specific skills can encode performance budgets, accessibility checklists, design system rules, and good/bad examples as measurable criteria.

Source: [[raw/articles/2026-06-03_anthropic_claude-code-feedback-loops]]

## Prompt Caching Architecture (April 2026)

Claude Code is built around prompt caching from day one. The team runs alerts on cache hit rate and declares SEVs if it's too low. Key architectural decisions:

- **Static-first layout**: System prompt → Claude.MD → Session context → Messages. Any change anywhere in the prefix invalidates everything after it.
- **Messages over prompt edits**: When information becomes stale, `<system-reminder>` tags in messages preserve the cache.
- **No mid-session model switching**: Cache is per-model. Switching mid-conversation is more expensive than continuing.
- **Tool state via tools, not tool set changes**: Plan Mode uses `EnterPlanMode`/`ExitPlanMode` as tools rather than swapping tool definitions.
- **Deferred tool loading**: Lightweight stubs (`defer_loading: true`) with `ToolSearch` for discovery keep the prefix stable.
- **Cache-safe compaction**: Context compaction reuses the parent's exact system prompt, tools, and history to get cache hits.

**April 2026 Regression**: Shipped a 47% performance regression caught by user community before internal monitoring — a widely-cited lesson on immature production agent eval practices even at the leaders.

Sources: "Lessons from Building Claude Code: Prompt Caching Is Everything" (April 2026), "Prompt auto-caching with Claude" (@RLanceMartin)

See also: [[concepts/prompt-caching]], [[concepts/context-engineering|Context Engineering]]

## Session Management (Agent SDK)

The Claude Code Agent SDK implements Context Engineering abstractions as **typed API primitives**. Session management ([Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions)) is the SDK-level embodiment of Martin's Write/Select/Compress/Isolate framework.

### Session Basics

A session is a complete conversation history including the prompt, all tool calls, all tool results, and all responses. Automatically persisted to `~/.claude/projects/<encoded-cwd>/*.jsonl`. Sessions persist **conversation** state; **filesystem changes** are separately managed by File Checkpointing (separation of concerns).

### Three Operations: Continue / Resume / Fork

| Operation | API | Function | Context Engineering Equivalent |
|------|-----|------|------------------------|
| **Continue** | Python: `ClaudeSDKClient` / TS: `continue: true` | Auto-detect and append to latest session in current directory | **Write + Select** — transparent context persistence and restoration |
| **Resume** | `resume=<session_id>` | Restore a session by ID, accessing all past context | **Select** — precise context retrieval; supports process restart and multi-user |
| **Fork** | `resume=<id>, fork_session=True` | New session as a copy of the original; original remains immutable | **Isolate** — branch conversation history for safe experimentation with different approaches |

### Architecture Mapping with Context Engineering Framework

```
Context Engineering Abstraction     Claude Code SDK Implementation
─────────────────────────        ──────────────────────
Write (external persistence)     Auto session persistence (JSONL)
Select (selective retrieval)     Resume by session_id
Compress                        auto-compact (95% threshold)
Isolate                         Fork + Sub-agents (independent sessions)
Offload (filesystem separation)  File Checkpointing (conversation state ≠ file state)
```

**Cross-host**: Moving JSONL files or using the `SessionStore` adapter enables session restoration across CI/serverless environments. Utilities for listing, renaming, and tagging sessions (`list_sessions()`, `tag_session()`, etc.) are also provided.

### Design Implications

Context Engineering is evolving from ad-hoc prompt design toward **standardized typed APIs in the SDK**. In contrast to Martin's Bitter Lesson — "harnesses are stripped away as models improve" — foundational primitives like session management are being absorbed into the SDK.

Source: [[raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions]]

## The Infrastructure Layer
Before any agent patterns work, organizations need a unified infrastructure layer. Shopify built an internal **LLM proxy** ([[concepts/shopify-ai-engineering#llm-proxy-architecture|→ Shopify AI Engineering]]) that routes every AI request — from Claude Code, GitHub Copilot, Cursor, and other tools — through a single gateway. This provides centralized cost control, usage analytics, and the ability to swap models without changing any engineer's workflow.

The lesson: don't standardize on one tool. Standardize the layer *underneath* the tools.


### Dynamic Workflows (May 2026)
In May 2026, Anthropic introduced **Dynamic Workflows** for Claude Code as a research preview. This feature represents a fundamental shift in how Claude Code approaches large-scale codebase operations:

- **Hundreds of parallel subagents** per session — Claude Code plans a task, dynamically spins up parallel subagents, and coordinates their output
- **Codebase-scale migrations** across 100,000+ lines from kickoff to merge
- **Full workflow pipeline**: task planning → parallel execution → verification → merge
- **Dynamic agent spawning** based on task complexity — the system allocates more subagents for more complex tasks

This capability builds on the parallel agent patterns already used by organizations like Shopify (documented in [[concepts/claude-code#Pattern-1-Parallel-Agents-Not-Single-Chat|Pattern 1]]), but automates the orchestration layer that previously required manual engineer coordination.

Dynamic Workflows represents Anthropic's move toward automated multi-agent orchestration at scale, where the tool itself handles subagent spawning, work distribution, and output verification rather than requiring the engineer to manually launch and monitor parallel agents.

For a detailed breakdown of Claude Code's seven customization methods — CLAUDE.md, rules, skills, subagents, hooks, output styles, and system prompt append — see [[concepts/claude-code/claude-code-steering-methods|Claude Code Steering Methods]].


## Pattern 1: Parallel Agents, Not Single Chat
The foundational pattern shift: Claude Code is not a single-prompt-single-response tool at scale. Senior engineers launch **multiple agents simultaneously**, each working on different parts of the codebase:

- One agent refactors the auth module
- Another writes tests
- A third updates documentation
- The engineer reviews outputs, discards what doesn't work, merges what does

The engineer's role shifts from *writing code* to **reviewing and merging agent outputs**. [[entities/farhan-thawar|Farhan Thawar]] (VP Engineering at Shopify) describes this as "orchestrating intelligent systems." This is [[concepts/harness-engineering/agentic-design-patterns|agentic design patterns]] at production scale — engineers become orchestrators of parallel agent fleets rather than line-by-line authors.

This pattern maps to the broader [[concepts/multi-agents/multi-agent]] and [[concepts/multi-agents/agent-orchestration]] paradigm: the unit of work is not a prompt but a **delegated subtask with independent execution**.


## Pattern 2: Extended Critique Loops
Not every task benefits from parallelism. For complex architectural decisions, Shopify engineers run a single agent through **extended critique loops** — the agent generates an answer, evaluates it, revises it, and continues refining over long reasoning cycles.

Instead of accepting the first output, the agent is forced to argue with itself:

```text
"Propose an architecture for [X].
Then critique your own proposal: what breaks at scale?
Then revise based on your critique.
Then critique the revision.
Give me the final version with confidence levels for each decision."
```

This produces dramatically better results because Claude catches its own mistakes before a human has to. The pattern leverages the model's ability to self-correct through [[concepts/chain-of-thought]] reasoning and structured [[feedback-loop|feedback loops]].

**Key insight**: this is not just "ask twice." The structure — *propose → critique → revise → critique → finalize* — creates a deliberate adversarial dynamic that surfaces edge cases and assumptions that single-pass prompting misses.


## Pattern 3: MCP Integration (Shopify AI Toolkit)
In April 2026, Shopify released an open-source [[mcp|MCP]] server that connects Claude Code directly to Shopify's documentation, GraphQL API schemas, and live store operations:

```bash
claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest
```

This gives Claude Code 7 tools:
- Search current Shopify docs (not stale training data)
- Validate GraphQL queries against live schemas
- Execute store operations through Shopify CLI
- Create products, manage metafields, modify themes
- Run bulk operations with natural language

Without MCP, Claude hallucinates API fields and invents component patterns. With it, Claude works with **real platform data** — grounding LLM outputs in live schemas eliminates a major class of [[ai-coding]] errors.

The broader trend: MCP servers are being built by non-engineering teams (finance, sales, support) within Shopify, connecting Claude Code to Salesforce, Google Calendar, Gmail, and Slack — all without engineer help. This represents a significant [[concepts/vibe-coding]] democratization of tool-building.


## Pattern 4: CLAUDE.md as Team Infrastructure
CLAUDE.md is not personal config. At Shopify, it's **team infrastructure** committed to git and shared across all 23,000 engineers:

```markdown
# CLAUDE.md (Shopify internal pattern)


## StackRuby on Rails, React, GraphQL, MySQL


## Commands- Dev: `dev up && dev server`
- Test: `dev test [path]`
- Lint: `dev style`
- Type check: `bin/srb tc`


## Architecture- app/models/ → ActiveRecord models, business logic
- app/controllers/ → thin controllers, delegate to services
- app/services/ → service objects for complex operations
- app/graphql/ → GraphQL types, mutations, resolvers


## Rules- NEVER bypass Sorbet type checking
- All new code must have type signatures
- Database queries only through established patterns
- IMPORTANT: run `dev test` after every change
```

**Critical constraint**: keep CLAUDE.md under 60 lines. Stuffing it with every standard and convention makes performance *worse*, not better — you pay for all of it on every turn. The document serves as **context injection** that sets the agent's baseline understanding of the codebase, stack, and conventions.

This aligns with [[developer-experience]] best practices: the configuration is minimal, version-controlled, and shared. When a new engineer joins, the CLAUDE.md is part of the repo they clone — the agent inherits team conventions automatically.


## Pattern 5: Strategy-First Validation
Shopify flipped the engineering time ratio:

```
2024 workflow:
Strategy: 30% → Execution: 70%

2026 workflow (Shopify):
Strategy: 70% → Execution: 30%
```

Because AI handles most coding, engineers now spend 70% of time on **strategy**: mapping user flows, validating market demand, choosing the right architecture. Only 30% on execution. This represents an estimated ~20% productivity improvement — not from writing more code, but from **testing 10 approaches instead of 2**, faster prototyping, and higher-fidelity deliverables.

This shift embodies [[strategy-execution]] rebalancing: the bottleneck moves from "can we build it?" to "should we build it?" and "what's the right way?" The agent handles the *how*; the engineer focuses on the *what* and *why*.


## Pattern 6: Safe Autonomy with Guardrails
Shopify doesn't let agents run wild. Their permission-based guardrail system:

```json
{
  "permissions": {
    "allow": [
      "Read", "Glob", "Grep", "LS", "Edit",
      "Bash(dev test *)",
      "Bash(dev style *)",
      "Bash(git status)",
      "Bash(git diff *)",
      "Bash(git add *)",
      "Bash(git commit *)"
    ],
    "deny": [
      "Read(**/.env*)",
      "Bash(git push *)",
      "Bash(dev deploy *)",
      "Bash(bin/rails db:drop *)",
      "Bash(rm -rf *)"
    ],
    "defaultMode": "acceptEdits"
  }
}
```

Agents can read, write, test, and commit. They **cannot** push to remote, deploy to production, drop databases, or read secrets. A human stays in the loop for anything irreversible.

This is [[concepts/agent-safety]] at the operational level: explicit allowlists and denylists create a **bounded autonomy** zone where agents can work freely without risking production systems. The `acceptEdits` default mode means agents can edit files without constant human approval, but the denylist prevents escape from the sandbox.


### Minimal Effective CLAUDE.md- **Stack**: one line per technology (Ruby on Rails, React, GraphQL, MySQL)
- **Commands**: 3-5 essential dev commands (dev, test, lint, type check)
- **Architecture**: directory-to-responsibility mapping (app/models/ → business logic)
- **Rules**: hard constraints (NEVER bypass type checking), test-after-change requirement
- **Total**: under 60 lines — larger files degrade performance on every turn


### Parallel Agent Workflow1. Identify independent subtasks (different files/modules)
2. Launch 2-3 agents in separate terminals
3. Each agent receives a focused prompt for its subtask
4. Engineer reviews all outputs, merges what works, discards what doesn't


### Critique Loop Prompt Pattern```
"Propose [solution]. Critique your proposal. Revise. Critique again. 
Give final version with confidence levels per decision."
```


### Guardrail Setup- **Allow**: read, write (via Edit), test, lint, commit
- **Deny**: push, deploy, database drops, secret access, destructive filesystem operations
- **Default mode**: acceptEdits


## Adoption Path for Teams
1. **Standardize CLAUDE.md** — stack, commands, architecture, rules. Under 60 lines. Commit to git.
2. **Set up parallel agents** — 2-3 agents in separate terminals for larger tasks
3. **Install relevant MCP servers** — connect to your stack's APIs (GitHub, Slack, database)
4. **Add guardrails** — allow read/write/test/lint/commit, deny push/deploy/delete/secrets
5. **Flip the ratio** — spend 70% on strategy, let agents handle execution


## Current State and Trajectory
Shopify targets 90% autonomous coding by Q3 2026 with 23,000 engineers working toward it. The 20% productivity gain comes not from writing more code but from exploring more approaches, prototyping faster, and catching mistakes earlier. The teams getting the most out of Claude Code aren't the ones with the best prompts — they're the ones who built the infrastructure to let agents work **safely, in parallel, on real codebases**.


## See Also
- [[concepts/shopify-ai-engineering]] — Shopify's AI-first engineering approach
- [[entities/claude-code]] — Claude Code entity overview
- [[entities/shopify]] — Shopify entity page
- [[entities/anthropic]] — Anthropic
- [[concepts/harness-engineering/agentic-design-patterns]] — Agentic design patterns
- [[entities/farhan-thawar]] — Farhan Thawar (VP Engineering, Shopify)
- [[entities/coding-agents]] — Coding agents ecosystem overview

