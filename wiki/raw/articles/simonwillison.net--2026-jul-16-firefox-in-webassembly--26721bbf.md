---
title: "Firefox in WebAssembly"
url: "https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything"
fetched_at: 2026-07-17T07:00:57.729727+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Firefox in WebAssembly

Source: https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything

16th July 2026 - Link Blog
Firefox in WebAssembly
(
via
) This is absurdly cool: Puter compiled Firefox to WebAssembly such that the whole browser runs in another browser.
Here's my blog, running in Firefox, running in WebAssembly, running in Chrome:
They chose Firefox/Gecko because it has strong single-process support. The project used an estimated $25,000 worth of Claude Opus and Fable tokens, but took advantage of a Claude Max subscription plan so cost much less in actual dollars.
The demo funnels all traffic over a WebSocket protocol (using the
Wisp protocol
) through Puter's server - a requirement to get this kind of thing to work because code running in browsers can't open arbitrary network connections.
(That proxying sounds expensive! The team
had to scale the servers up
to handle the traffic during the Hacker News conversation about the project.)
Puter claim this supports end-to-end encryption and that looks to be true - I inspected the WebSocket messages and traffic to my own HTTPS site was encrypted whereas requests and responses to
http://www.example.com/
were in cleartext.
Here's the repo
for
firefox-wasm
.
theogbob/WebkitWasm
is a similar project that compiles WebKit to WASM, but that one doesn't currently have an accessible online demo.
