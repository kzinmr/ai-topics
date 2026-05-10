---
title: "Building Spectre: Internal Collaborative Cloud Agent Platform"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/building-spectre-internal-collaborative-cloud-agent-platform"
scraped: "2026-05-10T01:27:03.460192+00:00"
lastmod: "2026-04-07T17:00:00.000Z"
type: "sitemap"
---

# Building Spectre: Internal Collaborative Cloud Agent Platform

**Source**: [https://www.harvey.ai/blog/building-spectre-internal-collaborative-cloud-agent-platform](https://www.harvey.ai/blog/building-spectre-internal-collaborative-cloud-agent-platform)

Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
About
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Assistant
→
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
→
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
→
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
In-House
→
Streamline work and shift focus to strategy and speed.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
Collaboration
→
Work with legal teams across organizations in secure, shared spaces.
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
→
Resources for maintaining a uniform and professional presentation of the Harvey brand.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
→
About Harvey, our leadership, and career opportunities.
Newsroom
→
Press releases and partnership announcements.
2025 Year in Review
→
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Login
Request a Demo
Platform
Overview
A unified view of how Harvey's products work together to support your entire practice.
Assistant
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
In-House
Streamline work and shift focus to strategy and speed.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
Collaboration
Work with legal teams across organizations in secure, shared spaces.
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
Resources for maintaining a uniform and professional presentation of the Harvey brand.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
Company
About Harvey, our leadership, and career opportunities.
Newsroom
Press releases and partnership announcements.
2025 Year in Review
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Request a Demo
Login
US
EU
AU
Technical
Building Spectre
Harvey’s internal collaborative cloud agent platform.
by
Joey Wang
and
Gabe Pereyra
•
Apr 7, 2026
Spectre is Harvey’s internal collaborative cloud agent platform. A request can start in Slack, the web app, or an automation; Spectre turns that request into a durable run, executes it inside an isolated sandbox, connects it to systems like GitHub, Datadog, and Linear through explicit boundaries, and returns reviewable artifacts such as summaries, diffs, branches, and pull requests. Spectre is not just a background agent runtime. It is a new collaborative surface for building software in the open inside Harvey.
We built Spectre because local coding agents, while already indispensable, break down at the organizational boundary. They are tied to one laptop, one working directory, one set of credentials, and one engineer’s private context. That makes them hard to share, hard to secure, and hard to integrate deeply with the systems where engineering work actually happens. Existing tools were improving quickly, and many teams were converging on the same direction:
take the increasingly capable local loop and move it into the cloud
, then
connect it to the systems where engineering work already happens
. But they still did not give us the combination of isolation, durable history, resumability, explicit permissions, shared review surfaces, and company-context integration that we needed.
That shift changes what an agent system is useful for. Spectre lets engineers investigate incidents in public threads, hand off work without re-explaining context, and wake up to reviewable pull requests and recurring maintenance runs. It also expands who can participate: engineers, product managers, and designers can all collaborate around the same runs and artifacts instead of routing everything through one person’s terminal. This post is about how we built that system, why the architecture looks the way it does, and what building it is teaching us about the infrastructure and organizational transformation that other knowledge industries, including legal,
will need next
.
The First Version
Take the local coding-agent loop that was already powerful, point it at a repository in a remote sandbox, and get the result back somewhere actionable. In practice, that meant: create a run, start a fresh sandbox, hydrate the repository, run the agent, stream the output, and persist the artifacts. Success meant a branch, a PR, a summary, and enough history to see what happened. Failure meant a human got the result back in a place where they could decide what to do next.
Spectre’s run view. The run page is the durable record of work: repository context, file tree, diff, structured summary, and completion state all hang off the same run rather than a single terminal session.
That version was useful quickly because it changed the ergonomics of coding agents in a way that felt qualitatively different from IDE assistance. You could kick off real work and walk away, run several things at once, ask the agent to investigate instead of only implement, and hand the run to another engineer without turning your terminal into the source of truth. Just as importantly, the work stopped being trapped in one person’s local session. The run, its context, and its artifacts became shareable, which made it much easier for engineers and non-engineers alike to collaborate around the same piece of work.
It also made the next layer of the problem obvious. To make Spectre effective for a team of engineers working together, we needed a remote coding agent that was not just a model in a container. Once it is operating on behalf of a team, you need a durable run rather than a fragile process, an execution boundary rather than an ambient desktop, a harness that can coordinate providers and tools, and shared surfaces where the work can be streamed, reviewed, resumed, and scheduled.
The Core Technical Primitives
Durable runs, ephemeral workers
The most important design choice is that the durable object is the run record, not the worker process. Users collaborate around one stable record that carries ownership, sharing, attachments, execution history, artifacts, and provider session references. Spectre workers are short-lived. They exist to execute one slice of work and then terminate.
This simplifies failure recovery because the system never has to preserve a live process as the primary state holder. It makes follow-ups tractable because a new worker can resume from an archived session state rather than trying to reanimate an old sandbox. It also keeps the product model stable across surfaces. Slack, web, CLI, and scheduled work all point at the same durable run instead of inventing their own session semantics. In practice, a follow-up does not wake up an old container. The control plane appends new interaction state to the durable run, starts a fresh worker, restores the relevant provider session context, and continues.
Sandboxes as the execution boundary
The sandbox defines the execution boundary. Spectre workers are isolated environments that are allowed to see a repository workspace, a configured set of tools, and a constrained set of credentials. They are not allowed to mutate the core system state directly. That means the worker receives its configuration on initialization, can stream events and call approved external systems, but it does not get ambient access to the control plane.
This boundary matters for both security and correctness. Once the agent can run commands, read and write files, push branches, query telemetry, or call MCP-connected tools, the blast radius of mistakes becomes real. The cleanest answer is to make the worker powerful inside its sandbox and strictly define the boundary. Repository access is short-lived and scoped. Tool configuration is injected at run start. Temporary skills live only for the duration of the run. Durable state changes go back through the control plane instead of happening implicitly inside the worker. This is also why the system uses ephemeral workers rather than keeping long-lived environments warm by default. Disposable sandboxes are much easier to reason about than a fleet of mutated, half-reused environments with sticky states.
A harness, not just a wrapper
The harness is the component that turns "a model that can use tools" into
a system that can do work
. In Spectre, it assembles the working context of a run, starts the right provider adapter, translates provider-native events into a stable internal shape, decides how progress is represented, and determines how and when the run changes state inside
a larger agent loop with clear tools, state, and stop conditions
.
This is where many of the most important product decisions live. Runs need an explicit notion of progress, not just a text stream. They need clear terminal states, per-run accounting for cost and usage, attachment handling, execution timeouts, post-processing rules for commits and PRs, and a way to carry context forward across follow-ups without making the whole system provider-specific.
This is also why the harness should be thought of as a real system component rather than a thin SDK wrapper. A useful shorthand is
models using tools in a loop
plus
the surrounding work of context engineering
, but the practical work is turning that loop into something durable, observable, and safe inside a real company. A thin wrapper is fine until you need durability, shared visibility, retry semantics, cost accounting, multi-provider support, and collaboration surfaces. At that point the harness becomes the product.
Collaboration surfaces are part of the runtime
One of the biggest changes from local agents to background agents is that the prompt box stops being the primary interface. Slack mattered for Spectre not because it was a nice notification surface, but because it was already where a large amount of the relevant engineering context lived. The thread often contains the initial diagnosis, the links to telemetry, the open questions, and the first round of clarification. Starting the run there preserves the actual context instead of asking a human to compress it into a brand-new prompt.
The important technical point is that the Slack invocation, the web run page, the resulting PR, and any follow-up interaction all refer back to the same durable run. The surfaces differ. The object underneath them does not. That keeps collaboration anchored to one artifact and avoids the common failure mode where every client ends up with its own semi-private session. It also enables hybrid workflows. Some runs should go from prompt to PR. Others should be used for investigation, planning, or triage and then handed back to a human in a local environment.
Human-agent collaboration in the same thread. Spectre can be invoked from Slack, run against a repository in the background, and return concrete findings back into the conversation where the work started.
Scheduled Runs
The final primitive that mattered more than expected was scheduled work. Once the runtime exists, it is natural to ask it to do work that is not triggered by a human in the moment. Cleanup passes, test generation, branch management, dependency checks, and verification loops are all better represented as scheduled runs than as manual prompts. In practice, Spectre uses cron-based automations to materialize those runs.
The key architectural choice here is not the scheduler itself. It is that scheduled work uses the same runtime as interactive work. The scheduler should materialize ordinary runs with ordinary visibility, ordinary history, and ordinary artifacts, rather than creating a parallel background-job world. That keeps the system understandable and prevents automation from becoming a second-class subsystem that nobody can inspect with the same tools.
Automations as first-class runs. Scheduled work uses the same runtime as interactive work, so recurring checks, cleanup passes, and verification loops are visible, reviewable, and resumable in the same system.
Security Requires Explicit Boundaries
The same runtime properties that make Spectre collaborative also make its security model much more important. Once an agent can run commands, read and write files, inspect telemetry, push branches, or call internal tools, security is no longer something added in review after the fact. It becomes part of the runtime design itself. The key questions move into the harness: what the agent can see, what it can call, what identity it acts under, what state it can mutate directly, and what must cross an explicit approval or API boundary.
One of the clearest lessons from building Spectre is that desktop-first agent products hit a hard wall in enterprise settings because their boundaries are implicit. They feel powerful because they inherit an engineer’s whole machine: browser sessions, SSH agents, local clones, downloaded documents, terminal history, notes, and everything else in reach. That convenience is also the problem. Once a desktop agent is doing real work on behalf of a company, it becomes difficult to answer basic security questions precisely: what exactly could this run access, which credentials did it use, what unrelated data sat next to it, and how would we reproduce the same boundary tomorrow. Desktops mix customers, credentials, files, side-channel context, and personal workflow in ways that are hard to observe and nearly impossible to standardize.
The cleanest decision we made was to make the worker powerful inside the sandbox and strictly defined at the boundary. Workers can operate on a repository workspace, stream output, and use approved tools, but they do not get direct access to the control plane’s database. Repository access is scoped and short-lived. Tool access is injected at run start rather than inherited ambiently from one engineer’s machine. Temporary runtime capabilities exist only for the duration of the run and are cleaned up afterward. That keeps runtime state, repository state, and system state from collapsing into one another, and it makes the exposed surface explicit: one repository, one tool bundle, one set of short-lived credentials, one artifact path, one audit trail. For enterprises and regulated environments, that is why the center of gravity keeps moving from desktops toward cloud runtimes: not because local agents stop being useful, but because useful agents eventually require reproducible permissions, constrained egress, durable audit, deliberate separation between runs, and clear attribution of who initiated, approved, and executed the work.
What Spectre Taught Us About Harvey
Those security and boundary constraints point to a broader lesson: once agent work matters, the problem is no longer just remote execution. It is how the company itself becomes legible to agents in a way that is shared, inspectable, and enforceable. That was one of the biggest reasons to build Spectre ourselves. A local setup can be powerful, but it fragments quickly: each engineer has different credentials, tools, prompt patterns, and pockets of context living on one machine. A shared runtime lets us standardize the important parts instead: repositories, tools, permissions, artifacts, review surfaces, and execution history. That makes agent work something the organization can understand, improve, and coordinate as a system, rather than something each person assembles privately on their laptop.
That matters because one of the central engineering challenges ahead is coordinating large amounts of human and agent work without losing context, ownership, or coherence. Spectre is a concrete way to start solving that problem. The durable run becomes a common object around which people and agents can collaborate: it can start in Slack, attach to a repository, pull in telemetry, produce artifacts, and then be inspected, resumed, redirected, or approved by someone else. Just as importantly, that collaboration extends beyond engineering. Designers, product managers, and other teammates can participate much earlier and much more concretely because the work is visible and shareable. They can prototype ideas, inspect outputs, and contribute useful context without needing to be the person driving a private terminal session. That makes the whole company better at building software because more of the relevant context shows up inside the work itself.
The other reason Spectre mattered was what it taught us about Harvey’s core product. The translation is not literal, but the analogies are strong: repositories and pull requests become matters and review workflows; diffs and execution history become document versions, provenance, and approval trails; sandbox boundaries and scoped credentials become ethical walls, client isolation, and controlled access to legal work. Law firms and in-house teams are going to have to go through a similar transition as agents become real operating components in their workflows. By working through the security model, collaboration model, and runtime architecture ourselves, we are getting a much clearer picture of the infrastructure they will need next. Spectre has already influenced how we think about product and technical design for legal, and it is changing how we prototype and build together inside Harvey.
Acknowledgements
We owe a lot to the DevEx team, especially Zhiyu Chen, Po-Lin Yeh, Shubhang Chaudhary, and Bob Chen; to the Security team, especially Chad Scott, Nick Gonella, and Michael Roberts; and to Philip Cerles, Philip Lan, Sarah Varghese, Doron Roberts-Kedes, and Steve Mardenfeld, who have been building the parallel pieces of this architecture inside Harvey's core product and customer-facing cloud agent platform. We also owe a lot to the many EPD teammates who have been dogfooding Spectre, filing bugs, suggesting features, and contributing ideas and code as the system has evolved.
Next Up
How we Built Image Understanding for Legal Documents
How Harvey Secures Embeddings at Scale
Rebuilding the Review Algorithm to Increase Accuracy and Speed
Unlock Professional Class AI for Your Firm
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Assistant
→
Vault
→
Knowledge
→
Workflow Agents
→
Ecosystem
→
Partnerships
→
Solutions
Innovation
→
In-House
→
Transactional
→
Litigation
→
Mid-Sized Firms
→
Collaboration
→
About
Customers
→
Security
→
Company
→
Newsroom
→
Careers
→
Law Schools
→
Resources
Blog
→
Resources Hub
→
Harvey Academy
→
Help Center
→
Legal
→
Privacy Policy
→
Press Kit
→
Your Privacy Choices
→
Follow
X
→
LinkedIn
→
YouTube
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
