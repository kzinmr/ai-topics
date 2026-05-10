---
title: "Your Data, Your Control: How Harvey Manages Customer Data"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/how-harvey-manages-customer-data"
scraped: "2026-05-10T01:27:20.408269+00:00"
lastmod: "2026-03-20T15:00:00.000Z"
type: "sitemap"
---

# Your Data, Your Control: How Harvey Manages Customer Data

**Source**: [https://www.harvey.ai/blog/how-harvey-manages-customer-data](https://www.harvey.ai/blog/how-harvey-manages-customer-data)

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
Company
Your Data, Your Control: How :Harvey: Manages Customer Data
Sharing the core pillars that underpin our commitment to keeping customer data secure.
by
Chad Scott
•
Mar 20, 2026
Legal teams handle some of the most sensitive data in the world, and Harvey’s architecture was built with that responsibility at its core. We believe that customer data (e.g. customer inputs, outputs, and documents uploaded to Harvey) belongs only to the customer. Our systems are designed to access only the information relevant to a request, and only for the time period needed to fulfill it.
This principle is embedded into every layer of our infrastructure, from access control to encryption. Trust isn't something we apply after the fact — it's engineered into the system from the start. Our internal mantra for
security
is "Provably Secure," and we bring that discipline into every design decision. Throughout the rest of this post, I’ll walk through the core pillars that bring this mission to life.
Zero Data Access
Harvey is built on the principle that customer data should never be within reach of anyone who doesn’t absolutely need it. By design, the only entity that interacts directly with customer data is the Harvey architecture itself.
Our engineers and operations staff do not have access to customer data except where required or requested by our customers (for instance, to investigate a support request). Role-based access controls, network segmentation, and identity federation enforce this separation. Rather than relying on policy alone, we design our automations and systems to ensure customer data remains sealed off, even from our own team.
Infrastructure as Code and Just-in-Time Processing
Harvey’s backend environments are configured and managed through Infrastructure as Code (IaC), a SaaS security best practice. IaC manages and provisions infrastructure, such as networks, virtual machines, and load balancers, using machine-readable definition files instead of manual configuration of each component.
This approach allows Harvey’s infrastructure to be defined, deployed, and updated through code. Any changes to the core architecture by the Engineering team are versioned and reviewed, which makes it easier for human experts to track and audit changes. It also allows our environments to be recreated or rolled back to a known state when needed.
Encryption and Customer Control
Encryption isn’t a box we check, it’s a fundamental part of how Harvey keeps customer data under customer control.
All customer data and content handled by Harvey is encrypted both in transit and at rest. Encryption is applied automatically across every storage and communication layer, ensuring protection wherever your data resides or moves. There are no unencrypted pathways in our system; confidentiality is enforced by design, not by policy.
For organizations that require additional control, Harvey supports Bring Your Own Key (BYOK). With BYOK, customers manage the encryption key used to secure their stored data. They can rotate or revoke that key at any time, immediately rendering the data inaccessible to any system, including Harvey. This gives customers full cryptographic ownership of their information and the ability to define their own trust boundary.
Context Without Retention
When Harvey's models process a request, they work only with the data needed to complete that specific task. The relevant text or documents are assembled into a temporary query, with context that exists just long enough for the model to generate a response. Once the relevant model output is delivered and the AI request is complete, our model partners immediately delete that data.
By design, customer information does not persist between sessions, and no context is shared across users or workspaces unless you intentionally share selected data through a secure, scoped mechanism. (Learn more about Shared Spaces and our new
collaboration
capabilities
here
.)
Data Flow: From Input to Deletion
Customer data enters the Harvey environment in two primary ways: through prompts and through document uploads. Each one follows a distinct, tightly controlled path.
Prompt Data
When a user submits a prompt, Harvey's vector search engine identifies the most relevant documents from the customer's selected
vault
or uploaded documents. Those documents are then retrieved and incorporated into the model's temporary context window for inference. No document leaves the customer's environment or becomes visible to any other workspace.
Uploaded Documents
When customers upload files, those files are transmitted over encrypted channels (TLS 1.2+) to blob storage within the customer's regional environment, and each file is encrypted at rest using an AES-256 key. When Harvey's application later retrieves a document for a query, it's decrypted only in memory. Once the customer-defined retention period expires (Harvey supports retention from time of upload and time of last use), the source file is securely destroyed.
This lifecycle ensures that every byte of customer data — from upload to deletion — remains encrypted, isolated, and ephemeral.
Continuous Monitoring
In addition to the above protocols, Harvey’s Security team continuously monitors data access and system activity to ensure our controls work as intended. Every access attempt — whether by a user, service, or internal process — is logged and correlated across multiple systems for auditing and anomaly detection.
Our systems automatically monitor behavior that deviates from expected patterns, such as unusual access times, locations, or volume. These alerts feed into automated and human review where we assess system activity and metadata — never your customer data by default — to confirm that no unauthorized activity has occurred. In this way, monitoring isn't just a compliance requirement; it validates that our principles of least privilege, isolation, and ephemeral access hold true in daily operation.
A Platform Built for Trust
Every aspect of the Harvey platform — including how it stores, processes, and protects data — is designed around a single principle:
The customer stays in control
.
Access is deliberate, temporary, and verifiable. Encryption secures data even when it's not in use. Our systems discard context as soon as it's no longer needed. Continuous monitoring confirms that these guarantees hold true, consistently.
Harvey's approach to security is about architecture, not checklists. We build systems that enforce confidentiality by default, so our customers can focus on their work knowing their data remains theirs alone.
If you want to learn more about how Harvey manages and protects customer data, contact our team:
Request a Demo
Unable to load form. Please try again.
Try Again
Thank you!
We'll be in touch shortly.
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
