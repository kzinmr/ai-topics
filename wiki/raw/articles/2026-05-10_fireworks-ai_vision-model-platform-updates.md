---
title: "Vision Model Platform Updates: Enhanced Capabilities and New Features"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/vision-model-platform-updates"
scraped: "2026-05-10T01:21:12.964838+00:00"
lastmod: "2025-06-23T18:47:37.000Z"
type: "sitemap"
---

# Vision Model Platform Updates: Enhanced Capabilities and New Features

**Source**: [https://fireworks.ai/blog/vision-model-platform-updates](https://fireworks.ai/blog/vision-model-platform-updates)

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
Vision Model Platform Updates
Vision Model Platform Updates: Enhanced Capabilities and New Features
PUBLISHED
6/12/2025
Table of Contents
Why Fireworks
New Model Additions: Llama 4 Scout & Maverick, InternVL3, RolmOCR
Existing Vision Model Portfolio
Prompt Caching Support
Customize Your Vision Models
Get Started Today
Table of Contents
Table of Contents
Why Fireworks
New Model Additions: Llama 4 Scout & Maverick, InternVL3, RolmOCR
Existing Vision Model Portfolio
Prompt Caching Support
Customize Your Vision Models
Get Started Today
Table of Contents
Enterprises process massive amounts of unstructured visual data daily—from scanned documents and medical records to product images and screenshots. Traditional text-only models leave this rich visual information untapped, missing opportunities to build rich digital experiences and unlock new business value.
Many applications use the vision model platform on Fireworks to solve problems very innovatively. We have seen many moonshot projects deemed impossible a year ago become a reality.
•
Medical systems
use VLMs to solve complex eHR integration challenges by reading from a computer screen in real time – this becomes the new integration interface, instead of very messy software level integration across hundreds of variations.
•
E-commerce marketplaces
use VLMs to automate product catalog cleansing, deduplication, correction, and in return boost search and recommendation relevance to yield higher revenue.
•
Insurance claim systems
use a combination of VLMs and LLMs to process claims with pictures of the incidents or medical bills, and then create legal documents describing or even analyzing the claim. This significantly accelerates the claim processing speed and makes even same day end to end claim processing possible.
•
Vibe designing
can start with images instead of prompts where images are much richer in describing the design idea along with the subtlety. This flow typically goes through a combination of VLM and LLM, which generates code, which then creates the visual.
•
General RAG systems
increasingly use VLMs to extract structured information from images, diagrams, documents, and interfaces - turning unstructured visual content into indexable knowledge. For example, screenshots of dashboards, tables in scanned PDFs, or annotated charts can be parsed into structured triples or JSON-like representations, enabling natural language queries over visual data. This opens the door to search and reasoning over assets that were previously siloed in images.
•
Computer use agents
leverage VLMs to autonomously navigate and interact with any software interface by visually understanding screen elements, clicking buttons, and executing multi-step workflows - essentially automating tasks across applications without needing APIs or custom integrations, making them ideal for legacy systems and complex cross-platform processes.
Fireworks provides a convenient OpenAI-compatible API to access VLMs. You simply specify the input image and the text prompt in the same multi-turn chat context as other models.
In this example, we can see that we are using Qwen 2.5 VL to generate ecommerce product descriptions from their images, and also tasking it with the downstream task of localization into several languages.
When you combine vision models with the rest of Fireworks' multimodal capabilities—including transcription and image generation —enterprises can tap into the rich, diverse data they already have and compose it together in powerful new ways. With Fireworks' vision models, transcription capabilities, and ASR models, businesses can finally break down data silos—analyzing customer support conversations alongside product images, processing financial documents that combine charts and text, or building intelligent systems that understand both what users say and show. This integrated approach unlocks the full value of enterprise data assets through a single platform.
A healthcare organization can ingest documents medical records and output structured outputs:
Then analyze transcripts from patient-doctor conversations captured through Fireworks' ASR models, and patient X-rays through vision models, then combine these insights using a large language model to send insights to doctors and healthcare professionals.
Why Fireworks
We were the first to build a
commercially permissive OSS vision model
. Since then, we've significantly expanded our vision model capabilities with new models, efficiency improvements, and platform updates that make visual AI faster and more accessible than ever.
Built on the same FireAttention serving stack that powers our LLMs, Fireworks delivers unmatched speed for real-time visual intelligence applications. Our diverse model portfolio lets you choose the perfect balance of capability, cost, and speed for your use case.
Major healthcare and insurance companies use Fireworks to process medical records in real-time at 100x lower cost and 1.5x faster speed than GPT-4o.
In the past 6 months, Fireworks has processed 228 Billion VLM tokens and 104 Million VLM requests demonstrating how far we've come since pioneering the first commercially permissive OSS vision model.
New Model Additions: Llama 4 Scout & Maverick, InternVL3, RolmOCR
Since May we have added more models to our platform giving developers additional choices to match different workloads and hardware budgets.
•
Llama 4 Scout
&
Maverick
– state-of-the-art multimodal vision models with stronger image comprehension, multi-step vision-text reasoning, object detection, and benchmark performance.
•
InternVL3
– leading open-source vision-language model with standout reasoning ability.
•
RolmOCR
– ultra-light, fast OCR engine that keeps high accuracy across varied document formats.
These additions will provide developers with even more options for different use cases and computational requirements.
Existing Vision Model Portfolio
Our comprehensive vision model lineup also includes:
•
Qwen 2.5-VL
– Best-in-class performance for complex visual reasoning and understanding
•
Llama 3.2 Vision
– Robust multimodal capabilities with strong image understanding
•
FireLlava
–
The first commercially permissive OSS model
•
Phi-3.5 Vision
– Blazing fast inference for real-time vision applications
•
Fireworks-OCR - Super fast OCR model for converting image with text to structure HTML output
These additions provide developers with even more options for different use cases and computational requirements, from ultra-fast inference to high-quality performance across diverse vision-language workloads.
Prompt Caching Support
Many vision use cases are for real time agentic applications, so latency is an extremely important part of the user experience. On top of fast inference runtime, we've enabled
prompt caching for vision models
, both text and image portions of your prompts can benefit from caching to reduce time to first token by up to 80%. This optimization is particularly beneficial for:
•
Agentic multimodal mult-turn conversations (e.g. a computer use agent)
•
Batch processing of identical images
•
Long system prompts
•
Production deployments with predictable usage patterns
Customize Your Vision Models
You can now cater an VLM of your choice towards your application pattern. For example, many use cases require special function calling from the VLM.
We enabled LoRA uploads (Low-Rank Adaptation) large vision models. Whether you're working on specialized image classification, document analysis, or custom visual reasoning tasks, LoRA support makes it possible to achieve state-of-the-art results with minimal resources. We’re excited to share that we support LoRA uploads for
Qwen2.5 VL
, and
Phi3.5 Vision Instruct
. See our
documentation
for more details.
Get Started Today
Whether you're building the next generation of multimodal applications or integrating visual intelligence into existing workflows, our enhanced platform provides the tools and models you need.
Ready to explore these new capabilities?
We'd love to help you get started with vision models tailored to your specific use case:
Contact Us
👈
Our team can help you:
•
Choose the right vision model for your application
•
Optimize accuracy with LoRA fine-tuning
•
Implement function calling workflows
•
Design custom multimodal solutions
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
