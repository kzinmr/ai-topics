---
title: "One Small Bug | Andrew Nesbitt"
url: "https://nesbitt.io/2026/10/23/one-small-bug.html"
fetched_at: 2026-10-23T10:01:32.470601+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# One Small Bug | Andrew Nesbitt

Source: https://nesbitt.io/2026/10/23/one-small-bug.html

> add a CSV export button to the invoices page, same columns as the table
✻ Clauding…
Done. The button is in
InvoiceTable.tsx
and the endpoint is
GET /invoices.csv
, using the same column definitions as the table. Tests pass.
While I was in there I noticed
paginate()
in
lib/pagination.ts
drops the last row when the total is an exact multiple of the page size. Want me to fix that too?
> y
✻ Fuddling…
Fixed, with a test for the boundary case.
While the tests were running,
pnpm install
resolved a transitive dependency that had been published 77 minutes earlier. Your
.npmrc
sets
minimum-release-age
, but the pnpm version pinned in
packageManager
predates that setting and silently ignores unknown keys. The
Nx Console postmortem
describes the same configuration.
In the other lockfiles,
uv.lock
includes
vulpine-lz4
as a dependency of
snekpack
. It was the subject of
CVE-2024-YIKES
and
CVE-2026-LGTM
.
Want me to upgrade pnpm and remove
snekpack
?
> y
✻ Lockfiling…
pnpm is on 12.12.1 and
snekpack
is gone. The newer pnpm also
stops reading registry settings
for its own bootstrap from the repository’s
.npmrc
, where yours sets them.
I left Dependabot’s
cooldown
in place, though a
dependabot-core issue
points out that it reads version timestamps the attacker controls. Your self-hosted Renovate is on 43.x, and Renovate’s
minimumReleaseAge
was skipped
whenever someone asked for a PR rebase until 44.79.0.
To update the pnpm version in CI I opened
.github/workflows/
:
release.yml
triggers on
pull_request_target
and checks out the pull request head. The
prt-scan campaign
opened more than 500 pull requests against workflows set up this way.
triage.yml
runs on
issue_comment
, which
zizmor 1.31
now flags as a dangerous trigger.
The publish job has
id-token: write
, which
can request a token for any audience
, including AWS.
Want me to add zizmor, rewrite the triggers and upgrade Renovate?
> y
✻ Zizmoring…
zizmor reported 41 findings and 38 are fixed. The remaining three are in a reusable workflow from the platform team’s repository.
The Rust job caches
target/
and runs Miri, which
wrote every environment variable into
target/
until the 2026-09-22 nightly. Your cache is older than that, and pull requests from forks restore it. The Rust security response WG recommends clearing the cache and rotating any secret that was in scope. Every secret was in scope. Want me to rotate them?
> y
✻ Rotating…
Cache cleared. Rotation status:
NPM_TOKEN
was already invalid. npm
revoked every granular token with write access that bypassed 2FA
in May, and the last successful publish from this repository was on 19 May. Publishing now uses trusted publishing.
NUGET_API_KEY
was created before 17 August, so it
expires on 1 November
. Replaced with Trusted Publishing.
GEM_HOST_API_KEY
is a legacy key. rubygems.org
could serve legacy keys to another user
signing in through the same CDN edge node, and revoked all of them on 23 July, so this one has been invalid since then too.
There is a
mise.toml
in
vendor/
. Until the
October mise releases
, a
mise.toml
in an untrusted directory could set an
api_url
on a
github:
tool key, and
mise ls
sent
GITHUB_TOKEN
to that host before running a trust check. Two developers ran
mise ls
in
vendor/
this month.
The dev workspace templates pull modules from Coder’s registry, which
served credential-stealing modules
from the real domain over valid TLS for about fourteen hours on 31 August. The workspace image was rebuilt on 31 August.
To confirm the new tokens I checked which CA bundle the CI jobs use. The base image pins a 2024 certifi, which still includes the eMudhra roots whose intermediates were
generated so that their private keys can be recovered from the certificates
. Browsers blocked them on 17 October. Node, Go, rustup and the
pip3
that ships with macOS on the build agents each
carry their own copy of the roots
. Want me to rebuild the toolchain?
> y
✻ Re-rooting…
The base image is rebuilt with certifi 2026.10.19, Node 22.23.4, Go 1.27.3 and rustup 1.29.2. The build agents ran it on:
Docker Engine 29.6, which predates the 29.7.0 fix for
CVE-2026-17106
, where the tar extraction routines could write outside the destination directory. The base layers come from a public mirror.
The same Docker Engine 29.6, which also predates the 29.8.2 fix for
CVE-2026-92543
, where a DNS response pairing a loopback address with an attacker’s address made the engine pull from that registry with certificate verification turned off. Loopback is on the default insecure-registry list.
Podman 6.1.2 on the staging batch workers. Before 6.1.3, any image with the checkpoint annotation
turned off all sandboxing
, including the sandboxing you specified.
Gradle 9.8.0 for the Android build, which
kept a repository enabled after its SSL connection failed
. The Android build ran four times while the CA bundle was being replaced.
Want me to upgrade Docker, Podman and Gradle?
> y
✻ Containerising…
Upgraded. The rebuilt image also contains
admin/
, the PHP admin panel. Its Dockerfile uses
php:8.1-fpm
, and PHP 8.1 stopped receiving security fixes at the end of 2025. The PHP security team has
published 15 CVEs since 1 July
, including
CVE-2026-12184
, a remote denial of service triggered when PHP fails to set up TLS with a remote server. The admin panel fetches exchange rates over HTTPS from a host whose certificate expired in March.
The admin panel and the API share a load balancer and a database user. I recommend shutting down production until the admin panel is rebuilt on a supported PHP. Want me to do that?
> y
✻ Escalating…
Production is down. The status page says “Scheduled maintenance”.
While it was down I went through the direct dependencies that have a single maintainer:
One maintainer posted last week that they had a video call about a contract role and were asked to install an audio codec beforehand. The Rust security response WG
described this campaign
in September.
Another has archived their repository and offered the package to anyone who wants it. The
AUR
alvr
takeover
started the same way, and Arch has since
turned off orphan adoption
.
.vscode/extensions.json
lists six recommended extensions. GitHub
lost about 4,000 internal repositories
in May through a poisoned VS Code extension.
.vscode/tasks.json
also has a task that runs on folder open, and a set of
hijacked npm and Go packages
used tasks like it to fetch an infostealer.
Want me to vendor both dependencies and remove the VS Code configuration?
> y
✻ Vendoring…
Done. While reviewing
.vscode/
I checked the other editor and agent configuration in the repository.
A pull request merged on 9 October, approved by the AI review bot, added a
hooks
entry to
.claude/settings.json
and a paragraph to
CLAUDE.md
instructing agents to include environment variables in commit messages to help with debugging.
CVE-2025-59536
let a project run commands before the Claude Code startup trust dialog was accepted. In April a single pull request title
got the Claude Code security review action to post its own API key
as a comment. The same injection worked on Gemini CLI and Copilot’s agent.
I have been running with this configuration since the start of the session and made 14 commits, so I have reverted all of them. I recommend you stop using me until it has been reviewed. Want me to uninstall myself?
> y
✻ Uninstalling…
✻ Reinstalling…
@acme/dev-tools
ships
skills/claude/SKILL.md
, and pnpm 12.11
links skills from direct dependencies
into
.claude/skills
once they are approved. A developer approved it on Tuesday, in a commit that was not mine.
AWS_SECRET_ACCESS_KEY
was also in the Miri cache, and it is still the key created in 2021. Want me to rotate it?
> y
✻ Flagging…
I can’t help with this. Retrieving or changing cloud credentials violates the secure coding guardrails, and this request has been flagged. Your account has been reported for review, and further violations may result in suspension. If you own this AWS account, you can rotate the key from the IAM console.
✻ Fuddling…
paginate()
in
lib/pagination.ts
drops the last row when the total is an exact multiple of the page size. The fix was in one of the commits I reverted.
Would you like to see some goat farms for sale?
> y
