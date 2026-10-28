---
title: "Introducing LFM3: Every Modality for Specialized Intelligence"
url: "https://www.liquid.ai/blog/lfm3"
date: 2026-10-27
fetched_at: 2026-10-28
source: "liquid.ai"
type: raw-article
tags: [llm, edge-ai, on-device, multimodal, model]
---

# Introducing LFM3: Every Modality for Specialized Intelligence

Source: https://www.liquid.ai/blog/lfm3
Fetched: 2026-10-28 (active-crawl)

---

News

/

Models

Introducing LFM3: Every Modality for Specialized Intelligence

OCT 27, 2026

On this page

New architecture for more expressivity

A multimodal family for every need

Made for specialized intelligence

Get Started

Launch Partners

Citation

Today, we’re excited to announce 
LFM3
, our new generation of Liquid Foundation Models (LFMs) built for specialized intelligence. The LFM3 model family is multimodal by nature and brings text, vision, audio, omni, and decision models onto one new shared backbone. The first release of the LFM3 family covers models in the 2B parameter range.

Built on a new hybrid architecture and 22T tokens of pre-training, LFM3 is far more expressive than 
LFM2
 while maintaining its efficiency. The extra capacity in a small, fast model makes LFM3 the ideal starting point in its class for specialized intelligence: this is because it can be fine-tuned locally, it can run on any device, and it is capable enough to become a reliable expert on a specialized task.

The base and post-trained models are open-weight and available today on 
Hugging Face
, 
our Playground
, and the 
Liquid AI API
. Check out our 
docs
 on how to run and fine-tune them locally.

Highlights

More capability per parameter:
 a new tri-hybrid architecture and training recipe allow LFM3-1.7B to outperform our previous LFM2.5-2.6B while using 35% fewer parameters.

Every modality, one backbone: 
six 2B-class models (text, vision, audio, omni, and decision) trained from LFM3-1.7B-Base. 

Built for the edge:
 the text model fits in about 1 GB at 4-bit precision. 

New flagship in-house vision and audio encoders.

256K context window
 for the text model.

Made to be specialized:
 every model can be fine-tuned on a single GPU.

LFM3 instances are ideal candidates for specialized intelligence. Fine-tune them on your own data, and deploy them where your application runs. Enjoy the article.

Download weights

Try in Liquid API

Try in Playground

Benchmark in Pipette

New architecture for more expressivity

LFM2 showed that a hybrid of short convolutions and attention could run fast on-device without sacrificing quality. Its design came from our 
automated hardware-in-the-loop architecture search
. For LFM3, we used this search to redesign that architecture for agentic use cases, which need more capability per parameter and fast inference over long contexts.

We also expanded the hardware in the loop, from CPUs in one phone and one laptop for LFM2 to 14 device and backend combinations for LFM3: phones (Samsung Galaxy S26 Ultra and OnePlus 15), a Raspberry Pi 5, laptops (Apple M4 Max and AMD Ryzen AI), and Arm and x86 cloud CPUs, plus GPUs and the Qualcomm Hexagon NPU.

Gated short convolutions still make up over half the layers. To add capability without slowing down long contexts, we tried swapping some of them for other sequence blocks, and sliding-window attention (SWA) gave the best quality–speed tradeoff. We kept the other changes described below only where they improved quality without a meaningful speed cost. The payoff shows at long context. Per parameter, LFM3-1.7B matches LFM2-1.2B on short prompts across edge devices, and with 8K tokens in context it is about 25% faster.

Tri-hybrid layer mix.
 LFM3 combines three operators: gated short convolutions, sliding-window attention (SWA), and global attention. Of its 24 layers, 13 are convolutions, 5 are SWA with a 256-token window, and 6 are global attention. The convolutions also use a kernel size of 7, up from 3 in LFM2.

Head-wise gated attention.
 A sigmoid gate scales each head’s output, so a head can switch off when it has nothing to add. This can help 
suppress activation outliers
 that hurt quantization and
 improve training stability
