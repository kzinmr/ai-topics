---
title: "OpenAI Finds 948 Local Privilege Escalation Bugs in the Linux Kernel (Phoronix)"
type: article
created: 2026-11-08
updated: 2026-11-08
source: https://www.phoronix.com/news/OpenAI-948-Linux-LPE-Bugs
published: 2026-11-06
tags: [openai, security, vulnerability-discovery, linux]
sha256: 639a67b935c1be5241d023d783166ff938a79fe0c478dd0d497225125a0cbf42
---

OpenAI Finds 948 Local Privilege Escalation Bugs In The Linux Kernel - Phoronix 

 Articles & Reviews 
 News Archive 
 Forums 
 Premium Ad-Free Contact 
 Popular Categories 
 Close 

 Articles & Reviews 

 News Archive 

 Forums 

 Premium 

 Contact 

 Categories 

 Computers Display Drivers Graphics Cards Linux Gaming Memory Motherboards Processors Software Storage Operating Systems Peripherals 

 OpenAI Finds 948 Local Privilege Escalation Bugs In The Linux Kernel 
 Written by Michael Larabel in AI on 5 November 2026 at 05:00 AM EST. 43 Comments 

OpenAI published a blog post outlining their work on autonomous vulnerability discovery. To showcase their AI potential, they found 948 valid local privilege escalation vulnerabilities within the Linux kernel.

 OpenAI's prototype found 2,308 candidate vulnerabilities in the Linux kernel, dynamically reproduced 1,724 vulnerabilities, and ultimately found 948 local privilege escalation exploits for allowing unprivileged local users to gain root access. They also generated candidate patches for maintainer review.

 Discovering nearly one thousand local privilege escalation vulnerabilities consumed $1.2 million USD in API credits.

 OpenAI researchers noted in their blog post:
 "Within the next few years, we believe that if there are vulnerabilities in a given software project, frontier models will likely be able to discover them and even less capable models may be able to develop exploits once disclosed. In a world of no unknown vulnerabilities, it will be critical to build and maintain high assurance software, especially core software such as operating systems, browsers, image parsing libraries, the TCP/IP stack, and more. Investing in training models to write secure code by default, minimizing attack surface by removing unnecessary features, and formal verification are promising areas of future research to effectively scale software security, in addition to finding and fixing existing vulnerabilities." 
 Another interesting takeaway is that their GPT-5.5 Cyber model is finding more than 5x more novel LPEs than their GPT-5.6 Sol model despite three months of hardening/patches in the Linux kernel between scans.

 Those wanting to go through this OpenAI showcase in more detail can do so via their blog post . 

 43 Comments 

 Tweet 

 Related News 
 PostgreSQL 19 Running Behind Schedule Due To AI/LLM Burden Modular's MAX Source Code Now Fully Opened, Under New MAX License Google's Sashiko AI Has Completed 191k Patch Reviews, Cited On Nearly 500 Kernel CVEs AI Makes "Open-Source, Clean Room" Implementations Of Adobe Photoshop & Premier In Rust Lemonade Fixes AMD APU Model Streaming, Drops OpenMOSS ROCm As ~40x Slower Than Vulkan NVIDIA-Started Open Secure AI Alliance Moves To The Linux Foundation 

 About The Author 
 Michael Larabel is the principal author of Phoronix.com and founded the site in 2004 with a focus on enriching the Linux hardware experience. Michael has written more than 20,000 articles covering the state of Linux hardware support, Linux performance, graphics drivers, and other topics. Michael is also the lead developer of the Phoronix Test Suite, Phoromatic, and OpenBenchmarking.org automated benchmarking software. He can be followed via Twitter , LinkedIn , or contacted via MichaelLarabel.com . 

 Popular News This Week 
 Synaptics Appears To Use Legal Threats To Block Open-Source DisplayLink Driver The Linux 7.4 Merge Window Is Easily The Largest In Kernel History OpenAI Finds 948 Local Privilege Escalation Bugs In The Linux Kernel Enlightenment 0.28 Released With Many Improvements Debian's APT Affected By Man-In-The-Middle Attack For Arbitrary Code Execution As Root The Linux Kernel Preparing To Remove The Last Of Its MMX Optimized Code New Linux 7.4 Feature For Reducing AI Noise Already Reverted Due To A "Crazy Beast" Fedora 45 Released With Many Leading-Edge Linux Innovations 

 Latest Linux News 
 AMD PerfOpt Performance Boosting Code Tweaked For Linux 7.4-rc2 

 Yunsilicon Working To Upstream Their High Performance Linux Network Driver 

 GCC 17 Feature Development Ends Next Week 

 Linux Fixes Faulty Mitigation Selection For BHI Vulnerability 

 OpenIndiana 2026.10 Released With Updated Tools & Compilers, New Apps 

 Automake 1.20 Brings New Features, Desires To Re-Establish GNU As Leading Build System 

 HyprBSD Provides Wayland-Based Desktop Built Atop FreeBSD, Complete With Steam Gaming 

 Kmorph Aims To Provide Rebootless Linux Kernel Crash Recovery 

 KDE Plasma 6.9 Will Stop Leaking Memory When Right Clicking Files/Folders On Desktop 

 Vulkan 1.4.368 Released With New Extensions From Valve & NVIDIA 

 Microsoft's Azure Linux 3.0.2022 Ships With More Than 470 Security Fixes 

 Asahi Linux Makes Progress On Gaming, More Apple Silicon Upstreaming 

 FreeBSD 15.2 Beta 1 Allows Experimental Cross-Building Of Base Packages On Linux/macOS 

 Show Your Support, Go Premium 
 Phoronix Premium allows ad-free access to the site, multi-page articles on a single page, and other features while supporting this site's continued operations. 

 Latest Featured Articles 
 Arch Linux vs. CachyOS vs. Omarchy 4.5 Performance Benchmarks 

 Linux 7.4 Showing Few Performance Gains With Initial Benchmarks On AMD Ryzen Threadripper 

 Linux 7.4 Features Steam Frame VR Headset, More AMD Zen 6 Enablement & Initial Apple M4 / A18 Pro Bring-Up 

 NVIDIA Vera Single vs. Dual Socket CPU Performance 

 CachyOS vs. Fedora 45 vs. Ubuntu 26.10 Performance On AMD Ryzen 9 

 Support Phoronix 
 The mission at Phoronix since 2004 has centered around enriching the Linux hardware experience. In addition to supporting our site through advertisements, you can help by subscribing to Phoronix Premium . You can also contribute to Phoronix through tips/donations via PayPal or Stripe . 

 Phoronix Media 

 Contact 
 Michael Larabel 

 Phoronix Premium 

 Support Phoronix 
 While Having Ad-Free Browsing, 
 Single-Page Article Viewing 

 Share 

 Facebook 
 Twitter / X 

 Legal Disclaimer, Privacy Policy, Cookies | Privacy Manager | Contact 
 Copyright © 2004 - 2026 by Phoronix Media . 
 All trademarks used are properties of their respective owners. All rights reserved.

