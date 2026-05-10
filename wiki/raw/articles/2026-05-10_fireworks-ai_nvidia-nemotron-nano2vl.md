---
title: "Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/nvidia-nemotron-nano2vl"
scraped: "2026-05-10T01:21:02.151212+00:00"
lastmod: "2026-02-12T18:51:16.000Z"
type: "sitemap"
---

# Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks AI

**Source**: [https://fireworks.ai/blog/nvidia-nemotron-nano2vl](https://fireworks.ai/blog/nvidia-nemotron-nano2vl)

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
Nvidia Nemotron Nano2vl
Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks AI
PUBLISHED
10/27/2025
Exciting news for vision AI! Fireworks is proud to offer Day-0 support for the highly anticipated NVIDIA Nemotron Nano2 VL, a 12B multimodal reasoning model for accelerating your document intelligence and video understanding applications.
NVIDIA Nemotron Nano2 VL, the latest innovation in the
NVIDIA Nemotron
family, is a vision language model (VLM) designed to push the boundaries of intelligent document processing, AI assistant video understanding, video captioning, multi-modal agentic workflows, and more. It enables AI assistants to extract, interpret, and act on information across text, images, tables, and video. VLMs are built by combining an LLM with a vision encoder, enabling the LLM with eyes. VLMs often require a more complex architecture to integrate across multiple modalities. With
Fireworks' Multimedia
, developers can effortlessly unlock insights across various modalities from VLMs like NVIDIA Nemotron Nano2 VL, bypassing the complexities of unstructured multi-domain workflows. In an invoice analysis example, Nemotron Nano2 VL surpassed over 90% accuracy, resulting in a high quality output. In the scenario, the Nemotron Nano2 VL model automated the entire process of data extraction, classification, and summarization, eliminating the need for tedious, time-consuming manual evaluation.
With its high accuracy, compact model footprint, and multimodal capabilities, Nemotron Nano 2 VL seamlessly extracts and comprehends information from complex documents, videos and images. For intelligent document assistants, this includes diverse inputs from text-base documents to images, charts and graphs, making it an ideal solution for automating document workflows across industries like finance, healthcare, legal, and government. In multi-image processing, it assists with tasks such as captioning and content curation, making it ideal for product catalog parsing and image search. Lastly it is optimal for multimodal and agentic pipelines that may need image aware retrieval and tool use.
What Makes NVIDIA Nemotron Nano 2 VL Unique?
The efficient model combines the optimized hybrid Mamba-Transformer architecture from the
Nemotron family
for the LLM with a Vision Encoder based on CRADIOH-V2, and an efficient video search token compression model.
It provides three key features:
•
High Accuracy: Nemotron Nano 2 VL is trained with NVIDIA curated high quality synthetic data to achieve leading accuracy for character recognition, chart reasoning,visual Q&A, video understanding, and document intelligence.
•
High Efficiency: Using the hybrid Mamba-Transformer architecture compared to the previous Nemotron VL Model with Efficient Video Sampling (EVS), developers can process longer videos in the same time, lowering total cost of inference
•
Flexibility with Open Source: It is an OSS model that can be fine tuned to your specific use case rather than locked into one specific workload. Additionally, 11M samples of multimodal training data and model training recipe are openly available.
Check out the figure below showcasing a variety of benchmarks from NVIDIA on the Nemotron Nano2 model.
Figure 1: NVIDIA Benchmarks on Nemotron Nano VL vs. Nemotron Nano 2 VL
Getting Started on Fireworks
We're excited to announce that the latest Nemotron Nano VL model is now available on Fireworks! We've prepared a
comprehensive cookbook
to help you explore its performance. The model is optimized for things like OCR(optical character recognition) in document processing. Unlike older OCRs systems that simply convert an image to text, a VLM understands the semantic context and spatial relationships between elements. In this process the model will analyze the image and distinguish between the characters and the background. The model used the pattern found in the image to identify the characters and convert them into machine readable text. This example demonstrated NVIDIA Nemotron Nano 2 VL on Fireworks AI being used for invoice processing and document intelligence. The main task was to extract invoice numbers, dates, line items, and totals. The table below shows our test result success rates for parsing the invoices. With NVIDIA Nemotron we were able to achieve overall quality rates in the 90s.
Test
Quality Rate
Invoice Number
100%
Date
100%
Item Count
100%
Total Amount
63.2%
Overall
90.8% (19/20 Successful Extractions)
Other use cases that could benefit from a scenario similar to invoice processing include account payable automation, expense management and receipt processing, financial document digitization, and compliance and audit workflows.
Next Steps:
Ready to deploy this solution in production? Try:
Test the cookbook with your domain-specific documents
Add validation rules for total amount extraction
Implement confidence-based routing for human review
Scale to multi-page documents (contracts, statements, purchase orders)
VLMs like Nemotron can drastically outperform manual document analysis by offering superior speed, accuracy, and scale, as they holistically understand both the text and the context of these complex documents. This automation eliminates human error, significantly lowering operational costs, and freeing staff to focus on more strategic work.
Automate your document intelligence and multi-image processing workflows today by deploying
Nemotron Nano 2 VL
on Fireworks AI. For further questions, reach out on Discord or via
[email protected]
.
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
