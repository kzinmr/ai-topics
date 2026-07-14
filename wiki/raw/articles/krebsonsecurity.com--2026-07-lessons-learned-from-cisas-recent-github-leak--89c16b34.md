---
title: "Lessons Learned from CISA’s Recent GitHub Leak"
url: "https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/"
fetched_at: 2026-07-14T07:01:12.695446+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Lessons Learned from CISA’s Recent GitHub Leak

Source: https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/

The
Cybersecurity and Infrastructure Security Agency
(CISA) has issued a postmortem on a recent data leak in which a contractor published dozens of internal CISA credentials — including AWS Govcloud keys — in a public GitHub repository for almost six months before being notified by KrebsOnSecurity. Experts say the gaps identified in the agency’s initial response provide important lessons that all security teams should absorb.
On May 15, 2026, the security firm
GitGuardian
asked for help in notifying CISA about the existence of a public GitHub repository called “Private CISA” that included 844 MB of sensitive CISA-related data. One of the exposed files, titled “importantAWStokens,” included the administrative credentials to three Amazon AWS GovCloud servers. Another file — “AWS-Workspace-Firefox-Passwords.csv” — listed plaintext usernames and passwords for dozens of internal CISA systems.
CISA quickly acknowledged our initial alert, but took more than 48 hours to invalidate the AWS keys and many other important secrets leaked in the GitHub repo. In
its report on the data leak
, CISA said the complexities of the agency’s systems and interconnections with federal and industry partners caused its key rotation to take longer than anticipated.
“Drawing on this experience, CISA encourages others to maintain mature and well-tested key management capabilities,” the report notes.
CISA also admitted it can do better when it comes to responding to security incident notifications from external parties. The postmortem stresses that clear and distinct reporting channels are essential to ensure that incidents affecting the organization itself are handled differently from those involving its products or customers.
“In CISA’s case, these channels were not well defined, leading the security researcher to try multiple avenues – including emailing the contractor, submitting through CISA’s vulnerability disclosure platform (which is intended for vulnerabilities impacting the broader cybersecurity community), and ultimately involving a reporter,” reads the analysis written by
Preston Werntz
and
Brad Libbey
, the acting chief information officer and acting chief information security officer at CISA, respectively.
CISA said it is refining its reporting channels to make them easier and faster for researchers. “Additionally, while many researchers rely on the security.txt file, organizations can ensure clarity by publishing reporting instructions in multiple prominent locations,” the CISA authors wrote.
Guillaume Valadon
, the GitGuardian researcher who first contacted KrebsOnSecurity about the exposed CISA credentials, said CISA ignored nine automated alerts about the exposed credentials prior to our notification on May 15. Valadon’s company constantly scans public code repositories at GitHub and elsewhere for exposed secrets, automatically alerting the offending accounts of any apparent sensitive data exposures.
“Letting nine notification emails go unanswered is how a one-day incident becomes a six-month exposure,” Valadon
wrote
in an analysis of CISA’s report. “Make it trivial to report a leak about you, not just about your products. The person reporting a leak to you is not the threat. Publish a
security.txt
, but do not stop there. Put reporting instructions in several prominent places, and make sure a report about your own infrastructure does not land in a product-bug queue.”
The report’s authors also emphasized the importance of continuously scanning public code repositories like GitHub for exposed secrets, and said CISA has since rotated all secrets and created an action plan to improve management of developer secrets and to better monitor for them going forward.
The report notes that while CISA had developed a playbook for responding to cybersecurity incidents, that playbook somehow didn’t include what to do in situations involving GitHub or other cloud services. Valadon said the report validates the need to scan continuously — not just quarterly — for exposed secrets.
“The Private-CISA repository sat public for six months,” Valadon wrote. “Continuous monitoring of public GitHub surfaced it. Comprehensive internal scanning could have caught the plaintext passwords and committed backups long before they left the building.”
CISA gave itself passing grades on several areas of security preparedness that it said helped the agency gauge the scope and impact of the exposed secrets, including enhanced logging capabilities, and the adoption of zero-trust principles in both its production and development systems. CISA said those detailed logs allowed it to show that no customer or mission data was exposed, and that the leaked credentials were not used outside of CISA’s environments. The agency said the contractor who exposed the secrets had their system access revoked.
Valadon reckons the biggest takeaway is the CISA postmortem itself, and praised the agency for being transparent about what worked and what didn’t.
“To my knowledge, it is also the first time a national cybersecurity agency has publicly advocated for secrets scanning and for simplifying relations with security researchers,” Valadon wrote. “That is exactly the incident communication we should expect from every organization.”
