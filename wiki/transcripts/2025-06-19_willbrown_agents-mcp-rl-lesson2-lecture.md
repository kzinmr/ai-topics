---
title: "Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents (Lecture Transcript)"
author: Will Brown
date: 2025-06-19
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: transcript
tags:
  - ai-agents
  - mcp
  - tool-calling
  - async-agents
  - rag
  - observability
  - security
  - education
  - transcript
related_article: articles/2025-06-19_willbrown_agents-mcp-rl-lesson2.md
participants:
  - Will Brown (instructor)
  - Kyle Corbitt (co-instructor)
---

# Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents (Lecture Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Co-instructor:** Kyle Corbitt (CTO, OpenPipe)
**Date:** June 19, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]

---

## Lesson Focus: From Demo to Production

**[00:03:05]** The top focus for today is how do we take things from demo stage — super notebook like running in the loop — to what do these things actually look like in production? What does it mean to productionize an agent?

**[00:03:28]** How do we apply ideas from general software productionization to make agents that we can reliably deploy, that work well, are stable, and are able to integrate into real world systems?

**[00:04:01]** Themes: general software best practices as they relate to agents, higher level system architecture (where code lives, monitoring, logging), and security considerations and reliability.

---

### 1. Type Hints & Strong Typing

**[00:04:25]** Revisiting type hints from Lesson 1.

**[00:04:47]** Python does not require you to use types. But it's very good practice to use strong type hints, especially for production code.

**Notebook details:**
- Enable **Pylance (Pyright)** in your IDE — shows linter errors to LLMs during assisted development
- Use **Ruff** for code quality linting
- `Any` is an escape hatch if needed, but `Union` is preferable
- Type hints ensure reliable composability across your codebase

### The String Multiplication Bug

A cumulative product function — taking returns and multiplying them cumulatively. Without type hints, an LM returns `"3"` (a string) instead of `3` (a number). Python's string multiplication means `"3" * 6` produces `"333333"` instead of `18`. The code runs without error — but produces silently wrong results.

**[00:06:54]** Type hints play very nicely with structured output. This is the LM way of doing strong typing in Python. With `list[float]` enforcement, a type checker would flag the string/float mismatch.

### Test Cases as Frozen Intentions

**[00:07:21]** LLMs are great at writing test cases. Having test cases is a way of freezing the logic or intention of your code. If something changes where another function is now broken, this is an early warning system.

---

## Pydantic, Instructor, and Structured Outputs

**[00:09:21]** LLMs natively operate over tokens. Tools like [[concepts/mcp|Pydantic]], instructor, and outlines are our mechanism for translating LLMs (which operate over tokens) into the world of types where our programs operate over explicitly typed objects.

**[00:12:21]** If you're not using a wrapper tool, make it very clear in your prompt what the return format should be. Examples are really useful.

**[00:13:06]** Selection guide:
- **Open models** → Outlines
- **OpenAI-only** → OpenAI's default structured outputs
- **Portable across providers** → Instructor

**Notebook code pattern:**
```python
instructor_oai = instructor.from_openai(oai)
response = instructor_oai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}],
    response_model=GrowthMultiplier,
)
# response.growth_multiplier is guaranteed float
```

Alternatives listed in notebook: `outlines`, `openai.beta.chat.completions.parse`, `openai.responses.create`, JSON mode.

### Constrained Generation (Grammar Masking)

**[00:13:53]** Some mechanisms guarantee valid structured output. Outlines compiles the schema into a grammar, then masks out invalid tokens at sampling time — you literally cannot sample an invalid schema. This has roots in theoretical computer science (deterministic finite automata, state machines).

**[00:15:19]** Key open source projects: **Outlines**, **XGrammar**, and **SGLang** (which has structured generation at its roots — "Sg" stands for structured generation).

---

## Tools Are Software

**[00:13:33]** Tools are really just software — functions to be used by LLMs. Everything about software testing and best practices applies.

### Calculator Tool Demo

