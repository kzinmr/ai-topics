---
title: "Context Repositories (Git-based Agent Memory)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags:
  - context-management
  - context-engineering
  - memory-systems
  - coding-agents
  - developer-tooling
  - ai-agents
sources:
  - "[[raw/articles/2026-02-12_letta_context-repositories]]"
related:
  - "[[concepts/agent-memory]]"
  - "[[concepts/letta-code]]"
  - "[[concepts/progressive-disclosure]]"
  - "[[concepts/context-engineering|Context Engineering]]"
---

# Context Repositories (Git-based Agent Memory)

Context Repositories are a **Git-based agent memory management** architecture proposed by Letta. By storing agent context on the local filesystem and versioning it with Git, they enable programmable memory operations and concurrent multi-subagent work.

## Background

Limitations of traditional agent memory (MemGPT, memory tools):
- Agents must use **specialized tools** for memory operations → limited expressiveness
- No support for **concurrent memory writes** by multiple sub-agents
- No version control → no rollback capability

## Architecture

### Basic Principles

```
Memory = files on the local filesystem
Operations = terminal commands + scripts (bash, Python)
Version control = Git
```

Following Unix philosophy, agents can manipulate memory with standard tools (`grep`, `find`, `cat`, `for` loops).

### Progressive Disclosure

```
context-repo/
├── system/           ← Always fully loaded into system prompt
│   ├── identity.md
│   └── rules.md
├── memory/           ← Only file tree structure shown in prompt
│   ├── user-prefs.md  (frontmatter: description="User preferences")
│   └── project-x.md   (frontmatter: description="Project X learnings")
```

- File hierarchy and filenames serve as **navigation signals**
- Each file's YAML frontmatter contains a **description**
- Only files in `system/` directory are fully loaded
- Agents manage their own file organization and movement

### Multi-Agent Memory Swarm

- **Independent Git worktrees** for each sub-agent
- Concurrent memory processing → resolved via Git merge
- Divide and conquer: multiple sub-agents learn from different perspectives
- Example: `/init` tool learns from Claude Code/Codex history

## Comparison: Context Repositories vs Traditional Approaches

| Aspect | Context Repositories | Traditional Memory Tools | Virtual File System |
|------|---------------------|-----------------|-------------------|
| Operation | Terminal + Scripts | Specialized tool calls | FS operation tools |
| Concurrency | Git merge | Not supported | Not supported |
| Version control | ✅ Git commit | ❌ | ❌ |
| Progressive disclosure | File hierarchy + frontmatter | Tool-dependent | Directory structure only |
| Programmability | All scripting languages | Within tool scope | Within file operation scope |

## Applications

- **Token-Space Learning**: Reprocess and abstract past agent trajectories
- **Continuous Learning**: Accumulate knowledge across sessions
- **Team Memory**: Multiple developers' agents share knowledge

## References

- [Introducing Context Repositories — Letta Blog](https://www.letta.com/blog/context-repositories) (2026-02-12)
- [Effective Context Engineering for AI Agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
