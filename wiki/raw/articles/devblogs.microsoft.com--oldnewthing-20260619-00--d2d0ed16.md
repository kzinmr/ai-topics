---
title: "What does it mean when the bottom bit of my HMODULE is set?"
url: "https://devblogs.microsoft.com/oldnewthing/20260619-00/?p=112447"
fetched_at: 2026-06-21T07:00:48.796283+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What does it mean when the bottom bit of my HMODULE is set?

Source: https://devblogs.microsoft.com/oldnewthing/20260619-00/?p=112447

The numeric value of an
HMODULE
is normally the base address of the DLL or EXE it represents. These base addresses are
always multiples of 64KB
, so the bottom 16 bits are all zero. Yet you may run across one with the bottom bit set. What does that mean?
Normally, when you load a DLL, it gets an entry in the table of loaded modules. This table is consulted by functions like
Get­Module­Handle
and
Enum­Process­Modules
to identify all the DLLs that have been loaded. It also is used to keep track of how many times each DLL has been loaded, so that the DLL is removed from memory when the correct number of
Free­Library
calls has been made.
Many of the flags to the
Load­Library­Ex
function alter how the system locates the DLL to load, but some of them alter how the DLL is itself loaded into memory. The interesting one here is the
LOAD_
LIBRARY_
AS_
DATAFILE
flag.
If you ask that a DLL be loaded as a data file, and there isn’t already a copy of the DLL loaded normally, then the loader will search the file system for the DLL in the manner described by the other flags, and then it will just map the DLL into memory without doing any of the usual stuff like applying fixups, and then returns you an
HMODULE
that represents the location where the DLL was mapped into memory, but it also sets the bottom bit as a note to itself to say “This wasn’t loaded the normal way.”
If the loader decides to map the DLL into memory directly, then the DLL does not get an entry in the list of loaded modules. While the module was loaded in a strict sense of the term, it was not loaded as a
functional
module. The code is not ready to execute: Its dependencies were not resolved. Its initialization was not run. It’s just a bunch of bytes mapped into memory. If you call
Get­Module­Handle
or
Enum­Process­Modules
, the module won’t show up because those functions use the list of “properly” loaded modules, and your datafile DLL wasn’t put on that list.
Functions like
Find­Resource
recognize these “not really a module” modules. For example, if you ask to find a resource in a loaded-as-datafile module, the
Find­Resource
function knows that it has to convert RVAs in the PE header into physical file offsets.
And when you pass the
HMODULE
back to
Free­Library
, it sees that the bottom bit is set and knows, “Oh, this was never entered into the module list, so I don’t have to remove it from the module list either.”
This special behavior of the bottom bit is locked into the ABI thanks to this macros provided in the
Load­Library­Ex
documentation:
#define LDR_IS_DATAFILE(handle)      (((ULONG_PTR)(handle)) & (ULONG_PTR)1)
I don’t know if this use of the bottom bit was intended to be an implementation detail, or whether documenting it was an intentional decision, but what’s done is done, and it’s documented, so it’s too late to change it now.
Bonus chatter
: You can see in the documentation another macro that reveals that the second-from-bottom bit is also used as a special signal:
#define LDR_IS_IMAGEMAPPING(handle)  (((ULONG_PTR)(handle)) & (ULONG_PTR)2)
