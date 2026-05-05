---
title: "A path forward for an LLVM toolchain on Windows"
url: "https://blog.llvm.org/2013/09/a-path-forward-for-llvm-toolchain-on.html"
fetched_at: 2026-05-05T07:01:42.940649+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# A path forward for an LLVM toolchain on Windows

Source: https://blog.llvm.org/2013/09/a-path-forward-for-llvm-toolchain-on.html

A path forward for an LLVM toolchain on Windows
By Chandler Carruth
Sep 5, 2013
#C++
,
#Clang
2 minute read
Over the past several months, contributors from Google and elsewhere in the community have begun actively working on bringing an LLVM toolchain to Windows in a way that would support and enhance a fully native development experience. This toolchain works with Visual Studio and the Windows development process that Windows developers are already using, making LLVM tools and technologies available to them. We want to cross the streams (in the Ghostbuster proton-pack sense) of the Visual Studio IDE and the LLVM-based C++ tools to enable developers to build C++ software better.
To that end, we’ve been driving many of the efforts around compatibility with Visual Studio and native Windows C++ code in Clang and LLD (the LLVM linker). Today, as announced at
my GoingNative 2013 talk
, we are able to build a trivial C++ application that in turn links against native C++ libraries and uses them in real, interesting ways. This is a huge milestone for the project, and something we’re really excited to be talking more about. Lots of folks in the LLVM project came together to get the open source project here. Thanks to every single one of you.
Going forward, we would really like to see an increased level of involvement from Windows developers. We’re launching an
alpha-build website
as part of llvm.org where you can get fresh builds of Clang, various Clang-based-tools, LLD, and the rest of the LLVM toolchain for Windows on a regular basis. These installable packages should make it dramatically easier to test and experiment with this new set of tools in your development environment. Please feel free to try it out,
file bugs
, and even
submit patches
to help move the toolchain forward on this new platform. Keep in mind, we are following the tried-and-true open source release mantra of releasing early and frequently. These are alpha-quality releases intended at developers interested in helping us track down and understand bugs.
There is still a lot of exciting work left to make LLVM and the C++ toolchain built on top of LLVM fully support the Windows platform. Come join the fun, because this is one place where patches are truly welcome.
-Chandler Carruth
