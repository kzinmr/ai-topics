---
title: "Stefano Marinelli"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---


# Stefano Marinelli

**Blog:** [it-notes.dragas.net](https://it-notes.dragas.net) — "Scattered IT Notes"  
**Fediverse:** [@stefano@mastodon.bsd.cafe](https://mastodon.bsd.cafe/@stefano), snac instance  
**Location:** Italy  
**Focus:** System administration, BSD/illumos, open-source infrastructure, AI criticism

## Overview

Stefano Marinelli is an Italian system administrator and blogger who writes about FreeBSD, illumos, Void Linux, and infrastructure management. His blog, *IT Notes*, has been running since 2014 and covers practical system administration alongside increasingly critical commentary on AI's role in software and infrastructure.

Marinelli's perspective is grounded in decades of hands-on system administration experience. He is a vocal advocate for BSD operating systems, the illumos project, and community-run infrastructure. His writing on AI is distinctive because it comes from someone who manages production servers for real clients — not a researcher or theorist — giving him a ground-level view of how AI is actually being deployed and its real-world consequences.

## Core Ideas

### EnshittifAIcation: The New Wave of Platform Degradation

Marinelli coined "EnshittifAIcation" to describe how AI is accelerating the degradation of software and services. His March 2026 essay documents three incidents in one week:

1. **AI bots hallucinating requirements** — Clients receiving VPN recommendations that don't match their actual needs
2. **Misconfigured servers** — AI recommending Apache configs on nginx servers
3. **Absurd infrastructure advice** — Suggesting replacing 128 GB RAM servers with cloud VPS instances

> "The enormous problem with my work these days is the extreme confidence that certain companies project, replacing humans — even senior ones — with AI, with no right of appeal. The result is monstrous confusion, enormous wasted time for everyone, and a widespread erosion of reliability, all papered over by the AI's unshakeable assertiveness."

He argues that AI systems are "stochastic machines, not experts" and that companies are rewarding confidence over actual competence — a bug that has "produced disasters throughout history."

### Vibe Coding Will Rob Us of Our Freedom

Marinelli's most widely-read essay (June 2025) examines the trend of "vibe coding" — developers using AI assistants to generate code they don't fully understand, testing only whether the output "seems to work."

> "We're shifting from being architects to being interior decorators."

His central concern: when developers are trained on prompting rather than code structure, they lose the ability to understand, maintain, and audit what they've built. This creates a dependency on the companies that sell AI tools — the very opposite of the freedom that open-source software was meant to provide.

> "Today, writing code is something free, potentially doable even on a beat-up laptop. But tomorrow? Will we be completely dependent on AIs (even) for this?"

He references Serena Sensini's OSDay 2025 talk: "The point is not to let ourselves be replaced by AIs, but to use them to improve ourselves and our productivity."

### The Botnet Disruption of AI Infrastructure

Marinelli documents a practical, ground-level problem: **deliberate botnet attacks targeting servers**, especially e-commerce ones. The traffic comes from residential connections worldwide, and he believes these are "deliberate disruption campaigns, a side effect" of AI scraping infrastructure.

> "Over the past few months, I've been witnessing a dramatic increase in botnet attacks targeting some of the servers I manage, especially e-commerce ones."

This represents a tangible cost of the AI gold rush — server operators worldwide are dealing with the infrastructure consequences of unregulated AI scraping and deployment.

### FreeBSD and the Philosophy of System Control

Marinelli is a committed FreeBSD advocate, having used it since 2002. His writing emphasizes:

- **Control**: FreeBSD gives administrators complete control over their systems
- **Stability**: The OS philosophy prioritizes reliability over novelty
- **Community**: The BSD community values transparency, documentation, and mutual aid
- **Sovereignty**: Running your own infrastructure is an act of digital independence

His blog includes practical guides for:
- Installing Void Linux on encrypted ZFS with hibernation
- Setting up Time Machine inside a FreeBSD jail
- Boosting Mastodon performance with self-hosted SeaweedFS
- Static web hosting performance comparisons across BSD, Linux, and illumos

### The illumos Cafe: Community Infrastructure

Marinelli helped launch the **illumos Cafe** — a community-run hub on illumos, Fediverse-ready (Mastodon, snac), built for OS diversity, transparency, and community. This reflects his broader philosophy: infrastructure should be community-owned, transparent, and diverse.

## Key Quotes

> "The enormous problem with my work these days is the extreme confidence that certain companies project, replacing humans — even senior ones — with AI, with no right of appeal."

> "We're shifting from being architects to being interior decorators."

> "Today, writing code is something free, potentially doable even on a beat-up laptop. But tomorrow? Will we be completely dependent on AIs (even) for this?"

> "AI systems are stochastic machines, not experts. They can solve some problems, but there's a limit. There will always be a limit, at least with current technology."

> "Rewarding confidence over actual competence is a bug humanity has always had. It has produced disasters throughout history, it is producing disasters now."

> "The point is not to let ourselves be replaced by AIs, but to use them to improve ourselves and our productivity." — referencing Serena Sensini, OSDay 2025

## Recent Themes (2024–2026)

- **EnshittifAIcation** — AI-driven platform degradation, hallucinated infrastructure advice, botnet disruption
- **Vibe coding criticism** — The danger of AI-generated code that developers don't understand
- **FreeBSD advocacy** — System control, stability, community, digital sovereignty
- **illumos and BSD diversity** — The illumos Cafe project, community-run infrastructure
- **Mastodon and Fediverse** — Self-hosted social media, snac instances, community communication
- **Practical system administration** — Real-world guides for ZFS, jails, bhyve VMs, backup systems
- **Anti-AI-dependency** — Maintaining human skills and understanding in an AI-saturated world

## Related

- [[jayden-milne]] — AI culture criticism, digital sovereignty
- [[george-hotz]] — AI infrastructure, open-source ethos
- [[grant-slatton]] — AI alignment, technocapital economics
- [[john-carmack]] — Pragmatic AI tool use
-  — Operating system Marinelli advocates for and uses extensively
-  — Open-source Solaris derivative, community infrastructure
-  — Self-hosted infrastructure, community control

## Sources

- [it-notes.dragas.net](https://it-notes.dragas.net) — "Scattered IT Notes" blog
- "EnshittifAIcation" (March 2026)
- "Vibe Coding Will Rob Us of Our Freedom" (June 2025)
- "Why I Love FreeBSD" (March 2026)
- "Introducing the illumos Cafe" (August 2025)
- "FreeBSD vs. SmartOS: Who's Faster for Jails, Zones, and bhyve VMs?" (September 2025)
- OSDay 2025 talk by Serena Sensini (referenced)

## References

- it-notes.dragas.net--2025-03-23-osday-2025-why-choose-bsd-in-2025--c5a669ee
- it-notes.dragas.net--2025-04-07-launching-bssg-my-journey-from-dynamic-cms-to-bas--69c8c85e
- it-notes.dragas.net--2025-04-22-make-your-own-internet-presence-with-netbsd-and-a--fa9b9ef0
- it-notes.dragas.net--2025-05-13-the-server-that-wasnt-meant-to-exist--a33ee1b1
- it-notes.dragas.net--2025-05-21-the-day-glusterfs-tried-to-kill-my-career--e7a05d7f
- it-notes.dragas.net--2025-06-05-vibe-coding-will-rob-us-of-our-freedom--204416ce
- it-notes.dragas.net--2025-07-02-install-freebsd-providers-mfsbsd--8c964d47
- it-notes.dragas.net--2025-07-18-make-your-own-backup-system-part-1-strategy-befor--2d97d1db
- it-notes.dragas.net--2025-07-21-new-article-wordpress-on-freebsd-bastillebsd-on-b--d7c3e8de
- it-notes.dragas.net--2025-07-29-make-your-own-backup-system-part-2-forging-the-fr--a16081cc
- it-notes.dragas.net--2025-08-18-introducing-the-illumos-cafe--0bea1603
- it-notes.dragas.net--2025-09-19-freebsd-vs-smartos-whos-faster-for-jails-zones-bh--8e81c120
- it-notes.dragas.net--2025-10-08-the-email-they-shouldnt-have-read--2efbb236
- it-notes.dragas.net--2025-11-06-self-hosting-your-mastodon-media-with-seaweedfs--69d6b27d
- it-notes.dragas.net--2025-11-19-static-web-hosting-intel-n150-freebsd-smartos-net--e43d5773
- it-notes.dragas.net--2025-11-24-why-i-still-love-linux--32033d6e
- it-notes.dragas.net--2025-12-22-void-linux-zfs-hibernation-guide--52100cfa
- it-notes.dragas.net--2026-01-28-time-machine-freebsd-jail--e4982eed
- it-notes.dragas.net--2026-03-16-why-i-love-freebsd--309b65c6
- it-notes.dragas.net--2026-03-20-enshittifaication--c07938ff
