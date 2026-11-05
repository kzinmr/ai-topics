---
title: "Updated GPG Signing key for Warp Linux Releases"
source: "Warp Blog"
url: "https://www.warp.dev/blog/updated-gpg-signing-key-for-warp-linux-releases"
scraped: "2026-11-05T06:00:25.067492+00:00"
lastmod: "2026-11-04T18:08:19.000Z"
type: "sitemap"
---

# Updated GPG Signing key for Warp Linux Releases

**Source**: [https://www.warp.dev/blog/updated-gpg-signing-key-for-warp-linux-releases](https://www.warp.dev/blog/updated-gpg-signing-key-for-warp-linux-releases)

Company
Updated GPG Signing key for Warp Linux Releases
Warp
|
November 4, 2026
Due to precautionary measures from a
security incident
last week, we recently rotated our GPG signing subkey which we use to sign some of our Warp Linux artifacts.
We have no evidence of misuse by unauthorized parties but we’re doing this out of an abundance of caution.
Follow the instructions below to get our updated public key.
Ubuntu / Debian (if using our package repo)
Sh
wget -qO- https://releases.warp.dev/linux/keys/warp.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/warpdotdev.gpg

sudo apt update
If you configured our apt repository manually (following our docs) instead of installing the .deb, the key is at
/etc/apt/keyrings/warpdotdev.gpg
; use that path instead.
Arch
Sh
sudo pacman-key -r "linux-maintainers@warp.dev"
sudo pacman -Syu
Fedora 43 and newer
Import the updated key, then upgrade. Fedora 43's rpm updates the existing key in place, so there is nothing to remove first:
Sh
sudo rpm --import https://releases.warp.dev/linux/keys/warp.asc
sudo dnf upgrade warp-terminal
Fedora 42 and older, RHEL, CentOS, Rocky, AlmaLinux
Remove the old key before importing the new one. Importing while the old key is still installed can appear to succeed without changing anything.
Sh
sudo rpm -e --allmatches gpg-pubkey-d60f803f-65c9382c
sudo rpm --import https://releases.warp.dev/linux/keys/warp.asc
sudo dnf upgrade --refresh warp-terminal
openSUSE / SLE
Remove the old key before importing the new one. Importing while the old key is still installed can appear to succeed without changing anything. Then refresh zypper and update:
Sh
sudo rpm -e --allmatches gpg-pubkey-d60f803f-65c9382c
sudo rpm --import https://releases.warp.dev/linux/keys/warp.asc
sudo zypper refresh && sudo zypper update warp-terminal
Verify the key
Our public key is published at
https://releases.warp.dev/linux/keys/warp.asc
. To check its fingerprints:
Sh
wget -qO- https://releases.warp.dev/linux/keys/warp.asc | gpg --show-keys --with-subkey-fingerprints
Primary key (unchanged):
0913 165C 78D5 B7A4 1B42 AC65 7FF7 AB39 D60F 803F
New signing subkey:
D272 B58E 4BF4 EA3E 7CB9 58A5 5AC0 1A19 A09F A9A6, expires 2028-10-29
Revoked signing subkey:
19A1 E427 461B 1795 F73F 6296 31F4 254A FE49 E02E
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Oct 3, 2026
|
Company
1
min
Build the factory. Let it run. Go kayaking.
1
min
Sep 28, 2026
|
Company
8
min
Adapting for a world of software factories
8
min
Jun 18, 2026
|
Company
7
min
We are now factory engineers, not product engineers
7
min
Jun 12, 2026
|
Company
5
min
How Rectangle Health Built an AI Teammate That Writes Its Own Code
5
min
Apr 28, 2026
|
Company
4
min
The virtuous loop of open, automated development
4
min
View all articles
