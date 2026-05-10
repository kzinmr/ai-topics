---
title: "FireLLaVA: the first commercially permissive OSS LLaVA model"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/firellava-the-first-commercially-permissive-oss-llava-model"
scraped: "2026-05-10T01:20:36.435116+00:00"
lastmod: "2026-02-12T18:53:16.000Z"
type: "sitemap"
---

# FireLLaVA: the first commercially permissive OSS LLaVA model

**Source**: [https://fireworks.ai/blog/firellava-the-first-commercially-permissive-oss-llava-model](https://fireworks.ai/blog/firellava-the-first-commercially-permissive-oss-llava-model)

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
Firellava The First Commercially Permissive Oss Llava Model
FireLLaVA: the first commercially permissive OSS LLaVA model
PUBLISHED
1/18/2024
Table of Contents
What is a VLM model and what are the use cases
FireLLaVA
Demo
Model performance
Using the API
References:
Table of Contents
Table of Contents
What is a VLM model and what are the use cases
FireLLaVA
Demo
Model performance
Using the API
References:
Table of Contents
We have come to rely heavily on text as input for foundation models to generate responses. However, in real-world applications, we frequently process and analyze data from various sources, such as images and sound. Notably, images often contain more intricate and dense information than text. To address this, multi-modality models have been developed to process and analyze data from multiple sources effectively, providing a more comprehensive and accurate understanding of the input data.
We are excited to announce that we have open-sourced FireLLaVA under the Llama 2 Community License. It is the first LLaVA multi-modality model with a commercially permissive license. You can now download FireLLaVA from our
Huggingface repository
, use it directly from our fast API, or experiment with it in our
playground
. By utilizing FireLLaVA, we can advance the development of more sophisticated and versatile models capable of handling diverse data sources.
What is a VLM model and what are the use cases
Vision-Language Models (VLMs) are multi-modal models that understand both visual content and text prompts.VLMs are valuable for a variety of use cases, such as writing marketing descriptions given product images or building chatbots that can interpret charts. LLaVA is a Visual Language Model (VLM) developed by Haotian Liu et al that achieves strong performance on 11 benchmarks. The best performing open source version of LLaVA 1.5 is based on the Vicuna v1.5 13B language model as the LLM component and the OpenAI CLIP-Vit as the vision component. It proposes a generic architecture and a training methodology that enables the language model to understand vision content and respond accordingly.
While LLaVA v1.5 13B model weights are open sourced, a big hurdle to using the OSS LLaVA model for commercial usage is that it was trained with GPT4 generated training data and is subject to non-commercial licenses like cc by-nc-4.0.
Do note that FireLLaVA, similar to the original LLaVA model, was also trained with a single image in the conversation, and therefore its performance may degrade with multiple images present in the conversation. When using the FireLLaVA model to build a vision-capable chat bot, we recommend including only the last image in the conversation. It also has similar limitations as the original LLaVA model in that input images are generally downscaled and small texts in the input images may be hard for the model to read.
FireLLaVA
Fireworks.ai set out to recreate a commercially-usable version of the LLaVA model leveraging only OSS models for data generation and training. More specifically, LLaVA authors came up with a novel approach to generate visual language conversations using GPT4 language-only model by giving the model bounding box labels and captions of images, and using them for instruction fine-tuning. We recreated these training data with a language-only OSS model, the CodeLlama 34B Instruct model following their approach (more details in the
original paper
). CodeLlama 34B Instruct model was picked to strike a balance between model quality and efficiency. The final mix of the data for the instruction fine-tuning stage consists of 588K lines of single and multi-turn visual question answering or conversation data, mixed from the permissive portion of the original LLaVA training data and Fireworks.ai generated training data. Moreover, we are open-sourcing the model at
fireworks-ai/FireLLaVA-13b
that can be loaded for inference with transformers version >= 4.35.3, and named it FireLLaVA.
Demo
You can now try out FireLLaVA in our
playground
. The model is able to respond reasonably well to clear instructions such as And perform some reasoning based on visual inputs such as Or, visual understanding of more abstract content such as
Model performance
To grasp an understanding of how well FireLLaVA compared to one that was trained on GPT-4 generated data, we conducted seven benchmarks that are commonly included in visual understanding model academic papers, following the instructions
here
. The result is as follows:
As the results show, FireLLaVA trained on our OSS model training data performs close to the original LLaVA model trained on GPT4 generated data, and even slightly beats the original LLaVA model on four of the seven benchmarks.
This result highlights the fact that bootstrapping Language-Only Model for high quality VLM model training data generation is useful, and with careful prompt engineering, getting training data at a similar level of quality as GPT4 generated data is achievable.
Using the API
We are providing both the completions API and chat completions API to the commercially-viable LLaVA model. The API interface is compatible with OpenAI Vision models except that the “detail” parameter is currently ignored since all images are treated uniformly by the nature of LLaVA model. Developers can easily integrate the vision-capable APIs into their applications to unlock new capabilities. Here is an example:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
import
fireworks
.
client
url
=
"https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
prompt
=
"What is the season?"
completion
=
fireworks
.
client
.
ChatCompletion
.
create
(
model
=
"accounts/fireworks/models/firellava-13b"
,
messages
=
[
{
"role"
:
"user"
,
"content"
:
[
{
"type"
:
"text"
,
"text"
:
prompt
}
,
{
"type"
:
"image_url"
,
"image_url"
:
{
"url"
:
url
}
}
,
]
,
}
,
]
,
max_tokens
=
512
,
temperature
=
0
,
)
print
(
completion
.
choices
[
0
]
.
message
.
content
)
#####################################################
# The season is spring, as indicated by the blooming cherry blossoms and the presence of a tall building in the background.
References:
•
LLaVA: Large Language and Vision Assistant Visual Instruction Tuning:
https://llava-vl.github.io/
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
