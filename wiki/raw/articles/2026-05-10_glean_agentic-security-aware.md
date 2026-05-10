---
title: "How to Deploy AI Agents With Confidence: Introducing AWARE and New Glean Protect Capabilities"
source: "Glean Blog"
url: "https://www.glean.com/blog/agentic-security-aware"
scraped: "2026-05-10T01:27:03.907293+00:00"
lastmod: "None"
type: "sitemap"
---

# How to Deploy AI Agents With Confidence: Introducing AWARE and New Glean Protect Capabilities

**Source**: [https://www.glean.com/blog/agentic-security-aware](https://www.glean.com/blog/agentic-security-aware)

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
Last updated Mar 12, 2026.
How to Deploy AI Agents With Confidence: Introducing AWARE and New Glean Protect Capabilities
0
minutes read
Sandy Tang
Product Marketing
Sunil Agrawal
Chief Security Officer
Allan Livingston
Product Lead, Enterprise
Sarika Mohapatra
Software Engineer
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
AI agents are rapidly becoming central to enterprise applications, but most organizations still lack AI-specific controls and worry about AI-powered data leaks, creating a widening gap between innovation and governance for CIOs and CISOs.
Glean, alongside Databricks and Palo Alto Networks, introduces the AWARE framework—Actor Intent, Work Context, Autonomous Guardrails, Real-Time Risk Scoring & Blocking, and Ecosystem Observability—to give enterprises a structured way to evaluate, govern, and monitor AI agents so they stay in scope and accountable across systems.
Glean operationalizes AWARE through Glean Protect and a private-by-design platform, adding restricted topics, agent alignment models, runtime attack protection, sensitive content policies and triage, SIEM/SOAR and Palo Alto integrations, and flexible single-tenant or customer-managed deployments with strong certifications like ISO 42001, ISO 27001, SOC 2 Type II, and HIPAA.
AI agents are rapidly becoming more capable by the day, transforming how work gets done by automating decisions, orchestrating workflows, and acting on behalf of people at unprecedented scale. By the end of 2026, Gartner predicts that
40%
of enterprise applications will embed task-based AI agents. However,
69%
of organizations cite AI-powered data leaks as their top security concern, while
47%
have no AI-specific controls in place, according to Big ID. Enterprise leaders are asking: how do we deploy agents without losing control?
The gap between AI innovation and governance is widening. Traditional security frameworks weren't built for AI that acts autonomously across your entire tech stack. With CIOs looking for speed and innovation, while CISOs are pushing for better visibility and governance, there’s a real tension around AI agents.
Introducing AWARE: A framework for secure AI agent deployment
To help unravel this tension between innovation and governance, we’ve created the AWARE framework to codify a philosophy on how enterprises should think about the governance of AI agents.
The AWARE framework is a collaboration led by the
Work AI Institute,
our research center at Glean, in partnership with security leaders who aren’t just researching AI, they’ve seen it in production, know the guardrails enterprises need, and are actively building the next security standard. Our framework’s co-authors Databricks and Palo Alto Networks agree: AI agents have changed how we should think about security and governance.
The AWARE framework helps you answer five critical questions about agent behavior:
A – Actor Intent
:
Who or what is acting, and why?
Agents operate with a specific job to be done, often on behalf of a human. Ensuring the agents understand the intent of that job and stay within that scope is key.
W – Work Context: Is this data or action sensitive in this context?
Sensitivity depends on both the job to be done, the person, and when it’s being asked, something static labels alone can’t capture.
A – Autonomous Guardrails: Is this behavior within policy and purpose?
Agents hallucinate, drift, and act out of scope, that’s why guardrails are needed at runtime.
R – Real-Time Risk Scoring & Blocking: How risky is this right now?
The agent system should act on risks as they occur, such as rapid access patterns, unexpected API calls, and more to curb abuse patterns.
E – Ecosystem Observability: Can we trace what the agent did, across systems and time?
Agents operate across apps, APIs, files, and cloud tools. Being able to trace the agent is important for accountability and reliability.
With this framework, both IT and security can collaborate to assess their overall agentic system and each newly created agent. By going through these questions, teams can ensure there are clear guardrails and accountability for agent actions. They can also continuously monitor and remediate any potentially risky behavior.
This enables CIOs to drive innovation and business agility and CISOs to have confidence that every agent operates with secure, governed boundaries. With AWARE, organizations empower agent adoption without sacrificing trust or control.
Have a look at the
complete AWARE framework
for guidance on how to approach AI agent deployments securely.
Guardrails on. Risks down. Agents up. See what’s new in Glean Protect.
While the market races to ship AI capabilities, many solutions are bypassing foundational security controls and leaving enterprises exposed at the platform level. We took a different approach: instead of bolting security afterwards, we’re building it according to our AWARE framework into the foundation of Glean.
AI agents that stay in scope
As agents become more autonomous, Glean Protect continues to implement comprehensive guardrails: controls on who can build and deploy agents and limits on the actions they can take.
Now, you can enforce
restricted topics policies
that flag or prevent conversations on disallowed topics in real time. For many organizations, this is a critical way to enforce acceptable use for AI at work and keep it focused on productivity while preventing risky conversations about compensation, performance decisions, and personal financial advice.
Glean Protect provides several restricted topics policies to help you quickly get started.
These are the kinds of topics enterprises worry about when they bring AI into the organization and Glean helps stop them before they turn into a privacy or compliance issue. We also made it easy to get started with out-of-the-box policies for common high-risk topics. These deterministic guardrails around AI agents capture multiple aspects of the AWARE framework, but it embodies the W – Work Context the most, given that this data and action are sensitive in this context.
Glean Protect also offers
agent alignment models
that check what an agent plans to do before allowing it to proceed. These checks pre-scan every write action before it runs. The models detect and flag unsafe or misaligned agent attempts to reduce the risk of harmful changes across your systems. Imagine a performance coach agent planning to share notes to an org-wide Slack channel instead of a private DM, the agent alignment models will catch this before it happens. To refer back to the AWARE framework, this is the A – Autonomous Guardrails.
This is all in addition to Glean Protect’s existing runtime protection designed to block prompt injections, malicious code, and toxic content the moment they occur. These can be captured under R – Real-Time Risk Scoring and Blocking from the AWARE framework as it is assessing risk and stopping attacks.
Effortlessly keep all your data safe
Enterprise AI needs to be grounded in the full context of your company. But when data becomes widely available to AI, it can surface overshared information that was previously buried. This content wasn't necessarily a problem before, because finding it required knowing exactly where to look. Security through obscurity isn't a policy, but for many enterprises, it was an accidental reality. This is why permissions alone are not enough. As AI increases visibility, permission gaps become far more apparent, which is why enterprises need an additional layer of protection through sensitive data detection and enforcement.
To build in deterministic guardrails, Glean Protect now empowers you with pre-built sensitive content policies you can immediately turn on. Instead of beginning on a blank slate for data loss prevention, these policy templates can start scanning for common high-risk patterns and oversharing behaviors.
Glean Protect empowers you to turn on sensitive content policies with one-click.
Some of these
out-of-the-box policies
include secrets and credentials, payment card and banking data, personal medication information, and PII such as sensitive personal IDs. As you get started with a template, you can make adjustments to the policy to cater to your organization’s needs.
Glean continuously discovers sensitive content that’s been overshared and automatically hides it. You don’t need to be a data security expert, Glean’s models start protecting your data right away.
Glean’s sensitive content models separate signal from the noise to determine the severity level of sensitive findings. You can now also
tune the model
to understand what's sensitive to your organization with natural language, like "If documents owned by HR and containing ‘credentials’ infotypes are shared with someone outside of HR, increase the severity." That way, the sensitive content models can work for your organization.
Both sensitive content policies and models are relevant to the W - Work Context of the AWARE framework. It's important to have these policies in place to determine the types of content that is sensitive within your organization and safeguard it.
Glean Protect makes it easy to organize and triage sensitive findings.
Glean now offers a
triage workflow for sensitive content findings
. If you want to play it safe, you can auto-hide sensitive data. But many organizations want a review and remediation cycle so they can validate findings, assign clear ownership, strengthen their data security posture, and tune their models or policies based on what’s actually sensitive to their organization. We make that possible with a new triage workflow for sensitive content findings.
And through our open ecosystem, you can easily export these findings to your SIEM/SOAR of choice.
Today, security teams can automate how sensitive findings are managed by
integrating
Tines SOAR remediation runbooks
to investigate and resolve cases. By managing cases within Tines, you can fully remediate overshared content at the source.
While we’ve already partnered with Palo Alto Networks to leverage
Prisma AIRS
for AI runtime security, we have now added
Cortex Cloud DSPM
for data security posture management, so security teams can standardize security using the tools you’re already invested in. We are also expanding this secure ecosystem by bringing agentic Glean search into Prisma Browser, empowering users with intelligent, AI-driven discovery directly within their secure browsing sessions.
Our open approach to our security program embodies the E – Ecosystem Observability in the AWARE framework. We extend beyond Glean’s UI and into best-in-class security tools your teams are already using.
This suite of security guardrails ensure your data is always AI-ready without creating new exposure risks.
Private-by-design platform
Our approach to the cloud is different. Instead of a traditional multi-tenant SaaS model, we built for enterprises that need AI data to reside in a
single-tenant environment
. Our architecture supports
deployment in the cloud of your choice
(AWS, Azure, or GCP) along with regional coverage to meet enterprise data sovereignty requirements, all fully isolated from every other customer.
Today, we’re introducing a new deployment model:
customer-managed deployment.
Built for some of our largest and most security-conscious customers, this model gives organizations direct
control over the deployment of Glean code in their cloud.
It’s designed for teams with strong requirements around where software runs, how traffic flows, and who controls access to data.
With customer-managed deployment, you control the deployment of code in your environment. You also get
private connectivity
, where every user request, response, and log can stay on your private network instead of traveling over the public internet. You define the destinations Glean is allowed to reach, and Glean stays within those boundaries. You can also use
customer-managed keys,
so your data is encrypted with keys you control.
In practice, this means the infrastructure runs in your cloud, you own the operational controls, and you hold the keys that ultimately govern access to your data.
With Glean, the platform is private by design. It starts with our deployment models and carries over to connectors that enforce permissions, AI interactions that are authorized by the user, and models that only access the data a user is permitted to see, backed by agreements with model providers to prevent training on customer data or data retention.
You have the option to run Glean in your cloud, in your region, or in your VPC.
Glean’s platform is validated through independent certifications. Glean recently achieved
ISO 42001
, the world’s first certifiable standard for AI Management Systems (AIMS), and maintains ISO 27001, SOC 2 Type II, and HIPAA certifications, delivering the security foundation and verified assurances that make
enterprise AI safe
.
The path forward: Deploy AI agents with confidence
We hope that introducing the AWARE framework provides a better way for CIOs and CISOs to speak a common language about agent risk and governance.
Here at Glean, we've put the AWARE framework into practice. That starts with A – Actor Intent where agents act on behalf of the user with granular role-based access controls. W – Work Context by helping keep AI focused on approved use cases with restricted topics policies. A – Autonomous Guardrails that include agent alignment models that keep agents in scope instead of drifting from their intended purpose. R – Real-Time Risk Scoring & Blocking to block attacks like prompt injection and malicious code. And, E – Ecosystem Observability where customers can plug Glean into their broader security stack without losing the logging, auditability, and control they need to govern AI with confidence.
With AWARE and Glean Protect, you don’t have to choose between agents and security.
Want to see it in action? Watch the
Security Showcase
, and sign up for a
demo
today to learn more about Glean.
Feature availability: Many of these capabilities are now generally available, including out-of-the-box sensitive content policies, Tines SOAR remediation runbooks, customer-managed deployment model, private connectivity, and customer-managed keys. Certain capabilities, including restricted topics policies, agent alignment models, fine-tuning sensitive content models in natural language, triage workflows for sensitive findings, Cortex Cloud DSPM, and Glean directly embedded in Prisma browser are currently in beta.
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
