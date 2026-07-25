---
title: "This Week in Package Management: 25 July 2026"
url: "https://nesbitt.io/2026/07/25/this-week-in-package-management.html"
fetched_at: 2026-07-25T10:10:36.564656+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 25 July 2026

Source: https://nesbitt.io/2026/07/25/this-week-in-package-management.html

Week ten of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Releases
RubyGems and Bundler 4.0.17
validate the spec name before writing to the spec cache, escape glob metacharacters in install paths, and fix a run of Windows path-handling bugs in
gem open
,
bundle open
and the
MAKE
/
rake
environment variables.
uv 0.11.31
lets workspace sources reference members of a different workspace by path, supports
.venv
files that point at a centralised project environment, and adds
audit.malware-check
and
audit.malware-check-url
settings. There is also a preview
hash-algorithm
setting per index for lockfile generation.
0.11.32
followed, rejecting non-canonically formatted lockfiles in
uv lock --check
and regenerating them with
uv lock --refresh
.
opam 2.6.0-alpha1
is the first alpha of the 2.6 series. The shell env hook now updates opam’s bin directory in
PATH
in place instead of always moving it to the front, repositories are read from
index.tar.gz
in memory via
ocaml-tar
so
opam update
needs one syscall instead of tens of thousands on slow filesystems, and build directories are deleted sooner to cut disk use.
pnpm 11.11–11.14
is a wrap-up post covering four minors. New since
last week
:
pnpm doctor
for end-to-end installation diagnosis,
pnpm access
for managing package permissions on the registry, convergence overrides, scheme-carrying
peerDependencies
specifiers, a path-traversal fix, and roughly 30% lower peak memory during cold-cache resolution.
mise 2026.7.11
is the first published release since 2026.7.7; 2026.7.8 through 2026.7.10 were tagged but never went out because of a release-pipeline problem. Structured tool definitions now accept
version
,
path
,
prefix
and
ref
selectors consistently across root
[tools]
, task definitions and templates, and shell activation does less redundant work.
2026.7.12
adds a
MISE_SAFE=1
mode that turns mise into an inert config reader, so CI and bots can run
mise lock --bump
against untrusted branches without trust prompts or arbitrary code execution. The
npm:
backend no longer needs node installed, and skopeo, crane and gpg are replaced with built-in implementations.
2026.7.13
lets
rename_exe
map several executables out of a single archive instead of one, adds shell completions for Homebrew casks, and reads tool versions from
go.mod
.
Conan 2.31.0
moves the Workspace feature out of incubating, adds regex support to
replace_in_file
, and lets a
conanws.py
define workspace member versions dynamically via a new
get_ref(folder)
method.
2.31.1
fixes a false “pattern not found” error when a replacement leaves the file unchanged.
vcpkg 2026-07-24
switches dependency snapshots to canonical vcpkg PURLs and adds Git tree gitoids to its SPDX SBOMs.
Also out:
Homebrew 6.0.12
,
Deno 2.9.4
,
Podman 6.0.2
,
snapd 2.76.3
,
Cabal 3.18.1.0
,
pipx 1.16.2
,
winget 1.30.70-preview
,
sbt 2.0.3
,
pnpm 11.15.1
,
pnpm 12.0.0-alpha.21
,
Renovate 43.280.4
,
Dependabot Core 0.388.0
.
Security
RubyGems.org disclosed
a CDN caching bug that could serve one account’s legacy API key to another user signing in through the same edge node for up to an hour. It affects sign-ins from gem clients older than v3.2.0, still 18% of
gem signin
traffic, and for the first several years of the bug that was every client. All legacy keys were revoked on 23 July; scoped and OIDC keys were unaffected.
PyPI now rejects new files uploaded to releases older than 14 days
, so a compromised publishing token can no longer add files to a long-stable release. Of the top 15,000 packages, only 56 had added Python 3.14 wheels to an existing release more than 14 days after it shipped; formal semantics for closed releases are planned for the Upload 2.0 API.
Articles
Securing our GitHub Actions workflows with zizmor
(Packagist blog) continues their supply-chain security series: every action pinned to a commit SHA, token permissions cut to read-only, and
pull_request_target
workflows removed across the Composer and Packagist repositories.
Who’s responsible for bug reports on old software versions?
(Nate Graham) argues that distributors shipping frozen versions carry the support burden for those versions, and that a high-quality discrete-release OS is more work than a competent rolling release, not less.
Guix: creating a package from a binary
(Aloys Berger) walks through packaging the Caddy binary in Guix as a stopgap, because a from-source build would require packaging a dozen Go dependencies first.
Elsewhere
EuroPython 2026 ran in Kraków last week with a full-day
Packaging Summit
hosted by Jannis Leidel. Packaging-track talks included
Demystifying CRA for the community
(Anwesha Das) on the first wave of Cyber Resilience Act obligations landing in September,
Should you trust Trusted Publishing?
(Nikita Karamov) reviewing three years of PyPI’s OIDC-based publishing, and
Binary Dependencies: Identifying the Hidden Packages We All Depend On
(Vlad-Stefan Harbuz) on the compiled dependencies that manifests like
pyproject.toml
don’t record.
CHRONO-RESOLUTION
(arXiv) is a dataset of dependency-resolution results computed at each package’s release point across npm, PyPI and crates.io, for research that needs the historical dependency graph rather than today’s.
Scrutineer
, the Alpha-Omega scanner mentioned in
last week’s Rust Foundation post
, is
now in Homebrew
.
git-pkgs
I tagged
git-pkgs v0.18.1
,
enrichment v0.6.3
,
registries v0.6.3
,
vulns v0.2.1
and
purl v0.1.15
.
Send links for next week to
@
[email protected]
.
