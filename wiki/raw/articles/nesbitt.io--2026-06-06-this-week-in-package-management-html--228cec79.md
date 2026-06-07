---
title: "This Week in Package Management: 6 June 2026"
url: "https://nesbitt.io/2026/06/06/this-week-in-package-management.html"
fetched_at: 2026-06-07T07:01:35.191633+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 6 June 2026

Source: https://nesbitt.io/2026/06/06/this-week-in-package-management.html

Third week of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
. Five new project blog feeds and the NixOS announcements feed landed in the OPML this week.
Security
Bundler 4.0.13
ships
Cooldown
, a configurable time window that holds back resolution to gem versions younger than N days, so a freshly published malicious release ages past the window before a
bundle install
will pick it up. The companion
RubyGems 4.0.13
release blocks gem extraction from escaping the destination directory via pre-existing symlinks.
The Packagist supply-chain series continues.
Closing Composer’s Download Fallback Paths
covers how the dist-to-source fallback, originally designed for resilience, can be used to fetch a different artifact than the one Composer expected.
Blocking Malware Downloads for Every Composer Version
describes how Private Packagist enforces malware blocking for installs from Composer versions older than 2.10, before the dependency policy framework existed.
Enforce a Safe Composer Version Across Your Organization
closes the loop by letting Private Packagist organisations restrict which Composer client versions can fetch the repository at all, rejecting older clients with an error that surfaces in the developer’s terminal.
New HexDocs URLs: per-package subdomains
moves public Elixir and Erlang package docs from
hexdocs.pm/package
to
package.hexdocs.pm
, and organization docs to a separate registrable domain (
hexorgs.pm
). The browser’s same-origin policy now isolates packages from each other, addressing a finding from Hex’s recent security audit that docs pages run maintainer-controlled HTML, CSS, and JavaScript under a shared origin.
Homebrew’s
Tap-Trust documentation
describes an upcoming change to how non-official taps are loaded. Today any installed tap contributes formulae, casks, and commands by default. Under Tap-Trust, taps need explicit approval via
brew trust user/repo
(or a per-formula variant) before Homebrew evaluates their code. The change becomes the default in Homebrew 6.0.0 or 5.2.0, whichever ships first.
HOMEBREW_REQUIRE_TAP_TRUST=1
opts in early.
Composer 2.10.1
fixes shell escaping when opening an editor and verifies the backup phar’s signature before
self-update --rollback
restores it.
NuGet.Server 3.4.3
fixes an unauthenticated denial-of-service on the package upload endpoint (CWE-696/CWE-400) by moving API key validation ahead of the file I/O and package processing it used to do first.
Releases
Yarn 4.16.0
adds
yarn npm stage
for npm’s staged publishing queue, alongside editor SDK support for oxc’s formatter and linter.
Hatch 1.17.0
deprecates
hatch fmt
in favour of a new
hatch check
command group with
code
,
fmt
, and
types
subcommands. Type checking is wired up to Pyrefly. The release also adds
hatch env lock
for locking environments and switches the HTTP client from httpx to httpx2.
NixOS 26.05 “Yarara”
is the latest six-monthly release of Nixpkgs and NixOS. The Nixpkgs side added 20,442 new packages and updated 20,641 since 25.11, and dropped 17,532. This is also the final release with
x86_64-darwin
support, since upstream Apple has deprecated the platform.
Stack 3.11.0.1 RC
switches the default 64-bit Windows MSYS environment from MINGW64 to CLANG64, following the MSYS2 project’s deprecation of MINGW64 in March.
Dependabot Core 0.380.0
adds a lockfile generator for bun via PR
#14882
. The same release passes
--config.minimumReleaseAge=0
to pnpm security updates, bypassing any
pnpm-workspace.yaml
cooldown setting so security PRs aren’t blocked behind the release-age policy.
mise 2026.6.0
wires npm into Corepack when
node.corepack=true
and
node.npm_shim=false
, so the Corepack-managed npm shim sits alongside yarn and pnpm, and aligns aqua’s Windows extension handling with upstream.
Windows Package Manager 1.29.250
is the 1.29 release candidate. Sources can now be assigned a numeric priority (experimental). When several sources offer the same package, installs prefer the higher-priority source without prompting. Export and import round-trip override and custom installer arguments, and the MCP server gained upgrade actions.
Also out:
Cargo 0.97.1
,
uv 0.11.19
,
pip 26.1.2
,
Conda 26.5.2
,
Mamba 2.8.0
,
pixi 0.70.1
,
pnpm 11.5.2
,
pipx 1.14.0
,
Deno 2.8.2
,
Homebrew 5.1.15
,
Docker Engine 29.5.3
,
Go 1.25.11
,
Go 1.26.4
,
sbt 2.0.0-RC14
,
cargo-semver-checks 0.48.0
.
Articles
Where does the money come from?
(Daniel D. Beck) is a catalogue of every channel he knows that gets technical-documentation authors and maintainers paid, from foundation grants and staff tech-writer roles to docs-for-hire arrangements and tip jars.
How OSPOs can measure the impact of OSS funding
(Dawn Foster) is the case OSPOs can make internally when budgets tighten and the funded projects don’t translate directly into product revenue. Dawn also has a
four-page piece in IEEE Computer
on how governance choices shape open source project sustainability, aimed at project leads.
The
Rust Foundation Maintainers Fund
launched this week as a “Maintainer in Residence” programme that pays existing Rust Project maintainers from a donor-funded pool.
Rendering a lock file with pipdeptree
is a new tutorial for the
from-lock
subcommand, which prints the dependency tree of a PEP 751 lock file offline without resolving or installing anything.
The
Reproducible Builds May 2026 report
leads with
Debian’s decision
to require reproducibility for packages migrating into the next release (“forky”), blocking unreproducible packages from migration.
Papers
Poking Around in the Dark: Why a Shared Understanding of Components Matters
(Reichmann et al., arXiv) finds that SBOM generators disagree on what counts as a component in the same software, leaving gaps in supply-chain vulnerability identification.
PyFEX: Uncovering Evasive Python-based Threats via Resilient and Exhaustive Path Exploration
(Wang et al., arXiv) is a forced-execution engine for Python that recovers from crashes mid-run and flagged 212 previously unknown malicious uploads on PyPI.
Elsewhere
crates.io PR #13855
proposes surfacing standard-library replacements on crate pages: a banner on the crate page and a marker in dependency lists, each linking to the
std
API that covers what the crate did. Seeded with
lazy_static
,
once_cell
,
matches
, and
num_cpus
. The PR cites my
features everyone should steal from npmx
post as one of the inspirations.
Send links for next week to
@
[email protected]
.
