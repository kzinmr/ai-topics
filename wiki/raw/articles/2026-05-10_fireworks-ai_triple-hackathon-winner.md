---
title: "Three projects, one platform: A developer's winning streak with Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/triple-hackathon-winner"
scraped: "2026-05-10T01:27:16.417853+00:00"
lastmod: "2026-02-12T18:52:43.000Z"
type: "sitemap"
---

# Three projects, one platform: A developer's winning streak with Fireworks AI

**Source**: [https://fireworks.ai/blog/triple-hackathon-winner](https://fireworks.ai/blog/triple-hackathon-winner)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Triple Hackathon Winner
Three projects, one platform: A developer's winning streak with Fireworks AI
PUBLISHED
10/14/2024
Table of Contents
Core architecture
Technical implementation
From preparation to execution
Pre-hackathon preparation
During the hackathon
Nehil Jain: Unstoppable builder and AI Engineer
Selvam Palanimalai: Technical architecture expert
A track record of excellence
Hackathon 1: KinConnect - Optimizing hackathon team formation
Technical stack
Hackathon 2: LazyPMs Inc - Automating release notes with multi-agent AI
System architecture
Words of wisdom
Table of Contents
Table of Contents
Core architecture
Technical implementation
From preparation to execution
Pre-hackathon preparation
During the hackathon
Nehil Jain: Unstoppable builder and AI Engineer
Selvam Palanimalai: Technical architecture expert
A track record of excellence
Hackathon 1: KinConnect - Optimizing hackathon team formation
Technical stack
Hackathon 2: LazyPMs Inc - Automating release notes with multi-agent AI
System architecture
Words of wisdom
Table of Contents
When it comes to building with Fireworks AI, few developers can match
Nehil Jain's
track record. His latest triumph – securing second place at the E2B x Fireworks AI hackathon alongside
Selvam Palanimalai
– marks his third consecutive success using the platform. From automating release notes with LazyPMs to matching hackathon teams with KinConnect, and now ensuring documentation reliability with ProoferX, Nehil has consistently demonstrated the power and versatility of Fireworks AI.
"The speed I get using Fireworks endpoints for Llama models is one of the key drivers for successful outcomes," explains Nehil, whose deep understanding of the platform has been crucial to his winning streak. "A combination of Llama for intelligence and Firefunction for tool calling, along with structured outputs, lets me build reliable AI pipelines."
His latest project, ProoferX, developed with technical architecture expert Selvam Palanimalai, tackles one of the most persistent challenges in the developer tools ecosystem: maintaining reliable technical documentation. You can see their solution in action in their
demo on X
or check out all the
hackathon demos on YouTube
.
The problem: documentation in crisis
"Good tech products need solid docs and examples. Developer experience and trust are essential for these products to grow," explains Nehil Jain, co-creator of ProoferX. "Out-of-date code examples in public technical documentation can really hurt the product builders."
The team uncovered several real-world examples that validated their concerns:
•
OpenAI's structured output introduction contained broken references to data files
•
Vite's installation docs had issues that could frustrate junior developers
•
E2B's Python API key documentation contained a small but significant typo
The challenge, Nehil points out, goes beyond simple maintenance: "It is unimaginable to expect a team to manually check that their guides work for all the versions of the libraries used in the examples for all the OSes for different versions of compilers the user is using. The only way to achieve this is through automation."
From E2B’s Tereza Tizkova LinkedIn post,
“🏆 Who won our first hackathon?“
The solution: ProoferX
Core architecture
Drawing on his experience with Fireworks AI, Nehil worked with Selvam to architect a solution that could tackle this complex challenge.
ProoferX operates through three crucial steps:
Code Extraction
: Analyzes blog posts and documentation to create complete, end-to-end working code snippets
Success Definition
: Determines the intended outcome for readers
Sandbox Validation
: Executes code in a fresh environment to replicate the reader's experience
Technical implementation
At the heart of ProoferX lies a carefully orchestrated pipeline that begins with Firecrawl converting documentation URLs into markdown format.
*Diagram from Nehil Jain’s blog post, “
**How we won Code Interpreter 2.0 with ProoferX
”.***
Code extraction pipeline
•
Uses Firecrawl to convert URLs into markdown
•
Employs Llama 3.2 models via Fireworks AI for information extraction
•
Implements Pydantic for structured data handling and validation
Analysis flow
URL → Markdown → Code Snippets → Success Criteria → Validation
Key components
•
crewAI application for iterative code extraction
•
E2B sandboxes for code execution
•
Structured output with Pydantic models
•
Python dependency management system
Agentic approach
•
Moved beyond simple Chain of Thought prompting
•
Implemented iterative extraction for better recall
•
Handled multiple code illustrations in single documents
•
Used E2B Code Sandbox for code execution
Check out Nehil’s blog for a
full video demo of ProoferX
and more details about his and Selvam’s personal perspective on their most recent hackathon.
From preparation to execution
The team's success wasn't just about technical innovation – it was built on methodical preparation and execution.
Pre-hackathon preparation
•
Researched sponsor guides and available credits
•
Pre-formed team with complementary skills
•
Prepared starter kits and relevant documentation
•
Used Cursor IDE for efficient development
During the hackathon
During the event, their process was equally structured.
•
Created a clear data flow diagram
•
Implemented 45-minute sync cycles for code merging
•
Started with simple prompt chains to understand LLM capabilities
•
Used Firecrawl for URL-to-markdown conversion
•
Implemented Pydantic for structured data handling
The team behind ProoferX
Nehil Jain: Unstoppable builder and AI Engineer
Nehil
brings deep expertise as:
•
Founder of DemoDrive
•
Former engineer at QuantumBlack, McKinsey, and Super.com
•
Expert in AI engineering, focusing on GenAI, MLOps, and modern data platforms
•
Track record of transforming complex business challenges into practical, scalable AI solutions
"We have been building data platforms, infra, and engineering pipelines for various use cases for a long time in our careers," Nehil explains. "Using ML and now AI on top of it is a natural progression to unlock more value."
Selvam Palanimalai: Technical architecture expert
As co-founder at DemoDrive,
Selvam
(ex-Zomato, Rubikloud, and Kinaxis) contributed crucial expertise:
•
Based in Toronto, traveled to SF specifically for this hackathon
•
Expert in Cloud infrastructure, Application development
•
Focused on building tools to help devtools scale their communities and user bases
The team's complementary skills proved crucial for ProoferX's success, with Nehil handling LLMs and prompting while Selvam managed code sandboxes and app scaffolding.
Technical mastery with Fireworks
Throughout his hackathon successes, Nehil has consistently leveraged Fireworks AI's capabilities:
•
Fast Llama model endpoints for rapid development
•
Cost-effective model selection enabling rapid iteration
•
Reliable function calling for structured outputs
•
OpenAI-compatible APIs for seamless integration
"We used Llama 3.2 models to get excellent outputs for extracting essential information like goals, summaries, and steps from the markdown article," shares Nehil. "It was cheap so that we can iterate on the prompts freely."
A track record of excellence
ProoferX represents just the latest chapter in Nehil's journey with Fireworks AI. His previous hackathon victories demonstrate not only his technical versatility but also his deep understanding of how to leverage Fireworks AI's capabilities across different use cases.
Hackathon 1: KinConnect - Optimizing hackathon team formation
Before tackling documentation challenges, Nehil turned his attention to a problem he knew firsthand: the challenge of forming effective hackathon teams. At the MongoDB GenAI Hackathon, he developed KinConnect, a sophisticated matching system that transformed the typically random team formation process into a data-driven solution. The project not only secured first place but also demonstrated the power of combining Fireworks AI with modern database technologies.
From Nehil Jain’s blog,
“I built an AI app to Connect with Your Dream Team at a Hackathon”
Technical stack
The solution's architecture showcased Nehil's ability to build complex, integrated systems:
Frontend experience
•
Streamlined profile creation through Google Forms
•
Automated match delivery via email system
Backend components
•
Sophisticated profiler system for participant analysis
•
AI-powered recommender system for team matching
•
Event-driven integration through Pipedream
•
High-performance compute with FastAPI hosted on Modal Labs
Data processing
Breaking new ground in search technology, KinConnect implemented MongoDB's Hybrid Search, combining:
•
Vector search for semantic understanding
•
Precision text search for keyword matching
•
Advanced weighted reciprocal rank fusion, prioritizing keyword search signals
AI integration
The project leveraged multiple Fireworks AI models, each chosen for specific tasks:
•
Synthetic data generation powered by mixtral-8x22b-instruct
•
Query enhancement using Llama-v3-70b-instruct
•
Structured extraction from form submissions
Hackathon 2: LazyPMs Inc - Automating release notes with multi-agent AI
In another impressive showing at the
Agents and Compound AI Systems Hackathon
, Nehil and his team secured third place with LazyPMs Inc., a solution that redefined how teams handle release notes. This project showcased the potential of combining multiple AI agents to tackle complex documentation tasks.
From James Barney, LinkedIn post: “
I had a ton of fun hacking with the best and brightest AI minds this weekend!
“
System architecture
The heart of LazyPMs Inc. was its sophisticated agent network, where each AI entity played a crucial role:
Agent network
Data engineer agent
Served as the information gatherer, collecting comprehensive GitHub data including issues, PRs, and commits
PM agent
Transformed technical details into accessible summaries
Stakeholder agent
Provided feedback from multiple perspectives, ensuring comprehensive documentation
Supervisor agent
Maintained quality control and documentation standards
With minimal oversight and only final approval needed, the coordinated agent system transformed brief release notes into rich, user-friendly documentation.
Future vision
The team is actively working to launch ProoferX as a production-ready solution. Their roadmap includes several high-value use cases:
•
Enabling DevTool companies to proactively fix user-facing guides
•
Helping product teams create ready-to-run apps for blog posts
•
Supporting sales teams with custom sandboxes featuring ready-to-use API keys
Words of wisdom
The team shares an unexpected insight: "Stay away from junk food if you want to boost your mental performance. Taking care of your physical and mental state is an underappreciated alpha for winning hackathons."
Build your own ProoferX with Fireworks
Nehil Jain and Selvam Palanimalai harnessed the power of Fireworks AI to tackle the persistent challenge of maintaining reliable technical documentation.
Inspired by ProoferX and want to build a similar solution? Here's how to get started:
•
Learn about structured responses and function calling:
Dive deeper into our documentation for advanced techniques:
•
Grammar-Based Structured Output
•
Structured Response Formatting
•
Function Calling Guide
•
Join our community:
Connect on
Discord
to exchange ideas with other developers and get feedback from the Fireworks team.
•
Reach out for guidance:
Contact us
if you need help building, deploying, or scaling your application with Fireworks.
Whether you're tackling documentation challenges, building AI agents, or creating the next game-changing developer tool, Fireworks provides the performance and reliability you need to succeed.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
