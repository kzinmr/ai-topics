---
title: Unrolling the Codex Agent Loop
category: other
status: active
---

# Unrolling the Codex Agent Loop
**Source:** OpenAI Engineering Blog | **Date:** January 23, 2026 | **Author:** Michael Bolin (Member of Technical Staff)
**URL:** https://openai.com/index/unrolling-the-codex-agent-loop/

---

## Overview
Codex CLI is a cross-platform local software agent for producing high-quality, reliable software changes safely and efficiently. Open-source at https://github.com/openai/codex

## The Agent Loop
Simplified illustration:
```
User Input → Codex CLI → Responses API → Model → Tool Call → Execution → Output → Loop
```

### Prompt Construction
1. System instructions from `~/.codex/config.toml` or bundled files
2. Developer instructions
3. Tool definitions (shell, web_search, MCP servers)
4. Environment context (cwd, shell type)
5. User message

### Input Message Sequence
```
1. sandbox permission
2. developer instructions  
3. tool definitions
4. environment context
5. user query
```

### The Agent Loop Cycle
1. **HTTP Request** → Responses API (configurable endpoint)
2. **Model Inference** → tokenized, sampled, streamed
3. **Branching:**
   - Final response: assistant message (loop ends)
   - Tool call: execute, append result, re-query
4. **Iteration** until assistant message generated

### Context Window Management
- Legacy: Manual `/compact` with custom summarization
- Current: Automatic compaction via `/responses/compact` when `auto_compact_limit` exceeded
- Mechanism: Replaces `input` with condensed list containing `type=compaction` + `encrypted_content`
- Codex helped build the compaction system by serving as early user

### Zero Data Retention (ZDR)
Codex intentionally avoids `previous_response_id` to keep requests stateless and support ZDR. Encrypted content from reasoning messages can be decrypted server-side without persisting raw conversation data.

### Prompt Caching Best Practices
- Static content (instructions, tools) at start → cache hits require exact prefix matches
- Variable content at end
- Cache miss triggers: changing tools, model, sandbox config, approval mode, cwd
- MCP dynamic tool lists can break caching → append new messages instead of modifying existing

### Configurable Endpoints
- ChatGPT: `https://chatgpt.com/backend-api/codex/responses`
- OpenAI API: `https://api.openai.com/v1/responses`
- Local OSS (Ollama/LM Studio): `http://localhost:11434/v1/responses`
- Cloud Providers (Azure, etc.)
