---
title: "Devstral"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/devstral"
scraped: "2026-05-10T01:20:37.783667+00:00"
lastmod: "2025-05-21T22:15:30.387Z"
type: "sitemap"
---

# Devstral

**Source**: [https://mistral.ai/news/devstral](https://mistral.ai/news/devstral)

Devstral
Research
Introducing the best open-source model for coding agents.
May 21, 2025
Mistral AI
Today we introduce Devstral, our agentic LLM for software engineering tasks. Devstral is built under a collaboration between Mistral AI and
All Hands AI
🙌, and outperforms all open-source models on SWE-Bench Verified by a large margin. We release Devstral under the Apache 2.0 license.
Agentic LLMs for software development
While typical LLMs are excellent at atomic coding tasks such as writing standalone functions or code completion, they currently struggle to solve real-world software engineering problems. Real-world development requires contextualising code within a large codebase, identifying relationships between disparate components, and identifying subtle bugs in intricate functions.
Devstral is designed to tackle this problem. Devstral is trained to solve real GitHub issues; it runs over code agent scaffolds such as OpenHands or SWE-Agent, which define the interface between the model and the test cases. Here, we show Devstral’s performance on the popular SWE-Bench Verified benchmark, a dataset of 500 real-world GitHub issues which have been manually screened for correctness.
Devstral achieves a score of 46.8% on SWE-Bench Verified, outperforming prior open-source SoTA models by more than 6% points. When evaluated under the same test scaffold (OpenHands, provided by
All Hands AI
🙌), Devstral exceeds far larger models such as Deepseek-V3-0324 (671B) and Qwen3 232B-A22B.
In the table below, we also compare Devstral to closed and open models evaluated under any scaffold (including ones custom for the model). Here, we find that Devstral achieves substantially better performance than a number of closed-source alternatives. For example, Devstral surpasses the recent GPT-4.1-mini by over 20%.
Versatile: local deployment ↔️ enterprise use ↔️ copilots
Devstral is light enough to run on a single RTX 4090 or a Mac with 32GB RAM, making it an ideal choice for local deployment and on-device use. Coding platforms such as
OpenHands
can allow the model to interact with local codebases and provide fast resolution to issues. To try it yourself, view the
documentation
or
tutorial video
.
The performance of the model also makes it a suitable choice for agentic coding on privacy-sensitive repositories in enterprises, especially ones subject to stringent security and compliance requirements.
Finally, if you’re building or using an agentic coding IDE, plugin, or environment, Devstral is a great choice to add to your model selector.
Availability
We release this model for free under an Apache 2.0 license for the community to build on, customize, and accelerate autonomous software development. To try it for yourself, head over to our
model card
.
The model is also available on our API under the name devstral-small-2505 at the same price as Mistral Small 3.1: $0.1/M input tokens and $0.3/M output tokens.
Should you choose to self-deploy, you can download the model on
HuggingFace
,
Ollama
,
Kaggle
,
Unsloth
,
LM Studio
starting today.
For enterprise deployments that require fine-tuning on private codebases, or higher-fidelity customization such as continued pre-training or distilling Devstral’s capabilities into other models, please
contact us
to connect with our applied AI team.
What’s next
Devstral is a research preview and we welcome feedback! We’re hard at work building a larger agentic coding model that will be available in the coming weeks.
Interested in discussing how we can help your team put Devstral to use, and about our portfolio of models, products and solutions?
Contact us
and we’ll be happy to help.
Share this article
More from Mistral AI
News
Models
AI Services
