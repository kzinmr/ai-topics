---
title: "The 7.2 kernel has been released"
url: "https://lwn.net/Articles/1088991/"
fetched_at: 2026-08-17T10:30:55.209485+00:00
source: "LWN.net"
tags: [blog, raw]
---

# The 7.2 kernel has been released

Source: https://lwn.net/Articles/1088991/

The 7.2 kernel has been released
[Posted August 16, 2026 by corbet]
The
7.2 kernel
has been released.
Linus said:
Well, this last week of the release was - once again - bigger than
	I would have wished for, but hey, with the whole "new normal"
	thing, if I delayed releases for that reason we'd probably never
	have a release at all.
Significant features in this release include
common
attributes support
in the
bpf()
system call,
cache-aware load balancing
for the CPU
scheduler,
large-folio support in the Btrfs filesystem,
further
swap subsystem improvements
,
improvements to the Landlock security module,
support for block devices with inline encryption hardware via the
dm-inlinecrypt
device-mapper target, and much more.
See the LWN merge window summaries
(
part 1
,
part 2
) and
the KernelNewbies 7.2 page
for more information.
