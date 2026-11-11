---
source_url: https://www.lorekit.io/blog/open-agent-memory-format
title: "Agent memory needs its OpenTelemetry moment"
site: LoreKit blog
author: Mads Thines (LoreKit; works with OpenTelemetry at Dash0)
published: 2026-11-07
fetched: 2026-11-11
capture: full_html_cleaned
hn_item: 50411467
hn_points: 191
hn_comments: 110
---

# Agent memory needs its OpenTelemetry moment

Mads Thines · November 7, 2026 · 7 min read

Every agent tool stores memory in its own shape, and every week someone builds another one. None of them can read the others. Observability had the same problem until OpenTelemetry gave everyone one data model to share. A tour of today's memory formats, the proposals that already exist, and what a shared spec could look like.

## Count the memory formats on your machine

A typical setup today:

- an `AGENTS.md` or `CLAUDE.md` in most repos, and `.cursor/rules/*.mdc` in a few
- an agent writing files to a `/memories` directory through Anthropic's memory tool
- Copilot keeping facts about each repo on GitHub's side
- a memory MCP server keeping a JSONL knowledge graph

That's four different shapes, and none of them can read the others. A lesson your CI agent learns stays in whatever wrote it. Your editor agent can't read it, and neither can the next tool you try.

Each format is reasonable on its own. Together, they rebuild the same small idea again and again: a note an agent left for its future self, stored at some address, true for a while.

The author builds one of these tools, LoreKit (open source), and states explicitly: "This isn't a pitch that LoreKit has solved memory. Its format is one proposal among several, with gaps of its own. The point is that this is the moment to agree on a shared shape, and that another field has already shown how."

## We've seen this before

Before 2019, every observability vendor shipped its own agent, instrumentation library and data format. Switching vendors meant instrumenting your code again. OpenTracing and OpenCensus tried to fix that and competed with each other too. In 2019 they merged into **OpenTelemetry**. What mattered was what vendors agreed to stop competing on:

1. **A data model**: what a span, a metric and a log record are.
2. **Semantic conventions**: shared names like `service.name` and `http.*`.
3. **A protocol**: OTLP, one way to send the data.
4. **Reference implementations**: shared SDKs and the Collector.

Vendors kept competing on what they do with the data (storage, querying, analysis). Users instrument once.

"Agent memory is where observability was before 2019. The timing is good: the formats are young enough to change, and there's already a neutral home for agent standards. MCP and AGENTS.md both sit under the Linux Foundation's Agentic AI Foundation."

## A tour of the shapes (snapshot from late 2026)

| Family | Example | Unit of memory | Addressed by | Forgetting |
|---|---|---|---|---|
| Instruction files | AGENTS.md, CLAUDE.md, Cursor .mdc rules | A whole Markdown file | File path (plus globs for Cursor) | Never. A person edits it |
| Agent-managed files | Anthropic's memory tool | A file under /memories | A path the model picks | Never, unless the model deletes it |
| Hosted repo facts | GitHub Copilot Memory | A fact with code citations | One repository | Deleted after 28 days unused |
| Context blocks | Letta core memory | A labeled block with a character limit | A label on an agent | Never. Always in context |
| Extracted facts | Mem0 | A fact the service extracts from messages | user_id / agent_id / run_id / app_id | Optional expiration date |
| Namespaced store | LangGraph BaseStore | A JSON value dict | A namespace tuple + key | Optional TTL, reset when read (default) |
| Knowledge graph | MCP reference memory server | Entities, relations, observations | Entity name | Never |
| Temporal graph | Graphiti / Zep | A fact on a graph edge | Entities + edge | Facts invalidated rather than deleted, on two timelines |
| Addressed record | LoreKit | A record with a scope, key and lifecycle | A scope string + key | Never, unless a TTL is set |

What each got right that a shared spec should keep: Copilot Memory pairs checkable code citations with forgetting by default (but is locked inside one product). LangGraph shows how small the core can be: `put(namespace, key, value)`. Graphiti models time properly, with separate timelines for when a fact was true vs. when it was recorded. AGENTS.md shows a plain file at a known path can become a standard.

## The proposals that already exist

- **MacPaw Research Portable Memory** — a `.mem` bundle with byte-reproducible serialization, deletion tombstones and optional signing; authors say it isn't widely adopted yet.
- **Open Memory Protocol** — an April 2026 draft for moving conversations and derived memories between platforms as a ZIP with a manifest.
- **Cognee COGX** — imports from Mem0, Letta and Zep.

These mostly solve **export** (moving one person's memory from vendor A to vendor B). Coding tools have a second, open problem: **live addressing** — when a CI job, an editor agent and a review bot work in the same repo at once, how do they read and write the same place and agree on what it means? "A complete spec needs both."

## What a shared spec could look like

Every format answers the same five questions differently: **where** a memory is true, what its **identity** is (does a second write update or duplicate it?), what it **says**, **when** it stops being true, and **which version** is current. Nobody disagrees that those matter.

The one real fork: **who writes the memory**. In instruction files it's a person. In the memory tool, Letta and LoreKit, it's the model. In Mem0 and Graphiti, a service extracts facts from the conversation. "A spec doesn't need to pick one. It needs to record which, so a reader knows how much to trust what it reads."

Illustrative record (author notes field names aren't a proposal):

```yaml
---
spec: agent-memory/0.1
id: 8f0c2a6e-4b1d-4c7a-9e2f-3a5b6c7d8e9f
address: { level: repo, value: github.com/acme/checkout }
key: tests-need-local-postgres
kind: lesson
version: 3
supersedes: 41b9e0c2-7d3a-4f15-8c6e-0a9b8c7d6e5f
written_by: { type: agent, name: claude-code }
content_type: text/markdown
lifecycle: { expires_at: null, extended_by: write }
attributes: { vcs.pr: 482, ci.run_url: "https://ci.example/runs/123" }
---
Integration tests fail with `ECONNREFUSED 127.0.0.1:5432` unless Postgres
is already running. Start it before `pnpm test`:
    docker compose up -d db
The test setup does not start it for you.
```

Frontmatter is the envelope: `address`+`key` say where it's true, `id` is identity, `lifecycle` says when it stops, `written_by` answers the fork. `version` counts corrections to this record; `supersedes` names an older record this one replaces. A fix to the same claim bumps `version`; a different claim that replaces it is a new record at version 1 that supersedes the old one. Anything else goes in `attributes` under ignorable namespaces. Same record serialises to JSON for wire use.

Around that record, a spec would mirror OpenTelemetry's layers: **Conventions** (shared names for address levels — global, project, repo, branch, plus whatever monorepos need — for kinds, and for attribute namespaces `vcs.*`, `ci.*`, `agent.*`, in one versioned registry) and **a contract** (a few operations).

## Remaining sections (present in original)

"What a skeptic would say" and "Open questions" sections exist in the post; their full body text was truncated in this capture.
