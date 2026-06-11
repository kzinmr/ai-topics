---
title: "Claude Code Skills — Mechanism and Role Patterns"
created: 2026-05-15
updated: 2026-06-04
type: concept
tags:
  - claude-code
  - agent-skills
  - harness-engineering
  - ai-agent-engineering
  - skill-graph
  - developer-tooling
sources:
  - raw/articles/2026-03-17_trq212_lessons-building-claude-code-skills.md
  - https://x.com/trq212/status/2033949937936085378
  - "[[raw/articles/2026-06-03_anthropic_claude-code-feedback-loops]]"
related:
  - agent-skills
  - skill-architecture-patterns
  - claude-code-best-practices
  - agent-harness
  - mcp
status: active
---

# Claude Code Skills — Mechanism and Role Patterns

Based on practical knowledge gained by Claude Code Team member Thariq Shihipar ([[entities/thariq-shihipar]]) from operating hundreds of Skills within Anthropic — the essence of Skills' **mechanism** and their classification into **9 role patterns**.

> "Skills have become one of the most used extension points in Claude Code. They're flexible, easy to make, and simple to distribute."

## Mechanism: The Essence of Skills

### Skills ≠ Markdown Files

The most important misconception to clear up. Skills are not just `.md` files:

- **They are folders**: Directory structures containing scripts, assets, data, and configuration files
- **Agent-discoverable, explorable, and operable**: Claude reads files, executes scripts, and references data as needed
- **Dynamic Hook registration**: PreToolUse/PostToolUse hooks enable scoped behavioral constraints activated during Skill invocation

### Filesystem = Medium for Context Engineering

```
skill-name/
├── SKILL.md              # Required: YAML frontmatter + body instructions
├── references/           # Optional: Detailed references (progressive disclosure)
│   └── api.md            # → Claude reads only when needed
├── scripts/              # Optional: Executable code
│   └── fetch_data.py     # → Claude executes, only the result enters context
├── assets/               # Optional: Templates, images, etc.
│   └── template.md       # → Output format template
└── config.json           # Optional: Setup state persistence
```

**Progressive Disclosure**:
1. **L1**: `name` + `description` → Always injected at session start as the full Skill list
2. **L2**: `SKILL.md` body → Claude reads autonomously when relevant tasks arise
3. **L3+**: Files under `references/` → Claude judges and reads as needed

> "Tell Claude what files are in your skill, and it will read them at appropriate times."

### Deterministic Operations through Code Execution

Code in the `scripts/` folder is more deterministic and efficient than token generation:
- Sorting, data processing, form extraction — code execution is more accurate
- Claude reads only the execution result, not the script itself, into context
- Guarantees consistency and reproducibility

### On-Demand Hooks

Dynamic behavioral constraints that activate only during Skill invocation and persist for the session:

| Hook | Function | Use Case |
|------|----------|----------|
| `/careful` | Blocks `rm -rf`, `DROP TABLE`, `force-push`, `kubectl delete` | Only activate during production operations (always-on is annoying) |
| `/freeze` | Blocks Edit/Write outside specific directories | Debugging when "trying to add a log but it 'fixes' unrelated places" |

### Memory and Data Persistence

Skills can save their own state to the filesystem:
- **append-only logs**: `standups.log` stores past post history → enables delta detection on next execution
- **JSON/SQLite**: Structured data storage
- **`${CLAUDE_PLUGIN_DATA}`**: Stable storage path that survives Skill upgrades

## Role Patterns (9 Types of Skills)

After cataloging all Skills within Anthropic, they converged into 9 reusable patterns. Ideally each Skill fits cleanly into one type — straddling multiple types causes confusion.

### Type 1: Library & API Reference

**Purpose**: Teach Claude the correct usage of specific libraries, CLIs, and SDKs.

**Characteristics**:
- Edge cases and footguns of internal libraries
- Reference code snippets
- Gotchas sections highlighting points where Claude tends to err

**Examples**:
- `billing-lib` — Edge cases and pitfalls of internal billing library
- `internal-platform-cli` — All subcommands of internal CLI and when to use them
- `frontend-design` — UI generation adhering to design system

### Type 2: Product Verification

**Purpose**: Define verification methods to ensure code works correctly.

**Characteristics**:
- Integrates with external tools like Playwright/tmux
- Programmatic state assertions
- One of the most important Skill types — "worth an engineer spending a week refining a verification Skill"
- Visualizing verification results through video output is also effective

**Examples**:
- `signup-flow-driver` — Runs signup → email verification → onboarding in a headless browser, asserting state at each step
- `checkout-verifier` — Operates payment UI with Stripe test cards, verifies invoice correctness
- `tmux-cli-driver` — Testing of interactive CLIs requiring TTY

### Type 3: Data Fetching & Analysis

