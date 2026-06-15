---
title: "The 7.1 kernel has been released"
url: "https://lwn.net/Articles/1077758/"
fetched_at: 2026-06-15T07:00:43.200078+00:00
source: "LWN.net"
tags: [blog, raw]
---

# The 7.1 kernel has been released

Source: https://lwn.net/Articles/1077758/

The 7.1 kernel has been released
[Posted June 14, 2026 by corbet]
Linus has
released the 7.1 kernel
.
"
So it's only Sunday morning back home, but it's Sunday afternoon where
I am right now, so I'm doing the 7.1 release at the regular time -
just not in the regular timezone.
"
Significant changes in 7.1 include
the removal of support for some old 486-based architectures,
some
new
clone()
flags
making
process management easier,
BPF support
for io_uring,
zero-copy-I/O support for the
ublk
user-space block
driver,
initial (incomplete)
sub-scheduler support
in sched_ext,
more
swapping improvements
,
a
completely rewritten NTFS
implementation
,
and much more.  See the LWN merge-window summaries (
part 1
,
part 2
) for details.
