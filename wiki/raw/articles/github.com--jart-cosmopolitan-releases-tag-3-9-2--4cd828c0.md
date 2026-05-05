---
title: "Cosmopolitan v3.9.2"
url: "https://github.com/jart/cosmopolitan/releases/tag/3.9.2"
fetched_at: 2026-05-05T07:01:27.848772+00:00
source: "Justine Tunney"
tags: [blog, raw]
---

# Cosmopolitan v3.9.2

Source: https://github.com/jart/cosmopolitan/releases/tag/3.9.2

Cosmopolitan's Windows support may finally be feature complete. It's now
possible to send signals between processes using kill() on Windows. Ten
new torture test programs have been written to tease out more fixes and
offer a high level of assurance that signal handling is correct. Some of
these tests are good enough to deadlock the signal handling of UNIX OSes
but not our signaling module for Windows. They also demonstrate that our
Windows signal handling actually outperforms many UNIX OSes at latency.
0d74673
Introduce interprocess signaling on Windows
f68fc1f
Put more thought into new signaling code
dd8c4db
Write more tests for signal handling
126a44d
Write more tests attempting to break windows
8527462
d50f4c0
Fix ECHILD with WNOHANG on Windows
Other improvements include:
e975245
Upgrade to superconfigure z0.0.56
1bfb348
Add weak self make_shared variant (
#1299
)
87a6669
Clean up and test the MSG_FOO constants
0e59afb
Fix conflicting RTTI related symbol
8313dca
Show file descriptors on crash on Windows
d730fc6
Make NESEMU1 demo more reliable
This release includes a new build of cosmos, which is our collection of
prebuilt open source software. Special care has been placed into making
sure programs like Emacs, vim, wget, curl, etc. all work well on Windows.
Instructions
are provided for its installation on UNIX and Windows systems.
It's available for download below, and mirrored to the following URLs:
Your cosmocc toolchain has
instructions here
, and is mirrored to the
following URLs:
