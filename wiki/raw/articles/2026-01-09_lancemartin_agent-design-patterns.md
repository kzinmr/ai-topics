# Agent Design Patterns

**Source:** https://rlancemartin.github.io/2026/01/09/agent_design
**Date:** January 9, 2026
**Author:** Lance Martin

---

**2025 milestones**: Meta buys Manus for **>$2B**, Claude Code reaches **$1B run rate**. Context management is the core challenge driving agent design.

## The Context Challenge

- Agent task length doubles every **7 months** (@METR_Evals), but model performance degrades as context grows ("context rot", failure modes).
- **Context is a finite resource** with diminishing returns — LLMs have an "attention budget."

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step."
> — @karpathy

## 1. Give Agents a Computer

Agents direct their own actions. Giving them primitives like a **filesystem** (persistent context) and a **shell** (run built-ins, CLIs, or self-written code) is fundamental.

> "The fundamental coding agent abstraction is the CLI … agents need access to the OS layer."
> — @rauchg

## 2. Multi-Layer Action Space

- **Problem**: Loading many tool definitions overloads context (e.g., GitHub MCP server: **35 tools, ~26K tokens** just for definitions), and overlapping tools confuse models.
- **Solution**: Keep the tool-calling layer lean; push broad actions to the computer.

| Agent         | Reported tool count |
|---------------|----------------------|
| Claude Code   | ~**12** tools |
| Manus         | **<20** tools |
| Amp Code      | "only a few" |

**How they still perform many actions**: Use a hierarchical action space. A bash tool can invoke shell utilities, CLIs, or write/execute arbitrary code. The **CodeAct paper** showed agents can chain many actions by writing and executing code — this also saves tokens because the agent does not process intermediate tool results.

## 3. Progressive Disclosure

Show only essential information upfront; reveal details on demand.

- **At the tool-calling layer**: Index tool definitions and retrieve tools on demand.
- **For computer-side utilities/CLIs**: Manus provides a list of available commands; agent uses `--help` to learn about any one when needed.
- **For MCP servers**: Cursor Agent syncs MCP tool descriptions to a folder, gives a short list, and lets the agent read full descriptions only if the task requires.
- **Skills (Anthropic standard)**: `SKILL.md` files with YAML frontmatter. Frontmatter loaded into agent instructions; the agent reads `SKILL.md` only if necessary.

## 4. Offload Context

Shift context out of the agent's window to the filesystem.

- Manus writes old tool results to files; summarisation is applied only when offloading shows diminishing returns.
- Cursor Agent stores tool results and agent trajectories on disk; agent can read them back if needed.
- This mitigates **information loss** from compaction (summarisation).
- A plan file can be written and periodically read back to reinforce objectives or verify work.

## 5. Cache Context

Agents manage context as a linear list of messages (append-only). That makes **prompt caching** critical — without it, costs explode.

- Manus calls **"cache hit rate"** the most important production metric.
- A more expensive model with high cache hit rate can be *cheaper* than a lower-cost model without caching.
- @trq212: coding agents (Claude Code) would be **cost-prohibitive** without caching.

## 6. Isolate Context – Sub-Agents & the "Ralph Wiggum" Loop

Delegate tasks to sub-agents with **isolated context windows, tools, and instructions**.

- **Parallelisation**: Claude Code uses sub-agents for code review (map-reduce pattern).
- **Ralph Wiggum loop**: An initializer agent sets up environment (plan file, tracking file); sub-agents tackle individual tasks from the plan file. Stop hooks verify work after each loop iteration.
- **Context sharing via filesystem**: Progress communicated across agents through git history.

## 7. Evolve Context – Continual Learning in Token Space

- **Memories**: Agents can learn and accumulate skills over time.
- **Sleep-time compute**: Agents reflect on past sessions during "offline" periods to update memories or skills.
- **@Letta_AI**: Shows agents can think offline about their own context.
- **@jeffreyhuber**: Suggests models may learn to perform their own context management, reducing need for hand-crafted approaches.

## The Bitter Lesson

The Bitter Lesson predicts that compute/model scaling often overtakes hand-crafted approaches. For example, rather than manual compaction, **Recursive Language Models (RLM)** from @lateinteraction, @a1zhang, @primeintellect suggest LLMs can learn to perform their own context management. Much of the prompting or scaffolding packed into agent harnesses might get absorbed by models over time.

> Context management can include hand-crafted prompting for compression, spawning sub-agents, determining when / what context to offload, and how to evolve context for learning over time. The Bitter Lesson predicts that compute / model scaling often overtakes such hand-crafted approaches.
