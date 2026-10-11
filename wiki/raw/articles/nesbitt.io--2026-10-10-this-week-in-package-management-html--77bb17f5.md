---
title: "This Week in Package Management: 10 October 2026"
url: "https://nesbitt.io/2026/10/10/this-week-in-package-management.html"
fetched_at: 2026-10-11T10:01:12.170274+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 10 October 2026

Source: https://nesbitt.io/2026/10/10/this-week-in-package-management.html

This week’s package management news, gathered from the
package manager OPML feed collection
, my posts and boosts on
Mastodon
, and anything people sent me. The collection now includes the
vlt blog
and
vlt CLI releases
.
Releases
uv 0.13.0
makes Python 3.15 the default download, prefers native ARM64 interpreters on Windows ARM64, and changes the cache format, so dependencies may be downloaded or rebuilt after upgrading. It now honours
--require-hashes
in constraints files included with
-c
and rejects editable requirements in them, so installs that previously passed can fail. Astral’s
Python 3.15 post
also covers a
build-lazy-imports
preview that runs build backends under
-X lazy_imports=all
. Astral measured wheel builds up to 18% faster with it.
pnpm 12.11
installs and signature-checks the Rust toolchain named in
rust-toolchain.toml
, and links
skills/<name>/SKILL.md
files shipped by direct dependencies into directories such as
.claude/skills
once they are approved with
pnpm approve
. A new
permissions
setting records what each dependency may do, with its
build
capability taking precedence over
allowBuilds
.
12.10
added an experimental
loaded
node linker that loads compatible dependencies straight from the content-addressable store through a Node.js loader.
RubyGems and Bundler 4.1.0.beta2
add
gem build --content-addressable
, drop setuid, setgid and sticky bits when extracting gems, let a Bundler override drop or replace a single dependency of a gem, and add a
sparse_checkout
option for git sources.
Bun 1.4.3
skips downloading tarballs for packages that stay out of
node_modules
, such as bundled dependencies and packages for other platforms, when installing without a lockfile. Installing
[email protected]
went from 196 tarball downloads to 1. Registry and tarball URLs are also parsed more strictly before credentials are attached.
mise 2026.10.1 to 2026.10.7
runs
auto_update
in the background from an activated shell, still honouring
minimum_release_age
, and stores finished downloads in a content-addressed cache that is hashed again before each reuse.
java@21
and other vendorless Java versions now install Temurin builds.
PIE 1.5
installs several PHP extensions in one command and adds
pie upgrade
, which upgrades each extension within the constraint it was installed with.
--select=<extension>=<vendor/package>
replaces
--allow-non-interactive-project-install
for unattended installs, and the Sigstore attestation library PIE uses to verify its own updates now accepts attestation sources other than GitHub.
cargo-semver-checks 0.51.0
adds six lints for C-ABI variadic functions, which are new in Rust 1.99. This is the first language feature to get SemVer lints in the same release that added it. The project’s own dependency updates now use
-Z min-publish-age
with seven days and an allowlist of build scripts pinned by hash.
Docker Engine 29.9.0
adds a
lazy-pull
daemon feature that skips layer content a remote snapshotter such as
soci
or
stargz
already provides, and fixes containerd-store pulls that left images runnable but incomplete for export or push.
jj 0.46.0
can colocate secondary workspaces by creating Git worktrees, and
jj git push
can push to several remotes at once.
Terraform 1.17.0-rc1
allows variables and locals in provider requirements.
Also out:
Security
Gradle 9.8.1
fixes three high-severity advisories:
pnpm 12.10
stops a dependency version string with path traversal from writing files outside the global virtual store, and stops a lockfile overriding the integrity of a config dependency pinned with
version+integrity
.
pnpm audit signatures
now checks against the integrity recorded in the lockfile, and archive metadata over 64 MiB is rejected before being loaded into memory.
11.28.5
carries the fixes on the 11.x line.
Go 1.27.2 and 1.26.9
include security fixes to the
go
command along with
crypto/tls
,
html/template
,
net/http
,
net/textproto
and
os
.
SCORED
The
SCORED 2026 workshop
ran on Tuesday as part of
OpenSSF Community Day Europe
in Prague, and most sessions have slides on the schedule. A few were preprints already linked here:
Software Dark Matter
, which won best paper,
No Snake Oil
, the
trusting-trust attack through GNU strip
, and
the lemons review
.
Hurry Up and Wait: Malware Detection Timelines and Minimum Release Age for npm
(Dominic Tassio et al., SCORED) matches 520 malicious package versions from 403 CWE-506 GitHub advisories against npm publish times. 69% of attack windows closed within eight days, and weighting by downloads raises that to 94.2%, and the authors recommend an eight-day minimum release age.
Did You Forkget It? Detecting One-Day Vulnerabilities in Open-source Forks With Global History Analysis
(Romain Lefeuvre et al., SCORED) propagates OSV introduced and fixed commits across the Software Heritage commit graph. Starting from 7,162 repositories referenced in OSV, it finds 2.2 million forks carrying a presumed vulnerable commit, 1.7 million of them with an unpatched head.
When SBOMs Differ
(Lukas Gehrke et al., SCORED) publishes over 467,000 SBOMs for 93,445 repositories from Syft, Trivy and the GitHub dependency graph. The three sources produce different dependency sets and encode dependency structure differently, and sbomqs scores their output differently against regulatory guidelines.
Mind the Gap: How SBOM Specification Ambiguities Lead to Divergent Software Bills of Materials
(Alan Prado et al., SCORED) compares three SBOM generators against lockfiles for over 3,000 JavaScript and Rust projects. Most of the differences are systematic and come from each generator handling dependency scope, naming, provenance and representation in its own way.
Over the Shoulder: Improving SBOM Accuracy by Watching the Build
(Sanchit Sahay et al., SCORED) evaluates SBOMit, which records filesystem and network activity during a build with eBPF as in-toto attestations and turns them into package identities. Across 98 CNCF projects the median runtime overhead was 12.4%.
Librarian Catches Thief
(Gale Fagan, SCORED) runs document similarity over ClawHub, where attackers uploaded hundreds of near-identical agent skills that led users to credential-stealing malware. The scan found the campaigns and linked poisoned copies to the skills they were cloned from. It ran in five minutes on one workstation.
Canary in the Code Mine
(Timothy Brennan, SCORED) tries to predict which of 2,053 Jenkins plugins will get the next security advisory. A ROC-AUC of 0.96 turned out to come from a label leak, and the out-of-time figure under a pre-registered protocol was 0.67. Repeating the protocol on PyPI reproduced the leak and reversed which features came out as predictive.
SandScope
(Zhuoran Tan et al., SCORED) audits MCP servers by running them under WASI or over stdio and tracing environment, file and tool-input data into LLM-visible output. It completed shallow dynamic scans for 38.5% of a 100-repository MCP corpus.
When Models Meet Loaders: Deserialization Risk in Huggingface
(Xiang Guo et al., SCORED) measures how common 41 model serialization formats are across 10,000-model snapshots of Hugging Face taken at 39 points in time, 56,533 models in total. Each format depends on its own deserialization library, which becomes part of the supply chain of any application loading the model.
SoK: What Software Supply Chain Security Can Learn from Decades of Physical Supply Chain Risk Management
(Linus Kühl and Michael Dircksen, SCORED) maps 17 physical supply chain instruments onto software counterparts, such as bills of materials to SBOMs and dual sourcing to tested substitute dependencies. Five transfer directly and ten need adaptation. Safety stock fails to transfer because software copies are not used up, and threat modelling transfers in the other direction.
Ghost in the Codebase
(Luca Galli, Open Systems, SCORED) describes how Open Systems moved to a Bazel monorepo with one version per dependency after tracking Log4Shell by hand, then added SCA and SAST gates in CI that emit SARIF. Coding agents now go through the same gates, with an agent skill that reads the SARIF report.
Papers
Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub
(Fahd Seddik, arXiv) builds a dated copy network from the git history of every
SKILL.md
in GitSkills, covering 2.2 million skill adoptions. A few repositories are the source of almost all copies, and almost all copies stay at the version they were copied from. Reviewing the top 100 source repositories would prevent 14.9% of later adoptions of high-risk skills, against 0.5% for the 100 most-starred.
Assessing the Cross-Version Applicability of Java Library Vulnerability Exploits
(Zirui Chen et al., ASE) runs 259 exploits against 28,150 versions of 128 Maven libraries. Unmodified exploits identify affected versions with 83.0% recall and 99.3% precision, better than most vulnerability databases, and the work contributed 796 missing affected versions to the CPE dictionary.
Articles
How we made registry metadata 70% smaller
(vlt) describes the trimmed packument vlt.io serves by default, which shrinks vite’s from 4.41 MB to 104 KB. It drops
dist.signatures
,
dist.shasum
and attestation documents, which are base64 and hex strings that compress poorly under gzip, but keeps
time
,
license
and
libc
so pnpm and Bun can run minimum release age checks from the trimmed document. A
?stable
query filters prereleases, which are 58.6% of published versions across the top 1,000 packages.
The Era of Software Quality, or the Era of Ostriches?
(Michael Catanzaro) counts GNOME CVEs rising from 37 in 2024 to 97 in 2025 and 141 so far in 2026, and WebKitGTK reaching 305 this year, mostly from AI analysis of bundled Skia and ANGLE. The GNOME bug bounty paid €183,900 before ending in February because of AI-driven submissions. Catanzaro opposes Rust in GNOME because of the supply-chain risk of pulling in Cargo dependencies.
Rewind VM: a flaky build you only catch once
(Farid Zakaria) runs Nix builds in a single-vCPU KVM guest where clocks, interrupts and I/O completions are recorded, so each run is reproducible, and
rewind check
perturbs thread schedules to find failing interleavings. It found a
SIGPIPE
failure in a Nix test that had passed 20,000 runs on a laptop. The follow-up,
Nix wrote half of my debugger
, uses nixpkgs’
separateDebugInfo
outputs and debuginfod to show symbols and source for every binary in the VM, kernel included.
Mirko Swillus wrote up the
Alpha-Omega roundtable
at Open Source Summit Europe. Abandoned packages, the
Bernies
I wrote about in May, make up roughly 10 to 20% of the dependency trees behind critical infrastructure, and some package managers are starting to recommend replacements. Participants proposed ecosystem councils to prioritise abandoned packages by blast radius.
Elsewhere
The Deno team is
joining Cloudflare
, and JSR stays online with its infrastructure moving to Cloudflare. The Deno runtime gets monthly bug fix and security releases for one more year, after which Cloudflare stops developing it, and Deno Deploy shuts down in six months.
Guix channel files can now be an alias for a remote file with
downloaded-channels
, which takes an HTTPS URL or a SWHID, so the channel commits everyone pulls can be set from a CI server or by one person on a team.
R-Forge is being retired
after 20 years because the FusionForge software it runs on is unmaintained. The site goes read-only in January 2027 and SVN in January 2028.
git-pkgs
I tagged
proxy v0.9.1
.
Send links for next week to
@
[email protected]
.