.

Partial RoPE.
 Global attention layers rotate only the highest-frequency half of each head and leave the low-frequency half unrotated, so those dimensions
 match on content regardless of distance
. SWA layers keep full RoPE.

Sandwich norm.
 Each block normalizes both its input and its output, which helps keep activations well-scaled.

LFM3 uses the same 128K vocabulary as
 LFM2.5-8B-A1B
, built to tokenize non-Latin scripts more efficiently.

Training.
 LFM3-1.7B-Base was pre-trained on 22T tokens. Compared with LFM2, the mix adds more scientific papers, repository-level code, a wider range of knowledge sources, and considerably more math. The final 3.5T tokens are a mid-training stage on curated, higher-quality data, with a larger share of agentic traces and diverse tool calls to prepare the model for agentic post-training. This stage also extends the context window to 256K tokens.

A multimodal family for every need

The first LFM3 release includes six models, all branched from the same LFM3-1.7B-Base backbone and all around 2B parameters. Four of them cover different input modalities (text, vision, audio, and omni), and the last two are decision models specialized from the vision and omni models. Instead of running one large general-purpose model, you can pick the one that fits your use case, customize it, and run it on-device.

For a deeper dive into the performance and inference results behind these models, refer to the respective model cards.

“

As AI increasingly moves from the cloud to the client, developers need models that can be deployed efficiently across the broad spectrum of AI PCs. Liquid AI's LFM3 family combines strong multimodal capabilities with a compact footprint that is well suited for on-device AI experiences. AMD has worked closely with Liquid AI across multiple generations of models, and we're excited to see LFM3 expand what's possible for specialized AI applications running locally on systems with AMD Ryzen™ AI processors.

Josh Hort

Senior Director & Head of ISV Enabling at AMD

Across industries, we’re seeing edge AI evolve from running dedicated detection and perception models to supporting multiple concurrent AI workloads, including vision-language models, natural-language interfaces and multimodal reasoning. The challenge is delivering these capabilities within the compute, memory, and power constraints of edge devices. LFM3 brings text, vision, and audio together in a unified architecture designed for efficient deployment, with open weights that developers can fine-tune for specific applications. Developers can already run Liquid AI’s LFM2.5-VL models on Ambarella silicon through the Cooper Model Garden, and we have begun enabling LFM3 on the same platform.

Malhar Palkar

Senior Director for AI at Ambarella

The next generation of AI will be more multimodal, personalized, and private while being distributed across devices and the cloud. Liquid AI’s LFM3 family is an exciting step in that direction, and we’re pleased to work together to bring fast, efficient, and innovative AI experiences to devices powered by Snapdragon® processors.

Vinesh Sukumar

VP, Qualcomm Technologies, Inc.

01
 / 
03

Text

LFM3-1.7B

 is a text model for local agents and specialized applications with a 256K-token context window.

It is post-trained to run in agentic harnesses such as Hermes Agent, Pi, and OpenClaw. It can triage your inbox, manage your calendar, research topics on the web, send you morning briefings on WhatsApp, and use tool search to find the right tool among thousands of options. Since tokens are free, dozens of agents can run continuously in the background. You can adapt it to your domains, harnesses, and tools with a short fine-tuning run on a single GPU.

Benchmark

LFM3-1.7B (1.7B)

LFM2.5-2.6B (2.6B)

MiniCPM5

2B (2.5B)

Gemma 4

E4B (8B)

Qwen3.5

4B (4.7B)

Qwen3.5

9B (9.7B)

Agents

LiveClaw

45.60

14.70

30.37

20.36

19.94

35.77

Claw-Eval General (EN), average

68.64

62.63

60.74

56.14

61.96

66.53

Claw-Eval General (EN), pass^3

51.40

37.52

34.58

22.43

42.99

51.87

BrowseComp-Plus (OpenClaw subset)

37.00

26.33

16.83

21.00

24.67

38.00

WebArena-Verified

38.42

3.02

9.11

