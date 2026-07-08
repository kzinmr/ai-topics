---
title: "How did Windows 95 decide that a setup program ran?"
url: "https://devblogs.microsoft.com/oldnewthing/20260707-00/?p=112508"
fetched_at: 2026-07-08T07:00:56.757290+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How did Windows 95 decide that a setup program ran?

Source: https://devblogs.microsoft.com/oldnewthing/20260707-00/?p=112508

A little while ago, I mentioned that
Windows 95 had some defenses against installers that overwrite a file with an older version
. These defenses kicked in whenever it detected that a setup program had finished. But
how does it know that a setup program was running
?
It guesses.
If the name of the program contains the word “setup”, “install”, or some other magic words, then it is considered to be a setup program. Here’s the list of magic words.
Magic word
Notes
setup
install
Redundant
inst
imposta
Italian?
ayarla
Turkish?
felrak
Hungarian?
The entry for
install
is redundant with
inst
, because anything that contains “install” will also contain “inst”. My guess is that “install” came first, and then later somebody found that a lot of setup programs were called “
blah
inst” for various values of “blah” so they added an entry for “inst”, but failed to remove the redundant entry for “install”.
If there are no matches on the program name, Windows 95 also checks whether the path to the executable contains the word “Setup”.
In the above two cases, the file check is delayed until the next start, because some setup programs will realize that the file is in use and cannot be replaced, so they use
Exit­Windows­Exec
to exit Windows back to MS-DOS, run a batch file, and then start Windows back up. We have to wait until the restart of Windows to catch any files that were improperly modified by the batch file.
As a special bonus, Windows 95 does a live file check after any multimedia driver installs via an INF file. I guess the multimedia team discovered that a lot of drivers overwrite system DLLs in their INF files, so they asked for a cleanup pass afterward.
