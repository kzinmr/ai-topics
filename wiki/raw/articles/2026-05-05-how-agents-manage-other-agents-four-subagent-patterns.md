---
title: "How Agents Manage Other Agents: Four Subagent Patterns in 2026"
source: "x-bookmarks"
author: "Philipp Schmid"
date: "2026-05-05"
url: "https://www.philschmid.de/subagent-patterns-2026"
tweet_id: "2051674663965606052"
bookmarks: 488
likes: 304
retweets: 35
---

# How Agents Manage Other Agents: Four Subagent Patterns in 2026

By Philipp Schmid, May 5, 2026.

This report outlines four evolving architectural patterns for multi-agent systems, categorized by the level of control a "main agent" exerts over its "subagents." As models improve in planning and tool use, workflows are shifting from simple task isolation to complex, autonomous agent teams.

---

## 1. Inline Tool: Subagent as a Function Call
The simplest and most common pattern. The main agent treats a subagent exactly like a standard tool (e.g., `read_file`).

* **Mechanism:** The main agent calls a tool (e.g., `call_agent`), which spawns a subagent, executes a task, and returns the result as a tool response.
* **Sync vs. Async:**
    * **Sync:** The main agent blocks until the subagent finishes.
    * **Async:** The tool returns an `agent_id` immediately. The result is later injected into the conversation as a notification message.
* **Best For:** Self-contained tasks like research lookups, code reviews, or test generation.
* **Limitations:** No way to send follow-up instructions or course-correct mid-task.

## 2. Fan-Out: Spawn and Wait
The main agent dispatches multiple tasks and decides when to collect the results. Spawning and collecting are decoupled.

* **Mechanism:** Uses two tools: `spawn_agent` (returns an ID immediately) and `wait_agent` (blocks until one or more agents finish).
* **Key Advantage:** Allows the main agent to interleave its own work while subagents run in parallel.
* **Best For:** Multiple independent tasks that can run concurrently without needing intermediate results from each other.
* **Limitations:** Requires the model to know when to wait; calling `wait_agent` immediately after spawning negates the parallel benefit.

## 3. Agent Pool: Persistent Messaging
Subagents are long-lived, stateful, and interactive. The main agent acts as a coordinator between specialists.

* **Mechanism:** A rich toolset including `spawn_agent`, `send_message`, `wait_agent`, `list_agents`, and `kill_agent`.
* **Key Advantage:** Subagents retain conversation history. The main agent can send a task, receive a draft, send feedback, and ask for a revision.
* **Best For:** Multi-step workflows (e.g., a Researcher finding data and a Writer using that data to draft a post).

## 4. Teams: Direct Inter-Agent Communication
The main agent acts as a high-level supervisor. It sets up the team and then steps back, allowing subagents to message each other directly.

* **Mechanism:** Subagents have their own `send_message` tools to address teammates by name or path.
* **Key Advantage:** Keeps the main agent's context clean. Complex coordination logic happens "under the hood."
* **Best For:** Large-scale tasks where coordination logic exceeds what a single agent can manage.
* **Limitations:** High risk of "agent loops" (A waits for B, B waits for A). Requires frontier-class models for every member of the team.

---

## Summary Comparison Table

| Pattern | Tools | Main Agent Role | Agent Lifetime |
| :--- | :--- | :--- | :--- |
| **Inline Tool** | `call_agent` | Caller | Single task |
| **Fan-Out** | `spawn`, `wait` | Dispatcher | Single task |
| **Agent Pool** | `spawn`, `send`, `wait`, `list`, `kill` | Coordinator | Multi-turn |
| **Teams** | All above + cross-agent `send` | Supervisor | Persistent |

---

## Actionable Insights for Implementation

1. **Start Simple:** Begin with Pattern 1 (Inline Tool). Most multi-agent needs are actually just well-prompted single-task calls.
2. **Model Selection:**
    * Patterns 1 & 2: Work well with smaller, cheaper models.
    * Pattern 3: Requires models capable of tracking multi-agent states across turns.
    * Pattern 4: Requires frontier models (e.g., GPT-4o, Claude 3.5 Sonnet) for all roles to prevent coordination collapse.
3. **Result Collection:** In advanced patterns (2-4), the framework provides the tools, but the model controls the orchestration. The developer must ensure the model understands it is responsible for calling `wait_agent` or `kill_agent` to manage resources.
4. **Future Proofing:** A task requiring four coordinated agents today may be solvable by a single, more capable model tomorrow. Design for flexibility.
