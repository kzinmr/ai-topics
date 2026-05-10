---
title: "DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/deepseek-model-architecture"
scraped: "2026-05-10T01:27:11.532517+00:00"
lastmod: "2026-02-12T18:52:23.000Z"
type: "sitemap"
---

# DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical

**Source**: [https://fireworks.ai/blog/deepseek-model-architecture](https://fireworks.ai/blog/deepseek-model-architecture)

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
Deepseek Model Architecture
DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical
PUBLISHED
2/7/2025
Table of Contents
TLDR;
Architecture Overview
More Aggressive Mixture-of-Expert
What changed from Deepseek v2 to v3?
Structural change
Local Balanced Routing to Experts
First ever FP8 Precision OSS LLM pre-training
Side Note on fp8 quantization
How is it done?
Fine granularity quantization
More Mantissa bits of fp8
Side Note on quantization errors:
Better Accumulation Precision:
Online Quantization
More customized data format and scaling factor
Conclusion
Table of Contents
Table of Contents
TLDR;
Architecture Overview
More Aggressive Mixture-of-Expert
What changed from Deepseek v2 to v3?
Structural change
Local Balanced Routing to Experts
First ever FP8 Precision OSS LLM pre-training
Side Note on fp8 quantization
How is it done?
Fine granularity quantization
More Mantissa bits of fp8
Side Note on quantization errors:
Better Accumulation Precision:
Online Quantization
More customized data format and scaling factor
Conclusion
Table of Contents
TLDR;
•
This article introduces the architecture of DeepSeek v3 and DeepSeek R1, which shares exactly the same architecture.
•
Explain DeepSeek MoE (Mixture of Experts) and FP8 pre-training in depth.
Architecture Overview
DeepSeek v3 and R1 continue to use the traditional Transformer block, incorporating SwiGLU, RoPE, and RMSNorm. It also inherits Multi-head Latent Attention (MLA) and radical Mixture-of-Experts (MoE) introduced by DeepSeek v2.
But what makes DeepSeek v3 so remarkable?
Despite compute limitations, it leverages the scaling law by adopting a
more aggressive MoE
and utilizing
FP8 precision for training
.
More Aggressive Mixture-of-Expert
As we all know, linear layers of Feed-Forward Network are low-rank in nature (That’s why LoRA performs exceptionally well), that most parameters in the FFN are not as important. That leaves optimization opportunities: how to only activate the useful parameters for each incoming prompt?
The result is a sparsely-activated model, more famously known as Mixture of Experts (MoE).
(MoE does not seem like the most appropriate name, since the MoE under LLM context emphasizes more on sparsity than expertise. There aren’t any real “experts” involved here, and adding actual expertise could potentially have negative effects).
Experiments from
Mixtral
have demonstrated that sparse large language models employing 8 experts, where only 2 are activated during inference, can achieve quality benchmarks comparable to similar-sized dense models.
This opens up the possibility of achieving the same quality with the same amount of parameters, but at a much lower inference-time computation cost.
Let’s recap the
scaling law
:
As the number of parameters increases, larger models tend to achieve lower loss values by the end of pre-training.
Therefore conversely, with the same inference cost, we can achieve higher quality benchmarks by increasing sparsity and boosting model size.
This also raises an intriguing question: what if we move beyond the traditional paradigm of 8 experts with 2 activated? By dramatically increasing the number of experts—perhaps to over 100 or even 200—while maintaining a reasonable number of activated experts, we could potentially construct an ultra-large model.
Model Name
Activated / Total Parameters
Number of Activated / Total Experts
Mixtral 8x22B
39B out of 141B
2 out of 8
Grok-1 by xAI
86B out of 314B
2 out of 8
DBRX by Databricks
36B out of 132B
4 out of 16
Deepseek v2
21B out of 236B
8 out of 162 (2 shared)
DeepSeek v3
37B out of 671B
9 out of 257 (1 shared)
What changed from Deepseek v2 to v3?
Structural change
The number of layers in DeepSeek v2 and v3 are nearly identical, with 60 and 61 layers respectively.
However, the number of routed experts per layer increased by 60%, from 160 to 256. Doubling the FFN size means significantly more capacity for knowledge and memory.
v3 also inherits the concept of the “shared expert”, i.e. an always-activated expert. Each FFN layer has 1 shared expert.
Also for better representation of the input data, v3 increases the all-experts-activated layer from 1 to 3.
So given 29.36M parameters per expert, and (61-3)_9 + 3 _ 257 = 1354 activated experts, we have 37.96B activated FFN parameters in total.
Local Balanced Routing to Experts
How is a token assigned to an expert? The assignment is based on the token-to-expert affinity in embedding space. However, if all tokens repeatedly get routed to the same expert, this leads to an issue known as routing collapse.
Routing collapse negatively impacts model quality during pre-training: even when the inputs are diverse, the model consistently selects only a few experts, saturating these parameters, while hindering sufficient training on other experts.
DeepSeek v2 introduced three auxiliary losses—expert-level, device-level, and communication-level—to avoid routing collapse. However, these auxiliary losses can negatively impact model quality if they overshadow the token-to-expert affinity: this token is better suited for this expert, but routed to other experts for the sake of “balance”.
Thus, v3 eliminates these auxiliary losses entirely and instead introduces a bias term to the gating value. This bias term is only used for routing purposes instead of being included in the overall loss, and only gets manually adjusted when its corresponding expert is overloaded/underloaded.
Therefore the load balancing objective doesn't compete with the quality optimization objective.
While DeepSeek v3 suffers from significantly worse load balancing, it ultimately results in better overall model performance.
First ever FP8 Precision OSS LLM pre-training
FP8 has been widely adopted as a quantization format during LLM inference, but using fp8 during training is a novel and innovative approach.
Advantages of Using fp8 for Training:
Compute Efficiency
: Nvidia’s Tensor Core FP8 FLOPS are exactly double that of FP16. FP8 enables faster matrix multiplications and improves overall training speed.
Memory Savings
: Compared with bf16, fp8 reduces the memory in half, which allows larger and deeper models to fit within the same hardware constraints.
Efficient Communication
: fp8 lowers data transfer bandwidth requirements in distributed training, reducing communication overhead and improving synchronization efficiency across multiple GPUs.
However, FP8 also introduces additional challenges: lower precision means lower numerical stability, leading to higher error rates per computation.
The DeepSeek team invested countless engineering efforts to minimize quantization and computation errors.
And they achieved a miracle: eventually, compared with the bf16 baseline, the relative loss error of their fp8 training model remains consistently below 0.25%.
Side Note on fp8 quantization
FP8 quantization doesn’t mean the entire model is trained in fp8. For instance, embedding and attention layers still use bf16, as well as the more sensitive optimizer states. Master weights and gradients are even stored in fp32.
Similar to int4 quantization: FFN is in int4, while attention layers are kept in int8 or fp8.
Thus, it’s more complex than simply computing with fp8 alone, as it involves a mixed precision computation.
How is it done?
Fine granularity quantization
Previously, quantization can be performed with these 2 granularities:
Per-tensor scaling: A single scaling factor is applied uniformly across the entire matrix. This means every value in the matrix is scaled by the same scalar number.
Per-channel scaling: Each column/row in the matrix gets its own unique scaling factor. This results in the matrix being scaled by a vector of values rather than a single number, allowing for more granular control.
When the hidden dimension grows very large (approaching 10,000), the likelihood of encountering significant value imbalances increases. Even a single outlier value can create substantial imbalance across the matrix.
If you use per-channel scaling (scaling everything by a single constant), you'll be forced to scale down 10,000 values to accommodate the outliers. This leads to poor precision for the smaller values, since they'll be compressed into a smaller numeric range (even all in the same bucket).
This approach doesn't make optimal use of the available FP8 number representation buckets, since most values end up clustered in a narrow range while leaving other potential value ranges unused.
Thus DeepSeek v3 implemented a more fine-grained approach: instead of quantizing at the full row/column level, it breaks the matrix down into smaller 1x128 tiles.
In cases where per-tensor scaling was previously used (like linear weights' forward and backward passes), they now split into 128x128 blocks instead.
More Mantissa bits of fp8
DeepSeek v3 uses E4M3 over E5M2.
Side Note on quantization errors:
There are 2 type of quantization errors:
_Resolution error: difference between original value
x
and de-quantized value
x’
, computed as rounding((x/scale) _ scale).*
Clamping error: Take int8 for example, if the quantized value is bigger than 127, but clamped at 127.
To keep as much Tensor information as possible, quantization range is chosen to minimize the Mean-Absolute-Error. This method is known as entropy based range optimization.
However, due to the limitation on the number of bits, a trade-off must be made between the two:
Smaller bucket means smaller range, which means an outlier can contribute to tremendous clamping error, thus very bad MAE.
Bigger bucket means bigger range, accommodating outliers. But more weights will be congested in those few buckets, leading to worse resolution error. (On average, resolution_error equals half the bucket width).
Tile-wise/block-wise grouping quantization already brings in more balanced weights, which helps reduce the occurrence of outliers and, as a result, lowers the clamping error naturally.
Therefore we don’t have to trade one error for another.
Allocating more bits to the mantissa in the linear scale (smaller bucket) instead of the exponential scale (larger bucket) enables finer precision, thereby reducing resolution error.
To conclude, Mean-Absolute-Error of E4M3 quantization is lower than E5M2.
Better Accumulation Precision:
MMA (Matrix-Multiplication Accumulation) is the most common operation in pre-training. However, for FP8 operations, the accumulation precision in Nvidia Tensor Core is bounded at 14bits.
In the worst-case scenario, the 2-bit overflow during FP8 x FP8 multiplication can result in an error rate of up to 2%.
The DeepSeek team alleviates the issue by promoting MMA operations in CUDA Core.
Online Quantization
Also known as Dynamic Range Quantization
Side Note on static and dynamic range quantization: Static quantization: use a fixed scalar for scaling and cast the values to fp8.
Dynamic Range quantization: calculate the minimum and maximum values of each tile, and dynamically compute a scaling factor to fully utilize the fp8 range.
Historically, only the Activation layer uses online quantization, as activation values differ with each inference. In contrast, linear layer parameters remain fixed, so they do not require dynamic scaling like activations do.
DeepSeek v3 opted to use online quantization for all layers, further minimizing quantization error across the entire network.
More customized data format and scaling factor
To minimize quantization errors in critical areas, like immediately following the attention operation, use scaling factors that are powers of 2. This ensures no errors occur during scaling or descaling.
Additionally, use a customized E5M6 (fp12) data format exclusively for these activations to balance between precision and memory efficiency.
Conclusion
DeepSeek v3 and R1 are perfect examples that demonstrate how engineering efficiency and thoughtful design can push the boundaries of artificial intelligence performance.
Feel free to try DeepSeek
V3
and
R1
on the Fireworks platform.
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
