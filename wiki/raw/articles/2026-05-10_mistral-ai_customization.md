---
title: "My Tailor is Mistral"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/customization"
scraped: "2026-05-10T01:20:04.903148+00:00"
lastmod: "2025-01-30T01:18:54.355Z"
type: "sitemap"
---

# My Tailor is Mistral

**Source**: [https://mistral.ai/news/customization](https://mistral.ai/news/customization)

My Tailor is Mistral
Research
Fine-tune and deploy your custom Mistral models using Mistral fine-tuning API and SDK.
Jun 5, 2024
Mistral AI team
Today, we're introducing model customization on la Plateforme, to bring performance, speed and fine editorial control to your AI application.
You can now easily and efficiently adapt Mistral AI models to your specific needs, reducing the cost and expertise required for customizing generative AI models at scale.
Whether you want to fine-tune Mistral AI models on your own infrastructure or leverage our proprietary fine-tuning techniques with our managed fine-tuning services, we've got you covered.
Fine-tuning is a powerful technique for customizing and improving the performance of LLMs, providing better responses, flexibility and efficiency to specific applications. When tailoring a smaller model to suit specific domains or use cases, it offers a way to match the performance of larger models, reducing deployment costs and improving application speed.
Tailor Mistral models at home, on la Plateforme, and with the team
We're proud to announce three different entry points for specialising Mistral AI models.
Open-source fine-tuning SDK for Mistral models
For developers who want to fine-tune Mistral's open-source models on their infrastructure, we've released
mistral-finetune
, a lightweight and efficient codebase for fine-tuning.
Our codebase is built on the LoRA training paradigm, which allows for memory-efficient and performant fine-tuning. With mistral-finetune, you can fine-tune all our open-source models on your infrastructure without sacrificing performance or memory efficiency.
Serverless fine-tuning services on la Plateforme
To further facilitate fine-tuning without infrastructure hassle, we're introducing new fine-tuning services on la Plateforme.
These services leverage Mistral's unique fine-tuning techniques, refined through extensive research and development, to allow fast and cost-effective model adaptation and effective deployment of fine-tuned models. It's a new step in our mission to expose advanced science methods to AI application developers. We use LoRA adapters under the hood to prevent forgetting base model knowledge and allow for efficient serving.
Figure 1: Mistral LoRA finetuning is more efficient while having similar performance than full Fine-tuning for both Mistral 7B and Mistral Small:  The evaluation metric is an normalized internal benchmark very similar to the MTBench evaluation (1 being the reference to full Fine-tuning of Mistral Small).
Traditionally, fine-tuned models have required a significant investment for enterprises. Our expertise in the field enables us to offer fine-tuning in a highly efficient way, which translates into lower costs for both training and serving.
Today, our fine-tuning services are compatible with Mistral 7B and Mistral Small. Thus, users who are leveraging one of these models can immediately use our API to customise our models effectively to meet their specific needs. We will add new models to our finetuning services over the coming weeks.
Get started with by registering on
la Plateforme
, and discover our guide and our tutorial on how to build an application with a custom LLM.
Custom training services
Our custom training services involve fine-tuning Mistral AI models on a customer's specific applications using their own proprietary data. This approach enables the creation of highly specialized and optimized models for their particular domain. We propose advanced techniques such as continuous pretraining to include proprietary knowledge within the model weights themselves.
These custom training services are available to a select group of customers and are tailored to meet their specific needs. Feel free to contact
our sales team
to know more.
Join our community of builders
If you're looking to dive in and experiment with our brand new fine-tuning API, be sure to participate in the Mistral Fine-Tuning Hackathon, taking place from June 5 - 30, 2024.
You can find more details about the hackathon here
.
Share this article
More from Mistral AI
News
Models
AI Services
