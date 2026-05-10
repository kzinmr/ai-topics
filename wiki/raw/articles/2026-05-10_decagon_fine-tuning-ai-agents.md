---
title: "Engineering fast, performant AI agents through fine-tuning"
source: "Decagon Blog"
url: "https://decagon.ai/blog/fine-tuning-ai-agents"
scraped: "2026-05-10T01:19:40.228418+00:00"
lastmod: "None"
type: "sitemap"
---

# Engineering fast, performant AI agents through fine-tuning

**Source**: [https://decagon.ai/blog/fine-tuning-ai-agents](https://decagon.ai/blog/fine-tuning-ai-agents)

Introducing Proactive Agents.
Learn more
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Build
AOPs
Workflows for AI agents
Integrations
Support tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & Reporting
Voice of the Customer
Watchtower
Always-on QA
Suggestions
AI-powered knowledge
Industries
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
AI and the next generation of customer experience
Why exceptional service is the new brand differentiator as AI reshapes consumer expectations.
Spring ’26 Release: Proactive Agents
See how user memory, outbound voice, and Agent Workbench can help you build stronger customer relationships
Company
About
Careers
Security
Sign in
Sign in
Get a demo
Sign in
Get a demo
Product Update
Company news
Technology & research
Industry
Technology & Research
Blog
/
Engineering fast, performant AI agents through fine-tuning
Engineering fast, performant AI agents through fine-tuning
November 21, 2025
Written by
Max Lu
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
At Decagon, we don't rely on a single, monolithic model to power our agents. Instead, our architecture is built around a network of specialized models that work in coordination. Each is responsible for a distinct function, such as interpreting user intent, executing workflows, detecting
hallucinations
, or determining when to escalate to a human. This orchestration allows our agents to deliver precise, reliable, and controllable behavior, which a single large model can't guarantee on its own.
Great AI-driven experiences prioritize accuracy above all, because even a fast response is useless if it's wrong. But latency still matters, since the right answer must arrive quickly enough to keep the experience seamless and engaging. This is especially true for voice channels and other real-time applications, where every millisecond matters. Every component model in the agent architecture must be optimized for both performance and correctness.
Fine-tuning is critical to achieving that optimization. The process transforms general-purpose models into highly specialized experts that not only operate faster but also outperform larger frontier models on their targeted tasks. By fine-tuning smaller models for specific functions, we deliver both the low latency customers expect and the high reliability they depend on.
Why off-the-shelf models fall short
General-purpose LLMs are trained to handle the broadest possible range of topics, not the narrow, high-precision tasks that our customer-facing agents require. For example, choosing the right
Agent Operating Procedure (AOP)
based on a user's query is not something an off-the-shelf model has any inherent understanding of, as it wasn't part of its original training data. Without fine-tuning, these models struggle to execute customer-facing workflows reliably.
Beyond domain understanding, every off-the-shelf model family has its own trade-offs when used in an agentic system. Larger models tend to follow instructions more reliably and exhibit stronger reasoning, but they come with high latency, making them impractical for real-time experiences like voice. On the flip side, smaller models are lightweight and fast but lack the depth of reasoning and necessary instruction-following capabilities.
Therefore, the best way to achieve both speed and accuracy is to start with a smaller model and fine-tune it for each task within the agent architecture. Fine-tuning allows us to teach these compact models exactly what they need to know, while still cleaning and filtering training data to remove PII and protect customer IP. The result is a set of specialized systems that run efficiently, respond instantly, and perform their roles with accuracy exceeding much larger models.
Our approach to fine-tuning models
To optimize each model for its role within the agent, we rely on two complementary techniques: supervised fine-tuning (SFT) and reinforcement learning (RL). Both approaches adapt base models for specialized use cases, but they excel in different ways depending on the nature of the task.
Supervised fine-tuning trains a model on curated examples of the desired behavior. By providing input-output pairs, we effectively show the model what “good” looks like so it can adjust its weights accordingly. For example, we might train a workflow-selection model on historical user queries paired with the correct AOP chosen in each case. Over time, the model generalizes these patterns and applies them to new inputs. SFT is efficient, predictable, and offers a clear, interpretable path from training data to behavior.
Reinforcement learning is best suited for tasks where we can define and measure a quantifiable reward signal. Instead of mimicking labeled outputs, the model learns to maximize expected reward using techniques like GRPO, GSPO, or DPO. Rewards may come from automated metrics, human preference data, or a learned reward model. Because RL can learn from preferences and task-level feedback rather than strict gold labels, it provides more flexibility in the data we depend on and allows us to optimize more abstract behaviors. It also enables models to generalize beyond the training set by exploring behaviors not explicitly represented in the original dataset. The tradeoff is that RL training can be unstable, reward models are hard to build, and it is more computationally demanding.
These two approaches aren't mutually exclusive. We typically begin with SFT to establish a strong behavioral foundation, then layer RL to sharpen decision boundaries and optimize for measurable outcomes. While this combined approach increases cost and complexity, applied selectively it delivers substantial gains in real-world reliability.
The power of model independence
Fine-tuning isn't a one-time optimization, but a continuous process of
evaluation
and refinement. Each deployment reveals new insights into how our agents perform in real-world conditions, and those insights feed directly back into model specialization. Because our architecture is modular, we can fine-tune individual components without disrupting the entire system. This flexibility allows us to adopt new base models quickly and evolve our performance rapidly.
Our approach also remains model-agnostic by design. We experiment across multiple providers, constantly evaluating which offer the best blend of reasoning, latency, and cost efficiency for each task. By combining smaller, specialized models with careful fine-tuning and orchestration, we deliver an experience that customers can trust to handle complex interactions in real time.
We're continuing to push the limits of what agents can handle in real-world deployments, and our AI research team is expanding to support that goal. If you're passionate about building the next generation of adaptive, high-performance AI agents, check out our careers page.
Recent posts
Bringing the AI concierge to Australia
Decagon is opening a new office in Sydney, Australia
Introducing automatic optimization and Root Cause Analysis
Today, we’re excited to announce two new capabilities to help you rapidly improve your agent’s performance.
Bringing Decagon’s AI concierge solution to Google Cloud Marketplace
We're excited to announce that Decagon is now available on Google Cloud Marketplace.
Deliver the concierge experiences your customers deserve
Get a demo
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
