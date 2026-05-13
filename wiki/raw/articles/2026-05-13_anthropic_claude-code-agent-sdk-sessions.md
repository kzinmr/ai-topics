---
title: "Work with sessions — Claude Code Agent SDK"
author: Anthropic
source_url: https://code.claude.com/docs/en/agent-sdk/sessions
date_ingested: 2026-05-13
type: documentation
tags: [claude-code, agent-sdk, session-management, context-engineering, anthropic]
---

# Work with sessions

> How sessions persist agent conversation history, and when to use continue, resume, and fork to return to a prior run.

A session is the conversation history the SDK accumulates while your agent works. It contains your prompt, every tool call the agent made, every tool result, and every response. The SDK writes it to disk automatically so you can return to it later.

Returning to a session means the agent has full context from before: files it already read, analysis it already performed, decisions it already made. You can ask a follow-up question, recover from an interruption, or branch off to try a different approach.

> **Note**: Sessions persist the **conversation**, not the filesystem. To snapshot and revert file changes the agent made, use file checkpointing.

## Choose an approach

| What you're building | What to use |
|---|---|
| One-shot task: single prompt, no follow-up | Nothing extra. One `query()` call handles it. |
| Multi-turn chat in one process | `ClaudeSDKClient` (Python) or `continue: true` (TypeScript). The SDK tracks the session for you with no ID handling. |
| Pick up where you left off after a process restart | `continue_conversation=True` (Python) / `continue: true` (TypeScript). Resumes the most recent session in the directory, no ID needed. |
| Resume a specific past session (not the most recent) | Capture the session ID and pass it to `resume`. |
| Try an alternative approach without losing the original | Fork the session. |
| Stateless task, don't want anything written to disk (TypeScript only) | Set `persistSession: false`. The session exists only in memory for the duration of the call. Python always persists to disk. |

### Continue, resume, and fork

Continue, resume, and fork are option fields you set on `query()` (`ClaudeAgentOptions` in Python, `Options` in TypeScript).

- **Continue** finds the most recent session in the current directory. You don't track anything. Works well when your app runs one conversation at a time.
- **Resume** takes a specific session ID. You track the ID. Required when you have multiple sessions (for example, one per user in a multi-user app) or want to return to one that isn't the most recent.
- **Fork** creates a new session that starts with a copy of the original's history. The original stays unchanged. Use fork to try a different direction while keeping the option to go back.

## Automatic session management

### Python: `ClaudeSDKClient`

`ClaudeSDKClient` handles session IDs internally. Each call to `client.query()` automatically continues the same session. Call `client.receive_response()` to iterate over the messages for the current query. The client must be used as an async context manager.

```python
async with ClaudeSDKClient(options=options) as client:
    # First query: client captures the session ID internally
    await client.query("Analyze the auth module")
    async for message in client.receive_response():
        print_response(message)

    # Second query: automatically continues the same session
    await client.query("Now refactor it to use JWT")
    async for message in client.receive_response():
        print_response(message)
```

### TypeScript: `continue: true`

The stable TypeScript SDK doesn't have a session-holding client object. Instead, pass `continue: true` on each subsequent `query()` call and the SDK picks up the most recent session in the current directory.

```typescript
// First query: creates a new session
for await (const message of query({
  prompt: "Analyze the auth module",
  options: { allowedTools: ["Read", "Glob", "Grep"] }
})) { ... }

// Second query: continue: true resumes the most recent session
for await (const message of query({
  prompt: "Now refactor it to use JWT",
  options: { continue: true, allowedTools: ["Read", "Edit", "Write", "Glob", "Grep"] }
})) { ... }
```

## Use session options with `query()`

### Capture the session ID

Resume and fork require a session ID. Read it from the `session_id` field on the result message (`ResultMessage` in Python, `SDKResultMessage` in TypeScript), which is present on every result regardless of success or error.

```python
async for message in query(
    prompt="Analyze the auth module and suggest improvements",
    options=ClaudeAgentOptions(allowed_tools=["Read", "Glob", "Grep"]),
):
    if isinstance(message, ResultMessage):
        session_id = message.session_id
```

### Resume by ID

Pass a session ID to `resume` to return to that specific session. The agent picks up with full context from wherever the session left off:

- **Follow up on a completed task.** The agent already analyzed something; now you want it to act on that analysis without re-reading files.
- **Recover from a limit.** The first run ended with `error_max_turns` or `error_max_budget_usd`; resume with a higher limit.
- **Restart your process.** You captured the ID before shutdown and want to restore the conversation.

**Storage location**: `~/.claude/projects/<encoded-cwd>/*.jsonl`, where `<encoded-cwd>` is the absolute working directory with every non-alphanumeric character replaced by `-`.

### Fork to explore alternatives

Forking creates a new session that starts with a copy of the original's history but diverges from that point. The fork gets its own session ID; the original's ID and history stay unchanged.

> Forking branches the conversation history, not the filesystem. If a forked agent edits files, those changes are real and visible to any session working in the same directory.

```python
# Fork: branch from session_id into a new session
async for message in query(
    prompt="Instead of JWT, implement OAuth2 for the auth module",
    options=ClaudeAgentOptions(resume=session_id, fork_session=True),
):
    if isinstance(message, ResultMessage):
        forked_id = message.session_id

# Original session is untouched; resuming it continues the JWT thread
async for message in query(
    prompt="Continue with the JWT approach",
    options=ClaudeAgentOptions(resume=session_id),
): ...
```

## Resume across hosts

Session files are local to the machine that created them. To resume a session on a different host:

- **Move the session file.** Persist `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` from the first run and restore it to the same path on the new host before calling `resume`. The `cwd` must match.
- **Don't rely on session resume.** Capture the results you need as application state and pass them into a fresh session's prompt.

Both SDKs expose functions for enumerating sessions on disk: `listSessions()` / `getSessionMessages()` (TypeScript), `list_sessions()` / `get_session_messages()` (Python). Also: `get_session_info()`, `rename_session()`, `tag_session()` for organizing sessions.

## Related resources

- How the agent loop works: Understand turns, messages, and context accumulation within a session
- File checkpointing: Track and revert file changes across sessions
- Python `ClaudeAgentOptions`: Full session option reference
- TypeScript `Options`: Full session option reference
