---
title: "Why we Built our own Cloud Agent Infrastructure"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/why-we-built-our-own-cloud-agent-infrastructure"
scraped: "2026-06-02T06:00:08.397929+00:00"
lastmod: "2026-06-01T14:00:00.000Z"
type: "sitemap"
---

# Why we Built our own Cloud Agent Infrastructure

**Source**: [https://www.harvey.ai/blog/why-we-built-our-own-cloud-agent-infrastructure](https://www.harvey.ai/blog/why-we-built-our-own-cloud-agent-infrastructure)

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
Agents
→
Purpose built agents execute complex legal work end to end.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
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
Agents
Purpose built agents execute complex legal work end to end.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
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
Why we Built our own Cloud Agent Infrastructure
Solving for multi-model, zero data retention, and cost.
by
Gabe Pereyra
•
Jun 1, 2026
Over the past year, we've moved Harvey from a chat product to cloud agents — from answering a lawyer's question to completing a lawyer's task end to end, like reviewing a data room and producing a first-pass issues list across hundreds of thousands of documents. When we started, the infrastructure to run agents like that didn't exist, so we built our own.
Managed agent runtimes are now emerging from the frontier labs — Anthropic's Claude Managed Agents and OpenAI's — and from the cloud providers building on AWS, Microsoft's Foundry, and Google. They're impressive, and we work closely with all of them to shape where this goes. So it's worth being precise about why we still run our own: serving law firms and regulated enterprises imposes a handful of requirements that none of them meet yet, and won't for a while.
There are three main considerations:
being multi-model
, zero data retention, and controlling cost. None of them is unusual, and we expect each to be solved over time, especially by the cloud providers. But each is a hard blocker today — and the first one is worth dwelling on, because most people underestimate how universal it's about to become.
Law Firms Can't be Locked to a Single Model
The clearest reason is conflicts. A firm that represents one of the model providers is under real commercial pressure to run on that provider's model; the relationship suffers when a marquee client's own technology isn't the one its outside counsel uses. That alone makes a single-model platform awkward. But the sharper version is about confidentiality: a client that builds its own models will not allow its outside counsel to send sensitive legal matters through a competitor's model. And as more companies train their own models, and as the labs expand into more industries, the set of firms caught by this grows quickly.
Today it's easy to wave this away as a handful of firms with a handful of conflicted clients. It won't stay that way. Within a few years, a firm that wants to serve a broad client base will need to be able to run on essentially any model, because important clients will inevitably object to any given one. Multi-model isn't a feature for edge cases; it is becoming table stakes for representing technology companies at all.
Conflicts are a hard requirement but they’re not the only reason to be multi-model. Quality and cost optimization are increasingly critical. Different models are better at different things — our
legal agent benchmark
(LAB) shows clear separation by practice area and task type — and that spread is widening, not narrowing, as open-source models improve. The industry is shifting from "Which model is best?" to "Which model is most efficient for this specific task?" Answering it at all requires access to every model.
Then there is platform risk, which agents make far more acute than chat ever did. If you commit to a single provider's managed runtime and that provider's models fall behind, or it runs out of capacity, deprioritizes your vertical, changes its pricing, or drops a feature you depend on, you are stranded. And the lock-in is no longer just your model, it's your entire agent workforce. The agents your teams have built, tuned, and come to rely on live inside that provider's runtime, in its formats and against its orchestration. You can't pick them up and move them. For a firm betting its operations on agents, that is company-level risk, and it is the best reason to keep the runtime under your own control.
This is also where the two kinds of managed runtime diverge. A frontier lab's runtime ties you to that lab's models — maximum lock-in. The cloud providers' runtimes are model-flexible, which is the right shape, but they tend to lag the labs on the newest models and still run into redundancy and uptime limits. Neither is sufficient on its own, which is why we work with all of them and route across them.
Building that routing is the hard part. Every provider exposes a different agent harness — different tool-call formats, stop conditions, streaming behavior, and failure modes — and a different execution sandbox, and the same task tuned for one model will underperform on another. We built an abstraction layer that normalizes the harness, the sandbox, and the behavioral differences beneath a single interface, so that for everything above it, the choice of model is just a routing decision.
Zero Data Retention is a Requirement
Every law firm contract we sign, and every enterprise contract, requires zero data retention (ZDR). This is not a nice-to-have a buyer might trade away; it is a gate, because the data in question is privileged and confidential and cannot sit on a third party's servers. The frontier labs' managed runtimes don't offer ZDR, which means running a firm's matters through them would leave that firm's client data retained on the lab's infrastructure. For our customers, that is a complete nonstarter.
The important thing to understand about ZDR is that it can't be bolted on. There is a tempting shortcut — store data during the run and call a deletion endpoint afterward — but that isn't zero retention; it is retention followed by deletion, and for a firm's purposes the two are not the same. ZDR means designing the runtime so customer data is not written into durable application storage by default. Agent sandboxes still need a transient working disk while a task runs, but that disk is lifecycle-bound to the sandbox and automatically cleaned up as part of teardown. That is an architectural property of the runtime, not a setting you toggle at the end.
Agents make this harder than chat did, for a reason that runs through this whole post: agents are stateful. A long-running agent accumulates working memory, intermediate files, tool results, and the checkpoints it uses to recover from interruptions — and a managed runtime earns its keep precisely by persisting all of that for you, in its cloud. That persisted state is customer data at rest in someone else's environment. Automatic state persistence and zero retention are mutually exclusive; you cannot have both.
Because we own the runtime, the agent's entire lifecycle runs inside our security boundary. State is scoped to the session and purged, so the zero-retention guarantee covers the whole workflow rather than just the final model call.
Cost is Becoming the Main Constraint
Of the three considerations, cost may be the one that matters most, and it is the one growing fastest. Our usage is climbing steeply, and serving the most capable models as agents at scale is extraordinarily expensive. A single agent run can involve hundreds of model and tool calls over a large corpus, so the per-task cost of the naive approach — route everything to the best frontier model — is not sustainable. Increasingly, the firms we work with are asking us not just to make agents work, but to make them economical.
Figure: Harvey’s agentic usage growth.
The key insight is that for most tasks, you no longer need the largest model. As models have improved, a growing share of legal work has become intelligence-saturated: the task sits well within reach of a small or open-source model, and a top frontier model is simply overspending capability the task doesn't require. Our LAB benchmark bears this out — across many task types, open-source models match frontier quality at a fraction of the cost. The goal has shifted from finding the best model to finding the one that's good enough, cheapest, and fastest for the task at hand.
Figure: The mean criterion pass rate per LAB task across popular closed source and open source models. Rubrics were graded by GPT-5.4. Error bars show 95% bootstrap Cls.
Doing that at scale requires fine-grained control over both model routing and the execution sandbox, and this is where managed platforms fall short today — they don't expose enough of either to optimize aggressively. Owning the runtime lets us route each task to the most efficient model that meets the quality threshold, including open-source models we host ourselves, and lets us optimize the sandbox — how files are loaded, how work is parallelized, how compute is sized — around legal workloads specifically.
The combined effect can be large: empirically we see 3-5x cost reductions versus a frontier-only approach, depending on model and workload. That level of optimization is structurally unavailable to anyone building on top of someone else's runtime. It’s the difference that makes serving agents over a firm's full document set — hundreds of thousands or millions of files — economically viable rather than a line item that spirals out of control.
Building for the Future
We don't expect to run our own agent infrastructure forever in its current form. Many of these gaps will close over time and we think the cloud providers in particular will get there. They have strong incentives to support multi-model routing, zero retention, and open-source models, and we're working with them to make it happen. We built our runtime so that we can absorb those improvements as they arrive, not so that we can route around the ecosystem indefinitely. When a provider can do a piece of this better than we can, we want to use it.
Owning the runtime is also what makes the legal-specific layer possible at all, and why it’s important long term. Firms will need multi-cloud resilience and real data residency, including the ability to keep matters within a specific jurisdiction. Our largest and most regulated customers increasingly want sovereign deployments: the option to self-host their own cloud agent infrastructure through us, inside their own boundary. They need conflict-aware governance that encodes which models a given matter is even allowed to touch, and a complete, inspectable record of what every agent did, for work-product and privilege. None of that is something a general-purpose runtime will solve for the legal industry, and all of it is what makes owning this layer durable rather than temporary. There is more here too — security and isolation, and a longer list of regulated-industry requirements — but these are the ones that matter most.
We built our own cloud agent infrastructure for a simple reason: our clients needed agents in production now, and meeting their requirements for multi-model flexibility, zero data retention, and cost means owning the runtime they operate on. The firms that depend on us can't wait for the ecosystem to catch up, and the part of this that is specific to legal work was always going to be ours to get right.
Next Up
Building an Agentic Security Operations Center
How we Built Image Understanding for Legal Documents
How Harvey Secures Embeddings at Scale
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
