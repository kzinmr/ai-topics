---
title: "Speaker diarization: What is it, how it works, and use cases"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/what-is-speaker-diarization"
scraped: "2026-08-26T06:00:57.232537+00:00"
lastmod: "2026-08-25T14:12:45.593Z"
type: "sitemap"
---

# Speaker diarization: What is it, how it works, and use cases

**Source**: [https://elevenlabs.io/blog/what-is-speaker-diarization](https://elevenlabs.io/blog/what-is-speaker-diarization)

Blog
Resources
What is speaker diarization? How it works and use cases
Written by
Jack
Limebear
Published
Aug 25, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Learn more
Get API key
On this page
Introduction
Summary
What is speaker diarization, and how does it work?
Key differences between speaker segmentation and speaker identification
Popular open source speaker diarization tools and libraries
Real-time diarization: Challenges and use cases
How to evaluate speaker diarization performance
Get started with ElevenAPI for speaker diarization
FAQ
Speaker diarization takes an audio stream with an unknown number of speakers and produces a timeline of labeled segments: speaker A from 0:00 to 0:42, speaker B from 0:42 to 1:15, speaker A again from 1:15 onward. The system does not know who the speakers are, but it knows they are different people, and it keeps their labels consistent throughout the recording.
This process is what makes multi-speaker audio usable. Meeting notes,
call center
analytics, interview transcriptions, podcast editing, and legal records all depend on knowing not just what was said but also who said it.
This guide explains how diarization works, how it differs from related techniques like segmentation and identification, which open source tools handle it, and how to measure whether a diarization system is performing well.
Create your API key for in-app diarization
Get API key
Summary
Speaker diarization segments an audio recording by who is talking, producing labeled speaker turns without identifying anyone by name.
Speaker diarization differs from speaker segmentation, which finds when speakers change, and speaker identification, which matches voices to real names.
Diarization performance is measured with diarization error rate (DER) for overall accuracy and Jaccard error rate (JER) to check that accuracy holds across every speaker.
What is speaker diarization, and how does it work?
Speaker diarization is the process of partitioning an audio stream into segments according to who is speaking. A transcript with speaker diarization labels each segment of audio with a speaker identity. Simply put, it answers the question "Who spoke when?"
A raw transcript of a meeting gives you the words, while a diarized transcript tells you that speaker 1 asked the question, speaker 2 answered it, and speaker 3 interrupted halfway through.
Most speaker diarization systems follow a pipeline with four stages:
Let’s break these stages down in more detail.
Voice activity detection (VAD)
Voice activity detection separates speech from everything else: silence, background noise,
music
, or keyboard clicks. Only the audio segments containing actual speech move to the next stage.
If there are any errors at this stage, they’ll propagate throughout the rest of the stages.
Segmentation
Those speech-containing segments are then divided at points where the speaker is likely to change, for example, a shift in vocal tone, a pause between turns, or a change in pitch pattern. Most systems detect these change points directly by comparing the acoustic characteristics on either side of a candidate boundary.
Some segmentation tools cut audio into short uniform windows, such as two-second chunks, then rely on the clustering stage to merge adjacent windows that belong to the same speaker.
Embedding extraction
Each speech segment is converted into a speaker embedding, or a numerical vector that captures the vocal characteristics of whoever is speaking in that segment. Embeddings from the same speaker cluster close together in vector space, while embeddings from different speakers sit farther apart.
Clustering
The embeddings are then grouped so that segments from the same speaker share a label. The system typically does not know the number of speakers in advance, so the clustering algorithm has to infer it, deciding whether that slightly different-sounding segment is a new speaker or the same person speaking with a different tone.
The output is a set of speaker labels attached to time ranges, usually paired with a transcript. For example, a diarized transcript from a two-person call looks like:
[speaker_0]
Thanks for calling. How can I help?
[speaker_1]
Hi, I'm calling about my invoice from last month.
[speaker_0]
Sure, let me pull that up.
The labels are anonymous and internally consistent. Speaker_0 is the same voice every time it appears, but the system does not know that speaker_0 is named Fergal. Attaching real identities is a different task, which we cover below.
Key differences between speaker segmentation and speaker identification
Speaker segmentation and speaker identification both closely overlap with diarization, meaning that the three are often conflated with one another.
Each of them solves a slightly different problem, so understanding the distinction important when assessing tooling.
As we explained earlier, speaker segmentation is a step within diarization that occurs early in the pipeline. It finds the boundaries where the speaker changes from one voice to another, all without assigning labels. Segmentation tells you that a change happened at 0:42. Diarization builds on that by grouping the resulting segments and producing a fully labeled output, letting you know the voice at 1:15 is the same one that spoke at the start of the recording.
Speaker identification is a separate capability outside of diarization but is frequently combined with it. Identification determines who those speakers actually are. An identification system compares voices against enrolled voiceprints, using a reference of known speakers to return identities. After identification, speaker_0 and speaker_1 become "Fergal" and "Eric."
Many products combine these tools to produce a more comprehensive final transcript. A meeting tool might do this automatically (potentially even pulling from strings like the name someone has set on Teams or Meet) so that every attendee's contributions are attributed by name without any manual review.
Popular open source speaker diarization tools and libraries
Open source speaker diarization tools are worth considering when you need control, flexibility, or local deployment. The best choice depends on the kind of audio you handle (phone calls, meetings, podcasts, broadcast), your latency requirements, and how much engineering time you can invest.
Here are some of the most popular options.
Pyannote.audio
Pyannote.audio
is a PyTorch-based toolkit built specifically for speaker diarization and one of the most commonly used open-source options. It provides pretrained pipelines covering the full diarization stack, including VAD, segmentation, embeddings, and clustering, along with the building blocks to train or fine-tune models on your own data.
Its pretrained models are distributed through Hugging Face and are commonly used as the diarization layer in larger transcription projects.
WhisperX
WhisperX
combines OpenAI's Whisper transcription with diarization and forced alignment. Whisper by itself produces strong transcripts, but it does not assign speaker labels, and its timestamps are only approximate. WhisperX adds word-level timestamp alignment and integrates pyannote-based diarization, producing transcripts where each word carries both an accurate timestamp and a speaker label.
NVIDIA NeMo
NVIDIA NeMo
includes diarization as part of its broader
conversational AI
framework. It provides trainable diarization models, including end-to-end approaches that handle overlapping speech, and is designed for teams building custom speech systems at scale on GPU infrastructure.
Each of these tools requires you to manage the diarization infrastructure, including model deployment, scaling, monitoring, and updates. For teams that do not want that operational overhead, managed speech diarization APIs provide a simpler alternative. They can either integrate with existing workflows or handle the entire diarization pipeline, making them well-suited for production use cases, such as
customer support
analytics, meeting transcription, and podcast processing.
Real-time diarization: Challenges and use cases
Real-time diarization is substantially harder than diarization on a finished recording because the system has to make decisions with incomplete context.
An offline system sees the entire recording before it commits to anything. It can compare a voice at minute 2 against a voice at minute 40 and confidently decide they're the same speaker, because it has both moments available at once. A real-time system never gets that luxury, as it has to label speech the instant it arrives, with no access to what's said next and little or no chance to revise a decision once it's made.
That missing future context is what makes three specific problems so much harder to solve in real time:
Latency vs. accuracy:
Without the ability to look back and forth across the whole conversation, meeting tighter response-time budgets comes directly at the expense of accuracy.
Overlapping speech:
When people talk over each other, a system that could reprocess the audio might untangle it. A real-time system has to force it into a single label or lean on specialized overlap-aware models on the fly.
Short utterances:
A quick "yes" or "go ahead" barely gives the system enough voice to work with and, without surrounding context to lean on, it still has to commit to a label immediately.
Despite the difficulty, some applications cannot wait for a recording to finish.
Live captioning
for meetings and broadcasts needs speaker labels as people speak.
Contact center software
that surfaces guidance to
agents
mid-call needs to know which words the customer is using in real time.
Voice agents
handling calls with multiple participants need to track who is asking what without delay. In each case, a system that is slightly less accurate but immediate beats one that is more accurate but delayed.
For workloads that do not genuinely require real-time labels, such as analytics, compliance review, and transcript generation, batch diarization remains the better choice because it is significantly more accurate.
How to evaluate speaker diarization performance
Two metrics matter most when you are measuring diarization accuracy: diarization error rate (DER), which captures overall accuracy, and Jaccard error rate (JER), which checks whether that accuracy holds up for every speaker.
DER specifically calculates the fraction of total speech time that is attributed incorrectly. It combines three error types:
False alarm speech:
The system labeled a segment as speech when no one was speaking.
Missed speech:
Someone was speaking, but the system labeled it as silence.
Speaker confusion:
Speech was detected but attributed to the wrong speaker.
DER = (false alarm + missed speech + speaker confusion) / total speech duration
A DER of 10% means errors equal to one-tenth of the total speech time, across those three types. Lower is better, and scores are only comparable when measured on the same data under the same conditions. DER varies enormously with audio quality, speaker count, and how much overlap the recording contains.
Jaccard error rate (JER) measures diarization accuracy for each speaker separately, then averages the result across all speakers. For each reference speaker, the evaluator matches the system’s closest speaker label and compares the time they overlap correctly with the total time assigned to either speaker.
For example, imagine a 60-minute meeting where speaker A talks for 50 minutes and speaker B talks for 10. A diarization system labels 48 of speaker A’s 50 minutes correctly, but only 4 of speaker B’s 10 minutes correctly. Its overall DER may still look relatively strong because most of the meeting belongs to speaker A. JER makes speaker B’s poor result count equally, because it evaluates speaker A and speaker B independently before averaging their scores.
JER_speaker =
1 - (correct_overlap / (ref_time + sys_time - correct_overlap))
The final JER is the average of those per-speaker error rates:
JER =
(1 / N) * Σ[JER_speaker_i]  or i = 1..N
Tracking both DER and JER provides a fuller picture of how accurate the diarization is: DER for overall accuracy, JER for whether that accuracy holds across every participant, including people who speak less often.
Testing on production-representative audio
When evaluating a speaker diarization system, calculate both DER and JER on audio that matches your actual deployment conditions: your typical speaker counts, your audio quality, and your amount of crosstalk.
Published benchmark scores may be measured on clean, controlled datasets like
studio
recordings that rarely match what real call recordings or live meetings sound like. A system that scores well on benchmarks can still underperform significantly on noisy, overlapping, real-world audio. Test on your own data before committing to a diarization product.
Get started with ElevenAPI for speaker diarization
If you are ready to build a transcription feature with multi-speaker support,
Scribe v2
from ElevenLabs makes
speaker diarization
available through a single
Speech to Text
API. Send audio to the endpoint with diarize=true, and the JSON response labels each word with a speaker ID, across up to 32 speakers, in 90+ languages, on files up to 10 hours long.
Two options extend the standard diarization output. For call recordings, detect_speaker_roles=true labels speakers as agent and customer instead of anonymous numbers. If your workspace has registered speaker profiles, use_speaker_library=true can match detected speakers against enrolled voices, bringing diarization and identification together in one request.
A
diarization threshold parameter
lets you tune the tradeoff between over-splitting and merging speakers. And when your speakers are already isolated on separate audio channels, such as stereo call recordings,
multichannel transcription
assigns speakers by channel and skips diarization entirely.
The
Speech to Text quickstart
walks through the first integration step by step. For regulated deployments, the platform is SOC 2, ISO 27001, PCI DSS L1, and HIPAA compliant, with EU data residency and zero retention mode available.
Ready to build speaker diarization into your systems? Start by
getting your API key
or take a look at the
ElevenLabs Docs
to learn more.
Set up your API key
Get API key
FAQ
What does "enable speaker diarization" mean?
“Enable speaker diarization” means turning on speaker labeling in a transcription tool or API, usually via a parameter such as diarize=true. With diarization enabled, the output attaches a speaker label to each word or segment, so the transcript shows who said what rather than an undifferentiated block of text. Diarization is typically optional because it adds processing work that single-speaker audio does not need.
What is the difference between speaker segmentation and diarization?
Segmentation is one step inside diarization. It finds the points in time where the speaker changes, without labeling anyone. Diarization completes the job: it groups the segments between those boundaries and assigns consistent speaker labels, so every segment from the same voice carries the same label across the whole recording.
What is the difference between speaker diarization and speaker identification?
Diarization detects when different people are speaking and labels them anonymously as speaker_0, speaker_1, and so on. Identification determines who those speakers actually are by matching voices against enrolled voiceprints, returning real identities. Diarization needs no prior knowledge of the speakers; identification requires each speaker to be enrolled in advance.
Can speaker diarization work in real time?
Speaker diarization can work in real time, but with an accuracy cost. Real-time diarization must assign speaker labels without seeing future audio, which removes the context that makes offline clustering accurate. Overlapping speech and short utterances are the hardest cases. Real-time diarization is worth the tradeoff for live captioning and in-call agent guidance; for analytics and transcript generation, batch processing produces better results.
How is speaker diarization accuracy measured?
The standard metric is diarization error rate (DER): the share of total speech time that was misattributed, combining false alarm speech, missed speech, and speaker confusion. Jaccard error rate (JER) complements it by weighting every speaker equally rather than by speaking duration, which reveals whether accuracy holds for minor participants and not just the dominant voice.
