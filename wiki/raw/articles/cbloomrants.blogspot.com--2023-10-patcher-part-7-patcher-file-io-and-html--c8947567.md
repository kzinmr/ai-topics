---
title: "Patcher Part 7 : Patcher File IO and Parallelism"
url: "http://cbloomrants.blogspot.com/2023/10/patcher-part-7-patcher-file-io-and.html"
fetched_at: 2026-05-05T07:01:47.825313+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Patcher Part 7 : Patcher File IO and Parallelism

Source: http://cbloomrants.blogspot.com/2023/10/patcher-part-7-patcher-file-io-and.html

In the real world, a lot of the issues for making a very fast patcher are in the practical matters of parallelism and file IO, so let's dig
into those a bit.
I believe that it is bad practice to take unnecessarily slow algorithms and just throw them onto threads to make your program fast by using
tons of threads.  So first we tried to make the patcher algorithms as fast as possible on a single thread, and we got the
core operation (CDC "signature" computation) down to 1.5 cycles/byte, but that's still not fast enough to keep up with IO, so we will need
parallelism.
The "speed of light" for patcher, the fastest it can possibly ever go, is the time to just do the IO to read the previous & new file sets, and
to write the patch output.  We want to hit that speed, which means we want to be totally IO bound.   A typical current SSD can do around 6 GB/s ;
on a 3 GHz CPU that's 0.5 cycles/byte for IO.  So naively that tells us we need 3 computation threads running 1.5 cycle/byte work to keep up with IO.
(modern PCIe 5 drives can go even faster and would need more computation threads to saturate the IO).
When doing parallelism work, it's useful to think about what is the single-threaded critical path that cannot be
parallelized and will limit your speed (even if you had infinite thread count).  In this case it's easy, it's just the IO.
So as long as we are always doing IO, keeping the disk running at maximum speed, and overlapping CPU work alongside that,
we will achieve maximum speed.
The primary operation of the patcher is the computation of the CDC signature, which has the basic form :
read whole file into buffer

scan over buffer doing hash computations, making fragments
Parallelizing over patch sets that consist of lots of small files is trivial, but to parallelize (and
crucially, overlap the IO and computation time) over single large files requires interleaving the IO and
computation work on individual files.  The real world data sets we work on tend to be either single very
large files (such as when patching a whole distribution that's packed together with something like tar), or
a bunch of files of various sizes, we want to handle all those cases well.
Since IO speed is crucial here, I did some experiments on a couple different disk types on a couple
different machines, and I will briefly summarize what I found.  Caveats: this is very Windows specific; I use
the Win32 OVERLAPPED API.  I do not have a modern PCI5 super-fast SSD or a Zen 4 CPU to test on; my fastest SSD is around 6 GB/s, some
results may differ on new PCI5 SSD's.  I did test on 3 machines : an Intel CPU, a Ryzen Zen 3, and a ThreadRipper, all with
both an M2 SSD and a spinning platter HDD.  I did not test with
SetFileValidData
to get true async writes, as that is not practical to use in the real world so is moot.
Summarizing what I found :
You can use multiple IO threads to read from SSD's at full speed, but multiple threads reading from HDD
are a huge huge disaster.  You must use only 1 thread for IO on HDD.
Always do reads unbuffered.  Using a buffered read causes extra mem copies through the IO buffers, which
is a significant speed penalty on fast SSD's.  (buffered reads don't hurt on HDD, but it's simpler to just say use
unbuffered reads all the time).
Use unbuffered writes on SSD.  Use buffered writes on HDD.  On some of the HDD's on some of my systems,
buffered writes were significantly faster than unbuffered (120 MB/s vs 80 MB/s).  (to be clear I mean buffered at
the Win32 CreateFile HANDLE level, you should never use stdio or your own extra buffering system for fast IO).
Use 4-16 MB io chunk sizes.  This is small enough to be incremental at reasonable granularity and big enough to
run at full speed.
For incremental reading of a file on a single thread, do OVERLAPPED async IO and keep two OVERLAPPED structs running at all
times, like a double-buffer.  That is, fire off two async reads, when the first completes fire it for the next chunk, etc.
This ensures you always have a pending async read enqueued to the device, you aren't doing an IO, then going back to your io thread
to enqueue the next, leaving the device idle for a while until you get the next chunk requested.
SSD's can run reads and writes at the same time at full speed.  For example, to do a file copy on an SSD you
should run the reads and writes at the same time, which can be done on a single thread use triple-buffering of async/overlapped IO
(so you always have an async read and write in progress).
Some IO operations (eg. dir listing) benefit from being heavily multi-threaded (running on all cores, not just 1), because they are mostly CPU
bound (working on data structures that are often in memory already).  For the real bandwidth heavy work (reading,writing),
lots of threads doesn't help.  You can get full speed with only 1 IO thread for HDD, and 2 for SSD.
On the 3 machines and 6 disks that I tested on, this recipe gave near-optimal speed in all cases.  That is by no means
a thorough survey, and different disks or OS or config situations may give different results.
My goal was to find a simple standard recipe for fast IO that doesn't involve a lot of per-machine tweaking, which
could easily get over-trained for my specific machines.  I also believe in using as few threads as possible that get you
to full speed.
Out in the wild you can have funny issues affecting IO perf, such as running in some kind of VM or container, running with a virtual file system
driver from a virus scanner, files on network drives, etc.  Timing IO can be tricky because of the effects of OS buffers, and writes returning
from your API call before they actually go to disk.  Some disks are fast at first them go into a slower mode when used heavily, either due to
caches or thermal throttle.
Detecting SSD vs HDD is pretty simple on Windows; it's in
cblib
("DetectDriveType")
as is a basic double-buffered OVERLAPPED reader and triple-buffered copier ("win32_sync_copy").
The basic threading model patcher uses is this :
Run 1 file at a time on HDD, 2 at a time on SSD

