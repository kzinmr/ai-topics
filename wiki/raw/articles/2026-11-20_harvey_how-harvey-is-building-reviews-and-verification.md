---
title: "Proof, Not Just Trust: How Harvey is Building Reviews and Verification"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/how-harvey-is-building-reviews-and-verification"
scraped: "2026-11-20T06:00:37.851094+00:00"
lastmod: "2026-11-19T18:00:00.000Z"
type: "sitemap"
---

# Proof, Not Just Trust: How Harvey is Building Reviews and Verification

**Source**: [https://www.harvey.ai/blog/how-harvey-is-building-reviews-and-verification](https://www.harvey.ai/blog/how-harvey-is-building-reviews-and-verification)

:Harvey:
Products
Solutions
Customers
Security
Resources
Company
Platform
Overview
→
One platform for all legal AI work
Agents
→
AI agents designed for legal work
Vault
→
Store and analyze legal documents
Knowledge
→
Legal, regulatory, and tax research
Spaces
→
Secure, shared legal workspaces
Command Center
→
Analytics to lead AI transformation
Memory
→
AI that remembers your preferences
Review Tables
→
Connected, cited tables your team builds on
Legal Work Orchestration
→
Orchestrate legal work with agents
Apps
Contract Intelligence
→
AI contract review and negotiation
Horizon Scanning
→
Track and act on regulatory changes
Intake
→
Capture and resolve legal requests
Facts & Chronologies
New
→
Connect facts, strengthen your case
Connect
Connector Library
New
→
Connect your tools to Harvey via MCP
Ecosystem
→
Use Harvey wherever you work
Overview
For In-House Teams
→
For Law Firms
→
For Mid-Size Firms
→
Industries
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
→
Public Sector
→
Practice Area & Teams
Litigation
→
Transactional
→
Innovation
→
Featured
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey
Research
→
Research on the frontier of legal AI
Press Kit
→
Official logos and brand guidelines
Support Hub
→
Product documentation and trainings
Services
→
Harvey’s experts, working alongside your team
Featured
Four Legal AI Workflows to Help Mid-Sized Firms Take on More
→
Explore four practical legal AI workflows that help mid-sized law firms expand capacity, improve matter economics, and take on more complex work.
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
Newsroom
→
Press releases and partnership announcements.
Featured
Harvey Raises $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
→
Login
Request a Demo
Products
Platform
Overview
One platform for all legal AI work
Agents
AI agents designed for legal work
Vault
Store and analyze legal documents
Knowledge
Legal, regulatory, and tax research
Spaces
Secure, shared legal workspaces
Command Center
Analytics to lead AI transformation
Memory
AI that remembers your preferences
Review Tables
Connected, cited tables your team builds on
Legal Work Orchestration
Orchestrate legal work with agents
Apps
Contract Intelligence
AI contract review and negotiation
Horizon Scanning
Track and act on regulatory changes
Intake
Capture and resolve legal requests
Facts & Chronologies
New
Connect facts, strengthen your case
Connect
Connector Library
New
Connect your tools to Harvey via MCP
Ecosystem
Use Harvey wherever you work
Solutions
Overview
For In-House Teams
For Law Firms
For Mid-Size Firms
Industries
Healthcare & Life Sciences
Energy & Utilities
Technology
Media, Entertainment & Telecom
Public Sector
Practice Area & Teams
Litigation
Transactional
Innovation
Featured
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team
Resources Hub
The latest videos, webinars, guides, and reports from Harvey
Research
Research on the frontier of legal AI
Press Kit
Official logos and brand guidelines
Support Hub
Product documentation and trainings
Services
Harvey’s experts, working alongside your team
Featured
Four Legal AI Workflows to Help Mid-Sized Firms Take on More
Explore four practical legal AI workflows that help mid-sized law firms expand capacity, improve matter economics, and take on more complex work.
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
Newsroom
Press releases and partnership announcements.
Featured
Harvey Raises $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Request a Demo
Login
US
EU
AU
Product
Proof, Not Just Trust: How Harvey is Building Reviews and Verification
Lawyers sign their name to their work. AI should give them clear proof, not just ask for trust.
by
Dana Ingraham
and
Ryan Samii
•
Nov 19, 2026
A lawyer signs their name to every piece of work that leaves their desk, even when Harvey wrote the first draft. As Harvey takes on more of that work, from reviewing tens of thousands of documents in a single table to working through an entire data room for a diligence memo, verification becomes the bottleneck.
In most fields, the output tells you most of what you need to know. An engineer can run AI-written code. A designer can judge a screen on sight. But a diligence memo can read cleanly and still be wrong because the agent never opened a side letter or missed an amendment. The only way to know is to see how the answer was produced: what was read, what was skipped, and what it relied on. In legal, the work itself is part of the output.
Today that check is the lawyer: a partner reading a draft line by line, or an associate clicking through every citation. That doesn’t scale at the speed agents now work.
So we think about solving verification for legal AI across three dimensions:
What Harvey checks on its own:
citations, quotes, and pin cites.
How Harvey shows its work,
so lawyers can judge what a machine can’t:
what it read, what it might have missed, and the calls it made.
Where Harvey stores the record of lawyers’ reviews:
who checked what, who signed off, and the sources that follow the document to the next stage.
The first two localize and sharpen the lawyer’s review; the third records it.
Harvey Checks What Can be Checked
Some questions in legal work have a clear answer. Does this case exist? Does it say what the brief claims at that page? Is the quote accurate? A machine can answer those, so Harvey should answer them before a lawyer reads a word.
Harvey has invested in these checks from the start. In 2024, our BigLaw Bench sourcing evaluation measured whether a model can point to the exact passage behind each claim. In legal research,
agentic search
ties each answer to specific documents.
Harvey Graph
catches authority that has been overruled or limited. And our open-source
Legal Agent Benchmark
grades long-horizon legal work.
Those checks work on the answers Harvey writes. The harder case is the full document a lawyer is about to sign: a 40-page brief with dozens of citations from Harvey and elsewhere. Checking each one by hand could take longer than the research itself.
Cite Check
, coming to Early Access later this year, runs these machine checks on a full brief. It sticks to questions that have a right answer.
Upload a brief and it finds every citation, then checks each quote and pin cite against the full opinion in
US Case Law
. Each citation is marked “verified,” “needs review,” or “issue found.” Findings appear as review cards in the brief, with suggested fixes as tracked changes to accept or reject.
Cite Check shows the work for one part of the brief. Every “verified” citation is one a lawyer no longer needs to click through by hand. Whether the argument holds up is still a judgment call, which brings us to the second layer of our product strategy.
Harvey Shows its Work, so Lawyers Can Judge it
Most of what matters in legal work can’t be checked automatically. Is the analysis complete? Did Harvey treat an anti-assignment clause as a change-of-control issue? Those calls need a lawyer. Harvey’s job is to make them easy to find.
Harvey has made its work checkable from the start. Every answer links each statement to the passage that supports it, so a lawyer can click straight to the source. That was a deliberate choice. When we
tested general-purpose models in 2024
, asking them for sources made their answers shorter and less accurate. Review Tables took this further: every cell has its own citation, so any single answer can be checked in one click.
Models have come a long way since then, and agents change the problem. When Harvey works through a buyer’s request list across an entire data room, the risk isn’t only a wrong citation. It’s the document Harvey never opened, the search term it didn’t try or the judgment call it made without confirming. A citation can’t show any of those.
Today, thinking states show which files Harvey is searching, what it searched for, and what it reads as it works. This means that an associate’s memo and Harvey’s work have had the same blind spot: nothing on the page shows what they
didn’t
find.
Next, Harvey’s answers will come with a short scope note that gives you visibility into which documents it read in full, what language it looked for, and which files it couldn’t read. Harvey will display something like, “Read all 212 contracts in full, including amendments and side letters. Couldn’t open 3 password-protected files.” In our conversations with early design partners, lawyers trusted a plain account like this more than a coverage percentage.
We’re also adding visibility into judgment calls Harvey made. Historically, when a junior associate brings a diligence summary to a partner’s office, the partner doesn’t reopen every source behind every sentence. They ask about the process. Which documents did you review? Did you account for the new deal mechanics? If the process was sound, the partner can rely on the work. If it wasn’t, the partner sends the assignment back with updated instructions, drawing on their expertise and the specifics of the matter.
Lawyers need to supervise agents the same way. Citations show where each statement came from. They don’t show which instructions or playbook Harvey followed, what it set aside, or where it made a judgment call.
We want finished work to carry that record, with Harvey’s judgment calls marked so a reviewer can check those first. We’re also exploring how Harvey can pause on a judgment call, ask the lawyer, and record the decision before continuing. And when the process was wrong, a lawyer should be able to correct the instructions and send the work back instead of fixing the output line by line.
We’re also continuing to prioritize building more specialized solutions in Harvey by practice area. For litigators, checking the work starts with the record. In a large matter, the facts are spread across thousands of documents, emails, and transcripts. Harvey’s
fact graph
will let Harvey extract each fact, link it to the page it came from, and organize it by issue, person, and event. It will build chronologies with every entry cited and flag inconsistencies. Lawyers accept, edit, or reject each suggested fact against its source, so the record the team builds on has already been checked.
Review With Harvey Becomes a Record
AI creates a new problem for supervising lawyers. A polished draft looks finished whether or not anyone checked it. We have regular conversations with partners who worry that associates aren’t verifying AI work, and that nothing shows whether they did. Software teams solved this with version control: in a system like Git, every change records who made it and when, and a teammate reviews and approves it before it’s merged.
AI-powered legal work needs something comparable, and Harvey has been building toward it.
Review Tables
came first. Teams can assign rows to colleagues, flag cells that need follow-up, and mark each cell as verified. Each cell keeps an
activity log
of who did what and when.
Harvey II
extended that record to the whole matter. In Spaces, lawyers can assign a task to a colleague or an agent, with a reviewer who’s notified when the work is ready.
As agents take on more of the work, firms also need a record for the agents themselves. In Command Center, admins already approve which agents are shared, set who can use each one, and see how they’re used.
But much of the review still happens outside these tools: in a Word draft emailed to a partner or in comments that don’t connect back to the sources.
So, we’re going to bring comments into the documents Harvey creates. A lawyer can comment on a clause, tag Harvey to check it against the firm’s form or the source documents, and see Harvey’s answer and suggested edit next to the text. Each document keeps a record of who checked which part and what they found.
Citations will stay with the document.
When a draft moves from Harvey to Word to a partner or client, its sources should move with it. Today, threads and Review Tables keep their citations, Word exports can include a references section, and Excel files Harvey creates cite individual cells. Next, we’re extending citations to every type of file Harvey creates.
Continuing Explorations at the Frontier
Verification is one of the most active problems in AI, and some of our clients are already ahead of the curve. Firms have used Workflow Builder to add a second step that checks the first against their own criteria. In effect, they’ve built their own LLM-as-judge workflows. Others are writing evaluation sets and review agents for their practice areas. That’s the closest thing yet to a legal test suite: checks written by the people who know what good work looks like, run every time.
We’re building on both with clients. A separate grader, ideally a different model, checks the work against a standard the firm sets and the agent can’t change. And we test our own checks against answer keys written by lawyers, so they catch real errors without flagging what’s already right.
A check also means more when the same task, run twice, gives the same answer. Engineers call this
determinism
, and it’s a body of work of its own at Harvey.
Where we’re headed is a single evidence trail for every piece of work: each statement tied to the source that supports it, the checks it passed, who reviewed it and what they decided. The lawyer’s job shifts from reading every line to setting the standard and reviewing the evidence.
Our product vision isn’t to ask lawyers for more trust. It’s to give them more proof.
Request a Demo
Thank you!
We'll be in touch shortly.
Next Up
Apply Institutional Knowledge to Legal AI Workflows with Harvey and DeepJudge
Build Review Tables Faster and Keep Them Current
GPT-6.2 Astra and GPT-6.2 Sol, Coming Soon to Harvey
Unlock Professional Class AI for Your Organization
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Products
Overview
→
Agents
→
Vault
→
Review Tables
→
Knowledge
→
Spaces
→
Command Center
→
Contract Intelligence
→
Horizon Scanning
→
Ecosystem
→
Intake
→
Partnerships
→
Memory
→
Legal Work Orchestration
→
Facts & Chronologies
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
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
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