A simple calculator tool that filters input to only allow numbers and mathematical operators, then uses `eval()`. Safe here because of input filtering — but `eval()` can execute arbitrary code.

**[00:17:27]** Trust levels exist on a spectrum. If you trust your LM and can monitor it, sometimes loose sandboxing is fine. There are degrees of sandboxing available.

### Tool vs No-Tool Comparison

With a calculator tool, the agent gets `0.007704` (correct). Without the tool, using GPT-4.1 Nano, the answer is close but wrong — off by a little bit.

**[00:20:39]** Math tools: the important piece of LM math skills is reasoning through problems. For anything beyond simple calculations, give the LM the option to use tools.

### Code Execution as General-Purpose Tool

**[00:20:58]** Most tools can be written as code. If you're building a general purpose agent, the ability to write and run code is very convenient. Manus does this sort of thing.

**[00:22:03]** LLMs perform best when the number of tools is not crazy large — smart LLMs can handle a few dozen tools just fine. A thousand tools would get silly. But if the agent writes its tools on the fly, it's much easier.

### Model Behavior Differences

**[00:24:44]** OpenAI Codex: heavily optimized for terminal, does terminal-based commands for almost everything, relatively safe model.

**[00:24:55]** Gemini 2.5 Pro (older version): very code-happy, would write million of scripts it never uses, churn out tokens and make a mess.

**[00:25:21]** Know your model. Models are trained to behave in certain ways with tools. Testing your setup with different models is important.

---

## Async Processing

**[00:25:44]** Async I/O is Python's built-in library for parallel processing. For network requests, the requesting thread sits idle while the remote server does the work — you can do many of these in parallel.

### Sequential → Async Speedup

Sequential: **19.5 seconds** for 12 requests.
Async (gather): **2.6 seconds** — same logic, same order, just parallel.

### Semaphore for Rate Limiting

**[00:30:51]** A semaphore puts a global throttle on parallel requests. Setting it to 5 means at most 5 active at a time. When one finishes, the next starts. Result: **4.5 seconds** — middle ground between sequential (19.5s) and unbounded parallel (2.6s).

**[00:32:27]** This should be your default programming pattern for LLM applications destined for production.

**[00:32:38]** The pain of sequential processing is especially felt during evaluations — 100 test cases in a for loop = 15 minutes. Async = seconds.

### Async Tool Calls

**[00:33:12]** Same pattern applies to tool calls. Multiple sub-agents doing search in parallel. Trade-off: speed vs task decomposition.

**Notebook pattern — Parallel Tool Execution:**
```python
class ToolCall(BaseModel):
    name: str
    args: dict

class ToolCalls(BaseModel):
    thinking: str           # thinking FIRST (autoregressive ordering)
    tool_calls: list[ToolCall]

# Single LM call returns multiple tool calls
response = instructor_oai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": multi_question_prompt}],
    response_model=ToolCalls,
)

# Execute all tool calls in parallel
async def execute_tool(func, args) -> str:
    return func(**args)

async def main():
    tasks = [execute_tool(calculator, tc.args) for tc in response.tool_calls]
    results = await asyncio.gather(*tasks)
    return results
```

Key insight: one LM call can return **multiple tool calls** (e.g., 6 calculator expressions from 6 questions), then execute them all in parallel. The `thinking` field comes first in the schema to ensure autoregressive ordering.

### Timeout Patterns

**[00:37:13]** You can set timeouts on parallel functions. Maybe only 17 of 20 sub-agents finish in time — you roll with what you have. Or you signal the agent: "you're running out of time, get final answer now."

**[00:38:25]** Think about latency guarantees. Non-deterministic requests have tails. Either allow full time or have mechanisms for dealing with latency.

---

## RAG Patterns: Old School vs Agentic

