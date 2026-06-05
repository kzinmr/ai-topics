---
title: "Agents That Build Themselves"
created: 2026-05-13
updated: 2026-06-05
type: concept
tags:
  - self-improving
  - harness-engineering
  - architecture
  - coding-agents
  - ai-agents
sources:
  - raw/articles/2026-02-28_substack_agents-that-build-themselves.md
  - raw/articles/2026-02-28_youtube_openclaw-from-scratch-workshop.md
  - transcripts/2026-02-28_youtube_openclaw-from-scratch-workshop.md
aliases: [self-extending-agents, self-building-agents, self-writing-tools, software-building-software]
---

# Agents That Build Themselves

**Self-extending agents** — a paradigm where agents write their own tools, hot-reload them, and extend their capabilities at runtime. Systematized in a February 2026 workshop by Hugo Bowne-Anderson and Ivan Leo (ex-Manus, Google DeepMind).

> *"Software building software. Agents modifying their own harness."*

## Core Concept

Conventionally in agent development, developers define tools and agents just use them. **Agents That Build Themselves** reverses this:

```
User: "I need a tool that generates files with Notion-style timestamps"
  → Agent reads agent_tools.py (its own tool definition file)
  → Agent writes a new tool class (NotionFileCreator) following the factory pattern
  → Runtime detects file modification via st_mtime
  → importlib.reload() — new tool is registered instantly
  → Agent calls the tool IT JUST WROTE to complete the request
```

This loop works **bidirectionally**: agents can **delete** tools as well as create them. The workshop demoed an agent removing its own bash tool from code, with the runtime detecting and removing it from the registry.

## The Three Enablers

### 1. Factory Pattern (Tool Factory)

Separate tool definitions as classes, decoupling execution logic from schema generation:

```python
class AgentTool(BaseModel):
    """Base class for all tools. Define parameters → auto-generate schema."""
    name: str
    description: str
    
    async def execute(self, ctx: AgentContext) -> ToolResult:
        raise NotImplementedError

class ReadFile(AgentTool):
    path: str
    name = "read_file"
    description = "Read contents of a file"
    
    async def execute(self, ctx: AgentContext) -> ToolResult:
        content = await aiofiles.read(self.path)
        return ToolResult(output=content)
```

**Benefits**:
- New tool = just add a new class to `agent_tools.py`
- Pydantic auto-generates function calling schema from type hints
- `execute()` method is independently testable without an LLM
- Runtime and agent loop are **never changed**

> *"All you need to implement a new tool is define the parameters you want. These are automatically converted into a schema. And you can test your execute function independently of your model being called."* — Ivan Leo

### 2. Hot Reload

Standard Python runtimes load modules once. An agent writing new tools would require a server restart. Hot reload solves this:

```python
class AgentRuntime:
    def __init__(self):
        self._tools_mtime = os.path.getmtime("agent_tools.py")
        self._load_tools()
    
    def _check_reload(self):
        current_mtime = os.path.getmtime("agent_tools.py")
        if current_mtime > self._tools_mtime:
            importlib.reload(agent_tools)
            self._load_tools()
            self._tools_mtime = current_mtime
```

Every time `get_tools()` or `execute_tool()` is called, checks for file changes. If changed, `importlib.reload()` instantly registers new tools.

> *"Because our tools are defined in another file we can just check when the file was last modified. All the tools — they're not concrete things. They're just definitions."*

### 3. Hooks Architecture (Hook System)

Making self-extension practical requires composable side effects for agent actions:

```python
class Agent:
    def __init__(self):
        self._hooks = {
            "on_model_response": [],
            "on_tool_call": [],
            "on_tool_result": [],
        }
    
    async def emit(self, event: str, **kwargs):
        for handler in self._hooks[event]:
            await handler(**kwargs)
```

- **Telegram integration** is just a hook — register a Telegram send handler on `on_model_response`, zero changes to the core loop
- **Pretty output** — Rich library syntax highlighting and visual diffs implemented as hooks
- **Logging/observability** — Logfire recording added as a hook

> *"Literally all we had to do to get the Telegram bot working wasn't any complex functionality — just define on_model_response and on_tool_result Telegram hooks. Everything works out of the box because you have very good primitives."*

