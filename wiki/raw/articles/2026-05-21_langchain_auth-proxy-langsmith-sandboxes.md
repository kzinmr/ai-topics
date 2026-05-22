---
type: x_article
x_article_title: "How Auth Proxy secures network access for LangSmith agent sandboxes"
x_article_author: "LangChain"
source_url: https://x.com/i/article/2057309362889326593
date: 2026-05-21
getxapi: false
tags:
  - langchain
  - langsmith
  - sandbox
  - auth-proxy
  - agent-security
  - egress
---

# How Auth Proxy secures network access for LangSmith agent sandboxes

## The problem: Agents are untrusted developers at scale

Enterprises have endpoint protection, browser filtering, device management, and secret scanners that protect trusted employees. Agents change the scale and shape of this problem — you may be spawning thousands, or eventually millions, of "untrusted developers" that can write code, run commands, install packages, and make network requests on your behalf.

For human developers, the environment often needs to stay open by default. For agents, the default can be different. If the agent only needs GitHub and an LLM provider, it should not be able to talk to every random host on the internet. If it needs a credential, that credential should not have to exist inside the runtime at all.

## Introducing the sandbox Auth Proxy

The auth proxy sits on the outbound network path and controls how sandboxed code interacts with external services. Instead of putting API keys into the sandbox as environment variables or files, it enforces policy for which destinations are allowed, what authentication is applied, and how requests are shaped before they leave the sandbox.

Three things become much easier:
1. **Credentials stay out of the runtime** — The agent can use an API without being able to read the API key
2. **Network access becomes explicit** — Encoded as infrastructure policy rather than left to the agent's judgment
3. **Cleaner separation of concerns** — Agent focuses on the task, sandbox provides isolation, proxy handles network authorization

## How it works

1. The agent or sandboxed code makes an outbound request
2. The request passes through Auth Proxy
3. Auth Proxy checks the configured policy for that destination
4. The proxy can block the request, allow it, or attach headers
5. The request continues to the destination without exposing credentials to the runtime

The proxy is implemented at the network level, not via HTTP_PROXY — it's completely transparent regardless of runtime, SDK, or subprocess behavior.

## Authenticate without handing credentials to your agent

Headers can be configured with different types:
- `workspace_secret`: references a secret stored in LangSmith workspace settings
- `plaintext`: stored and returned as-is
- `opaque`: write-only, encrypted at rest, never returned by the API

Example OpenAI rule: When sandbox calls `api.openai.com`, inject `Authorization: Bearer {OPENAI_API_KEY}` from a workspace secret.

The sandbox code does not need to know the API key, does not need an `.env` file, does not need a secret mounted into its filesystem.

## Locking down the network

The proxy boundary enables teams to define which destinations are expected:
- Allowing the model provider API and blocking everything else
- Allowing GitHub API paths the agent needs, but not arbitrary GitHub-adjacent domains
- Allowing a package registry, but only the internal mirror
- Blocking known malicious or untrusted package registries

## Dynamic credentials for real production auth

For advanced use cases (short-lived OAuth tokens, per-user-scoped tokens, tokens that need refresh), the auth proxy supports dynamic credentials with callbacks.

The proxy calls a callback endpoint with the target host and port, receives headers to inject, and caches the result for a configured TTL. If the callback fails, the proxy fails closed and rejects the sandbox request.

## What this unlocks next

- **DNS remapping**: Requests to public registries resolve to internal mirrors
- **Network logging**: Audit trail of which services agents called
- **Request transformation**: Redacting PII, adding organization metadata, enforcing request shape

The broader point: agent infrastructure needs control planes that live outside the runtime and aren't exposed to agent instructions and decisions.
