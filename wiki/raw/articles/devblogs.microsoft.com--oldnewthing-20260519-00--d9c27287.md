---
title: "What is the history of the ERROR_ARENA_TRASHED error code?"
url: "https://devblogs.microsoft.com/oldnewthing/20260519-00/?p=112339"
fetched_at: 2026-05-20T07:00:50.071707+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What is the history of the ERROR_ARENA_TRASHED error code?

Source: https://devblogs.microsoft.com/oldnewthing/20260519-00/?p=112339

Error code 7 is
ERROR_
ARENA_
TRASHED
. What does this mean? It sounds like a heavy metal band ran amok and made a mess of the performance area that they rented.
This error message was inherited from MS-DOS. MS-DOS internally kept track of memory in the form of a sequence of variable-sized memory blocks, each prefixed by a 16-byte block known as an
arena
:
arena   STRUC
arena_signature     DB  ?               ; 4D for valid item, 5A for last item
arena_owner         DW  ?               ; owner of arena item
arena_size          DW  ?               ; size in paragraphs of item
arena   ENDS
The
arena_owner
is the PDB of the process that allocated the memory, or zero if the memory is free. Each arena signature is
0x4D
(ASCII capital M), except for the final one which is
0x5A
(ASCII capital Z). Yes, those are the initials of Mark Zbikowski.
When walking through the memory blocks, say, when searching for memory to satisfy an allocation request, if MS-DOS saw that the signature was neither
0x4D
nor
0x5A
, then it declared that the arenas were “trashed” (corrupted)¹ and
returned
ERROR_
ARENA_
TRASHED
.
This is an MS-DOS specific error code. It is not used by Win32.²
Since it is a vestigial error code (like
EMPTY_
THREAD_
REAPER_
LIST
), it is a handy error code to use when mocking error conditions, because you can be fairly confident that if you see error 7, it came from your test harness and not from a genuine system error.
The fact that the error message is not used casts suspicions on the many web sites that claim to be able to help you “fix” the problem. If you read their explanation of “what this error means”, it’s just a bunch of vague text about how, y’know, sometimes computers aren’t doing all that great and they encounter errors, or maybe there is a hardware conflict, or a corrupted system file. But somehow, despite having no idea what the error means, they still are quite confident in the steps you should take to fix it. (Usually performing a system scan, a system file check, and checking for driver updates.)
¹ The use of the slang term “trashed” is further evidence that Microsoft developers were
just a bunch of undisciplined hackers
.
² Well, at least, it is not used by the Win32 kernel. I do see that there are a few user-mode components which use it to indicate that internal data structures have been corrupted, which is at least in the same spirit as the original meaning of the error.
