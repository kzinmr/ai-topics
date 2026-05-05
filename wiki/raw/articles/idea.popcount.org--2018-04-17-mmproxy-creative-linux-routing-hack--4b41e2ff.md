---
title: "mmproxy - creative linux routing hack"
url: "https://idea.popcount.org/2018-04-17-mmproxy---creative-linux-routing-hack"
fetched_at: 2026-05-05T07:01:08.717884+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# mmproxy - creative linux routing hack

Source: https://idea.popcount.org/2018-04-17-mmproxy---creative-linux-routing-hack

mmproxy - creative linux routing hack
17 April 2018
I've published an article on how we abused TPROXY iptables module to
build
mmproxy
, a simple Proxy Protocol v1 proxy that can "preserve"
(or locally spoof) client IP addreses. It's pretty useful together
with Cloudflare Spectrum:
