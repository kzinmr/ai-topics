---
title: "Model Switching in Graph Workflows"
type: concept
created: 2026-08-10
updated: 2026-08-10
tags:
  - multi-agent
  - kv-cache
  - orchestration
  - model-routing
  - context-management
  - inference
  - optimization
  - harness-engineering
aliases:
  - model-switching
  - cross-model-context
  - graph-model-switching
sources:
  - raw/articles/2026-06-29_cognition-devin-fusion-multi-model-harness.md
  - raw/articles/2026-07-25_akshay-pachaar_graph-engineering-clearly-explained.md
  - "https://langchain-ai.github.io/langgraph/"
  - "https://microsoft.github.io/autogen/"
  - "https://docs.llamaindex.ai/"
---

# Model Switching in Graph Workflows

## Summary

Model switching in graph-based agent workflows is the problem of changing which LLM handles a given node (or turn) in a multi-node graph, while managing the **KV cache cost** of that switch and preserving **context continuity** across different models. Unlike single-model loops where the KV cache accumulates incrementally, graph workflows with heterogeneous model nodes face a fundamental tension: **each model switch is a cache miss**, and different models have incompatible KV cache formats. This page documents the technical landscape, existing solutions, and open problems.

## The Core Problem

In a graph workflow (LangGraph, AutoGen GraphFlow, LlamaIndex Workflows, Google ADK 2.0), nodes can use different models:

```
[Research Node: Opus 4.8] → [Draft Node: Kimi 2.6] → [Review Node: Fable 5]
```

Each model transition involves:

1. **KV cache invalidation** — The outgoing model's KV cache is model-specific (different architectures, attention heads, layer counts). It cannot be reused by the incoming model.
2. **Context reconstruction** — The incoming model must re-process shared state as fresh tokens, paying full prefill cost.
3. **Information loss risk** — Context that was "understood" by one model through its accumulated attention patterns must be re-encoded for a different model with different attention behavior.

This is fundamentally different from single-model multi-turn, where the KV cache grows incrementally and each new turn only requires prefilling the delta.

## KV Cache Architecture: Why Model Switches Are Expensive

### Per-Model Cache Format

KV caches are model-specific. Each model has:
- Different numbers of layers and attention heads
- Different head dimensions and hidden sizes
- Different attention mechanisms (MHA, GQA, MLA, SWA)
- Different positional encodings (RoPE variants, ALiBi)

A KV cache from DeepSeek V4 (MLA with compressed latent vectors) is **structurally incompatible** with a KV cache from Claude Opus (standard MHA/GQA). There is no zero-copy transfer possible.

### Cost of a Model Switch

When a graph node transitions from Model A to Model B:

| Operation | Cost | Notes |
|-----------|------|-------|
| **Evict Model A's KV cache** | GPU memory freed | A's attention state is discarded |
| **Load Model B's weights** | If not already loaded | Cold start: seconds. Warm: milliseconds |
| **Prefill context for Model B** | Full prefill of shared state | O(n) where n = context length |
| **Lost cache affinity** | Repeated across graph executions | Unless KV-aware routing preserves B's cache between runs |

For a 32K-token context, a model switch means Model B must re-process all 32K tokens as a fresh prefill — no shortcut. This is why **Claude Code explicitly prohibits mid-session model switching**: "Cache is per-model. Switching mid-conversation is more expensive than continuing."

Source: [[entities/claude-code|Claude Code]] prompt caching architecture (April 2026)

### The Compounding Problem

In a multi-node graph with N model switches, the total wasted prefill work is:

```
Total wasted prefill = Σ(context_length_at_switch_i) for i = 1..N
```

For a 5-node graph with 3 different models and 20K-token context, this can mean 60K+ tokens of redundant prefill computation — often more expensive than the actual inference.

## How Frameworks Handle This

### LangGraph

LangGraph is **model-agnostic at the framework level**. It does not manage KV cache — it manages **typed state objects** flowing through graph nodes. Each node is a function that can call any model:

