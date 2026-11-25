---
title: "Active Intrusion Campaign Against Check Point Security Management Servers"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
status: complete
sources:
  - "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
  - "https://news.ycombinator.com/item?id=50630594"
sha256: 881048757cf89471cbc8d105947807ccb67844d962cd06a56825c5a9a282a672
---

# Active Intrusion Campaign Against Check Point Security Management Servers

Source: https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign

## Article

An Active Intrusion Campaign Against Check Point Security Management Servers 

 New! AI Cyber Index: Benchmarking AI Models on Defensive Capabilities
 View the index

 Plans 
 Integrations 
 
 Resources

 Company

 Login 
 Search for free 
 Get a demo 

 Plans 
 Integrations 
 
 Resources

 Company

 Link Link 2 Link 3 

 Blog >
 Threat Insights 

 Follow us

 Threat Insights 

 99 IPs but a C2 ain’t one: An Active Intrusion Campaign Against Check Point Security Management Servers
 Steve Miller
 
 November 23, 2026

 GreyNoise tracks threat activity using our Global Observation Grid (GOG), a sensor network designed to attract adversarial scanning and exploitation attempts on our managed infrastructure. One might think of these sensors as conventional “honeypots,” but that doesn’t quite capture the variety, versatility, and scale at which we deploy and manage the complex fabric of the GOG. Unsolicited activity against our sensors is sketchy if not outright nefarious, and our approach allows us to capture end-to-end intrusions and analyze a broad swath of attacker infrastructure, tools, and tactics in near realtime, without waiting for lengthy incident response investigations. We fuse data from our sensor network with additional novel sources and methods to develop a comprehensive picture of adversaries.
 ‍
 Campaign Summary
 GreyNoise recently discovered an intrusion campaign targeting Check Point Security Management Servers, with confirmed attack activity between October 17th and November 2nd, 2026, impacting at least 22 distinct organizations globally.
 We are tracking this set of threat activity as GreyNoise Threat 13 (GT13) which represents adversary infrastructure, tools and post-exploitation action against the 22 victims.
 The campaign targeting does not appear to be focused on any specific geography or industry sector. The impacted orgs include victims with assets in the United Kingdom, Ireland, France, Netherlands, Greece, Germany, Austria, Bulgaria, Poland, India, Thailand, Vietnam, South Korea, Hong Kong, China, Australia, and the United States. The victim orgs sit in sectors including financial services, energy, government, transportation, mining, engineering, and manufacturing.
 We do not attribute GT13 to any known or publicly tracked threat group at this time. We do not currently have enough information to make assessments relating to the motivation of the actor or alignment to a nation-of-origin.
 The actor used 99 IP addresses, much of which were disposable network infrastructure to conduct scanning, exploitation, and control of its victims, including the use of a compromised server acting as an “operational relay box” (ORB) or more simply, a “hop,” for interacting with downstream victim assets. The actor used this relay box / hop to save command results and data stolen from 24 distinct Check Point Security Management Servers.
 The actor used Nmap , Chisel , Impacket , Paramiko and other Python tooling to perform intrusion activities against their victim assets, including attempts to perform internal reconnaissance, privilege escalation, and lateral movement.
 The threat actor used or attempted to exploit multiple CVEs, including, but not limited to: CVE-2026-61500 (Rejetto HFS), CVE-2025-5777 (Citrix NetScaler), CVE-2024-21893 (Ivanti), CVE-2026-41089 (Windows NetLogon), CVE-2026-16232 (Check Point SmartConsole auth bypass to Run Script), and CVE-2026-98432 (Linux IPv4 UAF).
 Though we observed hands-on-keyboard activity, we believe that like most modern attacks, the actor used LLMs and agentic systems to perform vulnerability scanning, exploitation, tool development, and automated interaction with compromised assets.
 Our visibility into this attack activity stopped around November 2nd, 2026, but given the actor’s persistent access to victim Check Point devices, we expect that this intrusion campaign is ongoing.
 We are working with international government partners and CERTs to share relevant intelligence and notify the victims.
 
 ‍
 Observed Attacker Activities
 We witnessed the GT13 actor use 99 IP addresses, all of which were either egresses through ExpressVPN or compromised victim Check Point devices, including activity over 1400+ network sessions, 800+ command line artifacts, and 1200+ files downloaded, uploaded, or created. We cannot cite all of the details here, but we can highlight observed GT13 adversary activities to illustrate their tradecraft and tactics, techniques, and procedures (TTPs).
 ‍
 HFS Scanning and Exploitation
 The GT13 threat actor used an automated scanning and exploitation pipeline to compromise an HFS server using CVE-2026-61500 .
 2026-10-02 13:17:45 UTC - The actor scanned and began exploitation against the HFS server. Each POST to the HFS loginSrp1 endpoint returns a new signed session cookie containing a “sid” value drawn from JavaScript’s Math.random() function. Through conducting several logins in succession, the actor collected enough output to reconstruct the internal state of the V8 PRNG algorithm, and thus recover an HFS session-cookie signing key, then forge a signed admin session cookie. This allows the attacker to login as admin without a password.
 Example POST to loginSrp1 and response 
 
 Decoded hfs_http blob from 200 OK response showing the sid that is harvested 
 
 ‍
 2026-10-02 13:19:37 UTC - Minutes later, we observed admin requests with forged session cookies, leading us to believe this exploitation was indeed CVE-2026-61500 for session forgery, which was not patched on this server. The actor now had control of the server.
 Example HTTP POST request with forged cookie 
 
 ‍
 Note that this forged cookie contains “allow_session_ip_change:true” which does exactly what it sounds like, letting the forged cookie work from any IP address. This is perfect for an adversary behind a VPN or operating from multiple exits.
 2026-10-05 12:21:30 UTC - A few days later, the actor used this same flow to gain access to install HFS middleware hooks that would issue commands to the compromised server. This allowed the attacker to append an SSH key to /root/.ssh/authorized_keys.
 
 On October 8th, we observed the actor’s automation check in to the compromised server using HFS command hook for “uname -a; df -h / | tail -1; whoami”. Then there was a lull in activity until October 19th.
 ‍
 Establishing the Operational Relay Box / Hop
 2026-10-19 14:53:48 UTC - We don’t know why (possibly a problem with the multi-agent architecture), but the actor did not use the SSH access right away. Instead, the actor’s automated pipeline reused the HFS exploitation route to forge new session cookies and leverage the HFS server_code feature to attempt to download and install additional malware on the server. At this point, we can see that the actor intended to use the compromised server as a relay or “hop” for further intrusion operations.
 Example of HFS command, which was preserved on the compromised server. 
 
 ‍
 Example decoded base64 blob demonstrating that the actor was intending to download an apparent “ZULT” Linux implant to the compromised machine. 
 
 The malware download failed, and the adversary attempted to troubleshoot the download by checking running processes, invoking curl to access the resource, and viewing the network configuration.
 Example of the actor following up, attempting to check on their implant 
 
 They couldn't figure out why their implant did not download, and the actor returned the next day with a direct SSH connection to continue setting up their relay.
 2026-10-20 07:22:08 UTC - The actor created a script (/root/exfil/srv_post2_<redacted>.py) which set up an unauthenticated HTTP server on the hop, after which the actor began to upload files. The first exfiltrated .tgz file contained results from scan of network routes from a compromised Check Point Security Management Server, demonstrating that the actor already had access to targeted victim assets.
 
 The actor continued to set up their environment, uploaded and installed open-source tools like Nmap and Chisel , and then set up a Chisel server as a reverse proxy.
 
 ‍
 Intrusion Operations and Exfiltration
 Once the actor had the compromised server set up as a relay, they began to use it to manage their interactions with their previously compromised victim Check Point devices. There’s a lot of commingled victimology here, so we’ll refer to two sets of victims. During our visibility, the actor was actively working towards deepening their intrusion against Victim A, and we later observed bulk actions on 21 other victim Check Point devices.
 Between October 20th and 26th, the adversary had one of their Victim A compromised assets download the Chisel program and run it in client mode allowing them to further scan and interact with the Victim A environment. Over the Chisel tunnel, and by using a script for CVE-2026-16232 (Check Point SmartConsole auth bypass to Run Script), the actor launched over 100 management tasks on multiple Check Point Management Servers. This included copying the firewall database and the Internal CA, minting a new certificate (pivot.p12), and unloading security policies (which would disable the firewall). Further, the actor probed Citrix Netscaler, Ivanti Connect Secure, VMware vCenter, Microsoft Exchange, Oracle TNS assets and several domain controllers.
 The bulk of the adversary commands and interaction is too voluminous to dig into here, but we can expose some of the adversary’s TTPs by taking a glimpse at their tooling. The actor used at least 30 Python scripts, many of which were helpers or launchers for other scripts, and several of them were probes for vulnerabilities or runners of exploits. Excerpts are provided below to illustrate the more specialized tooling and workflows.
 2026-10-20 13:54:30 UTC - First use of exploit.py against a Victim A Check Point server.
 Excerpt from exploit.py - This CVE-2026-16232 script is purportedly an adaptation of the Metasploit module for the same function. This appears to be how the actor was sending commands to the victim Check Point Security Management Servers. 
 
 2026-10-20 14:17:51 UTC - spray_portal.py used to scan another Check Point server in the Victim A environment.
 Excerpt from spray_portal.py - note that this contained common/default/weak passwords, and those apparently tailored for the victim. 
 
 2026-10-21 00:34:51 UTC - The actor could not get the second compromised Check Point device to report back to the hop, so they created and launched pull_<redacted_id>.py to steal the data from the second Check Point server and save it on the first compromised server, which could help exfiltrate the data back to the hop server.
 Excerpt from pull_<redacted_id>.py - The actor named this script after their targeted device. The script runs exploit_socks.py which runs exploit.py for CVE-2026-16232, enabling the actor to harvest data from the second compromised Check Point device through the first, to the hop box. Notice that this steals credentials, internal CA files, and firewall configuration. 
 
 ‍
 2026-10-21 02:56:38 to 06:34:40 UTC - The actor runs broad port scanning using curl, telnet, nmap scripts, a domain controller probe and other tools for internal reconnaissance.
 2026-10-21 06:39:24 to 11:28:04 UTC - The actor uses exploit scripts against multiple target servers in the Victim A environment.
 CVE-2020-1472 (Microsoft Netlogon),
 CVE-2023-4966 (Citrix Netscaler),
 CVE-2024-21893 (Ivanti Connect Secure),
 CVE-2021-26855 /34473 (Microsoft Exchange) and
 CVE-2021-21972 / CVE-2023-34048 (VMware vCenter)
 2026-10-21 11:41:21 UTC - The actor uses comb.py, ssh_comb.py and ssh_spray.py to scan a variety of targets in Victim A’s network. Note that these scripts contain usernames and passwords that were themed to the target victim. The actor either knew or was guessing names and passwords that the target might use.
 Excerpt from comb.py 
 
 Excerpt from ssh_comb.py 
 
 Excerpt from ssh_spray.py 
 
 2026-10-26 02:17:30 UTC - The actor issued a bulk certificate managing task to 24 compromised Check Point Security Manager servers including those belonging to Victim A and 21 other victim assets. The results of this task were shipped back to the hop server in a text file. We did not observe the actor sending this command task to these devices, indicating that it was issued from another part of the adversary’s infrastructure.
 Note that these text files contained the victim IP addresses and were in incrementing IP order, indicating an automation looped through them to run the commands on the compromised Check Point servers, and deliver them via scp to this exfil folder. Each file was delivered from victim infrastructure, showing that each of the compromised devices hold the SSH private key that matches the public key planted on the hop.
 
 All of these files contain error messages which indicate that the certificate task failed. Though we did not see follow-on attempts, the task information and IP addresses from these outputs were enough for us to identify and notify many of the victim organizations either directly or through government partners.
 Excerpt from sample /root/exfil/pc_XXX-XXX-XXX-XXX.txt 
 
 One of the error messages had a preload error for /usr/lib/.libproc.so registered in /etc/ld.so.preload, which may indicate an implant on the device.
 
 After the certificate minting failures, the actor’s activity dropped again until November 2nd.
 ‍
 Protecting Their Access
 2026-11-02 02:28:27 UTC - By early November, other threat actors had begun to scan and attempt to abuse the compromised server. We observed the GT13 actor use a script to perform a self-check for a Linux IPv4 use-after-free bug (CVE-2026-98432). After the check, the actor attempted to patch the system using Linux’s own command-line tool nftables to drop IPv4 packets with IP options that may trigger the bug. This allowed the actor to protect their hop from others engaging in future exploitation of the bug.
 Excerpt from cve_2026_98432.py 
 
 Example commands of the actor testing a CVE-2026-98432 script on the hop box, and then attempting to patch the vulnerability with nftables, the built-in Linux firewall and packet-filtering framework. You’ll notice the patching commands happened quickly. 
 
 ‍
 Notes on Attack Timeframe and Timeline
 The GT13 adversary had access to the victim Check Point Security Management Servers before they compromised the HFS server. We could not determine when or how the attacker gained access to those Check Point assets.
 We observed GT13 attack activity between 2026-10-02 13:17:45 and 2026-11-02 03:19:46 UTC. During our observation of the actor, we did not observe any adversary hands-on-keyboard activity between ~17:00 UTC and ~00:19 UTC, and nothing in the 05:00 UTC hour. We know the risks of time zone analysis and do not put much weight into the actor’s tendency to operate in what would be a convenient UTC+7- or UTC+8 workday.
 The attack infrastructure was long established before we first saw it, as we note the attempted malware domain newpayapp[.]com was first registered on 2026-03-13 12:46:28 UTC. It may be a UTC+7-friendly coincidence that the domain was originally created with the registrant state as “Hai Phong” with country code “VN” (see Cloudflare’s RDAP service ).
 We suspect the GT13 actor has a mature AI-enabled offensive apparatus. We believe the actor has separate agentic harnesses and systems weaponizing vulnerabilities, scanning for vulnerable assets, and automatically exploiting them to gather sets of systems that can be later used for operational relays or true targets. We suspect some of the foibles in the timeline reflect agentic offensive operations.
 ‍
 Indicators
 Value Type Context 
 newpayapp.com Domain GT13 controlled domain 
 data-zt.newpayapp.com Domain GT13 “ZULT” malware download domain 
 api-zt.newpayapp.com Domain GT13 subdomain 
 2ev5.newpayapp.com Domain GT13 subdomain 
 eeca2460550b9ded084ecf2f70a75356 HASSH OpenSSH 10 hash, this is common, but may be useful in combination with other GT13 TTPs, such as the use of ExpressVPN. 
 Mozilla/5.0 (X11; Linux x86_64) research User-Agent String GT13 used during HFS exploitation and commands. 
 Mozilla/5.0 research User-Agent String GT13 used once near HFS commands. 
 216.73.161.130 IP Address GT13 used 2026-10-02 12:40:26 UTC - 2026-10-02 12:40:27 UTC. AS206092, ExpressVPN (inferred from /24) 
 216.73.161.123 IP Address GT13 used 2026-10-02 12:51:11 UTC - 2026-10-02 12:51:12 UTC. AS206092, ExpressVPN (inferred from /24) 
 45.92.229.10 IP Address GT13 used 2026-10-02 13:17:45 UTC - 2026-10-02 13:18:09 UTC. AS206092, ExpressVPN (inferred from /24) 
 45.92.229.9 IP Address GT13 used 2026-10-02 13:19:37 UTC - 2026-10-03 08:16:45 UTC. AS206092, ExpressVPN (inferred from /24) 
 173.239.211.240 IP Address GT13 used 2026-10-02 15:04:40 UTC - 2026-10-03 08:13:54 UTC. AS206092, ExpressVPN 
 45.92.229.6 IP Address GT13 used 2026-10-03 03:20:56 UTC - 2026-10-03 08:27:16 UTC. AS206092, ExpressVPN 
 173.239.211.248 IP Address GT13 used 2026-10-03 03:20:57 UTC - 2026-10-03 08:29:40 UTC. AS206092, ExpressVPN 
 216.73.161.118 IP Address GT13 used 2026-10-03 03:29:37 UTC - 2026-10-03 03:29:39 UTC. AS206092, ExpressVPN 
 173.239.211.238 IP Address GT13 used 2026-10-03 03:29:41 UTC - 2026-10-03 08:20:49 UTC. AS206092, ExpressVPN (inferred from /24) 
 45.92.229.11 IP Address GT13 used 2026-10-03 06:05:26 UTC - 2026-10-03 06:05:27 UTC. AS206092, ExpressVPN (inferred from /24) 
 216.73.161.120 IP Address GT13 used 2026-10-03 06:05:28 UTC - 2026-10-03 06:49:33 UTC. AS206092, ExpressVPN 
 216.73.161.116 IP Address GT13 used 2026-10-03 06:27:39 UTC - 2026-10-03 06:27:39 UTC. AS206092, ExpressVPN (inferred from /24) 
 173.239.211.251 IP Address GT13 used 2026-10-03 06:27:40 UTC - 2026-10-03 06:28:02 UTC. AS206092, ExpressVPN 
 216.73.161.131 IP Address GT13 used 2026-10-03 06:42:18 UTC - 2026-10-03 06:49:42 UTC. AS206092, ExpressVPN 
 45.92.229.8 IP Address GT13 used 2026-10-03 06:43:20 UTC - 2026-10-03 06:43:21 UTC. AS206092, ExpressVPN 
 173.239.211.243 IP Address GT13 used 2026-10-03 06:43:22 UTC - 2026-10-03 06:43:47 UTC. AS206092, ExpressVPN 
 216.73.161.134 IP Address GT13 used 2026-10-03 06:53:36 UTC - 2026-10-03 08:20:49 UTC. AS206092, ExpressVPN 
 216.73.161.129 IP Address GT13 used 2026-10-03 07:15:28 UTC - 2026-10-03 07:15:29 UTC. AS206092, ExpressVPN 
 173.239.211.242 IP Address GT13 used 2026-10-03 07:15:30 UTC - 2026-10-03 08:13:16 UTC. AS206092, ExpressVPN 
 173.239.211.245 IP Address GT13 used 2026-10-03 07:32:05 UTC - 2026-10-03 08:13:54 UTC. AS206092, ExpressVPN 
 216.73.161.117 IP Address GT13 used 2026-10-03 07:32:06 UTC - 2026-10-03 07:32:16 UTC. AS206092, ExpressVPN 
 45.92.229.1 IP Address GT13 used 2026-10-03 07:32:16 UTC - 2026-10-03 08:28:54 UTC. AS206092, ExpressVPN 
 216.73.161.112 IP Address GT13 used 2026-10-03 08:15:59 UTC - 2026-10-03 08:29:36 UTC. AS206092, ExpressVPN (inferred from /24) 
 173.239.211.246 IP Address GT13 used 2026-10-03 08:15:59 UTC - 2026-10-03 08:16:44 UTC. AS206092, ExpressVPN 
 173.239.211.241 IP Address GT13 used 2026-10-03 08:20:34 UTC - 2026-10-03 08:20:35 UTC. AS206092, ExpressVPN 
 173.239.211.234 IP Address GT13 used 2026-10-03 08:27:16 UTC - 2026-10-03 08:27:17 UTC. AS206092, ExpressVPN 
 216.73.161.132 IP Address GT13 used 2026-10-03 08:28:54 UTC - 2026-10-03 08:28:59 UTC. AS206092, ExpressVPN 
 63.135.161.10 IP Address GT13 used 2026-10-05 09:35:00 UTC - 2026-10-05 09:36:54 UTC. AS206092, ExpressVPN (inferred from /24) 
 63.135.161.27 IP Address GT13 used 2026-10-05 09:36:48 UTC - 2026-10-05 12:29:48 UTC. AS206092, ExpressVPN 
 63.135.161.29 IP Address GT13 used 2026-10-05 12:21:30 UTC - 2026-10-05 12:21:30 UTC. AS206092, ExpressVPN 
 63.135.161.22 IP Address GT13 used 2026-10-05 12:21:30 UTC - 2026-10-05 12:21:36 UTC. AS206092, ExpressVPN (inferred from /24) 
 63.135.161.24 IP Address GT13 used 2026-10-05 12:21:36 UTC - 2026-10-05 12:21:36 UTC. AS206092, ExpressVPN 
 216.73.160.188 IP Address GT13 used 2026-10-06 00:11:36 UTC - 2026-10-06 00:23:38 UTC. AS206092, ExpressVPN 
 216.73.160.190 IP Address GT13 used 2026-10-06 00:11:36 UTC - 2026-10-06 00:12:05 UTC. AS206092, ExpressVPN 
 216.73.160.183 IP Address GT13 used 2026-10-06 00:12:05 UTC - 2026-10-06 00:12:05 UTC. AS206092, ExpressVPN 
 216.73.160.29 IP Address GT13 used 2026-10-06 00:23:38 UTC - 2026-10-06 00:24:13 UTC. AS206092, ExpressVPN 
 216.73.160.23 IP Address GT13 used 2026-10-06 00:24:13 UTC - 2026-10-06 00:24:13 UTC. AS206092, ExpressVPN 
 45.130.83.138 IP Address GT13 used 2026-10-08 06:25:48 UTC - 2026-10-08 06:26:44 UTC. AS206092, ExpressVPN (inferred from /24) 
 45.130.83.119 IP Address GT13 used 2026-10-08 06:39:59 UTC - 2026-10-08 06:40:03 UTC. AS206092, ExpressVPN 
 45.92.229.208 IP Address GT13 used 2026-10-08 06:40:04 UTC - 2026-10-08 06:40:04 UTC. AS206092, ExpressVPN (inferred from /24) 
 45.130.83.34 IP Address GT13 used 2026-10-17 13:15:22 UTC - 2026-10-17 13:15:22 UTC. AS206092, ExpressVPN 
 45.130.83.49 IP Address GT13 used 2026-10-17 13:21:38 UTC - 2026-10-19 15:12:40 UTC. AS206092, ExpressVPN 
 45.130.83.39 IP Address GT13 used 2026-10-17 13:29:51 UTC - 2026-10-17 13:29:51 UTC. AS206092, ExpressVPN 
 45.130.83.43 IP Address GT13 used 2026-10-17 13:29:51 UTC - 2026-10-19 15:13:33 UTC. AS206092, ExpressVPN 
 45.130.83.48 IP Address GT13 used 2026-10-17 13:29:52 UTC - 2026-10-19 15:12:20 UTC. AS206092, ExpressVPN 
 45.130.83.47 IP Address GT13 used 2026-10-17 13:34:26 UTC - 2026-10-19 15:10:14 UTC. AS206092, ExpressVPN 
 45.130.83.46 IP Address GT13 used 2026-10-19 14:53:47 UTC - 2026-10-19 14:53:48 UTC. AS206092, ExpressVPN 
 45.130.83.55 IP Address GT13 used 2026-10-19 14:53:59 UTC - 2026-10-19 15:12:02 UTC. AS206092, ExpressVPN 
 45.130.83.45 IP Address GT13 used 2026-10-19 15:09:14 UTC - 2026-10-19 15:09:14 UTC. AS206092, ExpressVPN 
 45.92.229.171 IP Address GT13 used 2026-10-19 15:09:14 UTC - 2026-10-19 15:09:17 UTC. AS206092, ExpressVPN 
 45.130.83.58 IP Address GT13 used 2026-10-19 15:09:17 UTC - 2026-10-19 15:13:14 UTC. AS206092, ExpressVPN 
 45.92.229.181 IP Address GT13 used 2026-10-19 15:09:42 UTC - 2026-10-19 15:14:02 UTC. AS206092, ExpressVPN 
 45.92.229.174 IP Address GT13 used 2026-10-19 15:09:42 UTC - 2026-10-19 15:09:54 UTC. AS206092, ExpressVPN 
 45.130.83.57 IP Address GT13 used 2026-10-19 15:09:54 UTC - 2026-10-19 15:09:54 UTC. AS206092, ExpressVPN 
 45.130.83.42 IP Address GT13 used 2026-10-19 15:10:14 UTC - 2026-10-19 15:10:18 UTC. AS206092, ExpressVPN (inferred from /24) 
 45.130.83.51 IP Address GT13 used 2026-10-19 15:10:18 UTC - 2026-10-19 23:50:44 UTC. AS206092, ExpressVPN 
 45.130.83.30 IP Address GT13 used 2026-10-19 15:10:58 UTC - 2026-10-19 15:10:58 UTC. AS206092, ExpressVPN 
 45.130.83.53 IP Address GT13 used 2026-10-19 15:12:14 UTC - 2026-10-19 15:13:14 UTC. AS206092, ExpressVPN 
 45.130.83.40 IP Address GT13 used 2026-10-19 15:12:20 UTC - 2026-10-19 15:12:21 UTC. AS206092, ExpressVPN 
 45.130.83.56 IP Address GT13 used 2026-10-19 15:14:02 UTC - 2026-10-19 15:14:02 UTC. AS206092, ExpressVPN 
 45.92.229.170 IP Address GT13 used 2026-10-19 15:14:22 UTC - 2026-10-19 15:14:23 UTC. AS206092, ExpressVPN 
 45.92.229.161 IP Address GT13 used 2026-10-19 15:14:23 UTC - 2026-10-19 15:14:55 UTC. AS206092, ExpressVPN 
 45.92.229.175 IP Address GT13 used 2026-10-19 15:14:55 UTC - 2026-10-19 15:14:55 UTC. AS206092, ExpressVPN 
 45.8.19.209 IP Address GT13 used 2026-10-20 07:13:41 UTC - 2026-10-20 08:32:38 UTC. AS206092, ExpressVPN 
 216.73.161.174 IP Address GT13 used 2026-10-20 08:41:01 UTC - 2026-10-20 15:22:20 UTC. AS206092, ExpressVPN 
 45.8.19.244 IP Address GT13 used 2026-10-21 00:20:19 UTC - 2026-10-21 07:17:37 UTC. AS206092, ExpressVPN 
 216.73.161.233 IP Address GT13 used 2026-10-21 07:18:08 UTC - 2026-10-22 07:49:42 UTC. AS206092, ExpressVPN 
 216.73.161.107 IP Address GT13 used 2026-10-22 08:57:38 UTC - 2026-10-26 13:35:51 UTC. AS206092, ExpressVPN 
 216.73.160.129 IP Address GT13 used 2026-11-02 02:23:06 UTC - 2026-11-02 03:23:27 UTC. AS206092, ExpressVPN 

 This article is a summary of the full, in-depth version on the GreyNoise Labs blog.
 Read the full report 
 
 Like or share:

 Get the latest blog articles delivered right to your inbox.
 Thank you! Your submission has been received!

 Oops! Something went wrong while submitting the form.

 Be part of the conversation in our Community Slack group.
 Join us on Slack

 Follow us and don’t miss a thing.

 Related content
 View all related articles

 Threat Insights

 99 IPs but a C2 ain’t one: An Active Intrusion Campaign Against Check Point Security Management Servers
 Steve Miller
 
 Nov 23, 2026

 Threat Insights

 Global Event: Java4Shell (CVE-2026-114938) Live Activity Report
 GreyNoise
 
 Nov 18, 2026

 Threat Insights

 Global Event: N-able N-central Live Activity Report
 GreyNoise
 
 Nov 13, 2026

 Threat Insights 

 Products
 GreyNoise Platform 
 GreyNoise Block 
 For Government 
 For Enterprise 
 Plans 
 Integrations 
 
 Partners
 GreyNoise Partnerships 
 Reseller Partners 
 MSSPs 
 Technical Alliances 
 OEM Partners 
 
 Resources
 Blog 
 Resources Library 
 Tag Request 
 Documentation 
 
 Company
 About 
 Press Room 
 In the News 
 Upcoming Events 
 Community 
 Careers 
 GreyNoise Love 

 ©
 2026
 GreyNoise, Inc. All rights reserved.

 Terms 
 Privacy 
 Security 
 Cookies 
 Patents 
 Principles 

 Cookie Settings
 We use cookies to ensure you get the best experience on our website. Learn more 
 Got it

