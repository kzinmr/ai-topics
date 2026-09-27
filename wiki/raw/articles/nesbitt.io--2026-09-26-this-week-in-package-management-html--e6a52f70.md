---
title: "This Week in Package Management: 26 September 2026"
url: "https://nesbitt.io/2026/09/26/this-week-in-package-management.html"
fetched_at: 2026-09-27T10:01:13.420076+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 26 September 2026

Source: https://nesbitt.io/2026/09/26/this-week-in-package-management.html

Week nineteen of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Releases
pnpm 12.6
adds an
autoDedupe
setting that resolves compatible dependency versions to a single one during install, and
pnpm add --save-types
for the matching
@types/*
package.
12.7
has the global node shim read
.nvmrc
and
.node-version
when
devEngines.runtime
is unset, and adds
pnpm publish --publish-wait-timeout
to block until a published package is available before dependents publish.
RubyGems 4.1.0.beta1
adds content-addressable gems, an opt-in OS credential store for gem and Bundler credentials, ML-DSA post-quantum signatures for the signed-gem workflow, and a
--cooldown
flag on
gem install
,
update
and
outdated
.
npm 12.1.0
supports
read-write-stage-only
granular access tokens for staged publishing, and
npm stage
reports the status of packages held in staging. A
--provenance-file
argument now takes precedence over OIDC-generated provenance.
Poetry 2.5.0
adds an
installer.builtin-uninstall
setting that removes packages itself instead of calling pip, supports Python 3.15, and stops sending credentials configured for an HTTPS repository over plain HTTP.
2.5.1
fixes a
TypeError
in the new uninstaller.
Terraform 1.17.0-beta2
allows variables and locals in provider requirements and adds a
-minimal-refresh
planning option that only refreshes resources with proposed changes. Terraform Policy is now generally available and no longer requires the experimental-features flag.
Windows Package Manager 1.29.380
adds an experimental source priority setting: sources can be assigned a numeric priority via
winget source add
or
source edit
and are ordered by it in results.
mise 2026.9.14
lets registry entries require a verified GitHub attestation before a tool installs, and fetches release metadata for any public GitHub repo from mise-versions rather than the GitHub API.
Also out:
Security
The Rust security response WG
reported
that Miri wrote every environment variable to
target/
, so caching that directory in GitHub Actions could expose job secrets to pull requests that read from the cache. The nightly dated 2026-09-22 restricts persisted variables to
CARGO_*
(excluding
CARGO_*_TOKEN
) and
OUT_DIR
; the post recommends clearing existing caches and rotating any secrets that were in scope.
uv 0.12.18
fixes
GHSA-2cv4-cqwr-gwf7
, a path traversal during wheel installation on Windows. It also adds
--check
and
--output-format json
to
uv pip install
and
uv pip sync
, so planned changes can be reported while leaving the environment unchanged.
Flatpak 1.18.3
updates its vendored bubblewrap to 0.12.0 for
CVE-2026-87766
, where sandbox setup could follow a parent symlink through
/oldroot
to write files on the host, and its vendored xdg-dbus-proxy to 0.1.8 for
CVE-2026-93676
, where D-Bus broadcast filtering ignored the configured path, interface and member restrictions.
Elsewhere
The Rust project
announced
Scott Schafer as a full-time Maintainer in Residence for the Cargo team, funded through the Rust Foundation Maintainers Fund with additional money from the Rust Leadership Council’s Project Priorities budget and AWS. Separately the Rust Foundation
added
CodSpeed, Haevek and Perplexity as Silver members and the Software Stewardship Lab as an Associate member.
Jamie Tanna
reviewed
his first year as Renovate project lead: 1,813 releases, managers up from 110 to 118, datasources from 76 to 82, and external commits up 48% in the first half of 2026. Discussion-forum help requests fell 43% over the same period as users turned to LLM tools instead.
Josh Bressers
interviewed
Daniel Stenberg and Stefan Eissing about curl’s month-long pause on accepting vulnerability reports and the volume of AI-generated submissions that prompted it.
Farid Zakaria
wrote up omnibin
, a FUSE filesystem that presents every binary nixpkgs has shipped since 2013, 881,933 in total, by looking up store paths in Hydra’s published metadata and fetching them on first access; a cold
[email protected]
start takes about 2.7 seconds.
TrustBOM: A Scalable Architecture for Confidentiality-Preserving SBOMs Across Organizations
(Nguyen et al., arXiv) proposes a CI/CD-integrated attestation scheme in which a supplier proves that a given vulnerability or restricted licence is absent from its software while keeping the dependency graph private.
Git 2.56.0-rc2
was tagged.
git-pkgs
I tagged eight repos this week:
citation v0.1.0
(new), a pure-Go library for parsing and validating
CITATION.cff
files that preserves source positions, unknown fields and numeric spelling
scan v0.1.0
(new), a pure-Go library that matches many regular expressions against byte blocks by compiling patterns into shared literal filters and regex automata along Hyperscan lines
secrets v0.1.0
(new), which scans Git history for leaked credentials by running the Betterleaks rule corpus over every blob and attributing findings to the commits and paths that introduced them
spam v0.1.0
(new), an offline library for measuring promotional text in package manifests and READMEs
archives v0.8.0
clone v0.7.4
history v0.1.1
roles v0.1.1
Send links for next week to
@
[email protected]
.
