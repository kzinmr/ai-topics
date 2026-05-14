---
title: "The Context Layer AI Agents Actually Need"
created: 2025-12-24
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2003944353342149021"
x_article_author: "Kirk Marple"
x_article_author_handle: "@KirkMarple"
source: "https://x.com/KirkMarple/status/2003944353342149021"
tags: [x-article]
---

Foundation Capital's recent piece "Context Graphs: AI's Trillion-Dollar Opportunity" is the clearest articulation I've seen of where enterprise AI is heading. @JayaGup10 and @ashugarg argue that the next trillion-dollar platforms won't be built by adding AI to existing systems of record. They'll be built by capturing something enterprises have never systematically stored: the decision traces that show how rules were applied, where exceptions were granted, and why actions were allowed to happen.
They're right. But here's what their thesis implies that deserves more attention: you can't capture decision traces without first solving the operational context problem. Agents need to understand who owns what, how entities relate, what changed and when, and how information flows across systems—before they can meaningfully record why a decision was made.
That foundational layer is the substrate that makes context graphs possible. And it's largely missing from the current landscape.
The Context Graph Thesis
The argument starts with a critique of the current AI landscape. Systems of record like Salesforce, Workday, and SAP became trillion-dollar platforms by owning canonical data. The debate now is whether those systems survive the shift to agents.
Their answer: agents don't replace systems of record, but they do expose a missing layer. As they put it:
"Rules tell an agent what should happen in general. Decision traces capture what happened in this specific case—we used X definition, under policy v3.2, with a VP exception, based on precedent Z, and here's what we changed."
The insight is sharp. When a renewal agent proposes a 20% discount despite a 10% policy cap, it pulls context from multiple systems: incident history from PagerDuty, escalation threads from Zendesk, and precedent from a prior approval. Finance approves. The CRM records one fact: "20% discount."
Everything that made that decision legible—the inputs, the policy evaluation, the exception route, the approval chain—disappears. The reasoning that connected data to action was never treated as data in the first place.
They call the accumulated structure of those traces a context graph: "a living record of decision traces stitched across entities and time so precedent becomes searchable."
This is where the piece goes further than most analysis. The context graph isn't just better governance or semantic contracts. It's a new category of system of record—one that captures decisions, not just objects.
Two Layers of Context Agents Need
Here's where I want to add to the conversation. Building a context graph requires two distinct layers of context, and most enterprises have neither.
Operational Context: The Foundation
Before you can capture why a decision was made, agents need to understand the organizational reality in which the decision occurs:
Identity resolution. Who is Sarah Chen? Is she the same Sarah from the email thread, the Slack mention, and the meeting transcript? Agents can't reason about people, accounts, or systems if the same entity appears as fragmented text across tools.
Ownership and relationships. Who owns the Acme account? Which engineer is responsible for the payments service? How does the support escalation connect to the product team's roadmap? These relationships exist in people's heads and scattered across systems—but they're rarely modeled as queryable data.
Temporal state. What did the contract say when the decision was made? What was the customer's ARR at renewal time? Agents need to understand how things evolve, not just their current state.
Cross-system synthesis. The support lead checks customer tier in the CRM, sees open escalations in Zendesk, reads a Slack thread flagging churn risk, and decides to escalate. That synthesis happens in their head. No system captures it.
This is operational context: the identity, ownership, relationships, and temporal understanding that let agents reason about an organization as humans do.
Decision Context: The Next Level
Once operational context exists, you can build the decision layer the authors describe:
Decision traces. What inputs were gathered? What policy was evaluated? What exception was invoked? Who approved?
Precedent as artifact. When a similar case arises, agents can query: "How did we handle this before? What was the outcome?"
Auditability. Not just what happened, but why it was allowed to happen—with the full context preserved.
The relationship between these layers matters. You can't capture meaningful decision traces if agents don't know who the actors are, how entities relate, or what state the world was in when the decision occurred. Operational context is the foundation. Decision context is what you build on top.
Most enterprises lack both.
Why RAG and AI Memory Fall Short
The market has responded to the context problem with two approaches: RAG (retrieval-augmented generation) and "AI memory" platforms. Neither solves the operational context problem.
RAG retrieves text chunks, not organizational understanding. When you ask "What did Sarah say about the API integration?", RAG finds documents containing those keywords. It doesn't understand that Sarah is a person with a complete interaction history, that the API integration is a project connected to three teams, or that the conversation evolved across Slack, email, and a meeting transcript. RAG stores similarity, not meaning.
Most AI memory platforms store chat transcripts, not organizational reality. They capture what was said in conversations with the AI, but they don't model the entities, relationships, and temporal state that make an organization legible. A memory of "user discussed Acme pricing" is not the same as understanding Acme as an account with a relationship history, stakeholder map, and decision trail.
The gap is structural. These approaches treat organizational knowledge as documents to embed or conversations to remember. But organizational knowledge is a graph: people connected to accounts, accounts connected to projects, projects connected to decisions, decisions connected to outcomes—all evolving over time.
Without that graph, agents are context-blind. They can retrieve relevant text, but they can't understand who owns what, how decisions evolved, or which precedents actually govern reality.
What the Operational Context Layer Looks Like
So what would it actually take to build this foundational layer? The infrastructure that transforms an organization's scattered, multimodal work into an identity-resolved, time-aware knowledge graph?
The Core Capabilities
Identity-resolved entities. People, organizations, places, and events modeled as canonical entities—ideally aligned with standards like Schema.org. Sarah Chen isn't fragmented text appearing differently in each tool. She's a resolved entity connected to every conversation, document, and decision she's been part of.
Multimodal ingestion. Slack, email, meeting recordings, documents, code, CRM data, project management tools—content from across the enterprise, with structure preserved, not just text extracted.
Temporal modeling. Not just current state, but how entities and content evolve over time. Agents need to reason about what changed, when, and in what sequence.
Relationship mapping. Entities connect to each other. People belong to organizations. Content relates to projects. Decisions involve stakeholders. The graph captures these relationships as first-class data.
Agent interoperability. The context layer needs to be accessible to any agent through standard protocols—not locked into a single vendor's ecosystem.
Enterprise deployment options. For organizations with data governance requirements, the context layer needs to run in their own infrastructure, meeting compliance where it needs to.
What We're Building at Graphlit
This is the problem we've been working on since 2021. Graphlit provides the operational context layer for AI agents—the infrastructure that ingests multimodal content and transforms it into an identity-resolved, time-aware knowledge graph.
We built it like a modern media and sensor-data system, not a document store. We preserve structure, provenance, and time rather than flattening everything into text blobs for embedding. That architectural choice is what makes operational context possible—and it's what positions us to support decision context as the market evolves.
From Operational Context to Decision Graphs
The Foundation Capital thesis points to where the market is going. We're aligned with that direction, and our 2026 roadmap takes us further into the territory they describe.
Where We Are Today
Graphlit provides the operational context layer: identity resolution, entity extraction, relationship mapping, temporal modeling, and multimodal ingestion across 30+ sources. Agents that connect to Graphlit understand who owns what, how things relate, and what changed—the foundation for any meaningful decision capture.
Where We're Going
CRM as the entity spine. Our work with customers using Attio clarified something important: CRM objects (accounts, contacts, deals) provide the cleanest structured backbone for organizing multimodal content. Once canonical entities exist, everything else—Slack, email, documents, code—resolves cleanly into the graph. We're deepening CRM integration as the architectural wedge into enterprise context.
Agent memory and decision logging. As agents execute workflows through Graphlit, we're building the infrastructure to capture not just the content they access, but the reasoning traces they produce. What inputs were gathered? What context was synthesized? What action was taken?
Workflow instrumentation. The authors are right that capturing decision traces requires being in the execution path. Our MCP server already sits in the context-retrieval path for agents. Extending that to capture decision outputs—approvals, exceptions, precedents—is the natural next step.
Decision Traces Need a Standard
There's a parallel worth drawing here. The LLM observability space - LangSmith, AgentOps, Arize, Braintrust - has matured around capturing execution traces: inputs, outputs, latency, tool calls, token usage. That's valuable for debugging and optimization, but it's not what the Foundation Capital piece is describing.
Decision traces operate at a higher level of abstraction. Not "the agent called this tool with these parameters" but "this decision was made under this policy, with this exception, approved by this person, based on this precedent." It's business-level semantics layered on top of execution telemetry.
If decision traces become the foundation for a new category of system of record, the schema can't be proprietary to each orchestration platform. We'll need industry standards - the way OpenTelemetry standardized observability, or Schema.org standardized entity markup. Otherwise every platform captures decisions differently, and cross-system precedent queries become impossible.
This is an area where Graphlit's architectural choices matter. We already model entities using Schema.org and JSON-LD - canonical representations for people, organizations, places, and events. Extending that to decision traces (policy version, exception type, approver, precedent references) is a natural evolution. And because we're building on open standards rather than proprietary schemas, we're positioned to support whatever decision trace format the industry converges on.
The Honest Framing
We're not claiming to be the full "system of record for decisions" today. That requires being in the orchestration layer where decisions are committed, not just the context layer where information is retrieved.
But we're building the substrate that makes decision graphs possible. You can't capture meaningful decision traces without identity resolution, relationship modeling, and temporal state. That's what operational context provides. And as we extend into agent memory, decision logging, and workflow instrumentation, the pieces converge toward the vision they describe.
Why This Matters Now
Three shifts converged to make this the right moment:
ChatGPT created demand for enterprise context. Every organization wants AI that understands their business, not generic models trained on the public web. That demand is real, and it's not going away.
MCP standardized agent interoperability. The Model Context Protocol gives us a standard way to expose context to any agent. Build the context layer once, and it works with Cursor, Claude, custom agents, and whatever comes next.
Every company is experimenting with agents—without the context layer to make them work. This is the gap the piece identifies: agents are hitting walls that governance alone can't solve. They need operational context to reason correctly, and they need decision context to learn from precedent.
Someone has to build the context infrastructure. That's what we're focused on.
Getting Started
The context graph vision is compelling—and achievable. It starts with operational context: identity, ownership, relationships, and temporal understanding across your organization's multimodal knowledge.
We've been building this infrastructure for over three years. If you're deploying agents that need to understand your organization—not just retrieve documents—the context layer is where to start.
Learn more at graphlit.com.
Foundation Capital's full piece is worth reading: "Context Graphs: AI's Trillion-Dollar Opportunity". Jaya Gupta and Ashu Garg articulate the market dynamics clearly, and their framing of decision traces as a new category of system of record is the right way to think about where enterprise AI is heading.