## HN discussion highlights (item 50630594)

# HN checkpoint-intrusion — Active intrusion campaign against Check Point security management servers (289 pts, item 50630594)
# url: https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign

[mentalgear] Buckle up, this is just the beginning of the end. ATM only more sophisticated cyber criminals or state actors use LLMs to penetrate, but soon the chaotic landscape of 100.000s of cyber criminals will just use compute to prompt models to "Make me as much money as possible" , with the result of these models/swarms attacking any online service including critical infrastructure.
[nater5000]     The end of the brief and narrow era that the OP is familiar with that they assume is the most important thing to ever exist because it's all they know.
[morkalork]     If I had to guess, free and open internet where networks route traffic for all. Can already see it coming with all the ID verification laws to access porn sites. Google requiring accounts and government ID to create side-loaded apps. Banking and other services wanting full chain of trust down through OS to hardware on phones. The future internet is going to look like the French Minitel of the past. Bad actors won't even be allowed to send a packet without impersonating a corporate entity first. /doomerism
[persedes]   just came back from the honda dealer, they could not install a software update because honda got "cyberhacked" and they corrupted the update file, which caused the steering unit? to brick. The unit has been backordered now as a result and they've suspended all software updates until they know what's going on. If that is true (and the whole in person software update thing aside), these orgs will experience a lot of pain for years of neglect with their software practices...
[sigmoid10]     2 days ago I overheard cashiers at my local grocery chain talk about how they had to dump all the food from the fridges because they suddenly started heating in several stores. This was not reported anywhere yet, but after the exact same thing happened in France I'm 100% sure this was another cyberattack. Most companies probably have a really high incentive to never report this at all, because it would frighten away their customers. There are probably countless cases like this at smaller banks or financial providers that we'll never hear about because they will be swept under the rug for sure.
[fedupnow]   Thats not how it works, but sure. I don't think its healthy to assume this and just insitgate unecessary anxiety just because you think some lawless sci-fi future exists. Also, people dont refrain from committing crime because they're incapable, and they certainly don't need llms. People don't commit crime because most people are good people, and the ones who aren't or are questionable face almost certain consequences at some point. The same social frameworks that exist now to prevent crime will exist then as well.
[recursive]     The people that refrain from doing crime probably do it because they're good. And I even think that it's the overwhelming majority of people. But a small percentage of a large population is a large absolute number. And they really have been incapable so far of doing these types of crimes. Ripping off retail and convenience stores will probably continue the same as it has.
[ygjb]     Most people. Just by way of example, there was a study in 2006 from Kessler and Associates that said 13% of folks will just straight up steal from their employer, and another 66% will steal if they see others getting away from it. Some crime comes from sociapathy, some comes from mental illness, most petty crime comes from desperation, but there are social indicators that 'accepted crime' endorses the behaviour and causes proliferation and escalation. Assuming that people are good in general is just as unhealthy and risky as assuming everyone is bad in general. This goes in multiple directions
[pwython]     > Thats not how it works Yet. It has only been a few months since "swarms" of agents have shown their capabilities. <100B open models being just as good as Fable/Astra in a year is perfectly plausible. And by then, inference software will be much easier than even LM Studio.
[goodmythical]     But there are already more than hundreds of thousands working in fraud/scams/hacking. In the US, the FBI's recieved more reports YoY every year since '18 except for a dip in '22 only for '23 to again return to beating '21. Complaints of cyber crimes have nearly trippled in the US (from ~350k to >1m reports) in that time frame, with the 24/25 jump being the largest in terms of reported financial losses. The UN estimates that more than 300k people are "trapped in scam compounds" (being forced to or having no better option than to engage in fraud) across SEA alone, and similar compound infrastruc
[batch12]     As easy as it is now, and based on the attacks I've seen firsthand, I disagree partly. I don't think it will take 100ks of attackers to cause chaos- there's already a large number of 'lawless' people that haven't pivoted to llm assisted attacks yet. The new frameworks have made this easy and it will be worse before it gets better. There's too much technical debt.
[prescriptivist]     > insitgate unecessary anxiety If you work at an org with a dedicated security team that has access to the frontier labs security tools then you know anxiety levels are at their asymptotic ceiling already.
[yubblegum]     > Also, people dont refrain from committing crime because they're incapable, and they certainly don't need llms. People don't commit crime because most people are good people, and the ones who aren't or are questionable face almost certain consequences at some point. Counterpoint: consider interpersonal communications. People verbally act out in virtual environments. They chimp out. The most vulgar, unkind, caustic, and damaging interactions I've ever been exposed to have been online. Never have encountered people speaking like that in person. Counterpoint: consider dick pics. Normally, men do
[asdfman123]     > Also, people dont refrain from committing crime because they're incapable They often refrain because it's not profitable given the risk profile. And the large majority of criminals aren't actually smart enough for sophisticated cybercrime. > and they certainly don't need llms. LLMs make it profitable given the risk profile, and don't require as much intelligence to operate. > People don't commit crime because most people are good people I actually agree that most people are good people, but if you give LLM swarms to the 5% of the world comprised of shameless scammers that's a big problem. > 
[nomel]     > People don't commit crime because most people are good people This concern has nothing to do with the larger population of people that don't commit crimes.
[icantevenhold]     What consequences have hackers from North Korea or Russia ever faced? The social framework only works within a social group you belong to
