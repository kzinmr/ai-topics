---
title: "A sample use of the winstart.bat file in Windows 95"
url: "https://devblogs.microsoft.com/oldnewthing/20260908-00/?p=112679"
fetched_at: 2026-09-09T10:01:00.077373+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# A sample use of the winstart.bat file in Windows 95

Source: https://devblogs.microsoft.com/oldnewthing/20260908-00/?p=112679

In my earlier discussion of
the the litte-known
winstart.bat
batch file in Windows 3.1 and Windows 95
, Danielix Klimax wondered
whether it was useful in Windows 95, or whether it was primarily used only in Windows 3.x
.
I found a reference to
winstart.bat
in
the Windows 3.1
SETUP.TXT
file
:
Using the TIGA Display Driver
-------------------------------
If you are using the TIGA display driver, you must load the TIGACD.EXE
MS-DOS driver manually before running Setup to upgrade Windows.
Otherwise, Windows will not upgrade your system properly.

After successfully setting up Windows, you can increase the amount of
conventional memory available to non-Windows applications when Windows
is running in 386 enhanced mode by loading TIGACD.EXE from the
WINSTART.BAT file. The WINSTART.BAT file runs only in 386 enhanced
mode. If you want to run Windows in standard mode, you must load
TIGACD.EXE manually. For more information, see the README.WRI online
document.
TIGA is the
Texas Instruments Graphics Architecture
, a standard for high-resolution graphics modes on PCs. It held some sway for a while but ultimately fell to competing standards like VESA and SuperVGA.
The
TIGACD.EXE
program is the TIGA Communications Driver which seems to be the program which implements the TIGA APIs for a particular class of video cards. You need to run this TSR so that the Windows TIGA driver can use these TIGA APIs to run the video cards in resolutions higher than standard VGA, like (gasp) 800×600.
But on the other hand, it’s probably the case that only Windows needs to be able to use the video card at such high resolution. Your MS-DOS programs will just use the standard VGA resolution, if they use graphics mode at all!
In fact, MS-DOS programs
cannot
use the TIGA modes. The graphics card vendors wrote 16-bit Windows graphics drivers, which teach 16-bit Windows how to draw graphics with those modes. But they did not write 32-bit Windows virtual display drivers, which teach the 32-bit Windows virtual machine manager how to give each virtual machine their own virtual TIGA video card, each of which could be in a different TIGA mode. For example, this 32-bit driver has to save the video card state and memory when the user switches out of a full-screen MS-DOS program, and then restore it when the user switches back. In other words, they did not provide the necessary support for multitasking TIGA graphics among Windows and MS-DOS sessions. TIGA can be used in only one virtual machine, and the obvious choice is to let Windows use it.
This was the recommendation from Microsoft in Windows 3.1, and it appears that
the recommendation was extended by Siemens to cover Windows 95 as well
.
So at least one vendor continued to use it in Windows 95. I wouldn’t be surprised if there were others that also used it, but we simply don’t see them because they have such small audiences.
