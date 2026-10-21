---
title: "eMudhra Intermediate CA Compromise"
url: "https://simonwillison.net/2026/Oct/20/emudhra-certificates/"
fetched_at: 2026-10-21T10:00:51.524103+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# eMudhra Intermediate CA Compromise

Source: https://simonwillison.net/2026/Oct/20/emudhra-certificates/

20th October 2026 - Link Blog
eMudhra Intermediate CA Compromise
. This is very, very bad news:
The private keys of eight eMudhra intermediate CA certificates have been compromised. They chain to roots trusted by the Mozilla, Microsoft, Apple and Chrome root programs and by many downstream trust stores.
Any software that bundles a list of trusted certificates needs to be updated. This site is tracking software updates
via this GitHub repository
- Linux distros need to update their
ca-certificates
packages.
In Python world
uv 0.13.4
and
pip 26.2.2
and
certifi 2026.10.19
have been released with upgraded certificate lists.
