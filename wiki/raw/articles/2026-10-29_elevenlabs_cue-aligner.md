---
title: "Forced alignment with Cue: Character-level audio timing"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/cue-aligner"
scraped: "2026-10-29T06:00:39.911907+00:00"
lastmod: "2026-10-28T22:34:59.255Z"
type: "sitemap"
---

# Forced alignment with Cue: Character-level audio timing

**Source**: [https://elevenlabs.io/blog/cue-aligner](https://elevenlabs.io/blog/cue-aligner)

Blog
Research
How your transcript knows where each word is spoken
Written by
Mike
Murphy
Published
Oct 28, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Read the docs
Learn more
On this page
Introduction
What is forced alignment?
Where traditional aligners fall short
How Cue is different
Aligning songs
Try Cue today
If you’ve ever watched a movie on TV where there’s an issue with the broadcast, and the actors’ dialogue is completely out of sync with the captions, you know how distracting it can get, and pull you out of the story. Videos and software using voice models have the same problem: A subtitle that appears a second late, or a transcript that highlights the wrong word, can feel just as broken.
“Humans are quite good at aligning media, at the word level at least,” said Danila Kozlov, a researcher at ElevenLabs working on alignment. “We often have the inherent feel of where a word is beginning, but at the character level and with sub-millisecond precision, it’s a lot harder.”
Today, ElevenLabs is sharing more on Cue, a forced alignment model that places every character in an audio file on a precise timeline. Cue powers ElevenLabs’ Scribe model family, and on real-world recordings, it’s more accurate than every aligner ElevenLabs tested, in all 29 languages of the benchmark. It also handles recordings of any length in a single pass and aligns an hour of audio in less than a second.
What is forced alignment?
Imagine someone hands you a video and a transcript and asks you to match each word to the moment it’s spoken. That is forced alignment. When you click a word in an ElevenLabs transcript and the player jumps to that exact spot, an aligner is doing the work.
Forced alignment, however, is different from the more nebulous concept of AI alignment. That’s about designing AI systems so their behavior matches people’s value systems and business preferences. With forced alignment, we’re talking just about lining up text and sound.
Cue is the last step in the speech-to-text pipeline. Scribe, ElevenLabs’
Speech to Text model
, transcribes the audio, and the aligner sets the timing. Every Scribe request passes through it. The same model also powers subtitles, dubbing, and lyric timing for music, and it’s available on its own through the Forced Alignment API.
Because so many products depend on it, an aligner has to be precise in every supported language, extremely fast, and able to handle many requests at once.
Where traditional aligners fall short
Prior to the new model, the team built the aligner model that had been used in every ElevenLabs product to date. Although powerful, they knew they could make a new version stronger. When Kozlov joined, he and the team began by interviewing customers and internal users at ElevenLabs about what frustrated them when working with the previous aligner. Their complaints matched the limits of the open-source tools the team tested.
Length is the first major problem. Many aligners today work well for clips about 30 seconds long, but longer files have to be chopped into chunks. Each new chunk has the potential to add a little timing error, and stitching the seams between chunks can add more. On full recordings, Cue’s average amount of timing errors is just 179 milliseconds, while the open-source tools ranged from 283 ms to more than 6,000 ms.
Real-world recorded audio is even more of a challenge. Background noise, overlapping speech, and ambient music cause many tools to lose their place when matching up text to audio. But these are the sorts of files that many people actually want transcribed, as we all tend to live in places that aren’t perfectly quiet. On English recordings with background issues, Cue’s average error is 57 ms, compared with 65 ms to 920 ms for the others.
Language support is another constraint. Most open-source aligners need a separate model for each language they support, so languages with less training data often don’t perform as well, or just aren’t supported.
MMS-FA
is the only other tool that handles all 29 benchmark languages, and comparably, Cue was generally quicker at figuring out the boundaries between words.
Speed is also an issue for these models, as aligning large volumes of audio can get expensive quickly. Cue can align one hour of audio in around half a second on our production GPU. The next fastest tool, Qwen3-ForcedAligner, takes nearly 2 seconds, and the slowest tested, took well over a minute.
How Cue is different
Cue is a single model that covers more than 90 benchmark languages, unlike most of its competitors. It can also take recordings of any length in a single pass, which avoids the chunking that causes timing errors to build up on long files.
Pinch or Control-scroll to zoom. Swipe horizontally or Shift-scroll to pan. With a word focused, use plus and minus to zoom or Shift and the left or right arrow to pan.
Imagine
someone
hands
you
a
video
and
a
transcript,
and
asks
you
to
match
each
word
to
the
moment
it's
spoken.
That
is
forced
alignment.
Cue
places
every
character
on
the
audio
timeline,
so
the
right
words
show
up
at
the
right
time.
Select a word to see its characters
While most models have gotten larger as they get more performant, Cue is smaller than the previous ElevenLabs’ aligner, Kozlov said. It still runs on a GPU, but it aligns an hour of audio in about half a second.
The team built Cue around the types of audio people actually upload. Using the previous aligner as a baseline, they created a benchmark from real-world requests and scored every tool the same way, counting any word a tool failed to place as an error. Cue works at the character level, which is finer than the word-level labels most benchmarks use, so those scores likely understate its precision.
“At some point you reach the level of human abilities,” Kozlov said of aligner models. “Our current aligner is beyond that level, and so it becomes a lot harder to check whether you’re fully correct or just how precise you are, because there’s no golden benchmark for it. We had to use word-level benchmarks to benchmark a character-level system, which does not necessarily showcase Cue's full potential.”
Cue’s quality also reflects how quickly ElevenLabs can act on user feedback. Soon after Cue was rolled out, a customer alerted the team that Georgian and a couple other languages with fewer resources performed worse than they had been expected to. ElevenLabs keeps research close to the teams and customers using its products, which meant they were able to catch the issue quickly, conduct research on possible model improvements, train a new version of the model and release it — all within less than 24 hours  from when the customer first brought up the issue.
Aligning songs
Music is difficult because singing stretches and blurs words, and few models can do it well. The team didn’t expect Cue to handle it as well as it does. Cue was able to align a subset of songs from the Creative Commons-licensed
JamendoLyrics MultiLang
dataset. It was able to do this in English, French, Spanish, and German — in one pass — with surprising accuracy. It placed 92.7% of words within 0.3 seconds of the label, compared with 82.0% for the next best tool.
Cue’s average start error was 0.82 seconds, about half that of the closest competitor. It was more accurate than every other tool on at least 19 of the 22 songs. The potential for singing your favorite new songs at karaoke the day they’re released is huge.
Try Cue today
Cue is already behind every
Speech to Text
transcription on ElevenLabs. To use it directly, try the
Forced Alignment API
.
Acknowledgements
The work on ElevenLabs' aligner models would not have been possible without many people across the company. The team would like to thank everyone who worked on the previous version of the model, and the new one, including  co-founder and CTO Piotr Dąbkowski, researchers Danila Kozlov, Luca Lanzendörfer, Flavio Schneider, Max Levi, Tim von Känel, and Angelos Perivolaropoulos; as well as Ani Janelidze in Data Operations, our Forward Deployed Engineer and Support teams; and Lorenzo Dossi for his work on the visualization in this blog.
Written by
Mike Murphy
Blog editor and lead writer
View profile
Mike Murphy is the lead editor and writer for the ElevenLabs blog, where he turns complex research and technology into clear, compelling stories. Before joining ElevenLabs, he spent years as a technology reporter, including at Quartz, and ran content at IBM Research. He holds a master’s degree in journalism from Northwestern.
