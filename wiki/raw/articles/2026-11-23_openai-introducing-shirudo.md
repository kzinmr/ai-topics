---
title: "OpenAI and Cisco introduce Shirudo"
source: https://openai.com/index/introducing-shirudo/
author: OpenAI
type: raw-article
published: 2026-11-23
collected: 2026-11-24
sha256: 4acebb3649bd02bc2785c2020200dc59828cdf273ada4fd5159c6bc6bc8cc569
---

OpenAI and Cisco introduce Shirudo. An open-source runtime that helps operators protect running Linux systems without needing to wait for the patch or restarts. (November 23, 2026, Security.)

OpenAI and Cisco are launching Shirudo, an open-source runtime that helps teams protect Linux systems while they roll out patches. In a controlled test, a Codex-generated shield blocked a Java4Shell exploit attempt against a running Elasticsearch service without requiring a restart. OpenAI is inviting developers, security researchers, and infrastructure operators across the industry to help develop the project further. The project brings together OpenAI's frontier AI, security and infrastructure research and Cisco's infrastructure and security expertise.

Testing and deploying a patch can still take days or weeks. Protecting a service in the meantime can be challenging because an exploit and a legitimate request may rely on the same Linux operation. Blocking that operation entirely could take the service offline. Shirudo (Japanese for "shield") is designed to help security teams navigate this tradeoff. Teams can test whether a temporary safeguard, called a shield, blocks the behavior that exposes a vulnerability while allowing legitimate requests through. Once an operator approves the shield, it can be deployed while the service continues running.

Greg Brockman, President and Co-founder of OpenAI: "We're giving defenders better models and tools to find and fix vulnerabilities faster, but finding a bug today doesn't mean you can patch every system tomorrow. We are partnering closely with Cisco on Shirudo to help teams protect the systems they need to keep running while they build and roll out a fix. So many teams rely on the same software that it makes sense to build these tools in the open. Now when one team finds a better way to protect a system, others don't have to start from scratch."

How Shirudo works. Shirudo uses eBPF, a Linux technology that allows small programs to run at specific points inside the operating system. This makes it possible to observe suspicious activity and apply targeted security protections to running systems. OpenAI and Cisco are designing Shirudo around four core capabilities:

- Live protection: eBPF shields can block vulnerable code paths without restarting the system. Security teams can monitor how a proposed shield would affect applications before enforcing it.
- Defense at machine speed: OpenAI and Cisco are designing Shirudo to give agents programmable controls to investigate vulnerabilities, develop targeted shields, and validate their effectiveness against exploits and real workloads. Security teams control what gets deployed.
- Trusted deployment: Shields are cryptographically signed and verified before loading. Linux's eBPF verifier checks eBPF programs against its safety rules, while kernel security controls restrict unauthorized changes.
- Hardware-backed verification: Shirudo uses a Trusted Platform Module (TPM) to support a verifiable record of protections being loaded or removed. Operators can use this evidence to check whether systems meet their security requirements.

The Shirudo technical walkthrough from the Linux Plumbers Conference shows how to apply a shield and verify it on the target host. The Java4Shell vulnerability is another example illustrating how a targeted shield can protect a running application while a permanent patch is being prepared. Using OpenAI's Codex, the team generated a shield that added an input check to Java's Base64 decoder and attached it directly to a running Elasticsearch process. When attempting to exploit the vulnerability, the shield rejected the malicious input, blocking the attack while Elasticsearch continued running.

## HN discussion highlights (item 50619630, 72 pts / 23 comments)

- [futuraperdita] Feels to me to be a strange Japanification for a brand name here, given that "Shirudo" is just the English "shield" in kana.
- [qmarchi] I think it's different enough that those without Japanese exposure won't notice. It's still dumb tho. Could've used shahei (しゃへい, 遮蔽), since that's the actual term "to shield/block something", or tate (たて, 盾) the object of a shield. Marketing be damned I guess...
- [numpad0] That's extra funny considering most Japanese speakers won't recognize the word. It has to be "shi-rudo" with the hyphen indicating long vowel, else it'll be read like "shildo". Or is that the joke?
- [p0lychromatic] It sounds like a cool idea, at least the way OpenAI presents it. However, going to the page and requirements, I have to nope out. This basically requires a full measured boot setup (TPM2, unified kernel image etc.). This is definitely not a simple "vibe-code your patch" platform you can deploy in an emergency. I wish there was a reduced security mode that really just focuses on patching vulnerable software, and not defending itself from when the machine is already compromised as root.
- [rkagerer] I like the idea, but am not sure they've nailed an acceptable implementation. The eBPF bits run local (and can be deployed out of a repository you host). But to get most effective use out of this tech, it seems like you'd need to give an AI vendor (namely OpenAI) a bunch of telemetry and more potential control into your systems than I'm sure I'd be comfortable with.
- [cvadict] Requires a "Guardian Agent"... and guess who is going to sell that pricey subscription to you now that all of the open weight models are getting their cyber-security capabilities artificially nerfed prior to release. This is no different than organized crime creating the problem in a neighborhood and then offering you protection from the problem if you pay up.
- [siliconc0w] I tried to prototype something similar a few months ago but ran into OAI guardrails building the patches (so purely defensive work, not even exploits to 'test' if they work). This is sadly how the future is looking - you only get 'AI defending against AI' if you are a big company or willing to pay a big company a subscription fee.
- [fathermarz] In theory, sounds amazing. In practice I can foresee this being an escape hatch for swamped teams that never actually harden their systems. They just use Shirudo as the fix and keep adding rules to it forever... when you suppress the fire, the urgency to patch or fix long term evaporates quickly.
- [joj123] This was the argument against every "blocking" software (WAF, DDoS protection software, etc.). Need to wait and watch to see if that happens in this case too.
- [fc417fc802] If a bandaid is sufficient then why bother with more? If it isn't then it's on you to plan responsibly. I think the only way to fix the underlying problem is regulation with teeth that makes such failures unacceptably costly from the perspective of the executives.
- [jiveturkey] This is actually decently limited and the agentic magic doesn't seem to have any there there, at least not yet. I'm surprised this hasn't gotten more traction on HN but maybe it's just the timing. Contrary to what it says on the tin, it's not just eBPF-based.
