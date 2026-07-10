---
title: "I've decoded a #pragma detect_mismatch error and fixed the mismatch, but I still get the error"
url: "https://devblogs.microsoft.com/oldnewthing/20260709-00/?p=112512"
fetched_at: 2026-07-10T07:01:41.722757+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# I've decoded a #pragma detect_mismatch error and fixed the mismatch, but I still get the error

Source: https://devblogs.microsoft.com/oldnewthing/20260709-00/?p=112512

Some time ago, I showed
how to decode a
#pragma detect_mismatch
error
. A colleague ran into this error because they sync’d a change that modified the configuration of a common header file. “No problem, I’ll just rebuild after sync’ing.” But when they rebuilt their project, the error persisted. What went wrong?
The error message tells you the two pieces that are conflicting. In my colleague’s case, one of the pieces was an object file inside a library, and the other piece was an object file in their project. The catch was that the library was not part of their project. Therefore, rebuilding their project doesn’t rebuild the library.
After you fix a
#pragma detect_mismatch
mismatch, you need to recompile all of the object files that were dependent upon the header file that contained the mismatch. This rule isn’t special to
#pragma detect_mismatch
; it applies to any ODR error. If a structure changed definitions in a common header file, you need to recompile all of the object files that were dependent on the header file so they all agree on the new structure definition.
The fix was to rebuild the library that had been compiled against the old version of the header file. Safer would be to do a clean rebuild of the entire repo, to make sure no stale contents from the old header file still linger.
