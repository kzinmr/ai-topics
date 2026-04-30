---
title: "Here we go | exotext"
url: "https://rakhim.exotext.com/here-we-go"
fetched_at: 2026-04-30T07:01:14.422887+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# Here we go | exotext

Source: https://rakhim.exotext.com/here-we-go

I just wanted to write again. My old blog at
rakhim.org
is built with Hugo, and after installing a new version of Hugo things broke. After 25 minutes of attempts to fix it I though "yeah, that's it", and decided (as you do) to just build a simple blogging platform.
Static site generators are great. Hugo though has too many features I never use. But my overall issue with static site generators is UX. Unlike, apparently, many others in tech circles, I don't enjoy writing in my normal code editor, nor do I find joy in publishing via git, and not having simple image uploads.
Sure, there are fully fledged blog engines like Ghost and Wordpress (with its
drama
). I've used both for a long time in the past in various projects, and was generally ok with either. Today, ghost is trying really hard to become a "publishing" thing, with its magazine-like themes, paid memberships, and newsletters. Wordpress is just scary, to be honest (same vibe as Java or Kubernetes).
There are very nice, small platforms like
Bear
,
Pika
,
Mataroa
. Each would actually be pretty much perfect for me. But I always wanted to build my own platform, with some specific features and UX nuances.
So, yeah. I'm starting today! It's called Exotext, and for now there's only one blog: mine. I'll write (among other things) about its development. In short, I want to focus on these things:
Simple writing experience with minimized traction.
Beautiful design and typography out of the box.
Fast. Every page should render under 0.5s.
Old web UX. Absolute minimum JS, no SPA stuff, no client-side rendering shenanigans.
Portability. No lock in. It should be easy to export data and fully rendered HTML website when needed.
Some sort of community features. Perhaps comments.
Good online markdown editor and easy image uploads.
RSS (of course, especially since I'm also building
Minifeed
, an RSS discovery and search engine).
Speaking of markdown editors: it's damn hard to find a good one. For now, I'm using
TinyMDE
, which is almost perfect. It doesn't handle undo, though. Oh, you know what's even harder? Finding a Markdown editor which can be used with vanilla JS. There are some very nice editors built on React, Svelte, Vue and other frameworks, and I dread the though of dealing with that complexity.
Let's see how it goes.
