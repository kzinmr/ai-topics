---
title: "Wander Console 0.6.0"
url: "https://susam.net/code/news/wander/0.6.0.html"
fetched_at: 2026-05-09T07:01:08.607550+00:00
source: "susam.net"
tags: [blog, raw]
---

# Wander Console 0.6.0

Source: https://susam.net/code/news/wander/0.6.0.html

Wander Console 0.6.0
By
Susam Pal
on 08 May 2026
Wander Console 0.6.0 is now available.  This is the sixth release of
  Wander, a small, decentralised, self-hosted web console that lets
  visitors to your website discover interesting websites and pages
  recommended by a community of independent website owners.  To try
  it, go to
susam.net/wander/
.
  To learn how it works and how to set it up on your own website, see
  the project
README
.
The main change in this release is the removal of support for the
via
referral query parameter, which was added to
  recommended URLs so that website owners could identify visits coming
  from a Wander Console in their access logs.  The
via
query parameter was introduced in version
0.4.0
in response to
community
  demand
, but it turned out to be a misfeature.  Some websites
  refuse to serve web pages when arbitrary query parameters are added
  to URLs.  Although it was possible to turn this feature off via
  configuration, I would rather not keep a dubious feature that may
  prevent some pages from loading successfully.  This feature has now
  been completely removed.  See
this excellent
  article by Chris Morgan
to learn more about why adding arbitrary
  query parameters to URLs is a bad idea.  Commit
b26d77c
has more details about the removal of this feature.
Apart from this change, there are a few minor user interface
  adjustments and fixes.  See the
changelog
for more details.
If you own a personal website but have not set up a Wander Console
  yet, I suggest that you consider setting one up.  You can see what
  it looks like by visiting mine at
/wander/
.  To set up your
  own, follow the
installation
  instructions
in the README.  It only involves copying two files
  to your web server, so the installation is very straightforward.
Also, check out our new community page called
Wander Console
  Network
.  This page shows a recent snapshot of all known Wander
  Console instances along with the web pages they recommend.  We have
  an IRC channel too at
#wander
on
irc.libera.chat
in case you are looking for a place
  to hang out with the community.
Update on 09 May 2026:
See the post
I Will Not Add Query
  Strings to Your URLs
for an account of how the misguided
  referral query string feature was added and how it was removed.
