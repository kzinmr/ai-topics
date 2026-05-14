---
title: "Our response to the TanStack npm supply chain attack"
url: "https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack"
fetched_at: 2026-05-14T07:00:38.189355+00:00
source: "OpenAI News"
tags: [blog, raw]
---

# Our response to the TanStack npm supply chain attack

Source: https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack

We recently identified a security issue involving a common open-source library, TanStack npm, that is part of a broader attack known as
Mini Shai-Hulud
⁠
(opens in a new window)
. We found no evidence that OpenAI user data was accessed, that our production systems or intellectual property were compromised, or that our software was altered.
We have taken decisive steps to protect our user data, systems, and intellectual property. As part of our response, we are taking steps to protect the process that certifies our macOS applications are legitimate OpenAI apps.
Update your macOS applications by June 12, 2026
We are updating our security certificates, which will require all macOS users to update their OpenAI apps to the latest versions. This helps prevent any risk, however unlikely, of someone attempting to distribute a fake app that appears to be from OpenAI. You can update safely through an in-app update or at the official links below:
The security and privacy of your information are a top priority. We’re committed to being transparent and taking quick action when issues arise. We’re sharing more technical details and FAQs below.
What happened and what we are doing
Two employee devices in our corporate environment were impacted by this attack. Upon identification of the malicious activity, we worked quickly to investigate, contain, and take steps to protect our systems. As part of our investigation and response, we engaged a third-party digital forensics and incident response firm.
We observed activity consistent with the malware’s publicly described behavior, including unauthorized access and credential-focused exfiltration activity, in a limited subset of internal source code repositories to which the two impacted employees had access. We confirmed that only limited credential material was successfully exfiltrated from these code repositories and that no other information or code was impacted.
We acted immediately to contain the activity. We isolated impacted systems and identities, revoked user sessions, rotated all credentials across impacted repositories, temporarily restricted code-deployment workflows, and thoroughly scrutinized user and credential behavior. As part of our investigation, we have not observed evidence of impact to customer data, or our intellectual property, and our analysis has not identified misuse of impacted credentials or follow-on access by the threat actor.
The impacted source code repositories included signing certificates for our products, including iOS, macOS, and Windows. As a result, we are rotating code-signing certificates as a precaution, which will require macOS users to update their applications. Users do not need to take any action for Windows and iOS apps. Additional guidance will be provided to macOS users regarding these required updates.
In addition to rotating certificates, we are coordinating with platform providers to prevent any unauthorized use of these certificates by stopping new notarizations. We have also reviewed all notarization of software using our previous certificates to confirm no unexpected software signing has occurred with these keys, and validated that our published software did not have unauthorized modifications. We have found no evidence of compromise or risk to existing software installations.
Once we fully revoke our certificate on June 12, 2026, new downloads and launches of apps signed with the previous certificate will be blocked by macOS security protections.
After the
Axios incident
, we accelerated the deployment of specific security controls and technologies to reduce the impact of supply chain attacks such as this one. Our security response included further hardening of sensitive credential materials used in our CI/CD pipeline, deployment of package manager configurations with controls like minimumReleaseAge, and additional security software to validate the provenance of new packages.
This incident occurred during our phased deployment and rollout of these controls, and the two impacted employee devices did not have the updated configurations that would have prevented the download of the newly observed package containing malware.
This incident reflects a broader shift in the threat landscape: attackers are increasingly targeting shared software dependencies and development tooling rather than any single company. Modern software is built on a deeply interconnected ecosystem of open-source libraries, package managers, and continuous integration and continuous deployment infrastructure, which means that a vulnerability introduced upstream can propagate widely and quickly across organizations. We are continuing to invest in controls that validate the integrity and provenance of third-party components and to strengthen our defenses against these kinds of ecosystem-level supply chain attacks.
Were OpenAI products or user data compromised?
No. We have found no evidence that OpenAI products or user data were compromised or exposed.
Have you seen malware signed as OpenAI?
No. We have found no evidence of malicious software being signed with any of OpenAI’s certificates.
Do I need to change my password?
No. Customer/user passwords and API keys were not affected.
What platforms does this affect?
Our signing keys for Windows, macOS, iOS, and Android were impacted. All of our applications are being re-signed and released with new certificates. macOS users will need to take action to update by June 12, 2026 for applications to continue functioning.
Why are you asking me to update my Mac apps?
Updating ensures you are running versions signed with our latest certificate. This certificate helps customers know that software comes from the legitimate developer, OpenAI.
Where do I download the updated macOS apps?
Only download OpenAI apps from in-app updates or the official webpages below:
Do not install apps from links in emails, messages, ads, or third-party download sites. Be cautious of unexpected “OpenAI,” “ChatGPT,” or “Codex” installers sent through email, text, chat messages, ads, file-sharing links, or third-party download sites.
What happens after June 12, 2026?
Effective June 12, 2026, older versions of our macOS desktop apps will no longer receive updates or support, and may not be functional. These versions represent the last releases signed with our outdated certificate:
ChatGPT Desktop: 1.2026.125
Codex App: 26.506.31421
Codex CLI: 0.130.0
Atlas: 1.2026.119.1
Why are you not revoking the certificate immediately?
We have worked to block any further notarization of macOS apps with the impacted notarization material. This means that any fraudulent app posing as an OpenAI app using the impacted certificate will lack notarization, and therefore will be blocked by default by macOS security protections unless a user explicitly bypasses those protections. Because new notarization with the previous certificate is blocked, and because the revocation may cause macOS to block new downloads and first-time launches of apps signed with the previous certificate, we are giving our users until June 12, 2026 to update to minimize disruption. This window will help minimize user risk and allow impacted clients to update through built-in update mechanisms, ensuring they are appropriately remediated. We are working with our partners to monitor for any indicators of misuse of the signing certificate, and will accelerate the revocation timeline if we identify malicious activity during this window.
