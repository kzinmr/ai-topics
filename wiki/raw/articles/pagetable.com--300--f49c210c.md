---
title: "Apple Copland D11E4 Emulator in Your Browser"
url: "https://www.pagetable.com/300"
fetched_at: 2026-09-25T10:01:26.199735+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Apple Copland D11E4 Emulator in Your Browser

Source: https://www.pagetable.com/300

Apple’s ill-fated
Copland
operating system
1
is notoriously hard to run on real hardware, and has not previously been available in emulation. Here is the last build, D11E4 from June 1996, in an improved DingusPPC.
Click the screen to give the machine the keyboard and the mouse; Escape gives them back.
On real hardware, booting should take about 30s. A modern machine can match real-time in wasm.
If any code hits an assertion, it drops into the debugger: click “Continue” to make it go again.
Try running Copland HD→Applications→GXSlidemaster or Eric’s Solitaire.
The 11 patches necessary for unlocking Copland are on
this branch of my fork
. DingusPPC does not take patches written with the help of AI, so maybe someone wants to re-do these fixes based on the explanations in the commit messages. (The patches for this wasm version are on
this branch
.)
