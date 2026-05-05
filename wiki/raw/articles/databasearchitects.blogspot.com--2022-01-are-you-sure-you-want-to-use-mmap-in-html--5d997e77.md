---
title: "Are you sure you want to use MMAP in your database management system?"
url: "https://databasearchitects.blogspot.com/2022/01/are-you-sure-you-want-to-use-mmap-in.html"
fetched_at: 2026-05-05T07:01:29.014483+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Are you sure you want to use MMAP in your database management system?

Source: https://databasearchitects.blogspot.com/2022/01/are-you-sure-you-want-to-use-mmap-in.html

Many database management systems carefully manage disk I/O operations and explicitly cache pages in main memory. Operating systems implement a page cache to speed up recurring disk accesses as well, and even allow transparent access to disk files through the mmap system call. Why do most database systems then even implement I/O handling and a caching component if the OS provides these features through mmap? Andrew Pavlo, Andrew Crotty, and myself tried to answer this question in a
CIDR 2022 paper
. This is quite a contentious question as the
Hacker News discussion of the paper
shows.
The paper argues that using
mmap
in database systems is almost always a bad idea. To implement transactions and crash recovery with mmap, the DBMS has to write any change out-of-place because there is no way to prevent write back of a particular page. This makes it impossible to implement classical ARIES-style transactions. Furthermore, data access through mmap can take a handful of nanoseconds (if the data is in the CPU cache) or milliseconds (if it's on disk). If a page is not cached, it will be read through a synchronous page fault and there is no interface for asynchronous I/O. I/O errors, on the other hand, are communicated through signals rather than a local error code. These problems are caused by mmap's interface, which is too high-level and does not give the database system enough control.
In addition to discussing these interface problems, the paper also shows that Linux' page cache and mmap implementation cannot achieve the bandwidth of modern storage devices. One
PCIe 4.0 NVMe SSD
can read over 6 GB/s and
upcoming PCIe 5.0 SSDs
will almost double this number. To achieve this performance, one needs to schedule hundreds or even thousands (if one has multiple SSDs) of concurrent I/O requests. Doing this in a synchronous fashion by starting hundreds of threads will not work well. Other kernel-level performance issues are single-threaded page eviction and TLB shootdowns. Overall, this is an example of OS evolution lagging behind hardware evolution.
The OS has one big advantage over the DBMS though: it has control over the page table. Once a page is mapped, accessing it becomes transparent and as fast as ordinary memory. Any manually-implemented buffer manager, in contrast, will have some form of indirection, which causes some overhead. Pointer swizzling as implemented in
LeanStore
and
Umbra
is a fast alternative but is also more difficult to implement than a traditional buffer manager and only supports tree-like data structures. Therefore, an interesting question is whether it would be possible to have an mmap-like interface, but with more control and better performance. Generally I believe this kind of research between different areas should be more common.
