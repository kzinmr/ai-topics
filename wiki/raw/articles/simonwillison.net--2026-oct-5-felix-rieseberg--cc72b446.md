---
title: "A quote from Felix Rieseberg"
url: "https://simonwillison.net/2026/Oct/5/felix-rieseberg/"
fetched_at: 2026-10-06T10:01:33.871850+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A quote from Felix Rieseberg

Source: https://simonwillison.net/2026/Oct/5/felix-rieseberg/

5th October 2026
The "old" version of Cowork runs model inference in the cloud, executing tool calls in an Anthropic-provided VM we shipped to your computer. We added the VM for capability, safety, and security reasons - mapping in just the data you explicitly added to your session. People loved what they were able to do with Claude but didn't love the disk, battery, and performance cost of running the VM locally. Also, people didn't love that closing your laptop means the work stops.
The "new" version of Cowork runs model inference and the VM in the cloud. Each session gets its own sandbox, not sharing state with other sessions. When the VM needs something on the users' device (like a file), the desktop app is responsible for that file access tool call. [...]
We think this solves a lot of problems we've heard about  (like using Cowork from a phone, keeping work running, or getting all the same power without losing battery to the VM)
—
Felix Rieseberg
,
Anthropic, see also
this help page
