---
title: "SSDs Have Become Ridiculously Fast, Except in the Cloud"
url: "https://databasearchitects.blogspot.com/2024/02/ssds-have-become-ridiculously-fast.html"
fetched_at: 2026-05-05T07:01:28.508208+00:00
source: "Database Architects"
tags: [blog, raw]
---

# SSDs Have Become Ridiculously Fast, Except in the Cloud

Source: https://databasearchitects.blogspot.com/2024/02/ssds-have-become-ridiculously-fast.html

In recent years, flash-based SSDs have largely replaced disks for most storage use cases. Internally, each SSD consists of many independent flash chips, each of which can be accessed in parallel. Assuming the SSD controller keeps up, the throughput of an SSD therefore primarily depends on the interface speed to the host. In the past six years, we have seen a rapid transition from SATA to PCIe 3.0 to PCIe 4.0 to PCIe 5.0. As a result, there was an explosion in SSD throughput:
At the same time, we saw not just better performance, but also more capacity per dollar:
The two plots illustrate the power of a commodity market. The combination of open standards (NVMe and PCIe), huge demand, and competing vendors led to great benefits for customers. Today, top PCIe 5.0 data center SSDs such as the
Kioxia CM7-R
or
Samsung PM1743
achieve up to 13 GB/s read throughput and 2.7M+ random read IOPS. Modern servers have around 100 PCIe lanes, making it possible to have a dozen of SSDs (each usually using 4 lanes) in a single server at full bandwidth. For example, in our lab we have a single-socket Zen 4 server with 8 Kioxia CM7-R SSDs, which achieves 100GB/s (!) I/O bandwidth:
AWS EC2 was an early NVMe pioneer, launching the
i3 instance
with 8 physically-attached NVMe SSDs in early 2017. At that time, NVMe SSDs were still expensive, and having 8 in a single server was quite remarkable. The per-SSD read (2 GB/s) and write (1 GB/s) performance was considered state of the art as well. Another step forward occurred in 2019 with the launch of
i3en instances
, which doubled storage capacity per dollar.
Since then, several NVMe instance types, including i4i and im4gn, have been launched. Surprisingly, however, the performance has not increased; seven years after the i3 launch, we are still stuck with 2 GB/s per SSD. Indeed, the venerable i3 and i3en instances basically remain the best EC2 has to offer in terms of IO-bandwidth/$ and SSD-capacity/$, respectively. Personally, I find this very surprising given the SSD bandwidth explosion and cost reductions we have seen on the commodity market. At this point, the performance gap between state-of-the-art SSDs and those offered by major cloud vendors, especially in read throughput, write throughput, and IOPS, is nearing an order of magnitude. (Azure's top NVMe instances are only slightly faster than AWS's.)
What makes this stagnation in the cloud even more surprising is that we have seen great advances in other areas. For example, during the same 2017 to 2023 time frame, EC2 network bandwidth exploded, increasing from 10 Gbit/s (c4) to 200 Gbit/s (c7gn). Now, I can only speculate why the cloud vendors have not caught up on the storage side:
One theory is that EC2 intentionally caps the write speed at 1 GB/s to avoid frequent device failure, given the total number of writes per SSD is limited. However, this does not explain why the read bandwidth is stuck at 2 GB/s.
A second possibility is that there is no demand for faster storage because very few storage systems can actually exploit tens of GB/s of I/O bandwidth. See our
recent VLDB paper
. On the other hand, as long as fast storage devices are not widely available, there is also little incentive to optimize existing systems.
A third theory is that if EC2 were to launch fast and cheap NVMe instance storage, it would disrupt the cost structure of its other storage service (in particular EBS). This is, of course, the classic innovator's dilemma, but one would hope that one of the smaller cloud vendors would make this step to gain a competitive edge.
Overall, I'm not fully convinced by any of these three arguments. Actually, I hope that we'll soon see cloud instances with 10 GB/s SSDs, making this post obsolete.