## HN discussion highlights (item 50391804, 34pts)

[burner_] Source blog post: https://openai.com/index/a-thousand-fewer-paths-to-root/ > In a run in mid-October 2026, our pipeline using an upcoming cyber model dynamically reproduced 1,724 vulnerabilities and generated PoCs for 291 information leak vulnerabilities and 948 working local privilege escalation (LPE) exploits for a commonly used Linux distribution. The total run cost $1,213,430 in API credits, or $1,279 per LPE exploit.

[leoedin] I maintain a Linux build for an IoT product, and it's been a brutal few months trying to keep up with kernel patches. We're trying to go through certification right now, and one of the questions is effectively "are there any known vulnerabilities, and if so justify why they don't matter". Every time I manage to answer the question, a new set of CVEs comes out and we have to update everything before we can answer it again. I imagine the people who are committed to keeping LTS versions of the kern

[ActionHank] Impressive if these pan out to be actual issues. Last time this sort of claim was made with mythos most of the issues were nothing burgers. Not saying LLMs aren't pushing hard in security research right now, just that the tangibles seems to come largely from a knowledgeable person pushing an agent towards the find and not some autonomous process.

[eqvinox] Speaking as someone responding to security@ for a notable FOSS project (C code base dating back to 1996), a meta-comment: Our current quota is, ca. 20% of AI-found "critical" issues are in fact critical. 3-5% of reported "high" are also critical (i.e. unfortunately it's not possible to rely on AI being excessively alarmist, it does under-classify some issues.) This is with erring towards higher severity though; we didn't get anything that'd e.g. make HN front page. Simultaneously, ca. 35% of rep

[pixl97] >Our current quota is, ca. 20% of AI-found "critical" issues are in fact critical. What percentage of ALL returned AI security bugs are critical?

[j45] If the volume of bugs being found continues, maybe the rate of bugs will slow, but increase on the release of a sufficiently capable new model. The vibe coded nature of letting LLMs write patches without understanding the impacts, could invite bandaids on top of bandaids.

[spwa4] One thing I don't understand about security issues. If you look at the physics the rowhammer "bug" is not a cpu flaw, and not really a memory flaw either. This was known when capacitor based memory was invented, and was put forward as a disadvantage in the very first designs. It's physics. If you do any kind of DDR ram (including, I think, HBM), there is no way to avoid rowhammer-style bit flips. And fixed systems ... aren't fixed. Not even fixed systems currently being built. Capacitor based me

[bcrl] Rowhammer is most certainly a hardware flaw. DRAM manufacturers have pushed cells too close together to meet the specifications claimed on their datasheets. Increasing cell sizes would be the correct hardware fix for the issue. Engineering is accepting the reality of physics to build things that are useful. Unfortunately, we live in a world where the few percentage points on the production cost of DRAM needed to completely mitigate rowhammer is sufficient to ensure that defective DRAM continues 

[GuB-42] Security works by layers. The physics makes the rowhammer impossible to fix in practice, but you can add various mitigations: scrambling, ECC, detection and response, etc... On the application level, you can also make it so that it is not possible to do a rowhammer in the first place. Fix everything that can be fixed and mitigate what can't be fixed. And there is another security issue that can't be fixed, and is much worse than rowhammer: people. But we can't remove people, just like we can't r

[Veserv] Because software defects are more common, easier to exploit, faster to exploit, cheaper to find, and massively more consistent to leverage. If software improved to the degree that hardware and physics-level exploits were the easier, we would be in a world 100x more secure than what we have now. The real question you should be asking is why is it not “game over” right now given that most people would only hope in their wildest dreams that they would be so lucky that worrying about Rowhammer and t
