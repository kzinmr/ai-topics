---
title: "Duet-style hierarchical agent assistant"
created: 2026-10-30
updated: 2026-11-03
type: concept
tags:
  - ai-agents
  - agent-harness
  - human-in-the-loop
  - agent-architecture
  - context-management
  - agent-tooling
  - anthropic
sources:
  - raw/articles/fig.blue--posts-duet-is-the-future--3c8f5710.md
  - raw/articles/2026-10-22_anthropic-claude-duet-launch.md
  - raw/newsletters/2026-10-31-claude-duet.md
  - raw/newsletters/2026-11-02-how-i-ai-grok-vs-dot-vs-muse-vs-duet-how-figma-s-pms-actually-use-ai-every-day.md
related:
  - concepts/agent-harnesses
  - concepts/human-in-the-loop
  - concepts/multi-agent-session-observability
  - concepts/harness-engineering/agent-harness
confidence: medium
---

# Duet-style hierarchical agent assistant

A **Duet-style assistant** is a personal-agent product shape in which the unit of
work is not a chat session but a **channel**, and where capability is granted in a
**decreasing-access hierarchy** (top level sees everything but holds no low-level
access; channels hold real access inside constrained context; sub-threads are
constrained further to specific code sandboxes). The term comes from practitioner
reaction to Anthropic's Claude Duet research preview.

This page documents the *interaction-and-authorization pattern*, not the product.
For the launch facts (Opus 5.5 backing, morning brief, Approve/Not-now gates) see the
raw launch capture and [[entities/anthropic]].

Source (primary practitioner writeup): [fig.blue, "Duet is the future of chatbot
interaction", 2026-10-29](../raw/articles/fig.blue--posts-duet-is-the-future--3c8f5710.md)
(HN: 118 points / 125 comments). Written by a self-declared non-Anthropic affiliate,
"Written by a human."

## The hierarchy of concerns

The author names this as the single innovation that matters, and it is a
**capability-scoping** design rather than a memory or prompting design:

| Layer | Sees | Can do |
|---|---|---|
| Duet top level | bird's-eye view of all workstreams | **no low-level access** |
| Channel | one lane of work | real access (e.g. specific GitHub repos), constrained context |
| Sub-thread | one task | further constrained, works inside specific code sandboxes |
| Desktop app | local hosts the user permits | usually only QA / deployment edge, after cloud coding is done |

The notable inversion is that the *orchestrating* layer is the least privileged.
This is the opposite of the common harness design where a top-level planner holds
every credential and delegates downward. Compare [[concepts/harness-engineering/agent-harness]]
and [[concepts/capability-based-security]].

The author's own baseline: "Most of this is how I already preferred to arrange my
agents, and similar flows could be hacked together with some ducttape and API
credits. Duet just makes this hierarchy a natural part of the core product."

## Channels as session management

The pain point being solved is explicitly *session bookkeeping*, not model quality:
"workstreams get lost, context must be carefully maintained, sessions get
misnamed." Two properties do the work:

- The assistant **creates and manages channels itself**, so a natural hierarchy
  emerges without user bookkeeping.
- **Channels can see and reference each other**, so cross-lane context is available
  without merging lanes — routing work to the right lane becomes an agent task.
- `Cmd-k` channel switching is described as already reflexive for the author.

This is a UI-shaped answer to the same problem [[concepts/multi-agent-session-observability]]
addresses from the observability side: the failure mode is "some agent did brilliant
work for me on a box somewhere that I've neglected and will be forgotten forever."

## Access policy as a product feature

Two claims distinguish this from a credential-store assistant:

1. **Repo access is scoped per channel**, so a channel "cannot commingle work from my
   other projects."
2. **The product stores no credentials and actively discourages being given them.**
   At most it may act through an existing Chrome session on the user's behalf — which
   the author says has never been requested. It prefers the connector ecosystem the
   host already has, "and seems content to stay in its lane."

The author's stated pet peeve is the alternative: most assistant apps "won't do much
until you hand them the keys," and even a credential store that blinds the agent to
values "could still enter those in something untrusted."

## Latency and verbosity as first-class constraints

- **Speed over background completeness**: "Duet clearly prioritizes getting a snappy
  response to the user even if background work is needed." Reported as noticeably
  faster than the same base model in other Claude UIs, attributed to tuning. Framed
  as a hard usability requirement: "If you want to be my shell to the world, I am not
  going to sit and twiddle my thumbs between commands." Latency-as-assistant-prerequisite
  is the same axis as [[concepts/inference-speed-development]].
- **Short responses by default**: "Nobody wants to read a full page response to a
  simple question, which has been the de facto chatbot experience for years" —
  previously something the author had to obtain by instructing agents to be succinct.
- **Reaction emojis as a *low-bandwidth ack***: Duet "uses it to give me an okay
  without elaborating further", contrasted with a competitor that "tended to thumbs up
  everything." Personality changes whether a reaction is information or noise.

## Limitations and dissent (do not drop these)

- Beta defects reported: threads running but not visible; delegated repo access
  failing to attach, suspected race between agent start and access attachment.
- **Vendor dependence is real and load-bearing**: "It's supposedly powered by Opus 5.5."
  The speed claim is therefore about a tuned product/model pairing, not a general result.
- The author self-limits the verdict: his use cases favour Duet; "Muse might be a
  better fit for others. YMMV." Competitors **Dot** and **Muse** are rated better on
  voice — "Dot still reigns on voice interaction," while Anthropic's voice mode is
  "still just glorified speech-to-text."
- **The HN thread's top complaint is that the post never explains what Duet is**
  (125 comments, 118 points). The product-page framing — "Get back to what needs you",
  morning brief, Approve/Not-now cards for monetary and irreversible actions — is in the
  launch capture, and the practitioner piece assumes it.
- Predictive claim, unverified: "I suspect it's going to be the default experience for
  all chatbot UIs in the near future."
- **Aakash Gupta's hands-on review (Oct 31, 2026) adds two dissent data points**
  ([[raw/newsletters/2026-10-31-claude-duet.md]]): (a) for a power user, Duet is *not* a
  Claude Code replacement — "Claude Code is the best AI harness, but can Duet replace it?
  Spoiler alert, I don't think so" — and the fixed **Opus 5.5** backend with no model or
  effort picker is a cost problem for Sonnet-heavy workflows; (b) recall quality is weak,
  especially over local Claude Code sessions, and "most of it needs to be prompted"
  despite the proactive framing. He also contrasts **Grok Bot's "Vault"** (remembers
  logins/cards/addresses without the bot ever seeing them) as a differentiator Duet lacks
  — a privacy-shaped axis the fig.blue hierarchy analysis does not cover.

