---
title: "Speculating on how the buggy control panel extension truncated a value that it had right in front of it"
url: "https://devblogs.microsoft.com/oldnewthing/20260716-00/?p=112539"
fetched_at: 2026-07-17T07:00:58.741521+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Speculating on how the buggy control panel extension truncated a value that it had right in front of it

Source: https://devblogs.microsoft.com/oldnewthing/20260716-00/?p=112539

Last time,
we found that a crash in a control panel extension was caused by pointer truncation
. The code had a perfectly good 64-bit pointer in its hand, but somehow lost its mind and opted to throw away the top 32 bits.
How could something like this happen?
My guess is that this code started out as perfectly good 32-bit code:
HWND hwndButton = GetDlgItem(hdlg, ID_BUTTON);
SetWindowLong(hwndButton, GWL_WNDPROC, (LONG)g_originalWndProc);
And then they recompiled it as 64-bit code and got an error.
error C2065: 'GWL_WNDPROC': undeclared identifier
They then went back to the documentation and saw that for 64-bit Windows,
GWL_
WNDPROC
was renamed to
GWLP_
WNDPROC
.
So they fixed it by changing
GWL_
WNDPROC
to
GWLP_
WNDPROC
.
HWND hwndButton = GetDlgItem(hdlg, ID_BUTTON);
SetWindowLong(hwndButton,
GWL_WNDPROC
, (LONG)g_originalWndProc);
However, the point of renaming the value was not to annoy you. The point of renaming the value was to call your attention to places where pointer truncation is likely to occur. In this case, it’s the final parameter, the original 64-bit window procedure. The build break is telling you that you are probably passing a 32-bit value as something that should be 64-bit. In this case, because it was being cast to
(LONG)
. You are expected to upgrade the
GWL_
WNDPROC
to
GWLP_
WNDPROC
and at the same time upgrade the cast from
(LONG)
to
(LONG_PTR)
.
HWND hwndButton = GetDlgItem(hdlg, ID_BUTTON);
SetWindowLong(hwndButton,
GWL_WNDPROC
, (
LONG_PTR
)g_originalWndProc);
Now, this was likely an oversight rather than a systemic failure, because they did manage to subclass the window properly:
WNDPROC g_originalWndProc;

HWND hwndButton = GetDlgItem(hdlg, ID_BUTTON);
g_originalWndProc = (WNDPROC)SetWindowLong(hwndButton,
GWLP_WNDPROC
,
    (
LONG_PTR
)subclassWndProc);
They merely missed a spot. Perhaps the developer got distracted after fixing the symbol name and forgot to come back and fix the pointer.
Next time, we’ll look at why this bug has remained unfixed for so long.