## Memory: Markdown Compaction

For self-extending agents to remain useful long-term, they need memory. OpenClaw's approach uses **neither vector DBs nor embeddings**:

1. When conversation exceeds a threshold, summarize with a separate LLM call
2. Append to a timestamped Markdown file in the `memory/` folder
3. Agent reads this file back at startup or as needed

> *"People are so surprised that something simple like appending summaries to a markdown file works so well for memories. A lot of the love that OpenClaw has is just because the model can see the raw chats and the model can see the summaries."*

## The Full Architecture

```
┌─────────────────────────────────────────────────┐
│                  Agent Loop                       │
│  while True:                                     │
│    response = model.generate(contents, tools)     │
│    if response.is_text: return response           │
│    if response.is_tool_call:                      │
│      emit("on_tool_call", ...)    ← hooks         │
│      result = runtime.execute(name, args)         │
│      emit("on_tool_result", ...)  ← hooks         │
│      contents.append(result)                      │
│    runtime._check_reload()        ← hot reload    │
├─────────────────────────────────────────────────┤
│  AgentRuntime (factory + hot reload)              │
│  ┌─────────────────────────────────────────────┐ │
│  │ agent_tools.py (watched for changes)         │ │
│  │   class ReadFile(AgentTool): ...             │ │
│  │   class WriteFile(AgentTool): ...            │ │
│  │   class BashTool(AgentTool): ...             │ │
│  │   class NotionFileCreator(AgentTool): ... ←  │ │
│  │        ↑ agent writes this itself!           │ │
│  └─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────┤
│  Hooks (composable side effects)                  │
│  ├── on_model_response → Telegram send            │
│  ├── on_tool_call → Rich terminal diff            │
│  └── on_tool_result → Logfire observability       │
├─────────────────────────────────────────────────┤
│  Memory (markdown compaction)                     │
│  └── memory/2026-02-28.md ← timestamped summaries │
├─────────────────────────────────────────────────┤
│  Deployment (Modal sandbox)                       │
│  ├── FastAPI webhook server                       │
│  ├── modal.Queue (per-chat-id)                    │
│  └── modal.Sandbox (isolated execution)           │
└─────────────────────────────────────────────────┘
```

## Progressive Disclosure

A key design principle behind self-extension: **more tools is not always better**.

> *"Imagine if someone gave you 200 tools to choose from every time you had to make a decision. You wouldn't even be able to finish reading all of the tools before you had to give a response."* — Hugo Bowne-Anderson

Pi/OpenClaw philosophy: Start with 4 basic tools (read/write/edit/bash); let the agent add tools as needed. This:
- Avoids overwhelming the context window
- Prevents the model from "tool selection paralysis"
- Only extends capabilities when needed

## Safety: Runaway Loop Prevention

Self-extending agent risk: infinite tool-call loops. OpenClaw's mitigation:

```python
# Per-turn tool-call budget
TOOL_CALL_BUDGET = 5
calls_since_user_message = 0

# When budget exceeded:
# - Remove all tools from the API call
# - Inject guardrail instruction: "Summarize and respond to the user"
# - Model is FORCED to stop and produce a text response
```

## Relationship to Pi and OpenClaw

| Aspect | Pi | OpenClaw | This Workshop |
|--------|----|---------|---------------|
| Language | TypeScript | Python wrapper | **Pure Python** |
| Core tools | read/write/edit/bash | read/write/edit/bash | read/write/edit/bash |
| Extensions | TypeScript SDK + npm | Pi SDK + hooks | Factory pattern + hot reload |
| Memory | Claimed unnecessary | Markdown compaction | Markdown compaction |
| Deployment | CLI / RPC / SDK | Modal sandbox | Modal sandbox |
| Self-extension | Skills/packages | Skills + MCP | Agent writes own tool classes |

This workshop is a **Pure Python reconstruction of Pi and OpenClaw's design philosophy**. It shows the same principles can be implemented without TypeScript or npm dependencies.

## Key Insights

