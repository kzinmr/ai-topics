---
title: "Package Manager Trends"
url: "https://nesbitt.io/2026/09/10/package-manager-trends.html"
fetched_at: 2026-09-11T10:01:12.139219+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Package Manager Trends

Source: https://nesbitt.io/2026/09/10/package-manager-trends.html

I’m on holiday this week, so I’m phoning it in and doing a roundup of the trends I’ve seen across sixteen weeks of
This Week in Package Management
. Those posts are built from about eighty
RSS feeds
and whatever I’ve boosted on Mastodon. The short version: the same defensive features keep shipping in tool after tool, and the same three bug classes keep getting fixed.
Features
Release-age cooldowns appeared in more tools than any other feature: Deno
2.8
added
min-release-age
to its
.npmrc
handling in May, and by early September equivalent gates had shipped in
Bundler
,
npm
,
Yarn
,
mise
,
Hex
,
Mamba
, and Cargo via the nightly
-Zmin-publish-age
flag. Dependabot made a three-day cooldown its
unconditional default
in August. The interaction between cooldowns and security updates recurred as a special case: Dependabot, Renovate and Hex each added a way to lift the gate when an advisory is published against the held-back version. The
Nx compromise postmortem
noted an old pnpm ignoring
minimum-release-age
, and both
npm 12
and
pnpm 12
now error on unrecognised config keys rather than skip them.
Install-script blocking became the default in the JavaScript tools. npm 12
blocks lifecycle scripts by default
with an
allowScripts
allowlist,
Bun 1.4
restricts auto-trust to packages fetched from the npm registry, and pnpm extended
allowBuilds
to
git-hosted dependencies
. Related install-source restrictions shipped alongside: npm 12’s
allow-git
and
allow-remote
default to
none
, and Composer 2.10
disables
the fallback from dist to source on download failure.
Malware checks at install and publish time shipped in Composer 2.10 (native filtering against
an Aikido-supplied feed
, on by default), uv (via
UV_MALWARE_CHECK
and later a
config setting
), and the npm registry, which now
scans at publish time
and can attach a
contentPolicy
verdict to package metadata. Five tools added or expanded a built-in audit command:
Deno
(
deno audit fix
),
uv
(
uv audit
, later
uv tool audit
),
Homebrew
(
brew vulns
merged into core),
Bun
(
bun audit fix
), and
Hex
, which now surfaces advisories during
mix deps.get
.
pnpm and mise separated checked-in project config from machine-level trust across several releases each. pnpm progressively stopped project-level
.npmrc
and
pnpm-workspace.yaml
from
redirecting credentials
,
expanding environment variables
,
influencing self-update
, or
relocating machine-level state directories
. mise made
credential_command
global-only
, added a
MISE_SAFE=1
inert-reader mode
, and Renovate
adopted it
for lockfile updates.
pnpm made
tarball integrity mismatch a hard failure
and started
rejecting lockfile entries missing an
integrity
field
, while uv 0.12
enforces
--require-hashes
and refuses MD5-only sources.
Bun 1.4
records SHA-512 for GitHub and tarball dependencies.
Registry-side controls tightened at npm (staged publishing,
2FA-bypass token restrictions
), Packagist (
immutable versions
, transparency log), PyPI (
rejecting new files
added to releases older than fourteen days), NuGet.org (
API key lifetime cut
from 365 to 30 days), and AUR, which
disabled orphaned-package adoption
after two takeover incidents starting with
alvr
.
Outside the security cluster, workspace and monorepo support shipped or graduated in
PDM
,
Conan
,
pixi
,
Hatch
,
uv
and
mise
, and the pnpm 12
Rust rewrite
reached stable. GitHub Actions references started being treated as managed dependencies:
pnpm
,
Dependabot
and
Renovate
each added update or lockfile support for workflow
uses:
entries.
Vulnerabilities
Path traversal on archive extraction or install was fixed at least once in fourteen of the sixteen weeks, across uv, pnpm, RubyGems, Podman, Composer, Guix, opam, ORAS, Docker, Flatpak and Poetry. Symlinks pointing outside the target directory,
../
in package names or lockfile keys, hardlinks with relative targets, and
bin
entries resolving outside the package all appeared. pnpm alone shipped four separate traversal fixes; Docker shipped three and Composer two.
Credentials sent to the wrong host or output came up almost as often:
Cargo 1.96
fixed authentication against normalised registry URLs;
Dependabot
fixed npm registry credentials sent to sibling paths on the same host;
ORAS 1.3.4
fixed mTLS certificates presented to any HTTPS peer, custom headers forwarded across origins, and pre-signed URLs logged in debug output;
Composer 2.10.3
fixed GitLab URL matching that could send credentials to the wrong domain;
Renovate
disclosed four exfiltration paths via malicious
Link
headers and TLS private key exposure in logs. The RubyGems.org CDN
served one account’s legacy API key to another
via a caching misconfiguration.
Command injection via a VCS URL or reference appeared in
pnpm
(git commit field allowing
--upload-pack
injection),
Docker
(git bundle checkout), and
Composer
(Perforce URL). Four of the ten
Renovate advisories
fell into this class as well.
Sustainability
Alpha-Omega funded security-engineer residencies at the
PHP Foundation
and
Ruby Central
, and the
Rust Foundation
launched a Maintainers Fund that named its
first residents
in August with backing from Google, AWS and OpenAI. The Sovereign Tech Agency
invested €508,640 in Flatpak
and appears in the new
Composer sponsorship programme
via the PHP Foundation. NYU Tandon
launched
a Software Supply Chain Security Operations Center placing master’s students in open source projects for year-long security work.
The Python Software Foundation announced the
first Python Packaging Council election
, with seventeen candidates by mid-August. On the deprecation side,
Helm v3
set an EOL schedule ending February 2027,
Go dropped Bazaar
VCS support, pip
deprecated the legacy resolver
for 2027 removal, the
Nixpkgs core team disbanded
, and
Maven 3.8.x
reached end of life.
