---
title: "The evolution of window and class extra bytes in Windows"
url: "https://devblogs.microsoft.com/oldnewthing/20260629-00/?p=112484"
fetched_at: 2026-06-30T07:01:00.869437+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The evolution of window and class extra bytes in Windows

Source: https://devblogs.microsoft.com/oldnewthing/20260629-00/?p=112484

Windows provides a family of functions for accessing so-called “extra bytes”. There are two categories of extra bytes: Class extra bytes (which belong to the window class) and window extra bytes (which belong to each window created from that class). Applications can request extra bytes at class registration, and those are accessed at increasing offsets starting at zero. The system also defines a number of extra bytes, and those use negative offsets.
We’re going to look at the system-defined offsets.
In 16-bit Windows, these were the available extra bytes and the function you used to read them:
Name
Size
Accessor
Notes
GCW_MENUNAME
int16_t
GetClassWord
GCW_HBRBACKGROUND
int16_t
GetClassWord
GCW_HCURSOR
int16_t
GetClassWord
GCW_HICON
int16_t
GetClassWord
GCW_HMODULE
int16_t
GetClassWord
GCW_CBWNDEXTRA
int16_t
GetClassWord
GCW_CBCLSEXTRA
int16_t
GetClassWord
GCL_WNDPROC
int32_t
GetClassLong
GCW_STYLE
int16_t
GetClassWord
GCW_ATOM
int16_t
GetClassWord
Added in Windows 3.1
GWL_WNDPROC
int32_t
GetWindowLong
GWW_HINSTANCE
int16_t
GetWindowWord
GWW_HWNDPARENT
int16_t
GetWindowWord
GWW_ID
int16_t
GetWindowWord
GWL_STYLE
int32_t
GetWindowLong
GWL_EXSTYLE
int32_t
GetWindowLong
Added in Windows 3.0
DWL_MSGRESULT
int32_t
GetWindowLong
For dialog windows
DWL_DLGPROC
int32_t
GetWindowLong
For dialog windows
DWL_USER
int32_t
GetWindowLong
For dialog windows
There is clearly a naming pattern here for class and window bytes.
The first letter
G
stands for
Get
. The second letter
C
or
W
stands for
Class
or
Window
. And the third letter
W
or
L
stands for
Word
or
Long
.¹
For window bytes that apply only to dialog windows, the first letter changes to
D
for “dialog”. These values are zero or positive, since they are really just extra bytes registered to the standard dialog class.
Now, in 16-bit Windows, handles were 16-bit values, but in 32-bit Windows, they expand to 32-bit values, so 32-bit Windows changed the functions from
Get­Something­
Word
to
Get­Something­
Long
, and the prefixes correspondingly changed from
W
to from
L
. So our table now looks like this:
Name
16-bit prefix/size
32-bit prefix/size
MENUNAME
GCW_
int16_t
GCL_
int32_t ◱
HBRBACKGROUND
GCW_
int16_t
GCL_
int32_t ◱
HCURSOR
GCW_
int16_t
GCL_
int32_t ◱
HICON
GCW_
int16_t
GCL_
int32_t ◱
HMODULE
GCW_
int16_t
GCL_
int32_t ◱
CBWNDEXTRA
GCW_
int16_t
GCL_
int32_t ◱
CBCLSEXTRA
GCW_
int16_t
GCL_
int32_t ◱
WNDPROC
GCL_
int32_t
GCL_
int32_t ◱
STYLE
GCW_
int16_t
GCL_
int32_t ◱
ATOM
GCW_
int16_t
GCW_
int16_t
HICONSM
GCL_
int32_t 💥
WNDPROC
GWL_
int32_t
GWL_
int32_t ◱
HWNDPARENT
GWW_
int16_t
GWL_
int32_t ◱
ID
GWW_
int16_t
GWL_
int32_t ◱
STYLE
GWL_
int32_t
GWL_
int32_t
EXSTYLE
GWL_
int32_t
GWL_
int32_t
USERDATA
GWL_
int32_t 💥
MSGRESULT
DWL_
int32_t
DWL_
int32_t
DLGPROC
DWL_
int32_t
DWL_
int32_t
USER
DWL_
int32_t
DWL_
int32_t
The ◱ symbol represents a value that got bigger, and the 💥 symbol represents values that did not exist in 16-bit Windows.
Even though control IDs are typically small integers, the space for them was expanded from a 16-bit value to a 32-bit value because
some people were using it to hold pointers or handles
. (One way to create a process-wide unique number is to
allocate memory and use its address
.)
The next step in the evolution of extra bytes is the conversion from 32-bit to 64-bit Windows. Pointers and handles expand to 64-bit values on 64-bit Windows, so all of the extra bytes that are used to (or could be used to) hold a handle or pointer were expanded to a 64-bit version.
To make it possible to write code that targets both 32-bit and 64-bit Windows, the design of 64-bit Windows didn’t make the hard break that 32-bit Windows did from 16-bit Windows. Instead, they introduced new functions that accept pointer-sized integers, which are 32-bit values on 32-bit Windows and 64-bit values on 64-bit Windows. That way, you just use those new functions everywhere, and they will expand on 64-bit systems and remain the same on 32-bit systems.
The new functions have names like
Get­Window­Long­
Ptr
, and the corresponding prefixes were changed to
GWLP_
and so on.
Name
16-bit prefix/size
32-bit prefix/size
32/64-bit prefix/size
MENUNAME
GCW_
int16_t
GCL_
int32_t ◱
GCLP_
intptr_t ◱
HBRBACKGROUND
GCW_
int16_t
GCL_
int32_t ◱
GCLP_
intptr_t ◱
HCURSOR
GCW_
int16_t
GCL_
int32_t ◱
GCLP_
intptr_t ◱
HICON
GCW_
int16_t
GCL_
int32_t ◱
GCLP_
intptr_t ◱
HMODULE
GCW_
int16_t
GCL_
int32_t ◱
GCLP_
intptr_t ◱
CBWNDEXTRA
GCW_
int16_t
GCL_
int32_t ◱
GCL_
int32_t
CBCLSEXTRA
GCW_
int16_t
GCL_
int32_t ◱
GCL_
int32_t
WNDPROC
GCL_
int32_t
GCL_
int32_t ◱
GCLP_
intptr_t ◱
STYLE
GCW_
int16_t
GCL_
int32_t ◱
GCL_
int32_t
ATOM
GCW_
int16_t
GCW_
int16_t
GCW_
int16_t
HICONSM
GCL_
int32_t 💥
GCLP_
intptr_t ◱
WNDPROC
GWL_
int32_t
GWL_
int32_t ◱
GWLP_
intptr_t ◱
HWNDPARENT
GWW_
int16_t
GWL_
int32_t ◱
GWLP_
intptr_t ◱
ID
GWW_
int16_t
GWL_
int32_t ◱
GWLP_
intptr_t ◱
STYLE
GWL_
int32_t
GWL_
int32_t
GWL_
int32_t
EXSTYLE
GWL_
int32_t
GWL_
int32_t
GWL_
int32_t
USERDATA
GWL_
int32_t 💥
GWLP_
intptr_t ◱
MSGRESULT
DWL_
int32_t
DWL_
int32_t
DWLP_
intptr_t ◱
DLGPROC
DWL_
int32_t
DWL_
int32_t
DWLP_
intptr_t ◱
USER
DWL_
int32_t
DWL_
int32_t
DWLP_
intptr_t ◱
From the prefix on the name of the extra bytes, you can read off which function it is meant to be used with.
Prefix
Function
GCW_
↔
G
et
C
lass
W
ord
GWW_
↔
G
et
W
indow
W
ord
GCL_
↔
G
et
C
lass
L
ong
GWL_
↔
G
et
W
indow
L
ong
GCLP_
↔
G
et
C
lass
L
ong
P
tr
GWLP_
↔
G
et
W
indow
L
ong
P
tr
The weirdo is
DWLP_
because it needs to encode both the type of window that it can be used with (D = dialog) as well as the function name it goes with (
W
indow
L
ong
P
tr
).
As a concession, Windows lets you pass
GCL_
and
GWL_
values to
Get­Class­Long­Ptr
and
Get­Window­Long­Ptr
(respectively) even though they are intended to be used with
Get­Class­Long
and
Get­Window­Long
(respectively). If you do that, you get the corresponding 32-bit value zero-extended if necessary to be the size of a pointer.² This is seen primarily in the case of
GWL_ID
because most people don’t use the full range of IDs, so if you’re willing to live within the 32-bit subset, you can just pretend that the values are not pointer-sized.³
“Why bother changing all the prefixes? Doesn’t that just create a lot of busy work for people porting from 32-bit code to 64-bit code?”
Yes, but it’s good busy work. The point is to force build breaks at places where you need to make fixes, because you have to call the function that accesses a pointer-sized integer rather than a 32-bit integer; otherwise you suffer from integer truncation bugs.
¹ This is a common prefixing convention for classic Win32. For example, the operation parameter to
Show­Window
is prefixed
SW_
; the flags to
Set­Window­Pos
are prefixed
SWP_
; and the relationship parameter for
Get­Window
is prefixed
GW_
.
² The use of the
GWL_
values with
Set­Window­Long­Ptr
is a bit more problematic. It looks like you’re storing a pointer-sized integer, but only the bottom 32 bits are honored.
³ The
ID
is unusual in that it is defined both as
GWL_ID
and
GWLP_ID
. All of the other values are defined with only one prefix.
