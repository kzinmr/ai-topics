---
title: "Claude Code Best Practices"
created: 2026-04-13
updated: 2026-04-20
tags: [claude-code, prompt-engineering, mcp, subagents, workflow-patterns, agentic-engineering]
aliases: ["claude-code-tips", "claude-code-usage-patterns", "coding-agent-best-practices"]
related: [[concepts/agentic-engineering.md]], [[inference-speed-development]], [[claude-code-source-patterns]], [[context-window-management]]
sources:
  - url: "https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/"
    author: "Sankalp (@sankalp)"
    date: "2026"
    title: "My Experience with Claude Code 2.0 and How to Get Better at Using Coding Agents"
---

# Claude Code Best Practices

Practical patterns and techniques for effective Claude Code usage, synthesized from experienced users' real-world workflows. These complement the internal patterns found in [[claude-code-source-patterns]] with user-facing best practices.

---

## Core Philosophy

> "AI is not magic — it's a very smart intern with an excellent tailwind."
> — Sankalp, after 20 years of programming experience

The foundational mindset shift:
- **Claude Code is a collaborator, not an autopilot**
- **Your value is in direction and review, not typing**
- **The best users are those who know what good code looks like**

---

## MCP Server Patterns

**MCP (Model Context Protocol)** servers extend Claude Code's capabilities beyond file operations.

### Essential MCP Servers

| Server | Purpose | Use Case |
|--------|---------|----------|
| Browser tools | Web interaction, scraping | Testing web apps, gathering data |
| Database connectors | Direct DB queries | Schema exploration, data validation |
| Figma integration | Design-to-code | Converting designs to HTML/CSS |
| File system | Extended file ops | Batch operations, monitoring |
| Git | Version control | Commit management, history queries |

### MCP Best Practices

1. **Connect only what you need** — Each MCP server adds overhead and potential failure points
2. **Use for read-heavy operations** — MCP excels at fetching context (docs, schemas, designs)
3. **Verify MCP outputs** — Treat MCP responses as you would any external data source
4. **Combine with native tools** — MCP for context gathering, native tools for code modification

---

## Sub-Agent Delegation Patterns

### The `--max-turns` Pattern

Run independent tasks in parallel using Claude's sub-agent capability:

```bash
claude --max-turns 50 -p "Refactor the auth module to use the new JWT library. 
                           Update all tests. Commit with descriptive message."
```

**When to use sub-agents:**
- Self-contained tasks with clear success criteria
- Long-running operations (refactoring, test generation, documentation)
- Parallel workstreams that don't need human intervention mid-task

**When NOT to use sub-agents:**
- Tasks requiring creative judgment
- Ambiguous requirements needing clarification
- Work involving production systems or sensitive data

### Sub-Agent Best Practices

1. **Be explicit in the prompt** — Sub-agents can't ask clarifying questions
2. **Set reasonable turn limits** — `--max-turns 50` prevents runaway sessions
3. **Define success criteria** — "All tests pass" is better than "fix the auth module"
4. **Review output before committing** — Sub-agents work independently; verify before merging

---

## CLAUDE.md Strategy

### Team-Level CLAUDE.md

A shared `CLAUDE.md` in the project root serves as a "configuration file" for the entire team:

```markdown
# Project Context
- Architecture: React frontend, Python backend, PostgreSQL
- Key directories: /src (frontend), /api (backend), /tests
- Code style: Prettier + ESLint, Black + isort

# Agent Instructions
- Always run tests before suggesting changes
- Use TypeScript strict mode
- Prefer composition over inheritance
- When in doubt, ask before modifying database schemas

# Common Patterns
- API routes follow REST conventions
- Error handling uses Result<T, E> pattern
- State management via React Query + Zustand
```

### CLAUDE.md Best Practices

1. **Keep it current** — Outdated CLAUDE.md causes more harm than no CLAUDE.md
2. **Be specific, not verbose** — Concrete rules beat general guidance
3. **Include anti-patterns** — "Don't use X" is as valuable as "Use Y"
4. **Version control it** — CLAUDE.md should evolve with the project

---

## Context Management Techniques

### Session Hygiene

1. **Start fresh for new tasks** — Don't carry over irrelevant context
2. **Use `/compact` strategically** — Compress when session gets too long
3. **Reference, don't repeat** — Point to existing files instead of pasting content
4. **Clear scratch files** — Remove temporary files before ending sessions

### Context Window Optimization

| Technique | Effect | When to Use |
|-----------|--------|-------------|
| Start new session | Zero context, full attention | New task, topic change |
| `/compact` | Summarize conversation | Session getting long |
| Reference files | Load on-demand | Large codebases |
| Clear tool output | Remove noise | After successful operations |

See [[context-window-management]] for detailed patterns.

---

## Claude Code Routines (April 2026)

On April 14, 2026, Anthropic introduced **Routines** — a major evolution in Claude Code automation. Unlike local parameterized templates, Routines are server-side automations that run on Claude Code's web infrastructure, independent of the developer's laptop.

### What Are Routines?

