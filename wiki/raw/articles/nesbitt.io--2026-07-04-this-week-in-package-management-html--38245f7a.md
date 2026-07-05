---
title: "This Week in Package Management: 4 July 2026"
url: "https://nesbitt.io/2026/07/04/this-week-in-package-management.html"
fetched_at: 2026-07-05T07:00:45.471212+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 4 July 2026

Source: https://nesbitt.io/2026/07/04/this-week-in-package-management.html

Week seven of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Releases
Hex 2.5.0
adds organisation-defined dependency policies: an organisation publishes a named policy through its repository, a project opts in via
HEX_POLICY
or the
:hex
block in
mix.exs
, and resolution then filters out versions that carry an advisory above a given severity, are retired for listed reasons, or are newer than a release-age threshold.
Conan 2.30.0
adds SPDX expression support to its SBOM generation, a
conf=~
unset operator, and IntelCC support in the Meson, Autotools and Premake toolchains.
uv 0.11.25
hardens tar handling against parser differentials via an updated
astral-tokio-tar
, so uv may now reject malformed source distributions it previously accepted, and writes a full lockfile into tool receipts.
0.11.26
followed with resolver performance work reusing state across PubGrub iterations.
pixi 0.72.0
adds inline package manifests, so a git dependency without a Pixi Build manifest of its own can have build backend metadata set directly in the consuming project’s
dependencies
table.
mise 2026.7.0
adds
mise install --monorepo
with a tri-state
[monorepo].lockfile
setting for a single root lockfile across config roots, a per-tool
github_attestations
option to disable GitHub Artifact Attestation verification for one tool, and enables shell expansion in
env
by default.
Rust 1.96.1
is a point release fixing missing retries and timeouts in Cargo’s HTTP client and patching three libssh2 CVEs in the copy compiled into Cargo.
npm 12.0.0-pre.2
graduates the linked install strategy from experimental to stable and moves install-script approval under a dedicated
npm install-scripts
namespace.
brew-vulns 0.4.0
, which I maintain, uses the
resolves
field on formula patches added in Homebrew 6.0.4 to suppress false positives where the formula already carries a patch for the CVE, and records those as
analysis.state = resolved
in CycloneDX output.
Also out:
Homebrew 6.0.6
,
sbt 2.0.1
,
Cargo 0.97.2
,
Deno 2.9.1
,
Podman 5.8.4
,
Harbor 2.15.2
,
Dependabot Core 0.384.0
,
diffoscope 323
.
Security
Composer 2.10.2
and LTS
2.2.29
fix path traversal via package
bin
entries (
GHSA-gjfg-22fp-rrxx
), credential leakage in verbose output (
GHSA-g6xq-892h-64w3
), missing package name validation (
GHSA-499r-g7pc-vmp9
), and three further hardening changes around HTTP redirects, phar metadata and JSON error output.
Guix substitute and pull vulnerabilities
fixes four issues in the daemon and client: substitute extraction ran before hash verification so a malicious substitute could write arbitrary files as the daemon user, a substitute for one store item could be accepted in place of another,
file://
substitute URIs could leak daemon-readable files via error backtraces, and a malicious channel could overwrite user files via
guix pull
or
time-machine
. CVEs pending.
Mitigated: API bypass for download metadata on python.org
reports an authentication bypass in the python.org API where mixed handling of guest and API-key authentication could grant administrative privileges over download metadata; the fix separates the two modes and adds URL validation. Guix has a
tracking issue
on the implications for its importer.
Hijacked npm and Go packages use VS Code tasks to deploy infostealer
covers a campaign in which sixteen hijacked Go modules and a set of npm packages shipped fake font files and VS Code task definitions that fetched a Python infostealer.
Articles
GuixPkgs: every Guix package as a Nix flake
(Farid Zakaria) imports the full Guix package set into Nix by building a primitive that exposes each Guix derivation through a flake.
The Vulnerability Identity Crisis
(Jay Jacobs and Art Manion, Empirical Security) argues a vulnerability should be defined as a disposition, a structural property comprising a fault, conditions for exploitation, and a resulting security failure, rather than by surface characteristics.
Do excellent vulnerability reports
(Daniel Stenberg) is a guide for reporters on what an open source project needs from a vulnerability report to act on it.
All Package Management Functionality Moved from Compiler to Build System
(Andrew Kelley, Zig devlog) shifts package fetching, the HTTP client, TLS, the Git protocol and archive handling out of the
zig
binary into the build-side maker process, shipped as source. Networking now runs in
ReleaseSafe
with safety checks on and can be patched without rebuilding the compiler.
Papers
Mutating the “Immutable”: A Large-Scale Study of Git Tag Alterations
(Rapaport et al., arXiv) analyses 328.4 million repositories from Software Heritage and finds 10.2 million tags that were deleted or force-pushed after creation, undermining the assumption that a tag is a stable reference for reproducible builds.
Uncovering Similar but Different Packages in PyPI and Potential Security Threats
(Park et al., arXiv) measures package replication on PyPI, where a package duplicates most of an existing codebase, and traces how replicated packages propagate known vulnerabilities and provide cover for malicious variants.
Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware
(Ji et al., arXiv) builds payload transforms that evade all eight tested agent-skill scanners at over 90% via self-extracting packing, and proposes SkillDetonate, a sandboxed runtime auditor that catches 97% by observing behaviour at OS boundaries instead of inspecting at install time.
File-Level Copying Is an Implicit Dependency in Open Source
(He et al., arXiv) mines 690,500 copy events from World of Code and frames copied files as dependencies that lack the four signals a package manager provides: provenance, maintenance, security and compliance.
Elsewhere
The PSF has
announced the inaugural Python Packaging Council election
, establishing a technical decision-making body for Python packaging specs that coordinates across tools and teams.
The
Open Source Pledge
has a redesigned site marking $7 million paid to maintainers by member companies so far.
Once a Maintainer: Mike Dalessio
is an interview with the Nokogiri maintainer on the security work that comes with maintaining a widely depended-on gem.
git-pkgs
I tagged fifteen repos this week:
Send links for next week to
@
[email protected]
.
