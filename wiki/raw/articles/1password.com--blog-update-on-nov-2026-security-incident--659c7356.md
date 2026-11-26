---
title: "Update on a security incident involving 1Password’s backend systems."
url: "https://1password.com/blog/update-on-nov-2026-security-incident"
fetched_at: 2026-11-26T10:00:51.281592+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Update on a security incident involving 1Password’s backend systems.

Source: https://1password.com/blog/update-on-nov-2026-security-incident

The short version
An attacker gained access to some of our backend systems and copied a limited amount of customer account information from a subset of our customers, including the names and email addresses that customers use to sign into 1Password.
Your vault data, the items in them, and the keys that protect them are safe and were not affected.
1Password does not have access to your password or secret keys.
We implemented containment measures, restored clean versions of the affected service, and have triggered a rotation of internal credentials.
You do not need to update anything in your 1Password account.
We recommend being cautious of phishing attempts in the form of unexpected emails about 1Password, such as invitations or account recovery requests that you did not initiate.
1Password apps and services are working normally.
What happened
On November 19, 2026, 1Password began investigating indications that an attacker gained access to an employee’s corporate GitHub account. The actor used the account to access source code and push malicious code to backend services, which downloaded administrative data pertaining to our customers. This data included customer names and email addresses, in addition to non-secret internal metadata about the account. At no time were customer vault contents accessed by, or available to, the attacker.
What information was affected
The attacker downloaded account records for a subset of our users. These records include:
Names and email addresses
Account and user identifiers, and account creation and last sign-in times
Public keys (which are public by design, this has no impact to user security)
Secure Remote Password
protocol parameters (which cannot be used to access your account)
Tokens present in certain emailed links for invitations, provisioning and account recovery
Other non-secret account metadata relative to our internal architecture (e.g. version numeric identifiers, file numeric identifiers)
The attacker also copied source code from private repositories and gained access to our CI/CD system. Our source code is not customer data, and contains no user secrets. CI/CD contains infrastructure related secrets in order for our product to work. We have triggered a rotation of all credentials which may have been exposed, and there is no impact to 1Password’s services, availability, or product security.
When we send an email to a customer to accept a provisioning invite to an account, or to accept recovery of their account, it contains a token. A provisioning invite is specifically used for our
SCIM Bridge
or
Hosted Provisioning
. During this incident there were a small number of users in this state, who have been specifically notified. This token is used to complete the invitation or recovery process, but only when combined with an SSO sign-in or a six digit code sent to the user's registered email address. The token is not able to get access to the account by itself. In order to reduce the ability for a malicious third party to successfully guess the code, we’ve expanded the code from six numeric digits to ten alphanumeric digits. This makes brute force guessing practically impossible.
What was not affected
Your vaults and the items in them
The keys that protect your vaults
1Password does not store your account password or secret key
Account recovery keys
1Password apps and browser extensions
What we’ve done
Disabled the affected GitHub account, revoked the stolen token, and removed the access the attacker created.
Rotated or revoked all internal credentials which may have been exposed.
Lengthened the codes used in invitation and recovery emails from six digits to ten characters as a precautionary measure.
Tightened internal GitHub, CI/CD, and endpoint controls, and added new detections for this kind of attack.
Validated no internal evidence of user account takeovers or compromise using any exposed account provisioning tokens.
Brought in independent cybersecurity experts to validate our containment approaches and remediation efforts.
What you can do
Be cautious about phishing attempts in the form of unexpected emails, texts or calls that mention 1Password, invitations, or account recovery attempts.
1Password will never contact you to ask for your account password or Secret Key. Only enter them in the official 1Password app, or on our official website, and only when you’ve opened the app or typed the address yourself. Your Secret Key is only needed the first time you sign in on a new device or browser.
Keep your Secret Key and account password safe.
If you see something suspicious, tell us at support@1password.com.
Our commitment to you
You trust us with some of the most sensitive information you have. 1Password is designed so that a breach of our systems can’t expose your vault contents. Your vault secrets are encrypted with keys that only you hold, so we can’t access them, and neither can an attacker who gets into our servers.
We are committed to transparency in the interests of our customers' security and the security of the broader industry, which is why we have published and maintained our
Security Whitepaper
since 2015.  We’ll keep this blog post current, and we’ll update it if we find anything that changes what we’ve said here.
