---
title: "This site has buttons!"
url: "https://laplab.me/posts/buttons/"
fetched_at: 2026-05-05T07:01:23.778164+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# This site has buttons!

Source: https://laplab.me/posts/buttons/

This site has buttons now! Here, try to click it:
Click me!
I added buttons that act as a simple counter with a name attached. These are good for polls too!
Pineapple on pizza:
Yay
Nay
Of course, the results will be biased because there is no deduplication. I don’t limit the number of clicks at all. If you really want to express your view on the pineapple pizza or just love to click stuff - I encourage you to click multiple times!
I had a blast adding this little feature to the website. The whole thing is deployed on Cloudflare Workers and uses D1 as a database to store counters. To avoid blowing up the database size, none of the public APIs actually add any rows, they only update existing ones. All allowed counters are collected statically during the build time and uploaded through a private API during deploy.
I’m on free tier, so somebody can become really enthusiastic and spend my request limit on Worker calls. That’s fine! If somebody feels that strongly about a particular reaction, let them express it :) Static parts of this website will still work because they don’t go through a Worker and are served from CDN cache.
