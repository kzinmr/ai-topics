---
title: "Shared Code Between Package Managers"
url: "https://nesbitt.io/2026/08/11/package-manager-library-reuse.html"
fetched_at: 2026-08-12T10:18:35.231874+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Shared Code Between Package Managers

Source: https://nesbitt.io/2026/08/11/package-manager-library-reuse.html

Writing up the
package manager CWEs
list and then the
--end-of-options
survey, both of which come down to the same bug being fixed independently in tool after tool, left me wondering how much code these tools share with each other in the first place. So I went through the direct dependencies of
twenty package managers
, each with at least two same-language peers in the set, looking for package-management libraries reused between them and setting aside the general-purpose stuff any CLI would use (serde, clap, requests).
Three of the twenty depend directly on another manager’s own packages: Pixi declares twenty-eight uv crates as its PyPI backend (including
uv-resolver
,
uv-distribution
,
uv-client
,
uv-install-wheel
,
uv-pep440
, and
uv-git
), pnpm depends on five Yarn Berry packages (
@yarnpkg/core
,
@yarnpkg/lockfile
,
@yarnpkg/pnp
,
@yarnpkg/nm
,
@yarnpkg/extensions
), and uv takes
cargo-util
from the Cargo repository.
Eight of the shared libraries are npm-org packages used across npm, Yarn Berry, and pnpm in varying combinations:
semver
,
ssri
,
hosted-git-info
,
validate-npm-package-name
,
npm-registry-fetch
,
libnpmpublish
,
node-gyp
,
bin-links
. PyPA publishes
packaging
(PEP 440 specifiers, used by pip, Poetry, and Conda) and
pyproject-hooks
(PEP 517 build-backend invocation, used by pip and Poetry), and in both the npm and PyPA cases the publisher also maintains the spec the library implements. uv and Pixi both declare Embark Studios’
spdx
crate for licence-expression parsing, separately from Pixi’s use of uv’s crates. DNF5 and Mamba both use
libsolv
, the one solver library in the corpus adopted across unrelated registries.
pip, Bundler, and Homebrew reuse code by vendoring it rather than declaring a dependency, for bootstrap reasons. pip’s
_vendor/
directory contains
packaging
,
pyproject_hooks
,
distro
,
platformdirs
,
requests
, and about a dozen more, so pip does use the same PEP 440 parser as Poetry and Conda, without the dependency edge. A CVE fix in a vendored library reaches each consumer as a re-vendor commit, and all three have tooling for that step (pip’s is
nox -s vendoring
against a pinned
vendor.txt
).
The only overlap in the Ruby group is
ruby-macho
, for reading Mach-O headers, shared by Homebrew and CocoaPods. Until recently there was a second: CocoaPods’
Molinillo
resolver was vendored by Bundler from 2014 and by RubyGems from 2015. Bundler 2.4.0 replaced it with
pub_grub
in December 2022, and RubyGems
followed on master
in June 2026. No two managers share a git subprocess wrapper except through Pixi’s use of
uv-git
. Outside JavaScript, no two share an archive extractor with path checks.
Most of the twelve recurring client-side bug classes in that CWE list correspond to one of these reimplemented operations: path traversal in the archive extractor, argument injection in the git wrapper, ReDoS in the version-range parser, credential leaks in the registry HTTP client, integrity checks that fail open in the download path. npm’s
tar
package, which npm and Yarn Berry both depended on in 2021, had five path-traversal advisories that year (
CVE-2021-32803
,
CVE-2021-32804
,
CVE-2021-37701
,
CVE-2021-37712
,
CVE-2021-37713
): five fixes made in one codebase and taken by each consumer as a version bump. The same applied to
semver
(
CVE-2022-25883
) for npm, Yarn, and pnpm, and to
hosted-git-info
(
CVE-2021-23362
) for npm and pnpm.
The
--end-of-options
survey traced eight git argument-injection CVEs across six tools: Bundler in 2021, Composer in 2021 and 2022, CocoaPods and Poetry in 2022, pip in 2023, Go in 2026. Each of those eight was reported and fixed independently, with the affected tool vulnerable to a publicly documented attack from the first disclosure of the pattern until its own patch was released, a gap of five years in Go’s case.
npm ships inside Node, so npm’s bootstrap is handled by the Node installer. That lets npm’s internals be published as separate packages that competitors depend on. RubyGems and pip have no equivalent: a
git-source
gem published by the RubyGems team would be a dependency RubyGems itself couldn’t declare.
libsolv
is maintained outside any of the managers that use it, and the operations with per-tool advisory streams in the CWE dataset (git invocation, checked archive extraction, download-verify-cache) have no spec owner.