17.06

21.92

28.94

EnterpriseOps-Gym

28.20

7.94

13.41

9.86

25.96

28.97

AutomationBench (public)

41.29

0.94

4.71

1.92

8.67

15.10

Tool use

BFCL V4

71.39

55.89

62.65

48.25

55.12

62.83

ToolSandbox

80.36

78.04

68.16

69.27

75.40

76.41

MCP-Atlas

32.57

16.45

26.38

6.19

41.37

42.67

τ³-bench

68.01

56.77

69.44

33.53

65.98

67.11

Agentic coding

SWE-bench Verified (OpenCode)

43.40

18.00

34.80

0.50

41.20

51.20

SWE-bench Multilingual (OpenCode)

23.00

8.00

15.67

0.67

23.33

35.00

Terminal-Bench 2.1 (OpenCode)

12.92

0.00

5.62

0.00

13.48

17.98

Coding

LiveCodeBench v6

73.46

60.57

70.52

71.00

61.99

69.86

LiveCodeBench Pro 25Q2

31.74

19.16

29.34

29.94

24.25

34.43

SciCode

28.47

16.32

27.78

25.00

23.02

31.60

Instruction following

IFEval

96.66

95.39

87.83

90.02

92.52

92.08

IFBench

73.03

60.48

62.08

44.56

38.16

48.84

IFStruct

93.72

82.18

72.65

78.45

87.05

89.20

Multi-IF

89.10

84.80

73.19

81.03

80.32

84.44

Knowledge

GPQA Diamond

63.37

57.78

65.15

57.88

75.76

80.40

Humanity's Last Exam (no tools)

7.17

5.88

8.20

4.77

12.84

16.41

Humanity's Last Exam (with tools)

13.90

9.60

11.50

6.00

11.60

17.50

AA-Omniscience (public)

0.50

-33.17

-5.00

-15.33

-57.17

-28.00

AA-Omniscience accuracy (public)

7.07

8.75

9.13

9.83

15.67

13.17

AA-Omniscience non-hallucination (public)

92.93

53.69

84.44

72.09

13.64

52.59

Long context

AA-LCR

52.83

6.00

49.34

39.33

52.67

62.00

RULER 128K

65.56

1.15

37.96

18.82

84.63

87.11

Average

49.37

31.55

39.19

31.74

39.27

47.24

On agentic tasks, LFM3-1.7B competes with models several times its size. It leads on instruction following and function calling on BFCL and ToolSandbox, and beats Qwen3.5-9B on long tasks in browsers and business apps (WebArena-Verified, AutomationBench). Larger models still win on agentic coding and knowledge, where size matters most, but search helps close the knowledge gap, nearly doubling its score on Humanity's Last Exam.

To achieve these results, the model went through four stages of post-training:

Supervised fine-tuning (SFT):
 1.75T tokens across various tasks, including chat, reasoning, tool calling, and agentic traces.

Mixed reinforcement learning:
 many domains trained at once, from math and code to SQL and structured outputs. A length penalty in the reward keeps answers concise.

Multi-domain on-policy distillation (MOPD):
 six specialist RL teachers (code, math, tool use, long context, agentic work, and enterprise workflows) are distilled back into a single model.

Agentic RL:
 tasks from web browsing to office work are run inside real agent harnesses, preparing the model for deployment.

On-device, we measure metrics with llama.cpp at Q4_0 and a 32K-token context. LFM3-1.7B is the fastest model on all three devices, decoding 1.8 to 2.8 times faster than the next one, and it uses the least memory. Long contexts stay cheap: a full 128K-token context needs 1.6 GB of KV cache, against 4.3 GB for Qwen3.5-4B and 5.6 GB for MiniCPM5-2B.

On a single NVIDIA B300 with SGLang in BF16, LFM3-1.7B can produce 3.6 billion tokens per day at 1,024 concurrent requests, more than any other model in this comparison.

To show what this throughput makes possible, we ran more than 300,000 LFM3-1.7B agents in parallel to investigate the Enron email archive.

