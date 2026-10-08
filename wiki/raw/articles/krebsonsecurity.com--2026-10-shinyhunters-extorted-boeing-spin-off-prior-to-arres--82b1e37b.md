---
title: "ShinyHunters Extorted Boeing Spin-off Prior to Arrests"
url: "https://krebsonsecurity.com/2026/10/shinyhunters-extorted-boeing-spin-off-prior-to-arrests/"
fetched_at: 2026-10-08T10:01:35.912296+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# ShinyHunters Extorted Boeing Spin-off Prior to Arrests

Source: https://krebsonsecurity.com/2026/10/shinyhunters-extorted-boeing-spin-off-prior-to-arrests/

A teenager from Amman, Jordan suspected of leading the prolific data theft and extortion group
ShinyHunters
has been detained and is reportedly cooperating with the FBI to identify other members of the hacking gang. KrebsOnSecurity has learned that the suspect, who uses the hacker handle “
Rey
,” was detained as ShinyHunters was in the process of extorting a business unit recently divested by the global aerospace company
Boeing
, which manufactures the fleet of planes used by the employer of Rey’s father —
Royal Jordanian Airlines
.
The logo for Jeppesen ForeFlight, a business unit divested last year by the aerospace firm Boeing.
On October 3,
Reuters
cited
three unnamed sources saying a suspected ShinyHunters member in Amman named
Saif Al-din Khader
was detained by Jordanian authorities and was cooperating with the FBI. KrebsOnSecurity identified Rey as Khader in
a November 2025 profile
, in which the young man admitted working with multiple ransomware groups.
Rey was featured again in
a September 28 exclusive
about the Dutch police arresting 24-year-old convicted cybercriminal
Pepijn van der Stap
on suspicion of aiding in data thefts and extortions by ShinyHunters. The story noted that immediately following the Dutchman’s arrest on the evening of September 15, Rey assumed control over the ShinyHunters brand and boasted publicly about stealing highly sensitive data from the
FBI
and extorting the ransomware group
Cl0p
.
Rey taunted both the FBI and Cl0p with memes posted to his longtime account on Twitter/X, while simultaneously including images of the avatar used by Van Der Stap’s former hacker alias “
Umbreon
” in an apparent attempt to frame the Dutchman for both hacks.
A taunting meme uploaded to Twitter/X by Rey on Sept. 22. A giant sized version of the Pokemon character Umbreon can be seen in the bottom left.
As noted in our September 28 report, ShinyHunters gained access to the FBI site and other victims by exploiting a vulnerability (CVE-2026-35273) in
PeopleSoft
, a software-as-a-service platform from the tech giant
Oracle
that is broadly used by companies to manage hiring and human resources, benefits and payroll. Oracle quickly issued a fix for CVE-2026-35273, which ShinyHunters first began exploiting as a zero-day in June, and at the time Mandiant released web application firewall rules intended for organizations that couldn’t apply the security update quickly enough.
ShinyHunters
told BleepingComputer in June
that the original goal behind exploiting the PeopleSoft vulnerability was to breach the FBI’s own PeopleSoft database, but the hackers said those attacks were unsuccessful for some reason. In recent weeks, however, ShinyHunters
turned to a well-known URL-encoding trick
to bypass Mandiant’s suggested web application firewall rules.
In
a report
released Sept. 25, security experts at
Mandiant
and the
Google Threat Intelligence Group
(GTIG) confirmed that ShinyHunters had mass-exploited the PeopleSoft vulnerability to steal data from dozens of systems across a range of industries, including higher education, technology, healthcare, agriculture, transportation and government.
Reuters
reported October 5
that the FBI has removed a contractor at
Accenture
over their failure to patch the FBI recruitment website hacked by ShinyHunters, which exposed sensitive data on more than 5,000 FBI personnel, including each’s person’s unit and specialization, as well as medical and psychiatric records.
‘REY’ MEANS KING, AS IN ROYAL
According to two sources familiar with the ShinyHunters investigation, a navigation and digital aviation unit recently divested by the global aerospace company
Boeing
was among the victims that ShinyHunters was in the process of extorting when Rey was apprehended by Jordanian authorities.
Those sources said the FBI’s investigation into ShinyHunters gained renewed urgency with the group’s attempted extortion of the former Boeing unit, which allegedly included the theft of sensitive information that sources said could pose operational safety and security risks.
In a brief statement shared with KrebsOnSecurity, Boeing acknowledged the extortion attempts by ShinyHunters, and said the incident concerned data stolen from
Jeppesen ForeFlight
, a subsidiary that Boeing
sold in November 2025
to the private equity firm Thoma Bravo for $10.55 billion.
“We are aware of claims by a threat actor regarding data allegedly associated with Boeing and our former subsidiary Jeppesen ForeFlight,” a Boeing spokesperson shared. “We are actively reviewing the matter with the Jeppesen ForeFlight team.”
A spokesperson for Jeppesen ForeFlight shared a written statement in response to questions, saying the company has seen no impact on their end. “Based on our investigation to date into this claim and proactive security posture, there was no impact to our operations or products.”
Rey’s alleged involvement in attempting to extort the former Boeing unit is noteworthy because there is strong evidence that his father works for
Royal Jordanian Airlines
, which is mostly controlled by the Jordanian government and operates its long-haul fleet on passenger planes built by Boeing. Rey claimed on Telegram in early 2025 that his father was an airline pilot, although that could not be independently confirmed.
However, as noted in
our November 2025 profile of Rey
, his family’s shared computer was at one point compromised by password-stealing malware, and the data collected by that malware clearly shows Rey’s father used the same credentials to log in at multiple online portals for Royal Jordanian Airlines employees.
Royal Jordanian Airlines has not yet responded to a request for comment. In advance of our September 28 story, KrebsOnSecurity once again emailed Rey’s father to seek comment and update him on his son’s alleged activities. Neither of the Khaders have responded. But just hours after that request was sent, Rey began deleting his various social media accounts, including the Twitter/X account he previously used to taunt the FBI, Cl0p, and other ShinyHunters victims.
Rey may have nixed many of his social media profiles, but his cybersecurity blog on GitHub somehow escaped the purge, and it shows that Rey was fixated on the leaders of the Cl0p ransomware group. In March 2026, Rey’s blog featured
a lengthy post
that identified two Russian men as the core developers and hackers behind Cl0p.
Rey’s blog on GitHub. This post doxes two Russian men as the core operators behind Cl0p, one of the oldest and most established ransomware groups still in operation today.
MURDER FOR HIRE?
Meanwhile, news outlets in the Netherlands reported explosive new allegations leveled at Van der Stap, whose supposed personal transformation from convicted to reformed hacker has been widely covered in the tech news media. The Dutch daily
RTL reported on Sept. 29
that investigators suspect Van der Stap tried to orchestrate at least two murders. According to RTL, the murders were allegedly to be committed abroad, and there are indications Van der Stap gave the order for these attacks.
Van der Stap was released from prison after serving the better part of a four year sentence for data theft and extortion activity that prosecutors said netted between €1.5 million and €2.7 million. In an interview with KrebsOnSecurity on September 9, Van der Stap described his new role as “offensive security lead” at the Dutch cybersecurity company
Neo Security
, saying the job involved probing client networks for security vulnerabilities.
Neo Security’s owner
Benjamin Korper
told Reuters he has hired an outside firm to investigate whether Van der Stap had hacked Neo Security or its customers, but that so far investigators have found no evidence he acted against his employer or clients. Korper said Dutch forensic investigators visited his office on September 15, the night Van der ⁠Stap was arrested in a dramatic police raid that reportedly involved
flash bang grenades
.
A screenshot of a Sept 16 story by the Dutch news outlet at5.nl, describing a police raid on Van Der Stap’s residence that reportedly used flash-bang grenades.
Prior to his first arrest in 2023, Van der Stap was working as a software engineer at the Amsterdam-based cybersecurity startup Hadrian, while volunteering at the Dutch Institute for Vulnerability Disclosure (DIVD) — even as he was hacking into and extorting a number of large organizations.
When asked in a recent interview why anyone should believe the word of a self-described “reformed” cybercriminal who had so casually deceived countless friends, co-workers and journalists for years, Van der Stap replied that his work spoke for itself and there was nothing he could say that would convince his worst critics.
“You can throw a bunch of nice words at someone, but you can’t convince them if they don’t want to be convinced,” Van der Stap told KrebsOnSecurity on Sept. 9. “I’m doing what I can to repay victims, and that’s all I can do. If someone doesn’t want to believe me, then that’s on them.”
FRANCHISING AND BURNING A BRAND
Cybercriminals aligned with ShinyHunters have been responsible for
dozens of data breaches
involving billions of stolen records, and breaches claimed by the group stretch back to at least 2019. But experts say the people recently operating behind the ShinyHunters name are not the same core members that populated the group in its early days, most of whom are French citizens who have been arrested (if not also imprisoned) on
at least one prior occasion
for alleged cybercrime activity.
More to the point, ShinyHunters has become something of a franchise. Think the
Dread Pirate Roberts
character in the 1980s cult movie classic “The Princess Bride,” only succession by death is replaced with succession by arrest, and there can be multiple simultaneous Dread Pirate Robertses. Sources close to the investigation say the FBI is focusing on a remaining handful of cybercriminal freelancers or affiliates who have been feeding the group stolen credentials to various software-as-a-service (SaaS) platforms used by major companies in exchange for a cut of any data ransoms later paid by victims.
In the days after the news broke of Van der Stap’s arrest, a cybercrime-focused chat server on Telegram that was allegedly operated by Rey erupted with hot takes, with most participants heaping ridicule on the teenage hacker after he publicly backed down from threats against the FBI and Cl0p, and again when
the ShinyHunters’s darknet website suddenly went offline
. Several commentators accused Rey of resurrecting the ShinyHunters brand after its core members were rounded up in France, and making a mockery of the group’s name and reputation ever since.
“He bought the old forum PGP key and used it to make new Breachforum websites and Telegram channels larping as ShinyHunters to ransom companies and then sell the used data or resell his forum when he goes broke,” one member recounted.
A relatively new Telegram channel called “The Battle” has been doxing and needling Rey and other alleged ShinyHunters members for several weeks, and it has gained a considerable readership among the cybercrime communities operating on Telegram. One of the coordinators of that harassment campaign repeatedly portrayed Rey as clueless greenhorn who sought to ride the coattails of a cybercriminal brand that has long enjoyed a reputation for ruthlessly selling or publishing data stolen from victim companies who refuse to give in to extortion demands.
“Rey (Saif Al-Din Khader) made a serious mistake when he started pretending to be a member of ShinyHunters,” wrote the administrators of The Battle server on Telegram. “That group had already been dismantled, with many of its members either arrested or imprisoned, yet Rey still chose to use its name while carrying out his crimes. We’re aware of claims that [Rey] caused over $200 million in damages and helped around 5–6 friend groups in the community make money by using Shiny Hunters group aliases to negotiate deals for a 25–30% cut over the past few months.”
In an interview with
The Register
, ShinyHunters claimed they hacked the FBI to counter the agency’s narrative in
a May 2026 alert
that advised victims against paying a ransom to the group, which came off looking unprofessional and capricious in the FBI’s advisory.
A flash notice on ShinyHunters released by the FBI on May 15, 2026.
The public notice warned the group has been known to pursue a number of
different victim harassment strategies
, from sending threatening text messages and phone calls to victims and their family members to in some cases
swatting
victims. The FBI warned ShinyHunters members “may also falsely claim to have sensitive or compromising information, including embarrassing photographs or videos of victims, which frequently do not exist.”
The hackers told The Register their attack on the FBI “demonstrated our technical capabilities and directly refuted the misinformation disseminated by the FBI, journalists, and industry researchers.” At the same time, the group’s leaders seemed to acknowledge that the FBI’s warning materially harmed their prospects for convincing victims to pay, saying “this was fundamentally a public relations and marketing initiative for our business.”
