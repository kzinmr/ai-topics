# Project Think: Building Next-Gen AI Agents on Cloudflare

Source: https://blog.cloudflare.com/project-think/
Date: 2026-04-15
Authors: Sunil Pai, Kate Reznykova

## Key Excerpts

> "Code is the universal medium of action... instead of sequential tool calls, the LLM writes a single program that handles the entire task."

## Core Primitives

### Long-Running & Durable Execution
- **Actor Model**: Built on Durable Objects, every agent has a unique identity and its own SQLite database
- **Zero Idle Cost**: Agents consume no compute when hibernated
- **Fibers**: Durable function invocations with crash recovery and checkpointing (stash())

### The Execution Ladder (5 Tiers)
1. Tier 0 (Workspace): Virtual filesystem (SQLite + R2)
2. Tier 1 (Dynamic Worker): Sandboxed V8 isolate for LLM-generated JS
3. Tier 2 (npm): Runtime package resolution and bundling
4. Tier 3 (Browser): Headless browser via Cloudflare Browser Rendering
5. Tier 4 (Sandbox): Full OS access (git, compilers)

### Advanced Features
- Session API: Tree-structured conversations with forking and compaction
- Sub-agents (Facets): Isolated child agents with typed RPC
- Self-authored Extensions: Agents write TypeScript tools at runtime, loaded into Dynamic Workers

### Think Base Class
- `getModel()`, `getSystemPrompt()`, `getTools()`, `configureSession()`
- Context Blocks: Structured system prompt sections the model can update

## "Third Wave" Thesis
1. Chatbots (stateless)
2. Coding Agents (stateful but local)
3. Agents as Infrastructure (durable, serverless, safe by construction)

## Key Quote on PTC

> "Conventional tool-calling has an awkward shape. The model calls a tool, pulls the result back through the context window, calls another tool, pulls that back, and so on. As the tool surface grows, this gets both expensive and clumsy. A hundred files means a hundred round-trips through the model. But models are better at writing code to use a system than they are at playing the tool-calling game."