```python
from langgraph.graph import StateGraph

def research_node(state):
    # Uses Opus for deep research
    return {"draft": call_model(model="opus-4.8", messages=state["messages"])}

def write_node(state):
    # Uses cheaper model for drafting
    return {"draft": call_model(model="kimi-2.6", messages=state["messages"])}

def review_node(state):
    # Uses different model for review (avoids self-agreement)
    return {"verdict": call_model(model="fable-5", messages=state["messages"])}
```

**KV cache handling:** LangGraph delegates cache management entirely to the model provider (Anthropic prompt caching, OpenAI cached prompts, etc.). The framework's contribution is **state isolation** — the typed state schema ensures each node receives clean, structured input rather than raw conversation history.

**Key design pattern:** LangGraph's state object with reducers serves as the **context carryover mechanism** between model-switching nodes. The state is the "lingua franca" that survives model transitions — it's plain text/data, not KV cache.

Source: [[concepts/langgraph]], LangGraph low-level concepts (state, schema, reducers)

### AutoGen / AG2

AutoGen models multi-agent coordination as **conversations** between agents. Each agent can use a different model:

```python
researcher = AssistantAgent("researcher", llm_config={"model": "opus-4.8"})
writer = AssistantAgent("writer", llm_config={"model": "kimi-2.6"})
reviewer = AssistantAgent("reviewer", llm_config={"model": "fable-5"})
```

**KV cache handling:** Like LangGraph, AutoGen does not manage cross-model KV cache. Each agent maintains its own conversation history, and model switches happen at agent boundaries. The "conversation" abstraction naturally serializes context into messages — which any model can process.

**Key limitation:** AutoGen's group chat pattern means context accumulates as message history. When a new agent/model joins, it sees the full conversation as text — paying full prefill cost. There is no mechanism to "warm" the new model's cache from the previous model's cache.

Source: [[concepts/ag2-autogen]], [[comparisons/agent-orchestration-frameworks]]

### LlamaIndex Workflows

LlamaIndex Workflows use an event-driven architecture where steps can use different LLMs:

```python
class ResearchWorkflow(Workflow):
    @step
    async def research(self, ctx: Context, ev: StartEvent) -> DraftEvent:
        # Use powerful model for research
        response = await opus.complete(ev.query)
        return DraftEvent(draft=response)

    @step
    async def review(self, ctx: Context, ev: DraftEvent) -> StopEvent:
        # Use different model for review
        response = await fable.complete(ev.draft)
        return StopEvent(result=response)
```

**KV cache handling:** LlamaIndex, like LangGraph and AutoGen, treats LLM calls as opaque API invocations. Cache management is the provider's responsibility. The workflow context (`ctx`) carries state between steps as serializable data.

**LlamaIndex's contribution:** LlamaIndex popularized **context engineering** as a discipline — emphasizing how information is structured and delivered to LLMs matters as much as model capability. This is directly relevant to model switching: the way you structure context for Model A may not be optimal for Model B.

Source: [[entities/llamaindex]]

### Google ADK 2.0

ADK 2.0's workflow runtime uses the same graph pattern, with an explicit design rule: **deterministic code controls predictable routing**; models handle only steps requiring genuine judgment.

**Relevance to model switching:** ADK 2.0's routing philosophy implies that model selection should be deterministic (code-based), not model-decided. This avoids the instability of having a model choose which model runs next.

Source: [[concepts/graph-engineering]]

## Context Carryover Techniques

Since KV cache cannot transfer between models, context must be carried as **text/data**. Several techniques exist:

### 1. Shared State Object (LangGraph Pattern)

The most common pattern. The graph's state object carries structured data between nodes. Each node reads from and writes to specific fields.

**Advantages:** Clean, typed, debuggable. Model-agnostic.
**Disadvantages:** Every model must re-process the state as fresh tokens. No attention-level reuse.

```
State: {research_findings: "...", draft_text: "...", review_notes: "..."}
Node A (Opus) writes → research_findings
Node B (Kimi) reads → research_findings, writes → draft_text
Node C (Fable) reads → research_findings + draft_text, writes → review_notes
```

