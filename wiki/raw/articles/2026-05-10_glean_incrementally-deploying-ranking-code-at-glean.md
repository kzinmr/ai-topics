---
title: "Incrementally deploying ranking code at Glean"
source: "Glean Blog"
url: "https://www.glean.com/blog/incrementally-deploying-ranking-code-at-glean"
scraped: "2026-05-10T01:20:47.649703+00:00"
lastmod: "None"
type: "sitemap"
---

# Incrementally deploying ranking code at Glean

**Source**: [https://www.glean.com/blog/incrementally-deploying-ranking-code-at-glean](https://www.glean.com/blog/incrementally-deploying-ranking-code-at-glean)

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
Incrementally deploying ranking code at Glean
0
minutes read
Jeremy Lilley
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
Glean implemented a mechanism to dynamically load new code versions without restarting their Index Server, allowing for more frequent and less disruptive releases.
They used custom ClassLoaders and remapping tools to load multiple versions of code dynamically from Cloud Storage, facilitating experimentation and strong versioning.
This approach has led to faster incremental deployments, reduced server restart times, and improved flexibility in iterating on the Glean service.
In
Glean
search, we’re always trying to return the most relevant results. When we merge results from a variety of sources—from Slack threads to Jira bugs to O365 docs—there are many dimensions in which to experiment with our ranking functions.
To help build these features, we wanted frequent iterative releases for our ranking team. But rapid turn-around can be tricky in the context of a stateful service. Particularly, our main Index Servers need to preload significant amounts of index data into memory when they restart. In many cases, preloading this data could take 15+ minutes, which required either scheduled service downtime or somewhat involved mitigation.
In practice, with this constraint, we found we weren’t deploying customer updates as often as we wanted. And our engineers found that their development cadence was unnecessarily slowed down by long server restart times.
How did we fix this problem, and move towards faster incremental deployment?
We realized that much of the problem was solved if we could avoid restarting our Index Server to receive code updates in the common case.
Fortunately, this particular server was written in Java, which has a mechanism for dynamically loading code. After looking into custom ClassLoaders, we prototyped loading a Java JAR archive from Cloud Storage and using the classes in our process, without a restart.
Even with the ability to load code from Cloud Storage without restarting, Java only allows a single implementation for a given class name. That said, we realized we could add the release tag to our class package names. For instance, for the class
com.glean.ranking.TermInfo
,
we could load any number of versions in the server if we wrote a tool to rewrite and put the release tag in the name:
com.glean.ranking.release123.TermInfo, com.glean.ranking.release124.TermInfo, etc
. We used some open source libraries (e.g. ObjectWeb ASM) to help build this remapping tool. In the end, we had a script to remap the build artifacts for a specified release tag and upload to the cloud in seconds.
With the ability to load multiple versions of code dynamically from Cloud Storage, it was then a matter of plumbing these release tags through the system, so that the correct release or experiment was being used for a given query.
‍
We soon found the advantages of this approach:
More frequent, less disruptive releases: Since server restarts were no longer normally needed, we started rolling out ranking changes more frequently—nightly for internal deployment, and weekly for customers.
Experimentation: We also started using this mechanism for developer experiments; rather than coordinating use of a development cluster and waiting for a server restart, they could just upload a Jar file and quickly see the results.
Strong versioning: Errors could be associated with specific release tags, and different experiments were isolated from each other.
Rolling back support: Rolling back a problematic release could be done instantly with an online configuration change.
Like in any implementation, there was some tuning needed to make the mechanism work well. For instance:
Deciding which sets of packages to remap (the initial version didn’t remap some protobuf packages, which we quickly realized was a mistake!)
Caching/loading appropriately to avoid duplicate Jar file scans
Suppressing parallel fetches for the same classes
We found that the initial use of a given release tag has an additional latency of about a second, given the Cloud Storage retrieval and Jar decoding overhead, but that subsequent uses are cached and indistinguishable from a regular implementation. Hence for production releases, we typically send a warmup request before switching the configuration.
That said, the ability to dynamically load new releases and experiments without restarting a stateful service gives us some great flexibility and ability to iterate on improving the Glean service.
If
building
or
using
a best-in-class search product sounds interesting to you, reach out!
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
