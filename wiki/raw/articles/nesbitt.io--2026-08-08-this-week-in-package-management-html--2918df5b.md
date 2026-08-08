---
title: "This Week in Package Management: 8 August 2026"
url: "https://nesbitt.io/2026/08/08/this-week-in-package-management.html"
fetched_at: 2026-08-08T10:13:47.028896+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 8 August 2026

Source: https://nesbitt.io/2026/08/08/this-week-in-package-management.html

Week twelve of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
.
Releases
pnpm 11.20
fixes a package-substitution risk in projects with multiple named registries by recording packages under registry-qualified lockfile keys such as
foo@work:1.0.0
.
12.0.0-rc.1
, the Rust-engine release candidate, resolves git dependencies on known hosts through the canonical HTTPS URL so the lockfile never records an SSH URL, and refuses global commands run under
sudo
.
mise 2026.8.0–8.3
turns
mise bootstrap
into a declarative host-provisioning system: alongside packages it now converges files, users, systemd units, Docker Compose projects and firewall rules, with
mise bootstrap plan
to preview and remote execution over SSH. 8.3 adds a
flatpak-user
package manager and Linux font-cask support.
packaging 26.3
adds a
VersionRange
API that represents the versions a specifier set accepts as an interval set with intersection, union and difference operations, plus
is_subset
/
is_superset
/
is_disjoint
on
SpecifierSet
. It also accepts
Metadata-Version: 2.6
per
PEP 808
, which lets build backends extend list and table
[project]
fields that are also declared in
project.dynamic
.
uv 0.12.2
adds a preview
uv tool audit
command that runs the vulnerability audit against installed tools, using the per-tool
uv.lock
files from the
tool-install-locks
preview. It also ships CPython 3.15.0rc1 as a managed interpreter.
zizmor 1.29.0
is the first release to audit inputs beyond GitHub Actions: pre-commit configuration files and hook definitions are now supported, starting with a new
insecure-url-scheme
audit and pre-commit coverage in the existing
impostor-commit
and
forbidden-uses
audits. It also recognises GitHub’s new
uses: $/path/to/action
self-repository syntax. A
discussion thread
is collecting requests for further CI platforms.
Dependabot Core 0.390.0
adds security-update support for vcpkg ports, beta support for pnpm 11, and has the
github_actions
updater relock
gh-actions-lock
lockfiles alongside workflow updates. The three-day cooldown default is now unconditional.
Verdaccio 6.9.2
applies configured package access controls to the
GET /-/_view/starredByUser
endpoint, which previously returned a user’s starred packages without filtering by what the requesting client is authorised to see.
Mamba 2.9.0
adds
--exclude-newer
to filter out packages built after a given timestamp, for reproducing an environment as it would have resolved at a past point in time, and an option to opt out of running link scripts during install.
Also out:
Security
NuGet.org is
reducing the maximum API key lifetime
from 365 days to 30 days from 17 August, with all keys created before that date expiring on 1 November. Publishers are pointed at OIDC-based Trusted Publishing, which issues a short-lived key per publish operation against a policy configured by the package owner.
npm has
restricted 2FA-bypass granular access tokens
from token management, package access changes and organisation membership operations, which now require an interactive 2FA challenge. The tokens lose direct publish rights entirely in January 2027, with trusted publishing or staged publishing as the replacement for automated pipelines.
sbt 1.12.15 and 2.0.6
fix a remote code execution in the sbt server (
GHSA-m2pw-22cj-jq4v
) reachable when
Global / serverConnectionType
is set to
Tcp
. The setting defaults to a local Unix domain socket, so only builds that opted into TCP are affected.
Articles
Your composer.lock knows what a carmaker only guesses
(Sebastian Bergmann): a car manufacturer’s open-source attribution lists an Android botnet, giving away that the list came from a binary scanner rather than declared dependencies. Bergmann walks through how the PHPUnit PHAR discloses its own contents from
composer.lock
and argues an SBOM built from the lockfile is worth more than one reverse-engineered after the fact.
Making RubyGems Guides friendly to humans and AI
: guides.rubygems.org now serves
sitemap.xml
,
robots.txt
and per-page plain-text renderings so agents can fetch a guide without navigation and markup, prompted by the Evil Martians Ruby/Rails LLM discoverability scorecard.
A Vision for Cargo
(Ed Page): a Cargo team member sets out the workflows he wants to improve, covering dependency discovery and audit points in the crates.io ecosystem, build performance, plumbing commands and programmatic APIs for tools built on Cargo, and the state of the Cargo codebase itself.
Elsewhere
The
Software Stewardship Lab
launched on Thursday, a non-profit applied research lab for open source sustainability that I’m a director of. I’ve
written it up separately
, and there’s a
Sustain podcast episode
with executive director Vlad-Stefan Harbuz.
The Nixpkgs core team
has disbanded
. Its two members cite workload incompatible with continued technical contribution and friction with the Steering Committee, which now takes over the team’s responsibilities directly.
William Woodruff’s EuroPython 2026 keynote
Securing Python for the next decade
is online.
htmx 4: the game
(Seth Larson): htmx 4 shipped as a physical Game Boy cartridge, and the distribution mechanism for the library source is to finish the game and hand-type it from the screen.
help wanted
(Lake Hope): a maintainer responds to feedback from the community.
jj v0.44.0
stabilises tag support: tags can be tracked or untracked like bookmarks, with tracked tags pushed by default.
Stylometric Defenses Against Author Impersonation in Software Repositories
(Ravich et al., arXiv) builds a patch-level authorship verifier from twenty years of Linux kernel commit history and applies it retroactively to real supply-chain incidents: the 2021 PHP backdoor commits surface within about 1% of the maintainer review queue and the 2026 ForceMemo spoofs at a median 0.8% per-repository review burden.
The conda org’s
June and July release roundup
covers rattler 0.25.0 moving to resolvo 0.11.1 for roughly 40% faster large solves, conda-libmamba-solver 26.7.0 caching prefix records so a 50,000-record environment loads in seconds rather than timing out, and conda-pypi 0.11.0 building a conda channel from local wheel files.
OpenAlex is
adding research software as a first-class work type
in its scholarly graph, funded by a two-year Schmidt Sciences grant. A mention-extraction pipeline over paper full text will link works to the software they cite, with outbound identifiers to package registries, repository URLs, DOIs and Software Heritage, plus a versioning model and per-author software contribution metrics.
Who Will Keep Research Data Infrastructure Open and Running?
(Jennifer Gibson and Kaitlin Thaney, Issues in Science and Technology): nearly 200 research data repositories have shut down since 2000, more than half of those since 2018, and the piece argues for sustained operational funding of open infrastructure rather than project-based grants.
git-pkgs
I tagged
archives v0.5.0
,
clone v0.2.1
,
magic v0.2.0
,
manifests v0.7.0
,
proxy v0.6.1
and
spdx v0.3.0
.
Send links for next week to
@
[email protected]
.
