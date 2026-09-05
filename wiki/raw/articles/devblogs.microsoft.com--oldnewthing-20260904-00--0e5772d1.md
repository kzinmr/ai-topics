---
title: "What happens if you change a window class's GCL_CB­WND­EXTRA?"
url: "https://devblogs.microsoft.com/oldnewthing/20260904-00/?p=112675"
fetched_at: 2026-09-05T10:00:48.998696+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What happens if you change a window class's GCL_CB­WND­EXTRA?

Source: https://devblogs.microsoft.com/oldnewthing/20260904-00/?p=112675

After my historical look back on
the evolution of system-windows window and class extra bytes
, I noted that
there was one application that expected to be able to modify
GWW_
CB­CLS­EXTRA
.
It turns out that there are even more applications that expect to be able to modify
GWW_
CB­WND­EXTRA
. So many that it wasn’t worth creating an application compatibility exception for them.
So what happens when you modify
GWW_
CB­WND­EXTRA
, or its modern equivalent,
GWL_
CB­WND­EXTRA
?
The change in window extra bytes takes effect, but not retroactively.
Windows that are created after you change
CB­WND­EXTRA
receive the updated number of extra bytes, but windows that already exist are not modified. They still have the number of extra bytes that were assigned when the window was created.
Specifically to deal with people who change the number of window extra bytes on the fly, the system keeps track of what the number of extra bytes was
at the time the window was created
, and those are the bytes you get to access from that window. If you try to access the nonexistent bytes, you are told
ERROR_
INVALID_
INDEX
.
This does mean that you can get into a strange situation where
Get­Class­Long(hwnd,
GCL_
CB­WND­EXTRA)
tells you that you have 8 extra bytes, say, but if you use
Get­Window­Long(hWnd, 0)
, which asks for the
LONG
represented by bytes 0–3, you are told “Sorry, that’s out of range.” As far as you can tell, it is well within range. What you don’t know is that the window was created back when the
GCL_
CB­WND­EXTRA
was less than 4.
There is no way to ask a window, “How many extra bytes do you
really
have?” I mean, why the system go out its your way to improve the lives of people who are abusing it?
