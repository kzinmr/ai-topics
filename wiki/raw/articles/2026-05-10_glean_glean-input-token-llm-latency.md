---
title: "How input token count impacts the latency of AI chat tools"
source: "Glean Blog"
url: "https://www.glean.com/blog/glean-input-token-llm-latency"
scraped: "2026-05-10T01:20:17.724541+00:00"
lastmod: "None"
type: "sitemap"
---

# How input token count impacts the latency of AI chat tools

**Source**: [https://www.glean.com/blog/glean-input-token-llm-latency](https://www.glean.com/blog/glean-input-token-llm-latency)

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
How input token count impacts the latency of AI chat tools
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
There is a linear relationship between the number of input tokens and the time to first token (TTFT), with each additional token increasing TTFT by approximately 0.24ms.
Splitting a complex prompt into smaller parallel prompts can significantly reduce TTFT, improving user-perceived latency.
Understanding and optimizing input token counts can enhance the performance and user experience of AI chat tools by reducing latency.
Lately, foundational LLM companies have been racing to create LLMs with larger and larger context window sizes. After all, if the user can fit more information into the input window, the better it is, right? And if that’s true, shouldn’t tools like Glean Assistant make use of the entirety of those windows to provide a more powerful and comprehensive experience?
Curious to know the answer, we conducted a few tests to discover exactly how input token counts impact metrics such as time to first token (TTFT) and chat latency, in addition to their impact on the overall experience for our users.
What is the correlation between input token counts and TTFT?
The first correlation we wanted to investigate was between the volume of input tokens and time to first token. Before diving into the empirical data, here’s a quick explanation of what we expected to observe.
Generating the
first
completion token from an LLM at a
high
level consists of tokenizing the incoming prompt, and running the token tensor through the Transformer network—typically called the
initiation
phase. To generate subsequent tokens, the latest token is appended to the prompt and the process is repeated—this is commonly referred to as the
decoding
phase. Tokenizing is generally a linear time operation, but running the initial prompt through the transformer is
not.
In fact, it’s a quadratic time operation.
Why is this the case? The short answer is, computing
attention scores
within a Transformer involves doing matrix multiplications, and multiplying a matrix of shape (n, p), with another matrix (p, m), involves approximately 2*m*n*p operations. In the case of the of the attention layer, m and n are both equal to the size of the context window, w, meaning the cost of this operation becomes 2*p*w^2—a
quadratic
relation. The subtlety here is that the relation is with respect to the context window size, and
not
the number of incoming tokens.
Testing the correlation
Below we can see the empirical data of running such an experiment. Here we plot the TTFT P95 for GPT-4 Turbo versus the number of prompt tokens. For each data point, 25 LLM calls were run.
As a small, yet important aside, these tests were run using Azure’s provisioned throughput unit (
PTU
) model deployments. PTUs are a way to obtain reserved processing capacity just for you—unlocking predictable performance and mitigating the latency swings seen via their pay-a-you-go services. This ensures that our data isn't being muddled due to data center loads.
The plot below zooms into the bottom left corner for better readability.
Lastly, here is a plot of the average TTFT versus the number of prompt tokens.
Key observations here are:
We immediately notice a
linear
relationship between these two variables – with the number of prompt tokens ranging from 50 to 100,000.
We see that for every additional input token, the P95 TTFT increases by ~0.24ms and the average TTFT increases by ~0.20ms.
The next question to ask is, why was the correlation linear? This likely has to do with the fact that the Transformers mask all the unpopulated values in the context window vector with zeros, allowing GPUs to skip large portions of the matrix multiplication. Note here that the relation mentioned earlier was with respect to the context window size.
Many sources online state that reducing the number of input tokens does result in lower latency, but this is usually not a significant factor. In fact
Open AI states
that “cutting 50% of your prompt may only result in a 1-5% latency improvement.” I suspect the latency improvements mentioned here and elsewhere are E2E latency and
not
TTFT. This seems to line up with the numbers as well.
Finally, I’d like to emphasize that 0.24ms might seem like a negligible amount, but the data illustrates that splitting a complicated 3000 token prompt into three parallel 1000 token prompts, results in a reduction in the TTFT by 480 ms – a sizable drop in user perceived latency.
Improving Glean for the better
We’ll keep these results in mind as we continue to build and improve Glean Assistant to deliver a better, speedier service for our users. If you’re interested in learning more about topics like speeding up embedding calls, or the correlation between latency and output tokens, stay turned for new blogs coming up in the near future!
Looking to learn more about Glean? Get a free demo today—or check out our
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