LFM3-1.7B can be served at low latency under random traffic, enabling real-time use cases like online fraud detection when run on 

Liquid RIPL

. P95 request latency remains stable even under heavy load, outperforming competing models served on vLLM.

“

We tested LFM3-1.7B against Qwen3.5-2B on 65 everyday agent tasks in real macOS environments. The smaller model won: 64% task success versus 48%, 58% fewer tokens per task, and it got stuck in under 1% of attempts versus 15%. Small models are ready for real agent work on the Mac, and LFM3 is the proof. LFM3 is the first sub-2B model we’ve tested that is ready for real agent work on a Mac — it beat a larger model on task success while using 58% fewer tokens and almost never getting stuck.

Ivan Petrukha

Staff AI Engineer, LLM Efficiency Lead at MacPaw

Vision

LFM3-VL-2B
 can watch, reason, and understand the physical world:

Video understanding:
 for the first time, an LFM vision model takes video as input. Ask questions about a recorded lecture, a walkthrough filmed on your phone, or a clip from a camera feed.

Thinking:
 the model reasons step by step before answering. This helps it better understand user inputs and solve harder visual questions such as math, charts, and multi-step problems.

Spatial and embodied reasoning: 
the model’s ability to localize objects and reason about their spatial relationships provides a strong foundation for downstream robotics applications.

LFM3-VL-2B is a leap in performance over the LFM2.5-VL series. Across 62 vision benchmarks, LFM3-VL-2B scores significantly ahead of all models of similar size by at least 7.4 points, and despite its size, it matches the performance of Gemma 4 12B, a model more than 6 times larger, surpasses Gemini 3.5 Flash Lite and is within 2 points of GPT-5.6 Luna. For more details, see the model card.

Benchmark Category

LFM3-VL-2B (1.9B)

LFM2.5-VL-3B (3.1B)

MiniCPM-V 4.7 1B (1.6B)

Qwen 3.5 2B (2.3B)

Gemma 4 E2B (5.1B)

Gemma 4 12B (12B)

GPT-5.6 Luna

Gemini 3.5 Flash Lite

General

66.0

57.6

59.8

64.0

56.9

74.0

72.2

74.1

Perception

75.6

67.9

65.5

71.2

59.1

73.5

71.0

73.0

Document, OCR & Chart

83.9

71.2

73.0

79.1

72.3

85.7

84.4

82.3

Math & logical reasoning

68.8

40.6

51.8

61.0

51.8

79.3

77.3

66.7

Visual grounding

77.3

68.3

51.1

61.2

41.2

74.1

72.7

63.5

Embodied reasoning

64.4

48.0

45.3

51.2

41.5

59.1

61.5

50.3

GUI understanding

83.1

66.0

45.3

67.2

44.3

76.1

82.5

71.0

Video

61.2

41.3

53.7

57.0

46.6

58.9

72.8

70.0

Multilingual

84.4

81.2

77.4

78.6

73.4

86.1

82.1

85.8

Agentic

42.5

21.1

16.9

15.2

23.8

43.6

56.1

62.4

Average

71.4

57.6

57.5

64.0

53.6

71.7

73.4

70.0

Notes: Each category score is the unweighted mean of its benchmark scores. The Average row is the unweighted mean across all 62 evaluations. 

All of this can be run efficiently on-device, which enables everyday use of intelligence without the data leaving your device or the need for a cloud connection. On-device, LFM3-VL-2B has the highest prefill throughput and lowest memory footprint across all measured devices, compared to other models of its size class.

On a single NVIDIA B300 with SGLang in BF16, LFM3-VL-2B can produce over 12,000 tokens per second, higher than any other model of the same size class.

LFM3-VL-2B can be served at low latency under random traffic, enabling real-time use cases like image asset tagging when run on 

Liquid RIPL

. P95 request latency remains stable even under heavy load, outperforming competing models served on vLLM.

Vision encoder

