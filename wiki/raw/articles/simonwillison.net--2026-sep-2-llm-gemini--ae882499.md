---
title: "Release: llm-gemini 0.34"
url: "https://simonwillison.net/2026/Sep/2/llm-gemini/"
fetched_at: 2026-09-03T10:00:50.129432+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm-gemini 0.34

Source: https://simonwillison.net/2026/Sep/2/llm-gemini/

Google released
Gemini 3.8 Flash
(and 3.8 Flash Cyber, but that's available to "trusted defenders" only) today.
Here are
the pelicans
for high, medium, and low. This is high:
For comparison, here are the same pelicans
generated using Gemini 3.7 Flash
.
Something I appreciate about Gemini Flash is that it's fast, cheap, and competent at things like HTML and JavaScript. I was messing around with it and prompted "make me a cool thing in html" and
it built this
, which is certainly a cool thing in HTML! Took 13 seconds, cost 1.8 cents.
Your browser does not support HTML5 video.
If you click through to
the demo
you'll see one more thing I built with Gemini 3.8 Flash.
My
markdown-svg-renderer tool
lets me feed in the URL to a Gist with Markdown in and renders that markdown with fenced code blocks for SVG correctly rendered.
I used Gemini 3.8 Flash (with my
very
basic
llm-coding-agent
coding agent plugin) to add support for HTML as well, so now any HTML blocks in the Markdown are rendered using a sandboxed iframe.
Here's the transcript
.
