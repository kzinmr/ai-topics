---
title: "Creating a Personal URL Shortener with Dub and Raycast"
url: "https://danielwirtz.com/blog/personal-url-shortener"
fetched_at: 2026-11-01T10:01:33.404770+00:00
source: "danielwirtz.com"
tags: [blog, raw]
---

# Creating a Personal URL Shortener with Dub and Raycast

Source: https://danielwirtz.com/blog/personal-url-shortener

I’m a big fan of
Raycast
and occasionally watch their YouTube videos to stay updated on its features. My favorites are the “What’s in ____ Raycast” videos, where they showcase how others use Raycast.
One brilliant showcase is the
video with Max Stoiber
, where he walks through his hyper key setup (which I also adapted) and demonstrates various custom commands and scripts he uses. If you’re interested in Raycast, definitely check out that video.
One feature he implemented was a personal short link command, allowing him to create short links on the go and quickly search them. I found this quite useful and saw potential use cases for myself, so I started to look around for a cheap short link.
When I discovered that the domain
dawi.co
was available for purchase, I couldn’t resist. While there might be shorter domains (and cheaper ones…), I like that it’s basically a short form of my domain:
Similar to Max, I wanted to implement the URL shortener in Raycast. So I started working on a custom Raycast extension to integrate
LinkDrip
—which I own a lifetime subscription for. However, I was quickly stuck because the LinkDrip API doesn’t support custom slugs for short links. Ugh.
After some research on Reddit and Hacker News for modern URL shortener recommendations, I stumbled upon
Dub
. I think Dub is relatively new but perfect for my needs because it offers a generous free tier (great for personal use) and a Raycast extension. Exactly what I was looking for!
I’ve already implemented a few basic short links, such as my social media (e.g.,
dawi.co/x
) and quick meeting links (e.g.,
dawi.co/15
for a quick 15-minute meeting).
Do you have ideas for other short links I could implement? Let me know!
