---
title: "targeted attacks on prominent Rustaceans"
url: "https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/"
fetched_at: 2026-09-18T10:00:51.924909+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# targeted attacks on prominent Rustaceans

Source: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/

17th September 2026 - Link Blog
Be alert: targeted attacks on prominent Rustaceans
. Important warning from Adam Harvey and the crates security team:
We believe that there is an ongoing campaign targeting rust-lang members and owners of popular crates that is attempting to compromise devices and accounts in order to use them to publish malware.
A video call is set up for something positive — maybe for a job, maybe for a project, maybe for a contract opportunity — and then that's used as a vector to either get the target to install something on their computer (such as a purportedly missing audio codec) or execute another command (for example, via putting a command on the clipboard).
Last month this trick was used in a successful
supply chain attack against the array ref crate
, among others.
Any piece of software that depends on open source (which is almost
every
piece of software) has a network of human beings who are potential attack vectors - everyone with publishing rights to any of the packages in the dependency network for that software.
I guess our best defense right now is
dependency cooldowns
- giving new package releases a few days before upgrading to them, in the hope that supply chain attacks like this will be spotted by someone else.
