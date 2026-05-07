---
source: https://platform.claude.com/docs/en/managed-agents/webhooks
title: "Anthropic Managed Agents: Webhooks"
author: Anthropic
date: 2026-05-07
tags: [claude, managed-agents, webhooks, events]
---

# Anthropic Managed Agents: Webhooks Documentation Summary

Webhooks provide a push-based notification system for major state changes in long-running interactions, serving as a complement to the real-time SSE event stream.

## Core Architecture
- **Payload Design:** Webhooks return only the event `type` and `id`, not the full object. 
- **Action Required:** Upon receiving an event, you must perform a `GET` call to fetch the object. This ensures data is fresh and keeps delivery payloads small.
- **Uniqueness:** The top-level `event.id` is unique per event. Duplicate IDs indicate retries and should be discarded.

## Supported Event Types

### Session Events
| Event | Trigger |
| :--- | :--- |
| `session.status_run_started` | Agent execution began (triggers on every transition to `running`). |
| `session.status_idled` | Agent awaiting input (e.g., tool approval or user message). |
| `session.status_rescheduled` | Automatic retry after a transient error. |
| `session.status_terminated` | Terminal error reached. |
| `session.thread_created` | New multi-agent thread opened by the coordinator. |
| `session.thread_idled` | Multi-agent interaction waiting for input. |
| `session.thread_terminated` | Multi-agent thread archived. |
| `session.outcome_evaluation_ended` | Single iteration outcome evaluation completed. |

### Vault Events
- `vault.created` / `archived` / `deleted` — Lifecycle changes for a Vault.
- `vault_credential.created` / `archived` / `deleted` — Lifecycle changes for credentials.

## Implementation & Registration
- **URL:** Must be HTTPS, Port 443, with a publicly resolvable hostname.
- **Signing Secret:** A 32-byte `whsec_`-prefixed secret. **Store securely; it is only shown once.**
- **Signature Verification:** Use the SDK's `unwrap()` helper to verify the signature and parse the event.

## Delivery Behavior & Reliability
- **Ordering:** Not guaranteed. Use the `created_at` timestamp for sorting.
- **Retries:** Anthropic retries at least once on failure.
- **Redirects:** `3xx` codes are treated as failures; redirects are not followed.
- **Auto-disable Policy:** Endpoints are disabled after ~20 consecutive failures or immediately if the hostname resolves to a private IP.
