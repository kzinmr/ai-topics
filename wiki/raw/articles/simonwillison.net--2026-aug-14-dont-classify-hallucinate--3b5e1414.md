---
title: "Don't classify. Hallucinate!"
url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
fetched_at: 2026-08-15T10:14:58.302452+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Don't classify. Hallucinate!

Source: https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/

14th August 2026 - Link Blog
Don't classify. Hallucinate!
I still have quite a bit of older content on my blog that I never got round to tagging. My blog has
1,856 tags
- likely too many to feed to an LLM in one go and say "which of these tags match the following content".
Doug Turnbull has a neat solution. Tell the model to output tags without any details of the existing vocabulary, then use vector embeddings against the existing corpus to find the concrete tags that are closest to the ones the model imagined might fit!
His example prompt suggests including an example of the shape of your tags to help the model make a more useful guess:
Your task is to create novel, never seen before, furniture, home goods, or hardware classification that best fit a search query.
Product classifications might look like:
Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables
Décor & Pillows / Decorative Pillows & Blankets / Throw Pillows
Furniture / Bedroom Furniture / Dressers & Chests
Kitchen & Tabletop / Kitchen Organization / Food Storage & Canisters
School Furniture and Supplies / School Furniture / School Chairs & Seating / Stackable Chairs
Baby & Kids / Toddler & Kids Bedroom Furniture / Kids Beds
Here's the query to generate classifications for:
brown coffee table
