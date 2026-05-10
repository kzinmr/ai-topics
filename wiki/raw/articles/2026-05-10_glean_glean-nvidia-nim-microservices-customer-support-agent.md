---
title: "Building an Intelligent Customer Support Agent with Glean APIs and NVIDIA NIM Microservices"
source: "Glean Blog"
url: "https://www.glean.com/blog/glean-nvidia-nim-microservices-customer-support-agent"
scraped: "2026-05-10T01:27:33.471278+00:00"
lastmod: "None"
type: "sitemap"
---

# Building an Intelligent Customer Support Agent with Glean APIs and NVIDIA NIM Microservices

**Source**: [https://www.glean.com/blog/glean-nvidia-nim-microservices-customer-support-agent](https://www.glean.com/blog/glean-nvidia-nim-microservices-customer-support-agent)

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
Building an Intelligent Customer Support Agent with Glean APIs and NVIDIA NIM Microservices
0
minutes read
Arvind Jain
CEO
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
The collaboration between Glean and NVIDIA empowers organizations to build advanced AI applications for customer support by leveraging Glean's contextual knowledge graph and NVIDIA NIM™ microservices, ensuring secure and context-aware responses to queries.
NVIDIA NIM microservices, included in the AI Enterprise software platform, support a variety of AI models for self-hosting, enabling high-performance generative AI inferencing both on-premises and in the cloud.
The combined solution of Glean APIs and NVIDIA NIM microservices enhances retrieval precision, supports multimodal inputs, and ensures complete control over AI infrastructure, maintaining enterprise data security and scalability.
Introduction
The collaboration between Glean and NVIDIA unlocks a powerful, enterprise-grade AI architecture that is the foundation for modern customer support agents. By leveraging Glean's contextual knowledge graph and NVIDIA NIM™ microservices, organizations can create agentic AI applications that deliver precise, context-aware responses to complex queries while securely safeguarding enterprise data and prompts within their network. Read more about our collaboration announcement
here
. This post will outline how businesses can integrate Glean APIs with NVIDIA NIM microservices to deploy a cutting-edge AI support agent.
What is NVIDIA NIM?
NIM
microservices are included in the
NVIDIA AI Enterprise
software platform and speed up generative AI deployment in enterprises. Supporting a wide range of AI models, including
NVIDIA AI Foundation and custom models
, NIM microservices provide seamless, scalable AI inferencing, on-premises or in the cloud, leveraging industry-standard APIs.
With NIM, our customers can choose from a wide variety of language models to self-host on their own infrastructure. Customers can use the
NVIDIA API catalog
to experiment with the latest GPU-accelerated LLMs the day they are released, and easily integrate them with Glean Assistant. NIM makes it easy to deliver optimized LLM inference at scale, no matter where the model is hosted.
A key advantage of NIM is that it enables organizations to maintain complete control over their AI infrastructure and intellectual property. By allowing enterprises to self-host models on their own infrastructure, NIM ensures that sensitive company information, prompts, and customizations remain secure within their network, while still delivering high-performance AI inferencing capabilities.
Learn more about NVIDIA NIM microservices
here
. Each layer in the stack highlights key components or capabilities designed to enhance the deployment and performance of machine learning models. Here's what each part represents:
Prebuilt Container
: At the top of the stack, this indicates that NVIDIA provides preconfigured, containerized environments that simplify model deployment by including necessary dependencies and configurations.
Industry Standard APIs
: This layer ensures compatibility and ease of integration with commonly used APIs, facilitating seamless use of the module across various platforms and applications.
Support for Custom Models
: NVIDIA NIM accommodates not only pre-trained models but also user-defined or customized models, offering flexibility for specialized use cases.
Domain-Specific Code
: This layer signifies that the module includes optimizations and code tailored for specific industries or applications, such as healthcare, automotive, or retail.
‍
Optimized Inference Engines
: At the base of the stack, this layer ensures that the underlying inference engines are highly optimized for performance, leveraging NVIDIA hardware to deliver efficient and fast inferencing.
The stack emphasizes a combination of ease of use, flexibility, and high performance tailored to industry-specific needs.
How Glean APIs and NVIDIA NIM Work Together
The diagram below illustrates a customer service agent architecture that combines Glean APIs with NVIDIA NIM and NeMo microservices. This setup operates in four stages, aiming to enhance customer experience and improve operational efficiency:
initial query processing
,
retrieval system
,
reranking
, and
answer generation
. Integrating with Glean APIs ensures enterprise-grade accuracy, contextual relevance, and reliable content retrieval for these stages.
Glean APIs
provide powerful data retrieval, ensuring results are securely permissions-aware and contextually relevant. By indexing enterprise data across diverse sources, Glean APIs surface information that is both accessible and impactful for users.
NVIDIA NeMo
and NIM
microservices enhance retrieval precision and ranking while enabling multimodal input support.
Workflow Summary
User Query Contextualization
:
The user submits a query in text and/or image format.
Images are converted into natural language using NVIDIA NeMo’s image-to-text capabilities (
NeVA 22B NIM
) and NVIDIA NIM for LLM for Chat History Query Contextualization.
Query Guardrailing
:
NVIDIA NeMo Guardrails
evaluates queries to filter restricted queries and protect enterprise sensitive information.
The non-sensitive queries are sent to the ReAct Agent which uses another NIM to identify and filter the data sources that should feed into the answer.
Retrieval System
:
Multiple rephrased queries with different facets (e.g., date filters, keywords, user context) are sent to
Glean’s Search APIs
.
Glean’s APIs retrieve results from its
contextual knowledge graph
, providing highly relevant, real-time and permission-aware content.
Snippet Size
: Glean supports up to 25,000-character snippets, ensuring comprehensive retrieval for long or detailed responses.
Deduplication
: Results from multiple queries are deduplicated to remove redundant chunks and provide clean outputs.
Reranking
:
The NeMo Retriever reranking NVIDIA NIM
microservice prioritizes retrieved content based on relevance and accuracy.
Answer Generation
:
The LLM NIM for customer’s foundational model of choice (in this case, Llama 3.1) synthesizes the final response using the top-ranked content.
References
: Answers are enriched with inline citations using the
NeMo Retriever embedding microservice
to maintain transparency and display material below the complete answer for ease of access.
Deployment Flexibility
Glean APIs and NVIDIA NIM provide a highly adaptable framework for deploying advanced AI solutions across diverse environments.
Scalable Cloud Deployments:
Both platforms seamlessly integrate with major cloud providers, including AWS and GCP, offering businesses the scalability and resilience needed for enterprise-grade AI workloads.
On-Premises Compatibility:
NVIDIA NIM, as part of the NVIDIA AI Enterprise suite, extends deployment options to on-premises data centers, enabling organizations to leverage optimized infrastructure for sensitive or regulated environments. Glean complements this by connecting securely to on-premise systems, ensuring unified access to enterprise data.
Optimized Performance:
Glean's efficient retrieval mechanisms and NVIDIA's tailored inference engines ensure high throughput and low latency, delivering responsive performance for even the most demanding applications.
Unified Architecture:
Together, Glean and NVIDIA NIM create a robust solution that adapts to cloud-first, hybrid, and specialized on-premises strategies. This enables organizations to deploy cutting-edge AI with confidence.
For more information, visit the
NVIDIA AI Enterprise overview
or explore
Glean's deployment options
.
What Glean APIs Provide
Glean APIs play a critical role in the overall architecture by offering:
Contextual Knowledge Graph
: Glean builds a knowledge graph that indexes structured and unstructured enterprise data, ensuring responses are grounded in reliable and permission-aware information.
Search with Facets
: Glean Search APIs provide advanced filtering capabilities (e.g., date, document type, user context), enabling highly targeted query responses.
Large Snippet Support
: Glean retrieves up to 25,000-character content chunks, which ensures sufficient context for accurate answer generation.
User and Access Context
: Glean integrates user permissions and access controls, ensuring that only authorized content is surfaced in responses.
Query Deduplication
: Redundant results are removed automatically to deliver clean, unique data for downstream processing.
Real-Time Performance
: Glean APIs deliver responses with high throughput and low latency, ensuring smooth user experiences in production environments.
Why Use Glean and NVIDIA for Customer Support Bots?
Accuracy at Scale
: NVIDIA's RAG-based architecture paired with Glean’s extensive knowledge graph ensures high-quality responses.
Enterprise-Grade AI
: Robust security, access control, and data deduplication align with enterprise needs.
Multimodal Capabilities
: Support for both text and image inputs enhances the bot’s usability.
Seamless Integration
: Glean APIs and NVIDIA NIM inference microservices work together effortlessly.
Private Infrastructure Control
: Organizations can deploy AI models on their own infrastructure, ensuring sensitive company data, prompts, and intellectual property remain secure within their network while maintaining enterprise-grade performance and scalability.
Getting Started
For more technical documentation, visit:
NVIDIA NIM Deployment Guide
NVIDIA NeMo Retriever NIM Microservices
‍
NVIDIA Generative AI Examples on GitHub
‍
Build an Agentic AI With NVIDIA NIM and Glean
on Glean’s Developer Portal
Ready to build your intelligent support bot? Get started with Glean APIs and NVIDIA NIM today.
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
