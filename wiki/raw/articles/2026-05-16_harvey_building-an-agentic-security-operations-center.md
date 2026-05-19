---
title: "Building an Agentic Security Operations Center"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/building-an-agentic-security-operations-center"
scraped: "2026-05-16T06:00:21.325291+00:00"
lastmod: "2026-05-14T17:00:00.000Z"
type: "sitemap"
---

# Building an Agentic Security Operations Center

**Source**: [https://www.harvey.ai/blog/building-an-agentic-security-operations-center](https://www.harvey.ai/blog/building-an-agentic-security-operations-center)

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
Building an Agentic Security Operations Center
A persistent, agent-native SOC built around a world model of Harvey's threat surface, gated by human review, and running around the clock.
by
Mike Parowski
•
May 14, 2026
Harvey customers trust us with their most sensitive work: confidential M&A transactions, privileged client communications, ongoing litigation strategy, regulatory filings. Our Security team’s job is to protect that information every day against an attacker population that is getting faster, cheaper, and more automated.
Chad and Suha recently explained how we
protect customer data
by building a platform that is
secure by design
, and stays secure as the AI ecosystem evolves. Joey and Gabe also shared how
Spectre
, Harvey's internal collaborative cloud agent platform, makes the company itself legible to agents in a way that is shared, inspectable, and enforceable. This post sits at the intersection of those two ideas.
Our
agentic security operations center (SOC)
is a system of always-on AI agents that hunt, triage, investigate, author detections, triage alerts, and learn from one another. It’s built on top of an evolving, machine-readable model of Harvey's threat surface, and gated by human review on every production change. Secure by design, at agent-native speed.
Below, I walk through what we built, why it works, and how modern security teams can similarly augment their proactive defenses.
A World Model for Security
The artifact at the center of everything we do is what we've come to think of as a
security world model:
a persistent, machine-readable representation of Harvey's threat surface, the live telemetry flowing across it, and the accumulated interpretation of both. Jack Dorsey’s “
From Hierarchy to Intelligence
” similarly articulates the usefulness of this abstraction.
Security teams have long approximated security world models. These traditionally took the form of buying a vendor solution called Security Information and Event Management (SIEM), configuring data source ingestions, and manually writing queries atop those sources. Doing it right meant employing a sizable team of security-minded data engineers to sift through terabytes or petabytes per day, maintaining indefinitely-growing allowlists, and battling with domain-specific query languages to adequately model bad actors in the data. The process was slow, costly, riddled with unhelpful noise, and had little chance of surfacing real threats. For these reasons, proactive detection and response has historically been an underinvested layer of the security stack.
We’ve taken a more modern approach. Weaving agentic systems, human-in-the-loop domain expertise, and a state of the art security analytics corpus culminates in a living, breathing world model capable of true proactive observability that was previously unattainable.
Our model is comprised of:
The
security analytics corpus
itself: a continuous, high-volume (TBs/day) append-only stream of telemetry we ingest from Harvey's product, our infrastructure, and the long tail of SaaS and developer tooling any modern company runs on. This is the ground truth the agents reason over, served through optimized
ClickHouse
tables. Everything else in the model is interpretation laid over it.
A simple but powerful
MCP server
, built and maintained by
RunReveal
, granting agents legible tools to access and understand the corpus.
A
threat model system prompt
structured as paths to crown jewels: concrete chains of access an attacker would traverse to reach customer data. Every detection, hunt, and investigation anchors to one or more of those paths, and severity becomes a function of which path a finding sits on rather than how scary it sounds in isolation.
A
self-improving intelligence layer
consisting of a fleet of agents hunting through the data, deploying detections, kicking off investigations, and persisting memories of all such work. With every agentic loop, our SOC gets better and customers’ data gets safer.
The world model consists of
petabytes of historic data
, roughly
5,300 persistent memories across different categories
,
2,500+ investigations from the last 30 days
, and the deployment state of
400+ production detections
. One or two years ago, such numbers would indicate noise and illegibility. Today, they signal a comprehensive suite of high-fidelity detections and analytics queries tailored to Harvey’s custom threat model, which cares foremost about protecting our customers’ data.
Every agent loop accesses historic and current data, reads from its centralized memory, iterates on past work, and writes any new findings and context back to the model. We use this model to serve three primary functions every day: research and detect threats in real time, audit the ecosystem continuously, and inform future policy.
It Starts With the Data Layer
The SOC’s foundation lies in its underlying data corpus. Harvey is a complex application built within a tightly controlled ecosystem consisting of many disparate subsystems. The security analytics corpus is the raw representation of
who
is executing
which actions
and
when.
Think: customer data storage, user actions, varying degrees of employee access, internal communication channels, project management, sales data, and much more.
Operationalizing the corpus means enabling the agents to efficiently sift through billions of daily events and develop actionable insights. They must read live data, compare it to historic behavioral patterns, correlate across actors and log sources, and understand the external threat landscape as it relates to Harvey’s high stakes threat model.
None of this works at 20 queries per minute. The agentic SOC is fundamentally an exercise in spending compute to ask the data better questions, faster. The speed and shape of the data layer is the ceiling on how deeply any agent can think before it runs out of context.
We invested early and heavily in the substrate. Our log data lives in optimized ClickHouse tables that are semantically-enriched, column-pruned, indexed against the access patterns the agents actually use, and surfaced through a small set of curated views with normalized fields. For instance, deriving custom columns from raw data translates the verbose, token-expensive
JSONExtractString(rawLog, ‘data.resoures[1].subscription.value == ‘long-subscription-identifier’
to a simple
isProdCluster
.
A typical agent investigation issues dozens of queries;
the difference between 200ms and 2s per query is the difference between an agent that explores three hypotheses and one that explores 30
. The faster the agent can iterate, the more thoroughly it can chase a lead before its context budget runs out, and the sharper the world model gets with every loop. In practice, this data engineering effort compresses what might be a 200-line SQL query into a short, interpretable stanza. One such query, identifying anomalous secret modification in production, might look like:
Query identifying anomalous secret modification in production.
This is the part of our architecture that doesn't show up in a diagram, and that we feel can’t be emphasized enough:
invest in your log warehouse before you invest in your agents.
Semantically rich, fast, well-typed data multiplies every downstream loop. Schemaless dumps in object storage do not. The ceiling on what an agent can do is the ceiling its data layer imposes.
Eyes Always On: Round-the-Clock Operating Model
What the data layer enables, the agents continuously put to work. Persistent background workflows run on a schedule throughout the day:
Daily reports
scoring alert volume, detection performance, ingest anomalies, and surfacing leads worth deeper investigation.
Hourly alert triage
, semantically grouping the alert queue and auto-escalating the top critical clusters into deep-dive investigations.
A
threat-watch
workflow every morning, ingesting CISA KEV and other public threat intelligence sources, and cross-referencing them against our deployed detection coverage, authoring data-tested detections to fill in gaps where relevant.
None of these elements run in isolation. Each one reads from the world model and writes back to it. Yesterday's findings inform today's investigations. A learned baseline stays learned. A noisy detection stays flagged. A user behavior the analyst marked benign two weeks ago doesn't get re-flagged on a fresh run. The system gets sharper every day, in the literal sense that the next agent run starts from a more useful representation of the world than the last one did.
This is the difference between an SOC that is "always on" because someone is on call, and an SOC that is always on because the analysis itself never stops.
From Threat to Detection to Tuned Alert
The SOC autonomously operates through a continuous cycle of threat research, detection engineering, and alert tuning. Each stage informs the next to maintain a proactive security posture. Combining pre-defined workflow steps with autonomous agentic actions in this way loosely follows Anthropic’s learnings in “
Building Effective Agents
.”
Threat Research and Detection Engineering:
External intelligence is cross-referenced with internal context to identify coverage gaps. Our system then deploys a four-phase agent pipeline consisting of research, consolidate, validate, and finalize stages to produce well-documented detection proposals as pull requests for human review.
Four-phase pipeline with shared orchestration interface allows agents to develop high fidelity detections on live data.
Continuous Alert Tuning:
Hourly clustering workflows semantically group alerts to distinguish true positives from noise. This allows for automated tuning and deep-dive investigations, ensuring the SOC remains efficient as coverage expands. Each run produces a data-validated set of tuning rules, and posts them to GitHub for human review. What used to take a fleet of SOC analysts is now managed by a small team of domain experts.
Automated detection tuning creates a record of progress via Pull Requests.
Since implementation, we have expanded coverage from 75 to 400+ deployed detections while decreasing the weekly alert average from ~300,000 to ~20,000.
That’s a 5.7x increase in coverage while shrinking alert space by ~95%
. We use active triage, silent tripwires, and informational signals to ensure high-fidelity attention on critical events.
The shape of the partnership is the most important thing we've gotten right. Agents are extraordinary at the parts of detection work that are tedious like consolidation, deduplication, validation, documentation, and continuous tuning; they are merely competent at the parts that demand judgment. Putting humans on judgment and agents on tedium is a strict productivity win, and it produces a paper trail that traditional SOCs can't match.
Persistent Memory and Self-Evolution
The connective tissue across all of this is the agent's persistent memory backed by a Postgres knowledge base categorized facts (entity, finding, baseline, etc.) with TTLs, deduplication via prefix and Jaccard similarity, and per-profile injection budgets that determine which memories are loaded for which workflow.
Every agent loop reads from memory at the start and writes back to it at the end. The
daily report agent
inherits the fact that detection X is currently noisy, that user Y's home-to-office IP pattern is benign, that GitHub PAT Z is awaiting rotation. The
clustering agent
has access to prior clusters, recent detection deploys, and learned baselines. The
threat-watch agent
remembers which TTPs we already cover. None of these agents start from zero.
Human analysts close the loop with annotations: any artifact (a cluster, an investigation step, a workspace finding) can be tagged with a note that optionally persists as an agent memory marked
source='analyst'
. The agent reads that on its next run. Domain knowledge from human reviewers compounds into the world model rather than evaporating into Slack threads.
The implicit consequence is self-evolution. The system as a whole gets sharper over time without any single component being told to. The detection-engineering pipeline improves because
validation agents
remember which patterns have generated false positives historically. The clustering pipeline improves because it remembers prior verdicts. The threat-watch agent improves because it remembers what we already cover. Each loop's output is the next loop's input. The world model is the substrate that makes that compounding possible; the longer it runs, the more it knows.
Immediate Auditability
Like any sufficiently advanced tool, today’s AI systems augment both good and bad actors’ workflows alike. Just in the last month or so, several high profile vulnerability disclosures came to light in the public forum. For example:
CVE-2026-31431
: Linux kernel local privilege escalation
Axios npm supply chain
compromise
Trivvy / LiteLLM supply chain
compromise
For traditional SOCs, each release triggers an all-hands-on-deck effort to manually dig through data to verify whether their product’s been exploited. Our agentic workflows enable a one-button push investigation that interprets the disclosure, maps it onto our security world model, and provides an auditable narrative to inform our response, shortening investigations from hours or days to minutes. For example, we kicked off the following in response to Wiz’s
report
on the attack against LiteLLM:
Bespoke canvas enabling branched prompts for complex investigations.
Two Systems, One Discipline
A reasonable question, given the architectural overlap with Spectre: why two agentic platforms? The short answer is that Spectre operates
inside
Harvey's trust boundary, and the SOC operates
on
it. Product agents and security agents have fundamentally different optimization targets: speed of customer work versus adversarial robustness. Forcing both onto one substrate creates exactly the privilege-escalation path the SOC exists to prevent. The SOC's knowledge of detections, internal topology, and ongoing investigations is precisely the knowledge an attacker who compromised a product agent would want; sharing that memory is sharing blast radius.
The bet is straightforward. Agent capability will continue to improve exponentially. Our product surface and featureset will grow accordingly. If today’s data is indicative of tomorrow’s, the threat surface will
grow faster than either
. Attacker iteration isn't bound by review queues, change windows, or human approval. The companies that scale safely will be the ones whose security posture is itself agentic, persistent, and legible. Those whose security team has a system capable of meeting the new threat regime, not just a runbook describing what they'd do if they did.
Our promise to customers is the same one
Suha
and
Chad
previously articulated: We treat security at Harvey as a first-class engineering problem. We assume our adversaries are sophisticated and build accordingly. The agentic SOC is just one way we keep that promise as Harvey's product surface, customer base, and threat ecosystem all scale faster than any traditional security organization could match.
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
