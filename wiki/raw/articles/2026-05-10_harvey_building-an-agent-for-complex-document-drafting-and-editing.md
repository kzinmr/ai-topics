---
title: "Building an Agent for Complex Document Drafting and Editing"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/building-an-agent-for-complex-document-drafting-and-editing"
scraped: "2026-05-10T01:27:21.846814+00:00"
lastmod: "2026-03-24T15:00:00.000Z"
type: "sitemap"
---

# Building an Agent for Complex Document Drafting and Editing

**Source**: [https://www.harvey.ai/blog/building-an-agent-for-complex-document-drafting-and-editing](https://www.harvey.ai/blog/building-an-agent-for-complex-document-drafting-and-editing)

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
Building an Agent for Complex Document Drafting and Editing
How we designed an agent that iteratively builds a Word document in memory.
by
Aadil Manazir
and
Scott Werwath
•
Mar 24, 2026
Much of legal work happens inside Microsoft Word documents. Lawyers draft, revise, and circulate .docx files, often exchanging multiple rounds of redlines before a document is finalized. For Harvey to fit naturally into this workflow, its edits must be high-quality, low-latency, and preserve the document’s formatting and structure.
The .docx format is built on Office Open XML (OOXML), which has a long tail of complexity. For example:
Bolding a single word
splits the paragraph into three separate "run" elements, each carrying its own formatting properties.
List numbering
isn't stored with the text at all. It lives in a separate numbering.xml file as abstract numbering definitions, referenced through a chain of indirection that gets compiled at render time to produce the marker a user sees as "1." or "(a)."
In September 2025, we shipped
full document editing
in the Harvey for Word Add-In. As we pushed to support more complex editing capabilities, we reached clear limitations with the existing full document editing system.
This post explains what broke in the original system, the architectural shift we made, and the key capabilities it unlocked.
Challenges With our Previous System
Our first-generation architecture had an orchestrator dispatch one-shot sub-agents to process chunks of the document in parallel. The orchestrator read the full document, created an edit plan, and assigned chunks to workers.
The problem was compounding complexity. Each sub-agent simultaneously handled over 16 requirements in a single shot: exact paragraph indexing, full paragraph regeneration, tracked change understanding, chunk boundary constraints, and more.
When we began experimenting with advanced list editing support, we realized we hit a clear ceiling. For example, to create a new numbered list, the model had to generate a unique list key mid-output and reference that same key later to attach subsequent items, all while juggling every other requirement.
The deeper issue was architectural.
We were asking the model to be both a legal reasoning engine and a state machine simultaneously.
Every new capability we added made existing ones more fragile.
An Agent That Builds a Document in Memory
In the fall of 2025, we researched Claude’s Docx skill, which stood up Python scripts to edit .docx files directly. We found that it was too slow and produced lower quality results for the types of edits our users needed. Additionally, python-docx, the most widely used library for agentic docx editing, lacked full feature support for OOXML and is no longer actively maintained.
So, instead we designed a new system around two key insights:
The legal text is first class.
The document representation is a reduced form of the underlying XML. Most of the OOXML is noise when serving the user's query. We expose the minimal OOXML information for the agent to preserve the document's complex markup, and prioritize the legal text.
The model iterates on the document in memory.
We parse the docx file into an in-memory representation via a proprietary library with full OOXML support. We give the model tools to iterate on an in-memory document that are optimized for legal workflows. Each tool has a focused interface, and the model composes them in whatever order makes sense for the task. XML handling, state management, and edit generation stay in deterministic code.
Here’s an overview of the agent workflow:
The backend parses the uploaded .docx and constructs a mutable in-memory document.
The agent reads, searches the document, retrieves context from knowledge sources, and edits this representation through its tools. The document updates after each edit, so the agent always sees the current state as it iterates.
The agent verifies its edits to the document through a get_diff tool, which exposes the changes in a model-friendly diff. The agent can continue editing if it’s not satisfied.
The system maintains two copies of the document: an immutable snapshot of the original and the mutable working copy that the agent edits. When the agent finishes, an edit generator diffs these two states to produce the set of structured edits.
In the Harvey for Word Add-In, those edits are applied to the Document via OfficeJS and become tracked changes via a word-level diff.
In Harvey's web Assistant, the edits are applied directly back to the document via a docx service to produce an edited file.
Parallel Editing With Sub-Agents
The new system supports workflows on long, complex documents. For example, the agent can apply a compliance playbook and check defined terms, indemnification clauses, and boilerplate language. To improve latency and quality for these workflows, the system spawns sub-agents that each receive an isolated copy of the document.
Sub-agents can search and edit copies of the document independently without seeing each other's changes. When they finish, a reconciliation step auto-merges non-conflicting edits. Conflicts are surfaced to an orchestrator agent for resolution.
This architecture improves latency, since sub-agents process their portions of the document in parallel rather than sequentially.
How we Improved Quality
Three properties of the agentic architecture improved the issues with the previous system.
1. Context Window Awareness
The previous system's orchestrator planned all context allocation upfront. Each sub-agent received a fixed chunk and had to work within those boundaries.
Now, the agent gathers its own context. The system adapts to document size: small documents encourage a full read, while large documents require search-only access, forcing the agent to retrieve relevant paragraphs with surrounding context rather than stuffing the entire document into the context window.
2. Self-Review
The previous system had no opportunity for the model to verify its own work. Now the agent reviews a diff of every change relative to the original document after editing. We prompt it to check for specific issues (e.g. broken formatting, tracked change handling in the output) based on patterns identified from customer feedback.
3. Structured Tools
The previous system produced text changes, formatting, and list operations in a single shot, which caused complexity blow-up. Now, the model can iterate using optimized tools while most of the difficult XML work is offloaded to our backend service.
Agent-Powered Capabilities in the Harvey for Word Add-In
Agentic docx has transformed the
Word Add-In
experience. The three separate interaction modes (ask, edit, and draft) were unified into a single agent, which helped simplify the user experience. Latency is now dynamic, where simple queries return fast and complex queries take the time they need. Users also now have a collaborative editing experience. Follow-up requests build on previous context, and the agent reviews its own work until it produces a clean redline.
The agent handles advanced multi-step operations over lists, tables, and styles without breaking existing formatting. It also queries Vault, web sources, and uploaded files dynamically as it works, improving its handling of knowledge sources.
As a result, we’ve seen significant improvements in quality. Edit accept rate increased
40%
relative to the previous system, and average queries per WAU increased
70%
. Customers have described the new experience as a “night and day” improvement.
Agent-Powered Document Editing in Harvey’s Web Application
The same agent makes docx editing a first class workflow in Harvey’s web application: the agent runs behind docx-editing queries and applies edits to each file.
In the web app, document editing has moved beyond markdown to a full docx editing experience, allowing users to export polished docx files. We also support seamless multi-document workflows by coordinating several docx agents that work across multiple documents in a single session.
Docx editing is one of the hardest surfaces to get right in legal AI. This new system provides a high-quality document editing experience across the Harvey for Word Add-In and the Harvey web app, and gives us the foundation to keep raising the bar for our customers.
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