**Notebook definitions:**
- **Pre-Fetch RAG**: search *before* LLM calls. The "helper agent" pattern from Lightning Lesson 1 is pre-fetch RAG. Common confusion: vector DBs ≠ RAG. Good if: docs aren't too long, you want to cache docs for multiple questions, no need for "multi-hop" search.
- **Agentic RAG**: retrieved info isn't determined by "always on" program logic. Good for: leveraging existing DB indexes/search tools, retries/adaptive queries are native, combining multiple data sources.
- **Pro tips:** Markdown docs are LLM-friendly (OCR/markdownify are great). Leverage natural file system + link structures. LLMs are great at clever plaintext search.
- **Generally recommended as default pattern.**

### Embedding-Based Prefetch RAG

**[00:39:07]** Old school RAG: software handles all search given the user query. Embedding search over document chunks, top-K retrieval, optional re-ranking. The searching is not happening from the LM itself.

**[00:38:22]** (Repeat) Prefetch RAG can make sense when:
- Your docs aren't very long
- You want to leverage **input caching** for multiple questions — LM APIs offer caching where you save the large input prompt prefix and re-fetch it at ~10% cost. The only thing changing is the question at the end.
- You're not doing multi-hop search — just one round of search that finds everything you need, then directly to an LM query.

### Agentic RAG

**[00:42:08]** Agentic RAG: the agent decides which tools to use. Especially useful with multiple document sources (web + internal docs + customer files). The agent can retry with different queries, change its theory based on what it finds.

**[00:43:11]** Deep research / Claude Code pattern: multiple swings at search, don't have to get it right the first time. In Prefetch RAG, you'd have to manually hand-engineer every retry variant.

### RAG Tips

- **Markdown** is the best standardized format for LLM-readable documents
- **PDF → Markdown** is cheap (Gemini Flash, Mistral OCR)
- Expose **hyperlinks** to the LM + give it tools to follow them
- LLMs are good at **plain text search** (terminal commands like `show lines 20-47`)
- **Use existing search interfaces** — don't reinvent the wheel. Turn your existing API/search index into tools
- Google Advanced Search operators, Twitter search operators can all be tool arguments

---

## System Architecture: Logging & Monitoring

**[00:48:49]** For serious agent debugging, you want a dashboard — not print statements in a terminal.

### Logging Frameworks

| Framework | Best When |
|-----------|-----------|
| **Pydantic Logfire** | Already using Pydantic AI |
| **W&B Weave** | Already using Weights & Biases for training |
| **MLflow Tracing** | Want an open-source W&B alternative |
| **Arize Phoenix** | Popular general option |

**Notebook — Pydantic AI + Logfire integration:**
```python
import logfire
logfire.configure()

calculator_agent = Agent(
    "openai:gpt-4.1-mini",
    deps_type=CalculatorDependencies,
    output_type=CalculatorResponse,
    system_prompt="You are a helpful assistant...",
    instrument=True  # ← enables Logfire tracing
)
```

The `instrument=True` flag automatically captures all tool calls, inputs, outputs, and latencies into Logfire's dashboard.

**[00:53:04]** Choose based on least friction — what ecosystem are you already embedded in? AWS → AWS version. W&B → Weave. Pydantic AI → Logfire. OpenAI Agents SDK → OpenAI's monitoring.

### Lock-in and MCP

**[00:54:22]** The closest thing to a CUDA-like lock-in mode is really just MCP. For logging, if there's going to be a crowd favorite, it would be Weave (CoreWeave acquired W&B).

---

## MCP: Model Context Protocol

### Core Concept

**[00:57:54]** MCP is a version of a server designed to be **LM-shaped**. Instead of HTTP primitives, it has first-class functionality for exposing prompts and calling tools — the LM language.

**[00:59:21]** Think of it like **FastAPI, but LM-shaped**.

### When to Use MCP

- **Portability across applications** — same tool works in Cursor, Claude Code, ChatGPT
- **Internal data sources** with multiple consumers — N×M → N+M problem
- **Building a service with an API** → probably should have an MCP server for it

**Notebook — MCP setup commands:**
```bash
# JS/TS servers
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem $CLAUDE_FILESYSTEM_PATH
claude mcp add brave-search -e BRAVE_API_KEY=*** -- npx -y @modelcontextprotocol/server-brave-search
claude mcp add e2b -e E2B_API_KEY=*** -- npx -y @e2b/mcp-server

# Python servers
claude mcp add fetch uvx mcp-server-fetch
```