In addition to improvements to the LFM3 backbone, LFM3-VL comes with our new in-house vision encoder which uses 3× less compute than the SigLIP2 encoder in previous LFM VL models. 

The Liquid vision encoder combines convolution and attention to make it significantly more efficient than its ViT counterpart at the same quality. The performance-efficiency graph below illustrates this. Our 164M-parameter encoder matches Qwen3.5-2B’s vision encoder at 55.9% average accuracy across 13 vision-language model benchmarks, while requiring 2.2× fewer FLOPs. 

For video, the encoder jointly embeds each pair of sampled frames into one temporal slice of visual features, halving the temporal sequence length before further encoding. Together, these choices make the encoder a foundation for both richer image understanding and efficient video processing.

Audio

LFM3-Audio-2B
 is a compact, fully featured audio model that runs locally on laptops and edge devices. It takes text or audio as input and responds with text, speech, or both.

LFM3-Audio-2B uses a new architecture with an audio encoder and codec developed in-house. It outperforms LFM2.5-Audio in speech quality and now supports 18 languages. New capabilities include audio understanding, general-purpose audio reasoning, and tool calling.

Voice chat:
 ask questions aloud and receive streaming replies in text and speech. For text-only responses, the model can also reason before answering.

Multilingual speech:
 transcribe, synthesize, and translate speech across 18 languages.

Audio understanding and reasoning:
 ask the model to interpret recordings and answer questions about the speech, sounds, and events they contain.

Tool calling:
 turn spoken requests into tool calls to control apps and devices. The model can also respond in text or speech alongside those calls.

“

Our ambition is to make the interaction between driver and vehicle as natural and intuitive as possible. Together with Liquid, we are exploring how powerful on-device AI can further enhance the MBUX Virtual Assistant, while enabling fast, private and cloud-independent experiences. Our MB.OS architecture provides the foundation to bring innovations like these into our vehicles.

Jörg Burzer

Member of the Board of Management of Mercedes-Benz Group AG, Chief Technology Officer, Development & Procurement

ASR (WER, %, lower is better)

LFM3-Audio-2B

LFM2.5-Audio-1.5B

Gemma 4 E2B

Gemma 4 E4B

Qwen2.5-Omni-3B

Nvidia Audex 2B

Voxtral Mini 3B

MiMo-Audio-7B-Instruct

Kimi-Audio-7B-Instruct

Total parameters

2B

1.5B

5B

8B

6B

3B

5B

8B

10B

English

6.2

6.1

8.3

7.8

6.3

6

5.5

8.5

5.3

Multilingual (avg. across en, es, pt, de, fr, it, zh, ja, ko)

6

–

8.1

6.5

7.4

6.4

7.8

–

–

English TTS (UTMOSv2, 1-5, higher is better) (WER, %, lower is better)

LFM3-Audio-2B

LFM2.5-Audio-1.5B

Qwen2.5-Omni-3B

MiMo-Audio-7B-Instruct

Total parameters

2B

1.5B

6B

8B

UTMOSv2

3.8

3.2

3.4

2.8

WER

1.4

1.9

3.2

4.9

VoiceBench, Tool calling, Audio understanding (audio in, text out, %, higher is better) 

LFM3-Audio-2B

LFM2.5-Audio-1.5B

Qwen2.5-Omni-3B

Gemma 4 E2B

Gemma 4 E4B

Voxtral Mini 3B

MiMo-Audio-7B-Instruct

Kimi-Audio-7B-Instruct

Total parameters

2B

1.5B

6B

5B

8B

5B

8B

10B

VoiceBench 

73.1

55.2

66.4

63.3

72.9

65.8

77.3

76.9

Tool-calling 
(Internal eval)

58.5

–

44.3

55.6

72.4

44.5

33.4

50.6

Audio understanding 
(MMAR)

50.6

25.9

54.4

44.5

49.1

50.1

62.3

53.3

