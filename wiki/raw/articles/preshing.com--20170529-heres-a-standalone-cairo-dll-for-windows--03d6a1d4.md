---
title: "Here's a Standalone Cairo DLL for Windows"
url: "https://preshing.com/20170529/heres-a-standalone-cairo-dll-for-windows"
fetched_at: 2026-05-05T07:01:03.523868+00:00
source: "Preshing"
tags: [blog, raw]
---

# Here's a Standalone Cairo DLL for Windows

Source: https://preshing.com/20170529/heres-a-standalone-cairo-dll-for-windows

Cairo
is an open source C library for drawing vector graphics. I used it to create many of the diagrams and graphs on this blog.
Cairo is great, but it’s always been difficult to find a precompiled Windows DLL that’s up-to-date and that doesn’t depend on a bunch of other DLLs. I was recently unable to find such a DLL, so I wrote a script to simplify the build process for one. The script is shared
on GitHub
:
If you just want a binary package, you can download one from the
Releases
page:
The binary package contains Cairo header files, import libraries and DLLs for both x86 and x64. The DLLs are statically linked with their own C runtime and have no external dependencies. Since Cairo’s API is pure C, these DLLs should work with any application built with any version of MSVC. I configured these DLLs to render text using
FreeType
because I find the quality of FreeType-rendered text better than Win32-rendered text, which Cairo normally uses by default. FreeType also supports more font formats and gives text a consistent appearance across different operating systems.
Sample Application Using CMake
Here’s a
small Cairo application
to test the DLLs. It uses
CMake
to support multiple platforms including Windows, MacOS and Linux.
Hope this helps somebody!
