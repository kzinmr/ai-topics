---
source_url: https://aauth.dev
ingested: 2026-10-18
sha256: cc5f9d8a4aec30aeb015637683a579d69b77feca6c1b1dae2f04be851915605a
---

- 
 
- 
 
- 
 
- 
 
- 
 
- 
 
 
 
 
 
 
 
- 
 
- 
 
- 
 
- 
 
- 
 
- 
 
- 
 
- 
 
- 
 
- 
 
- 
 
- 
 AAuth — Agent Identity, Resource Access, and User Delegation
 
- 
 
- 
 
 
 Come to AAuth Night Oct 15 and the AAuth Workshop Oct 19. Details below 

 How AAuth WorksGetting StartedDeep DivesCommunity 

 

## Software Is Changing 

Clients used to be written. Now agents assemble them at runtime. 

The protocols underneath weren't built for that. > Try the demo Protocol Explorer 

 

## What Changed 

Software used to know at build time what it would call and what it would need. Now agents decide in the moment, against services they've never seen — the old protocols assumed neither. 

## > Client IDs Don't Travel 

In OAuth and OIDC, a client has no independent identity — a client_id at Google is meaningless at GitHub. Agents have no identity of their own to carry between services.

## > Copied Secrets Leak 

API keys are a shared secret issued by the service and copied to the client. Any secret copied to a workload will eventually leak somewhere it shouldn’t.

## > Decisions Happen Mid-Task 

Agents need authorization decisions mid-task. Consent lands on human timelines — and today's protocols treat pending as an error, not a first-class state.

## > Tool Chains Assemble Live 

Agents pick their tool chain at runtime, one call at a time. The sequence isn't declared in code — they choose the next tool as the task unfolds, and the chain shifts with every task.

## > Scopes Don't Capture Intent 

A scope is standing permission, not per-call intent. `mail.read` looks the same whether the agent is summarizing or scraping — policy can't tell them apart.

## > Calls Cross Trust Domains 

A single task can span orgs, clouds, and identity domains. Workload identity (SPIFFE) stops at the trust-domain edge — and authority stops there too. 

## Why AAuth? 

By Dick Hardt, author of OAuth 2.0 

After implementing authorization for our MCP server, I concluded OAuth is not a good fit for MCP ↗ and started working with others in the identity community who'd hit the same walls. 

AAuth is what came out of that work. It gives every HTTP client its own cryptographic identity and carries identity claims and authorization claims in the same token. It coexists with OAuth 2.0 and OpenID Connect rather than replacing them. 

The web gave servers identity. It's time clients got the same. 

## How AAuth Works 

AAuth has five access modes. All replace API keys with cryptographic identity. They differ in what the resource ends up knowing and which party established it — adopt incrementally as your needs expand. Per-call authorization, from R3, governs a single action rather than a class of access. Identity BasedResource ManagedPerson IdentityPerson Server ManagedFederatedPer-Call 

API keys replaced with a cryptographic agent identifier — no more shared secrets to leak. 
- 1 Agent → Resource HTTPSig w/ agent_token
- 2 Resource ⇠ Agent 200 OK 
- agent_token establishes the agent's identity 
- person_token names the person the agent acts for, at one resource 
- resource_token describes the access needed 
- auth_token grants an agent access to a resource 
- session-token issued by a resource for its own consumption, opaque to the agent 
- jwks_uri Person Server's JWKS endpoint, discovered via well-known metadata 

## Protocol Explorer 

Browse AAuth access modes, tokens, and headers with side-by-side wire examples. Open Explorer ↗ 

## Walkthrough Demo 
- › Bootstrap your own agent identity and keys 
- › Call the whoami AAuth resource 
- › Learn the protocol step by step 
- › Optionally uninstall when done 

Paste the prompt below into Claude Code, Cursor, or any CLI agent — your agent walks you through AAuth hands-on. 

AAuth is an HTTP authorization protocol that lets agents call protected resources on your behalf using signed requests instead of bearer tokens. The spec is at https://datatracker.ietf.org/doc/html/draft-hardt-oauth-aauth-protocol — consult it for any protocol detail.

This walkthrough teaches the protocol live, in front of a user who wants to learn it. Two goals:

- a keypair generated and the public key published, with agent metadata, at a URL the user controls
- signed calls to `whoami.aauth.dev` with each protocol step clearly explained — first the **identity-based flow**, then the **three-party flow** (agent ↔ person server ↔ resource)

