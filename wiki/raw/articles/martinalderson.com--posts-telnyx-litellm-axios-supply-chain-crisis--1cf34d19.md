---
title: "Telnyx, LiteLLM and Axios: the supply chain crisis"
url: "https://martinalderson.com/posts/telnyx-litellm-axios-supply-chain-crisis/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-28T07:02:44.011054+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Telnyx, LiteLLM and Axios: the supply chain crisis

Source: https://martinalderson.com/posts/telnyx-litellm-axios-supply-chain-crisis/?utm_source=rss&utm_medium=rss&utm_campaign=feed

While the world's been watching physical supply chains, a different kind of supply chain attack has been escalating in the open source ecosystem.
The issue
Over the past week a group of bad actors have been compromising various open source projects, pushing malicious versions of libraries which inject a trojan that collects sensitive data from systems that install the malicious version.
Ironically, the first attack started with
Trivy
, an open source package for
finding
security vulnerabilities.
The scale of the issue is growing and is alarming. This wave of attacks started with some smaller libraries, then started to hit more popular packages in the supply chain with
Telnyx
, a popular package for voice and SMS integration. This had ~150k/week downloads on the affected package.
LiteLLM
was next - a much more popular package for calling various APIs. This had ~22M/week downloads.
Finally, and most concerning, the npm package for
axios
- an
incredibly
widely used library for calling APIs, was
attacked
on March 31st. This has at least 100M downloads a week and is a very core piece of software that is used in millions of apps.
There was a rapid reaction to each of these attacks to remove the malicious versions, but even in the hours they were up, tens of thousands of machines (and potentially far more) were likely compromised.
The attackers are leveraging stolen credentials from the previous attack(s) to then infect more packages in the supply chain. This creates a vicious cycle of compromises that continues to grow.
Equally, other systems are at risk - for every system that the attack compromises who happens to also be a developer of
another
software library, there are probably thousands of other developers who have unfortunately leaked very sensitive data to the attackers.
Not a new issue
This is not a new issue, and last year we saw the
Shai-Hulud v1
and
v2
attacks against the npm ecosystem which in two waves backdoored over 1,000 packages. The aim of this attack appears to have been to steal crypto - with
reports
suggesting $8.5m was stolen.
The infrastructure providers behind this supply chain did respond by putting various mitigations in place. The primary two were requiring published packages to use short-lived tokens - which reduces the impact of "old" credentials being able to publish new packages.  It appears this has not solved the issue - given it seems these packages have managed to be published regardless.
The more invasive one is to allow developers to not install "brand new" packages. Instead, they get held for a time period - say 24 hours - with the idea being the community will (hopefully) detect malicious versions in the 24 hours and revoke them before they are installed.
This is a double edged sword though - as often you
need
rapid response to a vulnerable package to
avoid
security issues. This can be overridden manually - but it does introduce some overhead to response to urgent security flaws.
Finally, npm are rolling out staged publishing. This requires a separate step when publishing new versions of packages for a "trusted" human to do a check on the platform with two step verification to avoid automated attacks. However, given it seems developers computers' are being compromised it is not implausible to suggest that the attacker could also perform this step.
The broader picture
I'm extremely concerned about the cybersecurity risk LLMs pose, which I don't think is sufficiently priced in on the impact it is going to have outside of niche parts of the tech community. While it's hard to know for sure how the initial attacks were discovered, I strongly suspect they have been aided by LLMs to find the exploit(s) in the first place and develop subsequent attacks.
While this is conjecture, the number of exploits being found by non-malicious actors is
exploding
. I found one myself - which I wrote up in a
recent post
, still unpatched - in less than half an hour. There's
endless
other
examples
online
.
So it seems to me that LLMs are acting as an accelerant:
Firstly, they make finding security vulnerabilities far easier - which allows the whole supply chain attack cycle to start. And the leaked
rumours
about the new Mythos model from Anthropic being a step change
better
than Opus 4.6 (which is already exceptionally good at finding security issues) means the direction of travel is only going one way.
Secondly, they allow attackers to build far more sophisticated attacks
far
quicker than before - for example, one of the attacks in this recent wave hid one exploit in an audio file.
Next, this is all happening while the infrastructure providers of the software supply chain are on the back foot with improving mitigations.
xkcd 2347
Finally, so much of the software ecosystems' critical security infrastructure is maintained by volunteers who are often unpaid. As always, the above image illustrates the point far better than words can.
To reiterate - it may be that this is just a well resourced group that could have done all this without LLMs. But given adoption of coding agents is so high in the broader developer community, it seems far fetched to say they wouldn't be used for nefarious means.
Fundamentally, these attacks are possible because OSes (by default) are far too permissive and designed in a world where software is either trusted or not. The attempts to secure this - by trusting certain
publishers
- falls down for both agents and supply chain attacks because agents can use trusted software in unexpected ways, and if the
trusted
authors of the software are compromised it bypasses everything.
We need a new(ish) OS
Thinking a few steps ahead here, it seems to me that the core mitigations are (mostly) insufficient.
Any delay to publishing packages can backfire and introduce delays in responding to
real
security incidents
There is too much software - maintained or unmaintained - which is likely to be vulnerable
Much of this software, if it is maintained, is poorly resourced and is likely to burn out volunteers trying to resolve a flood of security issues in the near term
There are
some
things however that would help with the supply chain in particular:
Frontier labs donating compute and tokens to automatically scan
every
package update for potential signs of compromise before publishing. This would be an excellent use of their leading models
To me though I keep coming back to the realisation that the difficulty of
sandboxing agents
faces very similar challenges to helping mitigate the impact of this security issue.
iOS and Android were designed with this approach in mind - each app has very limited access to other apps and the OS as a whole. I think we need to move desktop and server operating systems to a similar model for this new world.
While this won't resolve all issues, it will dramatically reduce the "blast impact" of each attack and prevent the "virality" of many exploits from gathering traction.
The OS should know that
npm install
should only write package files to a certain set of folders and reject everything else. The OS should know a baseline of services a CI/CD run and what network calls it makes, to avoid connections to random command and control services. And like mobile OSes, one program shouldn't be able to read another programs files and data without explicit opt in.
If you've used sandbox mode in a coding agent, you will be familiar with this approach - all the pieces are there already.
Qubes OS
is probably the closest thing outside of mobile OSes to what I'm thinking we need to move to - a security focused Linux operating system which runs each app in a total self-contained VM.
It's an enormous undertaking to migrate the world's software to run like this, and perhaps governments should be allocating significant resources to open source projects to help them adopt this.
