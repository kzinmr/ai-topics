---
title: Koog
created: 2026-05-28
updated: 2026-05-28
type: entity
tags: [entity, ai-agents, agent-framework, kotlin, java, jetbrains, open-source, enterprise-ai]
sources:
  - raw/articles/2026-05-21_jetbrains_koog-1-0.md
  - https://github.com/JetBrains/koog/releases/tag/1.0.0
---

# Koog

**Koog** is a JVM (Java/Kotlin) framework by JetBrains for building predictable, fault-tolerant, enterprise-ready AI agents. It runs on backend servers, Android, iOS, and browser environments. The 1.0 stable release shipped May 21, 2026 with a long-term-supported API surface (4K GitHub stars).

## Architecture Highlights

### Stable/Beta Module Split
Modules are split into stable and beta streams — production code can pin to APIs that won't break without a deprecation cycle.

### Java Interop
- Uniform blocking API pattern across Kotlin and Java
- Deadlock-free reentrant calls (Kotlin → Java → Kotlin on single-threaded executor)

### Graph DSL
Finalized node naming conventions for LLM request, tool execution, and moderation flows.

### Memory & Persistence
- `AIAgentStorage` in checkpoints with `runFromCheckpoint` API
- Persistence for planner-based agents
- Amazon Bedrock AgentCore as `LongTermMemory` backend

### HTTP Transport Decoupled
LLM clients take `KoogHttpClient.Factory` — pluggable backends (Ktor, OkHttp, Java HTTP client, Spring RestClient) without touching Koog internals.

### Multiplatform OpenTelemetry
Langfuse, Weave, DataDog on every target. Built-in metrics (`gen_ai.client.token.usage`, `gen_ai.client.operation.duration`, `gen_ai.client.tool.count`) for Prometheus/Grafana.

### Anthropic Prompt Caching
Automatic and explicit cache control with end-to-end support.

## Model Support
Opus 4.7, GPT-5.5/5.5 Pro, DeepSeek V4 Flash/Pro, Kimi K2.5, MiniMax 2.5, Gemma 3, GPT OSS, Qwen 3.5, LiteRT local models.

## Related Concepts

- [[concepts/ai-agents]] — AI agent architectures
- [[concepts/agent-framework]] — agent framework ecosystem
- [[entities/jetbrains]] — JetBrains company
- [[entities/microsoft-agent-framework]] — Microsoft's agent framework
- [[entities/google-adk]] — Google Agent Development Kit

## References

- GitHub: [JetBrains/koog](https://github.com/JetBrains/koog) (v1.0.0, May 21, 2026)