## Cross-agent benchmark: Claire Vo's nine-task test (Nov 2, 2026)

Claire Vo (chatprd.ai / *How I AI*, Lenny's Podcast 2026-11-02) ran **Grok Bot, Dot, Meta's
Muse, and Claude Duet** through nine real-world tasks — Slack replies, inbox triage, coding,
video editing, Figma thumbnails, family projects, shopping — producing the first
multi-agent *evaluation* data bearing on this pattern (prior coverage here was one practitioner
essay plus vendor pages). Duet-relevant findings:

- **Duet was consistently the slowest of the four.** Vo's product principle: when an agent
  disappears for several minutes, users lose context and stop using it — the same
  latency-as-prerequisite axis as the fig.blue essay's "I am not going to sit and twiddle my
  thumbs between commands," now with comparative numbers (Muse won first place on 4 of 9 tasks).
- **Duet over-asks permission**: it requested approval **4 times** during the benchmark vs
  **1 time for every other agent**. The diminishing-access hierarchy (above) has a UX cost:
  caution reads as "something the user must supervise rather than trust."
- **Connector/skill asymmetry contaminated the field**: a Codex audit of Vo's setup found the
  agents lacked equivalent tools — Muse had no Slack or GitHub connectors, which blocked
  several of its work tasks. Fair personal-agent comparison requires equalized setups.
- **Where Duet still won**: strongest coding judgment alongside Dot — Duet found a *second* bug
  in a Sentry-fix task and avoided duplicating work Dot had already completed. Vo would still
  pick Claude/Codex for serious coding, "just not through Duet's personal-agent interface."
- **No universal winner; choose by job**: Grok Bot 93% overall (won Figma, inbox triage,
  shopping) is Vo's work pick; Muse is her personal-life pick (best short-form video and family
  newspaper with near-zero prompting); Dot showed the lone "chief-of-staff" moment (only agent
  that asked whether her Lovable talk was paid and remote). Her conclusion — different agents
  belong in different parts of life — cuts against the Duet page's implicit single-assistant
  framing.

Source: [How I AI: Grok vs. Dot vs. Muse vs. Duet](https://www.lennysnewsletter.com/p/how-i-ai-grok-vs-dot-vs-muse-vs-duet)
(raw: `raw/newsletters/2026-11-02-how-i-ai-grok-vs-dot-vs-muse-vs-duet-how-figma-s-pms-actually-use-ai-every-day.md`).
See also [[concepts/agentic-engineering/pm-os-shared-agent-skills]] (same episode).

## Status

`confidence: medium` — the pattern is documented from one practitioner essay plus one
vendor product page. The hierarchy and channel mechanics are described concretely and
consistently, but there is no independent evaluation, no benchmark, and no second
hands-on account. Note that "Duet" is also the name of an unrelated Decagon product
([[entities/decagon]]), so the term needs disambiguation in future mentions.

## Related pages

- [[concepts/agent-harnesses]]
- [[concepts/harness-engineering/agent-harness]]
- [[concepts/human-in-the-loop]] — Approve/Not-now gates
- [[concepts/multi-agent-session-observability]] — lost-workstreams failure mode
- [[concepts/context-engineering/index]] — lane-scoped context
- [[concepts/capability-based-security]] — least-privilege orchestration
- [[entities/anthropic]] — Claude Duet launch
- [[concepts/inference-speed-development]]
