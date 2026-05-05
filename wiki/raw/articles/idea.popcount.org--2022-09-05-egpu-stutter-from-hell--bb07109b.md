---
title: "eGPU stutter from hell"
url: "https://idea.popcount.org/2022-09-05-egpu-stutter-from-hell"
fetched_at: 2026-05-05T07:01:05.773563+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# eGPU stutter from hell

Source: https://idea.popcount.org/2022-09-05-egpu-stutter-from-hell

eGPU stutter from hell
05 September 2022
I was able to put my hands on an HTC Vive VR headset. Sadly, my
computers don't have a strong enough GPU for VR.
Since I only have laptops I decided to secure an eGPU (external GPU) -
a box with PCIe bus, connected over thunderbolt, which can house a
proper big graphics card. I got
Razer Core X
. Together
with the laptop, the setup looks like this:
Laptop with Razer Core X eGPU - connected with thunderbolt
And the Vive Headset like that - not that you haven't seen one before:
Good old HTC Vive headset
I stuffed an Nvidia 3080 into the eGPU, launched Windows and expected
to kill some aliens, zombies, drones, or at least slash red and blue
boxes.
Sadly, while Nvidia 3080 in the eGPU was working just fine, the games
were unplayable due to stutter. Every now and then the headset would
just freeze for a good fraction of a second. In VR this kind of
rendering issue is unacceptable.
There isn't a good way to visualize this, having frozen image when
moving the head is nauseous, confusing and frankly dangerous. Here's a
Steam VR "Frame Timing" chart. All the spikes in the bottom chart
indicate trouble - frames not being delivered on time. As you can see
this stutter causes a large number subsequent of frames to be
delayed. Note that it looks somewhat regular.
Stutter on Frame Timing from Steam VR
I'll save you the grueling debugging story. You have to believe me it
took me a lot of effort to understand the issue.
The issue, as far as I understand it, is rooted in a technology called
"Nvidia Optimus". You see, modern laptops sometimes have two graphics
cards. The power-efficient integrated GPU (iGPU) - like Intel UHD, and
performance discrete graphics (dGPU) - Nvidia Quadro in my case.
Windows wants to utilize appropriate GPU depending on many
circumstances. For example, when on battery, using iGPU might be
preferred. When rendering harder graphics, dGPU might be a better
choice. It's a constant performance vs power struggle. Nvidia optimus
is a marketing name for a piece of software that inspects the system
and decides on whether dGPU should be powered off.
Things change when eGPU is connected - in my case it was also Nvidia,
which can be a contributing factor. In such case, the embedded
discrete GPU is not used - rightfully so. All complex graphics is
rendered on eGPU. However, Nvidia Optimus keeps on running and checking
on the dGPU.
My understanding is: Nvidia Optimus polls graphics cards, and this
regular polling causes the stutter. It seems to interfere with smooth
eGPU rendering. Maybe there is a shared mutex somewhere in NVidia
driver.
I don't know how to disable Nvidia Optimus, but I'm aware of three
ways to work around the stuttering problem.
Solution 1 - render on dGPU
The whole idea is to do something with the dGPU in order to keep it
from idling. No idle dGPU - no stutter on eGPU. One way is to:
disconnect eGPU (there is a software "disconnect GPU" button in nvidia panel)
run something that requires dGPU
connect eGPU
observe that the workload remains on dGPU and it remains active
For example
this page contains some random Directx tutorial
. Look
for "tutorial1.exe" file.
Once started, tutorial1.exe keeps on running on dGPU
After enabling eGPU, the workload remains on the dGPU as can be seen
in Task Manager:
Task manager shows dGPU being used
If the dGPU (Nvidia Quadro in my case) is using more than 0%, the
stutter won't occur.
For completeness, in past it was possible to run OpenGL on specific
GPU. For example
tutorials from here
could be "Rendered on"
like this:
OpenGL "render on" used to work
Sadly, this stopped working for me. Even with dGPU chosen from this
menu, it doesn't seem to work and the Task Manager shows iGPU being
used. Oh well.
Solution 2 - keep dGPU busy
It's possible to keep dGPU busy with other tricks. For example, on
certain laptops, external HDMI / DisplayPort ports are connected to
dGPU. That means, with external display present, the dGPU
must
be
engaged, which can keep Nvidia Optimus from causing the stutter. If
connecting display is not sufficient, than moving GPU-heavy workload
- like a browser - to secondary screen might do the job.
Finally, there is a tool called
TrayPwrD3
, which is doing
exactly that. Sadly, it's not supporting the case of three GPUs -
iGPU, dGPU and eGPU, but maybe this can be added in the future.
Solution 3 - disable dGPU
Finally, there is a hardcore option - just disable dGPU in Device
Manager.
Disable dGPU in device manager
I
think
I tried this without success in past, but hey: it totally
works as of September 2022.
Stutter fixed
I'm using the "solution 3" most often. With it, the stutter problem
went away:
Fixed frame Timing from Steam VR
If you look carefully at the bottom chart, you might notice a single
delayed/dropped frame once in a while. While I'm not too scientific
about this, disabling dynamicticks seem to have fixed that minor issue
for me. Run cmd as Administrator:
bcdedit
/
set
disabledynamictick
yes
Ther was one more thing.
Once I had a case of a subpar quality HDMI cable, which resulted
totally terrible flicker. Here's how it looked:
Your browser does not support the video tag.
Flicker caused by bad HDMI cable
It took me a while to debug it. On first glance it looked like a
software problem - the image seemed half-rendered, with some white
noise patches. Anyhow, replacing the HDMI cable fixed it.