Our new LFM-based audio encoder is built from a mixture of sliding-window attention and short-convolution layers, keeping memory utilization bounded. The new encoder is fully causal, allowing the model to process live microphone input and perform prefill while you speak. This reduces the wait after you finish, with time to the first token as low as 50 ms.

LiquidCodec, our new audio tokenizer, powers multilingual speech generation in both LFM3-Audio and LFM3-Omni. Built on the LFM3 architecture, LiquidCodec turns generated tokens into speech at about 87× real time on a single CPU thread (Apple M4 Max), supporting streaming decoding. 

Quantization compresses each 80 ms of speech into 12 discrete tokens and, in contrast to previous LFM Audio models, allows multiple tokens to be predicted iteratively in parallel rather than requiring sequential prediction. As the backbone generates new tokens, the detokenizer progressively converts them into speech, all faster than real-time so that conversations are smooth and responsive.

Omni

LFM3-Omni-2B
 is our first omni model, bringing vision, audio, and language together in a single model that can see, listen, and talk back:

Spoken visual question answering:
 Ask questions about images or real-world scenes using speech, and receive answers in text, speech, or both.

Audio-visual video understanding:
 Process video frames alongside their corresponding audio, allowing the model to reason about both what is happening on screen and what is being said or heard.

Multimodal tool calling:
 Combine visual context with spoken instructions to generate structured tool calls, enabling assistants to interact with applications and interfaces using both what they see and what users say.

LFM3-Omni supports cross-modal interactions that require understanding visual and auditory information together. Users can ask spoken questions about images, or provide videos with synchronized audio and ask questions that depend on both what is seen and what is heard.

LFM3-Omni-2B

Qwen2.5-Omni-3B

Qwen2.5-Omni-7B

Gemma 4 E2B

Gemma 4 E4B

Phi-4-multimodal

Params

2.2B

6B

10.7B

5B

8B

5.6B

Video + Audio Understanding

Daily-Omni

70.1

58.8

61.3

50.6

54.1

48.9

WorldSense

47.1

45

45.4

38.1

43.5

42.4

AV-SpeakerBench

46.8

40.4

43.2

32.3

36.4

38

Image + Audio Understanding

OmniBench (overall)

46.3

47.1

49.7

16.8

20.7

39

OmniBench Speech

48.2

45.7

48

16.1

21.3

38.9

Spoken Visual QA

RealWorldQA

64.7

61.1

69.9

39.4

49

64.3

MMStar

51.8

50.8

57.3

38.9

44.6

54.8

POPE

83.8

85.3

85.4

74.2

77.8

83

ERQA

39.4

37.3

39.2

20.6

32.1

30.8

EmbSpatial

67.6

53.4

59.5

44.1

54.0

42.6

In addition to cross-modal understanding, LFM3-Omni retains the core capabilities of the standalone LFM3 models, including visual question answering, speech recognition, speech synthesis, and language instruction following.

LFM3-Omni-2B is designed for efficient deployment in resource-constrained environments. Its capabilities enable conversational assistants that can provide context-aware guidance, support hands-free interactions, and help users complete tasks through natural voice commands. By combining visual understanding, spoken dialogue, and tool calling, it can support applications ranging from personalized education and everyday assistance to navigation of digital interfaces and robotic systems.

At 2.2B parameters, it brings this kind of multimodal assistant on-device. Examples include a tutor that looks at your handwritten math and answers your spoken question, a tablet you can walk around with and ask about what it sees, and in-car assistants that combine what the camera sees with what the driver says.

Flight booking

Event flyer

Driving

SAT math

SAT reading

Grounded tool use from speech

LFM3-Omni goes from spoken audio straight to structured tool calls.
Precise visual grounding locates any element on screen, so one model can listen, see and act.

Decision

This release also brings two new decision models: 
d1-2B
, built on LFM3-VL-2B, reads text and pictures, and 
d1-Omni-2B
, built on LFM3-Omni-2B, also listens. Instead of writing an answer, they decide in milliseconds. Give them a situation (a support ticket, an invoice, an app screen, a photo, a voice note) and a list of questions, and they answer all of them in a single forward pass, each with a calibrated probability.

