---
title: "Altera Quartus Linux jtagd bug fixes"
url: "https://www.downtowndougbrown.com/2026/10/altera-quartus-linux-jtagd-bug-fixes/"
fetched_at: 2026-10-03T10:01:01.536706+00:00
source: "downtowndougbrown.com"
tags: [blog, raw]
---

# Altera Quartus Linux jtagd bug fixes

Source: https://www.downtowndougbrown.com/2026/10/altera-quartus-linux-jtagd-bug-fixes/

I went kind of overboard
looking into issues with Altera USB Blaster clones a couple of years ago
. While writing that post, I ran into some really frustrating intermittent problems in Linux with jtagd that I was never able to figure out:
I also experienced a really weird unrelated problem in Quartus Programmer 18.1 in Linux while I was testing things on one of my computers. I could see corrupted outgoing USB traffic in my Wireshark capture — before the FT245 or CPLD were even involved in the equation. This problem affected all of my blasters, not just the CPLD+FT245 ones.
I still sometimes notice a long (~30 second) delay the first time I try to do a JTAG operation in Linux after plugging in any of my CPLD-based USB Blasters. It doesn’t happen every time, but when it does, it seems like jtagd is hung up waiting to receive a byte, which never happens, so it times out and tries again. It works fine after that.
Since I was already exhausted from dealing with all of the other USB Blaster problems at the time, I completely lost interest in digging further into these particular nagging issues, so I left them alone. Until now. AI has opened up the ability for some of these little mysteries to be closed out without having to spend a bunch of time investigating them. Believe me, debugging can be an exciting challenge, but intermittent issues are just not fun to diagnose at all.
I fed both of these problems into Claude Opus 5.5. It happily jumped into reverse-engineering jtagd and easily identified both problems. At one point during its investigation and testing of the first bug, it started running into cyber guardrails, but I’ve noticed Opus 5.5 is a little better than past versions about trying a slightly different approach when a guardrail is hit, and even giving me a chance to reword my prompt instead of just immediately knocking me down to Opus 4.8 (and then potentially ending the session when Opus 4.8 hits a similar safeguard). That’s a very welcome improvement.
Anyway, I thought I’d quickly share the final discoveries, along with a link to a tool you can use to patch your jtagd if these bugs have been driving you crazy. First, here’s the link to the patch tool:
https://github.com/dougg3/altera-jtagd-linux-fixes
The first bug that causes corruption in the USB traffic ended up being an uninitialized variable in the constructor for
JTAG_SERVER_USB_BLASTER
. The constructor sets a bunch of nearby variables to zero, but this one variable must have been accidentally forgotten. If its value happens to be greater than 0, some extra data intended only for Altera’s newer USB-Blaster II gets inserted into the outgoing USB data, which confuses older USB Blasters. This perfectly explains the data corruption I referred to in my earlier post. Unlike the LLM, I didn’t have enough background info in my head to make the connection that the “corrupt data” was for the newer USB Blaster protocol. All of the clone devices that I’ve seen speak the original USB Blaster protocol, so they’re all affected. They end up with a 30-second hang followed by an
Unable to read device chain - JTAG chain broken
error.
It seems to only happen if you unplug and replug the blaster while leaving jtagd running, because the first allocation tends to always be zeroed out. Each hotplug results in a new
JTAG_SERVER_USB_BLASTER
object being created, and parts of the heap end up being reused. A lot of my original work back in 2024 involved a Windows VM, so it makes sense that I was probably hotplugging the device a lot. Maybe it’s not something a lot of people run into, but it was really freaking annoying.
The second bug with the 30-second delay is a bit more subtle. It seems to depend on what type of FTDI FT245 series chip your blaster uses, and maybe even how it’s connected to your computer. The crux of the problem is that when it first opens the chip, jtagd sends the following commands to the FT245, in order:
Reset
Purge TX
Purge RX
Set Latency Timer
This particular sequence of commands appears to cause some clone devices to ignore incoming data for about 250 ms. This wouldn’t ordinarily be much of a problem, except jtagd immediately starts talking to it to figure out the connected JTAG chain, and then gets stuck waiting 30 seconds for a response. I have different blaster clones that each respond in their own different ways to this command sequence (some are affected, and some are not), but these are just FT245 commands. Maybe different clones have different chip revisions? All I know is: changing this sequence so that Set Latency Timer comes first completely eliminates the problem.
Both of these issues have been in jtagd at least as far back as Quartus 18.1, and are still there as of Quartus 25.1. Altera, if you see this post, please consider fixing at least the first bug! I’m honestly not sure if the second one is actually a “bug” or if it’s just that certain clone devices have chips that don’t act exactly like the official device, but a 300 ms delay after Set Latency Timer would probably fix it too.
With fixes for these two problems applied, all of the USB Blaster clones I have access to work great now (after my previous firmware/CPLD fixes are also applied, of course). I even used a USB hub compatible with
uhubctl
to automate cycling power to all of the clone devices I have. That enabled me to create a feedback loop to do a bunch of stress testing to really verify that the fix actually works.
In reflection, I totally could (and should) have figured out the first bug on my own. It seems like valgrind would have just handed it to me on a silver platter. I’m kind of disappointed in myself for not thinking to try that. At the time, I was deep into an investigation with
rr
while trying to reproduce the bug, but it wasn’t compatible with my main development machine. When I got Quartus installed onto an older computer that
was
compatible with rr, I couldn’t replicate the issue anymore. I was sick of dealing with it all at that point, so I gave up. In my defense, this bug has been in jtagd for at least 8 years, and has mostly gone unnoticed, except for
this little post on Altera’s forums where someone realized something funky was going on
and was pretty much ignored.
My blog isn’t turning entirely into a “hey, look at what AI did for me” showcase. What I’m trying to do is share a useful workaround with the community and hopefully raise awareness for Altera to fix their long-standing bug. Also, maybe I’m just crazy, but it’s kind of fun fixing annoying bugs in closed-source software with AI. Especially when it’s an old loose end from the past that I thought was impractical to tie up. With that in mind, there actually is going to be a follow-up to this post where I resolve one final unanswered question from my past USB Blaster investigations.
