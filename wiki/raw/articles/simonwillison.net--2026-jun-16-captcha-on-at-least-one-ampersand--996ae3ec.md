---
title: "Cloudflare CAPTCHA on at least one ampersand"
url: "https://simonwillison.net/2026/Jun/16/captcha-on-at-least-one-ampersand/#atom-everything"
fetched_at: 2026-06-16T07:00:48.786141+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Cloudflare CAPTCHA on at least one ampersand

Source: https://simonwillison.net/2026/Jun/16/captcha-on-at-least-one-ampersand/#atom-everything

I'm using Cloudflare's CAPTCHA (they call it a "Web Application Firewall > Custom rules > Managed Challenge" these days) to prevent crawlers from aggresively spidering my
faceted search engine
on this site, but I got fed up of even simple
?q=term
searches triggering the challenge.
After some mucking around with Claude Code it turns out you can register the following rule instead, so the CAPTCHA only kicks in for search URLs containing at least one ampersand:
(http.request.uri.path wildcard r"/search/*" and http.request.uri.query contains "&")
And now
/search/?q=lemur
works without triggering a CAPTCHA!
Also included: notes on
trying out the Cloudflare MCP with Claude Code
, though it turned out not to be able to edit the rules in question so I had Claude Code
switch to the Cloudflare API
instead.
