---
title: "Announcing the Agent2Agent Protocol (A2A)"
source: "https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/"
date_published: "2025-04-09"
date_ingested: "2026-06-03"
type: raw_article
tags: [raw-article]
---

# Announcing the Agent2Agent Protocol (A2A)

**Source:** <https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/>
**Published:** 2025-04-09

Announcing the Agent2Agent Protocol (A2A)
            
            
            - Google Developers Blog

Cloud

Announcing the Agent2Agent Protocol (A2A)

APRIL 9, 2025

Rao Surapaneni

VP and GM

Business Application Platform

Miku Jha

Director, AI/ML Partner Engineering

Google Cloud

Michael Vakoc

Product Manager

Google Cloud

Todd Segal

Principal Engineer

Business Application Platform

Share

Facebook

Twitter

LinkedIn

Mail

A new era of Agent Interoperability

AI agents offer a unique opportunity to help people be more productive by autonomously handling many daily recurring or complex tasks. Today, enterprises are increasingly building and deploying autonomous agents to help scale, automate and enhance processes throughout the workplace–from ordering new laptops, to aiding customer service representatives, to assisting in supply chain planning.

To maximize the benefits from agentic AI, it is critical for these agents to be able to collaborate in a dynamic, multi-agent ecosystem across siloed data systems and applications. Enabling agents to interoperate with each other, even if they were built by different vendors or in a different framework, will increase autonomy and multiply productivity gains, while lowering long-term costs.

Today, we’re launching a new, open protocol called Agent2Agent (A2A), with support and contributions from more than 50 technology partners

like Atlassian, Box, Cohere, Intuit, Langchain, MongoDB, PayPal, Salesforce, SAP, ServiceNow, UKG and Workday; and leading service providers including Accenture, BCG, Capgemini, Cognizant, Deloitte, HCLTech, Infosys, KPMG, McKinsey, PwC, TCS, and Wipro. The A2A protocol will allow AI agents to communicate with each other, securely exchange information, and coordinate actions on top of various enterprise platforms or applications. We believe the A2A framework will add significant value for customers, whose AI agents will now be able to work across their entire enterprise application estates.

This collaborative effort signifies a shared vision of a future when AI agents, regardless of their underlying technologies, can seamlessly collaborate to automate complex enterprise workflows and drive unprecedented levels of efficiency and innovation.

A2A is an open protocol that complements Anthropic's Model Context Protocol (MCP), which provides helpful tools and context to agents. Drawing on Google's internal expertise in scaling agentic systems, we designed the A2A protocol to address the challenges we identified in deploying large-scale, multi-agent systems for our customers. A2A empowers developers to build agents capable of connecting with any other agent built using the protocol and offers users the flexibility to combine agents from various providers. Critically, businesses benefit from a standardized method for managing their agents across diverse platforms and cloud environments. We believe this universal interoperability is essential for fully realizing the potential of collaborative AI agents.

A2A design principles

A2A is an open protocol that provides a standard way for agents to collaborate with each other, regardless of the underlying framework or vendor. While designing the protocol with our partners, we adhered to five key principles:

Embrace agentic capabilities

: A2A focuses on enabling agents to collaborate in their natural, unstructured modalities, even when they don’t share memory, tools and context. We are enabling true multi-agent scenarios without limiting an agent to a “tool.”

Build on existing standards:

The protocol is built on top of existing, popular standards including HTTP, SSE, JSON-RPC, which means it’s easier to integrate with existing IT stacks businesses already use daily.

Secure by default

: A2A is designed to support enterprise-grade authentication and authorization, with parity to OpenAPI’s authentication schemes at launch.

Support for long-running tasks:

We designed A2A to be flexible and support scenarios where it excels at completing everything from quick tasks to deep research that may take hours and or even days when humans are in the loop. Throughout this process, A2A can provide real-time feedback, notifications, and state updates to its users.

Modality agnostic:

The agentic world isn’t limited to just text, which is why we’ve designed A2A to support various modalities, including audio and video streaming.

How A2A works

A2A facilitates communication between a "client" agent and a “remote” agent. A client agent is responsible for formulating and communicating tasks, while the remote agent is responsible for acting on those tasks in an attempt to provide the correct information or take the correct action. This interaction involves several key capabilities:

Capability discovery:

Agents can advertise their capabilities using an “Agent Card” in JSON format, allowing the client agent to identify the best agent that can perform a task and leverage A2A to communicate with the remote agent.

Task management:

The communication between a client and remote agent is oriented towards task completion, in which agents work to fulfill end-user requests. This “task” object is defined by the protocol and has a lifecycle. It can be completed immediately or, for long-running tasks, each of the agents can communicate to stay in sync with each other on the latest status of completing a task. The output of a task is known as an “artifact.”

Collaboration:

Agents can send each other messages to communicate context, replies, artifacts, or user instructions.

User experience negotiation:

Each message includes “parts,” which is a fully formed piece of content, like a generated image. Each part has a specified content type, allowing client and remote agents to negotiate the correct format needed and explicitly include negotiations of the user’s UI capabilities–e.g., iframes, video, web forms, and more.

See the full details of how the protocol works in our

draft specification

A real-world example: candidate sourcing

Sorry, your browser doesn't support playback for this video

right click to view in new tab

Hiring a software engineer can be significantly simplified with A2A collaboration. Within a unified interface like Agentspace, a user (e.g., a hiring manager) can task their agent to find candidates matching a job listing, location, and skill set. The agent then interacts with other specialized agents to source potential candidates. The user receives these suggestions and can then direct their agent to schedule further interviews, streamlining the candidate sourcing process. After the interview process completes, another agent can be engaged to facilitate background checks. This is just one example of how AI agents need to collaborate across systems to source a qualified job candidate.

The future of agent interoperability

A2A has the potential to unlock a new era of agent interoperability, fostering innovation and creating more powerful and versatile agentic systems. We believe that this protocol will pave the way for a future where agents can seamlessly collaborate to solve complex problems and enhance our lives.

We’re committed to building the protocol in collaboration with our partners and the community in the open. We’re releasing the protocol as open source and setting up clear pathways for contribution.

Review the

full specification draft

, try out code samples, and see example scenarios on the

A2A website

and learn how you can contribute.

We are working with partners to launch a production-ready version of the protocol later this year.

Feedback from our A2A partners

We're thrilled to have a growing and diverse ecosystem of partners actively contributing to the definition of the A2A protocol and its technical specification. Their insights and expertise are invaluable in shaping the future of AI interoperability.

Here's what some of our key partners are saying about the A2A protocol:

Technology & Platform Partners

ask-ai.com

Ask-AI is excited to collaborate with Google on the A2A protocol, shaping the future of AI interoperability and seamless agent collaboration, advancing its leadership in Enterprise AI for Customer Experience.

– CEO Alon Talmor PhD

Atlassian

With Atlassian's investment in Rovo agents, the development of a standardized protocol like A2A will help agents successfully discover, coordinate, and reason with one another to enable richer forms of delegation and collaboration at scale.

– Brendan Haire VP, Engineering of AI Platform. Atlassian

Articul8

At Articul8, we believe that AI must collaborate and interoperate to truly scale across the enterprise. We’re excited to support the development of the A2A interoperability protocol – an initiative that aligns perfectly with our mission to deliver domain-specific GenAI capabilities that seamlessly operate across complex systems and workflows. We’re enabling Articul8's ModelMesh (an 'Agent-of-Agents') to treat A2A as a first-class citizen, enabling secure, seamless communication between intelligent agents.

Arun Subramaniyan, Founder & CEO of Articul8

Arize AI

Arize AI is proud to partner with Google as a launch partner for the A2A interoperability protocol, advancing seamless, secure interaction across AI agents as part of Arize's commitment to open-source evaluation and observability frameworks positions.

– Jason Lopatecki, Cofounder & CEO, Arize AI

BCG

BCG helps redesign organizations with intelligence at the core. Open and interoperable capabilities like A2A can accelerate this, enabling sustained, autonomous competitive advantage.

Djon Kleine, Managing Director & Partner at BCG

Box

We look forward to expanding our partnership with Google to enable Box agents to work with Google Cloud’s agent ecosystem using A2A, innovating together to shape the future of AI agents while empowering organizations to better automate workflows, lower costs, and generate trustworthy AI outputs.

– Ketan Kittur, VP Product Management, Platform and Integrations at Box

C3 AI

