---
title: "Duet is the future of chatbot interaction"
url: "https://fig.blue/posts/duet-is-the-future"
published: 2026-10-29
fetched_at: "2026-10-30T11:20:00+00:00"
source: "fig.blue"
tags: [blog, raw]
scrape_status: "full"
---

## Duet is the future of chatbot interaction

Oct 29, 2026

Written by a human. Not affiliated with Anthropic.

Look, I really didn’t want to like Duet. I don’t want to be an Anthropic fanboy and it annoys me when they do things better than the competition. But they have done it again.

I have given serious effort to Muse, Dot, NanoClaw, and a host of other personal-assistant-type harnesses. Duet is the first one that felt more useful than tedious, and it feels like a serious evolution of the chat experience rather than another “give me all your credentials to be useful” agent. Here’s why I like it so far.

## 1. It’s fast

Other assistant apps are always doing who-the-hell-knows-what in the background while I wait for a response. Duet clearly prioritizes getting a snappy response to the user even if background work is needed. It’s supposedly powered by Opus 5.5, but I’ve never seen Opus move this fast in other Claude UIs. Clearly some tuning went on here. This is critical to be a useful assistant: If you want to be my shell to the world, I am not going to sit and twiddle my thumbs between commands.

## 2. Channels are neat

Maybe I’m just Slack-brained, but I really like Duet channels. In particular: I like that Duet can create and manage channels for me. One tedious aspect of working with LLMs is trying to keep track of chat sessions: workstreams get lost, context must be carefully maintained, sessions get misnamed, etc.

Duet does the tedious session organizing for me. A natural hierarchy has emerged for my work, and I suspect I will have fewer lost threads with Duet. Cmd-k was already reflex for me: it pulls up the list of channels and lets me rapidly swap between them. Channels can also see and reference each other so Duet can help me keep work in the right lane.

## 3. Access policies are meaningful

Access to Github repos is restricted per channel. I can add a few related repos to a specific channel, and not worry that the channel might commingle work from my other projects.

It also never tries to get my credentials. This is my pet peeve with most assistant apps: they won’t do much until you hand them the keys. Muse has a credential store, which at least makes the agent blind to the values, but it could still enter those in something untrusted.

Duet stores no credentials and actively discourages being given them. At best it might let you login via a Chrome session on its behalf. But it has never asked me to do that: it prefers to use the connector ecosystem Claude already has, and seems content to stay in its lane otherwise.

## 4. Responses are short

This isn’t unique to Duet, Dot and Muse seem to get this too: Nobody wants to read a full page response to a simple question, which has been the de facto chatbot experience for years. I have always had to add a bunch of instructions trying to persuade my agents to give succinct responses. They all can also add emoji “reactions” to messages, though I find that personality makes a difference here: Muse tended to thumbs up everything, whereas Duet uses it to give me an okay without elaborating further, and I find that delightful.

## THAT BEING SAID

It’s in beta, and definitely has some glitches. Sometimes threads are running but not visible. I’ve seen delegated repo access fail to attach correctly (race condition between agent start and access attachment?).

I also acknowledge my use-cases likely make Duet a better fit for me in particular. Muse might be a better fit for others. YMMV.

And Dot still reigns on voice interaction. Anthropic doesn’t even seem to care about having a conversational voice mode, it’s still just glorified speech-to-text.

## Duet is already replacing most of my AI workflows

I don’t really enjoy the management side of managing agents: remembering who is running and with what context where. There is always some agent somewhere waiting on me to make a decision or follow up on some task. I’m sure some agent did brilliant work for me on a box somewhere that I’ve neglected and will be forgotten forever.

The innovation that matters to me most is the hierarchy of concerns: The top level of Duet has a bird’s eye view of all my workstreams, but no low-level access. The channels carry more access, but under more constrained context. Sub-threads spun up by the channels can be even further constrained as they work in specific code sandboxes. The Desktop app can reach local hosts where I let it, and that’s usually only for the QA or deployment edge after the coding is done in the cloud.

Most of this is how I already preferred to arrange my agents, and similar flows could be hacked together with some ducttape and API credits. Duet just makes this hierarchy a natural part of the core product, and it works so well that I suspect it’s going to be the default experience for all chatbot UIs in the near future.

← All posts
