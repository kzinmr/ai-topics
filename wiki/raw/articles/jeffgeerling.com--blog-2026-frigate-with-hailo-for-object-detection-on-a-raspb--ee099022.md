---
title: "Frigate with Hailo for object detection on a Raspberry Pi"
url: "https://www.jeffgeerling.com/blog/2026/frigate-with-hailo-for-object-detection-on-a-raspberry-pi/"
fetched_at: 2026-04-29T07:02:14.017952+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Frigate with Hailo for object detection on a Raspberry Pi

Source: https://www.jeffgeerling.com/blog/2026/frigate-with-hailo-for-object-detection-on-a-raspberry-pi/

I run
Frigate
to record security cameras and detect people, cars, and animals when in view. My
current Frigate server
runs on a Raspberry Pi CM4 and a
Coral TPU
plugged in via USB.
Raspberry Pi offers
multiple AI HAT+'s
for the Raspberry Pi 5 with built-in Hailo-8 or Hailo-8L AI coprocessors, and they're useful for low-power inference (like for image object detection) on the Pi. Hailo coprocessors can be used with other SBCs and computers too, if you buy an
M.2 version
.
Frigate offers Hailo support, but getting it working on my new build (pictured above—full writeup coming soon) threw me for a loop, so I'm documenting the process for
my
build here, for my own future reference.
Assuming you have a fresh Pi OS install on a Pi 5 or CM5, and you have the Hailo module connected via PCIe (either a HAT+ module, or via an M.2 slot), do the following:
Follow
Frigate's guide to install the Hailo-8 driver from source
.
Follow
Frigate's guide for setting up Hailo as an object detector
in your Frigate
config.yml
(note: I use my open source
Pi NVR project
).
Start Frigate.
If you see a message like:
WARNING : CPU detectors are not recommended and should only be used for testing or for trial purposes.
Then your detector configuration is likely wrong. Check back through your
model
and
detectors
config in
frigate.yml
and try again :)
PCIe
force_desc_page_size
issue
Outside of configuration issues that took a few tries to fix, I ran into this error message when running
docker logs frigate
:
[HailoRT] [error] CHECK failed - max_desc_page_size given 16384 is bigger than hw max desc page size 4096
...
RuntimeError: HailoRT inference thread has stopped, restart required.
That error led me to
this forum thread
, which suggested a fix:
Create a file
/etc/modprobe.d/hailo_pci.conf
(e.g. with
sudo nano
), with the following contents:
options hailo_pci force_desc_page_size=4096
Then either reboot the Pi, or run the following commands to unload, then reload, the hailo driver:
sudo modprobe -r hailo_pci
sudo modprobe hailo_pci
The Frigate container logs should report the Hailo detector is now in use:
[2026-02-18 14:14:35] detector.hailo  INFO: Starting detection process: 621
And now, the system dashboard is showing
hailo
as running at around 12ms inference speed, with very low CPU usage overall (this was testing with two cameras):
The nice thing is, this works on the cheaper Hailo-8L that you can find in the $70 AI HAT+ (the 'base model'), which is often much cheaper than the now-ancient
Google Coral TPU
—at least the USB version that's more broadly compatible.
I'm still at a loss as to why Google abandoned Coral after one generation. It seems like they could've dominated the 'edge TPU' market, but they kinda gave it up after hitting 4 TOPS.
