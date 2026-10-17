---
title: "Building fast filesystems for VMs"
url: "https://modal.com/blog/vm-sandbox-filesystem"
fetched_at: 2026-10-17T10:05:42.259488+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Building fast filesystems for VMs

Source: https://modal.com/blog/vm-sandbox-filesystem

At Modal, we like to think that we know a thing or two about squeezing nanoseconds out of systems. We love to obsess over making our systems performant and capable from the ground up, and we have to! We build for the thousands of GPUs waiting for that latest RL rollout, for the millions of agent sessions waiting on the next tool call, and even for the human waiting for their project to compile. To us, it’s all the same: make stuff go
really
fast.
We
recently shipped VM Sandboxes
, supporting ever more sophisticated agentic workloads at scale, and with the same performance expectations that came with our gVisor-based platform. A fundamental building block of a Sandbox is its filesystem: everything in the Sandbox depends, in one way or another, on the speed of its filesystem. Today, we’ll be talking about how we evolved our filesystem stack to become the performant backbone behind VM Sandboxes.
Background: ImageFS and fast cold starts
We solved the “container filesystem” problem in April 2022 by shipping
ImageFS
, our distributed lazy-loading filesystem for containers. In a nutshell, ImageFS works by pulling only the minimum amount of metadata upfront, mounting it through a Rust-based FUSE (Filesystem in Userspace) server, and then presenting it to the container. ImageFS lazily fetches file contents from a tiered content-addressed cache, from local memory, to regional CDNs, all the way up to global blob storage. ImageFS also implements smart prefetching in the background, so accesses almost always hit files already sitting on local disk or in memory.
ImageFS is a large part of why Modal containers cold-start in under a second. While traditional Docker runs spend minutes pulling and unpacking layers, ImageFS only needs to load its metadata index before startup and can do so in milliseconds. And despite being FUSE-based, ImageFS is fast! Given its read-only nature, ImageFS can signal to the kernel to aggressively cache every FUSE request it answers.
To support writes, we use OverlayFS, a standard Linux filesystem that merges a read-only lower layer (ImageFS, in our case) with a writable upper layer. All file mutations end up on copies of the files in the upper layer.
Reads and writes on ImageFS
Reads pass through OverlayFS to ImageFS, which serves them from a local cache backed by a regional CDN and global blob storage. On the first write to a file, OverlayFS copies it from ImageFS into the writable upper layer while the write lands there.
HOST
process
OverlayFS
upper
writable
ImageFS
read-only lower
local
RAM · SSD
CDN
regional
blob
global
copy-up
copy-up
read
write
Reads go through OverlayFS to ImageFS. The first write to a file copies it into the writable upper layer.
Leaning on ImageFS
When we started designing VMs, we knew we would lean on ImageFS again to inherit the same great sandbox experience from our containers. Containers share the Linux kernel with the underlying host system, and thus can use ImageFS directly. On the other hand, VMs have a full “guest” kernel, which doesn’t have access to the host’s filesystems, including ImageFS.
In the VM world, virtio-fs is precisely what bridges that gap. virtio-fs is another FUSE-based filesystem which forwards guest VM filesystem operations to a “virtio-fs daemon” (
virtiofsd
) on the host.
virtiofsd
takes guest filesystem requests and safely applies them on the directory shared with the guest. If we point this at ImageFS, the VM inherits all of its properties: lazy loading, sub-second cold starts, and tiered caching. Assembled, the stack looks like this:
The VM filesystem stack with virtio-fs
A guest process reaches the FUSE driver and virtio-fs transport in the guest kernel; requests cross the VM boundary to virtiofsd on the host, which applies them to ImageFS through the OverlayFS that containers use.
GUEST VM
HOST
USER
KERNEL
process
FUSE
fs driver
virtio-fs
transport
virtiofsd
ImageFS
OverlayFS
VM boundary
And indeed, it worked! VMs booted from the same
modal.Image
s as our existing containers, with the same cold-start performance we expected. So we shipped it… right?
Fast to boot, slow to use
Fast cold starts are not the only criterion for a viable filesystem stack.
With virtio-fs, all we did was add an extra layer atop our existing ImageFS stack. By virtue of “doing more”, we expected it to be slower. However, we saw the performance of a recursive
chown
go from four seconds to over a minute! Real-world workloads like
pnpm install
and
bun install
looked thrice as slow, and
ripgrep
performance fell off a cliff.
To understand what was happening, we broke down the syscalls from our
bun
and
pnpm
workloads to devise synthetic microbenchmarks. We compared ImageFS used directly by the host, behind gVisor, and over virtio-fs in a VM:
Filesystem operations, 100,000 calls each
virtio-fs + ImageFS is slowest on every operation: chown 9.87 s against 2.31 s on gVisor and 1.58 s on ImageFS.
FILESYSTEM OPERATIONS
SECONDS · LOWER IS BETTER
stat
virtio-fs
3.23 s
gVisor
2.12 s
ImageFS
1.45 s
link
virtio-fs
9.75 s
gVisor
3.91 s
ImageFS
2.57 s
chown
virtio-fs
9.87 s
gVisor
2.31 s
ImageFS
1.58 s
hardlink tree
virtio-fs
12.61 s
gVisor
4.61 s
ImageFS
2.93 s
cp -R
virtio-fs
32.90 s
gVisor
17.75 s
ImageFS
6.48 s
0
5 s
10 s
15 s
20 s
25 s
30 s
35 s
Aha!
stat
was 2x slower under virtio-fs, whilst
chown
was over 6x worse. While we attributed the slower
stat
performance to the extra overhead imposed by virtio-fs, we were still surprised by
chown
. Tracing the syscalls again, this time on
virtiofsd
, showed us that
chown
decomposed into many more operations over virtio-fs:
The
chown
leaves the guest process as an
fchownat
and drops into the guest kernel.
The guest kernel checks and clears file capabilities by sending a
FUSE_GETXATTR
out of the VM to
virtiofsd
, which checks the file and replies, costing 3 host syscalls.
The guest kernel also checks and clears setuid bits, sending a
FUSE_GETATTR
to the host.
Finally, the ownership change goes out as a
FUSE_SETATTR
.
virtiofsd
changes the owner and returns the updated file attributes.
In total, a single
chown
required three round trips from guest VM to host, and
virtiofsd
made six host syscalls, each of which landed on ImageFS.
One chown over virtio-fs
One chown syscall reaches the guest's FUSE driver, which sends three requests, getxattr, getattr and setattr, over virtio-fs to virtiofsd and ImageFS on the host. The process waits about 99 µs per call.
GUEST VM
HOST
USER
KERNEL
process
chown()
FUSE
fs driver
virtio-fs
transport
virtiofsd
ImageFS
getxattr
getxattr
getattr
getattr
setattr
setattr
0 µs
0 µs
1 µs
2 µs
3 µs
4 µs
5 µs
6 µs
7 µs
8 µs
9 µs
10 µs
11 µs
12 µs
13 µs
14 µs
15 µs
16 µs
17 µs
18 µs
19 µs
20 µs
21 µs
22 µs
23 µs
24 µs
25 µs
26 µs
27 µs
28 µs
29 µs
30 µs
31 µs
32 µs
33 µs
34 µs
35 µs
36 µs
37 µs
38 µs
39 µs
40 µs
41 µs
42 µs
43 µs
44 µs
45 µs
46 µs
47 µs
48 µs
49 µs
50 µs
51 µs
52 µs
53 µs
54 µs
55 µs
56 µs
57 µs
58 µs
59 µs
60 µs
61 µs
62 µs
63 µs
64 µs
65 µs
66 µs
67 µs
68 µs
69 µs
70 µs
71 µs
72 µs
73 µs
74 µs
75 µs
76 µs
77 µs
78 µs
79 µs
80 µs
81 µs
82 µs
83 µs
84 µs
85 µs
86 µs
87 µs
88 µs
89 µs
90 µs
91 µs
92 µs
93 µs
94 µs
95 µs
96 µs
97 µs
98 µs
99 µs
0 µs
One
chown
over virtio-fs ends up making three host round trips and taking 99 µs.
And these numbers are with
virtiofsd
already tuned to maximally cache and coalesce operations. Files carry “meaning”, or metadata: names, owners, permissions, etc. Every metadata operation must thus ask whoever the authority on that metadata is. virtio-fs puts that authority on the far side of the VM boundary, to which the guest is only ever a client.
In other words, virtio-fs is a
shared
filesystem, even when nothing on our host side ever needs to read a VM’s root filesystem. It was time to go back to the drawing board.
Changing the language: speaking in blocks
What happens if we let the filesystem live solely inside the guest? With all the metadata interpreted within the guest, the host has no other job than to hold bytes and hand them back to the guest when necessary.
This arrangement already has a name: a block device! Blocks are the language spoken by physical drives, like hard drives and SSDs. Drives have
no idea
what a file is; they just handle chunks of data for us. From a bird’s-eye view, filesystems like ext4 are just translators from the language of files to the language of blocks.
Even more fortunately for us, the Linux kernel has had decades to get good at working with block devices. Block devices are the gold standard for physical machines, via HDDs and SSDs, and for VMs, via virtio-fs’ block-based counterpart: virtio-blk.
And, perhaps most importantly, unlike with virtio-fs, the guest kernel already treats every block device it has access to as exclusively owned. No filesystem operation has to go ask someone else about the state of the world.
With this, sending the earlier
chown
through a virtio-blk solution shows us:
The
chown
leaves the guest process as an
fchownat
and drops into the guest kernel, same as before.
The guest kernel checks and clears file capabilities, as the ext4 driver lives within the guest kernel.
The guest kernel checks and clears setuid bits, again without calling out anywhere.
ext4 makes the ownership change and logs it to its write-ahead journal.
The host only finds out about this later, when ext4 flushes a
batch
of writes carrying all changes since the last commit. This amortizes the cost of hundreds or thousands of file operations behind a single block command, and it happens asynchronously, leaving the filesystem active while doing so.
chown over virtio-blk
Each chown completes inside the guest's ext4 in about 2.1 µs, against 99 µs over virtio-fs. Every 5 seconds ext4 commits its journal and writes the accumulated changes to the host as one batch over virtio-blk.
GUEST VM
HOST
USER
KERNEL
process
chown()
ext4
journal
virtio-blk
transport
virtio-blk backend
virtio-fs 99 µs
2.1 µs
writeback
chown
over virtio-blk takes ~2.1 µs per call, to ext4's journal, which is batch-committed asynchronously.
Since the host only speaks blocks, it loses its ability to work with the VM’s filesystem. In return, we keep all operations, including the pesky metadata round trips, within the guest, and avoid all the extra FUSE round trips that
virtiofsd
would incur.
ImageFS-blk
Block devices made the VM filesystem fast, but how do we tie that back together with ImageFS, to support the properties it gave us, like
modal.Image
compatibility and lazy loading?
The naive approach, shelling out to
mkfs.ext4 -d
to create an ext4-formatted disk and sharing that over virtio-blk, doesn’t work with ImageFS’ lazy architecture. For
mkfs.ext4
to work, all image content
has
to be present upfront.
Instead, we asked ourselves: how can we trick the guest’s ext4 driver into thinking it has a fully materialized image, while actually serving file content on demand? Or equivalently, how can we apply ImageFS’ ideas to virtio-blk?
ext4 keeps a small record for every file, known as an inode, that holds its permissions, size and a list of “extents”, or ranges of blocks representing file data. For a requested
modal.Image
, we once again only pull in the minimal amount of file metadata upfront, and use it to map out and write ext4’s inode records ourselves.
We leave the rest of the ext4 image
sparse
, supplying the actual blocks only when the guest reads them. Since we wrote all of ext4’s metadata ourselves, we already have everything we need to be able to map block requests to ImageFS file bytes, and vice versa.
A host daemon, creatively named ImageFS-blk, handles the resulting block requests over virtio-blk. Its job is to serve contents lazily using our metadata mappings, serving the immutable image and persisting writes separately.
On write:
we persist the blocks to the sparse file and mark them as dirty in a bitmap. The sparse file only accumulates writes from the VM it supports, and operations like snapshots simply have to consult it to figure out what changed.
On read:
we consult our mappings to convert the requested block range into a file and byte range and fetch it from ImageFS. Dirty blocks and ext4 metadata are served directly from the sparse file, analogous to OverlayFS, but on a block level.
Reads and writes on ImageFS-blk
Block requests from the guest's ext4 reach ImageFS-blk on the host. Written blocks land in a sparse file; reads of unmodified blocks come from ImageFS, served from a local cache backed by a regional CDN and global blob storage.
GUEST VM
HOST
ext4
block requests
ImageFS-blk
sparse file
written blocks
ImageFS
image blocks
local
RAM · SSD
CDN
regional
blob
global
read
write
ImageFS-blk routes each block: written blocks to the sparse file, unmodified image blocks from the cache hierarchy.
During the ImageFS-blk design phase, we also realized we could outperform Linux’s OverlayFS mount on top of ImageFS. Before modifying a file in the immutable lower layer, OverlayFS must copy it into the writable upper layer. On a normal setup, this can be cheap: with upper and lower on the same XFS filesystem, reflinks let the two copies share the underlying data without physically copying it.
In our ImageFS setup, our lower is a FUSE filesystem and upper is XFS, meaning reflinks didn’t work. In degenerate cases, this incurs gigabytes of overhead to write individual bytes! ImageFS-blk can “copy on write” at the block level rather than the file level, bounding the worst-case overhead to copying a single block.
With prefetching in place, we were back to our sub-second cold starts, and booted without the need to download the entire image. All while reaping the benefits of letting the guest manage its own filesystem.
Benchmarking
ImageFS-blk completely blew the virtio-fs solution out of the water. Looking at the same syscall microbenchmark:
Filesystem operations, 100,000 calls each: ImageFS-blk against virtio-fs
ImageFS-blk is faster on every operation: chown 0.21 s against 9.87 s on virtio-fs + ImageFS.
FILESYSTEM OPERATIONS
SECONDS · LOWER IS BETTER
stat
virtio-fs
3.23 s
ImageFS-blk
0.90 s
link
virtio-fs
9.75 s
ImageFS-blk
0.80 s
chown
virtio-fs
9.87 s
ImageFS-blk
0.21 s
hardlink tree
virtio-fs
12.61 s
ImageFS-blk
1.29 s
cp -R
virtio-fs
32.90 s
ImageFS-blk
5.74 s
0
5 s
10 s
15 s
20 s
25 s
30 s
35 s
Our
bun install
benchmark dropped 12x, from 12.5 seconds to 1.07 seconds. It even beat out the classic ImageFS filesystem, since metadata operations in ImageFS-blk never leave the guest, and don’t traverse the FUSE path of ImageFS. Code navigation and read throughput also drastically improved.
These gains extended to database workloads.
pgbench
and
speedtest1
had massive speed improvements with ImageFS-blk, displaying the efficiencies of block devices.
Developer workflow and database benchmarks
bun install (12.5 / 3.1 / 1.07 s), ripgrep on the Linux repo (warm 6.03 / 3.77 / 0.18 s; cold 24.3 / 4.47 / 8.53 s), SQLite speedtest1 (543.4 / 289.8 / 43.2 s), pgbench read-only (98.2k / 137.1k / 230.1k TPS) and read-write (8.3k / 11.9k / 18.8k TPS), each for virtio-fs + ImageFS, ImageFS and ImageFS-blk.
DEVELOPER WORKFLOWS
bun install
lower is better
virtio-fs
12.5 s
ImageFS
3.1 s
ImageFS-blk
1.07 s
ripgrep, warm cache
Linux repo · lower is better
virtio-fs
6.03 s
ImageFS
3.77 s
ImageFS-blk
0.18 s
ripgrep, cold cache
Linux repo · lower is better
virtio-fs
24.3 s
ImageFS
4.47 s
ImageFS-blk
8.53 s
DATABASES
SQLite speedtest1
runtime · lower is better
virtio-fs
543.4 s
ImageFS
289.8 s
ImageFS-blk
43.2 s
pgbench read-only
TPS · higher is better
virtio-fs
98.2k
ImageFS
137.1k
ImageFS-blk
230.1k
pgbench read-write
TPS · higher is better
virtio-fs
8.3k
ImageFS
11.9k
ImageFS-blk
18.8k
And we’re constantly working on making our filesystem stack even faster!
Incoming performance wizardry from our FS wrangler
Daniel Norberg
.
Try it out!
If you want to test out everything we built here for yourself, VM Sandboxes
are generally available
, powered by our ImageFS-blk backend. If this sort of work interests you,
come join us
!
Acknowledgements
This project was a team effort and was only possible with the help of Daniel Norberg, Staffan Gimåker, Apoorva Bhagwat, Connor Adams, and Jonathon Belotti.
