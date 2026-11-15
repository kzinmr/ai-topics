---
title: "This Week in Package Management: 14 November 2026"
url: "https://nesbitt.io/2026/11/14/this-week-in-package-management.html"
fetched_at: 2026-11-15T10:00:55.897353+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 14 November 2026

Source: https://nesbitt.io/2026/11/14/this-week-in-package-management.html

This week’s package management news, gathered from the
package manager OPML feed collection
, my posts and boosts on
Mastodon
, and anything people sent me. Version control and forge news is in the Wednesday
This Week in Source Control
roundup.
Security
Composer 2.11.2
fixes seven security bugs, two of them reachable through a crafted
composer.lock
or
vendor/composer/installed.json
. Those are arbitrary command execution through the
prevent_url_access_callable
transport option (
GHSA-jhfp-4ppm-crmm
) and inline repository HTTP credentials sent to dist mirrors on other hosts (
GHSA-x82q-x274-r6pq
).
A malicious zip could also write outside the package directory through symlinked entries when extraction fell back from
unzip
to
ZipArchive
(
GHSA-w6hj-6587-3jh5
).
Composer 2.2.32
backports the zip and credential fixes to the LTS branch. 2.11.2 also adds an
exclude-branches
option for VCS repositories and aborts downloads that stall for 30 seconds.
Podman 6.2.0
and
5.8.10
fix three CVEs, one of which let untrusted image labels make
podman auto-update
restart the wrong systemd units (
GHSA-55rm-rwr7-q2wr
). The other two are a digest and signature validation bypass for malicious images (
GHSA-pggw-qqjf-6cxw
) and a bypass of the socket deny rule in the default seccomp profile. 6.2.0 also adds
podman push --platform
, which pushes one platform’s manifest instead of the whole list.
pnpm 11.28.12
makes a
${VAR}
placeholder in a registry URL in
pnpm-workspace.yaml
or the project
.npmrc
fail the command. pnpm does not expand environment variables in those files, and earlier versions skipped such a URL and resolved packages from another registry, such as npmjs.org.
From 8 December, GitHub
will turn off Dependabot alerts
on most repositories whose last activity is more than a year old. Activity means a push to any branch or tag, creating the repository, or turning alerts on. Existing alerts are archived, and any push restores them and restarts the one-year period. Repositories under an enforced security configuration that enables Dependabot alerts are exempt.
Releases
Rust 1.100.0
stabilises Cargo’s
min-publish-age
: setting
global-min-publish-age = "3 days"
under
[registry]
in
.cargo/config.toml
makes the resolver skip versions published more recently than that, and
cargo update
lists what it held back. Versions missing a
pubtime
in the index are always eligible, and
cargo install
resolves without the setting.
Cargo also now warns about unused dependencies, as part of a new linting system configured through the
[lints.cargo]
table. The warning appears only when every build target that could use the dependency is built, and it skips
dev-dependencies
.
pnpm 12.19.0
adds
pnpm fund
and an experimental
lockfile.format: v13
setting. The new format writes
pnpm-lock.yaml
in a JSON-like syntax that is still valid YAML, with one entry per package version, so updating a peer dependency changes only the lines that record its version.
12.21.0
lets
pnpm store add
prepare tarball and git dependencies for offline installs.
vlt 1.7.0
adds
vlt deploy
and
vlt update <pkg>
and locks git dependencies to a commit, and
1.8.0
installs from vlt’s public npm mirror with no setup and resolves unprefixed dependencies from the project’s own registry configuration.
mise 2026.11.4
(now
2026.11.8
) accepts
zip::
archives over HTTP or HTTPS for config and task includes. The contents behind the URL can change between fetches, and paranoid mode rejects zip config includes. From 2026.11.6,
[bootstrap.packages]
keys without a
manager:
prefix install through the first available system package manager, and the npm backend can install from an HTTPS tarball URL.
uv 0.13.8
extends the wheel variants preview to local paths, direct URLs and Git repositories, and detects x86-64 microarchitecture levels when selecting a variant. Plaintext credential files on Unix are now restricted to owner-only permissions.
Homebrew 7.0.13
adds a
pin: true
Brewfile option and prefetches bottle attestations in bulk. All official casks now require a
zap
stanza.
Harbor 2.16.0
replaces Redis with Valkey as the cache backend and ships images for arm64 as well as amd64. Proxy cache projects can now pass OCI referrers API requests to the upstream registry and merge the results with local ones.
Renovate 44.228.0 to 44.239.1
adds a
gemspec
manager that updates dependency constraints in
*.gemspec
files, and the
swift
manager now updates
.package(id:)
dependencies from Swift package registries. With the experimental
minimumReleaseAgePackageManagerSync
option, Renovate reads the release age configured for pnpm, Yarn, Cargo and Poetry and runs each tool with the longer of that and its own
minimumReleaseAge
, and npm’s
min-release-age
in
.npmrc
is read too.
renovate-config-validator --migrate
now writes out a migrated config file for configs that use old option names.
Also out:
Articles
Artifact integrity for Packagist and Composer
(Packagist blog) announces Alpha-Omega funding for Packagist.org to store package artifacts itself. Today it hosts only metadata, and more than 99% of versions point at a zip that GitHub generates on demand from the git repository. Those archives differ between GitHub servers and can change over time, so most packages have an empty checksum field. The funded work has five phases:
Permanent artifact storage, with checksums in the package metadata and the transparency log
A Sigstore signature and build provenance attestation for every stored artifact, verified by Composer
API tokens limited to specific packages and permissions, with expiry and automatic revocation when leaked
Trusted Publishing from CI workflows through OIDC
Artifact uploads and a
composer publish
command, with staged releases approved by hardware key
Uploads and Trusted Publishing will ship only together with mandatory signing and attestations. Stored artifacts also make it possible to publish several packages from one repository, which today requires splitting a monorepo into read-only mirrors.
Lock your GitHub Actions
(Hugo van Kemenade) shows how to adopt GitHub’s workflow lockfiles. The
gh actions-lock
extension rewrites SHA-pinned
uses:
lines back to version tags and records each tag’s commit, owner ID and repository ID in
.github/workflows/actions.lock
. Renovate and Dependabot both update the lockfile, and a CI job running
gh actions-lock --verify
fails when the lockfile is out of sync with the workflows.
Farid Zakaria has two posts on running builds inside Rewind, the deterministic virtual machine he is building.
Making profile-guided optimization reproducible
starts from Nixpkgs disabling profile-guided builds of Python and GCC because the training run varies between builds.
What if every Nix build were bit-reproducible?
wraps derivations in the VM so that content-addressed builds produce the same store path on every machine, with the VM version as a build input.
Bringing v1 recipes to conda-build
(conda blog) explains how conda-build now builds
recipe.yaml
recipes by dispatching to the Python bindings for the rattler-build crates. The existing
build
,
render
and
debug
subcommands handle both formats, and options unsupported on the v1 path raise an error. Maintainers with large collections of
meta.yaml
recipes can move them to the v1 format and keep their existing conda-build pipelines.
Swift’s
November news digest
opens with a reminder from Dave Verwer that CocoaPods stops accepting new pods and pod versions on 2 December 2026. Current pods and versions will still be served, read-only, so the change does not immediately break builds. Verwer also writes that he is now part of a team at Apple working on a public, cross-platform package registry for Swift.
python-sbom
(Bernát Gábor) is a build plugin that writes a CycloneDX 1.6 SBOM into every wheel under
.dist-info/sboms/
, the directory defined for SBOMs in the
installed packages specification
. It has plugins for hatchling, pdm-backend and setuptools and a wrapper backend for other build backends. The SBOM records the source commit, the interpreter, the build tools and any wheels the project bundles as data files.
Alpha-Omega published
a case study
of the PHP2Shell response. Volker Dusch, the PHP Foundation’s Security Engineer in Residence, coordinated with researchers, Linux distributions and WAF vendors while the core engineers wrote the fixes. PHP’s security team received more than 200 reports in the week after disclosure, many of them duplicates, and built TAMIS, which compares incoming reports against existing ones several times a day.
Reproducible Builds in October 2026
reports that GNU tar embeds its process ID in the member path when it writes a sparse file to a PAX archive, so identical inputs produce a different archive on each run. Robin Candau and Bernhard M. Wiedemann have also revived a shared repository of reproducibility patches, which currently holds patches from openSUSE and Arch Linux.
Elsewhere
I am tired
(Kushal Das) describes finding more than 90 vulnerabilities since July in open source projects, many of them written or used by Sunet, with LLM help and 16-hour days. Das writes that most maintainers and defenders of that infrastructure have neither the model access nor the hardware to do the same.
Dawn Foster published the video and slides of her Community Over Code talk,
Good Governance for Sustainable Open Source Projects
, with links to her five-part series on the same topics.
Anil Madhavapeddy
is using
brief
, which I wrote, to detect the languages and toolchains in a repository for automatic CI in his Tangled spindle.
An Empirical Study of Observability Limits in Advanced Software Supply Chain Attacks
(Zhuoran Tan et al., CCS) introduces SynthChain, a runtime telemetry dataset built from seven attack scenarios across PyPI, npm and C++ supply chains. The best single telemetry source recovers fewer than 40% of the expected attack steps. Combining two complementary sources improves reconstruction by roughly 1.6 times.
git-pkgs
I tagged 7 repos this week:
Send links for next week to
@
[email protected]
.
