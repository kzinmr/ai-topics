---
title: "Claude Code Best Practices"
type: concept
aliases:
  - claude-code-best-practices
  - claude-code-patterns
  - agentic-coding-patterns
  - claude-code-tips
  - claude-code-usage-patterns
  - coding-agent-best-practices
created: 2026-04-12
updated: 2026-04-20
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - prompting
  - mcp
  - ai-agents
  - agentic-engineering
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/"
  - "https://docs.anthropic.com/claude-code"
  - "https://code.claude.com/docs/en/claude-code-on-the-web"
  - "https://www.reddit.com/r/ChatGPTCoding/"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/context-engineering|Context Engineering]]"
  - "[[concepts/building-effective-agents]]"
  - "[[concepts/harness-engineering/agentic-engineering]]"
  - "[[concepts/inference-speed-development]]"
  - "[[concepts/claude-code-source-patterns]]"
  - "[[concepts/context-engineering/context-window-management|Context Window Management]]"
  - "[[concepts/ai-coding-reliability]]"
  - "[[concepts/harness-engineering/agentic-workflows/using-git-with-agents]]"
  - "[[concepts/harness-engineering/agentic-workflows/interactive-explanations]]"
---

# Claude Code Best Practices

Best practices for using Claude Code (Anthropic's agentic coding tool) from official Anthropic documentation and experienced users.

## Core Philosophy

> "AI is not magic — it's a very smart intern with an excellent tailwind."
> — Sankalp, after 20 years of programming experience

> "Agentic Environment: Claude Code reads files, runs commands, makes changes, and works autonomously. Shift from 'write & review' to 'describe & verify'."

> "Context window fills fast, and performance degrades as it fills. Every message, file read, and command output consumes tokens. Managing context is the #1 priority."

**The agentic environment requires a shift from "write & review" to "describe & verify." Context management is the top priority.**

## Verification & Workflow

### How to Have Claude Verify Its Work (Highest Leverage)

> "Give Claude a way to verify its work. Without clear success criteria, you become the only feedback loop."

| Strategy | Before | After |
|---|---|---|
| **Provide verification criteria** | `"Implement a function to validate email addresses"` | `"Write a validateEmail function. Test cases: user@example.com returns true, invalid returns false, user@.com returns false. Run the tests after implementation"` |
| **Visual verification of UI changes** | `"Make the dashboard better"` | `"[Attach screenshot] Implement this design. Take a screenshot of the result and compare with the original. List the differences and fix them"` |
| **Address root causes** | `"The build is failing"` | `"The build fails with this error: [paste error]. Fix it and verify the build passes. Address the root cause — don't suppress the error"` |

- **Invest in verification**: Test suites, linters, Bash commands. `"Let's invest in making verification robust"`
- Use the **Claude Chrome extension** for UI iteration

### Explore → Plan → Implement → Commit

Separate exploration from execution to avoid solving the wrong problem.

1. **Explore**: `read /src/auth and understand how we handle sessions and login...`
2. **Plan**: `I want to add Google OAuth. What files need to change? Create a plan.` → edit the plan with Ctrl+G in the editor
3. **Implement**: `implement the OAuth flow from your plan. write tests... run the test suite and fix any failures.`
4. **Commit**: `commit with a descriptive message and open a PR`

For complex or uncertain tasks, use **Plan Mode**. Skip for simple fixes.

## Prompting & Communication

### Provide Specific Context
- **Scope the task**: Specify files, scenarios, test configurations
- **Point to sources**: `"Look at the git history of ExecutionFactory and summarize how the API evolved"`
- **Reference patterns**: `"Look at the existing widget implementation... HotDogWidget.php is a good example. Follow that pattern..."`
- **Describe symptoms**: `"Users report login failures after session timeout. Check the auth flow in src/auth/... Write a failing test that reproduces the issue, then fix it"`

### Have Claude Interview You
For large features:
```text
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.
Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs.
Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```
**Start a fresh session with clean context** to implement the spec.

## CLAUDE.md (Persistent Context)

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

- Generate starter files with `/init`. Keep it **short and human-readable**
- **✅ Include**: Bash commands Claude can't guess, non-standard code styles, test setup, repo etiquette, architecture decisions, environment quirks, common pitfalls
- **❌ Exclude**: What Claude can infer, standard conventions, detailed API docs, frequently changing info, long tutorials, file-by-file explanations, trivial rules
- **Import syntax**: `See @README.md... Git workflow: @docs/git-instructions.md`
- **Location**: `~/.claude/CLAUDE.md` (global), `./CLAUDE.md` (project), `./CLAUDE.local.md` (personal, `.gitignore`), parent/child directories (auto-loaded)

> "If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long." Prune ruthlessly.

### CLAUDE.md Best Practices

1. **Keep it current** — Outdated CLAUDE.md causes more harm than no CLAUDE.md
2. **Be specific, not verbose** — Concrete rules beat general guidance
3. **Include anti-patterns** — "Don't use X" is as valuable as "Use Y"
4. **Version control it** — CLAUDE.md should evolve with the project

## Context Management

> "Managing context is the #1 priority."

**Context is a finite resource.** Anything that wastes context degrades performance.

- **Limit file reads**: Only load the exact files Claude needs. Don't load what can be inferred
- **Minimize output**: Redirect long command output to files. Show only necessary portions
- **Incremental approach**: Break large tasks into small steps. Verify at each step
- **External memory**: Leverage Claude Code's memory files (`memory.md`, etc.)

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

## LSP Hooks for Code Navigation

Community-developed hooks (April 2026) force Claude Code to use LSP (Language Server Protocol) instead of grep for code navigation, saving ~80% tokens:

```bash
# Example hook configuration
# Forces semantic-aware navigation instead of text search
```

- **Token savings**: ~80% reduction in navigation-related token usage
- **Accuracy improvement**: LSP understands symbol definitions, references, and types — grep only does text matching
- **Setup**: Configure hooks in Claude Code to intercept file search commands and route through LSP
- **Source**: Reddit r/LocalLLaMA community (April 14, 2026)

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

## Connection to [[concepts/harness-engineering/agentic-engineering]]

These best practices embody the agentic engineering philosophy:

| Agentic Engineering Principle | Claude Code Practice |
|-------------------------------|----------------------|
| Human directs, AI executes | Sub-agent delegation with clear prompts |
| Test-driven development | Write tests first, AI implements |
| Continuous review | Verify all AI output before commit |
| Context management | CLAUDE.md, session hygiene |
| Tool augmentation | MCP servers for extended capabilities |

## Related Concepts

- [[concepts/harness-engineering]] — Higher-level index
- [[concepts/context-engineering|Context Engineering]] — Context engineering
- [[concepts/building-effective-agents]] — Foundational principles of agent building
- [[concepts/harness-engineering/agentic-workflows/using-git-with-agents]] — Using Git with agents
- [[concepts/inference-speed-development]] — Fast iteration development
- [[concepts/claude-code-source-patterns]] — Claude Code internal patterns
- [[concepts/context-engineering/context-window-management|Context Window Management]] — Context management
- [[concepts/ai-coding-reliability]] — AI coding reliability

## Sources

- [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) — Official best practices
- [Sankalp: My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) — Primary source for patterns and best practices
- [Anthropic: Claude Code Documentation](https://docs.anthropic.com/claude-code) — Official MCP and CLAUDE.md guidance
- [Claude Code on the Web](https://code.claude.com/docs/en/claude-code-on-the-web) — Routines documentation
- [r/ChatGPTCoding: Claude Code Discussions](https://www.reddit.com/r/ChatGPTCoding/) — Community-sourced tips and workflows
