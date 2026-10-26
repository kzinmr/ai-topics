---
title: "Gheist: attempted scaled abuse of stolen GitHub tokens"
source: https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles
author: Wiz
type: article
collected: 2026-10-26
published: 2026-10-25
sha256: 860ba0f76c03d4673577806d508cdcca5066d14aefff3cab190ab4c9f217396a
---

GitHub Actions and GitLab runner credential files.

The Kubernetes service account token.

However, this job is buggy: it looks for the wrong runner key file, its URL-credential regex is broken, and it doesn't collect GCP or Azure tokens.

GitHub's approval hold and private repositories

Since July 28, 2026, GitHub has 
held potentially malicious workflow runs
 in public repositories until a collaborator approves them. Every public Gheist run we checked, across all variants including the self-hosted job, sits at action_required. 
The control worked, and the malicious payloads never ran.

Unfortunately, that hold doesn't apply to private repositories or GitHub Enterprise Server. There, GitHub audit logs show runs on 
ci-sync-*
 branches completing and then being deleted by the 
gheist
 user agent. CloudTrail shows the organizations' own workflows running on those branches and assuming AWS roles, which proves Actions executed without approval.

For defenders, that last signal finds Gheist without any GitHub logs, as shown below.

Other activity on the same accounts

This campaign is leveraging compromised GitHub access. The same accounts are used by other actors and campaigns, which demonstrates how compromised credentials can move throughout the threat actor ecosystem. We've observed overlaps with the following campaigns:

Lure repositories (malware distribution).
 On October 6, 391 accounts renamed about 1,461 repositories to cracked-software lures like fl-studio-crack and solana-sniper-lite. The rename wiped 610 
ci-sync
 branches as a side effect. 166 of these accounts never appear in Gheist activity, so the pool is larger than Gheist's footprint.

Free compute (cryptomining).
 On October 18, 25 Gheist accounts each created a "Windows RDP Runner" repository within nine minutes, attempting to abuse GitHub Actions for free compute cycles.

PolinRider.
 Some victims appear to be infected with 
PolinRider
, the DPRK-linked malware that hides JavaScript in build config files and force-pushes back-dated commits. On October 19 and 20, three victims re-pushed their Gheist commits with a loader appended to 
vite.config.js
 behind hundreds of whitespace characters, and in two cases an api.js that package.json runs before every dev and build.

Megalodon.
 57 accounts from Gheist's first phase were also victims of 
Megalodon
 in May.

The credential sources we could trace fit this picture: infostealer logs, and tokens exposed in earlier supply-chain compromises such as the Trivy compromise in March.

Note: Gheist is distinct from 
GhostAction
, which uses different workflow files and exfiltrates secrets to 193.32.204[.]199.

Which actions should security teams take?

Hunt

Look for branches named 
ci-sync-
 followed by six random characters, where the only change is a new file at 
.github/workflows/sync-check.yml
 with the commit message 
ci: sync config
.

In GitHub audit logs, look for workflow runs on 
ci-sync-*
 branches that were deleted within a minute of completing, and for any activity from the user agent 
gheist
.

If your workflows authenticate to the cloud with OIDC, check cloud audit logs for role assumptions or token exchanges whose subject includes a 
ci-sync-
 branch. That shows GitHub Actions ran on an attacker branch, even if you don't collect GitHub logs.

On self-hosted runners, look for the files 
.gdmp_pat
, 
.gdmp_patg
 and 
.gdmp_sweep
, and the string 
gdmp-pivot
 in job logs.

Respond

Rotate every repository, organization and environment secret available to an affected repository. Deleting the run or the branch doesn't undo the exposure.

Revoke the tokens that pushed the commits, and check their owners' devices for infostealers.

If a 
ci-sync
 branch ran on a self-hosted runner, treat the host and its instance role as compromised.

Don't approve held 
sync-check
 runs, and don't run code from 
ci-sync
 branches.

Harden.
 Require reviewers on environments with production secrets, scope OIDC trust policies to protected branches or environments, use GitHub Apps or short-lived fine-grained tokens instead of personal access tokens, and run self-hosted runners as ephemeral hosts without Docker socket or unrestricted metadata access.

Indicators of compromise

User agent 
gheist

Branch 
ci-sync-
 followed by six characters, matching 
^ci-sync-[0-9a-z]{6}$

Commit message 
ci: sync config
 adding only 
.github/workflows/sync-check.yml

Markers 
toJSON(secrets) }}' | base32 -w 120
 and 
===== gdmp-pivot:
; files 
.gdmp_pat
, 
.gdmp_patg
, 
.gdmp_sweep

Workflow blob SHAs: 
f3da2b8b357dcda02fd455d314be2a95007516a6
 (plain), 
d09535857a741bbb976bdc084a9a021713133291
 (timeout), 
1dc5af9cce950aad1eb1546ecce8565b117540c4
 (separator), 
c665b778b2d822453293003e7ca0bbb2cb08e39d
 (self-hosted job). Environment-matrix variants differ per repository.

How can Wiz help?

The 
Threat Center advisory
 includes an Event Explorer query covering planted commits, Gheist activity in GitHub audit logs and cloud role assumptions from attacker branches. Wiz Defend detects the activity with rules including "New Workflow Completed And Deleted In Short Time Span", "Workflow Pushed With Secret Dump" and "Commit Created With Known Malicious Commit Message".

Tags

#
Research
