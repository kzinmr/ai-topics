# Process Supervision Patterns for AI Agent Runtimes

Source: Brightlume AI Blog + OmniDaemon (PyPI)
URLs: https://brightlume.ai/blog/long-running-ai-agents-scheduling-durability-recovery
      https://pypi.org/project/omnidaemon/
Capture date: 2026-04-28

---

## Part 1: Long-Running AI Agents — Scheduling, Durability, and Recovery

### Execution Models
- **Synchronous:** Single request context. Fails on timeouts or process crashes.
- **Asynchronous:** Decouples triggers from results. Work is submitted to a queue.
- **Hybrid Model (Recommended):** Sync entry point returns Job ID; agent executes async in background.

### Durability: Surviving Infrastructure Failure

#### Layer 1: Checkpoint-Based State Management
Agents must write state to durable storage after every decision or step.
Key checkpoint data: Execution state, tool results, agent memory, timestamps.

#### Layer 2: Idempotent Tool Calls
Include unique UUIDs in API calls so receivers return cached results for retries.

#### Layer 3: Graceful Degradation & Escalation
Define if a tool is "critical" (stop and escalate) or "optional" (skip and log).

### Recovery Patterns
- **Exponential Backoff:** Doubling wait time between retries.
- **Circuit Breaker:** Reject requests immediately during cooldown after repeated failures.
- **Dead-Letter Queues (DLQ):** Move unprocessable events for later debugging.

### Production Architecture
1. Agent Runtime — engine for logic (LangGraph, Temporal)
2. State Store — database for persisting checkpoints
3. Message Queue — for async task distribution
4. Tool Registry — versioned catalog of skills
5. Observability Layer — tracing and metrics

### Framework Selection
| Option | Best For | Pros |
|--------|----------|------|
| Dedicated (Temporal) | Mission-critical reliability | Built-in durability, battle-tested |
| LLM Framework (LangGraph) | Teams in ecosystem | Flexible, good features |
| Custom Build | Unique use cases | Total flexibility |

## Part 2: OmniDaemon — Agent Supervisor

OmniDaemon manages agents in isolated processes, often described as "Kubernetes for AI Agents."

### The Agent Supervisor — Lifecycle State Machine
- IDLE → STARTING → RUNNING → STOPPING → STOPPED
- RUNNING → CRASHED → STARTING (auto-restart)
- CRASHED → STOPPED (max retries exceeded)

### Benefits
- **Fault Isolation:** If Agent A crashes, Agent B remains unaffected.
- **Resource Safety:** Strict memory/CPU boundaries per agent.
- **Observability:** Built-in metrics, logs, and state tracking.
- **Reliability:** Retries, Dead Letter Queues, and heartbeats.

### Implementation
```python
supervisor = await create_supervisor_from_directory(
    agent_name="greeter",
    agent_dir="./my_first_agent",
    callback_function="agent.greeter_callback"
)
```
