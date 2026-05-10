---
title: "How Glean scales monitoring capability in the cloud"
source: "Glean Blog"
url: "https://www.glean.com/blog/how-glean-scales-monitoring-capability-in-the-cloud"
scraped: "2026-05-10T01:20:37.907534+00:00"
lastmod: "None"
type: "sitemap"
---

# How Glean scales monitoring capability in the cloud

**Source**: [https://www.glean.com/blog/how-glean-scales-monitoring-capability-in-the-cloud](https://www.glean.com/blog/how-glean-scales-monitoring-capability-in-the-cloud)

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
How Glean scales monitoring capability in the Cloud
0
minutes read
Gary Luo
Engineering
Connor Lafferty
Engineering
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
Glean uses a single-tenant model to provide dedicated GCP projects for each customer, ensuring the best possible security experience while facing challenges in monitoring and operating multiple projects.
The Notification Dispatcher tool was developed to manage GCP alert notifications and Error Reporting errors, integrating with Slack, Jira, and OpsGenie to make information searchable and shareable.
Advanced features of the tool include incident and error deduplication, notification silence, frequency control, suppression, and auto escalation, significantly improving productivity and focus on important production issues.
Glean
uses a single-tenant model (providing every customer a dedicated GCP project) to deploy our services and provide the best possible security experience. One big challenge we face, however, is monitoring and operating multiple GCP projects as our customer base grows. Multiple alerts for separate GCP projects can fire simultaneously, making it a challenge to manage.
Google’s
Error Reporting
faces the same issue – where the same application exception may happen in multiple GCP projects at the same time. In this post, we’ll discuss how we use our Notification Dispatcher tool to scale our monitoring ability in Cloud.
Main Challenges
In order to manage multiple GCP projects effectively, we need to maintain a global view of alert notifications and application exceptions across all our GCP projects. This helps us to understand how widely a production issue has spread globally, and allows us to triage production issues in an efficient way.
Cloud Monitoring Alerting
supports many different types of notification channels, but it lacks Jira support. Error Reporting didn’t support notifications when the Notification Dispatcher tool was developed. Since Glean is a search-oriented company, we want to connect these important GCP production-related services to other SaaS applications like Jira – and more importantly, make the information searchable and turn resolutions into shareable knowledge.
On top of that, we develop many home-grown features that enable us to manage the same issues for multiple projects together.
Introducing Notification Dispatcher Tool
Notification Dispatcher is the internal tool at
Glean
for managing GCP alert notifications and Error Reporting errors. It is integrated with Cloud Monitoring and Error Reporting as the notification source, and is integrated with Slack, Jira, and OpsGenie as notification destinations.
This tool has a few components:
Error Reporting Crawler:
An App Engine Flex service that sends
Error Reporting API
calls to crawl errors from all our GCP projects. In order to obey Error Reporting API
quotas
, we use an App Engine Task Queue to crawl errors in a batch fashion.
Alert Notification Receiver:
Implemented as an App Engine Flex service that watches a PubSub channel for alert notifications. All of our alert policies have the PubSub channel added as their notification channel.
Notification Policy Rules:
A text proto file where Glean engineers can specify how to match alert incidents or errors and forward them to which SaaS application(s).
States Database:
A Cloud SQL database that stores the collected alert incidents, Error Reporting errors, and their dispatching states.
Notification Dispatcher:
The execution engine that processes all the notifications and dispatches them according to the notification policy rules. It is implemented as a shared client library which is compiled into both the Error Reporting Crawler and the Alert Notification Receiver Flex services.
Advanced Features
We’ve built some other cool features that enable us to scale operations in the Cloud:
Jira Integration:
Glean engineers can use the tool to specify which Jira components and which Jira priorities are to be used for creating new Jiras when alert incidents or Error Reporting errors are received. As Glean indexes our Jira instance, all the alert incidents, and errors become searchable.
Incident and Error Deduplication:
Notification matching rules are very flexible and support regular expressions, which allows Glean engineers to deduplicate the same alert incidents or errors without spamming engineer teams. This is especially important when there is a page storm or the same issue happens in multiple projects at the same time.
‍
Notification Silence:
We developed this feature before GCP introduced the
Notification Snooze
Pre-GA feature. It even allows Glean engineers to silence alerts by alert incident labels, or silence alerts for a whole project.
‍
Notification Frequency Control:
Glean engineers can specify how frequently they want to receive updates to the specified notification destinations. This prevents alerts from generating updates too often.
‍
Notification Suppression:
This feature is normally used when an alert incident with a higher severity is fired, we want to suppress a relevant alert with lower severity.
‍
Notification Auto Escalation:
Glean engineers can use this feature to raise OpsGenie or Jira priorities when the specified criteria are met. This normally means an issue has been widely spread and requires immediate attention.
‍
Error Grouping:
We introduced an error fingerprint similar to how GCP Error Reporting
grouped errors
. This useful technique allows us to group GCP errors across multiple projects. Besides that, Glean engineers can use notification policy rules to match errors by exception message, frame, or stack trace across all of our programming languages.
Takeaways
The Notification Dispatcher tool has improved our productivity dramatically since it was launched. It provides a mechanism for our engineers to consolidate production signals from all of our GCP projects and focus on important production issues. Once those notifications are forwarded to Jira or Slack, engineers can
Glean
the information and turn the resolutions or discussions into knowledge.
If you’d like to get hands-on with scaling our operations in the Cloud, check out our
careers page
– or schedule a
demo
to discover what Glean can do for you.
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