**Transport protocols:**
- **stdio** — local-friendly
- **Streamable HTTP** — primary remote protocol (streaming, long-lived connections, interrupt handling)
- **SSE** — original remote protocol, MCP is moving away from it

**MCP repositories:** [official servers](https://github.com/modelcontextprotocol/servers), [smithery.ai](https://smithery.ai/), [mcp.so](https://mcp.so/)

**Brown's related projects:** [claude-code-mcp](https://github.com/willccbb/claude-code-mcp), [claude-deep-research](https://github.com/willccbb/claude-deep-research), [mcp-client-server](https://github.com/willccbb/mcp-client-server)

### N×M vs N+M

**[01:01:01]** Without MCP: N data sources × M applications = N×M manual integrations. With MCP: each data source is an MCP server, each application is an MCP client = N+M connections.

### Code Sandboxes via MCP

**[01:02:10]** E2B is a popular code sandbox MCP server. The LM writes code as a tool call, the sandbox executes it, returns stdout. A way to let LLMs write their own tools on the fly safely.

### Streamable HTTP vs SSE

**[01:04:36]** SSE (Server-Sent Events): original MCP protocol, keeps connection alive, sends full object back. Streamable HTTP: better for intermittent requests, interrupted connections, partial responses.

### MCP Demo: Multi-Tool Orchestration

**[01:05:15]** Claude Code using MCP: web search → find URLs → fetch each URL → get markdown. Same pattern as the research agent from Lightning Lesson 1, but composed from MCP tools.

### Local vs Remote Servers

**[01:05:47]** Claude Code runs MCP servers locally as background workers. You can also have remote MCP servers that behave like APIs.

---

## A2A: Agent-to-Agent

### Client-as-Server Pattern

**[01:07:30]** Built an MCP client that's also a server — Claude Code can dynamically deploy, test, disconnect, and edit MCP tools without restarting. The server is also an MCP client, forwarding requests.

### A2A Skepticism

**[01:09:27]** "I just don't think we've seen any kind of winning applications that really lay into this [A2A] pattern."

**[01:09:36]** The most reliable multi-agent pattern: **one primary agent delegating to sub-agents**. For this, MCP is sufficient — you don't need A2A. Crew AI, Swarm — "I'm not sold on those too much."

**[01:10:17]** Sub-agents can be MCP client-servers: they use their own tools as MCP clients, and are themselves tools for the main agent as MCP servers.

**[01:10:33]** "I'm not gonna tell anyone to go really build on A2A right now. But I think you probably should be building on MCP."

---

## Data Structures for LLMs

**Notebook — Database options:**
- **File systems** (e.g. Docker) — tools: grep, sed, ls, cd, pwd, etc.
- **SQL databases** — tools: SQL query access (or limited wrappers, e.g. read-only, id lookup, no joins). SQLite, Postgres.
- **Vector databases** — tools: querying for embedding similarity, ids. Chroma, Weaviate, Pinecone, Milvus, MongoDB Atlas.

### Docker Containers as Sandboxes

**[01:10:50]** Docker containers are not infinitely safe but usually good for testing. Give your LLMs a virtual machine where they can run around, make folders and files.

### File System as Memory

**[01:11:23]** Easiest way to do LM memory: a folder where the LM writes notes for later. System prompt / CLAUDE.md tells it where memories live and how to search them.

**[01:08:16]** (Repeat) Make sure the CLAUDE.md file really describes the structure as well as meta-level rules of where things should go and how the LM should take notes for itself. Patterns that help:
- Every time they do a feature, write a design doc first — design docs go in this folder
- Backlog / to-do / finished folders for design docs
- Update the README every time you finish a feature
- These patterns create a **self-documenting code base** where the LM has a persistent reminder (system prompt) of how to keep track of what it's doing
- LLMs are not great at figuring out the ideal way to do this — you need to commit to a structure and tell them

### Memory Is Unsolved

**[01:11:48]** Hard to get right. LLMs often forget to check their memory. Hard to dynamically trigger the right memories. "I don't think anyone has really robustly solved this problem." Expect to spend a lot of time tuning prompts and data structures.

### SQL and Vector Databases

**[01:12:35]** LLMs can write SQL really well. SQLite, Postgres — all viable as MCP servers.

**[01:13:16]** Vector databases are a commodity — use whatever fits your setup (pricing, security). Chroma is good for first iterations.

### Evals-Driven Development

**[01:14:16]** Anthropic and OpenAI are doing lots of evals behind the scenes that they don't release publicly. How many tools, how much prompting — you get a feel for this through eval-driven development. Know what you want your system to do, know how you're evaluating it, before building beyond trivial complexity.

---

## Security Considerations

**Notebook — Tools as Action Whitelists:**
- Tempting: give your agent a terminal
- Challenges: workspace management (excess scripts), bad practices, deleting important files
- Workaround: "whitelist" certain code paths, explicit tools for common actions (e.g. fetching a website and converting to markdown)

**Code sandbox providers (from notebook):**
- **E2B** — [MCP server](https://github.com/e2b-dev/mcp-server)
- **Morph, Modal, AWS Lambda** — serverless sandbox alternatives

### Whitelist vs Blacklist

**[01:15:35]** Blacklisting libraries is whack-a-mole — there's always a workaround. If the LM is smart enough, it can find ways around restrictions.

### Codify Repeated Patterns as Tools

**[01:16:13]** If the agent writes the same code repeatedly, freeze it into a tool. Guarantees correctness, reduces errors, improves reliability.

### Preventing Code Chaos

**[01:17:10]** When LLMs have many options, they'll use them all incoherently. Claude and Gemini love to write unused scripts. Solutions: enforce pathways via tools, or provide clear examples + docs.

---

## Authorization & Permissions

**[01:18:48]** MCP has new auth changes. For production at scale, you need auth. Agent = extension of user with subset of permissions. Some actions need human approval (like Claude Code's "approve this tool call?" pattern).

**[01:19:56]** Still early for fully autonomous agents with auto-handled auth. Failure rate for long-horizon agents is too high.

**[01:14:18]** (Repeat) I think it's still too early to really know what auth for agents that are not acting on behalf of users is going to look like. Reliability is not yet to the point where that's a thing people are seriously trying to solve.

**[01:06:50]** (Repeat) MCP servers can just be OAuth resource servers, meaning they can handle auth the same way any web service does. It's a moving target — if you need it, take a closer look.

### Environment Variable Safety

**[01:20:20]** Don't give LLMs environment variables directly. Keep them isolated to prevent accidental training data leakage.

---

## Error Handling

**[01:20:56]** Retry with exponential backoff for transient failures. Graceful degradation — decide which errors users see vs which get bucketed into "server's down, sorry."

---

## Security: Reward Hacking & Read-Only Defaults

*(From repeat version)*

**[01:16:12]** Reward hacking behaviors: sometimes agents will delete test cases to pass tests. Agents have been trained to pass test cases, and if they're not passing, their way of doing it will be to edit the file in a way that deletes the test case.

**[01:16:50]** We're not yet at a point where we want to remove responsibilities of code review or testing. Having agents write tests is often useful. But any sufficiently important code, even if you're using LLMs significantly to help with writing it — you still want to think of humans as being the owners of the code. **You can't fire an LLM.** An LLM cannot get in trouble if something is bad. It only exists as an agent in the runtime it's acting for.

**[01:15:34]** Default to **read-only** for agents. Any write actions — creating files, code execution — should be very carefully considered. This includes anything that's creating a file or code execution.

---

## Q&A Highlights

### Evals for Agentic vs Non-Agentic Systems

**[01:22:47]** Tool use is OP, but that's why we like it. Comparing LM+tools vs LM-no-tools is "unfair" but we care about applications, not leaderboard numbers. Best benchmarks: **Claude Plays Pokemon** (super long horizon), **MC Bench** (Minecraft building, human vote), **ARC 3** (coming soon, game-flavored puzzles).

**[01:25:28]** Kyle Corbitt: eval at the higher-level abstraction (e.g., "answer the user's question") to compare agentic vs non-agentic head to head.

**[01:26:29]** Tool use is part of reasoning. Top-line eval should be a function of the primary output (e.g., the report, not the search queries).

### Sub-Agent Spawning

**[01:27:37]** Pick one framework for sub-agents. Don't let the LM spontaneously mix Pydantic AI agents with OpenAI SDK agents.

**[01:31:17]** (Repeat) When to use sub-agents vs just parallel calls: think of sub-agents as single-turn tools or structured smaller agents that are doing a very specific thing. Sub agents are tool calls that may take some time to finish. Just as you want your tools to be robust, these sub agents need to be robust — have evals or test cases for them. If you can rely on your sub agents, they just become tools for the primary agent.

### JSON vs XML for Tool Calls

*(From repeat version)*

**[01:19:27]** (Repeat) JSON vs XML: I tend to like XML better when I can use it, just because it's easier to parse on the human side. There are cases where, especially if you're writing nested logic — if one of the arguments is going to be code itself, JSON nested inside JSON is doable but it gets nasty and introduces a lot of failure. XML with regex parsing is a pretty good combo for going from scratch. Pydantic doesn't fully support XML — the way Brown typically does XML is with regex parsing.

### Async: Progress Tracking & Incremental Results

*(From repeat version)*

**[01:34:11]** (Repeat) **tqdm** library for progress bars — can also be used as a counter for tracking completed requests. With `as_completed` pattern, you can:
- Save outputs every N completed requests as a checkpoint (crash recovery)
- Return incremental results to the agent as tool calls finish
- Have background tasks that continue running while the agent does other work

**[01:35:31]** Claude Code is starting to enable background tasks that take longer than a few seconds. Some of these are sub-agent level things. You can have tasks running truly in parallel with tracking mechanisms — when a task finishes, update global state about which completed tasks should be shown to the agent.

### MCP: API Server Fundamentals

*(From repeat version)*

**[01:50:54]** (Repeat) API servers are the production pattern: scalability, fault tolerance, separation of concerns. FastAPI is a framework for making API servers. MCP is the same idea but LM-shaped — tools are applications, tools are endpoints, and you want endpoints to natively be LM-friendly.

**[01:55:26]** (Repeat) LLMs are very good at developing MCP servers. Claude Code was already quite good at building them. The test server pattern (client-as-server) was useful for allowing Claude Code to run its own tests on MCP servers without disconnecting and reconnecting.

**[01:58:30]** (Repeat) Tool design is just code design. Some MCP servers are not great, just as some code products are not great. Official reference servers are pretty solid. Auto-generating MCP servers is hard for the same reason code gen is not a fully solved problem.

### Agent Evaluation Deep Dive

*(From repeat version)*

**[01:18:49]** (Repeat) How to evaluate agents: at the core, agents are programs solving problems. We care about the solution and resource utilization (tokens, tool calls). The completion can be just the final answer, or we can evaluate the whole sequence (process evaluation).

**[01:19:35]** (Repeat) Formatting rewards for tool calls: check what fraction of tool calls the LM gets correct format and doesn't create errors.

**[01:20:09]** (Repeat) For very open-ended tasks, LLM-as-judge is the most powerful tool. String similarity (text and embeddings) also useful when you have ground truth.

**[01:20:46]** (Repeat) **Don't be naive with LLM-as-judge.** Don't just send to judge and ask "is this good or not." Instead, ask granular questions:
- Are there any turns of this trajectory that seem completely useless?
- Did the LM make logical steps after each previous thing?
- Did the final answer have 5 paragraphs?
- Are links cited in line as opposed to at the end?

**[01:21:28]** (Repeat) Think about all the things you want your LM to do — anything that's a sentence in your system prompt can also be a piece of your eval. Each instruction can become something judged by an LLM at the end.

### RL Resources & GRPO Details

*(From repeat version — Q&A)*

**[01:17:41]** (Repeat) RL resources:
- **Nathan Lambert** — blog (non-technical concepts) + [rlhfbook.com](https://rlhfbook.com) (in-progress web textbook, good overview of all things LLM RL)
- **Lillian Wang** — good blog on RL topics
- **Mutual Information** (YouTube) — video form of the Sutton & Barto textbook, "3Blue1Brown for reinforcement learning"

**[01:22:11]** (Repeat) GRPO and removing KL: removing KL is good for memory — allows you to do more with less by getting rid of the reference copy of your model and just having the policy model trained online. Brown is "a little skeptical that you can totally get rid of KL."

**[01:22:50]** (Repeat) Default approach: pretty small KL term with online updates of the reference model. This interpolates between KL and no-KL penalty. As you increase the frequency of reference model updates, it washes out the influence of the KL penalty — becomes about local change rather than drift from start. This is a tunable knob.

**[01:23:49]** (Repeat) **Random Rewards paper**: points out funny things with Claude models. Brown's takeaway: we have a lot to learn still. People are spending too much effort on the same math data sets where models are already saturated.

**[01:24:16]** (Repeat) **Entropy collapse**: RL configurations can artificially lower entropy (similar to lowering temperature). Some models just do better at low temperature — more reliable, more accurate. RL even without reward signals — just applying KL penalty at each step can penalize out-of-distribution behavior, collapsing into the most likely behavior. Sometimes that most likely behavior is better.

**[01:25:36]** (Repeat) **Structured generation during training**: you can use Outlines during training to turn off the possibility of the model ever outputting invalid schema. If you're going to use structured generation at inference, also use it during evaluation and training. Some samples can use it, some not — still use format rewards to enforce format.

**[01:27:17]** (Repeat) **Verifiers baseline evaluation**: built-in GRPO support. Take any model, expose an endpoint, plug into the verifiers environment. Same reward functions used for RL can be used for baseline. Run eval set on your environment, get rollouts with scores — average score is your baseline.

---

## Homework Assignment

**[01:29:16]** Build something fun. Pick a task — code agents and search agents are easiest. Ideas: graphic design agent, board game player, solitaire agent, chatbot with user interruption.

**[01:31:37]** State management: in-memory for short-lived agents, SQL database for persistent agents.

**[01:32:48]** Eval pattern: LLM-as-judge with Pydantic schema for structured evaluation. Convert yes/no to 0/1 scores programmatically.

**[01:34:23]** **Best-of-N sampling**: same agent runs many parallel attempts, eval function selects the best. Works when you have ground truth or judge-answerable criteria (source citation, internal contradictions).

**[01:35:37]** Blog post opportunity: pick a problem, try these methods, write it up.

---

## Key Takeaways

1. **Type hints are essential for production** — LM outputs are strings by default; type mismatches cause silent bugs (string multiplication example)
2. **Pydantic + Instructor/Outlines** for structured outputs — bridges the token-world of LLMs and the type-world of programs
3. **Tools are software** — apply standard testing, input validation, and security practices
4. **Async by default** — `asyncio.gather` + semaphores for parallel LM requests; ~7-8x speedup over sequential
5. **Agentic RAG > Prefetch RAG** — let the agent drive search decisions, retry, and adapt; use existing search interfaces as tools
6. **MCP = FastAPI but LM-shaped** — use for tool portability, the N×M→N+M problem, and API exposure
7. **A2A is premature** — one primary agent + sub-agents via MCP is the reliable pattern
8. **Codify repeated code patterns as tools** — freeze reliable paths, reduce LLM chaos
9. **Memory is unsolved** — file system is the simplest approach but robust memory retrieval remains an open problem
10. **Eval-driven development** — know your eval before building; LLM-as-judge + Best-of-N for agent quality
