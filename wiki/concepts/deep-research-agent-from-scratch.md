---
title: "Deep Research Agent from Scratch"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - deep-research
  - ai-agents
  - planning-agent
  - agent-loop
  - architecture
  - research-agent
aliases: [build-your-own-deep-research-agent, deep-research-from-scratch, research-agent-pipeline]
sources:
  - raw/articles/2026-03-28_youtube_deep-research-agent-workshop.md
  - raw/articles/2026-03-28_github_deep-research-agent-readme.md
---

# Deep Research Agent from Scratch

**A 10-step pipeline to build a deep research agent from scratch**, systematized at a March 2026 workshop by Ivan Leo (Google DeepMind, ex-Manus) and Hugo Bowne-Anderson. It builds end-to-end from raw Gemini API calls through clarifying questions, research plan generation, parallel dynamic sub-agent spawning (Exa search), and citation-attached report synthesis.

## The 10-Step Build Pipeline

```
Step 1: Raw API Call      -> Observe Gemini function calls
Step 2: Single Tool        -> Execute read_file, return results
Step 3: Tool Runtime       -> Tool dataclass + AgentRuntime (dispatch by name)
Step 4: State & Context    -> Separate RunConfig, RunState, AgentContext
Step 5: Hooks              -> Decouple rendering via .on() event system
Step 6: Agent Loop         -> run_until_idle() - loop until model stops tool calling
Step 7: Subagents          -> Spawn child Agent instances in parallel, delegate Exa search
Step 8: Beautiful Outputs  -> Rich rendering via hooks (diff, syntax highlight)
Step 9: Plan Generation    -> plan/execute mode switching + generate_plan tool
Step 10: OpenTelemetry     -> Full trace visualization via Logfire
```

## Core Architecture

### Phase Swapping: Plan -> Execute

The core of this architecture is **phase swapping**:

```python
class RunState:
    mode: Literal["plan", "execute"] = "plan"
    todos: list[Todo] = []
```

**Plan mode**:
- Only tool available is `generate_plan`
- Agent generates **clarifying questions** for ambiguous user queries
- Creates a research plan (Todo list) based on responses
- Switches to `mode = "execute"` when plan is complete

**Execute mode**:
- All tools (read, write, search, bash) become available
- Spawn sub-agents in parallel according to the Todo list
- Each sub-agent performs web searches via Exa
- Synthesizes results into a report with citations

> *"Phase swapping is how the agent moves from planning to execution — it's not two separate agents, it's one agent with two modes."*

### Deterministic Guardrails

Prevents agents from finishing without completing all Todos:

```python
def run_until_idle(self) -> str:
    while True:
        response = self._run_one_turn()
        if response.is_text:
            if self.state.is_incomplete():
                # Nudge: "You have unfinished todos. Complete them before responding."
                self.contents.append(nudge_message)
                continue  # Force another turn
            return response.text
```

- `state.is_incomplete()` checks for unfinished Todos
- Injects a nudge message if unfinished, forcing another turn
- **Even if the model says "done," the harness doesn't allow it**

### Dynamic Subagent Spawning

```python
class Agent:
    def spawn_subagent(self, prompt: str, tools: list[str]) -> Agent:
        child = Agent(
            config=RunConfig(model=self.config.model, max_iterations=5),
            state=RunState(todos=[], mode="execute"),
            tools=[t for t in self.tools if t.name in tools],
        )
        return child
```

- Parent agent spawns **any number** of child agents as needed
- Each child has its own RunState, iteration budget, and tool set
- Search queries executed in parallel via `asyncio.gather()`
- Each sub-agent handles web searches via the Exa API

## Design Decisions & Trade-offs

### Build Your Own vs. Provider SDKs

Key insight from Ivan Leo at the workshop - why Manus had to build its own runtime:

| Aspect | Provider SDK (e.g. Claude Agent SDK) | Build Your Own |
|--------|--------------------------------------|----------------|
| Learning Curve | Low | High |
| Control Granularity | Depends on SDK abstraction | **Full control** |
| Debugging | Easy to black-box | All layers visible |
| Production | Depends on SDK updates | Self-managed |
| Manus' Choice | No | Yes, after 5 re-architectures |

> *"Manus had no choice but to build their own runtime. When you're shipping to millions of users, you need control over every layer — retry logic, error handling, context management. Provider SDKs abstract too much away."* — Ivan Leo

### Why Tool Calling Beats Parsing Text Output

- Parsing text output is fragile (breaks on subtle JSON format differences)
- Function calling enforces **type contracts** - argument schemas are pre-defined for called functions
- Easier to write defensive code against invalid arguments and unknown tool calls

