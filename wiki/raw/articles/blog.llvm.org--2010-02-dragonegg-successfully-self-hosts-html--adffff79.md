---
title: "Dragonegg Successfully Self-Hosts!"
url: "https://blog.llvm.org/2010/02/dragonegg-successfully-self-hosts.html"
fetched_at: 2026-05-05T07:01:44.306764+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Dragonegg Successfully Self-Hosts!

Source: https://blog.llvm.org/2010/02/dragonegg-successfully-self-hosts.html

Dragonegg Successfully Self-Hosts!
By Duncan Sands
Feb 21, 2010
#dragonegg
One minute read
The
dragonegg GCC plugin
can host itself! Dragonegg lets you use the
LLVM
optimizers with
GCC-4.5
, much like
llvm-gcc
, but unlike llvm-gcc does not involve modifying GCC, thanks to the new GCC plugin infrastructure (currently one small patch is required). We built all of GCC-4.5, LLVM and dragonegg with dragonegg, then used the resulting binaries to build them all again. Why? Because we love to build! And because this was a great way of checking that nothing was miscompiled. The final dragonegg plugin was fully functional, successfully passing the entire dragonegg test suite.
