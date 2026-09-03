---
title: "Rebuilding Playbook Review as a Multi-Agent System"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/rebuilding-playbook-review-as-a-multi-agent-system"
scraped: "2026-09-03T06:00:53.924354+00:00"
lastmod: "2026-09-02T14:00:00.000Z"
type: "sitemap"
---

# Rebuilding Playbook Review as a Multi-Agent System

**Source**: [https://www.harvey.ai/blog/rebuilding-playbook-review-as-a-multi-agent-system](https://www.harvey.ai/blog/rebuilding-playbook-review-as-a-multi-agent-system)

Introducing Harvey II:
Harvey's agents inherit project and matter context, and memory of how you work.
Learn more
Introducing Harvey II:
Harvey's agents inherit project and matter context, and memory of how you work.
Learn more
Introducing Harvey II:
Harvey's agents inherit project and matter context, and memory of how you work.
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
Company
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Agents
→
Purpose built agents execute complex legal work end to end.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Spaces
→
Work with legal teams across organizations in secure, shared spaces.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
→
Your preferences carried across Harvey so every response comes back consistent with how you work.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
→
Streamline work and shift focus to strategy and speed.
Law Firms
→
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
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
Research
→
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
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
Agents
Purpose built agents execute complex legal work end to end.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
Your preferences carried across Harvey so every response comes back consistent with how you work.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
Streamline work and shift focus to strategy and speed.
Law Firms
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
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
Research
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
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
How We Rebuilt Playbook Review as a Multi-Agent System
Why we made the shift, how we measure quality in a domain where "correct" is a matter of legal judgment, and what the new architecture unlocks.
by
Maharshi Patel
,
Pablo Felgueres
, and
Zach Huang
•
Sep 2, 2026
Companies run their businesses with contracts and almost all contracts get negotiated. According to Gartner, legal departments spend
21% of their capacity
on contracting, which is more than any other activity. Reviewing a contract typically takes between 20 minutes to five hours, depending on contract type and size.
When a company receives a contract from a counterparty, someone in their legal department compares it, clause by clause, against their company’s playbook — an internal rulebook that companies define to codify which terms are acceptable, negotiable, or dealbreakers. Then they mark up the document with redlines, comments, and send it back to the counterparty for review. This goes on until both parties agree to mutually agreeable terms.
Earlier this year, we rebuilt Harvey's playbook review engine from the ground up to make it even more effective in reducing the toil of contract review for our users. In this post, we walk through how the old system worked, why we made that change, how we evaluate quality of this problem (which is very subjective and relies on legal judgement), and how this new multi-agent system analyzes a document against a playbook, flags risks, and proposes surgical redline suggestions that lawyers can trust.
Why Contract Review is Harder Than it Looks
Playbook rules are conceptually simple, and include the following elements:
Standard position
: the ideal term a company wants to see in their contracts
Acceptable deviations
: fallback provisions a company is willing to negotiate
Unacceptable deviations
: dealbreakers for the contract
Guidance
: how to interpret and apply the rule given specific deal context
Optional:
whether or not it is ok for a clause to be absent in a contract
But there are also a few reasons why reviewing a real contract is complicated, especially for AI systems:
Contracts include complex conditional logic:
Contracts have complex conditional logic and clauses span pages, reference each other, and describe when certain conditions are triggered and not. And even after creating a playbook, a counterparty’s contract will almost never use your playbook’s exact words. Positions are often qualified with conditional logic. An agent reviewing a clause, therefore, requires comprehending meaning and repercussions of these conditional, syntatic vs semantic differences instead of word matching.
Rules interact across a document:
A single rule about assignment rights can touch four different sections in the document and at the same time, another rule might propose an edit on the same sentence creating a conflict. This complicates parallelizing review.
The right answer depends on deal context:
Lawyers don’t review contracts they have written (First Party Paper) the same way they review counterparty-written contracts (Third Party Paper). The way lawyers negotiate contracts depends on a lot of factors: Which party do you represent? Is the contract on your paper or the counterparty's? Is this round one of the negotiations or round seven? The same clause can be fine in one deal posture and unacceptable in another. If the counterparty rejected the previous suggestion, the same one again isn’t a good idea to propose.
The best edit is usually the smallest one:
Every redline you send gets scrutinized by an opposing counsel. If a clause needs three words changed and an agent rewrites the entire clause it will both slow down a deal and create extra work for human reviewers. Lawyers call this taking the "lightest touch," and it's a quality bar that out-of-the-box AI models and agents miss.
Some decisions cannot be delegated:
A playbook alone cannot capture the nuance of deal. If the counterparty is an important customer, a contract reviewer will likely give them more leeway. A good system identifies when a clause requires escalating to a human with the reasoning laid out based on the context of a deal.
Along with the nuances of document understanding in a specific deal context, handling the scale of documents and playbooks, which can be hundreds of pages long, is also a challenge given LLM response quality degrades with more tokens. For the Harvey platform, we need to ensure we maintain the same high quality on real contracts that can span hundreds of pages and still produce edits in a timely fashion.
Our First System: A Pipeline of Prompts
Like most production LLM systems of its era, Harvey's original playbook review was a workflow: a fixed sequence of model calls, orchestrated in code, each with a carefully engineered prompt.
The system consisted of two phases, classification and redline. Classification ran as a waterfall of status match. For each batch of rules, one model call asked: Does the contract match the rule's
standard position
? Rules that failed moved to a second call checking
acceptable deviations
match; rules that failed moved to a third call checking
unacceptable deviations
. Once classifications were done, a separate retrieval step then located supporting text in the document, and a final call wrote the summary.
Redlines came from another single model call: given one clause, one position, and a list of the contract's defined terms, the model returned a revised version of the clause. We diffed the revision against the original, and that diff became the tracked change.
This design had its pros and cons. It was predictable, debuggable, and cost-effective. Every call had one job. But each stage of the pipeline hard-coded an assumption about how contract review decomposes and those assumptions caused the system to struggle in complex playbook reviews:
Context got lost between LLM calls and subtasks of contract review:
Since each LLM call worked on its own, the context of classification got lost during citations and redlines. This would sometimes lead to inconsistencies in final output.
Edits were scoped by clause:
The redline model call got the context of one clause at a time and could only edit or delete it. It couldn't move language to the section where it belonged, add a missing clause, or keep an edit consistent with the rest of the document. Suggested text sometimes landed in the wrong place or related sections drifted out of order.
Suggestions were made in isolation:
Every rule was evaluated independently, so two rules could propose contradictory edits to the same sentence, and there was no rewriting for those edge cases. End users would have to manually fix these mistakes. Rules and documents that have complex dependencies across paragraphs also suffered because a single LLM call with limited budget won’t be able to think through and give accurate output to solve complex documents and playbooks.
With these limitations, reviews could over-redline, miss flags, insert suggestions in the wrong location, and miss whose paper the contract was on. Incremental prompt fixes moved individual metrics, but ultimately we needed a different architecture. And before choosing one, we needed a benchmark to measure improvements.
Making Legal Judgment Measurable
When we started this revamp, no public benchmark captured this workflow end to end, so we built our own evaluation suite with our in-house legal team.
The core dataset pairs contracts with playbooks for various contract types across hundreds of provisions. The benchmark evaluates different aspects of contract review:
Risk classification:
Ability to identify and categorize issues by their level of risk.
Redline quality:
A list of considerations that a revision by a competent lawyer would have, both in substance and style. These rubrics are defined for each example.
Flagging risk is best understood and scored as a classification problem which is a straightforward task. Redline quality is more complex in that it requires judgment on whether an edit is
minimal, correctly placed, and legally sound
. After sourcing the rubrics with lawyers, we set up an evaluation framework that uses LLM judges to score against these rubrics. We then used a committee of three frontier models to score independently and aggregate the votes.
The Multi-Agent System
With evals in place, we explored a few architectures of increased complexity and graded them across quality, latency, and complexity:
Approach
Quality
Latency
Complexity
Rule-based LLM workflow
Moderate
Excellent
Low
Single agent reviewer
Excellent
Unacceptable
Moderate
Orchestrator agent with subagents
Excellent
Good
High
Single Agent Reviewer
Agentic systems are powerful because they allow LLMs to keep solving a problem until certain conditions are met. This works well at scale because an agent can be equipped with tools to search for various key parts of a document, then look up rules and other information needed until it's satisfied with finding a redlined document that will work for a given deal and playbook.
To prove this hypothesis, we built a single agent with context of the review document and playbook and allowed it to iterate on the document using doc editing tools until it met requirements of the playbook. This was the simplest agentic solution and performed well on the benchmark, but was very high latency and would make for a poor user experience.
Orchestrator Agent With Subagents
We proved with a single agent prototype that quality problems can be solved with an agent. Often the best way to improve on latency is to find ways to parallelize work. With that idea in mind, we implemented an orchestrator-worker pattern consisting of a lead agent in charge of distributing work between parallel agents. Each of these agents in turn focus on a specific task, in this case reviewing a rule, and finally the lead agent reconciles the results to ensure final output is of good quality.
We found that this architecture is a good balance between quality, latency, and engineering complexity:
Worker agents work on individual rules:
The orchestrator is prompted as the lead lawyer on the review. It spawns a team of subagents to review each playbook rule, running up to dozens in parallel. Each subagent works the way an associate would: it reads its rule, reads or searches the contract, decides whether the contract complies with the playbook, chooses which position to pursue (standard or a specific fallback), and then drafts a list of suggested edits.
Crucially, it is an agent, not a function: if a clause references an exhibit, it goes and reads the exhibit. To make it fast and precise for it to reference and search for various parts of a document, we gave each component of the document a unique identifier. This allows agents to cite and edit a specific element unambiguously. Each subagent concludes its work by filing a short memo that explains its classification of a rule, edits to the contract, and rationale for its steps.
Worker agents work on a copy of the document:
Dozens of agents editing one document concurrently would be chaos, as they often would need to apply edits to the same paragraph or sentence while addressing different rules. This would result in an inconsistent state in the document as previous work done by one agent would get overwritten by another agent. To solve this, we built a branching mechanism where each subagent works on its own branch of a versioned document model, and every proposed edit is a tracked change on that branch, tagged with the rule that produced it.
When subagents finish, a reconciliation step merges branches the same way a version-control system would: non-conflicting edits apply cleanly to the final doc, and collisions of two rules touching the same text are escalated for the lead agent to resolve.
The orchestrator ensures everything gets reviewed:
The orchestrator has the task to dispatch reviewers, collect their work, and resolve conflicts in the document the way a senior lawyer would by drafting edits that satisfies all conflicting rules. It then takes a final pass to validate the quality of the review as a whole. This ensures that every rule gets classified and has corresponding edits when needed.
The orchestrator and workers share context:
The system takes into account the same context that lawyers use while reviewing a contract: which party they represent, whether the contract is on your template or theirs, how strict or permissive this negotiation should be, and any deal-specific instructions. Reviews can also draw on precedent documents the user attaches as additional context. Every agent in the hierarchy sees this context and adjusts their behavior accordingly.
State persistence to ensure continuity:
Every agent's state — classifications, chosen positions, edit summaries, reasoning — persists with the review. When a user asks a follow-up question, switches chosen position, or applies some suggestions and wants the rest reconsidered, we reuse the relevant agents rather than re-running the full agentic loop end to end.
Eval Results
Given this overhaul of the system, we wanted to share the differences between the performance of both systems. We saw major improvements in our ability to flag and classify risks and redline quality. On the other hand, reviewing a contract with this system takes more time, but it’s a reasonable tradeoff to make as we are optimizing for the quality of output.
Metric
Before
After
Change
Risk classification
59%
77%
+18%
Redline rubric
53%
87%
+34%
Average latency (minutes)
2.6
3.8
+47%
Making it Scalable
The agentic redesign improved review quality but it also introduced new challenges. As a result of using agents to complete work end to end, tokens and overall system latency increased significantly, especially on long contracts or playbooks with high rule count. Our system performed well in offline evals but to enable it to scale in real production, we built a set of guardrails around the agent team to keep reviews fast, reliable, and within our infrastructure limits:
Custom timeouts and targeted retries.
During our eval runs, some model calls occasionally got stuck in unproductive loops on unusual clauses. The issue would self-resolve usually on retry. To mitigate this, we set timeouts by model, review phase, and document size, then retry only the affected rule. This prevented one bad subagent from derailing the entire review.
Limiting concurrency.
Since every rule in a playbook fans out a subagent, we added concurrency limits and exponential backoffs to avoid overwhelming shared model infrastructure.
Prompt caching.
On long documents and playbooks, input tokens would explode exponentially, resulting in prohibitive cost of doing playbook review. However, each rule reviews much of the same underlying document. We used that fact to redesign our prompts to optimize for prefix cache hits. That helped reduce model cost by a significant amount and improved latency.
Stream results.
Even after all the optimizations, time to first result was high. To mitigate this, we enabled streaming results such that each rule’s result becomes available as soon as its subagent finishes. This allows the end user to begin reviewing outputs within seconds instead of waiting for the final result. Streaming also lets us expose progress and isolate slow or retried rules without blocking the rest of the review.
Using the best model for each task.
Our evaluation showed that no single model performed best across subtasks of contract review. We built the system to switch models across phases of the same review, selecting each one based on its measured quality, latency, and cost for that specific task.
A multi-model harness.
We built our agent harness to normalize the differences between model providers. This helps future-proof the system since we are able to quickly swap to the best performing models with minimal overhead.
What Agentic Review Unlocks
We are excited about the possibilities that reliable first pass reviews unlock.
Contract reviews can now run in the background. Whenever a new contract arrives over email or a shared file system, Harvey kicks off a review workflow, frontloading the work and giving users a well reasoned draft as a starting point.
Closing the loop with self-improvement becomes possible. Every accepted, edited, or rejected redline helps agents understand a legal team's preferences. This will allow us to build towards a personalized system, from users to accounts, such that every new contract needs less guidance and effort than the last one.
A team’s historical contracts become a new input to inform better reviews. This opens the ability to search across thousands of documents for previous examples to trust agent outputs and quickly understand what a team has approved in the past and why.
This is what we are building towards with
Contract Intelligence
, so every contract review improves the next and legal teams can stay in control as volume grows.
Acknowledgements
Thank you to the following members of Harvey’s team for their work on Playbook Review: Karl De La Roche, Rina Kim, Scott Werwath, Jianan Zhang, Sakshi Pratap, Kunal Baweja, Will Huang, Andy Pham, Alex Conrad-Dormoy, Aniket Joshi, Naman Agrawal, Nanxi Liu, and Andres Limcaoco.
Next Up
Harvey Tenet Research Preview
Scaling Document Processing Across the Harvey Platform
Building a Faster, More Reliable Upload Experience in Vault
Unlock Professional Class AI for Your Organization
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Overview
→
Agents
→
Vault
→
Knowledge
→
Spaces
→
Command Center
→
Contract Intelligence
→
Ecosystem
→
Harvey Mobile
→
Partnerships
→
Solutions
Innovation
→
Transactional
→
Litigation
→
In-House
→
Law Firms
→
Mid-Sized Firms
→
Company
Customers
→
Security
→
About
→
Careers
→
Newsroom
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
Instagram
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
