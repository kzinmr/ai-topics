---
title: "Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts"
url: "https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/"
fetched_at: 2026-06-02T07:05:04.632669+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts

Source: https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/

The
Instagram
accounts for the Obama White House and the Chief Master Sergeant of the U.S. Space Force were briefly defaced with pro-Iranian images and messages over the weekend, after instructions began circulating on Telegram showing how to trick Meta’s “AI support assistant” bot into resetting account passwords.
A screenshot from a video released on Telegram claiming to show how Meta’s AI customer support bot could be tricked into resetting a target’s password.
On May 31, word began to spread on several Telegram instant message channels that Meta’s AI bot would happily add an email address to an existing account as part of the bot’s standard password reset flow.
A video released on Telegram by pro-Iran hackers claimed to document a remarkably simple exploit that appears to have involved using a VPN connection with an IP address that is in or near the target’s usual hometown, requesting a password reset for the account, and then choosing to chat with Meta’s AI support assistant. From there, the video shows the attacker told the bot to link the account in question to a new email address, after which the bot dutifully sent that address a one-time code that allowed a password reset.
The Telegram account that posted the video also linked to screenshots of pro-Iran images, videos and messages that defaced the hacked Instagram accounts, saying hackers had used the exploit to hijack a number of valuable (read: short) Instagram account names that allegedly have a resale value of more than a half million dollars.
Meta has not responded to requests for comment on the video’s claims, but Meta’s Andy Stone
said
on Twitter/X that the issue had been resolved and that they were securing impacted accounts. The security blog thecybersecguru.com
reports
that Meta pushed an emergency patch over the weekend, and clarified that no back end database was breached.
“Instagram has notoriously poor human support infrastructure,” Cybersecguru wrote. “Recovering a locked account – especially a high-value one can take weeks of back-and-forth with an automated ticketing system. Meta’s solution was to deploy a conversational AI layer to handle common recovery workflows: relinking a lost email address, triggering a password reset, verifying account ownership. The assistant, presumably, was supposed to reduce friction for legitimate users stuck in account-access hell.”
Ian Goldin
, a threat researcher at Lumen’s
Black Lotus Labs
, said we’re entering unchartered security territory as more large online platforms start allowing AI chatbots to handle sensitive account recovery requests. Just like human customer support employees can be social engineered into providing unauthorized access to someone’s account, AI bots are equally eager to help and vulnerable to persuasion and trickery, he said.
“AI chatbots create interesting new attack surface, and we’re likely going to see a lot more of these kinds of attacks,” Goldin said.
Securing your various online accounts means taking full advantage of the most secure form of multi-factor authentication (MFA) offered (such as a passkey or security key). In this case, even using the least robust form of MFA that Instagram offers — a one-time code sent via SMS — likely would have blocked the exploit: The hackers who released the video on Telegram said their exploit failed to work against any accounts that had MFA enabled.
