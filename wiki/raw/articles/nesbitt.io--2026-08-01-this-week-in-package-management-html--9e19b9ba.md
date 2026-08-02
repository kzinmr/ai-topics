---
title: "This Week in Package Management: 1 August 2026"
url: "https://nesbitt.io/2026/08/01/this-week-in-package-management.html"
fetched_at: 2026-08-02T10:14:20.186413+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 1 August 2026

Source: https://nesbitt.io/2026/08/01/this-week-in-package-management.html

Week eleven of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Releases
mise 2026.7.14–18
: the default shell-argument settings are now global-only, so an untrusted repo’s local config can’t influence command execution before trust evaluation runs. Experimental task output caching restores a task’s declared outputs and replays logs when its sources, tools and environment are unchanged, and experimental monorepo tasks now infer Node workspace dependency edges and import
package.json
scripts as
node:<package>#<script>
tasks.
Verdaccio 6.9.0
requires Node.js 22 as the minimum runtime and ships a dual CJS+ESM build with an
exports
field, so
import { runServer } from 'verdaccio'
resolves a real ES module. The bundled
@verdaccio/config
moves to js-yaml 4.3.0, resolving
GHSA-52cp-r559-cp3m
.
setup-uv v9.0.0
flips the
prune-cache
default to
false
to reduce load on PyPI infrastructure. The major bump reflects that workflows may see higher GitHub Actions cache usage as a result; the
reasoning is written up in #967
.
Renovate 43.282.0
has the mise manager run
mise lock
in the
MISE_SAFE=1
mode
added last week
, so lockfile updates against untrusted branches no longer need
allowedUnsafeExecutions
.
43.283.0
adds a
commitTrailers
option.
44.0.0
was an
accidental major
: a squash-merged PR carried a leftover
BREAKING CHANGE
footer that semantic-release acted on, so 44.x is being treated as a continuation of 43.x with no breaking change.
uv 0.11.33
runs the malware check against locked tools before reusing them from cache, and the preview lockfile format can now be written and read without embedded
package.metadata
.
0.12.0
collects accumulated correctness changes:
uv init
defaults to a packaged
src/
layout with
uv_build
, wheels that would overwrite the Python interpreter are rejected, and
--require-hashes
directives in requirements files are now enforced with MD5-only hashes refused.
0.12.1
adds per-package pre-release policies via
--prerelease-package
, accepts local HTML files as flat indexes, and the preview
uv check
gains
--fix
.
pip 26.2
adds
--only-deps
to install only a requirement’s dependencies, an experimental
--use-feature=venv-isolation
mode that uses a standard venv for build isolation instead of the
sitecustomize.py
overlay, and caches simple-index responses per their
Cache-Control
headers so repeated resolves against the same index are faster. The legacy resolver (
--use-deprecated=legacy-resolver
) is deprecated for removal in 2027. Richard Si has
a write-up of the release
.
pixi 0.74.0
lets environments define dependencies and solve strategy inline without a separate feature block, adds an
--offline
mode, and
pixi global install --git
can build a tool from source given only
--build-backend
and no package manifest.
0.75.0
has
pixi publish
publish all opted-in workspace packages in dependency order, refusing if a required source dependency has not opted in, and restricts
--offline
solves to packages already in the local cache or on a
file://
channel.
pnpm 11.15–11.19
on the stable branch:
pnpm update
and
pnpm outdated
now cover GitHub Actions references in workflow files,
pnpm update
can emit changesets for the bumps it makes,
pnpm self-update
ignores project-supplied configuration, web-based
pnpm login
works without a TTY, and peak resolution memory on large workspaces is cut several times over.
pnpm 12.0.0-beta.0
is the first beta of the Rust-engine rewrite; it now reads
frozenLockfile
,
savePrefix
,
savePeer
and
saveCatalogName
from
pnpm-workspace.yaml
and
PNPM_CONFIG_*
rather than only accepting them as CLI flags.
Maven 4.0.0-rc-6
fixes the RC-5 regressions: a globally-cached field-accessibility state that broke plugin configuration injection, a
ConcurrentModificationException
in the v4 API, and consumer POM conversion for BOM projects.
Docker 29.7.0
adds an experimental
embedded-containerd
feature that runs containerd inside the daemon process rather than as a separate managed process, promotes the
image
mount type out of experimental, and updates go-archive to 0.3.0 for
CVE-2026-17106
.
29.7.1
fixes two regressions from 29.7.0: pulling images whose layers omit explicit parent-directory entries, and
CopyToContainer
rejecting paths that traverse absolute symlinks.
Homebrew 6.0.14
attaches vulnerability data from the GitHub Advisory Database to the generated formula API and adds a
brew advisory-match
developer command (both from me), removes most subprocess forks from a no-op
brew
startup, and extends Landlock sandboxing to Linux kernel 6.1’s ABI 2.
Also out:
npm 12.0.2
,
Conda 26.7.0
,
pipx 1.16.5
,
sbt 2.0.4
,
snapd 2.77
,
vcpkg 2026-07-27
,
Dependabot Core 0.389.0
,
cabal-install 3.18.1.0
,
winget 1.30.80-preview
,
Yarn 4.18.0
,
Gradle 9.7.0-RC2
,
APT 3.3.2
,
Mamba 2.9.0.rc0
,
Podman 6.1.0-rc1
,
diffoscope 326
.
Security
npm now scans packages at publish time
before they become installable, holding or blocking uploads that trip the check. Packages with legitimate security-relevant behaviour declare it via a
contentPolicy
field in
package.json
plus a root
DISCLOSURE
file, and must then be published with 2FA or trusted publishing. Once declared, neither can be removed in later versions.
GitHub Actions
now holds workflow runs identified as potentially malicious
until a collaborator with write access approves them through an authenticated web session. It applies automatically to public repositories on github.com with no configuration.
Arch Linux has
disabled orphaned-package adoption on the AUR
after attackers adopted unmaintained packages to inject a Tor-based remote-access trojan, an escalation of the campaign that began with the
alvr takeover in June
. New account registration was suspended in June and reopened on 13 July with additional restrictions, which have not been sufficient.
LWN has more context
.
Articles
Open Source Must Be Fun or It Will Die
(Mike McQuaid) argues that maintainer enjoyment is the scarce resource that keeps a project alive, and points at Homebrew’s numbers: 26 of last year’s 29 maintainers are still active, with automation and CI doing the pedantic review work.
The Package Manager for Everywhere
(Patrick Linnane) breaks down Homebrew’s public analytics by platform: about a quarter of events are on Linux, Universal Blue images (which ship brew by default) account for roughly 26% of non-CI Linux traffic, and WSL is at 3.7%.
You Don’t Have a Supply Chain, You Have a Supply Soup
(Josh Bressers) argues the supply-chain metaphor breaks down when the inputs to a single dependency include CI runners, developer workstations and everyone with commit access, none of which current tooling captures.
Papers
No Edges, No Verdict
(Zięba-Kozarzewski, arXiv) analyses 78,000 SBOMs in the wild and finds 52.9% declare no dependency edges at all, and only 0.10% use CycloneDX compositions to flag that the graph is incomplete; treating edgeless SBOMs as degenerate raised KEV-detection recall from 0.600 to 0.950.
No Snake Oil: Verifying Python Package Builds
(Dietrich et al., arXiv) rebuilds 12,180 popular PyPI releases with macaron and oss-rebuild: only 15.4% and 19.1% of wheels come out byte-identical to the published artifact, but their daleq4py tool establishes semantic equivalence for 60.2% and 78.9% of source-equivalent rebuilds.
Elsewhere
The
EuroPython 2026 Packaging Summit notes
are up, following on from
last week’s
mention of the summit itself. Sessions covered wheel-variant provider trust (PEPs 817 and 825), whether PyPI should distribute application lockfiles separately from libraries, external build-dependency metadata via PURL (PEPs 725 and 804), and the Packaging Council election timeline.
Most WASI phase 2 proposals now have OCI packages published and are indexed on
wasm.directory
, a meta-registry for WebAssembly components that is intended for eventual donation to the Bytecode Alliance.
Composer and Packagist.org have
launched a formal sponsorship programme
with three annual tiers, funding operations, incident response and security-feature work such as malware detection and transparency logs. Ten companies signed on at launch alongside Sovereign Tech Agency funding routed via the PHP Foundation.
Renovate maintainer Sebastian Poxhofer has released a
Renovate Config Debugger
that steps through parsing, migration, validation, preset resolution and
packageRules
matching using Renovate’s own code compiled to run in the browser.
GitHub Actions workflows can now
reference actions in the same repository
with
uses: $/path/to/action
, which resolves to the workflow’s own repository at the commit that is running. It works in steps, composite actions and reusable workflow calls without a checkout, and satisfies policies that require full-length SHA pinning.
Fedora’s
Adopt PURL Metadata
change was accepted for Fedora 45: RPMs built from language-ecosystem packages will carry virtual Provides such as
purl(pkg:cargo/
[email protected]
)
across nine language ecosystems, with no spec file changes needed.
git-pkgs
I tagged 18 repos this week:
Send links for next week to
@
[email protected]
.
