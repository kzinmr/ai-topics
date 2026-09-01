---
title: "AWE does not require PAE, though PAE makes it much more useful"
url: "https://devblogs.microsoft.com/oldnewthing/20260831-00/?p=112660"
fetched_at: 2026-09-01T10:00:44.794199+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# AWE does not require PAE, though PAE makes it much more useful

Source: https://devblogs.microsoft.com/oldnewthing/20260831-00/?p=112660

The Address Windowing Extensions (AWE) is a feature of Windows that allows programs to allocate physical memory and map them on a page-by-page basis into a region of address space (the “address window”). PAE is the Physical Address Extension, which is a feature of the x86-32 CPU that allows a 32-bit processor to generate physical addresses larger than 32 bits, thereby allowing it to access more than 4GB of physical motherboard RAM.
Some time ago, I noted that
AWE does not require PAE
. The two features operate independently, but they are useful together.
If you use AWE without PAE, then your 32-bit Windows system can access only 4GB of onboard memory, so the feature of AWE that gives you access to lots of physical memory is of limited use: The system has only 4GB of memory to begin with, so that’s all that you can get. You wrote a lot of complex code for a high-RAM scenario when there isn’t really a lot of RAM available to take advantage of it.
It’s like getting a large teapot for making a single cup of tea: Your teapot has the capacity to hold a large amount of tea, but you’re going to put just one cup’s worth in it.
This is all largely historical information, since 64-bit processes running on 64-bit systems can allocate more than 4GB of memory and use it in the normal way. No special hoops necessary.
Note
: One thing that AWE does give you is the ability to allocate physical non-pageable memory. Again, you can use this feature whether or not you have also enabled PAE.
Note 1
: A 32-bit program that uses AWE will still run on a 64-bit system provided the 64-bit system uses the same page size as the 32-bit system. Looking at the
table of page sizes used by Windows
, it means that an x86-32 program (4KB page size) can run on an x86-64 system and an AArch64 system, but not an Itanium.
