---
title: "How KV caches impact time to first token for LLMs"
source: "Glean Blog"
url: "https://www.glean.com/blog/glean-kv-caches-llm-latency"
scraped: "2026-05-10T01:20:18.384538+00:00"
lastmod: "None"
type: "sitemap"
---

# How KV caches impact time to first token for LLMs

**Source**: [https://www.glean.com/blog/glean-kv-caches-llm-latency](https://www.glean.com/blog/glean-kv-caches-llm-latency)

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
How KV caches impact time to first token for LLMs
0
minutes read
Veraj Paruthi
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
KV caching significantly reduces time to first token (TTFT) latency and improves throughput for LLM calls by caching previous computations and reusing them across requests.
Experiments show that each cached input token saves approximately 0.15ms, leading to substantial reductions in TTFT when caching is used across multiple tokens.
Implementing KV caching in Glean Assistant enhances user experience by delivering faster and more efficient responses, crucial for maintaining satisfactory user sessions.
Welcome back to our series on LLM latency! In our
previous blog
, we took a close look at how input token count impacts the latency of LLM chat tools. In this blog, we’ll explore how KV (key-value) caching impacts time to first token (TTFT) latency and throughput for LLM calls.
The impact of KV caches on TTFT
LLMs are autoregressive models, where the generation of the ith token depends on all the tokens generated prior. This means that computing the attention scores for the ith token involves
all the same
operations as done for the i-1th token, plus the additional computations for this latest token. This is a great opportunity to cache.
Caching these values has the following implications:
The initiation phase, which we learned in the
previous blog
refers to generating the first token, is unaffected by the KV caching strategy since there are no previous steps. This phase now populates the KV cache for subsequent stages.
For the decoding phase we no longer use the whole sequence as input but only the last generated token and the KV cache.
So, how does attention computation scale now? As we discussed in the last blog, computing
attention scores
within a Transformer involves doing matrix multiplications and multiplying a matrix of shape (n, p), with another matrix (p, m), involves approximately 2*m*n*p operations. In the case of the of the attention layer, m and n are both equal to the size of the context window, w, meaning the cost of this operation becomes 2*p*w^2—a
quadratic
relation. However, since the query for subsequent generations is now a single token, the computation is
linear
(2*p*1^2).
This explains how completions within a
single
LLM call benefit from caching, but if this cache is persisted, it can be used
across
LLM calls. Two
possible
ways this can be taken advantage of are:
1. Caching in multi-turn use cases within a single conversation
Within a single conversation, the chat history is an ever growing string prefix that can be cached across turns!
2. Caching across workflows that have similar prefixes
Being able to reuse the KV cache
across
requests should enable TTFT latency wins as well as throughput improvements due to the memory footprint of concurrent requests with a shared prefix.
Experiment results
Luckily for us, Azure’s KV cache can persist these computations
across
LLM calls. Their
documentation
states that “the amount of throughput that you can achieve on the endpoint is a factor of the input size, output size, call rate, and cache match rate.” In fact, they suggest “mixing the calls can reduce your cache hit rate as they're both competing for the same space. When possible, it's recommended to have separate deployments for each workload”.
The data of using this cache across requests can be seen below. Each data point was obtained via 25 GPT4 Turbo calls using Azure’s provisioned throughput units (PTU). Cached calls had the
exact
same prompt over the 25 calls. Meanwhile, the uncached runs had the current request time as a prefix in each prompt, invalidating the prefix cache.
To note here again, in case you missed our
first latency blog
, we used Azure’s PTU model deployments to run these tests. PTUs are a way to obtain reserved processing capacity just for you—unlocking predictable performance and mitigating the latency swings seen via their pay-a-you-go services. This ensures that our data isn't being muddled due to data center loads.
The plot below zooms into the bottom left corner for better readability.
‍
This shows us that each cached input token saves ~0.15ms, the difference between the two slopes. I’d like to emphasize that 0.15ms might seem like a negligible amount, but the data illustrates that caching 1000 tokens across calls results in a reduction in TTFT by 100 ms!
Making Glean a better experience
When it comes to user experiences, we know that even a few milliseconds can make or break a satisfactory session. We’ll keep these results in mind as we continue to build and improve Glean Assistant to deliver a better, speedier service for our users.
Looking to learn more about Glean? Get a free
demo
today—or check out our
careers
page if you’re interested in helping us build the future of enterprise AI yourself!
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
