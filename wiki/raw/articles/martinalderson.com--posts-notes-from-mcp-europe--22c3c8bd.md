---
title: "Notes from MCP Dev Summit Europe: Where the Protocol Is Headed"
url: "https://martinalderson.com/posts/notes-from-mcp-europe/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-29T07:02:04.355921+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Notes from MCP Dev Summit Europe: Where the Protocol Is Headed

Source: https://martinalderson.com/posts/notes-from-mcp-europe/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I've been at the MCP Dev Summit Europe conference today in London. I don't think I've seen such a busy conference so quickly after a technology has been announced - it's clear to me there is enormous interest in it. Furthermore, a lot of the attendees were from large corporates, which is a bit unusual with bleeding edge technologies in my experience.
Future of MCP Protocol
David Soria Parra from Anthropic did a really great talk updating on the progress of the MCP standard. I think the big takeaway for me was Agentic Discovery, which David mentioned was a vision for the next year.
It feels like the use case for MCP Registry isn't an app store as we knew it from mobile apps, but MCPs discovered by LLMs that then install themselves.
I have big concerns about how this vision is going to work from a security perspective, but (small) steps are being made with DNS and GitHub based authentication for MCP servers. It's very hard to protect against prompt injection attacks, even when they are manually 'hand picked'. Having any kind of automated installation process is going to make it far harder.
If the security issues could be mitigated it opens so many incredible use cases for non technical end users. Configuring and installing MCP servers is too hard at the moment, so if it could figure out how to get the users data I think it's going to be absolutely transformative for b2b use cases, but also b2c - you can imagine it for travel finding flights, checking you in, booking your hotel and restaurants - across dozens of MCP servers, completely transparently to the user.
MCP clients support very little of the MCP standard
I hadn't quite put two and two together and realised how little of the MCP standard clients support. From data from the HuggingFace MCP server, these are the most popular MCP clients:
and overall support of various primitives:
Unfortunately the rate of compatibility for MCP clients supporting anything apart from the most basic parts of the spec is very low. Again, another chicken and egg problem.
I think it's important to keep this in mind when designing MCP servers. It's very easy to get excited by all the new parts of the spec (for good reason!) but for real world workflows it's reminding me a bit of the early web browsers with very fragmented compatibility, so much so it wasn't really worth pushing the envelope far. Hopefully this changes quickly, but my gut feeling says we're going to see much more of this and a lot of falling back to 'lowest common denominator' with MCP.
MCP Gateways
There are a
lot
of gateways for MCP being built, effectively "Cloudflare for MCP". Many of these looked genuinely interesting and it'll be interesting to see who gains marketshare on this.
The
main
selling point of these seemed to be easy OAuth integration, amongst other features. People aren't enjoying implementing OAuth for MCP, especially dynamic client registration which virtually none of the well known auth-as-a-service providers implement correctly out of the box.
AX - Agentic Experience
Finally I really enjoyed Frédéric Barthelet's talk on AX (agentic experience, similar to UX and DX). There was a lot of good stuff in the talk, and you can
find the slides here
which I'd really recommend reading through.
Very simple things - like having param sigs take a variety of formats can radically improve the accuracy of tool results.
Another good one was really thinking about error messages - far more than you'd probably think of in most software engineering.
I'm looking forward to reading more about AX - which I think is going to become a whole specialisation of its own in the very near future.