On each file, do async OVERLAPPED IO in chunks for incremental IO

As each chunk is done, kick off CPU work to process that chunk (compute "signature")
The "signature" finds CDC boundaries and computes hashes on each fragment.  We do this in 16 MB chunks, which means we get artificial
cut points (not content-determined) at the 16 MB IO chunk boundaries.  You could just ignore that, as it's a small fraction of the total
size, but instead what I do is after an adjacent pairs of chunks is done, I delete the fragments that were made near the boundary (two on
each side of the boundary) and re-find CDC boundaries in that small region.
On an SSD at 6 GB/s and CPU at 3 GHz, the rough times are 0.5 cycles/byte for IO and 1.5 cycles/byte for signature building.
So the timeline lookes like :
different 16 MB chunks labelled A,B,C
time is on the X axis

IO : ABCDEFG
work:AAADDDGGG
work: BBBEEE
work:  CCCFFF
That is, three time units of work on CPU worker threads per IO chunk, so we need three threads doing computation to keep up with the IO
speed.
The signature computation for the "previous" and "new" file are the vast majority of the CPU work, but once that is done we have to 
build the hash table and then match against that hash table, which is pure CPU work.  During this phase, we can be running the next file
in the set, doing its IO phase.
To do that easily, I use a simple semaphore to throttle the IO threads, rather than a true dedicated IO thread.  (I think a true IO thread
is probably a better model, with followup work spawned on IO completion, but it makes the code much less linear-imperative, so the semaphore
method while a bit less efficient is much easier to read and maintain).  The IO semaphore means only 1 thread can be running IO at a time
(as required for HDD, or 2-3 threads for SSD), but which thread that is changes.
So what we actually do is :
parallel for on files , (memory limited and io_sem limited, see later)
{

take io_semaphore { read file1 and make signature, incrementally, uses 3 worker threads }
take io_semaphore { read file2 and make signature, incrementally, uses 3 worker threads }

^ these two can run at the same time if two io_sem decrements are available

now the io_sem is released, so the next file can start its io work immediately

do cpu work :
build hash table
match against hash table
construct patch

release memory, which unblocks the memory limitted queue
}
For threading primitives, I used the C++ std::async, as well as Microsoft's concrt/ppl.  (I did this sort of as a learning experiment
to try some not-quite-modern C++ threading code instead of using the mechanisms I had written for Oodle).
On Windows, std::async and concrt/ppl are both built on the Windows thread pool.  When you start async tasks or do 
a parallel_for, they take threads from the thread pool, or create new ones if necessary.  Sadly on gcc/Linux, std::async starts a
new thread for each async task (no thread pool), which is no good, and means we can't use std::async to write cross platform code.
The Windows thread pool mostly works okay for our purposes.  Thread pools solve the "wait from worker" problem by switching to another
thread in the pool when you wait on a worker, which keeps a task running on all cores at all times.  (as opposed to coroutine yields, or
fibers, or "pop on wait", which are alternative solutions to "wait from worker").  
This is mostly okay but requires some care.  When you do a wait from a pool thread (such as waiting on an IO
to finish, or waiting on a mutex/critsec), it can cause a new thread to start up, so that something runs while you stall.  Then when your
wait is done, your thread can start running again, but the new thread that was started may still exist.  This can cause the pool to get
many more threads than cores, and give you extreme over-subscription.
As an example of a terrible way to use a thread pool, consider the common pattern of doing an IO to read a whole file, then doing some
processing on that file :
parallel_for over all files :
{
  phase1: read whole file into buffer (wait on io completion)
  phase2: act on buffer, doing some computation
}
Say you have something like 32 cores and 1000 files to process.  The parallel_for will make 1000 tasks and send them to the thread pool to
execute.  Initially the pool will kick off a task to a worker thread for each core (32 of them).  Each of those tasks will try to start a file IO then wait on it.
So those 32 threads will all go to sleep.  The thread pool will see it has no threads running on the cores, but lots of pending tasks,
so it needs to make more threads; it will make 32 more threads, all of which will block on IO and go to sleep.  Eventually we wind up with 1000 threads
all sleeping on IO.  Later, the IO's start to finish and the tasks are woken up to move onto phase2 for doing some computation on the IO results.
The problem is we now have 1000 threads that all want to run and do CPU work.
This is just in the nature of the way a thread pool addresses the "wait from worker" problem.  (note that "pop on wait" and "deep yield" also have their
own bad patterns and are by no means a magical solution either, it's simply a messy problem that will always have some bad cases).  There are some
fudges that make it not actually this bad, for example you can set a maximum thread count in the pool to be something like 2X the core count, but
the better solution is to just not use the thread pool in that way.
In general, it works well if you avoid waiting from tasks, and instead use followup tasks that trigger from task completions (eg. dependencies).
Specifically in the "patcher" case we do have this common pattern of do some IO and then kick off CPU work to act on that IO.  So we can use some
better primitives for that.  For example we can make a "parallel_for" that loads the file contents one by one, or using 2 threads, and then kicks off
the followup cpu-only work :
parallel_for over all files using 1 or 2 IO threads :
{
  phase1: read whole file into buffer (wait on io completion)
  start async task on thread pool of all cores :
  {
    phase2: act on buffer, doing some computation
  }
}
Another common useful pattern that I use is to have a parallel_for that pre-takes a critsec or semaphore.  Say you have some task that you know
needs to immediately take a critsec at the start of the task :
parallel_for :
{
  phase1:
    enter critsec C
      do X
    leave critsec C
  phase2:
    do more work Y
}
This will have a similar problem to the IO task on a threadpool.  You will start too many threads, they will all block on the critsec C, then once
they all get past phase1, you will have too many threads running phase2.
One solution is to have a parallel_for that only dispatches tasks with the critsec entered :
single threaded for :
{
  enter critsec C
  start async task on thread pool :
  {
    // critsec C is already owned by me
      do X
    leave critsec C
  phase2:
    do more work Y
  }
}
Note that when the async task leaves critsec C, the single threaded for loop can then step to the next item in the list 
while the async
task proceeds with "work Y".  So we get the desired result that "work Y" can run on the thread pool over all cores,
but we aren't starting threads just to park them in a wait on the critsec.  
(also note that this
has the non-ideal property of going back to the calling thread to activate followup work, which we would rather do with a dependency system
to do direct handoff, but that requires more complex mechanisms).
A related issue is that we sometimes don't want to go parallel over all cores, because we are working with large data sets and we can exceed RAM
if we go too wide on our parallelism.  It's catastrophic for performance to exceed RAM and go to swap file, so we would much rather dial down
parallelism.  eg. we often work on dirs containing many 4 GB files at Epic; we'd like to do a parallel_for over files on all of those, but only
as long as we fit in memory, which on something like a ThreadRipper can be lower than core count.
To do that I use a specialized memory limited parallel for.

Each task to be run in the memory_limited_parallel_for must report its memory use before running.  At the start of the parallel_for, the free
physical memory is queried; tasks will be run such that their total reported memory use is <= the initial free physical mem.
The parallel_for then starts tasks, up to a max of core count running at a time, and only if the memory use fits in current available count.
I use a simple greedy scheduler, which runs the largest memory use task which can fit in the current available.  This is not optimal but works okay
in practice.
(in "patcher", memory use and run time of tasks are both proportional to file size, so larger mem use tasks will take longer, so we want to start
the largest mem use tasks as early as possible.  Also when no tasks are running, we always run the largest mem use task, even if its reported mem
use exceeds the total available.)
Something that you find whenever you work with huge amounts of memory is that simply doing the VirtualFree() to free memory is
incredibly slow.  In the patcher, on a 30s run, fully 5s was in a VirtualFree which was on the critical path.
Some quick notes about VirtualAlloc/VirtualFree time, then I'll describe how I solved it in patcher.
VirtualAlloc takes no time and immediately returns you a pointer in virtual address space, but has not actually yet mapped pages of
memory to your process.  That doesn't happen until you actually touch those pages.  So the allocation time shows up as being very fast
and the actual time for it is distributed around your code as you use those pages.
(some people don't like that, so they will start up an async task to scan through the pages and touch them all right after the VirtualAlloc.
That may or may not help your net process time; in some cases it's better to let that work happen on first touch (eg. if you don't always actually
use all the memory you requested).  One big advantage of doing the separate action to touch pages is it's easy to parallelize that work,
and it removes that first-page-touch time from profiles of your other functions, which can make optimizing easier.)
(also large pages make this all better, but aren't practical to use in Windows because they require group policy tokens).
VirtualFree is blocking and slow; it has to go through all the pages mapped to your process and give them back to the system.
First note that if you didn't actually touch any of the pages, then VirtualFree will be fast.  It is
only slow if the pages have actually been mapped to your process.  If you just do a test app that does "VirtualAlloc then VirtualFree" without touching
pages, everything will seem fast.
(there are also issues that can arise with the Windows memory-zeroing of pages which we will not get into here)
You might think that just exiting without freeing, and letting Windows clean up the leaks in ExitProcess would save you from the time to VirtualFree,
but that is not the case.  Windows ExitProcess blocks on freeing all the memory you have allocated, so the net process time is not reduced by leaking
the memory.  (TerminateProcess is the same as ExitProcess in this regard).  You have to measure the time for your process to return to the
calling process.
To be very concrete :
int main(int argc,const char *argv[])
{
    SIZE_T size = 32LL<<30;
    
    void * mem;
    
    {
    SCOPE_LOG_TIMER("alloc");

    mem = VirtualAlloc(NULL,size,MEM_COMMIT|MEM_RESERVE,PAGE_READWRITE);
    }

    if ( do_touch )
    {
        SCOPE_LOG_TIMER("touch");

        char * ptr = (char *)mem;
        char * end = ptr + size;

        while(ptr
<
end)
        {
            *ptr = 0;
            ptr += 4096;
        }
    }

    if ( do_free )
    {
        SCOPE_LOG_TIMER("free");

        VirtualFree(mem,0,MEM_RELEASE);
    }

    return 0;
}
Then we can look at net process time with do_touch and do_free toggled :
c:\src\testproj\x64\release>timerun TestProj.exe
Timer : alloc : 0.000158 s
Timer : touch : 3.098679 s
Timer : free : 2.214244 s
---------------------------------------------
timerun: 5.332 seconds
    -> true allocation time is only seen when you touch pages

c:\src\testproj\x64\release>timerun TestProj.exe
Timer : alloc : 0.000162 s
Timer : touch : 3.089498 s
---------------------------------------------
timerun: 5.433 seconds
    -> 2.4s in process time not in the timers
    ExitProcess *does* stall on the free

c:\src\testproj\x64\release>timerun TestProj.exe
Timer : alloc : 0.000168 s
Timer : free : 0.000082 s
---------------------------------------------
timerun: 0.013 seconds
    -> free is fast if you don't touch pages
So we understand the issue a bit, what can we do about it?
Well, when we free memory, we don't usually need to block on that operation.  The next lines of code don't depend on the free being
fully done, we're just trying to say "I'm done with this, free it sometime".  So the obvious thing to do is to just launch the free
off on an async task, which we don't block on.  We just kick off the async task and let the free complete whenever it manages to do so.
(I call this a "detached" async task, when the handle to it is just dropped and it should delete itself when done).
There is one exception to that, which is the next time we need to allocate a lot of memory, we don't want that to fail (or go to page file)
because we had a detached free that was still pending.  eg. you're on a 128 GB system, you alloc 100 GB then free it, then go to alloc 100 GB again,
you actually now do want that preceding 100 GB free to be done before your next alloc.
This is a problem we can encounter in real runs in patcher, because we are working with very large data sets near RAM size.  To address that
I use what I call "robust detached frees".
For "robust detached frees" we still kick the free off on an async task, but we don't just forget the task handle, instead we keep a list of
pending frees.  As long as we never try to do a big alloc again, then those frees just detach and complete whenever they get around to it.
But, if we try to do an alloc that would cause the net committed memory to exceed physical memory size, then we see if there are any pending frees
that we did before and block on those before doing the alloc.
So further small allocs won't cause us to block on pending frees, but if we do try a big alloc we will wind up blocking.
This typically gets us the benefit of not blocking on the frees on our critical path.
Insert smug self-congratulatory conclusion here.
