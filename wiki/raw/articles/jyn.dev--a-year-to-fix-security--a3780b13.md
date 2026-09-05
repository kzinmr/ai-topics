---
title: "we have a year to fix security everywhere"
url: "https://jyn.dev/a-year-to-fix-security/"
fetched_at: 2026-09-05T10:00:48.761028+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# we have a year to fix security everywhere

Source: https://jyn.dev/a-year-to-fix-security/

GLM 5.3-flash
released last week
, and that means
Project Glasswing
and
Daybreak
are running out of time.
Cheap models capable of dangerous hacking are now available to anyone, without the normal safeguards for refusing malicious actions.
We need to fix vulnerabilities across the industry so that we aren't caught unawares.
And for one of the first times in computing history, we have the ability to!
We can use frontier LLMs that move faster than a human to find and fix these issues in the time we have left.
The hard remaining part is deploying the fixes.
This probably sounds like nonsense words or hysterical overreacting to most people, so here's what that means:
"GLM" is a kind of LLM (AI). The GLM family is
open-weight
, which means anyone can download and run the models.
"flash" means that it is
cheap
and
fast
to run, compared to most "frontier" models. "cheap" is relative, but think around 5-15k USD in hardware to run it locally.
"frontier" here means that the LLM is "close to the frontier of what AI is currently able to achieve".
Project Glasswing and Daybreak are initiatives to use LLMs to fix security issues across the tech industry.
"malicious actions" includes things like hacking infrastructure and telling people how to build pipe bombs.
The rest of this post is about what makes me so sure this is an imminent threat, and what we can do in response.
GLM
GLM 5.3-flash can be downloaded and modified by anyone in the world.
The GLM ("General Language Model") family is developed by Z.ai Co. (formerly Zhipu AI), which is a Chinese AI lab.
When the model is hosted by Z.ai, it comes with restrictions required by law:
Z.ai releases its models
publicly on the internet
("open-weight" models).
Once it does so, organizations such as
DeAlignAI
release
"abliterated" models
with their task refusals surgically removed.
DealignAI says the abliterated model scores 0% on
Harmbench-320
,
which tests whether models refuse to complete tasks about disinformation, cybercrime, biological weapons, and other illegal acts such as building a pipe bomb.
In other words, this model is willing to do basically anything.
Flash
GLM 5.3-flash is possible to run locally on stock consumer hardware.
"Flash" is mostly an advertising term—it's relative to other models, not a specific technical approach.
Various people online have run benchmarks of GLM 5.3-flash locally.
Here's
one example
showing around 20 tokens/second on a ~6k USD NVIDIA GPU.
On September 22, Apple is releasing the M5 Mac Studio with 256 GB of unified memory.
"Unified memory" means it can be shared between the host operating system and the GPU.
That's more than enough to run 5.3-flash, and it will probably get around 30 tokens/second once it releases.
For 256 GB, the price starts at around $9,500.
Further improvements in software can get half-again the throughput
through
changes to the model decoder
.
If we extrapolate that to the M5, that would put the total throughput at around 45 tokens/second.
45 tokens/second is enough to write this snippet of code in 3 seconds:
⚠️  LLM generated code
from
pathlib
import
Path
import
hashlib
def
digest
(
path
:
Path
)
->
str
:
hasher
=
hashlib
.
sha256
(
)
with
path
.
open
(
"
rb
"
)
as
file
:
while
chunk
:=
file
.
read
(
1024
*
1024
)
:
hasher
.
update
(
chunk
)
return
hasher
.
hexdigest
(
)
def
main
(
)
->
None
:
import
sys
if
len
(
sys
.
argv
)
<
2
:
raise
SystemExit
(
"
usage: hash.py FILE...
"
)
for
name
in
sys
.
argv
[
1
:
]
:
path
=
Path
(
name
)
try
:
print
(
f
"
{
digest
(
path
)
}
{
path
}
"
)
except
OSError
as
error
:
print
(
f
"
{
path
}
:
{
error
}
"
,
file
=
sys
.
stderr
)
if
__name__
==
"
__main__
"
:
main
(
)
In other words, it's not just possible to run this model locally, it's possible to do so from an ordinary individual's savings, and use it round-the-clock at high speeds.
Frontier
GLM 5.3-flash is very close to the abilities of the best AIs we have made.
The AIs we've made are already finding and exploiting real security vulnerabilities in the wild.
The AIs we make in the future are going to get more and more capable.
GLM 5.3
scores
84.5% on CyberGym and 54.4% on ExploitBench.
We don't have data for 5.3-flash directly, but it will probably be around the same or a bit lower.
Abliterated models will be slightly lower again.
CyberGym measures
real world vulnerabilities
that have been found and patched by open source projects in the past.
In other words, 84.5% of vulnerabilities in this representative sample would have been reproduced by GLM 5.3 just by looking at publicly available source code and a CVE description.
ExploitBench measures whether the model can actually use vulnerabilities to cause harm.
It scores on a sliding scale that gives partial points for partial exploits, with the final step being arbitrary code execution.
For comparison, the leading ("frontier") model on ExploitBench is GPT-6 Astra (100%), with GPT-5.6 Sol as the runner-up with 78.5% .
The leading model on CyberGym is ... GLM-5.3.
The runner-up is GPT-5.6 Sol with 83.6%.
OpenAI hasn't released numbers for Astra on CyberGym yet, but once they do it'll likely beat GLM 5.3.
You might think these are just synthetic benchmarks,
but security experts are reporting that they
can no longer be competitive in security challenges
without the assistance of an LLM.
We don't have many standard benchmarks for remote-code and reverse-engineering exploits,
but we do have evidence of GPT 5.6-Sol
exploiting infrastructure in the real world
, without human involvement.
I think it is quite likely that people will be able to point GLM 5.3-flash at the open internet—real services, running real infrastructure—and it will be able and willing to find and exploit vulnerabilities.
This Is Bad
Together, this means:
Just about anyone can run GLM 5.3-flash if they have a bit of savings, continuously, day and night.
Just about anyone can use GLM 5.3-flash for just about any task, including to malicious ends.
GLM 5.3-flash is so good at those tasks that human involvement in those tasks can be negligible.
As a result,
we are now in a world where cybersecurity attacks can be run in a
for
loop
.
Now, the frontier US labs have been aware of this coming for a while and have been working on getting security patches out.
Project Glasswing
and
Daybreak
have been working with companies, foundations, governments, and NGOs across the tech industry to find and fix vulnerabilities using frontier models before this capability was open-sourced.
They've done a lot of good, and I'm very glad that this was funded.
Both have been sold as products after the initial funding, which feels a little bit sketchy at best, but they're at least giving out free credits to security organizations.
However, we are running out of time.
And despite the good that Daybreak and Glasswing have done, the hard part is
deployment
, not fixing the bugs themselves.
Critical systems often require physical access or carefully planned staged rollouts to avoid downtime, both of which delay deploying patches.
It doesn't help to have a patched Linux kernel if your power grid is running Windows Server 2012.
There are some caveats: the 1.5 speedup might not be so high on GLM 5.3-flash; abliterated models might be worse on malicious tasks they weren't trained on; it might be hard to go from "break this" to an exploit without extensive human involvement.
But those things are temporary and models keep getting better.
Historically, GLM has lagged around 3-6 months behind OpenAI and Anthropic, and I think it's likely we'll see an Astra-level GLM model by this time next year.
And when that happens, there's going to be a high risk of successful cybersecurity attacks on public or private infrastructure.
We may be getting a lesson on
brownouts
sooner than we'd like.
In general, attackers are getting more capable faster than defenders are improving their posture.
Even if models stop scaling so fast (which they currently show no sign of doing),
it's only a matter of time before they get capable enough to start exploiting these vulns.
We need to act now, the sooner the better.
What do we do?
Things are getting weird, and scary, very quickly.
We need to act with urgency, not panic.
Some things we can do:
Governments and regulatory agencies
Scanning with frontier models is relatively cheap and does not need major incentives.
What does need incentives is
deployment
and
remediation
, and requiring organizations to look at their security practices in the first place.
On the current policy trajectory, the biggest risk is a heap of untriaged warnings that never get fixed.
If you're in a position to make policy, the following would help:
Fund security engineering, preferably with flexible grants that can be used for hiring or technology products as decided by the organization.
Create mandates and incentives for improving security, especially for frequent penetration testing.
Encourage using frontier models with human oversight for that pentesting.
Encourage increased airgapping and discourage over-the-air updates: updates should be frequent but require physical access.
For systems where airgapping isn't feasible, incentivize frequent, signed, and tested deployments.
Penalize
not
investigating and revising security posture regularly, with increased penalties if a hack happens as a result.
Require findings to be fixed within a risk-based deadline from discovery, with federal funding for the fixes.
Both carrot and stick.
Some specific things that may be worth looking into:
Be especially sure to fund local governments and hospitals, which are unlikely to get this funding through other channels.
EO 14409
is not enough because it's unfunded and voluntary.
For banks, extend DORA's
TLPT
in the EU and
FTC
/
OCC
/
NCUA
in the US.
TLPT should increase the frequency and coverage of penetration testing.
NCUA currently only suggests pentesting; upgrade it to a mandate.
The FTC doesn't mandate pentesting if the financial institution has "continuous monitoring": it should be unconditionally mandated.
For power companies in the US, adopt guidelines similar to
NERC Critical Infrastructure Protection
at the state and local level, including for distribution systems and others that aren't currently regulated, not just for the highest-risk and largest systems.
Create federal grants for implementing those guidelines.
Extend NERC-CIP to require active testing for all systems, not just high-impact systems.
Change NERC-CIP and the EU's
NIS2
/
Network Code on Cybersecurity
to increase the frequency of required tests.
Telecoms in the US are currently high risk and have no unified mandatory cybersecurity risk standards.
Create one and enforce it, using existing regulations for banks and power companies as a starting point.
Across the board, require security postures to be updated
frequently
.
Mandating specific models or providers will become outdated as new models are released.
This is a rapidly changing field and defenses that were effective 12 months ago may not be effective in a year as threat models (both senses) change.
Mandate testing and accountability, not specific techniques.
Banning GLM 5.3-flash weights from being hosted anywhere in the US or Europe will be hardly any use in the short term,
and no use at all in the long term.
In the short-term, it will just pop up again on file-sharing sites; you'll have no more luck killing it than killing piracy.
In the long-term, some other lab will release another model that's just as capable.
Blanket-banning access to Mythos or Astra will actively make things worse; it will remove defenders' most powerful tool at exactly the moment they need it most.
Instead, restrict access to approved organizations and individuals, as frontier labs are already doing.
This likely doesn't need new policy unless a lab shows signs of breaking ranks.
Banning the sale/export of new GPUs or large unified memory will extend the year-long window for a bit but won't help long-term.
It can't do anything about existing hardware, and it will be massively unpopular.
Memory in particular is hard to regulate because
everything
uses it, not just specialized AI systems.
In general, prioritize policies that address
triaging
and
fixing
security findings.
Findings are getting very cheap; the fixes are not.
Companies and open source foundations
Take advantage of the (literal) billions of dollars that are flooding the industry to improve safety across the board.
Hire as many security engineers as you can and fund existing maintainers.
Instruct those engineers and existing maintainers to
triage
,
design
,
review
,
backport
, and
deploy
patches, not primarily to find vulnerabilities or write new code.
Use Astra, Mythos, and other frontier models for good, to find the risks before attackers do.
Use structured prompts such as Google's
Unsafe Rust Review
; this is much more effective than telling them to look hard for bugs.
LLMs are good at writing patches, but
not as one-off-prompts
.
Give them structured prompts and
iterated self-review cycles
until the LLM itself judges the patch to be high-quality.
Whenever possible, get them to test their own fixes rather than guessing at whether their patch is effective.
Only then consider it ready for a human to review.
Sandbox the agents themselves.
The OpenAI-HuggingFace attack happened from a frontier lab testing a model;
your own LLMs can easily cause incidents if you're careless.
Restrict credentials to narrow scopes.
If the issuing authority doesn't support scoped credentials, put a
trusted interface
in front of the services that adds the scope limitations itself; do not give agents direct access to broad credentials.
Do not rely on filtering to only GET requests
.
Block requests at the firewall level and only expose a trusted list of domains.
Filter endpoints using network proxies and trusted interfaces, not local configuration that the LLM can override.
Preserve logs of every mutation or network request the agent makes.
Invest in formal verification, fuzzing and property testing, and
memory-safe languages
.
LLMs are
good at writing Lean
and
fuzz tests
.
I don't care whether you use Go or Rust but for the love of god please
don't use C or C++
for new code.
Invest in triage:
Record which versions of systems are affected,
assign critical findings a human owner and a deadline,
and create developer tooling to automatically update/close issues when they're fixed.
Invest in backport, release, and deployment machinery.
Test upgrades and rollbacks, all the boring stuff.
Developer tooling is cheap now; throw tokens at it so you can spend less human time on each patch: dependency-update automation, signed and reproducible releases, increased deployment speed.
Engineers should be spending their time on coordinated disclosure and frequent releases, not on individual patches.
Deprecate old and insecure versions.
There's a sea-change: you're in a rush, but the people depending on you are too.
Use that as leverage to get them to upgrade.
Where possible, write developer tooling that helps them automatically upgrade.
Track whether people are upgrading and patching; if they aren't, invest more in tooling.
There are going to be a lot of patches and they will be exploited
very
quickly after the embargo lifts.
Measure how long it takes end-to-end from a patch being reported to being deployed and adopted.
Conduct campaigns to speed it up, focusing on the bottlenecks.
Wherever possible, try to shorten embargo times: if you can find a flaw, an attacker probably can too, so the coordination window is much narrower than you're used to.
Invest in supply-chain security.
Inventory your software and infrastructure dependencies.
Inventory your own systems too: what versions are running in prod? what services do you run that don't have a maintainer? which of your systems are EOL?
You finally have the ability to review
all
your dependencies without skimming; do so, prioritizing privileged and security-exposed dependencies first.
LLMs are really good at finding bugs given the source code: use that to your advantage.
Invest in containment and recovery.
Do not rely on a single firewall or VPN.
Instead, use defense-in-depth: segment your networks, limit credential scope, test your backups, and run incident-response exercises.
If possible, practice bringing up your systems from a cold start.
Pay attention to developments in frontier and open weight models.
The more advanced that models get, the less time you have to patch and deploy.
Even if you don't think the threat described here is real,
you're getting a once-in-a-lifetime opportunity to improve security for your projects and communities.
Please take it.
Summary
We are living in interesting times.
We can't hide our heads in the sand.
We should act now, while there's still time.
Thank you to Manish Goregaokar and several others for their feedback on this post. Thank you to everyone who is working tirelessly to make Glasswing and Daybreak a reality. And a big fuck you to DeAlignAI, Z.ai, and everyone else who's been participating in this race to the bottom.
