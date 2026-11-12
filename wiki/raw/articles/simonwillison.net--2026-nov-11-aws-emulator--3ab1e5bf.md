---
title: "aws-emulator"
url: "https://simonwillison.net/2026/Nov/11/aws-emulator/"
fetched_at: 2026-11-12T10:01:09.683280+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# aws-emulator

Source: https://simonwillison.net/2026/Nov/11/aws-emulator/

11th November 2026 - Link Blog
aws-emulator
. Finally, an official emulator from AWS to run tests against a local clone of their many different services without having to provision a paid API key to do so.
It's written in Rust by a huge swarm of agents - 29,684 commits in the first three weeks of the project. Swaminathan (Swami) Sivasubramanian wrote about
how it came to be
in a guest post on Werner Vogels' blog.
It currently requires Docker to run on macOS or Windows. I'm hoping they fix that in the future - it would be great if you could download a single binary and use that as part of a standard test suite in other languages and on other platforms.
