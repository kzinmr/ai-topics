---
title: "Teaching flow-matching text-to-speech models with RL"
source: "Decagon Blog"
url: "https://decagon.ai/blog/teaching-flow-matching-tts-with-rl"
scraped: "2026-08-19T06:00:01.367914+00:00"
lastmod: "None"
type: "sitemap"
---

# Teaching flow-matching text-to-speech models with RL

**Source**: [https://decagon.ai/blog/teaching-flow-matching-tts-with-rl](https://decagon.ai/blog/teaching-flow-matching-tts-with-rl)

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
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Security
Sign in
Get a demo
Sign in
Get a demo
Research & Technology
Teaching flow-matching text-to-speech models with RL
Posted on
August 18, 2026
Cyrus Asgari
Member of Technical Staff, Research
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
Good demos, unreliable distributions
Modern text-to-speech (TTS) systems can sound remarkably natural. But average quality hides the failures that matter most: a rushed sentence, misplaced pause, or flattened intonation can dominate a listener's impression of an otherwise convincing interaction.
The goal of post-training TTS models is not to just achieve a better average sample, but a tighter distribution: fewer tail failures, no leakage onto ordinary prompts, and no loss of intelligibility, speaker identity, or naturalness.
Supervised fine-tuning is the foundation. It teaches a model what a behavior looks like and is useful when that behavior is absent. But once the model can produce several plausible generations, the remaining problem is comparative. Which generation has the right pace, pause, intonation, or expressive event?
We study two settings: control tags—inline cues such as [cough], [pause], and [slow] that request specific behaviors—and naturalness optimization.
Fig. 1 — Post-training improves the full output distribution, not only the average sample.
Choosing the right signal, and why flow models complicate it
The right training method depends on where the learning signal comes from:
Signal
Method
Use when
The behavior rarely appears
SFT
Teach the behavior before optimizing it
A reward can rank samples
RAFT
Select the best samples without policy probabilities
Clean better/worse pairs are available
DPO
Learn directly from contrasts
A dense, validated reward is available
GRPO
Optimize online for larger policy changes
‍
Applying DPO and GRPO to modern speech models requires resolving a basic mismatch. Flow-matching models generate speech by learning how to continuously transform noise into audio. Once the initial noise is chosen, generation follows a deterministic trajectory rather than a sequence of sampled actions with explicit probabilities.
Fig. 2 — The probability mismatch that motivates Flow-DPO and Flow-GRPO.
A token model samples discrete outputs from an explicit distribution, so each choice has a log-probability. A flow-matching model instead transforms noise into audio through a learned velocity field:
Here,
is the evolving audio representation,
is its position along the flow trajectory,
contains the text and speaker conditioning, and
is the model's learned velocity field. This process is described by an ordinary differential equation (ODE): at each point, the velocity field specifies how the audio representation should change. Once the initial noise is fixed, following the ODE produces a deterministic trajectory.
An autoregressive backbone conditions a flow head that generates the next latent audio patch. Each transition is a deterministic update, not distribution-sampled action. That leaves DPO without a policy-versus-reference score and GRPO without old and current action log-probabilities.
Our first workaround was Reward-rAnked Fine-Tuning (RAFT) which avoids log-probabilities by sampling several takes, ranking them by reward, and fine-tuning on the winners. It improved cough reliability, but the result did not generalize cleanly across controls. Pause RAFT either over-paused or traded firing for consistency, while prosody remained near the supervised fine-tuning ceiling.
That limitation motivated Flow-DPO and Flow-GRPO.
Flow-DPO: preferences without exact audio likelihoods
For a token policy, DPO increases the policy-versus-reference margin of a preferred output
over a rejected output
. A flow model does not expose exact waveform likelihoods, but it can measure how well its velocity field fits a supplied audio trajectory.
For a clean latent patch
, Gaussian noise
, and sampled flow time
, we construct a noisy intermediate latent
and its target velocity
:
The standard flow-matching loss
averages this velocity error across audio patches
, sampled flow times
, and noise draws
, using each patch's conditioning
:
We replace the unavailable policy-versus-reference log-probability gain with a negative relative flow loss
[2]
:
Here,
is the policy being trained and
is the frozen reference. Defining their loss difference as
gives:
Minimizing
pushes the preferred output
toward a lower policy-versus-reference loss difference
than the rejected output
. The logistic function
turns that margin into the training loss, while
controls its strength. To reduce variance, the policy and reference reuse the same flow times and noise. Winner-side flow and stop-head anchors preserve reconstruction and termination.
Flow loss is not an exact waveform likelihood, and it only provides the relative signal DPO needs to separate preferred and rejected trajectories.
That separation depends on clean pairs. In our first Flow-DPO experiment for the [cough] control tag, many rejected samples still contained real coughs, so voice and intelligibility differences carried the preference signal instead of the event itself. We rebuilt the dataset around same-prompt contrasts that isolated the cough, then filtered preferred samples for intelligibility, speaker consistency, and artifacts.
Flow-GRPO: creating probabilities inside a deterministic flow
GRPO converts rewards for several rollouts from the same prompt into group-relative advantages. Token models apply those advantages through old and current action log-probabilities, but deterministic flows have no equivalent transition probability.
Flow-GRPO
[3]
converts the deterministic ODE into a stochastic differential equation (SDE) by adding Gaussian noise at selected steps, giving each transition a probability. But noise alone would change the model's distribution. To correct for that change, we estimate the score from the velocity field:
The score
points toward higher-density intermediate latents. We use it to offset the distributional change introduced by the noise via a score correction:
Here,
controls the noise level,
is the integration step, and
is Brownian noise. Over one step, the corrected drift defines the expected next latent
, giving the Gaussian transition:
where
is the sampled next latent,
denotes a Gaussian distribution, and
is the identity matrix; the covariance is
.
Fig. 3 — How Flow-GRPO creates the transition probabilities needed for training.
During rollout, the policy samples
. During training, that action stays fixed while the updated policy recomputes
, moving the mean toward transitions from higher-reward utterances and away from lower-reward ones. We apply this stochastic treatment to selected flow steps across the utterance, broadcast the utterance-level advantage to them, and optimize a clipped policy objective with fixed-reference KL.
Training only the flow head is a cheap way to validate the method, but it limits how far the policy can move. We unfreeze the autoregressive backbone only after teacher-forced conditioning matches rollout conditioning, with fixed-reference KL and held-out evaluation as guardrails. In our runs, the two conditioning paths reached a cosine similarity of about 0.998, clearing the alignment check before full-model training.
Reward design: targets, shortcuts, and constraints
A control-tag reward has three jobs: produce the requested behavior, suppress it when unrequested, and preserve the surrounding speech.
Pause control showed how easily those goals can conflict. Because our reward penalized unwanted pauses and word errors more heavily than missed requested pauses, the policy learned to pause less everywhere. Mean reward improved by 35% even as requested-pause success fell from roughly 50% to 29.2%. The optimizer was working as intended; the objective was not.
The same pattern can appear across speech controls:
An event reward can increase requested activations while also increasing leakage onto ordinary prompts or changing the speaker's voice.
A pacing reward can be satisfied through silence or warbling rather than slower articulation.
A naturalness reward can be over-optimized until the voice drifts from the reference.
To prevent these shortcuts, we separate the target behavior from the properties that must be preserved:
Negative controls
cover prompts where the behavior should not occur.
Preservation gates
reject unintelligible, off-speaker, or artifact-heavy samples regardless of reward.
Reference anchors
limit broad drift from the starting policy.
Two-sided targets
optimize toward a validated range rather than maximizing a proxy without bound.
Held-out evaluation
tracks component metrics and blind listening, not only the training reward.
Naturalness was harder because no single metric captured it reliably. Rollout consistency worked well for finding unusually bad takes and constructing DPO pairs, but optimizing agreement with the model's own outputs risked rewarding bland, mode-seeking speech. Our most stable Flow-GRPO runs instead used an externally grounded reward
[7]
combining speaker similarity, ASR accuracy, and DNSMOS
[16]
quality.
Results: the method follows the feedback
Across coughs, pauses, and pace, the same methods behaved differently depending on how well the feedback captured the target behavior and its preservation constraints.
Behavior
Method / setup
Outcome
Commanded cough
RAFT · 3 rounds
Reliable firing
Cough success: ~79% → ~98%
Commanded cough
Flow-DPO · clean contrast pairs
Reliable, controlled firing
Cough success: 79% → 98.2%
Commanded cough
Flow-GRPO · initialized from SFT
Improved, but over-optimized
Cough success: 79% → 94.0–96.4%
Leakage ↑ · speaker similarity ↓
Slow prosody
RAFT · rejection sampling
Plateaued near SFT
Slow/neutral rate ratio: 0.91–0.92
Slow prosody
Flow-GRPO · full model
Strong pace improvement
Rate ratio: 0.908 → 0.815
(lower is slower)
‍
Naturalness proved harder to optimize. Flow-GRPO with the speaker-similarity, ASR, and DNSMOS reward produced more consistent high-quality generations and eliminated the tail failures seen in the baseline.
Across these experiments, two patterns stood out:
First,
Flow-DPO is robust when clean contrasts exist
. Pair purity and clean-prompt controls made the conditional behavior explicit. On coughs, Flow-DPO delivered strong, stable performance across target and preservation metrics, while GRPO over-optimized the reward, producing overly aggressive events, increased leakage, and lower speaker similarity.
Second,
Flow-GRPO enables larger policy movement
. That helped on pace, where the reward directly measured articulation rate and intelligibility was gated. The difference was reward quality: stronger optimization helped when the reward matched the intended behavior and hurt when it did not.
From speech models to voice agents
The goal extends beyond better TTS: it is a voice agent whose words, timing, prosody, and nonverbal behavior work together as a coherent policy. At Decagon, we're pursuing this by optimizing language and acoustics to improve naturalness without sacrificing reliability.
References
Flow matching and continuous-model alignment
[1] RAFT — Reward rAnked FineTuning for Generative Foundation Model Alignment.
arxiv.org/abs/2304.06767
[2] ARDM-DPO — Direct Preference Optimization for Speech Autoregressive Diffusion Models.
arxiv.org/abs/2509.18928
[3] Flow-GRPO.
arxiv.org/abs/2505.05470
[4] MAR-GRPO — GRPO for masked-autoregressive models with diffusion heads.
arxiv.org/abs/2604.06966
·
Code
[5] Diffusion-DPO.
arxiv.org/abs/2311.12908
[6] DanceGRPO.
arxiv.org/abs/2505.07818
·
Code
TTS and audio post-training
[7] Qwen 3.0.
arxiv.org/abs/2607.23938
[8] FlowTTS-GRPO.
arxiv.org/abs/2606.23190
[9] F5R-TTS.
arxiv.org/abs/2504.02407
[10] DMOSpeech 2.
arxiv.org/abs/2507.14988
·
Code
[11] Seed-TTS.
arxiv.org/abs/2406.02430
Reward design and evaluation
[12] No Verifiable Reward for Prosody.
arxiv.org/abs/2509.18531
[13] SpeechJudge.
arxiv.org/abs/2511.07931
[14] Attacking UTMOS.
arxiv.org/abs/2606.31105
[15] Align2Speak.
arxiv.org/abs/2509.21718
[16] DNSMOS.
arxiv.org/abs/2010.15258
Cyrus Asgari
—
Member of Technical Staff, Research
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
How we debugged a latent PgBouncer bug across four layers of the stack
Posted on
August 5, 2026
Research & Technology
What an air-gapped AI deployment actually requires
Posted on
July 9, 2026
Research & Technology
DuetBench: An evaluation of self-improving customer service agents
Posted on
June 9, 2026
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
