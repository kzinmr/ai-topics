---
title: "AWS EC2 Hardware Trends: 2015-2021"
url: "https://databasearchitects.blogspot.com/2021/07/aws-ec2-hardware-trends-2015-2021.html"
fetched_at: 2026-05-05T07:01:28.654035+00:00
source: "Database Architects"
tags: [blog, raw]
---

# AWS EC2 Hardware Trends: 2015-2021

Source: https://databasearchitects.blogspot.com/2021/07/aws-ec2-hardware-trends-2015-2021.html

Over the past decade, AWS EC2 has introduced many new instance types with different hardware configurations and prices. This hardware zoo can make it hard to keep track of what is available. In this post we will look at how the EC2 hardware landscape changed since 2015. This will hopefully help picking the best option for a given task.
In the cloud, one can trade money for hardware resources. It therefore makes sense to take an economical perspective and normalize the hardware resource by the instance price. For example, instead of looking at absolute network bandwidth, we will use network bandwidth per dollar. Such metrics also allow us to ignore virtualized slices, reducing the number of instances relevant for the analysis from hundreds to dozens. For example, c5n.9xlarge is a virtualized slice of c5n.18xlarge with half the network bandwidth and half the cost.
Data Set
We use historical data from
https://instances.vantage.sh/
and only consider current-generation Intel machines without GPUs. All prices are for us-east-1 Linux instances. Using these constraints, in July 2021 we can pick from the following instances:
name
vCPU
memory [GB]
network [Gbit/s]
storage
price [$/h]
m4.16x
64
256
25
3.20
h1.16x
64
256
25
8x2TB disk
3.74
c5n.18x
72
192
100
3.89
d3.8x
32
256
25
24x2TB disk
4.00
c5.24x
96
192
25
4.08
r4.16x
64
488
25
4.26
m5.24x
96
384
25
4.61
c5d.24x
96
192
25
4x0.9TB NVMe
4.61
i3.16x
64
488
25
8x1.9TB NVMe
5.00
m5d.24x
96
384
25
4x0.9TB NVMe
5.42
d2.8x
36
244
10
24x2TB disk
5.52
m5n.24x
96
384
100
5.71
r5.24x
96
768
25
6.05
d3en.12x
48
192
75
24x14TB disk
6.31
m5dn.24x
96
384
100
4x0.9TB NVMe
6.52
r5d.24x
96
768
25
4x0.9TB NVMe
6.91
r5n.24x
96
768
100
7.15
r5b.24x
96
768
25
7.15
r5dn.24x
96
768
100
4x0.9TB NVMe
8.02
i3en.24x
96
768
100
8x7.5TB NVMe
10.85
x1e.32x
128
3904
25
2x1.9TB SATA
26.69
Compute
Using our six-year data set, let's first look at the cost of compute:
It is quite remarkable that from 2015 to 2021, the cost of compute barely changed. During that six-year time frame, the number of server CPU cores has been growing significantly, which may imply that Intel compute power is currently overpriced in EC2. In the last couple of years EC2 has introduced cheaper AMD and ARM instances, but it's still surprising that AWS chose to keep Intel CPU prices fixed.
DRAM Capacity
For DRAM, the picture is also quite stagnant:
The introduction of the x1e instances improved the situation a bit, but there's been a stagnation since 2018. However, this is less surprising than the CPU situation because DRAM commodity prices in general did not move much.
Instance Storage
Let's next look at instance storage. EC2 offers instances with disks (about 0.2GB/s bandwidth), SATA SSDs (about 0.5GB/s bandwidth), and NVMe SSDs (about 2GB/s bandwidth). The introduction of instances with up to 8 NVMe SSDs in 2017 clearly disrupted IO bandwidth speed (the y-axis unit may look weird for bandwidth but is correct once we normalize by hourly cost):
In terms of capacity per dollar, disk is still king and the d3en instance (
introduced in December 2020
) totally changed the game:
Network Bandwidth
For network bandwidth, we see another major disruption, this time the introduction of 100GBit network instances:
The c5n instance, in particular, is clearly a game changer. It is only marginally more expensive than c5, but its network speed is 4 times faster.
Conclusions
These results show that the hardware landscape is very fluid and regularly we see major changes like the introduction of NVMe SSDs or 100 GBit networking. Truisms like "in distributed systems network bandwidth is the bottleneck" can become false! (Network latency is of course a different beast.) High-performance systems must therefore take hardware trends into account and adapt to the ever-evolving hardware landscape.
