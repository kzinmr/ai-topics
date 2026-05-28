# Koog 1.0.0 — First Stable Release

**Source**: https://github.com/JetBrains/koog/releases/tag/1.0.0
**Date**: May 21, 2026
**Repository**: JetBrains/koog (4K stars, Kotlin)

## Overview

Koog is a JVM (Java/Kotlin) framework for building predictable, fault-tolerant, enterprise-ready AI agents across backend, Android, iOS, and browser environments. This 1.0 release establishes a long-term-supported API surface.

## Major Features

### Stable / Beta Module Split
Modules split into stable and beta streams. All deprecated APIs removed.

### Java Interop Redesigned
- Uniform blocking API: `xxxBlocking` in Kotlin, plain `xxx` from Java
- Deadlock-free reentrant calls: Kotlin → Java → Kotlin on single-threaded executor

### Graph DSL Finalized
- String-input nodes keep original names
- Message.User-input variants use `nodeLLMSendMessage*` prefix
- `nodeExecuteTools` returns `ReceivedToolResults` directly

### Memory & Persistence
- `AIAgentStorage` in checkpoints
- Persistence for planner agents
- Amazon Bedrock AgentCore as `LongTermMemory`
- `LongTermMemory` promoted from experimental

### HTTP Transport Decoupled from Ktor
LLM clients take `KoogHttpClient.Factory` — plug in OkHttp, Java HTTP client, or Spring RestClient.

### OpenTelemetry on Every Target
Multiplatform OpenTelemetry: Langfuse, Weave, DataDog on every target. Built-in metrics for Prometheus/Grafana.

### Anthropic Prompt Caching
Automatic and explicit cache control, end-to-end support.

### New Providers
- LiteRT LLM client (local Google models)
- Oracle Database `ChatHistoryProvider`
- New model support: Opus 4.7, GPT-5.5, DeepSeek V4 Flash/Pro, Bedrock models
