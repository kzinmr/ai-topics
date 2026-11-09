---
title: "When Rabbit Holes Become Overwhelming"
url: "https://feed.tedium.co/link/15204/17518143/yak-shaving-ai-mental-health-effects"
fetched_at: 2026-11-09T10:11:04.354274+00:00
source: "tedium.co"
tags: [blog, raw]
---

# When Rabbit Holes Become Overwhelming

Source: https://feed.tedium.co/link/15204/17518143/yak-shaving-ai-mental-health-effects

Recently, I took on a project
that I thought would be a lot of fun … but in the end, I did not like how it made me feel. And I think it reflects the real dangers of leaning too aggressively on AI for stuff you’d like to try out.
A quick explainer: About four years ago, I got a hold of a
JingPad
, a Linux-based tablet with a massive Achilles’ heel. The problem? It was sold as a Linux-first tablet on ARM, but it was built around an SoC that was not actually particularly open. The Unisoc Tiger T510, as I’ve written, was built for Android, and it has PowerVR graphics that didn’t have an open-source driver. Worse,
the company that made it disappeared
off the face of the Earth just a handful of months after it first appeared.
The JingPad was a working, fully functional tablet that had been done dirty by its ownership and a bad engineering decision. It was a perfect candidate for the very kind of deconstruction project that has been taking the internet by storm in recent weeks.
So, my goal was this: Let’s see if I can use Claude, Deepseek, Xiaomi MiMo, and other LLMs to get this dang thing working in a modern version of Linux. Certain components, namely the proprietary GPU, might prove difficult, but using Ghidra,
Reverse Engineer Anything
(REA), and a willing-to-go-at-it LLM, it could take things down the road for me.
How hard could it be?
The good, and bad, of an insane yak-shaving project
This is an example of yak-shaving, a concept in which one project gradually evolves into numerous complex branches that never seem to end. For those not familiar, it is based on a
Ren & Stimpy
skit called “
Yak Shaving Day
,” which I’ve helpfully embedded above.
Tech projects have a tendency to devolve into wild goose chases like this, as hinted above, but this was a whole new beast to me.
Anyway, I want to make clear that this project wasn’t an outright failure. From literally nothing but an empty boot screen, we got the device to load a relatively modern version of Fedora on a “dirty” Linux kernel, based on 6.18. In many ways, it worked, complete with a working touchscreen screen, a charging battery, WiFi access, and an accessible GNOME interface. While not especially fast, I believe it is about as stable as JingOS, the software that came on it in 2022 and itself did not have GPU accelerated graphics.
There were even fun quirks that emerged as I was working on this. I got the flashlight for the camera working on the back, even though there’s literally no use case where it’d actually be useful. And I made significant progress adding FM radio support for the device, despite the fact that, like most mobile devices, FM radio support was never an actual feature of the tool. (In both cases, I thought it would be funny, even though the joke was honestly limited to just me.)
Unfortunately, getting to this point created a project that I would best describe as all-consuming. I had a swarm of different agents going at different components, different parts of the device, attempting to scrape details from old firmware versions and related projects in the hope that it’d uncover something missed previously. The result: I had to baby the damn thing all day, managing a bunch of LLMs and rebooting the device as the agents I was using went down one dead-end after another. And shockingly, the thing that kind of made the process less fun and more of a quagmire? It wasn’t the GPU, as I expected; it was the sound.
I got as far as having all the components of the sound card separately working; the DMA chip, the speakers, the codecs, and so on. The GNOME settings app even recognized that the sound card was there. But after receiving something like 50 “this is the last thing before you finally hear sound” messages from DeepSeek, I realized that I had gotten my own brain into a dangerous loop. It was nonstop dopamine hit on top of nonstop dopamine hit—the promise of instant gratification without getting gratified—and after a while, I kind of just felt mentally drained by it all.
This was a “me” project, one that I wanted to see in the world, but in the end it was kind of getting in the way of me thinking about literally anything else.
The way I broke the chain, at least for now, was simple: I put the tablet away for now. I’m going to try my best to get a healthy distance from it. If and when I come back to this project, I want to ensure I’m doing it for reasons that help me learn something rather than stress me out.
Evidence that, yes, I did get Fedora working on my JingPad.
In the right context, things like this can be good
This all sounds like a dangerous hobby. But to make the counterargument: For years, we’ve heard stories about smart devices and other objects losing support over time because a company shut down a server somewhere, or chose not to modernize them. With moves like these, we can revive these devices.
For example, the seemingly dead Hackintosh scene has actually seen signs of life, thanks to AI. There’s
now a driver for modern-day Nvidia cards
on Intel Hackintoshes. It is now possible to boot MacOS on a Snapdragon PC. And Cutefish, a new MacOS-like distro, has promised something previously thought impossible—
working graphical MacOS apps
in a Linux environment.
A decade ago, when Hackintosh was hitting its peak point in popularity, all this stuff was crazy talk. No way was this going to happen.
And to be clear, there have been other projects I’ve tried that went way better than the one above. As I recently wrote in
Boxed News
, I was able to turn Dux Shell (formerly Dank Material Shell) into
a usable TV computing experience
.
Yes, AI is capable of reshaping computing experiences in new ways, in ways that some might find
culturally frustrating
if the reason you get into tech is because of specific scenes. (I personally don’t, and think the line between cool stuff and gatekeeping is quite small.)
But I’m personally of the view that in cases like the JingPad, where this tablet would be sitting around being useless otherwise, stuff like REA could have genuine value. After all, even if I don’t end up using it to type the next Great American blog post, it can still be useful as a makeshift self-hosting device or even just a lightweight way to surf the web. And I’m hopeful that, eventually, I’ll turn this into a feature-complete device, even with the components that Unisoc and Imagination didn’t bother to make public. However …
(
Hamid Roshaan/Unsplash
)
Shave yaks? If you value your mental health, pace yourself
If there’s anything I’ve learned about myself over the past decade, I get sucked into different directions way too easily. I can get obsessed with things, and that obsession can sometimes lead to cool places. (See
&udm=14
.)
But something about the process of attempting to use AI to fix an old tablet felt kind of damaging to a routine in a way that few of my hobbies have over the years. I mentioned
Hackintoshing
before, and honestly that’s kind of what it reminds me of the most, this attempt to make something do a thing it was never meant to do. But when so much of what you’re doing is working up against something hyping up every action, it’s hard not to feel hollow at the end of it.
As is highlighted by the fact that I publish a little less often these days, I don’t use AI for any of my actual writing. I try taking my time with it. But in a world where it seems like AI is the decorative bird of technology, it can intrude in dangerous ways, with costs that don’t necessarily show themselves right away. And I’m not talking about tokens.
I’m a well-known
yak shaver
. It’s what I do. This newsletter is a shrine to yak-shaving at the end of the day. But I did not like the way I felt at the end of this week, having hit the reset button on the JingPad for the 250th time. I’m sure I’m not alone here.
My suggestion to anyone else who yak-shaves: Approach agents with caution. After all, an AI agent does not have a limit; you do. Projects like these only take and take your energy, and leave you with a broken-feeling brain.
And unlike a static code window or a page of docs, an agent can make false claims or hype up promises it can’t back up.
Yak-Free Links
Last week was utterly packed
with election stuff, which I’ll let you find yourself. But one story you may have missed last week was
the death of Salon
, one of the digital journalism OGs. Important website that deserved better than an unceremonial shutdown out of nowhere. I’m going to write more about this soon, I think.
I’m sure you haven’t asked yourself
what the guy from the “Pretty Fly (for a White Guy)” video has been up to for the past 28 years. But in case you had a poser-shaped hole in your brain,
here’s the answer
. Fun fact: He
still
appears on stage at shows for The Offspring sometimes.
As a counterpoint to the above,
let me just say that the way that firmware updates have
led synth-makers to embrace vibe coding
is genuinely interesting to see.
--
Find this one an interesting read?
Share it with a pal
! And if you need something weird in your life, I recommend the
Tedium Shopping Network
.
