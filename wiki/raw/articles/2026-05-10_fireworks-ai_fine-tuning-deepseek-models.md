---
title: "Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/fine-tuning-deepseek-models"
scraped: "2026-05-10T01:27:10.877285+00:00"
lastmod: "2026-04-21T21:28:15.000Z"
type: "sitemap"
---

# Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost

**Source**: [https://fireworks.ai/blog/fine-tuning-deepseek-models](https://fireworks.ai/blog/fine-tuning-deepseek-models)

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
Fine Tuning Deepseek Models
Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost
PUBLISHED
3/12/2025
Table of Contents
Challenges with training DeepSeek
Quantization Aware Training for accuracy and efficiency
Seamless QAT Training and Deployment on Fireworks
Measuring Quality with Quantization Aware Training
Expanding QAT to Llama, DeepSeek V2 & other BFloat16 Models
Eval Stability
Try it Now!
Table of Contents
Table of Contents
Challenges with training DeepSeek
Quantization Aware Training for accuracy and efficiency
Seamless QAT Training and Deployment on Fireworks
Measuring Quality with Quantization Aware Training
Expanding QAT to Llama, DeepSeek V2 & other BFloat16 Models
Eval Stability
Try it Now!
Table of Contents
At Fireworks, we’re happy to announce customization of DeepSeek R1 & V3, through Quantization Aware Fine Tuning, is now available as part of our
FireOptimizer adaptation engine
.
You can now tailor the behavior of these state-of-the-art open models specifically for your use case, and optimize for quality, latency & cost. You can deploy the tuned models with one-click on a dedicated deployment on Fireworks. To get started, reach out to your Fireworks representative, or
contact us
.
Challenges with training DeepSeek
DeepSeek R1
and V3 are state-of-the-art open models that excel at a variety of tasks including chat, code generation and reasoning over complex tasks, but fine tuning these models has proven very challenging:
Accuracy drops from different training and serving configurations -
DeepSeek is natively tuned and designed for FP8 serving. For nearly all existing LoRA methods, LoRA weights are assumed to be in an unquantized bfloat16 when doing inference. Merged models trained in bfloat16 and served in fp8 results in significant accuracy penalty, even when the base model is natively trained on fp8 as with DeepSeek R1 and V3.
High memory requirements for tuning
- DeepSeek R1 and V3 have 671 billion parameters and require substantial GPU memory. Even in FP8 format, the base model alone occupies 671 GB of GPU memory, excluding offloading to CPU. This exceeds the typical 640GB memory of an H100 host. The memory requirement further intensifies with increasing context length, as additional space is needed to store activations and intermediate tensors.
Complexities with large number of experts in DeepSeek -
DeepSeek v3 has a unique Mixture-of-Experts (MoE) structure with 256 different experts. It is therefore tricky to make the training efficient given that you need to have lora matrices for each expert in each MoE layer. The very naive implementation, for example, would run forward pass of the experts one by one, and would be extremely inefficient.
Quantization Aware Training for accuracy and efficiency
Quantization Aware Training (QAT) builds on LoRA and QLoRA techniques to get high accuracy while reducing memory needed during training.
•
LoRA
lowers memory requirements while maintaining high quality without overfitting due to its low rank nature
•
QLoRA
cuts base model memory by ~4x, while maintaining quality with only a small accuracy penalty.
To further mitigate the quantization penalty during inference, we employ quantization-aware training. Specifically, we solve the problem where
•
Lora modules are quite small and must be kept in bfloat16 precision for quality
•
During inference they should be merged into the base model weight for optional speed
•
During merging, we will lose precision when converting merged LoRA weights from bfloat16 to block-wise FP8
QAT uses “fake quantization” of merged weights and activation to better simulate inference setup. This allows us to keep both LoRA matrices’ gradients in bfloat16 while the resulting merged weight follows FP8 numerics during the forward pass.
Seamless QAT Training and Deployment on Fireworks
You can train and deploy models using QAT seamlessly in 3 lines of code with Fireworks. Here’s a minimal example recipe to tune and deploy
DeepSeek V3
model:
1
2
3
4
5
firectl create dataset my
-
dataset
/
path_to_my_dataset
.
jsonl
firectl create sftj
--
base
-
model accounts
/
fireworks
/
models
/
deepseek
-
v3
--
dataset my
-
dataset
--
output
-
model my
-
deepseek
-
v3
firectl create deployment my
-
deepseek
-
v3
--
live
-
merge
--
accelerator
-
type
NVIDIA_H200_141GB
--
accelerator
-
count
8
To get access, reach out to your Fireworks representative, or
contact us
.
Measuring Quality with Quantization Aware Training
We can test QAT-based tuning on a classification use case to identify wines based on reviews. We used this wine reviews
dataset
and filtered French wines (like this
cookbook
), with 15,000 records for training and 5,000 records for evaluation. Results are shown below for (a) Without fine-tuning (b) With non-QAT fine-tuning and (c)With QAT fine-tuning.
The results show that
Fine-tuning provides a strong improvement in model quality
QAT provides an edge over naive FP8 LoRA tuning
Expanding QAT to Llama, DeepSeek V2 & other BFloat16 Models
While QAT is great for
DeepSeek models
that have a native fp8 weight format, it can also be used also for models like Llama 3.3 and DeepSeek V2 Lite, that were trained in bfloat16, but can be quantized for faster inference.
We’ve conducted experiments by training using NF4 (original QLoRA), FP8 and bfloat16 base models and then using FP8 and bfloat16 inference. FP8 QAT serving would be tied for the fastest speeds of all methods and provide significant gains over BF16 serving. Simultaneously, we see that FP8 QAT training has superior accuracy to all training/inference combinations, except full bf16 for both training and serving.
Eval Stability
Another benefit of QAT training is that eval, which is running as a part of training, becomes much closer to inference numerics. To prove this point, we measure the
KL divergence
of eval running during training vs inference stack, and see significantly lower divergence in FP8 QAT.
Try it Now!
QAT fine-tuning for DeepSeek R1 and V3 is available now. To get started, reach out to your Fireworks representative, or
contact us
.
In the coming weeks we will also add QAT support for Llama and Qwen models so you can enjoy FP8 inference speeds without accuracy loss.
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
