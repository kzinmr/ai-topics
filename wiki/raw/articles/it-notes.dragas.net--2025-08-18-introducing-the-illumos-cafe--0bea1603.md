---
title: "Introducing the illumos Cafe: Another Cozy Corner for OS Diversity"
url: "https://it-notes.dragas.net/2025/08/18/introducing-the-illumos-cafe/"
fetched_at: 2026-04-28T07:02:49.792887+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Introducing the illumos Cafe: Another Cozy Corner for OS Diversity

Source: https://it-notes.dragas.net/2025/08/18/introducing-the-illumos-cafe/

Introducing the illumos Cafe: Another Cozy Corner for OS Diversity
From the BSD Cafe to illumos Cafe
The idea for this new project was born from the success of the BSD Cafe, an initiative I introduced to the world in July 2023, which received an incredibly positive response. Far more than I ever anticipated. The BSD community already had its well-established hubs: in the Fediverse, places like
bsd.network
,
exquisite.social
, and others were already thriving, not to mention all the forums, channels, and Reddit communities.
But in my vision, something was still missing: a hub of services with a positive spirit, built exclusively with open-source tools, where people could come to share, learn, and experience technology with a positive mindset. The BSD Cafe is therefore not just an instance, but a true Cafe -
I’ll be speaking more about the BSD Cafe in detail at the next EuroBSDCon
.
Why Another Cafe?
In a world increasingly dominated by centralized services under the control (or lack thereof) of the usual big players, it has become essential to create free, independent communities, devoid of the algorithmic and commercial controls that influence our overall experience. From day one, the BSD Cafe has embodied this spirit.
Linux is a good kernel, and there are excellent distributions based on it (some using the GNU userland, others only partially, like Alpine Linux), but it cannot and should not become a monoculture. The alternatives are extremely capable, and for many use cases - in my opinion and experience - they are even more suitable.
BSD systems have served me exceptionally well for over 20 years
, providing stability and security. At the same time, many other operating systems are renowned for their robustness, reliability, and the quality of their design and implementation.
Why illumos?
illumos
is one of them. As the open-source descendant of OpenSolaris, it is an operating system known for its enterprise-grade stability and innovative technologies like ZFS, DTrace, and "zones". It was born from the solid foundations of Solaris and has evolved over time while remaining true to many of its core principles. I have always seen illumos and its distributions as kindred spirits to the BSDs, despite their differences. The philosophy is one of evolution without revolution, of guaranteeing long-term continuity and reliability rather than chasing the latest hype. This is precisely why, for some time now (and thanks in part to the
inspiring posts by Joel Carnat
, which further sparked my curiosity), I have been running
OmniOS
and
SmartOS
alongside my BSD-based setups for certain workloads.
However, there is very little information online about services running on them. So, a few months ago, I began to consider a new project:
the illumos Cafe
.
The illumos Cafe Project
The illumos Cafe is a project similar to the
BSD Cafe
(though perhaps less complex, at least initially). It shares the same spirit of positivity and inclusivity and aims to provide services running on illumos-based operating systems to demonstrate that there are no reasons not to use them. Just like with the BSD Cafe, diversifying the operating systems we use - even while using the same platforms - is fundamental to improving the reliability and resilience of the Internet. The Internet was born as a decentralized network, but for most people, it has sadly become just a tool to access the services of big players.
Community and Philosophy
But we want to connect. We want relationships with people, between people. We don't want algorithms. We don't want our data to be monetized by "us and our 65535 partners". We want a network that serves us, an OS that serves us - not an OS that just serves as a vehicle to store our data in "someone else's house". The illumos Cafe, therefore, aims to be a home for anyone interested in developing, using, or who is simply curious about illumos-based operating systems.
Technical Setup
As with the BSD Cafe
, the entire setup will be documented. For now, it is very simple: there is a VM (running on FreeBSD and bhyve, on hardware I manage) where I have installed SmartOS. The physical host also runs the reverse proxy (in a jail). Inside the SmartOS VM, there are a series of zones:
Zone 1: nginx
(Web Server) - Currently serving
the project's homepage
.
Zone 2: Mastodon
(Social) - Hosting the Mastodon instance and its dependencies at
https://mastodon.illumos.cafe
.
Zone 3: PostgreSQL
(Database) - The Mastodon database, on a dedicated zone.
Zone 4: Redis
(Cache) - The Mastodon cache, on a dedicated zone.
Zone 5: snac
(LX Zone) - Currently in an LX zone (Alpine) as I ran into some issues getting it to work in a native zone. It will be moved to a native zone as soon as I resolve them. It's serving the snac instance at
https://snac.illumos.cafe
Media files are stored on an external physical server (running FreeBSD, the same one as the BSD Cafe, but in a dedicated jail) with
SeaweedFS
. I was able to compile and run SeaweedFS on illumos without any problems, but at the moment, I don't have a host with enough storage space for the media.
Available Services
More services will arrive over time. For now, two gateways to the Fediverse are already available:
Both instances share the same rules as the BSD Cafe. Positivity. Supporters, not haters. I want them to be places of enjoyment, not venting. Of friendship, not hate.
Registrations and Logo
Registrations for the Mastodon instance are now open, and the available themes are the default ones plus
the colorful TangerineUI
- whose orange hue echoes the illumos logo.
The project's logo was not generated by an AI. I made it myself by hastily sticking the illumos SVG onto a coffee cup. Basic, perhaps. But authentic.
Looking Ahead
The BSD Cafe will, of course, remain my primary home. But I want to bring illumos into the Fediverse and provide a home for anyone who wishes to share their interest in this excellent OS.
I will document the entire process, just
as I did with Mastodon on FreeBSD
, as it is a bit more intricate. Because in my dreams, I see Fediverse statistics showing instances spread fairly evenly across the major open-source operating systems. Because relying on a single OS, even if it's open-source, and ceasing to support the others is also a single point of failure.
