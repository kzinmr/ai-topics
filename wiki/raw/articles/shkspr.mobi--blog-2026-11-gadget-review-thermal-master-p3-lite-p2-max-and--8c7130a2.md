---
title: "Gadget Review: Thermal Master P3 Lite - and Linux Instructions"
url: "https://shkspr.mobi/blog/2026/11/gadget-review-thermal-master-p3-lite-p2-max-and-linux-instructions/"
fetched_at: 2026-11-14T10:01:03.105374+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Gadget Review: Thermal Master P3 Lite - and Linux Instructions

Source: https://shkspr.mobi/blog/2026/11/gadget-review-thermal-master-p3-lite-p2-max-and-linux-instructions/

The good folks at Thermal Master have sent me (yet another) thermal camera. The P3 Lite has a
detachable
macro lens. As well as being good for scanning your house for leaks and looking for wildlife, it can focus down on tiny electronic components.
I've previously reviewed their
P3 with adjustable macro focus
, the chunky
T2 Max
, and the wildlife spotting
DV2
- how does this compare?
Like most thermal cameras, it has a low-ish resolution - 256×192, but their X
3
software upscales it to 512×384 running at around 25fps. That's pretty decent for a small plug-in camera.
It also has a magnetically attachable lens for macro-focus, which allows you to see close up details.
You can
read the full specs
but, basically, it is suitable for all domestic tasks.
Note, all photos were originally 6MB JPGs - I've losslessly converted them to JPEG-XL and kept the (minimal) EXIF.
Point the camera at something and you'll see which bits are hot. Useful for checking your radiators are working.
Images are stored in portrait mode and have been rotated. As you can see, some of the UI elements remain in portrait mode. Here's a just-finished dishwasher:
A 30 second video is about 12MB - it does include audio from your phone's microphone. I've recompressed and rotated this. It is a tap running cold, then hot, then cold again.
Video quality is, I think, excellent.
There are a variety of different thermal palettes to choose from - and the camera excels at spotting where a circuit's hot spots are. Here's a Raspberry Pi:
So what about the macro lens? Here's a close-up shot of a circuit board where I
haven't
used the included lens:
Not bad, but what if we click the magnetic lens on?
Whoa! Much better. Here's a video demonstrating it.
The camera has a reasonably long USB-C protrusion - so it will fit in your phone even if you use a chunky case.
Because it is USB-C, you can have it facing you or facing away from you. Handy if you want some thermal selfies!
The lens is a simple affair. Note that the protective cover it ships with might not come away cleanly:
I had to prise off the sticker to prevent that residue dirtying the main lens.
It ships with a USB-C extension cable (with USB-A converter) - that's handy if you want to keep camera and phone somewhat separate. It also makes it easy to plug it in to a computer. More on that later.
There's a C to Lightning adapter if you're still stuck on an old iPhone.
Finally, it comes with a little carry case emblazoned with the logo.
The Thermal Master Android App isn't brilliant. It's slow to start and has a bafflingly complicated interface. It takes a couple of clicks to take a photo, rather than the single click you'd expect.
As you can see from the photos, despite the timestamp being rotated, other on-screen elements aren't. You can possibly change this manually in the settings, but it is rather annoying that it doesn't do it automatically. Speaking of which, there are lots of settings to fiddle with - but you'll probably just end up on one that you like and leave it there.
The app does work, but I wish it were snappier.
There is a
Windows App
. I couldn't get it working in either VirtualBox or Wine, so here's how to display the camera's feed in Linux.
Plug in the camera via the included USB-C extension cable. It will show up in
lsusb
as
3474:42b2 Thermal Master Technology Co., Ltd. P2 MAX
Note:
the device was previously known as the P2Max and this is reflected in the firmware.
Add a new udev rule with
sudo nano /etc/udev/rules.d/99-thermal-p2max.rules
Copy and paste this into the file, then save and exit.
Copied  to 📋
⧉
# Thermal Master P2 Max USB Rules
# Allow read/write access for all users
SUBSYSTEM=="usb", ATTRS{idVendor}=="3474", ATTRS{idProduct}=="42b2", MODE="0666"
Reload the rules with
sudo udevadm control --reload-rules && sudo udevadm trigger
Hurrah! Your Linux machine can now control the camera. There's two ways to view it - and easy way and a hard way.
The easy way is to use
https://ferrolho.github.io/thermal-master-viewer/
Open the website
in Chrome
, click the "Connect camera" button, after a moment you should have a view like this:
The harder way is to use dedicated Linux tools like
OpenP3
or
Thermal Camera Viewer
- you may need to hack around with them so they see the device. Usually that's as simple as adding the PID to the code.
You're looking at around
£220 for the camera
and can expect to pay about
£40 for the macro lens
. You can sometimes find them bundled for slightly cheaper.
Readers of this blog get an extra 6% off at
Thermal Master
or
Amazon UK/US
with code
THERMLITE6
.
Unfortunately, that's pretty cheap for a thermal camera. At that price, I'd recommend buying one to share with your local community. If you are a member of a hack-space, these are invaluable for finding hot-spots on your electronics.
The image quality is excellent. There's no bogus "AI" features to hallucinate what it thinks it saw - you just get the raw image. It would be lovely if it presented as a proper webcam on Linux, but there are open source tools to bridge that gap. The detachable macro lens is handy, and the magnet grip is reasonably strong - but I wish it had a strap or something to prevent it getting lost.
There's not a
lot
of difference between Thermal Master's various cameras. If you want to swap between wide shots and macro shots, this is probably as good a device as any.