Source: [[concepts/graph-engineering]] — "Keeping shared state clean" section

### 2. Message History Serialization (AutoGen Pattern)

Context is carried as a list of messages. New agents/models receive the full conversation history.

**Advantages:** Natural for conversational multi-agent patterns.
**Disadvantages:** Grows unboundedly; full prefill cost for each new model. No selectivity about what the new model needs to see.

### 3. Context Compaction Before Switch

Summarize/compress context before passing it to the next model. This reduces prefill cost at the expense of information fidelity.

**Implementation:** Use the outgoing model to produce a structured summary, then feed that summary (not the full history) to the incoming model.

```
Node A (Opus) → produces summary of research → passes summary to Node B (Kimi)
Node B (Kimi) receives 2K summary instead of 50K research context
```

**Trade-off:** 20-60s latency for LLM-based summarization; lossy. But reduces prefill cost dramatically.

Source: [[concepts/context-engineering/context-compaction]]

### 4. Compaction During Switch (Devin Fusion Pattern)

Cognition's key insight: **model switching during context compaction is effectively free**. When a session is compacted anyway (which triggers a cache miss), switching models at that point adds no additional cache penalty.

**How it works:**
1. Lightweight classifier monitors task complexity
2. When context compaction is triggered (approaching window limit), classifier signals whether to switch models
3. The compacted summary becomes the initial context for either model
4. Both models pay the same prefill cost (the compacted summary)

**Result:** 35% cost reduction at maintained quality. 41% with Fable 5 in the harness.

**Key detail:** Both main and sidekick agents maintain **persistent cached contexts** independently. The switch doesn't transfer cache — it transfers the *compacted text* that both models process fresh.

Source: [[concepts/multi-model-synthesis-strategies]], [[raw/articles/2026-06-29_cognition-devin-fusion-multi-model-harness]]

### 5. Task-Guided KV Cache Compaction (Latent Briefing)

The most advanced technique. **Latent Briefing** (Ramp Labs) compacts the orchestrator's reasoning trajectory into a KV cache that the worker model initializes with — but critically, this works **within the same model family** or models sharing the same architecture.

**How it applies to model switching:**

Latent Briefing's architecture is specifically designed for the **orchestrator → worker** pattern where both may use different models:

1. Orchestrator (e.g., Claude Sonnet 4) decomposes the task
2. Orchestrator's reasoning trajectory is forward-passed through the **worker model** (e.g., Qwen-14B)
3. Task prompt generates query vectors via attention to the trajectory
4. Trajectory's KV cache is compacted using these queries as relevance signal
5. Worker initializes with compacted KV cache

**The model-switching insight:** The trajectory is re-encoded through the *worker's* architecture. The orchestrator's model doesn't matter — what matters is that the trajectory is available as text, and the worker model creates its own KV cache from it. The compaction step selects which parts of the trajectory are relevant to the current task.

**Limitations:**
- Requires the trajectory to be available as text (not just KV cache)
- Compaction adds ~1.7s overhead
- The worker model must be loaded to perform the forward pass
- Works best when orchestrator and worker are in the same serving infrastructure

**Results:** 42-57% median worker token reduction. +3pp accuracy gain at optimal thresholds.

Source: [[concepts/latent-briefing]], [[concepts/kv-cache-compaction]]

### 6. KV-Aware Routing for Model Affinity

[[concepts/kv-aware-routing|KV-aware routing]] (NVIDIA Dynamo, Mooncake, vLLM) assigns requests to workers based on KV cache overlap. This has implications for model switching in graphs:

**Application to graph workflows:**
- If a graph repeatedly uses Model B for review nodes, KV-aware routing can ensure all review requests go to the same worker that has Model B's KV cache warm
- This doesn't help with cross-model cache transfer, but it **preserves per-model cache affinity** across graph executions

**NVIDIA Dynamo's prompt stabilization:** Strips session-specific headers to enable KV cache reuse. Without this, the same model's cache is invalidated by varying headers — a 5x TTFT degradation.

Source: [[concepts/kv-aware-routing]]

