---
title: "FreeBSD vs. SmartOS: Who's Faster for Jails, Zones, and bhyve VMs?"
url: "https://it-notes.dragas.net/2025/09/19/freebsd-vs-smartos-whos-faster-for-jails-zones-bhyve/"
fetched_at: 2026-04-28T07:02:49.783432+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# FreeBSD vs. SmartOS: Who's Faster for Jails, Zones, and bhyve VMs?

Source: https://it-notes.dragas.net/2025/09/19/freebsd-vs-smartos-whos-faster-for-jails-zones-bhyve/

Disclaimer
These benchmarks were performed on my specific hardware and tuned for the workloads I expect to run.
They should not be taken as absolute or universally applicable results.
Different CPUs, storage, networking setups, or workload profiles could produce very different outcomes.
What I’m sharing here is a faithful snapshot of
my
test environment and use case - a guidepost, not a final verdict.
Years ago, I installed a PCEngines APU at a client's site. It dutifully ran Proxmox with a few small VMs inside. It wasn't a speed demon, but it got the job done. Tasked with running in a closed, uncooled, and unsupervised server closet, it soldiered on for about seven years.
Then, while I was at BSDCan, I got the call. A series of power outages and surges had finally taken their toll, and the APU was dead. It was probably just the power supply, but given its age, we decided it was time for a replacement. I set up a remote bypass to keep them running, but I knew I'd need to install something more powerful soon.
I ordered a modern MiniPC-based on the low-power Intel Processor N150 platform, but with 16GB of RAM and more than enough performance to serve as a decent workstation. I have a similar one in my office running openSUSE Tumbleweed, and it works beautifully.
This time, however, I decided to replace Proxmox with a different virtualization system. This decision wasn't made in a vacuum. In the past, I've put bhyve head-to-head with Proxmox, and my findings were clear:
bhyve on FreeBSD is an extremely efficient hypervisor,
often outperforming KVM on Proxmox in my tests
.
This positive experience is what made FreeBSD with bhyve a top contender. The other path was a KVM-style approach (which would require fewer changes to the VMs), where my options would be NetBSD or an
illumos-based
OS like
SmartOS
. Since I had the new hardware on hand, I decided to run some tests to see how these different technologies stacked up against each other, and against the bare metal itself.
The Lineup: What I Put on the Test Bench
My goal was to test every reasonable option on this Intel N150 hardware. The final lineup covered the entire spectrum:
The Baseline:
FreeBSD 14.3-RELEASE Bare Metal:
The ground truth for performance on this hardware.
OS-Level Virtualization (Containers):
SmartOS Native Zone:
The baseline native container on SmartOS.
SmartOS LX Zone:
Running
Ubuntu 24.04
and
Alpine Linux
.
FreeBSD Native Jail:
The baseline native container on FreeBSD.
FreeBSD Jail with Linux:
A jail running a
Ubuntu 22.04
userland.
Full Hardware Virtualization (HVM):
SmartOS bhyve Zone:
A FreeBSD guest inside the bhyve hypervisor on a SmartOS host.
SmartOS KVM Zone:
A FreeBSD guest inside the KVM hypervisor on a SmartOS host.
FreeBSD bhyve VM:
A FreeBSD guest inside the bhyve hypervisor on a FreeBSD host.
The Benchmark: My
sysbench
Commands
To keep the comparison fair and simple, I used two core
sysbench
commands. To ensure consistency, I even compiled
sysbench
from scratch on the SmartOS native zone to match the versions and compile options on the other systems as closely as possible.
The commands I used in each environment were:
For CPU performance:
sysbench --test=cpu --cpu-max-prime=20000 run
For memory performance:
sysbench --test=memory run
First Look: CPU and Memory on the Intel N150
My initial tests on the Intel N150 hardware immediately revealed some interesting trends. The
sysbench
CPU results from any native FreeBSD environment (bare metal or jail) were on a completely different scale from the Linux and SmartOS guests, making a direct comparison meaningless.
However, by excluding the incompatible FreeBSD-native results, we get a very clear picture of the overhead between the various container technologies.
Valid CPU Performance Comparison (Single Thread, Intel N150)
Host OS
Container Tech
Guest OS
CPU Performance (Events/sec)
FreeBSD
Jail (OS-level)
Ubuntu 22.04
1108.18
SmartOS
LX Zone (OS-level)
Ubuntu 24.04
1107.13
SmartOS
Native Zone (OS-level)
SmartOS
1107.04
SmartOS
LX Zone (OS-level)
Alpine Linux
1022.81
The takeaway here was clear: for CPU work, the overhead from these containers is basically a rounding error. For CPU-bound tasks, neither SmartOS Zones nor FreeBSD Jails will be a bottleneck.
The memory results, which were consistent across all platforms, were far more revealing.
Overall Memory Performance Comparison (Intel Processor N150)
Host OS
Virtualization Tech
Guest OS
Memory Performance (Transfer Rate)
SmartOS
LX Zone (OS-level)
Ubuntu 24.04
4970.54 MiB/sec
SmartOS
Native Zone (OS-level)
SmartOS (Native)
4549.97 MiB/sec
FreeBSD
Jail (OS-level)
Ubuntu 22.04
4348.32 MiB/sec
FreeBSD
Bare Metal
FreeBSD (Native)
4005.08 MiB/sec
FreeBSD
Native Jail (OS-level)
FreeBSD (Native)
3990.13 MiB/sec
SmartOS
LX Zone (OS-level)
Alpine Linux
3803.72 MiB/sec
FreeBSD
bhyve VM (Full HVM)
FreeBSD
3636.01 MiB/sec
SmartOS
bhyve Zone (Full HVM)
FreeBSD
3020.15 MiB/sec
SmartOS
KVM Zone (Full HVM)
FreeBSD
205.18 MiB/sec
These initial numbers led to a few conclusions: a virtual layer could be a performance boost, the userland matters, and bhyve clearly outclassed the legacy KVM on SmartOS. However, one result was nagging at me: the performance gap between FreeBSD bare metal (
4005.08 MiB/sec
) and a native bhyve VM (
3636.01 MiB/sec
) was about 9%. This was a larger drop than I expected. It prompted a new question: was this overhead inherent to bhyve, or was it a quirk of the new N150 hardware?
Going deeper: Testing on an Intel i7-7500U
To see if more mature, better-supported hardware would tell a different story, I replicated the FreeBSD tests on an older Qotom Mini-PC powered by an Intel i7-7500U. The results were illuminating and dramatically changed the narrative.
CPU Performance Comparison (Intel i7-7500U)
Once again, the CPU tests produced strange results. The native FreeBSD environments all reported incredibly high numbers in the millions of events/sec, while the Ubuntu Linuxulator jail's result was on a completely different, incompatible scale. Frankly, given the massive discrepancy between FreeBSD-native and Linux-based environments, I'm unsure that the
sysbench
CPU figures can be considered totally reliable in absolute terms.
However, what
is
useful is comparing the native FreeBSD results against each other. This tells us about relative overhead.
Platform
CPU Performance (Events/sec)
Overhead vs. Bare Metal
FreeBSD Bare Metal
6,377,778
Baseline
FreeBSD Native Jail
6,379,271
~0.0%
FreeBSD bhyve VM
6,346,852
-0.48%
Even if we're skeptical of the absolute numbers, the relative comparison is crystal clear: the CPU overhead of bhyve is
less than half a percent
. This is the key takeaway.
Memory Performance Comparison (Intel i7-7500U)
The memory benchmarks, in contrast, were consistent and highly informative.
Platform
Memory Performance (Transfer Rate)
Overhead vs. Bare Metal
Ubuntu 22.04 Jail
4856.23 MiB/sec
+7.55%
FreeBSD Native Jail
4517.73 MiB/sec
+0.05%
FreeBSD Bare Metal
4515.24 MiB/sec
Baseline
FreeBSD bhyve VM
4491.60 MiB/sec
-0.52%
This is where the real story is. The memory performance of a bhyve VM was a mere
0.52%
slower than bare metal. This is the kind of near-native performance one hopes for from a top-tier hypervisor and stands in stark contrast to the 9% drop seen on the newer N150.
Breaking Down the Results: What I Learned From Both Tests
This comprehensive two-platform analysis paints a much clearer picture.
1. Hardware
Really
Matters
Performance is not an absolute. The difference between the two platforms was stark: on the mature i7-7500U, bhyve’s overhead was less than 1%, while on the newer, budget N150, it was a more significant 9%. This suggests the performance dip is likely due to missing optimizations for that specific CPU architecture, rather than a fundamental flaw in bhyve itself.
2. bhyve's True Potential is Near-Native Speed
The i7 tests prove that
bhyve is an exceptionally efficient hypervisor
on well-supported hardware. The relative CPU overhead was a negligible -0.48%, and more importantly, the reliable memory benchmarks showed a performance drop of just 0.52% compared to bare metal. This is the gold standard for virtualization.
3. FreeBSD Jails are Feather-Light
On both platforms, native FreeBSD jails demonstrated almost zero performance overhead. On the i7, both CPU and memory performance were virtually identical to bare metal (a 0.05% difference). The N150 CPU tests further showed that FreeBSD's container implementation is so efficient that running a Linux userland inside a jail delivered the best CPU scores of the entire lineup.
4. SmartOS Zones Are Also Extremely Efficient
Just like Jails, SmartOS's native Zones proved to be remarkably lightweight. The N150 CPU tests confirm this, showing that native and LX zones have virtually identical, top-tier performance. On the memory front, the native Zone delivered performance over 13%
faster
than the FreeBSD bare-metal baseline, pointing to the high efficiency of the illumos kernel.
5. The Linux Userland Excels at Throughput
A clear pattern emerged on both testbeds: the Ubuntu userland consistently delivered excellent benchmark results. On the CPU front, Ubuntu on both FreeBSD and SmartOS delivered the highest, and nearly identical, performance scores on the N150. For memory, the story was even more dramatic: the Ubuntu LX Zone on SmartOS was the top performer, beating bare-metal FreeBSD by nearly 25%, while the Ubuntu jail on the i7 also surpassed its host by over 7%.
Final Thoughts: The Verdict for My Client's New Server
So, what's the bottom line for my client's new MiniPC? This benchmarking journey has made the path forward much clearer.
At the beginning of this process, my main question was whether to stick with a KVM-based setup or make the switch to bhyve. The performance data answers that decisively. The legacy KVM on SmartOS showed a crippling performance penalty, making it a non-starter. Given that, the extra effort to migrate the existing VMs to a bhyve-compatible format is absolutely worth it. The performance gain is just too significant to ignore.
The final question, then, is
which
host OS to use for bhyve: SmartOS or FreeBSD? This is a much tougher call, as both platforms demonstrated incredible strengths.
SmartOS
, powered by the illumos kernel, was a true surprise. It delivered astonishing performance on the target N150 hardware. Its key advantage is the raw speed of its containerization for both CPU and memory tasks. The Ubuntu LX Zone not only ran flawlessly but delivered top-tier CPU scores and outperformed the bare-metal FreeBSD baseline in memory by a massive 25% margin. This points to a highly efficient kernel and offers the tantalizing prospect of running ultra-fast Linux containers alongside performant bhyve VMs on the same host.
On the other hand,
FreeBSD
proved its mastery of bhyve virtualization. The tests on the i7 hardware showed its implementation to be the gold standard, offering virtually zero performance overhead for full hardware virtualization. Its native Jails are equally efficient, and its Linux compatibility layer is so effective that an Ubuntu jail delivered the
fastest CPU performance
of all containers tested on FreeBSD. For workloads that
must
live in a full VM, FreeBSD offers the most performant and native bhyve experience, with the reasonable expectation that its support for newer hardware like the N150 will only improve over time.
Ultimately, the choice comes down to the primary workload. It's a decision between the raw container speed and Linux flexibility of SmartOS versus the pure, uncompromising HVM performance of FreeBSD.
But one thing is certain: thanks to this deep dive, the path forward is much clearer, and it's paved by bhyve.
