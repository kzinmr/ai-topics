---
title: "A security bug in AEAD sockets"
url: "https://lwn.net/Articles/1070454/"
fetched_at: 2026-05-05T07:01:25.787549+00:00
source: "LWN.net"
tags: [blog, raw]
---

# A security bug in AEAD sockets

Source: https://lwn.net/Articles/1070454/

A security bug in AEAD sockets
[Posted April 30, 2026 by daroc]
Security analysis firm
Xint
has disclosed
a security bug
in the Linux kernel
that allows for arbitrary 4-byte writes to the page cache, and which has been
present since 2017.
The vulnerability has
been fixed
in mainline kernels. A
proof-of-concept script
demonstrates how to use the flaw to corrupt a setuid
binary, which works on
multiple distributions, by requesting an AEAD-encrypted socket from user space
and splicing a particular payload into it.
A
supplemental blog
post
gives more details about the discovery and remediation.
A core primitive underlying this bug is splice(): it transfers data between file
descriptors and pipes without copying, passing page cache pages by reference.
When a user splices a file into a pipe and then into an AF_ALG socket, the
socket's input scatterlist holds direct references to the kernel's cached pages
of that file. The pages are not duplicated; the scatterlist entries point at the
same physical pages that back every
read()
,
mmap()
, and
execve()
of that file.
