---
type: x_article
x_article_title: "How to build your own agent harness???"
x_article_author: "@iiidevs (Mike Piccolo)"
x_article_id: "2060024515619397638"
getxapi: false
date: 2026-05-28
source: https://x.com/i/article/2060024515619397638
---

# How to build your own agent harness???

Most agent teams don't build a harness. They adopt one. LangChain, LangGraph, OpenAI Agents SDK, Anthropic SDK, CrewAI, AutoGen, the loop, the tools, the memory, and the orchestration are picked off the shelf as a single decision. The harness is a framework you import. If something inside it doesn't fit, you fork it, fight it, or work around it.

I think that shape is wrong, and it's the reason every long-running agent team eventually ends up rewriting its harness from scratch. The harness isn't one thing. It's ten or twelve different things bundled together because the surrounding ecosystem doesn't give you a way to compose them. Pi agent packages are on the right track, but they are still in the paradigm of "Add another service and integrate it with all others." The iii engine treats all workers the same and removes the integration logic completely. The provider router, the credential vault, the policy engine, the approval gate, the model catalog, the session storage, the budget tracker, the after-call hook fanout, and the durable turn loop are independent concerns. These are all interoperable with your queue, http/api server, streaming, even browser workers. A framework that ships them as one block is selling you a tradeoff you didn't have to make.

The bet underneath iii is that they shouldn't be one block. There should be a set of workers on a shared engine, each replaceable, each versioned independently, each connected by a single primitive: a trigger (iii.trigger()) that every other worker also uses. The harness becomes a stack of installable workers, and "build your own" stops meaning "fork a framework." It means "swap a few workers."

## The 15 jobs an agent harness has to do

If you strip a production agent harness back to its responsibilities, you get a list that looks roughly like this:

1. Accept a turn request from a client and persist it
2. Resolve credentials for whichever model provider gets called
3. Look up what the chosen model can actually do (vision, tools, streaming, context window)
4. Drive the per-turn state machine, provision, stream assistant, run tools, steer, tear down
5. Load and serve skill bodies that describe each function's request shape, error codes, and usage notes
6. Assemble the system prompt, mode paragraph, identity preamble, working directory, and default skills appendix
7. Stream tokens back to the client as the model produces them
8. Check every tool call against a policy before it runs
9. Pause tool calls that need a human decision and route the answer back to the right turn
10. Track LLM spend against per-workspace or per-agent budgets
11. Run hooks before and after tool calls (logging, redaction, custom side effects)
12. Persist the session as a branching tree so forks and resumes work
13. Compact session history when the context window fills up
14. Emit an event stream that the UI subscribes to
15. Carry one OpenTelemetry trace across every step so you can debug it

## The stack, by worker

The iii harness ships every one of those jobs as a separate worker on the workers.iii.dev registry:

| Worker | Job |
|--------|-----|
| harness-meta | Entrypoint + OpenTelemetry span seeding + policy engine |
| models-catalog | Static model capabilities manifest |
| provider-anthropic | Anthropic SSE stream → iii channel |
| provider-openai | OpenAI SSE stream → iii channel |
| auth-credentials | File-backed credential resolution |
| iii-directory | Skill body registry (iii://<worker>/<function>) |
| approval-gate | approval::resolve handler |
| session | Branching session tree CRUD |
| llm-budget | Per-workspace/per-agent spend tracking |
| hook-fanout | before/after tool call publish_collect |
| context-compaction | agent::turn_end subscriber |
| turn-orchestrator | 7-state durable per-turn FSM |

## How the loop actually runs

The turn-orchestrator has a 7-state FSM:
1. provisioning — boots sandbox, downloads skills, assembles system prompt
2. assistant_streaming — calls provider::<name>::stream, drains SSE into iii channel
3. function_execute — dispatches tool calls through dispatchWithHook (policy check → allow/deny/needs_approval)
4. function_awaiting_approval — waits for approval::resolve
5. steering_check — decides continue/stop/max_turns
6. stopped — clean exit
7. failed — error terminal state

Fail-closed by construction: if the policy worker is unreachable or the 5-second timeout fires, consultBefore denies the call.

## The harness is a slider, not a fork in the road

**Thin harness**: turn-orchestrator + provider-anthropic + auth-credentials + minimal harness-meta. No approvals, no budgets, no policy engine. Trust the model. For autonomous research agents, experimental loops.

**Thick harness**: all thirteen workers + context-compaction + custom policy worker + custom approval-gate + Slack-integrated approval surface + budget worker enforcing per-workspace caps. For customer workflows where every tool call needs to be auditable.

The architectural distance between thin and thick isn't a rewrite. It's a config change. Same primitives, same wire protocol, same trace shape, same observability story. The slider moves by adding and removing workers from your config.yaml.

## Build your own

Five concrete examples of replacing individual layers:
1. Replace model catalogue with live API worker
2. Add a new provider (one folder, one iii.worker.yaml, one register.ts)
3. Serve skills from private artifact store
4. Override system prompt entirely via run::start system_prompt field
5. Replace approval gate UI surface (Slack /commands instead of console)

## The bet

A harness is not a thing you install. A harness is a set of jobs your system has to do for an agent to run durably, safely and observably. The framework era bundled those jobs together because nothing underneath gave you a way to compose them.

iii's bet is that one primitive — a worker that connects to the engine over WebSocket and registers functions and triggers — is small enough to absorb every one of those jobs separately, and that the resulting stack is more useful than any framework because every layer is independently replaceable.

You don't adopt the iii harness. You install the workers you want, write the ones you need, and end up with a harness shaped exactly like your system.

— Mike Piccolo, Founder & CEO @iiidevs

Links: workers.iii.dev, github.com/iii-hq/workers, github.com/iii-hq/iii, iii.dev/docs, discord.gg/iiidev
