---
title: "Release: ttok 0.4"
url: "https://simonwillison.net/2026/Oct/8/ttok/"
fetched_at: 2026-10-09T10:01:07.918324+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: ttok 0.4

Source: https://simonwillison.net/2026/Oct/8/ttok/

ttok
is my CLI tool for counting tokens, using OpenAI's open source
tiktoken
library.
It hasn't been in updated in a couple of years, but I finally fixed a Click warning, updated CI, and added a
--list-models
command to list available models.
It works with
uvx
, so you can count tokens in anything like this:
cat file.txt | uvx ttok
