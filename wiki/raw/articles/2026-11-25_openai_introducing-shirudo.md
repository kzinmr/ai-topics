---
title: "OpenAI and Cisco Introduce Shirudo"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://openai.com/index/introducing-shirudo/"
status: complete
sources:
  - "https://openai.com/index/introducing-shirudo/"
  - "https://news.ycombinator.com/item?id=50619630"
sha256: 5144ddf1f1c0069f72ab4af4faa099921658e92c8a4314424175d613396bfe27
---

# OpenAI and Cisco Introduce Shirudo

Source: https://openai.com/index/introducing-shirudo/

## Article

OpenAI and Cisco introduce Shirudo | OpenAI 

 OpenAI November 23, 2026
 Security 
 OpenAI and Cisco introduce Shirudo

 An open-source runtime that helps operators protect running Linux systems without needing to wait for the patch or restarts

 Share 

 OpenAI and Cisco are launching Shirudo, an open-source runtime that helps teams protect Linux systems while they roll out patches. In a controlled test ⁠ (opens in a new window) , a Codex-generated shield blocked a Java4Shell exploit attempt against a running Elasticsearch service without requiring a restart. 

 We’re inviting developers, security researchers, and infrastructure operators across the industry to help develop the project further. The project brings together OpenAI’s frontier AI, security and infrastructure research and Cisco’s infrastructure and security expertise to help protect the systems people rely on every day. 

 Testing and deploying a patch can still take days or weeks. Protecting a service in the meantime can be challenging because an exploit and a legitimate request may rely on the same Linux operation. Blocking that operation entirely could take the service offline. 

 Shirudo (Japanese for “shield”) is designed to help security teams navigate this tradeoff. Teams can test whether a temporary safeguard, called a shield, blocks the behavior that exposes a vulnerability while allowing legitimate requests through. Once an operator approves the shield, it can be deployed while the service continues running. 

 “ We’re giving defenders better models and tools to find and fix vulnerabilities faster, but finding a bug today doesn’t mean you can patch every system tomorrow. We are partnering closely with Cisco on Shirudo to help teams protect the systems they need to keep running while they build and roll out a fix. So many teams rely on the same software that it makes sense to build these tools in the open. Now when one team finds a better way to protect a system, others don’t have to start from scratch. ”
 Greg Brockman, President and Co-founder of OpenAI 

 How Shirudo works 

 Shirudo uses eBPF, a Linux technology that allows small programs to run at specific points inside the operating system. This makes it possible to observe suspicious activity and apply targeted security protections to running systems. 

 How the guardian agent observes and protects a running system with eBPF. 

 OpenAI and Cisco are designing Shirudo around four core capabilities: 

 Live protection: eBPF shields can block vulnerable code paths without restarting the system. Security teams can monitor how a proposed shield would affect applications before enforcing it. 

 Defense at machine speed: OpenAI and Cisco are designing Shirudo to give agents programmable controls to investigate vulnerabilities, develop targeted shields, and validate their effectiveness against exploits and real workloads. Security teams control what gets deployed. 

 Trusted deployment: Shields are cryptographically signed and verified before loading. Linux's eBPF verifier checks eBPF programs against its safety rules, while kernel security controls restrict unauthorized changes. 

 Hardware-backed verification: Shirudo uses a Trusted Platform Module (TPM) to support a verifiable record of protections being loaded or removed. Operators can use this evidence to check whether systems meet their security requirements. 

 The Shirudo technical walkthrough ⁠ (opens in a new window) from the Linux Plumbers Conference shows how to apply a shield and verify it on the target host ⁠ (opens in a new window) . The Java4Shell vulnerability is another example illustrating how a targeted shield can protect a running application while a permanent patch is being prepared. Using OpenAI's Codex, the team generated a shield that added an input check to Java's Base64 decoder and attached it directly to a running Elasticsearch process. When attempting to exploit the vulnerability, the shield rejected the malicious input, blocking the attack while Elasticsearch continued running. You can read more here ⁠ (opens in a new window) . 

 Rethinking infrastructure 

 Shirudo is a first step toward infrastructure that can adapt to emerging threats while remaining reliable. We want to strengthen the operating system foundations needed to deploy these protections at scale, including hardening the kernel and core services, limiting workload permissions, and making updates and recovery safer. 

 Our long-term goal is to enable defenders and AI agents to quickly identify affected systems, validate protections, and deploy eBPF shields that block exploits without disrupting workloads. Applications should run with only the permissions they need, governed by policies that are automatically generated and maintained. 

 We will combine frontier AI with security and infrastructure research to discover vulnerabilities and test defenses against realistic attacks. We aim to make it easier for operators to detect and contain compromises, prevent attackers from moving across systems, and restore services to a verified, known-good state. Hardware-backed attestation and independent network controls provide additional assurance even if individual systems are compromised. 

 Building in the open 

 OpenAI and Cisco are open-sourcing Shirudo ⁠ (opens in a new window) so developers, security researchers, and infrastructure operators can inspect the code, test protections, and contribute to its development. Shirudo is licensed under BSD 2-Clause, with its BPF programs dual-licensed under BSD and GPL. 

 Our goal is to make tested shields available alongside vulnerability disclosures, giving operators a way to evaluate and deploy temporary protections while preparing permanent patches. 

 Try Shirudo: Follow the VM quickstart ⁠ (opens in a new window) to sign, load, and verify a test protection. 

 Get hands-on: Explore Shirudo through Isovalent's self-guided lab ⁠ (opens in a new window) . 

 Join the technical deep dive: Register for the December 15 webinar ⁠ (opens in a new window) . 

 We’re building Shirudo in the open with the people who build, run, and secure Linux systems. We welcome contributions to the runtime, new shields, and improvements to Linux and eBPF. If you'd like to get involved, take a look at the code on GitHub ⁠ (opens in a new window) , read the docs ⁠ (opens in a new window) , and let us know what you find ⁠ (opens in a new window) . 

 Partnerships 
 2026 
 
 Author
 OpenAI

 Keep reading

 View all 

 Partnering with Hacktron to strengthen OpenAI’s security
 Security Nov 6, 2026 

 GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents
 Product Nov 5, 2026 

 Daybreak Red is now available in AWS GovCloud (US-East)
 Product Nov 4, 2026
