---
title: "Scribe v3 Live Medical: transcription for healthcare agents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/scribe-v3-live-medical"
scraped: "2026-11-18T06:00:46.400947+00:00"
lastmod: "2026-11-17T19:56:22.494Z"
type: "sitemap"
---

# Scribe v3 Live Medical: transcription for healthcare agents

**Source**: [https://elevenlabs.io/blog/scribe-v3-live-medical](https://elevenlabs.io/blog/scribe-v3-live-medical)

Blog
Product
Scribe v3 Live Medical helps conversational agents get clinical details right
Written by
John
Durovsik
Published
Nov 17, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
Why live calls need medical transcription
Calls where clinical details matter
Tools for clinical conversations
How we evaluated Scribe v3 Live Medical
What healthcare teams are seeing
What fewer errors mean for healthcare teams
Protecting health information
Getting started
A voice agent acts on what it hears during a live call. When a patient says they take sitagliptin for diabetes, the agent can add it to their medication list for the clinician to review. But drug names are easy to mishear. In our testing, we saw a speech model transcribe sitagliptin as citalopram, an antidepressant. For many people, these calls are the first step in reaching their care team, and an agent can only help if it hears them correctly.
Today, ElevenLabs is releasing Scribe v3 Live Medical, which brings medical transcription to live calls. It’s built on
Scribe v3 Live
, our newest real-time Speech to Text model, and optimized for clinical language. It’s available now in ElevenAgents.
Why live calls need medical transcription
ElevenLabs already offers medical transcription for
recorded audio
, like dictation and visit recordings. But much of what healthcare teams build runs in real time, from scheduling and medical information lines to eligibility checks over the phone and claims follow-ups. Those calls can’t wait for a recording to end.
Medication names and doses rarely come up in everyday speech, so they’re the words a general real-time model is more likely to get wrong. Scribe v3 Live Medical is our first medical transcription built for agents, carrying the clinical focus of
Scribe v2 Medical
into real-time conversations. In our tests on
PriMock57
, a public set of mock live doctor visits, Scribe v3 Live Medical made fewer errors than any other medical model we evaluated.
Calls where clinical details matter
Scribe v3 Live Medical is designed for patient, member, and provider calls where the details are clinical, like a medication at intake, a procedure on a prior authorization, or a symptom on a follow-up call. Many healthcare agents also handle calls with no clinical details at all, like rescheduling an appointment or asking about office hours. Scribe v3 Live Medical improves accuracy on clinical details and holds its accuracy on everyday speech, so teams can use it for every call.
Tools for clinical conversations
Load up to 10,000 custom terms
Healthcare teams can add up to 10,000 of their own terms, and Scribe v3 Live Medical draws on the list only when a caller seems to say one of them. That’s enough for a regional health system to load every provider and clinic name across its locations, or for a pharmaceutical company to load its full portfolio by brand and generic name. With a custom term list loaded, Scribe v3 Live Medical made up to 48% fewer errors on medical terms in our tests.
Wait for callers to finish
Callers often read a member ID or date of birth in pieces, pausing between groups of digits as they find them on a card. An agent that treats every pause as the end of a turn jumps in mid-number, and the caller has to start again. Scribe v3 Live Medical recognizes when a number isn’t finished yet, so the agent waits for the rest before it replies.
Follow patients across languages
Patients and caregivers may switch languages mid-call, for example to describe a symptom more easily in their first language. Scribe v3 Live Medical supports more than 90 languages and follows those switches, so speech in a second language is transcribed instead of dropped.
How we evaluated Scribe v3 Live Medical
We tested Scribe v3 Live Medical against real-time Speech to Text models from leading providers, including specialized medical models and general-purpose models, all on the same recordings. We used two public benchmarks of doctor-patient conversations, compared Scribe v3 Live Medical with Scribe v3 Live on medical and everyday speech, and tested medical terms in English, French, and German. Results are in English unless noted.
We report word error rate (WER), the share of words transcribed incorrectly, and semantic WER, which counts only errors that change the meaning. Semantic WER treats “20 mg” and “twenty milligrams” as a match, so its scores run lower than WER.
Note: These results come from ElevenLabs’ internal testing of selected providers in real-time mode, with each model in its best available configuration. They don’t include every available model.
Primary care consultations (PriMock57)
PriMock57 includes 57 mock live primary care consultations, about 9 minutes each, between clinicians and actors playing patients. The conversations were unscripted on both sides. Actors worked from case cards covering symptoms, medical history, and current medications, and clinicians ran each consultation as they would a real one. The calls ran over telemedicine software, with clinicians on laptops and patients on mobile phones, in an office environment with background noise.
We used this benchmark because it has what makes patient calls hard to transcribe: unscripted back-and-forth conversations, phone audio with background noise, and dense clinical detail. Scribe v3 Live Medical had the lowest WER of the medical models we tested (12.8%), with 17% fewer errors than the next closest one.
Patient interviews (Fareez OSCE)
Fareez OSCE
is 272 recorded patient interviews in the format medical schools use to test clinical skills, the Objective Structured Clinical Examination (OSCE). In each one, a resident doctor or senior medical student asks someone playing the patient about their symptoms and history. Because a different team recorded it in another country, the set shows whether the results hold with new speakers, recording setups, and conditions. Scribe v3 Live Medical had the lowest semantic WER of the medical models we tested (0.6%).
Compared with Scribe v3 Live
Eka Medical ASR
contains more than 3,600 English recordings from doctors and medical students, focused on medical terms and branded drug names. Scribe v3 Live Medical made 4.7% fewer errors on Eka Medical ASR than Scribe v3 Live (11% vs. 11.54% semantic WER).
Model
Eka Medical ASR (semantic WER)
Scribe v3 Live Medical
11%
Scribe v3 Live
11.54%
Everyday speech (Common Voice and FLEURS)
Common Voice is Mozilla’s set of sentences read aloud by volunteers, and FLEURS is Google’s set of short, non-clinical sentences read in more than 100 languages. We scored both on their English sets to make sure teams using Scribe v3 Live Medical don’t give up accuracy on everyday speech. Even a sentence that names a drug is made up mostly of everyday words, so a medical model has to get both right.
Scribe v3 Live Medical performs about the same as Scribe v3 Live on both.
Medical accuracy across languages (MED-Term)
Many healthcare teams serve patients in more than one language.
MED-Term
, a public benchmark from Corti, is a set of spoken clinical case descriptions in English, French and German, each built around rare and specialized medical terms. We used it to check how Scribe v3 Live Medical handles clinical vocabulary beyond English. Its semantic WER was 2.24% in English, 2.81% in German, and 3.24% in French.
Language
Semantic WER (MED-Term)
English
2.24%
German
2.81%
French
3.24%
Low latency on live calls
On a live call, an agent can’t respond until it has the transcript, so any lag in transcription becomes a pause callers hear. Scribe v3 Live transcribes speech in about 150 milliseconds, and in testing, Scribe v3 Live Medical matches that latency, so its clinical focus adds no noticeable delay.
What healthcare teams are seeing
Teams are already building agents with Scribe v3 Live Medical.
“The interaction experience with
Eleven v4 Turbo
and Scribe v3 Live Medical is phenomenal” says Idin Jafari, Director, Digital Strategy & Innovation at Pfizer. “The agent sounds realistic, and it’s more accurate on the brand and generic names that come up in our conversations.”
On patient calls, that accuracy carries through to what care teams review after the call.
“ElevenLabs keeps raising the bar, and that lets Vintage Labs move faster. Our VIA platform makes pre- and post-procedure calls for large academic health systems. With Scribe v3 Live Medical, it understands patients better: their medications, their procedures, the names of their doctors,” says Shantanu Ghorai, Founder & COO of Vintage Labs AI. “Turn detection waits for patients to finish their date of birth before replying, and multilingual mode keeps up when callers switch to Spanish. Nurses can now trust the call summary without replaying the recording.”
What fewer errors mean for healthcare teams
Error rates are easier to judge on a real call. A 10-minute intake call runs about 1,500 words between the caller and the agent. At the PriMock57 error rates above, Scribe v3 Live Medical would get about 40 more of those words right than the next best medical model we tested. For a team handling 1,000 calls a day, that’s about 40,000 more words transcribed correctly every day. Not every word carries the same weight. A dropped “um” is harmless. A misheard medication puts the wrong drug on a refill request, and a wrong digit in a member ID stalls an eligibility check. Either one can turn into a callback, a transfer to staff, or a patient asked to repeat themselves.
Protecting health information
Healthcare agents hear protected health information (PHI) on many calls, including names, dates of birth, member IDs, medications, and symptoms. Scribe v3 Live Medical is HIPAA-eligible for enterprise customers with a business associate agreement (BAA) in place and
Zero Retention Mode
enabled.
Scribe v3 Live Medical runs on ElevenAgents, which is covered by our
compliance programs
, including SOC 2 Type II, ISO 27001, and PCI DSS Level 1. Patient data is stored in the US by default. Enterprise teams that need it stored outside the US can use isolated environments in the EU, India, or Singapore.
Getting started
Scribe v3 Live Medical
is available today in ElevenAgents.
Go to Settings > Automatic Speech Recognition and select it from the model dropdown.
Written by
John Durovsik
Growth
View profile
John is on the ElevenAgents growth team, with a focus on the healthcare industry.
