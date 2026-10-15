---
title: "The still unregulated solar power clouds: notes from 9th E.DSO - EE-ISAC - ENCS - ENISA Cybersecurity Forum"
url: "https://berthub.eu/articles/posts/solar-nightmare-at-the-conference/"
fetched_at: 2026-10-15T10:01:37.292560+00:00
source: "berthub.eu"
tags: [blog, raw]
---

# The still unregulated solar power clouds: notes from 9th E.DSO - EE-ISAC - ENCS - ENISA Cybersecurity Forum

Source: https://berthub.eu/articles/posts/solar-nightmare-at-the-conference/

Last week I attended the 9th
E.DSO
–
EE-ISAC
-
ENCS
–
ENISA
Cybersecurity Forum in Brussels. And as I had nothing to present, I tried to make myself useful by writing up an
apparently well read live-blog
(better version below!).
At this conference, hashtag #CyberGrids26, all relevant people were present. Regulators, European Commission, electricity generators, the organizations that
transmit
and
distribute
the power, vendors, researchers, standardization bodies: basically everyone.
And yet, we barely discussed the elephant in the room, and what I came to Brussels for
. The cyber aspects of domestic solar panel inverters, heat pumps and home batteries are
unregulated
since individually they are small fry. Yet, these >100GW contributions to our power grid are now
centrally
managed from
incredibly weakly secured non-European clouds
that could fall victim to the
ransomware attacks that are happening all the time
. This means there is a clear and present danger of hackers shutting down our societies, possibly as part of geopolitical ‘gray warfare’/hybrid attacks.
Transmission operators state
even a 3GW disruption
would take down their grid. And all this without regulators acting, for all kinds of reasons. This problem is
well known
and has been discussed for over a decade
.
The Dutch government just released a great report about it
(in Dutch, for now).
This #CyberGrids26 conference would’ve been the very best place to finally start addressing this problem, but except for brief moments, we didn’t. Now, the way back is also not easy.
The existing regulations
all don’t
quite
cover a cloud that controls 1TW of distributed solar power, but which (
as shown this week
) allow access
without supplying a password
.
NIS2, CRA, network codes etc all only touch on the problem. This leaves governments hesitant to act, since they lack a strong basis to do so. And what should they do?
Immediately do market surveillance to figure out the biggest clouds in terms of GW controlled
Forcibly audit these mostly Chinese companies to assess their cybersecurity
Force them to patch up the worst problems immediately, and also install 24/7 third party monitoring
Hardware Security Module supported firmware integrity checks, with formal verification
Institute architectural changes so that the clouds do not directly control the equipment in people’s homes:
authorize the individual users, so that only they can reconfigure their setup
Ban entities unwilling to relinquish such control
And we should hurry - we are now multiplying the solar panel problem by adding hundreds of gigawatts of heat pumps and home batteries, all of them also capable of overloading/underloading the net with
a single ransomware attack
.
Needless to say, the steps outlined above will require
emergency legislation
. The Cyber Security Act might have some appropriate options. But we won’t achieve anything with kind letters and exhortations. I do realize that no individual agency or even member state can solve this on their own.
I want to praise the single Belgian DSO employee who raised the alarm about this in the final few minutes of the conference Thursday. “We need government help, we can’t solve this as a grid operator”.
Please do read on for the very worthwhile other things we discussed, many of which are in fact shaded references to the better regulation we would need. The elephant was present in the room, and we did talk about the challenges, but sadly mostly indirectly, and only very briefly directly.
We could also do this,
but somehow we don’t
UPDATE: October 1st, the
Smart Energy Expert Group (SEEG)
Working Group on Cybersecurity
released version 1.1 of their report
Recommendations to address cybersecurity risk in photovoltaic generation
, and this appears to contain a lot of good words on the problem.
Report of the conference
Here is a somewhat cleaned up version of my live writeup. DO NOTE WELL: This is not super accurate. It is not appropriate to quote people from this live report. If you want to cite what someone might have said, please do take it up with the speaker first!
Still, I do suspect that this writeup could be of value for the many people that could not attend the session in person.
And you can also
access the slides of the presentation here
. And here are
also some great photos from the event
(both offered by the conference organisers).
The live report (and do check before you quote someone!)
Today I’m at the 9th E.DSO – EE-ISAC - ENCS – #ENISA Cybersecurity Forum
“Holding Together in a Changing World: Grid Cyber Resilience and Preparedness” - and as I have nothing to present, I will liveblog the conference.
The whole program can be found
here
.
And I’m sure will be talking about:
Source, member of European Parliament Bart Groothuis
Technical details on this hack
:
“So there seems to be eight (or more?) different ways to log in. We started iterating through the numbers and when we hit five, we were immediately logged in.” - these people control 1000GW of solar power. Set login type to 5 and you are in!
Good news, we have a hashtag! #CyberGrids26
Opening statements
The opening statements note that Japan EE-ISAC and North American EE-ISAC also traveled to be present at this European event, underlining the importance of the cybersecurity of the electricity grid.
https://www.ee-isac.eu
Ercola De Luca, board member of E.DSO, and of the Italian grid (Areti), is the first speaker. “Cybersecurity preparedness in a changing geopolitical landscape”. #cybergrids26 This on top of the energy transition. Natural response: add a lot of stuff to the grid. But if failure happens, you can’t point to your 30 year old study book. If you did what was in there, you are not resilient in 2026.
De Luca notes we should be brave, and not do business as usual. We should do new things, and he lauds the visitors for showing up, because this means we care about the grid in Europe. This is great kickoff for the day. Grid operators have historically been staid and stable organizations. The world is wilder now!
Dimitra Liveri of ENISA
Next up
Dimitra Liveri of #ENISA
.  ‘Cybersecurity preparedness in a changing geopolitical landscape". Head of resilience
of critical sectors unit. Asks: how can we be ready for what is to come? Notes that energy is one of the most critical systems in society. Electricity is hiding everyone’s threat model, often unwritten. The energy sector is changing towards efficiency and sustainability. But not necessarily resilience to cyber attacks.
Liveri highlights security by design. We’ve been talking about this for 30 years. Discussing it. But we need to DO it. She goes on to talk about supply chain security, the energy world is highly connected. Stuff is remotely maintained. Notes that not all 27 EU countries can build their independent cyber security. The EU ICT supply chain toolbox can be helpful, including with High Risk suppliers (🇨🇳). Mentions Cyber Security Act 2 revision. “We should be prepared”
Liveri goes on to talk about AI and notes load of people will talk about that. AI can optimize operations, but bad actors can also use AI to hack, and the AI itself can be vulnerable. Question is, can we deploy AI security while retaining enough control, and can we work with external failure (USA down?).  Mentions various EU acts that support cyber security. The regulation exists, we have started implementing. Notes three shameful EU member states that have not enacted NIS2.
Resilience across the entire energy ecosystems, actually test it, cooperate more. We are not there yet. The ecosystem grows, but the collaboration is also growing, but we need to expand this to other sectors. We need to simply the regulatory requirements into things you can do. We need to invest in people, capabilities, cooperation. We need lots of skilled people! We need to make everything resilient, and energy is at the heart of that.
Polish grid hacking incident of 2025
Chair notes that our interests are moving beyond the energy generators and transmission systems: we need to protect the whole ecosystem. Next  up Jeremi Gryka, senior expert, Polski Sieci PSE, who will talk about
an attack on the Polish Energy Sector in December 2025
.  PSE is the polish national grid operator. 51% of the power mix is renewable energy. 25GW of solar power peak.
Attack number 1: 29th of December 2025. On that day no problems were known. PSE ICT was working normally. A few renewable energy systems had cyber problems, but they had not informed PSE.  There were some communication problems with the renewable generators, but not exceptional. Lots of wind power.
Serious focused cyber attack against infrastructure of polish RES and CHP operators. I am not surprised to hear FORTINET was involved. The Fortinet devices were taken over using stolen credentials. Attackers had access since Q3 of 2025. On the 29th specific devices were rendered unusable by uploading bad firmware & rebooting & no longer working. Electricity generation was
not
affected. Grid connection point facilities were affected, but things continued to work on autopilot.
Attackers wiped many devices, removing traces of their activities. Wind and solar farms were rendered inaccessible. People had to physically go there to fix things. Multiple facilities relied on a single affected ICT provider. This was the first part to the attack.
Combined Heat and Power (CHP) systems were attacked. Entry point of attackers unknown. They gained access in Q2-Q4 to Active Directory. This attack was against office IT and was detected mostly in time. Energy production was not affected. The cloud services used by power plant were also taken over.  Exchange, Teams, SharePoint, copied important and sensitive files. OT and SCADA systems related.
“Private” GSM APN setup was also compromised, used to scan further systems. They managed to breach a small CHP plant, 50000 people city, and the attackers managed to briefly disrupt power  /heat generation. Access through badly configured access devices. Staff were paying attention because of their own ongoing maintenance, and were able to fix things quickly.
Later 2026-01-19 the PSE websites were attacked, not very successfully.  But service was briefly disrupted. Not super interesting, however the attackers (“QuietSec”) wrote about their attack, and claimed to be Russian “to open fire against Poland”. Next up, lessons learned.
This was a first of a kind attack on Poland. Long term pre-positioning. “AI and automation used extensively”. There were few effects, was this just a test? It felt like “digital arson”. The attack could have been way worse. They might have destroyed turbines. Or stop the energy production, they didn’t try. Root causes: simple routine hygiene gaps. Default password, reused passwords, no MFA, non-updated devices, bad segmentation. (THIS IS ALMOST ALWAYS THE CASE, GET THE BASICS RIGHT!)
PSE notes they were not themselves compromised and formally had no role. They coordinate the grid, and apparently that also includes coordinating the cybersecurity aspects. This cooperation was a bit slow to start but then went well. Lots of great followup, Poland has learned a very important lesson. Lots of media coverage, they consider it important. My note: Other countries should learn from this, I bet you are as vulnerable as Poland was! Poland documented this in English for our benefit.
(coffee break now - but I want to commend the Polish grid operator for doing a great job of
spreading the word
. The even went to hacker conference DEFCON to present on it.  I hope we’ll all take this seriously!) Will be back in a bit! #CyberGrids26
From Rules to Readiness: Making cyber regulation work
Back! Panel discussion time. Kick-off by Marta Grosso of the EE-ISAC. “From Rules to Readiness: Making cyber regulation work”. Resilience is key, she notes. And we hopefully can find solutions. The panelists will now comment on their initial insights.
Ruud Kempener
of DG ENER, European Commission. He notes he is from the “rules” side of the equation and he hopes to learn.
Øyvind Anders Arntzen Toftegaard
of the Norwegian Energy Regulatory authority is also a university researcher (NTNU) and he talks from his position as a researcher today. He notes that regulatory and operations are like two different countries and he hopes we can bridge that gap today a bit.
Carolina Cruz from Energy Storage Europe
comments on rules that come into force the coming months. Energy storage is like a house, people enter it, and you’d like to have control over it, know about it. Mentions that NIS2 tells you about the lock, but you need more rules about keys etc.
Zuzana Vobis Magurová
from E.ON, E.DSO. She also mentions the gap between regulation and operation. Regulation should set the scene, and not strangle operations. We as operators have an inherent interest in keeping things safe, and we like regulation that is lean and targeted.
Ron Wibbelink
, TenneT TSO The Netherlands, with second hat, convener of the
ENTSO-E Workgroup for the Network Code on Cyber Security
. Ron says he personally bridges the gap between regulation and operation. From TSO perspective, there is a lot of regulation coming. A lot of work to translate into operations, but he believes in it. He says that regulation is important since the European grid could otherwise face a blackout.
Panel question for Ruud, NIS2, CSA2 etc, where do you think the regulatory is solid today, and where are there still gaps? Ruud (EC) notes everyone sees more risks. He just came back from an oil conference, and the dependence there is terrible. But electrification can save us. And we can do that HERE. It is our challenge and we can solve it.
“However”, we are moving from a simple network dominated by a few parties, to a very complex ecosystem of suppliers/operators/consumers. Supply chain risk. Our legislation tries to address this. Notes a report written by the room on solar power security. Goes over the legislation, but report notes there are still gaps. Especially behind the meter. That part is not covered. (INDEED).
Ruud Kempener also notes that the impact of AI as as yet unknown (because of trading, optimisation etc). Will bring new vulnerabilities. Ruud rounds up that we’ll always be behind on regulation, and that all our feedback is very important to improve that.
Zuzana Vobis Magurova (E.ON, E.DSO) comments that Europe should  be a regulatory frontrunner, so should hold the pen, set the standards. Notes progress, reporting obligations now have a ‘single entry point’ rule in development, which will save a lot of time. Dependencies, supply chain, covered in different pieces of legislation. Calls for supplier DIVERSITY, suppliers that are physically able to deliver stuff. Argues for more Chinese suppliers which should not be banned. “We should mitigate”
Øyvind is asked, is NIS2 an important change compared to NIS"1". Øyvind asks what is security? “Good security is when nothing bad happens”. Security is not reports with KPIs, unless it directly helps. Calls for more directly useful things. Notes many operators don’t know well how their things work. Energy suppliers need expertise that is better than the hackers! NIS2 etc is a lot about reporting. Not how about you get better at cybersecurity. We need budget, knowledge, people.
“We need budget, motivation, knowledge!” (hear hear!). Legislation kills motivation. Budget goes to reporting people. Not to good motivated people. Knowledge of risk management people, that is the knowledge you get. You don’t get technical knowledge. BUILD A STATUE OF THIS MAN!
Øyvind notes things are really not getting better. NIS1 was a failure. Created a shift to doing A, B and C. While more technical measures, which was soft requirement in NIS1, get pushed aside for concrete perhaps not very useful things. Shift in goals to paper requirements. Not helpful. The bad guys are not kept out by reports!  Chair notes that is a KEY TAKEAWAY.
Caroline Cruz, on distributed energy storage, is the regulation good? Mentions that the industry experiences uncertainty about legislation , don’t know what to do. Says there is enough legislation. Now industry should do it, and perhaps go beyond regulation. “It is also good for us”.
Ron Wibbelink, does the legislation support vulnerability disclosure? Talks about vulnerabilities and incidents together, notes that legislation will help collect data & spread it quickly to the right people so they can learn. Speed is key here. #ENISA has taken a good step here. DSOs however need quite specific data and that specific part needs to be improved. We should cooperate here.
He (Ron) tells of a feasibility study of sharing information rapidly. Network code mandates  information sharing, which is good. Network code is immediately in force. Does not need to be transposed. This is all necessary threats are increasing. Moderator Marta notes that all organising bodies share the enthusiasm for such information sharing.
Zuzana is asked, how do you build the overall resilience to cover smart meters, the work force, plus the physical risks. Zuzana refers to the European parliamentary report written on that.  On the changing threat landscape. Gregor MEP report talks about smart metering, battery storage systems, edge devices. As DSOs we recognise this. The attack surface is increasing tremendously. Resilience is now important everywhere. Good procurement, supplier management, and the workforce.
Cloud systems, identity management in cloud, customer interfaces, mobile workers, all that needs to be encompassed. Processes, technologies, security wizards. Still need to work on awareness. Still basic hygiene stuff to address. (TRUE). Jokes a bit about corporate cybersecurity training. But important. “It is culture”
Øyvind speaks again: what is the next wave of developments. He notes that regulation is not all bad, since he works at a regulatory authority. But notes that resources should be put in place against actual attacks, to protect OT systems. NIS2 is silent on that. You might think it is in there, but every member state can do it differently. Companies take shortcuts in compliance when they can.
He is worried about skills level. People put a Chinese firewall with a guessable password on the internet. “but it is compliant”. Simple penetration testing always finds issues even with “compliant” places. The legislation will not solve this. The attackers are very motivated and our finding our gaps. We need motivated security staff, with the funding they need, with the knowledge they need to close the security holes.
Ruud Kempener of the EC chimes in. We can’t secure the world with rules. He’s a chemical engineer, applied for a job there long time ago, and was amazed by the security culture there. This was NOT because of rules, but it came from culture. “Hand to rail”.  Everyone agrees.
Audience question time! How do you convince your board? How do we get the executives to do their part? What would you like to see in the future for that? Ron of TenneT responds, we do need regulation for that. It gives us more power beyond the TSO.  Cyber risks are the biggest risks.
Notes that executives can be incentivized using regulation, and that especially the solar inverter field needs that. “We need to help them, they are willing”. (personally I’m not that certain about that). Ron wants to make legislation turn security into a business model.
Audience repeats the question, how do you get the executive board on board. Ron notes that this can indeed take some time. And legislation alone is not enough. “Investment is starting up now”. It helps convince leadership that so much is happening in the world. Executives now believe this is work that needs to be done.
Øyvind notes that Ron is arguing to regulate the rest of the world, and not the TSOs. Øyvind notes enhanced regulation showed a decrease in cybersecurity over at large companies, whereas the small ones are getting better [due to legislation]. But the large companies only turn “more compliant” but not better.
Zuzanna now states that DSOs really are motivated. They want to do good security she says. She argues for specific regulations that forces them to do specific things against a deadline.
Carolina Cruz from Energy Storage Europe talks a bit about green data centers, European goals, “how can we strike a balance between regulating the small guys”. Øyvind again notes how you can kill motivation to do the right thing with regulation. But it doesn’t need to. Asking for supplier diversity does not kill motivation.
Øyvind is my man! He notes most of the authors of the new network code had no background in these things at all. And that leads to rules that lead to friction. Involve more experts please. Ruud now defends the network code, notes that the implementation (made by Ron’s people) will now be done by experts.
Audience suggests using NIS2 to force compliance from vendors. Belgian speaker notes CRA compliance is being postponed,  suggests that vendors already demand CRA compliance ahead of enactment. Mentions DORA [banking resilience legislation] as well as an example. Might be inspirational (I agree). He wonders, if it now takes 175 days for industry to patch, how much is information sharing going to help?
Ron of Tennet /ENTSO-E comments on the slowness of deployment of patches. Says that OT requires more testing. On the other hand, if you had sufficient resources, you could have a REAL live testing environment, which might speed up deployment. “We’re not there yet”. So we don’t quickly deploy non-essential patches. This is not true for our internet-facing systems of course.
Audience from Ireland now compares our situation to the car industry which is indeed fully regulated. It took 50 years, but it does work, is that the way forward? No real answer. Personally, I note that industry is making an absolute mess of their cyber things.
Ukraine and AI in the SOC
Next on stage, UKRAINE!  NPC Ukrenergo presents on “Experiences and Developments , running a security operations center through a full-scale war”. 🇺🇦🇺🇦🇺🇦
Ukrenergo is the transmission system operator, synchronized with the European grid since 16 March 2022. “We do ISO 27001, but the enemy writes our rules”. 15 people (!) run integrated IT and OT SOC.
Lost 50% of staff to military service. SOC is now distributed across people and work locations. Suppliers stopped deliveries and support because of the war. “The grid does not get a maintenance window”. Now onto AI. Painfully good phishing attacks, faster malware, deepfakes and pretexting. They fought this through analysis of communications.
They demand second factor out-of-band verification of all communications.  They use AI for analysis, to compensate for the people they lost to mobilization.  “AI proposes, human decides, and not in OT environment”.
(can you imagine how a non-war-impacted TSO would respond do AI-enhanced phishing and impersonation?)
“Write down your knowledge in case you lose people” - people are the fragile part [in war]. “AI as a force multiplier in a Wartime SOC”. They lost vendor support, they did not offer “Wartime support”. They paste their problems in AI now and get better support than from vendors.
(with AI they built all kinds of interesting things from cybersecurity, included automated analysis of incidents, the analysts get a good initial start from their local models. The goal is to support the analyst). They have replaced many lost people with AI, and it works well for them. They did not do the AI because it was a hype, it works for them). Now, lunch break!
DIVD hacking demo
And we’re back from lunch! Chris van ’t Hof, Harm van den Brink and Humza Ahmad from ENCS will demonstrate a live hack and resolution of a high power IoT device. Chris from DIVD starts with a talk on “how we hack the power grid to make it safer”.
Chris starts with an introduction of DIVD, “we hack the whole world”, together with our partners like ENCS.
https://www.divd.nl/
and
https://encs.eu/
- “DIVD provides a place where helpful hackers can do their thing”. Also some other people, by the way.
Chris notes DIVD itself got hacked, and they get a lot of threats of lawsuits, but so far they themselves never had to go to court. We now move to their latest discovery, a solar panel control panel, for 10GW of power over 1 million subscribers. The control panel could also send out new “improved” firmware.
https://csirt.divd.nl/cases/
They contacted the vendor, who somewhat improved their act, but they never really fixed it. So DIVD went to the press and to the @Dutch digital government infrastructure inspection agency and they confirmed the situation was terrible. But government had no power to act. DIVD investigated the Enphase inverters subsequently. And the found they could try random customer numbers and gain access to random customers. DIVD assigned this a CVE vulnerability itself. And published the vulnerability.
DIVD moved away from the US vulnerability numbering system and moved to ENISA “since we no longer trust the US government, sorry Americans”. An American in the room chimes up “we also don’t”.  Publishing such hardware vulnerabilities with CVEs is good for supply chain awareness.
Chris explains how ENCS does testing on inverters, and they found that SolaX inverters have a very weak cloud setup, and they could hook into the MQTT stream of Sungrow, and see everyone’s data. Shows logos of Sungrow, Mennekes, Huawei, SolarEdge, Growatt and tell us they created 100 vulnerability CVEs for these vendors.
However, it turns out that some vendors do not respond to vulnerability reports. And then DIVD goes to the government, and the government will approach the vendor. Four vendors have now finally responded via this way. Some of these report were filed in January, but were only published now after intervention from the Dutch government.
Chris explains that DIVD is allowed to do this hacking because of Dutch law, which gives them the room to do this. Chris now explains how they themselves got hacked some time ago, through their helpdesk system Zammad, in which there were 2 0 days. They have now published the details of how they got hacked. NCSC-NL and ENISA have also been helpful. They have found notes in the hacked systems which are clearly AI-generated. And it looks weird. DIVD does this for free, and they are out of money.
Chris explains how big a benefit they supply to the energy community, and they’d appreciated some donations. Now, it is demo time! Harm van den Brink and Humza Ahmad from ENCS on stage now.
Here their battery box is what they are likely going to hack.
They explain you can do cloud based attacks, or locally, and they are going to do a local approach: Modbus. A 1970s plaintext very simple protocol. It does reads or writes, that’s it. Modbus is usually segmented because it has no security. In a home network, Modbus is typically very exposed. Modbus now also exists on TCP. It used to be serial wire only.
An attacker needs access to your home network somehow, and then they can talk Modbus to your stuff. Harm explains that the cloud vulnerabilities are too sensitive to disclose because they are 10-100GW scale vulnerabilities. This is a smaller local exploit, but attackers could also scale that.  They now show a Roomba cleaner, and Battery box, connected through their Wifi.
The vacuum cleaner has been hacked! It has connections to local devices, like the battery they show. They also have a lamp that is connected to the battery.
Harm promises that the vacuum cleaner will now clean! It does so. And now the light goes out, because the vacuum cleaner has hacked the battery. They repeat this to show that it works. Nice.
Humza now has some recommendations: turn off Modbus, and industry should move to better protocols that do have encryption.  Now we move to Q&A: Do you also scan IPv6? No, there are too many of them. Was it easy to hack the Roomba? How did you do that? Harm notes you can simply buy access through televisions/residential proxies.
Harm reiterates that the cloud is a far bigger worry. Question from the audience, is there something better than Modbus? MQTT could have TLS, but could also be insecure. Harm notes they are working together with ELAAAD (?) to write better protocols.
Panel: Building resilience: standards, supply chains & risk in action
“Building resilience: standards, supply chains & risk in action”. Headed by Heloise Enjalbal of ENCS. Panelists from EC (DG CNECT) , CEN/CENELEC, WithThegrid, ENISA and
I-DE
;E.DSO.
Every panelist gets an initial comment. Yonas from ENISA starts off with saying that the CRA is not going to make everything secure, but devices will start to become more secure, secure by design. CRA will make that happen.
Catherine Vigneron of CEN-CENELEC one of the standardisation groups in Europe. Catherine explains that their members are 34 European member state organisations. “Experts build standards”. Experts appointed by experts. (UNLIKE ETSI, she doesn’t say).
Paul Mignot of Withthegrid/windenergy, formerly with a grid operator, asks who is controlling the control layer, and what will it cost? Who controls the flexibility is important. The ability to control flex is “locked in”. We need flex for grid congestion. This is locked in to the manufacturer cloud, it is locked in to the trader. Changing this for more flexibility is expensive.
Paul calls for an independent layer, what are the security standards that we need? But also an energy system where we are in control ourselves. This layer needs to be sovereign,, European, flexible on asset and trader side, and must meet all the regulatory requirements. Sounds like a good idea.
Marta Solaz Hernandez (i-DE) now comments on the goals of DSOs: keep the lights on. Very neat and simple mission she says. Things are becoming more complex, lots of interconnections, technology. As DSOs we need data, digitalisation, we need technology. Notes that infrastructure is behind on that. Resilience is no longer local, but it goes abroad and to other places. “We don’t feel cyber secure only managing our own infrastructure”. Supply chain, technology, services: all worrying.
Standards can help, common language, a baseline, cooperation. Standards and regulation will help, but we also need to train and drill and test ourselves in a crisis scenario. Resilience is minimising impact, being able to continue to deliver service. She worries about dependencies [unclear to me which ones].
Matus Baliak from EC now. He notes many people have already said what he would like to say. He sees standards as major and essential. Legislation follows reality with a certain delay, 5, 10, 15 years. We can’t afford that anymore! We need standards so we can speed up. Developing standards is still challenging, capacity, time. Asks for more and better involvement with standards setting.
Heloise asks Matus what the role of certification can be. He worries most from the supply chain, vendors, software suppliers of connected equipment. If one supplier is compromised, this percolates through sectors and across borders. What we need to do to address this. Certification needs transparency. “What is in their supply chains?”. Entities can then not fully identify their risks. [talks of things I don’t understand on standards]
Catherine from CEN-CENELEC. Our standards come from committees. Agreed sets of rules. Lauds standards some more. We all love standards! [once we have them]. CEN-CENELEC goes on about the CRA, that they work on it on behalf of the EC. “We’re almost there”. CEN-CENELEC also works with other standardisation bodies. Standardisation is really great and important. Resources important too. Everybody should be at the table. More generic talk on standards. Standards!
Marta Solaz Hernandez (E.DSO) is asked, how should utilities and manufacturers share responsibilities, and where do these responsibilities begin and end. She notes cybersecurity is always shared. She thinks manufacturers are responsible, and DSOs need to deploy correctly. But it still is a shared thing. CRA will help. Obligations on the vendors. It plugs a gap. DSOs needs to manage their suppliers & dependencies: the basis for resilience.
This is not just a matter for contracts, not just add the requirements [cra etc]. We must do audits on our suppliers, we must manage our service very closely. We must work very closely during events, during training, involve them in our business continuity plans, have them join our exercises, so we can work together in an event. [This sounds very good, and unlike some DSOs]
Marta again stresses managing dependencies. Minimise even, keep track of them. We may need additional suppliers so if one vendor drops out, we have other options. Mignot of Withthegrid notes that they supplied sensors to DSOs on non-critical sensors. LOADS of regulation. Now when he supplies electricity management and trading: no regulations at all. CRA is again going to help, but far to go.
“We are missing the link between the cybersecurity standards and the grid themselves”. If you mess up your cybersecurity, you can stay on the grid. If you mess up the requirements for generators your assets get removed from the grid! But cyber is fine. Recommends balancing these risks - they are just as important.
Yonas Leguesse from ENISA also lauds standards and the hard work that has been done. In terms of lessons learned, recommends “reuse and not reinvent”. Mentions the Radio Equipment Directive (RED). I think he says more should have been reused. Are we ready? A standard is just the start. ENISA followed up with ’notified bodies’, who need to know what to do. Ecosystem still needs to grow, but Yonas thinks it is looking good, good baseline.
CEN-CENELEC’s Catherine weighs in, she states with the CRA they did not start from zero. ETSI and CEN-CENELEC had to develop a lot of standards. “Start with coherence between experts and industry as soon as possible”. Make sure the right expertise is around the table, not easy. This means training experts how to do standards.  Standards need to be developed quickly but they also need consensus. Catherine again thanks the experts & how hard they worked.
Are we ready or not? Well. Standards are processing well, many have finished the first step and about to be sent of to ? which is the first step. Heloise also comments, the experts are working very hard. It is a colossal project, we try our best.
Matus from EC: how are the vendors going to comply? He explains this is a newly regulated sector, and it will take time. Matus also thanks the experts, CEN-CENELEC, ETSI. Worries about capacity for conformance checks. Also working with the common criteria community on surveillance. Also notes the possibility of the delegated acts [in case things are not moving along].
Matus thinks the common criteria mechanisms will work to get vendors to comply with the CRA. Again notes the work on the delegated act and the presumption of conformity [these things are very important to hear for the CRA community]. Want to help manufacturers to match the requirements.
Paul Mignot is asked if the existing standards are sufficient for the rapidly evolving landscape with home batteries etc. Withhegrid sees “small things at home” as as problem, and the risk assessment of cloud controllability. That is where the gigawatts of capacity is. There is no regulation there (!). The OEM cloud is huge, we can’t quickly replace it. We need some kind of CC for OEM/Vendor clouds (YES) in order to be able to safely offer flexibility solutions, which is where the value is.
EVs, solar panels, heat pumps, batteries all need to become dynamic. The MONITORING clouds are not good enough not safe enough to actually CONTROL those gigawatts. Paul sees a future where there could be a physical device, behind the meter, to control all of this.
Mentions a business case of a 100kW grid connection with 300kW of generating/consuming devices on there. Can only work with a local edge device that coordinate all that safely to stay within 100kW. That is a business case.
Heloise asks, how should we deal with legacy equipment, sometimes out of support, and clearly pre-standard. Marta Solaz Hernandez responds, mentions again the dependencies, and this might impact us (DSOs). OT infra is not comparable to IT servers. Very long lifecycle investment, we cannot replace overnight everything, integrated in everything. Needs new documentation training monitoring. We need a balance, “a risk based approach”. This will give us some time, maybe 2028, 2029. This is after CRA
Marta Solaz Hernandez of i-DE/E.DSO Advocates for defense in depth, and not hurriedly replace everything. This means figuring out what is critical and what not, and what the paths are. Notes that things are very unpredictable. They too need to work on their devices. #CRA Conformity assessment is not yet delivered by EC. This makes it hard to be compliant! A lot of concern within DSOs. There is legal uncertainty who needs to comply.
Next up, audience questions. Your reporter’s brain has turned to mush, so only some highlights from here on!
Marta Solas Hernandez again (RIGHTFULLY) emphasises the need to inventory dependencies and TEST them. We discussed that earlier in the day also, keep it real, get those basics right. We can debate standards all day long, there is a lot of basic work that we need to start with.
Some unhappiness in the audience about the lack of enforcement of standards. DSO employee says they can’t enforce things. This is about the “behind the meter” area. Belgian DSO employee stresses the ENORMOUS impact of disruption of the grid is. “We must act on small devices with IP addresses that can kill the grid”. What is the point of the legislation if it can not be enforced.
This may be the most important part of the day. The gigawatts of electrical power per country controlled via absolutely terrible insecure cloud controllers remain unaddressed.
Finishing remarks from Slawomir Bryska from the ACER committee. He worries about the Polish attack, which was long in building.  He echoes the findings there - mediocre/bad cyber security. Basis hygiene not implemented.
The point was well taken that we need “wizards”, very good technical people, and not just more regulation. We need motivated people that work on our security. And not more forms.
Slawomir again underlined what Marta said, the infrastructure and OT challenges are enormous and require a lot of attention, including the dependencies. “This is the elephant in the room”.  Some remarks from ACER: it is a privilege to work with you, where “you” should be understood very widely. We all work on the European grid. ACER provides the covers of the book that everyone is writing.
https://european-union.europa.eu/institutions-law-budget/institutions-and-bodies/search-all-eu-institutions-and-bodies/agency-cooperation-energy-regulators-acer_en
ACER notes they work with actual electricity networks and generators and not just with other policy people. “We operate one layer lower”. ACER almost apologises for demanding precision and accurate answers, but they say the value is so high to get this right, they do it like this because it is so important.  ACER clearly loves the grid [I believe Slawomir]. He thanks us for our presence, and he hopes to be back next year!
And that ends the conference & also the live blog!