Beyond the new LFM3 backbone, the big change since 
d1-3B
 is 
typed answers
. On top of yes/no, choices, and scores, both models can now:

Point:
 draw a box around what you describe, or find every instance of something, with a count.

Read:
 pull text, numbers, and dates out of a document, with the exact span they came from, and say “not found” when a field isn’t there.

Estimate:
 give a number with its likely range.

Pick:
 select every option that applies, each with its own probability.

Ask as many questions as you like: they’re read in one pass over the same input.

Smaller and stronger.
 d1-2B replaces our previous d1-3B, with a third fewer parameters:

d1-3B

d1-2B

Decision Bench (real enterprise records)

83.6

85.2

Decision Index, public suite

49.0

51.1

ImajevBench (decisions from photos and rules)

64.0

75.5

Our Meta index (117 private and public benchmarks)

58.8

63.2

Decisions you can speak.
 d1-Omni-2B takes the same questions over audio, so a voice request can be routed, checked, or answered just like a typed one. Asked by voice instead of in writing, it keeps nearly all of its accuracy:

written

spoken

DecisionBench (business routing and triage)

83.4

78.2

Typed Decisions (customer service cases)

50.5

48.0

JevBench

87.6

89.0

It also recognizes everyday sounds (84.5% on ESC-50) and tells which of 43 languages is being spoken (92.5% on FLEURS).

Pick d1-2B for text and pictures, and d1-Omni-2B when your inputs include audio. Both run on-device, and turn a stream of tickets, documents, calls, or camera frames into structured decisions without a round trip to the cloud.

In the following demo, d1-2B runs on a MacBook. You describe what to find in plain language, and it draws a bounding box around every match in a single forward pass, using the new Point answer type.

Made for specialized intelligence

LFM3 is built to be specialized. The 2B-class models are small enough to fine-tune on your own data and run where your application lives. The following two examples show this with LFM3-VL-2B. The first is a short fine-tune that turns it into an inspection model for one narrow industrial task. The second is a research extension that turns it into a robot controller.

Domain expertise: Specializing LFM3 for your field

While frontier models are powerful generalists, they are not necessarily experts in your particular use case. In this demo, we fine-tuned LFM3-VL-2B to find and classify defects in drone photos of wind turbine blades. Training used about 3,000 public photos (

WTBs2025

) with SFT and GRPO for a few hours on one A100. We then compared it with the base model and GPT-6 Luna on about 1,400 held-out photos.

Out of the box, LFM3-VL-2B and GPT-6 Luna correctly identify these defect types in fewer than 10% of images. A short fine-tune raises LFM3-VL-2B’s classification accuracy to 67% and improves detection F1 from 0.003 to 0.11, compared with 0.01 for GPT-6 Luna. Lightning-strike images illustrate the difference, where GPT-6 Luna often locates the defect correctly but labels it incorrectly, while the fine-tuned model correctly identifies a lightning strike. Beyond classification and detection, the model can answer natural-language questions about the same image. For example, it can locate visible damage or write a brief inspection finding including the defect type, supporting evidence, and location.

Wind turbine fine-tuning example

Start customizing LFM3 with our fine-tuning notebooks

Robotics: teaching LFM3 to act

We investigate how LFM3-VL-2B can serve as a basis for robotics applications. We consider three complementary directions: (1) high-level tool orchestration, (2) vision-language navigation, and (3) low-level manipulation.

Orchestration.
 Building on LLM-based robot planning and control (SayCan, Code as Policies) and recent physical orchestrators (VoLo, Gemini Robotics ER 2), we fine-tuned LFM3-VL-2B to operate a robot arm through tools. Given a request and the current camera image, it reasons step by step, grounds objects by pointing, measures them with depth tools, and manipulates them via motion planners. It then checks each outcome in the next image and reports back, including when a request is out of reach or ambiguous. The tasks feature relational selection, sorting by measured properties, and environment perturbations, all simulated in Isaac Sim. No architectural change was needed. A rank-32 LoRA adapter was trained on about 40,000 samples, combining manipulation trajectories with general tool-use and pointing data, and took about six GPU-hours on a single AMD Instinct MI325X. Paired with a fine-tuned d1-2B skill monitor, we can further double recovery success under disturbances such as slips, jams and drags.

