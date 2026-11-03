---
title: "How are synthetic voices created? A step-by-step guide"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/synthetic-voices"
scraped: "2026-11-03T06:00:52.505416+00:00"
lastmod: "2026-11-03T00:01:13.565Z"
type: "sitemap"
---

# How are synthetic voices created? A step-by-step guide

**Source**: [https://elevenlabs.io/blog/synthetic-voices](https://elevenlabs.io/blog/synthetic-voices)

Blog
Resources
How are synthetic voices created for natural speech?
Written by
Jack
Limebear
Published
Nov 2, 2026
Last updated
Nov 3, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Learn more
Create a voice
On this page
Introduction
Summary
How synthetic voices are created, step by step
From speech data to neural text to speech
What makes AI voice generation sound natural?
How does voice cloning work?
How to record good voice samples for speech synthesis
How to create a voice without recording: Voice Design
How to tell if a voice is AI-generated
Build custom voice experiences with ElevenCreative
FAQ
Today’s sophisticated AI models create synthetic voices that sound like natural speech. Trained on huge datasets of real human voices, these models use advanced neural networks to identify and replicate authentic speech patterns. Creating a synthetic voice is also called speech synthesis or voice synthesis, while the audio it produces is called synthetic speech.
To create a new synthetic voice, a user records themselves talking. Meanwhile, the AI model analyzes their unique phonetic patterns and inflection and uses this data to replicate their voice. Then, the user can adjust vocal characteristics like accent, tone, and pacing to create the final product. Some synthetic voices are a direct clone of one person’s speech, while others are a blend of multiple voices. Voices can also be
designed from a text description
, with no recording at all.
Synthetic voices open up a wide range of creative possibilities for podcasts, audiobooks, video games, and advertising. In this article, we’ll explore how synthetic voices are created, what makes them sound natural, and how to build your own synthetic voice with ElevenLabs.
Create your Instant Voice Clone with ElevenCreative
Sign up
Summary
Synthetic voices are created with neural AI models that analyze and replicate human speech patterns.
Synthetic voices are helpful for narrating audiobooks, generating video game dialogue, creating podcasts and voiceovers at scale, creating customer service
AI agents
, or even preserving voices that are at risk.
Voice cloning
works by analyzing recordings of a specific person’s voice and replicating their unique accent and speech patterns.
Modern AI voices sound natural because they replicate human prosody and are context-aware, instead of just replicating individual words or syllables.
How synthetic voices are created, step by step
Synthetic voice creation is a three-step process.
Here’s what that looks like in practice:
Step 1: Collect voice data:
Synthetic voices start with real human speech. To create a new voice, you’ll need audio recordings of the speakers you want to replicate. The more data you provide, the more accurate and realistic the final voice will be. Here are some
best practices for voice cloning
.
Step 2: Train or fine-tune an AI model:
To create synthetic voices, AI models first analyze extensive datasets with a diverse range of speech recordings. The models use this data to understand human speech patterns. After an AI model has been trained, it can clone real-life voices using a single speech recording. In most cases, you’ll be using a pre-trained model rather than building your own from scratch.
Step 3: Generate audio from text:
Synthetic voices use
text to speech
to generate audio. You can adjust factors like speed and tone to match your preferences. For a deeper look, read our guide to
how text to speech technology works
.
From speech data to neural text to speech
Neural
text to speech
models are trained on numerous datasets of real speech recordings. This dataset includes recordings with different languages, accents, emotions, and pitch levels. Neural text to speech is a widely used form of speech synthesis today.
Traditional models stitched together existing recordings of words, syllables, and
phonemes
. The results were very robotic, as they couldn’t replicate the variations in pitch, rhythm, and expression that make speech sound human.
Instead of just learning how letters and syllables sound, modern neural text to speech models learn natural human pronunciation patterns and speech rhythms. When converting text to speech, these models assess the text, convert it into acoustic features, then use those features to generate waveforms.
Since acoustic features like pitch, rhythm, and tone are built into neural AI models, the resulting speech sounds much more natural and authentic than the models of the past.
The results are also customizable: you can change factors like speed, emotion, and even accent to get the exact voice you’re looking for. For example, your brand could use the same synthetic voice across your website but use excitement and urgency for marketing content and calmness for customer service interactions.
Standard, neural, and generative text to speech
Text to speech models fall into three broad generations.
Understanding the differences between them helps contextualize why modern models, like ElevenLabs Text to Speech, can sound so natural.
Standard text to speech:
These systems stitch together prerecorded sounds or follow rules and statistical models to pronounce text. The output is understandable but robotic, with limited emotion.
Neural text to speech:
Deep learning models learn pronunciation, rhythm, and intonation from large sets of recordings, and generate speech that sounds far more natural and consistent.
Generative text to speech:
Generative models are trained on even larger and more varied speech data, and they use the meaning of the text to decide emotion, pacing, and emphasis. You can steer their delivery with instructions, such as
audio tags
.
Modern voice platforms rely on neural and generative models, while standard text to speech mostly survives in legacy systems.
What makes AI voice generation sound natural?
Synthetic voices generated by AI sound very similar to human voices. In fact, it can be challenging to tell the difference between them if you’re not listening closely.
There are two reasons why AI-generated voices sound more natural than the robotic voices of the past: prosody and context awareness.
Prosody
Prosody
is the rhythm of natural human speech. Small changes in intonation and speed convey tone and emotion as we talk. For example, speaking quickly might convey stress or excitement, while raising your pitch at the end of a sentence turns a statement into a question.
Today’s AI voice models are trained to understand and replicate prosody. This means the output reflects the flow of natural human conversation, rather than sounding stiff or flat.
If you’re using a synthetic voice to narrate an audiobook or create video game dialogue, it will use prosody to reflect the character’s emotions. If you’re creating an educational content
voiceover
or customer service
AI agent
, the AI model will adjust the prosody for calm, empathetic delivery.
By understanding prosody, AI models can also replicate unique accents. For example, the rhythm of a North American English accent sounds very different from a British, Scottish, or Irish English accent, even though they’re speaking the same language.
Context awareness
Instead of processing each word individually, AI-powered TTS models assess the entire phrase, sentence, or conversation and adjust delivery based on the context.
For example, there are many words that are spelled the same but are pronounced differently depending on the tense and context. For example, the word “read” is pronounced like “reed” in the present tense but pronounced like “red” in the past tense.
Since AI voices are context-aware, they identify the appropriate pronunciation based on the rest of the text. They also adjust their delivery so the tone and emotion are appropriate for the situation.
How does voice cloning work?
Voice cloning works by using AI to assess a real person’s voice, then applying their vocal characteristics to synthetic speech.
First, the person cloning their voice must provide a short audio sample. The AI model uses the audio sample to identify the person’s accent, pitch, tone, and cadence. The model uses these characteristics to create a digital replica of the person’s voice. Users can generate new speech in this voice using text to speech technology.
There are two types of voice cloning: Instant and Professional. Instant cloning creates a voice replica with less than two minutes of sample audio. This makes it easy to test voice options before committing to a larger project.
Professional cloning uses between 30 minutes and three hours of audio samples to create a high-fidelity voice clone. Professional Voice Clones preserve subtle details like emotion and intonation that aren’t present in Instant Clones. They also require identity verification.
Voice cloning has a variety of use cases, from generating voiceovers quickly to
preserving voices
that might otherwise be lost.
How to record good voice samples for speech synthesis
The quality of a voice clone depends on the quality of the recording. Even without expensive recording equipment, there are a lot of small things you can do to improve how your voice clone sounds.
These habits help you capture clean samples:
Record in a quiet space:
Soft furnishings such as curtains and carpets reduce echo, and turning off fans and notifications removes background noise.
Keep the microphone at a steady distance:
A consistent distance keeps the volume even, and a pop filter reduces harsh plosive sounds.
Speak the way you want the clone to sound:
The clone copies your delivery. Record in the tone and pace you plan to use.
Avoid music and other voices:
Use a single speaker with no background music or overlapping speech.
Stay consistent:
Use the same microphone and room across your recordings.
While Instant Cloning needs less audio and Professional Cloning needs more, both depend on clean recordings. Clean audio of the right length gives better results than a large amount of noisy audio.
How to create a voice without recording: Voice Design
Not every synthetic voice starts with a recording. With
Voice Design
, you describe the voice you want in text, including details like age, gender, accent, tone, and pacing, and the AI model generates voice options that match your description. You can listen to the options, choose the one you like, and save it to your voice library.
Voice Design
is useful when you need a voice for a character, a brand, or a product and there is no real person to clone. Read the
Voice Design documentation
to learn how to write effective voice descriptions.
How to tell if a voice is AI-generated
There is no single giveaway that proves a voice is AI-generated. Combining careful listening, detection tools, and a check on where the audio came from works better than relying on any one of them.
Many people think they can tell the difference between a real voice and an AI-generated one, but they don’t always get it right. A 2025 survey found that
70% of consumers
thought they could correctly identify an
AI voice agent
, but 90% of them failed to do so correctly.
Instead of relying on the human ear, you can use a detection tool. Detection tools work in two main ways:
Watermark detection:
Some AI providers embed a watermark, a code that humans cannot hear, in the audio they generate. A detector can find the watermark and confirm where the audio came from. This only works on audio that carries a watermark.
Classifier-based detection:
A classifier analyzes the audio and estimates the probability that it was AI-generated. It can flag audio that has no watermark, but the result is a probability and can be affected by compression, background noise, or editing.
Neither method is perfect. Treat a detection result as one piece of evidence and check it against what you know about the source. We’ve written a guide to
audio deepfake detection
, which goes into more detail here.
ElevenLabs Speech Classifier
is a tool that identifies the probability that an audio sample was generated with ElevenLabs AI voice models. ElevenLabs has also partnered with
Reality Defender
on
deepfake detection initiatives
to identify and prevent voice fraud.
What to listen for
Detection tools are not always on hand, so it helps to know the common signs of a synthetic voice.
Listen for:
Uneven pacing:
Speech that is too steady or that pauses in unnatural places.
Odd breathing or mouth sounds:
Breaths that are missing, repeated, or misplaced. These could indicate audio artifacts that a model has inadvertently generated.
Mispronounced names or terms:
Unusual words said with the wrong stress. This is even more common in languages that have accent marks to emphasize certain syllables in words, like Spanish.
Flat or mismatched emotion:
Delivery that doesn’t fit the meaning of the words. This demonstrates a lack of understanding of the text itself, which is a common problem with legacy TTS models.
Modern synthetic voices often avoid all of these. A clean-sounding sample does not prove a voice is real. For anything high-stakes, such as a call asking for money, confirm through a second channel.
Build custom voice experiences with ElevenCreative
ElevenCreative helps you build custom
voice experiences
for your creative projects. Choose from an extensive library of over 20,000 pre-made voices or create your own with accurate and secure voice cloning.
Use ElevenCreative to replicate your voice using
Instant Voice Cloning
or
Professional Voice Cloning
. Instant Voice Cloning works in minutes to help you test voice options or launch personal projects fast. Professional Voice Cloning uses longer audio samples to create high-quality voices ideal for longer projects like audiobooks, video games, or podcasts. No matter which option you choose, the audio traces back to your account for security.
ElevenCreative
’s customizable
Voice Library
and voice cloning tools help you bring your creative projects to life.
Sign up for ElevenCreative
to explore iconic voices or create your own.
Get started with ElevenCreative
Sign up
FAQ
How can I tell if a voice is AI-generated?
Several factors give lower-quality AI voices away. Listen out for things like odd breathing sounds, mispronounced names, emotions that don't align with the text, or uneven pacing. Keep in mind that modern synthetic voices are hard to spot by ear. Detection tools can help. Some identify audio watermarks, and others estimate the probability that a sample was AI-generated. Read our
guide to AI voice detection
for a more detailed breakdown.
Is voice cloning illegal?
Voice cloning is not illegal. You can legally clone your own voice or clone someone else’s voice with their explicit, documented permission. However, cloning someone else’s voice without permission is usually illegal, especially when used for fraudulent activity or to reproduce copyrighted work.
Where does AI get its voices from?
AI models get their voices from a variety of sources. They’re trained on datasets of existing audio recordings. Individual users can also clone their voices. ElevenLabs has licensed
iconic voices
, which include notable actors and historical figures.
Do you need consent to clone someone’s voice?
You should always get explicit, documented permission from the person whose voice you want to clone. Laws vary by country and state, and several can apply at once: privacy and data protection rules (a voice recording can count as personal data), rules that protect a person’s voice and likeness, and laws against fraud and impersonation. Keep a written record of the consent that covers what the voice will be used for and for how long. This is general information, not legal advice.
How do you measure how natural a synthetic voice sounds?
A common method is a listening test, where a group of people rate voice samples on a scale. The ratings are often averaged into a mean opinion score (MOS). You can also run A/B tests that compare two voices on the same script. Alongside the ratings, check how the voice pronounces names and technical terms, whether the pacing feels right, and whether the emotion fits the text. For conversational uses such as AI agents, also measure how quickly the voice starts speaking.
Written by
Jack Limebear
Growth Marketing
View profile
Jack Limebear is on the Growth team, acting as a content writer and strategist across the blog and insights pages. Before ElevenLabs, he spent over a decade leading content strategy for organizations ranging from fast-growing SaaS startups to Fortune 500 companies. He holds a Master's degree in English Literature from the University of Cambridge.