This prompt is glue only. The bootstrap skills know how to set up and tear down; the fetch skill knows how to read and render `--explain` events. Before step 3, run `npx @aauth/fetch skill` and follow its "Inspecting requests" section — the events carry their own `summary` and `description` narration; render them, don't paraphrase or augment them.

## Pacing — one section per turn

The user reads in chat; pace the output so each piece lands alone.

- **One section per turn.** Each protocol exchange (or tight group, like the consent polls) is its own turn-ending message: the event's `summary` line on top, then the rendered events per the fetch skill. End the turn; the user's reply advances to the next section. Never bundle two sections into one message.
- **Front-load each phase.** Before Setup, the calls, and Uninstall, say in one or two sentences what's coming. The second call's front-loader must warn that it pauses for a browser approval.
- **Tell the user how to advance.** The front-loader before the first call must say the walkthrough pauses after each section and that replying with anything ("ok") advances it. Don't use a question prompt as the advance mechanism — a tool call after section text can swallow the text above it, so sections must end as plain text.
- **The CTA turn contains ONLY the CTA.** The moment `interaction_required` arrives, emit its `approval_url` (clickable), `code`, and `qr` (fenced code block, no language tag) plus one line saying you're waiting — nothing else in that turn. Latency here is the user staring at a spinner.
- **Deliverables end the turn.** Text emitted before a tool call in the same turn may never be displayed. The punchline must be the final text of its turn — no tool calls and no question tools after it.
- **No recap table, no closing invitation.** The per-section `summary` lines are the recap. After the punchline's explanation, stop — with one exception: if we installed this run, the punchline's final line tells the user one more reply brings the keep-or-uninstall question (see step 4). Without that line the user doesn't know the walkthrough has one turn left.
- **Don't leave background work running between turns.** The task notification fires when the background fetch exits — no polling loops, no `tail -f`.

## 1. Check for existing setup

```
npx @aauth/bootstrap list
```

If `agentProviders` is non-empty, the user already has an identity — name what's there in one line (agent URL, keystore, person server) and skip to step 3. Skip step 4 entirely: we didn't install it this run, so never offer to uninstall it.

## 2. Set up (if nothing exists)

```
npx @aauth/bootstrap skill setup
```

The skill is self-contained — follow it. Don't continue to step 3 until its `npx @aauth/fetch https://whoami.aauth.dev` verify step returns your `sub`.

## 3. Two signed calls

Both calls hit `whoami`, which echoes who is calling. Pass `--explain-log` with a path you choose under `~/.aauth/fetch/logs/` so you know exactly where the JSONL stream lands (a captured stderr stream is also JSONL when piped — either source works; pick one and stick with it).

### First call — identity-based flow (foreground; sub-second)

```
npx @aauth/fetch --explain --explain-log ~/.aauth/fetch/logs/walkthrough-1.jsonl https://whoami.aauth.dev
```

Render its one exchange as one section and end the turn. The response body is the point: the resource saw the agent's `sub` from the signature alone — no person server, no consent, no bearer token.

### Second call — three-party flow (background; pauses for consent)

```
npx @aauth/fetch --explain --explain-log ~/.aauth/fetch/logs/walkthrough-2.jsonl --prompt-consent "https://whoami.aauth.dev?scope=openid+profile"
```

`--prompt-consent` forces the consent prompt so the user sees the full interactive flow. Run it in the background with a `600000` ms timeout — the consent window is 600 s and humans take minutes to approve.

Then, one section per turn, the user advancing between them:

1. **The 401 exchange** — agent-token call → 401 + resource-token.
2. **The person-server exchange** — resource-token POSTed → 202 pending + approval code — immediately followed by **the CTA turn** (only the CTA; see Pacing).
3. **After the task notification: the consent polls** — 202s while the person decided, then the 200 whose body carries the freshly issued `auth_token`. That 200 is where the person server mints the token — don't bury it.
4. **The punchline** — the `auth_token_request` pair. The response body (`sub`, `agent`, `name`, `email`) shows the resource now sees both who is calling and on whose behalf, with claims the person server vouched for. This ends the turn. If we installed this run, close with one line saying a reply brings the keep-or-uninstall question; otherwise nothing follows the explanation.

## 4. Keep or uninstall (only if we installed in step 2)

If step 1 found an existing provider: the walkthrough is done — say so and stop.

If we ran setup this session: ask proactively in the turn **after** the punchline (never in the same turn — a question tool swallows any text above it). One question, keep first and default:

