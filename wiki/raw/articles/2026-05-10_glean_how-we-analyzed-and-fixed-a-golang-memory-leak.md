---
title: "How we analyzed and fixed a golang memory leak"
source: "Glean Blog"
url: "https://www.glean.com/blog/how-we-analyzed-and-fixed-a-golang-memory-leak"
scraped: "2026-05-10T01:27:46.295730+00:00"
lastmod: "None"
type: "sitemap"
---

# How we analyzed and fixed a golang memory leak

**Source**: [https://www.glean.com/blog/how-we-analyzed-and-fixed-a-golang-memory-leak](https://www.glean.com/blog/how-we-analyzed-and-fixed-a-golang-memory-leak)

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
How we analyzed and fixed a Golang memory leak
0
minutes read
Sharva Pathak
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
Glean identified a memory leak issue in their Golang service running on Google Cloud Platform, which caused the memory to ramp up and instances to get killed.
They used continuous profiling data and MemStats logging to determine that the issue was related to Golang's use of MADV_FREE, which did not return memory to the OS immediately in container environments.
By setting the GODEBUG environment variable to "madvdontneed=1", they resolved the issue, leading to a stable memory footprint and improved performance.
At
Glean
we’re building modern cloud-only architecture for solving some
hard enterprise search
and knowledge management-related problems. Performance and resource cost optimization is critical and often leads us into interesting technical challenges. Debugging one of these challenges led us to an interesting discovery that may be useful for others working on similar challenges.
At Glean, we use Golang for a moderately memory-intensive service. We also use Google Cloud Platform (GCP) for most of our deployment. We run this service as an app engine flexible instance using a
custom runtime
image that includes Go 1.15. We saw the following interesting behavior in our Golang service:
The memory would slowly ramp up, reach the limit (we were using 3GB as the AppEngine resource limit in this case) and then the instance would get killed, likely because it was exceeding the memory limit. Looking at the memory graph, the steady ramp-up smelled like a memory leak:
‍
Not an application memory leak
Thankfully, a memory leak on the application is not hard to debug in our case since we have access to continuous profiling data using the
cloud profiler
. In the past, we have seen cases of unclosed Google Remote Procedure Call (gRPC) connections causing such issues, but those were easy to debug using the continuous profiler. In particular, the
flame graph
in the profiler UI would clearly show heavy usage at a specific call site in such cases. In this case, that was not happening. One interesting thing the profiles revealed though was that the average heap size (i.e. by the in-use objects) was around 1.5G (i.e. ~2X less than the memory footprint app engine was seeing). This meant the memory was being held somewhere by the Golang runtime. The immediate next thought we had was whether this was a memory fragmentation issue because Golang is
known to be bad
in that aspect.
Not a fragmentation case
Luckily it wasn’t too hard to conclude that fragmentation was not the culprit either. We added a background thread that periodically logs the
MemStats
. An upper bound on fragmented memory can be easily obtained by subtracting HeapAlloc from HeapInuse. In particular, “HeapInuse minus HeapAlloc estimates the amount of memory that has been dedicated to particular size classes, but is not currently being used.” This amount was fairly small, ~3MB in our case.
It was also interesting to see that the values for HeapReleased were fairly large. We started looking more and came across
this thread
on similar issues.
{{richtext-banner-component}}
Golang / container environment interaction issue
The potential theory in the
Golang issue thread
is that Go started using MADV_FREE as the default in go 1.12. This meant it might not return the memory immediately to the OS, and the OS could choose to reclaim this memory when it felt memory pressure. However, if you go back to
how containers are implemented
, these are essentially just processes running under separate Cgroups. The OS, therefore, might not feel the memory pressure and will not free up the memory even though the container might hit the memory limit and get killed.
Fortunately, there’s a Golang debug flag to flip this behavior and use MADV_DONTNEED instead, by setting the
GODEBUG
environment variable to “
madvdontneed=1
”. In fact, go 1.16 has
reverted to using this
as the default now. The memory graph after this change looks much better and steady at 2G.
‍
Key takeaways
pprof
and flame graphs are pretty useful to analyze application memory leaks. A continuous profiler can really help you look at multiple snapshots of the profile and quickly figure out the cause of leaks.
Cloud profiler
is definitely a handy tool for GCP workloads.
MemStats logging can help analyze potential causes at a higher level. In particular, “HeapInuse minus HeapAlloc” can be used as an upper bound when estimating the amount of memory wasted fragmentation.
If you are using go between 1.12 to 1.15 within containers, you likely want to set
madvdontneed=1 in GODEBUG.
:-)
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Integrating LLMs and GPT into enterprise workflows
Discover in our white paper how improvements to generative AIs brought them to the forefront of modern workplace transformation – and how best to integrate them into several key areas of enterprise business.
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