1. **Just making tools into classes lets agents write their own tools** — The factory pattern is simple but opens the door to self-extension
2. **Make `execute()` async from day one** — Real-world agents spend most of their time waiting on network I/O
3. **Hooks make agents composable** — Telegram integration, logging, all added without touching the core loop
4. **Markdown appending is sufficient memory** — No vector DBs or embeddings needed
5. **"Empathy" for the model changes design** — Don't give 200 tools at once; disclose progressively

## Armin Ronacher's Perspective: Agents Built for Agents Building Agents

Armin Ronacher (Flask creator, major Pi user/advocate) explains Pi's design philosophy ([January 2026](https://lucumr.pocoo.org/2026/1/31/pi/)), providing the **worldview that is the premise** for the principles Hugo+Ivan's workshop implemented:

> *"Agents Built for Agents Building Agents — software that is malleable like clay. The agent maintains its own functionality."*

### Session Trees

Pi sessions have a **tree structure** with branching and navigation:

```
Main session (building feature X)
  ├── Branch: fix broken extension tool (side-quest)
  │   └── Agent rewrites tool → test → rewind to main
  └── Branch: code review context (fresh, isolated)
```

- Side-quests don't **waste** the main session's context
- After tool fix, returning to main session, Pi summarizes the branch's changes
- Different approach from Hugo+Ivan's `RunState` separation, but same goal: "preventing context pollution"

### Extension State in Sessions

Pi's AI SDK retains **custom messages** in session files in addition to model messages:

- Extensions persist state (not sent to the model)
- Maintain session portability across multiple providers (no dependency on specific provider features)
- Design analogous to Hugo+Ivan's separation of `AgentContext` (external dependency injection) and `RunState` (mutable state)

### No MCP — By Philosophy, Not Laziness

> *"Pi's entire idea is that if you want the agent to do something that it doesn't do yet, you don't go and download an extension or a skill. You ask the agent to extend itself."*

- MCP is intentionally **not supported** — it's philosophy, not laziness
- Design that **celebrates** agents writing their own tools
- Instead of downloaded extensions, tell the agent "look at that extension and modify it like this"

### Software Building Software — The Lived Experience

> *"None of this was written by me, it was created by the agent to my specifications. I told Pi to make an extension and it did. There is no MCP, there are no community skills, nothing. They are hand-crafted by my clanker."*

All of Armin's extensions (browser automation, code review, TODO management, commit message formatting) were **created by the agent itself**. This "software building software" experience is what drove immersion in Pi.

### The Pipeline: Write → Reload → Test → Loop

Pi's hot reload is the same pattern as Hugo+Ivan's `importlib.reload()`, but adds a **test-driven** element:

```
Agent writes extension code → hot reload → agent tests it → fails → rewrites → reloads → passes
```

This establishes an autonomous improvement loop of "iterate until it works." Complementary to Hugo+Ivan's workshop (Step 5 hooks + Step 6 agent loop).

## References

