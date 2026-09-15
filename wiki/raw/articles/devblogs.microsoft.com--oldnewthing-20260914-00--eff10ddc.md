---
title: "Why didn't Read­Directory­ChangesW provide a way to correlate the two sides of a rename operation?"
url: "https://devblogs.microsoft.com/oldnewthing/20260914-00/?p=112696"
fetched_at: 2026-09-15T10:01:19.888520+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why didn't Read­Directory­ChangesW provide a way to correlate the two sides of a rename operation?

Source: https://devblogs.microsoft.com/oldnewthing/20260914-00/?p=112696

Brian Dellisanti asked
why
Read­Directory­ChangesW
didn’t provide a way to correlate the two sides of a rename operation
.
I wasn’t there, but I can guess.
My guess is that the implementation always generated the two events one right after the other, so “obviously” the way you correlate them is to save the old name when you see the
FILE_
ACTION_
RENAMED_
OLD_
NAME
, and when the
FILE_
ACTION_
RENAMED_
NEW_
NAME
comes immediately after, you have your two sides.
But they never wrote down that the two events always occur in direct succession. Which meant that when new file systems came along, they might not honor the unwritten rule. If two files are being renamed at the same time, is it possible that the two sets of rename events end up interleaved? There was nothing written down to forbid it, so I guess it’s possible.
Note that I don’t know whether any file systems actually break this unwritten rule. From what I can tell, they do generate the two events in rapid succession, but rapid succession doesn’t
a priori
guarantee that they will come directly one after the other, particularly if there is a lot of concurrent disk activity going on.
In practice, I couldn’t find a lot of code tracking renames anyway. They generally treated the
FILE_
ACTION_
RENAMED_
OLD_
NAME
as a deletion and the
FILE_
ACTION_
RENAMED_
NEW_
NAME
as a creation. And the ones that did track renames assumed that renames did not interleave. (Not that they had much choice.)
I don’t think that providing the file IDs for the two sides of a rename operation was the purpose of
Read­Directory­Changes­ExW
‘s
Read­Directory­Notify­Extended­Information
. It was just a happy side effect that the extra information in the
Read­Directory­Notify­Extended­Information
also gives you the pieces needed to connect the dots reliably.
I thought you might appreciate me pointing out the trick, that’s all.
