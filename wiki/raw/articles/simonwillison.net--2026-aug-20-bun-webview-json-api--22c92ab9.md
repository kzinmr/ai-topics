---
title: "A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView"
url: "https://simonwillison.net/2026/Aug/20/bun-webview-json-api/"
fetched_at: 2026-08-21T10:01:06.650190+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView

Source: https://simonwillison.net/2026/Aug/20/bun-webview-json-api/

Today saw the long awaited
release of Bun 1.4
, the first stable version since the infamous Rust rewrite
a few months ago
.
Interestingly, the Rust rewrite was downplayed in the release notes, which introduced a bewildering array of new features and claimed 2,900 additional bug fixes:
Bun 1.4 adds +1,517 tests from the Node.js test suite - our biggest jump in Node.js compatibility since Bun 1.0. Bun v1.4 also fixes over 2,900 issues. It reduces idle CPU usage by 5x, reduces memory usage by up to 35%, and starts 50% faster on Linux. It adds
Bun.Image
,
Bun.WebView
,
Bun.markdown
,
Bun.cron()
,
Bun.Terminal
,
bun run --parallel
,
bun test --parallel
,
bun audit fix
,
bun dedupe
, and
bun prune
. And it rewrites Bun from Zig to Rust.
Of these the one that most caught my eye was
Bun.WebView
, which adds first class support for browser automation to Bun core using either macOS WebKit or control of a local Chromium process via the Chrome DevTools Protocol (CDP).
I had Claude Code for web build a prototype of a web API providing the ability to load a web page and then execute JavaScript against it, inspired by my
shot-scraper javascript
CLI tool - partly to see how much RAM would be needed by such a service.
Here's
that TypeScript server implementation
, which appears to need a 192MB-256MB container to run a full Chrome against complex web pages - tested using cgroups.
