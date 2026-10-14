---
title: 'Foreword: Building Secure and Reliable Systems'
source_url: https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/foreword02.html
license: CC-BY-4.0
license_url: https://creativecommons.org/licenses/by/4.0/
attribution: Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana
  Oprea, Adam Stubblefield; Google; O’Reilly, 2020
source_revision: 2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c
original_html: original-source.zip!/raw/foreword02.html
original_sha256: 837299e3f885e6ff8bf7d9bc7c994ae887a168f3f4cb0c66f15ea9163542c188
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/foreword02.html
ingested: '2026-10-14'
sha256: 55610b10d568159b685f0d61601e0e0c25cde694992c1507e56827d9a1d799d9
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Foreword by Michael Wildpaner
At their core, both Site Reliability Engineering and Security Engineering are concerned with keeping a system usable. Issues like broken releases, capacity shortages, and misconfigurations can make a system unusable (at least temporarily). Security or privacy incidents that break the trust of users also undermine the usefulness of a system. Consequently, system security is top of mind for SREs.
On the design level, security has become a highly dynamic property of distributed systems. We’ve come a long way from passwordless accounts on early Unix-based telephony switches (nobody had a modem to dial into them, or so people thought), static username/password combinations, and static firewall rules. These days, we instead use time-limited access tokens and high-dimensional risk assessment at millions of requests per second. Granular cryptography of data in flight and at rest, combined with frequent key rotation, makes key management an additional dependency of any networking, processing, or storage system that deals with sensitive information. Building and operating these infrastructure security software systems requires close collaboration between the original system designers, security engineers, and SREs.
The security of distributed systems has an additional, more personal, meaning for me. From my university days until I joined Google, I had a side career in offensive security with a focus on network penetration testing. I learned a lot about the fragility of distributed software systems and the asymmetry between system designers and operators versus attackers: the former need to protect against all possible attacks, while an attacker needs to find only a single exploitable weakness.
Ideally, SRE is involved in both significant design discussions and actual system changes. As one of the early SRE Tech Leads of Gmail, I started seeing SREs as one of the best lines of defense (and in the case of system changes, quite literally the last line of defense) in preventing bad design or bad implementations from affecting the security of our systems.
Google’s two books about SRE—
Site Reliability Engineering
and
The Site Reliability Workbook
—relate the principles and best practices of SRE, but don’t go into details about the intersection of reliability and security. This book fills that gap, and also has the space to dive deeper into security-focused topics.
For many years at Google, we’ve been pulling aside engineers and giving them “the talk”—a conversation about how to responsibly handle the security of our systems. But a more formal treatment of how to design and operate secure distributed systems is long overdue. In this way, we can better scale this previously informal
collaboration
.
Security is at the forefront of finding new classes of attacks and immunizing our systems against the varied threats in today’s networked environments, while SRE plays a major role in preventing and remediating such issues. There’s simply no alternative to pushing for reliability
and
security as integral parts of the software development lifecycle.
Michael Wildpaner, Senior Director,
Site Reliability Engineering
