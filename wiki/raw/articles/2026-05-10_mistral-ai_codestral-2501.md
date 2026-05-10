---
title: "Codestral 25.01"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/codestral-2501"
scraped: "2026-05-10T01:20:02.144579+00:00"
lastmod: "2025-05-06T09:10:25.489Z"
type: "sitemap"
---

# Codestral 25.01

**Source**: [https://mistral.ai/news/codestral-2501](https://mistral.ai/news/codestral-2501)

Codestral 25.01
Research
Access the Codestral 25.01 API
Jan 13, 2025
Mistral AI team
Among all the innovations in AI over the past year, code generation has arguably been the most significant. Akin to how the assembly line streamlined manufacturing and the calculator transformed mathematics, coding models represent a significant step change in software development.
Mistral AI has been at the forefront of this change with
Codestral
, a state of the art (SOTA) coding model released earlier this year. Lightweight, fast, and proficient in over 80 programming languages, Codestral is optimized for low-latency, high-frequency usecases and supports tasks such as fill-in-the-middle (FIM), code correction and test generation. Codestral has been used by thousands of developers as a highly capable coding companion, regularly boosting productivity several times over. And today, Codestral is getting a big upgrade.
Codestral 25.01
features a more efficient architecture and an improved tokenizer than the original, generating and completing code about 2 times faster. The model is now the clear leader for coding in its weight class, and SOTA for FIM use cases across the board.
Benchmarks
We have benchmarked the new Codestral with the leading sub-100B parameter coding models that are widely considered to be best-in-class for FIM tasks.
Overview
Python
SQL
Average on several languages
Model
Context length
HumanEval
MBPP
CruxEval
LiveCodeBench
RepoBench
Spider
CanItEdit
HumanEval (average)
HumanEvalFIM (average)
Codestral-2501
256k
86.6%
80.2%
55.5%
37.9%
38.0%
66.5%
50.5%
71.4%
85.9%
Codestral-2405 22B
32k
81.1%
78.2%
51.3%
31.5%
34.0%
63.5%
50.5%
65.6%
82.1%
Codellama 70B instruct
4k
67.1%
70.8%
47.3%
20.0%
11.4%
37.0%
29.5%
55.3%
-
DeepSeek Coder 33B instruct
16k
77.4%
80.2%
49.5%
27.0%
28.4%
60.0%
47.6%
65.1%
85.3%
DeepSeek Coder V2 lite
128k
83.5%
83.2%
49.7%
28.1%
20.0%
72.0%
41.0%
65.9%
84.1%
Per-language
Model
HumanEval Python
HumanEval C++
HumanEval Java
HumanEval Javascript
HumanEval Bash
HumanEval Typescript
HumanEval C#
HumanEval (average)
Codestral-2501
86.6%
78.9%
72.8%
82.6%
43.0%
82.4%
53.2%
71.4%
Codestral-2405 22B
81.1%
68.9%
78.5%
71.4%
40.5%
74.8%
43.7%
65.6%
Codellama 70B instruct
67.1%
56.5%
60.8%
62.7%
32.3%
61.0%
46.8%
55.3%
DeepSeek Coder 33B instruct
77.4%
65.8%
73.4%
73.3%
39.2%
77.4%
49.4%
65.1%
DeepSeek Coder V2 lite
83.5%
68.3%
65.2%
80.8%
34.2%
82.4%
46.8%
65.9%
FIM (single line exact match)
Model
HumanEvalFIM Python
HumanEvalFIM Java
HumanEvalFIM JS
HumanEvalFIM (average)
Codestral-2501
80.2%
89.6%
87.96%
85.89%
Codestral-2405 22B
77.0%
83.2%
86.08%
82.07%
OpenAI FIM API*
80.0%
84.8%
86.5%
83.7%
DeepSeek Chat API
78.8%
89.2%
85.78%
84.63%
DeepSeek Coder V2 lite
78.7%
87.8%
85.90%
84.13%
DeepSeek Coder 33B instruct
80.1%
89.0%
86.80%
85.3%
FIM pass@1:
Model
HumanEvalFIM Python
HumanEvalFIM Java
HumanEvalFIM JS
HumanEvalFIM (average)
Codestral-2501
92.5%
97.1%
96.1%
95.3%
Codestral-2405 22B
90.2%
90.1%
95.0%
91.8%
OpenAI FIM API*
91.1%
91.8%
95.2%
92.7%
DeepSeek Chat API
91.7%
96.1%
95.3%
94.4%
* GPT 3.5 Turbo is the latest FIM API available from OpenAI
Available starting today
Codestral 25.01 is being rolled out to developers worldwide through our IDE / IDE plugin partners. You can feel the difference in response quality and speed for code completion by selecting Codestral 25.01 in their respective model selector.
For enterprise use cases, especially ones that require data and model residency, Codestral 25.01 is available to deploy locally within your premises or VPC.
Check out the demo below and try it for free in Continue for
VS Code
or
JetBrains
.
* Codestral 25.01 Chat Demo
Ty Dunn, co-founder of Continue, said “For AI code assistants, code completion constitutes a large portion of the work, which requires models that are great at fill-in-the-middle (FIM). Codestral 25.01 marks a significant advancement in this area. Mistral AI’s new model is capable of providing more precise suggestions, much faster—a critical component of accurate, efficient software development. This is why Codestral is our recommended autocomplete model for developers.”
To build your own integration with the Codestral API, head over to
la Plateforme
and use
codestral-latest
. The API is also available on Google Cloud's Vertex AI, in private preview on Azure AI Foundry, and coming soon to Amazon Bedrock. To learn more, read the
Codestral documentation
.
Codestral 25.01 is debuting at #1 on the LMsys copilot arena leaderboard. We can’t wait to hear your experience!
Get in touch
Get in touch for large enterprise deployments.
First name
*
Last name
*
Company
*
Email
*
By submitting this form, you agree with our
Terms of Service
. We process your data to respond to your contact request in accordance with our
Privacy Policy.
Submit
