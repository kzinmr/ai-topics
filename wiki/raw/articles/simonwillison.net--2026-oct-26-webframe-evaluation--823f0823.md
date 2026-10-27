---
title: "evaluated as a scraper and a sandbox"
url: "https://simonwillison.net/2026/Oct/26/webframe-evaluation/"
fetched_at: 2026-10-27T10:01:03.521627+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# evaluated as a scraper and a sandbox

Source: https://simonwillison.net/2026/Oct/26/webframe-evaluation/

webframe
is a neat little project from Jeff Lindsay which lets you "run a web page like a program" - you point it at a URL or file and it executes it in a hidden headless web view and outputs
console.log()
to standard output and any exceptions to standard error.
It's written in Go on top of the
glaze
library, which provides access to a system browser ("WKWebView on macOS, WebKitGTK on Linux, WebView2 on Windows") so it doesn't need to bundle its own browser engine.
It reminds me of my own
shot-scraper javascript
tool, albeit in a much smaller package that doesn't depend on Playwright.
I had Claude Opus 5.5
put it through its paces
and prepare a research report for me. Here's the prompt I used:
Explore https://github.com/tractordev/webframe try running it and put it though its paces, build a few exploratory prototypes, then evaluate it as a potential sandboxing tool and as a tool for scraping web pages using the same patterns encouraged by the "shot-scraper JavaScript" command (see simonw/shot-scraper on GitHub, docs directory)
