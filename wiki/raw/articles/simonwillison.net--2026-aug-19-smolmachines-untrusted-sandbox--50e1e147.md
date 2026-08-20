---
title: "smolvm as a sandbox for untrusted Python & JavaScript"
url: "https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/"
fetched_at: 2026-08-20T10:00:46.508308+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# smolvm as a sandbox for untrusted Python & JavaScript

Source: https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/

I tasked Claude Fable 5 running in Claude Code for web with the following research task:
Put https://smolmachines.com through its paces as a fast secure sandbox. Explore what it would take to use this to run untrusted Python and JavaScript code in a way that is limited in what RAM and CPU time it can take up (protection against "while true") with no network access and filesystem access only to designated files
Goal is to be able to use this to execute user-provided tasks for things like data transformations
It quickly ran into a problem: the Claude Code for web environment can't run
smol machines
. Quoting the
notes it wrote
:
This Claude Code container: Linux 6.18.5-fc-v20 (itself a Firecracker guest), 4 vCPU, 15GB RAM.
No /dev/kvm, no vmx/svm CPU flags
→ no nested virt.
smolvm machine run
fails as expected: "kvm not available".
Plan B: GitHub Actions ubuntu runners DO expose /dev/kvm → run the real test battery via a temporary workflow on this branch, collect logs, remove workflow in final commit.
And Plan B is
what it did
, installing smolvm and running
these tests
directly in a GitHub Actions runner against that branch.
That was a creative solution to the environmental limits posed by Claude Code for web. Another example of Fable being
relentlessly proactive
.
