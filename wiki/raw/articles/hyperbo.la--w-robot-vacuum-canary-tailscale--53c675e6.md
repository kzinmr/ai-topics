---
title: "Enabling Codex to Upgrade My Robot Vacuum"
url: "https://hyperbo.la/w/robot-vacuum-canary-tailscale/"
fetched_at: 2026-04-29T07:02:14.890648+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Enabling Codex to Upgrade My Robot Vacuum

Source: https://hyperbo.la/w/robot-vacuum-canary-tailscale/

I have a Valetudo robot vacuum named Loki that runs a custom Tailscale binary to
safely expose the web interface for a home camera with wheels to my LAN. That
setup works great until it becomes maintenance debt: upgrading the access path
can also break the access path.
Codex.app
upgraded Loki’s Tailscale binary from
v1.90.8
to
v1.96.4
. More importantly, it changed the upgrade from replacing the
production binary over the production connection to a canary identity, a
checked-in runbook, and two explicit approvals from me.
The background here is David Anderson’s excellent
Tailscale
sucks
post, which walks through jailbreaking a robot vacuum,
installing
Valetudo
, and running Tailscale on the small Linux system
inside the appliance. That post covers the initial setup. My problem was
maintenance. Once the vacuum is a little Linux host on the tailnet, somebody
still has to keep its access path patched without losing the only remote path
into the device.
Enabling Codex to do this upgrade is a small, real example of
harness
engineering
. What I want to keep from it is not the canary
by itself, but the machinery Codex built around a maintenance job I historically
avoided, and sometimes did unsafely.
Here was
the tweet I posted during the canary run
:
the hard part is verification so Codex proposed giving my vacuum a canary
tailscale identity so new extra small tailscale builds can be deployed AND
TESTED before doing a cutover to an upgraded version. after 3 hours of
cooking, it seems to work?
I cared about verification because this path had already failed in concrete
ways. Several prior Tailscale upgrades forced me to adjust build tags as
upstream added more
ts_omit_*
switches and
--extra-small
stopped carrying
behavior Loki depends on: Tailscale SSH, userspace networking, exit-node
support, and the bundled CLI. Twice I broke Tailscale SSH and had to recover
with the SSH key I had baked into the Valetudo image.
The old cutover path made that failure mode worse. It used the production
identity to replace the production binary. If
/data/tailscaled
disappeared
while the deploy was connected through it, the deploy could strand itself.
Automation structure
There is a repo convention behind this automation: the Codex.app job is not the
task definition. The app provides the schedule, workspace, model, automation
memory, and inbox item
1
. The repo carries the durable instructions.
The actual Codex.app prompt is just the pointer:
Run the homelab Valetudo Tailscale upgrade assessment. Read
docs/automations/README.md
and
docs/automations/valetudo-tailscale-upgrades.md
, follow their guardrails,
and open an inbox item with the required summary.
I learned that convention earlier the same day. I had asked Codex to make a
daily docs deploy job, and it put too much of the task body into the Codex.app
prompt. I pushed back and made the structure legible to all future agent runs by
putting it in the repository: scheduled automation behavior belongs in
docs/automations/
, while the harness prompt stays slim and points back to the
repo doc.
That puts automations in the same category as skills. They can be versioned in
git, reviewed in PRs, changed by anyone working in the repo, and reused by the
next agent without copying a long prompt through the app UI. A PR can update the
automation contract next to the code and runbook it depends on. Over time, these
docs become points of shared leverage instead of private state attached to one
scheduled job.
The Valetudo Tailscale automation follows the same split. The scheduled run can
read release notes, inspect upstream source, compare build tags, build a local
linux/arm64
candidate, open a PR, update automation memory, and open an inbox
item. It cannot deploy to Loki. I wanted that boundary because a bad deploy can
remove the access path the deploy itself is using.
The deploy path lives in a different place. Codex had already built a repo-local
Go tool under
hld/valetudotailscale/
, then reworked it into the repo’s
hld
2
pattern. The tool gives the runbook a narrow command surface for the
risky parts of the deploy, and the runbook says when those commands are allowed
to run.
The canary came out of that work. In the original discussion, I asked whether we
could stage a new build and test SSH before the destructive cutover. Codex laid
out the tradeoff: the same Loki identity cannot run two
tailscaled
daemons
against the same state at once, but a second Tailscale node can show whether the
new binary can boot, join the tailnet, and accept Tailscale SSH. I picked
loki-canary
, then sketched the phases: build, copy into a canary slot over the
production identity, boot canary with separate state, test canary SSH, back up
production, promote over the canary identity, verify production, then stop the
isolated canary daemon.
That became a small command set that orchestrates each step in the deploy. The
first canary attempt also improved the tool. OpenSSH
scp
tried SFTP, legacy
scp
did not exit cleanly against Loki, and the tool ended up streaming the
binary over SSH into the canary slot. Codex also added the Tailscale
--accept-risk=lose-ssh
flag required for the canary auth flow and isolated
known-hosts handling for the new canary identity.
Checked-in docs
Inside the repo, the automation doc lives at
docs/automations/valetudo-tailscale-upgrades.md
, and the deploy runbook lives
at
docs/valetudo-tailscale-deploy-runbook.md
.
Here is the automation doc itself, with the private tailnet hostname redacted:
Automation doc at docs/automations/valetudo-tailscale-upgrades.md.
Valetudo Tailscale Upgrades Automation
The Valetudo Tailscale upgrades automation evaluates whether the custom
Tailscale binary used on Valetudo-managed robot vacuums should move to a newer
Tailscale release. Its canonical task definition lives in this file; the Codex
harness automation should stay slim and should point back here instead of
duplicating this runbook.
The automation must read
docs/automations/README.md
before running and
follow the repository-wide automation conventions there.
Schedule
Run once per week against the homelab repository.
Scope
This automation owns only the custom Valetudo Tailscale binary maintained by
hld/valetudotailscale/
and exposed through
go run ./hld/cmd/valetudo-tailscale-deploy
.
The manual deploy process is documented in
docs/valetudo-tailscale-deploy-runbook.md
.
The dependency sweep automation must not update this pin. If another
automation or Dependabot proposes a Valetudo Tailscale version change, treat
that pull request as out of scope for dependency auto-merge and require human
review.
Current Behavior
The current default command builds Tailscale
v1.90.8
for
linux/arm64
using
./build_dist.sh tailscale.com/cmd/tailscaled
and deploys it to the
production Loki tailnet identity at
/data/tailscaled
.
The build is intentionally small, but it must preserve:
Tailscale SSH for root access to the vacuum over the tailnet;
userspace networking behavior needed by the vacuum environment;
exit-node behavior, including the code paths needed for routing and
advertising/serving exit-node traffic;
the bundled CLI path enabled by
ts_include_cli
, which keeps local
operational inspection possible on a constrained device.
Candidate Selection
Fetch origin and inspect the latest
origin/trunk
.
Read
docs/automations/README.md
and this file.
Identify the current Tailscale tag in
hld/valetudotailscale/build/source.go
.
Find the latest stable upstream Tailscale release from authoritative
Tailscale sources.
Read the release notes for every release between the current tag and the
candidate tag.
Inspect upstream build-tag behavior for the candidate release, including
build_dist.sh
and source files that define or consume
ts_omit_*
tags.
Compare the current and candidate upstream extra-small omit sets. Generate
each set from the matching upstream checkout with
go run ./cmd/featuretags --min --add=osrouter
, which is the feature-tag
basis for
build_dist.sh --extra-small
.
Identify every omit tag added or removed from that extra-small baseline
between the current and candidate tags.
Skip the update and report why if release notes are missing, upstream tag
semantics are unclear, the candidate has known regressions for Linux ARM64,
userspace networking, SSH, or exit nodes, or the candidate is a major behavior
change rather than a routine Tailscale update.
Build-Tag Safety
Before proposing an update, reason explicitly about the omit tags in
hld/valetudotailscale/build/tags.go
.
The build must keep
ts_include_cli
.
The custom omit list should preserve the original extra-small intent wherever
it is safe to do so. When upstream adds new extra-small omit tags, add them to
hld/valetudotailscale/build/tags.go
unless the tag removes, or appears to
remove, behavior required by this runbook. If a new extra-small omit tag is
not taken, the run summary must say why.
Do not add omit tags that contain or imply any of these feature areas:
ssh
;
netstack
;
route
or
router
;
exit
.
If upstream renames build tags, removes a tag, adds a new default omission, or
changes how SSH, userspace networking, routing, or exit-node behavior is
built, stop and open an inbox item instead of making a pull request.
Do not rely on the local validator alone for this decision. The validator
checks tag names, but the automation must also read upstream feature
descriptions and source references for new omit tags to catch renamed or
indirect feature areas.
Compile success alone is not enough to prove the update is safe. The
automation must connect the release-note and source-code review to the feature
requirements above.
Build-Only Check
For a candidate version, run a local build-only check:
mise exec -- go run ./hld/cmd/valetudo-tailscale-deploy build --tailscale-tag <candidate-tag>
The check must build a
linux/arm64
tailscaled
binary and must not copy
anything to a vacuum, activate a binary, or reboot the device.
Do not run the deploy path from this automation. Deployment to the vacuum
requires human approval after review because a bad binary can break both
Tailscale SSH access and exit-node behavior.
Canary Deploy
After human approval, test a candidate on the vacuum as an isolated canary
before replacing the production binary:
mise exec -- go run ./hld/cmd/valetudo-tailscale-deploy canary deploy --tailscale-tag <candidate-tag>
The canary path must only copy the build to
/data/tailscaled.canary
, start
it with
/data/tailscale-canary-state
and
/tmp/tailscale-canary
, inspect
canary logs, and request a separate
loki-canary
tailnet identity. It must
not replace
/data/tailscaled
, write
/data/tailscaled.bak
, use the
production
/data/tailscale-state
, or reboot the vacuum.
If the canary identity is not authenticated, the command should print a
Tailscale auth URL. Open that URL for a human to approve, then test SSH to the
canary identity with
canary ssh
before considering a production cutover.
The production cutover phase is manual and must follow the deploy runbook:
prod backup
,
canary promote
,
prod ssh
,
prod logs
, then
canary stop
only after the promoted production identity looks good.
Pull Requests
If the candidate looks safe and the dry-run build passes, open a pull request
that updates:
the default Tailscale tag in
hld/valetudotailscale/build/source.go
;
hld/valetudotailscale/build/tags.go
when upstream added safe omit tags
that preserve the extra-small intent;
the documented custom Tailscale version in
docs/vacuums.md
;
this runbook if the reasoning changes any safety rule.
The pull request must include
codex
,
A-iot
,
A-deps
, and
C-automation
labels.
Do not enable auto-merge for Valetudo Tailscale upgrade pull requests. Assign
the pull request to
lopopolo
and explain that human review is required
before the updated binary can be deployed to the vacuum.
Summary
Open an inbox item after every run with:
the current Tailscale tag and latest candidate tag;
whether an update was skipped or proposed;
release-note findings relevant to SSH, userspace networking, and exit-node
behavior;
build-tag reasoning, including why the omit list still preserves required
features;
the extra-small omit-tag delta between the current and candidate tags,
including which new omit tags were added or intentionally skipped;
build-only result and binary size if a candidate was built;
any pull request created;
any manual follow-up needed before deployment.
The scheduled automation can prepare a PR only. It reads release notes, inspects
upstream build-tag semantics, runs a build-only check, and explains why the
feature set still preserves Tailscale SSH, userspace networking, exit-node
behavior, and the bundled CLI. The deploy path is a separate runbook with a
canary phase and a production cutover phase.
A polished run
The
v1.96.4
assessment also changed the automation doc. My original custom
build started from Tailscale’s
--extra-small
intent and then selectively kept
the features the vacuum needs. At first, Codex updated the version and preserved
the existing omit set. I pushed on that because the job expectation was
stronger: compare the upstream extra-small baseline between releases and carry
forward any new safe omissions.
The runbook now requires future runs to generate the current and candidate
extra-small omit sets from the matching upstream checkouts:
go
run
./cmd/featuretags
--min
--add=osrouter
For this upgrade, that comparison from
v1.90.8
to
v1.96.4
found six new safe
omissions and removed none:
ts_omit_cachenetmap
ts_omit_colorable
ts_omit_completion_scripts
ts_omit_conn25
ts_omit_qrcodes
ts_omit_webbrowser
Codex added all six. It also documented the rule that future runs must add safe
new extra-small omit tags or explain why they were skipped.
Codex added a second Tailscale identity for the same physical vacuum:
loki-canary
. The candidate binary is copied to
/data/tailscaled.canary
,
started with separate state in
/data/tailscale-canary-state
, and uses a
separate runtime directory under
/tmp/tailscale-canary
. It does not overwrite
/data/tailscaled
, touch the production state directory, or reboot the vacuum.
Human-in-the-loop work ended up being two operations:
I authenticated the canary identity to the tailnet.
I approved the production deploy after Codex built, staged, logged, and
tested the canary.
After those gates, Codex ran the runbook end to end. Production had
/data/tailscaled.bak
before promotion, and the canary state stayed in
/data/tailscale-canary-state
for the next upgrade.
The deploy also improved the tool.
prod backup
exposed a bug in the helper:
remote scripts were being passed through
ssh ... sh -c <script>
, which broke
on shell syntax like
if ... then ... fi
. Codex patched the helper to send
remote scripts over stdin to
sh -s
, added focused tests for the behavior,
reran validation, and then continued the deploy. I did not have to stop and fix
the tool by hand before the deploy could continue.
After the cutover, I asked Codex to put the deploy result on the PR. It
commented with the canary result, production cutover, SSH checks, backup, logs,
and rollback path, so the version bump also carries a record of the deploy.
The deploy runbook sequence:
sequenceDiagram
autonumber
participant App as Codex.app automation harness
participant Human
participant Codex
participant GitHub as GitHub PR
participant Prod as loki prod identity
participant Canary as loki-canary identity
participant Loki as Loki filesystem and processes
App->>Codex: trigger scheduled upgrade assessment
Codex->>App: read prior automation memory
Codex->>Codex: inspect release notes, omit tags, and candidate build
Codex->>GitHub: open version-bump PR
Codex->>App: persist assessment memory
Codex->>Codex: build v1.96.4 linux/arm64
Human->>Codex: approve canary deploy
Codex->>Prod: copy binary to /data/tailscaled.canary
Prod->>Loki: start canary daemon with separate state and runtime
Prod-->>Codex: canary logs and auth URL if needed
Human->>Canary: authenticate loki-canary in the tailnet
Codex->>Canary: canary ssh
Canary-->>Codex: SSH reachable
Human->>Codex: approve production cutover
Codex->>Prod: prod backup
Prod->>Loki: copy /data/tailscaled to /data/tailscaled.bak
Codex->>Canary: canary promote
Canary->>Loki: stop prod daemon, copy canary binary, start prod daemon
Codex->>Prod: prod ssh and prod logs
Prod-->>Codex: production running v1.96.4
Codex->>Prod: canary stop
Prod->>Loki: stop isolated canary daemon and preserve canary state
Codex->>App: persist deploy memory
Human->>Codex: ask for PR deploy summary
Codex->>GitHub: comment deploy details on version-bump PR
Codex->>App: persist PR-comment follow-up memory
Deploy runbook at docs/valetudo-tailscale-deploy-runbook.md.
Valetudo Tailscale Deploy Runbook
This runbook covers the custom Tailscale binary on Loki, the Valetudo-managed
robot vacuum. The deploy tooling lives at
go run ./hld/cmd/valetudo-tailscale-deploy
.
The default production identity is
loki
. The canary identity is
loki-canary
.
Safety Rules
Treat production cutover as destructive. Do not run it until the canary
identity has been authenticated and Tailscale SSH to the canary identity
works.
Use the production identity for canary staging. Canary staging may overwrite
/data/tailscaled.canary
, restart the isolated canary daemon, and write
/data/tailscale-canary-state
plus
/tmp/tailscale-canary
.
Canary staging must not write
/data/tailscaled
,
/data/tailscaled.bak
,
/data/tailscaled.new
, or
/data/tailscale-state
, and must not reboot
Loki.
Run
prod backup
immediately before
canary promote
. The promotion command
refuses to run unless
/data/tailscaled.bak
already exists.
canary stop
runs over the production identity, stops only the isolated
canary daemon, and preserves
/data/tailscale-canary-state
for future
canary reuse.
Command Reference
All examples should be run through
mise
from the repository root:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
<
comman
d
>
Command
Identity Used
Purpose
build
none
Build the candidate locally without remote mutation.
canary deploy
production
Build, copy to canary slot, start canary, log, auth.
canary start
production
Restart the existing canary slot without rebuilding.
canary logs
production
Tail isolated canary logs.
canary auth
production
Re-run
tailscale up
for the canary identity.
canary ssh
canary
Check Tailscale SSH to the canary identity.
prod backup
production
Copy
/data/tailscaled
to
/data/tailscaled.bak
.
canary promote
canary
Stop prod daemon, promote canary binary, start prod logs.
prod logs
production
Tail production Tailscale logs.
prod ssh
production
Check Tailscale SSH to the production identity.
canary stop
production
Stop isolated canary daemon, preserving canary state.
The root command performs a direct production deploy. Prefer the phased
commands in this runbook for Loki.
Canary Phase
Build the candidate locally:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
build
\
--tailscale-tag
<
candidate-ta
g
>
Stage and boot the isolated canary over the production identity:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
canary
deploy
\
--tailscale-tag
<
candidate-ta
g
>
This copies the build to
/data/tailscaled.canary
, starts it with
/data/tailscale-canary-state
and
/tmp/tailscale-canary
, tails the
canary log, then runs:
tailscale
up
--ssh
--hostname=loki-canary
--accept-dns=false
If Tailscale prints an auth URL, open it and authenticate the canary node.
Inspect logs again after authentication:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
canary
logs
Check Tailscale SSH to the canary identity:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
canary
ssh
Stop here unless the canary logs and SSH check look good.
Production Cutover
Run these steps only after explicit human approval.
Back up the current production binary over the production identity:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
prod
backup
Promote the canary binary over the canary identity:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
canary
promote
This stops the production
/data/tailscaled
process, copies
/data/tailscaled.canary
to
/data/tailscaled
, refreshes the
/data/tailscale
CLI symlink, starts production Tailscale with
/data/tailscale-state
, and tails
/tmp/tailscale/tailscaled.log
.
Check Tailscale SSH to the promoted production identity:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
prod
ssh
Inspect production logs:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
prod
logs
If production looks good, stop the isolated canary daemon over the
production identity while preserving the canary state directory:
mise
exec
--
go
run
./hld/cmd/valetudo-tailscale-deploy
canary
stop
Recovery Notes
If canary staging fails, production should still be untouched. Use
canary logs
and
canary start
for inspection and retry.
If promotion fails after
prod backup
, the previous binary should be
present at
/data/tailscaled.bak
. Prefer the canary identity or local robot
access for manual recovery.
Do not delete
/data/tailscale-state
; it contains the production tailnet
identity and Tailscale SSH state.
The deployment outcome was pleasantly boring. The canary reported
1.96.4-t41cb72f27
. Tailscale SSH to
loki-canary
passed. Production was
backed up, and the backup reported
1.90.8
. The canary binary was promoted to
/data/tailscaled
. Production restarted as
1.96.4
, Tailscale SSH to
loki
passed, logs reached
Running
, and the old production binary stayed available
at
/data/tailscaled.bak
.
The next Tailscale upgrade has a standing canary path. It is documented,
executable, tested, and separated from the scheduled assessment automation.
