---
title: "Glean: efficiently reading MySQL with Apache Beam streaming"
source: "Glean Blog"
url: "https://www.glean.com/blog/how-glean-uses-apache-beam-streaming-to-efficiently-read-a-large-corpus-from-mysql"
scraped: "2026-05-10T01:27:42.122593+00:00"
lastmod: "None"
type: "sitemap"
---

# Glean: efficiently reading MySQL with Apache Beam streaming

**Source**: [https://www.glean.com/blog/how-glean-uses-apache-beam-streaming-to-efficiently-read-a-large-corpus-from-mysql](https://www.glean.com/blog/how-glean-uses-apache-beam-streaming-to-efficiently-read-a-large-corpus-from-mysql)

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
How Glean uses Apache Beam Streaming to efficiently read a large corpus from MySQL
0
minutes read
Varshaa Naganathan
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
Glean uses Apache Beam Streaming on Google Cloud Dataflow to efficiently read and process a large corpus of documents from MySQL, ensuring content, permissions, and statistics are kept up-to-date.
The streaming pipeline setup allows for scalable and cost-effective processing, handling hundreds of documents per second on a single core by maintaining a cache of documents and issuing parallel database reads.
This approach has enabled Glean to deliver a better search experience by ensuring that documents are processed in real-time and re-processed periodically to handle any changes or dropped events.
At Glean, we crawl corpuses of hundreds of millions of documents every day. Once all these documents are crawled, we need to ensure they are constantly parsed and processed to keep content, permissions, and statistics fresh in order to deliver the best possible search experience.
Running a batch job for this purpose was costly, fragile, and difficult to integrate with MySQL. With a streaming job, however, we were able to re-process every document at least once a day. In this blog post, we describe how this was achieved using Cloud SQL (MySQL) and Apache Beam on Google Cloud Dataflow. All the pipelines described henceforth use a single worker, multi-core setup on Google Cloud Platform (GCP) which provides massive vertical scalability which is sufficient for our use cases.
On crawling a new document, the raw content is written to a MySQL table. We also maintain a Pub/Sub queue that is notified with the unique ID of the newly crawled document. This document needs to be processed to parse and extract structured information which is written back to the same MySQL table and indexed by our search system. The Pub/Sub queue ensures this is done in real time. Documents also need to be re-processed periodically to handle any events dropped by the Pub/Sub queue and to re-compute any statistics that change as the corpus evolves over time. This is achieved by continuously scanning and re-processing data from the MySQL table. In the rest of this blog post, we will mainly focus on how the system reads and processes data from MySQL.
To read documents from the MySQL table we use a streaming pipeline. Two main factors influenced our choice of streaming over batch – scalability and cost. With an ever growing corpus, a weekly batch job was not scalable and using a streaming pipeline enabled us to process each document at least once a day. A significant portion of this cost benefit came from the fact that we already needed to maintain a streaming pipeline to handle the Pub/Sub queue. Those machines were being underutilized and hence could be used to perform a streaming scan on the MySQL database at no additional cost.
Figure 1: Pipeline Architecture
‍
Figure 2: Document processing rate on a single core
‍
To set up a streaming pipeline (See Figure 1), we use Apache Beam with the Google Cloud Dataflow runner. We define a custom UnboundedSource, each instance of which creates a custom UnboundedReader that queries a cache of documents to fetch the next document that should be processed. This cache of documents is maintained by a static instance of a scanner object. Several parallel database reads are issued by this scanner to the MySQL table based on the number of cores in the worker in use. These reads fetch documents in batches ordered by document ID to ensure each document is processed at most once in each full scan of the corpus. With this setup, we achieve processing rates on the order of hundreds of docs per second on a single core (See Figure 2).
The scanner also keeps track of the cache state - the ID of the last document read, the number of documents left in the cache etc. It uses these to determine when to fetch additional documents as well as to determine when a full scan over the corpus is complete. Then it resets its state and starts scanning the corpus from the beginning again. Thus, this sets up an infinite queue of data for our streaming pipeline.
This design and optimizations process have made it possible to ensure that we are scalable and cost effective from our smallest to our largest customers. We are constantly iterating to ensure our users can find the documents they need, when they need them to get things done at work.
We’ll go into the details of additional SQL queries and optimizations in an upcoming blog, so stay tuned! If you found this blog post interesting and would like to work on such systems please
reach out
!
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
