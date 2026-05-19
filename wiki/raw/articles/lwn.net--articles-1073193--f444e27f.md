---
title: "Kernel prepatch 7.1-rc4"
url: "https://lwn.net/Articles/1073193/"
fetched_at: 2026-05-18T07:01:09.534062+00:00
source: "LWN.net"
tags: [blog, raw]
---

# Kernel prepatch 7.1-rc4

Source: https://lwn.net/Articles/1073193/

Kernel prepatch 7.1-rc4
[Posted May 17, 2026 by corbet]
The
7.1-rc4
kernel prepatch is out for
testing.
Some of the documentation updates might be worth highlighting: the
	continued flood of AI reports has basically made the security list
	almost entirely unmanageable, with enormous duplication due to
	different people finding the same things with the same
	tools. People spend all their time just forwarding things to the
	right people or saying "that was already fixed a week/month ago"
	and pointing to the public discussion.
Which is all entirely pointless churn, and we're making it clear
	that AI detected bugs are pretty much by definition not secret, and
	treating them on some private list is a waste of time for everybody
	involved - and only makes that duplication worse because the
	reporters can't even see each other's reports.
(He is referring to
this
pull request
with patches from Willy Tarreau defining
what constitutes a security
bug
and
responsible
ways to use AI to find bugs
).
