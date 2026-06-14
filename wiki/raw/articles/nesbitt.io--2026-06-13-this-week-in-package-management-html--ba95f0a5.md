---
title: "This Week in Package Management: 13 June 2026"
url: "https://nesbitt.io/2026/06/13/this-week-in-package-management.html"
fetched_at: 2026-06-14T07:00:54.255886+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 13 June 2026

Source: https://nesbitt.io/2026/06/13/this-week-in-package-management.html

Week four of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Security
GitHub announced the
breaking changes coming in npm v12
, estimated for July.
npm install
will stop running dependency lifecycle scripts unless they’re allowed via the
allowScripts
field that
11.16.0 introduced
in advisory mode, covered in the
install-script allowlists post
I wrote last week. Implicit
node-gyp
builds are blocked too, so a package with a
binding.gyp
and no install script needs approval like any other. Git dependencies and remote URL tarballs also stop resolving by default, each behind a new
--allow-git
/
--allow-remote
flag. Everything ships behind warnings in npm 11.16.0+ today.
uv audit
is a new preview command that scans Python dependencies for known vulnerabilities and adverse project statuses like deprecation, a uv-native alternative to pip-audit. The same announcement covers an experimental malware check:
uv add
and
uv sync
can look up previously-resolved packages against OSV on every sync, behind
UV_MALWARE_CHECK=1
.
pnpm 11.5.3
, backported to
10.34.2
, hardens the
packageManager
bootstrap path. The registry and proxy settings used to download a requested pnpm version now come only from trusted config sources, not the repository’s own
.npmrc
, and the downloaded binary’s npm registry signature is verified before it runs, failing closed. Repository-controlled config can no longer expand environment variables into registry URLs or credential values, and Node.js downloads get their
SHASUMS256.txt
checked against the release team’s PGP keys instead of trusting the configured mirror to vouch for itself. A
follow-up post
walks through the malicious-repository scenario the env-variable change blocks.
Composer plugin allowlists
are now available at the organization level for Private Packagist customers, the next post in Packagist’s supply-chain security series. Composer plugins run code during install and update, and the existing per-developer trust prompt is easy to clear without thinking, or to clear from a coding agent on autopilot.
The
Arch User Repository package alvr
was orphaned and immediately adopted by a threat actor who pushed an update carrying an infostealer payload. The
aur-general thread
tracks the takeover and the orphan-adoption mechanic that enabled it.
Podman 5.8.3
fixes
CVE-2026-44517
, where a Dockerfile
ADD
or
COPY
pulling from a malicious git repository or tar archive could write files outside the build context.
Ruby Central announced a
Security Engineers in Residence programme
, funded by an Alpha-Omega grant, to find and verify vulnerabilities in widely-used gems before reporting them to maintainers, following the model the Python, Rust and PHP foundations already run. I’m advising the team on package ecosystem security. The first engagement turned up a ReDoS in Nokogiri’s CSS query tokenizer, verified and fixed before disclosure.
Releases
RubyGems and Bundler 4.0.14
follow up on last week’s Cooldown feature: Bundler now preserves per-source cooldown settings when converging sources from the lockfile and stops excluding the locked version from cooldown during
bundle update
. On the RubyGems side, the gem installer validates executables and bindir, and C1 control characters are stripped from displayed gem text.
gem.coop namespaces
moved from beta to general availability, so a Gemfile can point at a per-publisher source like
https://gem.coop/@kaspth
. Cooldown support was added to every namespace via a
/cooldown
suffix, though that part stays on the beta domain while bugs get fixed.
npm 11.17.0
adds a
min-release-age-exclude
config to exempt named packages from the release-age gate. The
allowScripts
policy now applies across
prune
,
dedupe
,
uninstall
,
audit
and
link
, and a prototype-pollution path in the config Queryable setter is closed.
Dependabot Core 0.381.0
adds Bundler 4 support and disables the npm minimal-age gate for Yarn Berry security updates, the same cooldown-bypass-for-security-fixes pattern it applied to pnpm last week. Go module updates now respect
GONOPROXY
and
GONOSUMDB
.
mise 2026.6.3
adds excludes to its minimum release age setting so a cooldown policy can carve out specific tools, plus an opt-in
auto_env
that activates platform-aware config and lockfiles by detected OS and architecture.
2026.6.5
closes trust-bypass paths where an untrusted project’s
mise.toml
or
mise-tasks/
directory could run code before the user approved it, and makes
credential_command
global-only so a checked-out repo can’t run arbitrary shell through it.
Flatpak 1.18.0
exposes AMD’s compute interface (
/dev/kfd
) through the DRI device permission, prints failure causes in
flatpak update
output, and speeds up fish shell integration at startup.
Homebrew 6.0.0
adds a tap trust mechanism that requires explicit approval before a third-party tap’s Ruby runs on the machine. The release also ships a smaller default internal JSON API, sandboxing on Linux, and parallel formula installs from
brew bundle
. Three
security advisories
are addressed in the same release: an HTTPS-to-HTTP redirect bypass in the POST download strategy, root code execution via Git hooks in a macOS pkg postinstall, and the macOS installer trusting user-controlled plist files.
brew bundle
also adds npm, krew and winget support and now prompts before removing packages on cleanup. A
PR I sent
adds a
patches
key to
brew info --json
and the formulae.brew.sh API, so SBOM generators and vulnerability tools can see which patches each formula applies on top of upstream.
Deno 2.8.3
accepts
--env-file
in the
dependency
and
registry
subcommands, and suggests
DENO_TLS_CA_STORE
when a fetch hits an untrusted certificate.
Also out:
pixi 0.70.2
,
Mamba 2.8.1
,
uv 0.11.21
,
Chocolatey 2.7.3
,
sbt 2.0.0-RC16
,
Gradle 9.6.0-RC2
,
Conan 2.29.1
,
Helm 4.2.1
,
Helm 3.21.1
,
pnpm 11.6.0
,
Homebrew 6.0.1
,
Windows Package Manager 1.29.250
,
Docker Engine 29.6.0-rc.1
,
Podman 6.0.0-RC1
,
Verdaccio 7.0.0-next-7.21
,
Renovate 43.220.0
.
Articles
What We’re No Longer Seeing: AI and the Invisible Newcomer in Open Source
(Mara Averick, stdlib blog) argues that the friction of a newcomer’s first clumsy issue or pull request is how communities spot and welcome new contributors, and that AI assistance now smooths that friction away before anyone sees it.
We have to change the rules of security
(Josh Bressers) makes the case for deliberately choosing what security work to stop doing, rather than letting tasks fall through the cracks at random.
A Strategic Approach to Demonstrating the Value of OSS Efforts
(Dawn Foster) collects a year of her writing and talks on showing leadership the value of open source work in one place.
The Guix Nix Abomination: Leveraging Guix derivations in Nix
(Farid Zakaria) registers a Guix derivation in a Nix store and has Nix build it, showing the two tools share the same derivation machinery underneath the rivalry.
Nix flakes vs Guix
works through why there’s no single Guix equivalent of a flake: flakes bundle several concerns into one feature, where Guix covers the same ground with separate composable tools.
Are insecure code completions a vulnerability?
(Seth Larson) catches PyCharm’s line completion suggesting
CERT_NONE
and warning-suppression boilerplate, and argues a CVE is the wrong mechanism for systematically insecure suggestions, though vendors should still fix them at the source.
Helm v3 end-of-life
sets 9 September 2026 as the final feature release, limited to Kubernetes client library updates, and February 2027 as the cutoff for security patches. Existing Helm 3 releases can be managed by Helm 4 without chart rewrites.
Reuse Less Software
(Simon Heath) argues for vendoring every dependency into your own repository as a supply-chain firebreak, on the principle that the auto-fetch step is what lets a poisoned release propagate at CI speed and that giving up transitive dedup is a price worth paying for the break.
Papers
When LLMs Invent Rust Crates: An Empirical Study of Hallucination Patterns and Mitigation
(Zheng et al., arXiv) is the first large-scale study of crate hallucination in LLM-generated Rust code, building its dataset from Stack Overflow and GitHub tasks rather than the Python and JavaScript ecosystems earlier package-hallucination work measured.
Skilldex: A Package Manager and Registry for Agent Skill Packages with Hierarchical Scope-Based Distribution
(Saha et al., arXiv) proposes a package manager and registry design for distributing agent skills with scoped namespaces.
Elsewhere
Inside PyPI: Maria Ashna on Supporting Python’s Package Index
is a Behind the Commit interview about the day-to-day work of running PyPI.
Fixing Fedora’s Packaging Pipeline
is a Fedora Podcast episode with Jakub Kadlčík of the Copr build service on RPM packaging tooling.
The impact of AI on open source software development
is a panel Mike McQuaid put together with five open source practitioners on what AI assistance changes for the communities and projects underneath the tooling.
Sustain episode 289
has Courtney Miller on software abandonment, maintainer burnout, and what AI tooling changes for project sustainability.
Two versioning schemes:
PaceVer
versions user-facing apps as
MARKETING.NATIVE.OTA
, bumping by which channel a release ships through, the slow store-reviewed binary or the fast over-the-air update.
Kelvin versioning
(Devine Lu Linvega) counts versions down in Kelvin towards absolute zero, where the software is frozen and no further releases are possible.
git-pkgs
I tagged
proxy v0.5.0
.
Send links for next week to
@
[email protected]
.
