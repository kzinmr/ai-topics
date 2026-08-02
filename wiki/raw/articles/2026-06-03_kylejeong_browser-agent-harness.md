---
title: "The web wasn't built for browser agents, here's how we built a harness to make it work"
source: https://www.browserbase.com/blog/what-is-a-browser-agent-harness
author: Kyle Jeong
published: 2026-06-03
scraped: 2026-08-02
type: article
tags: [browser-agent, agent-harness, browserbase, stagehand, cdp, context-engineering, agent-infrastructure]
---

# The web wasn't built for browser agents, here's how we built a harness to make it work

Author: Kyle Jeong (Browserbase Engineering). Published June 3, 2026 (12 min read).

## TL;DR

The browser agent harness is what separates a cool demo and production agents. It should never be "give the model CDP and get out of the way." The moment you put a browser agent in front of real customers on the real web, you need a harness with security layers, caching, identity, credential brokering, and a skill memory.

## What even is an agent harness?

An "agent harness" is just rebranded context engineering. The concept was popularized by LangChain (the first "harness") and operationalized by Claude Code as a living example.

The harness is everything around the model that turns a next token predictor into something that ships work: the tools it can call, the files it can read, the loop that decides when it's done, and the guardrails that keep it from doing something dumb.

Claude Code is the canonical coding agent harness. It exposes Read/Write/Edit/Bash, an editable CLAUDE.md, a skill folder, a sandbox, and a small core loop.

A raw model in a raw terminal fails in predictable ways. The harness exists to fix four of them:

1. **Tools shaped to pre-training knowledge.** Claude Code's essential tool surface is five primitives: Read, Write, Edit, Bash, and web search. Models have core memory built during pre-training; the harness gives it tools it already understands from millions of code examples in training instead of highly specific verbs like `evaluate-bash-command`. The smaller and more familiar the tool surface, the fewer tokens the model wastes figuring out how to call it.

2. **Context-bloat prevention.** A real repo is millions of lines; an effective context window is not (~200k). Without a harness, the model either sees too little (hallucinates imports, APIs, file paths) or too much (drowns in irrelevant code). Claude Code solves this with surgical file reads, CLAUDE.md for project conventions, compact diffs, and a compaction step. The harness is a compression engine that decides what the model sees every turn.

3. **A reasoning loop for accuracy.** Single-shot code generation is brittle. A harness runs a plan-act-observe loop: propose an edit, apply it, read the result, run the tests, decide if it's right, iterate.

4. (Fourth failure mode referenced but implied: guardrails / safety.)

## The raw-CDP camp

Recently many people have been experimenting with browser agents exposing raw CDP commands as tool calls — "removing the harness and letting the agent run free." The argument: the model already knows CDP, helpers are abstractions, abstractions are constraints, delete them.

The author agrees on a narrow version: inside the sandbox, when a single agent iterates on a single task, you should let it touch the metal (as done inside Autobrowse, where an agent gets a real browser, runs end to end, and edits its own skill). But that's just the learning loop.

Production browser agents have four main problems a raw-CDP harness doesn't solve:

1. **The DOM is adversarial input.** Every page the agent loads is untrusted text. Without a layer between the DOM and the model's context, you have a prompt injection vector wearing a `<div>`. Not to mention token bloat from passing DOM to context.
2. **Relearning how to navigate the same site (a hundred times) is wasted tokens.** A naive loop pays the full discovery cost on every run.
3. **Production browsers need an identity.** A locally-spawned Chrome with default flags gets blocked, captcha'd, or fingerprinted out of existence on the sites that matter (banks, brokerages, portals).
4. **You can't show the model your customer's password.** "Let the model write the helper" stops being cute the moment the helper needs an MFA code.

## What a good browser agent harness actually looks like

Shipped at scale for Ramp, Interaction, Lovable, and a long tail of teams. The harness has converged on six layers, each small, editable, and existing for a reason they got burned by:

### 1. A security layer between the DOM and the model
The DOM is technically user-generated content; concatenating it into a prompt builds a prompt-injection delivery system. Every page the agent reads is treated as untrusted by default. Stagehand's `extract` and `observe` primitives don't hand the agent raw HTML — they hand it a structured, schema-validated projection of the page, with hidden text stripped, off-screen elements de-prioritized, and known injection patterns flagged. Pattern: **parse, project, validate, then prompt**. "Every byte of HTML the model reads is a place an attacker can put words."

### 2. A caching layer
Every site has a shape, but the login flow doesn't change between Tuesday and Wednesday. Cache three things:
- **Page-level snapshots** — accessibility tree, resolved DOM, screenshot, reused inside a session
- **Action-level cache** — the selector that worked for "checkout" last time gets tried first
- **Skill-level cache** — a full graduated Autobrowse playbook pinned to a domain, pulled in on first encounter and reused forever

### 3. An identity layer
A locally launched Chrome talking raw CDP is the most fingerprintable thing on the open web (automation flag, headless user-agent, navigator.webdriver, missing audio context, default font list). Production browser agents need: residential and mobile proxies rotated per session, real fingerprint stacks, captcha solving in the loop, and a signed agent identity for sites that want to allowlist agents.

### 4. A credential brokering layer
Split access into two halves: the agent gets a session reference and a short-lived token; the harness holds the real secret. When the loop says "fill the password field," the harness fills it out of band, before the model ever has the bytes in its context.

### 5. (Skill memory / filesystem layer)
Referenced in the closing summary: a browser agent harness has "simple primitives + an identity layer + a skill folder + a credential broker + a cache + a filesystem."

### 6. (Observability/debugging layer)
The platform layer: session replay, runtime.

## Stagehand vs. raw CDP decision tree

```
Does the agent need credentials it can't see?
├── yes → harness
└── no
    ├── Does the page contain untrusted text?
    │   ├── yes → harness
    │   └── no
    │       ├── Are you running this against many sites, many times?
    │       │   ├── yes → harness
    │       │   └── no
    │       │       ├── Are you iterating on a single task in a sandbox?
    │       │       │   ├── yes → raw CDP (Autobrowse-style)
    │       │       │   └── no  → raw CDP
```

- **Raw-CDP harnesses**: ~600 lines or less, model may edit its own helpers. Maximum action space, minimum scaffolding. Solo agent on the bench.
- **Stagehand**: `act`, `observe`, `extract`, `agent` primitives over raw CDP, with caching, schema validation, identity, and a Browserbase-native session. Production fit.
- **Browserbase platform**: the environment the harness runs in — Browsers, Identity, proxies, session replay, runtime.

## Why this changes workflows

Once the harness is in place, the operator's job changes from writing browser code to writing skills, schemas, and policies:
- An engineer writes a scraper → now a skill
- A security team writes a code review checklist → now a DOM policy
- A product team writes a crawler config → now a schema for what the agent extracts
- An ops team owns EC2 boxes running headless Chrome → a fleet of sessions with identity

The harness compresses "running a browser agent in production" from a six-month infra project into a config file plus a few markdown files.

## Conclusion

The raw-CDP camp is right that abstractions you can't edit are constraints; wrong that the answer is to delete them. The right answer is what Claude Code pioneered: small, editable, opinionated abstractions with the model in the loop. A coding agent harness has Read/Write/Edit/Bash plus a sandbox plus a skill folder. A browser agent harness has simple primitives + an identity layer + a skill folder + a credential broker + a cache + a filesystem. Same shape, harder problem.

> "The models are already good enough to drive the browser. The harness is what makes it reliable and safe to drive at scale." — Kyle Jeong
