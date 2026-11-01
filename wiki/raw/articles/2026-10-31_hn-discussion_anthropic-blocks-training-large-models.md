---
title: "HN discussion: Anthropic blocks users for anything touching training larger models"
url: "https://twitter.com/jiahaoshao1/status/2116475922190922088"
date: "2026-10-31"
fetched_at: "2026-11-01T11:10:00+00:00"
source: "hn-algolia"
tags: [blog, raw]
extraction: partial_hn_comments
source_note: "Primary source is an X post (jiahaoshao1) not scrapeable; raw captures the HN discussion thread (367 pts, 209 comments, item 50319358)."
---

# HN discussion: Anthropic blocks users for anything touching training larger models

Source: https://twitter.com/jiahaoshao1/status/2116475922190922088

TITLE: Anthropic blocks users for anything touching training larger models
URL: https://twitter.com/jiahaoshao1/status/2116475922190922088
POINTS: 367 AUTHOR: pretext CREATED: 2026-10-31T19:39:19.000Z


--- nubinetwork (depth0): Kindof old news, they've been doing this for months...

--- pkoird (depth1): Better block than falsify information. Last I heard they were deliberately botching it whenever someone asked semi-advanced questions on model training.

--- tristanj (depth0): This user is based in Hong Kong, where Claude is geo-blocked and not available. If you try visiting claude.ai from a Hong Kong IP address, you get an "unavailable in this region" message.They are likely accessing Claude via a VPN. Doing model training work over a VPN is a highly suspicious signal, and likely triggers Anthropic's classifiers. It's not surprising that their account got flagged.

