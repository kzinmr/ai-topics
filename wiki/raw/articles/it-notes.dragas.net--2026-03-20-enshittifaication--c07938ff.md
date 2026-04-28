---
title: "EnshittifAIcation - IT Notes"
url: "https://it-notes.dragas.net/2026/03/20/enshittifaication/"
fetched_at: 2026-04-28T07:02:49.408246+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# EnshittifAIcation - IT Notes

Source: https://it-notes.dragas.net/2026/03/20/enshittifaication/

Yesterday morning, first thing after waking up, I checked my emails. One of them was from a client - a sharp person, but not a tech expert - forwarding a message from one of their "digital marketplaces". They claimed that during site crawling, their bot upgrades the connection to HTTP/2, and that this somehow causes issues on their end, so they were asking us to disable HTTP/2 to fix the problem.
I contacted Alex directly - the person (spoiler: not a person) who had sent the email - explaining that if their bot has trouble with HTTP/2 (which, on the contrary, provides significant benefits for the e-commerce experience in question), that's their problem, not ours, and they should fix it. Completely unprompted, I received something unexpected in reply: a guide on how to configure Apache to do what they wanted. The problem? Not only did it completely ignore my stated position, but we don't use Apache - we use nginx. And, I should add, their guide was entirely wrong. I replied pointing all of this out and finally asked to be "escalated to a human, since I was clearly talking to an AI that wasn't understanding any of my responses". The reply was blunt:
"That's not possible for this type of issue. Follow our guide or we will suspend your service and your e-commerce visibility."
For me, obviously, that's a hard pass. For my client, though, it's a real problem - an intelligent person who understood the situation, but still a problem to solve.
Over the past few months, I've been witnessing a dramatic increase in botnet attacks targeting some of the servers I manage, especially e-commerce ones. These aren't directed at me personally - they also hit servers I manage on behalf of clients. At first I thought they were AI scrapers, but the traffic comes from everywhere, especially from residential connections scattered around the world. I believe these are deliberate disruption campaigns, a side effect of the turbulent geopolitical climate we're living through.
On several of these e-commerce servers, we decided to implement geo-blocking, as
I've described previously on this blog
. Normally, once you've identified your whitelist countries and the shop isn't a global operation, everything works fine. In other cases, problems arise.
A few days ago, a partner of one of my clients - a company that provides services and needs access to some prepared XML feeds - started complaining they could no longer connect. I asked them for the IP pool they connect from, or at least the country their connections originate from. Their vague reply was:
"We can't provide that information because we don't have a fixed IP or set of IPs."
They completely ignored the question about the country. I pushed further, but got nowhere - different "people", giving different answers, all wildly off the mark and ignoring what I was actually asking, insisting instead that I whitelist their user agent. I explained, repeatedly, that the block is at the firewall level - meaning I never even see their user agent: if the connection is dropped, there's no handshake, no HTTP headers, nothing. It didn't matter. They kept repeating the same thing without engaging with what I wrote. Eventually they went directly to my client. I'll paste the exact text:
We're having some trouble accessing the site and downloading the XML, as they both currently require a VPN connection. To ensure our Lambda functions can run correctly, could you please:
Remove the location-based restrictions for our access;
Or, allow the User-Agent "REDACTED" in your firewall/server settings?
Please let us know which option works best for you.
Let's break this down:
"Require a VPN connection"
- who said anything about a VPN? Pure hallucination.
"Remove the location-based restrictions for our access"
- they never once answered: which location?
"Allow the user agent"
- I explained, multiple times, that the block is at the firewall level. The connection is dropped before any handshake occurs. There is no user agent to allow.
This morning, another client writes:
"The marketing consultancy wants all the server load graphs to get an idea of where we stand."
This is the second time in just a few days I've received a request like this. I send both the graphs and the full specs of the dedicated server in use - average load under 5%. The response was staggering:
"The internal team, supported by the most advanced AI, believes your current setup is not adequate for the industry, load, and audience you're targeting, and recommends migrating to a cloud VPS with AT LEAST 8 GB of dedicated RAM to ensure sufficient resources, as the current ones are insufficient."
The current ones? 128 GB of RAM. Two modern CPUs. 48 cores total. If we followed their advice, the site would be down within five minutes - and that's just counting legitimate traffic. My client, unaware of the technical differences, asks me if we can implement what they're suggesting.
The shift was abrupt - not unlike when an intern arrives convinced they already know everything, often with the best of intentions: bringing fresh air into an environment that needs "modernising". But with an intern, you can talk. That same confidence often turns into curiosity, hunger to learn, real experience. I've watched eager interns grow into excellent professionals - people who eventually surpassed me in skill and success, and that felt genuinely satisfying, knowing I'd contributed, at least in part, to their growth. With AI, this is impossible. It doesn't grow, doesn't listen, doesn't update its mental model based on what you write back - and above all, it doesn't know what it doesn't know.
That's why I'd like companies to consider that AI systems are stochastic machines, not experts. They can solve some problems, but there's a limit. There will always be a limit, at least with current technology, and we can't afford to ignore it. The damage risks far outweighing the "savings" generated.
The enormous problem with my work these days is the extreme confidence that certain companies project, replacing humans - even senior ones - with AI, with no right of appeal. The result is monstrous confusion, enormous wasted time for everyone, and a widespread erosion of reliability, all papered over by the AI's unshakeable assertiveness - and by those who believe these systems are the
Answer to the Ultimate Question of Life, the Universe, and Everything
.
Rewarding confidence over actual competence is a bug humanity has always had. It has produced disasters throughout history, it is producing disasters now, and not only in the tech world.
So I find myself wondering: if they're so convinced that AI is better than senior professionals, why don't they replace the bosses with AI? I'm fairly confident the decisions would be considerably better - and humans would end up exactly where they should be.
