---
title: "Designing Agent-Friendly APIs"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/designing-agent-friendly-apis/"
scraped: "2026-08-15T06:00:08.750886+00:00"
lastmod: "2026-08-12T16:31:57Z"
type: "sitemap"
---

# Designing Agent-Friendly APIs

**Source**: [https://www.pinecone.io/blog/designing-agent-friendly-apis/](https://www.pinecone.io/blog/designing-agent-friendly-apis/)

←
Blog
Designing Agent-Friendly APIs
Joerg Schad
Aug 12, 2026
Engineering
Share:
Jump to section:
The consumer changed
How agents actually fail against a classic API
Measuring agent-friendliness
Principle 1: Errors are guidance
Principle 2: Budget the reader's context
Principle 3: Self-description beats documentation
Principle 4: Safe at machine tempo
Principle 5: Access without a human in the loop
Principle 6: The agent surface is a product, not a mirror
Old wine in new bottles?
Further reading
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
At Pinecone we develop our products with both human and agentic consumers in mind. Designing for that second kind of consumer taught the team something about API design that generalizes well past those three products: every API team is about to serve an agentic consumer, whether they design for it or not.
The consumer changed
API design has, until recently, assumed a particular reader: back when 'the reader' meant a human developer with docs open in one tab and Stack Overflow in the other. That developer evaluates the API once, writes an integration, and moves on. Agents are a second reader now, and likely soon the dominant one. The unit of adoption is shifting from a developer writing SDK code to an agent calling a tool mid-task: an agent doesn't integrate with an API once, it re-chooses the API on every task, and it either succeeds unattended or the product silently drops out of the loop.
Three properties make agents a new kind of consumer:
Their recovery is in-band and metered.
An agent can't file a support ticket or ping a colleague mid-task; everything it learns comes from what the API returns. Every detour through docs or search is billed in turns (one full round-trip through the model) and tokens. If the response doesn't say what went wrong and what to do next, the agent guesses, and every guess spends someone else's budget.
Their context is a scarce resource.
Every byte returned is billed as tokens, and it displaces the reasoning the agent needs to finish the job. A verbose response used to be a style complaint; now it's a defect with a per-request price tag. Cheaper tokens don't help, because context is attention: quality degrades as the window fills, and the budget shrinks even where the bill doesn't.
They operate at machine tempo.
Agents retry aggressively, parallelize freely, and act unattended, so whatever the API's failure modes are, they now execute at machine speed with no human sanity check in the loop.
This is becoming a discipline with a name:
Agent Experience
, or AX, coined in early 2025 by Netlify's Mathias Biilmann, sitting alongside developer experience the way DX once elbowed in next to UX. There's a
community site
and an emerging
scoring framework
— think Lighthouse, but for how well agents can use your service.
How agents actually fail against a classic API
Before principles, symptoms. Every failure pattern below is real, observed against production APIs, ours included. The ones our own audit caught have since been fixed (the list, with links, closes this post); we keep the examples in their original unflattering form, because these are the categories every classic API accumulates.
Training-data gravity.
Deprecated API shapes dominate the model's priors, because that's what years of tutorials and answers taught it. Unless docs and responses actively steer to the modern path, agents will write yesterday's API forever. We watched this live in our own cold trials: a smaller model's very first action was to install a package name we retired in 2024, while the current-generation model went straight to the modern API. The priors are a distribution channel, and they lag.
Capability cliffs.
The agent-facing surface — typically an MCP server (Model Context Protocol, the emerging standard interface between agents and tools) — exposes a strict subset of what the SDK can do. The agent starts a task inside the tool, hits the cliff halfway through, and either shells out to hand-written code or gives up.
The signup wall.
The first successful call requires a human with a browser, an email inbox, and a credit card. For a cold agent, time-to-first-call is infinite.
None of these registers as a bug when the reader is human. A person squints at the rejected-key message, checks their clipboard, figures it out. An agent can't squint. Agents are a magnifying glass for every corner an API cuts, and the person watching the transcript concludes, fairly or not, that the product doesn't work.
Measuring agent-friendliness
"Agent-friendly" stays a slogan until numbers get attached to it. We settled on two metrics that do most of the work:
Turns-to-first-successful-call (TTFSC).
Start an agent with zero prior context and a task that requires the API, then count the round-trips until the first successful call. This is time-to-hello-world for the agent era, and it's brutally honest: every unclear error, every doc detour, every auth dead-end shows up as a turn.
Unattended task-success rate.
The percentage of realistic, multi-step tasks an agent completes against the API with zero human intervention. This is the number that decides whether agents keep choosing a product.
Behind those two, we track the diagnostic ones: the percentage of errors that are actionable (they state a fix, not just a failure), token cost per completed task, tool calls per task, and error rates by class. We run these as
evaluations in CI
, the way Anthropic iterates on its own tools: a cold agent against staging on every release, with a TTFSC regression treated like any other broken build.
We ran the experiment on our own API while drafting this post: three cold trials of a current-generation model (Claude Sonnet 5) in a bare harness. An API key in the environment, no docs, no tools, no SDK preinstalled. The task was "store a handful of documents, retrieve the most relevant one." All three succeeded unattended: median 6 turns to the first successful API call, 11 turns to the first search that returned matches, roughly 90 seconds and $0.30 per run. Three runs of one model is a smoke test, not science, but the transcripts taught us more than the medians. The agent that chose raw REST reached its first successful call in 3 turns; its only stumble was a search right after upsert that silently returned empty until it retried. The two agents that chose our Python SDK spent nearly half their turns learning call signatures from bare TypeErrors — one ended up reading the SDK's source to find the contract. It cost three transcripts to learn that the raw API taught the agent what it needed and the SDK's errors didn't. (The specific findings, and the fixes they produced, are published at the end of this post.)
The rest of this post is the checklist we now hold our own surface to: six design principles, a note on docs, and one organizational lesson.
Principle 1: Errors are guidance
The error message is the only piece of documentation an agent is guaranteed to read, so we write it like the prompt it is.
Our standard: every user-facing error carries three things — what was wrong (the specific field or value, and what was expected), the fix (a concrete next action), and a doc link when the fix doesn't fit in a sentence. "Invalid request" fails all three.
Bad:
Invalid request.
Good:
Response is too large. To reduce the size, try a lower top_k value, or omit values and metadata.
The second error costs one turn. The first costs as many turns as the agent needs to guess our intent, if it ever does.
Alongside the prose, we expose a stable, machine-readable error code (
RFC 9457's Problem Details
is the standard shape). Codes are the contract agents and SDKs branch on; prose becomes non-contractual, free to improve anytime without a compatibility review.
Two failure patterns deserve explicit call-outs, because we've watched agents lose whole sessions to each. Missing and invalid get treated as different errors with different fixes: no credential and rejected credential aren't the same problem. A coarse check never masks a specific one either: validations are ordered so the most actionable error wins, or both signals return.
One objection came up repeatedly: rich errors seem like they'd leak information, since "index not found" tells an attacker which resources exist. The fix is a single invariant: authorized callers get the precise error, everyone else gets the same wall they always got. Enrichment for a caller who could legitimately reach the resource never expands the attack surface for one who couldn't.
We also gave errors one home. When public error text is authored independently in the gateway, the auth layer, and the service, the contract decays one layer at a time: the same failure teaches in one path and dead-ends in another. Every public message routes through a single choke point, where the contract is enforced.
Principle 2: Budget the reader's context
The response lands in a context window the agent needs for reasoning, so we spend that space carefully. Functionally, it's ours to spend or waste.
Everything gets bounded.
No unbounded lists, no dumps, no firehoses. Pagination and caps apply to every list-like response, including tool output and docs search, not just REST endpoints. When truncating, we say so and say how to narrow: "Showing 20 of 1,340 results; filter by namespace to reduce." A silent cap reads as "that's everything," and the agent proceeds on a false premise.
Responses are shaped for a reader that pays per token.
Anthropic's
tool-writing guide
has data on this: semantically meaningful identifiers measurably outperform opaque UUIDs for model precision, and offering a response_format of concise vs detailed cut token usage roughly threefold in their examples. High-signal fields come first; flexibility isn't a virtue when every field costs money.
Search wins over list.
When the agent knows what it's looking for, search_contacts(query) beats list_contacts() plus agent-side filtering; query planning shouldn't happen in the agent's head.
Success is verifiable in-band.
A successful write returns enough — IDs, counts, readiness state — that the agent can confirm the effect without a follow-up read.
Principle 3: Self-description beats documentation
An agent that can ask the API "what can I do here?" one-shots its task. An agent that has to guess, flails. We ship describe/capabilities endpoints that answer the operational questions in-band: what a resource accepts, which fields are filterable, what the limits are, what state it's in.
An OpenAPI spec is table stakes. Agents read descriptions exactly as written, so a complete spec with vague descriptions still fails them. A description that says what an endpoint returns but not when to use it leaves the choice to the model's priors, so every parameter gets a description and a realistic example.
Deprecation now means forever, unless someone acts on it. A deprecated shape that lingers in responses and canonical examples becomes every agent's default, because that's what the training data shows. We deprecate loudly, mark the old path unmistakably, and make the modern path the canonical example everywhere.
Principle 4: Safe at machine tempo
We design as if every operation will be retried, parallelized, and occasionally invoked with confidently wrong arguments, because it will be, at speeds no human operator ever achieved.
Idempotency is a contract, not a nicety.
Agents retry by default, so a retried mutation is a no-op, not a duplicate, and whichever semantics apply are documented explicitly. Where natural idempotency doesn't fit, idempotency keys fill the gap.
Rate limits are pace-able.
X-RateLimit-* headers and Retry-After let an agent throttle itself proactively; without them it slams into the wall and backs off blindly.
Predictability matters.
Same input and state yield the same shape and outcome; where results can legitimately vary, the response says so. Agents build multi-step plans on top of that consistency, and every surprise invalidates a plan.
Guardrails sit at the boundary:
dry-run and preview modes, reversibility where possible, confirmation gates on destructive operations. An agent will do the dumb thing faster than any human ever could, so the dumb thing, done fast, has to be recoverable.
Principle 5: Access without a human in the loop
Auth is where agent journeys die most often, and TTFSC includes credential acquisition. There's a maturity ladder here, and most APIs today are standing on the ground floor.
Short-lived keys
— credentials with TTLs measured in minutes to hours, not the immortal keys that end up in a repo somewhere.
Least-privilege scoping
below the account: per-resource, read vs. write vs. admin. An agent that requests broad scopes early and holds them forever is a standing blast radius.
Delegation-native flows
come next: OAuth 2.1 with PKCE for agents acting on behalf of a human, client credentials for autonomous service agents, RFC 8693 token exchange to narrow a broad credential to a task-scoped one. The Model Context Protocol's authorization spec is emerging as the common ground for how agent runtimes broker these flows.
The top rung is a
zero-signup sandbox
: claimable scratch resources, so a cold agent reaches its first successful call with no account at all, and a human claims the work afterward. Quotas and TTLs bound the abuse rather than a signup form — an abuse-economics trade, bounded spend for unbounded agent reach.
Through all of it, the human stays in the loop as an escalation, not a prerequisite: the agent operates freely within its scope, and privileged operations trigger approval.
Principle 6: The agent surface is a product, not a mirror
The reflexive move is one tool per endpoint, calling it an MCP server. We resisted it: a full mirror fails the agent twice. A large API can burn hundreds of thousands of tokens before the first call (
Cloudflare measured
over a million for its 2,500-endpoint surface), and endpoint granularity forces the agent to re-derive the API's workflows call by call.
The demand for curation is not hypothetical. In two of our three cold trials, the agent's very first action, before touching the API, was to search its harness for an installed tool for our product, only falling back to raw HTTP. Agents check for a front door before climbing through the window.
We curate instead.
Anthropic's guidance
is to build a few workflow-shaped tools rather than many endpoint-shaped ones, schedule_event rather than list_users plus list_events plus create_event.
Stainless
and
Speakeasy
converge on the same advice from the SDK side: expose capabilities instead of raw endpoints.
For large APIs, the spectrum runs further: dynamic meta-tools (list_endpoints / get_schema / invoke) let the agent discover operations on demand. At the far end sits
Cloudflare's Code Mode
, which exposes just search() and execute() over a typed SDK and lets the agent write code against an API, making those same 2,500 endpoints reachable for a fixed cost of about a thousand tokens. The common thread across the whole spectrum: someone has to design the agent surface. Generating it is how the mirror happens.
Two rules keep the curation honest.
Capability parity:
anything the SDK can do, the agent surface can do, or the gap is explicit and documented.
Zero-config defaults:
the path with the fewest decisions is the one every agent takes, so the default path is the good path. The long tail stays reachable through an escape hatch, a meta-tool, a code mode, or at minimum a documented pointer to the SDK, so no task dead-ends mid-flight.
Old wine in new bottles?
Every item here would look familiar to an API designer from a decade ago: actionable errors, bounded responses, self-description, idempotency, least privilege, honest docs. None of this is new; good API design always meant it, and the only reason the metrics looked fine is that human developers were quietly paying the cost themselves. Agents don't demand a new API discipline — they make the cost of ignoring the old one legible, billable, and churn-inducing. What's genuinely new is a shorter list: safety at machine tempo, delegation-native auth, the curated agent surface, and token cost as a design budget. The rest is the old religion, now with enforcement.
This is the experiment that started this post: point a cold agent at an API and count the turns to the first successful call. Not a demo agent with docs preloaded — a cold one. That number is the agent-experience baseline, and every principle above is a way to bring it down.
Nexus
and the
Pinecone agent skills
(npx skills add pinecone-io/skills) are both built this way: a chance to see what a purpose-built agent surface feels like from the agent's side of the conversation.
Further reading
Anthropic —
Writing effective tools for agents
Mathias Biilmann —
Introducing AX: Why Agent Experience Matters
·
agentexperience.ax
·
AXIS
Cloudflare —
Code Mode: give agents an entire API in 1,000 tokens
WorkOS —
Designing an MCP server from a REST API
Stainless —
From REST API to MCP server
· Speakeasy —
Designing MCP tools
RFC 9457: Problem Details for HTTP APIs
·
RFC 8693: OAuth 2.0 Token Exchange
Ahrefs —
We analyzed 137k sites: 97% of llms.txt files never get read
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
