---
title: "No, really, you need to pass all unhandled messages to DefWindowProc, part 2"
url: "https://devblogs.microsoft.com/oldnewthing/20260924-00/?p=112728/"
fetched_at: 2026-09-25T10:01:25.899981+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# No, really, you need to pass all unhandled messages to DefWindowProc, part 2

Source: https://devblogs.microsoft.com/oldnewthing/20260924-00/?p=112728/

A customer reported a memory leak in Windows that occurred when they called
Register­Drag­Drop
followed by
Revoke­Drag­Drop
. They included a time travel trace of a sample program that demonstrated the problem. (Though for some reason, they didn’t include the program itself; just the time travel trace.)
Now, it is strange that there would be a memory leak if you call
Register­Drag­Drop
followed by
Revoke­Drag­Drop
, seeing as this pattern is used heavily by thousands of applications, including many parts of Windows itself, so if there were a memory leak inherent in the pattern, you’d think it’d have been reported by now.
I suspected that there was something special about their sample program.
Some time ago, I noted that
No, really, you need to pass all unhandled messages to DefWindowProc
. And that was the source of the problem.
Debugging through the time travel trace showed that yes, they did call
Register­Drag­Drop
, and then they did call
Revoke­Drag­Drop
. But there’s more going on. When the window receives a
WM_DESTROY
message, it cleans up all its state. And for any messages that arrive after
WM_DESTROY
, the window procedure goes looking for its special state and doesn’t see it, so it gives up and just returns 0 without passing the message to
Def­Window­Proc
.
Oops.
If the window procedure can’t figure out what to do, it should pass all messages to
Def­Window­Proc
. In this case, it’s important because some of those messages are cleanup messages, and one of the things those cleanup messages do is free the last few fragments of memory still hanging around.
Bonus chatter
: But if I register a drop target, and then revoke it, shouldn’t the revoke free all the memory that was allocated by the register call?
There’s no requirement that registering something and then unregistering it will immediately free all the memory associated with the registration. The system is allowed to cache stuff that it thinks will be needed again.
In this case, what happened is that the
Register­Drag­Drop
function uses an infrastructure that is shared by many components. That infrastructure is created and attached to the window the first time anybody needs it, and it is cleaned up when the window is destroyed. The memory isn’t leaked. It’s just cached on the window, waiting to be used by another operation. And the cache is destroyed when the window is destroyed.
But it assumes that you give
Def­Window­Proc
a chance to do that cleanup.
