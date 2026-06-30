---
title: "Count the number of Safari tabs"
url: "https://simonwillison.net/2026/Jun/29/safari-tab-count/#atom-everything"
fetched_at: 2026-06-30T07:01:00.395885+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Count the number of Safari tabs

Source: https://simonwillison.net/2026/Jun/29/safari-tab-count/#atom-everything

29th June 2026
Tiniest TIL, using AppleScript to count the number of open browser tabs in Safari:
osascript -e 'tell application "Safari" to count tabs of every window'
