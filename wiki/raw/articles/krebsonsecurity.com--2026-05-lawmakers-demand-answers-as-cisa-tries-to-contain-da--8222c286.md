---
title: "Lawmakers Demand Answers as CISA Tries to Contain Data Leak"
url: "https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/"
fetched_at: 2026-05-23T07:01:05.825433+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Lawmakers Demand Answers as CISA Tries to Contain Data Leak

Source: https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/

Lawmakers in both houses of Congress are demanding answers from the
U.S. Cybersecurity & Infrastructure Security Agency
(CISA) after KrebsOnSecurity reported this week that a CISA contractor intentionally published AWS GovCloud keys and a vast trove of other agency secrets on a public
GitHub
account. The inquiry comes as CISA is still struggling to contain the breach and invalidate the leaked credentials.
On May 18, KrebsOnSecurity reported that a CISA contractor with administrative access to the agency’s code development platform had
created a public GitHub profile
called “
Private-CISA
” that included plaintext credentials to dozens of internal CISA systems. Experts who reviewed the exposed secrets said the commit logs for the code repository showed the CISA contractor disabled GitHub’s built-in protection against publishing sensitive credentials in public repos.
CISA acknowledged the leak but has not responded to questions about the duration of the data exposure. However, experts who reviewed the now-defunct Private-CISA archive said it was originally created in November 2025, and that it exhibits a pattern consistent with an individual operator using the repository as a working scratchpad or synchronization mechanism rather than a curated project repository.
In a written statement, CISA said “there is no indication that any sensitive data was compromised as a result of the incident.” But in a
May 19 a letter
(PDF) to CISA’s Acting Director
Nick Andersen
,
Sen. Maggie Hassan
(D-NH) said the credential leak raises serious questions about how such a security lapse could occur at the very agency charged with helping to prevent cyber breaches.
“This reporting raises serious concerns regarding CISA’s internal policies and procedures at a time of significant cybersecurity threats against U.S. critical infrastructure,” Sen. Hassan wrote.
A May 19 letter from Sen. Margaret Hassan (D-NH) to the acting director of CISA demanded answers to a dozen questions about the breach.
Sen. Hassan noted that the incident occurred against the backdrop of major disruptions internally at CISA, which
lost more than a third of it workforce
and almost all of its senior leaders after the Trump administration forced a series of early retirements, buyouts, and resignations across the agency’s various divisions.
Rep. Bennie Thompson
(D-MS), the ranking member on the House Homeland Security Committee, echoed the senator’s concerns.
“We are concerned that this incident reflects a diminished security culture and/or an inability for CISA to adequately manage its contract support,” Thompson wrote in
a May 19 letter
to the acting CISA chief that was co-signed by
Rep. Delia Ramirez
(D-Ill), the ranking member of the panel’s Subcommittee on Cybersecurity and Infrastructure Protection. “It’s no secret that our adversaries — like China, Russia, and Iran — seek to gain access to and persistence on federal networks. The files contained in the ‘Private-CISA’ repository provided the information, access, and roadmap to do just that.”
KrebsOnSecurity has learned that more a week after CISA was first notified of the data leak by the security firm
GitGuardian
, the agency is still working to invalidate and replace many of the exposed keys and secrets.
On May 20, KrebsOnSecurity heard from
Dylan Ayrey
, the creator of
TruffleHog
, an open-source tool for discovering private keys and other secrets buried in code hosted at GitHub and other public platforms. Ayrey said CISA still hadn’t invalidated an RSA private key exposed in the Private-CISA repo that granted access to a GitHub app which is owned by the CISA enterprise account and installed on the CISA-IT GitHub organization with full access to all code repositories.
“An attacker with this key can read source code from every repository in the CISA-IT organization, including private repos, register rogue self-hosted runners to hijack CI/CD pipelines and access repository secrets, and modify repository admin settings including branch protection rules, webhooks, and deploy keys,” Ayrey told KrebsOnSecurity. CI/CD stands for Continuous Integration and Continuous Delivery, and it refers to a set of practices used to automate the building, testing and deployment of software.
KrebsOnSecurity notified CISA about
Ayrey’s findings
on May 20. Ayrey said CISA appears to have invalidated the exposed RSA private key sometime after that notification. But he noted that CISA still hasn’t rotated leaked credentials tied to other critical security technologies that are deployed across the agency’s technology portfolio (KrebsOnSecurity is not naming those technologies publicly for the time being).
CISA responded with a brief written statement in response to questions about Ayrey’s findings, saying “CISA is actively responding and coordinating with the appropriate parties and vendors to ensure any identified leaked credentials are rotated and rendered invalid and will continue to take appropriate steps to protect the security of our systems.”
Ayrey said his company Truffle Security monitors GitHub and a number of other code platforms for exposed keys, and attempts to alert affected accounts to the sensitive data exposure(s). They can do this easily on GitHub because the platform publishes a live feed which includes a record of all commits and changes to public code repositories. But he said cybercriminal actors also monitor these public feeds, and are often quick to pounce on API or SSH keys that get inadvertently published in code commits.
The Private-CISA GitHub repo exposed dozens of plaintext credentials to important CISA GovCloud resources.
In practical terms, it is likely that cybercrime groups or foreign adversaries also noticed the publication of these CISA secrets, the most egregious of which appears to have happened in late April 2026, Ayrey said.
“We monitor that firehose of data for keys, and we have tools to try to figure out whose they are,” he said. “We have evidence attackers monitor that firehose as well. Anyone monitoring GitHub events could be sitting on this information.”
James Wilson
, the enterprise technology editor for the
Risky Business
security podcast, said organizations using GitHub to manage code projects can set top-down policies that prevent employees from disabling GitHub’s protections against publishing secret keys and credentials. But Wilson’s co-host
Adam Boileau
said it’s not clear that any technology could stop employees from opening their own personal GitHub account and using it to store sensitive and proprietary information.
“Ultimately, this is a thing you can’t solve with a technical control,” Boileau said on
this week’s podcast
. “This is a human problem where you’ve hired a contractor to do this work and they have decided of their own volition to use GitHub to synchronize content from a work machine to a home machine. I don’t know what technical controls you could put in place given that this is being done presumably outside of anything CISA managed or even had visibility on.”
Update, 3:05 p.m. ET:
Added statement from CISA. Corrected a date in the story (Truffle Security said it found the repo gained some of its most sensitive secrets in late April 2026, not 2025).
