---
title: "CSP Allow-list Experiment"
url: "https://simonwillison.net/2026/May/13/csp-allow/#atom-everything"
fetched_at: 2026-05-13T07:01:24.162748+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# CSP Allow-list Experiment

Source: https://simonwillison.net/2026/May/13/csp-allow/#atom-everything

An experiment that shows that you can load an app in a CSP-protected sandboxed iframe (see
previous note
) and have a custom
fetch()
that intercepts CSP errors and passes them up to the parent window... which can then prompt the user to add that domain to an allow-list and then refresh the page.
I built this one with GPT-5.5 xhigh running in the Codex desktop app.
