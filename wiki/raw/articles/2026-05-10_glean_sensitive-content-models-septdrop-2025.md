---
title: "Sensitive content models separate risk from noise at 80%+ accuracy"
source: "Glean Blog"
url: "https://www.glean.com/blog/sensitive-content-models-septdrop-2025"
scraped: "2026-05-10T01:21:09.256348+00:00"
lastmod: "None"
type: "sitemap"
---

# Sensitive content models separate risk from noise at 80%+ accuracy

**Source**: [https://www.glean.com/blog/sensitive-content-models-septdrop-2025](https://www.glean.com/blog/sensitive-content-models-septdrop-2025)

Product
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
Customers
Solutions
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
Resources
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
About
Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.
Sign in
Get a demo
Get a demo
Sign in
Get a demo
Get a demo
Product
Customers
Solutions
Resources
About
Sign in
Back
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
Last updated Jan 27, 2026.
Sensitive content models separate risk from noise at 80%+ accuracy
0
minutes read
Harsh Singhal
Software Engineer
Sarika Mohapatra
Software Engineer
Sunil Agrawal
Chief Security Officer
Julie Mills
PMM
Listen to article
0:00
0.5x
1x
1.5x
2x
Table of contents
Heading 2
Heading 3
Heading 4
Heading 5
Heading 6
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Share this article:
Listen to article
0:00
0.5x
1x
1.5x
2x
AI Summary by Glean
Glean’s multi-layered AI security approach leverages advanced detection models to proactively guard enterprises against prompt injection, toxic content, and malicious code, achieving industry-leading accuracy rates—97.8% for prompt injection, 93.5% for toxic content, and 94.3% for malicious code on industry-standard benchmarks.
Glean distinguishes itself in handling enterprise-specific risks by continuously refining its models for lower false positive rates and integrating context-aware reasoning, helping organizations trace and remediate threats using a comprehensive AI security dashboard and dual-model validation.
Glean’s sensitive content models, now in beta, automatically separate real risks from noise in unstructured enterprise data with over 80% accuracy by combining traditional classifiers, enterprise graphs, and contextual analysis, enabling precise data protection and confident AI scaling across diverse, complex environments.
Enterprise context is what makes AI relevant and valuable at work; the more context you bring the richer the insights. While context in Glean is permissions enforced, enforcement is only as good as the underlying permissions, and with hundreds of SaaS applications and billions of user-generated content, many enterprises can’t keep up with access controls and need additional help in getting data AI ready.
We introduced continuous protection and automated hiding of sensitive content in Glean across 100+ data sources at our annual user conference,
Glean:GO
. These features enabled customers to set up custom policies to detect what information is most sensitive for their organization—from employee data to passwords and authentication to top secret projects using 100+ infotypes, regex, and term matching.
Today, we’re excited to expand on this capability with sensitive content models that separate the signal from the noise by pairing traditional infotype classifiers with AI models trained on the full enterprise context, like document content, activities, and permissions.
These sensitive content models help to distinguish benign use cases from true exposure, seeing an 80% accuracy rate on unstructured data.
While many solutions detect sensitive content on structured data, few solve unstructured data, especially at the scale of coverage Glean provides. Unstructured content has no schema—sensitivity depends on context, not just content. That’s why Glean’s sensitive content models stand out: they interpret the context, leveraging proprietary search and enterprise graphs, around infotypes, regex, and term matches, to help companies automatically protect data at scale.
The design of sensitive content models
We’ve been fortunate to partner with several enterprises in developing these sensitive content models, enabling us to mirror how security teams actually assess exposure. Our enterprise customers’ security teams also helped identify use cases where data is less sensitive than it might first appear. These examples include:
Low severity
Medium severity
High severity
Test credentials shared with everyone in the organization.
Rationale for low severity: Security training materials, where the educational value outweighs minimal exposure risk since they are marked as examples
Personally identifiable data shared with the HR department.
Rationale for medium severity: Created and shared by the head of HR department.
Social security number shared with everyone in the company.
Rationale for high severity: Contains production SSNs and is anonymously accessible via link, meaning it's publicly exposed.
As shown in the examples above, we explain the decisions that the sensitive content models make so you can understand their logic. Based on in-product feedback, including thumbs up and thumbs down votes, the models continue to learn what is sensitive data to enterprises.
Sensitive content models understand context
The reason that sensitive content models can reason over unstructured data is because they understand context: individual document context, activity around the document, and enterprise relationships. Sensitive content models examine semantic relationships between document titles, content summaries, and the identified sensitive patterns. A document titled "Security best practices" containing example credentials receives fundamentally different treatment than a file called "Production database backup" with similar content patterns. The system understands contextual clues like "example," "sample," "template," and "training" that indicate educational rather than operational use.
Glean goes beyond looking at the document in isolation. It also looks at documents that are closely linked as well as where the document resides in folder structures, channels, and more. Documents owned by security teams, located in training containers, or tagged with educational metadata, receive different risk assessments than those in operational systems.
The models also use the enterprise graph, which maps the relationships behind enterprise data (including people, projects, and processes) to make AI context aware. The enterprise graph can discern the role of the document in the larger enterprise, whether the document is widely shared across security teams, frequently accessed by educators, or integrated into onboarding flows, suggesting that there’s a legitimate use case for sensitive content. On the other hand, documents with restricted access patterns, limited view history, or access concentrated in high-privilege roles may indicate higher risk.
Put AI to work with confidence using automated data security
Sensitive content models mark a shift—here at Glean, we’re now using AI to secure AI itself. By understanding both document and enterprise context, we can build AI models capable of discerning real, sensitive data from the noise across all unstructured data. Glean protects sensitive content with precision, and puts AI to work safely across the enterprise.
Check out our September Drop page for more details on other exciting Glean features that came out this week!
Sensitive content models are in beta and part of Glean Protect+, a premium security suite.
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Get The Resource
Get The Resource
Work AI for all.
Get a Demo
Work AI that works.
Get a demo
Ask AI for a summary about Glean
634 2nd Street
San Francisco, CA 94107
United States
Language
English (United States)
Japanese (Japan)
PRODUCT
Work AI Platform
Workplace Search
Assistant
Data Analysis
Deep Research
Canvas
Prompt Library
Agents
Agent Builder
Agent Orchestration
Agent Library
Agentic Engine
Connectors
Model Hub
Security
System of Context
SOLUTIONS
All Teams
Engineering
Sales
Marketing
Support
People
Retail
Financial Services
USE CASES
Enterprise AI
Enterprise Search Software
AI Agent Orchestration
COMPARISONS
Glean vs other alternatives
Glean vs ChatGPT Enterprise
Glean vs Microsoft 365 Copilot
Glean vs Claude Enterprise
RESOURCES
Resources Center
Product Videos
Guides
Customer Stories
Blog
Events
Webinars
Developers
Help Center
Download Glean
Product Drops
AI Glossary
Gleaniverse Community
COMPANY
About
Careers
Newsroom
Referrals
Partners
Trust center
260 Sheridan Ave, Suite 300
Palo Alto, CA 94306, United States
Gartner®, Peer Insights™, Voice of the Customer for Insight Engines, Peer Contributors, 28 June 2024.
Gartner Peer Insights content consists of the opinions of individual end users based on their own experiences, and should not be construed as statements of fact, nor do they represent the views of Gartner or its affiliates.
Gartner does not endorse any vendor, product or service depicted in this content nor makes any warranties, expressed or implied, with respect to this content, about its accuracy or completeness, including any warranties of merchantability or fitness for a particular purpose.
GARTNER is a registered trademark and service mark of Gartner, Inc. and/or its affiliates in the U.S. and internationally, and PEER INSIGHTS and GARTNER PEER INSIGHTS CUSTOMERS’ CHOICE BADGE is a registered trademark of Gartner, Inc. and/or its affiliates and are used herein with permission. All rights reserved.
©
2026
, Glean Technologies, Inc.
Website Terms
Privacy
