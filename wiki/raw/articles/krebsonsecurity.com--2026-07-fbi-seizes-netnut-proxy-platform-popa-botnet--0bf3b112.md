---
title: "FBI Seizes NetNut Proxy Platform, Popa Botnet"
url: "https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/"
fetched_at: 2026-07-03T07:00:57.304544+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# FBI Seizes NetNut Proxy Platform, Popa Botnet

Source: https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/

The
Federal Bureau of Investigation
(FBI) said today it worked with industry partners to seize hundreds of domains associated with
NetNut
, a sprawling residential proxy service operated by the publicly-traded Israeli company
Alarum Technologies
[NASDAQ: ALAR]. The action comes roughly two weeks after KrebsOnSecurity published findings from multiple security firms connecting NetNut to the
Popa
botnet, a collection of at least two million devices that have been compromised by malicious software with little or no consent from victims.
The NetNut homepage today was replaced by this seizure banner from the FBI.
On June 19, three different security firms
issued similar findings
: That NetNut is a residential proxy network which populates a botnet called Popa, and distributes software for devices commonly found in homes, such as smart TVs and streaming boxes. NetNut’s software turns those systems into always-on residential proxy nodes that are rented to others, who predominantly use them to relay abusive and intrusive Internet traffic, such as mass content scraping, advertising fraud, and account takeover activity.
Earlier today, NetNut’s homepage was replaced with a seizure notice from the FBI and the
Internal Revenue Service Criminal Investigation
division. The seizure notice thanked
Google
,
Lumen
,
Shadowserver
and other industry partners for their help in dismantling hundreds of domains tied to the Popa botnet, which experts say has long been synonymous with NetNut’s residential proxy infrastructure.
In a blog post published today, the
Google
Threat Intelligence Group
(GTIG) said NetNut’s proxy network is widely resold and white-labeled by a number of third-party proxy providers, and that its services are heavily sought out by cybercriminals seeking to obfuscate the source of their malicious traffic. The GTIG said that in a single week during June 2026, they observed 316 distinct clusters of threat actors using suspected NetNut exit nodes, including cybercriminal and espionage groups.
“These bad actors can use NetNut to mask their origin IP address when accessing victim environments, accessing their own infrastructure, and conducting password spray attacks,” Google’s GTIG
wrote
. “Furthermore, when a consumer device becomes an exit node, unauthorized network traffic passes through it. This means bad actors can access other private devices on the same home network, effectively exposing them to Internet threats.”
Google said it disabled Google accounts and services used by NetNut for malware command and control, and that it shared technical intelligence on NetNut’s software development kits (SDKs) and backend infrastructure with platform providers, law enforcement and research firms. The company also disabled apps known to bundle NetNut’s various SDKs.
Omer Weiss
, legal counsel for NetNut parent Alarum Technologies, said the company was aware of the FBI seizure and cooperating with investigators.
“Alarum takes this matter seriously and will fully cooperate with law enforcement to ensure any misuse of its infrastructure is thoroughly investigated and those responsible are held to account,” Weiss said in a written statement.
Benjamin Brundage
is founder of the proxy tracking service
Synthient
, one of the companies that
published evidence last month
linking the Popa botnet to NetNut and Alarum Technologies. Brundage said the domain seizures appear to have disrupted both the Popa botnet and the NetNut proxy network that rides on top of it.
Brundage said NetNut’s apparent demise is likely to be a great disadvantage for the cybercrime community, which was already reeling from
legal actions by Google
earlier this year that seized infrastructure for NetNut’s biggest competitor —
IPIDEA
.
“I think this takedown is going to have a big impact, because NetNut gained significant popularity after the IPIDEA takedown,” he said. “Also NetNut has been incredibly common among resellers, and they were on par with IPIDEA in terms of their daily traffic, quality, size, price per gigabyte, all of it.”
NetNut’s infrastructure, in a nutshell. Image: Black Lotus Labs, Lumen.
The NetNut and Popa botnet takedown may have another added benefit, Brundage said: Lessening the impact of large distributed denial-of-service botnets that have been built on the backs of poorly configured residential proxy services. In January, Synthient
revealed
how cybercriminals had built the world’s largest DDoS botnet (Kimwolf) by tunneling through IPIDEA proxy connections into the local networks of TV boxes owners, and infecting other Android-based devices behind the victim’s firewall.
While many of the bigger proxy providers took steps to block this activity, resellers of the major proxy networks have been far slower to respond to the threat, Brundage said.
“In terms of all these TV box devices getting compromised from the proxy network, it will have an impact on the DDoS botnets out there,” he said.
For its part, Google reckons today’s actions have caused “significant degradation to NetNut’s proxy network and its business operations, reducing the available pool of devices for the proxy operator by millions.” But the company warns that proxy networks can rebuild themselves by effectively reselling other proxy services, as IPIDEA has done over the past few months.
“Google has high confidence that many popular residential proxy brands are in fact whitelabeling the NetNut botnet,” the GTIG report concludes. “While we expect this disruption to have a larger ripple effect across the residential proxy ecosystem, observations after the disruption of IPIDEA proved that individual networks can appear resilient. What we have observed is that when faced with the degradation of their own botnet, proxy operators begin buying capacity from their competitors, effectively becoming a reseller. We recognize that creating a lasting disruption in this fluid ecosystem means we must scale our efforts to target the infrastructure of several interconnected providers.”
As KrebsOnSecurity has warned repeatedly, most of the no-name TV streaming boxes for sale on the major e-commerce websites either come
pre-installed with residential proxy software
, or require the installation of proxy SDKs in order to use the device for its stated purpose (streaming pirated movies, sporting events and TV shows). Google’s advice here is sound: When it comes to TV boxes, stick to name brands from reputable manufacturers, and then be sparing and judicious with any apps you choose to install.
The
sketchy TV boxes
that are being commandeered by the Popa botnet and other threats all come with or require the user to install unofficial Android operating systems that do not operate within the confines of Google’s Official Play Protect store. Google says consumers can confirm whether or not a device is built with the official Android TV OS and Play Protect certification by following
these instructions
.
Even people without TV streaming boxes can find their smart TVs enrolled in residential proxy networks, just by installing one of thousands of apps available for download on
Samsung
and
LG
smart TVs. In
a report
released last month, the proxy tracking company
Spur
found 42 percent of apps available for download via the webOS operating system on LG smart TVs include SDKs that turn one’s television into an always-on residential proxy node. More than a quarter of the apps made for Samsung’s
Tizen
operating system had similar residential proxy components, Spur found.
Image: Spur.us.
Update, 4:24 p.m. ET:
Included a statement shared post-publication from an attorney representing NetNut parent Alarum Technologies.
