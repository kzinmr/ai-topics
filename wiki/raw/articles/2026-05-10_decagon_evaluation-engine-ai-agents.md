---
title: "The evaluation engine behind Decagon’s AI agents"
source: "Decagon Blog"
url: "https://decagon.ai/blog/evaluation-engine-ai-agents"
scraped: "2026-05-10T01:19:40.110443+00:00"
lastmod: "None"
type: "sitemap"
---

# The evaluation engine behind Decagon’s AI agents

**Source**: [https://decagon.ai/blog/evaluation-engine-ai-agents](https://decagon.ai/blog/evaluation-engine-ai-agents)

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
The evaluation engine behind Decagon’s AI agents
The evaluation engine behind Decagon’s AI agents
July 7, 2025
Written by
Max Lu
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
At Decagon, we build AI agents for enterprises where every customer interaction is high-stakes, with the potential to shape satisfaction, loyalty, and business outcomes in real time. That means we need to continuously evaluate our models to optimize agent performance and ensure they deliver concierge-quality support while improving key metrics like CSAT and resolution rate.
Our AI agents are powered by a diverse set of models and orchestrated AI workflows that work in tandem to deliver exceptional performance. We use models from
OpenAI
,
Anthropic
,
Gemini
, and other providers, alongside our own fine-tuned versions of open-source and commercial models. We rigorously assess every component of the agent, from response generation to retrieval to safety. This comprehensive evaluation process is what enables us to build agents that earn customer trust and drive real results.
Inside the Decagon Model Evaluation Loop
We evaluate every model and system component through a two-phased framework: offline evaluation, followed by online A/B testing. This structured methodology ensures that only the most effective and reliable configurations are deployed to production to serve 100% of user traffic.
Each of these configurations, known as experiment variants, represent different approaches to agent behavior and performance. An experiment variant might involve anything from a new system prompt to an entirely new language model. By evaluating a wide variety of variants, we’re able to stress-test design decisions, surface tradeoffs, and identify the most promising approaches to building agents.
Offline evaluation: scalable, continuous, and stratified
Every variant must demonstrate consistent performance offline before it is eligible for online testing. Our offline evaluation process is structured around two core tracks, each providing a distinct but complementary signal to help assess model performance before deployment.
LLM-as-judge evaluation
Using an
LLM-as-judge
system, we evaluate structured triplets consisting of a user query, the context provided to the model, and the model's generated response. These triplets are drawn from real-world interactions, ensuring that our evaluation process reflects authentic user needs and scenarios. This format allows us to isolate how well the model is understanding the question, using relevant context, and crafting a meaningful answer.
Each response is scored against several key criteria as part of a scalable, continuous, and stratified evaluation process. We sample across key dimensions, such as issue types and customer segments, to ensure balanced testing. The criteria include aspects like:
Relevance:
Does the response directly address the user’s question?
Correctness:
Does the response reflect accurate information?
Naturalness:
Does the response sound human and conversational?
Empathy:
Does the response demonstrate understanding and care?
We also audit a subset of triplets with human labellers to further validate the LLM-as-judge scoring. These audits provide an extra layer of confidence and help us catch edge cases or nuances that automated evaluations might miss.
Ground truth evaluation
In parallel, we evaluate responses against a ground truth evaluation set: a curated collection of user queries with ideal responses, labeled by human experts. This high-confidence benchmark allows us to test for factuality and intent coverage with precision. Our evaluation framework also extends well beyond response generation; we apply similar rigor across the full spectrum of our AI workflows to ensure each component performs reliably and aligns with user and business needs
The combination of scalable LLM-based judgment and curated ground truth benchmarking gives us a fast, nuanced, and reliable evaluation signal before any model sees production traffic.
Online A/B testing: real-world performance evaluation
Once a variant passes offline thresholds, we move it into controlled online A/B testing with real customers. We manage rollouts by gradually increasing traffic to the variant group as performance improves, allowing us to limit risk while gaining signal. Customers can also opt out of experimentation, giving them full control over model exposure during evaluation.
During this phase, we track impact on business-critical metrics like CSAT and resolution rate through a unified evaluation view. This stage provides the ultimate signal: how well the model performs in live, unpredictable, customer-facing settings. To ensure trustworthiness of the results, we monitor closely for noise, novelty effects, and performance drift over time.
Continuous feedback and improvement
Evaluation doesn't stop once a variant ships. Insights from every phase feed back into the experiment loop: improving prompts, upgrading models, and refining overall agent behaviors.
Importantly, we evaluate more than just response generation. Our approach benchmarks and stress-tests the entire agent architecture, from knowledge base retrieval to reasoning to safety. Delivering exceptional customer experiences isn’t just about answering questions, but orchestrating the right system behaviors, end to end.
Beyond evaluation, Decagon’s platform also provides built-in tools that give teams visibility and control over agent performance. Features like
Watchtower
for always-on QA and Ask AI for natural language analysis of customer conversations help CX teams monitor and improve outcomes at scale.
If you’d like to see how our evaluation loop powers real-world performance,
sign up for a demo
to learn more about Decagon.
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
