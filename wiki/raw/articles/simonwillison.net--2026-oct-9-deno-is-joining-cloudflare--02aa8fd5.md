---
title: "Deno is joining Cloudflare"
url: "https://simonwillison.net/2026/Oct/9/deno-is-joining-cloudflare/"
fetched_at: 2026-10-10T10:00:52.548863+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Deno is joining Cloudflare

Source: https://simonwillison.net/2026/Oct/9/deno-is-joining-cloudflare/

9th October 2026 - Link Blog
Deno is joining Cloudflare
(
via
) The Deno team released the first version of
celld
back in August - their open source implementation of the Durable Objects pattern from Cloudflare Workers.
Today, Cloudflare are acquiring Deno outright, with the goal of building on
celld
to "make workerd self-hosting a first-class supported way to build and run apps using the Workers programming model" (see
the Cloudflare blog
.)
The bad news is that Deno itself will not be maintained by Cloudflare beyond the next year:
We will support the
Deno runtime
for another year with monthly releases containing bug fixes and security updates. After that year we will end our development of the Deno runtime. Deno will remain open source, and we welcome others who want to continue its development.
Deno (and Node.js) creator Ryan Dahl explained that decision in
a comment
on Hacker News:
It's a joint decision and I agree with it. I'm most invested in its success and have put the most work into it - and I no longer think it's where I can do the most important work. There are some good ideas in Deno and it's well engineered - but it ultimately is not solving big problems. It has been sucked into the gravity well of node compatibility, which forces it to behave exactly as Node does. Why reimplement Node? It works. Marginal performance or UX or security benefits are not enough.
I'm interested in building powerful new abstractions. celld has been working remarkably well, depending only on object storage for coordination and persistence. It is not just a slightly different API to interact with the file system or network - it's an entirely new model for server development.
My favorite feature of Deno has long been the permissions system, where you can run a Deno script and specify exactly which files and folders it can read and write to, and which network hosts it can access.
Node.js
has a similar permissions model
these days, added
in Node v20.0.0
in April 2023 and declared stable
in Node v22.13.0
in January 2025. They don't yet support allow-listing specific network hosts though - networking is either on or off.
