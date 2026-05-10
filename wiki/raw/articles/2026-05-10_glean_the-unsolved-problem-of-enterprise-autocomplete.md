---
title: "The unsolved problem of enterprise autocomplete"
source: "Glean Blog"
url: "https://www.glean.com/blog/the-unsolved-problem-of-enterprise-autocomplete"
scraped: "2026-05-10T01:28:00.979563+00:00"
lastmod: "None"
type: "sitemap"
---

# The unsolved problem of enterprise autocomplete

**Source**: [https://www.glean.com/blog/the-unsolved-problem-of-enterprise-autocomplete](https://www.glean.com/blog/the-unsolved-problem-of-enterprise-autocomplete)

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
The unsolved problem of enterprise autocomplete
0
minutes read
Shivaal Roy
Engineering
Ayushi Mrigen
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
Glean's Autocomplete feature aims to provide near-zero delay suggestions by surfacing various content types like query suggestions, documents, and structured results, enhancing user experience.
The team focuses on mining queries from indexed documents and predicting user needs to offer relevant document suggestions, addressing challenges like privacy, translation, and ranking of queries.
Continuous improvements in Autocomplete systems have led to significant reductions in user friction, with a notable percentage of result clicks coming from Autocomplete suggestions.
Autocomplete is an assistive search feature for getting users where they’re trying to go,
faster
, by suggesting potential queries or documents for a user to jump directly into as they form their query. Glean is able to surface many different types of content, such as query suggestions, documents, operators, and structured results, like people and teams, with each content type giving the user a unique modality for expediting their search.
No matter what we display in the dropdown, one thing is constant – we want to surface these results to the user as they type with near-zero delay. Since we can’t just run a search after every keystroke (as it would not meet our near-zero latency requirement), the
Glean
Search Features team has built out Autocomplete from the ground up to ensure a snappy experience. Today, Autocomplete already helps to lower our average time to satisfaction by 40%. This blog post will discuss the technical challenges associated with making fast and useful suggestions, wins we’ve had to-date, and active areas of development for the team.
Developing query suggestions for “small data”
Suggesting potential queries as a user types is the most familiar form of autocomplete on the open web. Query suggestions can help the user in two ways: 1) save the user time by not having to type out their full query, and 2) help the user formulate a (better) query that’s more likely to land them the information they’re ultimately seeking.
A standard practice among public search engines is to leverage sheer query volume to generate query suggestions. For example, an engine might mark a query as a public suggestion once it’s been issued by 100K+ unique users, a fairly reasonable threshold when the engine has 100M+ users.
Unfortunately, the same technique applied to the enterprise setting will fall short. Most companies have far fewer than 100K employees total, and enterprise queries are empirically ~3x less likely to be repeated compared to the public web. Though it’s certainly possible to generate suggestions from lower query volumes, the system will not be able generate as many high-quality query candidates, which, at worst, could even result in privacy-violating suggestions. Each launch with a new customer, moreover, would suffer from the “
cold start problem
”: such a system will not yet have sufficient information about user behavior to draw useful inferences.
We at Glean have instead focused our efforts on mining queries from already-indexed documents. Though this approach circumvents some of the issues discussed above, it does not come without challenges. First, mined queries need to be permission-aware so that no sensitive information is leaked. Furthermore, language used in a document doesn’t necessarily make for a good query, so document language must be translated into a query space. And finally, the mined queries need to be scored and ranked against each other so the system can return a tractable set of suggestions back to the user. Both translation and scoring are open problems the Search Features team continues to iterate on, as each is critical to the overall quality of query suggestions.
Smart document suggestions
25% of the time, users come to Glean looking to quickly jump to a document
they know
exists: a task they are working on, a document they remember reading last week, or a recently-presented company all-hands deck. The Autocomplete team has the unique opportunity to craft a stellar user experience by showing the user the document they were looking for – without having to press enter!
Because the document space is relatively small in an enterprise setting, we’re able to directly take users to documents from Autocomplete. As with Glean Search and query suggestions, we make sure to respect each document’s underlying permissions and only suggest a document to a user if they already have access.
A small document space, on the other hand, doesn’t mean that it’s easy for the system to find the exact document the user is looking for. Because users expect autocomplete to be near-instantaneous, the system doesn’t have the liberty to do the full set of computations that Glean Search can do to find the most useful result. To satisfy these demands, we’ve developed a low-latency model to predict what documents a user will visit next. As a user types, we further filter and rank the predicted document set by matching the input against keywords extracted from each document in the set. This step prevents noisy, difficult-to-explain suggestions from bubbling up to the user.
Even so, multiple documents in the predicted set often end up having similar keywords. If a user is staffed on Project X, there’s a good chance most documents, tickets, and presentations in the set are prefixed by “Project X: ”! Most users, moreover, tend to look at just the first few suggestions on the list. Thus, crafting an optimal ranking of this list becomes quite an important – and challenging – task.
The good news is that when done right, document suggestions can drastically decrease user friction. We see today that almost a fifth of our result clicks come from Autocomplete. On the flipside, about half of all users who see a document suggestion click on it - we still have a long way to go!
Better Autocomplete means being able to find things faster for our enterprise customers, and we’re constantly looking to improve our Autocomplete systems here at Glean. If the intersection of ranking and performance is something that interests you, please get in touch about
careers at Glean
! And if powerful workplace search sounds like something your team needs,
request a demo
.
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
