---
title: "Bring back MiniDV with this Raspberry Pi FireWire HAT"
url: "https://www.jeffgeerling.com/blog/2026/minidv-with-raspberry-pi-firewire-hat/"
fetched_at: 2026-04-28T07:02:52.853581+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Bring back MiniDV with this Raspberry Pi FireWire HAT

Source: https://www.jeffgeerling.com/blog/2026/minidv-with-raspberry-pi-firewire-hat/

In my last post, I showed you to use
FireWire on a Raspberry Pi
with a PCI Express IEEE 1394 adapter. Now I'll show you how I'm using a new
FireWire HAT
and a
PiSugar3 Plus
battery to make a portable MRU, or 'Memory Recording Unit', to replace tape in older FireWire/i.Link/DV cameras.
The alternative is an old used MRU like
Sony's HVR-MRC1
, which runs around $300 on eBay
.
In addition to a direct camera connection, this setup can be used to archive MiniDV tapes to the Pi with
dvgrab
, or even with other FireWire devices like audio interfaces and hard drives. After Apple
dropped FireWire support in macOS Tahoe
, some users were left in a lurch.
Video
This blog post is a companion to today's video, where I test recording to tape and to the Pi using two different setups, and even test how the 'old' NLE editing workflow used to work when I started my YouTube channel in 2006:
Don't like watching videos? I don't blame you—read on!
Hardware
The hardware I used in my final setup (pictured above) includes:
The Firehat model I'm using is a prototype (thanks to Twin CD for sending it!). As such, it has a requisite number of bodge wires :)
It will be sold either as a standalone Pi HAT (the 'Firehat'), or integrated into a small standalone device paired with a Radxa Rock 2F ('equip-1'), at least if their
equip-1 / Firehat Crowd Supply campaign
is successful,
To make my setup portable, I added on a PiSugar 3 Plus (pictured above), which uses pogo pins to mate to the bottom of the Pi 5, providing power and I2C communication for battery status and configuration.
In my testing, the included 5000 mAh battery gets between 2-4 hours of runtime, depending on whether you're recording the whole time, and what kind of storage media you're using (this setup has built-in WiFi, so you could record direct to a NAS!). I got over 3 hours recording straight to a 64GB Raspberry Pi microSD card.
Software
The Firehat uses the Pi's GPIO to accept input through three buttons, and the I2C bus and more GPIO pins to sound a buzzer for button feedback, and LED for recording and other status indication, and a small OLED display to show recording time, the device's IP address, storage information, and battery life (if using a PiSugar).
Because Pi OS doesn't come with Linux's FireWire support enabled, you'll have to recompile the Linux kernel first, then install and run the Firehat software to get it fully operational:
Enable FireWire support on the Pi
following my guide
Install the Firehat software
(under 'Equip-1 Setup')
(Optionally)
Enable the Firehat software at boot
Assuming you've set everything up correctly, when you reboot your Pi, you should see the default interface (with 'NO CAM' displayed if you don't have a camera plugged in and powered on):
If you create new recordings, they're saved under your default user account's home folder in a
captures
directory. From there, you can copy the files over to a USB drive, or copy them over WiFi to another computer.
On my Mac I used
Transmit's
SFTP capabilities to log into the Pi and copy down files. You could also use
scp
or
rsync
if you like.
Alternatives
As mentioned in my
earlier post
, you could buy a standard
Mini PCIe HAT
for the Pi, and install this
StarTech Mini PCIe FireWire adapter in it
. That setup was first demonstrated by Redditor toqer and labelled the
Open MRU
in the r/tapeless subreddit.
For all the details, I
documented my own Open MRU setup on GitHub
. Without any GPIO-enabled buttons, controlling
dvgrab
is a little more involved—I had to start and stop recordings via
dvgrab
on the command line.
The Open MRU build uses the TI XIO2213A controller, versus the VIA VT6315N in the Firehat. People have tested other FireWire controllers on the Pi in the past, but these are the only two I've
confirmed
work with the Pi 5 so far.
Other FireWire devices and the 2029 deadline
I haven't had a chance to test other FireWire devices yet, or FireWire networking (though a 400 Mbps network connection is less than half the speed of the Pi's built-in Ethernet!).
But I've heard from a few people still running FireWire audio interfaces, or wanting to interface with old Macs via their built-in FireWire ports, so if
you've
tested any non-camera IEEE 1394 devices, please share your experience in the comments.
This setup should continue working with the latest versions of Linux and Pi OS
until at least 2029
, but the future for FireWire in the Linux kernel after that is less clear.
The equip-1 and Firehat should be available through
this Crowd Supply page
. Fingers crossed they can get to production and ship soon!
