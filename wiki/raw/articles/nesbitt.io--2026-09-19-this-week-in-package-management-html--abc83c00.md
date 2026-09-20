---
title: "This Week in Package Management: 19 September 2026"
url: "https://nesbitt.io/2026/09/19/this-week-in-package-management.html"
fetched_at: 2026-09-20T10:01:20.279984+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 19 September 2026

Source: https://nesbitt.io/2026/09/19/this-week-in-package-management.html

Week eighteen of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
. I
added nineteen feeds
to the OPML this week, mostly project blogs, plus GNU Guix, Zig and the Reproducible Builds monthly reports.
Releases
Homebrew 7.0.0
overlaps package preparation with downloads for faster installs, sandboxes formula and cask operations (home-directory reads are blocked by default), and adds
brew vulns
, backed by a new CC0-licensed OSV-format advisory database. It also ships BrewUI, a native macOS app for browsing and installing packages, drops macOS 10.15 support, and moves Intel Macs to Tier 3. Patch releases through
7.0.4
fix Perl bottle relocation under the shorter prefix and restrict which files are verified when tapping.
Swift 6.4
makes Swift Build the default build system in SwiftPM and adds SBOM generation in SPDX and CycloneDX formats via
SE-0509
.
pnpm 12.5
extends the Python support added in 12.4: each workspace project selects its own interpreter against
requires-python
(downloaded from python-build-standalone if missing), projects with a
[build-system]
install as editable, and a
shared-environment
setting resolves multiple members into one workspace-root
pylock.toml
and
.venv
.
pnpm add
now accepts Package URLs across the npm, cargo and pypi types.
sbt 2.1.0-M1
moves the metabuild to Scala 3.9 and removes Apache Ivy as a dependency; plugins built for 2.1.x are incompatible with sbt 2.0.x.
RubyGems and Bundler 4.0.21
normalises absolute symlink targets during gem extraction and rejects Bundler redirects that downgrade HTTPS to HTTP.
Pixi 0.81.0
extends
pixi run --script
to fetch conda-script files from HTTP and HTTPS URLs, including Gists, reusing the cached environment.
uv 0.12.16
verifies downloaded wheels and sdists against hashes supplied by the index;
0.12.17
adds a preview
minimum-libc-version
setting for the glibc and musl floor a universal resolution must satisfy, and rejects
pylock.toml
wheels whose filenames differ from their declared name or version.
Renovate 44.103.2
: the Dockerfile manager
natively extracts
pinned
apk add
and
apt install
packages from
RUN
instructions without a custom regex manager, and the GitHub Actions manager
documents
the 81 actions whose
with:
version inputs it updates. A new
minimumReleaseAgeBuffer
option covers sibling packages published after the main package.
opam 2.6.0
is out. The shell hook now updates the opam-managed directory in place instead of prepending it to
PATH
, build directories are deleted sooner during install, and HTTP repository loads read
index.tar.gz
in memory to cut tens of thousands of syscalls to one on Windows and constrained filesystems.
Also out:
Security
The Rust security response WG
warned
of an ongoing social-engineering campaign against rust-lang team members and owners of popular crates: a video call is arranged under a job, project or contract pretext, then used to persuade the target to install a supposed audio codec or run a command placed on the clipboard, with the aim of publishing malware from the compromised account.
Podman 6.1.2
and
5.8.7
fix
CVE-2025-11395
, where
podman load
on an image with a crafted layer tarball, or
podman volume import
on a volume with crafted symlinks, could overwrite files on the host.
pnpm 12.4.2
stops a dependency’s executable from redirecting another package’s POSIX bin shim through its shell helpers (a reinstall replaces existing shims) and stops GitHub Actions homepage links from including server credentials. The Cygwin, MSYS2 and WSL shims still resolve
PATH
for Windows path conversion, so the redirect remains possible there.
Aaron Patterson
wrote up
the mechanism behind the May rubygems.org spam campaign covered
last week
: a
--load ./script.rb
line in a gem’s
.yardopts
runs during YARD documentation generation, so publishing a gem executed arbitrary code inside rubydoc.info’s networked container, which the campaign used to extract cached rubygems.org API keys and publish more gems.
Articles
PyPI posted an
incident summary
for the intermittent 502 and 503 errors on file downloads through the second half of August: a Fastly canary deployment misconfiguration on one cache node combined with bugs in PyPI’s own Fastly config around fallback routing and range requests, all resolved by 28 August. An earlier post explains that PyPI
changed its download counting
on 24 August to log only distribution file downloads (
.whl
,
.tar.gz
,
.zip
) rather than every package-related request. About 39% of the previous totals were metadata fetches and are now excluded.
Papers
An Exploratory Study of Dependabot Cooldown Adoption in Open-Source GitHub Projects
(Tanaka et al., arXiv) looks at repositories that enabled Dependabot’s cooldown feature: security was the stated motivation in 83 of the 92 adoptions that gave one, 97.2% set a general delay rather than per-update-type settings, and 64.3% of those set it to seven days.
Python Import as an Execution Boundary
(Chen and Li, arXiv) mines PyPI histories and advisories for bugs and vulnerabilities that trigger at
import
time: module-level and
__init__
code activates 98.3% of the cases they confirm, and 90% of the twenty initialisation-time advisory vulnerabilities are rated High or Critical. Fixes more often move when the import runs than remove the dependency.
GANADI: Uncovering C/C++ OSS Reuse Genealogies
(Kim et al., arXiv) clusters downstream C/C++ projects by pivotal functions to reconstruct which project copied code from which, then uses the resulting reuse tree to route vulnerability reports; 23 of 48 unpatched vulnerabilities they found this way were fixed after disclosure.
CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection
(Noirot Ferrand et al., arXiv) deobfuscates, unbundles and backward-slices npm package source before it reaches an LLM scanner, raising analysis coverage from 69.1–85.7% to 98.8–100% across 512 large package files and cutting false negatives by up to 18.6 points.
Freeriding and Rebellion: An Investigation of Open Source Vendor Relicensing and Member Hard Forking Events
(Foster and Germonprez, Information Systems Journal) studies vendor relicensing events and the hard forks that follow: vendors invoke freeriding concerns to justify governance changes, and community members respond by realigning their engagement into forks. Dawn Foster has a
summary post
.
Elsewhere
The OpenJS Foundation CNA is
pausing CVE triage, validation and assignment
from 17 September to 6 October, citing the volume of AI-generated security reports reaching its volunteer team. Incoming reports queue for processing after the break; actively exploited issues still get a response through the OpenJS Slack.
Pillow
updated its security policy
along the lines of CPython’s, asking reporters to verify LLM-generated findings, deduplicate batches, and check the project’s threat model before submitting; Hugo van Kemenade
noted
the previous day’s 82 reports totalled over 226,000 words.
Emma Irwin has moved
Open Source Wishlist
to a standalone teaching tool that uses
Ecosyste.ms
metadata to surface single-maintainer risk and open vulnerabilities for a chosen project and generate a support plan. Irwin argues that the data, standards and expertise for open source sustainability already exist and funding is the missing piece.
The PSF
announced the results
of the inaugural Python Packaging Council election covered
last week
: Brett Cannon and Pradyun Gedam take two-year seats, and Donald Stufft, Henry Schreiner and Ralf Gommers take one-year seats, on 541 ballots.
The Reproducible Builds
August report
covers Brett Cannon’s write-up of what a low-friction reproducible-builds path on PyPI would need,
daleq4py
for establishing equivalence between rebuilt Python wheels, and the AROMA+ study of build reproducibility feasibility across Maven Central. A separate
interview with Jochen Sprickerhof
covers
reproduce.debian.net
reaching over 98% reproducibility for Debian packages, up from 33% in 2024, and the May policy change blocking non-reproducible packages from entering new Debian releases.
Git 2.56.0-rc1
was tagged.
git-pkgs
I tagged nine repos this week:
Send links for next week to
@
[email protected]
.
