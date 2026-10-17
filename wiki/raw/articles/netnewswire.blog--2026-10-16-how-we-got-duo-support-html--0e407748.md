---
title: "How We Got Duo Support in NetNewsWire"
url: "https://netnewswire.blog/2026/10/16/how-we-got-duo-support.html"
fetched_at: 2026-10-17T10:05:41.250699+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# How We Got Duo Support in NetNewsWire

Source: https://netnewswire.blog/2026/10/16/how-we-got-duo-support.html

The
latest version
of NetNewsWire for iOS supports iPhone Duo, which is very much a novel iPhone with toolbars running up the side and all kinds of behavior.
How we did it: we didn’t do any work at all. We built the app using Xcode 27.1 and the default iOS SDK that comes with it, and that’s it.
Here’s the thing, though: we were already using standard controls — toolbars, navigation controllers, split views, etc. — and we were paying attention to size classes and such (as opposed to just looking at device type).
There is a good list of reasons to use standard controls in the standard ways, and near the top of that list is to be ready for these kinds of days, so we’re not bogged down for a month or more trying to adapt to big changes like this.
Here’s a secret: Brent didn’t even run this in the Duo simulator before releasing it. We were ready to
not
claim Duo support and just handle Duo in the next release. But here it is.
PS Of course there may be edge cases and issues in our Duo support we haven’t caught yet. We stand by, as always, ready to field and fix bugs.
PPS Thank you to all the engineers, designers, and testers at Apple who made this work so easily! Again, we didn’t do anything but build with the new SDK. Their achievement is pretty remarkable.
