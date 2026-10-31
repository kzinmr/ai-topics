---
title: "Remote code execution on Linux systems with multipath TCP"
url: "https://lwn.net/Articles/1104192/"
fetched_at: 2026-10-31T17:56:41.436907+00:00
source: "LWN.net"
tags: [blog, raw]
---

# Remote code execution on Linux systems with multipath TCP

Source: https://lwn.net/Articles/1104192/

Remote code execution on Linux systems with multipath TCP
[Posted October 30, 2026 by daroc]
On October 27, LLM provider Anthropic
reported
on
a
remotely exploitable use-after-free bug
affecting systems with
multipath TCP listeners open. The bug works by triggering a response to a
retransmitted SYN packet at the same moment that the TCP connection is
established in another thread, causing the first thread to access the
connection's options structure after the second thread has freed it. The first
thread can then disclose kernel memory or cause a buffer overflow, writing an
attacker-controlled payload. The fix was
to only free the structure after an RCU grace period
.
On October 29, the Go security team
advised
that all programs written in Go use multipath TCP by default
, so many
systems may be unknowingly vulnerable. And, of course, there is always the
possibility of related bugs in other sections of the TCP stack. Users may be
wise to update to a patched kernel as soon as one becomes available for their
distribution.
