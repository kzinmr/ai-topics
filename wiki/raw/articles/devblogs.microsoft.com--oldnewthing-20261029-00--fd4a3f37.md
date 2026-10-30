---
title: "The support case of a customer who said that all they could see was a black screen"
url: "https://devblogs.microsoft.com/oldnewthing/20261029-00/?p=112808/"
fetched_at: 2026-10-30T10:00:48.267367+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The support case of a customer who said that all they could see was a black screen

Source: https://devblogs.microsoft.com/oldnewthing/20261029-00/?p=112808/

If you hold a PC’s power button for 12 seconds, it will turn off at the hardware level without notifying the operating system. This is a safety feature so that you can turn of the computer even if the operating system’s “Shut down” command isn’t working.
After eight seconds of the power button being held down, the Windows kernel realizes that the user is trying to do a force-power-off of the system, and it quickly takes a kernel dump that can be uploaded to the Windows Error Reporting service the next time you turn the system on. (Sometimes four seconds isn’t enough time to get enough information, and the kernel dump is incomplete. I believe that on Windows Insider builds of Windows, you get a message that says something like “Please let go of the power button so we can collect more information, and then we will turn off the computer.” This gives the kernel more time to finish capturing its kernel dump.)
These emergency kernel dumps are internally classified as “long power button hold” (LPBH) failures. One of the pieces of information recorded in these emergency kernel dumps is whether the screen consists entirely of black pixels. Those failures are sub-classified as “black screen LPBH”, and they go to a special virtual team for analysis. (I happen to be a member of this black screen LPBH team.)
Sometimes the problem is a broken video driver. Sometimes the video driver is doing just fine, but the desktop compositor is just handing black pixels to the video driver. Sometimes the desktop compositor is doing just fine, but nobody is drawing anything to the screen. And those cases are further subdivided further into cases like “there is nobody around to draw anything” or “the person who normally draws stuff is hung.”
Back in the Windows 3.1 days, there was a customer product support call that would today have been classified as a “black screen” bug: The customer reported that they turned on the computer, and Windows started up, but when the logo went away, all they saw was a blank screen.
After some questioning, the customer support engineer put the story together: It turned out that this customer really liked the color black, so they decided to set up a
goth
theme. They set the wallpaper color to black. They set the title bar color to black. They set the button color to black. They set the window background color to black. They set the window text color to black. Every possible color you could pick in the Colors control panel was set to black.
Once you get yourself into this situation, it’s hard to get out because you can’t see anything.
I don’t know how the customer support engineer fixed the problem, but I’m guessing that they booted into MS-DOS, ran
EDIT.COM
, and
deleted the
[colors]
section from the
win.ini
file
, thereby returning all the system colors to defaults.
