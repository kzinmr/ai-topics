---
title: "Upgrading agentic coding capabilities with the new Devstral models"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/devstral-2507"
scraped: "2026-05-10T01:20:46.119742+00:00"
lastmod: "2025-07-10T14:25:05.890Z"
type: "sitemap"
---

# Upgrading agentic coding capabilities with the new Devstral models

**Source**: [https://mistral.ai/news/devstral-2507](https://mistral.ai/news/devstral-2507)

Upgrading agentic coding capabilities with the new Devstral models
Research
Jul 10, 2025
Mistral AI
Today, we introduce Devstral Medium, as well as an upgrade to Devstral Small. These models are released under the collaboration between Mistral AI and
All Hands AI
🙌, with a strong emphasis on generalization to different prompts and agentic scaffolds.
The new Devstral Small 1.1 is released under the Apache 2.0 license, and is state-of-the-art amongst open models for code agents. Devstral Medium is available through our API, and sets a new point on the cost/performance pareto frontier, surpassing Gemini 2.5 Pro and GPT 4.1 for a quarter of the price.
Devstral Small 1.1
As with the previous version of Devstral Small, we release Devstral Small 1.1 under the Apache 2.0 license. While the architecture remains the same, with only 24B parameters, Devstral Small 1.1 comes with significant improvements over its predecessor:
Enhanced Performance
Devstral Small 1.1 achieves a score of 53.6% on SWE-Bench Verified, and sets a new state-of-the-art for open models without test-time scaling.
Versatility and Generalization
Devstral Small 1.1 excels when paired with OpenHands, and also demonstrates better generalization to different prompts and coding environments. Its versatility is further enhanced by supporting both Mistral function calling and XML formats, making it adaptable to a wide range of applications and agentic scaffolds.
Devstral Medium
Devstral Medium builds upon the strengths of Devstral Small and takes performance to the next level with a score of 61.6% on SWE-Bench Verified. Devstral Medium is available through our public API, and offers exceptional performance at a competitive price point, making it an ideal choice for businesses and developers looking for a high-quality, cost-effective model.
For those who prefer on-premise solutions, Devstral Medium can be directly deployed on private infrastructure, offering enhanced data privacy and control. We also support custom finetuning for Devstral Medium, allowing enterprises to customize the model for specific use cases, and achieve optimal performance tailored to their specific requirements.
Availability
Both models are available through our API under the the following names:
devstral-small-2507 at the same price as Mistral Small 3.1: $0.1/M input tokens and $0.3/M output tokens.
devstral-medium-2507 at the same price as Mistral Medium 3: $0.4/M input tokens and $2/M output tokens.
We release Devstral Small 1.1 under the Apache 2.0 license for the community to build on, customize, and accelerate autonomous software development. To try it for yourself, head over to our
model card
.
Devstral Medium will also be available on
Mistral Code
for enterprise customers and on our
finetuning API
. To deploy and customize the model in your environment, please
contact us
.
We are dedicated to open-sourcing our most accessible and impactful models, ensuring the open-source community can easily utilize and benefit from our advanced technology. While Devstral Small is easily usable for local deployment and available under the Apache 2.0 license for everyone to use and build upon, Devstral Medium is available on our API and offers high performance for developers and enterprises.
Share this article
More from Mistral AI
News
Models
AI Services