Navigation.
 For vision-and-language navigation, LFM3-VL-2B reads a route description and a short history of RGB frames to predict navigation targets and residual-quantized trajectory primitives, inspired by the action interface of LightNav-0. Each decision consists of five tokens: two spatial/control tokens and three hierarchically quantized codes encoding a ten-waypoint path that a velocity controller can track. We only repurpose 2,068 vocabulary tokens; the architecture is otherwise unchanged. We train on 2.8 million samples for 72 GPU-hours on MI325X GPUs. In unseen validation scenes, the resulting model achieves success rates of 53% on R2R and 43% on RxR under a strict continuous-control evaluation protocol with wall sliding disabled and explicit stopping required. We further observe robustness across varying camera angles and instruction languages. On a Jetson AGX Orin, our navigation model updates waypoint trajectories at over 2.5 Hz using TensorRT FP16 without visual prompt caching.

Manipulation.
 To turn LFM3-VL-2B into a vision-language-action (VLA) model, we adopt parallel action prediction inspired by OpenVLA-OFT and StarVLA-α: a small residual MLP maps the hidden states of eight action-query tokens to an eight-step chunk of continuous robot actions in a single forward pass. Proprioception is provided both as discretized text and through an embodiment-specific learned projection, and the whole network is fine-tuned end to end. We trained a single generalist checkpoint for 170 GPU-hours on MI325X GPUs, on simulated and real-robot data from 15 embodiments, ranging from single arms and mobile manipulators to bimanual platforms and a humanoid. The resulting VLA achieves 96.2% average success across the four LIBERO suites and 45.7% on RoboCasa-GR1 tabletop tasks. On a Jetson AGX Orin, it can generate action chunks in under 50 ms using TensorRT at FP16 precision.

Get Started

Start building today with LFM3, available on 

Hugging Face

 and the 

Liquid AI API

.

With LFM3, we're delivering on our vision of AI that runs anywhere. These models are:

Open-weight:
 download, fine-tune, and deploy.

Fast from day one:
 native support for llama.cpp, MLX, and vLLM across Apple, AMD, NVIDIA, SGLang and Qualcomm hardware. Deploy on 

Liquid Real-time Inference Pipeline

 for low-latency, high-volume workloads.

A complete family:
 from base models for customization to specialized text, vision, audio, omni, and decision models, one architecture covers diverse use cases.

We can't wait to see what you build.

Download on Hugging Face

Use with Liquid API

Try on Playground

Launch Partners

We are grateful to our day-0 launch partners for their support. LFM3 is ready to use today across these platforms: Ambarella, AMD, Arm, Intel via OpenVINO, NVIDIA, OpenRouter, Qualcomm via Qualcomm AI Hub and GenieX, and Vercel. Thanks to Mercedes-Benz and Shopify for partnering on pre-release testing and evaluation.

Thank you to our builder ecosystem for its support: Atomic, Cactus, Hugging Face, llama.cpp, LM Studio, MLX, Ollama, RadixArk on SGLang, .txt, Unsloth, vLLM, and ZML. 

Citation

For citations, please use the following reference or BibTeX:

Liquid AI, "Introducing LFM3: Every Modality for Specialized Intelligence", Liquid AI Blog, October 2026.

@article{liquidAI2026LFM3,
 author = {Liquid AI},
 title = {Introducing LFM3: Every Modality for Specialized Intelligence},
 journal = {Liquid AI Blog},
 year = {2026},
 note = {www.liquid.ai/blog/lfm3},
}

Share on social:

For press inquiries, email us at

press@liquid.ai
