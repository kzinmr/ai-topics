---
title: "The Silicon Underground"
url: "https://dfarq.homeip.net/what-happened-to-arcnet/?utm_source=rss&utm_medium=rss&utm_campaign=what-happened-to-arcnet"
fetched_at: 2026-07-27T10:17:12.865750+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# The Silicon Underground

Source: https://dfarq.homeip.net/what-happened-to-arcnet/?utm_source=rss&utm_medium=rss&utm_campaign=what-happened-to-arcnet

ARCNET was the first commercially available local area network standard, beating both Ethernet and Token Ring to market. Conceptually, it had similarities with both, and because it was inexpensive and efficient, it was popular for a good 15 years or so. ARCNET was an abbreviation for Attached Resource Computer NETwork. But you’re probably using some variant of Ethernet to read this blog post. So what happened to ARCNET?
ARCNET’s emergence and early lead
Initially ARCNET was efficient and inexpensive. But a delayed update to 20 megabits per second was just one of the reasons Ethernet overtook ARCNET.
ARCNET was invented by Datapoint, the company that arguably
accidentally invented the desktop computer
and the microprocessor and the direct ancestor of the Intel x86 architecture. That’s a whole other story, but it raises even more might-have-been questions. ARCNET hit the market in 1977, before Ethernet became available. Ethernet, although invented in 1973 at
Xerox PARC
, didn’t become commercially available until 1980.
Datapoint invented ARCNET as a method to network its computers together and share peripherals. Although the Internet as we know it did not exist yet, the use case had similarities to the modern day, all the way back in 1977.
The modern OSI model didn’t exist yet, but conceptually, it worked like a modern network. And when the OSI model was invented, ARCNET took well to it.
As other types of computers became popular, ARCNET interfaces became available for them as well. And ARCNET’s early success turned Datapoint into a Fortune 500 company.
The misconception of ARCNET
There is a common misconception the intent was to share 8-inch floppy drives, but the inventor, John Murphy, reached out to me and said this is not the case, that he hadn’t even seen an 8-inch floppy drive when he invented ARCNET.
It’s not often you get the opportunity to ask questions of the inventor of a significant technology, so of course I asked him what he intended to use it for. He said the idea came up when Harry Pyle had lunch with a Datapoint field engineer.
“The problem in the field was that our small computers could support a large number of terminals, but a very limited number of hard drives. So the field engineer suggested a hard drive controller that could be connected to two computers! (There were even a few people inside Datapoint that misunderstood what it was all about, and took that request quite literally!),” Murphy said.
“Harry, however, as I recall, came back from that lunch with a complete plan for the first LAN. What we needed, he explained, was a way for our computers to communicate with each other at ‘high’ speed (the hard disks of the day moved data at 2.5 Mbps), and then the multiple computers could share peripherals: disks, printers, modems, etc.). ARCNET was the resulting hardware and accompanying software that provided that communications,” Murphy said.
And with that, he answered another question. The reason ARCNET was 2.5 megabits was because that was the speed of the hard drives in 1977.
As for floppy drives, he said, “It was a big company, with lots of products, and there were probably even some floppy drives somewhere in the mix – but they nothing to do with the development of ARCNET.”
ARCNET vs Ethernet
The wiring topology was somewhat different from Ethernet, which made it cheaper and less finicky. It was more versatile too, supporting bus, star, and distributed star topologies. Besides the wiring being less expensive, the interface cards were less expensive than Ethernet too. A Dec 4, 1989 article in
Network World
said ARCNET cards cost 30-60 percent less than Ethernet cards did.
The catch was that ARCNET operated at 2.5 megabits per second, and that lagged Token Ring’s 4-megabit speed and Ethernet’s 10-megabit speed. The difference was that ARCNET didn’t have collisions. Conceptually, it was similar to Token Ring, where the network passed a token from machine to machine on the network, and no machine could speak until it had the token. This eliminated the dreaded problem of collision.
A collision was when two machines listened on the network, saw no traffic, and tried to send traffic at the same time. When that happened, they each had to pause and try again.
On paper, Ethernet was theoretically four times as fast as ARCNET and 2.5 times as fast as
Token Ring
. But collisions meant that advantage was purely theoretical. The increased overhead of dealing with collisions meant ARCnet and Ethernet ran at about the same speed, especially on early PCs that ran at 10 MHz or slower.
But from a marketing standpoint, Ethernet’s 10 megabit speed gave it the advantage. If you weren’t a network engineer, you perceived Ethernet as faster and better, period.
The problem for ARCNET was that as time moved on, faster processors could process collisions much faster. From what I was able to gather, the tipping point came at around a 20-25 MHz 386. On that class of a machine or better, Ethernet was faster. So even though ARCNET had the early lead, its sales didn’t grow as quickly as Ethernet or even Token Ring as the 1980s moved on. By 1988, Ethernet overtook it in market share.
What happened with ARCNET Plus
Datapoint announced a faster 20-megabit version of ARCNET, called ARCNET Plus in 1989. But its release slipped multiple times, finally appearing on the market in February 1992. The delay led some impatient customers to switch to Ethernet or Token Ring. Not only was it late, but it was expensive. The Oct 5, 1992 issue of Computerworld noted a 20-megabit ARCNET card cost $995, versus $120 for a 4-megabit ARCNET card or $175 for a 10-megabit Ethernet card. So you paid five times as much for what appeared to be double the performance of Ethernet.
If it had had arrived on time and at a more competitive price, ARCNET Plus might have helped ARCNET regain the lead. At best, it was too little, too late. More likely, it drove people to switch to Ethernet. Ethernet was cheaper, and by 1992, word was out that 100-megabit Ethernet was on its way. If you were going to switch, you might as well switch to Ethernet so you could be ready for the newer, faster version, which arrived in 1995.
And Ethernet didn’t stand still. Gigabit Ethernet wasn’t far behind, arriving in 1998. And as all of this was going on in the early 90s, CAT5 wiring and network switches came to Ethernet, making the cabling less finicky and almost eliminating collisions.
By the mid 1990s, ARCNET had fallen by the wayside as a mainstream networking technology. The problem for ARCNET was that as its technological advantages eroded away, its cost advantage also eroded away.
ARCNET today
ARCNET still exists in certain industrial applications, especially factory floors. In factories, lifecycles for equipment tend to be measured in decades rather than years. That means ARCNET equipment does still exist and is still being manufactured. It’s just a niche technology now, not existing in the types of volumes that Ethernet has. But as someone who started my career in a Token Ring shop, I’ve gone from seeing more Token Ring than ARCNET to the other way around.
What might have been
It’s fun to imagine what might have happened if Datapoint had realized the full value of what they had. And it is potentially less of a stretch to imagine ARCNET faring better. The turning point seems to have been around the time of the Novell NE2000 network card. It was a minimum-viable-product Ethernet card, but Novell designed it to be cheap so they could sell more network software, and they encouraged others to clone it. This economy of scale allowed Ethernet to come much closer to meeting ARCNET’s price, and later to overcome it.
By 1988, Ethernet was the leading network topology, with ARCNET in second place, according to a May 30, 1988 article in
Infoworld
written by Mark Stephens.
The NE2000 became possible when National Semiconductor released an inexpensive Ethernet chipset. If National Semiconductor or another major chip maker at the time had released a disruptively inexpensive ARCNET chipset around that time, it’s possible Novell would have gone that direction instead. Of course Novell went by the wayside soon after ARCNET, but one of the reasons Windows was able to take over as the dominant network operating system was because it supported all of the same hardware Netware supported.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
