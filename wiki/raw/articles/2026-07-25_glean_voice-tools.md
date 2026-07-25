---
title: "Why Enterprise Voice Demands a Better Tool Stack"
source: "Glean Blog"
url: "https://www.glean.com/blog/voice-tools"
scraped: "2026-07-25T06:00:40.025840+00:00"
lastmod: "None"
type: "sitemap"
---

# Why Enterprise Voice Demands a Better Tool Stack

**Source**: [https://www.glean.com/blog/voice-tools](https://www.glean.com/blog/voice-tools)

Product
Platform Overview
See how Glean works.
Connectors & Actions
Glean offers more than 250 connectors
APIs
Build generative AI experiences
Model Hub
Get access to the latest models
AI Gateway
Accurate and efficient tools
Security
Safely scale AI at work
Glean Assistant
Your personal AI assistant
Proactive Intelligence
Anticipate what matters next
Data Analysis & Research
Turn context into insights
Content Creation
Create grounded, on-brand content
Work Execution
Turn insight into action
Glean Agents
Build and manage agents
Agent Builder
Build agents your way
Agent Orchestration
Automate work across systems
Agent Governance
Scale agents with control
Agent Library
Discover trusted, reusable agents
Agent Harness
Plan and adapt intelligently
Glean Enterprise Context
Context for it all.
Enterprise Search
The foundation for answers
Personal Graph
Understand how you work
Enterprise Graph
Understand how your company works
System of Context
Context that boosts productivity
Hybrid Search
Search grounded in context
Glean browser extension
Customers
Solutions
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
IT
Marketing
B2B Marketing
B2C Marketing
People
Finance
Legal
INDUSTRIES
Retail
Consumer Goods
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Professional Services
Consulting
Construction
IT Services
Financial Services
Banking
PE/VC
Asset management
Insurance
Government
Healthcare
Higher Education
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
The Work AI Index 2026
Workers say AI saves them 11 hours a week. Where is that time going?
Download the report
Company
About us
Careers
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
Company
Sign in
Sign in
Get a demo
Get a demo
PRODUCT
Platform Overview
See how Glean works.
Connectors & Actions
Glean offers more than 250 connectors
APIs
Build generative AI experiences
Model Hub
Get access to the latest models
AI Gateway
Accurate and efficient tools
Security
Safely scale AI at work
Glean Assistant
Your personal AI assistant
Proactive Intelligence
Anticipate what matters next
Data Analysis & Research
Turn context into insights
Content Creation
Create grounded, on-brand content
Work Execution
Turn insight into action
Glean Agents
Build and manage agents
Agent Builder
Build agents your way
Agent Orchestration
Automate work across systems
Agent Governance
Scale agents with control
Agent Library
Discover trusted, reusable agents
Agent Harness
Plan and adapt intelligently
Glean Enterprise Context
Context for it all.
Enterprise Search
The foundation for answers
Personal Graph
Understand how you work
Enterprise Graph
Understand how your company works
System of Context
Context that boosts productivity
Hybrid Search
Search grounded in context
Glean browser extension
Sign in
Get a demo
Get a demo
SOLUTIONS
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
IT
Marketing
B2B Marketing
B2C Marketing
People
Finance
Legal
INDUSTRIES
Retail
Consumer Goods
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Professional Services
Consulting
Construction
IT Services
Financial Services
Banking
PE/VC
Asset management
Insurance
Government
Healthcare
Higher Education
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
Sign in
Get a demo
Get a demo
RESOURCES
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
The Work AI Index 2026
Workers say AI saves them 11 hours a week. Where is that time going?
Download the report
Sign in
Get a demo
Get a demo
COMPANY
About us
Careers
Last updated Jul 24, 2026.
What enterprise voice demands of your tool stack
0
minutes read
Sitaram Iyer
Software Engineer
Mohit Gupta
Software Engineer
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
The main lesson from building Glean Voice is that the bottleneck is usually not the model. It’s the tool stack.
Voice answers questions from your company's knowledge, out loud and in real time. That means every response depends on calling the right tools at the right moment to reach the right enterprise context – or to take the right action.
Glean's tool stack was already battle-tested in enterprise chat, but voice exposed a new level of demand we hadn't fully designed for. Voice models are often smaller, their context windows are tighter, they have to respond within a strict latency budget, and bad actions are harder to walk back. A bad tool call in text chat can quietly get fixed on the next turn without the user noticing. In voice, the model is already speaking — the user hears the gap in real time. There's less buffer to course-correct without the voice experience feeling broken.
That changes where the engineering work goes. The biggest gains came from making the tool stack cleaner and stricter: better filtering, better ranking, more tool detail surfaced up front, and one canonical execution path. We wrap tools into skills, pairing the tools needed for a task with detailed instructions for completing it. For each request, we run a live search and ranking over the catalog to retrieve the best skill for the task and user, rather than giving the model a huge list of tools and asking it to pick.
Retrieval quality matters earlier than people expect
A complex action like "set up a meeting" sounds like one tool call, but in practice, it involves determining who should attend, resolving each person’s identity, reconciling calendars across time zones, finding a slot that dodges the hard conflicts while overriding the soft ones, possibly reserving a room, and only then creating the event in each provider-specific format.
Asking the model to reconstruct all of that real-world logic around a bare tool is demanding and unreliable. Instead, we wrap one or more tools and their detailed instructions into a skill. Execution then happens in two stages: first retrieve the right skill from a catalog, then follow its instructions and invoke its constituent tools.
For voice, in particular, the quality of the retrieved skills and tools is paramount to quality, because voice models often have less reasoning capacity and fewer opportunities to recover from retrieval mistakes. A voice model presented with fewer, cleaner, better-ranked skills can therefore outperform a higher reasoning model working from a noisier set. That was one of the non-obvious results when we built Voice. Much of the leverage came from dynamic skill and tool discovery, particularly the filter-rank-trim funnel ahead of execution: first for eligible skills, then for tools within the selected skill.
The other lesson was that dense embeddings are not enough when there is a short list of repetitive tools. Many entries share the same verbs: send, create, update. The useful signal is often the rare token that disambiguates Slack from Gmail or Jira. Simple lexical weighting helped more than expected because it preserved those distinctions instead of washing them out.
Voice needs the tool contract inline
Text chat can absorb more indirection. A chat model can follow links, inspect schemas later, or recover from a vague validation error. Voice usually cannot.
For voice, more of the tool contract has to be present up front: canonical names, server identity, argument names, and enough schema detail to make a correct first call. Otherwise the model fills in the gaps, and those guesses are often plausible enough to be dangerous. This approach differs from the one we take with text models, where we use progressive disclosure of tools to minimize context overhead.
We also see voice models needing more context around errors. In chat, a generic validation failure may still be recoverable. In voice, validation errors need to function as structured retry signals. If the system says exactly which field is wrong and what type it expected, the model can often repair the call. If it just receives “that didn’t work,” the turn is usually lost.
Voice tends to center action-oriented work
One useful way to think about voice is that the work often skews more action-oriented than in text chat. People use voice to send messages, create events, or file tickets while they are in motion, and these are less correctable than, say, search results. Those actions are not unique to voice, but voice has less room to hedge around them. That means the stack needs exact retries, explicit auth state, and deterministic execution semantics.
Voice tool reliability improved when we collapsed these choices into a single canonical path: find the skill, resolve the authorized tool, validate the call, execute, and confirm the result. This made the system more predictable. Authorization state could be surfaced explicitly. The model could be prevented from claiming success before the downstream system confirmed it. Retries could be driven by execution state instead of improvised in language.
Voice exposes problems that already existed
One useful side effect of voice is that it reveals problems in the underlying tools and infrastructure that are less visible in chat. A number of failures that first appeared as “voice bugs” were really retrieval, initialization, or execution-path issues that chat could often absorb through retries, longer deliberation, or a more forgiving UI. Voice just made those weaknesses visible.
That is why work like caching, pooling, and taking setup off the request path mattered so much. In realtime systems, infrastructure discipline shows up directly as product quality, and it also helped with improving quality and latency of text chat tool calling.
The broader takeaway
Voice does not just need better prompts. It needs a tighter contract with tools.
That means a retrieval layer that is compact and trustworthy, a ranker that understands provenance as well as relevance, enough schema detail exposed early to avoid guessing, and an execution path that treats external actions as commitments rather than suggestions.
That lesson is not unique to voice. Voice just makes it impossible to ignore.
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
Go to Glean's Twitter Account
Go to Glean's Linkedin Account
Go to Glean's Instagram Account
Go to Glean's Instagram Account
Language
English (United States)
Japanese (Japan)
French (France)
PRODUCT
Work AI Platform
Workplace Search
Assistant
Proactive Intelligence
Data Analysis and Research
Content Creation
Work Execution
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
Enterprise AI Software
AI Agent Builder
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
Cookie Preferences
Website Terms
Privacy
