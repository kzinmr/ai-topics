---
title: "DeepSeek R1 Just Got Eyes with Fireworks AI Document Inlining"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/deepseek-r1-got-eyes"
scraped: "2026-05-10T01:27:23.753235+00:00"
lastmod: "2026-02-12T18:52:25.000Z"
type: "sitemap"
---

# DeepSeek R1 Just Got Eyes with Fireworks AI Document Inlining

**Source**: [https://fireworks.ai/blog/deepseek-r1-got-eyes](https://fireworks.ai/blog/deepseek-r1-got-eyes)

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
Deepseek R1 Got Eyes
DeepSeek R1 Just Got Eyes with Fireworks AI Document Inlining
PUBLISHED
2/5/2025
Table of Contents
A Quick Recap of DeepSeek R1
Bridging the Gap: Document Inlining with Fireworks AI
How Does Document Inlining Work?
Technical Deep Dive: API Integration
1. Imports and Dependencies
2. API Client Configuration
3. Constructing the API Request
4. Processing the Output
Experimenting with Different Prompts
Top 5 Findings
Main Contributions
Prompt 2:
Key Benchmark Comparisons:
Distilled Models:
Key Strengths:
Limitations:
Why This Matters to AI Engineers
Conclusion
Table of Contents
Table of Contents
A Quick Recap of DeepSeek R1
Bridging the Gap: Document Inlining with Fireworks AI
How Does Document Inlining Work?
Technical Deep Dive: API Integration
1. Imports and Dependencies
2. API Client Configuration
3. Constructing the API Request
4. Processing the Output
Experimenting with Different Prompts
Top 5 Findings
Main Contributions
Prompt 2:
Key Benchmark Comparisons:
Distilled Models:
Key Strengths:
Limitations:
Why This Matters to AI Engineers
Conclusion
Table of Contents
A smart reasoning LLM is good, but a smart reasoning VLM is better! So let’s give DeepSeek R1 eyes.
We’re excited to demonstrate how
DeepSeek R1
, a state-of-the-art reasoning model from DeepSeek AI, can now process and reason over both text and image inputs using the
Fireworks AI Document Inlining
feature. This capability extends DeepSeek R1’s powerful reasoning to multimodal analysis, opening new avenues for research and application in AI.
A Quick Recap of DeepSeek R1
DeepSeek R1 has been making waves in the AI research community, consistently performing at the top of industry benchmarks and rivaling even some of the most prominent closed-source models. DeepSeek R1, developed by DeepSeek AI, is a state-of-the-art reasoning model with a massive 671 billion parameter (671B) configuration. It has demonstrated top-tier performance across various benchmarks, positioning itself as a leading open-source alternative in the AI space.
For this demo, we are running DeepSeek R1 on the Fireworks AI platform, where it operates at an impressive 100 tokens per second (100t/s) output speed. However, until now, the model's API was limited to textual reasoning—leaving a gap in scenarios that demand a visual understanding.
Bridging the Gap: Document Inlining with Fireworks AI
While DeepSeek R1 excels in complex reasoning tasks, many practical use cases, such as document analysis, research paper summarization, and multimedia content understanding, require a multimodal approach. This is where
Fireworks AI Document Inlining
comes into play. With this new feature, you can effortlessly extend DeepSeek R1’s capabilities into the visual domain.
How Does Document Inlining Work?
The concept is deceptively simple yet incredibly powerful: by appending #transform=inline to the end of your PDF or image URL, you enable the DeepSeek R1 model to inline the document. This transforms your text-based reasoning model into a fully capable vision-language model (VLM) without any additional overhead.
For example, if you have a research paper URL like this:
https://arxiv.org/pdf/2501.12948
simply modify it to:
https://arxiv.org/pdf/2501.12948#transform=inline
This small tweak instructs the model to process and inline the visual content of the document, empowering it to analyze both the textual and visual components seamlessly.
Technical Deep Dive: API Integration
Below, we provide a detailed technical breakdown of how to integrate and utilize the DeepSeek R1 model with the Fireworks AI API for multimodal analysis.
1. Imports and Dependencies
Before making the API call, ensure you have the necessary imports:
1
2
3
4
5
import json
from base64 import b64encode
from fireworks import Fireworks
from pydantic import BaseModel
2. API Client Configuration
Set up the Fireworks client by initializing it with your API key:
1
2
fireworks_client = Fireworks(api_key="YOUR_API_KEY")
3. Constructing the API Request
The request is designed to handle multimodal input, combining both text and images:
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
response = client.chat.completions.create(
model="model-deployment-name",
messages=[
{
"role": "user",
"content": [
{
"type": "image_url",
"image_url": {
"url": "https://arxiv.org/pdf/2501.12948#transform=inline"
},
},
{
"type": "text",
"text": "Summarize the research paper with top 5 findings, and the main contributions of the paper"
},
],
}
],
response_format={"type": "text"}
)
4. Processing the Output
Finally, handle the API response:
1
2
print(response)
The printed output contains the summary generated by
DeepSeek R1,
which now leverages both its reasoning and newly acquired visual analysis capabilities to deliver a comprehensive understanding of the research paper.
Experimenting with Different Prompts
We tested DeepSeek R1 using Fireworks AI Document Inlining with the following two prompts:
1
2
{"text": "Summarize the research paper with top 5 findings, and the main contributions of the paper"}
Result:
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
<think>
Okay, so I need to summarize this research paper. Let me start by reading through the user-provided content carefully. The paper is titled "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" by DeepSeek-AI. The main idea seems to be using reinforcement learning (RL) to enhance the reasoning capabilities of large language models (LLMs) without relying on supervised fine-tuning (SFT) initially.
First, the paper introduces two models: DeepSeek-R1-Zero and DeepSeek-R1. The former is trained using RL directly on the base model, while the latter incorporates some cold-start data and a multi-stage training pipeline. The authors claim that DeepSeek-R1-Zero achieves performance comparable to OpenAI's 01-0912 and that DeepSeek-R1 matches OpenAI-01-1217 on reasoning tasks. They also mention distilling these models into smaller versions, which performed well on benchmarks.
The key contributions mentioned are using RL without SFT, developing a pipeline for DeepSeek-R1, and showing that smaller models can be empowered through distillation. The evaluations cover various reasoning tasks, knowledge benchmarks, and other applications like creative writing.
Top findings probably include the effectiveness of RL in improving reasoning, the self-evolution observed in R1-Zero, the impact of cold-start data in enhancing readability and performance, comparison with existing models like OpenAI's, and the success of distillation. The main contributions would be the RL approach without SFT, the multi-stage training pipeline, distillation results, and releasing open-source models.
Now, I need to structure the summary with five key findings and main contributions. Let me verify each point from the paper. For instance, the emergence of self-verification and reflection in R1-Zero through RL is a finding. The performance comparisons showing DeepSeek-R1's parity with OpenAI-01-1217 is another. The distillation leading to better small models than RL alone is a contribution. Also, the unsuccessful attempts section provides insights into methods that didn't work, which might be relevant but perhaps not a top finding.
Finally, make sure to highlight the benchmarks and open-source contributions. Alright, I think I have all elements needed for the summary.
</think>
Summary of "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
Top 5 Findings
Reinforcement Learning (RL) Alone Achieves Strong Reasoning
:
•
DeepSeek-R1-Zero
, trained purely via RL without supervised fine-tuning (SFT), achieves
71% pass@1
on AIME 2024 (rising to
86.7% with majority voting
), matching OpenAI-01-0912. RL induces emergent reasoning behaviors like self-verification, reflection, and long CoT generation.
Multi-Stage RL + Cold-Start Data Enhances Performance
:
•
DeepSeek-R1
, which combines RL with cold-start SFT data and multi-stage training (incl. rejection sampling and additional alignment), achieves parity with
OpenAI-01-1217
on reasoning benchmarks (79.8% pass@1 on AIME 2024, 97.3% on MATH-500).
Small Models Benefit from Distillation
:
•
Distilling reasoning capabilities from DeepSeek-R1 into smaller models (e.g., 32B, 70B) outperforms RL training on base models. For instance,
DeepSeek-R1-Distill-Qwen-32B
scores
72.6%
on AIME 2024, surpassing OpenAI-01-mini and QwQ-32B-Preview.
Self-Evolution of Reasoning Behaviors
:
•
During RL training, models naturally learn to extend CoT length (e.g., from 15.6% to 71% accuracy on AIME) and develop problem-solving strategies, including correcting early mistakes (observed via "Aha moments" in intermediate checkpoints).
Superior Performance Across Tasks
:
•
DeepSeek-R1 excels in
math/coding
(e.g., Codeforces Elo rating:
2029
, outperforming 96.3% humans),
knowledge benchmarks
(90.8% on MMLU), and
human preference alignment
(87.6% win-rate on AlpacaEval 2.0).
Main Contributions
Pure RL for Reasoning
:
•
First method to validate RL-driven reasoning without SFT. DeepSeek-R1-Zero demonstrates scalability and emergent problem-solving strategies, reducing dependency on curated data.
Cold-Start Multistage Pipeline
:
•
A training pipeline integrating RL with minimal cold-start data (thousands of examples) and iterative SFT/RL stages to improve readability, alignment, and generality.
Open-Source Models and Insights
:
•
Released
DeepSeek-R1-Zero/R1
and
distilled models
(1.5B to 70B). Highlighted distillation’s superiority over direct RL for smaller models, enabling community access to state-of-the-art reasoning capabilities.
Benchmark Advancements
:
•
Set new records for dense models on reasoning tasks (e.g.,
94.3% on GPQA Diamond
for distilled 32B models) and competitive performance against closed models like Claude 3.5 Sonnet and GPT-40.
Failure Analysis
:
•
Shared insights on unsuccessful attempts (e.g., Process Reward Models, Monte Carlo Tree Search) and limitations (language mixing, prompt sensitivity), guiding future research. DeepSeek R1 provided an in-depth breakdown of the research paper, including:
The effectiveness of reinforcement learning (RL) in enhancing reasoning abilities.
The impact of cold-start data on improving readability and performance.
Self-evolution of reasoning behaviors, including self-verification and problem-solving.
Performance comparisons demonstrating parity with OpenAI-01-1217.
Insights from distillation techniques used for smaller models.
Prompt 2:
1
2
{"text": "How does the R1 model perform on the benchmarks compared to other models?"}
1
2
3
4
5
<think>
Okay, let me try to figure out how the R1 model performs compared to other models based on the provided context. First, I'll start by skimming through the sections where benchmark results are mentioned. The paper has several sections discussing experiments and evaluations, like Section 3.1 and 3.2. In Table 4, there's a detailed comparison between DeepSeek-R1 and other models like Claude-3.5, GPT-40, DeepSeek-V3, OpenAI-01-mini, and OpenAI-01-1217. Looking at the numbers, it seems that DeepSeek-R1 matches or surpasses these models on various benchmarks. For instance, on AIME 2024, R1 scores 79.8% pass@1, which is slightly higher than OpenAI-01-1217's 79.2%. On MATH-500, it's even better with 97.3% versus 96.4%. The Codeforces rating for R1 is 2029, which is just under OpenAI's 2061 but still outperforms 96.3% of human participants. For tasks like MMLU and MMLU-Pro, R1 scores 90.8% and 84.0% respectively, trailing only slightly behind OpenAI-01-1217 but still leading others. In some areas like AlpacaEval 2.0 and ArenaHard, R1 shows strong performance with 87.6% and 92.3% win rates, which suggests excellent general capabilities beyond just reasoning. The distilled models also perform well, with the 32B and 70B versions surpassing QwQ-32B-Preview and even OpenAI-01-mini on several benchmarks. The paper mentions that distillation helps smaller models achieve competitive results without RL, indicating R1's effectiveness as a teacher model. The discussion also notes that R1 has some limitations, like sensitivity to prompts and issues with non-English languages, but overall, it's positioned as competitive with top models like OpenAI's, especially in reasoning tasks.
</think>
The DeepSeek-R1 model demonstrates competitive performance across various benchmarks compared to other state-of-the-art models, particularly matching or slightly exceeding OpenAI-01-1217 in many reasoning tasks while maintaining strong general capabilities:
Key Benchmark Comparisons:
Reasoning Tasks
:
•
AIME 2024
: 79.8% Pass@1 (vs. OpenAI-01-1217: 79.2%)
•
MATH-500
: 97.3% Pass@1 (vs. OpenAI-01-1217: 96.4%)
•
CodeForces
: 2029 Elo rating (human-crush level, outperforming 96.3% of competition participants) and 96.3% problem-solving accuracy (vs. OpenAI-01-1217: 96.6%).
Knowledge Tasks
:
•
MMLU
: 90.8% (vs. OpenAI-01-1217: 91.8%)
•
MMLU-Pro
: 84.0% (slightly trailing OpenAI-01-1217: 84.0%)
•
GPQA Diamond
: 71.5% (vs. OpenAI-01-1217: 75.7%).
General Capabilities
:
•
AlpacaEval 2.0
: 87.6% win-rate (surpassing GPT-40 and DeepSeek-V3)
•
ArenaHard
: 92.3% win-rate (vs. OpenAI-01-1217's unpublished baseline).
Coding Tasks
:
•
LiveCodeBench
: 65.9% Pass@1 (vs. OpenAI-01-1217: 63.4%).
Distilled Models:
•
The distilled models (1.5B to 70B) outperform base models like GPT-40 and Claude-3.5-Sonnet, with
DeepSeek-R1-Distill-Qwen-32B
achieving 72.6% on AIME 2024 and 94.3% on MATH-500, surpassing QwQ-32B-Preview and rivaling OpenAI-01-mini.
Key Strengths:
•
Cold-Start Advantage
: R1 avoids the readability/language-mixing issues of its predecessor (R1-Zero) by incorporating multi-stage training.
•
Scalability
: Distillation transfers reasoning patterns effectively to smaller models (e.g., 7B model outperforms Qwen-32B-Preview).
•
Versatility
: Strong performance on both exam-style reasoning (AIME, MATH) and practical tasks (Codeforces, software engineering).
Limitations:
•
Underperforms OpenAI-01-1217 on engineering-focused coding benchmarks (e.g., SWE-Bench Verified: 49.2% vs. 48.9%).
•
Sensitive to prompting strategies (zero-shot preferred over few-shot).
•
Language mixing persists in non-English/Chinese prompts.
Overall, DeepSeek-R1 sets new benchmarks for open-source models and matches leading proprietary models like OpenAI-01-1217 in core reasoning tasks while offering scalability via distillation. DeepSeek R1 was benchmarked against leading models, showing:
•
AIME 2024
: 79.8% pass@1, slightly outperforming OpenAI-01-1217 (79.2%).
•
MATH-500
: 97.3% pass@1, surpassing OpenAI-01-1217 (96.4%).
•
CodeForces Elo
: 2029, outperforming 96.3% of human participants.
•
MMLU
: 90.8%, close to OpenAI-01-1217 (91.8%).
•
Distilled Model Performance
: Smaller models achieved competitive results, showcasing DeepSeek R1’s effectiveness as a teacher model.
These results illustrate DeepSeek R1’s ability to match or surpass other state-of-the-art models, particularly in reasoning tasks, while also demonstrating its capability in distillation to create high-performing smaller models.
Why This Matters to AI Engineers
Integrating document inlining into DeepSeek R1 represents a significant advancement for AI engineers looking to build systems that require deep multimodal analysis. By seamlessly combining textual reasoning with visual comprehension, the Fireworks AI Document Inlining feature addresses critical gaps in current use-cases, such as:
•
Research Analysis
: Automatically extracting key insights from research papers that include both text and figures.
•
Multimedia Content Processing
: Handling complex documents that blend images and text without the need for separate processing pipelines.
•
Enhanced User Applications
: Empowering applications like digital assistants and knowledge management systems with comprehensive content understanding.
Conclusion
The integration of
Fireworks AI Document Inlining
with the DeepSeek R1 model heralds a new era of multimodal reasoning. By simply appending #transform=inline to your document URLs, you unlock a vast new set of capabilities, transforming DeepSeek R1 from a powerful textual reasoning model into a comprehensive vision-language model.
For AI engineers eager to harness these capabilities, the code example provided above offers a straightforward pathway to integrate and experiment with this hybrid approach. As the AI community continues to push the boundaries of what’s possible, innovations like this pave the way for richer, more context-aware systems that are well-equipped to tackle real-world challenges.
Happy coding and exploring:
fireworks.ai
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
