---
title: "Introducing Scribe v3 and v3 Live, our most accurate speech to text models"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/scribe-v3"
scraped: "2026-11-11T06:00:35.115439+00:00"
lastmod: "2026-11-10T20:23:32.832Z"
type: "sitemap"
---

# Introducing Scribe v3 and v3 Live, our most accurate speech to text models

**Source**: [https://elevenlabs.io/blog/scribe-v3](https://elevenlabs.io/blog/scribe-v3)

Blog
Product
Introducing Scribe v3 and v3 Live, our most accurate speech to text models
Written by
Min
Kim
Published
Nov 10, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
The feedback that shaped Scribe v3
Speaker labels, turn detection, and more control over the output
How Scribe v3 measures up
What a few points of accuracy are worth
Getting it right the first time in ElevenAgents
Built for enterprise
Get started today
Products built on audio start with a transcript: meeting notes, voice agents, dubbing, clinical documentation, and broadcast archives that span decades of content. Getting that transcript right the first time matters, because every error travels downstream, where it costs far more to fix.
But real world audio is messy. It’s several people talking over each other in a meeting, a customer on a busy street who pauses halfway through a sentence, or a support call where neither person is speaking their first language.
Today ElevenLabs is launching two new Speech to Text models built for exactly these conditions:
Scribe v3
, for recorded audio, makes 27% fewer word errors than Scribe v2 across 102 languages and has the most accurate speaker labels of any model we tested,
Scribe v3 Live
is the low latency variant for realtime audio and makes 43% fewer errors than Scribe v2 Realtime. It also includes speaker diarization for the first time (labeling who said what) and improved turn detection.
Scribe v3 Live is available today in
ElevenAgents
. Both models are also available in
ElevenAPI
, where switching from Scribe v2 is a one-line change to the model ID.
The feedback that shaped Scribe v3
Scribe has powered hundreds of millions of hours of transcription for meeting-notes apps, contact centers, clinical documentation tools, and voice agents. Across use cases, the teams building on it kept asking for the same five things.
Meeting and note-taking teams wanted better diarization in quick back-and-forth and with three or more speakers. Voice agent teams said a silence timer cuts callers off when they pause mid-sentence or slow down to read out a number. Teams building live products were giving up accuracy for speed, since realtime ran noticeably worse than batch. Customers in India wanted Hindi to match English, even when callers switch between the two mid-sentence. And many wanted more control over the output, from numbers written as “123” to key term lists long enough for a product catalog or a list of drug names.
Speaker labels, turn detection, and more control over the output
Diarization that holds up in a crowded room
In a meeting transcript, identifying the right speaker matters just as much as getting the right words. Scribe v3 makes 17% fewer diarization errors than Scribe v2 on recordings with three or more speakers, which are the recordings where most existing models fail. Scribe v3 Live also brings diarization to realtime transcription for the first time, with 39% fewer diarization errors than the next-best realtime model we tested.
Turn detection that listens to the conversation
For conversations to feel natural, voice agents need to accurately predict when a speaker is done talking. Traditional turn-taking systems do so based on periods of silence. But silence alone forces a trade-off: setting a short threshold could interrupt people who pause in the middle of a sentence and a long one makes an agent feel slow. Scribe v3 Live uses the context of the conversation as well as the audio, so a caller who pauses halfway through a number isn’t cut off. This is the same turn detection ElevenAgents already uses, now available in ElevenAPI.
More control over languages, terminology, and formatting
Scribe v3 can infer hints about which languages a recording may contain and lets you choose whether numbers return as digits or words. Keyterm prompting takes up to 1,000 terms you know will come up, such as brand names, acronyms and jargon, and transcript edits apply formatting rules written in plain English, such as “write every date as YYYY-MM-DD.”
Scribe v3 Live adds a multilingual mode for conversations that switch languages mid-sentence. It also adds a keyterm library for vocabularies too large for a list. Where keyterm prompting covers terms you
know
will come up, keyterm library holds thousands that
might
, and the model consults it only when it hears a likely match.
How Scribe v3 measures up
ElevenLabs evaluated both models against Scribe v2, Scribe v2 Realtime, and other popular Speech to Text models, scoring each on the same datasets. Multilingual accuracy was measured on an internal version of the
FLEURS benchmark
, which tests short, clean read speech in 102 languages. FLEURS can’t measure diarization, since every clip has one speaker, so we also built our own dataset of real meetings, agent calls, and voice notes across 16 languages. We’ll be open sourcing this soon.
Speaker diarization
Scribe v3 has the lowest diarization error of any model we tested, with 12% fewer errors than Scribe v2 overall and 17% fewer on recordings with three or more speakers.
Multilingual transcription accuracy
We report word error rate (WER) alongside semantic WER, which counts an error only when the meaning of the transcript changes.
Across 102 languages on FLEURS, Scribe v3 reduces WER by 27% compared with Scribe v2 and improves in every language tested. In languages easier to transcribe, German improved by 42%, Spanish by 35%, and English by 23%. The improvements are larger in languages that are harder to transcribe: Swahili drops by 34%, Tamil by 29%, and Thai by 28%.
Scribe v3 also makes fewer word errors than every other batch (non-streaming) model we tested, comparing each one on the languages both models support.
Speaker diarization in realtime
On the English portion of our 16-language real-world dataset, Scribe v3 Live has a diarization error rate of 3.1%, compared with 5.9% to 7.3% for the other realtime models we tested.
Standard diarization scores also count transcription mistakes, such as missed words, and realtime models miss more words than batch models. To measure only whether each word was given to the right speaker, we aligned each model’s transcript to the reference before scoring. This lowers every model’s error rate, so these results can’t be compared with the batch diarization results above.
Multilingual accuracy in realtime
For realtime models we lead with semantic WER. A streaming model writes text before it has heard the whole sentence, and each provider formats numbers, punctuation and casing differently as it goes. Standard WER counts those differences as errors even when the meaning is the same, so semantic WER is the fairer comparison.
Across 102 languages, Scribe v3 Live reduces semantic WER by 43% and WER by 31% compared with Scribe v2 Realtime. It improves in every language, and has a lower error rate than every other realtime model we tested.
The improvements are largest where realtime transcription has lagged: Greek improves by 77%, Danish by 54%, and Croatian by 45%, while Hindi improves by 36%.
A note on method: we scored each language on its own before averaging, so all 102 languages count equally. Many published results pool every clip into a single score, which tends to give lower numbers, so results measured in different ways aren’t directly comparable.
What a few points of accuracy are worth
Every model launch comes with percentages, this one included, and on paper, it’s difficult to discern what a few points mean in real-world scenarios. A one-hour meeting at 150 words per minute is about 9,000 words, so the gap between a 4% and a 2% word error rate is 180 wrong words, three for every minute someone was talking. Diarization error is measured in time rather than words so in that same meeting, every point is 36 seconds of speech under the wrong name.
What those errors cost depends on where they land. In a podcast transcript a wrong word is a typo, but on an earnings call “fifteen” heard as “fifty” ends up in an analyst’s model. Errors also cluster in names, numbers, acronyms and jargon, which are exactly the words a summary or an agent most needs to get right.
Getting it right the first time in ElevenAgents
Voice agents feel this most, because a single misheard digit can fail the check that starts the call. Eneco, which supplies energy to more than 2 million homes and businesses in the Netherlands, runs its voice agent on ElevenAgents and tested Scribe v3 Live on it ahead of launch. In real customer calls, the agent recognized Dutch postcodes correctly on the first try 40% more often, and house numbers 15% more often.
“ElevenLabs is a true partner for Eneco. Together with their forward deployed engineers, we are working to further improve our voice agent,” said Ruud Huigsloot, a Senior Product Manager at Eneco. “It’s great to see significant results this early, and we are excited to continue collaborating.”
Built for enterprise
Scribe v3 and Scribe v3 Live run in the US by default, and are offered in isolated EU, India, and Singapore environments for enterprise customers with data residency requirements.
Zero Retention Mode
deletes audio and text as soon as a request completes. Both models are covered by our SOC 2, ISO 27001, and PCI DSS Level 1 programs, are HIPAA-eligible with a Business Associate Agreement, and are available for private deployment.
Get started today
Scribe v3 Live is available in
ElevenAgents
, and both v3 and v3 Live are the default in the ElevenLabs app.
Sign up
to try it.
Both models are also available in ElevenAPI today. Existing integrations upgrade by changing the model ID to
scribe_v3
or
scribe_v3_live
.
import
{ ElevenLabsClient }
from
"@elevenlabs/elevenlabs-js"
;
const
elevenlabs
= new ElevenLabsClient();
const
connection
=
await
elevenlabs.speechToText.realtime.connect({
modelId:
"scribe_v3_live"
,
commitStrategy:
"turn_prediction"
,
});
For healthcare teams, we’re also releasing a version of Scribe v3 Live optimized for medical conversations in ElevenAgents.
Written by
Min Kim
View profile