### Start With the Best Model, Then Optimize Down

- First verify the task is **actually achievable** with Gemini 2.5 Pro (best performance)
- If achievable, downgrade to Flash or cheaper models for optimization
- **Cost optimization comes after validation** - starting with cheap models and giving up is the worst pattern

## Key Design Patterns

### 1. State Separation

```python
@dataclass
class RunConfig:       # Immutable configuration
    model: str
    max_iterations: int
    user_confirmation: bool

@dataclass  
class RunState:        # Mutable execution state
    iteration: int = 0
    mode: str = "plan"
    todos: list[Todo] = field(default_factory=list)

@dataclass
class AgentContext:    # External dependency injection
    api_keys: dict
    working_dir: Path
```

**Clear separation of Config (immutable), State (mutable), and Context (external dependencies)** enables testability and independent sub-agent spawning.

### 2. Todo-Driven Execution

The agent manages its own Todo list:

```
User: "Research the impact of AI on software engineering"
  → Plan mode: Agent generates clarifying questions
  → User answers
  → Agent creates Todo list:
      1. [pending] Search: AI coding assistant adoption rates
      2. [pending] Search: developer productivity studies
      3. [pending] Search: job market impact of AI tools
      4. [pending] Synthesize findings into report
  → Execute mode: Spawns 3 subagents (parallel), then synthesizes
```

### 3. Hooks for Lifecycle Events

Decouples rendering from the core loop (same pattern as [[concepts/agents-that-build-themselves]]):

```python
agent.on("message", lambda msg: print(f"[{msg.role}]: {msg.content}"))
agent.on("llm_tool_call", lambda call: print(f"🔧 Calling {call.name}..."))
agent.on("tool_result", lambda result: print(f"✅ {result.name} done"))
```

### 4. Don't Break Your Cache

Ivan Leo's production lesson:

- Changing a tool's `description` field breaks the model's tool selection pattern
- Cached function calling schemas become invalidated
- **Backward compatibility** of tool definitions is crucial in production

## When Deep Research Makes Sense

| Good fit | Poor fit |
|---|---|
| Cross-referencing multiple sources needed | Single fact-check |
| Search path evolves during exploration | Summarizing known info |
| Competitive analysis, tech research, lit reviews | Routine data retrieval |
| Conflicting sources need synthesis | Computation or transformation |

> *"Deep research is not the right tool for everything. Sometimes a single web search is faster and better. Know when to use what."* — Hugo Bowne-Anderson

## Production Observability (Step 10)

Full tracing via OpenTelemetry + Logfire:

```
┌─ Turn Span (per agent run) ──────────────────────┐
│  model: gemini-2.5-pro                            │
│  tokens: 4,200 input / 850 output                 │
│  ├─ tool_call span: search_exa("AI adoption...")  │
│  │  └─ tool_executed span: 5 results, 1.2s        │
│  ├─ tool_call span: search_exa("developer...")    │
│  │  └─ tool_executed span: 3 results, 0.9s        │
│  └─ subagent span: delegated_search               │
│     └─ (child agent's own turn spans)             │
└──────────────────────────────────────────────────┘
```

[Logfire Public Trace](https://logfire-us.pydantic.dev/public-trace/eb9a4dec-edd0-439e-941e-0ce43dcc8c48?spanId=47d016809c9b61f0)

## Sample Output

Step 10 agent output example -> [`airpods_report.md`](https://github.com/hugobowne/build-your-own-deep-research-agent/blob/main/airpods_report.md) - generates a structured report with citations for research queries.

## Related Concepts

- [[concepts/agents-that-build-themselves]] - Previous workshop by Hugo + Ivan Leo on tool factories, hot reload, hooks
- [[concepts/subagents]] - Sub-agent parallel delegation patterns
- [[concepts/research-agent-fundamentals]] - Anthropic Claude Agent SDK research agent
- [[concepts/agentic-loop]] - Agent loop basics
- [[concepts/pi-autoresearch]] - Pi autoresearch feature
- [[concepts/karpathy-rl-agents-agentic-research-loop]] - Karpathy RL agents + research loop

## References

- [Build Your Own Deep Research Agent (YouTube, 89min)](https://www.youtube.com/watch?v=LUfqQgz1-Os) — Full live build session
- [GitHub: build-your-own-deep-research-agent](https://github.com/hugobowne/build-your-own-deep-research-agent) - 10-step companion code
- [[entities/hugo-bowne-anderson]] - Host, Vanishing Gradients
- [[entities/ivan-leo]] - Co-host, Google DeepMind (ex-Manus)
