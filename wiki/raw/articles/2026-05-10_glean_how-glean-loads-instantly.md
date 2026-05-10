---
title: "Know how Glean helps search load instantly"
source: "Glean Blog"
url: "https://www.glean.com/blog/how-glean-loads-instantly"
scraped: "2026-05-10T01:27:41.682420+00:00"
lastmod: "None"
type: "sitemap"
---

# Know how Glean helps search load instantly

**Source**: [https://www.glean.com/blog/how-glean-loads-instantly](https://www.glean.com/blog/how-glean-loads-instantly)

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
How Glean loads instantly - Glean
0
minutes read
Tony Gentilcore
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
Glean optimized their search load times by using Service Workers to load pages from cache and redux-persist to cache preferences locally, avoiding server round trips.
They implemented render caching by pre-rendering HTML pages and storing them in the Service Worker, allowing for immediate display without JavaScript execution.
These techniques, including contributions to open source tools, resulted in significantly faster load times and improved user experience.
At
Glean
,
Speed
is our favorite
feature
. Unlike some companies, we’re unencumbered by any motivation to hold people’s eyeballs as long as possible just to show them ads. We’re free to optimize for helping people and teams find what they need and get out as fast as possible, so they can get big things done.
One of the quickest ways to find things with Glean is via its New Tab Page. It’s personalized and customized by each user – the layout, background, favorite sites, and suggested documents. Even with all this dynamic content, everyone expects a new tab to open immediately, with no perceptible delay. That presented a fun challenge for our
engineering team
– one that required a novel solution.
Take a look at the result in this video. This technical post explains how we did it.
‍
‍
Step 1 - Service Worker
When a web browser loads a page, it first has to fetch all of its resources. Historically this required several seconds of waiting for the network.
Service Workers
have changed that entirely. So, the first thing we did was to set up
Workbox
, an excellent open source framework which makes it simple to create a Service Worker that loads your page entirely from cache, even when offline.
Step 2 - Redux-Persist
Now that loading our code and resources was fast, the next problem was that it still required a round trip to the server to fetch the preferences. To avoid this, we cached everything locally to IndexedDB using
redux-persist
.
This seemed to work at first, but caused all kinds of performance issues in the app, especially for machines under load. Luckily, two of the founding members of Google’s Chrome Speed Team now work at Glean so we knew the tool to debug -
Chrome Tracing
. It uncovered that, by default, Chrome waits to flush all IndexedDB writes to disk via an fsync. Some browsers like Firefox do not, but at least Chrome gave us a tool to avoid it –
relaxed durability
. So we wrote our own redux-persist backend and also contributed a fix to Workbox. Now filesystem operations no longer get pathologically backed up.
Step 3 - Render Caching
Even though our caching was complete and efficient, it still wasn’t fast enough. The browser was still spending several hundred milliseconds compiling our JavaScript and bringing up React for that first render. So we had to think out of the box by taking a cue from
Server Side Rendering
. This is a technique to render a DOM on the server and ship its HTML to the browser so that it can present it immediately with only CSS/HTML parsing and layout while React is loading.
The insight was that this could also work for a page dynamically built on the client. After it loads, we snapshot the DOM’s HTML and persist it to the Service Worker so that upon the next load, there’s already a pre-rendered HTML page in the cache that requires no JavaScript in order to be displayed. The details are esoteric. They required some careful considerations in order to avoid pitfalls like clearing search inputs, improper hydration and avoiding staleness.
But the end result speaks for itself. As far as we can tell, this is a novel technique. If there’s interest, we’d be happy to open source a generalized Workbox plugin.
What’s Next?
We’re hoping you know! Interested in solving fun challenges like this and pushing the web platform to its limits with us? Check out our
careers
page.
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
