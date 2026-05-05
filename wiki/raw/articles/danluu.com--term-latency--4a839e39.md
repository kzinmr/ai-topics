---
title: "Terminal latency"
url: "https://danluu.com/term-latency/"
fetched_at: 2026-05-05T07:01:31.238712+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Terminal latency

Source: https://danluu.com/term-latency/

There’s
a great MSR demo from 2012 that shows the effect of latency on the experience of using a tablet
. If you don’t want to watch the three minute video, they basically created a device which could simulate arbitrary latencies down to a fraction of a millisecond. At 100ms (1/10th of a second), which is typical of consumer tablets, the experience is terrible. At 10ms (1/100th of a second), the latency is noticeable, but the experience is ok, and at < 1ms the experience is great, as good as pen and paper. If you want to see a mini version of this for yourself, you can try a random Android tablet with a stylus vs. the current generation iPad Pro with the Apple stylus. The Apple device has well above 10ms end-to-end latency, but the difference is still quite dramatic -- it’s enough that I’ll actually use the new iPad Pro to take notes or draw diagrams, whereas I find Android tablets unbearable as a pen-and-paper replacement.
You can also see something similar if you try VR headsets with different latencies.
20ms feels fine, 50ms feels laggy, and 150ms feels unbearable
.
Curiously, I rarely hear complaints about keyboard and mouse input being slow. One reason might be that keyboard and mouse input are quick and that inputs are reflected nearly instantaneously, but I don’t think that’s true. People often tell me that’s true, but I think it’s just the opposite. The idea that computers respond quickly to input, so quickly that humans can’t notice the latency, is the most common performance-related fallacy I hear from professional programmers.
When people measure actual end-to-end latency for games on normal computer setups, they usually find latencies in the
100ms
range
.
If we look at
Robert Menzel’s breakdown of the the end-to-end pipeline for a game
, it’s not hard to see why we expect to see 100+ ms of latency:
~2 msec (mouse)
8 msec (average time we wait for the input to be processed by the game)
16.6 (game simulation)
16.6 (rendering code)
16.6 (GPU is rendering the previous frame, current frame is cached)
16.6 (GPU rendering)
8 (average for missing the vsync)
16.6 (frame caching inside of the display)
16.6 (redrawing the frame)
5 (pixel switching)
Note that this assumes a gaming mouse and a pretty decent LCD; it’s common to see substantially slower latency for the mouse and for pixel switching.
It’s possible to tune things to get into the 40ms range, but the vast majority of users don’t do that kind of tuning, and even if they do, that’s still quite far from the 10ms to 20ms range, where tablets and VR start to feel really “right”.
Keypress-to-display measurements are mostly done in games because gamers care more about latency than most people, but I don’t think that most applications are all that different from games in terms of latency. While games often do much more work per frame than “typical” applications, they’re also much better optimized than “typical” applications. Menzel budgets 33ms to the game, half for game logic and half for rendering. How much time do non-game applications take? Pavel Fatin measured this for text editors and found latencies ranging from
a few milliseconds to hundreds of milliseconds
and he did this
with an app he wrote that we can use to measure the latency of other applications
that uses
java.awt.Robot
to generate keypresses and do screen captures.
Personally, I’d like to see the latency of different terminals and shells for a couple of reasons. First, I spend most of my time in a terminal and usually do editing in a terminal, so the latency I see is at least the latency of the terminal. Second, the most common terminal benchmark I see cited (by at least two orders of magnitude) is the rate at which a terminal can display output, often measured by running
cat
on a large file. This is pretty much as useless a benchmark as I can think of. I can’t recall the last task I did which was limited by the speed at which I can
cat
a file to
stdout
on my terminal (well, unless I’m using eshell in emacs), nor can I think of any task for which that sub-measurement is useful. The closest thing that I care about is the speed at which I can
^C
a command when I’ve accidentally output too much to
stdout
, but as we’ll see when we look at actual measurements, a terminal’s ability to absorb a lot of input to
stdout
is only weakly related to its responsiveness to
^C
. The speed at which I can scroll up or down an entire page sounds related, but in actual measurements the two are not highly correlated (e.g., emacs-eshell is quick at scrolling but extremely slow at sinking
stdout
). Another thing I care about is latency, but knowing that a particular terminal has high
stdout
throughput tells me little to nothing about its latency.
Let’s look at some different terminals to see if any terminals add enough latency that we’d expect the difference to be noticeable. If we measure the latency from keypress to internal screen capture on my laptop, we see the following latencies for different terminals
These graphs show the distribution of latencies for each terminal. The y-axis has the latency in milliseconds. The x-axis is the percentile (e.g., 50 means represents 50%-ile keypress i.e., the median keypress). Measurements are with macOS unless otherwise stated. The graph on the left is when the machine is idle, and the graph on the right is under load. If we just look at median latencies, some setups don’t look too bad -- terminal.app and emacs-eshell are at roughly 5ms unloaded, small enough that many people wouldn’t notice. But most terminals (st, alacritty, hyper, and iterm2) are in the range
where you might expect people
to
notice the additional latency
even when the machine is idle. If we look at the tail when the machine is idle, say the 99.9%-ile latency, every terminal gets into the range where the additional latency ought to be perceptible, according to studies on user interaction. For reference, the internally generated keypress to GPU memory trip for some terminals is slower than
the time it takes to send a packet from Boston to Seattle
and back
, about 70ms.
All measurements were done with input only happening on one terminal at a time, with full battery and running off of A/C power. The loaded measurements were done while compiling Rust (as before, with full battery and running off of A/C power, and in order to make the measurements reproducible, each measurement started 15s after a clean build of Rust after downloading all dependencies, with enough time between runs to avoid thermal throttling interference across runs).
If we look at median loaded latencies, other than emacs-term, most terminals don’t do much worse than at idle. But as we look at tail measurements, like 90%-ile or 99.9%-ile measurements, every terminal gets much slower. Switching between macOS and Linux makes some difference, but the difference is different for different terminals.
These measurements aren't anywhere near the worst case (if we run off of battery when the battery is low, and wait 10 minutes into the compile in order to exacerbate thermal throttling, it’s easy to see latencies that are multiple hundreds of ms) but even so, every terminal has tail latency that should be observable. Also, recall that this is only a fraction of the total end-to-end latency.
Why don’t people complain about keyboard-to-display latency the way they complain stylus-to-display latency or VR latency? My theory is that, for both VR and tablets, people have a lot of experience with a much lower latency application. For tablets, the “application” is pen-and-paper, and for VR, the “application” is turning your head without a VR headset on. But input-to-display latency is so bad for every application that most people just expect terrible latency.
An alternate theory might be that keyboard and mouse input are fundamentally different from tablet input in a way that makes latency less noticeable. Even without any data, I’d find that implausible because, when I access a remote terminal in a way that adds tens of milliseconds of extra latency, I find typing to be noticeably laggy. And it turns out that when extra latency is A/B tested,
people can and do notice latency in the range we’re discussing here
.
Just so we can compare the most commonly used benchmark (throughput of stdout) to latency, let’s measure how quickly different terminals can sink input on stdout:
terminal
stdout
(MB/s)
idle50
(ms)
load50
(ms)
idle99.9
(ms)
load99.9
(ms)
mem
(MB)
^C
alacritty
39
31
28
36
56
18
ok
terminal.app
20
6
13
25
30
45
ok
st
14
25
27
63
111
2
ok
alacritty tmux
14
terminal.app tmux
13
iterm2
11
44
45
60
81
24
ok
hyper
11
32
31
49
53
178
fail
emacs-eshell
0.05
5
13
17
32
30
fail
emacs-term
0.03
13
30
28
49
30
ok
The relationship between the rate that a terminal can sink
stdout
and its latency is non-obvious. For the matter, the relationship between the rate at which a terminal can sink
stdout
and how fast it looks is non-obvious. During this test, terminal.app looked very slow. The text that scrolls by jumps a lot, as if the screen is rarely updating. Also, hyper and emacs-term both had problems with this test. Emacs-term can’t really keep up with the output and it takes a few seconds for the display to finish updating after the test is complete (the status bar that shows how many lines have been output appears to be up to date, so it finishes incrementing before the test finishes). Hyper falls further behind and pretty much doesn’t update the screen after a flickering a couple of times. The
Hyper Helper
process gets pegged at 100% CPU for about two minutes and the terminal is totally unresponsive for that entire time.
Alacritty was tested with tmux because alacritty doesn’t support scrolling back up, and the docs indicate that you should use tmux if you want to be able to scroll up. Just to have another reference, terminal.app was also tested with tmux. For most terminals, tmux doesn’t appear to reduce
stdout
speed, but alacritty and terminal.app are fast enough that they’re actually limited by the speed of tmux.
Emacs-eshell is technically not a terminal, but I also tested eshell because it can be used as a terminal alternative for some use cases. Emacs, with both eshell and term, is actually slow enough that I care about the speed at which it can sink
stdout
. When I’ve used eshell or term in the past, I find that I sometimes have to wait for a few thousand lines of text to scroll by if I run a command with verbose logging to
stdout
or
stderr
. Since that happens very rarely, it’s not really a big deal to me unless it’s so slow that I end up waiting half a second or a second when it happens, and no other terminal is slow enough for that to matter.
Conversely, I type individual characters often enough that I’ll notice tail latency. Say I type at 120wpm and that results in 600 characters per minute, or 10 characters per second of input. Then I’d expect to see the 99.9% tail (1 in 1000) every 100 seconds!
Anyway, the
cat
“benchmark” that I care about more is whether or not I can
^C
a process when I’ve accidentally run a command that outputs millions of lines to the screen instead of thousands of lines. For that benchmark, every terminal is fine except for hyper and emacs-eshell, both of which hung for at least ten minutes (I killed each process after ten minutes, rather than waiting for the terminal to catch up).
Memory usage at startup is also included in the table for reference because that's the other measurement I see people benchmark terminals with. While I think that it's a bit absurd that terminals can use 40MB at startup, even the three year old hand-me-down laptop I'm using has 16GB of RAM, so squeezing that 40MB down to 2MB doesn't have any appreciable affect on user experience. Heck, even the $300 chromebook we recently got has 16GB of RAM.
Conclusion
Most terminals have enough latency that the user experience could be improved if the terminals concentrated more on latency and less on other features or other aspects of performance. However, when I search for terminal benchmarks, I find that terminal authors, if they benchmark anything,
benchmark the speed of
sinking stdout
or memory usage at startup. This is unfortunate because most “low performance” terminals can already sink
stdout
many orders of magnitude faster than humans can keep up with, so further optimizing
stdout
throughput has a relatively small impact on actual user experience for most users. Likewise for reducing memory usage when an idle terminal uses 0.01% of the memory on my old and now quite low-end laptop.
If you work on a terminal, perhaps consider relatively more latency and interactivity (e.g., responsiveness to
^C
) optimization and relatively less throughput and idle memory usage optimization.
Update: In response to this post,
the author of alacritty explains where alacritty's latency comes from and describes how alacritty could reduce its latency
Appendix: negative results
Tmux and latency: I tried tmux and various terminals and found that the the differences were within the range of measurement noise.
Shells and latency: I tried a number of shells and found that, even in the quickest terminal, the difference between shells was within the range of measurement noise. Powershell was somewhat problematic to test with the setup I was using because it doesn’t handle colors correctly (the first character typed shows up with the color specified by the terminal, but other characters are yellow regardless of setting,
which appears to be an open issue
), which confused the image recognition setup I used.
Powershell also doesn’t consistently put the cursor where it should be
-- it jumps around randomly within a line, which also confused the image recognition setup I used. However, despite its other problems, powershell had comparable performance to other shells.
Shells and stdout throughput: As above, the speed difference between different shells was within the range of measurement noise.
Single-line vs. multiline text and throughput: Although some text editors bog down with extremely long lines, throughput was similar when I shoved a large file into a terminal whether the file was all one line or was line broken every 80 characters.
Head of line blocking / coordinated omission: I ran these tests with input at a rate of 10.3 characters per second. But it turns out this doesn't matter much and input rates that humans are capapable of and the latencies are quite similar to doing input once every 10.3 seconds. It's possible to overwhelm a terminal, and hyper is the first to start falling over at high input rates, but the speed necessary to make the tail latency worse is beyond the rate at which any human I know of can type.
Appendix: experimental setup
All tests were done on a dual core 2.6GHz 13” Mid-2014 Macbook pro. The machine has 16GB of RAM and a 2560x1600 screen. The OS X version was 10.12.5. Some tests were done in Linux (Lubuntu 16.04) to get a comparison between macOS and Linux. 10k keypresses were for each latency measurements.
Latency measurements were done with the
.
key and throughput was done with default
base32
output, which is all plain ASCII text. George King notes that different kinds of text can change output speed:
I’ve noticed that Terminal.app slows dramatically when outputting non-latin unicode ranges. I’m aware of three things that might cause this: having to load different font pages, and having to parse code points outside of the BMP, and wide characters.
The first probably boils down to a very complicated mix of lazy loading of font glyphs, font fallback calculations, and caching of the glyph pages or however that works.
The second is a bit speculative, but I would bet that Terminal.app uses Cocoa’s UTF16-based NSString, which almost certainly hits a slow path when code points are above the BMP due to surrogate pairs.
Terminals were fullscreened before running tests. This affects test results, and resizing the terminal windows can and does significantly change performance (e.g., it’s possible to get hyper to be slower than iterm2 by changing the window size while holding everything else constant). st on macOS was running as an X client under XQuartz. To see if XQuartz is inherently slow, I tried
runes
, another "native" Linux terminal that uses XQuartz; runes had much better tail latency than st and iterm2.
The “idle” latency tests were done on a freshly rebooted machine. All terminals were running, but input was only fed to one terminal at a time.
The “loaded” latency tests were done with rust compiling in the background, 15s after the compilation started.
Terminal bandwidth tests were done by creating a large, pseudo-random, text file with
timeout 64 sh -c 'cat /dev/urandom | base32 > junk.txt'
and then running
timeout 8 sh -c 'cat junk.txt | tee junk.term_name'
Terminator and urxvt weren’t tested because they weren’t completely trivial to install on mac and I didn’t want to futz around to make them work. Terminator was easy to build from source, but it hung on startup and didn’t get to a shell prompt. Urxvt installed through brew, but one of its dependencies (also installed through brew) was the wrong version, which prevented it from starting.
Thanks to Kamal Marhubi, Leah Hanson, Wesley Aptekar-Cassels, David Albert, Vaibhav Sagar, Indradhanush Gupta, Rudi Chen, Laura Lindzey, Ahmad Jarara, George King, Tim Dierks, Nikith Naide, Veit Heller, and Nick Bergson-Shilcock for comments/corrections/discussion.
