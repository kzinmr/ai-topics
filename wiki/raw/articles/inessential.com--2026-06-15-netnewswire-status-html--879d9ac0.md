---
title: "NetNewsWire Status"
url: "https://inessential.com/2026/06/15/netnewswire-status.html"
fetched_at: 2026-06-19T07:00:57.620273+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# NetNewsWire Status

Source: https://inessential.com/2026/06/15/netnewswire-status.html

It’s been a year since I retired — my
last working day
was June 6, 2025 — and I like being able to say that I’ve spent the year adding nothing, not one penny, to shareholder value. 🌴
* * *
My hope for retirement was to get a lot of work done on
NetNewsWire
.
A year ago it was in sore need of modernization, tech debt pay-off, and bug fixes. People were asking for features, but the foundation needed a ton of work before I could get on to adding new rooms.
Here are some highlights of what we’ve done with 2,188 commits in the past year:
Adopted Swift structured concurrency and async/await
Adopted Liquid Glass UI while still supporting recent OSes
Ported our XML, HTML, and date parsers from Objective-C to Swift
Fixed a ton of bugs, including crashing bugs
Reduced battery use, memory use, hang rate, scroll hitch rate, and disk writes
Did a bunch of performance enhancements, including (especially) finding places where the app could just do less work
Did a bunch of hygiene things — got GitHub CI running again, started using SwiftLint, turned on treat-warnings-as-errors, started work on localizability, switched to Logger, added tests
Simplified and refactored code, deleted code, renamed things, etc. — gained clarity in a bunch of places
Added support for Cache-Control headers for feeds, so publishers can tune how often NetNewsWire checks their feeds
Optimized iCloud syncing (still more to do on that one)
Dealt with deprecations (switched to
NWPathMonitor
, for instance)
Added diagnostics and error reporting to the UI —
iCloud Storage Stats
and the
Error Log
are shipping, and more like these are currently in beta:
Dinosaurs
,
Current Activity
,
Activity Log
, and
Account Stats
.
A list of highlights means I’m glossing over — or not even mentioning — things I really want to tell you about!
For instance, at one point I got frustrated with how I was handling Mac crash logs, so I wrote a little system that downloads them from my server and does symbolication. It’s simple but it makes a big difference — and it means
not
migrating to some commercial system, and having to add their SDK to the app, for this.
* * *
That last bullet point, the one with all the links, is all about giving users insight into what’s happening so that, when the app doesn’t behave as they expect, they can see what’s going on.
Even when they can’t fix the problem themselves, they can at least then copy-and-paste and tell me what’s up so I don’t have to guess. Between this and various bug fixes and improvements I’m able to spend less time on support, which means more time for coding — and, eventually, more time for the new features people are asking for.
* * *
We’re not done with foundational work, but it’s getting close. It’s so much nicer working on this app now than it was a year ago, and I’m so glad we spent the year this way.
I say
we
on purpose — I may contribute the most, but we have a bunch of
other contributors
, and I thank them all for all their much-appreciated help. Our most prolific contributor after me is
Stuart Breckenridge
, who did the Liquid Glass work (among other things) — and who has a new browser-based
RSS reader named Gobbler
that you should check out!
* * *
PS In the past year we also switched from Slack to a
Discourse forum
, so support and discussions can be on the web instead of hidden away. 😀
