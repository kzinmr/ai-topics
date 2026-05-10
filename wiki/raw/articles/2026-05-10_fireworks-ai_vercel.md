---
title: "40X Faster, and Smarter Outputs: How Vercel Turbocharged their Code Fixing Model with Open Models, Speculative Decoding and Reinforcement Fine Tuning on Fireworks"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/vercel"
scraped: "2026-05-10T01:21:01.532407+00:00"
lastmod: "2026-02-12T18:51:13.000Z"
type: "sitemap"
---

# 40X Faster, and Smarter Outputs: How Vercel Turbocharged their Code Fixing Model with Open Models, Speculative Decoding and Reinforcement Fine Tuning on Fireworks

**Source**: [https://fireworks.ai/blog/vercel](https://fireworks.ai/blog/vercel)

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
Vercel
40X Faster, and Smarter Outputs: How Vercel Turbocharged their Code Fixing Model with Open Models, Speculative Decoding and Reinforcement Fine Tuning on Fireworks
PUBLISHED
11/3/2025
Table of Contents
What does Vercel’s v0 Model do?
What was the challenge?
The Vercel x Fireworks Solution
Key Takeaways
Table of Contents
Table of Contents
What does Vercel’s v0 Model do?
What was the challenge?
The Vercel x Fireworks Solution
Key Takeaways
Table of Contents
Vercel
, a leading platform provider for full-stack web applications, partnered with
Fireworks
to solve a critical challenge for their AI code generation tool,
v0
: maximizing both output quality and inference speed at scale. The solution involved optimizing v0’s auto-fixer solution for customized workloads. By implementing advanced techniques, including Reinforcement Fine-Tuning (
RFT
) and
speculative decoding
, Fireworks delivered a massive step-change in performance and quality for Vercel. The result is a platform capable of achieving a
93% error-free generation rate
and a
40X improvement in end-to-end latency
for v0 users, setting a new benchmark for developer-facing AI tooling.
Figure 1: Speed Chart on OSS vs. Closed Source
What does Vercel’s v0 Model do?
Vercel's v0
composite model family is a specialized AI architecture designed to generate high-quality, error-free code for building fast, full-stack web applications. It's a powerful tool for developers because it addresses the limitations of other models by combining retrieval-augmented generation (RAG) for specialized knowledge, reasoning from a large language model (LLM), and a custom streaming post-processing model run on Fireworks for error fixing. This allows it to stay up-to-date with the latest state of the art and results in a significantly higher rate of error-free code generation.
What was the challenge?
Generating functional code from natural language is difficult, but the real complexity lies in fixing runtime and semantic errors. Traditional proprietary models are slow to debug and iterate, creating poor user experiences. Originally Vercel started with a closed source proprietary model, Gemini Flash 2.0. They struggled to achieve their goal of best performance, quality, and latency. Often the only way to do customization on a closed source model would be to use prompt engineering. Manual error correction and error prone AI outputs not only broke builds and slowed developer velocity, but also created delays in product releases, increased operational costs and risked adoption of the v0 Platform. Vercel needed their proprietary auto-fixer model, which was designed for correcting generated code, to operate seamlessly and instantly under high load.
The Vercel x Fireworks Solution
Fireworks enabled real-time, context-aware code fixes with Day-0 access to fine-tuned models, accelerating development while keeping governance and visibility intact.
Malte Ubl, CTO at Vercel, highlighted “Vercel’s v0 model is a composite model. The SOTA in this space changes every day, so you don’t want to tie yourself to a single model. Using a fine-tuned reinforcement learning model with Fireworks, we perform substantially better than SOTA. In our evaluation, Sonnet 3.5 compiled at 62%, and we got our error-free generation rate well into the 90s”
Ido Pesok Engineering at Vercel shared, “The awesome news is our current model takes 2 passes to fix it, while using Fireworks this new model took 1. On a 800 LOC(Lines of Code) file, that is huge!”
The AI model landscape is evolving at an accelerating pace, making it crucial to adapt continuously as today's leading models may quickly be surpassed by new advancements. This rapid change highlights the disadvantage of being locked into a single model. Open-source models offer a significant advantage over closed-source proprietary models in this environment. Fireworks provides day-0 support for many of these open source-models, freeing developers from having to do additional optimization.
Open source models combined with optimizations like with Reinforcement Fine-Tuning (RFT), can achieve superior results compared to proprietary alternatives, demonstrating higher accuracy and faster generation.
This flexibility allowed Vercel developers to keep up with the state of the art and fine-tune solutions to specific problems that might not be possible with the more rigid closed model counterparts.
Leveraging Fireworks’ RFT and Speculative Decoding on its
v0 composite model
, Vercel attained Error-Free generation rates for v0 in the
93rd
percentile. See the table below for more details comparing the generation rates with the different models.
Figure 2:  Code Quality Chart on OSS vs. Closed Source
Model
Error-Free Generation Rate (Quality Score)
v0-1.5-md
93.87
v0-1.5-lg
89.80
claude-4-opus-20250514
78.43
claude-4-sonnet-20250514
64.71
gemini-2.5-flash-preview-05-20
60.78
gemini-2.5-pro-preview-05-06
58.82
o3
58.82
gpt-4.1
58.82
Table 1: Error Generation Rates Between DIfferent Models
(Source:
https://vercel.com/blog/v0-composite-model-family
)
The Auto Fix model consists of a custom function call that constantly checks the output stream for errors and inconsistencies, handling many issues mid-stream. It was trained using reinforcement fine-tuning on Fireworks to minimize error rates and performs significantly faster than other models while maintaining comparable error-free output rates. Both Vercel’s Auto Fix model and its v0 composite model uses Fireworks’ Speculative Decoding to speed up token generation. It predicts the next several tokens using a simple and fast n-gram model, and then an open source LLM confirms the predicted tokens. Any tokens that would have been generated by the LLM are quickly accepted and output as generated tokens. Fireworks’ Adaptive Speculation further speeds up this system by letting the n-gram model predict more tokens when the LLM thinks it has been accurate. This is much quicker than having the LLM generate each token one by one. As seen in Figure 1, Vercel was able to achieve a 40X Speed improvement on the auto-fixer model compared to gpt-4o-mini.
See the below table for more details on the Error-Free Generation Rate and Speed across different models.
Model Name
Error Free Generation Rate (%: Quality Score)
Speed (chars/sec)
vercel-autofixer-01
86.14
8,130.01
gemini-2.5-flash-preview-05-20
89.55
8,130.01
gpt-4o-mini
83.33
238.9
gpt-4.1-nano
79.31
374.26
gemini-2.0-flash
70.3
627.47
claude-3-5-haiku-20241922
61.03
246.05
gemini-2.0-flash-lite
26.67
733.55
Table 2: Autofixer Quality and Speed across different models
(Source:
https://vercel.com/blog/v0-composite-model-family
)
Key Takeaways
The collaboration between Vercel and Fireworks delivered a fundamental step-change in the performance and quality of the v0 AI code generation tool, translating directly into superior developer productivity and business impact:
•
Quality Scores in the 90s for near perfect reliability:
Achieving quality in the 90s means the generated code is reliable and production-ready, minimizing security risks and integration headaches.
•
Blazing Fast with 40X Faster Performance:
Optimizations on Fireworks unlocked more performance compared to proprietary models Gemini 2.0
Have a model you're passionate about, or a feature you need to optimize for performance or quality? Curious about what more RFT or speculative decoding can unlock? We'd love to chat! Connect with us on Discord or send an email to
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
