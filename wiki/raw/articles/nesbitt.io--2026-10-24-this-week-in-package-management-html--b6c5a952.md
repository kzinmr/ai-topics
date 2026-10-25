---
title: "This Week in Package Management: 24 October 2026"
url: "https://nesbitt.io/2026/10/24/this-week-in-package-management.html"
fetched_at: 2026-10-25T10:01:22.618459+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 24 October 2026

Source: https://nesbitt.io/2026/10/24/this-week-in-package-management.html

This week’s package management news, and what a week it’s been, gathered from the
package manager OPML feed collection
, my posts and boosts on
Mastodon
, and anything people sent me.
The compromised eMudhra intermediate CAs led to security releases from dozens of package managers, language runtimes and CA bundles this week.
Security
eMudhra generated eight of its intermediate CA certificates in a way that lets anyone
recover their private keys
. Browsers blocked them through their revocation lists, and tools that bundle their own copy of the roots shipped new releases. I wrote about where those copies end up, and how many critical packages bundle a CA file, in
Trust Stores Are Dependencies Too
. The disclosure page keeps
a table of patched software
with version numbers, including ca-certificates updates for most Linux distributions and the BSDs. The package management releases with the fix:
uv 0.13.4
updates the roots compiled into uv, and
0.13.5
updates the managed CPython builds so their pip and
ensurepip
carry certifi 2026.10.19
pip 26.2.2
Seth Larson’s
notice for Python users
lists the minimum versions of certifi, pip, uv, sigstore, conda and pixi, and gives a hash-pinned command for upgrading pip from an affected environment
conda 26.9.4
requires the updated certifi and ca-certificates, and the conda blog has
update instructions for conda, Mamba and Pixi
pixi 0.82.1
rustup 1.29.2
Root bundles that other packages vendor:
certifi 2026.10.19
,
webpki-roots and webpki-root-certs 1.0.10
,
rustls-webpki 0.103.16
,
Elixir castore 1.0.22
,
Erlang certifi 2.18.0
,
Perl Mozilla::CA 20261020
,
Composer ca-bundle 1.6.0 and 1.4.16
and the
curl CA bundle
Homebrew’s ca-certificates formula
Python 3.15.1, 3.14.9 and 3.13.17
Java 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.33 and 8u511
for OpenJDK and Oracle JDK
Go 1.27.3 and 1.26.10
Node.js 26.12.1, 24.22.1 and 22.23.4
update the bundled root certificates to NSS 3.131.1 and fix ten CVEs, four of them rated high, including a Brotli decoder out-of-bounds write that can lead to remote code execution
Hex 2.5.4
removes three emSign roots from its bundled CA list
Composer 2.11.0-RC1
rejects the intermediates even when the system CA store includes their roots
Deno 2.9.8
and
Bun 1.4.4
mise 2026.10.17
pypa/gh-action-pypi-publish 1.14.3
pnpm 11.28.8
embeds Node.js 26.12.1 in the standalone
@pnpm/exe
builds
Verdaccio 6.10.7
for its Docker image
Docker Engine 29.9.2
and
Docker Desktop 4.96.2
Git for Windows 2.56.0.3
OpenTofu 1.13.2
and
1.12.9
Terraform 1.16.7
For software already installed, EasyBuild maintainers published
a script that scans for and removes the untrusted roots
from EasyBuild installations. An option scans every
.pem
and
.crt
file under a given path.
Michał Górny
listed the places
a Python user has to upgrade:
certifi in every virtual environment and lockfile, with certifi excluded from dependency cooldowns
the certifi bundled in pip
the pip wheel that ships with Python for
ensurepip
Rust tools such as uv that compile in their own copy of the roots
Gentoo’s certifi package uses the system certificates, its pip package uses that certifi, and its Python uses a system
ensurepip
wheel. Upgrading those packages updates the system install.
PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35
(PHP Foundation) fix two remote code execution bugs in memory management and error handling. One can be triggered by an unauthenticated request on Apache with mod_php before any application code runs. The post explains that the root cause of the out-of-memory bug was first spotted during the 2024 Quarkslab audit, and the fix stalled for months while the security team weighed competing approaches. The CVE IDs leaked on 20 October, so the release moved forward a day. Chainguard broke the embargo, publishing images containing the fix more than six hours before the coordinated release. Special thanks to
Volker Dusch
, who leads the PHP Foundation’s Ecosystem Security Team, for his work behind the scenes on this release.
In
the project’s second compromise this year
,
LiteLLM 1.107.0
(Socket) was published to PyPI and GHCR with
.pth
and
sitecustomize.py
startup files that collect cloud credentials, SSH keys and coding agent auth files on every Python startup, including programs that never import LiteLLM. The container image’s build provenance records the source repository as
Berri-AI/litellm
, one hyphen away from the real
BerriAI/litellm
, and the payload files are absent from the release tag in the real repository. LiteLLM’s maintainers told Help Net Security that the attacker used what appear to be stolen GitHub CLI OAuth tokens for three engineers’ accounts. The attacker changed the release pipeline and triggered the release from the first, approved it from the second, and deleted the workflow records from the third.
Bloom Security found that
npm’s Trusted Publishing matched configurations on the
owner/repo
name
instead of the permanent numeric IDs GitHub includes in the OIDC token. After a maintainer renamed or deleted the bound repository, anyone could register the freed name and publish new versions of the package, with a valid provenance attestation naming their own repository, an exposure Bloom counted across more than 1,500 packages. GitHub’s fix,
announced on 2 October
, expires any configuration that goes 48 hours without validation. According to npm’s documentation, the first publish binds a configuration to the repository’s immutable identity.
Ruby 4.0.9, 3.4.12 and 3.3.13
fix bugs in the Onigmo regular expression engine that GitLab turned into remote code execution through user-supplied patterns, such as those in CI configuration. GitLab had already patched the Ruby it ships and assigned four CVEs. The bugs affect applications that pass attacker-controlled strings to
Regexp.new
or interpolate them into a regexp literal, and they remain exploitable with
Regexp.timeout
and pattern length limits in place. The four CVEs are GitLab’s, and the Ruby core team plans to discuss whether compiling untrusted patterns is a supported use case.
GitHub package firewall
is in public preview for GitHub Enterprise Cloud. It is a proxy between the upstream registry and CI runners, coding agents or internal registries. It checks metadata requests and downloads against an enterprise policy covering cooldown periods, malware and vulnerability advisories, and attestation downgrades. It supports npm only for now, and is free during the preview.
The curl project will
make LOW and MEDIUM severity vulnerability reports public
on the GitHub issue tracker from 26 October, keeping embargoes only for HIGH and CRITICAL issues. Daniel Stenberg wrote that the project received 13 vulnerability reports on a single Saturday, more than the small security team can handle in private.
Releases
Hex 2.6
adds Workload Identity, so a GitHub Actions job can publish a package or fetch an organisation’s private packages with its OIDC token instead of a stored key. Package builds are now reproducible, and the
build_env
metadata field records the Hex version needed to rebuild one and compare checksums. Policy overrides can accept a single advisory, retirement reason or the cooldown,
mix hex.audit --policy
applies the policy to packages already in
mix.lock
, and
mix hex.audit
can write SARIF for GitHub code scanning. Hex has dropped stored keys for organisation repositories. In CI,
mix hex.organization auth ORGANIZATION --key KEY
exchanges the key for a token that lasts about 25 minutes. Organisation admins can now require two-factor authentication for every member.
Composer 2.11.0-RC1
adds a
cooldown
policy that withholds newly released versions for a configurable period, and a
block-scope
option so custom policies can also block during
install
. It now escapes package-controlled paths and shebangs embedded in bin proxies, and stops sending custom repository headers to dist URLs on other hosts whose names start with the repository host. It also removes the
source-fallback
option added in 2.10.
pnpm 12.15
adds
lockfile.integrityTarget: tar
, which pins the hash of each package’s uncompressed tar so the lockfile stays the same when a registry recompresses tarballs. It accepts zstd-compressed registry responses and lets
pnpm-workspace.yaml
load settings from other files and from config dependencies through an
include
field.
pnpm install
now fails with
ERR_PNPM_REGISTRY_NAME_MISMATCH
when a registry returns metadata for a different package than the one requested. Before, pnpm installed it under the name in the metadata, which bypassed
allowBuilds
rules for the requested name.
mise 2026.10.13 to 2026.10.18
ignores
[settings]
from untrusted project configs as of
2026.10.13
, so a cloned repository’s
mise.toml
changes settings like
node.mirror_url
only after
mise trust
.
2026.10.15
applies the default 24-hour
minimum_release_age
to every backend, including asdf, vfox, conda and
http:
tools, and 2026.10.18 adds
mise lsp
, a language server for
mise.toml
.
vlt 1.5
adds
vlt skills
, which links the agent skills that installed dependencies ship into
.agents/skills
and
.claude/skills
. An
allow-skills
query in
vlt.json
selects which packages’ skills get linked, and the default
:not(:malware)
query also excludes packages still waiting for a Socket scan.
vlt 1.6
adds
--global
installs and parses
^0
,
^0.x
and
^0.0
as ranges instead of the exact version 0.0.0.
Bun 1.4.4
migrates Yarn Berry lockfiles to
bun.lock
with every pinned version preserved.
bun install
now retries with exponential backoff, where 1.4.3 ran all five retries within 5 ms, and the release closes 133
bun install
issues.
uv 0.13.2 to 0.13.5
removes exponential work when simplifying and exporting complex dependency markers and reduces resolver memory use for large graphs.
pylock.toml
exports now include supported environment restrictions, and the
wheel-variants
preview fetches and validates PEP 825 index-level variant metadata.
pixi 0.83
adds support for virtual package detectors, which channels will be able to register for virtual packages beyond pixi’s built-in set. pixi prompts for confirmation before running a detector and lists detectors in
pixi info
.
Mamba 2.10
removes its TUF implementation and
mamba-content-trust
and completes the
exclude_newer
policy. It also fixes authentication tokens being dropped on package downloads since 2.9.0.
Athens 0.20
proxies and caches Go toolchain downloads from go.dev/dl under
/dl/
, and serves cached
@latest
results in offline and fallback modes.
Terraform 1.17
supports variables and locals in provider requirements and makes Terraform Policy generally available, with a
-policies
flag for
plan
,
apply
and
query
.
Dependabot now supports npm 12, pnpm 11 and 12, and Bun 1.4
. When pnpm 12 writes
pnpm-lock.yaml
as two YAML documents, the dependency graph misses those dependencies for now, so Dependabot skips alerts and security updates for them and may close existing alerts. Alert responses in the REST API now include a
version_requirement
field
with the version Dependabot recorded.
Also out:
Papers
Sign Here: Attributing a Source for a More Trustworthy Software Supply Chain
(Derek Garcia et al., arXiv) tests whether building only packages that link to a buildable source repository would keep malware out. Across 47,066 known malicious npm and PyPI packages, checking for a source blocked between 87.7% and 99.9% of them depending on how strictly the source was vetted, while 47.4% of a sample of benign packages pointed to a source a user could build from.
Vibenix: Agentic Software Packaging and Maintenance with Nix
(Martim Monis et al., arXiv) is an LLM agent that writes Nix packaging expressions through a build-and-repair loop. It produced buildable packages for 95.3% of 466 tasks with Claude Haiku 4.5, against 5.6% for a single-shot tool, though manual checks found only 47% of a sample worked correctly before a refinement step added 35 percentage points.
What Is Under the Hood? A Cross-Ecosystem Study of Vulnerable Dependencies in Construction Software
(Mahzabin Tamanna et al., arXiv) ran OSV-Scanner over 904 construction-industry GitHub repositories. OSV-Scanner could scan 54.6% of them, and 80% of those had at least one dependency with a published advisory. Two upstream package families reached about 70% of the affected repositories.
Elsewhere
Sentry gave $1,000,000 to open source maintainers
(Vlad Miricioiu, Sentry) this year, up from $750,000. $495,000 went through thanks.dev and $100,000 through ecosyste.ms Funds, which I run, with the rest to foundations including the PSF, PHP Foundation, Ruby Central and Packagist. The Open Source Pledge’s 37 member companies have now paid $8,421,535 to maintainers and foundations.
Farid Zakaria’s
One store, two frontends
uses
$ORIGIN
support in
PT_INTERP
, which he worked on with Christian Brauner for Linux 7.3, to make nixpkgs outputs relocatable so Bazel and buck2 remote executors can use them without Nix installed. In
No quarter for gaps
he writes gemlock.nix, a Nix side for Bundler lockfiles with platform-specific gems. The bundix pull request that the nixpkgs manual points to for this was opened in 2019 and closed unmerged in August.
Who wrote this byte?
adds
rewind blame
to Rewind VM, his deterministic virtual machine for recording and replaying builds. Given two runs with different outputs,
rewind blame
reports the process that wrote the first differing byte.
Paul Battley has
archived the repositories of all his Ruby gems
and linked them to a post explaining why he has stopped working on them.
GitRoot 0.5.0
replaces plugin download URLs with Package URLs, a breaking change for existing forge configurations.
zizmor 1.32.0-rc1
adds experimental support for GitHub Actions workflow lockfiles, and William Woodruff
is asking for testers
with repositories that already use one.
Josh Bressers talks to CyberScoop’s Safe Mode podcast about
running VulnCheck’s coordinated disclosure
as AI-generated reports increase. He also covers how much less effort it now takes to find vulnerabilities than to fix them.
git-pkgs
I tagged 10 repos this week:
Send links for next week to
@
[email protected]
.
