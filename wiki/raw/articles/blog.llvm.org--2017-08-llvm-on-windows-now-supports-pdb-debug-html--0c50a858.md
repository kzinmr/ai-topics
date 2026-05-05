---
title: "LLVM on Windows now supports PDB Debug Info"
url: "https://blog.llvm.org/2017/08/llvm-on-windows-now-supports-pdb-debug.html"
fetched_at: 2026-05-05T07:01:38.504795+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM on Windows now supports PDB Debug Info

Source: https://blog.llvm.org/2017/08/llvm-on-windows-now-supports-pdb-debug.html

LLVM on Windows now supports PDB Debug Info
For several years, we’ve been hard at work on making clang a world class toolchain for developing software on Windows.  We’ve
written
about this
several
times in the past, and we’ve had full ABI compatibility (minus bugs) for some time. One area that been notoriously hard to achieve compatibility on has been debug information, but over the past 2 years we’ve made significant leaps.  If you just want the TL;DR, then here you go:
If you’re using clang on Windows, you can now get PDB debug information!
Background: CodeView vs. PDB
CodeView is a debug information format invented by Microsoft in the mid 1980s. For various reasons, other debuggers developed an independent format called DWARF, which eventually became standardized and is now widely supported by many compilers and programming languages.  CodeView, like DWARF, defines a set of records that describe mappings between source lines and code addresses, as well as types and symbols that your program uses.  The debugger then uses this information to let you set breakpoints by function name, display the value of a variable, etc.  But CodeView is only somewhat documented, with the
most recent official documentation
being at least 20 years old.  While some records still have the format documented above, others have evolved, and entirely new records have been introduced that are not documented anywhere.
It’s important to understand though that CodeView is just a collection of records.  What happens when the user says “
show me the value of Foo
”?  The debugger has to
find
the record that describes Foo.  And now things start getting complicated.  What optimizations are enabled?  What version of the compiler was used?  (These could be important if there are certain ABI incompatibilities between different versions of the compiler, or as a hint when trying to reconstruct a backtrace in heavily optimized code, or if the stack has been smashed).  There are a billion other symbols in the program, how can we find the one named Foo without doing an exhaustive O(n) search?  How can we support incremental linking so that it doesn’t take a long time to re-generate debug info when only a small amount of code has actually changed?  How can we save space by de-duplicating strings that are used repeatedly?  Enter PDB.
PDB (Program Database) is, as you might have guessed from the name, a database.  It
contains
CodeView but it also contains many other things that allow indexing of the CodeView records in various ways.  This allows for fast lookups of types and symbols by name or address, the philosophical equivalent of “tables” for individual input files, and various other things that are mostly invisible to you as a user but largely responsible for making the debugging experience on Windows so great.  But there’s a problem: While CodeView is at least kind-of documented, PDB is
completely undocumented
.  And it’s highly non-trivial.
We’re Stuck (Or Are We?)
Several years ago, we decided that the path forward was to abandon any hope of emitting CodeView and PDB, and instead focus on two things:
Make clang-cl emit DWARF debug information on Windows
Port LLDB to Windows and teach it about the Windows ABI, which would be significantly easier than teaching Visual Studio and/or WinDbg to be able to interpret DWARF (assuming this is even possible at all, given that everything would have to be done strictly through the Visual Studio / WinDbg extensibility model)
In fact, I even wrote another
blog post
about this very topic a little over 2 years ago.  So I got it to work, and I eventually got parts of LLDB working on Windows for simple debugging scenarios.
Unfortunately, it was beginning to become clear that we really needed PDB.  Our goal has always been to create as little friction as possible for developers who are embedded in the Windows ecosystem.  Tools like
Windows Performance Analyzer
and vTune are very powerful and standard tools in engineers’ existing repertoires.  Organizations already have infrastructure in place to archive PDB files, and collect & analyze crash dumps.  Debugging with PDB is extremely responsive given that the debugger does not have to index symbols upon startup, since the indices are built into the file format.  And last but not least, tools such as WinDbg are already great for post-mortem debugging, and frankly many (perhaps even most) Windows developers will only give up the Visual Studio debugger when it is pried from their cold dead hands.
I got some odd stares (to put it lightly) when I suggested that we just
ask
Microsoft if they would help us out.  But ultimately we did, and… they agreed!  This came in the form of some code uploaded to the
Microsoft Github
repo which we were on our own to figure out.  Although they were only able to upload a subset of their PDB code (meaning we had to do a lot of guessing and exploration, and the code didn’t compile either since half of it was missing), it filled in enough blanks that we were able to do the rest.
After about a year and a half of studying this code, hacking away, studying the code some more, hacking away some more, etc, I’m proud to say that lld (the LLVM linker) can finally emit working PDBs.  All the basics like setting breakpoints by line, or by name, or viewing variables, or searching for symbols or types, everything works (minus bugs, of course).
For those of you who are interested in digging into the internals of a PDB, we also have been developing a tool for expressly this purpose.  It’s called
llvm-pdbutil
and is the spiritual counterpart to Microsoft’s own
cvdump
utility.  It can dump the internals of a PDB, convert a PDB to yaml and vice versa, find differences between two PDBs, and much more.  Brief documentation for llvm-pdbutil is
here
, and a detailed description of the PDB file format internals are
here
, consisting of everything we’ve learned over the past 2 years (still a work in progress, as I have to divide my time between writing the documentation and actually making PDBs work).
Bring on the Bugs!
So this is where you come in.  We’ve tested simple debugging scenarios with our PDBs, but we still consider this alpha in terms of debug info quality.  We’d love for you to try it out and report issues on our
bug tracker
.  To get you started, download the
latest snapshot of clang for Windows
.  Here are two simple ways to test out this new functionality:
Have clang-cl invoke lld automatically
clang-cl -fuse-ld=lld -Z7 -MTd hello.cpp
Invoke clang-cl and lld separately.
clang-cl -c -Z7 -MTd -o hello.obj hello.cpp
lld-link -debug hello.obj
We look forward to the onslaught of bug reports!
We would like to extend a very sincere and deep thanks to Microsoft for their help in getting the code uploaded to the github repository, as we would never have gotten this far without it.
And to leave you with something to get you even more excited for the future, it's worth reiterating that all of this is done without a dependency on any windows specific api, dll, or library.  It's 100% portable.  Do I hear cross-compilation?
Zach Turner (on behalf of the the LLVM Windows Team)