- **Keep installed** — they just proved it works; the keys are useful next time.
- **Uninstall** — return to a clean state.

If they choose uninstall:

```
npx @aauth/bootstrap skill uninstall
```

The skill is self-contained; the Keep/Uninstall answer counts as its confirmation — don't re-ask. Verify world state, not exit codes: the JWKS URL returns 404, and `list` shows `agentProviders: []`. walkthrough.md — copy and paste into your agent Copy prompt 

## Specs 

 dickhardt/AAuth on GitHub — issues, discussions, and development 

## AAuth Protocol Internet-Draft 

The authorization protocol for agent-to-resource access. Five access modes, four token types, agent governance, missions, clarification chat, and call chaining. editor's copy ↗

## AAuth Bootstrapping Internet-Draft 

Guidance for agent providers on enrolling agents and issuing AAuth agent tokens — per-platform key handling, optional platform attestation, agent identifier strategies, and refresh patterns. editor's copy ↗

## AAuth Rich Resource Requests (R3) Exploratory 

Vocabulary-based authorization using formats agents already understand (MCP, OpenAPI, gRPC, GraphQL), plus per-call proposals for operations authorized one call at a time. 

## SDKs 

 

## Node.js SDK 

Reference SDK for agents and MCP servers with signed-request auth.

 

## .NET SDK 

Reference SDK and samples for .NET agents and MCP servers with signed-request auth.

 

## Go SDK 

Reference SDK for Go agents and MCP servers with signed-request auth.

 

## Python Demo Source 

End-to-end A2A multi-agent flow with Keycloak and user consent. 

## Deep Dives 

## Self-Driving Software: What OAuth Can’t Do for AI Agents 2026-09-02 

 Dick Hardt & Ken Simpson — MailChannels interview on agent accountability, why OAuth was never built for agents, and killing off API keys

## AAuth Night: Moving Beyond OAuth 2026-07-01 

 Talks and demos from the first AAuth Night — July 2026, AI Engineer World's Fair 

 What is AAuth? Dick Hardt ↗

 Why We Need AAuth Karl McGuinness ↗

 All talks & demos Playlist · 13 videos ↗

 AAuth Night recap Dick Hardt ↗

## The Errand: What Sending a Kid to the Shop Teaches Us About Agentic Delegation 2026-06-10 

 Dasith Wijesiriwardena — A corner-shop errand analogy for how AAuth lets agents act safely on a user's behalf

## Insecure Agents Podcast: Moving Beyond OAuth and the Future of Agent Auth 2026-06-03 

 Dick Hardt — Why OAuth breaks for agents and running them without API keys

## Exploring AAuth for Agent Identity and Access Management 2026-05-14 

 Christian Posta — Overview of an open-source AAuth demo with identity-based and three-party access modes

## Know Which of Your Agents Wrote What 2026-04-28 

 Mark Hendrickson — Per-row attribution for agent writes via AAuth identity in Neotoma

## AAuth Now Has a Mission Layer 2026-04-15 

 Karl McGuinness — Mission is now a first-class protocol object — is the layer strong enough?

## Open-World OAuth Still Needs Mission Shaping 2026-03-21 

 Karl McGuinness — Open-world OAuth, discovery, and bounded authority across delegation chains

## Mission Architecture on AAuth 2026-03-15 

 Karl McGuinness — Whether AAuth is the right protocol foundation for mission-bound authorization

## Deep Dive AAuth — Identity and Access Management for AI Agents 2026-02-17 

 Christian Posta — Comprehensive overview of AAuth architecture and design

## Do AI Agents Need Their Own Identity? 2025-06-02 

 Christian Posta — The case for independent agent identity 

## Community 

Join the discussion on Slack. 

## IETF Slack 

IETF #aauth channel for AAuth specification discussion and feedback.

## AAuth Slack 

AAuth community Slack for implementation discussion and questions. 

## Events 

## AAuth Night 

Our first AAuth Night was a huge success — thanks to everyone who came out! The next one will be October 15th in San Francisco the evening of the AI Security Summit. Save your spot on Luma. RSVP on Luma ↗ 

## AAuth Workshop 

Working on implementing AAuth? Join Dick Hardt and fellow builders at Postman HQ in San Francisco on October 19th, 1–5pm, for an afternoon of discussion, learning, and shared discoveries. RSVP on Luma ↗ AAuth 

Cryptographic identity, resource access, and user delegation — for every HTTP client. 

Founding sponsor: Geffen Posner llms.txt Edit this page ↗
