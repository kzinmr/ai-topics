---
title: "Bazel Module Versions Aren’t SemVer"
url: "https://nesbitt.io/2026/08/27/bazel-module-versions-arent-semver.html"
fetched_at: 2026-08-28T10:01:35.210110+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Bazel Module Versions Aren’t SemVer

Source: https://nesbitt.io/2026/08/27/bazel-module-versions-arent-semver.html

Aman Sharma
reported
this week that
packages.ecosyste.ms
had the latest version of protobuf on the
Bazel Central Registry
(BCR, the default package index for Bazel’s built-in dependency manager) as
3.19.6
. The
current release
is
36.0.bcr.1
. Protobuf
dropped the leading
3.
in 2022
and has shipped
21.x
through
36.x
since, so
3.19.6
is four years behind.
The
root cause
is that the “latest release” query filters out anything the
semantic
gem fails to parse. That code predates the
vers
library and I’ve yet to swap it over, so it’s still applying one strict SemVer parser to every ecosystem. SemVer requires exactly three numeric segments before the hyphen.
36.0
has two,
0.7.1.bcr.1
has five, and
bcr
contains letters, so every protobuf release since
3.19.6
fails the parse and gets treated as unstable. The same filter reports
glog
’s latest as
0.7.1
when the registry has
0.7.1.bcr.1
.
Bazel is a build tool first, and its module system (
bzlmod
, the default since Bazel 7) is mostly used to pull in existing C++, Java and Go projects that already have their own release histories. Rather than force those projects to renumber, Bazel
documents
its version format as a deliberate loosening of SemVer: any SemVer string is valid and sorts the same way, and beyond that the release part can have any number of segments and each segment can contain letters. Abseil’s date-based
20210324.2
and protobuf’s two-segment
36.0
are both accepted as-is. The grammar in
Version.java
is
RELEASE[-PRERELEASE][+BUILD]
, where
RELEASE
is dot-separated identifiers of ASCII letters and digits only. Comparison applies SemVer’s
prerelease identifier rules
to the release segments as well:
numeric identifiers sort numerically, so
36.0
>
4.0.0
any identifier containing a letter sorts above every purely numeric one, then as an ASCII string
a version with more release segments sorts above one that shares its prefix, so
0.7.1.bcr.1
>
0.7.1
a prerelease sorts below the same release part on its own, so
36.0-rc2
<
36.0
The
.bcr.N
suffix is a
registry convention
rather than part of the format. Registry entries are immutable once published, and the registry often carries small patches on top of the upstream tarball to make a project build cleanly under Bazel. When one of those patches needs updating and the upstream source stays as-is, the fixed entry is published under a new version with
.bcr.1
tacked onto the release part. That’s why
36.0.bcr.1
exists:
36.0
was
yanked
for a macOS toolchain integrity mismatch, and the fix went in as extra release segments rather than a
+build
tag so that it sorts strictly above
36.0
. That ordering matters because Bazel resolves dependencies with
Minimal Version Selection
, the same algorithm as Go modules, which always picks the highest version any dependent asked for; a suffix that sorted equal or lower would leave everyone pinned to the broken build.
Version.java
also handles build metadata differently from SemVer §10: rather than being ignored for comparison and kept, the
+BUILD
part is
stripped at parse time
before anything is stored or sent to a registry, so
1.2.3+abc
and
1.2.3
are equal and interchangeable rather than equal-but-distinct. The empty string is a valid version and
sorts higher than everything else
; it marks a module that’s been overridden to point at a local directory or git commit instead of a registry release, and sorting it top means a local override always wins MVS. Since the release segments have no fixed meaning, breaking changes were originally signalled by a separate
compatibility_level
integer in the module file, roughly equivalent to a SemVer major version. Both active release lines
made that field a no-op
in February 2026 (9.1.0, backported to 8.6.0) after it caused resolution failures only the module authors could resolve, leaving breaking changes to be reported by the module’s own build-time errors instead.
External parsers get
.bcr.N
wrong one of two ways:
strict SemVer (the
semantic
gem): rejects
0.7.1.bcr.1
because the release part must be exactly three integers, so it drops from the stable set
permissive generic (the vers fallback): accepts the extra segments, applies prerelease semantics to the alphabetic
bcr
, and sorts it below
0.7.1
The
vers spec
, the package-url project’s cross-ecosystem notation for version ranges, enumerates comparison schemes for
fifteen ecosystems
and has yet to cover Bazel, though
pkg:bazel
is a
registered purl type
so there is already a slot for a
vers:bazel
scheme. Both vers libraries I maintain hit the second case. The fix in
Ruby
and
Go
is a port of the
Version.java
sort as an implementation-defined
bazel
scheme ahead of the spec. The corresponding
ecosyste.ms change
keeps
.bcr.N
releases eligible as stable, lets the yanked flag exclude
36.0
, and moves both protobuf and glog to the correct latest version.
