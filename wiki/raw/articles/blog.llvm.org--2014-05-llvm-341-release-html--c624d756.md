---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2014/05/llvm-341-release.html"
fetched_at: 2026-05-05T07:01:42.298054+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2014/05/llvm-341-release.html

LLVM 3.4.1 Release
LLVM 3.4.1 has been released!  This is a bug-fix release that contains fixes for the AArch64, ARM, PowerPC, R600, and X86 targets as well as a number of other fixes in the core libraries.
The LLVM and Clang core libraries in this release are API and ABI compatible with LLVM 3.4, so projects that make use of the LLVM and Clang API and libraries will not need to make any changes in order to take advantage of the 3.4.1 release.
Bug-fix releases like this are very important for the project, because they help get critical fixes to users faster than the typical 6 month release cycle, and also make it easier for operating system distributors who in the past have had to track and apply bug fixes on their own.
A lot of work went into this release, and special thanks should be given to all the testers who helped to qualify the release:
Renato Golin
Sebastian Dreßler
Ben Pope
Arnaud Allard de Grandmaison
Erik Verbruggen
Hal Finkel
Nikola Smiljanic
Hans Wennborg
Sylvestre Ledru
David Fang
In addition there were a number community members who spent time tracking down bugs and helping to resolve merge conflicts in the 3.4 branch.  This is what made this release possible, so thanks to everyone
else who helped.
I would like to keep the trend of stable releases going to 3.5.x and beyond (Maybe even 3.4.2 if there is enough interest), but this can only be
done with the help of the community.  If you would like to help with the next stable release or even regular release, then the next time you see a proposed release schedule on the mailing list, let the release manager know you can help.  We can never have too many volunteers.
Thanks again to everyone who helped make this release possible.
-Tom