## Best Practices for Model Switching in Graphs

### 1. Minimize Model Switches

Each model switch is expensive. The graph engineering principle applies: "A node earns its place only if it represents a real specialty — different model, different toolset, or genuinely separate role."

**Rule of thumb:** If two adjacent nodes use different models but similar context, consider merging them into one node with one model.

### 2. Use Compaction as the Switch Point

Following Cognition's pattern: trigger model switches during context compaction, not mid-inference. The compaction cache miss absorbs the switch cost.

### 3. Design State for Model Portability

Structure shared state as **clean, typed data** rather than raw conversation history. Each model should receive only the context it needs:

```python
# Bad: pass everything
state = {"full_conversation": all_messages}

# Good: pass structured, relevant subset
state = {
    "research_findings": summarized_findings,  # 2K tokens
    "current_draft": draft_text,               # 4K tokens
    "review_criteria": criteria_list,           # 1K tokens
}
```

### 4. Use Different Models for Review (Anti-Agreement)

Graph engineering's fourth hard problem: agents on the same model agree too readily. The reviewer node should use a **different model** with **fresh context** — not the full conversation.

Source: [[concepts/graph-engineering]] — "Agents agreeing with each other"

### 5. Budget Caps Per Node

Multiple models running in parallel multiply cost. Put budget caps on each node. A weak verifier in a graph burns money concurrently with the main work.

### 6. Consider the Sidekick Pattern for Cost Optimization

Instead of sequential model switching, run two parallel agents (frontier main + cost-effective sidekick) with persistent cached contexts. Delegate routine work to the sidekick; reclaim for complex work. This avoids the cache miss problem entirely — both models maintain their own caches.

Source: [[concepts/multi-model-synthesis-strategies]]

### 7. Exploit Architectural Similarity

When switching between models of the same family (e.g., Claude Sonnet → Claude Opus), prompt caching can partially reuse the prefix. Anthropic's prompt caching works across models sharing the same tokenizer and system prompt format.

When switching between architecturally similar models (both GQA-based transformers), KV cache *dimensions* may be compatible — but this is not standardized and depends on provider implementation.

## Framework Comparison: Model Switching Support

| Feature | LangGraph | AutoGen | LlamaIndex Workflows | Google ADK 2.0 |
|---------|-----------|---------|---------------------|----------------|
| **Multi-model nodes** | ✅ Any model per node | ✅ Any model per agent | ✅ Any model per step | ✅ Any model per step |
| **KV cache management** | ❌ Delegated to provider | ❌ Delegated to provider | ❌ Delegated to provider | ❌ Delegated to provider |
| **Context carryover** | Typed state object | Message history | Workflow context | Session state |
| **State isolation** | ✅ Typed schema + reducers | ⚠️ Message-based | ✅ Context object | ✅ Session state |
| **Compaction support** | Via harness code | Via harness code | Via harness code | Via harness code |
| **Cache-aware routing** | ❌ External | ❌ External | ❌ External | ❌ External |
| **Model affinity** | ❌ Not managed | ❌ Not managed | ❌ Not managed | ❌ Not managed |

**Key finding:** No major graph framework provides built-in KV cache management for model switching. All delegate to the serving layer (API provider or inference engine). The frameworks' contribution is **state management** — ensuring clean, structured data flows between nodes regardless of which model processes them.

## Advanced: Latent Briefing as Cross-Model Context Bridge

Latent Briefing's most interesting property for model switching is its **task-guided query mechanism**. When the orchestrator's trajectory is compacted for the worker:

1. The **task prompt** (what the worker needs to do) generates query vectors
2. These queries attend to the orchestrator's trajectory
3. Only trajectory segments relevant to the worker's task survive compaction

This means the context transferred between models is **task-filtered** — not a raw dump of everything the previous model saw. This is fundamentally better than passing full message history.

**Application to graph workflows:**

```
[Node A: Opus] produces trajectory T
    ↓
[Latent Briefing] compacts T using Node B's task prompt as query
    ↓
[Node B: Kimi] receives compacted KV cache (task-relevant subset of T)
```

