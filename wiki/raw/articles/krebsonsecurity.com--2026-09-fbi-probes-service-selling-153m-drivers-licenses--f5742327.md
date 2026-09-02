---
title: "FBI Probes Service Selling 153M+ Drivers Licenses"
url: "https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/"
fetched_at: 2026-09-02T10:01:17.043716+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# FBI Probes Service Selling 153M+ Drivers Licenses

Source: https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/

A new identity theft service launched on the dark web this week is selling digital scans of more than 153 million drivers licenses from people in the United States and Canada. Based on interviews with individuals whose licenses are available for purchase on this service, it appears to be siphoning images collected by a widely-used identity verification company based in Louisiana. KrebsOnSecurity also has learned that the New Orleans field office of the
Federal Bureau of Investigation
(FBI) today launched an official inquiry into the source of the images.
A record available at this identity theft service that includes the drivers license for U.S. Defense Secretary Pete Hegseth, who is one of several high-ranking U.S. government officials whose drivers licenses can be found for sale.
On Monday, Aug. 31, a source alerted KrebsOnSecurity to a service advertised by a new user on the Russian cybercrime forum
Exploit
, offering access to digital scans of identity documents on more than 170 million people in North America. The source brought it to my attention because the proprietor of this identity theft service offered my Virginia drivers license as a free sample in their initial sales thread on Exploit.
The service, dubbed
Nexus
, claims to have more than 153 million drivers licenses for people in the United States and Canada, as well as more than 10 million identification cards; more than three million travel documents and/or international IDs; and at least 579,000 medical cards.
A quick look around Nexus finds they are likely not exaggerating about that 153 million number: Running a blank search in Nexus (with no search parameters entered) returns approximately 11.5 million pages of results, with roughly 15 results displayed per page. It includes documents from people in both Canada and the United States, but the bulk of these records are on Americans: searching for just Canadian drivers licenses returns approximately 1.1 million results, with the largest concentration from Ontario (473,673 records).
Curiously, the identity records include not only drivers licenses but also marijuana dispensary cards. Some of the records list their “source” as “CDL,” presumably short for “commercial drivers license.” Other records carry the source notation of “CAC,” which may refer to Common Access Cards, government issued identity cards that grant physical access to government buildings and secure rooms.
The people behind Nexus claim the license images are coming from an active breach at “a major identity verification company” whose customers include multiple Fortune 500 companies.
The record totals listed by the Nexus identity theft service. The number of drivers license records increased by nearly 400,000 in the span of just 24 hours.
“We have been continuously exfiltrating new data for over a year into our private database,” the service enthused in its introductory post on Exploit. “Records are available to preview before purchase with pertinent information redacted. Customer photos are displayed if available.”
Indeed, over the past 24 hours, the number of drivers license records listed as available in Nexus has increased by nearly 400,000, suggesting that freshly stolen license data is being harvested and uploaded to this service on a semi-regular basis.
The record that features my drivers license includes six image files — three pairs of photos of the license’s front and back — a basic image scan — as well as infrared and ultraviolet versions of the same images. A date and timestamp is appended to each image file, and the timestamp on my license scan corresponds to a date in June 2025 when I took a flight to the midwest United States to attend a family funeral.
Some of the 153 million+ license scans — including mine — feature six image files with date and timestamps appended to the filenames. Not all records include photos, and some that do feature photos do not display the associated filenames.
Intent on discovering the source of this data, KrebsOnSecurity asked more than a dozen friends and family members for permission to search for their licenses in this service. Each person whose license could be found (nine of them) confirmed having traveled on or very close to the dates in the timestamps attached to their images. It is unclear what timezone these timestamps are in, but from reviewing car rental records shared by several people who helped with this research, it appears the timezone is set to Greenwich Mean Time (GMT).
At first, I thought the source of the data might have something to do with airports. However, that theory went out the window when it became apparent there were no passports in this data set. Also, only some of those who helped with this research said they showed their drivers license at the airport on the day of their travel. One person whose license was in Nexus hadn’t flown at all recently, but was renting a car from
Hertz
for several months around the date of their timestamp.
Two of those who agreed to help are federal employees who said they shared other forms of government identification when passing through airport security. However, those individuals each said they shared their state-issued drivers licenses later that day when renting vehicles at their respective destinations, and that both rented their cars from Hertz.
After finding a note in my calendar for the day of my June 2025 flight reminding me to bring my passport, I remembered that I also never actually shared my drivers license when I went through security at Reagan National Airport on that day because I did not yet have a Real ID, a security-enhanced drivers license that is now required by the Transportation Security Administration (TSA) for all domestic travel. Instead, I showed the TSA agent my government-issued U.S. passport.
Here’s where it gets interesting: I was able to find my mother’s drivers license in this service as well, and the timestamps for her images are just a few seconds apart from mine. That’s notable because we both handed our licenses to the Hertz rental car representative at the same time.
According to my mom, the only place she gave her drivers license to that day was the rental car company, and if memory serves that is also true for me. I don’t recall if the rental car representative inserted our licenses into any kind of machine, but I remember they held onto them for several minutes behind the counter while we were signing various forms. KrebsOnSecurity sought comment from Hertz and will update this story in the event they reply.
Zach Edwards
is a well-known security and privacy researcher who recently launched a service called
DecryptAds
to help people better understand how online advertisers are tracking them. A scan of Edwards’s drivers license is available for purchase on this identity theft service, and Edwards said the timestamp on his record corresponds to the middle of a trip last month to Las Vegas for the annual DEFCON security conference.
Edwards told KrebsOnSecurity that although he did not rent a car in Vegas, he did hand over his license at the TSA checkpoint, at a marijuana dispensary in Vegas, and at his hotel (the Aria). But he said the only one of those three that for sure scanned his ID in some kind of device was the dispensary.
To enter Planet13’s weed dispensary in Las Vegas, one must pass through a red telephone booth. Image: Zach Edwards.
Edwards said the dispensary he visited that day was
Planet13
, a multi-state chain with stores in California, Florida, Illinois and Nevada. In 2022, the New Orleans-based identity provider
idscan.net
published
a press release
announcing an exclusive identity verification agreement with Planet13’s dispensaries nationally. IDScan says it processes ID verification for more than 1,000 marijuana dispensaries in 19 U.S. states.
The “trust” page of idscan.net states that the company provides identity verification services for numerous big brands, including Hertz,
Target
,
Fedex
,
Motorola Solutions
, the financial services giant
Jack Henry
, and
Caesars Entertainment
. And as idscan.net’s own
documentation states
, the technology scans IDs with both infrared and ultraviolet light. Idscan.net says the company’s systems and technology perform more than 21 million verifications monthly, at more than 20,000 locations around the world.
Image: idscan.net.
Contacted by KrebsOnSecurity, idscan.net said it was investigating the matter, but the company has not yet shared an official statement or a substantive reply to specific questions sent via email.
“At this point I’m not able to share any additional information, but the updates you have provided have been welcome, and helpful to our team’s investigation,” wrote
Jillian Kossman
, a marketing and operations leader at idscan.net.
During the course of my research for this story, word apparently got around to the FBI that I was poking at the apparent source of this new identity theft service’s data. Probably they were tipped off when I shared with a trusted source that Nexus also is selling the drivers license information for the assistant director of the FBI (I did not find FBI Director Kash Patel’s license in Nexus).
Earlier this afternoon, I was added to a conference call with a half-dozen FBI agents, including senior leaders from the agency’s cyber division. During that call, the FBI shared that earlier today their New Orleans field office opened an official investigation into an apparent breach involving idscan.net.
Edwards said that as more in-person and online experiences require sharing drivers licenses, vendors who collect this sensitive data need to be held to a higher standard.
“This episode should further strengthen the resolve for people who are fighting back against online ID schemes which are requiring countless providers to ask for drivers licenses in order to access services under the guise of protecting kids,” Edwards told KrebsOnSecurity. “These systems are putting sensitive data into more and more 3rd party vendors, and we don’t have nearly the oversight to ensure they are safe.”
Larry Baldwin
is principal intelligence researcher at the cybersecurity firm
Cybera
. Baldwin said a front and back scan of his drivers license available at Nexus contains timestamps that correspond to the date of a car rental from Hertz on a recent vacation.
Baldwin said the Nexus identity theft service presents multiple serious security and privacy threats, noting that state-issued drivers licenses are commonly used as proof of one’s identity when opening new lines of credit. Baldwin said the service could also dangerously expose many people who do not wish to be found but who cannot meaningfully change their appearance (or at least not enough to fool today’s AI-based image matching tools).
This category of people, he said, includes those fleeing domestic violence, and even people who have been assigned a whole new life and identity as part of the federal government’s witness protection program, which is generally reserved for criminal defendants in racketeering and conspiracy investigations who agree to cooperate with federal authorities.
“Just when it seems like we’re making some headway in improving authentication controls through drivers license verification systems, this happens and the very thing those improvements are dependent on are compromised,” Baldwin said.
Update, 8:56 p.m. ET:
Shortly after this story was published, the Nexus identity theft service website vanished from the darkweb, replacing its login page with a plain text message that reads, “This service is no longer available.”
This is a potentially fast-moving story. Any changes or updates will be noted here along with a timestamp.
