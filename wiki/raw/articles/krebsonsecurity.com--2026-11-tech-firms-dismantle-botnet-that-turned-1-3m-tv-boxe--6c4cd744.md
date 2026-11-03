---
title: "Tech Firms Dismantle Botnet That Turned 1.3M TV Boxes Into Proxies"
url: "https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/"
fetched_at: 2026-11-03T10:01:42.833735+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Tech Firms Dismantle Botnet That Turned 1.3M TV Boxes Into Proxies

Source: https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/

Google
said today it worked with industry partners to dismantle a botnet made up of more than 1.3 million
Android
TV set-top boxes that ship with malicious software which secretly rents the user’s Internet connection out to strangers and conducts advertising fraud. Experts involved in the takedown say the action is likely to sever the botnet’s access to more than 10 million additional compromised systems, including other Internet of Things (IoT) products such as Android-based healthcare devices and karaoke machines.
A report from the
Google Threat Intelligence Group
(GTIG) said Google has severed ties with
Videostrong Technology Co.
, a TV box manufacturer in China that GTIG and other industry experts concluded was responsible for including malware that enrolled more than 1.3 million set-top boxes in a botnet dubbed “
XCPE
” (named after one of the malware’s core code components).
The global distribution of XCPE botnet infections. Image: Google Threat Intelligence Group.
The report said the XCPE botnet loaded the user’s device with software that makes their Internet address available for resale by multiple “residential proxy” services, which allow customers to rent Internet addresses as a way to anonymize their web traffic or spoof their true location. As detailed in
several stories here over the past year
, residential proxy services are a major source of unwanted and often malicious traffic, including account takeover activity, advertising fraud, and mass content scraping for AI projects.
“Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices,” the
GTIG post
reads, noting that Google took legal action to take down the domains and servers Videostrong used to control the botnet and install additional malware. “A device manufacturer intentionally infecting their users with malware is an unacceptable breach of trust, and represents a serious risk to those users. Without users’ knowledge or consent, infected devices were offered as a distribution mechanism for a wide array of criminal actors.”
The report notes that while TV boxes made up the the majority of the botnet,
the same XCPE malware was found in other Android-based IoT products, including telehealth devices, karaoke machines, and even digital signage systems
.
Google said it requires all Android device makers to pass compatibility and security tests to ensure their products don’t harm users, but that Videostrong nevertheless found a way to load their malicious software immediately after a user boots up one of these devices for the first time (Google says it has since addressed that weakness).
The GTIG report calls out a number of residential proxy providers whose software development kits were routinely downloaded by devices infected by the XCPE botnet. Those include
AppSalt
, also known as
Honeygain
, which is owned by the Vilnius, Lithuania-based
Oxylabs
. In October 2026, Oxylabs was relaunched under a new brand called
Source
, after receiving $130 million in funding from private equity firm Warburg Pincus that
reportedly
valued the business at $3.6 billion. Oxylabs did not respond to a request for comment.
Another provider linked to the botnet was
NetNut
, a once sprawling residential proxy company operated by the publicly-traded Israeli company
Alarum Technologies
. In July 2026, the FBI worked with industry partners
to seize hundreds of domains associated with NetNut
, saying the company was responsible for operating a separate botnet called
Popa
that enslaved TV boxes as residential proxies. Other proxy providers named in the GTIG report include
EarnFM
,
Traffmonetizer
,
Jaguar
,
LINKFOG
,
BMW/IPWeb
and
GaGaNode
.
Google’s announcement credits a number of industry partners, including
Synthient
, a startup that tracks proxy providers. In January 2026, Synthient
published research
into the rapid spread of the
Kimwolf
botnet, which at the time was hammering networks worldwide with
record-smashing DDoS attacks
. Synthient documented how Kimwolf infected millions of Android set-top boxes virtually overnight, using a widespread vulnerability in these residential proxy services to compromise other Android-based devices inside the local networks of unsuspecting TV box users.
Synthient’s research caused dozens of residential proxy providers to patch their networks, which helped to fragment the Kimwolf botnet into much smaller pieces that made its
incessant and disruptive DDoS attacks
far easier for network operators to manage. It also attracted the attention of the
Motion Picture Association
(MPA), a trade group representing the major Hollywood studios, which partnered with Synthient to purchase and tear apart a number of popular Android TV set-top boxes — including some that were being infected by Kimwolf and other IoT botnets.
In
a report
published today, Synthient examined a popular, pre-infected TV box sold under the brand
MECOOL
by a publicly traded company in China called
Skyworth Technology
, concluding that MECOOL also bundled the malware from Videostrong Technology Co. and likewise installed AppSalt/Honeygain and other proxy components.
The MECOOL storefront and marketing. Image: Synthient.com.
Synthient founder
Ben Brundage
told KrebsOnSecurity that Videostrong’s malware also distributed software for the proxy service
Grass
. In our November 2025 story, “
Is Your Android TV Streaming Box Part of a Botnet?
” we quoted a researcher from
Censys
who found the popular
Superbox
TV streaming device bundled Grass’s residential proxy software. We also quoted the Grass founder, who denied any affiliation with the TV box maker.
That November 2025 story noted that Superbox and similar Android TV set-top boxes gain new customers primarily by engaging influencers on Tiktok and other social networks who praise the product’s ability to offer hundreds of (pirated) pay TV streaming services for a one-time fee.
Likewise, Synthient’s report observes that the MECOOL set-top boxes exploded in popularity after the product was mentioned in 2023 by the Youtube channel Linux Tech Tips, which has an audience of nearly 17 million subscribers [Linux Tech Tips said in a statement shared with Synthient that it has since updated the video to explicitly frame the product as a scam and have removed all associated affiliate links].
The popular Youtube channel Linus Tech Tips discussing MECOOL TV streaming boxes.
The GTIG report estimates the XCPE botnet takedown should sever access to at least 10 million additional compromised devices, noting that the various proxy and ad fraud affiliates of Videostrong “each have diversified distribution channels for their modules beyond XCPE.”
Synthient’s Brundage echoed that conclusion, calling the 1.3 million number “highly conservative.”
“The scale of affected devices is likely way higher,” he said. “This is probably the largest operation against backdoored TV boxes that we’ve seen.”
Further reading:
Plume Security Labs white paper on the XCPE botnet
(PDF)
Black Lotus Labs writeup on LinkedIn
TrendAI’s analysis
Synthient’s list of affected devices, broken down by model number
