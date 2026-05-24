---
title: "This Week in Package Management: 23 May 2026"
url: "https://nesbitt.io/2026/05/23/this-week-in-package-management.html"
fetched_at: 2026-05-24T07:01:05.697466+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 23 May 2026

Source: https://nesbitt.io/2026/05/23/this-week-in-package-management.html

I’m trying out a weekly roundup built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
npm is
removing
npm-shrinkwrap.json
entirely
in the v12 prereleases. The command, the config alias, and the loader all gone; project-root shrinkwraps need renaming to
package-lock.json
and shipping a locked tree inside a tarball now means
bundleDependencies
.
Security
uv 0.11.15
fixes two issues worth patching for: a
TAR parser differential
and
entry points escaping the scripts directory
.
0.11.16
followed with
uv audit
now refusing locked installs that match known-malware records.
Ruby 4.0.5
shipped with a fix for CVE-2026-46727; anyone on 4.0.0 through 4.0.4 should update.
GitHub confirmed that around 4,000 of its own internal repositories were exfiltrated this week.
The Register reports
the entry point was a poisoned VS Code extension and attributes it to TeamPCP, the group behind the Shai-Hulud worm.
The Nx team published a
postmortem of the Nx Console v18.95.0 compromise
, another poisoned VS Code extension. The detail that stands out: the affected contributor had
minimum-release-age
set in
.npmrc
, but their pnpm was old enough to silently ignore the unknown key, so a 77-minute-old malicious package sailed through.
A
dependabot-core issue
points out that the cooldown setting can be bypassed by an attacker who controls the version timestamps, which is most of them. Worth knowing if you’ve been treating it as a security control rather than a noise filter.
Releases
Deno 2.8
makes npm the default registry:
deno add
and
deno install
now treat an unprefixed name as an npm package, with
jsr:
becoming the thing you opt into. It also ships
deno pack
for turning a Deno or JSR project into an npm-publishable tarball, plus
deno ci
,
deno why
,
deno audit fix
, a pnpm-style
catalog:
protocol, optional hoisted
node_modules
, and
min-release-age
support in
.npmrc
. Hard not to read a direction of travel into that list.
pnpm 11.2.2
adds an opt-in preview where adding
@pnpm/pacquet
to
configDependencies
hands the materialisation phase of
pnpm install
to the Rust port. Resolution stays in pnpm; pacquet just fetches and links from the lockfile.
conda 26.5.0
lands parser support for conditional dependencies, optional dependency groups, and variant flags from
CEP 164–166
.
Composer 2.10.0-RC2
is out with a call for testers;
composer self-update --preview
to try it,
--stable
to bail.
Homebrew 5.1.12
adds
brew exec
, an npx-style launcher that finds which formula provides an executable and runs it.
5.1.13
followed with RubyGems licence checking in audit.
RubyGems and Bundler 4.0.12
tidy up
BUNDLE_VERSION
handling and add a warning when an indirect dependency might be confused with a direct one.
Verdaccio 6.7.0
bumps the Node baseline to 24 and starts soft-warning on older runtimes.
PDM 2.27.0
does the same for Python, now requiring 3.10.
Articles
The Go team
announced an official pkg.go.dev API
: stateless GET endpoints for modules, versions, symbols, vulnerabilities, and search. No more scraping the HTML.
npm
announced staged publishing and new install-source controls
.
npm stage publish
uploads to a holding queue and a human with a 2FA challenge has to promote it before anyone can install. Alongside it,
--allow-file
,
--allow-remote
, and
--allow-directory
join
--allow-git
so you can lock installs to registry sources only;
--allow-git
flips to
none
by default in v12.
The NuGet blog wrote up
package pruning in .NET 10
, which trims transitive packages that the shared framework already provides and cuts the corresponding noise out of vulnerability reports.
Gábor Bernát posted his
Python Packaging Summit recap
from PyCon US, covering what got argued about in the room this year.
A Bloomberg-authored piece in
ACM Queue
argues that companies need to move from passive consumption to active stewardship of the open source they depend on.
The PHP Foundation
announced an Ecosystem Security Team
funded by an Alpha-Omega grant. Packagist meanwhile has
malware filter list support live in Private Packagist
ahead of Composer 2.10.
Trail of Bits
wrote up several months of contributions to zizmor
. A
typosquatting audit
for Actions references that I wrote also landed this week.
Elsewhere
pypitoken-cli
from Catherine takes an account-scoped PyPI token and narrows it to a package-scoped one from the command line.
diffify
shows what changed between two versions of a CRAN or PyPI package: function signatures, dependencies, namespace exports.
listen to PyPI
plays a note for every upload to the index, in the
Listen to Wikipedia
tradition.
Anil Madhavapeddy has been
resurrecting OCaml system packaging
and writing up how it fits together.
The GitHub incident prompted an
open VS Code issue
asking for cooldowns on extension auto-updates. The Dependabot bypass above is a useful read before treating that as solved.
git-pkgs
I tagged
git-pkgs v0.16.1
along with a bunch of new versions other repos in the git-pkgs org:
brief
,
proxy
,
manifests
,
registries
,
resolve
,
forge
,
enrichment
,
spdx
,
outline
, and
gitignore
.
Send links for next week to
@
[email protected]
.
