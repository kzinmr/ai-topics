---
title: "We just shipped support for the ugliest part of HTTP: Vary"
url: "https://simonwillison.net/2026/Sep/23/hn-49823961/"
fetched_at: 2026-09-28T10:02:14.602692+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# We just shipped support for the ugliest part of HTTP: Vary

Source: https://simonwillison.net/2026/Sep/23/hn-49823961/

I've been wanting this from Cloudflare
for years
.
The classic problem here is if you do that thing where user agents that send "accept: text/html" get HTML, while user agents that don't get JSON or some other format.
This used to be impossible to deploy behind Cloudflare caching, because they ignored the Vary header on anything other than images - so you risked caching the JSON version and then serving it up to someone who was expecting HTML.
(Independent of the Cloudflare feature I ended up deciding never to use that pattern, because I prefer having URL that predictably returns HTML or JSON - I add a .json suffix to my apps to serve JSON instead.)
