---
title: "Together AI brings Thinking Machines Lab’s new model Inkling on day 0"
url: "https://www.together.ai/blog/together-ai-brings-thinking-machines-labs-new-model-inkling-on-day-0"
fetched_at: 2026-07-16T07:01:39.252617+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Together AI brings Thinking Machines Lab’s new model Inkling on day 0

Source: https://www.together.ai/blog/together-ai-brings-thinking-machines-labs-new-model-inkling-on-day-0

Today, Thinking Machines Lab released Inkling, a new multimodal mixture-of-experts model built for token-efficient reasoning, native multimodal understanding, and broad task versatility. Together AI is excited to collaborate with the Thinking Machines Lab team to make Inkling available to developers on our inference platform.
Inkling accepts text, image, and audio inputs and produces text outputs through a unified decoder architecture. It supports controllable inference effort, allowing developers to adjust how much reasoning the model applies based on the needs of each task. Its post-training also spans a wide range of capabilities, including scientific reasoning, coding, agentic workflows, forecasting, and calibrated prediction.
Under the hood, Inkling introduces several architectural innovations beyond a conventional decoder-only Transformer, including query-conditioned relative attention, short causal convolutions throughout the model, and a mixture-of-experts architecture with a shared expert sink. Together, these components are designed to support strong reasoning and multimodal capabilities while maintaining efficient model execution. Serving it efficiently at scale is nontrivial, and it's exactly the kind of workload Together AI's inference stack is built to optimize, so you get the model's efficiency gains in practice for production inference. On Together AI, Inkling runs with an optimized
FlashAttention-4–based attention kernel
designed to efficiently support its query-conditioned relative attention mechanism in production.
Congratulations to the Thinking Machines Lab team on the release.
Inkling at a glance
Token-efficient, controllable reasoning:
Developers can adjust inference effort to balance reasoning depth, token usage, and latency for different workloads.
Native multimodal inputs:
Inkling accepts audio, image, and text inputs and generates text outputs through a single model.
Broad task versatility:
The model is post-trained across reasoning, coding, agentic, forecasting, and calibrated prediction tasks.
A differentiated architecture:
Inkling combines grouped-query attention, learned relative-position bias, short causal convolutions, and shared-sink MoE routing.
Strong preliminary evaluations:
At its highest evaluated effort setting, Inkling shows strong results across scientific reasoning, mathematics, coding, agentic, vision, and audio benchmarks.
Available on Together AI:
Developers can access Inkling through serverless, with 1M context window, and OpenAI-compatible APIs.
Strong performance on challenging reasoning tasks
Preliminary evaluations of the current Inkling checkpoint show strong performance across graduate-level scientific reasoning and competition mathematics:
The results point to one of Inkling’s defining characteristics: versatility. The same model performs strongly across knowledge-intensive reasoning, mathematical problem solving, software engineering, browser-based tasks, visual document understanding, and audio comprehension.
Inkling is also post-trained on forecasting and calibrated prediction tasks. This expands the model’s usefulness beyond conventional question answering to applications where representing uncertainty and producing well-calibrated estimates are important.
‍
Why run Inkling on Together?
Day 0 access, zero setup:
Inkling is live on Together AI Serverless today. No waiting for capacity, no infrastructure to provision, no GPUs to manage.
Full multimodal input support, one endpoint:
Since Inkling natively accepts text, image, and audio, you don't need separate pipelines or preprocessing services, Together AI Serverless handles all three input types through a single API call. This is powerful as Together’s unified solution removes the tradeoff between latency, speed and operational stability.
Controllable reasoning effort, without managing your own infra:
Inkling's adjustable inference-effort setting lets you trade off depth, latency, and token spend per request. On Together AI, you control that dial through the API directly, so cost and speed tuning happens at the request level, not the infrastructure level.
‍
A new architecture for reasoning and multimodality
Inkling is a decoder-only mixture-of-experts model with
975B
total parameters,
40B
active parameters per token, and a context window of
1M tokens
.
Rather than using RoPE or absolute position embeddings, Inkling incorporates token position directly into attention through a learned, query-conditioned relative bias. Each attention layer combines the conventional query-key similarity score with an additional score based on the relative distance between tokens. This gives the model a flexible mechanism for representing token order and nearby context.
Inkling mixes sliding-window and full causal attention throughout the network. The standard architecture uses five local-attention layers followed by one full-attention layer, allowing most layers to focus efficiently on recent context while periodically integrating information across the full sequence.
The model also introduces
sconv
, a lightweight channelwise causal convolution with a four-token receptive field. Sconv is applied to the key and value streams before attention, as well as to the outputs of the attention and feed-forward sublayers. These short convolutions give each layer an additional mechanism for combining information across adjacent tokens without the cost of another full attention operation.
Inkling’s feed-forward layers use a mixture-of-experts architecture with
shared expert sink
. For every token, the router selects a small number of routed experts while also assigning weight to shared experts. Unlike conventional shared-expert MoE designs, Inkling normalizes the shared experts and selected routed experts together, allowing the shared path to dynamically compete for mixture weight on each token.
Inkling also supports image and audio inputs. Lightweight embedding towers transform image patches and quantized audio features into embeddings with the same width as text tokens. These embeddings are inserted directly into the model’s input sequence and processed by the same decoder stack.
Unified text, image, and audio inputs
Inkling accepts three input modalities: text, images, audio. All three modalities are processed by the same decoder stack, with text generated as the output.
Lightweight embedding towers transform image patches and quantized audio features into embeddings with the same width as text-token embeddings. These representations are inserted directly into the model’s input sequence, allowing the language model to reason jointly over text, visual, and audio information.
This unified design enables applications such as visual question answering, document analysis, audio comprehension, multimodal agents, and workflows that combine multiple input types within the same conversation.
Start building with Inkling on Together Serverless
Inkling is available through
Together AI Serverless today
.
Developers can:
Build text, image, and audio applications using a unified model
Scale from initial experimentation to dedicated production capacity
from together import Together

client = Together()

response = client.chat.completions.create(
    model="[INKLING MODEL ID]",
    messages=[
        {
            "role": "user",
            "content": "Analyze this problem carefully and provide the answer."
        }
    ],
    # Replace with the final supported API parameter.
    reasoning_effort="[SUPPORTED VALUE]",
)

print(response.choices[0].message.content)
