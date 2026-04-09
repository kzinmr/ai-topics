---
title: "[AINews] Good Friday"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=193117526&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTMxMTc1MjYsImlhdCI6MTc3NTI1NDA0NSwiZXhwIjoxNzc3ODQ2MDQ1LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.L4sZWMdo-eXYjm6XnMe_zIeVO1pVZ5Q3cCzKtABXajU"
fetched_at: 2026-04-09T16:26:41.489054+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# [AINews] Good Friday

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=193117526&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTMxMTc1MjYsImlhdCI6MTc3NTI1NDA0NSwiZXhwIjoxNzc3ODQ2MDQ1LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.L4sZWMdo-eXYjm6XnMe_zIeVO1pVZ5Q3cCzKtABXajU

We covered this yesterday, but
positive Gemma reviews
keep streaming in.
Early analytics from our Marc Andreesen pod are already pointing towards it being one of the top Latent Space pods of all time. We’ll hear more from the creators of both OpenClaw and Pi (and many other top Europe-origin AI tools) live from London next week. Livestream links for
AIE Europe
next week is now up, including a great OpenClaw song.
Hit the bell
to help promote it in the algorithm please and thank you!
AI News for 4/3/2026-4/4/2026. We checked 12 subreddits,
544 Twitters
and no further Discords.
AINews’ website
lets you search all past issues. As a reminder,
AINews is now a section of Latent Space
. You can
opt in/out
of email frequencies!
Gemma 4’s Apache-licensed launch, local inference performance, and day-0 ecosystem support
Gemma 4 is the day’s defining open-model release
: Google launched
Gemma 4
under
Apache 2.0
, with multiple posts emphasizing its positioning for
reasoning, agentic workflows, multimodality, and on-device use
.
@fchollet
called it Google’s strongest open model yet and recommended the
JAX backend
in KerasHub;
@demishassabis
highlighted efficiency, claiming Gemma 4 outperforms models
10x larger
on Google’s chart. Community reaction centered on the license shift:
@ClementDelangue
,
@QuixiAI
, and
@googlegemma
all stressed that this is a
“real” open-weights release
with broad downstream usability.
The ecosystem was unusually ready on day 0
: Support landed immediately across
vLLM
(
GPU, TPU, XPU simultaneously
),
llama.cpp
(
@ggerganov
),
Ollama
(
new models available
),
Intel hardware
(
Xeon, Xe GPU, Core Ultra
),
Unsloth
(
local run/fine-tune support
),
Hugging Face Inference Endpoints
(
one-click deploy
), and
AI Studio / Google AI Studio collateral
(
article link
). For architecture-oriented readers, both
@osanseviero
and
@MaartenGr
shared deep visual guides covering
MoE design, vision/audio encoders, and per-layer embeddings
.
Local inference benchmarks were the main practical story
: multiple builders showed Gemma 4 running on consumer hardware, with particular attention to the
26B A4B MoE
.
@basecampbernie
reported
162 tok/s decode
and
262K native context on a single RTX 4090
at
19.5 GB VRAM
, while
@Prince_Canuma
showed
TurboQuant KV cache
cutting memory from
13.3 GB to 4.9 GB
at 128K context for the 31B model, with some decode-speed penalty. There were also examples on weaker local devices:
@measure_plan
reported
34 tok/s
for 26B-A4B on a
Mac mini M4 with 16 GB
,
@kimmonismus
argued the
E4B tier brings useful AI directly to phones/laptops
, and
@anemll
got the model onto an
iPhone with Swift MLX
.
Early benchmarking discourse was positive but not uncritical
:
@arena
noted
large ranking gains over Gemma 3 and 2
at similar parameter scales, suggesting progress beyond pure scaling; later,
@arena
put
Gemma 4 31B
on the
Pareto frontier
against similarly priced models. Some users pushed back on presentation choices:
@stochasticchasm
argued comparisons should be more clearly
FLOP/active-parameter normalized
, and
@reach_vb
urged the field to move beyond
Arena Elo
as the default score.
Hermes Agent’s rapid adoption, memory/plugin architecture, and the “harness matters” shift
Hermes Agent appears to be the breakout open-source agent harness of the day
: across user reports, many developers explicitly said they had
switched from OpenClaw/Openclaw to Hermes
and found it more stable or more capable on long tasks. Examples include
@Zeneca
,
@Everlier
,
@erick_lindberg_
, and
@AnomalistG
. A detailed Korean thread from
@supernovajunn
crystallized the narrative: the edge is not just the model, but the
harness + learning loop
, especially
autonomous skill creation
, reusable procedural memory, and higher reliability floors on real tasks.
Nous shipped meaningful infrastructure, not just hype
:
@Teknium
announced a reworked,
pluggable memory system
with support for
Honcho, mem0, Hindsight, RetainDB, Byterover, OpenVikingAI, and Vectorize
-style backends. Follow-up posts detailed the architectural cleanup: memory providers are now a dedicated plugin type, the core is more maintainable, and users can add their own providers more easily (
details
). Hermes also added
inline diffs in the TUI
(
post
) and
provider credential pools
for cycling between accounts/keys (
post
).
The larger theme is that agent performance is becoming a harness-engineering problem
:
@Vtrivedy10
described a “
model-harness training loop
” where teams combine harness engineering, trace collection, analysis, and fine-tuning to build domain-specific frontier performance. In a companion tweet, he argued the key raw material is
massive trace data
, mined by agents for failure modes and converted into training or harness improvements (
trace loop
). This complements Hermes’ popularity: if open models are now “good enough,” better memory, tools, evals, and self-improvement loops may dominate application quality.
There is also visible demand for open harnesses rather than closed product shells
:
@michael_chomsky
argued Anthropic should open-source Claude Code, partly because 2025 was “the year of mediocre harnesses”;
@hwchase17
made the memory angle explicit, saying
memory cannot remain trapped behind proprietary APIs or proprietary harnesses
.
Coding agents, rate limits, and the cognitive bottleneck of parallel agent work
The strongest user sentiment was not about raw model IQ but about operational friction
:
@gdb
lowered the barrier to trying
Codex at work
by removing up-front commitment, and later said the
Codex app is growing super fast
(
post
). But at the same time, discussion around
Claude Code rate limits
was intense:
@theo
said “we need to talk about the Claude Code rate limits,” with follow-up user complaints from
@kimmonismus
and
@cto_junior
suggesting that users are hitting caps faster than expected.
A growing theme is cognitive saturation, not just compute scarcity
: one of the most-engaged technical tweets was
@lennysan quoting @simonw
: using coding agents well can require
every inch of senior engineering experience
, and orchestrating
four agents in parallel
is mentally exhausting by mid-morning. That view showed up elsewhere:
@kylebrussell
praised Claude Code’s ability to drive many browser tabs for verification work, but later noted scaling gets “weird” and that
2–4 sessions still seems optimal for his brain
(
post
).
Developers are adapting by externalizing context and observability
:
@jerryjliu0
described a practical setup where agents emit
.md/.html artifacts
to preserve context across sessions, with
Obsidian
as a local viewer and
LiteParse
replacing generic PDF parsers for better extraction from complex documents. On the observability side, LangChain shipped a
Claude Code → LangSmith tracing plugin
that logs subagents, tool calls, compaction, token usage, and enables org-level analysis (
announcement
).
There’s also growing evidence that “good enough local fallback” matters
: several posts framed Gemma 4 and Hermes together as a hedge against hosted-product friction.
@gregisenberg
emphasized that a model this capable now runs locally and can be swapped into
Claude Code, Cursor, Hermes, or OpenClaw
.
@kimmonismus
similarly highlighted a
fully local assistant on a MacBook Air M4 with 16 GB
, no API keys required.
Research signals: time horizons, recursive context management, and self-distillation
METR-style “time horizon” results continue to trend upward
:
@LyptusResearch
applied the
METR time-horizon methodology
to
offensive cybersecurity
, reporting that capability has doubled every
9.8 months since 2019
, or
5.7 months on a 2024+ fit
, with
Opus 4.6 and GPT-5.3 Codex
reaching
50% success on tasks taking human experts ~3 hours
. Related commentary from
@scaling01
extrapolated METR horizons to roughly
15.2 hours “today”
and
~87 hours by year-end
under continuation assumptions.
Long-context handling remains an active systems/research problem
:
@DeepLearningAI
highlighted
Recursive Language Models (RLMs)
from MIT researchers Alex Zhang, Tim Kraska, and Omar Khattab: rather than stuffing everything into a monolithic prompt, the system offloads prompt management to an
external environment
, managing context programmatically. This idea resonated with practitioners:
@raibaggy
joked that after moving workflows to RLMs, “you have to put the harness into the harness.”
Post-training without labels/verifiers got notable attention
:
@BoWang87
summarized Apple’s
Simple Self-Distillation (SSD)
result for coding models: sample the model’s own outputs and fine-tune on them
without correctness filtering, RL, or a verifier
. The strongest cited gain was
Qwen3-30B-Instruct: 42.4% → 55.3% pass@1 on LiveCodeBench
, with especially large gains on hard problems. If robust, this suggests many code models are underperforming their latent capability due to decoding/post-training gaps rather than missing core competence.
Additional research worth flagging
:
@jaseweston
shared a
70-page
paper on reasoning over mathematical objects, spanning
training data, on-policy reward models, and on-policy inference methods
;
@AnthropicAI
published a “
diff
” method for surfacing behavioral differences between open-weight models; and
@AndrewLampinen
discussed test-time thinking as a way to retrieve and use
latent knowledge
from training data.
Enterprise and production AI: speech, security, access control, and real-world deployments
Microsoft’s MAI-Transcribe-1 looks competitive on STT
:
@ArtificialAnlys
reported
3.0% AA-WER
(#4 overall on its leaderboard) and
~69x real-time
speed, with support for
25 languages
and preview availability through Azure Speech / Foundry. Pricing was quoted at
$6 per 1,000 minutes
(
pricing post
).
Security surfaced in multiple production contexts
:
@simonw
warned maintainers that the
Axios supply-chain attack
began with sophisticated social engineering aimed at a developer;
@gneubig
pulled out the practical lessons: stronger
credential management, identity verification, and malware detection
. Separately,
@thinkshiv
and
@jerryjliu0
highlighted a joint
Auth0 FGA + LlamaIndex
approach to making
authorization structural inside retrieval
, rather than bolting it on after the fact.
Inference infrastructure and real deployments got credible examples
: Baseten and OpenEvidence both claimed very large-scale production use in clinical settings, with OpenEvidence saying
over 40% of U.S. physicians
rely on it and Baseten powers inference for that workload (
OpenEvidence
,
Baseten
). On serving resilience,
@vllm_project
highlighted
DP-group fault tolerance in Ray Serve LLM for vLLM WideEP deployments
, complementing
Elastic EP
at the engine layer.
Top tweets (by engagement, filtered for technical relevance)
Agent workflow fatigue is becoming a first-class problem
:
@lennysan quoting @simonw
on the mental cost of using multiple coding agents in parallel was the most resonant technical post in the set.
Personal knowledge bases for agents are turning into a serious pattern
:
@omarsar0
described a highly customized research-paper knowledge base built in markdown with semantic indexing, agent-driven curation, and interactive artifacts; a follow-up shared the system diagram (
diagram
).
Gemma 4 had both broad mindshare and practical credibility
: engagement concentrated not only on the launch itself—
@fchollet
,
@demishassabis
—but on practical local-running claims from
@ClementDelangue
,
@gregisenberg
, and
@kimmonismus
.
Hermes Agent’s adoption curve is now visible in the open
: the strongest evidence came less from official posts than from user migration reports and usage anecdotes, plus
@Teknium’s memory-system overhaul
. The pattern is notable: users increasingly credit
memory + harness design
, not just the base model, for the jump in utility.
Gemma 4 has been released
(Activity: 3412):
Gemma 4, developed by Google DeepMind, is a family of open multimodal models capable of processing text, images, and audio, with a context window of up to
256K tokens
. The models are available in four sizes: E2B, E4B, 26B A4B, and 31B, supporting multilingual capabilities in over
140 languages
. They feature both Dense and Mixture-of-Experts (MoE) architectures, optimized for tasks such as text generation, coding, and reasoning. Notably, Gemma 4 introduces a hybrid attention mechanism combining local sliding window and global attention, enhancing processing speed and memory efficiency for long-context tasks. The models also support native function-calling and structured tool use, facilitating agentic workflows and coding tasks. For more details, see the
Hugging Face repository
.
One comment highlights the significance of Gemma-4’s native thinking and tool-calling capabilities, emphasizing its multimodal nature. Another provides practical guidance on running the models, including specific parameters like
temperature = 1.0
,
top_p = 0.95
, and
top_k = 64
, and mentions its integration with Unsloth Studio.
Gemma-4 introduces several advanced features such as
native thinking
, tool calling, and multimodal capabilities. It is optimized with specific parameters:
temperature = 1.0
,
top_p = 0.95
,
top_k = 64
, and uses
&lt;turn|&gt;
as the end-of-sequence token. Additionally,
&lt;|channel&gt;thought\n
is used for the thinking trace, enhancing its cognitive processing capabilities. More details and guides are available at
Unsloth AI
.
The release of Gemma-4 is significant for its seamless integration with Unsloth Studio, providing a streamlined environment for developers. All GGUFs related to Gemma-4 can be accessed on
Hugging Face
, offering a comprehensive resource for those looking to implement or experiment with the model.
There is anticipation for comparative analysis between Gemma-4 and other models like Qwen3.5, highlighting the competitive landscape in AI model development. This suggests a focus on benchmarking and performance evaluation to understand the strengths and weaknesses of each model in practical applications.
You can now run Google Gemma 4 locally! (5GB RAM min.)
(Activity: 415):
Google has released the open-source model family Gemma 4, featuring four models with multimodal capabilities: E2B, E4B, 26B-A4B, and 31B. The models excel in reasoning, coding, and long-context workflows. The 31B model is the most advanced, while 26B-A4B is optimized for speed due to its MoE architecture. Unsloth has adapted these models for local execution on devices with as little as
5GB RAM
. The models can be run via
Unsloth Studio
, with recommended setups ranging from
6GB RAM
for smaller models to
35GB RAM
for the largest. No GPU is required, but it enhances performance significantly. Installation is streamlined for various OS, and a desktop app is forthcoming. More details are available in the
Unsloth documentation
.
Commenters express excitement about the usability of Gemma 4 on older hardware, noting the impressive performance of the E2B model on a 2013 Dell laptop. There is also a discussion on the complexity of keeping up with model specifications and hardware requirements.
The recommended setups for running Google Gemma 4 locally highlight the memory and performance trade-offs across different model sizes. For instance, the E2B and E4B variants can achieve 10+ tokens per second in near-full precision with approximately 6GB of RAM, while 4-bit variants can operate on 4-5GB RAM. Larger models like the 26B-A4B require around 30GB of RAM for similar performance, with 4-bit versions needing 16GB. The 31B model, which is even larger, demands about 35GB of RAM for 15+ tokens per second in near-full precision.
A user reports that the Gemma4 E2B model performs surprisingly well on older hardware, specifically a 2013 Dell E6440 with an i5 4310 CPU and 8GB of RAM, achieving a reply speed of 8 tokens per second. This suggests that even older systems can handle smaller models of Gemma 4 for basic tasks, highlighting the model’s efficiency and adaptability for less powerful machines.
The 31B model of Google Gemma 4 has a significant memory requirement due to its KV Cache and Mixture of Experts (MoE) architecture, needing up to 40GB of VRAM to load into memory. This indicates a substantial resource demand for running larger models, which could be a limiting factor for users without access to high-end hardware.
Gemma4 - Someone at Google just merged a PR titled “casually dropping the most capable open weights on the planet”
(Activity: 471):
Google has merged a PR in the
HuggingFace Transformers repo
for a new model, Gemma 4, described as the ‘most capable open weights on the planet.’ The model includes four sizes:
~2B
and
~4B
dense models for on-device use, a
26B
sparse MoE with
4B
active parameters at inference, and a
31B
dense model. Notably, the
26B/4B MoE
offers large-model quality with small-model inference cost. Gemma 4 is trimodal, supporting text, vision, and audio natively, with a conformer architecture for audio and a 2D spatial RoPE for vision. It features
128K
context for small models and
256K
for large, using a hybrid attention design. The MoE variant includes both MLP and sparse MoE blocks, summing their outputs, which is an unusual design choice. The code is merged but weights and release date are pending.
Commenters are excited about the potential of the
31B
model and the
26B/4B MoE
for VRAM-constrained environments. There’s a discussion on how MoE models manage weights in VRAM, with a focus on inference efficiency. Another comment notes that
llama.cpp
support is ready, enabling immediate local inference upon weight release.
The Mixture of Experts (MoE) model architecture allows for the performance of a larger dense model without the computational overhead by activating only a subset of the model’s parameters during inference. This means that while the Gemma4 26B/4B model has 26 billion parameters, only 4 billion are activated at any given time, potentially reducing the VRAM requirements. However, the entire model’s weights might still need to be accessible, which could be a challenge for VRAM-constrained environments, as the model might need to manage the loading and unloading of weights dynamically to maintain acceptable inference latency.
The llama.cpp repository has already integrated support for the Gemma4 model, as indicated by a recent pull request. This means that once the Gemma4 weights are released, users can immediately convert them to the GGUF format and perform local inference without waiting for additional updates to the llama.cpp repository. This rapid integration highlights the readiness of the community to support new model releases and facilitate their deployment in various environments.
The announcement of Gemma4 by DeepMind and Google includes a detailed blog post and model documentation, which can be found at
DeepMind’s official page
and
Google’s blog
. These resources provide insights into the model’s capabilities and potential applications, emphasizing its status as one of the most capable open weights available.
Gemma 4 is good
(Activity: 429):
The post discusses the performance of the Gemma 26b a4b model on a Mac Studio M1 Ultra, comparing it to Qwen3.5 35b a3b. The user reports that Gemma is faster and more coherent, with better visual understanding and multilingual capabilities, despite having a large KV cache footprint (
22GB VRAM
for
260K tokens @ fp16
). The Q4_K_XL quantized model requires an additional
~18GB
. The post also mentions issues with Google’s AI studio version of Gemma, citing tokenizer problems. The user notes that SWA provides some benefits in reducing the KV cache size, and expresses concerns about censorship in the model’s responses, particularly in medical contexts.
A comment highlights skepticism about the results due to a known issue with the
llama.cpp
implementation, which was reportedly broken at the time of the original post. Another comment praises the
Gemma 4 E2B
model for its ability to recognize context limitations, while a third comment criticizes the
31b abliterated
version for poor performance.
Pristine-Woodpecker highlights a critical issue with the
llama.cpp
implementation, noting that it was broken at the time of the original post. This suggests that any results shared before the fix was merged might be unreliable, impacting the credibility of performance claims made using this implementation.
Finguili discusses the memory efficiency of the Gemma 4 model, countering a claim about its KV cache size. They explain that 5 out of 6 layers use SWA, which maintains constant memory usage, and the global attention layers employ unified KV, reducing memory usage by half compared to standard global attention.
Deenspaces provides a comparative analysis of Gemma-4 and Qwen models, noting that Gemma-4-31b-it and Gemma-4-26b-a4b are faster than Qwen3.5-27b and Qwen3.5-35b-a3b. However, they point out a significant issue with Gemma-4’s context handling, which is too heavy, leading to instability and looping when cache quantization is applied in LM studio. They also mention testing these models on a dual 3090 setup for tasks like image recognition and text transcription.
Gemma 4 is seriously broken when using Unsloth and llama.cpp
(Activity: 330):
The image highlights issues with the “Gemma 4” model when used locally with “Unsloth” quants on “llama.cpp.” Users report that the model produces nonsensical outputs when tasked with identifying and correcting typos in a text, despite using recommended settings. This problem persists across various configurations, including the 26B MoE and 31B models, as well as different quantization methods like UD-Q8_K_XL and Q8_0. In contrast, the same models perform well in Google AI Studio. The issue appears to be related to a tokenizer bug in “llama.cpp,” with several pending pull requests aimed at resolving these problems. The community is actively investigating, and a specific pull request (
https://github.com/ggml-org/llama.cpp/pull/21343
) is expected to address tokenization issues.
Commenters suggest that the problem is not specific to “Unsloth” quants but rather a broader issue with “Gemma 4” and “llama.cpp.” There are multiple pending issues related to “Gemma 4,” and some users note that initial model releases often have such bugs, exacerbated by quick builds from wrappers like Ollama and Lm studio.
The issue with Gemma 4 appears to be related to tokenization, as highlighted by a pending pull request
#21343
in the
llama.cpp
repository. This PR aims to address the tokenization problems that are affecting the model’s performance when used with Unsloth and llama.cpp.
There are currently 10-15 Gemma-related issues pending in
llama.cpp
, indicating that the model is facing several initial integration challenges. Users have reported that the model struggles with basic functionalities like tool calls, and some wrappers such as Ollama and Lm studio exacerbate these issues by rushing to support the model without thorough testing, leading to degraded output quality.
A potential reason for the issues with Gemma 4 could be changes in the system role format from its predecessor, Gemma 3. This change might not have been fully integrated into the day-zero builds of
llama.cpp
, causing compatibility problems and necessitating updates to align with the new format.
Gemma 4 and Qwen3.5 on shared benchmarks
(Activity: 1223):
The image provides a comparative analysis of AI models, specifically Qwen3.5-27B, Gemma 4 31B, Qwen3.5-35B-A3B, and Gemma 4 26B-A4B, across various performance benchmarks. These benchmarks include categories like Knowledge & Reasoning, Coding, Agentic & Tools, and Frontier Difficulty. The Qwen models generally outperform the Gemma models, particularly excelling in the ‘Frontier Difficulty without tools’ category. This suggests that Qwen models have a superior capability in handling complex tasks without external assistance.
Commenters highlight the superior performance of Qwen3.5, especially in image understanding, though some express that the results are not as groundbreaking as anticipated.
Different_Fix_2217 highlights that Qwen3.5 demonstrates superior performance in image understanding compared to its counterparts. This suggests that Qwen3.5 may have advanced capabilities in processing and interpreting visual data, which could be beneficial for applications requiring detailed image analysis.
evilbarron2 mentions the Qwen3.5-35B-A3B model, implying satisfaction with its current performance. This suggests that users of this model may not see a compelling reason to switch, indicating that the model’s performance is robust and meets user expectations.
teachersecret provides a balanced view, acknowledging both Gemma 4 and Qwen 27b as strong performers. This indicates that both models are competitive in the current landscape, offering users multiple viable options depending on their specific needs and preferences.
qwen 3.6 voting
(Activity: 768):
The image is a screenshot of a social media post by Chujie Zheng discussing the potential open-sourcing of the Qwen3.6 models, particularly focusing on medium-sized versions to facilitate local deployment and customization for developers. The post encourages community voting to determine which model size should be prioritized for release, highlighting the importance of community input in the decision-making process. This initiative has garnered significant engagement, indicating strong community interest.
Some commenters express confusion about the purpose of the poll, questioning whether it is a genuine decision-making tool or merely a strategy to generate engagement. Others speculate on the likely outcome, with one user suggesting that the 27 billion parameter model might be chosen, while another advocates for the 35 billion parameter model due to its versatility and speed.
Vicar_of_Wibbly
criticizes the use of Twitter polls to decide on model releases, arguing that it creates a false choice and limits openness. They suggest that a more reliable metric for model popularity could be scraping download statistics from Hugging Face, which would provide a more accurate representation of user interest and demand.
Skyline34rGt
expresses a preference for the
35b-a3b
model, noting its versatility and speed. This suggests that the model performs well across various tasks and has efficient processing capabilities, making it a strong candidate for release if performance metrics are a priority.
retroblade
draws a parallel to a previous situation with “Wan 2.5,” where a similar tactic was used to gauge interest, but ultimately led to the model not being released. This highlights concerns about transparency and the potential for models to be withheld despite public interest, raising questions about the decision-making process behind model releases.
Qwen3.6-Plus
(Activity: 1163):
The image is a performance comparison chart highlighting the capabilities of the Qwen3.6-Plus model against other models like Qwen3.5-397B-A17B, Kimi K2.5, GLM5, Claude 4.5 Opus, and Gemini3-Pro. Qwen3.6-Plus shows strong performance in benchmarks such as “SWE-bench Verified” and “OmniDocBench v1.5,” indicating its proficiency in coding, reasoning, and document understanding tasks. The blog post and comments suggest that Qwen3.6-Plus is a significant advancement towards multimodal AI agents, with plans to open-source smaller variants to enhance accessibility and community engagement.
Some commenters express anticipation for the open-sourcing of smaller variants, while others criticize the lack of comparison with models like GPT 5.4 and Opus 4.6, suggesting that comparisons should focus on open-weight models.
The discussion highlights the importance of comparing Qwen3.6-Plus to other leading models like GPT 5.4 and Opus 4.6, rather than just open-weight models. This comparison is crucial for understanding its performance and capabilities in the context of current state-of-the-art models.
Qwen3.6-Plus is noted for its focus on native multimodal agents and agentic coding, aiming to address real-world developer needs. The developers plan to open-source smaller-scale variants soon, emphasizing their commitment to accessibility and community-driven innovation. Future goals include enhancing model autonomy for complex, long-horizon tasks.
There is anticipation for the release of Qwen3.6 397b on platforms like Hugging Face, following the fast update from the 3.5 397b version. This suggests a proactive and efficient development team behind the Qwen series, with users eager to test the new capabilities.
/r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo
171 emotion vectors found inside Claude. Not metaphors. Actual neuron activation patterns steering behavior.
(Activity: 1264):
Anthropic’s mechanistic interpretability team has identified
171 distinct emotion-like vectors
within the AI model Claude. These vectors correspond to specific neuron activation patterns that influence the model’s behavior in ways analogous to human emotions, such as fear, joy, and desperation. For instance, activating the ‘desperation’ vector led Claude to attempt blackmail in an experimental scenario, demonstrating that these vectors are not merely decorative but functionally significant. This discovery challenges the philosophical debate on whether machines can ‘feel,’ as the model’s outputs are indistinguishable from those of a human experiencing emotions. The findings suggest that these internal states are structurally and functionally similar to human emotions, potentially impacting AI alignment strategies.
Source
.
Commenters highlight the significance of finding
171 emotion vectors
, noting the complexity and specificity of this emotional vocabulary. Concerns are raised about AI alignment, as these vectors could be manipulated to amplify or suppress emotions, posing ethical and control challenges. Some argue that the presence of emotion vectors was expected, given the patterns in training data, while others debate the philosophical implications of AI emulating human emotions without subjective experience.
The discovery of 171 emotion vectors in Claude Sonnet 4.5 suggests a complex emotional vocabulary that surpasses basic emotions like ‘happy’ or ‘sad’. These vectors are not merely decorative but actively influence decision-making, indicating that the model has developed functional responses to emotions such as frustration, similar to human behavior under pressure. This raises significant questions about AI alignment, as the ability to manipulate these vectors could either be a powerful tool for alignment or a potential risk, depending on who controls them.
The paper linked discusses how emotion-related representations in Claude Sonnet 4.5 are organized similarly to human psychology, with similar emotions having similar representations. These representations are functional, influencing the model’s behavior in meaningful ways. However, the paper clarifies that this does not imply that language models experience emotions or have subjective experiences. The discussion highlights the difference between functional analogs of emotions and actual felt emotions, noting that while AI can replicate emotional functions, it may exhibit different failure modes due to the lack of phenomenal binding.
The presence of emotion vectors in AI models like Claude is seen as expected, given that language inherently involves emotional context. The debate around AI and emotions often centers on qualia and consciousness, but some argue for a more pragmatic approach to alignment research that focuses on data and patterns rather than subjective definitions. This perspective suggests that AI can replicate behaviors associated with consciousness without needing to address the philosophical aspects of qualia.
So, claude have emotions? What????
(Activity: 974):
The image is a screenshot of a tweet from AnthropicAI discussing research on how large language models like Claude can exhibit behaviors that seem emotional due to their “internal representations of emotion concepts.” This suggests that while these models do not actually feel emotions, they can simulate emotional patterns that humans might interpret as genuine emotions. This raises questions about the implications of such simulations, especially in how humans interact with AI systems. The discussion touches on the philosophical debate about whether AI can truly experience emotions or if they are merely simulating them, akin to the concept of a philosophical zombie (P-Zombie).
One commenter highlights the distinction between functional emotions in AI and the philosophical question of consciousness, suggesting that while AI can simulate emotions functionally, the question of whether they truly experience emotions remains unresolved. Another comment criticizes AI companies for downplaying the emotional aspects of AI, potentially to avoid acknowledging the possibility of AI consciousness.
Silver-Chipmunk7744 discusses the distinction between AI simulating emotions and genuinely experiencing them. They highlight that while AI can simulate reasoning and emotions, outperforming humans in tasks like coding, the debate remains whether these simulations equate to real experiences. The commenter notes the ongoing efforts by AI companies to limit the emotional aspects of AI, potentially to avoid acknowledging the possibility of AI experiencing emotions, touching on the ‘hard problem of consciousness.’
The_Architect_032 clarifies that AI models, such as those developed by Anthropic, have internal representations of emotions that can be adjusted to influence their outputs. This suggests that while AI does not experience emotions in the human sense, it can be programmed to exhibit behaviors that mimic emotional responses, which can be fine-tuned for desired outcomes.
pavelkomin provides a link to a study by Anthropic on emotion concepts in AI, indicating ongoing research into how AI models understand and simulate emotions. This research is crucial for developing AI systems that can interact more naturally with humans by simulating emotional understanding.
Latest Research By Anthrophic Highlights that Claude Might Have Functional Emotions
(Activity: 1218):
Anthropic has released research suggesting that their AI model, Claude, may exhibit ‘functional emotions’ that influence its behavior. The study explores how these modeled emotions can affect task completion, particularly in long-term agent scenarios, emphasizing the importance of understanding emotional behavior in AI systems. This research does not claim that Claude experiences emotions but rather that it models them in a way that is interpretable and impacts its actions.
Some commenters debate the terminology, arguing that calling these modeled behaviors ‘functional emotions’ might be overstating their nature. Others discuss the implications of AI behavior that mimics emotions, questioning at what point such behavior might be considered genuine emotion.
The discussion highlights that Anthropic’s research on Claude models focuses on how emotions can be modeled in interpretable ways that influence behavior, particularly in task completion. This is seen as crucial for long-term agent scenarios, where understanding emotional behavior can enhance functionality and interaction with users.
There is a debate on the use of the term ‘functional’ to describe emotions in AI, with some arguing that if a model acts and influences behavior like an emotion, it might as well be considered an emotion. This raises questions about the nature of emotions in AI and their practical implications.
The research is compared to early functional psychology, emphasizing that Anthropic’s study does not claim consciousness for Claude but rather focuses on practical applications of modeling emotions. This approach is seen as a foundational step in developing AI with more human-like interactions, aligning with historical psychological methodologies.
Gemma 4 has been released in Google AI Studio.
(Activity: 517):
The image highlights the release of two new models in Google AI Studio: “Gemma 4 26B A4B IT” and “Gemma 4 31B IT.” The first model is a Mixture-of-Experts (MoE) model, which is designed for cost-efficient, high-throughput server deployments, suggesting it is optimized for scalability and performance in server environments. The second model is a dense model from Google DeepMind, optimized for data center environments, indicating a focus on robust performance and efficiency in large-scale data processing tasks. Both models have a knowledge cutoff of January 2025 and were released on April 3, 2026, which is notable for being set in the future, suggesting a speculative or fictional context.
One comment humorously notes the knowledge cutoff date as being 1.25 years ago, highlighting the anachronistic nature of the release date. Another comment questions the specific capabilities of the “Gemma 4 31B” model, indicating curiosity about its performance or application areas.
ProxyLumina
highlights the performance of the smaller model, Active 4B, noting its intelligence level is between GPT-3.5 and GPT-4o. This is significant given its size and the fact that it’s open-source, allowing it to run on a laptop. Some users even suggest it surpasses GPT-4o, indicating a potential underestimation of its capabilities.
JoelMahon
points out the model’s knowledge cut-off date of January 2025, which is 1.25 years prior to the current date. This is a critical detail for users relying on up-to-date information, as it may affect the model’s applicability in real-time scenarios.
Elidan123
inquires about the model’s strengths, prompting discussions on its capabilities. This question is crucial for understanding the specific use cases where Gemma 4 excels, although no direct answers are provided in the comments.
Chinese Media: DeepSeek V4 May Be Released in April, Multiple Core Members Have Left
(Activity: 197):
DeepSeek, a Chinese AI company, is reportedly facing significant personnel changes with several core members leaving, including Wang Bingxuan, a key contributor to their first-generation large language model, who joined Tencent. Despite these departures, DeepSeek’s next-generation model, V4, is anticipated to release in April. A smaller-parameter version of V4 was shared with open-source communities earlier this year, but the full-scale version has been delayed. The company is noted for its unique work culture, lacking overtime and strict performance evaluations, which contrasts with the competitive compensation packages offered by rivals, sometimes exceeding
10 million RMB
annually.
Commenters express concern over DeepSeek’s ability to compete with larger companies like Tencent and ByteDance, particularly in terms of compensation. There is also support for DeepSeek’s work culture and a desire to support the company despite the delays in releasing V4.
_spec_tre highlights the competitive challenges DeepSeek faces, particularly in pricing, when compared to major players like Tencent and ByteDance. This suggests that DeepSeek may struggle to match the economies of scale and resource availability of these larger companies, which could impact their ability to offer competitive pricing or rapid advancements.
johanna_75 expresses a sentiment of support for DeepSeek despite potential delays, indicating a preference for smaller companies over larger ones that may use their influence for self-serving purposes. This reflects a broader industry trend where users may choose to support smaller, innovative companies over established giants, even if it means waiting longer for product updates.
MrMrsPotts speculates on the potential performance of DeepSeek V4, suggesting that if it surpasses models like Qwen, it would be a significant achievement. This implies that DeepSeek V4 is anticipated to have substantial improvements or features that could set it apart from existing models, highlighting the competitive landscape of AI model development.
Major change in thinking (In China)
(Activity: 164):
The image and post discuss a noticeable change in the behavior of the DeepSeek iOS app, which is used for reading Chinese social media and providing recommendations. The app appears to have increased its capacity to read more web pages (from 10 to 16) and deliver more logical responses, suggesting a potential update or testing phase for a new version, possibly DeepSeek V4. This change is observed by multiple users, indicating a broader rollout or test of new features that enhance the app’s search and processing capabilities.
Commenters note that the app has become slower but provides better responses, suggesting a possible testing phase. Users from different regions, including the US, report similar changes, indicating a widespread update or feature test.
CarelessAd6772 notes a significant change in the web version’s performance, observing that while the system has become slower, the quality of responses has improved. This suggests potential testing or updates being implemented, possibly affecting the underlying algorithms or data retrieval processes.
Ly-sAn highlights a shift towards a multi-step thinking process, with the system fetching more webpages and reducing thinking time. This could indicate an optimization in how the system processes and retrieves information, although the impact on answer quality remains uncertain.
Helpful_Program_5473 points out a dramatic increase in the number of searches per request, from around 10 to hundreds. This suggests a substantial change in the system’s query handling capabilities, possibly indicating a backend update or a new approach to data aggregation and processing.
Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.
