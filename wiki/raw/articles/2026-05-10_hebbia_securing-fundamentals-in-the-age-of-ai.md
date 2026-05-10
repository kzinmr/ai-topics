---
title: "Securing Fundamentals in the Age of AI"
source: "Hebbia Blog"
url: "https://www.hebbia.com/blog/securing-fundamentals-in-the-age-of-ai"
scraped: "2026-05-10T01:27:02.832200+00:00"
lastmod: "2026-05-08"
type: "sitemap"
---

# Securing Fundamentals in the Age of AI

**Source**: [https://www.hebbia.com/blog/securing-fundamentals-in-the-age-of-ai](https://www.hebbia.com/blog/securing-fundamentals-in-the-age-of-ai)

Product
By Matt Aromatorio
04.22.26
Securing Fundamentals in the Age of AI
Most AI security discourse fixates on model-level threats. Platform-level threats are a different problem entirely.
If you follow AI security discourse, you'd be forgiven for thinking the existential threat to financial institutions is a language model hallucinating data or an agent escalating privileges. These risks are real, and Hebbia has an Applied Research team dedicated to solving them. But AI-specific attacks, prompt injection, model jailbreaks, hallucinated outputs, tend to be locally scoped: one user's session, one workflow, one output.
Infrastructure and platform attacks are a different beast. Broken authentication, compromised credentials, supply chain backdoors grant lateral movement, adversary persistence, and the ability to compromise an entire system simultaneously. Generally speaking,
prompt engineering breaks a session, but poor auth breaks a platform.
Two forces are making platform-level threats more dire. The dependency ecosystem that financial institutions rely on is growing, not shrinking. Every new appliance and piece of software is another node an attacker can traverse. At the same time, AI is compressing development cycles faster than legacy security processes can adapt, creating an elastic surge in demand that many organizations aren't prepared to meet. Anthropic's recent decision to limit the Mythos model to defenders is a prime example of this gap.
At Hebbia, this empirical view shapes every security decision we make. We ask what threats are proven and whether we're structurally exposed to them. Then we apply a single principle across every layer of the stack: maximize friction on the paths most likely to cause harm, and minimize it everywhere else.
Architecture: Why SaaS, Not On-Prem
The instinct for many security teams is to pull AI inside their perimeter: deploy on-prem, control the network, own the hardware. That instinct is understandable. But studying how supply chain attacks actually work reveals a more nuanced problem space.
In the 2013 Target breach, attackers compromised a "low risk" HVAC vendor's credentials and moved laterally through Target's internal network to reach payment processing systems. The vendor never needed deep network access, but the architecture granted it anyway. Seven years later, the SolarWinds compromise saw attackers insert a backdoor into a legitimate software update. Nearly every organization running Orion on their own servers, behind their own firewalls, executed the exploit with privileged access to their most sensitive systems. The on-prem model didn't slow down or prevent the attack. It
was
the attack surface.
On-prem means running vendor-supplied code of unknown provenance, and allowing third-party access to support it, inside your sensitive environment. If the vendor is compromised, you are compromised. The SaaS model inverts this. Rather than running inside a customer's environment, Hebbia runs on our own infrastructure. Our customers don't execute our code inside their environments or on their endpoints. Our engineers don't hold credentials to customer systems. The connection between user and application is a well-defined API boundary, not a shared network segment.
That model comes with tradeoffs. Customers have limited visibility into vendor-side logging telemetry and limited independent means to investigate or respond to suspicious activity. Hebbia reduces this exposure where possible. Enterprise customers can use Bring Your Own Key (BYOK) capabilities to protect their data within our infrastructure, and detailed audit logs give customers meaningful oversight of activity in their environment. Because customers must place trust in the SaaS provider, we strive to earn it through the technology, people, and process controls we put in place.
For organizations that weigh integrity and availability alongside confidentiality, the SaaS model limits blast radius in ways on-prem cannot easily match. This is particularly true for systems that, by their nature, require access to sensitive data.
Operations: Keeping the Foundation Safe
The same logic applies to how we secure our own internal operations. As development velocity and threat sophistication increase, Hebbia treats bug bounty programs, top-tier penetration testing, and advanced identity management as table stakes, not differentiators. That means:
Zero standing access.
Hebbia engineers don't have credentials to production environments. We use Just-in-Time (JIT) access grants: time-bound, scoped credentials issued through an audited workflow and automatically revoked when the window expires. A compromised engineer laptop, one of the most common initial access vectors, does not yield access to production.
Supply chain integrity.
Anthropic's Project Glasswing recently demonstrated that frontier AI models can autonomously discover thousands of high-impact vulnerabilities across major operating systems, browsers, and open-source libraries. That capability won't stay exclusive to defenders forever. Hebbia secures its software supply chain aligned with the SLSA framework, ensuring the code we ship is the code we wrote and the dependencies we include are the ones we intended. Our goal is to be fast to ship a fix, hard to ship a vulnerability.
Device trust.
JIT access solves the credential problem, but credentials are only half the equation. The device presenting them matters too. Hebbia's access model layers device-level checks alongside credential verification, ensuring that valid credentials from a non-compliant endpoint are insufficient to reach sensitive systems or data. When a device falls out of compliance, remediation is self-service, the user gets a clear explanation of what's wrong and how to fix it, not a locked-out screen and a ticket to IT.
Data: How Hebbia Handles AI Data Retention
The same principled approach applies to one of enterprise AI's most important security controls: data retention. For the majority of interactions, Zero Data Retention (ZDR) is the right default. No customer data persists beyond the request lifecycle. No customer data is used to train models.
Some of the most valuable AI capabilities require data to be persisted. A model executing a DCF calculation needs to store intermediate results for seconds while the analysis is built. Under strict binary ZDR, these features are impossible, and their absence puts a ceiling on what AI can deliver for customers.
Rather than treat them as mutually exclusive, Hebbia implements purpose-bound retention for features that require nonzero retention:
ZDR by default.
Retention is zero unless a specific feature explicitly requires state to function.
Task-scoped.
Retained data is bound to a single operation.
Time-bounded.
Data is purged automatically when the operation completes, typically within seconds.
Policy-governed.
Retention rules are enforced programmatically, not by convention, with redundant checks to ensure adherence.
The Same Evolution, Underway in AI
The pattern should look familiar. A decade ago, major financial institutions refused to put PII or MNPI in the cloud at all: private data centers, total network isolation, no exceptions. What unlocked cloud adoption wasn't a change in the underlying risk. It was the maturation of controls: encryption, VPCs, granular IAM, customer-managed keys. Once the risk was manageable, the utility was too significant to ignore. Today, you'd be hard-pressed to find a bank that isn't running critical workloads in one or more major cloud providers.
The same evolution is underway in AI. The institutions that will get the most out of it are the ones that evolve from "prove you don't keep a byte of our data" to "show us the controls that govern how you handle it." Potential is unlocked not by ignoring risk, nor by avoiding it entirely, but by applying friction precisely where it matters.
