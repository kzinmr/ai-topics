---
title: "Why is there no Windows hot-patching support for other architectures like 32-bit ARM and MIPS?"
url: "https://devblogs.microsoft.com/oldnewthing/20261002-00/?p=112753/"
fetched_at: 2026-10-04T10:01:14.815656+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why is there no Windows hot-patching support for other architectures like 32-bit ARM and MIPS?

Source: https://devblogs.microsoft.com/oldnewthing/20261002-00/?p=112753/

Windows hot-patching supports
x86-32
,
x86-64
,
64-bit ARM
, and
Itanium
, but why not the other architctures like 32-bit ARM, MIPS, Alpha AXP, PowerPC, and SH-3?
These architectures fall into two buckets.
MIPS, Alpha AXP, PowerPC, and SH-3 all predate hot-patching, so they naturally couldn’t conform to rules that didn’t exist yet.
Meanwhile, 32-bit ARM support was introduced¹ to Windows in the Windows 8 era, and at that time, hot-patching had already existed. But there were no provisions for hot-patching 32-bit ARM binaries because hot-patching is a Windows Server feature. Since there was no version of Windows Server for 32-bit ARM, there was no need to support hot-patching on 32-bit ARM binaries.
¹ More accurately,
re
-introduced, since Windows CE supported 32-bit ARM as well.
