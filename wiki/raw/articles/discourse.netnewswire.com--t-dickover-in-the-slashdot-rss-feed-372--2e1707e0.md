---
title: "Dickover in the Slashdot RSS feed"
url: "https://discourse.netnewswire.com/t/dickover-in-the-slashdot-rss-feed/372"
fetched_at: 2026-09-07T10:01:46.522689+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Dickover in the Slashdot RSS feed

Source: https://discourse.netnewswire.com/t/dickover-in-the-slashdot-rss-feed/372

Joerg
September 6, 2026,  4:45am
1
Since a couple of weeks I see a cookie banner presented in the slashdot feed. I don‘t think I have ever seen something like that in an RSS feed before and I‘m unsure if this is a bug or if NNW can do something about it. Because it somehow interrupts the flow.
The feed URL:
Slashdot
1 Like
buchb
September 6, 2026,  1:49pm
2
Looks like it’s loading the actual website, probably in an iframe
brent
September 6, 2026,  3:26pm
3
Which version of NetNewsWire are you using? In NetNewsWire 7.1.3 we added some code to prevent this from Slashdot.
(It’s possible that they’ve changed their HTML so that our fix no longer works, of course.)
Joerg
September 6, 2026,  4:42pm
4
It‘s the current Testflight Build 7210. I noticed that the message doesn‘t pop up on every new article. Kind of odd.
