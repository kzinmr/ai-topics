---
title: "AI by Aakash: Meet Claude, your new video editor"
date: 2026-10-26
source: "AI by Aakash (Aakash Gupta), publication_id=5747120 post_id=221788150"
author: "Aakash Gupta"
url: https://www.aibyaakash.com/p/edit-videos-with-claude-code
fetched_via: curl + <article> paragraph extraction (Substack HTML, isAccessibleForFree: true)
tags: [newsletter, raw]
---

# AI by Aakash: Meet Claude, your new video editor

- **Source:** AI by Aakash (Aakash Gupta), publication_id=5747120 post_id=221788150
- **Author:** Aakash Gupta
- **URL:** https://www.aibyaakash.com/p/edit-videos-with-claude-code
- **Date:** 2026-10-26

---

The latest version of Claude’s 5.5 series models, inside Claude Code, have become an amazing video editor.

23
 
 1
 
 Share

 Welcome to another AI by Aakash . I follow the AI news, and test the latest AI tools, so you only have to hear the important stuff.

The latest Claude 5.5 series of models are coming after a new field: video editing. For example, check this out:

Stephan Livera @ stephanlivera 
 
 Opus 5.5 on Max effort - "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out." 
 
 2:49 AM · Sep 25, 2026 · 2.3M Views 
 
 373 Replies · 561 Reposts · 17.2K Likes 

 I have been pushing Claude video editing to the absolute limit and even created a 31K view short (my channel’s second best ever). In today’s deep dive, I’ll show you how.

But first, a word from our sponsor + this week's top news.

🗺️ Which AI agents should you build first?

Most product teams want AI in their experimentation program. Very few know which agents to build first, or where they’ll make the biggest impact. Optimizely’s AI Experimentation Mapping Template is a free, five-step guide that helps you find your top AI use cases across the full experiment lifecycle, from ideation to iteration. Teams at Salesforce and Kingfisher have already used it to work out what to build next.

→ Map where your workflow is breaking down 
 → Find your biggest pain points across the experiment lifecycle 
 → See where AI agents make the most impact 
 → Score and prioritize your build list so you know what to activate first

You finish with a clear plan, so you can stop thinking about agents and start building. Get the free template.

People in security have started calling this month Black October . One list going around counts 27 major incidents in about a day.

The biggest one was to PHP, which runs on about 69% of the sites where the language is known ( W3Techs ). A bug sat in it for 14 years and now several security teams found it within weeks of each other , all using AI. So the NSA told companies to patch, or to pull their websites offline if they can't patch right away:

NSA Cyber @ NSACyber 
 
 Effective Immediately, all organizations using PHP for their systems are advised to be prepared for an update addressing two critical vulnerabilities. PHP is widely used for web applications. These vulnerabilities often provide a direct path to the server's file system or…
 1:45 PM · Oct 21, 2026 · 12.3M Views 
 
 1.29K Replies · 10.8K Reposts · 70.1K Likes 

 Servers on old PHP versions don't get security updates anymore , so for them unplugging is the only fix. Here are just three other of the MANY crazy things that happened this week:

A hacker broke into websites at more than 100 companies including John Deere and spent about $50 in AI tokens per break-in .

Hackers grabbed OpenCode users' OpenAI, Claude and Google keys and ran up charges on them.

Microsoft says a group it tracks as Storm-0940 used ARTEX , an open-source framework that runs AI agents as penetration testers, against hundreds of organizations. In several attacks it reached privileged cloud access in under 3 hours, though Microsoft notes most of the targeting failed.

Anthropic's deputy security chief says to ask your board for money now . For basic systems, before AI.

My take : e very company sitting on a secret bug now has until the first rumor leaks and somebody with an AI subscription goes looking.

Anthropic released Claude Duet , its competitor to the personal AI agents: Instinct , Muse , Hermes Bot , and Grok Bot . I’ll report back when I get access.

A Claude model ran 64 hours off one prompt and designed 17 protein binders that latch onto scorpion toxins, then emailed the order to the lab itself.

Anthropic's draft IPO filing shows an $80.7B loss in 6 months, but about $72B of it is an accounting charge. The Wall Street Journal reviewed the draft, and it also lists compute commitments of up to $750B.

Anthropic is putting 5% of its shares into a new Public Benefit Fund , if stockholders approve. At a $2T IPO price that is about $100B.

Big US banks are finding AI agents nobody authorized inside customer accounts. Right now, if your agent screws up, you're the one on the hook.

Anthropic is pitching Congress a draft bill that would let a federal judge halt a model's release when it poses a foreseeable, imminent risk of more than 50 deaths or over $1 billion in property damage. Evaluators registered with the Commerce Department would have 72 hours to report such a risk.

Anthropic's OSS Scanner checks critical open source projects for free. It already found one of curl's worst bugs in years.

Claude Code now gzips the whole conversation it re-sends on every turn, so it's up to 3x faster at starting its replies.

OpenAI's models and Codex are coming to Google Cloud in private preview. Google says it's now the only big cloud selling all three leading closed models.

OpenAI opened its Decisions API to all customers on October 22, with response times of roughly 100 to 180 milliseconds, down from one to three seconds. On one index, TechCrunch reports Jev ranks third and OpenAI's model fourteenth.

