---
title: "OpenSSH 10.4 released"
url: "https://lwn.net/Articles/1081536/"
fetched_at: 2026-07-07T07:01:42.631259+00:00
source: "LWN.net"
tags: [blog, raw]
---

# OpenSSH 10.4 released

Source: https://lwn.net/Articles/1081536/

OpenSSH 10.4 released
[Posted July 6, 2026 by jzb]
OpenSSH 10.4 has been released. In addition to a number of security
and bug fixes, there are a few notable changes; this release adds
experimental support for a composite post-quantum signature scheme
combining ML-DSA 44 and Ed25519 as described in
this
IETF draft
. With 10.4, if OpenSSH is compiled with sandbox support
it will fail on Linux systems that have not enabled
SECCOMP
or
NO_NEW_PRIVS
; prior to this release,
sshd
would log an error
but continue operation. See the
release notes
for
a full list of changes.
