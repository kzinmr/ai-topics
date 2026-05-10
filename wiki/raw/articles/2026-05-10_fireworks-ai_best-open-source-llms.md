---
title: "Best Open Source LLMs in 2026: We Reviewed 7 Models"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/best-open-source-llms"
scraped: "2026-05-10T01:27:08.614513+00:00"
lastmod: "2026-03-20T21:35:08.000Z"
type: "sitemap"
---

# Best Open Source LLMs in 2026: We Reviewed 7 Models

**Source**: [https://fireworks.ai/blog/best-open-source-llms](https://fireworks.ai/blog/best-open-source-llms)

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
Best Open Source Llms
Best Open Source LLMs in 2026: We Reviewed 7 Models
PUBLISHED
1/13/2026
Table of Contents
The best open source LLMs at a glance
What makes a great open source LLM?
How we evaluated these models
How these models compare on benchmarks
Reasoning and knowledge
Software engineering performance
Key takeaways
Kimi K2.5
What is Kimi K2.5?
Who should use Kimi K2.5?
Standout features
Pros and cons
FAQ
Kimi K2 Thinking
What is Kimi K2 Thinking?
Who should use Kimi K2 Thinking?
Standout features
Pros and cons
Qwen3 VL 235B A22B (Vision + LLM)
What is Qwen3 VL 235B?
Who should use Qwen3 VL 235B?
Standout features
Pros and cons
FAQ
GLM-5
What is GLM-5?
Who should use GLM-5?
Standout features
Pros and cons
FAQ
DeepSeek v3.2
What is DeepSeek v3.2?
Who should use DeepSeek v3.2?
Standout features
Pros and cons
FAQ
Google Gemma 3
What is Google Gemma 3?
Who should use Google Gemma 3?
Standout features
Pros and cons
FAQ
MiniMax-M2.5
What is MiniMax-M2.5?
Who should use MiniMax-M2.5?
Standout features
Pros and cons
FAQ
Why run these models on Fireworks
Performance at scale
Deployment options
Why it matters for these models
Table of Contents
Table of Contents
The best open source LLMs at a glance
What makes a great open source LLM?
How we evaluated these models
How these models compare on benchmarks
Reasoning and knowledge
Software engineering performance
Key takeaways
Kimi K2.5
What is Kimi K2.5?
Who should use Kimi K2.5?
Standout features
Pros and cons
FAQ
Kimi K2 Thinking
What is Kimi K2 Thinking?
Who should use Kimi K2 Thinking?
Standout features
Pros and cons
Qwen3 VL 235B A22B (Vision + LLM)
What is Qwen3 VL 235B?
Who should use Qwen3 VL 235B?
Standout features
Pros and cons
FAQ
GLM-5
What is GLM-5?
Who should use GLM-5?
Standout features
Pros and cons
FAQ
DeepSeek v3.2
What is DeepSeek v3.2?
Who should use DeepSeek v3.2?
Standout features
Pros and cons
FAQ
Google Gemma 3
What is Google Gemma 3?
Who should use Google Gemma 3?
Standout features
Pros and cons
FAQ
MiniMax-M2.5
What is MiniMax-M2.5?
Who should use MiniMax-M2.5?
Standout features
Pros and cons
FAQ
Why run these models on Fireworks
Performance at scale
Deployment options
Why it matters for these models
Table of Contents
With new open source LLMs launching nearly every week, figuring out which model actually fits your use case has become its own research project. Models like DeepSeek v3.2, Kimi K2.5, and Qwen3 VL now compete at the frontier. Each brings distinct strengths in reasoning, multimodal understanding, and efficiency.
The stakes are higher than benchmark scores suggest. Your choice of foundation model shapes inference costs, response latency, and the quality your users experience in production.
This roundup compares the top open source LLMs available today, breaking down their trade-offs and ideal applications so you can make an informed decision without running your own eval suite.
TL;DR
•
Choose
Kimi K2.5
if you need visual-to-code generation, agent swarms, and multimodal coding at scale.
•
Choose
Qwen3 VL 235B
if you need frontier-grade vision, OCR across 32 languages, and GUI automation.
•
Choose
DeepSeek v3.2
if you need elite math reasoning and cost-efficient coding at scale.
•
Choose
Google Gemma 3
if you need multimodal capabilities on a single consumer GPU.
MoE architectures dominate this generation: trillion-parameter models that activate only 10B to 40B parameters per token. All seven models in this roundup are available on Fireworks for instant serverless inference.
Talk to an expert
The best open source LLMs at a glance
Model
Release date
Params
Context window
Best for
On Fireworks
MiniMax-M2.5
February 12, 2026
229B total (10B active)
196,608 tokens
Real-world productivity and software engineering workflows
Try in playground
GLM-5
February 12, 2026
744B total (40B active)
200K input tokens
Complex systems engineering and long-horizon agentic tasks
Try in playground
Kimi K2.5
January 27, 2026
1 Trillion total (32B active)
256K tokens
Front-end visual coding and distributed market research
Try in playground
DeepSeek v3.2
December 1, 2025
671B total (37B active)
128K - 163K tokens
Math reasoning, enterprise agents, and coding (96.0% GSM8K, 67.8% SWE-Bench)
Try in playground
Kimi K2 Thinking
November 6, 2025
1 Trillion total (32B active)
256,000 tokens
Building autonomous AI agents and coding assistants
Try in playground
Qwen3 VL 235B A22B (Vision + LLM)
September 22, 2025
235B total, 22B active
256K tokens natively
Deep visual comprehension and agentic GUI automation
On-demand deployment
Google Gemma 3
March 12, 2025
270M, 1B, 4B, 12B, 27B
128K tokens
Local agentic workflows and on-device vision tasks
On-demand deployment
What makes a great open source LLM?
Architecture efficiency is the single biggest differentiator in this generation. Six of seven models here use Mixture-of-Experts (MoE), activating a fraction of their total parameters per token. Kimi K2 Thinking has 1 trillion total parameters but only fires 32B per inference step. DeepSeek v3.2 runs 37B of its 671B. That ratio directly determines your GPU bill.
Context window size matters, but only if the model holds coherence at length. A 256K window is useless if the model hallucinates at 100K. DeepSeek's Sparse Attention mechanism and GLM-5's 128K output limit represent distinct engineering approaches to the same problem: maintaining quality across long sequences while keeping memory consumption manageable.
Licensing determines what you can ship. Apache 2.0 (Qwen3 VL) and MIT (DeepSeek v3.2, GLM-5) impose minimal restrictions. Modified MIT licenses (Kimi K2.5, MiniMax) add usage constraints worth reading before you build a product. For example:
The Kimi K2.5 MIT License modification adds a commercial attribution clause
for hyperscale usage — if your product exceeds certain thresholds (commonly cited as >100 million monthly active users or >$20 million monthly revenue), you must prominently display “Kimi K2.5” in your product’s interface or marketing.
How we evaluated these models
We reviewed technical specifications, architecture papers, and official benchmark results from model cards and HuggingFace repositories. Community feedback from r/LocalLLaMA, Hacker News, and GitHub issues informed our assessment of real-world strengths and failure modes that benchmarks alone miss.
We compared models across reasoning quality, coding performance, hardware requirements, licensing terms, and production readiness. Benchmark scores come from official sources and verified third-party evaluations, not self-reported marketing claims.
How these models compare on benchmarks
For evaluating the best open source LLMs, we focus on benchmarks that test core reasoning, coding ability, and general knowledge: the fundamental capabilities users expect from top-tier language models.
Claude Opus 4.6 benchmarks are provided for reference.
Reasoning and knowledge
Model
GSM8K (Math)
MMLU (Knowledge)
Kimi K2.5
94.1%
Not available
Qwen3 VL 235B
90.3%
87.1%
GLM-5
Not available
Not available
Kimi K2 Thinking
93.9%
83.2%
DeepSeek v3.2
96.0%
80.9% - 81.9%
Google Gemma 3 (27B)
95.9%
76.9%
MiniMax-M2.5
Not available
Not available
Opus 4.6
99%
91%
What these benchmarks measure:
•
GSM8K
: Mathematical reasoning through grade school math word problems
•
MMLU
: Broad knowledge across 57 academic subjects from elementary to professional level
Software engineering performance
Model
SWE-Bench Verified
GPQA-Diamond
GLM-5
77.8%
86.0%
DeepSeek v3.2
73.1%
Not available
MiniMax-M2.5
80.2%
85.2%
Kimi K2 Thinking
71.3%
85.7%
Kimi K2.5
76.8%
87.6%
Google Gemma 3 (27B)
Not available
Not available
Qwen3 VL 235B
Not available
Not available
Opus 4.6
80.8%
91.3%
Key takeaways
•
DeepSeek v3.2 leads in mathematical reasoning
with 96.0% on GSM8K
•
MiniMax-M2.5 tops SWE-Bench
at 80.2%, matching Claude Opus 4.6 levels
•
Qwen3 VL 235B has the highest MMLU score
at 87.1%, reflecting broad knowledge coverage
•
Benchmark reporting varies widely
: newer models like GLM-5 report on specialized benchmarks (AIME, Vending Bench) rather than traditional metrics
Note: Benchmark scores shown are from official model cards, third-party evaluations, and technical reports. Actual performance varies based on prompt engineering, quantization, and inference settings.
Kimi K2.5
What is Kimi K2.5?
•
Release Date:
January 27, 2026
•
Parameters:
1 trillion total (32B active per token), 400M MoonViT vision encoder
•
Context Window:
256K tokens
•
License:
Modified MIT License
•
GitHub Stars:
~1.2k Not available
•
Corporate Sponsor:
Moonshot AI
•
Official Repo:
github.com/MoonshotAI/Kimi-K2.5
🚀 Try Kimi K2.5 on Fireworks →
Kimi K2.5 is the multimodal successor to K2 Thinking, adding native vision through a 400M-parameter MoonViT encoder jointly pre-trained on 15 trillion mixed tokens. It shares the same 1-trillion-parameter MoE backbone (61 layers, 384 experts, 8 routed per token) but introduces Parallel-Agent Reinforcement Learning (PARL) for spawning up to 100 concurrent sub-agents.
The model's sweet spot is visual-to-code workflows. Feed it a UI mockup, and it generates functional React/CSS components with scroll-triggered animations. Community users report costs at roughly 1/8th of Claude Opus for comparable coding quality, though first-pass output tends to be verbose and over-engineered. Its Chatbot Arena ELO of 1451 places it among the highest-ranked open models.
Who should use Kimi K2.5?
Frontend developers prototyping UIs from design files. The model autonomously generates interactive code from static images or video workflows, handling layout, animations, and responsive design in a single pass.
Teams running distributed research workflows benefit from Agent Swarm mode, which decomposes broad queries into parallel sub-tasks. A market analysis request splits into simultaneous competitor searches across multiple domains. Be prepared for latency: users report 20+ minute wait times on very broad queries.
Standout features
•
Visual-to-code generation
from UI mockups, producing functional React/CSS with animations
•
Agent Swarm mode
boosts BrowseComp scores from 60.6% (single-agent) to 78.4% (parallel)
•
Chatbot Arena ELO of 1451
, among the highest for open models
•
MMLU-Pro score of 87.1%
for advanced knowledge tasks
•
GSM8K accuracy of 94.09%
for mathematical reasoning
•
HLE with tools score of 50.2%
, surpassing the K2 Thinking variant
Pros and cons
Pros
Cons
Generates functional frontend code directly from design mockups
First-pass code is often verbose and over-engineered, requiring simplification prompts
Agent Swarm mode parallelizes research across 100 sub-agents
Scores -11 on AA-Omniscience index , indicating frequent general knowledge hallucinations
~1/8th the API cost of Claude Opus for comparable coding quality
Agent Swarm mode can take 20+ minutes on broad, open-ended research queries, per community reports
Native multimodality trained jointly, not bolted on
Local deployment requires 240GB+ unified memory even at 1.8-bit quantization
FAQ
Q: How does K2.5 differ from K2 Thinking?
K2.5 adds native vision (400M MoonViT encoder), Agent Swarm parallel execution, and a higher HLE score (50.2% vs 44.9%). K2 Thinking is text-only and better suited for pure reasoning chains. K2.5 is the choice when visual inputs are involved.
Q: Why does Agent Swarm mode feel slow?
Each sub-agent runs its own search-and-synthesis loop. Broad queries spawn many agents that each take time to resolve. Narrow, cleanly decoupled tasks (search 10 competitors simultaneously) complete faster than open-ended research.
Q: How do I get less verbose code from K2.5?
Append explicit instructions like "Write simple, maintainable code without over-engineering" to your initial prompt. The model responds well to simplification requests on the second pass.
Q: K2.5 or Qwen3 VL for vision tasks?
Qwen3 VL has better OCR (32 languages) and higher MMLU (87.1% vs 87.1% MMLU-Pro, different benchmarks). K2.5 excels specifically at visual-to-code generation and frontend prototyping. For document processing and GUI agents, Qwen3 VL wins. For building UIs from mockups, K2.5 wins.
See
Kimi K2.5 API
details on Fireworks.
🚀 Try Kimi K2.5 in the Fireworks Playground →
Kimi K2 Thinking
What is Kimi K2 Thinking?
•
Release Date:
November 6, 2025
•
Parameters:
1 trillion total (32B active per token)
•
Context Window:
256,000 tokens
•
License:
Modified MIT License
•
GitHub Stars:
10.4k
•
Corporate Sponsor:
Moonshot AI
•
Official Repo:
github.com/MoonshotAI/Kimi-K2
🚀 Try Kimi K2 Thinking on Fireworks →
Kimi K2 Thinking is a trillion-parameter MoE model built by Moonshot AI as a "thinking agent" that reasons step-by-step while dynamically invoking external tools. It uses 384 experts (8 selected per token), Multi-head Latent Attention, and SwiGLU activations across 61 layers. The model natively supports INT4 quantization via Quantization-Aware Training, achieving 2x generation speed with minimal quality loss.
The design philosophy centers on long-horizon autonomy. Where other models struggle after a dozen tool calls, Kimi K2 Thinking executes 200 to 300 sequential tool calls (browsing, Python execution, file operations) without losing coherence or drifting from the original goal. Community users report it as the first open-weights model to match proprietary models like Claude 4.5 Sonnet in complex agentic workflows.
Who should use Kimi K2 Thinking?
Developers building autonomous AI agents and coding assistants that require stable, long-running tool orchestration. If your application chains web searches, code execution, and file manipulation across hundreds of steps, this model was built for it.
Research teams benefit from its agent swarm capabilities: the newer K2.5 update adds an orchestrator that spawns up to 100 sub-agents for parallel execution. Financial analysts chain hundreds of web searches to build comprehensive reports on supply chains and competitor pricing.
Standout features
•
200-300 sequential tool calls
without coherence loss, verified by community practitioners
•
Native INT4 quantization
via QAT delivers 2x speed-up with no measurable quality degradation
•
Agent swarm mode
dynamically spawns up to 100 parallel sub-agents for concurrent task execution
•
Chatbot Arena ELO of 1438
, placing it among frontier-tier models
•
HLE with tools score of 44.9%
under INT4 precision, reflecting realistic deployment performance
Pros and cons
Pros
Cons
Unmatched tool-call chain length (200-300 calls without drift)
Requires ~240GB combined RAM/VRAM even when quantized to fit locally
Native INT4 quantization preserves quality at 2x speed
Generates up to 2.5x more tokens than competitors due to extended thinking
Open weights under Modified MIT license
Occasional loops when tool-calling chains exceed context limits in some IDEs
First open model competitive with Claude 4.5 Sonnet on agentic tasks
Temperature must be set to 1.0 for optimal performance (counterintuitive)
See
Kimi K2 Thinking API
details on Fireworks.
🚀 Try Kimi K2 Thinking in the Fireworks Playground →
Qwen3 VL 235B A22B (Vision + LLM)
What is Qwen3 VL 235B?
•
Release Date:
September 22, 2025
•
Parameters:
235B total, 22B active per token
•
Context Window:
256K tokens natively (expandable to 1M)
•
License:
Apache 2.0
•
GitHub Stars:
~26.7k
•
Corporate Sponsor:
Alibaba Cloud (Qwen Team)
•
Official Repo:
github.com/QwenLM/Qwen3-VL
🚀 Qwen3 VL 235B Available for On-Demand Deployment on Fireworks →
Qwen3-VL-235B-A22B is Alibaba Cloud's largest multimodal model, combining text and visual processing through an MoE architecture with Interleaved-MRoPE and DeepStack. It comes in both Instruct and reasoning-enhanced Thinking variants. OCR support covers 32 languages, and the vision encoder handles everything from hand-drawn sketches to complex GUI screenshots.
The model's standout trait is cross-modal depth. Community users report it correctly identifies specific retro video game locations and obscure movie scenes from contextless screenshots, tasks where the 235B parameter count pays for itself in stored world knowledge. For pure vision tasks, smaller Qwen3-VL variants (32B, 35B) often perform comparably. The 235B excels when deep reasoning meets visual input.
Who should use Qwen3 VL 235B?
Teams building computer-use agents, RPA systems, or any application that parses GUIs. The model outputs accurate relative coordinates for clicking UI elements, adapting to different screen resolutions without hardcoded pixel values.
Frontend developers converting design mockups into HTML/CSS/JS code get strong results. The model reliably recreates UIs from screenshots or hand-drawn wireframes. Document processing teams benefit from its 32-language OCR, which handles poor lighting and complex layouts.
Standout features
•
32-language OCR
that handles degraded images, poor lighting, and complex document layouts
•
GUI agent capabilities
with normalized relative coordinate output for any screen resolution
•
MMLU score of 87.1%
, the highest knowledge benchmark in this roundup
•
Apache 2.0 license
with no commercial restrictions
•
Expandable to 1M tokens
of context for massive document processing
•
HellaSwag score of 87.8%
, indicating strong common sense reasoning
Pros and cons
Pros
Cons
Best-in-class vision and OCR across 32 languages
Severe VRAM memory leaks reported when running on vLLM for continuous image processing
Apache 2.0 license allows unrestricted commercial use
Aggressive quantization (Q4) disproportionately degrades reasoning in MoE architectures
GUI grounding accurate enough for production RPA agents
Smaller Qwen3-VL variants offer better performance-to-hardware ratios for pure vision tasks
Highest MMLU score (87.1%) among models reviewed
Minor OCR hallucinations on hex values (confusing '4' for 'A', '7' for '1')
FAQ
Q: Is the 235B model worth it over smaller Qwen3-VL variants?
For pure vision and OCR, the 32B and 35B models perform within striking distance. The 235B justifies its hardware cost when tasks require both deep world knowledge and visual reasoning, like identifying obscure content from screenshots or complex STEM problem-solving with diagrams.
Q: How do I handle the vLLM memory leak?
Schedule periodic server restarts. Setting
--enforce-eager
or changing
tp_mode
does not resolve the issue in vLLM v0.11.1. Keep the vision encoder (
mmproj
) in FP16 or Q8_0 even if you quantize the language model heavily.
Q: What local inference speeds can I expect?
On RTX 5090s with smaller quants, prompt processing hits 2,000 to 3,000 tokens/second with generation around 60 tokens/second. The full 235B model with heavy CPU RAM offloading runs at roughly 15 tokens/second.
Q: How does it compare to GPT-5 for vision tasks?
Community users validate that the Thinking variant feels GPT-5-class for vision, particularly in STEM, math, and spatial reasoning tasks. It outperforms Gemma 3 and Mistral models in visual comprehension by a wide margin.
See
Qwen3 VL 235B API
details on Fireworks.
🚀 Qwen3 VL 235B Available for On-Demand Deployment on Fireworks →
GLM-5
What is GLM-5?
•
Release Date:
February 12, 2026
•
Parameters:
744B total (40B active per token)
•
Context Window:
200K input tokens (up to 128K output tokens)
•
License:
MIT License (weights) / Apache 2.0 (code)
•
GitHub Stars:
~1.4k
•
Corporate Sponsor:
Zhipu AI (
Z.ai
)
•
Official Repo:
github.com/zai-org/GLM-5
🚀 Try GLM-5 on Fireworks →
GLM-5 is Zhipu AI's largest foundation model, built for complex systems engineering and long-horizon agentic workflows. Its defining feature: up to 128K output tokens per inference pass. This eliminates the looping workarounds required when generating entire codebases or lengthy reports. The MoE architecture activates 40B of its 744B total parameters, and it uses DeepSeek Sparse Attention for efficient long-context processing.
The model was pre-trained entirely on domestic Chinese hardware (Huawei Ascend chips). Community users report a 56% reduction in hallucinations compared to its predecessor GLM-4.7, particularly during sustained coding tasks. On SWE-Bench Verified, it scores 77.8%, placing it above Gemini 3 Pro and GPT-5.2 for software engineering.
Who should use GLM-5?
Developers building automated PR workflows and full-stack code generation pipelines. The 128K output limit means you generate complete modules, reports, or game codebases in a single inference pass without chunking scripts.
Teams working on long-horizon agentic tasks (economic simulations, multi-step operational planning) benefit from the 200K input context combined with massive output capacity. Backend refactoring projects that need to ingest entire repositories at once are a natural fit.
Standout features
•
128K output tokens
per pass, the largest in this roundup, eliminating generation loops
•
SWE-Bench Verified score of 77.8%
, beating Gemini 3 Pro and GPT-5.2
•
AIME 2026 I score of 92.7%
for advanced mathematical reasoning
•
MIT-licensed weights
with no commercial restrictions
•
56% hallucination reduction
vs. GLM-4.7 during sustained coding, per community reports
•
Vending Bench 2 score of $4,432
, ranking first among open models for long-term operational tasks
Pros and cons
Pros
Cons
128K output eliminates need for looping in large generation tasks
Requires enterprise-grade clusters or extreme prosumer rigs (dual RTX 6000s minimum) for local use
MIT license with no usage restrictions
Official GLM-5 API performance can vary under load (latency spikes and throttling), though third-party inference providers like Fireworks can help mitigate these issues.
77.8% on SWE-Bench Verified places it among frontier coding models
Community speculation about training data overlap with Anthropic models due to stylistic similarities
Activates only 40B parameters despite 744B total size
Full 200K context processing is painfully slow locally
FAQ
Q: How fast is GLM-5 when running locally?
On dual RTX Pro 6000 / Threadripper setups using MXFP4/Q2 quantization, users report 16.5 to 17 tokens/second. You need at minimum 128GB of combined RAM/VRAM and should limit context to 16K if speed is a priority.
Q: What is the "Claude personality" issue?
Some users on Reddit
discovered that when given a system prompt claiming it is Claude, GLM-5 changes writing style and bypasses built-in censorship. This suggests training data overlap with Anthropic model outputs, though it does not affect normal operation.
Q: How does GLM-5 compare to Claude Opus for coding?
Community consensus: performance parity with Opus 4.5 for implementation. Opus is faster and slightly better at high-level structural decisions. GLM-5 excels at dense, heavy code generation, especially when you need thousands of lines in a single pass.
Q: Should I use GLM-5 or DeepSeek v3.2 for coding?
GLM-5 has the higher SWE-Bench score (77.8% vs 73.1%) and the 128K output limit is a clear advantage for large-scale generation. DeepSeek v3.2 is faster for interactive coding with shorter outputs and excels in pure mathematical reasoning.
See
GLM-5 API
details on Fireworks.
🚀 Try GLM-5 in the Fireworks Playground →
DeepSeek v3.2
What is DeepSeek v3.2?
•
Release Date:
December 1, 2025
•
Parameters:
671B total (37B active per token)
•
Context Window:
128K
•
License:
MIT License
•
GitHub Stars:
~1.5k
•
Corporate Sponsor:
DeepSeek
•
Official Repo:
github.com/deepseek-ai/DeepSeek-V3.2-Exp
🚀 Try DeepSeek v3.2 on Fireworks →
DeepSeek-V3.2 is a reasoning-first MoE model engineered for mathematical problem-solving and agentic coding. Its standout innovation is DeepSeek Sparse Attention (DSA), which cuts memory consumption and speeds up reasoning paths by up to 3x for long-context scenarios. The model comes in three variants: Base, Exp, and Speciale (a maximum-compute reasoning variant).
The "Thinking in Tool-Use" architecture separates it from predecessors. Where older models discard their reasoning trace after invoking a tool, V3.2 retains its chain-of-thought and tool-call history throughout the session. The Speciale variant achieves gold-medal performance on IMO 2025 and 96.0% on AIME 2025, placing it at the frontier of mathematical AI. All of this ships under a permissive MIT license.
Who should use DeepSeek v3.2?
Teams building autonomous coding agents that need to write, test, and fix code without human intervention. The model's 67.8% on SWE-Bench Verified means it resolves real-world GitHub issues at a high rate. Developers using tools like Cline and Aider get strong results.
Researchers and power users tackling Olympiad-level math problems through the Speciale API variant. The base model handles complex tool-use workflows where persistent reasoning context across multiple invocations saves tokens and reduces errors.
Standout features
•
96.0% on GSM8K
, the highest math reasoning score in this roundup
•
DeepSeek Sparse Attention
delivers up to 3x faster long-context reasoning with lower memory
•
Persistent chain-of-thought
across tool calls (thinking in tool-use)
•
MIT license
with no commercial restrictions
•
Speciale variant
achieves IMO 2025 gold-medal performance
•
HMMT score of 99.2%
, surpassing Gemini's 97.5%
Pros and cons
Pros
Cons
Highest GSM8K score (96.0%) and IMO gold-level math performance
Full 671B model requires massive VRAM for local deployment
DSA mechanism cuts memory and speeds long-context reasoning by 3x
Web interface reportedly buggier than the API for code debugging
MIT license allows unrestricted commercial use
Speciale variant is API-only and does not support tool-calling
Retains reasoning trace between tool calls, saving tokens
Tensor Parallelism 8 on Hopper/Blackwell GPUs causes severe overhead due to kernel padding
FAQ
Q: What's the difference between Base, Exp, and Speciale variants?
Base is the standard model. Exp is the experimental release with expanded capabilities. Speciale is a high-compute reasoning variant that uses extended thinking for maximum accuracy on hard problems. Speciale is API-only and deliberately omits tool-calling support.
Q: How does DeepSeek v3.2 compare to GPT-5?
The Speciale variant edges out GPT-5 High on AIME 2025 (96.0% vs 94.6%) and HMMT (99.2% vs 97.5%). For interactive coding, community users rate it comparable to Claude Opus 4.5 on single-prompt tasks. GPT-5 retains a slight edge on some pure text-only reasoning metrics.
Q: Any tips for running it on vLLM?
Set
VLLM_USE_DEEP_GEMM=0
to disable the MoE part of DeepGEMM and skip long warmups, especially on H20 GPUs. Avoid TP=8 on Hopper/Blackwell GPUs: the kernel pads from 16 heads per rank to 64, creating massive overhead.
Q: How should I handle multi-turn API calls?
Always preserve and return the complete
reasoning_details
array in your API requests. This prevents the model from wasting tokens recalculating its previous logic across conversation turns.
See
DeepSeek v3.2 API
details on Fireworks.
🚀 Try DeepSeek v3.2 in the Fireworks Playground →
Google Gemma 3
What is Google Gemma 3?
•
Release Date:
March 12, 2025
•
Parameters:
270M, 1B, 4B, 12B, 27B
•
Context Window:
128K tokens
•
License:
Gemma Terms of Use
•
GitHub Stars:
4.1k Not available
•
Corporate Sponsor:
Google DeepMind
•
Official Repo:
github.com/google-deepmind/gemma
🚀 Gemma 3 27B Available for On-Demand Deployment on Fireworks →
Google Gemma 3 is a family of lightweight models ranging from 270M to 27B parameters, built from the same research powering Gemini 2.0. Unlike every other model in this roundup, Gemma 3 is a dense transformer (not MoE). It uses a 5:1 interleaved local/global attention pattern with RoPE rescaling and a SigLIP vision encoder. The 27B model runs on a single consumer GPU.
The trade-off is clear: Gemma 3 sacrifices raw parameter count for deployment flexibility. The 4B model handles vision tasks on laptops. The 27B variant hits 95.9% on GSM8K and 87.8% on HumanEval, punching well above its size class. But community users consistently flag weak factual accuracy. On SimpleQA, the 27B model scores just 10.0 , inventing answers rather than admitting it doesn't know.
Who should use Google Gemma 3?
Developers who need multimodal inference on consumer hardware with zero cloud dependency. The 4B model processes images on a laptop. The 27B model fits on a 24GB RTX 3090 using official QAT quantization with minimal quality loss.
Privacy-focused teams running local agentic workflows through tools like RA.Aid. Offline product analysis pipelines that process user feedback and sentiment via Docker. Edge deployment scenarios where sending data to a cloud API is not an option.
Standout features
•
Runs on a single consumer GPU
: the 27B model fits on 24GB VRAM with official QAT quantization
•
Native vision from 4B+
: multimodal capabilities on hardware where larger models cannot run
•
128K context window
, a massive jump from Gemma 2's 8K limit
•
95.9% on GSM8K
and
87.8% on HumanEval
at just 27B parameters
•
35+ languages
supported out of the box, pre-trained on 140+ languages
•
Chatbot Arena ELO of 1338
, placing in the top 10 at time of release
Pros and cons
Pros
Cons
27B model runs on a single 24GB consumer GPU
SimpleQA score of 10.0 reflects frequent factual hallucinations
Native vision starting at 4B parameters for edge deployment
Invents answers instead of refusing when it lacks knowledge
95.9% GSM8K and 87.8% HumanEval at 27B parameters
Base (pre-trained) models feel noticeably weaker than instruction-tuned variants
Official QAT models with minimal quality degradation
Non-English performance is inconsistent despite claims of 140+ language support
FAQ
Q: How does Gemma 3 compare to Llama for general knowledge?
Gemma 3 beats Llama 3.2 on math (GSM8K) and coding (HumanEval) at equivalent sizes. Llama 3.1 8B retains a clear lead on knowledge retrieval and factual accuracy. If your workload is fact-heavy, Llama is the better choice.
Q: Should I use the QAT or standard model?
Use the official QAT models. They preserve nearly all quality while fitting the 27B variant on consumer GPUs. Community users report no perceptible difference for most tasks.
Q: Is Gemma 3 good for coding agents?
Yes, with caveats. It follows system prompts strictly and handles function calling via markdown code blocks. It integrates with agentic frameworks like RA.Aid, executing multi-step tasks with proper tool invocation. Avoid tasks requiring strong factual recall or knowledge-intensive reasoning.
Q: What's the best size variant for my use case?
The 4B handles basic vision and lightweight tasks on laptops. The 12B is a solid mid-range option. The 27B delivers the best quality and runs on a single high-end consumer GPU. Skip the 270M and 1B for anything beyond simple text classification.
See
Gemma 3 API
details on Fireworks.
🚀 Gemma 3 27B Available for On-Demand Deployment on Fireworks →
MiniMax-M2.5
What is MiniMax-M2.5?
•
Release Date:
February 12, 2026
•
Parameters:
229B total (10B active per token)
•
Context Window:
196,608 tokens (~200K)
•
License:
Modified MIT (MiniMax-Open)
•
GitHub Stars:
~386
•
Corporate Sponsor:
MiniMax AI
•
Official Repo:
github.com/MiniMax-AI/MiniMax-M2.5
🚀 Try MiniMax-M2.5 in the Fireworks Playground →
MiniMax-M2.5 is an agent-native MoE model trained with reinforcement learning across hundreds of thousands of complex real-world environments. Its 10B active parameters per token make it the most efficient model in this roundup by activation ratio. The model comes in standard and "Lightning" API variants, with the Lightning version optimized for throughput.
The model's signature behavior is "spec-first" architecture planning. Before writing code, it proactively decomposes features, plans directory structures, and outlines UI designs. On SWE-Bench Verified, it scores 80.2%, matching Claude Opus 4.6 while completing tasks in 22.8 minutes (compared to Opus's 22.9). Community users report it generates 4,000+ lines of correct code in a single pass where GLM-5 and Kimi K2.5 fail.
Who should use MiniMax-M2.5?
Developers who need a brute-force code executor. The model excels when handed well-defined specifications and asked to produce large codebases. Use another model (Kimi K2.5 or DeepSeek) for ideation, then pass the plan to M2.5 for implementation.
Teams running budget-conscious coding pipelines benefit from the pricing: $1/hour for 100 tokens/second on the official API, roughly 1/10th to 1/20th the cost of Claude Opus. Local deployment via Unsloth 3-bit GGUF runs on a 128GB Mac Studio at 20+ tokens/second.
Standout features
•
80.2% on SWE-Bench Verified
, reaching Claude Opus 4.6 levels at a fraction of the cost
•
Only 10B active parameters
per token, the most efficient activation ratio in this roundup
•
Spec-first code generation
: decomposes features and plans architecture before writing code
•
$1/hour for 100 TPS
on the official API
•
BFCL score of 76.8%
, beating Claude Opus 4.5's 68.0% on function calling
•
Unsloth 3-bit GGUF
shrinks the model to ~101GB for local deployment
Pros and cons
Pros
Cons
80.2% SWE-Bench at 1/10th the cost of Claude Opus
Hallucinates on vague prompts without strict context and documentation
10B active parameters make it the most efficient model here
API compatibility issues with some existing coding agents (Continue.dev, OpenCode)
Generates complete applications with spec, wireframes, and code
Long-context performance degrades faster than competitors
Runs locally on 128GB Mac Studio via 3-bit quantization
Verbose output (56M tokens on Artificial Analysis Intelligence Index vs 15M average)
FAQ
Q: Is MiniMax-M2.5 a good general-purpose model?
No. It shines in structured coding and productivity workflows with clear context and goals. For open-ended conversation or knowledge retrieval without strict prompting, it hallucinates more than GLM-5 or DeepSeek v3.2.
Q: How should I use it in a multi-model pipeline?
Use a stronger reasoning model (Kimi K2.5, DeepSeek) to figure out the logic and architecture. Then hand the spec to M2.5 for bulk code generation. Users report this "architect/executor" split produces the best results.
Q: What's the recommended sampling configuration?
MiniMax recommends
temperature=1.0
,
top_p=0.95
, and
top_k=40
for optimal reasoning performance. Always encourage the model to write a specification document first; forcing it to skip to code degrades output quality.
Q: Can I run it on Fireworks?
Yes. MiniMax-M2.5 is available on Fireworks for serverless inference. You can also access it via the official MiniMax API or run it locally using Unsloth GGUF quantizations.
See
MiniMax-M2.5 API
details on Fireworks.
🚀 Try MiniMax-M2.5 in the Fireworks Playground →
Why run these models on Fireworks
Fireworks AI is an inference platform built for serving open source models at production scale. All seven models in this roundup are available on Fireworks for immediate use.
Performance at scale
The platform delivers 3-12x lower latency and 6-40x higher throughput compared to vLLM. It processes over 300 billion tokens per day across 100+ hosted models. Cursor, one of Fireworks' customers, achieved 2x faster inference than GPT-4 with 30% fewer code errors and 1,000 tokens/second throughput using Fireworks' Speculative Decoding API.
Deployment options
Option
How it works
Best for
Serverless
Pay per token, no cold boots, 1 line of code
Prototyping and variable workloads
On-Demand
Private GPUs, ~250% better throughput vs vLLM, auto-scaling
Production workloads with predictable traffic
Enterprise Reserved
Dedicated GPUs, SLAs, priority support, bring-your-own-cloud
High-volume production with compliance requirements
Why it matters for these models
Running trillion-parameter MoE models like Kimi K2 or DeepSeek v3.2 locally requires 240GB+ of RAM/VRAM. Fireworks handles the infrastructure: handwritten CUDA kernels, distributed inference, semantic caching, and fine-grained quantization. New models get support immediately, not weeks after release.
The OpenAI-compatible API means switching from GPT-4 to DeepSeek v3.2 or Kimi K2 Thinking requires changing one line of code. Notion used Fireworks to reduce latency from 2 seconds to 350 milliseconds with a fine-tuned 8B model. Vercel improved code compilation rates from 62% to "way into the 90s" using reinforcement learning fine-tuning on the platform.
New users get $1 in free credits for serverless inference. No setup, no cold starts.
Talk to an expert
|
See Fireworks Plans
The information provided in this article is accurate at the time of publication. Model capabilities, benchmarks, and availability are subject to change. Always verify current specifications on official model repositories.
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