A Routine is a Claude Code automation you configure once — including a prompt, repo, and connectors — then run on a schedule, from an API call, or in response to an event. Routines run on [Claude Code's web infrastructure](https://code.claude.com/docs/en/claude-code-on-the-web), so nothing depends on your laptop being open.

Before Routines, developers managed cron jobs, infrastructure, and MCP servers themselves. Routines ship with access to repos and connectors, packaging automations into set-and-forget workflows.

### Three Routine Types

#### 1. Scheduled Routines
Give Claude Code a prompt and a cadence (hourly, nightly, weekly) — it runs on schedule:
```
Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.
```
Existing `/schedule` CLI tasks are now scheduled routines.

#### 2. API Routines
Configure routines triggered by API calls. Every routine gets its own endpoint and auth token:
```
POST a message → get back a session URL. Wire Claude Code into alerting, deploy hooks, internal tools.
```
Example: Read an alert payload, find the owning service, post a triage summary to #oncall.

#### 3. Webhook Routines (GitHub)
Subscribe a routine to automatically kick off in response to GitHub events:
```
Flag PRs that touch the /auth-provider module. Summarize changes and post to #auth-changes.
```
Claude opens one session per PR and continues feeding updates (comments, CI failures).

### Common Routine Patterns

- **Backlog management:** Triage new issues nightly, label, assign, post summary to Slack
- **Docs drift:** Scan merged PRs weekly, flag docs referencing changed APIs, open update PRs
- **Deploy verification:** CD pipeline posts after deploy, Claude runs smoke checks, scans error logs for regressions, posts go/no-go
- **Security scanning:** Weekly dependency audit, flag vulnerabilities, create fix PRs
- **PR triage:** Auto-flag PRs touching sensitive modules, summarize changes for review channels

### Why Routines Matter

| Aspect | Before Routines | After Routines |
|--------|-----------------|----------------|
| Runtime | Local laptop required | Web infrastructure (always-on) |
| Triggers | Manual or cron setup | Scheduled, API, webhooks |
| Session management | Developer-managed | One session per event (per PR) |
| Connector access | Manual MCP setup | Built-in with repo/connector access |
| Scalability | Limited by local resources | Cloud-scaled |

### Best Practices for Routines

1. **Define clear boundaries** — Each routine should have a focused scope
2. **Use connectors wisely** — Leverage built-in connectors (Linear, GitHub, Slack) to avoid custom infrastructure
3. **Monitor routine output** — Review routine sessions regularly; they run autonomously
4. **Start with schedules** — Nightly triage and weekly scans are low-risk entry points
5. **Leverage per-PR sessions** — Webhook routines maintain per-PR context for ongoing discussions

### Related Patterns
- [[claude-code-source-patterns]] — Internal Claude Code implementation details
- [[concepts/harness-engineering/agentic-workflows/interactive-explanations.md]] — Reusable workflow patterns
- [[context-window-management]] — Managing context across routine invocations

---

## Anti-Patterns to Avoid

### 1. The Infinite Session

**Problem**: Keeping one Claude Code session open for days, accumulating context.

**Symptoms**:
- Slower response times
- Irrelevant code suggestions
- Model confusion about current task

**Solution**: Start fresh sessions for distinct work items.

### 2. Over-Delegation

**Problem**: Asking Claude to handle tasks requiring human judgment.

**Examples**:
- "Make the app better" (too vague)
- "Choose the right database" (requires context Claude doesn't have)
- "Fix this security vulnerability" (requires understanding of threat model)

**Solution**: Break down into specific, verifiable subtasks.

### 3. Blind Trust

**Problem**: Accepting AI-generated code without review.

**Risk**: Security vulnerabilities, logic errors, style inconsistencies.

**Solution**: Always review before committing. Run tests. Verify edge cases.

### 4. Prompt Bloat

**Problem**: Writing multi-paragraph prompts with excessive context.

**Effect**: Model loses focus, misses key instructions.

**Solution**: 
- One clear objective per prompt
- Reference files instead of pasting content
- Use CLAUDE.md for persistent context

---

## Workflow Patterns

### The Exploration Pattern

1. **Ask Claude to analyze** — "What's the structure of this codebase?"
2. **Review the analysis** — Verify accuracy
3. **Refine the question** — "Focus on the auth module specifically"
4. **Extract insights** — Use for planning

### The Implementation Pattern

1. **Write failing test** — Define expected behavior
2. **Ask Claude to implement** — "Make this test pass"
3. **Review implementation** — Check correctness, style, edge cases
4. **Refine if needed** — "Handle the null case too"
5. **Commit with message** — "Let Claude generate the commit message"

### The Refactoring Pattern

1. **Identify target** — "Refactor this function to use async/await"
2. **Set constraints** — "Don't change the public API"
3. **Review diff** — Check all changes
4. **Run tests** — Verify nothing broke
5. **Commit** — With descriptive message

---

## Connection to [[concepts/agentic-engineering.md]]

These best practices embody the agentic engineering philosophy:

| Agentic Engineering Principle | Claude Code Practice |
|-------------------------------|----------------------|
| Human directs, AI executes | Sub-agent delegation with clear prompts |
| Test-driven development | Write tests first, AI implements |
| Continuous review | Verify all AI output before commit |
| Context management | CLAUDE.md, session hygiene |
| Tool augmentation | MCP servers for extended capabilities |

---

## Related Concepts

- [[concepts/agentic-engineering.md]] — The broader methodology these practices serve
- [[inference-speed-development]] — How these practices enable faster iteration
- [[claude-code-source-patterns]] — Internal patterns that inform user practices
- [[context-window-management]] — Techniques for managing conversation context
- [[ai-coding-reliability]] — Why review and verification are essential

## Sources

- [Sankalp: My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) — Primary source for patterns and best practices
- [Anthropic: Claude Code Documentation](https://docs.anthropic.com/claude-code) — Official MCP and CLAUDE.md guidance
- [r/ChatGPTCoding: Claude Code Discussions](https://www.reddit.com/r/ChatGPTCoding/) — Community-sourced tips and workflows
