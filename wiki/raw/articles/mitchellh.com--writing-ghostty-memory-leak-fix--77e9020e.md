---
title: "Finding and Fixing Ghostty's Largest Memory Leak"
url: "https://mitchellh.com/writing/ghostty-memory-leak-fix"
fetched_at: 2026-04-30T07:01:53.332193+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Finding and Fixing Ghostty's Largest Memory Leak

Source: https://mitchellh.com/writing/ghostty-memory-leak-fix

A few months ago, users started reporting that Ghostty was consuming absurd
amounts of memory, with one user reporting
37 GB
after 10 days of uptime.
Today, I'm happy to say
the fix has been found and merged
.
This post is an overview of what caused the leak, a look at some of
Ghostty's internals, and some brief descriptions of how we tracked it down.
1
The leak was present since at least Ghostty 1.0, but it is only recently
that popular CLI applications (particularly Claude Code) started producing
the correct conditions to trigger it at scale. The limited conditions that
triggered the leak are what made it particularly tricky to diagnose.
The fix is merged and is available in
tip/nightly releases
,
and will be part of the tagged 1.3 release in March.
The PageList
To understand the bug, we first need to understand how Ghostty manages
terminal memory. Ghostty uses a data structure called the
PageList
to store terminal content. PageList is a doubly-linked list of
memory pages that store the terminal content (characters, styles, hyperlinks,
etc.).
PageList: A doubly-linked list of memory pages
Page 1
oldest
scrollback
Page 2
Page 3
Page 4
newest
active screen
The underlying "pages" are not single
virtual memory pages
but they are a contiguous block of memory aligned to page boundaries
and composed of an even multiple of system pages.
2
These pages are allocated using
mmap
.
mmap
isn't particularly fast,
so to avoid constant syscalls, we use a
memory pool
. When we need
a new page, we pull from the pool. When we're done with a page, we return
it to the pool for reuse.
The pool uses a
standard size
for pages. Think of it like buying
standard-sized shipping boxes: most things people ship fit in a standard box,
and having a standard box comes with various efficiencies.
But sometimes terminals need more memory than a standard page provides.
If a set of lines has many emoji, styles, or hyperlinks, we need
a larger page. In these cases, we allocate a
non-standard page
directly with
mmap
, bypassing the pool entirely. This is typically a
rare scenario.
Two types of page allocations
Standard Pages (from pool)
• Fixed size
• Returned to pool when freed
• Reusable for future allocations
Non-Standard Pages (direct mmap)
• Variable size (larger than standard)
• Must call munmap to free
• Cannot be reused
When we "free" a page, we apply some simple logic:
If the page is
<= standard size
: return it to the pool
If the page is
> standard size
: call
munmap
to free it
This is the core background for terminal memory management in Ghostty,
and the idea itself is sound. A logic bug around an optimization is
what produced the leak, as we'll see next.
There's one more background detail we need to cover to
understand the bug: scrollback pruning.
Ghostty has a
scrollback-limit
configuration that caps how much history
is retained. When you hit this limit, we delete the oldest pages in
the scrollback buffer to free up memory.
But this often happens in a super hot path (e.g. when outputting large
amounts of data quickly), and allocating and freeing memory pages is
expensive, even with the pool. Therefore, we have an optimization:
reuse the oldest page as the newest page
when we reach the limit.
Scrollback pruning: reusing the oldest page
Before: at scrollback limit
Remove from front, reuse at back
After: page reused at end
Page 2
now oldest
Page 3
Page 4
This optimization works great. It requires zero allocations and uses
only some quick pointer manipulations to move the page from the
front to the back of the list. We do some metadata cleanup to "clear" the
page but otherwise leave the previous memory intact.
It's fast and empirically speeds up scrollback-heavy workloads significantly.
The Bug
During the scrollback pruning optimization, we always
resized our page back to standard size
. But we didn't resize the
underlying memory allocation itself, we only noted the resize in the
metadata. The underlying memory was still the large
non-standard
mmap
allocation, but now the PageList
thought
it was standard
sized.
How metadata desync causes the leak
1
Allocate non-standard page
2
Scrollback prunes & reuses
BUG:
metadata reset to std_size, but mmap unchanged!
3
Free the page
std_size, assume pooled.
munmap never called!
Standard
Non-standard
Leaked
Eventually, we'd free the page under various circumstances (e.g. when
the user closes the terminal, but also other times). At that point,
we'd see the page memory was within the standard size, assume it
was part of the pool, and we would
never call
munmap
on it.
A classic leak.
This all seems pretty obvious, but the issue is that non-standard
pages are rare by design. The goal of our design and optimizations is
that standard pages are the common case and provide a fast-path. Only
very specific scenarios produce non-standard pages and they're usually
not produced in large quantities.
But the rise of
Claude Code
changed this. For some reason, Claude Code's CLI produces a lot of
multi-codepoint grapheme outputs which force Ghostty to regularly
use non-standard pages. Additionally, Claude Code uses the primary screen
and produces a significant amount of scrollback output. These things
combined together created the perfect storm to trigger the leak
in huge quantities.
I want to be explicit that this bug is not Claude Code's fault. Claude Code is simply exercising
Ghostty in a way that exposes this long-standing bug.
The Fix
The fix is conceptually simple:
never reuse non-standard pages
.
If we encounter a non-standard page during scrollback pruning, we
destroy it properly (calling
munmap
) and allocate a fresh
standard-sized page from the pool.
The core of the fix is in the snippet below, but some extra
work was needed to fix up some other bits of accounting we have:
if
(first
.
data
.
memory
.
len
>
std_size) {
self
.
destroyNode
(first)
;
break
:
prune
;
}
We could've also reused the non-standard page and just retained the
large memory size, but until we have data that shows otherwise, we're
still operating under the assumption that standard pages are the common case
and it makes sense to reset back to a standard pooled page.
Other users have recommended more complex strategies (e.g. maintaining
some metrics on how often non-standard pages are used and adjusting
our assumptions accordingly), but more research is needed before
making those changes. This change is simple, fixes the bug, and aligns
with our current assumptions.
As part of the fix, I added support for virtual memory tags on macOS
provided by the Mach kernel. This lets us tag our PageList memory allocations
with a specific identifier that shows up in various tooling.
inline
fn
pageAllocator
() Allocator {
// In tests we use our testing allocator so we can detect leaks.
if
(builtin
.
is_test)
return
std
.
testing
.
allocator
;
// On non-macOS we use our standard Zig page allocator.
if
(
!
builtin
.
target
.
os
.
tag
.
isDarwin
())
return
std
.
heap
.
page_allocator
;
// On macOS we want to tag our memory so we can assign it to our
// core terminal usage.
const
mach
=
@import
(
"../os/mach.zig"
)
;
return
mach
.
taggedPageAllocator
(
.
application_specific_1)
;
}
Now when debugging memory on macOS, Ghostty's PageList memory shows up
with a specific tag instead of being lumped in with everything else.
This made it trivial to identify the leak, associate it with the PageList,
and also verify that the fix worked by observing the tagged memory
being properly freed.
Preventing Leaks in Ghostty
We do a lot of work in the Ghostty project to find and prevent memory leaks:
In debug builds and unit tests, we use leak-detecting Zig allocators.
The CI runs
valgrind
on our full unit test suite on every commit
to find more than just leaks, such as undefined memory usage.
We regularly run the macOS GUI via macOS Instruments to look for
leaks particularly in the Swift codebase.
We run every GTK-related PR using Valgrind (the full GUI) to look
for leaks in the GTK codepath that isn't unit tested.
This has worked really well to date, but unfortunately it didn't catch
this particular leak because it only triggers under very specific
conditions that our tests didn't reproduce. The merged PR includes a
test that does reproduce the leak to prevent regressions in the future.
Conclusion
This was the largest known memory leak in Ghostty to date, and the only
reported leak that has been confirmed by more than a single user.
We'll continue to monitor and address memory reports as they come in,
but remember that reproduction is the key to diagnosing and fixing memory leaks!
Big thanks to
@grishy
who finally
got me a reliable reproduction so I could analyze the issue myself. Their
own analysis reached the same conclusion as mine, and the reproduction
let me verify both our understandings independently.
Thanks also to everyone who reported this issue with detailed diagnostics.
The community's analysis, especially around the
footprint
output and
VM region counting, gave me important clues that pointed toward the PageList
as the culprit.
