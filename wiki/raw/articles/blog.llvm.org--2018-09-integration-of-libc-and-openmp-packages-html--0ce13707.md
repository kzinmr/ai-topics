---
title: "Integration of libc++ and OpenMP packages into llvm-toolchain"
url: "https://blog.llvm.org/2018/09/integration-of-libc-and-openmp-packages.html"
fetched_at: 2026-05-05T07:01:37.993506+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Integration of libc++ and OpenMP packages into llvm-toolchain

Source: https://blog.llvm.org/2018/09/integration-of-libc-and-openmp-packages.html

Integration of libc++ and OpenMP packages into llvm-toolchain
A bit more than a year ago, we gave an
update about recent changes in apt.llvm.org
. Since then, we noticed an important increase of the usage of the service. Just last month, we saw more than 16.5TB of data being transferred from our CDN.
Thanks to the Google Summer of Code 2018, and after number of requests, we decided to focus our energy to bring new great projects from the LLVM ecosystems into
apt.llvm.org
.
Starting from version 7, libc++, libc++abi and OpenMP packages are available into the llvm-toolchain packages. This means that, just like clang, lldb or lldb, libc++, libc++abi and OpenMP packages are also built, tested and shipped on
https://apt.llvm.org/
.
The integration focuses to preserve the current usage of these libraries. The newly merged packages have adopted the llvm-toolchain versioning:
libc++ packages
libc++abi packages
libc++abi1-7
libc++abi-7-dev
OpenMP packages
libomp5-7
libomp-7-dev
libomp-7-doc
This packages are built twice a day for trunk. For version 7, only when new changes happen in the SVN branches.
Integration of libc++* packages
Both libc++ and libc++abi packages are built at same time using the clang built during the process. The existing libc++ and libc++abi packages present in Debian and Ubuntu repositories will not be affected (they will be removed at some point). Newly integrated libcxx* packages are not co-installable with them.
Symlinks have been provided from the original locations to keep the library usage same.
Example:  /usr/lib/x86_64-linux-gnu/libc++.so.1.0 -> /usr/lib/llvm-7/lib/libc++.so.1.0
The usage of the libc++ remains super easy:
Usage:
$ clang++-7 -std=c++11 -stdlib=libc++ foo.cpp
$ ldd ./a.out|grep libc++
libc++.so.1 => /usr/lib/x86_64-linux-gnu/libc++.so.1 (0x00007f62a1a90000)
libc++abi.so.1 => /usr/lib/x86_64-linux-gnu/libc++abi.so.1 (0x00007f62a1a59000)
In order to test new developments in libc++, we are also building the experimental features.
For example, the following command will work out of the box:
$ clang++-7 -std=c++17 -stdlib=libc++ foo.cpp -lc++experimental -lc++fs
Integration of OpenMP packages
While
OpenMP packages
have been present in the Debian and Ubuntu archives for a
while, only a single version of the package was available.
For now, the newly integrated packages creates a symlink from /usr/lib/libomp.so.5 to
/usr/lib/llvm-7/lib/libomp.so.5 keeping the current usage same and making them non
co-installable.
It can be used with clang through -fopenmp flag:
$ clang -fopenmp foo.c
The dependency packages providing the default libc++* and OpenMP package are also
integrated in llvm-defaults. This means that the following command will install all these
new packages at the current version:
$ apt-get install libc++-dev libc++abi-dev libomp-dev
LLVM 7 => 8 transition
In parallel of the libc++ and OpenMP work,
https://apt.llvm.org/
has been updated to
reflect the branching of 7 from the trunk branches.
Therefore, we have currently on the platform:
Stable
6.0
Qualification
7
Development
8
Please note that, from version 7, the packages and libraries are called 7 (and not 7.0).
Cosmic support
In order to make sure that the LLVM toolchain does not have too many regressions with
this new version, we also support the next Ubuntu version, 18.10, aka Cosmic.
A Note on coinstallability
We tried to make them coinstallable, in the resulting packages we had no control over
the libraries used during the runtime. This could lead to many
unforeseen
issues.
Keeping these in mind we settled to keep them conflicting with other versions.
Future work
Code coverage build fails for newly integrated packages
Move to a 2 phases build to generate clang binary using clang
Reshabh Sharma & Sylvestre Ledru