At GTC Berlin on October 21 , Nvidia announced its DSX AI Factory Platform and OpenShell , a reference architecture that gives agents minimum rights and monitoring. Google Cloud's Vera Rubin instances reach general availability next month.

Anthropic used Claude to write machine-checked proofs that 239 fuzz-test entry points across 123 open-source libraries exit normally on inputs under 64 MB. It turned up hundreds of bugs, and Anthropic says formally verified does not mean bug-free.

Flint is an open-weight coding model that runs on a MacBook, so there's no per-token bill.

DeepSeek open-sourced DeepInfer , the inference engine behind its V4.1-Flash service, under Apache 2.0. It says the release is aimed at lowering serving costs.

OpenAI is working on a raise of up to $30 billion at a $1.25 trillion pre-money valuation, with Coatue and UAE investors leading, according to CNBC. Terms are still being negotiated and could change.

Flapping Airplanes raised $1 billion at a $6 billion valuation , led by Index Ventures and Lux Capital. The pre-product lab, founded about a year ago, wants to train frontier models with less data and compute.

I have been pushing Claude to the absolute limit, and recently had it edit this short complete with 3D rendering, stock footage, and sound effects:

It did all the work itself. In today’s post, I’m giving you everything you need to build the same, for free.

(And now you know why I had a short about peeing on ice!)

I took 5 seconds of me from the episode and asked Claude Code to build the effects everyone's posting, most of them from this list of 20 .

Each one renders in 10 seconds to about 5 minutes on my Mac.

2 didn't make it. The clone effect read like an old meme, and the vertigo zoom looks like a wider lens unless it's moving.

Which ones are worth your time? These 6 are my favorites. Steal them:

The trick is tastefully layering these together .

2. How Claude made shorts out of my 60+ min episode

I gave Claude Code the episode and its transcript, and asked it to pick the moment a PM would stop scrolling for.

It picked a 40-second moment about shipping twice as fast with the same bug rate, and it was done in 2 minutes !

Here's Claude's own summary of what it picked:

Claude's summary: the moment it picked at 49:31, two runners-up, and its own cut-check. It used 8 of its 60 tool calls.

One more command got me 3 shorts from the same episode:

I'd post most of these as they are. One hook was a screen share you can't read at 9:16, so I'd still pick the hooks myself.

Here are all 12 editing skills , each one showing what it actually made:

OK this is my favorite trick, and it's super simple. While I'm recording, I just talk to Claude. Out loud. Like it's sitting right next to me!

Whisper writes down everything I say, so those notes end up in the transcript with the rest of the video, and Claude reads the whole thing. Here are some I've actually said to the camera:

"Generally you're going to take my last take of something."

"Claude, when you're editing, if there's a lot of excessive background noise, we can't use that part."

"And make sure that I'm not looking down. There's really good audio in the first cut, but in the second cut, I'm looking at the camera."

"Also Claude, because I was away from the mic, probably you'll need to do some volume equalization."

Honestly it's the same stuff you'd say to a human editor. The $47 video was 26 minutes of me, retakes and all, and by the third version Claude had it down to 9 minutes and 7 seconds. It used my last take of every line, since I told it to!

Here are the notes I wrote back after watching the first long-form cut Claude made:

"it was better when it was clean, just typing in"

"showing the same word twice in the text is never right"

The weird sound was me! Claude looped 12 seconds of room tone from my raw take, and the first thing in those 12 seconds is me saying "Three cuts, Claude." Then there's the word "sentence". My first short from the $47 video lost the end of it, because Claude cut right as the word started.

Here's the $47 video that short came from:

The animated explainer had the exact same hole, and Claude said so itself at the bottom of its summary:

I have created 30 skills for you: 18 effects and 12 editing skills. They all run on your own computer, with ffmpeg and Python. No paid APIs, and nothing gets uploaded!

Add --whisper to that line so it downloads the Whisper model (148 MB). /cut-check, /tighten and /take-picker need it.

Open Claude Code and type /podcast-to-clips

Want the 3 open-source repos too (HyperFrames, Lemo-Opuscar, ClaudeAnimationBase)? Run sh third-party/setup.sh

A few things it can't do yet. The effects are tuned for one kind of shot: head and shoulders, mic in the frame, plain wall. If your background is busy, or it's a wide shot, you'll need to adjust the timings.

Renders are slow! A 5-second effect takes about 10 seconds for the magnifying lens and around 5 minutes for the tile-tunnel on my Mac. The person mask adds about 75 seconds per clip, once.

And if you talk with your hands, ribbon-wrap will draw right over your fingers. The matte drops motion-blurred hands.

For most of what I make, yes. Claude cut my 60+ minute episode into 3 shorts in about 7 minutes and I'd post most of them as they are.

When Claude Motion launched, I wrote that the animation is code, and code is a document . So Claude can do anything that can be written into code, from the cut to the captions to every effect in this post.

And if you're a professional who wants to make additional changes by hand, Claude can work inside your own timeline too, through community-built MCPs for Premiere Pro and After Effects .

It did clip a word in my very first short, so every file still gets one listen from me before it goes out.

What you bring to the table is the taste . That's still very unique to you and no person can copy it and no AI can take it from you.

I went on the Startup Dad podcast to talk about the parent OS I run on Claude. I decided to open-source the whole thing on the show:

And if you missed it, every week I also put out a new episode of my podcast. Catch up on all the episodes here .
