---
title: "Common Package Specification"
url: "https://nesbitt.io/2026/04/13/common-package-specification.html"
fetched_at: 2026-05-01T07:02:04.422458+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Common Package Specification

Source: https://nesbitt.io/2026/04/13/common-package-specification.html

The
Common Package Specification
went stable in CMake 4.3 last year and the name caught my attention because it sounds like it might be addressing the cross-ecosystem dependency problem I’ve
written about before
. Reading the spec, the “common” turns out to mean common across build systems rather than common across language ecosystems: it’s a JSON format that CMake and Meson and autotools can all read to find out where an installed library lives and how to link against it, replacing the mix of
.pc
files and
*Config.cmake
scripts that currently fill that role.
The schema is full of include paths, preprocessor defines, link flags, component types like
dylib
and
archive
and
interface
for header-only libraries, and feature strings like
c++11
and
gnu
, which makes sense given it came out of Kitware and the C++ tooling study group and is being driven by people building large C++ applications who are tired of every build system having its own incompatible way of describing the same installed library.
Conan can already
generate CPS files
for everything in ConanCenter, and CMake’s
find_package()
reads them with fallback to the older formats, so libraries built through that toolchain will start leaving
.cps
files in install prefixes whether anyone outside the C++ world notices or not. Each one is a small structured record of an installed binary: its location on disk, its version, what other components it requires, what platform it was built for.
For something like the
binary dependency tracing
Vlad and I have been looking at, that’s a useful data source sitting alongside the symbol tables we’d be extracting anyway, particularly for the version field, which is the thing you can’t reliably recover from
nm
output and currently have to guess from filenames or distro package databases.
The closer fit is native extension builds in language package managers. Ruby’s mkmf has
pkg_config()
baked into it
and the
pkg-config gem
reimplementing the format in pure Ruby has tens of millions of downloads, while node-gyp users shell out to
pkg-config
from
binding.gyp
action blocks to find headers and libraries at install time. These are doing exactly what CPS is designed to replace, and a CPS reader for mkmf would be a small piece of code, but the libraries that gems actually build against (libxml2, libpq, libsqlite3, openssl) ship
.pc
files because pkg-config has been around since 2000 and don’t yet ship
.cps
files because almost nothing outside CMake produces them.
There’s an
open proposal
to add a
package_url
field using purl identifiers so a CPS file could record which conan or vcpkg or distro package it came from, which would close a loop between the build-system world’s description format and the identifier scheme everything else has converged on.
Python has been moving on the adjacent problems independently, with
PEP 770
reserving
.dist-info/sboms/
inside wheels for CycloneDX or SPDX documents describing bundled libraries, and auditwheel
already implementing it
by querying
dpkg
or
rpm
or
apk
at repair time to find which system package each grafted
.so
came from before writing the result as purls. CPS wouldn’t help here. Wheel consumers never compile anything, so what they need is provenance for what got bundled, and Python correctly reached for SBOM formats. The numpy 2.2.6 wheel I pulled to check still doesn’t have an SBOM in it despite the spec being accepted a year ago, which mostly tells you how long the tail is on rebuilding the world, and is part of why reconstructing this data from binaries after the fact stays useful even as the metadata standards land.
PEP 725
declares
dep:generic/openssl
style requirements in
pyproject.toml
so build tools know what needs to be present before they start, using a purl-derived scheme that again has no relationship to CPS despite covering ground that pkg-config users would recognise.
None of these efforts reference each other much, which is roughly what you’d expect when the C dependency problem gets solved piecewise by whichever community hits it hardest, but the pieces are at least using compatible identifiers now, and a CPS file with a purl in it is something you could trace through to a PEP 770 SBOM entry without anyone having planned for that to work.