- [Building Agents That Build Themselves (Substack)](https://hugobowne.substack.com/p/building-agents-that-build-themselves) — Hugo Bowne-Anderson, Feb 2026
- [Build Your Own AI Assistant (GitHub)](https://github.com/hugobowne/build-your-own-ai-assistant) — Companion code repo
- [Workshop Livestream (YouTube, 96min)](https://www.youtube.com/watch?v=dDQ4rKXeHRw) — Full live build session
- [[concepts/self-evolving-agents]] — Related concept
- [[concepts/agent-harness]] — Agent harness fundamentals
- [[entities/pi]] — Pi coding agent (Mario Zechner)
- [[entities/openclaw]] — OpenClaw (Peter Steinberger)
- [[concepts/hermes-agent-architecture]] — Hermes Agent architecture (capability accumulation, self-generating skills)
- [[entities/hugo-bowne-anderson]] — Hugo Bowne-Anderson
- [[entities/ivan-leo]] — Ivan Leo

## Transcript Insights (Feb 2026 Workshop)

### Ivan Leo's "Context and Capabilities" Framework

The OpenClaw workshop transcript reveals the mental model Ivan uses for all agent design, attributed to Jason Liu:

> *"If you don't take anything away from today's talk, keep this idea at the back of your head of like context and capabilities. I got this idea from Jason and it's really helped me shape a lot of how I think about building agents."*

- **Context** = what information the model has access to (in the prompt, in memory files, in daily summaries)
- **Capabilities** = what the model can *do* (tools it can call, skills it can load, extensions it can create)

This framework directly motivates the self-extension pattern: when the model lacks a *capability*, it writes a new tool. When it lacks *context*, it reads memory files or creates daily summaries.

### "Build Software to Build Software" — The Core Philosophy

Ivan articulated the fundamental principle behind agents that build themselves:

> *"A lot of it comes down to the fact that you want to build software to build software. And so being able to add whether it's skills, whether it's modifying system prompt, whether it's tools, MCPs — at the end of the day, when you're building an agent, what you're thinking about is: can I give the agent better context?"*

This reframes agent development: you're not building an agent that does task X. You're building an **agent-building system** — a meta-agent that can acquire new capabilities on demand.

### Memory Compaction: How OpenClaw's Daily Files Actually Work

The workshop transcript reveals the specific compaction mechanism:

> *"What happens is that you actually append it to a memory file and so what the model sees is that you interact with it throughout the day — it has a timestamp memory where let's say for example now at 8:47 a.m. in Singapore you might see a simple markdown file with 8:47 a.m. — this is what we did, this is what we discussed with the user, we ran into these issues."*

The compaction flow:
1. Conversation reaches context limit → trigger summarization via a separate LLM call
2. Summary appended to a timestamped Markdown file in the `memory/` folder
3. Raw JSON traces (full conversation) remain accessible to the model
4. At startup or on demand, the model reads both the summary and raw traces

> *"A lot of the love that OpenClaw has is just because the model can see the raw chats and the model can see the summaries."*

### Why Flash Is Good Enough for Self-Extending Agents

Ivan chose Gemini Flash over more expensive models for the workshop, with a practical justification:

> *"Flash is fast enough that it feels like it's almost instant. And so for the use cases of this, and it's also pretty cheap, so I thought I would give it a try."*

This matters for self-extending agents because the tool-writing loop (write → reload → test) requires **many rapid iterations**. A fast, cheap model that can generate valid Python tool classes is preferable to a slow, expensive one for this pattern. The quality bar for tool-writing is lower than for complex reasoning.

### Hugo's Desktop Cleanup Demo: General-Purpose Computer Use

The workshop's opening demo reframed "coding agents" as general-purpose computer-use agents:

> *"We should stop referring to them as coding agents because they really are computer use agents that happen to be good at coding or great at writing code when you give them a bash tool."*

Hugo ran a 133-line agent with 4 tools (read/write/edit/bash) and asked it to organize his messy desktop folder. The agent successfully created a folder hierarchy and moved files — demonstrating that self-extending agents aren't limited to code. Any task expressible as file operations or shell commands is within scope.

### General-Purpose Agents in 133 Lines of Code

The workshop demonstrated that the entire agent loop + tool calling + conversational interface fits in ~133 lines of Python:

> *"You can actually build a general purpose agent in 133 lines of Python code. With four tools: read, write, edit, bash."*

This minimalism is the enabler for self-extension — when the agent's own codebase is small and well-structured, it can understand and modify its own tool definitions without getting lost in framework abstractions.

### Skills and Progressive Disclosure in Practice

The workshop walked through OpenClaw's skill system, which implements progressive disclosure practically:

- Skills are loaded on-demand based on user intent (not all at startup)
- Each skill can register its own tools, hooks, and system prompt extensions
- The agent can discover and load skills dynamically, or the user can request a specific skill

> *"Imagine if someone gave you 200 tools to choose from every time you had to make a decision. You wouldn't even be able to finish reading all of the tools before you had to give a response."* — Hugo Bowne-Anderson

### Sandboxing Self-Extension: Modal Workers

The workshop covered deployment to Modal with sandboxed execution — critical for safety when agents write and execute their own code:

- **Modal Sandbox** isolates agent execution from the host system
- **modal.Queue** provides per-chat-id message routing
- **FastAPI webhook server** bridges external inputs (Telegram, web) to the agent loop
- The agent can write tools, hot-reload them, and execute them — all within the sandbox

This addresses the key safety concern of self-extending agents: the agent's code modifications don't escape the sandbox.
