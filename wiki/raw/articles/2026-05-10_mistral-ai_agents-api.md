---
title: "Build AI agents with the Mistral Agents API"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/agents-api"
scraped: "2026-05-10T01:20:36.275280+00:00"
lastmod: "2026-01-14T11:04:13.113Z"
type: "sitemap"
---

# Build AI agents with the Mistral Agents API

**Source**: [https://mistral.ai/news/agents-api](https://mistral.ai/news/agents-api)

Build AI agents with the Mistral Agents API
Product
May 27, 2025
Mistral AI
Today we announce our new Agents API, a major step forward in making AI more capable, useful, and an active problem-solver.
Traditional language models excel at generating text but are limited in their ability to perform actions or maintain context. Our new Agents API addresses these limitations by combining Mistral's powerful language models with:
Built-in connectors for code execution, web search, image generation, and MCP tools
Persistent memory across conversations
Agentic orchestration capabilities
The Agents API complements our
Chat Completion API
by offering a dedicated framework that simplifies implementing agentic use cases. It serves as the backbone of enterprise-grade agentic platforms.
By providing a reliable framework for AI agents to handle complex tasks, maintain context, and coordinate multiple actions, the Agents API enables enterprises to use AI in more practical and impactful ways.
Mistral agents in action.
Explore the diverse applications of Mistral’s Agents API across various sectors:
Coding assistant with Github.
An agentic workflow built with Mistral's agents API where an agent interacts with Github and oversees a developer agent, powered by DevStral to write code. The agent is granted full authority over Github, showcasing automated software development task management.
Read our cookbook
Linear tickets assistant.
An intelligent task coordination assistant powered by our Agents API, using multi-server MCP architecture to transform call transcripts to PRDs to actionable Linear issues and track project deliverables.
Read our cookbook
Financial analyst.
A financial advisory agent constructed with our Agents API, orchestrating multiple MCP servers to source financial metrics, compile insights, and archive results securely.
Read our cookbook
Travel assistant.
A powerful AI travel assistant that helps users plan their trips, book accommodations, and manage travel needs.
Read our cookbook
Nutrition assistant.
An AI-powered food diet companion designed to help users establish goals, log meals, receive personalized food suggestions, track their daily achievements, and discover dining options that align with their nutritional targets.
Read our cookbook
Create an agent with built-in connectors and MCP tools.
Each agent can be equipped with powerful built-in connectors, which are tools that are deployed and ready for Agents to call on demand, and MCP tools:
Code execution
The Agents API can use the code execution connector, empowering developers to create agents that execute Python code in a secure sandboxed environment. This enables agents to tackle a wide range of tasks, including mathematical calculations and analysis, data visualization and plotting, and scientific computing.
Image generation
The image generation connector tool, powered by Black Forest Lab FLUX1.1 [pro] Ultra, enables agents to create images for diverse applications. This feature can be leveraged for various use cases such as generating visual aids for educational content, creating custom graphics for marketing materials, or even producing artistic images.
Document library
Document Library is a built-in connector tool that enables agents to access documents from Mistral Cloud. It powers the integrated RAG functionality, strengthening agents’ knowledge by leveraging the content of user-uploaded documents.
Web search
The Agents API offers web search as a connector, enabling developers to combine Mistral models with diverse, up-to-date information from web search, reputable news, and other sources. This integration facilitates the delivery of up-to-date, informed, evidence-supported responses.
Agents with web search capabilities show a significant improvement in performance. In the SimpleQA benchmark, Mistral Large and Mistral Medium with web search achieve scores of 75% and 82.32%, respectively, compared to 23% and 22.08% without web search (see figure below).
SimpleQA Accuracy (Higher is better)
MCP tools
The Agents API SDK can also leverage tools built on the Model Context Protocol (MCP)—an open, standardized protocol that enables seamless integration between agents and external systems. MCP tools provide a flexible and extensible interface for agents to access real-world context, including APIs, databases, user data, documents, and other dynamic resources. Check out the
Github
,
Financial Analyst
, and
Linear
MCP demos to learn how to use MCP tools with Mistral Agents in action.
Memory and context with stateful conversations.
The Agents API provides robust conversation management through a flexible and stateful conversation system. Each conversation retains its context, allowing for seamless and coherent interactions over time.
Conversation management
There are two ways to start a conversation:
With an Agent: Create a conversation with a specific agent_id to leverage its specialized capabilities.
Direct Access: Start a conversation by directly specifying the model and completion parameters, providing quick access to built-in connectors.
Each conversation maintains a structured history through conversation entries, ensuring that the context is preserved across interactions.
Stateful interactions and conversation branching
Developers are no longer required to monitor conversion history; they have the ability to view past conversations. They can always continue any conversation or initiate new conversation paths from any point.
Streaming output
The API also supports streaming outputs, both when starting a conversation and continuing a previous one. This feature allows for real-time updates and interactions.
Agent orchestration.
The true power of our Agents API lies in its ability to orchestrate multiple agents to solve complex problems. Through dynamic orchestration, agents can be added or removed from a conversation as needed—each one contributing its unique capabilities to tackle different parts of a problem.
Creating an agentic workflow
To build a workflow with handoffs, start by creating all necessary agents. You can create as many agents as needed, each with specific tools and models, to form a tailored workflow.
Agent handoffs
Once agents are created, define which agents can hand off tasks to others. For example, a finance agent might delegate tasks to a web search agent or a calculator agent based on the conversation's needs.
Handoffs enable a seamless chain of actions. A single request can trigger tasks across multiple agents, each handling specific parts of the request. This collaborative approach allows for efficient and effective problem-solving, unlocking powerful possibilities for real-world applications.
Get started.
To get started, check out our
docs
, create your first agent, and start building!
Share this article
More from Mistral AI
News
Models
AI Services
