---
title: "This Week in Package Management: 15 August 2026"
url: "https://nesbitt.io/2026/08/15/this-week-in-package-management.html"
fetched_at: 2026-08-16T10:14:41.326540+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 15 August 2026

Source: https://nesbitt.io/2026/08/15/this-week-in-package-management.html

Week thirteen of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Releases
pnpm 12, the Rust rewrite, reached
RC 5
and the project published
What’s different in pnpm 12
: commands, flags, settings and the lockfile format are unchanged from pnpm 11, so upgrading is not a migration. RC 5 breaks dependency cycles canonically during peer resolution by ordering cycle members by package id and always cutting the closing edge in the same place, so the same dependencies produce the same lockfile regardless of importer or resolution order.
Hatch 1.18.0
adds a
sources
environment option that redirects individual dependencies to a local path, Git repository, URL, alternate index or workspace member at install time without altering the published metadata, and
hatch build --all
to build every workspace member at once.
Hatchling 1.32.0
lets the
version
command set a version that is statically defined in
project.version
, rewriting
pyproject.toml
in place.
Renovate 44.24.0–44.30.3
adds
support
for GitHub’s Actions lockfile, relocking it alongside
uses:
reference updates. 44.28.0 adds a
gomodTidyAll
option to run
go mod tidy
across every module in a Go monorepo after a dependency update, and 44.29.5
stops updating a PR branch
while it sits in a GitHub merge queue.
DNF5 5.4.3.0
ports the bootc integration from DNF4, adds
--allow-vendor-change
/
--no-allow-vendor-change
with a warning when upgrades are silently skipped by the vendor-change restriction,
remove --duplicates
to clear older duplicate packages, and a
gpgcheck_policy
setting.
Also out:
Security
Flatpak 1.18.1
and
1.19.0
fix six advisories including a sandbox escape to full host filesystem read/write via a symlink attack on app data directories (
GHSA-8688-9x26-hhxj
) and a local root privilege escalation via revokefs symlink traversal and commit tampering (
GHSA-qrwq-7qwx-q9rp
).
Docker Engine 25.0.17
backports fixes for three symlink and path-traversal vulnerabilities in mount handling and
docker cp
(
CVE-2026-41567
,
CVE-2026-41568
,
CVE-2026-42306
).
Podman 5.8.6
fixes
CVE-2026-19730
:
podman quadlet install --replace
did not truncate the file being replaced, so replacing a longer file with a shorter one left trailing content from the original.
GitHub Actions needs OIDC audience constraints
(William Woodruff): a workflow job with
id-token: write
can request an identity token for any audience at runtime, so a compromised PyPI publishing job can mint a token for AWS or any other configured relying party. The proposal is to make the permission list allowed audiences statically, e.g.
id-token: [pypi]
, as GitLab CI already supports.
Articles
nixpkgs multiverse: every version that ever existed
(Farid Zakaria) describes
nixpkgs-multiverse
, a flake that exposes every historical package version across all 1,393 nixpkgs channel revisions since 2017. A pair of JSON index files map each package version to its source revision so the target nixpkgs is fetched lazily on use, avoiding the overhead of pinning multiple inputs.
OxCaml opam guards
(Anil Madhavapeddy) explains how the Jane Street OCaml fork is packaged: an opam overlay repository ships patched
+ox
variants of packages that don’t compile against the extended compiler, and pairs of conflicting
.guard
and
.enabled
meta-packages use
conflicts:
fields to stop the solver installing an incompatible upstream release once the overlay is enabled.
I hate packaging my software for Linux
(Noam Lewis) walks through the trade-offs of deb, rpm, AUR, Flatpak, AppImage and Nix from the perspective of a TUI editor author, and lands on shipping a statically linked self-updating binary as the primary distribution mechanism instead. There’s a long
Lobsters thread
.
PyPI dependencies, resolved and built for you
(Sundaram Krishnan, Fedora Copr blog) introduces
coprtree
, which resolves a Python package’s dependency tree from
ecosyste.ms
metadata, drops packages already available in Fedora repositories or the target Copr project, and topologically sorts the remainder into a build order.
What is a package registry?
(Dave Verwer, Swift Package Index): following the index joining Apple, the two are building a Swift package registry. SwiftPM has resolved
.package(id:from:)
registry dependencies since Swift 5.7, fetching an immutable source archive instead of cloning a repository and checking out a mutable tag. Artifactory, AWS CodeArtifact, Cloudsmith and the read-only Tuist cache already implement the protocol.
Elsewhere
Following
PEP 833
, PyPI’s
HTML simple index representation is now frozen
: it will keep serving new packages and releases indefinitely but no new metadata fields will be added to it, with future index standardisation targeting only the JSON representation. pip and uv already prefer JSON.
Seventeen candidates are
standing
for the five seats on the 2026 Python Packaging Council, the
PEP 772
body with authority over packaging standards and PyPA tools. Voter registration closes 25 August and the vote closes 15 September.
Soar
is a distro-independent Linux package manager from pkgforge that installs static binaries, AppImages and FlatImages into the user’s home directory without root. Packages come from the
soarpkgs
repository, built on remote CI and verified with BLAKE3 checksums and minisign signatures.
git-pkgs
I tagged 24 repos this week:
Send links for next week to
@
[email protected]
.