**Current limitation:** Latent Briefing requires the compacting model to be loaded to perform the forward pass. In a multi-model serving environment, this means both models must be available simultaneously — which may not be feasible with limited GPU memory.

**Future direction:** If KV cache formats become standardized (unlikely in the near term), or if latent-space representations become model-agnostic (more plausible with shared architectures), true zero-copy cache transfer between models becomes possible.

Source: [[concepts/latent-briefing]], [[concepts/kv-cache-compaction]]

## Production Lessons

### Maven Clinic: Model Switching Is Never Drop-In

Maven Clinic's production experience (1,000+ test scenarios, LLM-as-judge, manual review) showed that every model swap requires comprehensive re-evaluation. The evaluation harness is the "central operating system for iteration."

> "If anyone says they can swap a model and know with no manual review that it'll be better, they're lying." — William Horton, Maven Clinic

Source: [[concepts/production-ai-agents]]

### Claude Code: Cache Is Per-Model

Claude Code's explicit prohibition of mid-session model switching reveals a fundamental constraint: prompt caching is model-specific. Switching models invalidates the cache, making it more expensive than continuing with the current model.

**Design implication for graphs:** If your graph uses prompt caching (which Claude Code treats as critical), model switches should be minimized or confined to natural cache boundaries (compaction points, session breaks).

Source: [[entities/claude-code]]

### Augment Prism: Cache Eviction Cost in Routing Decisions

Augment Prism's per-turn router explicitly considers **cache eviction cost** when deciding whether to switch models. The router weighs expected quality gain against the cost of losing the current model's cached state.

**Formula:** `switch_if(quality_gain(model_b) > cache_eviction_cost(model_a))`

This is the first production system that makes model switching economically rational by accounting for cache state.

Source: [[concepts/coding-agents/model-routing]]

## Open Questions

1. **Can KV cache formats be standardized?** If models shared a common KV cache format (even approximately), cross-model cache transfer would become possible. Current trends (MLA, GQA, hybrid attention) are moving in the opposite direction — toward more specialized, model-specific formats.

2. **Is latent-space context transfer the answer?** Latent Briefing shows that task-guided compaction can bridge models. Could this be generalized to a "context interchange format" — a compressed, model-agnostic representation of context?

3. **Do graph frameworks need cache-aware scheduling?** Currently, no framework considers cache state when scheduling nodes. A cache-aware scheduler could batch model switches, warm caches proactively, and route to workers with warm caches.

4. **Will model convergence reduce the problem?** As models converge in capability (GPT-5.6 vs DeepSeek V4 Flash price war), the need for heterogeneous model graphs may decrease. If one model can handle all nodes, the switching problem disappears.

5. **How does DeepSeek V4's 2% KV cache affect this?** DeepSeek V4's Compressed Sparse Attention achieves KV cache at 2% of naive attention at 1M context. If all models adopted similar compression, the absolute cost of cache misses would drop dramatically — potentially making model switching cheaper than context engineering.

## Related Concepts

- [[concepts/graph-engineering]] — The coordination layer where model switching occurs
- [[concepts/multi-model-synthesis-strategies]] — Three approaches to multi-model coordination (Sidekick, Panel, Orchestration)
- [[concepts/kv-cache-compaction]] — Attention-matching framework for KV cache reduction
- [[concepts/latent-briefing]] — Ramp Labs' task-guided KV cache compaction
- [[concepts/kv-aware-routing]] — Request routing based on KV cache state
- [[concepts/coding-agents/model-routing]] — Per-turn model selection with cache-awareness
- [[concepts/context-engineering/context-management]] — Context window management strategies
- [[concepts/context-engineering/context-compaction]] — Context compaction techniques
- [[concepts/langgraph]] — LangGraph framework architecture
- [[concepts/ag2-autogen]] — AutoGen/AG2 multi-agent framework
- [[entities/llamaindex]] — LlamaIndex framework
- [[concepts/production-ai-agents]] — Maven Clinic model switching lessons
- [[entities/claude-code]] — Claude Code's per-model cache constraint
