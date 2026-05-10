---
title: "How we migrated 150 cloud SQL instances using GCP DMS"
source: "Glean Blog"
url: "https://www.glean.com/blog/how-we-migrated-150-cloud-sql-instances-using-gcp-dms"
scraped: "2026-05-10T01:27:46.478114+00:00"
lastmod: "None"
type: "sitemap"
---

# How we migrated 150 cloud SQL instances using GCP DMS

**Source**: [https://www.glean.com/blog/how-we-migrated-150-cloud-sql-instances-using-gcp-dms](https://www.glean.com/blog/how-we-migrated-150-cloud-sql-instances-using-gcp-dms)

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
How we migrated 150 Cloud SQL instances using GCP DMS
0
minutes read
Satyam Shanker
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
Glean migrated from MySQL5 to MySQL8 for their Cloud SQL instances using GCP DMS, motivated by performance improvements, especially for JSON operations.
The migration involved creating new MySQL8 instances, copying large amounts of data, and ensuring minimal service disruption by using continuous migration jobs and an asynchronous operations framework.
The migration resulted in significant performance gains, including reduced CPU usage, lower disk read I/O, and better query caching, despite challenges like replication lag and large initial dump times.
Our Cloud SQL instances are a central part of the
Glean
index building architecture. Among other things, they serve as a repository for all our crawled data which eventually makes its way to the served index. They also store other information like
answers
created by Glean users. When we started Glean, we saved all this in Google Big Table, but later moved it to Cloud SQL due to cost considerations. Historically, all our Cloud SQL instances were MySQL5 instances. We decided to migrate these instances to MySQL8 recently after GCP started supporting MySQL8.
Motivation
‍
In addition to using the latest and greatest version, the main motivation behind moving with the migration were the JSON improvements introduced as a part of
MySQL8
. Before MySQL8 we had cases where some upgrades took close to 48 hours to complete as some Alter Table commands operating on the JSON columns took a long time. We believed using MySQL8 would enable us to significantly speed up such operations as we might be able to update JSON in place.
Main challenges
Since this was a major version upgrade we would need to create a completely new MySQL8 instance and then copy over the data from the old instance. The size of this data that needed to be copied over was quite large in some of our deployments running into TBs.
While the copying of the data was being done, the source DB needed to be available for regular operation.
Depending upon how our services connected to the DB, eventually when we switched from the old DB to the new DB, some services would need to be restarted, while some services would need to be redeployed. We also implemented some services to detect the change in the GCP connection settings and thereby refresh their in memory SQL connection pools, thereby eliminating the need for a restart or redeploy.
Since the switch could mean redeployment of some services, this needed to happen under someone’s supervision. Also this meant that it could only happen when the customer load on the system was low.
Using GCP DMS
Given the above constraints, we decided to use GCP DMS to migrate our DBs from MySQL5 to MySQL8. DMS is a Google recommended service when moving SQL workloads from other infrastructure to Google managed cloud SQL instances. We decided to use the
continuous
type of migration jobs which use an initial dump phase and then use primary secondary replication in the CDC phase. We monitored the replication lag and when the replication lag was low, we were ready to switch from the old instance to the new instance. While this condition may be satisfied at any time of the day, we switched the instance only during nights and weekends so that customer service disruption was minimized.
Asynchronous operations framework
‍
Historically our upgrades were run by the
push_master
who is continuously monitoring the upgrades. They mostly run for a period of 2 hours. However given the large data size (point 1 above), the SQL upgrade was expected to run for many days. Also we had to upgrade close to 75 projects with 2 cloud SQL instances each which would mean a manual upgrade cumbersome. We decided to implement what we call the
AsynchronousUpgradeframework
to solve this issue.
At a very high level, this is a state machine. The current state of the upgrade is stored in a GCS bucket in a file called the state file. There is a periodic tick that comes in, loads the state file and sends GCP queries to look into the current state of the migration. Then depending upon these 2 inputs the state machine may update the state, and take some action. One example of this can be, the current state of migration jobs is running, we look into the replication lag and it’s quite high so we stay in the same state. However, in the case the replication lag is found to be low, and the use of the system is low (point 4 above), we decide to make a state transition by patching the new instance, switching it and triggering the restarts and redeployments.
All the operations performed by this framework need to be idempotent in case there are intermittent issues. Hence they need to leave the system in a consistent state for the next tick.
Gains using MySQL8 vs MySQL5
While a detailed comparison of the performance of MySQL8 vs MySQL5 for the Glean workloads could be the topic of a separate post, some early indications include:
Significant gains in the CPU for the same workload. For example in one case the CPU was around 30% where it initially hovered around 50%.
Lower disk read I/O.
Memory utilization seems to be similar. We think that MySQL tries to keep the memory at around 85% of the available memory.
We also saw much better caching of similar queries.
Some learnings
‍
Over the course of the project we learned many things.
It is difficult to lower the replication lag quickly if there is high load on the source DB. We initially decided to let the source DB run at full throttle when the replica was catching up. We assumed that tuning the parameters for parallel replication and transaction commits semantics we would be able to bring the lag down. However we quickly realized that it was not working for our case. We had to pause the activity on the source DB.
Large initial dump time: If the data is concentrated in a few tables in the source DB then the initial dump would be very long. We had a case where about 90% of the data was in one table in a specific project. In our first attempt the initial dump took more than 7 days. Since the maximum replication log retention on the source could be 7 days, the job would never get the correct updates. Luckily we were able to ignore some of this data using dumpFlags and then recrawl it once the switch to the new instance happened.
Scaling with the current model where we have a separate GCP project for each customer can be tricky for future migrations. We should move to multi-tenant architecture where we have single projects for more customers.
‍
‍
If
building
or
using
a best-in-class search product sounds interesting to you, we’d love to talk with you!
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
