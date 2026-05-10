---
title: "Building Harvey’s iManage Integration"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/building-harveys-imanage-integration"
scraped: "2026-05-10T01:27:11.061459+00:00"
lastmod: "2025-10-29T13:00:00.000Z"
type: "sitemap"
---

# Building Harvey’s iManage Integration

**Source**: [https://www.harvey.ai/blog/building-harveys-imanage-integration](https://www.harvey.ai/blog/building-harveys-imanage-integration)

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
Building :Harvey:’s iManage Integration
How Harvey’s engineers solved technical challenges across security, scaling, and networking in order to bring this integration to life.
by
Reggie Cai
,
George Tamer
,
Ken Chen
,
Elaine Lu
,
Sandeep Uppaluri
, and
Abhishek Verma
•
Oct 29, 2025
Harvey now
integrates directly with iManage
, enabling teams to pull documents into Harvey, work with them, and push as artifacts back to iManage seamlessly. No exports or duplicates; just a secure, bidirectional flow that removes friction from legal workflows.
We codeveloped solutions and worked closely with both customer teams and iManage to ensure the integration met Harvey’s bar for enterprise readiness and governance. Throughout the rest of this post, we’ll dive deep into how we solved technical challenges across security, scaling, and networking in order to bring this integration to life.
Security: End-to-End Protection by Design
On the user side, the process to set up Harvey’s iManage integration is simple. First, an administrator installs the Harvey app from the iManage app directory in iManage Control Center (a one-minute process). Then, they initiate an industry standard OAuth 2.0 authentication flow from within the Harvey application.
We architected the integration to minimize customer risk at every stage. All
data is encrypted
both in transit and at rest, and
administrators can disconnect iManage accounts
with one-click at either the individual or workspace level. The integration also
builds off of Harvey’s existing governance framework
— ensuring that imported files and metadata follow the same segregation, retention, and compliance policies as any other customer data. This required updates to our data model such that it does not differentiate between file import sources.
Scale: Balancing Load Across the Platform
Building on top of iManage’s Universal API, we seamlessly incorporated both download and export functionalities into all of our platform’s surface areas that interact with files.
The Challenge: Allocating Limited Resources
The Harvey platform has multiple product surfaces, each with different usage patterns. For example,
Assistant
and
Workflows
are designed for real-time interaction and optimized for low end-to-end latency, while
Vault
is designed for larger, more asynchronous workloads with large payloads that can accept a higher latency.
In an ideal world, we submit all required requests to iManage in parallel to maximize concurrency and reduce latency. However, in reality, computing resources are not infinite. iManage implements rate limits on API endpoints as a best practice to ensure system stability, fair resource allocation across all tenants, and consistent performance for all users — architectural choices that are critical for enterprise grade document management systems.
This poses an interesting engineering challenge: How can we integrate iManage across the entire Harvey platform and ensure the best possible product experience in the face of limited resources? For example, a few
large Vault uploads
occurring in parallel could in theory trigger API rate limits if allowed to proceed without restrictions. This would cause real-time user journeys (like uploading files to an Assistant thread) to be delayed while waiting for additional quota. We needed a system that ensures no single request and no single product can consume all the external API quota, which would detrimentally impact other product areas and degrade the user experience.
The Solution: Distributed Rate Limiters
To address this challenge, we leveraged our distributed Redis caching layer and expanded it to build a rate limiter that accepts dynamic updates to existing quota limits for iManage. The dynamic rate limiter enables us to automatically respond to any quota changes; prevents large volumes of requests originating from a single task from detrimentally impacting others in the same workspace; and guarantees the prioritization and fairness of quota allocation across various products.
This rate limiter works with iManage's quota information provided in response headers after each API request completes — at both the API endpoint and customer tenant level — allowing us to respect iManage's resource management policies in real-time. We then allocate the quota remaining for a given period of time across Harvey’s various product surface areas based on pre-established distributions in order to maximize fairness across products.
If a product is attempting to use more than its allotted quota, when it tries to submit a network request to iManage, our internal rate limiter will intercept it and first attempt to acquire quota for the request. When that fails, the rate limiter throws an internal rate limiting error so that the original request never makes it to iManage servers, thus preventing that product from consuming too much quota within a given time period.
This way, we can cap the percentage of total quota a product like Vault can consume for a given workspace so that users in the same workspace do not need to worry about Vault file downloads causing Assistant file downloads to fail. This ensures the lowest latency for synchronous user journeys, while provisioning enough quota for the continuation of background tasks.
In other words, customers can effortlessly interact with the vital context stored in their iManage instance across Harvey’s platform without worry.
Networking: Integrating With iManage On-Prem
While many solutions focus solely on iManage Cloud, we invested equally in building reliable support for
on-prem environments
, because those are often the most complex setups owned by our largest enterprise customers. Installing an application on an on-prem tenant still requires manual configuration within iManage, but Harvey’s setup flow streamlines this process so customers can deploy on-prem just as easily as cloud.
The tougher problem was connectivity. On-prem systems sit deep inside corporate networks with no natural path in or out, and any external traffic has to satisfy tight security boundaries. To make the integration work, we collaborated closely with our customers’ infrastructure and security teams to design a network path that allowed Harvey’s API requests to reach iManage without being hijacked by SSO redirects or blocked by firewalls.
“
:Harvey:'s engineers collaborated with us to create a secure iManage on-premises integration. After exploring various configurations and security measures, we implemented a solution that connects seamlessly with our on-premises instance ensuring a smooth experience for our users.
”
John Jovanovski
Head of AI & Cyber, Clayton Utz
The most common and secure pattern we’ve seen is publishing iManage through Azure Application Proxy. In most customer environments, Azure Application Proxy is used to safely expose internal apps to the internet. It works by running a lightweight connector inside the corporate network that makes an outbound TLS connection to Microsoft’s Edge. External users hit Microsoft’s Edge endpoint and their traffic is relayed back through that tunnel, so admins don’t need to open inbound firewall ports. This solution can be extended to app proxies hosted in other cloud providers.
For integrations like ours, customers typically set up a dedicated API hostname and configure App Proxy in Passthrough mode. This avoids the interactive Entra ID pre-auth flow that breaks server-to-server calls, while still hiding the iManage server behind Microsoft’s Edge and allowing customers to layer on their own security controls such as IP allowlists or WAF rules. In practice, this setup separates user and machine traffic cleanly: Employees continue to access iManage through the user-facing URL with MFA and Conditional Access, while Harvey connects to the API hostname through a hardened, tunnel-backed route built for automation.
By investing deeply in security, scalability, and network resilience, Harvey’s
iManage integration
empowers customers to use their proprietary knowledge safely and efficiently across the platform. We’re excited for teams to experience a system designed for real-world enterprise needs, where AI and document management work seamlessly together.
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
