---
title: "SFX v3 API: generate sound effects from multi-part prompts"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/sfx-v3-for-developers"
scraped: "2026-11-03T06:00:52.132888+00:00"
lastmod: "2026-11-02T15:31:38.976Z"
type: "sitemap"
---

# SFX v3 API: generate sound effects from multi-part prompts

**Source**: [https://elevenlabs.io/blog/sfx-v3-for-developers](https://elevenlabs.io/blog/sfx-v3-for-developers)

Blog
Introducing SFX v3 for developers
Written by
Tadas
Petra
Published
Nov 2, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Learn more
On this page
Introduction
Model ID
How to prompt
Test both models
Try SFX v3
Today, we're releasing SFX v3, our newest sound effects model in the Sound Effects API. It follows prompts with multiple instructions more closely than SFX v2, and handles vocals and music better. To try it, set
model_id
to
eleven_text_to_sound_v3
on the POST
/v1/sound-generation
endpoint.
Model ID
To update to the new model, simply update the model ID:
from
elevenlabs
import
ElevenLabs

elevenlabs = ElevenLabs()

audio = elevenlabs.text_to_sound_effects.convert(
text
=
"Football crowd cheering, hearing a ball drop, crowd booing"
,
model_id
=
"eleven_text_to_sound_v3"
,
)
The model picks the length of the sound effect based on the prompt. If you need specific timing, set the duration_seconds to your desired time.
If outputs drift from what you asked for, raise prompt_influence above its default of 0.3. Higher values follow the prompt more closely and vary less between generations. The output_format query parameter sets the codec and sample rate, such as mp3_44100_128 or pcm_48000.
Looping currently only works with eleven_text_to_sound_v2, so if you need that for your request stick to the v2 model with loop: true.
How to prompt
SFX v3 is great at multi-part sound effects. To get the best out of the model the order of the prompts matter. List events in the sequence they should happen, such as: "Footsteps on gravel, then a metallic door opens." For a single sound, a short, concrete prompt works best.
Wording matters too. One of our testers found that "a couple arguing in French" worked much better than "a couple fighting in French." Try a few phrasings of the same event before you lock one in.
Test both models
SFX v3 is an incremental update. It's less likely to clip on high-frequency sounds like gongs, chimes, and kettle whistles, and our engineering team says it sounds more natural overall.
Because both models run on the same endpoint, an A/B test is cheap. Run your most common prompts through both v2 and v3 to compare the results before you switch.
Try SFX v3
Check the
Create sound effect API reference
for the full parameter list, then send your first v3 request. If you'd rather hear your sound effects before writing code, they’re also in the Sound Effects tab, Flows, and Studio in
ElevenCreative
.
Written by
Tadas Petra
View profile
Tadas Petra is a Developer Relations Engineer helping developers build with ElevenLabs product suite. He is also the founder of Hungrimind, a developer education platform. Previously, he was a Lead Developer Advocate at Agora and an instructor at Zero To Mastery.
