---
title: "A Guide to Choosing Voice AI Models"
source: "Cartesia Blog"
url: "https://www.cartesia.ai/blog/choosing-voice-ai-models"
scraped: "2026-11-21T06:00:34.488842+00:00"
lastmod: "None"
type: "sitemap"
---

# A Guide to Choosing Voice AI Models

**Source**: [https://www.cartesia.ai/blog/choosing-voice-ai-models](https://www.cartesia.ai/blog/choosing-voice-ai-models)

Choosing Models for Enterprise Voice AI
Many teams assume building an AI Voice Agent is as easy as picking a Text-To-Speech (TTS) voice that “sounds professional,” hooking it up to their existing chat bot, wiring it to an LLM and adding some Automatic Speech Recognition (ASR) to kick it all off. After a few months they ship a prototype that benchmarks at 600–800ms round-trip in a quiet room on macOS.
But then in real life, this system hits 2 - 4 seconds on real telephony infrastructure, with P95 (95th percentile latency – the maximum latency number that 95% of calls experience) spiking to 5 seconds. Add to this lower quality that comes with 8khz telephony infrastructure, and the “IRL” experience of voice agents can be starkly different from eval conditions.
It is tempting to choose the models based on benchmarks that measure them in laboratory conditions. But real-life conversations are messy, and that makes enterprise-grade voice agents a hard engineering problem. We cannot solve these hard problems by treating voice models as interchangeable commodities. Instead, they must be picked, analysed and measured against their performance
for their intended use case
.
The same model that nails a British broadcast accent for studio podcasts, might not perform for an airline helpdesk connected via PSTN telephony. One that is designed to transcribe speech very accurately in a browser may struggle to detect speaker utterances over a call. One that excels at push-to-talk use cases might struggle to know when a user has finished speaking, or has merely trailed off while they’re thinking. You get the point!
Demos & Benchmarks vs Reality
Public benchmarks are a very useful and valid starting point, but should not form the entire basis of the final vendor selection. We must also apply scrutiny to whether the benchmarks reflect the intended use case. For example, many voice AI Benchmark datasets contain “ideal audio” - studio recordings, audiobook excerpts, and scripted prompts — speech with no “uhm,” no trailing off, no background noise, long silences, etc.
But when a customer says “umh, actually let me [long pause] check something else…” and is rummaging around their desk, a rules-based VAD (Voice Activity Detection) may fire a
turn_ended
event because it detected a pause and is optimized to reduce latency by rushing ahead. This triggers the ASR model to transcribe the audio, then the orchestration layer pipes the transcription to the LLM to generate a response. The LLM’s text response is immediately converted into smooth speech, with great tone. That sounds good, except the user resumes talking and the agent speaks over them.
Realistic audio training and benchmarking datasets is very hard to (legally) acquire at scale, which is why many benchmarks measure the ideal (laboratory) conditions and not realistic scenarios.
So if your intended use case is a conversational AI Agent that handles customer conversations over the phone, in noisy environments, you need to investigate whether the models you use are designed to handle these all-too-real scenarios.
What “Choosing Voice AI Models” Actually Means
1. Evaluating Time-to-Complete-Transcript (TTCT), Not Time-to-First-Token
Most teams benchmark ASR models on TTFT (Time to First Token) ,
RTF (Realtime Factor)
, or average per-word latency. But these are often vanity metrics
for
realtime
AI Voice
Agents
.
For voice agents, we believe the metric that matters is TTFS - Time to Final Segment (aka the Time to Complete Transcript (TTCT)).
This is the time gap from the millisecond the user finishes their turn to the millisecond the model outputs a
finalized
transcript that an LLM agent can rely on. TTFS determines whether the agent feels present or lagging, and also the downstream quality of the conversation and its next turn.
Below 200ms (measured
end-to-end
, not per ASR/LLM/TTS segment in the pipeline) and the conversation feels natural. Between 500ms–1s, users notice the delay but tolerate it. Above 1s, they start repeating themselves or “colliding” at unexpected times. As you can imagine, these collisions compound — the user speaks louder, the ASR model gets distracted by their own previous words, the LLM gets garbage input, and the whole loop degrades.
2. Evaluating Turn detection, and Interruption Handling
Turn-detection
is also known as end pointing – because it refers to detecting when the user has finished their turn. It is extremely hard to do accurately as Speech to Text models do not have visual or other cues like humans do in conversation. That makes high-quality turn detection incredibly important for conversational AI - poor turn detection results in very long awkward pauses and high latency in the voice agent’s conversation.
The absence of visual cues also means that the voice agent orchestration layer and harness must handle scenarios where the user abruptly resumes speaking or interrupts the voice agent. A robust voice agent will cancel its LLM call
and
in-flight TTS generation when a user starts a new turn (or resumes one that was assumed to be over).
When they’re evaluating latency and conversational flow in ASR models, most teams fail to realize that they are actually evaluating turn-detection and “precision vs recall”. The realization dawns only when they debug the gap between demo and production. Like all debugging, it’s fastest and cheapest when you
shift-left
and catch it early.
“Precision” is the accuracy with which a turn-detecting ASR model correctly detects a user’s
turn_start
and
turn_end
- a falsely detected
turn_start
means interruptions to transcription and the pipeline, and a falsely detected
turn_end
means the agent may interrupt the user. “Recall” is the measure of whether the ASR model missed a
turn_start
(meaning the agent missed the user’s turn entirely) or
turn_end
(meaning the agent never responds).
ASR with integrated turn-detection is common these days. However, precision/recall is what determines state of the art. Historically precision and recall were traded off - high precision came at the cost of recall. But now Cartesia’s
Ink-2 ASR model
has
established the state of the art
because of high precision
and
high recall for both turn-end detection and turn-start detection.
This is achieved because Ink-2 doesn’t just use silence-length as the rule - it uses the spoken
context
to detect user turns. That’s how Ink-2 understands whether you’re reading a phone number, trailing off, thinking or are actually done.
3. Accuracy Where It Matters
Word Error Rate (WER)
for STT/ASR is a misleading metric if you’re looking at the wrong or irrelevant classes of errors. Or if you’re comparing a non-streaming ASR model (which is inherently easier to be accurate on) with a streaming ASR model. Unfortunately many benchmarks do not distinguish between ASR streaming vs non-streaming use cases.
It is best to measure WER across categories of input data because a single average WER metric hides category-level weaknesses (how the ASR model handles phone numbers, names, UUIDs, etc.). The same model that gets phone numbers at 2% WER can hit 23% on accented speech. Also, some domains like medicine and law have domain-specific vocabulary or phrases, and off-the-shelf consumer-grade benchmarks may not measure this requirement at all.
If your agent handles inbound customer support across diverse geographies, your WER on accented speech matters more than your WER on clean English-only earnings call transcripts.
Your intended use case may require a low WER on only
some
categories - which is worth knowing when analyzing tradeoffs with other performance metrics. If the benchmarks you’re relying on have not tested on data that your use case will encounter, then those benchmarks are meaningless -
to you
.
On the TTS side, WER measures intelligibility of the synthesized speech compared to the input transcript. What matters is the coherence of the speech, the quality of pronunciation, pacing,
prosody
, handling numbers, acronyms, amounts, quantities (how it handles “March 3rd” vs “03/03” and “twelve hundred dollars” vs “$1,200” ). Also, the pronunciation of domain-specific vocabulary matters for specific use cases.
Ideally the best way to measure accuracy in your chosen models is:
Identify the categories of performance you care about.
Measure all of them separately, across a mix of scenarios.
Examine performance across all scenarios and categories.
Pick the model that is robust to your use-cases / needs.
Once again, being decisive about metrics that move the needle, and incisive when looking at benchmarks, is critical to pick the right voice models for your voice agent.
4. Cloning Voices
Many customers prefer cloned voices for their use cases that require continuity between current human-customer interactions and the agentic interactions they’re designing for.
At Cartesia, there are two ways to clone a voice:
Instant voice cloning
(“IVC”, done from 5 seconds of audio) and
Professional Voice Cloning
(“PVC”, done from 30+ minutes of voice audio).
When cloning voices enterprise customers must deeply understand what qualities make that voice fit for its intended purpose, and what attributes must be preserved and optimized for.
There are also important design and speech implications when
“localizing”
these voices to other languages, such that the voice sounds “native” to the other language. Having clear expectations on localization, accent adjustment, custom pronunciations and other attributes will help in designing effective voice agents as these attributes can greatly influence the conversational experience.
5. The Voice Design Surface
Every voice AI platform exposes some version of three controls on their Text to Speech model: Speed, Volume, Emotion.
Cartesia’s Sonic-3.5 TTS model goes further. You can configure these attributes, but the Sonic will emote in
alignment
with the input text provided and disregard configuration that may be at odds with the semantic context of the input text.
So, if you want an empathetic tone, your LLM must generate empathetic text. Thus, the voice design is made context-aware and coupled with the LLM’s generation.
Coupling the voice agent’s design with its text inputs gives you more power and flexibility when choosing your LLM and in matching your system’s personality to the intended use case.
Cartesia also designs each voice to have a root emotiveness - designed for scenarios where the voice must match a specific use case. A “cheerful fixer” voice sounds different from a “trusted confidant” voice. Match the voice to the emotion you need, then match the LLM prompt to the voice you picked.
A Framework for Choosing
Truly effective conversational Voice Agents are a difficult technical accomplishment. Here’s what we’ve seen from our most successful customers:
Step 1: Define goals, then map them to voice characteristics.
An example of mappings you may define for your use case:
Use case
Voice speed
Emotion / temperature
Responsiveness
Reference
Outbound sales
1.1× – 1.3× (urgent, forward-moving)
High (warm, enthusiastic)
Medium-Fast (300-500ms)
Customer support
0.8× – 1.0× (measured, calm)
Low to medium (steady, reassuring)
Medium (500-650ms, space to think)
Collections / compliance
0.9× – 1.0× (clear, firm)
Low (controlled, professional)
Slow 650-800ms (let statements finish)
Meditation App
0.7× – 1.0× (calm)
Low (soothing, reassuring)
Slow-medium 650-400ms – unhurried, relaxed
If you’re building an appointment scheduler for a clinic, a wrong phone number or misheard date is a compliance incident and a potential loss of sale. If you’re building an IVR for credit card collections, accuracy matters more than conversational enthusiasm.
Start with your worst-case call scenario, not the ideal one, and work backwards from what drives the undesirable outcomes.
Step 2: Analyse public benchmarks to see if they test what you need
Voice AI benchmarks are meaningless if the evaluation dataset doesn’t match your commercial reality. In fact, it is counterproductive when what sounds attractive can also cause reliability issues (e.g. low latency from aggressive turn-end detection, resulting in too much interruption or bad inputs into tool calling).
Many public benchmarks rely on mislabelled datasets, archaic audiobook data, short, mid-sentence clips, studio recordings, or read-aloud datasets because they’re easy to get. Open datasets are often weak at mirroring production conditions — and models overfit to them so badly they learn to guess the wrong label from dataset artifacts, not from understanding speech.
These datasets may have little resemblance to your conversational agent’s operating environment.
A good strategy would be to do vendor red-teaming. Give your Voice Agent vendors 50 real phone calls from your actual customer base — with background noise, accents, overlapping speech, product names, and the awkward silence that happens when people switch from typing to speaking. Analyse the end to end performance and “feel” for several weeks.
You can also scale this approach by using Sierra’s
Voice Sims
, to simulate callers who speak different languages, have different needs, call from different locations (at home with the TV on, from the street, on a train), in different emotional states, and in different situations.
Step 3: Identify the metrics that your use case depends on
As we discussed earlier in this blog, not every metric matters and when they do, they generally don’t matter equally. A healthcare scheduling agent must perform very well on domain-vocab WER for medical terminology and structured data (drug names, dates, dosages). A high-volume outbound sales agent cares most about end-to-end latency and barge-in accuracy. A compliance-sensitive collections agent needs reliable turn detection that never cuts off a legally required disclosure. And ultimately, the most important metric for AI Voice Agents in enterprises is: did it get the job done efficiently, scalably and with minimal handover to human agents.
Map your use case to the two or three metrics that influence your commercial goals, and evaluate your options against those.
Step 4: Own your timing budget
Set a latency budget for each component. Something like:
ASR turn detection: 50ms
ASR TTCT (TTFS): 200ms
LLM first token: 300ms
TTS generation
buffers
for LLM-originated text input
TTS first audio: 100ms
Total pipeline: 500ms end-to-end
Now assign owners for each budget line. The team will tell you within two weeks whether 500ms is unrealistic under telephony conditions — that friction is useful, because it surfaces the real constraint before you’re in production.
Parting thoughts
Building enterprise voice agents is harder than the internet makes it sound.
If you’re a product buyer or engineering leader evaluating voice vendors, the right question is: which architecture handles your use cases, your latency budget, and your compliance posture in a brand-aligned way — even when the customer is on a landline from a hotel room, speaking with a regional accent, and interrupting mid-sentence?
It’s tempting to pick voice models based on how they sound or how they perform on a sanitized benchmark, only to discover a P95 metric that undermines months of work and expensive development.
If you’re looking to combine cutting-edge AI research with focused commercial pragmatism when building your enterprise-grade Voice Agent, reach out to us at
business@cartesia.ai
– we can help.
