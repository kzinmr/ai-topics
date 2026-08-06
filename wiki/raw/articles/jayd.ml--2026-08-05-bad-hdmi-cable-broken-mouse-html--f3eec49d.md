---
title: "A Bad HDMI Cable Broke My Mouse"
url: "https://jayd.ml/2026/08/05/bad-hdmi-cable-broken-mouse.html"
fetched_at: 2026-08-06T10:18:24.319535+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# A Bad HDMI Cable Broke My Mouse

Source: https://jayd.ml/2026/08/05/bad-hdmi-cable-broken-mouse.html

I got tasked to fix some bizarre issues a friend was having with their gaming PC.
They had had lots of bluetooth issues, and recently their mouse stopped working
entirely in Windows 11 - nothing would show up in Control Panel. Other mice also
didn’t work.
It worked fine in the BIOS and in an Manjaro installer, so I got suspicious and
for the first time in my storied career there was actually bad stick of RAM!
This person had expressed interest in switching to Linux before, and they had
done enough fiddling around with drivers (plus the OS was installed with bad ram
I’m never trusting it again) that I convinced them to install Manjaro.
The mouse worked fine in the installer, rebooted, no mouse. Or keyboard now! We
made it worse!
Ctrl
+
Alt
+
F1
switched to a working TTY though, which was odd. I tried
updating the BIOS, checking
dmesg
. The chatbots had me going down wild goose
chases in the BIOS fiddling IOMMU settings and XHCI handoffs.
Finally I decided to just start unplugging things to see if something was screwing
up the USB bus. WiFi/BT card didn’t help, so the next step was the 4k Samsung
monitor.
The mouse immediately started working.
I plugged it back in.
It stopped.
I used a different HDMI cord.
It continued to work.
̄_(ツ)_/ ̄
Reminds me of the time
I had a cheap USB switch that would cause WiFi / HDMI
radio interference
but only when the screen was mostly white
. I guess HDMI is cursed.