**Purpose**: Provide connections to data stacks and monitoring stacks with analysis workflows.

**Characteristics**:
- Includes credentials, dashboard IDs, and query patterns
- Encapsulates boilerplate patterns for complex joins and aggregations

**Examples**:
- `funnel-query` — Event joining method for "signup → activation → billing" with normalized user_id table
- `cohort-compare` — 2-cohort retention/conversion comparison with statistical significance flags
- `grafana` — Data source UIDs, cluster names, issue → dashboard mapping table

### Type 4: Business Process & Team Automation

**Purpose**: Consolidate repetitive workflows into a single command.

**Characteristics**:
- Relatively simple instructions but depends on other Skills or MCP
- **Logging of past execution results** is key to consistency — Claude reads its own history and detects deltas
- Standardizes integration between ticket systems, Slack, and GitHub

**Examples**:
- `standup-post` — Auto-generates daily standup from ticket tracker + GitHub + Slack history
- `create-<ticket>-ticket` — Schema enforcement (valid enum values, required fields) + post-creation flow (reviewer notification, Slack link)
- `weekly-recap` — Merged PRs + closed tickets + deployments → formatted report

### Type 5: Code Scaffolding & Templates

**Purpose**: Generate framework-specific boilerplate.

**Characteristics**:
- Scaffold generation including natural language requirements (things that can't be expressed in code alone)
- Increased flexibility through composition with scripts

**Examples**:
- `new-<framework>-workflow` — New service/handler generation with annotations
- `new-migration` — Migration file template + common pitfalls
- `create-app` — New app with pre-wired auth, logging, deployment config

### Type 6: Code Quality & Review

**Purpose**: Enforce organizational code quality standards and support reviews.

**Characteristics**:
- Maximize robustness through deterministic scripts/tools
- Suitable for auto-execution with Hooks or GitHub Actions
- Enforces code styles Claude defaults to being bad at

**Examples**:
- `adversarial-review` — Fresh subagent performs critical review → fixes implemented → repeat until criticism becomes trivial
- `code-style` — Enforces code styles Claude defaults to being bad at
- `testing-practices` — Instructions on how to write tests and what to test

### Type 7: CI/CD & Deployment

**Purpose**: Automate code checkout, push, and deployment.

**Characteristics**:
- Can also collect data by integrating with other Skills
- Gradual rollout, automatic rollback, conflict resolution

**Examples**:
- `babysit-pr` — PR monitoring → flaky CI retry → merge conflict resolution → auto-merge
- `deploy-<service>` — Build → smoke test → gradual traffic rollout + error rate comparison → auto-rollback
- `cherry-pick-prod` — Isolated worktree → cherry-pick → conflict resolution → PR with template

### Type 8: Runbooks

**Purpose**: From symptoms (Slack notifications, alerts, error signatures) through multi-tool investigation to structured report generation.

**Characteristics**:
- Symptom → tool → query pattern mapping table
- Standardized on-call workflows

**Examples**:
- `<service>-debugging` — Symptom → tool → query pattern mapping table (for high-traffic services)
- `oncall-runner` — Alert acquisition → usual suspects check → findings formatting
- `log-correlator` — Cross-system log retrieval via request ID

### Type 9: Infrastructure Operations

**Purpose**: Guardrailed automation for routine maintenance including destructive operations.

**Characteristics**:
- Safe identification and gradual cleanup of orphan resources
- Standardized query patterns for cost investigation
- Makes it easier for engineers to follow best practices

**Examples**:
- `<resource>-orphans` — Detection of orphaned Pods/Volumes → Slack notification → soak period → user confirmation → cascading cleanup
- `dependency-management` — Organizational dependency approval workflow
- `cost-investigation` — Investigation query patterns for "why storage/egress costs spiked"

## Overview of 9 Patterns

| # | Type | Focus | Automation Level | External Dependencies | Memory Usage |
|---|------|------|-----------------|----------------------|-------------|
| 1 | Library & API Reference | Knowledge injection | Low | Low (static files) | Not needed |
| 2 | Product Verification | Quality assurance | High | High (Playwright/tmux) | Medium (video output) |
| 3 | Data Fetching & Analysis | Data connectivity | Medium | High (credentials, DB) | Medium (query results) |
| 4 | Business Process | Workflow automation | High | High (tickets, Slack, GitHub) | High (log history) |
| 5 | Code Scaffolding | Code generation | Medium | Medium (frameworks) | Not needed |
| 6 | Code Quality & Review | Quality enforcement | Medium-High | Low (static analysis) | Low |
| 7 | CI/CD & Deployment | Deployment automation | High | Medium (CI/Git) | Medium (deploy history) |
| 8 | Runbooks | Incident response | Medium | High (monitoring, logs) | Medium (investigation reports) |
| 9 | Infrastructure Operations | Infrastructure maintenance | Medium | Medium (cloud API) | High (cleanup history) |

## Design Principles (Tips for Making Skills)

### 1. Don't State the Obvious

Claude Code knows the codebase well, and Claude has default opinions about coding. Skills should focus on **information that pushes Claude out of its normal thought patterns**.

> "The frontend design skill was built by iterating with customers on improving Claude's design taste, avoiding classic patterns like the Inter font and purple gradients."

### 2. Gotchas Sections Have the Highest Signal

The Gotchas section, which accumulates "failure points Claude has actually encountered," accounts for most of a Skill's information value. Ideally, **invest time to continuously update it**.

### 3. Progressive Disclosure via Filesystem

> "A skill is a folder, not just a markdown file."

- Separate detailed function signatures into `references/api.md` → Claude reads only when needed
- If output is Markdown, place template in `assets/` → Claude copies and uses it
- Tell Claude "what files exist" and it will read them at appropriate times

### 4. Don't Over-Railroad Claude

Skills have high reusability, so **don't make instructions too specific**. Give Claude the information it needs, but leave flexibility to adapt to the situation.

### 5. Think Through the Setup

For Skills requiring user-specific configuration (e.g., which Slack channel to post to), the pattern of saving to `config.json` is effective:
- If not set, Claude asks the user
- Once set, it's reused

### 6. Description Field is for the Model

Claude Code builds a list of all Skill descriptions at startup and scans "is there a Skill for this request?" So the description is **not a summary, but a description of trigger conditions**.

### 7. Memory and Data Persistence

- Append all past posts to `standups.log` → detect deltas on next execution
- `${CLAUDE_PLUGIN_DATA}` is a stable path that survives Skill upgrades
- Complexity is optional — from simple log files to SQLite

### 8. Providing Scripts and Code Generation

> "One of the most powerful tools you can give Claude is code."

- Provide helper function groups for data fetching → Claude composes them for advanced analysis
- For a prompt like "What happened on Tuesday?", Claude generates and executes a script on the fly

### 9. On-Demand Hooks

Annoying when always-on, but occasionally extremely useful constraints:
- `/careful` — Blocks dangerous commands during production operations
- `/freeze` — Blocks edits outside specific directories during debugging

## Distribution Patterns

| Method | Suitable Scale | Trade-off |
|--------|---------------|-----------|
| **Repo check-in** (`./.claude/skills/`) | Small teams, few repos | More Skills compress everyone's context |
| **Plugin Marketplace** | Large organizations | Each developer installs only needed Skills |

### Marketplace Operations

- **No centralized selection team**: Organically discover the most useful Skills
- **Sandbox → Traction → PR → Marketplace**: First upload to GitHub sandbox folder, share on Slack etc. Once sufficient traction gained, submit PR to marketplace
- **Curration is mandatory**: Low-quality duplicate Skills can easily be created, making pre-release review process important

### Composing Skills

Native dependency management doesn't exist yet, but referencing other Skills by name lets the model call installed ones:
- "CSV generation Skill" references "file upload Skill"
- Model autonomously chains execution

**Production example — Claude Code team workflow (June 2026):** The team bundles multiple skills into a single feature-development workflow that rolls all manual steps into one automated pipeline:
- `/simplify` — clean up the diff
- Custom `/verify` — confirm the change works end-to-end (browser verification, tests)
- Design check — if the diff touched UI
- Open and subscribe to a PR
- Watch CI and auto-fix failures as they come in

This pattern — skills that call other skills — is the fundamental mechanism for creating feedback loops that reduce human babysitting. The key insight: "If a process is clear, encode as much of it as possible as a skill." Domain-specific verification (frontend browser checks, mobile audits, performance budgets, accessibility checklists) becomes automatable when encoded as measurable criteria that Claude can evaluate against.

Source: [[raw/articles/2026-06-03_anthropic_claude-code-feedback-loops]]

### Measuring Skills

Use PreToolUse hooks to log Skill usage:
- Discover popular Skills
- Identify undertriggering Skills (activated less than expected)

## See Also

- [[concepts/harness-engineering/agent-skills-overview]] — Agent Skills concept cluster map (parent page)
- [[concepts/agent-skills]] — Agent Skills open standard (Anthropic Engineering)
- [[concepts/skill-architecture-patterns]] — Self-Authored vs Governed (Hermes Agent vs OpenClaw)
- [[concepts/harness-engineering/agent-harness]] — Agent Harness overview
- [[concepts/mcp]] — Model Context Protocol
- [[concepts/claude-code/claude-code-best-practices]] — Claude Code operational best practices
- [[entities/thariq-shihipar]] — Author
- [[concepts/skill-graph]] — Skill Graph architecture
