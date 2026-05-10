---
title: "Learning lessons from building an enterprise AI assistant"
source: "Glean Blog"
url: "https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise"
scraped: "2026-05-10T01:20:40.534186+00:00"
lastmod: "None"
type: "sitemap"
---

# Learning lessons from building an enterprise AI assistant

**Source**: [https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise](https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise)

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
How to build an AI assistant for the enterprise
0
minutes read
Chau Tran
Engineering
Mrinal Mohit
Engineering
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
Fine-tuning large language models (LLMs) on enterprise data can lead to increased hallucinations and is not suitable for factual recall. Instead, retrieval augmented generation (RAG) is recommended for integrating proprietary knowledge.
Building a centralized index with scalable, permission-aware crawling and search capabilities is essential for effective enterprise search. Glean provides pre-built connectors to integrate data from various sources.
Combining traditional keyword-based methods with modern neural-network-based semantic embedders enhances search relevance. Glean's knowledge graph personalizes search results by understanding content, context, and user interactions within the organization.
Large Language Models (LLMs) like GPT-4 and PALM are powerful reasoning engines that form the foundation of most text-based generative AI experiences seen today. Ask the LLM a question, and it usually provides an intelligent answer. They are able to reach into the depths of knowledge provided by the data they were trained on – or what we call "world knowledge".
But what about data that is proprietary – say, information restricted to your company’s employees? If you ask a generic LLM a question about the status of your latest customer deal, it will likely tell you that it doesn’t have enough context to answer. Worse yet, it might hallucinate and fabricate an incorrect reply, resulting in the spread of misinformation and potentially serious workflow consequences.
Applying generative AI technologies like ChatGPT to enterprise data is challenging given the complexity of handling security permissions, scaling infrastructure, and establishing a broad, high-quality knowledge graph. In this blog post, we’ll walk through some approaches to make ChatGPT work on enterprise data, their pitfalls, and how Glean solves for them through
Glean Chat
.
The challenges of fine-tuning LLMs on enterprise data
In the previous generation of natural-language-processing models (e.g. BERT, RoBERTa, and others), one popular paradigm was “fine-tuning” – where one would start with the weights of a foundational model, and then train them to better fit the needs of their specific tasks and domain.
However, how has the fine-tuning paradigm fared in today’s era of LLMs? Let’s start with how a modern LLM like ChatGPT is trained:
First, a “foundational model" is trained on massive amounts of data (trillions of tokens), which requires immense compute power (costing millions of dollars). This is what it costs to build the impressive reasoning and generation abilities you’ve seen from ChatGPT.
Then, the model enters a fine-tuning stage where it’s trained to follow natural language instructions, and aligned to human values. This stage is critical to ensure the model behaves ethically by avoiding potential harms like toxicity, bias, and privacy violations.
A seemingly natural way to infuse proprietary knowledge into an LLM is at the fine-tuning stage. However, the fine-tuning stage is meant to improve task-specific performance, not to teach the model about new knowledge. When an LLM is fine-tuned on unfamiliar knowledge, it actually
increases
hallucinations
. This is because we’re essentially teaching the model to generate responses for topics it does not have a strong, factual understanding of. It’s why we agree with
OpenAI
that “fine-tuning is better suited to teaching specialized tasks or styles, and is less reliable for factual recall.”
Alternatively, one could try including company private data at the foundational pretraining stage through domain adaptation (similar to
BloombergGPT
, or
MedPALM
). While this approach is effective for adapting LLMs for broad domains, it has several fundamental limitations when building an
enterprise AI
copilot:
Freshness
– One could fine-tune models on a snapshot of their company’s data, but what happens when that changes on an hourly basis? Users are interested in having the most recent and relevant data, but continually training the model to provide that is expensive and difficult to maintain.
Permissions
– Not every employee has access to see all of the data within their company. Sensitive conversations might happen between the CEO and the CFO, performance reviews might be restricted to managers, and engineers might not have access to Salesforce. Throwing “all” data into a LLM results in generated answers leaking sensitive details.
Explainability
– When your employees are relying on an assistant to help them with their job, you want the answers to not just be correct, but verifiable. If a support agent recommends a fix for a ticket using an assistant, they should be able to verify what document was the source of the recommended fix. Does a source document even exist? Did the model hallucinate one? Is the document canonical, or was last updated 10 years ago? Is there any additional context in the document they should know about? All of this is impossible to process if you trust LLM generations blindly.
Catastrophic forgetting
– The amount of proprietary data in your company is several orders of magnitude smaller than the vast amount of data used to train a base LLM. As a result, fine-tuning the model risks it either forgetting much of the broad, general world knowledge it had originally gained, or failing to learn the nuances of your proprietary data.
In conclusion, while fine-tuning/training LLMs is appealing for improving task-specific performance, there are too many limitations and risks with this approach for
workplace AI assistants
.
Retrieval Augmented Generation: Vector search is not enough
To separate the ability of LLMs to generate coherent, well-reasoned responses from their (in)ability to reliably retrieve factual knowledge, the system can be designed as a pipeline. We first retrieve knowledge through a separate search system, and
then
give it to the LLM to read in order to ground its reasoning and synthesis. This is widely known as
Retrieval Augmented Generation (RAG)
.
Knowledge is always as recent and relevant as possible, since the regularly updated search index is inserted into the LLM at query-time.
The LLM will never access something a user doesn't have access to.
Users can look at the subset of documents which were fed into the LLM and to verify that the generated response is grounded in truthful information.
Catastrophic forgetting doesn’t happen, as it retrieves relevant knowledge at query-time rather than trying to retain all knowledge within the model.
At the heart of RAG is the retrieval component – underpinning the security of your company’s data and the relevance of the generated responses your workers need to succeed. We’ll go through why this is essentially a search problem, along with some of the technical requirements of implementing this in the enterprise setting.
Data: Scalable permission-aware indexing
When building the data layer for an
enterprise search solution
, there are a couple approaches to consider.
Federated search across individual app APIs is one approach, but it comes with major downsides. Each app's search API has its own nuances, requirements, and rate limiting, making it largely unscalable. Federated search also results in suboptimal ranking algorithms (since they only understand data within that single app, and search features in SaaS are usually underinvested), ultimately providing a poor search experience.
A better solution is to build a centralized index by crawling and indexing data from all sources. However, building a scalable, permission-aware crawler and search platform is an engineering challenge that can take years of work – from scaling to corpuses billions of documents in size, to creating a unified document model that’s capable of handling a wide variety of different data sources.
Glean provides over
100 pre-built connectors
that hook into apps like Google Drive, Slack, Jira, Salesforce, and more – helping users start indexing data quickly and skip years of development. For enterprise customers with hundreds of thousands of employees, billions of documents, and hundreds of terabytes of data, Glean’s infrastructure (built over a period of nearly five years) handles data at this scale wonderfully.
By indexing data from all sources into a single platform, Glean is able to build a
cross-app knowledge graph
that thoroughly understands all the content, context, and collaborators across the organization. By then applying advanced ranking algorithms to surface the most relevant results, Glean delivers a vastly improved search experience over systems that use individual app APIs.
For any company looking to unlock the value of their data, a scalable indexing platform with pre-built connectors is the way to go over federated search. Glean provides turnkey access to
enterprise search
with an indexing solution built for the modern SaaS-powered workplace.
Topical relevance: Hybrid search with reranking
With a scalable indexed corpus, the next challenge is retrieving the most relevant knowledge for a given query. Among the billions of documents in your company’s corpus, how do you find the ones that contain the most useful, accurate, and up-to-date information?
To fetch these “relevant” documents to feed into the LLM, vector search has emerged as a prime candidate. The system “embeds” each piece of text into a vector of numbers, and stores that in a vector database. When a query comes, it’s similarly embedded into the database. The closest file to the query in the vector space is then sourced as the most relevant piece of information.
Database providers such as Pinecone or Weaviate have been getting a lot of attention lately. What isn’t discussed enough, however, is that the
quality
of the vector embeddings is usually a bigger bottleneck than having a database to host those embeddings.
We’ve shown
previously
that if you
fine-tune embedding encoders
on company-specific data, you can get far better matching quality than most “generic” embedding models, open-source (MPNet, E5, Instructor) or close-source (OpenAI, Cohere). This of course requires expertise in training these models, along with the infrastructure to do so continuously. Glean has been steadily building and refining this over the past years.
But even though embeddings are powerful, traditional keyword-based methods are far from being obviated. In fact, what works well in practice are “hybrid” methods, which take the best of classical information retrieval techniques and modern neural-network based semantic embedders (
Thakur et al. (2021)
). Tuning a
hybrid retrieval and reranking
system is an extremely complicated task – it requires training models to combine dozens different ranking signals (including semantic similarity, keyword match, document freshness, personalization features, and more) in order to produce a final relevance score. Our search models are continuously learning and improving from every query to provide the most relevant results for each employee.
{{richtext-banner-component}}
Personalization: Extensive knowledge graph
Even with a perfect textual search system, documents that are textually related to the search query may not always contain the right information to answer a user’s question. For example, an engineer may ask where the latest design specs are kept. However, the search results may contain hundreds of documents/pull requests/messages about the topic. This scenario is also why we believe that using a much larger context window (up to 1 million tokens) would not eliminate the need for search relevancy, since providing wrong and outdated information would cause the language model to give an incorrect answer.
Dense vector methods are specifically designed to handle text, whereas in reality, there are more data mediums at play. To make search personalized to each individual user, Glean continually builds a
knowledge graph of all information
being created within your company. The nodes in this knowledge graph include:
Contents
– Individual documents, messages, tickets, entities, etc.
People
– Identities and roles, teams, departments, groups, etc.
Activity
– Critical signals and user behavior, sharing and usage patterns
The edges in the graph are how all these entities interact with each other:
Document linkage
– Documents that are linked from other documents, or mentioned by other users are more likely to be relevant (
PageRank - the paper that started Google
)
User-User interactions
– Documents from authors who are on the same team, who I have interacted with in the past, whom I have an upcoming meeting with, … are more likely to be relevant to me.
User-Document interactions
– Documents that I (or someone from my team) created/edited/shared/commented/… are all more likely to be relevant to me
Integrating LLMs: Enhancing search itself
LLMs are not only useful for summarizing and synthesizing search results – they can also enhance the overall search experience. For example, LLMs enable the enterprise AI copilot to do
advanced
query planning
, allowing systems to interpret natural language commands and translate them into a set of search queries that yield the intended results. A command like:
"
Read through our Glean Chat code changes in the last month. Give me a list of enhancements we are making to the feature. You can also check our #project-glean-chat channel for more discussion.
"
…could be translated into two search queries, and synthesize results from them:
Github pull requests in the last month that mentions “Glean Chat”
Messages from the #project-glean-chat Slack channel that talks about project progress
LLMs can also help bootstrap domain-specific encoders for new customers by
augmenting sparse real-world data
with machine-generated examples (
Promptagator
,
InPars
). Since each customer's data is used exclusively to train their own encoders, synthetic data helps compensate for the lack of large in-domain datasets while retaining the customer's unique language and terminology. This results in enterprise-adapted encoders that are customized for and generalize better to each customer's data.
‍
Unlock the full value of generative AI today – not tomorrow
Building an enterprise-ready ChatGPT system is no small feat. There are significant requirements around freshness, permissions, explainability, and catastrophic forgetting that come with applying LLMs to company data. While vector search and embeddings have received a lot of recent interest, developing high-quality embeddings and the infrastructure to support them at scale is an engineering challenge of its own. For most companies, developing an in-house solution for unlocking the power of LLMs in their workplace data will require years of work and expertise across machine learning, search, and scalable data infrastructure.
Rather than building from scratch, Glean provides an out-of-the-box solution for enterprise search and knowledge management powered by the latest generative AI technologies. Glean's underlying platform also enables you to easily build custom point solutions through our APIs for numerous enterprise workflows. The end result is an enterprise implementation that harvests the benefits of generative AI at a fraction of the cost and complexity of an in-house solution.
With Glean, companies can stay focused on higher-level goals like driving new business and innovation, while fast-tracking to success through the latest innovations in generative AI without having to wait. To see how Glean helps leading companies unlock the value of their data,
request a demo today
. You'll be on your way to transforming how your organization leverages knowledge through market-leading enterprise search and
AI-powered chat assistance
– without any of the hassle of building it yourself.
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Enterprise search buyer’s guide
Enterprise search solutions have become essential to ensuring employee satisfaction, workflow efficiency, and business success. Discover what features and capabilities to look for when considering the best search solution for you.
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
