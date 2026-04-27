---
title: "Wander Console 0.3.0"
url: "https://susam.net/code/news/wander/0.3.0.html"
fetched_at: 2026-04-27T07:58:01.362939+00:00
source: "susam.net"
tags: [blog, raw]
---

# Wander Console 0.3.0

Source: https://susam.net/code/news/wander/0.3.0.html

Wander Console 0.3.0
By
Susam Pal
on 25 Mar 2026
Wander 0.3.0 is the third release of Wander, a small, decentralised,
  self-hosted web console that lets visitors to your website explore
  interesting websites and pages recommended by a community of
  independent website owners.  To try it, go
  to
susam.net/wander/
.
This release brings small but important bug fixes.  The previous
  release,
version 0.2.0
introduced a number
  of new features.  Unfortunately, two of them caused issues for some
  users.  A new feature in the previous release was
  the
ignore
list feature.  The
ignore
list
  defines console URLs and page URLs that the console never uses while
  discovering page recommendations.  While this feature works fine,
  due to a bug in the implementation, the
Console
dialog fails to load in consoles that do not define
  any
ignore
list.  This has now been fixed.
There was another issue due to which the
<iframe>
that displays discovered websites and pages could not load certain
  websites.  In particular, any website that relied on same-origin
  context to load its own resources failed to load in the console.
  This has been fixed as well.  Please see
codeberg.org/susam/wander/issues/7
for a detailed discussion on this issue.
Apart from these two important fixes, there are a few other minor
  fixes too pertaining to preventing horizontal scrolling in small
  devices and preventing duplicate recommendations from appearing too
  close to each other.  Please
  see
CHANGES.md
for a detailed changelog.
To learn more about Wander, how it works and how to set it up,
  please read the project README at
codeberg.org/susam/wander
.
  To try it out right now, go to
susam.net/wander/
.
