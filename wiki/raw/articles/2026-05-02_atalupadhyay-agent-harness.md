---
title: "The Agent Harness: What It Is, Why It Matters, and How to Build One from Scratch"
source: "atalupadhyay.wordpress.com"
author: "Atal Upadhyay"
date: 2026-05-02
url: "https://atalupadhyay.wordpress.com/2026/05/02/the-agent-harness-what-it-is-why-it-matters-and-how-to-build-one-from-scratch/"
x_bookmark_id: "2050631735529095575"
x_author_id: "1639972809781673984"
tags: [agent-harness, harness-engineering, agent-architecture, llm-agents]
---

# The Agent Harness: Architecture, Components, and Implementation

This guide defines the "Agent Harness"—the architectural layer that transforms a Large Language Model (LLM) into a persistent, autonomous problem solver.

## Part 1: Defining the Agent Harness
An **agent harness** is a fixed, pre-wired architecture that turns a one-shot LLM into a persistent, action-taking problem solver.

### The Engine vs. Car Analogy
*   **LLM (Engine):** High performance but stationary; it revs (processes) and stops.
*   **Harness (Chassis/Controls):** The steering, brakes, and fuel lines that wrap around the engine.
*   **Agent (Complete Car):** The resulting system capable of reaching a destination (goal).

### Harness vs. Framework
| Aspect | Framework (e.g., LangChain, CrewAI) | Harness (e.g., Claude Code, Cursor) |
| :--- | :--- | :--- |
| **Purpose** | Building blocks to *assemble* an agent. | A *working* agent out of the box. |
| **Control Flow** | User defines the graph/state machine. | Fixed `while` loop with escape hatches. |
| **Mental Model** | "I will build an agent." | "I will give it a task and let it run." |

---

## Part 2: The 9 Core Components
1.  **The `while` Loop:** The heartbeat that manages the "Decide → Act → Observe" cycle. Must include `max_iterations` to prevent infinite loops.
2.  **Context Management:** Handles token budgeting. When limits are reached, it triggers **compaction** (summarizing old turns while keeping recent ones verbatim).
3.  **Tools & Skills Registry:** A map of capabilities (e.g., `read_file`, `run_bash`) with defined schemas and permission levels.
4.  **Sub-Agent Management:** Spawns isolated sessions for parallel or complex tasks to prevent single-thread "choking."
5.  **Built-In Skills:** Out-of-the-box capabilities like file operations and code navigation.
6.  **Session Persistence:** Append-only logs (JSON/Markdown) that allow the agent to resume after crashes.
7.  **System Prompt Assembly:** Dynamically injects project-specific rules (e.g., `.cursor/rules`) into a static core prompt.
8.  **Lifecycle Hooks:** Pre-tool and post-tool hooks for auditing, modifying, or blocking actions.
9.  **Permissions & Safety:** A hierarchy (`read`, `workspace`, `full`) that classifies commands and requires human approval for destructive actions.

---

## Part 3: Minimal Python Implementation
This reference implementation demonstrates the core logic of a harness.

### Key Logic: The Execution Loop (`main.py`)
```python
def main():
    # ... Initialization of Registry, Context, Memory ...
    for i in range(config.MAX_ITERATIONS):
        ctx.compact()
        context = ctx.get_context()
        
        response = mock_llm_call(system_prompt, context)
        
        if response["type"] == "text":
            print(f"🤖 Agent: {response['content']}")
            break
        elif response["type"] == "tool_call":
            tool_name = response["tool"]
            # Pre-hook check & Permission check
            if not check_permission(tool_def.permission, current_mode):
                print(f"🔒 Permission denied")
                break
            # Execute
            output = registry.dispatch(tool_name, response["args"])
            ctx.add("user", f"[Tool Result] {output}")
```

### Safety Classification (`permissions.py`)
```python
DANGEROUS_COMMANDS = ["rm", "del", "sudo", "shutdown"]

def classify_bash_permission(cmd: str) -> str:
    cmd_lower = cmd.lower().strip()
    if any(c in cmd_lower for c in DANGEROUS_COMMANDS):
        return "full"
    return "workspace"
```

---

## Part 4: Production Scaling & Pitfalls

### Critical Production Layers
*   **Real LLM Integration:** Use tools like OpenAI or Anthropic SDKs with `tool_choice="auto"`.
*   **Semantic Compaction:** Use a smaller LLM to summarize history while preserving function signatures and error traces.
*   **Prefix Caching:** Always keep the **static core prompt first**. Changing the order of dynamic content invalidates the cache, causing 3-5x latency spikes.

### Common Pitfalls
| Issue | Symptom | Fix |
| :--- | :--- | :--- |
| **Context Bloat** | Latency spikes | Strict token caps + semantic compaction. |
| **Permission Bypass** | `rm -rf /` executes | Parse commands via AST/shlex, not just strings. |
| **State Leakage** | Sub-agents mess up parent files | Use isolated `tmpdirs` and read-only mounts. |

---

## Part 5: Architectural Insights for Interviews
*   **On Context Limits:** Use a multi-tier approach: Recent turns (verbatim) + Older turns (summarized) + Critical state (structured memory).
*   **On Sub-Agents:** Use them for independent tasks (parallel analysis) or when different tool sets are required (frontend vs. backend).
*   **On Safety:** Implement a "Sandbox" approach using restricted containers and interactive approvals for "full" tier commands.

> **Final Thought:** "Don't just prompt the model. Engineer the loop. The harness is where agency becomes reliable."
