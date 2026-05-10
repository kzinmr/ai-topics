---
title: "Speaking of Voxtral"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/voxtral-tts"
scraped: "2026-05-10T01:21:11.332048+00:00"
lastmod: "2026-04-28T12:32:29.978Z"
type: "sitemap"
---

# Speaking of Voxtral

**Source**: [https://mistral.ai/news/voxtral-tts](https://mistral.ai/news/voxtral-tts)

Voxtral
Text-to-Speech
Marie - Neutral
Bienvenue
dans
ce
nouvel
épisode.
Oliver - Excited
Hello,
thank
you
for
calling.
How
can
I
help
you?
Nick - neutral
¡Estamos
encantados
de
anunciar
el
lanzamiento
de
nuestro
nuevo
producto!
Voxtral
Text-to-Speech
Bienvenue
dans
ce
nouvel
épisode.
¡Estamos
encantados
de
anunciar
el
lanzamiento
de
nuestro
nuevo
producto!
Hello,
thank
you
for
calling.
How
can
I
help
you?
Marie - Neutral
Nick - neutral
Oliver - Excited
Speaking of Voxtral
Listen to the article
Today we’re releasing Voxtral TTS, our first text-to-speech model with state-of-the-art performance in multilingual voice generation. The model is lightweight at 4B parameters, making Voxtral-powered agents natural, reliable, and cost-effective at scale.
Highlights.
Realistic, emotionally expressive speech in 9 popular languages with support for diverse dialects.
Very low latency for time-to-first-audio.
Easily adaptable to new voices.
Available to test out in
Mistral Studio
.
Enterprise-grade text-to-speech, powering critical voice agent workflows.
A natural voice generation hinges on the model’s ability to not only recite but interpret a text accurately. Contextual understanding - like neutral, happy, sarcastic, etc. - determines whether the listener considers the generation accurate or robotic. Our model excels at both contextual understanding and speaker modeling: capturing how a specific person naturally speaks. Our voice adaptation goes beyond traditional read-speech by capturing a speaker’s personality, including their natural pauses, rhythm, intonation, and emotional dexterity. With its compact size, low cost and latency, and easy adaptability, Voxtral TTS gives full control and customization for enterprises looking to own their voice AI stack.
Audio is the new UX. Create new interactions for collaboration and understanding only found in speech. Begin now in AI Studio with our Mistral Voices in American, British, and French dialects.
Listen and decide: can you tell the difference?
Our team speaks dozens of languages in multiple dialects, we understand the importance of cultural nuance and built a model that is a reflection of us. Speech generation builds trust via natural-like rhythm, emotion, and even the use of humor. That’s why with voice emulation, we focused on authenticity and emotional expressiveness.
Voice emulation
Margaret
Sanchit
Angele
Gustavo
Khyathi
Nick
Yassir
Patrick
Original voice
Margaret
Model Behavior Architect
English (US)
Emulation
Prompt
Boy oh boy! I'm so excited for the summer. It's going to be so warm here, can't wait for swimming in the Lido and making cherry pie.
State-of-the-art performance.
Automated metrics such as word-error-rate and audio quality scores for multilingual text-to-speech systems are unable to measure naturalness of speech. What makes speech natural is extremely nuanced and requires a deep understanding of cultural differences and typical speaking patterns. Hence, comparative human evaluations performed by native speakers are crucial.
For voice agents, latency and quality are in constant tension. Human evaluations show that Voxtral TTS achieves superior naturalness compared to ElevenLabs Flash v2.5 while maintaining similar Time-to-First-Audio (TTFA). Voxtral also performs at parity with the quality of ElevenLabs v3, successfully supporting emotion-steering for more lifelike interactions.
We conducted a comparative human evaluation of Voxtral TTS and ElevenLabs v2.5 Flash in a zero-shot custom voice context. Using two recognizable voices in their native dialects for each of the 9 supported languages, 3 annotators performed a side-by-side preference test per pair on naturalness, accent adherence, and acoustic similarity to the original reference. Voxtral TTS widens the quality gap to v2.5 Flash in this zero-shot multilingual custom voice setting, highlighting the instant customizability of Voxtral TTS to any voice.
Spoken natively.
Trained on a large speech dataset, Voxtral TTS is built for global application. It supports state-of-the-art performance in 9 languages: English, French, German, Spanish, Dutch, Portuguese, Italian, Hindi, and Arabic.
The model was trained to adapt to a custom voice with a reference as little as 3s and capture not just the voice but also nuances like subtle accent, inflections, intonations and even disfluencies similar to those expressed in the reference. We offer some preset voice options in the API but it is simple to extend to your in-house voice library customizing it to the use-case, localize it to the language and accent, keep it neutral or more emotive, casual or formal, more natural and conversational or robotic.
The model also demonstrates zero-shot cross-lingual voice adaptation even though it’s not explicitly trained for it. For example, the model can generate English speech with a French voice prompt and English text. The resulting speech sounds natural while adopting the accent of the provided voice prompt (in this example, the generated speech has a natural French-accented English). This makes the model useful for building cascaded speech-to-speech translation systems.
Cascaded speech-to-speech translation
Click or connect a speaker to the prompt block to enable cascaded speech-to-text translation.
Paul
English (US)
Marie
French
Oliver
English (UK)
Before we begin, I'll need to verify a few details. Can you confirm your full name and date of birth?
English
French
Spanish
German
Voxtral TTS
Paul
English (US)
Marie
French
Oliver
English (UK)
Prompt
Before we begin, I'll need to verify a few details. Can you confirm your full name and date of birth?
English
French
Spanish
German
Generated Audio
Voxtral TTS
Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.
Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.
Built for low-latency streaming.
Latency is critical for voice agent applications. Voxtral TTS achieves a model latency of 70ms for a typical input voice sample of 10 seconds and 500 characters, with a real-time factor (RTF) of ≈9.7x. The model natively generates up to two minutes of audio, and our API handles arbitrarily long generations with smart interleaving.
Voxtral TTS architecture.
The model is a transformer-based, autoregressive, flow-matching model, built on
Ministral 3B
. It consists of the following components:
3.4B parameters transformer decoder backbone
390M flow-matching acoustic transformer
300M neural audio codec (symmetric encoder-decoder)
The model takes a voice prompt (5 to 25 seconds) and a text prompt in 9 supported languages. For each audio frame, the transformer backbone predicts a semantic token, then the flow-matching transformer runs 16 function evaluations (NFEs) to produce the acoustic latent.
We developed an in-house codec, which processes audio causally using a semantic VQ (8192 vocabulary) and an acoustic FSQ (36 dim and 21 levels) latent and produces them at 12.5Hz frame rate.
Powering enterprise voice workflows.
Voxtral TTS closes the loop on audio intelligence, giving enterprise voice pipelines an output layer that passes the human test. It works alongside
Voxtral Transcribe
for full speech-to-speech, or integrates into any existing speech-to-text and LLM stack, with cross-lingual support.
Workflows
Customer Support
Financial Services
Manufacturing and Industrial Operations
Public Services and Government
Compliance and Risk
Supply Chain and Logistics
Automotive and In-Vehicle Systems
Sales & Marketing
Real-Time Translation
Customer Support
Voice agents that route and resolve queries across channels with natural, brand-appropriate speech.

      Place Voxtral TTS into existing contact support call systems for automated spoken responses, with output that integrates into existing workflows.
Thank
you
for
contacting
support.
I
see
your
concern
about
the
unexpected
charge
on
March
22nd.
Let
me
pull
up
your
account
details.
Ah,
yes.
This
appears
to
be
a
temporary
hold
for
a
subscription
upgrade
you
requested.
Would
you
like
me
to
cancel
the
hold
or
adjust
your
plan?
Your
call
is
important
to
us,
so
I'll
stay
on
the
line
until
this
is
resolved.
Jane
Test-run the model in Mistral Studio.
Experiment with Voxtral TTS directly in the
Mistral Studio playground
. Select one of the Mistral voices or record your own.
Get started with Voxtral TTS.
Voxtral TTS is available now via API at $0.016 per 1k characters.
Try it now in
Mistral Studio
or in
Le Chat
.
A model with several reference voices is available as open weights on
Hugging Face
under CC BY NC 4.0 license.
Explore the model’s
documentation
or read our
research paper
.
Sign up for our upcoming
webinar
to learn more!
We’re hiring!
We are building the voice layer for AI, and If this is the kind of problem you want to work on,
we'd love to hear from you
.
Share this article
More from Mistral AI
News
Models
AI Services
