---
title: "Visualizing a search in searchcode.com through the blinkenlights"
url: "https://boyter.org/posts/visualizing-a-search-in-searchcode/"
fetched_at: 2026-05-05T07:01:54.265477+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Visualizing a search in searchcode.com through the blinkenlights

Source: https://boyter.org/posts/visualizing-a-search-in-searchcode/

At GopherCon2023 I presented a talk about
how I built a custom index for searchcode
. In there somewhere I mentioned that having a visualization of how the search works is something I would like to add in.
With some free time on a weekend rather than “wasting” time playing a game I decided to actually build it, and as is the current trend on the internet attempted to vide code it, at least for the UI portion anyway.
You can view the result here
https://searchcode.com/tools/blinkenlights/
where it will play a speed controllable animation showing how the filter is being read, where the matches occur. Note that it is pulling the data from real searches that searchcode has processed, albeit only for a single of the bloom filters that back it.
When a search is run against the index one of the 4096 bit filters records the bits inspected, as well as the matches made. This data is kept and then if requested displayed to whoever is watching. If you don’t like the current search patterns refresh the page to get a new one.
A brief animation of what it looks like is included below with the speed set to the maximum. In reality the searches run on the server in ~20ms so the animation is several orders of magnitude slower than what actually happens.
I do like watching it run through. It’s especially interesting to see the patterns, and the skip ahead logic kick in when it identified there are no matches in the shard and skips to the next shard. If you see a total matches value greater than 10,000 you might even see it hit the early termination logic as well where the search has found too many matches.
