---
title: "This Week in Package Management: 22 August 2026"
url: "https://nesbitt.io/2026/08/22/this-week-in-package-management.html"
fetched_at: 2026-08-23T10:01:40.583735+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 22 August 2026

Source: https://nesbitt.io/2026/08/22/this-week-in-package-management.html

Week fourteen of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Releases
Go 1.27
is out. On the module side,
go mod tidy
now consolidates duplicate
require
blocks into the canonical direct/indirect pair for modules declaring
go 1.27
or later,
go doc
accepts
package@version
to fetch documentation for a specific module version, and the
go
command drops support for fetching modules from Bazaar repositories. A
compress/flate
encoder change
also means
archive/zip
and
compress/gzip
produce different bytes than under Go 1.26, which is worth checking anywhere a Go-built tool’s archive output is hash-pinned downstream (forge tarball endpoints, module proxies, release pipelines).
Rust 1.98
ships Cargo with an unstable
-Zmin-publish-age
flag implementing
RFC 3923
: resolution filters out crate versions published more recently than a configured threshold. It also fixes a 1.96 Windows regression in
cargo:token-from-stdout
credential providers.
Bun 1.4
is the first release of the
Rust rewrite
, the bulk of which Jarred Sumner produced from the Zig codebase with Claude Code workflows. It fills out the package manager subcommands:
bun pm diff
shows un-minified source diffs between package versions and flags new install scripts,
bun audit fix
upgrades vulnerable dependencies,
bun dedupe
and
bun prune
clean up the lockfile and
node_modules
, GitHub and tarball dependencies now record SHA-512 hashes in the lockfile, and only packages from the npm registry are auto-trusted to run install scripts by default.
pnpm 11.22
shipped alongside a
11.21–11.22 recap
:
pnpm install
now edits the lockfile in place for most everyday manifest changes without re-resolving the whole dependency graph, global installs switch over atomically,
pnpm cache path
prints the store location, and a project’s
pnpm-workspace.yaml
can no longer relocate machine-level state directories. pnpm 12 reached
RC 8
: the
registries
setting is now keyed by URL with scopes and tarball layout declared per entry, and
packageImportMethod: auto
tries hardlinks before reflinks on Linux, roughly halving the time to materialise
node_modules
from a warm store on btrfs.
Hex 2.5
surfaces security advisories during
mix deps.get
and
mix deps.update
, printing a summary of vulnerable packages at the end of the run. A
cooldown
setting withholds versions younger than a configured age from resolution, lifted automatically when the currently locked version is itself retired or has an advisory, and organisations can publish signed dependency policies that opted-in projects apply centrally.
Renovate 44.33.0–44.39.1
adds
PEP 691 JSON simple index
support to the PyPI datasource and passes
POETRY_SOLVER_MIN_RELEASE_AGE
through to Poetry when
minimumReleaseAge
is configured.
Also out:
Security
crates.io
removed
malicious versions of
arrayref
,
internment
,
append-only-vec
and several typosquat crates published from a compromised maintainer account. The malicious versions carried a build script that downloaded a remote payload and were live for under two hours before deletion; the post gives a command to check the local Cargo cache for the affected versions.
sbt 2.0.6
and
1.12.15
fix
GHSA-m2pw-22cj-jq4v
, a remote code execution via the sbt server when
serverConnectionType
is set to
Tcp
, and
2.0.7
/
1.13.0
fix the same class of bug in the BSP handler (
GHSA-943m-f264-54p4
). Builds using the default Unix domain socket connection type are unaffected.
Articles
What’s missing to have reproducible builds on PyPI
(Brett Cannon) sets out three gaps: distributions don’t record the source location they were built from, sdists have no standard place to store build-environment SBOM data the way wheels do, and there’s no channel for independent verifiers to attest to PyPI that they reproduced a distribution.
Protecting the Rust standard library from breakage
(Predrag Gruevski): rust-lang/rust CI now runs cargo-semver-checks against
core
,
alloc
and
std
, treating
#[stable]
and
#[unstable]
attributes as the public-API boundary. Getting there meant new stability fields in rustdoc’s JSON output and threading them through the linter’s query layer without rewriting existing lints.
Spinel dev log, July 2026
: the Ruby tooling cooperative’s monthly update on
rv
(a Ruby version manager with its own
precompiled Ruby builds
), the Dyad shell helper, and brut-pack for bundling scripts.
How mature is this repository?
(Alexandre Dulaunoy) introduces
OSSTRL
, which computes a 1–9 Technology Readiness Level for a GitHub repository from automatically gathered evidence across community, governance, development, support and security dimensions, with maturity gates so a single strong signal can’t inflate the overall level.
Papers
Implicit, Yet Impactful: Understanding Hidden Dependencies in Java Projects
(Zhang et al., arXiv) measures transitive Maven dependencies whose classes are referenced directly by a project’s own code without being declared: across 972 GitHub modules, 34% contain at least one, 48% of those introduce breaking API changes, and 36 CVEs in the sample expose vulnerable methods that the root project calls directly.
SMTpip: Interpreter-Aware SMT-Based Dependency Conflict Resolution
(Sakib et al., arXiv) encodes both package version constraints and Python interpreter compatibility as SMT formulas so a solver can decide up front whether a satisfying environment exists, reporting a 6.9× speedup over pip’s backtracking resolver on their benchmark.
Elsewhere
Commonhaus and HeroDevs launch OSSI
(Josh Bressers, Open Source Security): an interview with Erin Schnabel and Rob Nalen on a partnership funding CVE remediation and extended support for end-of-life releases of Commonhaus-hosted projects, starting with Hibernate, Jackson and Quarkus.
How AWS powers PyPI and the PSF
(PyPI blog): AWS’s open source credits programme covers PyPI’s infrastructure bill and its security sponsorship funds engineering time, but PyPI is currently maintained by roughly one and a half full-time engineers plus one on support. A line describing PyPI as a supply chain risk given that staffing was later
reworded
.
Inside Modern Software Engineering with Homebrew’s Mike McQuaid
(Giant Robots podcast): an interview covering Homebrew’s history and open source maintainership.
Sustain #293
has Daniel Roe and Matias Capeletto on
npmx
, the community-built npm registry browser, covering how the project reached hundreds of contributors since January and its governance and funding.
git-pkgs
I tagged 16 repos this week:
Send links for next week to
@
[email protected]
.
