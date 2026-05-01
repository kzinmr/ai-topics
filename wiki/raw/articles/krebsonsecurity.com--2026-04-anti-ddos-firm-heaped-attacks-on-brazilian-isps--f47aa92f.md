---
title: "Anti-DDoS Firm Heaped Attacks on Brazilian ISPs"
url: "https://krebsonsecurity.com/2026/04/anti-ddos-firm-heaped-attacks-on-brazilian-isps/"
fetched_at: 2026-05-01T07:13:04.785000+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Anti-DDoS Firm Heaped Attacks on Brazilian ISPs

Source: https://krebsonsecurity.com/2026/04/anti-ddos-firm-heaped-attacks-on-brazilian-isps/

A Brazilian tech firm that specializes in protecting networks from distributed denial-of-service (DDoS) attacks has been enabling a botnet responsible for an extended campaign of massive DDoS attacks against other network operators in Brazil, KrebsOnSecurity has learned. The firm’s chief executive says the malicious activity resulted from a security breach and was likely the work of a competitor trying to tarnish his company’s public image.
An Archer AX21 router from TP-Link. Image: tp-link.com.
For the past several years, security experts have tracked a series of massive DDoS attacks originating from Brazil and solely targeting Brazilian ISPs. Until recently, it was less than clear who or what was behind these digital sieges. That changed earlier this month when a trusted source who asked to remain anonymous shared a curious file archive that was exposed in an open directory online.
The exposed archive contained several Portuguese-language malicious programs written in Python. It also included the private
SSH authentication keys
belonging to the CEO of
Huge Networks
, a Brazilian ISP that primarily offers DDoS protection to other Brazilian network operators.
Founded in Miami, Fla. in 2014, Huge Networks’s operations are centered in Brazil. The company originated from protecting game servers against DDoS attacks and evolved into an ISP-focused DDoS mitigation provider. It does not appear in any public abuse complaints and is not associated with any known
DDoS-for-hire services
.
Nevertheless, the exposed archive shows that a Brazil-based threat actor maintained root access to Huge Networks infrastructure and built a powerful DDoS botnet by routinely mass-scanning the Internet for insecure Internet routers and unmanaged
domain name system (DNS)
servers on the Web that could be enlisted in attacks.
DNS is what allows Internet users to reach websites by typing familiar domain names instead of the associated IP addresses. Ideally, DNS servers only provide answers to machines within a trusted domain. But so-called “DNS reflection” attacks rely on DNS servers that are (mis)configured to accept queries from anywhere on the Web. Attackers can send spoofed DNS queries to these servers so that the request appears to come from the target’s network. That way, when the DNS servers respond, they reply to the spoofed (targeted) address.
By taking advantage of an extension to the DNS protocol that enables large DNS messages, botmasters can dramatically boost the size and impact of a reflection attack — crafting DNS queries so that the responses are much bigger than the requests. For example, an attacker could compose a DNS request of less than 100 bytes, prompting a response that is 60-70 times as large. This amplification effect is especially pronounced when the perpetrators can query many DNS servers with these spoofed requests from tens of thousands of compromised devices simultaneously.
A DNS amplification and reflection attack, illustrated. Image: veracara.digicert.com.
The exposed file archive includes
a command-line history
showing exactly how this attacker built and maintained a powerful botnet by scouring the Internet for
TP-Link Archer AX21
routers. Specifically, the botnet seeks out TP-Link devices that remain vulnerable to
CVE-2023-1389
, an unauthenticated command injection vulnerability that was patched back in April 2023.
Malicious domains in the exposed Python attack scripts included DNS lookups for
hikylover[.]st
, and
c.loyaltyservices[.]lol
, both domains that have been flagged in the past year as control servers for an Internet of Things (IoT) botnet powered by a
Mirai malware
variant.
The leaked archive shows the botmaster coordinated their scanning from a Digital Ocean server that has been
flagged for abusive activity hundreds of times
in the past year. The Python scripts invoke multiple Internet addresses assigned to Huge Networks that were used to identify targets and execute DDoS campaigns. The attacks were strictly limited to Brazilian IP address ranges, and the scripts show that each selected IP address prefix was attacked for 10-60 seconds with four parallel processes per host before the botnet moved on to the next target.
The archive also shows these malicious Python scripts relied on private SSH keys belonging to Huge Networks’s CEO,
Erick Nascimento
. Reached for comment about the files, Mr. Nascimento said he did not write the attack programs and that he didn’t realize the extent of the DDoS campaigns until contacted by KrebsOnSecurity.
“We received and notified many Tier 1 upstreams regarding very very large DDoS attacks against small ISPs,” Nascimento said. “We didn’t dig deep enough at the time, and what you sent makes that clear.”
Nascimento said the unauthorized activity is likely related to a digital intrusion first detected in January 2026 that compromised two of the company’s development servers, as well as his personal SSH keys. But he said there’s no evidence those keys were used after January.
“We notified the team in writing the same day, wiped the boxes, and rotated keys,” Nascimento said, sharing a screenshot of a January 11 notification from Digital Ocean. “All documented internally.”
Mr. Nascimento said Huge Networks has since engaged a third-party network forensics firm to investigate further.
“Our working assessment so far is that this all started with a single internal compromise — one pivot point that gave the attacker downstream access to some resources, including a legacy personal droplet of mine,” he wrote.
“The compromise happened through a bastion/jump server that several people had access to,” Nascimento continued. “Digital Ocean flagged the droplet on January 11 — compromised due to a leaked SSH key, in their wording — I was traveling at the time and addressed it on return. That droplet was deprecated and destroyed, and it was never part of Huge Networks infrastructure.”
The malicious software that powers the botnet of TP-Link devices used in the DDoS attacks on Brazilian ISPs is based on
Mirai
, a malware strain that made its public debut in September 2016 by launching
a then record-smashing DDoS attack
that kept this website
offline for four days
. In January 2017, KrebsOnSecurity
identified the Mirai authors
as the co-owners of a DDoS mitigation firm that was using the botnet to attack gaming servers and scare up new clients.
In May 2025, KrebsOnSecurity was hit by another Mirai-based DDoS that Google called
the largest attack it had ever mitigated
. That report implicated a 20-something Brazilian man who was running a DDoS mitigation company as well as several DDoS-for-hire services that have since been seized by the FBI.
Nascimento flatly denied being involved in DDoS attacks against Brazilian operators to generate business for his company’s services.
“We don’t run DDoS attacks against Brazilian operators to sell protection,” Nascimento wrote in response to questions. “Our sales model is mostly inbound and through channel integrator, distributors, partners — not active prospecting based on market incidents. The targets in the scripts you received are small regional providers, the vast majority of which are neither in our customer base nor in our commercial pipeline — a fact verifiable through public sources like
QRator
.”
Nascimento maintains he has “strong evidence stored on the blockchain” that this was all done by a competitor. As for who that competitor might be, the CEO wouldn’t say.
“I would love to share this with you, but it could not be published as it would lose the surprise factor against my dishonest competitor,” he explained. “Coincidentally or not, your contact happened a week before an important event – ​​one that this competitor has NEVER participated in (and it’s a traditional event in the sector). And this year, they will be participating. Strange, isn’t it?”
Strange indeed.
