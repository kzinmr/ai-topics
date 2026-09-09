---
title: "Audio-native semantic speaker-change detection"
source: "Decagon Blog"
url: "https://decagon.ai/blog/audio-native-semantic-speaker-change-detection"
scraped: "2026-09-09T06:00:02.036613+00:00"
lastmod: "2026-09-04T10:13:34.525Z"
type: "sitemap"
---

# Audio-native semantic speaker-change detection

**Source**: [https://decagon.ai/blog/audio-native-semantic-speaker-change-detection](https://decagon.ai/blog/audio-native-semantic-speaker-change-detection)

Decagon Dialogues 2026 is here.
Register today
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Duet AI partner
Build
AOPs
Workflows for AI agents
Integrations
Support for tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & reporting
Voice of the customer
Watchtower
Always on QA
Suggestions
AI powered knowledge
Industries
Financial services
Travel & hospitality
Health & wellness
Technology
Retail
Telecommunications
Media
Customers
Resources
Resources Hub
Blog
Decagon University
Videos
Glossary
Guides
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Trust Center
LinkedIn
X
Sign in
Get a demo
Sign in
Get a demo
Research & Technology
Audio-native semantic speaker-change detection
Posted on
September 3, 2026
Alan Ragoler
Research Intern
Dante Everart
Speech AI Researcher
Article
Table of contents
Introduction
What is an Agent Engineer?
Subscribe to our Newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Must be a valid company email (i.e. example@companydomain.com)
Get a demo
Done!
Oops! Something went wrong while submitting the form.
The problem: knowing when another user joins the conversation
In customer support, voice agents need to know not only what was said, but who is participating. If another person takes over a call or begins instructing the customer, the agent may need to pause, re-authenticate, or restrict sensitive actions. Missing that change creates security and fraud risk, while flagging every background voice would constantly interrupt legitimate conversations.
Standard ASR-to-LLM-to-TTS pipelines cannot reliably make this decision. They miss out on whether speech came from the customer, another participant, a television, an announcement, or background voices. To solve this problem, we need dynamic audio-native solutions that can act on the raw waveform.
Benchmark construction
Production benchmarks should measure whether the system behaves correctly, not just whether a second voice is acoustically present. A loud airport announcement should not interrupt the call; someone taking over or coaching the customer through a sensitive action should. We therefore annotate only relevant speaker changes—those that should alter the agent’s behavior—and stratify ambiguous misses and false positives by their likely impact on conversation flow.
Because one false trigger can disrupt an otherwise successful call, we measure conversation-level false-positive rate (cFPR): the share of conversations with any false trigger before or without a relevant speaker change. Turn-level FPR understates this compounding risk:
Fig. 1 — Turn-level FPR compounds to create conversation-level FPR
For positive conversations, conversation-level recall asks whether the system triggers on the first request containing the relevant new speaker; a late trigger both misses the change and may fire after that speaker has left. We therefore maximize conversation-level recall at a fixed cFPR ceiling.
Solutions
Diarization
Diarization asks “who spoke when?” Models like
Pyannote
and
Sortformer
can be adapted by flagging whenever their output contains more than one speaker ID. But they are optimized to segment every acoustically distinct speaker, whereas our detector should trigger only when a change warrants intervention. A person speaking on a television is therefore a correct diarization event but a harmful false trigger for the agent.
This objective mismatch creates false triggers even when the acoustic segmentation is correct. Separately, these models also have high FPR on literal speaker-change detection, even on clean synthetic data; turn-level errors then compound at conversation level on production calls.
Speaker embeddings
Unlike a diarizer, speaker embeddings like
TitaNet
offer lower-level building blocks: it maps variable-length audio to an embedding space rather than directly identifying speakers or deciding who spoke when. It’s trained with an additive angular-margin (AAM) loss function that optimizes the embedding space for cosine comparison, so utterances from the same speaker should point in similar directions.
Fig. 2 — TitaNet Architecture
To turn embeddings into a speaker-change score, we split audio into overlapping windows and compare them with cosine similarity. We evaluated three methodologies:
Approach
How it works
Where it works well
Where it fails
Mean dissimilarity
Average the cosine distance across every pair of windows.
A sustained or recurring second speaker creates many dissimilar cross-speaker pairs, so the evidence accumulates even if that speaker comes and goes.
A short intrusion contributes few dissimilar pairs. As same-speaker context grows, those pairs are diluted by the much larger number of similar pairs.
Maxsplit
Test every chronological boundary, compare the centroids before and after it, and keep the largest distance.
In a clean A→B handoff, each side is dominated by one speaker, producing strongly separated centroids without averaging over every pair in the call.
In an A→B→A pattern, no single boundary separates the speakers: at least one centroid mixes A and B, shrinking the score.
Graph methods
Represent windows as nodes and their similarities as weighted edges, then look for multiple well-connected clusters.
Because clustering does not assume one chronological boundary, all windows from a recurring or interleaved speaker can still form one group.
Consistent non-speaker variation—such as silence, a channel shift, or a change in intonation—can form a separate cluster that looks like another speaker.
These methodologies are cheap, fast, and outperform off-the-shelf diarization. They can be tuned for high recall, but their scores capture acoustic separability rather than relevance, so precision remains insufficient for a final decision. That makes them useful as an acoustic gate: we discard low-scoring candidates, then let a multimodal model judge whether the remaining changes are relevant.
Multimodal post-training
Multimodal LLMs combine audio comprehension with reasoning and holistic understanding. These models do not perform well on this task out-of-the-box, and prompting and in-context learning mostly move them along the cFPR-recall Pareto frontier, not past it. To improve performance, we focus on post-training these models.
Synthetic dataset generation
Post-training data must cover the conditions that drive production errors: conversation length and turn structure, background noise, and speaker variation. We considered three sources, each trading off acoustic realism, semantic coherence, distribution control, and scale:
Human-recorded conversations
provide the most natural voices and interaction patterns, but recording and review are slow and expensive. They are also difficult to balance across production conditions—especially less common combinations of age, accent, pitch, prosody, and timbre.
Spliced speech corpora
, such as
LibriSpeech
and
VCTK
, preserve real voices and make it easy to control turn counts, durations, and noise at scale. But their utterances were typically read in isolation, so the resulting exchanges lack conversational and semantic coherence.
LLM-generated conversations rendered with TTS
provide coherent scenarios, precise semantic control, and scalable coverage of the production distribution. Their weakness is acoustic fidelity: cloned voices do not reproduce the full variation in human prosody, timbre, and other fine-grained vocal cues.
Fig. 3 — Tradeoffs between various synthetic dataset generation methods
In our SFT experiments evaluated on production conversations, adding training data improved AUC: the model ranked relevant changes above irrelevant ones more reliably overall. But higher AUC did not necessarily improve the low-cFPR tail, where a small number of difficult false positives determines production performance.
In deployment, a speaker-embedding gate filters out low-scoring candidates before they reach the LLM.
The training curriculum should therefore target the cases that survive this gate—especially irrelevant changes with high embedding scores, alongside subtle relevant changes—and match their production conditions as closely as possible.
Supervised fine-tuning from first principles
At inference, the model produces a yes/no answer, but its token log-probabilities provide a continuous score. Thresholding the yes/no log-odds lets us choose the recall–cFPR operating point.
The objective follows naturally from these log-odds. For request
, let
be the model’s log-odds of answering yes rather than no, and let
be the corresponding probability after conditioning on the valid yes/no choices:
This normalization ignores any residual probability assigned to other tokens; with a constrained yes/no response format, that mass is typically negligible.
For a conversation
, let
contain every request (which consists of all the audio recorded up until a given moment in time) that does not contain a speaker change. If the conversation contains a relevant speaker change, let
denote the single recall-relevant request at which it should be detected. A negative conversation is correct only if nothing in
fires, a positive conversation is correct only if nothing in
fires and
does. Therefore:
Taking the negative log of the conversation-level probability gives:
Assign target
to every request in
and
to the single recall request. If
for a negative conversation and
for a positive one, then:
Under this factorization, the conversation-level negative log-likelihood decomposes into binary cross-entropy on the normalized yes/no probabilities. This is effectively standard maximum-likelihood SFT. The gradients make the equivalence explicit:
These gradients push every specificity request toward no and the single recall request toward yes using ordinary cross-entropy. Paired with log-odds thresholding, SFT directly optimizes the scores used at deployment. On production conversations, SFT with a TitaNet cohesion gate achieved three times the recall of diarization models at 1% cFPR.
DPO is another option, but it underperformed SFT in our experiments. DPO optimizes a relative preference margin rather than the calibrated yes/no likelihood used at a fixed deployment threshold. Binary cross-entropy is better aligned with this objective: its updates scale with probability error, concentrating the largest corrections on confident mistakes.
Future of audio models
Many general-purpose audio-language models still use representations and objectives optimized for transcription or response generation, which can discard evidence needed for acoustic reasoning. This limitation is not universal:
TitaNet
,
WavLM
,
CLAP
, and
BEATs
are explicitly trained to preserve speaker or broader acoustic information.
However, there are still several major gaps in today’s audio models. Semantic tokens are compact but often remove fine acoustic detail; codec tokens preserve more of the waveform but produce much longer sequences. Preserving the signal is only half the problem: models must also be trained to use evidence across timescales, from timbre and intonation to rhythm and harmony.
What is missing is an audio-native analogue of
InstructGPT
: information-preserving representations, a broad curriculum of audio-native tasks, and evaluations that require answers to be grounded in the waveform. Models such as
Qwen3-Omni
move in this direction, but broad, reliable audio reasoning remains an open problem.
At 1% cFPR, a TitaNet cohesion gate improved recall by 50% over a Sortformer gate when paired with the same post-trained LLM; TitaNet also performed better as a standalone detector.
Alan Ragoler
—
Research Intern
Dante Everart
—
Speech AI Researcher
“With Decagon Voice, we’re able to combine high performance and seamless brand customization with cross-channel memory, ensuring every interaction is connected and true to Chime’s member-first values.”
Janelle Sallenave
Chief Operating Officer
Start improving your workflow with Decagon
With Decagon, CX teams don’t have to guess whether a change will improve CSAT or deflection. They can move quickly, measure what matters, and act on what works.
Get a demo
Your browser does not support the video tag.
Join us
There are very few places where you can prototype with frontier LLMs, ship to production in days, and watch users engage with the systems you built—all while owning the entire stack, from intent parsing and tool usage to API integration and observability. This role at Decagon is one of those places.
From my own experience working across both agent development and broader engineering initiatives at Decagon, I’ve seen firsthand how uniquely impactful this work can be. Whether I’m building intelligent workflows for customers or designing infrastructure that supports our agent platform, it’s rare to find an environment where the work transitions from concept to production within days, actively powering user experiences and transforming how businesses operate.
If you’re looking for a role where you can:
Build at the frontier of LLMs, automation, and user interaction
Deploy AI agents that solve high-value business use cases across industries including retail, travel and hospitality, fintech, edtech, and more
Work directly with customers on high-impact use cases
Ship fast, iterate constantly, and own your work from idea to production
Join a fast-moving, collaborative team solving real-world challenges with AI
We’d love to hear from you!
Explore careers
Related posts
Research & Technology
How we made one of our largest inference workloads 4.7× more GPU-efficient
Posted on
September 3, 2026
Research & Technology
Scaling real-time text-to-speech inference
Posted on
August 20, 2026
Research & Technology
Teaching flow-matching text-to-speech models with RL
Posted on
August 18, 2026
Explore more topics
AI agent building
Test & experimentation
Analytics & Voice of Customer
Voice & omnichannel support
Guardrails, security, & governance
Use cases & experiences
Workplace
The AI concierge for every customer.
Get a demo
Footer
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
