---
title: "The 7.3 kernel has been released"
url: "https://lwn.net/Articles/1101143/"
fetched_at: 2026-10-19T10:06:25.435730+00:00
source: "LWN.net"
tags: [blog, raw]
---

# The 7.3 kernel has been released

Source: https://lwn.net/Articles/1101143/

The 7.3 kernel has been released
[Posted October 18, 2026 by corbet]
Linus Torvalds has
released
the 7.3
kernel, as expected.
It's Sunday afternoon, and this week I somehow kept my wits
	together long enough to keep track of the day of the week, so the
	release isn't randomly delayed. Will wonders never cease?
Anyway, nothing very special seems to have happened this last week,
	so as expected the final 7.3 is out, and thus tomorrow the merge
	window for 7.4 opens. Except I'm on my annual family vacation, so
	instead of merging anything first thing in the morning, I'll spend
	most of the day on a boat and under water. I'll get back to merging
	in the afternoon, but I expect my schedule to be a bit unusual for
	a while.
This release is a record-breaker on all fronts; it brought in 18,765
non-merge commits from 3,021 developers, 807 of whom were first-time kernel
developers.
Significant changes in this release include some
significant binfmt_misc extensions
, some
group-scheduling work
aimed at improving performance on large systems, the new
failfs
filesystem that fails all operations, the
fchroot()
system call,
global per-CPU data for BPF programs, the
completion
of
the sched_ext subscheduler feature
,
working-set tracking
for virtual
machines,
alternative
data-stream support
in the ntfs3 filesystem,
a
long
list of SMB server improvements
,
and much more.  See the LWN merge-window summaries 
(
part 1
,
part 2
) and
the KernelNewbies 7.3 page
for details.
