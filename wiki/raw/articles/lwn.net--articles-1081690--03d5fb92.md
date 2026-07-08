---
title: "Woodruff: You shouldn't trust trusted publishing"
url: "https://lwn.net/Articles/1081690/"
fetched_at: 2026-07-08T07:00:57.521322+00:00
source: "LWN.net"
tags: [blog, raw]
---

# Woodruff: You shouldn't trust trusted publishing

Source: https://lwn.net/Articles/1081690/

Woodruff: You shouldn't trust trusted publishing
[Posted July 7, 2026 by jzb]
William Woodruff, better known online as "yossarian", has
published
a blog post to make the case that users should not place their trust
in
trusted
publishing
:
Trusted Publishing is a mechanism for establishing trust between an
external machine identity (like a CI/CD workflow) and one or more
projects on a package index/registry. The "trust" in "Trusted
Publishing" refers to that trust relationship, and not to anything
else.
It is not, and cannot be, a signal for package trust or
quality. You cannot use it to determine whether a package is safe or
"good," and PyPI consciously stymies attempts to misuse it for that
purpose by not rendering it as a "green checkmark" or anything else of
the sort.
Or as another framing: Trusted Publishing is just a form of
authentication. It doesn't tell you anything other than that an upload
was authenticated, which all uploads to PyPI are.
LWN
covered
trusted
publishing in June.
