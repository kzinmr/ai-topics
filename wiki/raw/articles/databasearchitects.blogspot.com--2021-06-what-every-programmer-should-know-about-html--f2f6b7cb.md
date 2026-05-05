---
title: "What Every Programmer Should Know About SSDs"
url: "https://databasearchitects.blogspot.com/2021/06/what-every-programmer-should-know-about.html"
fetched_at: 2026-05-05T07:01:28.547350+00:00
source: "Database Architects"
tags: [blog, raw]
---

# What Every Programmer Should Know About SSDs

Source: https://databasearchitects.blogspot.com/2021/06/what-every-programmer-should-know-about.html

Solid-State Drives (SSDs) based on flash have largely replaced magnetic disks as the standard storage medium. From the perspective of a programmer, SSDs and disks look very similar: both are persistent, enable page-based (e.g., 4KB) access through file systems and system calls, and have large capacities.
However, there are also important differences, which become important if one wants to achieve optimal SSD performance. As we will see, SSDs are more complicated and their performance behavior can appear quite mysterious if one simply thinks of them as fast disks. The goal of this post is to provide an understanding of why SSDs behave the way they do, which can help creating software that is capable of exploiting them. (Note that I discuss NAND flash, not Intel Optane memory, which has different characteristics.)
Drives not Disks
SSDs are often referred to as disks, but this is misleading as they store data on semiconductors instead of a mechanical disk. To read or write from a random block, a disk has to mechanically move its head to the right location, which takes on the order of 10ms. A random read from an SSD, in contrast, takes about 100us – 100 times faster. This low read latency is the reason why booting from an SSD is so much faster than booting from a disk.
Parallelism
Another important difference between disks and SSDs is that disks have one disk head and perform well only for sequential accesses. SSDs, in contrast, consist of dozens or even hundreds of flash chips ("parallel units"), which can be accessed concurrently.
SSDs transparently stripe larger files across the flash chips at page granularity, and a hardware prefetcher ensures that sequential scans exploit all available flash chips. However, at the flash level there is not much difference between sequential and random reads. Indeed, for most SSDs it is possible to achieve almost the full bandwidth with random page reads as well. To do this, one has to schedule hundreds of random IO requests concurrently in order to keep all flash chips busy. This can be done by starting lots of threads or using asynchronous IO interfaces such as libaio or io_uring.
Writing
Things get even more interesting with writes. For example, if one looks at write latency, one may measure results as low as 10us – 10 times faster than a read. However, latency only appears so low because SSDs are caching writes on volatile RAM. The actual write latency of NAND flash is about 1ms – 10 times slower than a read. On consumer SSDs, this can be measured by issuing a sync/flush command after the write to ensure that the data is persistent on flash. 
  On most data center/server SSDs, write latency cannot be measured directly: the sync/flush will complete immediately because a battery guarantees persistence of the write cache even in the case of power loss.
To achieve high write bandwidth despite the relatively high write latency, writes use the same trick as reads: they access multiple flash chips concurrently. Because the write cache can asynchronously write pages, it is not even necessary to schedule that many writes simultaneously to get good write performance.  However, the write latency cannot always be hidden completely: for example, because a write occupies a flash chip 10 times longer than a read, writes cause significant tail latencies for reads to the same flash chip.
Out-Of-Place Writes
Our understanding is missing one important fact: NAND flash pages cannot be overwritten. Page writes can only be performed sequentially within blocks that have been erased beforehand. These erase blocks have a size of multiple MB and therefore consist of hundreds of pages. On a new SSD, all blocks are erased, and one can directly start appending new data.
Updating pages, however, is not so easy. It would be too expensive to erase the entire block just to overwrite a single page in-place. Therefore, SSDs perform page updates by writing the new version of the page to a new location. This means that the logical and physical page addresses are decoupled. A mapping table, which is stored on the SSD, translates logical (software) addresses to physical (flash) locations. This component is also called Flash Translation Layer (FTL).
For example, let's assume we have a (toy) SSD with 3 erase blocks, each with 4 pages. A sequence of writes to pages P1, P2, P0, P3, P5, P1 may result in the following physical SSD state:
Block 0
P1 (old)
P2
P0
P3
Block 1
P5
P1
→
Block 2
Garbage Collection
Using the mapping table and out-of-place write, everything is good until the SSD runs out of free blocks. The old version of overwritten pages must eventually be reclaimed. If we continue our example from above by writing to pages P3, P4, P7, P1, P6, P2, we get the following situation:
Block 0
P1 (old)
P2 (old)
P0
P3 (old)
Block 1
P5
P1 (old)
P3
P4
Block 2
P7
P1
P6
P2
At this point we have no more free erase blocks (even though logically there should still be space). Before one can write another page, the SSD first has to erase a block. In the example, it might be best for the garbage collector to erase block 0, because only one of its pages is still in use. After erasing block 0, we make space for 3 writes and our SSD looks like this:
Block 0
P0
→
Block 1
P5
P1 (old)
P3
P4
Block 2
P7
P1
P6
P2
Write Amplification and Overprovisioning
To garbage collect block 0, we had to physically move page P0, even though logically nothing happened with that page. In other words, with flash SSDs the number of physical (flash) writes is generally higher than the number of logical (software) writes. The ratio between the two is called write amplification. In our example, to make space for 3 new pages in block 0, we had to move 1 page. Thus we have 4 physical writes for 3 logical writes, i.e., a write amplification of 1.33.
High write amplification decreases performance and reduces flash lifetime. How large write amplification is depends on the access pattern and how full the SSD is. Large sequential writes have low write amplification, while random writes are the worst case.
Let's assume our SSD is filled to 50% and we perform random writes. In steady state, wherever we erase a block, about half the pages of that block are still in use and have to be copied on average. Thus, write amplification for a fill factor of 50% is 2. In general, worst-case write amplification for a fill factor f is 1/(1-f):
f
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
0.95
0.99
WA
1.11
1.25
1.43
1.67
2.00
2.50
3.33
5
10
20
100
Because write amplification becomes unreasonably high for fill factors close to 1, most SSDs have hidden spare capacity. This overprovisioning is typically 10-20% of the total capacity. Of course, it is also easy to add more overprovisioning by creating an empty partition and never write to it.
Summary and Further Reading
SSDs have become quite cheap and they have very high performance. For example, a Samsung PM1733 server SSD costs about 200 EUR per TB and promises close to 7 GB/s read and 4 GB/s write bandwidth. Actually achieving such high performance requires knowing how SSDs work and this post described the most important behind-the-scenes mechanisms of flash SSDs.
I tried to keep this post short, which meant that I had to simplify things. To learn more, a good starting point is
this tutorial
, which also references some insightful papers. Finally, because SSDs have become so fast, the operating system I/O stack is often the performance bottleneck. Experimental results for Linux can be found in our
CIDR 2020 paper
.
