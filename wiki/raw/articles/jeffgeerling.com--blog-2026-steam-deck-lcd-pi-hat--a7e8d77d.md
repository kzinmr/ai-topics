---
title: "Getting the Steam Deck LCD working on a Raspberry Pi"
url: "https://www.jeffgeerling.com/blog/2026/steam-deck-lcd-pi-hat/"
fetched_at: 2026-08-21T10:01:06.664569+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Getting the Steam Deck LCD working on a Raspberry Pi

Source: https://www.jeffgeerling.com/blog/2026/steam-deck-lcd-pi-hat/

The
BOE TV070WXM-TV0 LCD
used in the original Steam Deck can be had for around $30. It's a serviceable 7" touchscreen with 400 nits of brightness and a resolution of 1280x800 (for a sharp 216 ppi).
The specs are a lot nicer than the
Pi 7" Touch Display
, which costs twice as much, with giant bezels and half the resolution!
Until today, the Steam Deck LCD didn't work with a Raspberry Pi. But the folks at
Scandent
were trying to standardize on a mass-market touchscreen for one of their own devices, and built a
Linux kernel driver
for it which they intend to upstream.
Not only that, they've open sourced a
Pi HAT design
which adapts the Raspberry Pi 5 or CM4's MIPI connection
to the special 39-pin connector on the Steam Deck LCD.
The repository linked above has detailed build instructions, and the KiCAD project if you'd like to build a HAT of your own. Scandent was kind enough to send me not one but
two
prototype HATs (the first one was damaged in shipping), and I put together this setup for testing:
Scandent isn't planning on productizing the HAT, they just wanted a decent touchscreen they could use that will be in good supply for at least a few years. Making it more accessible to hobbyists or others building Pi-based touchscreen projects should strengthen the market for this LCD, too.
From what I understand, LCD panels like these are often built for a specific purpose, and if a product line that uses it stops being manufactured, the specific LCD gets discontinued at some point, meaning downstream users have to work on supporting
another
one.
Just like switching from one SoC to another creates annoying rework, trying to sync up hardware signaling and a working kernel driver with multiple touchscreens is a pain.
I tested the Steam Deck LCD on a Raspberry Pi 5, and found it to work quite well. In person, I didn't see any real flickering or waviness, and brightness was good, even under my studio lights.
The touch targets are a little bit iffy at the Pi's default resolution scaling, but if you bump that up or build your own HMI/UI, you can make this thing quite usable. Maybe someone out there will build out the rest of the hardware and a 3D print for a RetroPie-based open source Steam Deck?
