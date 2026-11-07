---
title: "Why are we all worked up about atomicity when applying hot-patches if we can just suspend all the threads?"
url: "https://devblogs.microsoft.com/oldnewthing/20261106-00/?p=112838/"
fetched_at: 2026-11-07T10:01:30.007501+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why are we all worked up about atomicity when applying hot-patches if we can just suspend all the threads?

Source: https://devblogs.microsoft.com/oldnewthing/20261106-00/?p=112838/

I noted that one of the concerns of the Windows hot-patching system is that the patch can be activated atomically. But why does it need to be atomic? Can’t just suspend all the threads of the process (except for the one doing the patching)? That way, nobody else can be executing a half-installed patch.
For processors with variable-length instructions (
looking at you, x86
), the patched instruction cannot be shorter than its replacement. This applies even if you can suspend all the threads of the process, because you might suspend a thread just as it’s about to execute bytes from what would be the second of half of the replacement instruction.
instruction
pointer
↓
original
XX
YY
patch
AA BB
If you were unlucky and froze the thread after it executed the
XX
instruction and was about to execute the
YY
instruction, and then replaced both bytes with a two-byte instruction
AA BB
, then when the thread resumes, it will execute
BB
as if it were the start of a new instruction.
Okay fine, so
we’ll make sure that the original instruction is at least as big as the replacement instruction
, so that a frozen thread is never caught in the middle of the replacement instruction. But assuming we do that, can’t we just suspend all the threads, and then patch at will without having to worry about atomicity?
While it’s true that you suspended all the threads in the process, that doesn’t prevent new threads from being created in the process by a function like
Create­Remote­Thread
. The caller of
Create­Remote­Thread
can specify whether the new thread is suspended or not, and if it chooses non-suspended (or if it chose suspended and then decided to resume it), you now have a live thread running in the process while you are busy trying to patch it.
Atomicity is important so that you don’t accidentally patch code while an injected thread happens to be running it.
Bonus chatter
: Now, atomicity is still not bulletproof, because even if you manage to suspend all the threads, and prevent new ones from being injected, you still have the case where somebody calls
Write­Process­Memory
to modify the bytes of the process while everything in it is suspended.
And we saw earlier that
Write­Process­Memory
is not atomic
, so it’s possible that a two-byte
Write­Process­Memory
writes the first byte, and then you do your atomic update of both bytes, and then the
Write­Process­Memory
finishes by writing the second byte, leaving a mishmash of your patch and the rogue one.
On the other hand, anybody who was using
Write­Process­Memory
to do code patching was already broken because of this lack of atomicity, so we are not introducing a new problem.
Furthermore, since the hot-patching space is reserved for Windows Update, an outsider that uses
Write­Process­Memory
to apply a hot-patch from another process is already breaking the rules. At this point Windows Update says, “Look, I can’t protect myself from this, and you’re in double-unsupported territory by the time we got here, so whatever happens is your problem.”
