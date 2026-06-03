---
title: "Query Snowflake Data with Glean Assistant"
source: "Glean Blog"
url: "https://www.glean.com/blog/query-snowflake-data-in-glean-assistant"
scraped: "2026-06-03T06:00:32.910439+00:00"
lastmod: "None"
type: "sitemap"
---

# Query Snowflake Data with Glean Assistant

**Source**: [https://www.glean.com/blog/query-snowflake-data-in-glean-assistant](https://www.glean.com/blog/query-snowflake-data-in-glean-assistant)

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
Finance
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
Professional
Services
Consulting
Construction
IT Services
Legal
Scroll for more
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
Finance
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
Professional
Services
Consulting
Construction
IT Services
Legal
Scroll for more
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
Last updated Jun 02, 2026.
Introducing Snowflake in Glean Assistant — and Why Glean Was Named 2026 AMER Snowflake Product Innovation Partner of the Year
0
minutes read
Kelly Huang
Product Marketing Manager
Aditya Sharma
Product Manager
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
Glean Assistant now allows employees to query Snowflake data using natural language without needing SQL expertise or switching between tools
The integration uses Snowflake Cortex Analyst to combine structured data queries with unstructured enterprise knowledge for highly contextual answers
The platform respects existing permissions and governance models to ensure self-serve data access remains fully secure and accurate
‍
Most organizations have invested heavily in becoming data-driven. They've built data warehouses, built data teams, and standardized on tools like Snowflake to store and govern their most valuable structured data. However, data accessibility still remains out of reach for most employees. They need proficiency in SQL, someone with technical expertise, or a dashboard that can answer their specific question.
At Glean, we believe every employee should be able to ask a question in natural language and quickly receive an accurate, governed answer, regardless of where that data lives. We've spent the past year building toward this: first enabling Glean Agents to query Snowflake data in automated workflows, then becoming a launch partner for Snowflake Intelligence so data teams could bring Glean context into Snowflake.
Today, we’re excited to announce Snowflake in Glean Assistant is generally available, enabling any employee to query Snowflake data directly from Glean Assistant, with no agent to build, no tool to switch, no ticket to file, and no SQL required.
We are also proud to announce that Glean has been named the 2026 AMER Snowflake Product Innovation Partner of the Year. This award reflects a simple idea: your company’s most important data should not be locked behind SQL, dashboards, or a queue of reporting requests. It should be available to the people who need it, when they need it, in the tools where they already work. That is the opportunity Glean and Snowflake are unlocking together.
What's new: Snowflake in Glean Assistant
Snowflake is now available as a native data source in Glean Assistant. Employees can ask questions in plain English and receive answers grounded in live Snowflake data, combined with the full context of your company's knowledge across documents, tickets, chats, and more.
Under the hood, Glean Assistant leverages Snowflake Cortex Analyst and Cortex Agent’s powerful text-to-SQL capabilities to translate natural language into precise Snowflake queries, then combines those structured results with unstructured context from across your enterprise. The result is an answer that's both numerically accurate and contextually rich.
‍
Let’s assume a sales leader needs to know
“how many defects were detected last month?”
Snowflake returns the production line data while Glean provides the call transcripts, support tickets, and opportunity notes from your CRM. Glean now combines your structured and unstructured data in one place, making it easy to understand the “why” behind the “what.”
Snowflake in Glean Assistant is built on enterprise-grade trust where every answer respects existing permissions and governance. Glean returns only what each user is authorized to see, with citations and links back to source documentation. Snowflake's governance model and Glean's permission-aware retrieval work together to ensure that self-serve data access doesn't mean unsecured data access.
How your teams can unlock data analytics
As our Snowflake partnership has expanded, we've built distinct experiences for different users at different points in their data journey. Here's how to think about which experience is right for your team:
Business users and everyday employees :
Ask your Snowflake questions directly in Glean Assistant, where structured data answers are enriched with your company's full knowledge context. No SQL required. No context switching. The answer comes to you.
Data users who live in Snowflake :
Snowflake Intelligence
now surfaces Glean as an MCP tool, so your Cortex Agents can pull in permission-aware enterprise context — the "why" behind the "what" — without leaving the Snowflake environment.
Builders and workflow architects :
Glean Agents
remain the right choice for multi-step automation that incorporates Snowflake data at any step — from deal-risk monitors to weekly business review agents to customer health scoring workflows.
Each path shares the same underlying context layer and the same governance model. You don't have to choose between access and control.
Single interface with full context, for immediate action
The deeper ambition behind today's launch is about more than connecting one more data source. It's about eliminating the fragmentation that defines how most people work with information today. The data is in Snowflake, the context is in Confluence or Google Drive or Gong, and the next step is in Jira or email or Slack. Getting from question to answer to action requires moving between all of them and employees don’t have excess time for context switching.
Instead of teaching employees where to go for data, where to go for company context, and where to go next to act on the answer, Glean brings those together in one place. Ask your question, get a grounded, contextualized, permission-aware answer, and act faster without interrupting your workflow.
Get started
Snowflake in Glean Assistant
is available now for joint Glean and Snowflake customers. Reach out to your Glean account team to enable the integration, or
get a demo
to see it in action.
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
French (France)
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
Enterprise AI Software
AI Agent Builder
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
