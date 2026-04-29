---
title: "AI software I'm surprised doesn't exist yet"
url: "https://grantslatton.com/ai-software-nonexistence"
fetched_at: 2026-04-29T07:02:16.097306+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# AI software I'm surprised doesn't exist yet

Source: https://grantslatton.com/ai-software-nonexistence

AI software I'm surprised doesn't exist yet
State of play
I'm writing this on 20 February 2025. It's been:
4.5 years since GPT3
2.5 years since DALLE-2 and StableDiffusion
2 years since ElevenLabs voice cloning
1.5 years since Llama 2
1 year since Suno AI music
3 months since OpenAI o1
The good
I don't like to be overly pessimistic, so I'll start by listing a few applications of AI that
do
exist that I'm impressed by:
Chat
This goes without saying. The chat models continue to get better. I use them every day. The recent batch of "reasoning models" (OpenAI o1, DeepSeek R1, etc) has been even better. I pay for o1-pro and it's the first model that I actually find
professionally
useful (not just hobby hackery).
Translation
Kind of a subset of the text modality described above, but worth calling out on its own. I view translation as essentially solved except for the most artistic of cases (e.g. translating poetry, high-literature, etc).
Transcription
Speech to text is really, really good now, start with OpenAI's Whisper model and a few others since then. There's still some room to improve — I once tried to transcribe all of the Seattle police/fire radio and the low quality radio static made it not accurate enough to be reliable. So not human level yet, but totally amazing for non-adversarial environments.
Code copilots
Github Copilot, Cursor's Copilot++, etc are all wonderful productivity enhancers that provide way more value than they cost. Even if you just use them as "great context aware autocomplete" they save at least several minutes per day, hours per month — this is worth hundreds of dollars at typical software salaries.
Music
Suno AI, Udio & friends — pretty decent AI music that is getting better every release, totally great for "infinite lofi" or "cafe jazz" type stuff. I recently listened to an hour of background jazz on a YouTube playlist, not realizing once it was AI generated.
De novo image models
Midjourney, Flux, etc are all great at generating great images from text. They still aren't great at
edits
or
iteration
of those images (more on this below). But are great for that one-shot use.
Self-driving cars
Waymo, Tesla, and Comma AI are all crushing it. There are some Chinese companies I know less about that I'm also told are doing great. I fully expect my kids to never learn to drive. Tesla FSD drives about 90% of my miles and gets better every release.
Honorable mentions
Other things I'm excited about, not
yet
blown away by, but also didn't expect to be blown away by at this point:
Humanoid robotics (Tesla Optimus, Figure, Clone, Unitree, etc) — these are developing fast, the bottleneck is now squarely in the software court, mostly held back by great training data for the particular hardware
Video generation (Sora, Runway, Veo, etc) are steadily improving but still not ready for prime time
End-to-end app development (Lovable, Replit, etc) are now pretty good for small apps without too much surface area, i.e. the kind of thing with a simple UI on top of a <= 1000 line backend
Probably many others I'm forgetting.
What doesn't exist
And now to the point of this post. Here is stuff I feel like should be
relatively
straightforward to build, but doesn't exist or isn't anywhere near the quality I'd expect.
Microsoft Paint with AI Infill
There are a few AI image editors.
There was
Playground
that was an AI image editor, but I'm learning as I write this
apparently pivoted
to just AI design recently.
Then there's
Krea
which seems to be pretty similar to what Playground was. I'm going to pick on it for a second, even though I'm sure it's a great tool for many cases, because it illustrates what drives me crazy about this whole genre of tools.
A year ago I wanted to edit this long-haired photo of me to reflect my current shorter cut. People I met online and later got coffee with were surprised I didn't match my profile picture. I figured this would be a great way to test AI image editors.
I expect I'll be able to load the image into an AI editor, erase my long hair, give a prompt like "man with short messy hair holding a corgi" and voila.
So I load this image into Krea and use the "cut" tool to select my hair. But I can't actually select all the strands, just the bulk of the hair.
This is a problem because when you try to inpaint, the spare strands mess up the inpainting model. Undeterred, let's select a large region around it and try the generation function anyway:
This is the result, probably due to the straggler hairs getting included in the input? But there is no way to remove them, so I'm out of luck.
This should not be hard! We have had great diffusion models for years now! And I know the technology exists, because I was able to successfully give myself an AI haircut with the
Replicate Playground
which is just a janky frontend to one of the inpainting models they host.
The closest thing to an actual solution here is
Dingboard
which is mainly geared towards quickly hacking together memes, so it's a little hard to produce something with a bit of polish.
Truly, all I want is 1990s Microsoft Paint tier UI where I can cut, copy, paste, delete, and use a paintbrush tool to AI inpaint. Why does this not exist?!?!?
This one has been driving me so crazy for over a year now, I actually made my own for personal use. It works great! And only took like 2 hours to make! ChatGPT wrote the whole thing! It's like 500 lines of code!
And my AI haircut came out great! Looks just like my real hair.
I am completely blown away that this product doesn't exist. If anyone wants to produce a slightly more real version of my hacky 2 hour project, I will pay money to use it. Just do like whatever Replicate charges for the flux-fill-pro model + 20% or whatever. Easy money!
The same tech can also be used to easily splice people into group photos, edit objects out of photos, etc. You really only need cut, copy, paste, delete, and infill for a 99% solution to everyday photo editing.
Spaced Repetition Assistant
I want to love
spaced repetition
. But I have an ultra-low tolerance for friction. It's one of my biggest personality flaws. And creating spaced repetition cards is friction.
I suspect there are a few million other nerds in the same category. They've heard of spaced repetition, they know the benefits, but it's just too much work.
AI can solve this. I want a browser extension that I give prompts about the kind of stuff I want it to create flashcards, how I want the flashcards to be structured, and it just creates them for me in the background as I browse.
E.g. I could give it prompts like "I want to remember…"
the start and end years of all historical wars I read about on wikipedia, and the powers involved
what city anyone I follow on Twitter lives in
the type signature of any Rust library function I visit more than 5 times
Then I could just click my browser extension icon at the start of every day and review cards and that would be that! Zero friction spaced repetition!
You'd also want some ad-hoc features so I could e.g. click the browser extension icon, click "record" and then say aloud "remember xyz's birthday is February 25th", and it would create the appropriate card.
In addition to creating all these cards automatically, it would record the context (i.e. source material) the card was created from so you could always link back to where you learned something, amend the card, etc.
This product is a little more niche than the AI Paint suggestion above, but probably could still make a lifestyle business out of it. It dominates Anki.
AI TikTok
TikTok is famous for its algorithms tuning to the user's desires. You may not know you really wanted to watch 4 hours of juggling videos, but TikTok sees that twinkle in your eye and will figure it out for you.
So now that AI image generation is pretty good, at least for certain classes of images, I'm surprised there isn't a popular app that has the same swiping mechanic as TikTok, but all the content is AI-generated, and it has an algorithm that quickly learns what you want to see more of.
I remember when the first round of AI image generators came out (DALL-E, StableDiffusion), people reported spending
hours
clicking the "generate" button when they found a prompt that produced really cool stuff. It has the same dopamine characteristics as a slot machine — variable reward, tight feedback loop.
So I'm not really sure why something like this hasn't taken off. Even for some particular vulgar niche like pornography. I'm sure there are degenerates out there who would pay money for an infinite feed of "Ethiopian bikini babe on motorcycle" or whatever their particular thing is.
Maybe it exists and I just don't know about it (I'm not the kind of degenerate who'd be a customer…).
I have a $100 charity bet with Emmett Shear that such an AI TikTok app will exist with 1 million monthly active users by mid 2027, so we'll see. But I'm surprised I haven't already won! So there's something I don't understand.
Actually good AI audiobooks
At the end of 2023, I predicted that AI audiobooks would be great by the end of 2024:
I was totally wrong! Not on price — that has come down to less than $100 for an audiobook-length text-to-speech — but on quality.
All existing text to speech services have far too little emotional range, and, equally importantly, cadence range. Real human speech has a surprising amount of speeding up and slowing down that communicates a lot of information.
Services like
ElevenLabs
and OpenAI's voice offerings are totally fine for reading emails and making websites accessible to the blind, but way too monotone and monotempo for longform.
The thing I really don't understand is audiobooks are literally among the best training data that exists for AI. You have:
Super clean, curated data
Perfect ground-truth (the exact original text, and easy to line up the text to the audio with transcription models like Whisper)
Millions of hours of data
It should be
totally straightforward
to train such a model. That
Suno
can generate songs with a lot of emotional, cadential, and stylistic range exhibits the point. Singing isn't too different from audiobook narration from a difficulty point of view.
Another piece of evidence that this is technically feasible is that
Google NotebookLM
can generate a fake podcast interview about whatever topic you want. The podcast hosts have
much
better mastery of cadence than most text-to-speech systems. They are, unfortunately, stuck in "NPR interviewer" style, though, so not appropriate for audiobook narration.
And, finally, ChatGPT 4o voice mode, before being trained not to, is
capable of cloning anyone's voice
with just a few seconds of audio. I can't recommend enough to listening to the 42 second clip in that link. The generated voice has all the cadence and tonality of a real human. If only they had used it to narrate an audiobook!
So I'm actually baffled that this product doesn't exist. I have a few, completely unsubstantiated guesses as to why this might be the case.
It could
actually
destroy the audiobook narrator job market. Audiobook narrator is as close to a black box job as you can get. Author sends a book and perhaps some directorial instructions to the narrator, the narrator sends back some mp3 files. It should be straightforward to ~entirely replace the human in the black box.
This is different than using AI for coding, illustration, etc, where the AI is a
tool
used by human professionals. This is a task that has the potential to be
completely
replaced.
And no major lab wants the bad press of being the first one to destroy livelihoods. The total market size is < $10B/yr, so it may simply not be worth the trouble.
The other source of trouble is legal. All the training data is owned by big media companies that are hyper-litigious. Best not to upset them, particularly for such a relatively small market. That said, Suno almost certainly trained on copyrighted music, and various image models on copyrighted images, so I don't know about this one.
I still expect this service to exist any day now — and can't wait to be a customer! There are loads of old books in the public domain I want read to me.
Conclusion
I'm sure after I post this I'll think of some more, but these are the first that jumped to mind. Please someone, build these!
