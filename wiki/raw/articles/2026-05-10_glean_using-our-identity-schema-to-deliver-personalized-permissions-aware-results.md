---
title: "Using our identity schema to deliver personalized results"
source: "Glean Blog"
url: "https://www.glean.com/blog/using-our-identity-schema-to-deliver-personalized-permissions-aware-results"
scraped: "2026-05-10T01:28:05.520293+00:00"
lastmod: "None"
type: "sitemap"
---

# Using our identity schema to deliver personalized results

**Source**: [https://www.glean.com/blog/using-our-identity-schema-to-deliver-personalized-permissions-aware-results](https://www.glean.com/blog/using-our-identity-schema-to-deliver-personalized-permissions-aware-results)

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
Using our identity schema to deliver personalized, permissions-aware results
0
minutes read
Shreya Shekhar
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
Glean's identity schema ensures users see the most relevant and permission-aware search results by fitting users into groups and memberships, respecting each connector's permissions model.
Optimizing the Salesforce connector's identity crawl improved crawl times by up to 98% for some customers, enhancing the efficiency of querying and indexing SaaS applications.
The improvements in identity crawl times and filtering out fake or stale users are crucial for maintaining up-to-date and accurate search results, contributing to a better user experience.
As an intern at
Glean
this past summer, I worked on many impactful projects on our backend Connectors team. Our team works on efficiently querying and indexing everyday SaaS applications, such as Slack, Jira, Confluence, and so on. These projects allowed me to contribute to our backend infrastructure to help serve queries for applications such as Greenhouse and Salesforce, and get a detailed understanding of how Glean keeps information as up-to-date as possible.
Working as an engineer on the Connectors team exponentially increased my learnings in such a short time, and really resonated with my idea of what an ideal internship should be. Learning from and bonding with such close-knit coworkers made the internship fulfilling, and helped me understand what I believe is important in my career going forward. This brings me to an important concept here at Glean: identity.
Identity is the core concept behind what a user sees on their Glean homepage every day, and what they see in all of their search results. Being the powerful
search
tool that Glean is, it’s imperative that users be able to see results most related to their job, and only ones that they are allowed to see. Respecting the permissions model of each connector is an important challenge we tackle in the backend, especially since these permissions can be changed at any time! We incorporate these permissions through periodic crawls, and by fitting users into our own identity schema of groups and memberships.
Given that these connector applications serve large companies with hundreds of thousands of users, sometimes these crawls can take exceptionally long to complete, especially for complex permissions models. One such project involved our Salesforce connector, and its incredibly inefficient identity crawl.
Salesforce crawl: the problem
When performing identity crawls for connector applications, many steps are involved, such as crawling users, groups, and members, and making API requests in order to verify permissions at each of these stages.The crawl speed is determined by the rate at which we can make these requests, and how many of them we have to make.
In Salesforce’s case, the crawl was being limited by both of these factors, and my job was to investigate how to optimize it.
Our solution
After meticulously documenting our current crawl structure, I was able to put together a plan for optimization based on the different steps which did and did not require API calls. Salesforce in particular has a large number of different permissions groups, based on documents, document types, profiles, networks, roles, and more. Not all of these groups, however, require the use of API calls to be created, since some are internal groups which we use to filter results for Glean users.
By executing tasks which did not require them concurrently, and at a faster pace than API related tasks, I was able to gain up to a 98% identity crawl time improvement for one of our customers, and at least a 22% improvement for some others! Furthermore, I implemented filtering based on user domains in order to ensure there were no fake or stale users included in the identity crawl. These kinds of improvements are crucial in an early and ever-evolving system like ours.
Working on interesting problems like this throughout my internship made the experience unparalleled. If
building
or
using
a best-in-class search product sounds interesting to you, reach out!
Author:
Shreya Shekhar, software engineering intern
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
