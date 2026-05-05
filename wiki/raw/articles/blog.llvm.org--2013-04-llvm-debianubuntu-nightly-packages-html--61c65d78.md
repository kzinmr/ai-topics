---
title: "LLVM Debian/Ubuntu nightly packages"
url: "https://blog.llvm.org/2013/04/llvm-debianubuntu-nightly-packages.html"
fetched_at: 2026-05-05T07:01:43.428229+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Debian/Ubuntu nightly packages

Source: https://blog.llvm.org/2013/04/llvm-debianubuntu-nightly-packages.html

In order to facilitate testing and to improve the deployment of the LLVM toolchain, we are happy to
publish LLVM Debian/Ubuntu nightly packages
. Read on for information about how it works and what we're building.
These packages provide LLVM, Clang, compiler-rt, polly and LLDB.
They are built for Debian:
Wheezy (future stable)
Unstable
and Ubuntu:
For now, amd64 and i386 are supported.
For example, installing the nightly build of clang 3.3 is as simple as:
echo "deb http://llvm.org/apt/wheezy/ llvm-toolchain-wheezy main"> /etc/apt/sources.list.d/llvm.list
apt-get update
apt-get install clang-3.3
Packages are automatically built twice a day for every architecture and operating system in clean chroots. They are built by a
Jenkins instance
hosted by
IRILL
and push the LLVM infrastructure.
Repositories
Debian
wheezy (currently testing)
deb http://llvm.org/apt/wheezy/ llvm-toolchain-wheezy main
deb-src http://llvm.org/apt/wheezy/ llvm-toolchain-wheezy main
sid (unstable)
deb http://llvm.org/apt/unstable/ llvm-toolchain main
deb-src http://llvm.org/apt/unstable/ llvm-toolchain main
Ubuntu
Precise (12.04)
deb http://llvm.org/apt/precise/ llvm-toolchain-precise main
deb-src http://llvm.org/apt/precise/ llvm-toolchain-precise main
Quantal (12.10)
deb http://llvm.org/apt/quantal/ llvm-toolchain-quantal main
deb-src http://llvm.org/apt/quantal/ llvm-toolchain-quantal main
Raring (13.04)
deb http://llvm.org/apt/raring/ llvm-toolchain-raring main
deb-src http://llvm.org/apt/raring/ llvm-toolchain-raring main
Install
The following commands will install all packages provided by the llvm-toolchain:
apt-get install clang-3.3 clang-3.3-doc libclang-common-dev libclang-dev libclang1 libclang1-dbg libllvm-3.3-ocaml-dev libllvm3.3 libllvm3.3-dbg lldb-3.3 llvm-3.3 llvm-3.3-dev llvm-3.3-doc llvm-3.3-examples llvm-3.3-runtime
Technical workflow
Twice a day, each jenkins job will checkout the debian/ directory necessary to build the packages. The repository is available on the Debian hosting infrastructure:
http://anonscm.debian.org/viewvc/pkg-llvm/llvm-toolchain/branches/
. In the
llvm-toolchain-*-source
, the following tasks will be performed:
upstream sources will be checkout
tarballs will be created. They are named:
llvm-toolchain_X.Y~svn123456.orig-lldb.tar.bz2
llvm-toolchain_X.Y~svn123456.orig-compiler-rt.tar.bz2
llvm-toolchain_X.Y~svn123456.orig.tar.bz2
llvm-toolchain_X.Y~svn123456.orig-clang.tar.bz2
llvm-toolchain_X.Y~svn123456.orig-polly.tar.bz2
Debian .dsc package description is created
Start the jenkins job
llvm-toolchain-X-binary
Then, the job
llvm-toolchain-X-binary
will:
Create a chroot using cowbuilder or update it is already existing
Install libisl >=0.11 if necessary (for polly)
Build all the packages
Launch lintian, the Debian static analyzer
Publish the result on the LLVM repository
Note that a
few patches
are applied over the LLVM tarballs (and should be merged upstream soon).
Future
This versatile infrastructure allows some more interesting features like:
Automatic launch of scan-build on the whole code
Full bootstrap of LLVM/Clang
Code coverage on the latest release
