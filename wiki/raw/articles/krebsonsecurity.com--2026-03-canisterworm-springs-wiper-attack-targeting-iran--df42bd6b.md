---
title: "‘CanisterWorm’ Springs Wiper Attack Targeting Iran"
url: "https://krebsonsecurity.com/2026/03/canisterworm-springs-wiper-attack-targeting-iran/"
fetched_at: 2026-04-29T07:02:06.284574+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# ‘CanisterWorm’ Springs Wiper Attack Targeting Iran

Source: https://krebsonsecurity.com/2026/03/canisterworm-springs-wiper-attack-targeting-iran/

A financially motivated data theft and extortion group is attempting to inject itself into the Iran war, unleashing a worm that spreads through poorly secured cloud services and wipes data on infected systems that use Iran’s time zone or have Farsi set as the default language.
Experts say the wiper campaign against Iran materialized this past weekend and came from a relatively new cybercrime group known as
TeamPCP
. In December 2025, the group began compromising corporate cloud environments using a self-propagating worm that went after exposed Docker APIs, Kubernetes clusters, Redis servers, and the React2Shell vulnerability. TeamPCP then attempted to move laterally through victim networks, siphoning authentication credentials and extorting victims over Telegram.
A snippet of the malicious CanisterWorm that seeks out and destroys data on systems that match Iran’s timezone or have Farsi as the default language. Image: Aikido.dev.
In a profile of TeamPCP published in January, the security firm
Flare
said the group weaponizes exposed control planes rather than exploiting endpoints, predominantly targeting cloud infrastructure over end-user devices, with Azure (61%) and AWS (36%) accounting for 97% of compromised servers.
“TeamPCP’s strength does not come from novel exploits or original malware, but from the large-scale automation and integration of well-known attack techniques,” Flare’s
Assaf Morag
wrote
. “The group industrializes existing vulnerabilities, misconfigurations, and recycled tooling into a cloud-native exploitation platform that turns exposed infrastructure into a self-propagating criminal ecosystem.”
On March 19, TeamPCP executed a supply chain attack against the vulnerability scanner
Trivy
from
Aqua Security
, injecting credential-stealing malware into official releases on GitHub actions. Aqua Security said it has since
removed
the harmful files, but the security firm Wiz
notes
the attackers were able to publish malicious versions that snarfed SSH keys, cloud credentials, Kubernetes tokens and cryptocurrency wallets from users.
Over the weekend, the same technical infrastructure TeamPCP used in the Trivy attack was leveraged to deploy a new malicious payload which executes a wiper attack if the user’s timezone and locale are determined to correspond to Iran, said
Charlie Eriksen
, a security researcher at
Aikido
. In
a blog post
published on Sunday, Eriksen said if the wiper component detects that the victim is in Iran and has access to a Kubernetes cluster, it will destroy data on every node in that cluster.
“If it doesn’t it will just wipe the local machine,” Eriksen told KrebsOnSecurity.
Image: Aikido.dev.
Aikido refers to TeamPCP’s infrastructure as “
CanisterWorm
” because the group orchestrates their campaigns using an
Internet Computer Protocol
(ICP) canister — a system of tamperproof, blockchain-based “smart contracts” that combine both code and data. ICP canisters can serve Web content directly to visitors, and their distributed architecture makes them resistant to takedown attempts. These canisters will remain reachable so long as their operators continue to pay virtual currency fees to keep them online.
Eriksen said the people behind TeamPCP are bragging about their exploits in a group on Telegram and claim to have used the worm to steal vast amounts of sensitive data from major companies, including a large multinational pharmaceutical firm.
“When they compromised Aqua a second time, they took a lot of GitHub accounts and started spamming these with junk messages,” Eriksen said. “It was almost like they were just showing off how much access they had. Clearly, they have an entire stash of these credentials, and what we’ve seen so far is probably a small sample of what they have.”
Security experts say the spammed GitHub messages could be a way for TeamPCP to ensure that any code packages tainted with their malware will remain prominent in GitHub searches. In a newsletter published today titled
GitHub is Starting to Have a Real Malware Problem
,
Risky Business
reporter
Catalin Cimpanu
writes that attackers often are seen pushing meaningless commits to their repos or using online services that sell GitHub stars and “likes” to keep malicious packages at the top of the GitHub search page.
This weekend’s outbreak is the
second major supply chain attack
involving Trivy in as many months. At the end of February, Trivy was hit as part of an automated threat called
HackerBot-Claw
, which mass exploited misconfigured workflows in GitHub Actions to steal authentication tokens.
Eriksen said it appears TeamPCP used access gained in the first attack on Aqua Security to perpetrate this weekend’s mischief. But he said there is no reliable way to tell whether TeamPCP’s wiper actually succeeded in trashing any data from victim systems, and that the malicious payload was only active for a short time over the weekend.
“They’ve been taking [the malicious code] up and down, rapidly changing it adding new features,” Eriksen said, noting that when the malicious canister wasn’t serving up malware downloads it was pointing visitors to
a Rick Roll video
on YouTube.
“It’s a little all over the place, and there’s a chance this whole Iran thing is just their way of getting attention,” Eriksen said. “I feel like these people are really playing this Chaotic Evil role here.”
Cimpanu observed that supply chain attacks have increased in frequency of late as threat actors begin to grasp just how efficient they can be, and his post documents an alarming number of these incidents since 2024.
“While security firms appear to be doing a good job spotting this, we’re also gonna need GitHub’s security team to step up,” Cimpanu wrote. “Unfortunately, on a platform designed to copy (fork) a project and create new versions of it (clones), spotting malicious additions to clones of legitimate repos might be quite the engineering problem to fix.”
Update, 2:40 p.m. ET:
Wiz is
reporting
that TeamPCP also pushed credential stealing malware to the
KICS
vulnerability scanner from
Checkmarx
, and that the scanner’s GitHub Action was compromised between 12:58 and 16:50 UTC today (March 23rd).
