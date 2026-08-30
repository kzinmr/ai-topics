---
title: "This Week in Package Management: 29 August 2026"
url: "https://nesbitt.io/2026/08/29/this-week-in-package-management.html"
fetched_at: 2026-08-30T10:01:00.237974+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 29 August 2026

Source: https://nesbitt.io/2026/08/29/this-week-in-package-management.html

Week fifteen of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
pnpm 12
pnpm 12.0
is the stable release of the Rust rewrite. The commands, flags, settings and lockfile format from pnpm 11 carry over unchanged; a companion
what’s different
post lists the seven behavioural changes.
Git dependencies on GitHub, GitLab and Bitbucket now resolve through the host’s canonical HTTPS URL regardless of how they were specified, so lockfiles record only the canonical HTTPS URL for those hosts. Dependency cycles are broken canonically during peer resolution, so the lockfile is a pure function of the dependency graph. Cycle-heavy workspaces resolve peers 2-3x faster with roughly 25% less memory.
Globally installed tools resolve to the version pinned in the current project, and pnpm can provision npm, Yarn and Bun as managed tools with a
pnx
command for one-off runs. Unrecognised keys in
pnpm-workspace.yaml
are now errors.
On the 11.x branch,
11.23
reworks the
registries
setting so an Artifactory or GitLab registry can keep its tarball URLs out of
pnpm-lock.yaml
, and
11.24
restores
pnpm approve-builds --global
and groups recursive publishes by registry so a credential mismatch is caught before anything is uploaded.
Releases
Stack 4.1.0.1 RC
adds cross-package Backpack support: when a package uses signatures and mixins to depend on an abstract interface from another package, Stack now generates the extra instantiation build steps Cabal needs. Private Backpack, with signatures and implementations in the same package, was already supported.
winget 1.29.290
adds an experimental
sourcePriority
feature: sources can be given a numeric priority via
source add
or
source edit
, and higher-priority sources sort first in search results when other ranking factors are equal.
Maven 3.10.0-rc-1
is the first release candidate for the 3.10 line, which aligns 3.x behaviour with Maven 4: classpath ordering, version-range resolution filtering and the Resolver 2.0.19 changes are backported, and the super POM drops the deprecated
release-profile
and default plugin management.
Renovate 44.42.0
sets
CI=true
for every child process it spawns, and
44.49.0
fetches changelog entries newest-first and stops once the target platform’s PR body length limit is reached, instead of fetching hundreds of releases.
Also out:
Security
The Renovate project
disclosed ten advisories
affecting the CLI, nine High and one Moderate: four command injection vectors, four credential exfiltration paths via malicious
Link
headers, TLS private key exposure in logs, and a
minimumReleaseAge
bypass. All are fixed in 44.14.7, released 7 August.
Composer 2.10.3
and
2.2.30
fix four issues:
CVE-2026-59944
(path traversal via symlinked
bin
entries),
command injection via a malicious Perforce URL
, URL-embedded credentials leaking into more places than intended, and GitLab URL matching that could send credentials to the wrong domain.
ORAS 1.3.4
fixes three credential-scoping issues: mTLS client certificates supplied via
--cert-file
were presented to any HTTPS peer including cross-origin redirect and bearer-realm targets, custom
--header
values were forwarded to hosts other than the configured registry, and
--debug
traces logged pre-signed URL parameters, cookies, proxy authorisation and token response bodies.
Articles
Rumour is the exploit
(Anil Madhavapeddy): after opening a public PR fixing a path traversal in OCaml’s cohttp, Anil’s server logs showed probes for the exact pattern within minutes, and an agent given only a rough description of the bug produced a working exploit in under a minute. He argues that once the existence of a fix is public an agent can rediscover the bug independently, so the coordinated-disclosure window that embargoes are meant to protect has closed for open source maintainers.
What’s new in Private Packagist, August 2026
(Packagist blog): MFA enforcement now covers Composer authentication tokens, regenerated tokens invalidate the old one immediately (previously cached for 14 days), and security monitoring reads Composer 2.10’s
config.policy
section to determine which advisories to suppress.
Papers
Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code
(arXiv) shows that prior measurements overstate hallucinated-package rates by counting standard-library modules as hallucinations (by 9.4 percentage points for Python) and evaluates seven decoding-time strategies for reducing them.
The Rising Cost of Trust: Practitioners’ Trust Signals, Controls, and Responses in the Software Supply Chain
(arXiv) is a semi-structured interview study of 38 industry and open source practitioners on which signals they use when deciding to depend on a package and what controls they apply.
AROMA+: A Study of Factors Affecting Reproducible Builds in the Maven Ecosystem
(arXiv) automatically recovers the build environment for Maven Central releases and attempts to reproduce them: 32% of packages are feasible for automatic reproduction, of which 12% reproduce fully, and the recovered build specs match Reproducible Central’s manually curated ones field-for-field 99.8% of the time.
Elsewhere
The Rust project
announced
its first Maintainers in Residence, funding five contributors (including rustup maintainer rami3l) full-time and two more via grants for at least twelve months from a Rust Foundation maintainers fund backed by Google, AWS and OpenAI.
Fettle and the CVE problem
(Josh Bressers, Open Source Security): an interview with Paul Asadoorian on Fettle, a tool for checking a Linux system’s outdated packages, pending firmware updates and binary hardening flags, and on his InfraTrust Pulse report which tracks vendor advisories rather than raw CVE counts.
Additional Sustainability Topics from the CHAOSS Practitioner Guides
(Dawn Foster) covers the Security, Diverse Leadership and Sunsetting guides; the Security guide recommends Libyears and release frequency as dependency-currency metrics.
The Sovereign Tech Agency is
investing €508,640 in Flatpak
over two years, funding a contractor team organised by Modal Collective and Para-Real to build new portals for PipeWire audio, network isolation, VPN and spell-checking, plus an entitlements system for app permissions.
Rust Metadata Carver
(Decoder Loop) is a Binary Ninja plugin that extracts panic metadata from Rust binaries, recovering which crates and Rust version a stripped binary was built with.
renovate-pretty-log-tui 0.6.0
(Jamie Tanna) adds a summary view and HTML export to the terminal UI for reading Renovate debug logs, and surfaces errors more clearly.
git-pkgs
I tagged 9 repos this week:
Send links for next week to
@
[email protected]
.
