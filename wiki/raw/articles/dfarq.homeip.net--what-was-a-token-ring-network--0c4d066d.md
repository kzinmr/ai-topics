---
title: "What was a Token Ring network?"
url: "https://dfarq.homeip.net/what-was-a-token-ring-network/?utm_source=rss&utm_medium=rss&utm_campaign=what-was-a-token-ring-network"
fetched_at: 2026-10-16T10:00:37.342214+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# What was a Token Ring network?

Source: https://dfarq.homeip.net/what-was-a-token-ring-network/?utm_source=rss&utm_medium=rss&utm_campaign=what-was-a-token-ring-network

What was a Token Ring network? Token Ring is an obsolete networking technology that competed with Ethernet in the 1980s and 1990s. IBM first announced it October 15, 1985. It is more of a curiosity today, as the networking standard that lost. But when Token Ring equipment turns up, it can look enough like Ethernet to confuse people. And why it lost can be interesting to study.
Ethernet versus Token Ring
This Intel Token Ring card can pass for Ethernet. The best indicator from this photo is the DE-9 connector on the back. Ethernet never used that. Even though it was an IBM technology, companies like Intel and 3Com wanted in on the game.
Token Ring gets a bad rap today, and that isn’t necessarily fair. Token Ring was a standard backed by IBM. Ethernet was an open standard backed by
DEC
,
3Com
and others. Of course Ethernet won.
The main reason Ethernet won the war was because it was cheaper. Once you bought everything you needed, Ethernet cost a third as much. Whether Ethernet was half as good or 75% as good was always a matter of debate, but for a third the price, it only needed to be half as good to be a reasonable value.
Token Ring had one big weakness besides cost. It ran at specific speeds, and unlike Ethernet, all the cards on the ring had to talk at the same speed. If you had a 16 megabit network and brought up a system at 4 megabits, it took down the whole network.
I know this from experience. But I only made that mistake once.
But as long as you didn’t do that, Token Ring was extremely robust. it didn’t have a problem with collisions, unlike early Ethernet. The way Token Ring worked was the systems passed a token around the network. If you didn’t have the token, you didn’t get to talk. That meant no collisions. And it handled saturation much better.
I brought down an Ethernet network once just by trying to clone a classroom full of systems using Symantec Ghost’s multicast feature. I did it all the time when I worked in a Token Ring shop. The first time I did that on an Ethernet network, I took down all of the networking in the building. They had to isolate the classroom behind a bridge to allow me to do that. That was 24 years ago and I guarantee there are two people who who still hold that against me even though none of us work there anymore.
Why Ethernet won
Ethernet was junk if you went with the cheapest options all around, but you could make it acceptable if you invested some of the savings in improved technology. Replacing hubs with switches mostly eliminated the collision problem. Buying higher quality cards cut down on the reliability problem.
But the other reason Ethernet won was because of scale. It scaled to higher speeds first, so it won the war through brute force. Ethernet made it to 100 megabits first. Anyone who saw 16 megabit Token Ring in action can tell you it was way more than 60% faster than 10 megabit Ethernet, but 16 megabit Token Ring couldn’t keep up with 100 megabit Ethernet. And when 100 megabit Token Ring came out, the next iteration was going to be 128 megabit. Gigabit Ethernet came out before 128 megabit Token Ring ever saw the light of day.
And at gigabit speeds, the advantage of Token Ring over Ethernet was mostly academic. Maybe the network itself was a bit more robust in some ways, but the better efficiency didn’t matter much. The bus the cards plugged into and the disks in the system were bigger bottlenecks.
In 2022, we have a faster bus and SSDs so we’d be able to tell a difference, but then we’d be back at that problem of scale.
Telling the difference between a Token Ring and Ethernet card today
Whenever a retro computing Youtuber does a mail call that includes batches of random ISA cards, inevitably, when faced with a mystery network card, they will wonder aloud into the camera whether it is Ethernet or Token Ring. Telling the difference can be difficult. Even in the ’90s when both technologies were viable, professionals sometimes made the mistake. Plugging Ethernet into a Token Ring network because they were both CAT5 is just as fun as bringing up a node at 4 megabits on a 16 megabit network. And by fun, I mean destructive.
Yes, by the mid-90s, both technologies could run on RJ45 cabling. The pinout was different, but you could use the same cable for either. If you want to try to tell the difference by toning it out with a multimeter, what you need to know is that on Token Ring, the outer pins weren’t connected. On Ethernet from the same time period, the two center pins were the unconnected pins.
The D-sub connectors
But it’s usually easier to distinguish the two by looking at the other connectors. Ethernet used a 15-pin connector that looks quite a bit like a PC joystick connector. Token Ring used a 9-pin connector that looks like a 9-pin video connector or an Atari style joystick plug.
Coax connections
Coax connectors for Token Ring did exist, but were more common on Ethernet networks. The presence of a coax connector on a card isn’t a reliable indicator of either network type. But it was more common with Ethernet than Token Ring, so if I see a coax connector on an unknown card, it tilts it in favor of Ethernet.
Speed indicators
The LEDs and other printing on the card can be a very good indicator. The majority of ISA Ethernet cards you will find ran at 10 megabits. PCI cards ran at 10 and 100 megabits. So look for any speed indicator legends that might be printed or embossed on the card, either on the backplate or on the PCB itself.
Token Ring ran at 4 megabits and 16 megabits. So on an ISA card, if you see both a link activity light and a speed light, and the light indicates a speed of 4 or 16, that’s Token Ring. If there is a dip switch to set a speed of 4 or 16 megabits, that’s Token Ring.
Brand
You can’t necessarily go by brand. IBM sold Ethernet cards, and Intel and 3Com did make Token Ring cards. So don’t automatically assume a 3Com or Intel ISA card that looks like a network card is Ethernet.
There were other obscure makers of Token Ring cards, including Thomas Conrad and Madge.
Is Token Ring hardware worth messing with today?
I liked Token Ring when it was still on the market, though I might have thought differently if I had been in on the yearly computing budget. But once it was becoming clear that Token Ring was the
Betamax of networking
, people started replacing it with Ethernet. Since the cards took up less space, they were less likely to get scrapped than the equipment in the racks or wiring closets.
It’s easier to find the cards today than the necessary supporting infrastructure, like a MAU, the equivalent of an Ethernet switch. And bridging Ethernet and Token Ring is more difficult than just slapping one of each card in a Linux box and configuring the two cards to route.
That’s not to say using it is impossible today. It’s impractical and difficult. But if that’s your idea of fun, don’t let me dissuade you. It’s not my idea of fun. But I don’t think coax-based Ethernet is worth messing with either, and there are people who do that.
Why anyone messed with Token Ring at all
One question I hear sometimes is why anyone messed with Token Ring at all, since Ethernet was an open standard, and open standards are better.
It helps to remember that the IBM of the 1980s was not the same company that
IBM is today
. Not only you were they a dominant player in the personal computer market, they were also the dominant player in the minicomputer and mainframe markets, which, at the time, was what some people considered serious computing. It was the preferred networking option for IBM minicomputers and mainframes.
There was a saying in the 1980s that nobody got fired for choosing IBM. That alone gave Token Ring a chance, for a few years.
ARCNET
was another competitor from the same timeframe. It, too, was a contender for a while because it was backed by
Datapoint
, a pioneer in office automation using small computers.
Are Ethernet and Token Ring interchangeable or interoperable?
Sometimes you will see cards and hubs listed on eBay as both, which may lead someone to believe the two are interchangeable, or that some kind of dual-standard cards and hubs existed for a time. Don’t believe the listing. Network cards were one or the other, not both. Hubs and switches are Ethernet. The equivalent equipment for Token Ring was called a MAU.
Unless you can tell from looking at the photos what it is, don’t buy it. And if they listed it as both, assume it’s untested. If the price is good and the photographs permit identification, you
may
be able to snag a bargain.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
