---
source: https://karpathy.bearblog.dev/hacker-tube/
author: Andrej Karpathy
published: 2026-10-31
collected: 2026-11-01
type: article
sha256: 4ac20e51334bc58c4e1ddf33ce54f48368c683c6458b6d77101650010a96de7a
---

HackerTube

karpathy
Home Blog

HackerTube

31 Oct, 2026

It was Friday night at 11pm, I was tired, I went to YouTube to watch something and realized that I was looking at an enshittified wall of slop. Insanely exaggerated thumbnails, dumb recommendations of the same tired topics, truly terrible idiocracy-grade content. I'm sure this algorithm works well for the median person on the internet, but it definitely does not work for me. So this morning (Saturday) I took a hold of my Opus 5.5 and gave it the task: Let's write our own YouTube clone based on whatever videos have been recommended on Hacker News. And Opus came back with: hackertube.org !

Opus downloaded all comments of HackerNews, filtered them, ran Sonnet over them in a Workflow (Claude Code feature), got rid of spam, and narrowed everything down to 40K comments recommending a YouTube video. In total, we get 6,454 YouTube videos that have been recommended by a few people on HN from 2007-2026 across 150 topics. Then we wrap it up in a YouTube UI, get a domain, push to a VPS, secure, harden, optimize and voila! HackerTube:

Contains quality content
Uses the 50% thumbnail instead of the uploaded thumbnail
Custom and good ForYou recommendations without any user accounts, storing state in local browser session
Keyboard shortcuts
Export of the site's data available to give to your agent to easily create your own version

This takes ~2 hours now. I can breathe again. Thank you Opus 5.5

EDIT: A little bit more on my process. I use Claude Code (desktop app for Mac). I use Opus 5.5 on Medium effort as my default. I don't actually do anything resembling traditional engineering anymore (read/write code, run commands in a terminal, or etc.), I only talk to Claude and have it do everything. In this case, the only "manual work" I did was: 1) I had to create some kind of API key from Google Cloud UI to query YouTube for video metadata, 2) I booted up a VPS box and 3) I bought the domain name. I worked on this in between Claude's actual work so it still feels a little bit like team work :) Once the box was up I gave Claude the IP and told it update, deploy, secure, harden and optimize the code, and it did the whole thing.

---

## HN discussion highlights (item 50319510, 1453pts)

[karpathy] I'm on subscription but I had Claude add it up: 504M input tokens (90% cached), 7.6M output tokens. 90+% of that was Sonnet calls to label the comments, all of the actual work, the app and deploy etc was ~1M tokens of Opus 5.5, I compacted context once. i.e. very small project by modern standards.

[karpathy] I didn't publish the server because it's a vibe coded mess, but if you point your Opus 5.5 at the zip and ask for YouTube-like site it will be basically instant. This part was like 3 min. EDIT: one caveat is that i couldn't distribute the YouTube data so you'd have to create a (free) API key for that part. Luckily it's only ~1 min of hassle.

[privacyishuman] I like this a lot. I was just thinking about a site where you could share your YouTube cookies and then use anybody's curated algorithm because you can curate it quite fast in signed out mode.

[mentalgear] Appreciate the effort, yet I think there is a place this is needed even more: "an enshittified wall of slop". Please do the same thing on Social Media: Facebook, 'X', reddit, instagram, etc. Maybe find a 'hacker signal' that identifies quality content across those platforms and have them aggregated for the public.

[jumploops] I'm always surprised how bad YouTube's recommendation algorithm seems to be. It will suggest the exact same content/topic. TikTok's recommended content is miles ahead, much more difficult to close.

[globular-toast] Bad by what metric? They're interested in getting you to watch ads, they couldn't care less what you want.
