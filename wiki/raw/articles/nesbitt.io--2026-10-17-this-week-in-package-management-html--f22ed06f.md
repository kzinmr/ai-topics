---
title: "This Week in Package Management: 17 October 2026"
url: "https://nesbitt.io/2026/10/17/this-week-in-package-management.html"
fetched_at: 2026-10-18T10:01:01.308404+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 17 October 2026

Source: https://nesbitt.io/2026/10/17/this-week-in-package-management.html

This week’s package management news, gathered from the
package manager OPML feed collection
, my posts and boosts on
Mastodon
, and anything people sent me.
Releases
pnpm 12.12 to 12.14
add a
remoteCache
setting that shares signed task results and dependency builds through a pnpr server or any server that implements the Turborepo Remote Cache API, and 12.14 adds
sideEffectsCache.exclude
for packages whose builds depend on system libraries outside the cache key.
12.13
adds
pnpm profile
and
pnpm token
, plus a
storeIndexFormat: files
setting that replaces the SQLite store index with one file per package for stores shared over a network filesystem.
mise 2026.10.8 to 2026.10.12
reads release lists, tags and attestations from its mise-versions host instead of
api.github.com
. A cold
mise install
of
github:
tools now makes no GitHub API requests, and
mise ls-remote python
went from 961 ms to 93 ms.
2026.10.9
fixes a trust bypass where an untrusted
path:
tool version could put a directory on
PATH
, and 2026.10.11 fixes a trust issue in remote task files.
vlt 1.4.0
turns the global store on by default on macOS, cloning packages with copy-on-write
clonefile
through
node:ffi
on Node 26.1 and later. A warm reinstall went from 9.6 s to 3.1 s. It also adds
--save-types
, which adds the matching
@types
package to devDependencies, and a
vlt outdated
command whose JSON output includes the install command for each update.
.NET 11 RC2
adds
--min-publish-age-hours
to
dotnet nuget add source
and
dotnet nuget update source
, which writes the
minPublishAgeHours
setting to
nuget.config
. According to the
NuGet release notes
,
dotnet package add
and
dotnet package update
apply the cooldown, and restoring a floating version fails with NU1020 when the cooldown excludes every matching version.
pixi 0.82.0
adds
exclude-newer
to the
pixi global
manifest, taking a date or a duration such as
"7d"
, and accepts
amdgpu = true
or a specific GPU architecture such as
"gfx90a"
in platform declarations.
sbt 2.1.0-RC1
removes Apache Ivy from its dependencies and publishes without it. The metabuild moves to Scala 3.9, so plugins built for sbt 2.1 require sbt 2.1 or later.
pipx 1.18
runs
upgrade-all
,
reinstall-all
and
install-all
across several environments at once, and masks passwords in index and package URLs in its output and logs.
1.18.2
accepts absolute file URLs for local package installs.
uv 0.13.1
reports missing trusted hashes in resolution errors and adds preliminary parsing of PEP 825 variant labels in wheel filenames behind the
wheel-variants
preview. Tool and managed Python uninstalls now delete only their own storage directories and leave files next to them in place.
Spack Packages v2026.10.0
has 9,095 packages, up from 8,752 in 2026.06.0, and deprecates versions of several packages to address CVEs. It uses the v2.2 Package API, which works with Spack 1.0.0 and later. Its binaries are published to a
releases/v2026.10
build cache mirror.
Renovate 44.161 to 44.165
resolves Go modules whose
go-import
meta tag names a
mod
proxy as of
44.164.0
, which covers generated modules from a private Buf Schema Registry. An Ubuntu libcurl security update in the 44.161.0 base image made git send username-only credentials on the first request of a clone and omit them from the follow-up. Self-hosted users with a personal access token
could no longer clone private repositories
. The fix in
44.164.1
puts the token after
x-access-token:
in GitHub clone URLs.
44.164.9
adds a fallback username for SCM-Manager and is the version the maintainers recommend upgrading to. In the configuration JSON Schema,
#46945
limits known object properties to their listed keys.
Dependabot Core 0.400.0
adds an
apm
(Agent Package Manager) ecosystem and supports Bun 1.4 lockfiles.
zizmor 1.31
treats
issue_comment
as a dangerous trigger and flags
cache-mode: write
and
write-only
alongside dangerous triggers.
typosquat-uses
now also checks pre-commit inputs.
Also out:
Security
Package managers have an integrity problem
(Keegan Ryan, Trail of Bits) runs 25 package managers with default settings against a simulated compromised repository behind mitmproxy. Go and vcpkg were the two that verified every download when there was no lockfile, and Go alone verified signatures by default. Fewer than half check lockfile hashes for tampering by default. The post proposes recording signer identity in lockfiles, backed by Sigstore identity signing and a transparency log.
rubygems.org now shows security warnings
(Anton Bondaronok) on gem version pages, using OSV data refreshed every hour. Reports from the OpenSSF Malicious Packages project are labelled as malware, and older affected versions get a warning icon in the versions list. For now the warnings appear on rubygems.org pages only, and the next step is adding advisory data to the Compact Index so
gem install
and
bundle install
can show them.
RubyGems 4.0.23
drops setuid, setgid and sticky bits from files when it extracts a gem.
PyPI now checks email reputation
when an address is used to register or is added to an account, and rejects disposable addresses using a service donated by UserCheck. In the past month the check blocked 62 disposable domains and more than 120 disposable addresses on otherwise valid domains. PyPI banned
outlook.com
and
hotmail.com
in June 2024 after a malware campaign used them to register accounts in bulk, and with the check in place both domains are accepted again.
GitHub’s malware advisories now cover eight ecosystems
(OpenSSF), up from npm only to npm, PyPI, Maven, RubyGems, NuGet, Go, crates.io and Composer. GitHub imports reports from the
OpenSSF Malicious Packages
repository, which contains more than 238,000 reports in OSV format, and Dependabot users with malware alerts turned on get the wider coverage with their existing configuration.
pnpm 12.12.1
and
11.28.6
make
pnpm publish
use an
NPM_ID_TOKEN
only when its
aud
claim matches the registry being published to, so a CI identity token goes only to the registry it was issued for.
12.12.0
makes an
allowBuilds
entry set to
false
take precedence over
dangerouslyAllowAllBuilds
, which previously ran those build scripts anyway.
Hex 2.5.3
fixes
CVE-2026-96596
, where a GNU sparse file in a package or docs tarball could put
mix deps.get
into an infinite loop. It also percent-encodes package names and versions in request URLs, so a
/
,
?
,
#
or
..
stays inside its path segment.
Docker Engine 29.9.1
updates containerd to 2.4.2 for three advisories where a malicious registry or crafted image could crash containerd or fill the host disk.
OpenTofu 1.12.8
and
Terraform 1.16.6
both fix excessive CPU usage when
init
connects to an attacker-controlled HTTP/2 server while installing dependencies, which Terraform’s notes track as CVE-2026-78669.
How the PHP Security Team Handles Your Reports
(Alexandre Daubois, PHP Foundation) covers the triage process for php-src. Since 1 July the team has published 15 CVEs and closed 106 other reports as invalid, duplicates or not reproducible. Reports are reproduced on Linux, macOS and Windows under AddressSanitizer and UndefinedBehaviorSanitizer. AI-written reports are accepted if the issue reproduces on a PHP build.
Articles
Nixpkgs for the frontend impaired
(Farid Zakaria) introduces
jinx
, which compiles each
.nix
file to a TypeScript module. Across three platforms, 229,063 of nixpkgs’ 231,777 attributes produce the same drvPath as Nix, and the other 2,714 fail in both. It runs in Node 24 or a browser tab, three to five times slower than Nix. A second post,
Always, sometimes, never
, adds property checks such as
single-writer
and
atomic-replace
to Rewind VM’s schedule exploration.
Reproducible Builds in September 2026
covers the summit in Gothenburg and seven proposals for the
SOURCE_DATE_EPOCH
specification that are open for feedback until 1 December. dettrace now runs on most Debian and openSUSE architectures and supports PGO builds.
Thank you, Deno
(Darcy Clarke, vlt), written after last week’s Cloudflare news, credits competition from Deno and Bun for features Node and npm later shipped, including
fetch
, the built-in test runner, type stripping and npm 12 making install scripts opt-in.
Elsewhere
Mend upgraded 184 open source organisations to the Renovate Community plan
(Jamie Tanna, Mend). The upgrade covers about 3,000 repositories on Mend-hosted Renovate, including Argo, Biome, Nuxt, Tauri and the Rust project. The plan raises resource limits and concurrency and adds Merge Confidence. Other projects can request it in a Mend Hosted Request discussion.
VulnBump
(Gabija Pasiunaite et al., arXiv) is a benchmark from Snyk of 307 dependency upgrade tasks covering 2,066 fixable vulnerabilities in 43 repositories across six package managers. A task passes when dependencies resolve and a rescan shows the fix, with the build and previously passing tests still green. Applying Snyk’s recommended version passed 46.9% of tasks, Claude Code on its own 59.6%, and Snyk’s remediation agent 90.2%.
Forgejo 17.0
reads
FUNDING.yml
to show a Donate button on repositories and profiles, and adds LFS views for locks and pointer files, plus a list of the commits that changed each file. The project
recommends waiting before upgrading to 17.0.0
while it investigates an issue in that release that can stop pushes, merges and other code operations.
The
Python Packaging Council
has made its
GitHub repository
public, and will post the notes from each meeting there. People can file issues on the tracker to ask the council for a decision or for input.
git-pkgs
I tagged
bibtex v0.1.0
(new), a Go library for reading BibTeX such as
CITATION.bib
files and entries embedded in READMEs, built for scanning untrusted input in bulk, alongside
brief v0.14.2
and
integrity v0.2.0
.
Send links for next week to
@
[email protected]
.
