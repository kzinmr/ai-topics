---
title: Rachel by the Bay
created: 2026-04-09
updated: 2026-04-10
tags:
- person
- blogger
- hn-popular
- sysadmin
- infrastructure
- unix
- monitoring
- operations
- feed-readers
aliases:
- rachelbythebay.com
- rachelbythebay
---

# Rachel by the Bay

| | |
|---|---|
| **Blog** | [rachelbythebay.com/w](https://rachelbythebay.com/w/) |
| **RSS** | https://rachelbythebay.com/w/atom.xml |
| **Also writes** | [rachelbythebay.com/sv](https://rachelbythebay.com/sv/) (software versioning, technical notes) |
| **Known for** | Sysadmin war stories, infrastructure monitoring, feed reader behavior analysis, Unix operations wisdom, outage postmortems |
| **Bio** | Long-time systems administrator and infrastructure engineer. Writes deeply practical, often humorous accounts of keeping systems running at scale. Author of a multi-year feed reader behavior analysis project, regular contributor of outage postmortems, and a sharp critic of software that wastes resources or ignores established protocols. |

## Overview

Rachel by the Bay is one of the internet's most distinctive voices on systems administration, infrastructure reliability, and the art of keeping things running when nobody notices — until they break. Her writing combines deep technical expertise with a wry, no-nonsense tone that's earned her a devoted following among practitioners who value hard-won operational wisdom over theoretical best practices.

Her blog spans several recurring themes: sysadmin war stories (servers, networks, outages, hardware failures), feed reader behavior analysis (a multi-year project monitoring and scoring RSS/Atom reader compliance with HTTP protocols), monitoring and alerting philosophy, and occasional deep dives into Unix internals, filesystems, and embedded systems.

What sets Rachel apart is her **empirical approach**: she doesn't just complain that feed readers are wasteful — she built a scoring service, logged 70K+ requests from 97 distinct reader instances, and published detailed reports showing exactly which programs respect `If-Modified-Since` headers and which don't. She doesn't just say "monitor your systems" — she explains how to let the network tell you where you are, how to decode proprietary wireless sensor protocols, and why SSD death in read-only filesystems reveals deeper architectural truths.

## Core Ideas

### The Feed Reader Score Project

Rachel's most sustained technical project is a feed reader behavior monitoring service — a personalized URL that feeds zero-nutritional-content RSS to reader programs and logs everything they do. The project emerged from years of frustration with poorly-behaved crawlers and feed aggregators:

> *"I don't think people really appreciate what kind of mayhem some of their software gets up to."*

Key findings from her analysis:
- **Conditional requests are still broken everywhere** — After 28 years of `If-Modified-Since` (RFC 1945, May 1996), most feed readers still download full copies every poll cycle
- **Retry timing is chaos** — Readers poll at arbitrary intervals (some every 20 minutes unconditionally), wasting bandwidth and battery
- **User-Agent spoofing draws attention** — Readers claiming to be GoogleBot actually trigger IP filters more easily
- **The double-tap problem** — Some readers request the feed twice within milliseconds when first added, tripping 429 rate limits
- **Cache bugginess** — Readers like Newsboat and BazQux get stuck on old ETag values and never update them

> *"It's not any of the carriers and it's not Hurricane Electric. It's my end, and it's not an accident. Hosts that get auto-filtered are usually running some kind of feed reader that flies in the face of best practices, and then annoys the web server, receives 429s, and then ignores those and keeps on going."*

The project exemplifies Rachel's philosophy: **don't argue about best practices, measure them.** Her scoring system turns subjective complaints into objective data — if your reader scores poorly, the logs prove it.

### Infrastructure Monitoring: Let the Network Tell You

Rachel advocates for passive, infrastructure-level monitoring over active probing:

> *"Let the network tell you where you are."*

Her approach:
- **Port-scan your own fleet** — Regular, automated port scanning reveals services that shouldn't be running, firewalls that drifted, and configurations that diverged
- **Use existing traffic patterns** — Rather than adding synthetic checks, analyze the traffic that's already flowing
- **Monitor the monitors** — Alerting systems themselves need health checks; "the night of 1000 alerts (but only on the Linux boxes)" taught her that monitoring failures cascade
- **Unintentional troubleshooting** — Sometimes the most useful monitoring emerges from trying to solve an unrelated problem

Her "nerd snipe" story about decoding a SkyScan wireless weather sensor protocol demonstrates this: what started as curiosity about a gadget's RF emissions became a lesson in reverse-engineering proprietary protocols and understanding how embedded systems communicate.

### Outage Culture and Postmortems

Rachel's outage stories are distinctive in their matter-of-fact tone. She doesn't dramatize — she documents:

- **SSD death and read-only filesystems** — When an SSD fails into read-only mode, the system keeps running but silently stops accepting writes. The fix requires understanding that the filesystem isn't corrupted, it's just frozen.
- **The parasitic RPC service** — A service that broke core dumps by consuming the same socket configuration, demonstrating how "innocent" infrastructure changes can cascade into debugging nightmares.
- **Port-scanning the fleet** — How a routine security sweep revealed misconfigured services across dozens of machines, and the triage process of deciding which fires to fight first.

> *"Systems design and being bitten by edge-triggering"* — Her essay on this topic explains how edge-triggered vs. level-triggered event systems create fundamentally different failure modes, and why the wrong choice makes debugging nearly impossible.

### Web Architecture Philosophy

Rachel's writing reveals a consistent architectural philosophy:

1. **Respect the protocols** — HTTP has been well-specified for decades. If your software ignores `If-None-Match`, `If-Modified-Since`, and proper User-Agent strings, it's not clever — it's broken.
2. **Don't waste resources** — Bandwidth, battery, CPU, and storage are all finite. Software that burns them unnecessarily is hostile to users.
3. **Measure, don't guess** — Her feed reader project is the canonical example: build instrumentation, collect data, publish results.
4. **Design for failure** — Systems will fail. The question is whether they fail gracefully (returning proper error codes, respecting rate limits) or catastrophically (spinning infinite loops, ignoring 429s, beating up the server).

### Autoconf and Software Evolution

Rachel has written critically about autoconf and build system complexity:

> *"Autoconf makes me think we stopped evolving too soon."*

Her argument: the proliferation of configure scripts, feature tests, and platform-specific workarounds represents a failure to converge on stable interfaces. Instead of standardizing, the ecosystem accumulated layers of compatibility code that no single person fully understands.

She contrasts this with systems that work because their interfaces are simple and stable — Unix pipes, HTTP conditionals, POSIX signals — versus systems that work *despite* their complexity, which inevitably break under edge cases.

### Working Inside Data Centers

Her "Thoughts on working inside a data center suite" essay captures the physical reality of infrastructure work:

- The sensory experience: noise, temperature, cable management, physical access controls
- The gap between "cloud" abstractions and the actual metal running them
- Why hands-on experience with physical infrastructure makes you a better engineer, even in a containerized world

> *"There's something about standing in a room full of blinking lights and humming fans that changes your relationship with 'the cloud.'"*

## Key Quotes

> *"I don't think people really appreciate what kind of mayhem some of their software gets up to."*

> *"If a web site makes an RSS or Atom feed available, it's not a bad idea to poll it from time to time. Actually doing it badly is a different matter entirely."*

> *"It's been over 25 years, and it's time to start using If-Modified-Since. It's in RFC 1945, aka the HTTP/1.0 spec."*

> *"The requirements become known after you start doing the thing."*

> *"Systems design and being bitten by edge-triggering — edge-triggered systems tell you once. Level-triggered systems keep telling you until you deal with it."*

> *"Let the network tell you where you are."*

## Recent Themes (2024–2026)

### Feed Reader Behavior Analysis (Ongoing)
- **Summarizing the last 45 days of feed reader behaviors** (Mar 2025) — Latest comprehensive report showing the state of reader compliance across 97+ distinct instances
- **Feed readers which don't take "no" for an answer** (Dec 2024) — Analysis of readers that ignore 429 rate limits and continue hammering servers
- **Feed score update: new hostname in effect** (Jan 2025) — Infrastructure migration to cast off abandoned reader instances and focus on active participants
- **A common bug in a bunch of feed readers** (Aug 2024) — Identified caching failures across multiple reader programs
- **Some early results for feed reader behavior monitoring** (Jun 2024) — Initial findings from the scoring project launch

### Systems Administration & Infrastructure
- **Problems with the heap** (Mar 2025) — Deep dive into memory management failures and heap corruption patterns
- **More thoughts on the 1670 modem's weird noises** (Mar 2025) — Acoustic analysis of modem signaling and protocol negotiation
- **Two modems, a length of line cord, and no battery** (Feb 2025) — Hardware debugging and telephony infrastructure
- **SSD death, tricky read-only filesystems, and systemd magic?** (May 2024) — Storage failure modes and recovery
- **Port-scanning the fleet and trying to put out fires** (Apr 2024) — Infrastructure security scanning and incident triage
- **Unintentionally troubleshooting a new way to filter traffic** (Jun 2024) — Accidental discoveries in network monitoring
- **Thoughts on working inside a data center suite** (Sep 2024) — Physical infrastructure operations

### Build Systems & Software Engineering
- **autoconf makes me think we stopped evolving too soon** (Mar 2024) — Critique of build system complexity accumulation
- **Hitting every branch on the way down** (Apr 2024) — Code coverage and testing philosophy
- **Reader feedback on autoconf and bugginess in general** (Apr 2024) — Community discussion on software quality

### Ethics & Philosophy
- **A reader asks how to avoid working for evil** (Dec 2022, still referenced) — Practical advice on ethical career choices in tech
- **Set me right on whether caring is even possible** (Oct 2024) — Reflection on emotional investment in infrastructure work
- **Web page annoyances that I don't inflict on you here** (Dec 2024) — Philosophy of reader-respecting web design

## Related

- [[entities/drewdevault-com]] — Shares Rachel's protocol-respect philosophy and critique of wasteful software
- [[concepts/feed-reader-behavior]] — Rachel's scoring methodology and findings
- [[concepts/http-conditional-requests]] — If-Modified-Since, If-None-Match, ETag best practices
- [[concepts/infrastructure-monitoring]] — Passive monitoring, fleet scanning, alert design
- [[concepts/outage-postmortems]] — Culture of incident documentation and learning
- [[concepts/unix-systems-administration]] — Practical operational wisdom

## Sources

- [rachelbythebay.com/w](https://rachelbythebay.com/w/) — Main blog
- [Summarizing the last 45 days of feed reader behaviors](https://rachelbythebay.com/w/2025/03/03/feed/) (Mar 2025)
- [Feed readers which don't take "no" for an answer](https://rachelbythebay.com/w/2024/12/17/packets/) (Dec 2024)
- [Two months of feed reader behavior analysis](https://rachelbythebay.com/w/2024/08/02/fs/) (Aug 2024)
- [A sysadmin's rant about feed readers and crawlers](https://rachelbythebay.com/w/2022/03/07/get/) (Mar 2022)
- [Problems with the heap](https://rachelbythebay.com/w/2025/03/26/heap/) (Mar 2025)
- [autoconf makes me think we stopped evolving too soon](https://rachelbythebay.com/w/2024/03/21/autoconf/) (Mar 2024)
- [Thoughts on working inside a data center suite](https://rachelbythebay.com/w/2024/09/23/dc/) (Sep 2024)
- [Systems design and being bitten by edge-triggering](https://rachelbythebay.com/w/2022/12/16/edge/) (Dec 2022)
- [The night of 1000 alerts](https://rachelbythebay.com/w/2022/11/18/alerts/) (Nov 2022)
- [Let the network tell you where you are: a nerd snipe story](https://rachelbythebay.com/w/2024/09/25/nerd-snipe/) (Sep 2024)
