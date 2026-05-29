# Managed Agents Quickstart — Gemini API

**Source:** https://ai.google.dev/gemini-api/docs/managed-agents-quickstart
**Retrieved:** 2026-05-29
**Via:** X post by @_philschmid (2026-05-29)
**Archived for:** wiki knowledge base

---

## Quickstart for creating and using Managed Agents on the Gemini API

This quickstart walks through creating and using Managed Agents on the Gemini API, focusing on the **Antigravity** agent. It covers initial interactions, multi-turn conversations, streaming, file downloads, and saving/re-using custom agents.

## 1. Run Your First Agent Interaction

A single call provisions a Linux sandbox, runs the agent loop, and returns the result.

- **Agent**: `"antigravity-preview-05-2026"`
- **Environment**: `"remote"` (fresh sandbox)
- **Input**: Describe the task (text)

```python
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
```

```bash
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "..."}],
    "environment": {"type": "remote"}
}'
```

### Response
- `interaction.id` – Use to continue conversation
- `interaction.environment_id` – References the sandbox environment
- `interaction.output_text` – Final agent output
- `interaction.steps` – List of steps (reasoning, tool calls, code execution)

## 2. Continue the Conversation (Multi‑Turn)

Two independent state dimensions:
- **Conversation context**: chat history, reasoning trace, tool use – via `previous_interaction_id`
- **Environment state**: files, packages, sandbox – via `environment` (environment ID or `"remote"`)

**Automatic Context Compaction**: Native compaction step at ~135k tokens to prevent "context rot" and maintain agent focus.

## 3. Stream the Response

```python
stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)
```

## 4. Download Files from the Environment

Download via Files API with HTTP GET. Response is a tarball snapshot.

## 5. Save a Custom Agent Instance

```python
saved_agent = client.managed_agents.create(
    display_name="My Custom Agent",
    agent="antigravity-preview-05-2026",
    interaction_id=interaction.id,
)
# Use: client.interactions.create(agent=saved_agent.name, ...)
```

## 6. Share a Custom Agent Instance

Managed agents support sharing with other users (Google account-based).

## 7. Built-in Tools

Antigravity includes:
- **Code execution** (Python)
- **File system** for artifact persistence
- **Browser** for web access
- **Shell** tool
- Support for custom tool extensions

## API Details
- Base URL: `https://generativelanguage.googleapis.com/v1beta/`
- Required header: `Api-Revision: 2026-05-20`
- SDKs: Python (`google-genai`), JavaScript (`@google/genai`)
- Authentication: API key via `x-goog-api-key` header

---

## Key Takeaway

Google's Gemini API now offers a **managed agent runtime** where a single API call provisions a sandboxed Linux environment, runs an agent loop (code execution, browsing, shell), and returns results. This is Google's answer to coding agents — a hosted, API-accessible agent infrastructure with built-in multi-turn memory, context compaction at ~135k tokens, streaming, file download, and custom agent saving/sharing.
