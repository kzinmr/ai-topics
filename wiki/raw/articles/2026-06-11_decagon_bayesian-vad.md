---
title: "Bayesian VAD: Fixing turn detection in production voice pipelines"
source: "Decagon Blog"
url: "https://decagon.ai/blog/bayesian-vad"
scraped: "2026-06-11T06:00:21.340739+00:00"
lastmod: "None"
type: "sitemap"
---

# Bayesian VAD: Fixing turn detection in production voice pipelines

**Source**: [https://decagon.ai/blog/bayesian-vad](https://decagon.ai/blog/bayesian-vad)

Introducing Duet Autopilot.
Learn more
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
Product Update
Company news
Technology & research
Industry
Technology & Research
Blog
/
Bayesian VAD: Fixing turn detection in production voice pipelines
Bayesian VAD: Fixing turn detection in production voice pipelines
March 24, 2026
Written by
Dante Everart
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
When a voice AI agent cuts a customer off mid-sentence, the interaction feels dismissive and erodes the trust that enterprise deployments depend on.
Most voice AI agents run on a cascade pipeline: speech-to-text (STT), agent logic, then text-to-speech (TTS). Each stage inherits the errors of the last, which makes detecting when someone is done speaking and reliably converting it to text particularly consequential.
The problem is especially acute in customer support. Callers call in from noisy environments, switch between languages mid-conversation, and rarely speak in well-punctuated sentences. The pipeline has to handle all of it.
The typical speech-to-text path looks like this:
Voice Activity Detection (VAD)
estimates the probability of speech occurring in each audio frame.
Turn detection
estimates the probability of the user is actually done talking.
Automatic Speech Recognition (ASR)
transcribes the accumulated audio to text.
After analyzing production audio at scale, we found that premature turn endings (i.e., the agent jumping in before the user is done) account for the majority of VAD-based errors. We discovered two root causes: the underlying probabilities are poorly calibrated for real-world audio, and thresholding individual frames is simply the wrong tool for making turn decisions.
We developed novel statistical methods to solve each without retaining any models. The result was 42% fewer broken turns and a 20% reduction in transcription error.
Measuring STT
Before fixing anything, we needed to measure the right things. STT has two jobs:
detect
user turns and
transcribe
them. A user turn is a complete start-of-speech to end-of-thought segment spoken by the user. Each requires its own ground-truth and metrics.
Detection metrics
Three things matter for turn detection:
Did we find the right boundaries (i.e., the start and end timestamps of the turn)?
Did we accidentally split a single turn into multiple segments?
How quickly did we commit to a decision?
Metric
Definition
Why it’s important
Boundary precision and recall
Precision:
Of the detected turn boundaries, how many are correct?
Recall:
Of the true turns, how many did we capture?
Misplaced boundaries mean the agent responds to incomplete input
Break rate
% of ground-truth turns incorrectly split into multiple segments
Every break is a moment a customer gets cut off mid-sentence
Expected breaks per turn
Average number of breaks across all turns and conversations
Break rate masks the extent of fragmentation for a turn; this catches it
Turn commit latency
Time from true turn end to the system committing that the turn is over
Too slow and the agent feels sluggish, but reducing latency at the cost of accuracy just trades one bad experience for another
Transcription metrics
The industry standard for transcription quality is Word Error Rate (WER), but standard practice has a blind spot. It feeds clean, ground-truth audio segments directly to ASR and reports WER on those. This hides detection errors entirely. If the system only captured half a turn, a perfect transcription still looks like 50% accuracy to the user.
To address that gap, we developed
Pipeline WER
, a conversation-level metric that includes fragmented and missed turns. It uses a simple sentinel decomposition approach that we prove is equivalent to the theoretically correct per-turn WER (see Appendix).
We determine the right sample size for these metrics by computing an incremental stability statistic over the data. (see Appendix).
Turn-taking problems
So where do the premature turn endings come from?
VAD models are extremely responsive and handle speech start just fine. The failures are entirely on the end-of-turn side and trace back to two structural issues.
Problem 1: Miscalibrated probabilities
Off-the-shelf VAD models are trained on clean speech corpora. Deploy them on real-world audio (e.g., noisy environments, accented speech, cross-talk) and the probabilities they output are wrong.
We measured roughly 20 percentage points of average calibration error. For example, a model-reported 20%
actually corresponded to a true probability closer to 40%. Every downstream threshold is operating on a distorted probability space.
Calibration curve: predicted vs actual probability. The model should follow the diagonal (black line), instead it's the blue line.
Probability distribution before calibration. Probability mass is concentrated at extremes (0.1 and 0.9), leaving little usable dynamic range.
Fixing calibration: Isotonic regression
To remap model outputs to true probabilities, we applied isotonic regression — a technique that fits a monotone mapping from predicted to observed probabilities:
Optimized via the Pool Adjacent Violators Algorithm (PAVA), the results are striking:
Calibration curve after isotonic regression. Now near-perfectly on the diagonal. Calibration error drops from ~20pp to ~0.4pp.
Probability distribution after calibration. Probability mass is evenly distributed, giving meaningful dynamic range.
Plotting raw (purple) versus post-isotonic (cyan) probabilities on a sample conversation shows the difference clearly. Probabilities are now meaningful, but the sharp dips remain:
Raw vs calibrated VAD probabilities
Calibration alone gains 1–2pp in turn boundary precision/recall since we can more easily find the optimal threshold, but the fundamental issue of reacting to individual frames is still unresolved. That’s the second structural issue.
Problem 2. Wrong decision framework
Even with well-calibrated probabilities, the standard approach to turn detection is fundamentally flawed.
The typical method relies on two heuristics: threshold a single VAD frame to detect silence, then wait a fixed timeout before committing to a turn end. The problem is that VAD outputs are inherently noisy: plosives, breaths, and natural inter-word pauses all produce momentary dips in the speech probability signal. Every dip is an opportunity for a false turn ending.
Per-frame thresholding is asking the wrong question. Instead of
"is speech absent right now?"
, the right question is:
"given everything observed so far, is there enough accumulated evidence that the speaker is actually done?"
Bayesian hazard statistic
To answer that question, we developed a new decision statistic that replaces both heuristics with a single learned statistic, cutting broken turns by 42%. The construction has two steps.
Step 1: Define “Evidence of silence”
Let
be VAD probability of speech, so
is the probability of silence. We define the
evidence of silence
as the elapsed time multiplied by the probability each moment was silence:
This is a change of measure constructed via the Radon–Nikodym theorem: it warps wall-clock time
by the probability of silence,
, to create a new "silence-centric" time scale
. Practically, it means brief dips during speech barely register: a 100ms pause where
contributes only 50ms of silence evidence. Sustained, confident silence accumulates quickly; hesitations and breath sounds do not.
Silence evidence accumulation diagram
Step 2: Define “evidence speaker is done”
Knowing how much silence has accumulated isn't enough on its own. We also need to find the rate at which turns actually end given a level of accumulated silence evidence. This is a
hazard function
:
At short
→ hazard is low since most within-turn gaps last long enough to accumulate more silence evidence. At large
→ hazard rises sharply since very few natural pauses persist that long.
The cumulative hazard over silence evidence gives the
total evidence of a true turn end given silence evidence so far
— the decision statistic we actually want to threshold on.
This replaces the fixed timeout and threshold heuristic with a single, learned statistic. Momentary dips have to accumulate enough
to matter and land in a region where
is high. Only sustained silence evidence drives
past threshold, which is exactly when a turn has actually ended.
Effect on the signal
Plotting all three signals on the same conversation makes the improvement visible. The raw VAD probabilities (purple) are jagged and reactive. Post-isotonic regression (blue) is better calibrated but still noisy. The Bayesian hazard statistic (green) smooths out the within-speech dips and responds decisively to genuine silence:
Comparison of raw, calibrated, and bayesian-smoothed signals.
Results
We found isotonic calibration and the hazard statistic improved every metric across the board. Because the hazard statistic is a proper evidence-accumulation framework, it also gives us a smooth, theoretically grounded tradeoff between decision latency and accuracy.
All graphs swept over
Turn detection accuracy
43% improvement
in turn boundary precision
14% improvement
in turn boundary recall
Turn detection results
Turn breaks
42% reduction
in broken turn rate
44% reduction
in expected breaks per turn
Turn break comparison
Pipeline WER
20% reduction
in pipeline WER
WER results
Latency–accuracy tradeoff
A nice side effect of collapsing both the threshold and timeout into a single statistic
is that you get a clean knob that directly trades off decision latency for accuracy.
None of this required retraining a model or changing any architecture. The gains came entirely from fixing calibration and replacing a broken decision heuristic with one grounded in the right statistical framework.
The lesson generalizes. Before reaching for a better model, it's worth asking whether the framework around the model is sound.
Appendix
Pipeline WER
The industry-standard WER is the edit (Levenshtein) distance between ASR hypothesis
and reference
, normalized by reference length.
Pipeline WER
extends this to the full conversation, including fragmented and missed turns.
Computing it normally requires matching detected segments back to ground-truth turns, which gets messy when boundaries are wrong, so we developed a sentinel decomposition: insert unique tokens
between turns in both strings based on true timestamps, then compute a single WER over the full concatenation. The sentinels force edit distance to respect turn boundaries automatically, and we prove this is exactly equivalent to the theoretically correct per-turn sum.
Proof
Setup.
Let
be the word vocabulary. For each turn
, let
be the reference and hypothesis word sequences. Let
denote standard Levenshtein distance. Introduce
unique sentinel tokens
with
and each
distinct. Define:
We show
by proving both
and
.
Upper bound.
For each turn
, take an optimal edit transformation
costing
. Concatenating these transformations (leaving every sentinel untouched) is a valid transformation
with total cost
. Since
is the minimum over all transformations,
.
Lower bound.
Each sentinel
appears exactly once in
and once in
, and no sentinel is in
. Deleting a sentinel costs 1 and reinserting it costs 1 (total
), while matching it in place costs 0. So every optimal alignment must match all sentinels. Matched sentinels are order-preserving, partitioning the alignment into
independent regions where
must map to
. Each region costs
, so
.
Combining
both bounds:
. ∎
Metric Stability
It's important to know how many samples we need to draw reasonable conclusions from any metrics. One such way is to compute an
incremental stability statistic
. If we compute each metric
over an incrementally growing dataset, adding conversations in batches of
, then the statistic:
measures the stability at
. Choosing a stability threshold
(e.g., <1pp), the smallest
where
for all subsequent
gives confidence that metric changes
are meaningful with at least
samples.
Recent posts
Introducing Duet Autopilot: The self-improving agent for conversational AI
Today, we're announcing Duet Autopilot, the next evolution of Duet that allows your Decagon agent to self improve.
DuetBench: An evaluation of self-improving customer service agents
DuetBench is the first benchmark in the customer service domain designed to evaluate agent self-improvement.
From Technical Account Management to Agent Strategy: Why I joined Decagon
The best way I can describe the role is that you get to be two things at once: a strategic advisor and a technical lead.
Deliver the concierge experiences your customers deserve
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
