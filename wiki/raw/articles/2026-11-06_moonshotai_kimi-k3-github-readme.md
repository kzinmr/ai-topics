---
title: "Kimi K3 — Model Repository README (MoonshotAI/Kimi-K3)"
url: "https://github.com/MoonshotAI/Kimi-K3"
fetched_at: 2026-11-06T11:25:00+00:00
source: "github.com (Wayback snapshot 2026-10-12)"
tags: [raw, github]
---

README
License
More items
📰  Tech Blog |     📄  Full Report
## 1. Model Introduction
Kimi K3 is an open-weight, native multimodal agentic model and our most capable model to date. It is a 2.8T-parameter model built on Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), with native vision capabilities and a 1-million-token context window. It is the world's first open 3T-class model, designed for frontier intelligence across long-horizon coding, knowledge work, and reasoning.
## Key Features
New Architecture: Kimi K3 is built on Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), and scales up MoE sparsity with a Stable LatentMoE framework that activates 16 out of 896 experts — yielding an approximate 2.5× improvement in overall scaling efficiency over Kimi K2.
Long-Horizon Coding: Operating with minimal human oversight, Kimi K3 sustains long engineering sessions, navigates massive repositories, and orchestrates terminal tools — from GPU kernel optimization and compiler development to vision-in-the-loop game dev, CAD, and even chip design.
Agentic Knowledge Work: Kimi K3 advances end-to-end knowledge work, producing deep research with interactive visualizations, widgets and dashboards, and motion design and video editing, powered by its native multimodal architecture.
Native Multimodality & Long Context: Kimi K3 understands text, images, and video within the same model, and supports a 1-million-token context window.
Open Frontier Weights: We release the full Kimi K3 model weights under the Kimi K3 License, making frontier intelligence openly available for research, deployment, and further innovation.
## 2. Model Summary
Architecture
Mixture-of-Experts (MoE)
Total Parameters
2.8T
Activated Parameters
104B
Number of Layers
93
Number of Dense Layers
1
Attention-Layer Composition
69 KDA + 24 Gated MLA
Attention Hidden Dimension
7168
Number of Attention Heads
96
Latent MoE Dimension
3584
MoE Hidden Dimension (per Expert)
3072
Number of Experts
896
Selected Experts per Token
16
Number of Shared Experts
2
Vocabulary Size
160K
Context Length
1048576
Attention Mechanism
KDA & Gated MLA
Activation Function
SiTU-GLU
Vision Encoder
MoonViT-V2
Parameters of Vision Encoder
401M
Quantization
MXFP4 weights / MXFP8 activations
(quantization-aware training)
Modality
Text, Image
## 3. Evaluation Results
Benchmark
Kimi K3
(max)
Claude Fable 5
(max, w/ fallback)
GPT-5.6 Sol
(max)
Claude Opus 4.8
(max)
GPT-5.5
(xhigh)
GLM-5.2
(max)
Reasoning & Knowledge
GPQA Diamond
93.5
92.6
94.1
91.0
93.5
91.2
CritPt
23.4
28.6
32.3
20.9
27.1
20.9
AA-LCR
74.7
70.0
73.7
67.7
74.3
71.3
HLE-Full
43.5 / 56.0
53.3 / 63.0
44.5 / 58.0
49.8 / 57.9
41.4 / 52.2
—
Coding
DeepSWE
67.5
70.0
73.0
59.0
67.0
46.2
ProgramBench
77.8
76.8
77.6
71.9
70.8
63.7
Terminal-Bench 2.1
88.3
88.0
88.8
84.6
83.4
82.7
FrontierSWE
81.2
86.6
71.3
66.7
64.9
67.3
SWE-Marathon
42.0
35.0
39.0
40.0
14.0
13.0
PostTrainBench
36.6
41.4
34.6
34.1
28.4
34.3
MLS-Bench-Lite
48.3
49.9
46.2
42.8
35.5
40.4
SciCode
58.7
60.2
56.1
53.5
56.1
50.5
Kimi Code Bench 2.0
72.9
76.9
64.8
71.7
69.0
64.2
Agentic
BrowseComp
91.2
88.0
90.4
84.3
84.4
—
DeepSearchQA (F1)
95.0
94.2
—
93.1
—
—
ResearchRubrics
76.2
—
73.8
73.5
64.0
71.1
GDPval-AA v2 (Elo)
1686
1747
1736
1593
1491
1510
Toolathlon-Verified
76.5
77.9
74.9
76.2
73.5
59.9
MCPMark-Verified
94.5
87.4
92.9
76.4
92.9
—
MCP-Atlas
84.2
84.7
83.6
83.6
82.8
82.6
AutomationBench
30.8
29.1
29.7
27.2
22.7
12.9
JobBench
54.3
57.4
45.4
48.4
38.3
43.4
AA-Briefcase (Elo)
1548
1583
1495
1354
1158
1260
Agents' Last Exam
28.3
25.7†
29.6
27.0
26.6
20.4
APEX-Agents
41.0
43.3
39.9
39.4
38.5
35.6
OfficeQA Pro
63.3
69.9
63.2
63.9
60.9
41.4
SpreadsheetBench 2
34.8
34.7
32.4
31.6
29.1
28.1
OSWorld-Verified
84.8
85.0
83.0
83.4
79.0
—
OSWorld 2.0
58.3
66.1
62.6
55.7
49.5
—
SaaS-Bench
60.1
—
61.4
56.1
43.8
—
τ³-Banking
33.4
26.8
33.0
27.6
31.3
26.8
Harvey Lab-AA
94.6
93.6
87.2
91.1
86.3
91.0
CorpFin v2
71.6
71.8
64.4
66.7
68.4
66.1
Finance Agent v2
54.4
56.3
53.8
53.9
51.8
49.7
Legal Research Bench
44.2
49.5
48.1
43.8
40.4
31.3
Vision
WorldVQA ForceAnswer
51.0
56.7
41.8
39.1
38.5
—
OmniDocBench
91.1
89.8
85.8
87.9
89.4
—
PerceptionBench
58.5
57.2
59.7
47.2
55.8
—
Video-MME (w. sub)
90.0
—
89.5
86.0
89.3
—
MMVU
82.1
—
81.2
79.2
81.7
—
BabyVision w/ python
85.7
90.5
88.9
81.2
83.6
—
MMMU-Pro
81.6 / 83.4
81.2 / 86.5
83.0 / 84.6
78.9 / 82.7
81.2 / 83.2
—
CharXiv (RQ)
84.8 / 91.3
88.9 / 93.5
84.6 / 89.1
80.5 / 89.9
84.1 / 89.0
—
MathVision
94.3 / 97.8
94.8 / 98.6
95.8 / 97.8
86.7 / 97.1
92.2 / 96.8
—
ZeroBench (pass@5)
23.0 / 41.0
23.0 / 46.0
17.0 / 35.0
17.0 / 34.0
22.0 / 41.0
—
Footnotes
All Kimi K3 results are obtained with reasoning effort set to 'max' and temperature = 1.0. For single-step tasks, such as GPQA Diamond, HLE-Full, and vision benchmarks without tools, we set top-p = 0.95; for agentic tasks, we set top-p = 1.0. For HLE-Full, MMMU-Pro, CharXiv (RQ), MathVision, and ZeroBench, each cell reports the scores without and with tool augmentation (general tools for HLE-Full, Python for the vision benchmarks), in that order.
Reasoning & knowledge benchmarks
CritPt and AA-LCR. Scores are cited from Artificial Analysis as of July 23, 2026.
Coding benchmarks
DeepSWE. Kimi K3 is evaluated with the Kimi Code harness. The GLM-5.2 score is taken from the GLM-5.2 release blog; all remaining scores are from the official DeepSWE leaderboard, under which Kimi K3 attains 67.3 with the mini-SWE-agent harness. We report the DeepSWE v1.1 tasks.
Terminal-Bench 2.1. Kimi K3 is evaluated with the Kimi Code harness. For all other models, we report the best score across harnesses: GLM-5.2 with Claude Code (GLM-5.2 release blog); Claude Opus 4.8 and Claude Fable 5 with Terminus 2 (Artificial Analysis); GPT-5.5 and GPT-5.6 Sol with Codex (OpenAI).
ProgramBench. Kimi K3 is evaluated with the Kimi Code harness. The GLM-5.2 score is from the GLM-5.2 release blog; all other scores are from Vals AI.
SWE-Marathon. Kimi K3, Claude Opus 4.8, and Claude Fable 5 are evaluated with the Claude Code harness; GPT-5.6 Sol is evaluated with the Codex harness. The GLM-5.2 score is from the GLM-5.2 release blog. Our evaluation is based on an H20-calibrated branch of the official tasks as of July 9, 2026, prior to the final v1.1 release: the Docker images, performance gates, and reference oracles for the GPU tasks have been recalibrated for H20, while the correctness and anti-cheat validators remain unchanged. Additionally, Claude Fable 5 hit fallbacks on 35% of the tasks in our evaluation, which may have negatively impacted its measured performance.
FrontierSWE. Kimi K3 is evaluated with the Kimi Code harness and GPT-5.6 Sol with the Codex harness; all other results are from FrontierSWE. Dominance scores are recomputed from the raw scores using the official evaluation script and are current as of July 16, 2026.
PostTrainBench. Scores for GLM-5.2, GPT-5.5, and Claude Opus 4.8 are adopted from the official PostTrainBench results. Kimi K3, Claude Fable 5, and GPT-5.6 Sol are evaluated with the official Harbor implementation at maximum reasoning effort, averaged over three runs on H20 GPUs (instead of H100 in the official setting) — Kimi K3 and Claude Fable 5 with the Claude Code harness, and GPT-5.6 Sol with the Codex harness.
MLS-Bench-Lite. Kimi K3 is evaluated with the Kimi Code harness; GLM-5.2 and the Claude models with the Claude Code harness; GPT-5.5 and GPT-5.6 Sol with the Codex harness.
SciCode. Scores are cited from Artificial Analysis as of July 23, 2026.
Kimi Code Bench 2.0 (in-house). Kimi K3 is evaluated with the Kimi Code harness (it attains 73.7 with the Claude Code harness); GLM-5.2, Claude Opus 4.8, and Claude Fable 5 with the Claude Code harness; GPT-5.5 and GPT-5.6 Sol with the Codex harness. All models are evaluated at maximum reasoning effort, except GPT-5.5, which uses the "xhigh" setting. As the benchmark includes cybersecurity and safety-related tasks, we also disclose the fraction of refused or fallback tasks: Claude Fable 5 hit 13 fallbacks and 1 refusal out of 80 tasks; 10 refusals out of 80 tasks entered GPT-5.6 Sol's cyber guard; GPT-5.5 had 3 refusals out of 80 tasks.
Agentic benchmarks
OfficeQA Pro. Each test case provides the agent with the entire PDF corpus, with all PDFs rendered as images and no machine-readable text available.
OfficeQA Pro and SpreadsheetBench 2. Kimi K3, GLM-5.2, Claude Opus 4.8, and Claude Fable 5 are evaluated with the Claude Code harness; GPT-5.5 and GPT-5.6 Sol are evaluated with the Codex harness.
MCP-Atlas. All models are evaluated on the 500-task public subset with a 100-turn limit, using Gemini 3.1 Pro as the judge.
AutomationBench. All models are evaluated on the 600-task public subset, following the official GitHub setup in all other respects.
BrowseComp. We adopt a context-compaction strategy triggered at 300K tokens. When evaluated with the full 1M-token context window and no context management, Kimi K3 achieves a score of 90.4. The results of Claude Fable 5, Claude Opus 4.8, GPT-5.6 Sol, and GPT-5.5 are cited from Anthropic and OpenAI.
GDPval-AA v2, AA-Briefcase, τ³-Banking, Harvey Lab-AA, and APEX-Agents. Scores are cited from Artificial Analysis and the APEX-Agents leaderboard as of July 23, 2026. For Harvey Lab-AA, we report the criterion pass rate.
CorpFin v2, Finance Agent v2, and Legal Research Bench. Scores are cited from Vals AI.
Agents' Last Exam. Scores are cited from the official leaderboard as of July 23, 2026; we report the leaderboard's primary pass-rate metric. On the leaderboard, each model is paired with a specific harness: Kimi K3 with Kimi Code; GPT-5.6 Sol and GPT-5.5 with Codex; Claude Fable 5, Claude Opus 4.8, and GLM-5.2 with Claude Code. † The Claude Fable 5 entry runs at xhigh effort with 40% of tasks annotated as downgraded.
Multimodal benchmarks
Except for ZeroBench, which follows the official setting and is run five times, all multimodal scores are averaged over three runs. MMMU-Pro is evaluated following the official protocol, preserving the original input order and prepending images to the text input.
PerceptionBench is an in-house benchmark that focuses on atomic visual perception capabilities.
## 4. Native MXFP4 Quantization
Kimi K3 applies quantization-aware training from the SFT stage onward, using MXFP4 weights with MXFP8 activations for broad hardware compatibility.
## 5. Deployment
Note
You can access Kimi K3's API on https://platform.kimi.ai by selecting kimi-k3, and we provide an OpenAI/Anthropic-compatible API for you. Currently, Kimi K3 is recommended to run on the following inference engines:
vLLM — see recipes
SGLang — see cookbook
TokenSpeed — see recipes
## 6. Model Usage
Kimi K3 always has thinking enabled, and will return reasoning_content. Thinking effort is configured with the top-level reasoning_effort request field, which supports "low", "high", and "max" (default "max").
Kimi K3 was trained in the preserved thinking history mode. For multi-turn conversations and tool calls, Kimi K3 requires the complete assistant message returned by the API to be passed back to messages as-is — including reasoning_content and tool_calls, not just content:
import openai
def chat_with_preserved_thinking(client: openai.OpenAI, model_name: str):
 messages = [
 {
 "role": "user",
 "content": "Tell me three random numbers."
 },
 {
 "role": "assistant",
 "reasoning_content": "I'll start by listing five numbers: 473, 921, 235, 215, 222, and I'll tell you the first three.",
 "content": "473, 921, 235"
 },
 {
 "role": "user",
 "content": "What are the other two numbers you have in mind?"
 }
 ]
 response = client.chat.completions.create(
 model=model_name,
 messages=messages,
 stream=False,
 max_tokens=4096,
 reasoning_effort="max",
 )
 # the assistant should mention 215 and 222 that appear in the prior reasoning content
 print(f"response: {response.choices[0].message.reasoning}")
 return response.choices[0].message.content
For full guides and examples (vision input, structured output, partial mode, tool choice, dynamic tool loading, context caching), see the Kimi K3 Quickstart and Thinking Effort.
## Coding Agent Framework
Kimi K3 works best with Kimi Code CLI as its agent framework. We warmly invite you to give it a try — run Kimi Code in your terminal and select Kimi K3 using the /model command. We hope you enjoy building with Kimi K3, and we would love to hear your feedback!
## 7. License
Both the code repository and the model weights are released under the Kimi K3 License.
## 8. Contact Us
If you have any questions, please reach out at support@moonshot.ai.