---
title: "Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation"
url: "https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/"
fetched_at: 2026-09-29T10:01:08.933326+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation

Source: https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/

Authorities in the Netherlands have arrested a 24-year-old convicted cybercriminal on suspicion of aiding in data thefts and extortions by the prolific hacker group
ShinyHunters
. In the days immediately following the suspect’s arrest, remaining ShinyHunters members dramatically escalated their attacks, stealing highly sensitive data from the
FBI
and extorting the Russian ransomware group
Cl0p
.
According to three sources familiar with the matter, the Dutch man arrested by authorities this month is
Pepijn van der Stap
, a convicted cybercriminal from Almere and Lelystad in the Netherlands. Van der Stap was previously convicted in 2023 in connection with a string of data thefts and extortions that prosecutors said earned between €1.5 million and €2.7 million.
At his trial in late 2023, van der Stap admitted that he lived a Dr. Jekyll and Mr. Hyde existence, secretly using the hacker handle “
Umbreon
” to extort victims and post their data on English language hacking communities like the now-defunct RaidForums and Breached. By day, however, van der Stap was working as a software engineer at the Amsterdam-based cybersecurity startup
Hadrian
, while volunteering at the
Dutch Institute for Vulnerability Disclosure
(DIVD), a nonprofit security research group.
Pepijn van der Stap’s alter ego “Umbreon” selling a database on RaidForums, offering information on 2.3 million people from The Netherlands in September 2021. This user’s avatar is a depiction of the Pokemon character Umbreon. Image: KELA.
Van der Stap confessed to his data theft and extortion activity, and was sentenced to four years in prison (one of which was suspended). During his trial, van der Stap opted to remain in custody for a time rather than at home, saying he could not find better treatment on the outside for his ongoing psychological issues, which he claimed included PTSD related to childhood trauma. He was released from prison in December 2025.
In an interview with KrebsOnSecurity on September 9, 2026, Van der Stap cast himself as a reformed hacker who was trying to turn his life around and make a positive contribution to society. Van der Stap is currently employed as offensive security lead at the Dutch company
Neo Security
, which did not respond to requests for comment.
Van der Stap said he was still dealing with civil lawsuits and restitution related to his previous cybercrime victims, and that he was trying his best to make amends. But not long after that interview, the Dutch hacker abruptly stopped replying to messages. Efforts by others close to him also repeatedly failed to elicit a response for the past two weeks.
The LinkedIn profile for Pepijn van der Stap.
According to two sources with knowledge of the matter, Van der Stap was arrested by Dutch authorities on or around September 16, and has been held in custody for questioning since. One source said a colleague of theirs personally witnessed Dutch authorities carting items out of Van der Stap’s residence.
Authorities in the Netherlands have been
asking the public for help
in identifying the voice in a recorded telephone call from February 2026 in which a native Dutch-speaking ShinyHunters member social engineered their way into
Odido
, the nation’s largest mobile telecommunications provider. In that intrusion, ShinyHunters tricked an Odido employee into logging in at a spoofed website, and then used that access to steal data on more than 6.2 million Dutch people.
Responding to Dutch news media, ShinyHunters confirmed that the suspect in the audio clip is indeed a member of the hacker collective.
“Our team member has our full support – emotionally, mentally, and financially,” the hackers said. “Everything has been arranged, including a criminal defense lawyer. We do not look down on our staff and members; we take excellent care of them,” reads a statement ShinyHunters shared with
NL Times
. It remains unclear if the Dutch police have matched the Odido caller to a confirmed real-life identity. The Dutch police unit handling the Odido incident did not respond to requests for comment.
The group also lashed out at the authorities in the Netherlands. “The Dutch police will need all the luck in the world – and everyone’s prayers – if they want to catch him before we carry out another large-scale data theft in the Netherlands,” the ShinyHunters statement said. “Frankly, the Dutch police are a big joke; they are incapable of doing anything. Incompetent. Irrelevant. Unimportant. Useless.”
FBI, CL0P HACKS
Just days after sources say Van der Stap was detained by Dutch authorities, ShinyHunters claimed credit for an unusually brazen breach at the FBI’s job application site apply.fbijobs.gov. According to
reporting from 404 Media
, the data stolen from the FBI site includes Social Security numbers and
personal information
on more than 5,000 officials.
404 Media and
Reuters reported
the FBI data included each person’s job title or team, such as special agent, threat intake examiner, major cybercrimes unit, and those investigating cyber threats from foreign state-backed actors. Reuters examined documents shared by ShinyHunters and found they included sensitive psychiatric and medical files of FBI staff. The FBI issued
a brief statement
confirming the hack.
ShinyHunters said it gained access to the FBI site and other victims by exploiting a recently patched vulnerability (CVE-2026-35273) in
PeopleSoft
, a software-as-a-service platform from the software giant
Oracle
that is broadly used by companies to manage hiring and human resources, benefits and payroll. Oracle quickly issued a fix for the Peoplesoft vulnerability that ShinyHunters reportedly began exploiting as a zero-day in June, and at the time Mandiant released web application firewall rules intended for organizations who couldn’t apply the security update quickly enough.
But on Friday, BleepingComputer reported that ShinyHunters
used a URL-encoding trick
to bypass Mandiant’s suggested web application firewall rules designed to mitigate the threat from the PeopleSoft flaw. In
a report
released Sept. 25, security experts at
Mandiant
and the
Google Threat Intelligence Group
(GTIG) confirmed that ShinyHunters had mass-exploited the PeopleSoft vulnerability to steal data from dozens of systems across a range of industries, including higher education, technology, healthcare, agriculture, transportation and government.
Van der Stap’s former hacker alias Umbreon was hidden in plain sight throughout the imagery ShinyHunters used to spread news about the FBI hack: The defacement image that ShinyHunters left behind on the hacked FBI jobs site included an ASCII art design featuring the Pokemon character Umbreon. The message at the top read, “This site has been seized by ShinyHunters. rooting your systems since ’19 ;)” The image appears identical to a defacement message ShinyHunters used in their
2020 hack
of the English-language cybercrime community Hackforums.
The defacement message left by ShinyHunters on the FBI jobs site included an ASCII art rendition of the Pokemon character Umbreon. Image: Bleeping Computer.
Multiple sources close to the ShinyHunters investigation said the group’s recent risky attacks against the FBI and one of Russia’s most venerated ransomware groups amounted to a major pivot away from the more measured tenor of the hacking gang’s operations. Those sources said the sudden shift came about after ShinyHunters was taken over by
a teenage cybercriminal from Amman, Jordan
who goes by the nickname
Rey
and operates as part of a cybercrime group called
ScatteredLapsussHunters
(SLSH), which experts say is an amalgamation of three hacking groups —
Scattered Spider
,
LAPSUS$
and
ShinyHunters
.
Those sources said Rey had an ongoing beef with the Dutch hacker over control of the ShinyHunters brand and data, and that the inclusion of the oversized Umbreon Pokemon image in the FBI jobs site defacement was likely an attempt by Rey to pin the hack on the Dutchman.
Rey was
first publicly identified
by the cybersecurity firm
KELA
in March 2025. In advance of our
November 2025 profile of Rey
, KrebsOnSecurity messaged Rey’s father and asked for permission to interview his teenage son. Rey’s dad merely forwarded the message to his son, who admitted to participating in ransomware attacks and said he was trying to extricate himself from the SLSH hacker group.
BLAMING UMBREON
Immediately after news of the FBI jobs site hack was picked up in the media, Rey’s main account on Twitter/X (Ryan Moran/@rmoskovy) was taunting the Cl0p ransomware group and the FBI, crudely depicting them as the twin towers in New York being struck by planes labeled “cl0p drama” and “fbi breach claim.” In the foreground of the city is the giant Pokemon figure of Umbreon.
A taunting meme uploaded to Twitter/X by Rey’s now-defunct account on Sept. 22. A giant float-sized version of the Pokemon character Umbreon can be seen in the bottom left.
On Sept. 24, KrebsOnSecurity again contacted Rey’s dad, asking to interview him and his son for a story on Rey’s apparent ascendency as the head of ShinyHunters. Just hours after that request, Rey deleted his longtime Twitter/X account. Meanwhile, Rey’s dad, who works for the Royal Jordanian Airlines, has failed to respond to a half-dozen emailed requests for comment about his son’s alleged activities.
Where does the bad blood between SLSH and ShinyHunters come from? According to
a story in Wired
this month, ShinyHunters and SLSH members briefly partnered earlier this year to help better monetize important stolen credentials collected by
TeamPCP
, an upstart group that was having great success compromising global code supply chains with malicious software but hadn’t been able to profit much from their stolen data (two alleged leaders of TeamPCP
were arrested last month in Australia
, and in an interview the TeamPCP leader claimed they made just $20,000).
The Wired story noted how Mandiant had infiltrated TeamPCP and was secretly responsible for having the crime group’s stolen credentials burned so quickly: Mandiant was secretly feeding those credentials to the major cloud providers like Amazon and Microsoft, who quickly invalidated the stolen keys. Meanwhile, the formerly cooperating hacker groups began to blame one another for causing the credentials to become worthless.
Wired’s
Andy Greenberg
reported that a few weeks after partnering with TeamPCP, “ShinyHunters went rogue, carrying out its own extortions with TeamPCP’s credentials but without giving the supply-chain hackers their cut.”
Mandiant researcher
Austin Larsen
told KrebsOnSecurity earlier this month that ShinyHunters has been enjoying a successful extortion spree so far this year, and is on track to pull in nearly $100 million in extortion payments from cybercrime victims in 2026.
Van der Stap claims he was never motivated by money and that his earlier hacker activity was driven by a desire to have the world’s most complete collection of stolen databases. Speaking with reporters from Bloomberg in 2024, Van der Stap said that singular focus in turn fueled his desire to carry out cyberattacks.
“The hacking was very easy for me, and it wasn’t a compulsion,” he
told Bloomberg
. “My habit was collecting. Collecting data, organizing data, downloading data, creating folders.”
DIVD, the nonprofit security research group where Van der Stap previously served as a volunteer,
disclosed on LinkedIn last week
that the organization was dealing with an internal cybersecurity incident that appears to have involved the malicious use of artificial intelligence. DIVD has released few details about that incident, but a spokesperson for the nonprofit told KrebsOnSecurity it does not appear related to ShinyHunters, nor are there any signs the matter involves the work of a previous volunteer.
Update: 3:44 p.m. ET:
Corrected Van der Stap’s age, which is 24 (not 23).
Update, 4:54 p.m. ET:
The Dutch police have confirmed the arrest of a 24-year-old in connection with the ShinyHunters investigation. In
a statement on Twitter/X
, the Dutch police said the man will appear on Tuesday, September 29 before the chambers of the Rotterdam District Court, and that it will provide more information tomorrow.
