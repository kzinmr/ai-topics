---
title: "Hands-on with Raspberry Pi's CM5 Programming Jig"
url: "https://www.jeffgeerling.com/blog/2026/cm5-programming-jig/"
fetched_at: 2026-08-19T10:00:59.068193+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Hands-on with Raspberry Pi's CM5 Programming Jig

Source: https://www.jeffgeerling.com/blog/2026/cm5-programming-jig/

In the before-times, when Raspberry Pi CM5s were (relatively) affordable, I built a number of Pi clusters (
example
), and one of the most annoying parts of the build was flashing Raspberry Pi OS to all the Pis.
One, two, or even three Pis isn't a big deal, but once you hit 4+, the process of plugging the Compute Module into a carrier board, plugging that into a computer, managing Raspberry Pi Imager, and trying to match up details like a hostname, MAC address, and the physical Pi itself, gets annoying.
Solvable, but annoying.
Raspberry Pi has a solution for that, now. It's the
CM5 Programming Jig
(pictured above), one of which they sent for testing.
Because of a tight schedule this week, I only got a few hours to get up to speed. I haven't gotten an end-to-end CM5 imaging line going, but I was able to get most of the way there.
Demo of the CM5 Programming Jig
For the tl;dr, you can watch the video with an unboxing, full demonstration, and more context here:
But if you enjoy reading, skip the video and carry on!
Programming and Testing Jigs
Before talking about Raspberry Pi's Jig (which was
developed in tandem with EDAtec
), I would be remiss not to mention Everypin's
CM5 Flash Jig
, which is very closely related, but works with Everypin's open source Python libraries and costs €2200 (about $2500 USD).
The Raspberry Pi version costs $600, and works out of the box with Raspberry Pi's own Pi imaging/management tools, like
rpi-sb-provisioner
(which runs on the Jig) and
pi-gen
.
Everypin did excellent work
documenting the CM5 test points
and
their own Jig
, but a price well over $2k makes it very difficult to justify for smaller CM5 production runs.
The Raspberry Pi version is relatively expensive, but easier to justify if you're a small business (or even factory production line) provisioning hundreds or thousands of Compute Modules.
Getting the Programming Jig Ready
Raspberry Pi has documentation for the Programming Jig, so I won't rehash all that, but the basic process is:
(Assuming the Programming Jig is not already flashed): Flash Jig OS to the Jig using Raspberry Pi Imager 2.0.11 or later.
Build your own Raspberry Pi .img images using
pi-gen
Configure the Programming Jig via it's local web UI
Start popping in CM5s to flash.
The LED on the Jig will start flashing blue, and after a few minutes, when the CM5 is finished, it should switch to green.
pi-gen
to build an OS Image
Just as a note, when I tried building my own Pi OS image on my Mac running macOS Tahoe, I ran the included Docker script, and had to check out the
arm64
branch of the
pi-gen
software.
Here are the contents of my
config
file used for image generation:
RELEASE
=
trixie
ARCH
=
arm64
IMG_NAME
=
"jeffpios-trixie"
PI_GEN_RELEASE
=
"Jeff Geerling Pi OS"
USE_QEMU
=
0
# Account and SSH settings
FIRST_USER_NAME
=
"jgeerling"
PASSWORDLESS_SUDO
=
1
ENABLE_SSH
=
1
PUBKEY_ONLY_SSH
=
1
PUBKEY_SSH_FIRST_USER
=
"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA+PT1uOv/gmUyD+Dj++gQAMrmsXmGDtUesd1CrIRD1d jeff@macmini"
I generated a Trixie 'Lite' image and copied that over to the Programming Jig using
magic-wormhole
.
rpi-sb-provisioner
to Provision the CM5s
The provisioner has it's own web UI that you can use to monitor CM5 flashing progress. It will also log all successful runs in a local manufacturing database with information about the CM5's MAC address, serial number, and hardware specs.
I guess it's up to you to feed that data into other manufacturing systems, labeling workflows, etc. And larger operations would certainly have more automation for loading and unloading CM5s. It wouldn't surprise me if Raspberry Pi themselves use this or a version of it in their own manufacturing lines.
I know they were working on CM4 test jigs years ago when I visited the Sony factory (see photo above), but it used the more fragile Hirose connectors, which are only rated for around 30 insertions before signal integrity is not guaranteed. I can imagine feeding a thousand Pis a day into those connectors was a recipe for annoying quirks!
Instead, the Programming Jig has a 'bed of nails' (a bunch of pogo pins) which target test pad locations on the bottom of every CM5:
Much more repeatable, and this is the same kind of setup I saw them using for Pi 4 production when I visited their factory.
Conclusion
Honestly, this is not something an individual tinkerer could justify buying, even if you manage a few small Pi clusters. But to some small businesses and systems integrators, the CM5 Jig will be immensely useful.
And in 5-10 years, if you start seeing these things show up in used factory surplus, know that they have a little CM5 tucked inside you could harvest :)
