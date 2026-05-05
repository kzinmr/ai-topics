---
title: "Infinite disk"
url: "https://danluu.com/infinite-disk/"
fetched_at: 2026-05-05T07:01:32.703989+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Infinite disk

Source: https://danluu.com/infinite-disk/

Hardware performance “obviously” affects software performance and affects how software is optimized. For example, the fact that caches are multiple orders of magnitude faster than RAM means that
blocked array accesses
give better performance than repeatedly striding through an array.
Something that's occasionally overlooked is that hardware performance also has profound implications for system design and architecture.
Let's look at this table of latencies that's been passed around since 2012
:
Operation                                Latency (ns)     (ms)
L1 cache reference                            0.5 ns
Branch mispredict                             5   ns
L2 cache reference                            7   ns
Mutex lock/unlock                            25   ns
Main memory reference                       100   ns
Compress 1K bytes with Zippy              3,000   ns
Send 1K bytes over 1 Gbps network        10,000   ns    0.01 ms
Read 4K randomly from SSD               150,000   ns    0.15 ms
Read 1 MB sequentially from memory      250,000   ns    0.25 ms
Round trip within same datacenter       500,000   ns    0.5  ms
Read 1 MB sequentially from SSD       1,000,000   ns    1    ms
Disk seek                            10,000,000   ns   10    ms
Read 1 MB sequentially from disk     20,000,000   ns   20    ms
Send packet CA->Netherlands->CA     150,000,000   ns  150    ms
Consider the latency of a disk seek (10ms) vs. the latency of a round-trip within the same datacenter (.5ms). The round-trip latency is so much lower than the seek time of a disk that we can dis-aggregate storage and distribute it anywhere in the datacenter without noticeable performance degradation, giving applications the appearance of having infinite disk space without any appreciable change in performance. This fact was behind the rise of distributed filesystems like GFS within the datacenter over the past two decades, and various networked attached storage schemes long before.
However, doing the same thing on a 2012-era commodity network with SSDs doesn't work. The time to read a page on an SSD is 150us, vs. a 500us round-trip time on the network. That's still a noticeable performance improvement over spinning metal disk, but it's over 4x slower than local SSD.
But here we are in 2015. Things have changed. Disks have gotten substantially faster. Enterprise NVRAM drives can do a 4k random read in around 15us, an order of magnitude faster than 2012 SSDs. Networks have improved even more. It's now relatively common to employ a low-latency user-mode networking stack, which drives round-trip latencies for a 4k transfer down to 10s of microseconds. That's fast enough to disaggregate SSD and give applications access to infinite SSD. It's not quite fast enough to disaggregate high-end NVRAM, but
RDMA
can handle that.
RDMA drives latencies down another order of magnitude, putting network latencies below NVRAM access latencies by enough that we can disaggregate NVRAM. Note that these numbers are for an unloaded network with no congestion -- these numbers will get substantially worse under load, but they're illustrative of what's possible. This isn't exactly new technology: HPC folks have been using RDMA over InfiniBand for years, but InfiniBand networks are expensive enough that they haven't seen a lot of uptake in datacenters. Something that's new in the past few years is the ability to run RDMA over Ethernet. This turns out to be non-trivial; both
Microsoft
and
Google
have papers in this year's SIGCOMM on how to do this without running into the numerous problems that occur when trying to scale this beyond a couple nodes. But it's possible, and we're approaching the point where companies that aren't ridiculously large are going to be able to deploy this technology at scale.
However, while it's easy to say that we should use disaggregated disk because the ratio of network latency to disk latency has changed, it's not as easy as just taking any old system and throwing it on a fast network. If we take a 2005-era distributed filesystem or distributed database and throw it on top of a fast network, it won't really take advantage of the network. That 2005 system is going to have assumptions like the idea that it's fine for an operation to take 500ns, because how much can 500ns matter? But it matters a lot when your round-trip network latency is only few times more than that and applications written in a higher-latency era are often full of "careless" operations that burn hundreds of nanoseconds at a time. Worse yet, designs that are optimal at higher latencies create overhead as latency decreases. For example, with 1ms latency, adding local caching is a huge win and 2005-era high-performance distributed applications will often rely heavily on local caching. But when latency drops below 1us, the caching that was a huge win in 2005 is often not just pointless, but actually counter-productive overhead.
Latency hasn't just gone down in the datacenter. Today, I get about 2ms to 3ms latency to YouTube. YouTube, Netflix, and a lot of other services put a very large number of boxes close to consumers to provide high-bandwidth low-latency connections. A side effect of this is that any company that owns one of these services has the capability of providing consumers with infinite disk that's only slightly slower than normal disk. There are a variety of reasons this hasn't happened yet, but it's basically inevitable that this will eventually happen. If you look at what major cloud providers are paying for storage, their
COGS
of providing safely replicated storage is or will become lower than the retail cost to me of un-backed-up unreplicated local disk on my home machine.
It might seem odd that cloud storage can be cheaper than local storage, but large cloud vendors have a lot of leverage. The price for the median component they buy that isn't an Intel CPU or an Nvidia GPU is staggeringly low compared to the retail price. Furthermore, the fact that most people don't access the vast majority of their files most of the time. If you look at the throughput of large HDs nowadays, it's not even possible to do so. A
typical consumer 3TB HD
has an average throughput of 155MB/s, making the time to read the entire drive 3e12 / 155e6 seconds = 1.9e4 seconds = 5 hours and 22 minutes. And people don't even access their disks at all most of the time! And when they do, their access patterns result in much lower throughput than you get when reading the entire disk linearly. This means that the vast majority of disaggregated storage can live in cheap cold storage. For a neat example of this,
the Balakrishnan et al. Pelican OSDI 2014 paper
demonstrates that if you build out cold storage racks such that only 8% of the disk can be accessed at any given time, you can get a substantial cost savings. A tiny fraction of storage will have to live at the edge, for the same reason that a tiny fraction of YouTube videos are cached at the edge. In some sense, the economics are worse than for YouTube, since any particular chunk of data is very likely to be shared, but at the rate that edge compute/storage is scaling up, that's unlikely to be a serious objection in a decade.
The most common counter argument to disaggregated disk, both inside and outside of the datacenter, is bandwidth costs. But bandwidth costs have been declining exponentially for decades and continue to do so. Since 1995, we've seen an increase in datacenter NIC speeds go from 10Mb to 40Gb, with 50Gb and 100Gb just around the corner. This increase has been so rapid that, outside of huge companies, almost no one has re-architected their applications to properly take advantage of the available bandwidth. Most applications can't saturate a 10Gb NIC, let alone a 40Gb NIC. There's literally more bandwidth than people know what to do with. The situation outside the datacenter hasn't evolved quite as quickly, but even so, I'm paying $60/month for 100Mb, and if the trend of the last two decades continues, we should see another 50x increase in bandwidth per dollar over the next decade. It's not clear if the cost structure makes cloud-provided disaggregated disk for consumers viable today, but the current trends of implacably decreasing bandwidth cost mean that it's inevitable within the next five years.
One thing to be careful about is that
just because we can disaggregate something, it doesn't mean that we should
. There was a
fascinating paper by Lim et. al at HPCA 2012 on disaggregated RAM
where they build out disaggregated RAM by connecting RAM through the backplane. While we have the technology to do this, which has the dual advantages of allowing us to provision RAM at a lower per-unit cost and also getting better utilization out of provisioned RAM, this doesn't seem to provide a performance per dollar savings at an acceptable level of performance, at least so far.
The change in relative performance of different components causes fundamental changes in how applications should be designed. It's not sufficient to just profile our applications and eliminate the hot spots. To get good performance (or good performance per dollar), we sometimes have to step back, re-examine our assumptions, and rewrite our systems. There's a lot of talk about how hardware improvements are slowing down, which usually refers to improvements in CPU performance. That's true, but there are plenty of other areas that are undergoing rapid change, which requires that applications that care about either performance or cost efficiency need to change. GPUs, hardware accelerators, storage, and networking are all evolving more rapidly than ever.
Update
Microsoft seems to disagree with me on this one. OneDrive has been moving in the opposite direction. They got rid of infinite disk, lowered quotas for non-infinite storage tiers, and changing their sync model in a way that makes this less natural. I spent maybe an hour writing this post. They probably have a team of Harvard MBAs who've spent 100x that much time discussing the move away from infinite disk. I wonder what I'm missing here. Average utilization was 5GB per user, which is practically free. A few users had a lot of data, but if someone uploads, say, 100TB, you can put most of that on tape. Access times on tape are glacial -- seconds for the arm to get the cartridge and put it in the right place, and tens of seconds to seek to the right place on the tape. But someone who uploads 100TB is basically using it as archival storage anyway, and you can mask most of that latency for the most common use cases (uploading libraries of movies or other media). If the first part of the file doesn't live on tape, and the user starts playing a movie that lives on tape, the movie can easily play for a couple minutes off of warmer storage while the tape access gets queued up. You might say that it's not worth it to spend the time it would take to build a system like that (perhaps two engineers working for six months), but you're already going to want a system that can mask the latency to disk-based cold storage for large files. Adding another tier on top of that isn't much additional work.
Update 2
It's happening. In April 2016, Dropbox announced that they're offering "Dropbox Infinite", which lets you access your entire Dropbox regardless of the amount of local disk you have available. The inevitable trend happened, although I'm a bit surprised that it wasn't Google that did it first since they have better edge infrastructure and almost certainly pay less for storage. In retrospect, maybe that's not surprising, though -- Google, Microsoft, and Amazon all treat providing user-friendly storage as a second class citizen, while Dropbox is all-in on user friendliness.
Thanks to Leah Hanson, bbrazil, Kamal Marhubi, mjn, Steve Reinhardt, Joe Wilder, and Jesse Luehrs for comments/corrections/additions that resulted in edits to this.
