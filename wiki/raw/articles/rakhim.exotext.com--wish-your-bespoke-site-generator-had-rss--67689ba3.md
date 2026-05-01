---
title: "I wish your bespoke React-Tailwind-etc static site generator had RSS"
url: "https://rakhim.exotext.com/wish-your-bespoke-site-generator-had-rss"
fetched_at: 2026-05-01T07:01:23.420904+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# I wish your bespoke React-Tailwind-etc static site generator had RSS

Source: https://rakhim.exotext.com/wish-your-bespoke-site-generator-had-rss

I discover and curate dozens of blogs every day while working on
Minifeed
. The blogging is far from dead, there are SO many blogs out there!
Sadly, lots of blogs don't have RSS. What's surprising is that the "techiest" of blogs usually don't have RSS. Quite often, I come across a beautiful blog, handcrafter with love by a passionate programmer, usually built with some modern frontend stack like React/Vue/Svelte, with Tailwind or Astro or what have you; there's a complex deployment pipeline with automatic publishing on git commits, some automated intelligent image-optimization CDN integration, client-side search with shortcuts and amazing performance, dark mode... Lots of stuff!
But no RSS.
Sometimes the blog is not just a handcrafted frontend app, but is the output of a handcrafted static site generator. They who hadn't written their own SSG can cast the first stone! I built multiple, and some of them did not have RSS either. Guilty! But it's hard to justify, as generating an RSS feed is going to be a simple task once you've written the actual HTML generation. It's basically the same, just a different format of XML :) Please, consider adding RSS to your hand-crafted SSG.
Other times, RSS is there, but it has issues. Some of them:
There is no
meta
tag, so blog readers cannot find the feed by parsing the HTML page.
<link rel="alternate" type="application/rss+xml" title="RSS Feed for petefreitag.com" href="/rss.xml" />
RSS is invalid. Simply outputting the HTML into an XML value might break things. Please, validate your RSS (e.g.
here
).
RSS content does not match actual content.
RSS items don't have permanent IDs, and force RSS readers to come up with heuristics to uniquely identify entries. Usually, the URL is used for this purpose, but authors often edit the URL after publishing, sometimes multiple times. Readers might see this as 3 separate entries (2 of which will link to 404).
The standard, off-the-shelf blogging solutions are the best. Whenever I see a good old Wordpress, Blogspot, or a Ghost blog, I know there will be a working and valid RSS. Interestingly, newsletter platforms like Substack or
Buttondown
offer full-content RSS! "Standard" static site generators like Jekyll and Hugo usually mean there will be RSS. But since it's so customizable, there are still problems sometimes. Especially when the author uses Hugo's rich (and, subjectively, confusing) content organization features.
