---
title: "This Week in Package Management: 7 November 2026"
url: "https://nesbitt.io/2026/11/07/this-week-in-package-management.html"
fetched_at: 2026-11-08T10:01:04.089686+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 7 November 2026

Source: https://nesbitt.io/2026/11/07/this-week-in-package-management.html

This week’s package management news, gathered from the
package manager OPML feed collection
, my posts and boosts on
Mastodon
, and anything people sent me. Version control and forge news is in the Wednesday
This Week in Source Control
roundup.
Security
Vox Pupuli fixed three critical vulnerabilities
that a Neodyme researcher reported in OpenVox, the community fork of Puppet. OpenVox Server deserialised Ruby objects embedded in agent run reports, which allowed remote code execution. The shared Trapperkeeper authorisation library matched every plain-string rule in
auth.conf
as a wildcard, so a certificate for
evil.target.example.com
was accepted as
target.example.com
. The OpenVoxDB container image allowed any certificate to reach its API because its allowlist script failed on startup.
All known Puppet implementations are affected, and the fixes are in openvox-agent 8.32.0 and 9.3.0 and openvox-server and openvoxdb 8.18.0 and 9.2.0. Updates to open source Puppet, including security fixes, have ended, so Vox Pupuli recommends migrating to OpenVox.
An
issue on actions/runner-images
reports that GitHub’s public macOS runners still accept certificates from the compromised eMudhra intermediates covered here last week. Apple has yet to patch the system
/etc/ssl/cert.pem
. Homebrew has shipped patched
ca-certificates
,
curl
and
git
, but the runner images disable Homebrew updates, so jobs run the vulnerable preinstalled versions.
DSA-6607-1
fixes
CVE-2026-109518
in APT, found by Max Justicz. When an HTTP redirect gave two package downloads the same URI, APT could merge them. A retried download then let an attacker on the network path, including a malicious mirror or proxy, replace a package after verification and run code as root.
The attack needs
Acquire::Retries
set to 1 or higher, and the default is 3 from Debian 12 and Ubuntu 22.04. Fixed versions are 3.0.4 for trixie, 2.6.2 for bookworm and 3.3.6 in unstable.
A
Nixpkgs advisory
covers two bugs in
darwin.linux-builder
, the Linux VM that macOS users run as a remote builder. The
run-builder
script added the whole
keys
directory to the world-readable Nix store, so any local user could log in as
builder
, a trusted user on the VM’s Nix daemon (
GHSA-45qr-47fw-2p57
).
The QEMU variants also forwarded the builder’s SSH port on every network interface (
GHSA-w5j5-2jpq-3cv3
). Fixes are on unstable and 26.05, and after updating the advisory says to delete the old key pair from the store, regenerate it and delete the builder’s disk image.
Docker Engine 29.9.3
fixes four CVEs in the engine and SwarmKit. It also updates to BuildKit 0.34.2, which fixes a resolver cache poisoning crash when a build resolves the same Git source twice.
Releases
hex.pm
opened Workload Identity and staged publishing
to every package and organisation. A GitHub Actions job can exchange its OIDC token for a Workload Identity token that expires after 15 minutes and can publish only that package. An organisation can also use a read identity to fetch its private packages in CI with only the job’s OIDC token. Staged publishing holds releases published with a key or a workload identity until a person approves them with a fresh 2FA code.
New packages get staging by default and existing packages have to opt in. Staged releases expire after seven days.
Hex 2.7.0
adds
mix hex.publish --wait
, which blocks until the release is approved and exits with an error if it is rejected or expires. A new
--check-unused-ignores
flag makes
mix hex.audit
fail on ignore entries that match nothing in
mix.lock
.
PyPI’s
redesigned project pages
add a Security tab that shows each release’s provenance and the attestations for each file. A release counts as having full provenance only when every file has a Trusted Publisher or SLSA build attestation. Warnings flag incomplete, inconsistent, changed or lost provenance, and files uploaded more than 14 days after an older release get a late-upload marker.
conda 26.10.0
makes
conda-rattler-solver
the default solver, including after upgrades where the solver setting is unset.
--solver=libmamba
selects the libmamba solver, and the classic pycosat solver now ships in a bundled
conda-pycosat-solver
plugin. The release also records when an environment was last activated and adds
--disable-plugins
and
--enable-plugins
for switching individual plugins off and on.
pnpm 12.18.0
publishes platform variants of a package to pnpr registries as one archive per target, and installs the variant that fits the host. Publishing to any other registry requires
--no-variants
, which publishes only the archive that targets any platform. Agent skills are now approved one skill at a time and linked under their own names.
pnpr 0.1.0-alpha.18
stores hosted package metadata in SQLite or libSQL and logs release records in transparency logs.
mise 2026.11.0
(now
2026.11.3
) makes
--locked
require checksums, and safe mode now ignores project lockfiles. It adds opt-in Sigstore provenance verification for
npm:
tools, which checks only the tool’s own package and requires the embedded aube package manager. Tasks can now declare a
lock
so that runs sharing a database or simulator execute one at a time, even across worktrees.
pixi 0.84.0
(now
0.84.1
) moves
exclude-newer
into the
[workspace]
table and supports exemptions to the cutoff. A workspace can apply the cutoff to new releases by default and exempt vetted security releases. A rattler fix for hash collisions between unequal package versions means lockfiles written by older pixi versions may require a
pixi lock
before pixi accepts them as locked.
pip 26.3
blocks unexpected imports during installation and warns about unsafe ones afterwards. HTTP redirects to
file:
URLs are now rejected, and PyPI’s restriction on direct URL dependencies now covers extras and cached wheels.
-r pylock.toml
now supports extras and non-default dependency groups, and accepts
--no-binary
. The security policy now states that installing untrusted wheels has always been unsafe, since Python’s import system can run third-party code during installation.
Gradle 9.9.0
promotes the custom
dependencies
block API out of incubation, including bundles and constraints from providers. When the
wrapper
task regenerates
gradle-wrapper.properties
, it now carries over existing settings such as distribution type, timeouts and retries. It still regenerates
distributionUrl
, which overwrites a custom host.
zizmor 1.32.0
adds experimental support for GitHub’s new
workflow lockfiles
. It now collects only the inputs GitHub Actions reads, so it skips workflows in vendored directories.
Renovate 44.210.0 to 44.222.0
adds a
julia
manager with a datasource for the General registry and Julia versioning, and reads transitive dependencies from
uv.lock
for security updates. Extracted constraints are now shared across managers. A tool version pinned in mise or
rust-toolchain
limits the updates other managers open.
Dependabot version updates
now support Microsoft’s Agent Package Manager
on github.com, following the
apm
ecosystem added in Dependabot Core 0.400.0. It opens pull requests for git dependencies declared in
apm.yml
and regenerates
apm.lock.yaml
when present. The support covers version updates only.
Also out:
Articles
Friction in the Python Packaging Standards Process
(konsti, uv) lists problems with how packaging PEPs get made. The text goes through editing passes before and after discussion and moves between reStructuredText and Markdown. Discussions on discuss.python.org have no concern tracking, and several maintainers avoid the forum. Small changes, such as removing a decade-old unimplemented feature, require a full PEP. The post points to Rust’s RFC concern tracking and final comment period as prior art.
Scrutinize our assessments
(Daniel Stenberg) follows up on curl moving low and medium severity vulnerability handling into public GitHub issues. Stenberg explains the
vuln:ASSESS
,
vuln:NONE
,
vuln:LOW
and
vuln:MEDIUM
labels and asks outsiders to challenge the severity calls. CVE IDs are visible from assignment, and the full records are published on the release date.
The author of
No, npm, “estee” is not a typo of “testem”
(smoores.dev) hit npm’s typosquat check while naming a package for the Storyteller project. The registry rejected
estee
as too similar to
espree
and
testem
, then flagged the fallback
hoid
against
hoek
,
hono
,
uuid
and
zod
. npm support declined to lift the automated block. The author infers an edit-distance-of-two rule against popular names. Under that rule
preact
and
estree
would also be blocked.
The intensional model in disguise
(Farid Zakaria) maps Nix onto Bazel and buck2. Bazel and buck2 key actions by the content of their inputs, so editing a comment in a C file stops the rebuild once the compiled output comes out the same. Nix gets that early cutoff only with content-addressed derivations, because by default it addresses outputs by their recipe. The post lines up Nix’s resolved derivations, realisations and store with Bazel’s actions, action cache and CAS.
Josh Bressers
talked to Roi Nisimi
about backport gaps: security fixes merged to a project’s main branch but missing from its latest release. Nisimi’s
write-up for Orca Security
reports hundreds of confirmed cases from a scan of thousands of repositories. Advisories and published vulnerable ranges are often missing for these fixes, so scanners report the current release as clean.
Elsewhere
DCFinder
(Xiaoya Zhu et al., Journal of Computer Security) detects dependency confusion in Python projects that use more than one index. It builds the transitive tree from private indexes and PyPI and checks whether the resolver would select a public version. On 28 real projects it reports 88.7% precision and 83.3% recall, against zero detections from the baseline tools.
Vlad Miricioiu, director of the Software Stewardship Lab and one of my FOSDEM devroom co-organisers,
talked to RedMonk
about binary dependencies, maintainer burnout, funding models and the Bernies. The Stewardship Lab
received $5,000 from Syntax and Sentry
towards an annual survey of burnout among open source maintainers.
Software Line Specialist
(Lovro Bikić) is a delightful bit of satire.
git-pkgs
I tagged 14 repos this week:
Send links for next week to
@
[email protected]
.
