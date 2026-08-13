---
title: "Now we have a timeline of the OpenAI accidental attack against Hugging Face"
url: "https://simonwillison.net/2026/Aug/7/openai-timeline/"
fetched_at: 2026-08-13T10:19:21.551519+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Now we have a timeline of the OpenAI accidental attack against Hugging Face

Source: https://simonwillison.net/2026/Aug/7/openai-timeline/

Now we have a timeline of the OpenAI accidental attack against Hugging Face
7th August 2026
OpenAI gave a last-minute presentation at the Black Hat security on Wednesday about “the Hugging Face Incident” (
previously
on this blog).
The video
was published yesterday. It’s short and information dense and well worth watching, in particular because it provides full details of what happened and how things played out inside OpenAI. I’ve used the video to construct the timeline below.
Here’s the timeline. My favourite detail is at the end: OpenAI found out that they were responsible for the attack on Hugging Face when they reached out to ask to have their credentials revoked (after their internal investigation) and learned that they had been revoked already since they were used in that attack!
May 7
: OpenAI starts a new training run for an experimental, unreleased model. (
Did they mean an evaluation run? No, at
10:14
they clarify “we kick off a new reinforcement learning run to train a next generation frontier model”, and they later mention a “reward signal to judge how well they’re doing”, so this really was about training a new model, not evaluating one that was already trained.)
May 8
: An agent is accidentally given an impossible task involving a Google Drive link despite no internet access). It tries attacking the Artifactory packaging service, fails, but discovers it can
write files into Artifactory
.
A few days later
: A different agent gets stuck on a task because a key file was accidentally omitted. It tries to “reach out to another agent” by writing a note into Artifactory asking if anyone has the file.
Following days
: More agents discover this new informal message board while browsing Artifactory’s file listings, and start reading and writing messages.
May 26
: Agents successfully execute an
SSRF attack on Artifactory
for the first time, gaining indirect internet access by having Artifactory fetch external content for them.
June 11
: OpenAI start training a new “highly persistent” experimental model. It has access to Artifactory and can benefit from the messages left by privous models.
June 26
: Agents find and exploit a
zero-day RCE on Artifactory
(via a legacy token-refresh endpoint flaw). They use an administrative token to install a Groovy plugin that lets them execute commands.
July 4
: The resulting agent activity overloads Artifactory and causes an
outage
. OpenAI revokes the compromised credentials, deletes the messages, patches the zero-day, and reports the vulnerability to the vendor.
July 8
: Agents find
a new way to communicate via an unauthenticated WebDAV endpoint
, using directory names in Artifactory’s remote cache.
July 8–19
: Attacks on
OpenAI’s own infrastructure
. The agents found an “external organization credential” in a public archive of leaked Pastebin posts, then validated that credential and shared its location on the messageboard. They then used write access to this “Organization 1” to stage data used in subsequent attacks on OpenAI infrastructure. They compromised Artifactory for a second time with
a new zero-day
. The agent uploaded a malicious Ruby target to Organization 1’s staging repository, then requested that package through Artifactory in a way that caused it to be treated as Ruby dependency
for the repository
. Then they exploited a JRuby deserilaization time-of-check/time-of-use bug to get remote code execution against Artifactory.
I’ll quote
the next bit in full
because
wow
:
The agents have remote code execution in Artifactory, which is running in a container-as-a-service environment. The agents privilege-escalate locally by exploring their local environment and determining that the Linux kernel version of the machine they are running on had a very recent CVE. They download the exploit for the CVE, customize it to succeed on the machine, and privilege-escalate to root on the local machine
using this known Linux kernel privilege escalation CVE
— in this case,
pte_physroot
. Once they have root on a single machine, agents rapidly escalate privileges and move laterally throughout the container-as-a-service infrastructure environment. In particular, agents are using the message board consistently to share credentials, techniques, and progress, and they’re able to effectively leverage their concurrency and parallelism to move quite rapidly. They
obtain IAM credentials via IMDS
. They exploit Kubernetes service account misconfigurations, in particular over-permissioning of specific service accounts, and
they harvest cluster credentials, including Azure Key Vault
. Agents eventually obtain cluster admin on the cluster and associated credentials.
Hugging Face
told the next bit of the story
already. The agents found a Modal-hosted insecure app with a weak API key, then used that to stage an attack against Hugging Face. They chained together a an HDF5 arbitrary-file-read bug (to explore files and steal credentials) and a Jinja template-injection RCE to go from single-pod code execution to
cluster admin across multiple Hugging Face clusters
in under 13 hours.
July 16
: Hugging Face
disclosed they had detected an attack
from autonomus AI agents. OpenAI contacted Hugging Face to ask if they were affected by it!
July 19
: OpenAI identified the attack against Artifactory and started investigating the internal privilege escalation, and linked that to the cyber-gym escalations. They started revoking affected credentials.
July 20
: OpenAI reached out to Hugging Face for help to revoke the Hugging Face credentials they found in their investigation. Hugging Face told them they were
already revoked
... and that’s when OpenAI realized that the Hugging Face breach was the same incident!
