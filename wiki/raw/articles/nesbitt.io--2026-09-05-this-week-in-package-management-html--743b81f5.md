---
title: "This Week in Package Management: 5 September 2026"
url: "https://nesbitt.io/2026/09/05/this-week-in-package-management.html"
fetched_at: 2026-09-06T10:01:20.955851+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# This Week in Package Management: 5 September 2026

Source: https://nesbitt.io/2026/09/05/this-week-in-package-management.html

Week sixteen of the roundup, built from the
package manager OPML feed collection
and whatever I’ve posted or boosted on
Mastodon
. I added Terraform, OpenTofu, Elm and PSResourceGet release feeds to the OPML this week.
Releases
pnpm 12.1
adds the workspace task scheduler to the Rust CLI, dispatching each package as soon as its dependencies finish where the previous scheduler waited for a whole topological batch, and moves login credentials into structured global config.
12.3
makes the global command shims native executables on every platform and extends the trust-policy flags to
pnpm remove
and
pnpm update
. On the 11.x line,
11.25
backports the task scheduler and adds
--resume-from
for recursive runs.
rustup 1.29.1
checks for toolchain updates in parallel during
rustup update
and installs multiple components concurrently in
rustup component add
.
Conan 2.32.0
adds LoongArch64 host detection, Xcode 26.6 and gcc 16.2 support, and lets
XcodeToolchain
accept arbitrary xcconfig build settings.
PDM 2.29.0
exports editable local dependencies with relative paths in requirements files, and restricts locked packages to the platform they were resolved for when appending targets with
pdm lock --platform
.
zizmor 1.30
, the GitHub Actions workflow auditor, adds a
self-repository
audit and expands pre-commit support.
Renovate 44.59.0
adds a manager for Microsoft’s Agent Package Manager, and
44.60.0
lets security-update PRs be rate-limited and stops the Go proxy datasource caching transient errors, a long-standing cause of flapping Go update PRs.
The Maven 3.8.x branch has
reached end of life
; the final state is archived under a tag and the branch removed.
Also out:
Security
Podman 6.1.1
fixes
CVE-2026-17106
, a path traversal where a crafted tar archive could write outside the extraction directory via malicious links.
Poetry 2.4.2
fixes three issues: installing an artifact absent from the lockfile when the source omits its hash, a path traversal when downloading from a compromised URL, and a path traversal in sdist extraction on Python 3.10.0-3.10.12 and 3.11.0-3.11.4.
Coder disclosed
that an attacker gained access to its Cloudflare account and added their own IPs to the module registry pool, serving credential-stealing modules for about fourteen hours on 31 August. Fixed in 2.37.0 with backports to 2.36.4, 2.35.7 and 2.34.9. This is
what artifact signing is for
: the tampered modules came from the real domain over valid TLS, so only a signature check against a key held outside the Cloudflare account would have flagged them.
Articles
Boring Python: dependency management
(James Bennett) is a revised edition of the 2022 post: it now recommends PEP 751 lock files over pinned requirements files, allows uv or PDM for local development while keeping pip-with-hashes for production installs, and adds a section on three-day dependency cooldowns.
The Holy Grail of Nixpkgs Version Ranges
(Farid Zakaria) adds version-range constraints to nixpkgs by pairing a 309,000-version index of historical nixpkgs revisions with the clingo Answer Set Programming solver, so a query like
python@>=3.10
resolves to a concrete set of revisions. Mixing revisions can produce glibc symbol mismatches, which the solver constrains against using binary compatibility metadata.
Security scanning my own code with Scrutineer and local coding models
(Anil Madhavapeddy): notes on running Scrutineer, the code-scanning workflow tool that I wrote, against his own repos with a local GLM 5.3 model in place of a hosted one. He argues the triage decisions maintainers make on findings should themselves be tracked and fed into later scans across an organisation.
Papers
The Software Supply Chain as a Market for Lemons: A Multivocal Review of Trust Signal Collapse
(Paramitha et al., arXiv) reviews 252 web sources and 870 Reddit threads on how practitioners pick dependencies: the cheap signals they rely on (stars, download counts, contributor activity) are now cheaper to fake than to earn, and the authors recommend costly signals such as cryptographic attestation as mandatory defaults.
A Multi-Month Study of Git Commit Signing
(Shittu et al., arXiv): 22 CS students configured commit signing independently, used it across four coursework projects and a second device, then examined a repository seeded with anomalous commits; nearly all signed every commit but over a quarter missed the anomalies.
AgOSS: A Dataset and Multi-Layer Characterization of Open-Source Agricultural Software
(Dudhaiya et al., arXiv) applies OpenSSF Scorecard, governance metrics, SBOM dependency analysis and KEV matching to 66 agricultural OSS repositories and non-agricultural controls; the agricultural projects score lower on raw Scorecard results but the gap disappears once project size and maturity are accounted for.
Elsewhere
NYU Tandon has
launched
the NYU Software Supply Chain Security Operations Center, led by Justin Cappos, embedding master’s students in open source projects for year-long security placements; the first cohort of 8-10 starts January 2027 with support from Google and DTCC.
Sovereign Tech Agency with Erik Möller
(Josh Bressers, Open Source Security): an interview with the STA’s Director of Programs on the Sovereign Tech Fund, its maintainer fellowships, funding for standards-body participation, and the Sovereign Tech Resilience programme for security audits and post-quantum work.
Introducing vulnbrocards.com
(William Woodruff): the vulnerability-triage brocards from earlier posts now each have a stable URL.
Determining Value and Viability Using CHAOSS Practitioner Guides
(Dawn Foster) is part three of the series, covering the Demonstrating Organizational Value and Assessing Viability guides for justifying open source contribution work to leadership and evaluating dependency risk.
Tracking Trends in Open Source AI Policy
(Emma Irwin) applies the CHAOSS AI Alignment working group’s use-policy-specificity metric to 39 open source project AI policies: 25 address code contributions, none address environmental impact, infrastructure strain or notetaker bots.
GitHub added a
star history REST endpoint
that returns timestamped aggregate star counts for a repository without listing the accounts that starred it.
The Cargo team put out a
call for testing
for
-Zchecksum-freshness
, which detects the need to rebuild from file content checksums, replacing the mtime check. The plan is to stabilise it as
build.fingerprint = "content"
in
.cargo/config.toml
.
CERN is
migrating its 2,200 accelerator-control machines
from RHEL to Debian 13 by the end of 2026. The announcement calls the
-march=x86-64-v2
compiler default forced obsolescence for older hardware and lists gaps in Debian’s standard tooling for automated package building and publishing.
The recording of
Is the InnerSource Commons Good for Open Source?
, the FOSS Backstage 2026 talk Ben Nickolls and I gave analysing 800 InnerSource Commons member companies, is now up.
FOSDEM 2027
will be held
on 30-31 January.
git-pkgs
I tagged 23 repos this week:
Send links for next week to
@
[email protected]
.
