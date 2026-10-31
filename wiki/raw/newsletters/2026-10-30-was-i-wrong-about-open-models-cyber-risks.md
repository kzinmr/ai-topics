---
title: "Was I wrong about open models & cyber risks?"
date: 2026-10-30
author: Nathan Lambert
publication: Interconnects / Robotic (Substack pub 48206, post 222715088)
canonical_url: https://www.interconnects.ai/p/was-i-wrong-about-open-models-and
source_label: "uid=858"
processed_at: 2026-10-31
retrieved_via: curl + <p> extraction from interconnects.ai (full body, ~27 paragraphs)
tags: [newsletter, raw]
---

# Was I wrong about open models & cyber risks?

Nathan Lambert, Interconnects (Robotic), 2026-10-30. Self-correction essay after the "Black October" vulnerability-disclosure onslaught (PHP2Shell, GitLab).

## Key claims (full body extracted)

- A few weeks before the vulnerability-disclosure acceleration, Lambert wrote that open-weight models were not the cyber threat claimed. He revisits it with more diligence: "I largely still stand by my above writing a few weeks ago, but I'm nervous about it."
- **Falsifiable-prediction framing**: "The leading proponents of this new wave of open-weight fear mongering have effectively been making a falsifiable prediction — that the current open-weight models are going to cause substantial, not seen before AI harms by crippling our cyber infrastructure... Based on all the evidence I have... they're set up to be wrong."
- **GLM-5.3 crossed the alleged Mythos threshold**: "By all measures, GLM-5.3 is the model that crosses that threshold of capability, and there's little public evidence that much has changed, and we're over a month out of the model weight release."
- **Stronger claim**: "If Claude Mythos was accidentally released as open-weight, it seems like the world would have been more or less fine." (with acknowledgment of some incident increase)
- **WSJ data point**: "The best guess for what is happening in the cybersecurity space is that the behind the scenes work has only accelerated, bringing more people and resources in to try and patch the internet — the Wall Street Journal reported that cyber first responders [were mobilized]..."

## Receipts: the "cyber weapon" language he is auditing

- **Rob Wiblin** (80,000 Hours host, own podcast, April 10, 2026): "If it fell into the hands of criminals or hostile state cyber actors, it would be an actual disaster."
- **Anthropic, Project Glasswing announcement blog** (April 7, 2026): "Given the rate of AI progress, it will not be long before such capabilities proliferate, potentially beyond actors who are committed to deploying them safely. The fallout—for eco[nomy and national security]..."
- **Zvi Mowshowitz** (April 9, 2026, cited as the "more reasonable" end): "Claude Mythos would give attackers a cornucopia of zero-day exp[loits]..."

## Epoch AI Firefox exploit (multi-stage argument)

- Epoch AI published internal work using GLM-5.3 to find and chain vulnerabilities: "We used GLM 5.3 to create a website that, simply when visited by a Firefox user and without further interaction, gave the attacker the ability to exfiltrate files from the user's computer."
- Lambert's counter-framing: "the exploit is in Firefox, and a would-be hacker needs to plant a website that is looking for this exploit. This is doable, and could have serious consequences, but just finding the exploit is only one step in a multi-stage process."

## Offense-defense and threat-actor modeling

- Open models are "providing balance in the offense-defense equation, and Mythos coming sooner wouldn't have massively upended this." Expects companies to adopt open-weight models faster (for cost/control).
- Bakery-tweet framing of threat actors: "Life is a lot easier once you stop seeing threat actors as hackers who want to break into systems by any means possible, and start seeing them as businesses with well defined business processes. A bakery isn't going to start making dog food because..."
- "I expect most of these vulnerabilities are being found by closed models, but I have very high error bars on this prediction."
- Framing: "we're working through the backlog of cyber vulnerabilities as we transition from the human-focused internet to closed silos of human activity mediated by agents."
- "All of this... is way more about AI's capabilities and diffusion generally than anything about open vs. closed models." (cites Joshua Saxe, Chris Hughes)

## Notable comment thread (Lambert-endorsed)

- Chris Hughes comment (liked by Lambert): research from frontier corps + external teams (Epoch, Irregular) heavily emphasizes **offensive** tasks; little work on demonstrating **defensive** capabilities. Reasons: (1) frontier corps incentivized to demonize open-weight models for competitive factors; (2) offense far more verifiable than defense; (3) defense research would highlight refusals legitimate defensive users hit with closed models. "Almost all the hype and attention is on offensive use cases... which inevitably... makes each model subsequently better at wreaking havoc vs. mitigating it."
- Reader comment on PHP2Shell: "the exploits built around the vul have largely failed because many vuls need more to work at scale."
