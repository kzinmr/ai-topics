---
title: "Signal Messenger: Embrace, extend, extinguish"
url: "https://iczelia.net/posts/signal-embrace-extinguish/"
fetched_at: 2026-05-05T07:01:18.428961+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Signal Messenger: Embrace, extend, extinguish

Source: https://iczelia.net/posts/signal-embrace-extinguish/

Most chat apps are centralised, corporate-owned and unwilling to compromise on client choice.
Discord
enforces its
Terms of Service
by actively blocking third-party clients. The company changes and obfuscates its server APIs to detect unauthorized connections, monitor traffic patterns, and identify signatures of non-official software. Once detected, users of these clients
face account bans
.
Discord’s official line of reasoning behind this change is intending to limit the damage done by
self-bots
, which are automated accounts that spam or scrape data. However, this move also conveniently eliminates competition from third-party clients that offer unique features or improved accessibility, on top of protecting their revenue streams from premium subscriptions. Unfortunately, long time users likely know that this battle is already lost:
Botting
and
scraping
on Discord is common-place and waving a stick in the air against third-party clients likely won’t change that. The accounts affected by this will likely not be spammers, but rather users who prefer alternative clients for accessibility or privacy reasons.
This state is rather sad and prompts many people to move away from Discord. I ran an experiment for a couple of years where I self-hosted a
Matrix
server and used
Element
as my main chat app. I was quite happy with it, but the experience was not without its flaws. Constant encryption errors, small and hermetic community, strongly politically polarised user base as is common for privacy-oriented messengers
, client bugs, and the need to self-host a brittle server with high maintenance cost
made me look for alternatives as soon as I encountered my first show-stopping bug.
The only two other alternatives for a good messenger that I was considering were
Telegram
and
Signal
.
I
don’t
trust
Telegram’s
security
model
, I don’t like the people who usually tend to hang out there and the main client feels clunky. I see it as a worse but less aggressive version of Discord, so I didn’t walk the path of the Dubai messenger for long.
Signal, on the other hand, has a great reputation for security and privacy. It is open-source, uses the well-regarded
Signal Protocol
for end-to-end encryption, and is recommended by many security experts. However, Signal is also a centralised service (i.e., other Signal servers can not connect to the general network) owned by a non-profit organisation, which means it has control over user data and can enforce its own policies. While Signal claims to collect minimal metadata, the fact that it operates as a single entity raises concerns about potential censorship and surveillance.
A big and rather bizzare problem concerns the use of 3rd party clients and inherent dependency on phone numbers. Focusing on the former, Signal’s owner is
quite unhappy
about the existence of 3rd party clients:
I’m not OK with LibreSignal using our servers, and I’m not OK with LibreSignal using the name “Signal.” You’re free to use our source code for whatever you would like under the terms of the license, but you’re not entitled to use our name or the service that we run. If you think running servers is difficult and expensive (you’re right), ask yourself why you feel entitled for us to run them for your product.
The inability for 3rd party clients to connect to non-federated network of Signal-run servers means that users are effectively locked into the official client. While this wouldn’t have been a major issue to me otherwise, the official client sucks, perhaps even worse than Discord’s.
Issues with message synchronisation across devices are known to me from my Matrix experience. Slow and resource-consuming Desktop apps are familiar to me from Discord and Element. I found that using Discord in the browser makes the experience much smoother and less resource-intensive, which also lets me dodge having to periodically install updates on my system. However, Signal does not offer a web client, and the Desktop app is a non-native application that must, by design, be updated frequently.
I would be partial to Signal if these limitations that carefully pick out the worst parts of each messenger weren’t inherent to greedy leadership but to technical constraints and general lack of maturity in the ecosystem. This in essence makes Signal’s practice parallel Microsoft’s old
embrace, extend, extinguish
strategy: embrace existing technology (E2EE, open-source text messaging), extend it with proprietary features (centralised service, no 3rd party clients) and extinguish competition (lock-in to official client, no federation).
This sometimes makes me feel like we’ve forgotten the lessons that Netscape had to learn and choose to trade one wall-garden for another. In conclusion, I don’t think Signal will save us.
