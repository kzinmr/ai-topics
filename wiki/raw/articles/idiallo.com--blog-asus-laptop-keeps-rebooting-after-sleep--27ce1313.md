---
title: "Why My Asus Laptop Kept Rebooting After Sleep and How to Fix it"
url: "https://idiallo.com/blog/asus-laptop-keeps-rebooting-after-sleep"
fetched_at: 2026-10-04T10:01:14.930440+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# Why My Asus Laptop Kept Rebooting After Sleep and How to Fix it

Source: https://idiallo.com/blog/asus-laptop-keeps-rebooting-after-sleep

Three years ago, I bought an Asus laptop, specifically the Zenbook Pro 17. It's a powerful machine and works just fine for my needs, but it had one problem that made me want to either return it or throw it out the window.
I would work on projects for hours on end and close the lid when I was done. I haven't manually shut down a computer in more than 10 years. I only do so after a forced update or during a debugging session. So I would close the lid, and a couple of hours later I would open it back up. Instead of waking from sleep, the computer would start from scratch as if it had been turned off and the battery was nearly dead.
That meant everything I had open was closed. I'm lucky that most of the applications I run can restore a previous session, but it was extremely annoying. I had a similar issue with my previous Asus, and I had blamed Windows for it. The computer often woke from sleep just so Microsoft could perform an update, which used up all my battery. Sometimes I would open my backpack to find a dead laptop that was warm to the touch.
I've written this blog post at least five times. Each time I thought I had solved the issue, but then it came back. This time, though, I think I have finally resolved it.
So if you have an Asus laptop running Windows and you experience this very annoying issue, you are not alone. In my case, the culprit was the Wi-Fi adapter, specifically the MediaTek Wi-Fi 6E MT7922.
The Solution
On Windows:
Open
Device Manager
.
Expand
Network adapters
.
Right-click the MediaTek device and click
Properties
.
Click the
Advanced
tab.
In the
Property
box, select
Power Saving
.
In the
Value
field, select
Disabled
.
That's it. After three years of annoying restarts, this finally solved my problem. Now let me explain what was going on.
What Was Happening (based on Windows Event Viewer)
When the laptop lid is closed, Windows initiates "Modern Standby." In this state, the screen turns off to save power, but the system remains partially active to maintain background network connectivity.
Shortly after, Windows attempts to transition into a deeper low-power state and disconnects the network adapter to conserve battery. However, the MediaTek Wi-Fi driver (
mtkwlex
) fails to handle this low-power transition properly. About a minute later, it generates Event ID 1033 errors referencing a network device path (specifically
\Device\NDMP3
in my logs).
Because the driver's error message resource is missing or corrupted, Windows Event Viewer cannot interpret the error and displays a generic warning instead:
"The description for Event ID 1033 from source mtkwlex cannot be found. Either the component that raises this event is not installed on your local computer or the installation is corrupted..."
Because the Wi-Fi driver fails to sleep, it keeps the system partially awake. This causes abnormal background battery drain and heat buildup, which is exacerbated when the laptop is in an enclosed space like a bag.
In response to this abnormal drain, Windows triggers
Event 507: "Austerity Battery Drain Budget Exceeded."
It's important to note that this event is Windows
intentionally waking the laptop up
to prevent the battery from dying completely. However, because the Wi-Fi driver is already in a crashed or unstable kernel state, the system fails to recover from this forced wake-up. The result is a silent system crash or thermal shutdown, followed by
Event 12 ("The operating system started")
, which confirms the laptop rebooted.
The Result
With the fix in place, the Wi-Fi device no longer attempts to enter its power-saving sleep mode, so it never crashes. The ultimate solution would be a fixed MT7922 driver, but try as I might, I haven't been able to find one online.
It's been three weeks so far, and I've been able to resume my work without coming back to a crashed computer. I hope this helps someone else.
