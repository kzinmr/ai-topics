---
title: "If somebody tries to hot-patch an already-hot-patched function, how do they avoid conflicts?"
url: "https://devblogs.microsoft.com/oldnewthing/20261005-00/?p=112755/"
fetched_at: 2026-10-06T10:01:34.832613+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# If somebody tries to hot-patch an already-hot-patched function, how do they avoid conflicts?

Source: https://devblogs.microsoft.com/oldnewthing/20261005-00/?p=112755/

For the past few days, I did a quick survey of hot-patching mechanisms. But the hot-patch design accommodates only one hot-patcher. If somebody goes to hot-patch a function and finds that it’s already been hot-patched, what happens?
If somebody goes to hot-patch a function and finds that it’s already been hot-patched, then something has gone wrong.
The intended audience of hot-patching is Windows Update on systems that support hot-patching (as of this writing,
Windows Server
and more recently
Windows 11 Enterprise
, as far as I can tell). The idea is that when a Windows Update arrives, and the administrator has opted into hot-patching, and a file in the update is marked as “safe for hot-patching”,¹ then Windows Update will use the space reserved for hot-patching to replace the affected functions on the fly.
Since the only code authorized to use the hot-patch space is Windows Update, the system doesn’t have to deal with the case that the function has already been hot-patched by somebody else. There is no other code authorized to be somebody else!
But what if the function has been detoured or otherwise patched by somebody not authorized to do so?
My reading of the hot-patching code suggests that if the hot-patch code detects rogue patching, it declares the file to be not hot-patchable, and the system will have to reboot. (This tends to make customers unhappy.)
There is a race condition: The prescan may show that all the functions are safe to patch, but then somebody might patch a function
after
the prescan completes. In that case, the patcher will get halfway through and then discover the rogue-patched function, and now it’s kind of stuck. It can’t continue forward, and it can’t reliably roll back (because the rollback is probably also going to fail because the patch got overpatched). You’re stuck with a binary in memory that is half-patched, and who knows what’ll happen now.
An application that uses the hot-patching space is parking in a fire zone. Everything seems to be fine until the fire truck shows up, and then somebody’s house burns to the ground because the fire truck can’t get there.
Related reading
:
Application compatibility layers are there for the customer, not for the program
.
¹ Not all changes are safe for hot-patching, For example, if it changes a data structure’s layout or invariants, it isn’t hot-patchable because any instances of the data structure that were created before the hot-patch will not be in a legal state after the hot-patch.
