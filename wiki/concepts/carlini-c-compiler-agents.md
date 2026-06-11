---
title: "Carlini C Compiler Agent Team"
type: concept
created: 2026-05-08
updated: 2026-05-26
tags:
  - multi-agent
  - architecture
  - claude-code
  - harness-engineering
  - methodology
aliases:
  - C compiler agent team
  - parallel Claude agents
  - Nicholas Carlini compiler
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_building-c-compiler.md
  - https://www.anthropic.com/engineering/building-c-compiler
related:
  - agent-team-swarm
  - multi-agent-orchestration-architecture
  - effective-harnesses-for-long-running-agents
  - building-effective-agents
---

# Carlini C Compiler Agent Team

Nicholas Carlini (Anthropic Safeguards team) conducted an experiment running 16 Claude agents in parallel to build a Rust-based C compiler from scratch. A validation of agent team architecture limits and a treasure trove of practical insights.

## Experiment Overview

| Item | Value |
|------|-------|
| Agent Count | 16 parallel agents |
| Claude Code Sessions | ~2,000 |
| API Cost | $20,000 |
| Deliverable | 100,000 lines of C compiler |
| Validation | Successfully compiles Linux 6.9 kernel on x86/ARM/RISC-V |

## Architecture

### Infinite Agent Loop

```bash
while true; do
    COMMIT=$(git rev-parse --short=6 HEAD)
    claude --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)" \
           --model claude-opus-X-Y &> "$LOGFILE"
done
```

A simple loop where agents autonomously select the next task upon completion.

### Parallel Task Locking

Minimal Git-based synchronization mechanism:
- Agents write files like `current_tasks/parse_if_statement.txt` to claim locks
- On conflict, git synchronization forces the second agent to select a different task
- Pull → merge → push → unlock cycle

### Container Isolation

Each agent gets a Docker container + `/upstream` mount + `/workspace` local clone.

## Practical Lessons

### 1. Write Extremely High-Quality Tests
> Claude autonomously solves given problems. So if the task verifier isn't nearly perfect, Claude will solve the wrong problem.

- Choosing a high-quality compiler test suite
- Verifying open source package build scripts
- Observing Claude's mistakes → designing new tests

### 2. Think from Claude's Perspective
The importance of environment design. Design tests, environments, and feedback so agents can autonomously find direction.

### 3. Importance of CI/CD Pipelines
Addressing the problem of new features breaking existing functionality through CI/CD and strict test enforcement.

### 4. Using Specialized Agents
- Documentation maintenance agent
- Code quality monitoring agent
- Specialized subtask agents

### 5. Merge Conflicts
Frequent, but Claude is smart enough to resolve them.

## Limitations

- No orchestration agent (minimal prototype)
- No inter-agent communication mechanism
- No high-level goal management process
- Relies on each agent's autonomous judgment (choosing the "next obvious" problem)

## Episodes

Claude once accidentally ran `pkill -9 bash`, killing itself (and the loop).

## See Also

- [[concepts/multi-agents/agent-team-swarm]] — Agent team/swarm architecture overview
- [[concepts/multi-agents/multi-agent-orchestration-architecture]] — Multi-agent orchestration patterns
- [[concepts/effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
- [[concepts/building-effective-agents]] — Building effective agents
- [[harness-design-long-running-apps]] — Harness design for long-running apps
