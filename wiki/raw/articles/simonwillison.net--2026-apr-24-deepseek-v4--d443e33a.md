---
title: "DeepSeek V4-almost on the frontier, a fraction of the price"
url: "https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything"
fetched_at: 2026-04-28T07:01:58.833114+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# DeepSeek V4-almost on the frontier, a fraction of the price

Source: https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything

DeepSeek V4—almost on the frontier, a fraction of the price
24th April 2026
Chinese AI lab DeepSeek’s last model release was V3.2 (and V3.2 Speciale)
last December
. They just dropped the first of their hotly anticipated V4 series in the shape of two preview models,
DeepSeek-V4-Pro
and
DeepSeek-V4-Flash
.
Both models are 1 million token context Mixture of Experts. Pro is 1.6T total parameters, 49B active. Flash is 284B total, 13B active. They’re using the standard MIT license.
I think this makes DeepSeek-V4-Pro the new largest open weights model. It’s larger than Kimi K2.6 (1.1T) and GLM-5.1 (754B) and more than twice the size of DeepSeek V3.2 (685B).
Pro is 865GB on Hugging Face, Flash is 160GB. I’m hoping that a lightly quantized Flash will run on my 128GB M5 MacBook Pro. It’s
possible
the Pro model may run on it if I can stream just the necessary active experts from disk.
For the moment I tried the models out via
OpenRouter
, using
llm-openrouter
:
llm install llm-openrouter
llm openrouter refresh
llm -m openrouter/deepseek/deepseek-v4-pro 'Generate an SVG of a pelican riding a bicycle'
Here’s the pelican
for DeepSeek-V4-Flash
:
And
for DeepSeek-V4-Pro
:
For comparison, take a look at the pelicans I got from
DeepSeek V3.2 in December
,
V3.1 in August
, and
V3-0324 in March 2025
.
So the pelicans are pretty good, but what’s really notable here is the
cost
. DeepSeek V4 is a very, very inexpensive model.
This is
DeepSeek’s pricing page
. They’re charging $0.14/million tokens input and $0.28/million tokens output for Flash, and $1.74/million input and $3.48/million output for Pro.
Here’s a comparison table with the frontier models from Gemini, OpenAI and Anthropic:
Model
Input ($/M)
Output ($/M)
DeepSeek V4 Flash
$0.14
$0.28
GPT-5.4 Nano
$0.20
$1.25
Gemini 3.1 Flash-Lite
$0.25
$1.50
Gemini 3 Flash Preview
$0.50
$3
GPT-5.4 Mini
$0.75
$4.50
Claude Haiku 4.5
$1
$5
DeepSeek V4 Pro
$1.74
$3.48
Gemini 3.1 Pro
$2
$12
GPT-5.4
$2.50
$15
Claude Sonnet 4.6
$3
$15
Claude Opus 4.7
$5
$25
GPT-5.5
$5
$30
DeepSeek-V4-Flash is the cheapest of the small models, beating even OpenAI’s GPT-5.4 Nano. DeepSeek-V4-Pro is the cheapest of the larger frontier models.
This note from
the DeepSeek paper
helps explain why they can price these models so low—they’ve focused a great deal on efficiency with this release, especially for longer context prompts:
In the scenario of 1M-token context, even DeepSeek-V4-Pro, which has a larger number of activated parameters, attains only 27% of the single-token FLOPs (measured in equivalent FP8 FLOPs) and 10% of the KV cache size relative to DeepSeek-V3.2. Furthermore, DeepSeek-V4-Flash, with its smaller number of activated parameters, pushes efficiency even further: in the 1M-token context setting, it achieves only 10% of the single-token FLOPs and 7% of the KV cache size compared with DeepSeek-V3.2.
DeepSeek’s self-reported benchmarks
in their paper
show their Pro model competitive with those other frontier models, albeit with this note:
Through the expansion of reasoning tokens, DeepSeek-V4-Pro-Max demonstrates superior performance relative to GPT-5.2 and Gemini-3.0-Pro on standard reasoning benchmarks. Nevertheless, its performance falls marginally short of GPT-5.4 and Gemini-3.1-Pro, suggesting a developmental trajectory that trails state-of-the-art frontier models by approximately 3 to 6 months.
I’m keeping an eye on
huggingface.co/unsloth/models
as I expect the Unsloth team will have a set of quantized versions out pretty soon. It’s going to be very interesting to see how well that Flash model runs on my own machine.