At C3 AI, we believe that open, interoperable systems are key to making Enterprise AI work and deliver value in the real world–and A2A has the potential to help customers break down silos and securely enable AI agents to work together across systems, teams, and applications.

Nikhil Krishnan - C3 AI SVP and Chief Technology Officer, Data Science

Chronosphere

A2A will enable reliable and secure agent specialization and coordination to open the door for a new era of compute orchestration, empowering companies to deliver products and services faster, more reliably, and enabling them to refocus their engineering efforts on driving innovation and value.

– Rob Skillington, Founder /CTO

Cognizant

"As a pioneer in enterprise multi-agent systems, Cognizant is committed and actively pursuing agent interoperability as a critical requirement for our clients."

Babak Hodjat, CTO - AI

Cohere

At Cohere, we’re building the secure AI infrastructure enterprises need to adopt autonomous agents confidently, and the open A2A protocol ensures seamless, trusted collaboration—even in air-gapped environments—so that businesses can innovate at scale without compromising control or compliance.

– Autumn Moulder, VP of Engineering at Cohere

Confluent

A2A enables intelligent agents to establish a direct, real-time data exchange, simplifying complex data pipelines to fundamentally change how agents communicate and facilitate decisions.

– Pascal Vantrepote, Senior Director of Innovation, Confluent

Cotality (formerly CoreLogic)

A2A opens the door to a new era of intelligent, real-time communication and collaboration, which Cotality will bring to clients in home lending, insurance, real estate, and government—helping them to improve productivity, speed up decision-making.

– Sachin Rajpal, Managing Director, Data Solutions, Cotality

DataStax

DataStax is excited to be part of A2A and explore how it can support Langflow, representing an important step toward truly interoperable AI systems that can collaborate on complex tasks spanning multiple environments.

– Ed Anuff, Chief Product Officer, DataStax

Datadog

We're excited to see Google Cloud introduce the A2A protocol to streamline the development of sophisticated agentic systems, which will help Datadog enable its users to build more innovative, optimized, and secure agentic AI applications.

– Yrieix Garnier, VP of Product at Datadog

Elastic

Supporting the vision of open, interoperable agent ecosystems, Elastic looks forward to working with Google Cloud and other industry leaders on A2A and providing its data management and workflow orchestration experience to enhance the protocol.

– Steve Kearns, GVP and GM of Search, Elastic

GrowthLoop

A2A has the potential to accelerate GrowthLoop's vision of Compound Marketing for our customers—enabling our AI agents to seamlessly collaborate with other specialized agents, learn faster from enterprise data, and rapidly optimize campaigns across the marketing ecosystem, all while respecting data privacy on the customer's cloud infrastructure.

– Anthony Rotio, Chief Data Strategy Officer, GrowthLoop

Harness

Harness is thrilled to support A2A and is committed to simplifying the developer experience by integrating AI-driven intelligence into every stage of the software lifecycle, empowering teams to gain deeper insights from runtime data, automate complex workflows, and enhance system performance.

– Gurashish Brar, Head of Engineering at Harness.

Incorta

Incorta is excited to support A2A and advance agent communication for customers,making the future of enterprise automation smarter, faster, and truly data-driven.

– Osama Elkady CEO Incorta

Intuit

Intuit strongly believes that an open-source protocol such as A2A will enable complex agent workflows, accelerate our partner integrations, and move the industry forward with cross-platform agents that collaborate effectively.

– Tapasvi Moturu, Vice President, Software Engineering for Agentic Frameworks, at Intuit

JetBrains

We’re excited to be a launch partner for A2A, an initiative that enhances agentic collaboration and brings us closer to a truly multi-agent world, empowering developers across JetBrains IDEs, team tools, and Google Cloud.

– Vladislav Tankov, Director of AI, JetBrains

JFrog

JFrog is excited to join the A2A protocol, an initiative we believe will help to overcome many of today’s integration challenges and be a key driver for the next generation of agentic applications.

– Yoav Landman, CTO and Co-founder, JFrog

LabelBox

A2A is a key step toward realizing the full potential of AI agents, supporting a future where AI can truly augment human capabilities, automate complex workflows and drive innovation.

– Manu Sharma Founder & CEO

LangChain

LangChain believes agents interacting with other agents is the very near future, and we are excited to be collaborating with Google Cloud to come up with a shared proto

[... truncated ...]