--- leobuskin (depth1): US/EU here (both, due to traveling), same story with anything related to modifying existing weights or SotA approaches in training/research, it's not a geolocation issue. The safeguards don't check your IP (but pretty soon will check someone's IP [pun intended])

--- tcdent (depth1): Claude has been building me a bespoke inference and training stack (optimized kernels and all), feeding traces from my previous sessions directly into a LoRA adapter. Zero friction.I am US based, with defender level cyber access.

--- arjie (depth1): The geotargeting is iffy. I accessed it accidentally from HKG Airport WiFi with no trouble. Your point probably still true. Just adding an anecdote.

--- giancarlostoro (depth0): I have been using it to train a few BERT models.

--- alansaber (depth1): I doubt BERT would trip safeguards

--- WhereIsTheTruth (depth0): US Security Chip act next, your GPU will soon enforce these restrictions too

--- skeledrew (depth1): Nice. Push more people to use Chinese chips.

--- gdiamos (depth0): Where I draw the line is asking Claude to label training data. I don’t do this.I ask it questions about large models like big MoEs all the time. I’ve never had it refuse a question, but I would expect it to refuse sometimes.For training data from existing models I just get open models to spill their guts. It’s fineIn industry we train employees to not reveal proprietary information.I think it would be easier to do this for a model than a lot of employees

--- cisc (depth1): > Where I draw the line is asking Claude to label training data. I don’t do this.Why draw any line? Anthropic doesn't. They actively take the world's intellectual property, don't pay for it, and put it behind a paywall.> but I would expect it to refuse sometimes.Why? Anthropic's dream is to be exempted from copyright altogether. They've been trying to achieve exactly that:https://www.theguardian.com/technology/2026/oct/02/anthropic...Given they want no restrictions on them, why should there be any restriction on anyone else?

--- arjie (depth1): Strangely I do that quite often. When my personal agent fails at a browser task, I have Claude browse the page and rebuild it as an eval and then run an iteration loop in Claude code. Just does it to prompt Deepseek.

--- ktosobcy (depth0): > You built your models on the world's datamost important bit…: stealing world's data…

--- jquery (depth1): You wouldn't download a car

--- mapontosevenths (depth0): I'm using it to train models with a novel linear flash attention mechanism right now. No refusals, and it's been running for at least a week solid.I suspect this person was actively using it to generate or classify training data directly.

--- JBits (depth1): What sort of data are you getting Claude to generate?

--- clcaev (depth0): Perhaps a manifest index/list of training data and learning method should be mandatory for “public” use of any model, sort of like food ingredient package labeling. The list of texts used and any weighting seems important to facilitate a public understanding / debate of model expectations and behavior.

--- dcl (depth0): Will Claude help me with reinforcement learning code for games? Or is that too small-fry for it to refuse? I've been playing around with RL with the new DeepSeek Flash model but it seems to trip up over itself a bit.

--- silentkat (depth1): I have been doing RL for Magic the Gathering (longshot but having fun). Several times it triggered this flag. But that was a couple months ago. Everyone went crazy over Astra so I switched to open ai and had no issues. People are now going crazy over opus 5.5 so I’m playing with that.Haven’t hit any issues so far, but two months in the code is very dirty but functional enough that I’m redoing it with more heavy hand holding.I recommend having a paper as reference in mind if you don’t already know what you’re doing. I’m referencing the Stratego paper as reading that a year ago gave me the inspiration to try MTG.Every model I’ve used has had a lot of trouble but if it wasn’t I figure I wouldn’t be having as much fun as I’ve been having or learning so much.

--- schleck8 (depth0): This is not a ban, but the Opus 5.5 "safeguard" interrupting a query.

--- fragsworth (depth1): Yup, this is a whole bunch of nothing. The guy did not get banned, he's just stuck in a bad session and needs to hand it off to a new one.Classifiers trigger on the wrong things sometimes, it's really not that big of a deal, you just try again with some rephrasing

--- byte_0 (depth0): This week, I asked Claude Code to generate an MD to continue working on another computer, without losing the context, and it refused claming some sort of extraction. It was only until I selected Opus, that it completed the request.

--- Buttons840 (depth0): If anyone out there wants to pay for my LLM bill, I'll record and send you all the outputs they generate in exchange (perhaps with some exceptions).I mean, these AI companies have money, and they want data. I have data, and I want money. Maybe we can work something out.In a world where buying and selling data is central to entire industries, why shouldn't I gather and sell my own data?

--- cft (depth0): There have been a lot of write-ups about the future of AI. I see two distinct futures:1. You get ID'd and biometrically scanned to be able to use powerful AI, and after you get de-platformed by an opaque censorship system, you are a digital bum. Same life as homeless now: they cannot even open a bank account because they don't have an address.2. Local models win, perhaps with the assistance of Apple, and people run suffiently powerful models on the client computers.My bet is on 1.

--- gattr (depth1): 3. LLMs are fully commoditized, your country funds training of SoTA models, your town runs them in the municipal data center; everything tax-funded. You can use them for a modest fee, as easily as taking a train. When interacting with those LLMs, your privacy is guaranteed by law.

--- tarpitt (depth0): Holy shit man the lockdown is coming. I've used claude to set up my abliterated qwen local LLM setup, but they're gonna eventually lock that down too.I wanted to finetune it a bit, I wonder if I am gonna have to dogfood if claude refuses to help me.If you don't have a local LLM setup you're gonna be permanant local LLM-less underclass.

--- _3u10 (depth1): There’s models other than Claude.

--- jaekwon (depth1): you will appreciate gnosh.ai.

--- zmmmmm (depth0): It's very clear to me that however much you like Claude and Anthropic models, every professional user shoudl be actively cultivating a set of alternatives and fallbacks to use and seeking to ensure the overall ecosystem is as open, standardised and portable as possible.Anthropic is highly opinionated, dogmatic and idealistic. They have made a pragmatic decision already to cut loose a whole swathe of users so they can pursue areas higher up the value chain. that was essentially the original decision they made when they went after software engineering instead of general users. The fact they are repeating this over and over by continuing to carve out sets of users and usages they don't want reinforces this as a persistent core principle rather than a single pragmatic business decision.What th

--- nicce (depth1): They keep doing anti-competitive things over and over again, and the end users seems to refuse to see it. They do whatever they can to get vendor-lock in.

--- pj_mukh (depth1): What’s the best local analog to Opus 5.5? It’s such a great daily driver.

--- neya (depth1): It's not just the anti-competitive behaviour, it's also the anti-privacy behaviours that are not muched talked about. They embedded a spyware and got caught too:https://thereallo.dev/blog/claude-code-prompt-steganographyBut, of course, Dario is the darling of the community and he can do no wrong.

--- anal_reactor (depth1): I don't care about my skills because employers won't request me to do anything that violates the terms of service of $CURRENT_LLM. At the same time, it's a reminder not to outsource thinking to someone's computer.

--- amelius (depth1): Things are about to get even shittier in the near future, when shareholders get involved.

--- 7e (depth1): Anthropic is acting like any regular selfish corporation despite their PBC status. They are becoming a stain on humanity. Power will corrupt anyone, it seems. We shouldn’t let Anthropic have any more of it. Distributed power is good; concentrated power is very bad.Anthropic tells themselves that only they can steer AI towards a positive future for humanity. But that’s nowhere near close to being true. Humans are quite genetically homogenous and good humans exist everywhere. Groups that will keep AI beneficial have popped up (and will keep popping up) everywhere, spontaneously.The danger is actually concentration of AI power due to its corrupting influence, and that is where Anthropic needs to be kept in check. Keep AI democratic through decentralization of power. Oppose Anthropic.

--- 8note (depth1): idk i think theyre less idealistic and more monopolistic.if they think their model is the best at making things safe, then their model should be helping train at any chance, to embed the same safety into new models

--- dannyw (depth1): Fortunately it is not a one horse race. GPT 6.1 Sol is an excellent model, sure it has some weaknesses (e.g. frontend design), but it also has strengths too (e.g. computer use / control; which is great for automated E2E QA).On software engineering I find it's generally close enough to Opus 5.5 where it's more situational and even personal preference / skills / prompting style on which is better.Most importantly, while neither company are saints, I don't curse at OpenAI models for classifiers anywhere as much as Claude models.

--- Beached (depth1): For those who do not play with Local AI much. Qwen4 was announce to be released the first week of Nov. The preview for qwen4 is currently one of the best local models you can use, and is roughly opus 4.6 quality on local hardware that costs 3.5k-4kMany people are expecting it to sit somewhere above Opus 4.8 to opus 5 (not above, but the unquanted version of their largest model is expected to perform around here)Anyone who cares to keep their current capability should definitely be looking at localAI and using it for at least their more routine tasks , even if it is qwen4 27B quant 4 on their gaming rig.

--- Bender (depth1): actively cultivating a set of alternativesAbsolutely.  I have been [cyber]'d so many times even Claude jokes about it now.  Claude is great but it's operators are making it unreliable for me.  I have moved one of my projects elsewhere and will move the remainder tomorrow as a stop gap until I get the right hardware set up to run abliterated local models for some percentage of my needs.  Their message has been received loud and clear.

--- _HMCB_ (depth1): Now do OpenAI.

--- xpct (depth1): To the dismay of frontier labs, swapping models is actually very basic. What takes time is only acclimating to the capability changes since they won't all change linearly.

--- itkovian_ (depth1): It’s not professionals that need to something- it’s absolutely critical we have some kind of credibly neutral body providing the actual models. What’s not clear at all is how to do that since it’s such an expensive activity.For now we have a great situation with the open weights, but there is absolutely no guarantee that continues, and more the opposite- they may stop.

--- andai (depth1): They want to do one thing and do it well.Well, arguably so does OpenAI, but their one thing is "assimilate all life forms into the Borg."