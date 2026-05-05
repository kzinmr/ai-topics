---
title: "Devirtualization in LLVM and Clang"
url: "https://blog.llvm.org/2017/03/devirtualization-in-llvm-and-clang.html"
fetched_at: 2026-05-05T07:01:38.369565+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Devirtualization in LLVM and Clang

Source: https://blog.llvm.org/2017/03/devirtualization-in-llvm-and-clang.html

define void @function(%struct.A* %a) {
%1 = load {...} %a, !invariant.group !0
%2 = load {...} %1, !invariant.load !1
call void %2(%struct.A* %a)
%3 = load {...} %a, !invariant.group !0
%4 = load {...} %4, !invariant.load !1
call void %4(%struct.A* %a)
ret void
}
!0 = !{!"_ZTS1A"} ; mangled type name of A
!1 = !{}
define void @function(%struct.A* %a) {
%1 = load {...} %a, !invariant.group !0
%2 = load {...} %1, !invariant.load !1
call void %2(%struct.A* %a)
call void %2(%struct.A* %a)
ret void
}
