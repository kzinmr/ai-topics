---
title: "Scribe v2 Medical is now available to everyone"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/scribe-v2-medical-generally-available"
scraped: "2026-09-23T06:00:04.242596+00:00"
lastmod: "2026-09-22T21:40:34.846Z"
type: "sitemap"
---

# Scribe v2 Medical is now available to everyone

**Source**: [https://elevenlabs.io/blog/scribe-v2-medical-generally-available](https://elevenlabs.io/blog/scribe-v2-medical-generally-available)

Blog
Product
Scribe v2 Medical is now available to everyone
Written by
Min
Kim
Published
Sep 22, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
Scribe v2 Medical is optimized for clinical use cases
Customers in production
Strong performance on general speech
Built for protected health information
Getting started
Clinical audio is one of the hardest tests for accurate speech recognition. Drug names are long, rare, and easy to mix up (hydroxyzine and hydralazine are one misheard syllable apart). Vocabulary is dense, with dosages, units, anatomy, and pathology terms that can arrive in rapid sequence. The stakes are also higher because a transcription error could end up in a patient’s chart.
That’s why ElevenLabs is today releasing
Scribe v2 Medical
, our Speech to Text model fine-tuned for clinical audio, which is now generally available on ElevenAPI. Across the evaluations presented below, it consistently scores one of the lowest word error rates (WER) among the models compared, and reduces WER on clinical audio by approximately 35% compared to our base Scribe v2 model.
General purpose models are great at handling everyday speech, but can degrade where clinical workflows need them the most. We trained a medical fine-tune of Scribe v2 focused on medication names along with clinical dictation, on public benchmarks anyone can reproduce.
Scribe v2 Medical is optimized for clinical use cases
Clinical dictation (MedDictate)
Corti’s MedDictate
tests transcription of dictated clinical notes, which include drug names, dosages, and units arriving back to back in English, French, and German. In our evaluation, Scribe v2 Medical records the lowest overall WER among the models we tested, and approximately 35% lower WER than base Scribe v2.
Model
EN
FR
DE
Overall WER
Scribe v2 Medical
3.0%
8.3%
7.2%
4.9%
OpenAI GPT Transcribe
3.9%
7.8%
9.6%
5.9%
Scribe v2 (base)
5.0%
10.7%
11.7%
7.6%
Muse Voice Transcribe 1.0
4.5%
11.0%
13.3%
7.8%
Deepgram Nova-3 Medical*
5.5%
-
-
-
*English only (24 clips) - Deepgram Nova-3 Medical does not support French or German.
Medical terminology (MedTerm)
MedTerm
is also a dataset published by Corti and includes a 600-sample clinical terminology benchmark in the same three languages, with the medical terms in each sample annotated. That annotation makes it possible to score models on two dimensions beyond the whole transcript WER. Term recall is the percentage of annotated medical terms that appear correctly in the transcript (higher is better). Term-WER is the error rate over those terms alone, ignoring the ordinary speech around them (lower is better).
Scribe v2 Medical leads every model tested on both dimensions, and leads every other provider in all three languages:
Model
Term recall ↑
Term-WER ↓
Scribe v2 Medical
77.7%
10.4%
Scribe v2 (base)
77.1%
10.7%
OpenAI GPT Transcribe
74.0%
12.3%
Muse Voice Transcribe 1.0
73.4%
12.9%
Deepgram Nova-3 Medical*
72.5%
13.6%
Omi Health Medical Speech to Text benchmark
Performance holds up on independent testing as well.
Omi Health
maintains a public leaderboard of 30 models scored on 1,513 clinical English clips (7.2 hours across 57 consultations), and Scribe v2 Medical scores the lowest overall WER of all 30 models tested (5.88%) and delivers substantially improved dosage accuracy over base Scribe v2 (86.2% vs. 79.8%).
Omi's benchmark updates with the Scribe v2 Medical results on September 25, and the figures above are shared with their permission ahead of that update.
Eka Medical ASR benchmark
The
Eka Medical ASR benchmark
contains 3,619 English clinical audio samples — across isolated drug and condition names, clinical sentences, and conversations between clinicians and patients — with per-term annotations and a published leaderboard on the dataset card.
Since the published dataset includes older models like Gemini 2.5 Flash and GPT-4o, we ran the evaluation against newer models. SemWER (semantic WER) scores whether the model heard the right content, regardless of formatting ("mg" and "milligrams" count as the same answer), and kwWER (keyword WER) applies the same scoring to the annotated medical keywords only.
Model
semWER
kwWER
Scribe v2 Medical
6.50%
6.02%
Scribe v2 (base)
7.35%
7.04%
Deepgram Nova-3 Medical
7.79%
7.65%
Muse Voice Transcribe 1.0
8.85%
8.99%
OpenAI GPT Transcribe
13.90%
13.20%
Eka annotates the medical terms in each sample, which makes it possible to score Scribe v2 Medical's gains over base at a more granular level on the medical terms alone. Scribe v2 Medical makes 15% fewer errors than base (9.5% vs. 11.1%), and the gains are largest where terms appear inside full clinical sentences (7.5% vs. 9.9%).
A caveat from the same data is that isolated single-word clips (a lone drug name spoken with no surrounding context) remain the hardest case for every model on the leaderboard, including Scribe v2 Medical. It scored 14.3% WER on isolated terms compared to 7.5% when those terms appear in sentences. With zero context, a misheard syllable can result in memorable failures:
etodolac (an NSAID) → "It'll do the luck"
levomilnacipran (an antidepressant) → "Leave me alone now, Sephora."
methdilazine (an antihistamine) → "Let's play our scene."
One way to reduce these errors is with
keyterm prompting
, which lets you highlight drug names or medical phrases to bias the model towards successfully transcribing them.
Customers in production
Customers are already using Scribe v2 Medical in production and seeing improvements in clinical audio.
"Since switching from Deepgram to ElevenLabs Scribe v2 Medical, we're seeing much higher accuracy on clinical terminology, and that changed how the team work,” said Mendel Erlenwein, CEO and founder of CareCo. “When our coordinators trust transcripts, they can spend less time correcting notes and more time on the phone with patients. Our patients are on complicated regimens, and the note the care team reads has to be right.”
Strong performance on general speech
The team also verified that the medical fine-tune does not degrade performance in other areas. On 6,000 samples of everyday, non-medical speech derived from
Common Voice
, Scribe v2 Medical scores the same as base Scribe v2 when rounded, a 5.3% WER in both cases. So with v2 Medical, you get the benefits of a specialized medical model — without giving up accuracy on this benchmark.
Built for protected health information
Scribe v2 Medical is HIPAA-eligible for enterprise customers with Business Associate Agreements in place and
Zero Retention Mode
(ZRM) enabled.
With ZRM enabled for Speech to Text API requests, audio input and text output are deleted immediately after each request completes. ElevenLabs retains neither, and your application receives the full API response and controls how transcripts are retained.
Getting started
Scribe v2 Medical is available on the
Speech to Text API
. Simply pass the new model id:
scribe_v2_medical
import
{ ElevenLabsClient }
from
"@elevenlabs/elevenlabs-js"
;
const
elevenlabs
= new ElevenLabsClient({
apiKey:
"YOUR_API_KEY"
});
const
fileData
=
await
fs.promises.readFile(
"clinical_audio.mp3"
);
const
transcription
=
await
elevenlabs.speechToText.convert({
file:
new Blob([fileData], {
type:
"audio/mp3"
});,
modelId:
"scribe_v2_medical"
,
});

console.log(transcription.
text
);
The model runs on the batch Speech to Text endpoint.
