---
title: "Building effective agent automations"
author: Lance Martin & CJ Avilla (Anthropic / claude.dev blog)
date: 2026-10-08
type: web_article
source_url: https://claude.dev/blog/building-effective-agent-automations/
ingested: 2026-10-13
tags: [ai-agents, anthropic, managed-agents, agent-deployment, memory, guardrails]
---

# Building effective agent automations

> Shared by Lance Martin (@rlancemartin) on X: https://x.com/rlancemartin/status/2108327973078315274 (2026-10-08). Condensed structured summary of the claude.dev post (authors: Lance Martin and CJ Avilla, "A reference implementation walkthrough with common failure modes", 9 min read).

## Overview

Anthropic's common internal pattern: simple agent automations that run on a schedule, gather context in the background, and proactively report what you need to know. Built on **Claude Managed Agents (beta)**, the reference implementation reads custom sources (e.g., Slack and GitHub repos) on a schedule, tracks what changed since the last run, and posts a "daily brief" to Slack. A Claude Code command configures it for you: after `claude update`, run `/claude-api managed-agents-onboard <post-url>` — the claude-api skill reads the post, proposes a setup, writes files to an `agents/` folder, and creates resources via `ant apply`.

## Architecture pieces (all declarative files, applied with `ant apply`)

- **Agent (`agent.md`)**: versioned config — model (claude-sonnet-5-5), system prompt (8 numbered run steps), tools/MCP servers. MCP tools default to requiring approval but no human is present on scheduled runs, so the GitHub toolset is set `always_allow` with a **read-only** GitHub token.
- **Deployment (`deployment.md`)**: names the agent, environment, first message of each run, cron schedule, vaults, memory stores, budget. Each schedule fire starts a fresh agent session.
- **Environment**: sandbox with host allowlist (e.g. only `slack.com`), `networking: limited`.
- **Credential vault**: bot tokens injected via `claude-lock.json` vault entries (with per-credential host allowlists), attached to the deployment via `vault_ids`.
- **Memory stores**: folders mounted read-write/read-only at `/mnt/memory/` and persisted between runs.

## Six rules (the core durable knowledge)

1. **Read each source from a bookmark, not a fixed time window.** A "last 24 hours" window leaves gaps on late runs and repeats items on early runs. The agent writes the newest-read timestamp per source to `bookmarks.json` in the `state` memory store; the next run stretches/shrinks to cover everything since.
2. **Report a failed read as unreadable, never as a quiet day.** If an MCP server is down or its token expired, the run still starts without those tools and the agent would report "nothing new". Rules: keep that source's bookmark unchanged, write the brief from the other sources, and end the brief naming what couldn't be read ("pull requests unavailable this run").
3. **Re-check every item right before posting.** The world moves between reading sources and posting: resolved → drop; changed → fix the line; can't confirm → drop and log in the run record's cuts. "One stale 'still waiting on you' costs more trust than ten missing items — assert it or drop it." Links must be copied from the source's own link field, never assembled by hand.
4. **Count a post as sent only when the destination confirms it.** Check for today's title in recent channel messages (no duplicate editions); count as sent only on Slack `"ok": true` + message ts; update ledger and bookmarks only after confirmation; if unclear, mark the run "maybe posted" and change nothing else. Run records live in `runs/<date>.md` with statuses posting → posted/maybe posted.
5. **Re-read preferences every run, from a store the agent can't edit.** Two memory stores: `preferences` (human-owned, read-only to the agent: channels/repos to read, exclusions, length cap, destination) and `state` (agent read-write: bookmarks, ledger of reported items with stable IDs and last-known status, run records, proposed preference changes, per-source behavior notes). If preferences can't be read, the agent stops and says so rather than running on defaults. Baking preferences into the prompt causes stale rules to keep applying.
6. **Give read-only access wherever the agent only reads, and cap spend.** Prompt-injection defense by capability limitation: read-only GitHub token, read-only preferences store, host-allowlisted environment. A planted instruction can change what the brief says but can't write to GitHub or edit the rules. Slack is the exception (same token posts → invite the bot only where needed). Budget: `max_list_cost` in cents; start at 3–5× normal run cost and tighten with real numbers — a run that hits the cap *pauses* with `budget_reached` rather than failing, so a too-low cap looks like a brief that went quiet.

## Brevity guidance

agent.md steers toward short briefs: an item earns a line only if the reader would act on it today or it changes an imminent decision; when unsure, leave it out (most days: a few items, sometimes none). Counts ("12 open reviews") are not items; still-open items carry as one marked line ("still waiting, day 3"), not re-reported; retired topics stay retired. Compute all dates in the reader's timezone (a common bug: agent calls this morning "yesterday" using the server's timezone).

## Related

- Prior claude.dev post in this series: "Automating eval design and hillclimbing with Claude" (2026-09-28, also Lance Martin).
- Same `/claude-api` skill command family: `build-eval`, `hillclimb`, now `managed-agents-onboard`.
