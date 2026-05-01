---
title: "Ubiquiti And VPN Clients"
url: "https://philiplaine.com/posts/ubiquiti-and-vpn-clients/"
fetched_at: 2026-05-01T07:01:58.397691+00:00
source: "philiplaine.com"
tags: [blog, raw]
---

# Ubiquiti And VPN Clients

Source: https://philiplaine.com/posts/ubiquiti-and-vpn-clients/

I have for some time wanted to learn about the different VPN services offered by AWS. Having invested some money into a full Unifi setup I thought that it would be a good idea to setup an
AWS Site-to-Site VPN and AWS Client VPN
connection between my lab network and my AWS account. I struggled for some time, messing around with the settings trying to get my
USG
to connect to the VPN server but it would not work. I probably wasted a couple of days of my free time pulling my hair out not really understanding why it wouldn’t connect.
After digging a bit deeper I finally understood that it would never work. The reason to this is that AWS Virtual Private Gateway required AES-256-GCM encryption for the communication to work. While the USG due to a lack of updates only support AES-256-CBC. Sure it seems like a small difference in the names of the cyphers but the impact is large. I will not go into detail about the differences between the ciphers, as I would probably mess it up, you can read about it
here
.
The blame for the lack of support falls on Ubiquiti themselves and their unwillingness to update their dependencies in their OS. As of recording the current version of OpenVpn in their OS is 2.3.2. Their have been
calls for them to upgrade their dependendcy
without any success. The issue seems to have been around for at least a year, I just stumbled upon it now. This is really a big issue considering the CVEs pointing to issues with the ciphers being used. I am just as dissapointed as the people in the thread. It has made me rethink the relationship a customer has to Ubiquiti as we do not have the option to control the dependencies in the OS in the same way one would have in “normal” linux distro. Sadly it does not seem like change is on its way, while I am on my way to Pfsense.
