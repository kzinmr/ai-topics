# Context Engineering for Agents

**Source:** https://rlancemartin.github.io/2025/06/23/context_engineering/
**Date:** June 23, 2025
**Author:** Lance Martin

---

> **TL;DR:** Agents need context to perform tasks. Context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory. This post groups common strategies into **write**, **select**, **compress**, and **isolate**.

## What is Context Engineering?

Andrej Karpathy compares LLMs to operating systems: the LLM is the CPU, the context window is the RAM (working memory). Context engineering curates what goes into that RAM.

> "Context engineering is the … delicate art and science of filling the context window with just the right information for the next step."
> — Andrej Karpathy

**Three core context types managed:**
- **Instructions** – prompts, memories, few-shot examples, tool descriptions
- **Knowledge** – facts, memories
- **Tools** – feedback from tool calls

## Why Context Engineering Matters for Agents

Agents interleave LLM invocations and tool calls, often for long-running tasks. This can:
- Exceed context window limits
- Balloon cost / latency
- Degrade performance through:

| Problem | Description |
|--------|-------------|
| **Context Poisoning** | A hallucination enters the context |
| **Context Distraction** | Context overwhelms the model's training |
| **Context Confusion** | Superfluous context influences responses |
| **Context Clash** | Parts of the context contradict each other |

> "Context engineering … is effectively the #1 job of engineers building AI agents."
> — Cognition

> "Agents often engage in conversations spanning hundreds of turns, requiring careful context management strategies."
> — Anthropic

## Four Core Strategies for Context Engineering

### 1. Write Context
_Save information outside the context window for later use._

- **Scratchpads:** Notes persisted during a session.
  - Can be a file-writing tool, a field in a runtime state object.
  - Example: Anthropic's multi-agent researcher saves its plan to memory to avoid truncation.
- **Memories:** Long-term storage across sessions.
  - **Reflexion** introduced reflection and reuse of self-generated memories.
  - **Generative Agents** synthesized periodic memories from past feedback.
  - Products like **ChatGPT**, **Cursor**, **Windsurf** auto-generate long-term user-agent memories.
- **Three memory types:**
  - **Episodic** – few-shot examples from past interactions
  - **Procedural** – instructions/styles/rules learned over time
  - **Semantic** – facts about the user, codebase, or world

### 2. Select Context
_Pull relevant information into the context window when needed._

- **Scratchpad selection:** Tool call (if file-based) or developer-controlled exposure of state fields.
- **Memory selection:** Simple (always include `CLAUDE.md`) vs. complex (embeddings/knowledge graphs for large collections).
  - ⚠️ Challenge: Incorrect selection can feel intrusive (Simon Willison's example of ChatGPT adding his location to an image).
- **Tools selection:** Apply RAG to tool descriptions to fetch relevant tools (reported 3× selection accuracy improvement).
- **Knowledge selection (RAG):** Windsurf example — AST parsing, semantic chunking, grep/file search, knowledge graph retrieval, re-ranking step.

### 3. Compress Context
_Retain only the tokens necessary for the task._

- **Context Summarization:**
  - **Claude Code** auto-compacts when >95% of context window is used — summarizes full user-agent trajectory.
  - Can be applied after token-heavy tool calls or at agent-agent boundaries.
  - **Cognition** uses a fine-tuned model for summarization to capture critical events.
- **Context Trimming:**
  - Heuristic pruning (e.g., removing older messages).
  - **Provence**: a trained context pruner for Question-Answering.

### 4. Isolate Context
_Split context across sub-agents or environments._

- **Multi-Agent Isolation:**
  - Motivation: separation of concerns (**OpenAI Swarm**).
  - Each sub-agent has its own tools, instructions, and context window, focusing on a narrow sub-task.
  - **Anthropic's multi-agent researcher**: isolated sub-agents outperformed single-agent.
  - Trade-offs: higher token usage (up to 15× more), need for careful planning and coordination.
- **Environment Isolation (Code Agents):**
  - **HuggingFace's deep researcher** uses a CodeAgent that generates code executed in a sandbox. Only selected return values go back into the LLM context.
  - Isolates token-heavy objects (images, audio, large datasets) from the main context.

## Future Directions: Learning to Manage Context

- **In-context RL/RLVF:** Agents can learn to manage their own context via reinforcement learning.
- **Sleep-time compute:** Agents reflect on past sessions and update memories/skills during "offline" periods.
- **The Bitter Lesson:** Compute scaling may eventually absorb many hand-crafted context management techniques into the model itself. However, for now, explicit context engineering remains essential for practical agents.
