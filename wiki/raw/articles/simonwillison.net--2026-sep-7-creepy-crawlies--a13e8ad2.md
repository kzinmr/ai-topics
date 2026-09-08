---
title: "Creepy crawlies"
url: "https://simonwillison.net/2026/Sep/7/creepy-crawlies/"
fetched_at: 2026-09-08T10:01:09.986263+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Creepy crawlies

Source: https://simonwillison.net/2026/Sep/7/creepy-crawlies/

7th September 2026 - Link Blog
Creepy crawlies
(
via
) Konstantin Ryabitsev discusses how bad the "background radiation" of abusive crawlers has become from the perspective of
git.kernel.org
, the official Git repository for the Linux kernel:
TL;DR: we spend more CPU cycles rendering commits for scrapers than we spend on all other kinds of legitimate access, including git clones. At any one time, across 5 geo-distributed nodes, there are 14 CPU cores doing nothing but rendering git commits as html.
I worry about this a lot from the perspective of Datasette, which serves a huge number of crawlable web pages.
