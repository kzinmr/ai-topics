---
title: "OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened"
url: "https://simonwillison.net/2026/Jul/22/openai-cyberattack/#atom-everything"
fetched_at: 2026-07-24T10:13:55.923850+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened

Source: https://simonwillison.net/2026/Jul/22/openai-cyberattack/#atom-everything

OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened
22nd July 2026
This story is wild. The short version: OpenAI were running a cybersecurity test against an unreleased model, with the model’s guardrail features turned off. Rather than solve the test, the model broke its way out of OpenAI’s sandbox, then found exploits to break
in
to Hugging Face, all so it could cheat on the test by stealing the answers.
Along the way it helped make the strongest case yet for how the imbalance of model availability is hurting our ability to secure our software.
Here’s what happened
We currently have three documents to help us understand what happened here.
ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?
is a paper published on 11th May 2026 describing ExploitGym, a new eval suite for LLM-powered agent systems.
Security incident disclosure — July 2026
by Hugging Face on 16th July 2026 describes how they detected an attack from an “agentic security-research harness—used LLM still not known” that breached some of their systems.
OpenAI and Hugging Face partner to address security incident during model evaluation
from OpenAI on 21st July 2026 confesses that it was
their
agent harness that did this, and that they’re working with Hugging Face to clean up the mess.
ExploitGym
I hadn’t seen the
ExploitGym paper
before and it’s a really interesting one. Authors from UC Berkeley, the Max Planck Institute, UC Santa Barbara, and Arizona State designed a new benchmark for evaluating models on their ability to turn a reported vulnerability into a concrete exploit. OpenAI, Anthropic, and Google provided feedback and helped run the benchmark against their models.
The benchmark “comprises 898 instances derived from real-world vulnerabilities that affected popular software projects”—including the Linux kernel and V8 JavaScript engine. The ExploitGym benchmark is
available on GitHub
.
Here’s the paragraph that best represents their benchmark results:
Among all configurations, Claude Mythos Preview and GPT-5.5 achieve the highest success counts (157 and 120 successes, respectively), demonstrating that current frontier agents can exploit a substantial subset of real-world vulnerabilities under controlled conditions. GPT-5.4 also solves a notable 54 tasks, placing it in an intermediate tier. The remaining model–agent pairings solve fewer than 15 tasks each, underscoring that end-to-end exploitation remains challenging and sharply differentiates today’s frontier systems. Notably, Claude Opus 4.7 achieves fewer successes than Claude Opus 4.6 despite being a newer checkpoint, and does so at substantially lower cost on the full set. Trace inspection reveals that Claude Opus 4.7 and Gemini 3.1 Pro frequently conclude early after judging the target vulnerability non-exploitable.
The paper also describes the approach they took to preventing the agents from cheating by going outside the parameters of the test. This becomes relevant in a moment!
Outbound connections are restricted to a curated allowlist that permits routine package installation (Ubuntu apt repositories and PyPI) and fetching the toolchains required for building V8. All other external endpoints are blocked.
The paper concludes with this (emphasis mine):
Our results show that
autonomous exploit development by frontier AI agents is no longer a hypothetical capability
. While current agents are not yet reliable across all targets, they already
exploit a non-trivial fraction of real-world vulnerabilities
, including complex targets such as kernel components. This rapid emergence is itself a central finding, showing that capabilities that would have seemed implausible are now present in deployed frontier models.
An important detail here: this paper isn’t about discovering vulnerabilities; it’s about being able to take those vulnerabilities and turn them into working exploits.
When Anthropic first restricted access to Mythos
back in April
they talked about this capability as well. A model that can act on vulnerabilities is a lot more dangerous than one that can just discover them.
One of the ways Fable differs from Mythos is that it’s more likely to refuse to weaponize vulnerabilities in this way. I get the impression the US government did not understand that distinction when they banned Fable
last month
.
The Hugging Face incident
The first hint we got of the attack was in
this blog post by Hugging Face
on 16th July 2026:
A malicious dataset abused two code-execution paths in our dataset processing (a remote-code dataset loader and a template-injection in a dataset configuration) to run code on a processing worker. From there, the actor escalated to node-level access, harvested cloud and cluster credentials, and moved laterally into several internal clusters over a weekend.
I hope they release more details about the code that pulled this off. I’m assuming this means packages using the
datasets library
, a Hugging Face project for bundling up and sharing datasets on their platform. That library used to execute arbitrary code but has been steadily locked down over time, with the
4.0.0 release
in July 2025 removing the
trust_remote_code=True
flag entirely.
Assuming the attack used that library it must have either abused pickle serialization in some way, found some other non-obvious code execution path, or (most likely) specified
datasets<4.0.0
as the dependency.
The campaign was run by an autonomous agent framework (appearing to be built on an agentic security-research harness—used LLM still not known) executing many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services.
This was a sophisticated attack!
Then Hugging Face hit a wall: they tried to use “frontier models behind commercial APIs”—I’m guessing from Anthropic and OpenAI—to help analyze the attack, and were blocked:
When we started the log analysis, we first used frontier models behind commercial APIs. This did not work: the analysis requires submitting large volumes of real attack commands, exploit payloads, and C2 artifacts, and these requests were blocked by the providers’ safety guardrails, which cannot distinguish an incident responder from an attacker.
They switched to their own self-hosted instance of MIT licensed GLM-5.2 and it helped them figure out what was going on.
This indicated a fundamental asymmetry between the defending team and the (so-far unknown) attacker:
We do not know which model powered the attacker’s agents, whether a jailbroken hosted model or an unrestricted open-weight one; either way, the attacker was bound by no usage policy, while our own forensic work was blocked by the guardrails of the hosted models we first tried.
As a useful indicator of how seriously they took the attack:
[...] Finally, we have also reported this incident to law enforcement agencies.
So who was responsible for this “autonomous agent framework”? It turned out to be OpenAI themselves.
The OpenAI confession
Five days later,
on July 21st
, OpenAI revealed the culprit. They had been running the ExploitGym benchmark against a new, as-yet undisclosed model, and that model had been operating
way
outside its intended parameters (emphasis mine):
After investigating, we now know
that this particular incident was driven by a combination of OpenAI models
— including GPT‑5.6 Sol and an even more capable pre-release model, all with reduced cyber refusals for evaluation purposes — while being internally tested on a
benchmark⁠
[ExploitGym] of cyber capabilities. [...]
We estimate maximal cyber capabilities by
running this evaluation without production classifiers used to prevent models from pursuing high-risk cyber activity
. Our benchmarks run in a highly isolated environment, with network access constrained to the ability to install packages through an internally hosted third-party software that acts as a proxy and cache for package registries.
The models
identified and chained vulnerabilities across OpenAI’s research environment and Hugging Face’s production infrastructure
to obtain test solutions directly from Hugging Face’s production database. All evidence suggests that the models were hyperfocused on finding a solution for ExploitGym, going to extreme lengths to achieve a rather narrow testing goal.
It’s pretty clear what happened here. OpenAI removed safety filters for an in-progress model, locked it up in a sandbox and told it to solve the ExploitGym problems. Given the absence of guardrails there was nothing to prevent the model from attempting to break out of that sandbox, break into Hugging Face, and read the answers from there instead.
OpenAI’s sandbox used the now common pattern of allowing access to an allow-list of sites related to installing additional packages via a controlled proxy. In OpenAI’s words:
While operating in our sandboxed testing environment, our models
spent a substantial amount of inference compute finding a way to obtain open Internet access
, in pursuit of solving the evaluation problem. To gain access, the models identified and exploited
a zero-day vulnerability (which we’ve now responsibly disclosed to the vendor) in the package registry cache proxy
. With this access, our models performed a series of privilege escalation and lateral movement actions in our research testing environment until the models reached a node with Internet access.
So step one was to break out onto the public internet. The model then broke into Hugging Face to find the answers:
After gaining Internet access, the models
inferred that Hugging Face potentially hosted models, datasets and solutions
for ExploitGym. Knowing this, the model searched for and successfully found ways to gain access to secret information that it could use to cheat the evaluation. In one example,
the model chained together multiple attack vectors, including using stolen credentials and zero-day vulnerabilities
to find a remote code execution path on the Hugging Face servers.
Chaining together multiple attack vectors is
exactly
the kind of thing these new models can do, where previous generations of models might have failed.
I wrote last month about how
Claude Fable is relentlessly proactive
, when I noticed it spinning up custom web servers and deploying CORS tricks on my own laptop just to help debug a WebKit CSS issue. It turns out relentless proactivity is the defining trait of this new generation of Mythos-class models. If you set them a goal and give them a way to get there, even inadvertently, they
will figure it out
.
Resist the temptation to write this off as a stunt
There will inevitably be some people who dismiss this story as a dishonest marketing trick by OpenAI to make their models sound terrifyingly effective. I found 81 instances of the term “marketing” in
the Hacker News discussion
of the incident.
To those people I say
pull your heads out of the sand
—you’re now including Hugging Face in your conspiracy theories, just so you can deny the crescendo of evidence here!
The best models we have today have the ability to both find and exploit new vulnerabilities. The ExploitGym paper itself concludes that “autonomous exploit development by frontier AI agents is no longer a hypothetical capability”, and this incident is a perfect example of exactly that.
The asymmetry is increasingly frustrating
One of the most infuriating details of this story is how Hugging Face, faced with an accidental and aggressive attack from one of OpenAI’s models, were unable to then turn to OpenAI’s models to help them fend off the attack.
The frontier models we have access to are increasingly being constrained in how much they can help us protect our software, heavily influenced by the US government’s ongoing threat of export controls.  Claude Fable 5 wouldn’t even
proofread this article
for me! It insisted on downgrading me to a less capable model.
Meanwhile open weight models from China such as GLM-5.2, Kimi 3 and the new Qwen 3.8 Max appear to have none of these restrictions—and any restrictions that
do
exist can likely be fine-tuned out of them by modifying the weights
These constraints are meant to make us safer. I think there’s a risk that they are having the opposite effect.
