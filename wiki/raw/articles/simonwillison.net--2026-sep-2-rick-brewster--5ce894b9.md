---
title: "A quote from Rick Brewster"
url: "https://simonwillison.net/2026/Sep/2/rick-brewster/"
fetched_at: 2026-09-02T10:01:16.961969+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A quote from Rick Brewster

Source: https://simonwillison.net/2026/Sep/2/rick-brewster/

Direct2D has always been the biggest hurdle for Paint.NET on WINE, and it's clear that it will never be completed enough for Paint.NET's use. And I can't just "disable" the use of Direct2D. So, instead,
Paint.NET now has an internal, from-scratch, clean-room reverse-engineered rewrite of Direct2D that it uses on WINE
(triggered by using
/wine
). It lives in
PaintDotNet.Windows.Direct2D1.Managed.dll
. This was written by our good friend
Claude
, without whom this would NOT have been possible and would NEVER have happened. [...]
Most of this code is, as they say, "vibe coded." By that I mean that it has not been thoroughly reviewed, it's more "trust me bro" style. I cannot possibly review 180,000 lines of code, it's just way way
way
too much. For reference, the rest of Paint.NET is about 700,000 lines of code and I've been working on it for over 20 years. [...]
At times, Claude was working with the fury of 10 freshly unshackled Einstein genius-level 10x coders. And other times ... well, not so much. I had to babysit Claude quite a bit to make sure it did resource management correctly (for awhile it just wasn't doing the COM equivalent of AddRef() for reference counted objects, oops). I had to slap it a few times when I found some really bad design or architecture decisions. And I was also impressed at some rather clever and tireless reverse engineering work it did to figure out all the formulas needed for implementing Direct2D's built-in effects library.
