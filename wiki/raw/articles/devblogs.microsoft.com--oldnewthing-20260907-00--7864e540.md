---
title: "Why don't we allow stacks to be sparse, instead of forcing them to be contiguous?"
url: "https://devblogs.microsoft.com/oldnewthing/20260907-00/?p=112677"
fetched_at: 2026-09-09T10:01:00.101083+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why don't we allow stacks to be sparse, instead of forcing them to be contiguous?

Source: https://devblogs.microsoft.com/oldnewthing/20260907-00/?p=112677

When I discussed
why we don’t just make the entire stack out of guard pages
,
commenter BCS wondered
, “Why require that the stack use contiguously mapped pages? What would break if only touched pages got mapped in? That could actually be a good thing for example with a function that wanted to
alloca
512MB on the stack but only read/writes a few pages.”
So the question is asking why the stack must be contiguous. Why not let it be sparse and fault in only the pages that are touched?
The first issue is that the stack check code would have to include an explicit check against the stack limit, instead of just walking down the stack a page at a time. This explicit check is needed to avoid security vulnerabilities if somebody manages to
alloca
a buffer so large that it goes past the end of the stack reservation entirely. If you go a single page at a time, you will eventually hit the no-access page that marks the end of the stack. But if you can leap over multiple pages at a time without touching them, you might leap so far past the end of the stack that you land somewhere else and start corrupting that other memory because you’re using it as a stack. In linux circles, this vulnerability is nicknamed “
Stack Clash
“¹ and goes more formally by “
stack guard-page hopping
.”²
After fixing that issue, you have another problem: How would you report a failure to commit a page in the middle of the stack?
void dosomething()
{
    void* buffer = NULL;
    __try {
        buffer = alloca(65536);
    } __except (GetExceptionCode() == STATUS_STACK_OVERFLOW) {
        if (!_resetstkoflw()) __fastfail(FAST_FAIL_FATAL_APP_EXIT);
    }

    if (buffer != NULL) {
        ⟦ use the buffer ⟧
    }
}
If you allowed sparse stacks, then the memory for the
buffer
would not actually be committed until the code used it. But the point the code uses the buffer is
outside
the exception handler for the failed
alloca()
. The code assumes, not unreasonably, that if
alloca
succeeds, then the memory is indeed allocated.
I guess you could fix this by committing the memory without making it present. That would mean making a call to
Virtual­Alloc
to expand the stack rather than just accessing the memory. Not only would this make the stack expansion code more complicated, particularly since
you have to preserve all the registers that might possibly be used by any calling convention
, but you also have to make sure that the
Virtual­Alloc
function itself doesn’t allocate too much stack!
Now, you can still tweak the x86-32 stack prober to avoid
pete.d
‘s problem, where a large stack frame is made completely present, with the resulting page-ins creating noticeable performance issues. The x86-32 prober could short-circuit the stack probe (
like the MIPS and other processors listed in the table on this page
) so that the page-ins occur only when the stack is actually expanding.
¹ Bonus reading about Stack Clash:
² Some systems mitigate stack guard-page hopping by creating a really large no-access region beyond the end of the stack. However, this isn’t a fix; just a mitigation. It just makes people have to leap further to clear the no-access region. If you already have this vulnerability, it’s probably because an attacker can control the size of the allocation, in which case you didn’t really slow them down by much; they just have to put a bigger number in their attack payload.
Other systems address this more thoroughly by (surprise) probing each page of the stack in sequence.
Stack Clash continues to be a problem even though gcc had a solution in 2020.
Here’s CVE-2026-77658 from just a few days ago
.
