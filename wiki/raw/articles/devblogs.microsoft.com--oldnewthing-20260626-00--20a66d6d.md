---
title: "The case of the DLL that was not present in memory despite not being formally unloaded, part 2"
url: "https://devblogs.microsoft.com/oldnewthing/20260626-00/?p=112472"
fetched_at: 2026-06-27T07:01:07.484851+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the DLL that was not present in memory despite not being formally unloaded, part 2

Source: https://devblogs.microsoft.com/oldnewthing/20260626-00/?p=112472

Last time,
we looked at crashes caused by a DLL being removed from memory behind everybody’s back
, causing crashes when somebody tried to call into that no-longer-there DLL that everybody thought was still there.
A colleague of mine who was looking at other crashes coming from this process found that most of those other crashes were also of the form “a data structure was corrupted because somebody wrote the single byte
01
into it.” That piece of information made everything fall into place for my side of the investigation.
We saw earlier that
the bottom bit of the
HMODULE
is set for datafile module handles
. Therefore, if one of these stray
01
bytes happens to overwrite the bottom byte of an existing
HMODULE
handle, that turns it into a (fake) datafile module handle. And then, during process destruction, a component dutifully cleans up the DLLs they loaded by freeing them (say because they were stored in an RAII type like
wil::
unique_
hmodule
), the code will pass this (fake) datafile module handle to
Free­Library
. The
Free­Library
function sees the bottom bit set and says, “Oh, this must be the handle to a module that was loaded via
LOAD_
LIBRARY_
AS_
DATAFILE
,” so it frees it as a datafile.
Freeing a datafile module means undoing the steps that were taken when the module was loaded as a datafile: Unmapping the DLL from memory. In particular, loading a module as a datafile does not add the DLL to the list of DLLs that were loaded as code; therefore, unloading a datafile module doesn’t remove it from that list. As far as the DLL list is concerned, the DLL is still in memory.
A one-bit error caused the code to lie and attempt to free a module handle that did not correspond to a
Load­Library
call, resulting in mass havoc.
The “DLL unmapped from memory” crash is just an alternate manifestation of the “somebody is writing
01
bytes to places they shouldn’t” bug. The original bug had a larger
bucket spray
than we initially thought.
The good news is that all of the crashes have funneled down to a single bug. The bad news is that you now have to debug this one memory corruption bug.
Unfortunately, at the time of this writing, the root memory corruption bug in the third party program has yet to be identified. We don’t know whether it’s coming from an operating system component or from the program itself. Though the fact that it appears to occur only in one process, where it sprays across multiple modules, suggests that it’s a problem with that program, or that there’s something peculiar about how this specific process uses the system.
If you look at the original stack trace, you can see that the problem is occurring at process termination. That’s probably why the problem has lurked for so long: Crashes at exit often go unnoticed because there is no end-user loss of functionality. The user was finished with the program anyway. Whether it exits cleanly or with a crash doesn’t affect the user much.
Sorry. Not all stories have a happy ending.
