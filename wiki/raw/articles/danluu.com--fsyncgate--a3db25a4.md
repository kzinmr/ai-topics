---
title: "errors on fsync are unrecovarable"
url: "https://danluu.com/fsyncgate/"
fetched_at: 2026-05-05T07:01:31.084601+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# errors on fsync are unrecovarable

Source: https://danluu.com/fsyncgate/

This is an archive of the original "fsyncgate" email thread. This is posted here because I wanted to have a link that would fit on a slide for
a talk on file safety
with
a mobile-friendly non-bloated format
.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Subject:Re: PostgreSQL's handling of fsync() errors is unsafe and risks data loss at least on XFS
Date:2018-03-28 02:23:46
Hi all
Some time ago I ran into an issue where a user encountered data corruption after a storage error. PostgreSQL played a part in that corruption by allowing checkpoint what should've been a fatal error.
TL;DR: Pg should PANIC on fsync() EIO return. Retrying fsync() is not OK at least on Linux. When fsync() returns success it means "all writes since the last fsync have hit disk" but we assume it means "all writes since the last SUCCESSFUL fsync have hit disk".
Pg wrote some blocks, which went to OS dirty buffers for writeback. Writeback failed due to an underlying storage error. The block I/O layer and XFS marked the writeback page as failed (AS_EIO), but had no way to tell the app about the failure. When Pg called fsync() on the FD during the next checkpoint, fsync() returned EIO because of the flagged page, to tell Pg that a previous async write failed. Pg treated the checkpoint as failed and didn't advance the redo start position in the control file.
All good so far.
But then we retried the checkpoint, which retried the fsync(). The retry succeeded, because the prior fsync()
cleared the AS_EIO bad page flag
.
The write never made it to disk, but we completed the checkpoint, and merrily carried on our way. Whoops, data loss.
The clear-error-and-continue behaviour of fsync is not documented as far as I can tell. Nor is fsync() returning EIO unless you have a very new linux man-pages with the patch I wrote to add it. But from what I can see in the POSIX standard we are not given any guarantees about what happens on fsync() failure at all, so we're probably wrong to assume that retrying fsync( ) is safe.
If the server had been using ext3 or ext4 with errors=remount-ro, the problem wouldn't have occurred because the first I/O error would've remounted the FS and stopped Pg from continuing. But XFS doesn't have that option. There may be other situations where this can occur too, involving LVM and/or multipath, but I haven't comprehensively dug out the details yet.
It proved possible to recover the system by faking up a backup label from before the first incorrectly-successful checkpoint, forcing redo to repeat and write the lost blocks. But ... what a mess.
I posted about the underlying fsync issue here some time ago:
https://stackoverflow.com/q/42434872/398670
but haven't had a chance to follow up about the Pg specifics.
I've been looking at the problem on and off and haven't come up with a good answer. I think we should just PANIC and let redo sort it out by repeating the failed write when it repeats work since the last checkpoint.
The API offered by async buffered writes and fsync offers us no way to find out which page failed, so we can't just selectively redo that write. I think we do know the relfilenode associated with the fd that failed to fsync, but not much more. So the alternative seems to be some sort of potentially complex online-redo scheme where we replay WAL only the relation on which we had the fsync() error, while otherwise servicing queries normally. That's likely to be extremely error-prone and hard to test, and it's trying to solve a case where on other filesystems the whole DB would grind to a halt anyway.
I looked into whether we can solve it with use of the AIO API instead, but the mess is even worse there - from what I can tell you can't even reliably guarantee fsync at all on all Linux kernel versions.
We already PANIC on fsync() failure for WAL segments. We just need to do the same for data forks at least for EIO. This isn't as bad as it seems because AFAICS fsync only returns EIO in cases where we should be stopping the world anyway, and many FSes will do that for us.
There are rather a lot of pg_fsync() callers. While we could handle this case-by-case for each one, I'm tempted to just make pg_fsync() itself intercept EIO and PANIC. Thoughts?
From:Tom Lane <tgl(at)sss(dot)pgh(dot)pa(dot)us>
Date:2018-03-28 03:53:08
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
Retrying fsync() is not OK at least on Linux. When fsync() returns success it means "all writes since the last fsync have hit disk" but we assume it means "all writes since the last SUCCESSFUL fsync have hit disk".
If that's actually the case, we need to push back on this kernel brain damage, because as you're describing it fsync would be completely useless.
Moreover, POSIX is entirely clear that successful fsync means all preceding writes for the file have been completed, full stop, doesn't matter when they were issued.
From:Michael Paquier <michael(at)paquier(dot)xyz>
Date:2018-03-29 02:30:59
On Tue, Mar 27, 2018 at 11:53:08PM -0400, Tom Lane wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
Any callers of pg_fsync in the backend code are careful enough to check the returned status, sometimes doing retries like in mdsync, so what is proposed here would be a regression.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-03-29 02:48:27
On Thu, Mar 29, 2018 at 3:30 PM, Michael Paquier
wrote:
On Tue, Mar 27, 2018 at 11:53:08PM -0400, Tom Lane wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
Any callers of pg_fsync in the backend code are careful enough to check the returned status, sometimes doing retries like in mdsync, so what is proposed here would be a regression.
Craig, is the phenomenon you described the same as the second issue "Reporting writeback errors" discussed in this article?
https://lwn.net/Articles/724307/
"Current kernels might report a writeback error on an fsync() call, but there are a number of ways in which that can fail to happen."
That's... I'm speechless.
From:Justin Pryzby <pryzby(at)telsasoft(dot)com>
Date:2018-03-29 05:00:31
On Thu, Mar 29, 2018 at 11:30:59AM +0900, Michael Paquier wrote:
On Tue, Mar 27, 2018 at 11:53:08PM -0400, Tom Lane wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
Any callers of pg_fsync in the backend code are careful enough to check the returned status, sometimes doing retries like in mdsync, so what is proposed here would be a regression.
The retries are the source of the problem ; the first fsync() can return EIO, and also
clears the error
causing a 2nd fsync (of the same data) to return success.
(Note, I can see that it might be useful to PANIC on EIO but retry for ENOSPC).
On Thu, Mar 29, 2018 at 03:48:27PM +1300, Thomas Munro wrote:
Craig, is the phenomenon you described the same as the second issue "Reporting writeback errors" discussed in this article?
https://lwn.net/Articles/724307/
Worse, the article acknowledges the behavior without apparently suggesting to change it:
"Storing that value in the file structure has an important benefit: it makes it possible to report a writeback error EXACTLY ONCE TO EVERY PROCESS THAT CALLS FSYNC() .... In current kernels, ONLY THE FIRST CALLER AFTER AN ERROR OCCURS HAS A CHANCE OF SEEING THAT ERROR INFORMATION."
I believe I reproduced the problem behavior using dmsetup "error" target, see attached.
strace looks like this:
kernel is Linux 4.10.0-28-generic #32~16.04.2-Ubuntu SMP Thu Jul 20 10:19:48 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
1open("/dev/mapper/eio", O_RDWR|O_CREAT, 0600) = 3
2write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = 8192
3write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = 8192
4write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = 8192
5write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = 8192
6write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = 8192
7write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = 8192
8write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = 2560
9write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 8192) = -1 ENOSPC (No space left on device)
10dup(2)                                  = 4
11fcntl(4, F_GETFL)                       = 0x8402 (flags O_RDWR|O_APPEND|O_LARGEFILE)
12brk(NULL)                               = 0x1299000
13brk(0x12ba000)                          = 0x12ba000
14fstat(4, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 2), ...}) = 0
15write(4, "write(1): No space left on devic"..., 34write(1): No space left on device
16) = 34
17close(4)                                = 0
18fsync(3)                                = -1 EIO (Input/output error)
19dup(2)                                  = 4
20fcntl(4, F_GETFL)                       = 0x8402 (flags O_RDWR|O_APPEND|O_LARGEFILE)
21fstat(4, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 2), ...}) = 0
22write(4, "fsync(1): Input/output error\n", 29fsync(1): Input/output error
23) = 29
24close(4)                                = 0
25close(3)                                = 0
26open("/dev/mapper/eio", O_RDWR|O_CREAT, 0600) = 3
27fsync(3)                                = 0
28write(3, "\0", 1)                       = 1
29fsync(3)                                = 0
30exit_group(0)                           = ?
2: EIO isn't seen initially due to writeback page cache;
9: ENOSPC due to small device
18: original IO error reported by fsync, good
25: the original FD is closed
26: ..and file reopened
27: fsync on file with still-dirty data+EIO returns success BAD
10, 19: I'm not sure why there's dup(2), I guess glibc thinks that perror should write to a separate FD (?)
Also note, close() ALSO returned success..which you might think exonerates the 2nd fsync(), but I think may itself be problematic, no? In any case, the 2nd byte certainly never got written to DM error, and the failure status was lost following fsync().
I get the exact same behavior if I break after one write() loop, such as to avoid ENOSPC.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-03-29 05:06:22
On Thu, Mar 29, 2018 at 6:00 PM, Justin Pryzby
wrote:
The retries are the source of the problem ; the first fsync() can return EIO, and also
clears the error
causing a 2nd fsync (of the same data) to return success.
What I'm failing to grok here is how that error flag even matters, whether it's a single bit or a counter as described in that patch. If write back failed,
the page is still dirty
. So all future calls to fsync() need to try to try to flush it again, and (presumably) fail again (unless it happens to succeed this time around).
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-03-29 05:25:51
On 29 March 2018 at 13:06, Thomas Munro
wrote:
On Thu, Mar 29, 2018 at 6:00 PM, Justin Pryzby
wrote:
The retries are the source of the problem ; the first fsync() can return EIO, and also
clears the error
causing a 2nd fsync (of the same data) to return success.
What I'm failing to grok here is how that error flag even matters, whether it's a single bit or a counter as described in that patch. If write back failed,
the page is still dirty
. So all future calls to fsync() need to try to try to flush it again, and (presumably) fail again (unless it happens to succeed this time around).
http://www.enterprisedb.com
You'd think so. But it doesn't appear to work that way. You can see yourself with the error device-mapper destination mapped over part of a volume.
I wrote a test case here.
https://github.com/ringerc/scrapcode/blob/master/testcases/fsync-error-clear.c
I don't pretend the kernel behaviour is sane. And it's possible I've made an error in my analysis. But since I've observed this in the wild, and seen it in a test case, I strongly suspect that's what I've described is just what's happening, brain-dead or no.
Presumably the kernel marks the page clean when it dispatches it to the I/O subsystem and doesn't dirty it again on I/O error? I haven't dug that deep on the kernel side. See the stackoverflow post for details on what I found in kernel code analysis.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-03-29 05:32:43
On 29 March 2018 at 10:48, Thomas Munro
wrote:
On Thu, Mar 29, 2018 at 3:30 PM, Michael Paquier
wrote:
On Tue, Mar 27, 2018 at 11:53:08PM -0400, Tom Lane wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
Any callers of pg_fsync in the backend code are careful enough to check the returned status, sometimes doing retries like in mdsync, so what is proposed here would be a regression.
Craig, is the phenomenon you described the same as the second issue "Reporting writeback errors" discussed in this article?
https://lwn.net/Articles/724307/
A variant of it, by the looks.
The problem in our case is that the kernel only tells us about the error once. It then forgets about it. So yes, that seems like a variant of the statement:
"Current kernels might report a writeback error on an fsync() call, but there are a number of ways in which that can fail to happen."
That's... I'm speechless.
Yeah.
It's a bit nuts.
I was astonished when I saw the behaviour, and that it appears undocumented.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-03-29 05:35:47
On 29 March 2018 at 10:30, Michael Paquier
wrote:
On Tue, Mar 27, 2018 at 11:53:08PM -0400, Tom Lane wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
Any callers of pg_fsync in the backend code are careful enough to check the returned status, sometimes doing retries like in mdsync, so what is proposed here would be a regression.
I covered this in my original post.
Yes, we check the return value. But what do we do about it? For fsyncs of heap files, we ERROR, aborting the checkpoint. We'll retry the checkpoint later, which will retry the fsync().
Which will now appear to succeed
because the kernel forgot that it lost our writes after telling us the first time. So we do check the error code, which returns success, and we complete the checkpoint and move on.
But we only retried the fsync, not the writes before the fsync.
So we lost data. Or rather, failed to detect that the kernel did so, so our checkpoint was bad and could not be completed.
The problem is that we keep retrying checkpoints
without
repeating the writes leading up to the checkpoint, and retrying fsync.
I don't pretend the kernel behaviour is sane, but we'd better deal with it anyway.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-03-29 05:58:45
On 28 March 2018 at 11:53, Tom Lane
wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
No. I'm quite serious. Worse, we quite possibly have to do it for ENOSPC as well to avoid similar lost-page-write issues.
It's not necessary on ext3/ext4 with errors=remount-ro, but that's only because the FS stops us dead in our tracks.
I don't pretend it's sane. The kernel behaviour is IMO crazy. If it's going to lose a write, it should at minimum mark the FD as broken so no further fsync() or anything else can succeed on the FD, and an app that cares about durability must repeat the whole set of work since the prior succesful fsync(). Just reporting it once and forgetting it is madness.
But even if we convince the kernel folks of that, how do other platforms behave? And how long before these kernels are out of use? We'd better deal with it, crazy or no.
Please see my StackOverflow post for the kernel-level explanation. Note also the test case link there.
https://stackoverflow.com/a/42436054/398670
Retrying fsync() is not OK at least on Linux. When fsync() returns success it means "all writes since the last fsync have hit disk" but we assume it means "all writes since the last SUCCESSFUL fsync have hit disk".
If that's actually the case, we need to push back on this kernel brain damage, because as you're describing it fsync would be completely useless.
It's not useless, it's just telling us something other than what we think it means. The promise it seems to give us is that if it reports an error once, everything
after
that is useless, so we should throw our toys, close and reopen everything, and redo from the last known-good state.
Though as Tomas posted below, it provides rather weaker guarantees than I thought in some other areas too. See that lwn.net article he linked.
Moreover, POSIX is entirely clear that successful fsync means all preceding writes for the file have been completed, full stop, doesn't matter when they were issued.
I can't find anything that says so to me. Please quote relevant spec.
I'm working from
http://pubs.opengroup.org/onlinepubs/009695399/functions/fsync.html
which states that
"The fsync() function shall request that all data for the open file descriptor named by fildes is to be transferred to the storage device associated with the file described by fildes. The nature of the transfer is implementation-defined. The fsync() function shall not return until the system has completed that action or until an error is detected."
My reading is that POSIX does not specify what happens AFTER an error is detected. It doesn't say that error has to be persistent and that subsequent calls must also report the error. It also says:
"If the fsync() function fails, outstanding I/O operations are not guaranteed to have been completed."
but that doesn't clarify matters much either, because it can be read to mean that once there's been an error reported for some IO operations there's no guarantee those operations are ever completed even after a subsequent fsync returns success.
I'm not seeking to defend what the kernel seems to be doing. Rather, saying that we might see similar behaviour on other platforms, crazy or not. I haven't looked past linux yet, though.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-03-29 12:07:56
On Thu, Mar 29, 2018 at 6:58 PM, Craig Ringer
wrote:
On 28 March 2018 at 11:53, Tom Lane
wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
No. I'm quite serious. Worse, we quite possibly have to do it for ENOSPC as well to avoid similar lost-page-write issues.
I found your discussion with kernel hacker Jeff Layton at
https://lwn.net/Articles/718734/
in which he said: "The stackoverflow writeup seems to want a scheme where pages stay dirty after a writeback failure so that we can try to fsync them again. Note that that has never been the case in Linux after hard writeback failures, AFAIK, so programs should definitely not assume that behavior."
The article above that says the same thing a couple of different ways, ie that writeback failure leaves you with pages that are neither written to disk successfully nor marked dirty.
If I'm reading various articles correctly, the situation was even worse before his errseq_t stuff landed. That fixed cases of completely unreported writeback failures due to sharing of PG_error for both writeback and read errors with certain filesystems, but it doesn't address the clean pages problem.
Yeah, I see why you want to PANIC.
Moreover, POSIX is entirely clear that successful fsync means all preceding writes for the file have been completed, full stop, doesn't matter when they were issued.
I can't find anything that says so to me. Please quote relevant spec.
I'm working from
http://pubs.opengroup.org/onlinepubs/009695399/functions/fsync.html
which states that
"The fsync() function shall request that all data for the open file descriptor named by fildes is to be transferred to the storage device associated with the file described by fildes. The nature of the transfer is implementation-defined. The fsync() function shall not return until the system has completed that action or until an error is detected."
My reading is that POSIX does not specify what happens AFTER an error is detected. It doesn't say that error has to be persistent and that subsequent calls must also report the error. It also says:
FWIW my reading is the same as Tom's. It says "all data for the open file descriptor" without qualification or special treatment after errors. Not "some".
I'm not seeking to defend what the kernel seems to be doing. Rather, saying that we might see similar behaviour on other platforms, crazy or not. I haven't looked past linux yet, though.
I see no reason to think that any other operating system would behave that way without strong evidence... This is openly acknowledged to be "a mess" and "a surprise" in the Filesystem Summit article. I am not really qualified to comment, but from a cursory glance at FreeBSD's vfs_bio.c I think it's doing what you'd hope for... see the code near the comment "Failed write, redirty."
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-03-29 13:15:10
On 29 March 2018 at 20:07, Thomas Munro
wrote:
On Thu, Mar 29, 2018 at 6:58 PM, Craig Ringer
wrote:
On 28 March 2018 at 11:53, Tom Lane
wrote:
Craig Ringer
writes:
TL;DR: Pg should PANIC on fsync() EIO return.
Surely you jest.
No. I'm quite serious. Worse, we quite possibly have to do it for ENOSPC as well to avoid similar lost-page-write issues.
I found your discussion with kernel hacker Jeff Layton at
https://lwn.net/Articles/718734/
in which he said: "The stackoverflow writeup seems to want a scheme where pages stay dirty after a writeback failure so that we can try to fsync them again. Note that that has never been the case in Linux after hard writeback failures, AFAIK, so programs should definitely not assume that behavior."
The article above that says the same thing a couple of different ways, ie that writeback failure leaves you with pages that are neither written to disk successfully nor marked dirty.
If I'm reading various articles correctly, the situation was even worse before his errseq_t stuff landed. That fixed cases of completely unreported writeback failures due to sharing of PG_error for both writeback and read errors with certain filesystems, but it doesn't address the clean pages problem.
Yeah, I see why you want to PANIC.
In more ways than one ;)
I'm not seeking to defend what the kernel seems to be doing. Rather, saying
that we might see similar behaviour on other platforms, crazy or not. I haven't looked past linux yet, though.
I see no reason to think that any other operating system would behave that way without strong evidence... This is openly acknowledged to be "a mess" and "a surprise" in the Filesystem Summit article. I am not really qualified to comment, but from a cursory glance at FreeBSD's vfs_bio.c I think it's doing what you'd hope for... see the code near the comment "Failed write, redirty."
Ok, that's reassuring, but doesn't help us on the platform the great majority of users deploy on :(
"If on Linux, PANIC"
Hrm.
From:Catalin Iacob <iacobcatalin(at)gmail(dot)com>
Date:2018-03-29 16:20:00
On Thu, Mar 29, 2018 at 2:07 PM, Thomas Munro
wrote:
I found your discussion with kernel hacker Jeff Layton at
https://lwn.net/Articles/718734/
in which he said: "The stackoverflow writeup seems to want a scheme where pages stay dirty after a writeback failure so that we can try to fsync them again. Note that that has never been the case in Linux after hard writeback failures, AFAIK, so programs should definitely not assume that behavior."
And a bit below in the same comments, to this question about PG: "So, what are the options at this point? The assumption was that we can repeat the fsync (which as you point out is not the case), or shut down the database and perform recovery from WAL", the same Jeff Layton seems to agree PANIC is the appropriate response: "Replaying the WAL synchronously sounds like the simplest approach when you get an error on fsync. These are uncommon occurrences for the most part, so having to fall back to slow, synchronous error recovery modes when this occurs is probably what you want to do.". And right after, he confirms the errseq_t patches are about always detecting this, not more: "The main thing I working on is to better guarantee is that you actually get an error when this occurs rather than silently corrupting your data. The circumstances where that can occur require some corner-cases, but I think we need to make sure that it doesn't occur."
Jeff's comments in the pull request that merged errseq_t are worth reading as well:
https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=088737f44bbf6378745f5b57b035e57ee3dc4750
The article above that says the same thing a couple of different ways, ie that writeback failure leaves you with pages that are neither written to disk successfully nor marked dirty.
If I'm reading various articles correctly, the situation was even worse before his errseq_t stuff landed. That fixed cases of completely unreported writeback failures due to sharing of PG_error for both writeback and read errors with certain filesystems, but it doesn't address the clean pages problem.
Indeed, that's exactly how I read it as well (opinion formed independently before reading your sentence above). The errseq_t patches landed in v4.13 by the way, so very recently.
Yeah, I see why you want to PANIC.
Indeed. Even doing that leaves question marks about all the kernel versions before v4.13, which at this point is pretty much everything out there, not even detecting this reliably. This is messy.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-03-29 21:18:14
On Fri, Mar 30, 2018 at 5:20 AM, Catalin Iacob
wrote:
Jeff's comments in the pull request that merged errseq_t are worth reading as well:
https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=088737f44bbf6378745f5b57b035e57ee3dc4750
Wow. It looks like there may be a separate question of when each filesystem adopted this new infrastructure?
Yeah, I see why you want to PANIC.
Indeed. Even doing that leaves question marks about all the kernel versions before v4.13, which at this point is pretty much everything out there, not even detecting this reliably. This is messy.
The pre-errseq_t problems are beyond our control. There's nothing we can do about that in userspace (except perhaps abandon OS-buffered IO, a big project). We just need to be aware that this problem exists in certain kernel versions and be grateful to Layton for fixing it.
The dropped dirty flag problem is something we can and in my view should do something about, whatever we might think about that design choice. As Andrew Gierth pointed out to me in an off-list chat about this, by the time you've reached this state, both PostgreSQL's buffer and the kernel's buffer are clean and might be reused for another block at any time, so your data might be gone from the known universe -- we don't even have the option to rewrite our buffers in general. Recovery is the only option.
Thank you to Craig for chasing this down and +1 for his proposal, on Linux only.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-03-31 13:24:28
On Fri, Mar 30, 2018 at 10:18:14AM +1300, Thomas Munro wrote:
Yeah, I see why you want to PANIC.
Indeed. Even doing that leaves question marks about all the kernel versions before v4.13, which at this point is pretty much everything out there, not even detecting this reliably. This is messy.
There may still be a way to reliably detect this on older kernel versions from userspace, but it will be messy whatsoever. On EIO errors, the kernel will not restore the dirty page flags, but it will flip the error flags on the failed pages. One could mmap() the file in question, obtain the PFNs (via /proc/pid/pagemap) and enumerate those to match the ones with the error flag switched on (via /proc/kpageflags). This could serve at least as a detection mechanism, but one could also further use this info to logically map the pages that failed IO back to the original file offsets, and potentially retry IO just for those file ranges that cover the failed pages. Just an idea, not tested.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-03-31 16:13:09
On 31 March 2018 at 21:24, Anthony Iliopoulos
wrote:
On Fri, Mar 30, 2018 at 10:18:14AM +1300, Thomas Munro wrote:
Yeah, I see why you want to PANIC.
Indeed. Even doing that leaves question marks about all the kernel versions before v4.13, which at this point is pretty much everything out there, not even detecting this reliably. This is messy.
There may still be a way to reliably detect this on older kernel versions from userspace, but it will be messy whatsoever. On EIO errors, the kernel will not restore the dirty page flags, but it will flip the error flags on the failed pages. One could mmap() the file in question, obtain the PFNs (via /proc/pid/pagemap) and enumerate those to match the ones with the error flag switched on (via /proc/kpageflags). This could serve at least as a detection mechanism, but one could also further use this info to logically map the pages that failed IO back to the original file offsets, and potentially retry IO just for those file ranges that cover the failed pages. Just an idea, not tested.
That sounds like a huge amount of complexity, with uncertainty as to how it'll behave kernel-to-kernel, for negligble benefit.
I was exploring the idea of doing selective recovery of one relfilenode, based on the assumption that we know the filenode related to the fd that failed to fsync(). We could redo only WAL on that relation. But it fails the same test: it's too complex for a niche case that shouldn't happen in the first place, so it'll probably have bugs, or grow bugs in bitrot over time.
Remember, if you're on ext4 with errors=remount-ro, you get shut down even harder than a PANIC. So we should just use the big hammer here.
I'll send a patch this week.
From:Tom Lane <tgl(at)sss(dot)pgh(dot)pa(dot)us>
Date:2018-03-31 16:38:12
Craig Ringer
writes:
So we should just use the big hammer here.
And bitch, loudly and publicly, about how broken this kernel behavior is. If we make enough of a stink maybe it'll get fixed.
From:Michael Paquier <michael(at)paquier(dot)xyz>
Date:2018-04-01 00:20:38
On Sat, Mar 31, 2018 at 12:38:12PM -0400, Tom Lane wrote:
Craig Ringer
writes:
So we should just use the big hammer here.
And bitch, loudly and publicly, about how broken this kernel behavior is. If we make enough of a stink maybe it'll get fixed.
That won't fix anything released already, so as per the information gathered something has to be done anyway. The discussion of this thread is spreading quite a lot actually.
Handling things at a low-level looks like a better plan for the backend. Tools like pg_basebackup and pg_dump also issue fsync's on the data created, we should do an equivalent for them, with some exit() calls in file_utils.c. As of now failures are logged to stderr but not considered fatal.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-01 00:58:22
On Sun, Apr 01, 2018 at 12:13:09AM +0800, Craig Ringer wrote:
On 31 March 2018 at 21:24, Anthony Iliopoulos <[1]ailiop(at)altatus(dot)com> wrote:
On Fri, Mar 30, 2018 at 10:18:14AM +1300, Thomas Munro wrote:

 > >> Yeah, I see why you want to PANIC.
 > >
 > > Indeed. Even doing that leaves question marks about all the kernel
 > > versions before v4.13, which at this point is pretty much everything
 > > out there, not even detecting this reliably. This is messy.
There may still be a way to reliably detect this on older kernel
 versions from userspace, but it will be messy whatsoever. On EIO
 errors, the kernel will not restore the dirty page flags, but it
 will flip the error flags on the failed pages. One could mmap()
 the file in question, obtain the PFNs (via /proc/pid/pagemap)
 and enumerate those to match the ones with the error flag switched
 on (via /proc/kpageflags). This could serve at least as a detection
 mechanism, but one could also further use this info to logically
 map the pages that failed IO back to the original file offsets,
 and potentially retry IO just for those file ranges that cover
 the failed pages. Just an idea, not tested.
That sounds like a huge amount of complexity, with uncertainty as to how it'll behave kernel-to-kernel, for negligble benefit.
Those interfaces have been around since the kernel 2.6 times and are rather stable, but I was merely responding to your original post comment regarding having a way of finding out which page(s) failed. I assume that indeed there would be no benefit, especially since those errors are usually not transient (typically they come from hard medium faults), and although a filesystem could theoretically mask the error by allocating a different logical block, I am not aware of any implementation that currently does that.
I was exploring the idea of doing selective recovery of one relfilenode, based on the assumption that we know the filenode related to the fd that failed to fsync(). We could redo only WAL on that relation. But it fails the same test: it's too complex for a niche case that shouldn't happen in the first place, so it'll probably have bugs, or grow bugs in bitrot over time.
Fully agree, those cases should be sufficiently rare that a complex and possibly non-maintainable solution is not really warranted.
Remember, if you're on ext4 with errors=remount-ro, you get shut down even harder than a PANIC. So we should just use the big hammer here.
I am not entirely sure what you mean here, does Pg really treat write() errors as fatal? Also, the kind of errors that ext4 detects with this option is at the superblock level and govern metadata rather than actual data writes (recall that those are buffered anyway, no actual device IO has to take place at the time of write()).
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-01 01:14:46
On Sat, Mar 31, 2018 at 12:38:12PM -0400, Tom Lane wrote:
Craig Ringer
writes:
So we should just use the big hammer here.
And bitch, loudly and publicly, about how broken this kernel behavior is. If we make enough of a stink maybe it'll get fixed.
It is not likely to be fixed (beyond what has been done already with the manpage patches and errseq_t fixes on the reporting level). The issue is, the kernel needs to deal with hard IO errors at that level somehow, and since those errors typically persist, re-dirtying the pages would not really solve the problem (unless some filesystem remaps the request to a different block, assuming the device is alive). Keeping around dirty pages that cannot possibly be written out is essentially a memory leak, as those pages would stay around even after the application has exited.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-01 18:24:51
On Fri, Mar 30, 2018 at 10:18 AM, Thomas Munro
wrote:
... on Linux only.
Apparently I was too optimistic. I had looked only at FreeBSD, which keeps the page around and dirties it so we can retry, but the other BSDs apparently don't (FreeBSD changed that in 1999). From what I can tell from the sources below, we have:
Linux, OpenBSD, NetBSD: retrying fsync() after EIO lies
FreeBSD, Illumos: retrying fsync() after EIO tells the truth
Maybe my drive-by assessment of those kernel routines is wrong and someone will correct me, but I'm starting to think you might be better to assume the worst on all systems. Perhaps a GUC that defaults to panicking, so that users on those rare OSes could turn that off? Even then I'm not sure if the failure mode will be that great anyway or if it's worth having two behaviours. Thoughts?
http://mail-index.netbsd.org/netbsd-users/2018/03/30/msg020576.html
https://github.com/NetBSD/src/blob/trunk/sys/kern/vfs_bio.c#L1059
https://github.com/openbsd/src/blob/master/sys/kern/vfs_bio.c#L867
https://github.com/freebsd/freebsd/blob/master/sys/kern/vfs_bio.c#L2631
https://github.com/freebsd/freebsd/commit/e4e8fec98ae986357cdc208b04557dba55a59266
https://github.com/illumos/illumos-gate/blob/master/usr/src/uts/common/os/bio.c#L441
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-02 15:03:42
On 2 April 2018 at 02:24, Thomas Munro
wrote:
Maybe my drive-by assessment of those kernel routines is wrong and someone will correct me, but I'm starting to think you might be better to assume the worst on all systems. Perhaps a GUC that defaults to panicking, so that users on those rare OSes could turn that off? Even then I'm not sure if the failure mode will be that great anyway or if it's worth having two behaviours. Thoughts?
I see little benefit to not just PANICing unconditionally on EIO, really. It shouldn't happen, and if it does, we want to be pretty conservative and adopt a data-protective approach.
I'm rather more worried by doing it on ENOSPC. Which looks like it might be necessary from what I recall finding in my test case + kernel code reading. I really don't want to respond to a possibly-transient ENOSPC by PANICing the whole server unnecessarily.
BTW, the support team at 2ndQ is presently working on two separate issues where ENOSPC resulted in DB corruption, though neither of them involve logs of lost page writes. I'm planning on taking some time tomorrow to write a torture tester for Pg's ENOSPC handling and to verify ENOSPC handling in the test case I linked to in my original StackOverflow post.
If this is just an EIO issue then I see no point doing anything other than PANICing unconditionally.
If it's a concern for ENOSPC too, we should try harder to fail more nicely whenever we possibly can.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-02 18:13:46
Hi,
On 2018-04-01 03:14:46 +0200, Anthony Iliopoulos wrote:
On Sat, Mar 31, 2018 at 12:38:12PM -0400, Tom Lane wrote:
Craig Ringer
writes:
So we should just use the big hammer here.
And bitch, loudly and publicly, about how broken this kernel behavior is. If we make enough of a stink maybe it'll get fixed.
It is not likely to be fixed (beyond what has been done already with the manpage patches and errseq_t fixes on the reporting level). The issue is, the kernel needs to deal with hard IO errors at that level somehow, and since those errors typically persist, re-dirtying the pages would not really solve the problem (unless some filesystem remaps the request to a different block, assuming the device is alive).
Throwing away the dirty pages
and
persisting the error seems a lot more reasonable. Then provide a fcntl (or whatever) extension that can clear the error status in the few cases that the application that wants to gracefully deal with the case.
Keeping around dirty pages that cannot possibly be written out is essentially a memory leak, as those pages would stay around even after the application has exited.
Why do dirty pages need to be kept around in the case of persistent errors? I don't think the lack of automatic recovery in that case is what anybody is complaining about. It's that the error goes away and there's no reasonable way to separate out such an error from some potential transient errors.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-02 18:53:20
On Mon, Apr 02, 2018 at 11:13:46AM -0700, Andres Freund wrote:
Hi,
On 2018-04-01 03:14:46 +0200, Anthony Iliopoulos wrote:
On Sat, Mar 31, 2018 at 12:38:12PM -0400, Tom Lane wrote:
Craig Ringer
writes:
So we should just use the big hammer here.
And bitch, loudly and publicly, about how broken this kernel behavior is. If we make enough of a stink maybe it'll get fixed.
It is not likely to be fixed (beyond what has been done already with the manpage patches and errseq_t fixes on the reporting level). The issue is, the kernel needs to deal with hard IO errors at that level somehow, and since those errors typically persist, re-dirtying the pages would not really solve the problem (unless some filesystem remaps the request to a different block, assuming the device is alive).
Throwing away the dirty pages
and
persisting the error seems a lot more reasonable. Then provide a fcntl (or whatever) extension that can clear the error status in the few cases that the application that wants to gracefully deal with the case.
Given precisely that the dirty pages which cannot been written-out are practically thrown away, the semantics of fsync() (after the 4.13 fixes) are essentially correct: the first call indicates that a writeback error indeed occurred, while subsequent calls have no reason to indicate an error (assuming no other errors occurred in the meantime).
The error reporting is thus consistent with the intended semantics (which are sadly not properly documented). Repeated calls to fsync() simply do not imply that the kernel will retry to writeback the previously-failed pages, so the application needs to be aware of that. Persisting the error at the fsync() level would essentially mean moving application policy into the kernel.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-02 19:32:45
On 2018-04-02 20:53:20 +0200, Anthony Iliopoulos wrote:
On Mon, Apr 02, 2018 at 11:13:46AM -0700, Andres Freund wrote:
Throwing away the dirty pages
and
persisting the error seems a lot more reasonable. Then provide a fcntl (or whatever) extension that can clear the error status in the few cases that the application that wants to gracefully deal with the case.
Given precisely that the dirty pages which cannot been written-out are practically thrown away, the semantics of fsync() (after the 4.13 fixes) are essentially correct: the first call indicates that a writeback error indeed occurred, while subsequent calls have no reason to indicate an error (assuming no other errors occurred in the meantime).
Meh^2.
"no reason" - except that there's absolutely no way to know what state the data is in. And that your application needs explicit handling of such failures. And that one FD might be used in a lots of different parts of the application, that fsyncs in one part of the application might be an ok failure, and in another not. Requiring explicit actions to acknowledge "we've thrown away your data for unknown reason" seems entirely reasonable.
The error reporting is thus consistent with the intended semantics (which are sadly not properly documented). Repeated calls to fsync() simply do not imply that the kernel will retry to writeback the previously-failed pages, so the application needs to be aware of that.
Which isn't what I've suggested.
Persisting the error at the fsync() level would essentially mean moving application policy into the kernel.
Meh.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-02 20:38:06
On Mon, Apr 02, 2018 at 12:32:45PM -0700, Andres Freund wrote:
On 2018-04-02 20:53:20 +0200, Anthony Iliopoulos wrote:
On Mon, Apr 02, 2018 at 11:13:46AM -0700, Andres Freund wrote:
Throwing away the dirty pages
and
persisting the error seems a lot more reasonable. Then provide a fcntl (or whatever) extension that can clear the error status in the few cases that the application that wants to gracefully deal with the case.
Given precisely that the dirty pages which cannot been written-out are practically thrown away, the semantics of fsync() (after the 4.13 fixes) are essentially correct: the first call indicates that a writeback error indeed occurred, while subsequent calls have no reason to indicate an error (assuming no other errors occurred in the meantime).
Meh^2.
"no reason" - except that there's absolutely no way to know what state the data is in. And that your application needs explicit handling of such failures. And that one FD might be used in a lots of different parts of the application, that fsyncs in one part of the application might be an ok failure, and in another not. Requiring explicit actions to acknowledge "we've thrown away your data for unknown reason" seems entirely reasonable.
As long as fsync() indicates error on first invocation, the application is fully aware that between this point of time and the last call to fsync() data has been lost. Persisting this error any further does not change this or add any new info - on the contrary it adds confusion as subsequent write()s and fsync()s on other pages can succeed, but will be reported as failures.
The application will need to deal with that first error irrespective of subsequent return codes from fsync(). Conceptually every fsync() invocation demarcates an epoch for which it reports potential errors, so the caller needs to take responsibility for that particular epoch.
Callers that are not affected by the potential outcome of fsync() and do not react on errors, have no reason for calling it in the first place (and thus masking failure from subsequent callers that may indeed care).
From:Stephen Frost <sfrost(at)snowman(dot)net>
Date:2018-04-02 20:58:08
Greetings,
Anthony Iliopoulos (ailiop(at)altatus(dot)com) wrote:
On Mon, Apr 02, 2018 at 12:32:45PM -0700, Andres Freund wrote:
On 2018-04-02 20:53:20 +0200, Anthony Iliopoulos wrote:
On Mon, Apr 02, 2018 at 11:13:46AM -0700, Andres Freund wrote:
Throwing away the dirty pages
and
persisting the error seems a lot more reasonable. Then provide a fcntl (or whatever) extension that can clear the error status in the few cases that the application that wants to gracefully deal with the case.
Given precisely that the dirty pages which cannot been written-out are practically thrown away, the semantics of fsync() (after the 4.13 fixes) are essentially correct: the first call indicates that a writeback error indeed occurred, while subsequent calls have no reason to indicate an error (assuming no other errors occurred in the meantime).
Meh^2.
"no reason" - except that there's absolutely no way to know what state the data is in. And that your application needs explicit handling of such failures. And that one FD might be used in a lots of different parts of the application, that fsyncs in one part of the application might be an ok failure, and in another not. Requiring explicit actions to acknowledge "we've thrown away your data for unknown reason" seems entirely reasonable.
As long as fsync() indicates error on first invocation, the application is fully aware that between this point of time and the last call to fsync() data has been lost. Persisting this error any further does not change this or add any new info - on the contrary it adds confusion as subsequent write()s and fsync()s on other pages can succeed, but will be reported as failures.
fsync() doesn't reflect the status of given pages, however, it reflects the status of the file descriptor, and as such the file, on which it's called. This notion that fsync() is actually only responsible for the changes which were made to a file since the last fsync() call is pure foolishness. If we were able to pass a list of pages or data ranges to fsync() for it to verify they're on disk then perhaps things would be different, but we can't, all we can do is ask to "please flush all the dirty pages associated with this file descriptor, which represents this file we opened, to disk, and let us know if you were successful."
Give us a way to ask "are these specific pages written out to persistant storage?" and we would certainly be happy to use it, and to repeatedly try to flush out pages which weren't synced to disk due to some transient error, and to track those cases and make sure that we don't incorrectly assume that they've been transferred to persistent storage.
The application will need to deal with that first error irrespective of subsequent return codes from fsync(). Conceptually every fsync() invocation demarcates an epoch for which it reports potential errors, so the caller needs to take responsibility for that particular epoch.
We do deal with that error- by realizing that it failed and later
retrying
the fsync(), which is when we get back an "all good! everything with this file descriptor you've opened is sync'd!" and happily expect that to be truth, when, in reality, it's an unfortunate lie and there are still pages associated with that file descriptor which are, in reality, dirty and not sync'd to disk.
Consider two independent programs where the first one writes to a file and then calls the second one whose job it is to go out and fsync(), perhaps async from the first, those files. Is the second program supposed to go write to each page that the first one wrote to, in order to ensure that all the dirty bits are set so that the fsync() will actually return if all the dirty pages are written?
Callers that are not affected by the potential outcome of fsync() and do not react on errors, have no reason for calling it in the first place (and thus masking failure from subsequent callers that may indeed care).
Reacting on an error from an fsync() call could, based on how it's documented and actually implemented in other OS's, mean "run another fsync() to see if the error has resolved itself." Requiring that to mean "you have to go dirty all of the pages you previously dirtied to actually get a subsequent fsync() to do anything" is really just not reasonable- a given program may have no idea what was written to previously nor any particular reason to need to know, on the expectation that the fsync() call will flush any dirty pages, as it's documented to do.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-02 23:05:44
Hi Stephen,
On Mon, Apr 02, 2018 at 04:58:08PM -0400, Stephen Frost wrote:
fsync() doesn't reflect the status of given pages, however, it reflects the status of the file descriptor, and as such the file, on which it's called. This notion that fsync() is actually only responsible for the changes which were made to a file since the last fsync() call is pure foolishness. If we were able to pass a list of pages or data ranges to fsync() for it to verify they're on disk then perhaps things would be different, but we can't, all we can do is ask to "please flush all the dirty pages associated with this file descriptor, which represents this file we opened, to disk, and let us know if you were successful."
Give us a way to ask "are these specific pages written out to persistant storage?" and we would certainly be happy to use it, and to repeatedly try to flush out pages which weren't synced to disk due to some transient error, and to track those cases and make sure that we don't incorrectly assume that they've been transferred to persistent storage.
Indeed fsync() is simply a rather blunt instrument and a narrow legacy interface but further changing its established semantics (no matter how unreasonable they may be) is probably not the way to go.
Would using sync_file_range() be helpful? Potential errors would only apply to pages that cover the requested file ranges. There are a few caveats though:
(a) it still messes with the top-level error reporting so mixing it with callers that use fsync() and do care about errors will produce the same issue (clearing the error status).
(b) the error-reporting granularity is coarse (failure reporting applies to the entire requested range so you still don't know which particular pages/file sub-ranges failed writeback)
(c) the same "report and forget" semantics apply to repeated invocations of the sync_file_range() call, so again action will need to be taken upon first error encountered for the particular ranges.
The application will need to deal with that first error irrespective of subsequent return codes from fsync(). Conceptually every fsync() invocation demarcates an epoch for which it reports potential errors, so the caller needs to take responsibility for that particular epoch.
We do deal with that error- by realizing that it failed and later
retrying
the fsync(), which is when we get back an "all good! everything with this file descriptor you've opened is sync'd!" and happily expect that to be truth, when, in reality, it's an unfortunate lie and there are still pages associated with that file descriptor which are, in reality, dirty and not sync'd to disk.
It really turns out that this is not how the fsync() semantics work though, exactly because the nature of the errors: even if the kernel retained the dirty bits on the failed pages, retrying persisting them on the same disk location would simply fail. Instead the kernel opts for marking those pages clean (since there is no other recovery strategy), and reporting once to the caller who can potentially deal with it in some manner. It is sadly a bad and undocumented convention.
Consider two independent programs where the first one writes to a file and then calls the second one whose job it is to go out and fsync(), perhaps async from the first, those files. Is the second program supposed to go write to each page that the first one wrote to, in order to ensure that all the dirty bits are set so that the fsync() will actually return if all the dirty pages are written?
I think what you have in mind are the semantics of sync() rather than fsync(), but as long as an application needs to ensure data are persisted to storage, it needs to retain those data in its heap until fsync() is successful instead of discarding them and relying on the kernel after write(). The pattern should be roughly like: write() -> fsync() -> free(), rather than write() -> free() -> fsync(). For example, if a partition gets full upon fsync(), then the application has a chance to persist the data in a different location, while the kernel cannot possibly make this decision and recover.
Callers that are not affected by the potential outcome of fsync() and do not react on errors, have no reason for calling it in the first place (and thus masking failure from subsequent callers that may indeed care).
Reacting on an error from an fsync() call could, based on how it's documented and actually implemented in other OS's, mean "run another fsync() to see if the error has resolved itself." Requiring that to mean "you have to go dirty all of the pages you previously dirtied to actually get a subsequent fsync() to do anything" is really just not reasonable- a given program may have no idea what was written to previously nor any particular reason to need to know, on the expectation that the fsync() call will flush any dirty pages, as it's documented to do.
I think we are conflating a few issues here: having the OS kernel being responsible for error recovery (so that subsequent fsync() would fix the problems) is one. This clearly is a design which most kernels have not really adopted for reasons outlined above (although having the FS layer recovering from hard errors transparently is open for discussion from what it seems [1]). Now, there is the issue of granularity of error reporting: userspace could benefit from a fine-grained indication of failed pages (or file ranges). Another issue is that of reporting semantics (report and clear), which is also a design choice made to avoid having higher-resolution error tracking and the corresponding memory overheads [1].
[1]
https://lwn.net/Articles/718734/
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-02 23:23:24
On 2018-04-03 01:05:44 +0200, Anthony Iliopoulos wrote:
Would using sync_file_range() be helpful? Potential errors would only apply to pages that cover the requested file ranges. There are a few caveats though:
To quote sync_file_range(2):
Warning
       This  system  call  is  extremely  dangerous and should not be used in portable programs.  None of these operations writes out the
       file's metadata.  Therefore, unless the application is strictly performing overwrites of already-instantiated disk  blocks,  there
       are no guarantees that the data will be available after a crash.  There is no user interface to know if a write is purely an over‐
       write.  On filesystems using copy-on-write semantics (e.g., btrfs) an overwrite of existing allocated blocks is impossible.   When
       writing  into  preallocated  space,  many filesystems also require calls into the block allocator, which this system call does not
       sync out to disk.  This system call does not flush disk write caches and thus does not provide any data integrity on systems  with
       volatile disk write caches.
Given the lack of metadata safety that seems entirely a no go. We use sfr(2), but only to force the kernel's hand around writing back earlier without throwing away cache contents.
The application will need to deal with that first error irrespective of subsequent return codes from fsync(). Conceptually every fsync() invocation demarcates an epoch for which it reports potential errors, so the caller needs to take responsibility for that particular epoch.
We do deal with that error- by realizing that it failed and later
retrying
the fsync(), which is when we get back an "all good! everything with this file descriptor you've opened is sync'd!" and happily expect that to be truth, when, in reality, it's an unfortunate lie and there are still pages associated with that file descriptor which are, in reality, dirty and not sync'd to disk.
It really turns out that this is not how the fsync() semantics work though
Except on freebsd and solaris, and perhaps others.
, exactly because the nature of the errors: even if the kernel retained the dirty bits on the failed pages, retrying persisting them on the same disk location would simply fail.
That's not guaranteed at all, think NFS.
Instead the kernel opts for marking those pages clean (since there is no other recovery strategy), and reporting once to the caller who can potentially deal with it in some manner. It is sadly a bad and undocumented convention.
It's broken behaviour justified post facto with the only rational that was available, which explains why it's so unconvincing. You could just say "this ship has sailed, and it's to onerous to change because xxx" and this'd be a done deal. But claiming this is reasonable behaviour is ridiculous.
Again, you could just continue to error for this fd and still throw away the data.
Consider two independent programs where the first one writes to a file and then calls the second one whose job it is to go out and fsync(), perhaps async from the first, those files. Is the second program supposed to go write to each page that the first one wrote to, in order to ensure that all the dirty bits are set so that the fsync() will actually return if all the dirty pages are written?
I think what you have in mind are the semantics of sync() rather than fsync()
If you open the same file with two fds, and write with one, and fsync with another that's definitely supposed to work. And sync() isn't a realistic replacement in any sort of way because it's obviously systemwide, and thus entirely and completely unsuitable. Nor does it have any sort of better error reporting behaviour, does it?
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-02 23:27:35
On 3 April 2018 at 07:05, Anthony Iliopoulos
wrote:
Hi Stephen,
On Mon, Apr 02, 2018 at 04:58:08PM -0400, Stephen Frost wrote:
fsync() doesn't reflect the status of given pages, however, it reflects the status of the file descriptor, and as such the file, on which it's called. This notion that fsync() is actually only responsible for the changes which were made to a file since the last fsync() call is pure foolishness. If we were able to pass a list of pages or data ranges to fsync() for it to verify they're on disk then perhaps things would be different, but we can't, all we can do is ask to "please flush all the dirty pages associated with this file descriptor, which represents this file we opened, to disk, and let us know if you were successful."
Give us a way to ask "are these specific pages written out to persistant storage?" and we would certainly be happy to use it, and to repeatedly try to flush out pages which weren't synced to disk due to some transient error, and to track those cases and make sure that we don't incorrectly assume that they've been transferred to persistent storage.
Indeed fsync() is simply a rather blunt instrument and a narrow legacy interface but further changing its established semantics (no matter how unreasonable they may be) is probably not the way to go.
They're undocumented and extremely surprising semantics that are arguably a violation of the POSIX spec for fsync(), or at least a surprising interpretation of it.
So I don't buy this argument.
It really turns out that this is not how the fsync() semantics work though, exactly because the nature of the errors: even if the kernel retained the dirty bits on the failed pages, retrying persisting them on the same disk location would simply fail.
might
simply fail.
It depends on why the error ocurred.
I originally identified this behaviour on a multipath system. Multipath defaults to "throw the writes away, nobody really cares anyway" on error. It seems to figure a higher level will retry, or the application will receive the error and retry.
(See no_path_retry in multipath config. AFAICS the default is insanely dangerous and only suitable for specialist apps that understand the quirks; you should use no_path_retry=queue).
Instead the kernel opts for marking those pages clean (since there is no other recovery strategy),
and reporting once to the caller who can potentially deal with it in some manner. It is sadly a bad and undocumented convention.
It could mark the FD.
It's not just undocumented, it's a slightly creative interpretation of the POSIX spec for fsync.
Consider two independent programs where the first one writes to a file and then calls the second one whose job it is to go out and fsync(), perhaps async from the first, those files. Is the second program supposed to go write to each page that the first one wrote to, in order to ensure that all the dirty bits are set so that the fsync() will actually return if all the dirty pages are written?
I think what you have in mind are the semantics of sync() rather than fsync(), but as long as an application needs to ensure data are persisted to storage, it needs to retain those data in its heap until fsync() is successful instead of discarding them and relying on the kernel after write().
This is almost exactly what we tell application authors using PostgreSQL: the data isn't written until you receive a successful commit confirmation, so you'd better not forget it.
We provide applications with
clear boundaries
so they can know
exactly
what was, and was not, written. I guess the argument from the kernel is the same is true: whatever was written since the last
successful
fsync is potentially lost and must be redone.
But the fsync behaviour is utterly undocumented and dubiously standard.
I think we are conflating a few issues here: having the OS kernel being responsible for error recovery (so that subsequent fsync() would fix the problems) is one. This clearly is a design which most kernels have not really adopted for reasons outlined above
[citation needed]
What do other major platforms do here? The post above suggests it's a bit of a mix of behaviours.
Now, there is the issue of granularity of error reporting: userspace could benefit from a fine-grained indication of failed pages (or file ranges).
Yep. I looked at AIO in the hopes that, if we used AIO, we'd be able to map a sync failure back to an individual AIO write.
But it seems AIO just adds more problems and fixes none. Flush behaviour with AIO from what I can tell is inconsistent version to version and generally unhelpful. The kernel should really report such sync failures back to the app on its AIO write mapping, but it seems nothing of the sort happens.
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-03 00:03:39
On Apr 2, 2018, at 16:27, Craig Ringer
wrote:
They're undocumented and extremely surprising semantics that are arguably a violation of the POSIX spec for fsync(), or at least a surprising interpretation of it.
Even accepting that (I personally go with surprising over violation, as if my vote counted), it is highly unlikely that we will convince every kernel team to declare "What fools we've been!" and push a change... and even if they did, PostgreSQL can look forward to many years of running on kernels with the broken semantics. Given that, I think the PANIC option is the soundest one, as unappetizing as it is.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-03 00:05:09
On April 2, 2018 5:03:39 PM PDT, Christophe Pettus
wrote:
On Apr 2, 2018, at 16:27, Craig Ringer
wrote:
They're undocumented and extremely surprising semantics that are arguably a violation of the POSIX spec for fsync(), or at least a surprising interpretation of it.
Even accepting that (I personally go with surprising over violation, as if my vote counted), it is highly unlikely that we will convince every kernel team to declare "What fools we've been!" and push a change... and even if they did, PostgreSQL can look forward to many years of running on kernels with the broken semantics. Given that, I think the PANIC option is the soundest one, as unappetizing as it is.
Don't we pretty much already have agreement in that? And Craig is the main proponent of it?
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-03 00:07:41
On Apr 2, 2018, at 17:05, Andres Freund
wrote:
Don't we pretty much already have agreement in that? And Craig is the main proponent of it?
For sure on the second sentence; the first was not clear to me.
From:Peter Geoghegan <pg(at)bowt(dot)ie>
Date:2018-04-03 00:48:00
On Mon, Apr 2, 2018 at 5:05 PM, Andres Freund
wrote:
Even accepting that (I personally go with surprising over violation, as if my vote counted), it is highly unlikely that we will convince every kernel team to declare "What fools we've been!" and push a change... and even if they did, PostgreSQL can look forward to many years of running on kernels with the broken semantics. Given that, I think the PANIC option is the soundest one, as unappetizing as it is.
Don't we pretty much already have agreement in that? And Craig is the main proponent of it?
I wonder how bad it will be in practice if we PANIC. Craig said "This isn't as bad as it seems because AFAICS fsync only returns EIO in cases where we should be stopping the world anyway, and many FSes will do that for us". It would be nice to get more information on that.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-03 01:29:28
On Tue, Apr 3, 2018 at 3:03 AM, Craig Ringer
wrote:
I see little benefit to not just PANICing unconditionally on EIO, really. It shouldn't happen, and if it does, we want to be pretty conservative and adopt a data-protective approach.
I'm rather more worried by doing it on ENOSPC. Which looks like it might be necessary from what I recall finding in my test case + kernel code reading. I really don't want to respond to a possibly-transient ENOSPC by PANICing the whole server unnecessarily.
Yeah, it'd be nice to give an administrator the chance to free up some disk space after ENOSPC is reported, and stay up. Running out of space really shouldn't take down the database without warning! The question is whether the data remains in cache and marked dirty, so that retrying is a safe option (since it's potentially gone from our own buffers, so if the OS doesn't have it the only place your committed data can definitely still be found is the WAL... recovery time). Who can tell us? Do we need a per-filesystem answer? Delayed allocation is a somewhat filesystem-specific thing, so maybe. Interestingly, there don't seem to be many operating systems that can report ENOSPC from fsync(), based on a quick scan through some documentation:
POSIX, AIX, HP-UX, FreeBSD, OpenBSD, NetBSD: no
Illumos/Solaris, Linux, macOS: yes
I don't know if macOS really means it or not; it just tells you to see the errors for read(2) and write(2). By the way, speaking of macOS, I was curious to see if the common BSD heritage would show here. Yeah, somewhat. It doesn't appear to keep buffers on writeback error, if this is the right code
1
.
[1]
https://github.com/apple/darwin-xnu/blob/master/bsd/vfs/vfs_bio.c#L2695
From:Robert Haas <robertmhaas(at)gmail(dot)com>
Date:2018-04-03 02:54:26
On Mon, Apr 2, 2018 at 2:53 PM, Anthony Iliopoulos
wrote:
Given precisely that the dirty pages which cannot been written-out are practically thrown away, the semantics of fsync() (after the 4.13 fixes) are essentially correct: the first call indicates that a writeback error indeed occurred, while subsequent calls have no reason to indicate an error (assuming no other errors occurred in the meantime).
Like other people here, I think this is 100% unreasonable, starting with "the dirty pages which cannot been written out are practically thrown away". Who decided that was OK, and on the basis of what wording in what specification? I think it's always unreasonable to throw away the user's data. If the writes are going to fail, then let them keep on failing every time.
That
wouldn't cause any data loss, because we'd never be able to checkpoint, and eventually the user would have to kill the server uncleanly, and that would trigger recovery.
Also, this really does make it impossible to write reliable programs. Imagine that, while the server is running, somebody runs a program which opens a file in the data directory, calls fsync() on it, and closes it. If the fsync() fails, postgres is now borked and has no way of being aware of the problem. If we knew, we could PANIC, but we'll never find out, because the unrelated process ate the error. This is exactly the sort of ill-considered behavior that makes fcntl() locking nearly useless.
Even leaving that aside, a PANIC means a prolonged outage on a prolonged system - it could easily take tens of minutes or longer to run recovery. So saying "oh, just do that" is not really an answer. Sure, we can do it, but it's like trying to lose weight by intentionally eating a tapeworm. Now, it's possible to shorten the checkpoint_timeout so that recovery runs faster, but then performance drops because data has to be fsync()'d more often instead of getting buffered in the OS cache for the maximum possible time. We could also dodge this issue in another way: suppose that when we write a page out, we don't consider it really written until fsync() succeeds. Then we wouldn't need to PANIC if an fsync() fails; we could just re-write the page. Unfortunately, this would also be terrible for performance, for pretty much the same reasons: letting the OS cache absorb lots of dirty blocks and do write-combining is
necessary
for good performance.
The error reporting is thus consistent with the intended semantics (which are sadly not properly documented). Repeated calls to fsync() simply do not imply that the kernel will retry to writeback the previously-failed pages, so the application needs to be aware of that. Persisting the error at the fsync() level would essentially mean moving application policy into the kernel.
I might accept this argument if I accepted that it was OK to decide that an fsync() failure means you can forget that the write() ever happened in the first place, but it's hard to imagine an application that wants that behavior. If the application didn't care about whether the bytes really got to disk or not, it would not have called fsync() in the first place. If it does care, reporting the error only once is never an improvement.
From:Peter Geoghegan <pg(at)bowt(dot)ie>
Date:2018-04-03 03:45:30
On Mon, Apr 2, 2018 at 7:54 PM, Robert Haas
wrote:
Also, this really does make it impossible to write reliable programs. Imagine that, while the server is running, somebody runs a program which opens a file in the data directory, calls fsync() on it, and closes it. If the fsync() fails, postgres is now borked and has no way of being aware of the problem. If we knew, we could PANIC, but we'll never find out, because the unrelated process ate the error. This is exactly the sort of ill-considered behavior that makes fcntl() locking nearly useless.
I fear that the conventional wisdom from the Kernel people is now "you should be using O_DIRECT for granular control". The LWN article Thomas linked (
https://lwn.net/Articles/718734
) cites Ted Ts'o:
"Monakhov asked why a counter was needed; Layton said it was to handle multiple overlapping writebacks. Effectively, the counter would record whether a writeback had failed since the file was opened or since the last fsync(). Ts'o said that should be fine; applications that want more information should use O_DIRECT. For most applications, knowledge that an error occurred somewhere in the file is all that is necessary; applications that require better granularity already use O_DIRECT."
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-03 10:35:39
Hi Robert,
On Mon, Apr 02, 2018 at 10:54:26PM -0400, Robert Haas wrote:
On Mon, Apr 2, 2018 at 2:53 PM, Anthony Iliopoulos
wrote:
Given precisely that the dirty pages which cannot been written-out are practically thrown away, the semantics of fsync() (after the 4.13 fixes) are essentially correct: the first call indicates that a writeback error indeed occurred, while subsequent calls have no reason to indicate an error (assuming no other errors occurred in the meantime).
Like other people here, I think this is 100% unreasonable, starting with "the dirty pages which cannot been written out are practically thrown away". Who decided that was OK, and on the basis of what wording in what specification? I think it's always unreasonable to
If you insist on strict conformance to POSIX, indeed the linux glibc configuration and associated manpage are probably wrong in stating that _POSIX_SYNCHRONIZED_IO is supported. The implementation matches that of the flexibility allowed by not supporting SIO. There's a long history of brokenness between linux and posix, and I think there was never an intention of conforming to the standard.
throw away the user's data. If the writes are going to fail, then let them keep on failing every time.
That
wouldn't cause any data loss, because we'd never be able to checkpoint, and eventually the user would have to kill the server uncleanly, and that would trigger recovery.
I believe (as tried to explain earlier) there is a certain assumption being made that the writer and original owner of data is responsible for dealing with potential errors in order to avoid data loss (which should be only of interest to the original writer anyway). It would be very questionable for the interface to persist the error while subsequent writes and fsyncs to different offsets may as well go through. Another process may need to write into the file and fsync, while being unaware of those newly introduced semantics is now faced with EIO because some unrelated previous process failed some earlier writes and did not bother to clear the error for those writes. In a similar scenario where the second process is aware of the new semantics, it would naturally go ahead and clear the global error in order to proceed with its own write()+fsync(), which would essentially amount to the same problematic semantics you have now.
Also, this really does make it impossible to write reliable programs. Imagine that, while the server is running, somebody runs a program which opens a file in the data directory, calls fsync() on it, and closes it. If the fsync() fails, postgres is now borked and has no way of being aware of the problem. If we knew, we could PANIC, but we'll never find out, because the unrelated process ate the error. This is exactly the sort of ill-considered behavior that makes fcntl() locking nearly useless.
Fully agree, and the errseq_t fixes have dealt exactly with the issue of making sure that the error is reported to all file descriptors that
happen to be open at the time of error
. But I think one would have a hard time defending a modification to the kernel where this is further extended to cover cases where:
process A does write() on some file offset which fails writeback, fsync() gets EIO and exit()s.
process B does write() on some other offset which succeeds writeback, but fsync() gets EIO due to (uncleared) failures of earlier process.
This would be a highly user-visible change of semantics from edge- triggered to level-triggered behavior.
dodge this issue in another way: suppose that when we write a page out, we don't consider it really written until fsync() succeeds. Then
That's the only way to think about fsync() guarantees unless you are on a kernel that keeps retrying to persist dirty pages. Assuming such a model, after repeated and unrecoverable hard failures the process would have to explicitly inform the kernel to drop the dirty pages. All the process could do at that point is read back to userspace the dirty/failed pages and attempt to rewrite them at a different place (which is current possible too). Most applications would not bother though to inform the kernel and drop the permanently failed pages; and thus someone eventually would hit the case that a large amount of failed writeback pages are running his server out of memory, at which point people will complain that those semantics are completely unreasonable.
we wouldn't need to PANIC if an fsync() fails; we could just re-write the page. Unfortunately, this would also be terrible for performance, for pretty much the same reasons: letting the OS cache absorb lots of dirty blocks and do write-combining is
necessary
for good performance.
Not sure I understand this case. The application may indeed re-write a bunch of pages that have failed and proceed with fsync(). The kernel will deal with combining the writeback of all the re-written pages. But further the necessity of combining for performance really depends on the exact storage medium. At the point you start caring about write-combining, the kernel community will naturally redirect you to use DIRECT_IO.
The error reporting is thus consistent with the intended semantics (which are sadly not properly documented). Repeated calls to fsync() simply do not imply that the kernel will retry to writeback the previously-failed pages, so the application needs to be aware of that. Persisting the error at the fsync() level would essentially mean moving application policy into the kernel.
I might accept this argument if I accepted that it was OK to decide that an fsync() failure means you can forget that the write() ever happened in the first place, but it's hard to imagine an application that wants that behavior. If the application didn't care about whether the bytes really got to disk or not, it would not have called fsync() in the first place. If it does care, reporting the error only once is never an improvement.
Again, conflating two separate issues, that of buffering and retrying failed pages and that of error reporting. Yes it would be convenient for applications not to have to care at all about recovery of failed write-backs, but at some point they would have to face this issue one way or another (I am assuming we are always talking about hard failures, other kinds of failures are probably already being dealt with transparently at the kernel level).
As for the reporting, it is also unreasonable to effectively signal and persist an error on a file-wide granularity while it pertains to subsets of that file and other writes can go through, but I am repeating myself.
I suppose that if the check-and-clear semantics are problematic for Pg, one could suggest a kernel patch that opts-in to a level-triggered reporting of fsync() on a per-descriptor basis, which seems to be non-intrusive and probably sufficient to cover your expected use-case.
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-03 11:26:05
On 3 April 2018 at 11:35, Anthony Iliopoulos
wrote:
Hi Robert,
Fully agree, and the errseq_t fixes have dealt exactly with the issue of making sure that the error is reported to all file descriptors that
happen to be open at the time of error
. But I think one would have a hard time defending a modification to the kernel where this is further extended to cover cases where:
process A does write() on some file offset which fails writeback, fsync() gets EIO and exit()s.
process B does write() on some other offset which succeeds writeback, but fsync() gets EIO due to (uncleared) failures of earlier process.
Surely that's exactly what process B would want? If it calls fsync and gets a success and later finds out that the file is corrupt and didn't match what was in memory it's not going to be happy.
This seems like an attempt to co-opt fsync for a new and different purpose for which it's poorly designed. It's not an async error reporting mechanism for writes. It would be useless as that as any process could come along and open your file and eat the errors for writes you performed. An async error reporting mechanism would have to document which writes it was giving errors for and give you ways to control that.
The semantics described here are useless for everyone. For a program needing to know the error status of the writes it executed, it doesn't know which writes are included in which fsync call. For a program using fsync for its original intended purpose of guaranteeing that the all writes are synced to disk it no longer has any guarantee at all.
This would be a highly user-visible change of semantics from edge- triggered to level-triggered behavior.
It was always documented as level-triggered. This edge-triggered concept is a completely surprise to application writers.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-03 13:36:47
On Tue, Apr 03, 2018 at 12:26:05PM +0100, Greg Stark wrote:
On 3 April 2018 at 11:35, Anthony Iliopoulos
wrote:
Hi Robert,
Fully agree, and the errseq_t fixes have dealt exactly with the issue of making sure that the error is reported to all file descriptors that
happen to be open at the time of error
. But I think one would have a hard time defending a modification to the kernel where this is further extended to cover cases where:
process A does write() on some file offset which fails writeback, fsync() gets EIO and exit()s.
process B does write() on some other offset which succeeds writeback, but fsync() gets EIO due to (uncleared) failures of earlier process.
Surely that's exactly what process B would want? If it calls fsync and gets a success and later finds out that the file is corrupt and didn't match what was in memory it's not going to be happy.
You can't possibly make this assumption. Process B may be reading and writing to completely disjoint regions from those of process A, and as such not really caring about earlier failures, only wanting to ensure its own writes go all the way through. But even if it did care, the file interfaces make no transactional guarantees. Even without fsync() there is nothing preventing process B from reading dirty pages from process A, and based on their content proceed to to its own business and write/persist new data, while process A further modifies the not-yet-flushed pages in-memory before flushing. In this case you'd need explicit synchronization/locking between the processes anyway, so why would fsync() be an exception?
This seems like an attempt to co-opt fsync for a new and different purpose for which it's poorly designed. It's not an async error reporting mechanism for writes. It would be useless as that as any process could come along and open your file and eat the errors for writes you performed. An async error reporting mechanism would have to document which writes it was giving errors for and give you ways to control that.
The errseq_t fixes deal with that; errors will be reported to any process that has an open fd, irrespective to who is the actual caller of the fsync() that may have induced errors. This is anyway required as the kernel may evict dirty pages on its own by doing writeback and as such there needs to be a way to report errors on all open fds.
The semantics described here are useless for everyone. For a program needing to know the error status of the writes it executed, it doesn't know which writes are included in which fsync call. For a program
If EIO persists between invocations until explicitly cleared, a process cannot possibly make any decision as to if it should clear the error and proceed or some other process will need to leverage that without coordination, or which writes actually failed for that matter. We would be back to the case of requiring explicit synchronization between processes that care about this, in which case the processes may as well synchronize over calling fsync() in the first place.
Having an opt-in persisting EIO per-fd would practically be a form of "contract" between "cooperating" processes anyway.
But instead of deconstructing and debating the semantics of the current mechanism, why not come up with the ideal desired form of error reporting/tracking granularity etc., and see how this may be fitted into kernels as a new interface.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-03 14:29:10
On 3 April 2018 at 10:54, Robert Haas
wrote:
I think it's always unreasonable to throw away the user's data.
Well, we do that. If a txn aborts, all writes in the txn are discarded.
I think that's perfectly reasonable. Though we also promise an all or nothing effect, we make exceptions even there.
The FS doesn't offer transactional semantics, but the fsync behaviour can be interpreted kind of similarly.
I don't
agree
with it, but I don't think it's as wholly unreasonable as all that. I think leaving it undocumented is absolutely gobsmacking, and it's dubious at best, but it's not totally insane.
If the writes are going to fail, then let them keep on failing every time.
Like we do, where we require an explicit rollback.
But POSIX may pose issues there, it doesn't really define any interface for that AFAIK. Unless you expect the app to close() and re-open() the file. Replacing one nonstandard issue with another may not be a win.
That
wouldn't cause any data loss, because we'd never be able to checkpoint, and eventually the user would have to kill the server uncleanly, and that would trigger recovery.
Yep. That's what I expected to happen on unrecoverable I/O errors. Because, y'know, unrecoverable.
I was stunned to learn it's not so. And I'm even more amazed to learn that ext4's errors=remount-ro apparently doesn't concern its self with mere user data, and may exhibit the same behaviour - I need to rerun my test case on it tomorrow.
Also, this really does make it impossible to write reliable programs.
In the presence of multiple apps interacting on the same file, yes. I think that's a little bit of a stretch though.
For a single app, you can recover by remembering and redoing all the writes you did.
Sucks if your app wants to have multiple processes working together on a file without some kind of journal or WAL, relying on fsync() alone, mind you. But at least we have WAL.
Hrm. I wonder how this interacts with wal_level=minimal.
Even leaving that aside, a PANIC means a prolonged outage on a prolonged system - it could easily take tens of minutes or longer to run recovery. So saying "oh, just do that" is not really an answer. Sure, we can do it, but it's like trying to lose weight by intentionally eating a tapeworm. Now, it's possible to shorten the checkpoint_timeout so that recovery runs faster, but then performance drops because data has to be fsync()'d more often instead of getting buffered in the OS cache for the maximum possible time.
It's also spikier. Users have more issues with latency with short, frequent checkpoints.
We could also dodge this issue in another way: suppose that when we write a page out, we don't consider it really written until fsync() succeeds. Then we wouldn't need to PANIC if an fsync() fails; we could just re-write the page. Unfortunately, this would also be terrible for performance, for pretty much the same reasons: letting the OS cache absorb lots of dirty blocks and do write-combining is
necessary
for good performance.
Our double-caching is already plenty bad enough anyway, as well.
(Ideally I want to be able to swap buffers between shared_buffers and the OS buffer-cache. Almost like a 2nd level of buffer pinning. When we write out a block, we
transfer
ownership to the OS. Yeah, I'm dreaming. But we'd sure need to be able to trust the OS not to just forget the block then!)
The error reporting is thus consistent with the intended semantics (which are sadly not properly documented). Repeated calls to fsync() simply do not imply that the kernel will retry to writeback the previously-failed pages, so the application needs to be aware of that. Persisting the error at the fsync() level would essentially mean moving application policy into the kernel.
I might accept this argument if I accepted that it was OK to decide that an fsync() failure means you can forget that the write() ever happened in the first place, but it's hard to imagine an application that wants that behavior. If the application didn't care about whether the bytes really got to disk or not, it would not have called fsync() in the first place. If it does care, reporting the error only once is never an improvement.
Many RDBMSes do just that. It's hardly behaviour unique to the kernel. They report an ERROR on a statement in a txn then go on with life, merrily forgetting that anything was ever wrong.
I agree with PostgreSQL's stance that this is wrong. We require an explicit rollback (or ROLLBACK TO SAVEPOINT) to restore the session to a usable state. This is good.
But we're the odd one out there. Almost everyone else does much like what fsync() does on Linux, report the error and forget it.
In any case, we're not going to get anyone to backpatch a fix for this into all kernels, so we're stuck working around it.
I'll do some testing with ENOSPC tomorrow, propose a patch, report back.
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-03 14:37:30
On 3 April 2018 at 14:36, Anthony Iliopoulos
wrote:
If EIO persists between invocations until explicitly cleared, a process cannot possibly make any decision as to if it should clear the error
I still don't understand what "clear the error" means here. The writes still haven't been written out. We don't care about tracking errors, we just care whether all the writes to the file have been flushed to disk. By "clear the error" you mean throw away the dirty pages and revert part of the file to some old data? Why would anyone ever want that?
But instead of deconstructing and debating the semantics of the current mechanism, why not come up with the ideal desired form of error reporting/tracking granularity etc., and see how this may be fitted into kernels as a new interface.
Because Postgres is portable software that won't be able to use some Linux-specific interface. And doesn't really need any granular error reporting system anyways. It just needs to know when all writes have been synced to disk.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-03 16:52:07
On Tue, Apr 03, 2018 at 03:37:30PM +0100, Greg Stark wrote:
On 3 April 2018 at 14:36, Anthony Iliopoulos
wrote:
If EIO persists between invocations until explicitly cleared, a process cannot possibly make any decision as to if it should clear the error
I still don't understand what "clear the error" means here. The writes still haven't been written out. We don't care about tracking errors, we just care whether all the writes to the file have been flushed to disk. By "clear the error" you mean throw away the dirty pages and revert part of the file to some old data? Why would anyone ever want that?
It means that the responsibility of recovering the data is passed back to the application. The writes may never be able to be written out. How would a kernel deal with that? Either discard the data (and have the writer acknowledge) or buffer the data until reboot and simply risk going OOM. It's not what someone would want, but rather
need
to deal with, one way or the other. At least on the application-level there's a fighting chance for restoring to a consistent state. The kernel does not have that opportunity.
But instead of deconstructing and debating the semantics of the current mechanism, why not come up with the ideal desired form of error reporting/tracking granularity etc., and see how this may be fitted into kernels as a new interface.
Because Postgres is portable software that won't be able to use some Linux-specific interface. And doesn't really need any granular error
I don't really follow this argument, Pg is admittedly using non-portable interfaces (e.g the sync_file_range()). While it's nice to avoid platform specific hacks, expecting that the POSIX semantics will be consistent across systems is simply a 90's pipe dream. While it would be lovely to have really consistent interfaces for application writers, this is simply not going to happen any time soon.
And since those problematic semantics of fsync() appear to be prevalent in other systems as well that are not likely to be changed, you cannot rely on preconception that once buffers are handed over to kernel you have a guarantee that they will be eventually persisted no matter what. (Why even bother having fsync() in that case? The kernel would eventually evict and writeback dirty pages anyway. The point of reporting the error back to the application is to give it a chance to recover - the kernel could repeat "fsync()" itself internally if this would solve anything).
reporting system anyways. It just needs to know when all writes have been synced to disk.
Well, it does know when
some
writes have
not
been synced to disk, exactly because the responsibility is passed back to the application. I do realize this puts more burden back to the application, but what would a viable alternative be? Would you rather have a kernel that risks periodically going OOM due to this design decision?
From:Robert Haas <robertmhaas(at)gmail(dot)com>
Date:2018-04-03 21:47:01
On Tue, Apr 3, 2018 at 6:35 AM, Anthony Iliopoulos
wrote:
Like other people here, I think this is 100% unreasonable, starting with "the dirty pages which cannot been written out are practically thrown away". Who decided that was OK, and on the basis of what wording in what specification? I think it's always unreasonable to
If you insist on strict conformance to POSIX, indeed the linux glibc configuration and associated manpage are probably wrong in stating that _POSIX_SYNCHRONIZED_IO is supported. The implementation matches that of the flexibility allowed by not supporting SIO. There's a long history of brokenness between linux and posix, and I think there was never an intention of conforming to the standard.
Well, then the man page probably shouldn't say CONFORMING TO 4.3BSD, POSIX.1-2001, which on the first system I tested, it did. Also, the summary should be changed from the current "fsync, fdatasync - synchronize a file's in-core state with storage device" by adding ", possibly by randomly undoing some of the changes you think you made to the file".
I believe (as tried to explain earlier) there is a certain assumption being made that the writer and original owner of data is responsible for dealing with potential errors in order to avoid data loss (which should be only of interest to the original writer anyway). It would be very questionable for the interface to persist the error while subsequent writes and fsyncs to different offsets may as well go through.
No, that's not questionable at all. fsync() doesn't take any argument saying which part of the file you care about, so the kernel is entirely not entitled to assume it knows to which writes a given fsync() call was intended to apply.
Another process may need to write into the file and fsync, while being unaware of those newly introduced semantics is now faced with EIO because some unrelated previous process failed some earlier writes and did not bother to clear the error for those writes. In a similar scenario where the second process is aware of the new semantics, it would naturally go ahead and clear the global error in order to proceed with its own write()+fsync(), which would essentially amount to the same problematic semantics you have now.
I don't deny that it's possible that somebody could have an application which is utterly indifferent to the fact that earlier modifications to a file failed due to I/O errors, but is A-OK with that as long as later modifications can be flushed to disk, but I don't think that's a normal thing to want.
Also, this really does make it impossible to write reliable programs. Imagine that, while the server is running, somebody runs a program which opens a file in the data directory, calls fsync() on it, and closes it. If the fsync() fails, postgres is now borked and has no way of being aware of the problem. If we knew, we could PANIC, but we'll never find out, because the unrelated process ate the error. This is exactly the sort of ill-considered behavior that makes fcntl() locking nearly useless.
Fully agree, and the errseq_t fixes have dealt exactly with the issue of making sure that the error is reported to all file descriptors that
happen to be open at the time of error
.
Well, in PostgreSQL, we have a background process called the checkpointer which is the process that normally does all of the fsync() calls but only a subset of the write() calls. The checkpointer does not, however, necessarily have every file open all the time, so these fixes aren't sufficient to make sure that the checkpointer ever sees an fsync() failure. What you have (or someone has) basically done here is made an undocumented assumption about which file descriptors might care about a particular error, but it just so happens that PostgreSQL has never conformed to that assumption. You can keep on saying the problem is with our assumptions, but it doesn't seem like a very good guess to me to suppose that we're the only program that has ever made them. The documentation for fsync() gives zero indication that it's edge-triggered, and so complaining that people wouldn't like it if it became level-triggered seems like an ex post facto justification for a poorly-chosen behavior: they probably think (as we did prior to a week ago) that it already is.
Not sure I understand this case. The application may indeed re-write a bunch of pages that have failed and proceed with fsync(). The kernel will deal with combining the writeback of all the re-written pages. But further the necessity of combining for performance really depends on the exact storage medium. At the point you start caring about write-combining, the kernel community will naturally redirect you to use DIRECT_IO.
Well, the way PostgreSQL works today, we typically run with say 8GB of shared_buffers even if the system memory is, say, 200GB. As pages are evicted from our relatively small cache to the operating system, we track which files need to be fsync()'d at checkpoint time, but we don't hold onto the blocks. Until checkpoint time, the operating system is left to decide whether it's better to keep caching the dirty blocks (thus leaving less memory for other things, but possibly allowing write-combining if the blocks are written again) or whether it should clean them to make room for other things. This means that only a small portion of the operating system memory is directly managed by PostgreSQL, while allowing the effective size of our cache to balloon to some very large number if the system isn't under heavy memory pressure.
Now, I hear the DIRECT_IO thing and I assume we're eventually going to have to go that way: Linux kernel developers seem to think that "real men use O_DIRECT" and so if other forms of I/O don't provide useful guarantees, well that's our fault for not using O_DIRECT. That's a political reason, not a technical reason, but it's a reason all the same.
Unfortunately, that is going to add a huge amount of complexity, because if we ran with shared_buffers set to a large percentage of system memory, we couldn't allocate large chunks of memory for sorts and hash tables from the operating system any more. We'd have to allocate it from our own shared_buffers because that's basically all the memory there is and using substantially more might run the system out entirely. So it's a huge, huge architectural change. And even once it's done it is in some ways inferior to what we are doing today -- true, it gives us superior control over writeback timing, but it also makes PostgreSQL play less nicely with other things running on the same machine, because now PostgreSQL has a dedicated chunk of whatever size it has, rather than using some portion of the OS buffer cache that can grow and shrink according to memory needs both of other parts of PostgreSQL and other applications on the system.
I suppose that if the check-and-clear semantics are problematic for Pg, one could suggest a kernel patch that opts-in to a level-triggered reporting of fsync() on a per-descriptor basis, which seems to be non-intrusive and probably sufficient to cover your expected use-case.
That would certainly be better than nothing.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-03 23:59:27
On Tue, Apr 3, 2018 at 1:29 PM, Thomas Munro
wrote:
Interestingly, there don't seem to be many operating systems that can report ENOSPC from fsync(), based on a quick scan through some documentation:
POSIX, AIX, HP-UX, FreeBSD, OpenBSD, NetBSD: no Illumos/Solaris, Linux, macOS: yes
Oops, reading comprehension fail. POSIX yes (since issue 5), via the note that read() and write()'s error conditions can also be returned.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-04 00:56:37
On Tue, Apr 3, 2018 at 05:47:01PM -0400, Robert Haas wrote:
Well, in PostgreSQL, we have a background process called the checkpointer which is the process that normally does all of the fsync() calls but only a subset of the write() calls. The checkpointer does not, however, necessarily have every file open all the time, so these fixes aren't sufficient to make sure that the checkpointer ever sees an fsync() failure.
There has been a lot of focus in this thread on the workflow:
write() -> blocks remain in kernel memory -> fsync() -> panic?
But what happens in this workflow:
write() -> kernel syncs blocks to storage -> fsync()
Is fsync() going to see a "kernel syncs blocks to storage" failure?
There was already discussion that if the fsync() causes the "syncs blocks to storage", fsync() will only report the failure once, but will it see any failure in the second workflow? There is indication that a failed write to storage reports back an error once and clears the dirty flag, but do we know it keeps things around long enough to report an error to a future fsync()?
You would think it does, but I have to ask since our fsync() assumptions have been wrong for so long.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-04 01:54:50
On Wed, Apr 4, 2018 at 12:56 PM, Bruce Momjian
wrote:
There has been a lot of focus in this thread on the workflow:
write() -> blocks remain in kernel memory -> fsync() -> panic?
But what happens in this workflow:
write() -> kernel syncs blocks to storage -> fsync()
Is fsync() going to see a "kernel syncs blocks to storage" failure?
There was already discussion that if the fsync() causes the "syncs blocks to storage", fsync() will only report the failure once, but will it see any failure in the second workflow? There is indication that a failed write to storage reports back an error once and clears the dirty flag, but do we know it keeps things around long enough to report an error to a future fsync()?
You would think it does, but I have to ask since our fsync() assumptions have been wrong for so long.
I believe there were some problems of that nature (with various twists, based on other concurrent activity and possibly different fds), and those problems were fixed by the errseq_t system developed by Jeff Layton in Linux 4.13. Call that "bug #1".
The second issues is that the pages are marked clean after the error is reported, so further attempts to fsync() the data (in our case for a new attempt to checkpoint) will be futile but appear successful. Call that "bug #2", with the proviso that some people apparently think it's reasonable behaviour and not a bug. At least there is a plausible workaround for that: namely the nuclear option proposed by Craig.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-04 02:05:19
On Wed, Apr 4, 2018 at 01:54:50PM +1200, Thomas Munro wrote:
On Wed, Apr 4, 2018 at 12:56 PM, Bruce Momjian
wrote:
There has been a lot of focus in this thread on the workflow:
write() -> blocks remain in kernel memory -> fsync() -> panic?
But what happens in this workflow:
write() -> kernel syncs blocks to storage -> fsync()
Is fsync() going to see a "kernel syncs blocks to storage" failure?
There was already discussion that if the fsync() causes the "syncs blocks to storage", fsync() will only report the failure once, but will it see any failure in the second workflow? There is indication that a failed write to storage reports back an error once and clears the dirty flag, but do we know it keeps things around long enough to report an error to a future fsync()?
You would think it does, but I have to ask since our fsync() assumptions have been wrong for so long.
I believe there were some problems of that nature (with various twists, based on other concurrent activity and possibly different fds), and those problems were fixed by the errseq_t system developed by Jeff Layton in Linux 4.13. Call that "bug #1".
So all our non-cutting-edge Linux systems are vulnerable and there is no workaround Postgres can implement? Wow.
The second issues is that the pages are marked clean after the error is reported, so further attempts to fsync() the data (in our case for a new attempt to checkpoint) will be futile but appear successful. Call that "bug #2", with the proviso that some people apparently think it's reasonable behaviour and not a bug. At least there is a plausible workaround for that: namely the nuclear option proposed by Craig.
Yes, that one I understood.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-04 02:14:28
On Tue, Apr 3, 2018 at 10:05:19PM -0400, Bruce Momjian wrote:
On Wed, Apr 4, 2018 at 01:54:50PM +1200, Thomas Munro wrote:
I believe there were some problems of that nature (with various twists, based on other concurrent activity and possibly different fds), and those problems were fixed by the errseq_t system developed by Jeff Layton in Linux 4.13. Call that "bug #1".
So all our non-cutting-edge Linux systems are vulnerable and there is no workaround Postgres can implement? Wow.
Uh, are you sure it fixes our use-case? From the email description it sounded like it only reported fsync errors for every open file descriptor at the time of the failure, but the checkpoint process might open the file
after
the failure and try to fsync a write that happened
before
the failure.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-04 02:40:16
On 4 April 2018 at 05:47, Robert Haas
wrote:
Now, I hear the DIRECT_IO thing and I assume we're eventually going to have to go that way: Linux kernel developers seem to think that "real men use O_DIRECT" and so if other forms of I/O don't provide useful guarantees, well that's our fault for not using O_DIRECT. That's a political reason, not a technical reason, but it's a reason all the same.
I looked into buffered AIO a while ago, by the way, and just ... hell no. Run, run as fast as you can.
The trouble with direct I/O is that it pushes a
lot
of work back on PostgreSQL regarding knowledge of the storage subsystem, I/O scheduling, etc. It's absurd to have the kernel do this, unless you want it reliable, in which case you bypass it and drive the hardware directly.
We'd need pools of writer threads to deal with all the blocking I/O. It'd be such a nightmare. Hey, why bother having a kernel at all, except for drivers?
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-04 02:44:22
On Wed, Apr 4, 2018 at 2:14 PM, Bruce Momjian
wrote:
On Tue, Apr 3, 2018 at 10:05:19PM -0400, Bruce Momjian wrote:
On Wed, Apr 4, 2018 at 01:54:50PM +1200, Thomas Munro wrote:
I believe there were some problems of that nature (with various twists, based on other concurrent activity and possibly different fds), and those problems were fixed by the errseq_t system developed by Jeff Layton in Linux 4.13. Call that "bug #1".
So all our non-cutting-edge Linux systems are vulnerable and there is no workaround Postgres can implement? Wow.
Uh, are you sure it fixes our use-case? From the email description it sounded like it only reported fsync errors for every open file descriptor at the time of the failure, but the checkpoint process might open the file
after
the failure and try to fsync a write that happened
before
the failure.
I'm not sure of anything. I can see that it's designed to report errors since the last fsync() of the
file
(presumably via any fd), which sounds like the desired behaviour:
https://github.com/torvalds/linux/blob/master/mm/filemap.c#L682
When userland calls fsync (or something like nfsd does the equivalent), we want to report any writeback errors that occurred since the last fsync (or since the file was opened if there haven't been any).
But I'm not sure what the lifetime of the passed-in "file" and more importantly "file->f_wb_err" is. Specifically, what happens to it if no one has the file open at all, between operations? It is reference counted, see fs/file_table.c. I don't know enough about it to comment.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-04 05:29:28
On Wed, Apr 4, 2018 at 2:44 PM, Thomas Munro
wrote:
On Wed, Apr 4, 2018 at 2:14 PM, Bruce Momjian
wrote:
Uh, are you sure it fixes our use-case? From the email description it sounded like it only reported fsync errors for every open file descriptor at the time of the failure, but the checkpoint process might open the file
after
the failure and try to fsync a write that happened
before
the failure.
I'm not sure of anything. I can see that it's designed to report errors since the last fsync() of the
file
(presumably via any fd), which sounds like the desired behaviour:
[..]
Scratch that. Whenever you open a file descriptor you can't see any preceding errors at all, because:
/* Ensure that we skip any errors that predate opening of the file */
f->f_wb_err = filemap_sample_wb_err(f->f_mapping);
https://github.com/torvalds/linux/blob/master/fs/open.c#L752
Our whole design is based on being able to open, close and reopen files at will from any process, and in particular to fsync() from a different process that didn't inherit the fd but instead opened it later. But it looks like that might be able to eat errors that occurred during asynchronous writeback (when there was nobody to report them to), before you opened the file?
If so I'm not sure how that can possibly be considered to be an implementation of _POSIX_SYNCHRONIZED_IO: "the fsync() function shall force all currently queued I/O operations associated with the file indicated by file descriptor fildes to the synchronized I/O completion state." Note "the file", not "this file descriptor + copies", and without reference to when you opened it.
But I'm not sure what the lifetime of the passed-in "file" and more importantly "file->f_wb_err" is.
It's really inode->i_mapping->wb_err's lifetime that I should have been asking about there, not file->f_wb_err, but I see now that that question is irrelevant due to the above.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-04 06:00:21
On 4 April 2018 at 13:29, Thomas Munro
wrote:
On Wed, Apr 4, 2018 at 2:44 PM, Thomas Munro
wrote:
On Wed, Apr 4, 2018 at 2:14 PM, Bruce Momjian
wrote:
Uh, are you sure it fixes our use-case? From the email description it sounded like it only reported fsync errors for every open file descriptor at the time of the failure, but the checkpoint process might open the file
after
the failure and try to fsync a write that happened
before
the failure.
I'm not sure of anything. I can see that it's designed to report errors since the last fsync() of the
file
(presumably via any fd), which sounds like the desired behaviour:
[..]
Scratch that. Whenever you open a file descriptor you can't see any preceding errors at all, because:
/* Ensure that we skip any errors that predate opening of the file */ f->f_wb_err = filemap_sample_wb_err(f->f_mapping);
https://github.com/torvalds/linux/blob/master/fs/open.c#L752
Our whole design is based on being able to open, close and reopen files at will from any process, and in particular to fsync() from a different process that didn't inherit the fd but instead opened it later. But it looks like that might be able to eat errors that occurred during asynchronous writeback (when there was nobody to report them to), before you opened the file?
Holy hell. So even PANICing on fsync() isn't sufficient, because the kernel will deliberately hide writeback errors that predate our fsync() call from us?
I'll see if I can expand my testcase for that. I'm presently dockerizing it to make it easier for others to use, but that turns out to be a major pain when using devmapper etc. Docker in privileged mode doesn't seem to play nice with device-mapper.
Does that mean that the ONLY ways to do reliable I/O are:
single-process, single-file-descriptor write() then fsync(); on failure, retry all work since last successful fsync()
direct I/O
?
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-04 07:32:04
On Wed, Apr 4, 2018 at 6:00 PM, Craig Ringer
wrote:
On 4 April 2018 at 13:29, Thomas Munro
wrote:
/* Ensure that we skip any errors that predate opening of the file */ f->f_wb_err = filemap_sample_wb_err(f->f_mapping);
[...]
Holy hell. So even PANICing on fsync() isn't sufficient, because the kernel will deliberately hide writeback errors that predate our fsync() call from us?
Predates the opening of the file by the process that calls fsync(). Yeah, it sure looks that way based on the above code fragment. Does anyone know better?
Does that mean that the ONLY ways to do reliable I/O are:
single-process, single-file-descriptor write() then fsync(); on failure, retry all work since last successful fsync()
I suppose you could some up with some crazy complicated IPC scheme to make sure that the checkpointer always has an fd older than any writes to be flushed, with some fallback strategy for when it can't take any more fds.
I haven't got any good ideas right now.
As a bit of an aside, I gather that when you resize files (think truncating/extending relation files) you still need to call fsync() even if you read/write all data with O_DIRECT, to make it flush the filesystem meta-data. I have no idea if that could also be affected by eaten writeback errors.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-04 07:51:53
On 4 April 2018 at 14:00, Craig Ringer
wrote:
On 4 April 2018 at 13:29, Thomas Munro
wrote:
On Wed, Apr 4, 2018 at 2:44 PM, Thomas Munro
wrote:
On Wed, Apr 4, 2018 at 2:14 PM, Bruce Momjian
wrote:
Uh, are you sure it fixes our use-case? From the email description it sounded like it only reported fsync errors for every open file descriptor at the time of the failure, but the checkpoint process might open the file
after
the failure and try to fsync a write that happened
before
the failure.
I'm not sure of anything. I can see that it's designed to report errors since the last fsync() of the
file
(presumably via any fd), which sounds like the desired behaviour:
[..]
Scratch that. Whenever you open a file descriptor you can't see any preceding errors at all, because:
/* Ensure that we skip any errors that predate opening of the file */ f->f_wb_err = filemap_sample_wb_err(f->f_mapping);
https://github.com/torvalds/linux/blob/master/fs/open.c#L752
Our whole design is based on being able to open, close and reopen files at will from any process, and in particular to fsync() from a different process that didn't inherit the fd but instead opened it later. But it looks like that might be able to eat errors that occurred during asynchronous writeback (when there was nobody to report them to), before you opened the file?
Holy hell. So even PANICing on fsync() isn't sufficient, because the kernel will deliberately hide writeback errors that predate our fsync() call from us?
I'll see if I can expand my testcase for that. I'm presently dockerizing it to make it easier for others to use, but that turns out to be a major pain when using devmapper etc. Docker in privileged mode doesn't seem to play nice with device-mapper.
Done, you can find it in
https://github.com/ringerc/scrapcode/tree/master/testcases/fsync-error-clear
now.
Warning, this runs a Docker container in privileged mode on your system, and it uses devicemapper. Read it before you run it, and while I've tried to keep it safe, beware that it might eat your system.
For now it tests only xfs and EIO. Other FSs should be easy enough.
I haven't added coverage for multi-processing yet, but given what you found above, I should. I'll probably just system() a copy of the same proc with instructions to only fsync(). I'll do that next.
I haven't worked out a reliable way to trigger ENOSPC on fsync() yet, when mapping without the error hole. It happens sometimes but I don't know why, it almost always happens on write() instead. I know it can happen on nfs, but I'm hoping for a saner example than that to test with. ext4 and xfs do delayed allocation but eager reservation so it shouldn't happen to them.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-04 13:49:38
On Wed, Apr 4, 2018 at 07:32:04PM +1200, Thomas Munro wrote:
On Wed, Apr 4, 2018 at 6:00 PM, Craig Ringer
wrote:
On 4 April 2018 at 13:29, Thomas Munro
wrote:
/* Ensure that we skip any errors that predate opening of the file */ f->f_wb_err = filemap_sample_wb_err(f->f_mapping);
[...]
Holy hell. So even PANICing on fsync() isn't sufficient, because the kernel will deliberately hide writeback errors that predate our fsync() call from us?
Predates the opening of the file by the process that calls fsync(). Yeah, it sure looks that way based on the above code fragment. Does anyone know better?
Uh, just to clarify, what is new here is that it is ignoring any
errors
that happened before the open(). It is not ignoring write()'s that happened but have not been written to storage before the open().
FYI, pg_test_fsync has always tested the ability to fsync() writes() from from other processes:
Test if fsync on non-write file descriptor is honored:
(If the times are similar, fsync() can sync data written on a different
descriptor.)
    write, fsync, close                5360.341 ops/sec     187 usecs/op
    write, close, fsync                4785.240 ops/sec     209 usecs/op
Those two numbers should be similar. I added this as a check to make sure the behavior we were relying on was working. I never tested sync errors though.
I think the fundamental issue is that we always assumed that writes to the kernel that could not be written to storage would remain in the kernel until they succeeded, and that fsync() would report their existence.
I can understand why kernel developers don't want to keep failed sync buffers in memory, and once they are gone we lose reporting of their failure. Also, if the kernel is going to not retry the syncs, how long should it keep reporting the sync failure? To the first fsync that happens after the failure? How long should it continue to record the failure? What if no fsync() every happens, which is likely for non-Postgres workloads? I think once they decided to discard failed syncs and not retry them, the fsync behavior we are complaining about was almost required.
Our only option might be to tell administrators to closely watch for kernel write failure messages, and then restore or failover. :-(
The last time I remember being this surprised about storage was in the early Postgres years when we learned that just because the BSD file system uses 8k pages doesn't mean those are atomically written to storage. We knew the operating system wrote the data in 8k chunks to storage but:
the 8k pages are written as separate 512-byte sectors
the 8k might be contiguous logically on the drive but not physically
even 512-byte sectors are not written atomically
This is why we added pre-page images are written to WAL, which is what full_page_writes controls.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-04 13:53:01
On Wed, Apr 4, 2018 at 10:40:16AM +0800, Craig Ringer wrote:
The trouble with direct I/O is that it pushes a
lot
of work back on PostgreSQL regarding knowledge of the storage subsystem, I/O scheduling, etc. It's absurd to have the kernel do this, unless you want it reliable, in which case you bypass it and drive the hardware directly.
We'd need pools of writer threads to deal with all the blocking I/O. It'd be such a nightmare. Hey, why bother having a kernel at all, except for drivers?
I believe this is how Oracle views the kernel, so there is precedent for this approach, though I am not advocating it.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-04 14:00:15
On 4 April 2018 at 15:51, Craig Ringer
wrote:
On 4 April 2018 at 14:00, Craig Ringer
wrote:
On 4 April 2018 at 13:29, Thomas Munro
wrote:
On Wed, Apr 4, 2018 at 2:44 PM, Thomas Munro
wrote:
On Wed, Apr 4, 2018 at 2:14 PM, Bruce Momjian
wrote:
Uh, are you sure it fixes our use-case? From the email description it sounded like it only reported fsync errors for every open file descriptor at the time of the failure, but the checkpoint process might open the file
after
the failure and try to fsync a write that happened
before
the failure.
I'm not sure of anything. I can see that it's designed to report errors since the last fsync() of the
file
(presumably via any fd), which sounds like the desired behaviour:
[..]
Scratch that. Whenever you open a file descriptor you can't see any preceding errors at all, because:
/* Ensure that we skip any errors that predate opening of the file */ f->f_wb_err = filemap_sample_wb_err(f->f_mapping);
https://github.com/torvalds/linux/blob/master/fs/open.c#L752
Our whole design is based on being able to open, close and reopen files at will from any process, and in particular to fsync() from a different process that didn't inherit the fd but instead opened it later. But it looks like that might be able to eat errors that occurred during asynchronous writeback (when there was nobody to report them to), before you opened the file?
Holy hell. So even PANICing on fsync() isn't sufficient, because the kernel will deliberately hide writeback errors that predate our fsync() call from us?
I'll see if I can expand my testcase for that. I'm presently dockerizing it to make it easier for others to use, but that turns out to be a major pain when using devmapper etc. Docker in privileged mode doesn't seem to play nice with device-mapper.
Done, you can find it in
https://github.com/ringerc/scrapcode/tree/master/
testcases/fsync-error-clear now.
Update. Now supports multiple FSes.
I've tried xfs, jfs, ext3, ext4, even vfat. All behave the same on EIO. Didn't try zfs-on-linux or other platforms yet.
Still working on getting ENOSPC on fsync() rather than write(). Kernel code reading suggests this is possible, but all the above FSes reserve space eagerly on write( ) even if they do delayed allocation of the actual storage, so it doesn't seem to happen at least in my simple single-process test.
I'm not overly inclined to complain about a fsync() succeeding after a write() error. That seems reasonable enough, the kernel told the app at the time of the failure. What else is it going to do? I don't personally even object hugely to the current fsync() behaviour if it were, say, DOCUMENTED and conformant to the relevant standards, though not giving us any sane way to find out the affected file ranges makes it drastically harder to recover sensibly.
But what's come out since on this thread, that we cannot even rely on fsync() giving us an EIO
once
when it loses our data, because:
all currently widely deployed kernels can fail to deliver info due to recently fixed limitation; and
the kernel deliberately hides errors from us if they relate to writes that occurred before we opened the FD (?)
... that's really troubling. I thought we could at least fix this by PANICing on EIO, and was mostly worried about ENOSPC. But now it seems we can't even do that and expect reliability. So how the @#$ are we meant to do?
It's the error reporting issues around closing and reopening files with outstanding buffered I/O that's really going to hurt us here. I'll be expanding my test case to cover that shortly.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-04 14:09:09
On 4 April 2018 at 22:00, Craig Ringer
wrote:
It's the error reporting issues around closing and reopening files with outstanding buffered I/O that's really going to hurt us here. I'll be expanding my test case to cover that shortly.
Also, just to be clear, this is not in any way confined to xfs and/or lvm as I originally thought it might be.
Nor is ext3/ext4's errors=remount-ro protective. data_err=abort doesn't help either (so what does it do?).
What bewilders me is that running with data=journal doesn't seem to be safe either. WTF?
[26438.846111] EXT4-fs (dm-0): mounted filesystem with journalled data
mode. Opts: errors=remount-ro,data_err=abort,data=journal
[26454.125319] EXT4-fs warning (device dm-0): ext4_end_bio:323: I/O error
10 writing to inode 12 (offset 0 size 0 starting block 59393)
[26454.125326] Buffer I/O error on device dm-0, logical block 59393
[26454.125337] Buffer I/O error on device dm-0, logical block 59394
[26454.125343] Buffer I/O error on device dm-0, logical block 59395
[26454.125350] Buffer I/O error on device dm-0, logical block 59396
and splat, there goes your data anyway.
It's possible that this is in some way related to using the device-mapper "error" target and a loopback device in testing. But I don't really see how.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-04 14:25:47
On Wed, Apr 4, 2018 at 10:09:09PM +0800, Craig Ringer wrote:
On 4 April 2018 at 22:00, Craig Ringer
wrote:
It's the error reporting issues around closing and reopening files with
outstanding buffered I/O that's really going to hurt us here. I'll be
expanding my test case to cover that shortly.
Also, just to be clear, this is not in any way confined to xfs and/or lvm as I originally thought it might be.
Nor is ext3/ext4's errors=remount-ro protective. data_err=abort doesn't help either (so what does it do?).
Anthony Iliopoulos reported in this thread that errors=remount-ro is only affected by metadata writes.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-04 14:42:18
On 4 April 2018 at 22:25, Bruce Momjian
wrote:
On Wed, Apr 4, 2018 at 10:09:09PM +0800, Craig Ringer wrote:
On 4 April 2018 at 22:00, Craig Ringer
wrote:
It's the error reporting issues around closing and reopening files with
outstanding buffered I/O that's really going to hurt us here. I'll be
expanding my test case to cover that shortly.
Also, just to be clear, this is not in any way confined to xfs and/or lvm as I originally thought it might be.
Nor is ext3/ext4's errors=remount-ro protective. data_err=abort doesn't help either (so what does it do?).
Anthony Iliopoulos reported in this thread that errors=remount-ro is only affected by metadata writes.
Yep, I gathered. I was referring to data_err.
From:Antonis Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-04 15:23:31
On Wed, Apr 4, 2018 at 4:42 PM, Craig Ringer
wrote:
On 4 April 2018 at 22:25, Bruce Momjian
wrote:
On Wed, Apr 4, 2018 at 10:09:09PM +0800, Craig Ringer wrote:
On 4 April 2018 at 22:00, Craig Ringer
wrote:
It's the error reporting issues around closing and reopening files with outstanding buffered I/O that's really going to hurt us here. I'll be expanding my test case to cover that shortly.
Also, just to be clear, this is not in any way confined to xfs and/or lvm as I originally thought it might be.
Nor is ext3/ext4's errors=remount-ro protective. data_err=abort doesn't help either (so what does it do?).
Anthony Iliopoulos reported in this thread that errors=remount-ro is only affected by metadata writes.
Yep, I gathered. I was referring to data_err.
As far as I recall data_err=abort pertains to the jbd2 handling of potential writeback errors. Jbd2 will inetrnally attempt to drain the data upon txn commit (and it's even kind enough to restore the EIO at the address space level, that otherwise would get eaten).
When data_err=abort is set, then jbd2 forcibly shuts down the entire journal, with the error being propagated upwards to ext4. I am not sure at which point this would be manifested to userspace and how, but in principle any subsequent fs operations would get some filesystem error due to the journal being down (I would assume similar to remounting the fs read-only).
Since you are using data=journal, I would indeed expect to see something more than what you saw in dmesg.
I can have a look later, I plan to also respond to some of the other interesting issues that you guys raised in the thread.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-04 15:23:51
On 4 April 2018 at 21:49, Bruce Momjian
wrote:
On Wed, Apr 4, 2018 at 07:32:04PM +1200, Thomas Munro wrote:
On Wed, Apr 4, 2018 at 6:00 PM, Craig Ringer
wrote:
On 4 April 2018 at 13:29, Thomas Munro
wrote:
/* Ensure that we skip any errors that predate opening of the file */ f->f_wb_err = filemap_sample_wb_err(f->f_mapping);
[...]
Holy hell. So even PANICing on fsync() isn't sufficient, because the kernel will deliberately hide writeback errors that predate our fsync() call from us?
Predates the opening of the file by the process that calls fsync(). Yeah, it sure looks that way based on the above code fragment. Does anyone know better?
Uh, just to clarify, what is new here is that it is ignoring any
errors
that happened before the open(). It is not ignoring write()'s that happened but have not been written to storage before the open().
FYI, pg_test_fsync has always tested the ability to fsync() writes() from from other processes:
Test if fsync on non-write file descriptor is honored:
    (If the times are similar, fsync() can sync data written on a
different descriptor.) write, fsync, close 5360.341 ops/sec 187 usecs/op write, close, fsync 4785.240 ops/sec 209 usecs/op
Those two numbers should be similar. I added this as a check to make sure the behavior we were relying on was working. I never tested sync errors though.
I think the fundamental issue is that we always assumed that writes to the kernel that could not be written to storage would remain in the kernel until they succeeded, and that fsync() would report their existence.
I can understand why kernel developers don't want to keep failed sync buffers in memory, and once they are gone we lose reporting of their failure. Also, if the kernel is going to not retry the syncs, how long should it keep reporting the sync failure?
Ideally until the app tells it not to.
But there's no standard API for that.
The obvious answer seems to be "until the FD is closed". But we just discussed how Pg relies on being able to open and close files freely. That may not be as reasonable a thing to do as we thought it was when you consider error reporting. What's the kernel meant to do? How long should it remember "I had an error while doing writeback on this file"? Should it flag the file metadata and remember across reboots? Obviously not, but where does it stop? Tell the next program that does an fsync() and forget? How could it associate a dirty buffer on a file with no open FDs with any particular program at all? And what if the app did a write then closed the file and went away, never to bother to check the file again, like most apps do?
Some I/O errors are transient (network issue, etc). Some are recoverable with some sort of action, like disk space issues, but may take a long time before an admin steps in. Some are entirely unrecoverable (disk 1 in striped array is on fire) and there's no possible recovery. Currently we kind of hope the kernel will deal with figuring out which is which and retrying. Turns out it doesn't do that so much, and I don't think the reasons for that are wholly unreasonable. We may have been asking too much.
That does leave us in a pickle when it comes to the checkpointer and opening/closing FDs. I don't know what the "right" thing for the kernel to do from our perspective even is here, but the best I can come up with is actually pretty close to what it does now. Report the fsync() error to the first process that does an fsync() since the writeback error if one has occurred, then forget about it. Ideally I'd have liked it to mark all FDs pointing to the file with a flag to report EIO on next fsync too, but it turns out that won't even help us due to our opening and closing behaviour, so we're going to have to take responsibility for handling and communicating that ourselves, preventing checkpoint completion if any backend gets an fsync error. Probably by PANICing. Some extra work may be needed to ensure reliable ordering and stop checkpoints completing if their fsync() succeeds due to a recent failed fsync() on a normal backend that hasn't PANICed or where the postmaster hasn't noticed yet.
Our only option might be to tell administrators to closely watch for > kernel write failure messages, and then restore or failover. :-( >
Speaking of, there's not necessarily any lost page write error in the logs AFAICS. My tests often just show "Buffer I/O error on device dm-0, logical block 59393" or the like.
From:Gasper Zejn <zejn(at)owca(dot)info>
Date:2018-04-04 17:23:58
On 04. 04. 2018 15:49, Bruce Momjian wrote:
I can understand why kernel developers don't want to keep failed sync buffers in memory, and once they are gone we lose reporting of their failure. Also, if the kernel is going to not retry the syncs, how long should it keep reporting the sync failure? To the first fsync that happens after the failure? How long should it continue to record the failure? What if no fsync() every happens, which is likely for non-Postgres workloads? I think once they decided to discard failed syncs and not retry them, the fsync behavior we are complaining about was almost required.
Ideally the kernel would keep its data for as little time as possible. With fsync, it doesn't really know which process is interested in knowing about a write error, it just assumes the caller will know how to deal with it. Most unfortunate issue is there's no way to get information about a write error.
Thinking aloud - couldn't/shouldn't a write error also be a file system event reported by inotify? Admittedly that's only a thing on Linux, but still.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-04 17:51:03
On Wed, Apr 4, 2018 at 11:23:51PM +0800, Craig Ringer wrote:
On 4 April 2018 at 21:49, Bruce Momjian
wrote:
I can understand why kernel developers don't want to keep failed sync buffers in memory, and once they are gone we lose reporting of their failure. Also, if the kernel is going to not retry the syncs, how long should it keep reporting the sync failure?
Ideally until the app tells it not to.
But there's no standard API for that.
You would almost need an API that registers
before
the failure that you care about sync failures, and that you plan to call fsync() to gather such information. I am not sure how you would allow more than the first fsync() to see the failure unless you added
another
API to clear the fsync failure, but I don't see the point since the first fsync() might call that clear function. How many applications are going to know there is
another
application that cares about the failure? Not many.
Currently we kind of hope the kernel will deal with figuring out which is which and retrying. Turns out it doesn't do that so much, and I don't think the reasons for that are wholly unreasonable. We may have been asking too much.
Agreed.
Our only option might be to tell administrators to closely watch for kernel write failure messages, and then restore or failover. :-(
Speaking of, there's not necessarily any lost page write error in the logs AFAICS. My tests often just show "Buffer I/O error on device dm-0, logical block 59393" or the like.
I assume that is the kernel logs. I am thinking the kernel logs have to be monitored, but how many administrators do that? The other issue I think you are pointing out is how is the administrator going to know this is a Postgres file? I guess any sync error to a device that contains Postgres has to assume Postgres is corrupted. :-(
see explicit treatment of retrying, though I'm not entirely sure if the retry flag is set just for async write-back), and apparently unlike every other kernel I've tried to grok so far (things descended from ancestral BSD but not descended from FreeBSD, with macOS/Darwin apparently in the first category for this purpose).
Here's a new ticket in the NetBSD bug database for this stuff:
http://gnats.netbsd.org/53152
As mentioned in that ticket and by Andres earlier in this thread, keeping the page dirty isn't the only strategy that would work and may be problematic in different ways (it tells the truth but floods your cache with unflushable stuff until eventually you force unmount it and your buffers are eventually invalidated after ENXIO errors? I don't know.). I have no qualified opinion on that. I just know that we need a way for fsync() to tell the truth about all preceding writes or our checkpoints are busted.
*We mmap() + msync() in pg_flush_data() if you don't have sync_file_range(), and I see now that that is probably not a great idea on ZFS because you'll finish up double-buffering (or is that triple-buffering?), flooding your page cache with transient data. Oops. That is off-topic and not relevant for the checkpoint correctness topic of this thread through, since pg_flush_data() is advisory only.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-04 22:14:24
On Thu, Apr 5, 2018 at 9:28 AM, Thomas Munro
wrote:
On Thu, Apr 5, 2018 at 2:00 AM, Craig Ringer
wrote:
I've tried xfs, jfs, ext3, ext4, even vfat. All behave the same on EIO. Didn't try zfs-on-linux or other platforms yet.
While contemplating what exactly it would do (not sure),
See manual for failmode=wait | continue | panic. Even "continue" returns EIO to all new write requests, so they apparently didn't bother to supply an 'eat-my-data-but-tell-me-everything-is-fine' mode. Figures.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-05 07:09:57
Summary to date:
It's worse than I thought originally, because:
Most widely deployed kernels have cases where they don't tell you about losing your writes at all; and
Information about loss of writes can be masked by closing and re-opening a file
So the checkpointer cannot trust that a successful fsync() means ... a successful fsync().
Also, it's been reported to me off-list that anyone on the system calling sync(2) or the sync shell command will also generally consume the write error, causing us not to see it when we fsync(). The same is true for /proc/sys/vm/drop_caches. I have not tested these yet.
There's some level of agreement that we should PANIC on fsync() errors, at least on Linux, but likely everywhere. But we also now know it's insufficient to be fully protective.
I previously though that errors=remount-ro was a sufficient safeguard. It isn't. There doesn't seem to be anything that is, for ext3, ext4, btrfs or xfs.
It's not clear to me yet why data_err=abort isn't sufficient in data=ordered or data=writeback mode on ext3 or ext4, needs more digging. (In my test tools that's: make FSTYPE=ext4 MKFSOPTS="" MOUNTOPTS="errors=remount-ro, data_err=abort,data=journal" as of the current version d7fe802ec). AFAICS that's because data_error=abort only affects data=ordered, not data=journal. If you use data=ordered, you at least get retries of the same write failing. This post
https://lkml.org/lkml/2008/10/10/80
added the option and has some explanation, but doesn't explain why it doesn't affect data=journal.
zfs is probably not affected by the issues, per Thomas Munro. I haven't run my test scripts on it yet because my kernel doesn't have zfs support and I'm prioritising the multi-process / open-and-close issues.
So far none of the FSes and options I've tried exhibit the behavour I actually want, which is to make the fs readonly or inaccessible on I/O error.
ENOSPC doesn't seem to be a concern during normal operation of major file systems (ext3, ext4, btrfs, xfs) because they reserve space before returning from write(). But if a buffered write does manage to fail due to ENOSPC we'll definitely see the same problems. This makes ENOSPC on NFS a potentially data corrupting condition since NFS doesn't preallocate space before returning from write().
I think what we really need is a block-layer fix, where an I/O error flips the block device into read-only mode, as if blockdev --setro had been used. Though I'd settle for a kernel panic, frankly. I don't think anybody really wants this, but I'd rather either of those to silent data loss.
I'm currently tweaking my test to do some close and reopen the file between each write() and fsync(), and to support running with nfs.
I've also just found the device-mapper "flakey" driver, which looks fantastic for simulating unreliable I/O with intermittent faults. I've been using the "error" target in a mapping, which lets me remap some of the device to always error, but "flakey" looks very handy for actual PostgreSQL testing.
For the sake of Google, these are errors known to be associated with the problem:
ext4, and ext3 mounted with ext4 driver:
[42084.327345] EXT4-fs warning (device dm-0): ext4_end_bio:323: I/O error
10 writing to inode 12 (offset 0 size 0 starting block 59393)
[42084.327352] Buffer I/O error on device dm-0, logical block 59393
xfs:
[42193.771367] XFS (dm-0): writeback error on sector 118784
[42193.784477] XFS (dm-0): writeback error on sector 118784
jfs: (nil, silence in the kernel logs)
You should also beware of "lost page write" or "lost write" errors.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-05 08:46:08
On 5 April 2018 at 15:09, Craig Ringer
wrote:
Also, it's been reported to me off-list that anyone on the system calling sync(2) or the sync shell command will also generally consume the write error, causing us not to see it when we fsync(). The same is true for /proc/sys/vm/drop_caches. I have not tested these yet.
I just confirmed this with a tweak to the test that
records the file position
close()s the fd
sync()s
open(s) the file
lseek()s back to the recorded position
This causes the test to completely ignore the I/O error, which is not reported to it at any time.
Fair enough, really, when you look at it from the kernel's point of view. What else can it do? Nobody has the file open. It'd have to mark the file its self as bad somehow. But that's pretty bad for our robustness AFAICS.
There's some level of agreement that we should PANIC on fsync() errors, at least on Linux, but likely everywhere. But we also now know it's insufficient to be fully protective.
If dirty writeback fails between our close() and re-open() I see the same behaviour as with sync(). To test that I set dirty_writeback_centisecs and dirty_expire_centisecs to 1 and added a usleep(3*100*1000) between close() and open(). (It's still plenty slow). So sync() is a convenient way to simulate something other than our own fsync() writing out the dirty buffer.
If I omit the sync() then we get the error reported by fsync() once when we re open() the file and fsync() it, because the buffers weren't written out yet, so the error wasn't generated until we re-open()ed the file. But I doubt that'll happen much in practice because dirty writeback will get to it first so the error will be seen and discarded before we reopen the file in the checkpointer.
In other words, it looks like
even with a new kernel with the error reporting bug fixes
, if I understand how the backends and checkpointer interact when it comes to file descriptors, we're unlikely to notice I/O errors and fail a checkpoint. We may notice I/O errors if a backend does its own eager writeback for large I/O operations, or if the checkpointer fsync()s a file before the kernel's dirty writeback gets around to trying to flush the pages that will fail.
I haven't tested anything with multiple processes / multiple FDs yet, where we keep one fd open while writing on another.
But at this point I don't see any way to make Pg reliably detect I/O errors and fail a checkpoint then redo and retry. To even fix this by PANICing like I proposed originally, we need to know we have to PANIC.
AFAICS it's completely unsafe to write(), close(), open() and fsync() and expect that the fsync() makes any promises about the write(). Which if I read Pg's low level storage code right, makes it completely unable to reliably detect I/O errors.
When put it that way, it sounds fair enough too. How long is the kernel meant to remember that there was a write error on the file triggered by a write initiated by some seemingly unrelated process, some unbounded time ago, on a since-closed file?
But it seems to put Pg on the fast track to O_DIRECT.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-05 19:33:14
On Thu, Apr 5, 2018 at 03:09:57PM +0800, Craig Ringer wrote:
ENOSPC doesn't seem to be a concern during normal operation of major file systems (ext3, ext4, btrfs, xfs) because they reserve space before returning from write(). But if a buffered write does manage to fail due to ENOSPC we'll definitely see the same problems. This makes ENOSPC on NFS a potentially data corrupting condition since NFS doesn't preallocate space before returning from write().
This does explain why NFS has a reputation for unreliability for Postgres.
From:Andrew Gierth <andrew(at)tao11(dot)riddles(dot)org(dot)uk>
Date:2018-04-05 23:37:42
Note: as I've brought up in another thread, it turns out that PG is not handling fsync errors correctly even when the OS
does
do the right thing (discovered by testing on FreeBSD).
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-06 01:27:05
On 6 April 2018 at 07:37, Andrew Gierth
wrote:
Note: as I've brought up in another thread, it turns out that PG is not handling fsync errors correctly even when the OS
does
do the right thing (discovered by testing on FreeBSD).
Yikes. For other readers, the related thread for this is
Meanwhile, I've extended my test to run postgres on a deliberately faulty volume and confirmed my results there.
2018-04-06 01:11:40.555 UTC [58] LOG:  checkpoint starting: immediate force
wait
2018-04-06 01:11:40.567 UTC [58] ERROR:  could not fsync file
"base/12992/16386": Input/output error
2018-04-06 01:11:40.655 UTC [66] ERROR:  checkpoint request failed
2018-04-06 01:11:40.655 UTC [66] HINT:  Consult recent messages in the
server log for details.
2018-04-06 01:11:40.655 UTC [66] STATEMENT:  CHECKPOINT



Checkpoint failed with checkpoint request failed
HINT:  Consult recent messages in the server log for details.



Retrying



2018-04-06 01:11:41.568 UTC [58] LOG:  checkpoint starting: immediate force
wait
2018-04-06 01:11:41.614 UTC [58] LOG:  checkpoint complete: wrote 0 buffers
(0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s,
sync=0.000 s, total=0.046 s; sync files=3, longest=0.000 s, average=0.000
s; distance=2727 kB, estimate=2779 kB
Given your report, now I have to wonder if we even reissued the fsync() at all this time. 'perf' time. OK, with
sudo perf record -e syscalls:sys_enter_fsync,syscalls:sys_exit_fsync -a
sudo perf script
I see the failed fync, then the same fd being fsync()d without error on the next checkpoint, which succeeds.
postgres  9602 [003] 72380.325817: syscalls:sys_enter_fsync: fd:
0x00000005
        postgres  9602 [003] 72380.325931:  syscalls:sys_exit_fsync:
0xfffffffffffffffb
...
        postgres  9602 [000] 72381.336767: syscalls:sys_enter_fsync: fd:
0x00000005
        postgres  9602 [000] 72381.336840:  syscalls:sys_exit_fsync: 0x0
... and Pg continues merrily on its way without realising it lost data:
[72379.834872] XFS (dm-0): writeback error on sector 118752
[72380.324707] XFS (dm-0): writeback error on sector 118688
In this test I set things up so the checkpointer would see the first fsync() error. But if I make checkpoints less frequent, the bgwriter aggressive, and kernel dirty writeback aggressive, it should be possible to have the failure go completely unobserved too. I'll try that next, because we've already largely concluded that the solution to the issue above is to PANIC on fsync() error. But if we don't see the error at all we're in trouble.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-06 02:53:56
On Fri, Apr 6, 2018 at 1:27 PM, Craig Ringer
wrote:
On 6 April 2018 at 07:37, Andrew Gierth
wrote:
Note: as I've brought up in another thread, it turns out that PG is not handling fsync errors correctly even when the OS
does
do the right thing (discovered by testing on FreeBSD).
Yikes. For other readers, the related thread for this is
Yeah. That's really embarrassing, especially after beating up on various operating systems all week. It's also an independent issue -- let's keep that on the other thread and get it fixed.
I see the failed fync, then the same fd being fsync()d without error on the next checkpoint, which succeeds.
postgres  9602 [003] 72380.325817: syscalls:sys_enter_fsync: fd:
0x00000005 postgres 9602 [003] 72380.325931: syscalls:sys_exit_fsync: 0xfffffffffffffffb ... postgres 9602 [000] 72381.336767: syscalls:sys_enter_fsync: fd: 0x00000005 postgres 9602 [000] 72381.336840: syscalls:sys_exit_fsync: 0x0
... and Pg continues merrily on its way without realising it lost data:
[72379.834872] XFS (dm-0): writeback error on sector 118752 [72380.324707] XFS (dm-0): writeback error on sector 118688
In this test I set things up so the checkpointer would see the first fsync() error. But if I make checkpoints less frequent, the bgwriter aggressive, and kernel dirty writeback aggressive, it should be possible to have the failure go completely unobserved too. I'll try that next, because we've already largely concluded that the solution to the issue above is to PANIC on fsync() error. But if we don't see the error at all we're in trouble.
I suppose you only see errors because the file descriptors linger open in the virtual file descriptor cache, which is a matter of luck depending on how many relation segment files you touched. One thing you could try to confirm our understand of the Linux 4.13+ policy would be to hack PostgreSQL so that it reopens the file descriptor every time in mdsync(). See attached.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-06 03:20:22
On 6 April 2018 at 10:53, Thomas Munro
wrote:
On Fri, Apr 6, 2018 at 1:27 PM, Craig Ringer
wrote:
On 6 April 2018 at 07:37, Andrew Gierth
wrote:
Note: as I've brought up in another thread, it turns out that PG is not handling fsync errors correctly even when the OS
does
do the right thing (discovered by testing on FreeBSD).
Yikes. For other readers, the related thread for this is news-spur.riddles.org.uk
Yeah. That's really embarrassing, especially after beating up on various operating systems all week. It's also an independent issue -- let's keep that on the other thread and get it fixed.
I see the failed fync, then the same fd being fsync()d without error on the next checkpoint, which succeeds.
postgres  9602 [003] 72380.325817: syscalls:sys_enter_fsync: fd:
0x00000005 postgres 9602 [003] 72380.325931: syscalls:sys_exit_fsync: 0xfffffffffffffffb ... postgres 9602 [000] 72381.336767: syscalls:sys_enter_fsync: fd: 0x00000005 postgres 9602 [000] 72381.336840: syscalls:sys_exit_fsync: 0x0
... and Pg continues merrily on its way without realising it lost data:
[72379.834872] XFS (dm-0): writeback error on sector 118752 [72380.324707] XFS (dm-0): writeback error on sector 118688
In this test I set things up so the checkpointer would see the first fsync() error. But if I make checkpoints less frequent, the bgwriter aggressive, and kernel dirty writeback aggressive, it should be possible to have the failure go completely unobserved too. I'll try that next, because we've already largely concluded that the solution to the issue above is to PANIC on fsync() error. But if we don't see the error at all we're in trouble.
I suppose you only see errors because the file descriptors linger open in the virtual file descriptor cache, which is a matter of luck depending on how many relation segment files you touched.
In this case I think it's because the kernel didn't get around to doing the writeback before the eagerly forced checkpoint fsync()'d it. Or we didn't even queue it for writeback from our own shared_buffers until just before we fsync()'d it. After all, it's a contrived test case that tries to reproduce the issue rapidly with big writes and frequent checkpoints.
So the checkpointer had the relation open to fsync() it, and it was the checkpointer's fsync() that did writeback on the dirty page and noticed the error.
If we the kernel had done the writeback before the checkpointer opened the relation to fsync() it, we might not have seen the error at all - though as you note this depends on the file descriptor cache. You can see the silent-error behaviour in my standalone test case where I confirmed the post-4.13 behaviour. (I'm on 4.14 here).
I can try to reproduce it with postgres too, but it not only requires closing and reopening the FDs, it also requires forcing writeback before opening the fd. To make it occur in a practical timeframe I have to make my kernel writeback settings insanely aggressive and/or call sync() before re-open()ing. I don't really think it's worth it, since I've confirmed the behaviour already with the simpler test in standalone/ in the rest repo. To try it yourself, clone
https://github.com/ringerc/scrapcode
and in the master branch
cd testcases/fsync-error-clear
less README
make REOPEN=reopen standalone-run
See
https://github.com/ringerc/scrapcode/blob/master/testcases/fsync-error-clear/standalone/fsync-error-clear.c#L118
.
I've pushed the postgres test to that repo too; "make postgres-run".
You'll need docker, and be warned, it's using privileged docker containers and messing with dmsetup.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-08 02:16:07
So, what can we actually do about this new Linux behaviour?
Idea 1:
whenever you open a file, either tell the checkpointer so it can open it too (and wait for it to tell you that it has done so, because it's not safe to write() until then), or send it a copy of the file descriptor via IPC (since duplicated file descriptors share the same f_wb_err)
if the checkpointer can't take any more file descriptors (how would that limit even work in the IPC case?), then it somehow needs to tell you that so that you know that you're responsible for fsyncing that file yourself, both on close (due to fd cache recycling) and also when the checkpointer tells you to
Maybe it could be made to work, but sheesh, that seems horrible. Is there some simpler idea along these lines that could make sure that fsync() is only ever called on file descriptors that were opened before all unflushed writes, or file descriptors cloned from such file descriptors?
Idea 2:
Give up, complain that this implementation is defective and unworkable, both on POSIX-compliance grounds and on POLA grounds, and campaign to get it fixed more fundamentally (actual details left to the experts, no point in speculating here, but we've seen a few approaches that work on other operating systems including keeping buffers dirty and marking the whole filesystem broken/read-only).
Idea 3:
Give up on buffered IO and develop an O_SYNC | O_DIRECT based system ASAP.
Any other ideas?
For a while I considered suggesting an idea which I now think doesn't work. I thought we could try asking for a new fcntl interface that spits out wb_err counter. Call it an opaque error token or something. Then we could store it in our fsync queue and safely close the file. Check again before fsync()ing, and if we ever see a different value, PANIC because it means a writeback error happened while we weren't looking. Sadly I think it doesn't work because AIUI inodes are not pinned in kernel memory when no one has the file open and there are no dirty buffers, so I think the counters could go away and be reset. Perhaps you could keep inodes pinned by keeping the associated buffers dirty after an error (like FreeBSD), but if you did that you'd have solved the problem already and wouldn't really need the wb_err system at all. Is there some other idea long these lines that could work?
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-08 02:33:37
On Sun, Apr 8, 2018 at 02:16:07PM +1200, Thomas Munro wrote:
So, what can we actually do about this new Linux behaviour?
Idea 1:
whenever you open a file, either tell the checkpointer so it can open it too (and wait for it to tell you that it has done so, because it's not safe to write() until then), or send it a copy of the file descriptor via IPC (since duplicated file descriptors share the same f_wb_err)
if the checkpointer can't take any more file descriptors (how would that limit even work in the IPC case?), then it somehow needs to tell you that so that you know that you're responsible for fsyncing that file yourself, both on close (due to fd cache recycling) and also when the checkpointer tells you to
Maybe it could be made to work, but sheesh, that seems horrible. Is there some simpler idea along these lines that could make sure that fsync() is only ever called on file descriptors that were opened before all unflushed writes, or file descriptors cloned from such file descriptors?
Idea 2:
Give up, complain that this implementation is defective and unworkable, both on POSIX-compliance grounds and on POLA grounds, and campaign to get it fixed more fundamentally (actual details left to the experts, no point in speculating here, but we've seen a few approaches that work on other operating systems including keeping buffers dirty and marking the whole filesystem broken/read-only).
Idea 3:
Give up on buffered IO and develop an O_SYNC | O_DIRECT based system ASAP.
Idea 4 would be for people to assume their database is corrupt if their server logs report any I/O error on the file systems Postgres uses.
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-08 02:37:47
On Apr 7, 2018, at 19:33, Bruce Momjian
wrote: Idea 4 would be for people to assume their database is corrupt if their server logs report any I/O error on the file systems Postgres uses.
Pragmatically, that's where we are right now. The best answer in this bad situation is (a) fix the error, then (b) replay from a checkpoint before the error occurred, but it appears we can't even guarantee that a PostgreSQL process will be the one to see the error.
-- -- Christophe Pettus xof(at)thebuild(dot)com
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-08 03:27:45
On 8 April 2018 at 10:16, Thomas Munro
wrote:
So, what can we actually do about this new Linux behaviour?
Yeah, I've been cooking over that myself.
More below, but here's an idea #5: decide InnoDB has the right idea, and go to using a single massive blob file, or a few giant blobs.
We have a storage abstraction that makes this way, way less painful than it should be.
We can virtualize relfilenodes into storage extents in relatively few big files. We could use sparse regions to make the addressing more convenient, but that makes copying and backup painful, so I'd rather not.
Even one file per tablespace for persistent relation heaps, another for indexes, another for each fork type.
That way we can use something like your #1 (which is what I was also thinking about then rejecting previously), but reduce the pain by reducing the FD count drastically so exhausting FDs stops being a problem.
Previously I was leaning toward what you've described here:
whenever you open a file, either tell the checkpointer so it can open it too (and wait for it to tell you that it has done so, because it's not safe to write() until then), or send it a copy of the file descriptor via IPC (since duplicated file descriptors share the same f_wb_err)
if the checkpointer can't take any more file descriptors (how would that limit even work in the IPC case?), then it somehow needs to tell you that so that you know that you're responsible for fsyncing that file yourself, both on close (due to fd cache recycling) and also when the checkpointer tells you to
Maybe it could be made to work, but sheesh, that seems horrible. Is there some simpler idea along these lines that could make sure that fsync() is only ever called on file descriptors that were opened before all unflushed writes, or file descriptors cloned from such file descriptors?
... and got stuck on "yuck, that's awful".
I was assuming we'd force early checkpoints if the checkpointer hit its fd limit, but that's even worse.
We'd need to urgently do away with segmented relations, and partitions would start to become a hinderance.
Even then it's going to be an unworkable nightmare with heavily partitioned systems, systems that use schema-sharding, etc. And it'll mean we need to play with process limits and, often, system wide limits on FDs. I imagine the performance implications won't be pretty.
Idea 2:
Give up, complain that this implementation is defective and unworkable, both on POSIX-compliance grounds and on POLA grounds, and campaign to get it fixed more fundamentally (actual details left to the experts, no point in speculating here, but we've seen a few approaches that work on other operating systems including keeping buffers dirty and marking the whole filesystem broken/read-only).
This appears to be what SQLite does AFAICS.
https://www.sqlite.org/atomiccommit.html
though it has the huge luxury of a single writer, so it's probably only subject to the original issue not the multiprocess / checkpointer issues we face.
Idea 3:
Give up on buffered IO and develop an O_SYNC | O_DIRECT based system ASAP.
That seems to be what the kernel folks will expect. But that's going to KILL performance. We'll need writer threads to have any hope of it not
totally
sucking, because otherwise simple things like updating a heap tuple and two related indexes will incur enormous disk latencies.
But I suspect it's the path forward.
Goody.
Any other ideas?
For a while I considered suggesting an idea which I now think doesn't work. I thought we could try asking for a new fcntl interface that spits out wb_err counter. Call it an opaque error token or something. Then we could store it in our fsync queue and safely close the file. Check again before fsync()ing, and if we ever see a different value, PANIC because it means a writeback error happened while we weren't looking. Sadly I think it doesn't work because AIUI inodes are not pinned in kernel memory when no one has the file open and there are no dirty buffers, so I think the counters could go away and be reset. Perhaps you could keep inodes pinned by keeping the associated buffers dirty after an error (like FreeBSD), but if you did that you'd have solved the problem already and wouldn't really need the wb_err system at all. Is there some other idea long these lines that could work?
I think our underlying data syncing concept is fundamentally broken, and it's not really the kernel's fault.
We assume that we can safely:
procA: open()
procA: write()
procA: close()
... some long time later, unbounded as far as the kernel is concerned ...
procB: open()
procB: fsync()
procB: close()
If the kernel does writeback in the middle, how on earth is it supposed to know we expect to reopen the file and check back later?
Should it just remember "this file had an error" forever, and tell every caller? In that case how could we recover? We'd need some new API to say "yeah, ok already, I'm redoing all my work since the last good fsync() so you can clear the error flag now". Otherwise it'd keep reporting an error after we did redo to recover, too.
I never really clicked to the fact that we closed relations with pending buffered writes, left them closed, then reopened them to fsync. That's .... well, the kernel isn't the only thing doing crazy things here.
Right now I think we're at option (4): If you see anything that smells like a write error in your kernel logs, hard-kill postgres with -m immediate (do NOT let it do a shutdown checkpoint). If it did a checkpoint since the logs, fake up a backup label to force redo to start from the last checkpoint before the error. Otherwise, it's safe to just let it start up again and do redo again.
Fun times.
This also means AFAICS that running Pg on NFS is extremely unsafe, you MUST make sure you don't run out of disk. Because the usual safeguard of space reservation against ENOSPC in fsync doesn't apply to NFS. (I haven't tested this with nfsv3 in sync,hard,nointr mode yet,
maybe
that's safe, but I doubt it). The same applies to thin-provisioned storage. Just. Don't.
This helps explain various reports of corruption in Docker and various other tools that use various sorts of thin provisioning. If you hit ENOSPC in fsync(), bye bye data.
From:Peter Geoghegan <pg(at)bowt(dot)ie>
Date:2018-04-08 03:37:06
On Sat, Apr 7, 2018 at 8:27 PM, Craig Ringer
wrote:
More below, but here's an idea #5: decide InnoDB has the right idea, and go to using a single massive blob file, or a few giant blobs.
We have a storage abstraction that makes this way, way less painful than it should be.
We can virtualize relfilenodes into storage extents in relatively few big files. We could use sparse regions to make the addressing more convenient, but that makes copying and backup painful, so I'd rather not.
Even one file per tablespace for persistent relation heaps, another for indexes, another for each fork type.
I'm not sure that we can do that now, since it would break the new "Optimize btree insertions for common case of increasing values" optimization. (I did mention this before it went in.)
I've asked Pavan to at least add a note to the nbtree README that explains the high level theory behind the optimization, as part of post-commit clean-up. I'll ask him to say something about how it might affect extent-based storage, too.
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-08 03:46:17
On Apr 7, 2018, at 20:27, Craig Ringer
wrote:
Right now I think we're at option (4): If you see anything that smells like a write error in your kernel logs, hard-kill postgres with -m immediate (do NOT let it do a shutdown checkpoint). If it did a checkpoint since the logs, fake up a backup label to force redo to start from the last checkpoint before the error. Otherwise, it's safe to just let it start up again and do redo again.
Before we spiral down into despair and excessive alcohol consumption, this is basically the same situation as a checksum failure or some other kind of uncorrected media-level error. The bad part is that we have to find out from the kernel logs rather than from PostgreSQL directly. But this does not strike me as otherwise significantly different from, say, an infrequently-accessed disk block reporting an uncorrectable error when we finally get around to reading it.
From:Andreas Karlsson <andreas(at)proxel(dot)se>
Date:2018-04-08 09:41:06
On 04/08/2018 05:27 AM, Craig Ringer wrote:>
More below, but here's an idea #5: decide InnoDB has the right idea, and go to using a single massive blob file, or a few giant blobs.
FYI: MySQL has by default one file per table these days. The old approach with one massive file was a maintenance headache so they change the default some releases ago.
https://dev.mysql.com/doc/refman/8.0/en/innodb-multiple-tablespaces.html
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-08 10:30:31
On 8 April 2018 at 11:46, Christophe Pettus
wrote:
On Apr 7, 2018, at 20:27, Craig Ringer
wrote:
Right now I think we're at option (4): If you see anything that smells like a write error in your kernel logs, hard-kill postgres with -m immediate (do NOT let it do a shutdown checkpoint). If it did a checkpoint since the logs, fake up a backup label to force redo to start from the last checkpoint before the error. Otherwise, it's safe to just let it start up again and do redo again.
Before we spiral down into despair and excessive alcohol consumption, this is basically the same situation as a checksum failure or some other kind of uncorrected media-level error. The bad part is that we have to find out from the kernel logs rather than from PostgreSQL directly. But this does not strike me as otherwise significantly different from, say, an infrequently-accessed disk block reporting an uncorrectable error when we finally get around to reading it.
I don't entirely agree - because it affects ENOSPC, I/O errors on thin provisioned storage, I/O errors on multipath storage, etc. (I identified the original issue on a thin provisioned system that ran out of backing space, mangling PostgreSQL in a way that made no sense at the time).
These are way more likely than bit flips or other storage level corruption, and things that we previously expected to detect and fail gracefully for.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-08 10:31:24
On 8 April 2018 at 17:41, Andreas Karlsson
wrote:
On 04/08/2018 05:27 AM, Craig Ringer wrote:> More below, but here's an idea #5: decide InnoDB has the right idea, and
go to using a single massive blob file, or a few giant blobs.
FYI: MySQL has by default one file per table these days. The old approach with one massive file was a maintenance headache so they change the default some releases ago.
https://dev.mysql.com/doc/refman/8.0/en/innodb-multiple-tablespaces.html
Huh, thanks for the update.
We should see how they handle reliable flushing and see if they've looked into it. If they haven't, we should give them a heads-up and if they have, lets learn from them.
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-08 16:38:03
On Apr 8, 2018, at 03:30, Craig Ringer
wrote:
These are way more likely than bit flips or other storage level corruption, and things that we previously expected to detect and fail gracefully for.
This is definitely bad, and it explains a few otherwise-inexplicable corruption issues we've seen. (And great work tracking it down!) I think it's important not to panic, though; PostgreSQL doesn't have a reputation for horrible data integrity. I'm not sure it makes sense to do a major rearchitecting of the storage layer (especially with pluggable storage coming along) to address this. While the failure modes are more common, the solution (a PITR backup) is one that an installation should have anyway against media failures.
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-08 21:23:21
On 8 April 2018 at 04:27, Craig Ringer
wrote:
On 8 April 2018 at 10:16, Thomas Munro
wrote:
If the kernel does writeback in the middle, how on earth is it supposed to know we expect to reopen the file and check back later?
Should it just remember "this file had an error" forever, and tell every caller? In that case how could we recover? We'd need some new API to say "yeah, ok already, I'm redoing all my work since the last good fsync() so you can clear the error flag now". Otherwise it'd keep reporting an error after we did redo to recover, too.
There is no spoon^H^H^H^H^Herror flag. We don't need fsync to keep track of any errors. We just need fsync to accurately report whether all the buffers in the file have been written out. When you call fsync again the kernel needs to initiate i/o on all the dirty buffers and block until they complete successfully. If they complete successfully then nobody cares whether they had some failure in the past when i/o was initiated at some point in the past.
The problem is not that errors aren't been tracked correctly. The problem is that dirty buffers are being marked clean when they haven't been written out. They consider dirty filesystem buffers when there's hardware failure preventing them from being written "a memory leak".
As long as any error means the kernel has discarded writes then there's no real hope of any reliable operation through that interface.
Going to DIRECTIO is basically recognizing this. That the kernel filesystem buffer provides no reliable interface so we need to reimplement it ourselves in user space.
It's rather disheartening. Aside from having to do all that work we have the added barrier that we don't have as much information about the hardware as the kernel has. We don't know where raid stripes begin and end, how big the memory controller buffers are or how to tell when they're full or empty or how to flush them. etc etc. We also don't know what else is going on on the machine.
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-08 21:28:43
On Apr 8, 2018, at 14:23, Greg Stark
wrote:
They consider dirty filesystem buffers when there's hardware failure preventing them from being written "a memory leak".
That's not an irrational position. File system buffers are
not
dedicated memory for file system caching; they're being used for that because no one has a better use for them at that moment. If an inability to flush them to disk meant that they suddenly became pinned memory, a large copy operation to a yanked USB drive could result in the system having no more allocatable memory. I guess in theory that they could swap them, but swapping out a file system buffer in hopes that sometime in the future it could be properly written doesn't seem very architecturally sound to me.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-08 21:47:04
On Sun, Apr 08, 2018 at 10:23:21PM +0100, Greg Stark wrote:
On 8 April 2018 at 04:27, Craig Ringer
wrote:
On 8 April 2018 at 10:16, Thomas Munro
wrote:
If the kernel does writeback in the middle, how on earth is it supposed to know we expect to reopen the file and check back later?
Should it just remember "this file had an error" forever, and tell every caller? In that case how could we recover? We'd need some new API to say "yeah, ok already, I'm redoing all my work since the last good fsync() so you can clear the error flag now". Otherwise it'd keep reporting an error after we did redo to recover, too.
There is no spoon^H^H^H^H^Herror flag. We don't need fsync to keep track of any errors. We just need fsync to accurately report whether all the buffers in the file have been written out. When you call fsync
Instead, fsync() reports when some of the buffers have not been written out, due to reasons outlined before. As such it may make some sense to maintain some tracking regarding errors even after marking failed dirty pages as clean (in fact it has been proposed, but this introduces memory overhead).
again the kernel needs to initiate i/o on all the dirty buffers and block until they complete successfully. If they complete successfully then nobody cares whether they had some failure in the past when i/o was initiated at some point in the past.
The question is, what should the kernel and application do in cases where this is simply not possible (according to freebsd that keeps dirty pages around after failure, for example, -EIO from the block layer is a contract for unrecoverable errors so it is pointless to keep them dirty). You'd need a specialized interface to clear-out the errors (and drop the dirty pages), or potentially just remount the filesystem.
The problem is not that errors aren't been tracked correctly. The problem is that dirty buffers are being marked clean when they haven't been written out. They consider dirty filesystem buffers when there's hardware failure preventing them from being written "a memory leak".
As long as any error means the kernel has discarded writes then there's no real hope of any reliable operation through that interface.
This does not necessarily follow. Whether the kernel discards writes or not would not really help (see above). It is more a matter of proper "reporting contract" between userspace and kernel, and tracking would be a way for facilitating this vs. having a more complex userspace scheme (as described by others in this thread) where synchronization for fsync() is required in a multi-process application.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-08 22:29:16
On Sun, Apr 8, 2018 at 09:38:03AM -0700, Christophe Pettus wrote:
On Apr 8, 2018, at 03:30, Craig Ringer
wrote:
These are way more likely than bit flips or other storage level corruption, and things that we previously expected to detect and fail gracefully for.
This is definitely bad, and it explains a few otherwise-inexplicable corruption issues we've seen. (And great work tracking it down!) I think it's important not to panic, though; PostgreSQL doesn't have a reputation for horrible data integrity. I'm not sure it makes sense to do a major rearchitecting of the storage layer (especially with pluggable storage coming along) to address this. While the failure modes are more common, the solution (a PITR backup) is one that an installation should have anyway against media failures.
I think the big problem is that we don't have any way of stopping Postgres at the time the kernel reports the errors to the kernel log, so we are then returning potentially incorrect results and committing transactions that might be wrong or lost. If we could stop Postgres when such errors happen, at least the administrator could fix the problem of fail-over to a standby.
An crazy idea would be to have a daemon that checks the logs and stops Postgres when it seems something wrong.
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-08 23:10:24
On Apr 8, 2018, at 15:29, Bruce Momjian
wrote: I think the big problem is that we don't have any way of stopping Postgres at the time the kernel reports the errors to the kernel log, so we are then returning potentially incorrect results and committing transactions that might be wrong or lost.
Yeah, it's bad. In the short term, the best advice to installations is to monitor their kernel logs for errors (which very few do right now), and make sure they have a backup strategy which can encompass restoring from an error like this. Even Craig's smart fix of patching the backup label to recover from a previous checkpoint doesn't do much good if we don't have WAL records back that far (or one of the required WAL records also took a hit).
In the longer term... O_DIRECT seems like the most plausible way out of this, but that might be popular with people running on file systems or OSes that don't have this issue. (Setting aside the daunting prospect of implementing that.)
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-08 23:16:25
On 2018-04-08 18:29:16 -0400, Bruce Momjian wrote:
On Sun, Apr 8, 2018 at 09:38:03AM -0700, Christophe Pettus wrote:
On Apr 8, 2018, at 03:30, Craig Ringer
wrote:
These are way more likely than bit flips or other storage level corruption, and things that we previously expected to detect and fail gracefully for.
This is definitely bad, and it explains a few otherwise-inexplicable corruption issues we've seen. (And great work tracking it down!) I think it's important not to panic, though; PostgreSQL doesn't have a reputation for horrible data integrity. I'm not sure it makes sense to do a major rearchitecting of the storage layer (especially with pluggable storage coming along) to address this. While the failure modes are more common, the solution (a PITR backup) is one that an installation should have anyway against media failures.
I think the big problem is that we don't have any way of stopping Postgres at the time the kernel reports the errors to the kernel log, so we are then returning potentially incorrect results and committing transactions that might be wrong or lost. If we could stop Postgres when such errors happen, at least the administrator could fix the problem of fail-over to a standby.
An crazy idea would be to have a daemon that checks the logs and stops Postgres when it seems something wrong.
I think the danger presented here is far smaller than some of the statements in this thread might make one think. In all likelihood, once you've got an IO error that kernel level retries don't fix, your database is screwed. Whether fsync reports that or not is really somewhat besides the point. We don't panic that way when getting IO errors during reads either, and they're more likely to be persistent than errors during writes (because remapping on storage layer can fix issues, but not during reads).
There's a lot of not so great things here, but I don't think there's any need to panic.
We should fix things so that reported errors are treated with crash recovery, and for the rest I think there's very fair arguments to be made that that's far outside postgres's remit.
I think there's pretty good reasons to go to direct IO where supported, but error handling doesn't strike me as a particularly good reason for the move.
From:Christophe Pettus <xof(at)thebuild(dot)com>
Date:2018-04-08 23:27:57
On Apr 8, 2018, at 16:16, Andres Freund
wrote: We don't panic that way when getting IO errors during reads either, and they're more likely to be persistent than errors during writes (because remapping on storage layer can fix issues, but not during reads).
There is a distinction to be drawn there, though, because we immediately pass an error back to the client on a read, but a write problem in this situation can be masked for an extended period of time.
That being said...
There's a lot of not so great things here, but I don't think there's any need to panic.
No reason to panic, yes. We can assume that if this was a very big persistent problem, it would be much more widely reported. It would, however, be good to find a way to get the error surfaced back up to the client in a way that is not just monitoring the kernel logs.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-09 01:31:56
On 9 April 2018 at 05:28, Christophe Pettus
wrote:
On Apr 8, 2018, at 14:23, Greg Stark
wrote:
They consider dirty filesystem buffers when there's hardware failure preventing them from being written "a memory leak".
That's not an irrational position. File system buffers are
not
dedicated memory for file system caching; they're being used for that because no one has a better use for them at that moment. If an inability to flush them to disk meant that they suddenly became pinned memory, a large copy operation to a yanked USB drive could result in the system having no more allocatable memory. I guess in theory that they could swap them, but swapping out a file system buffer in hopes that sometime in the future it could be properly written doesn't seem very architecturally sound to me.
Yep.
Another example is a write to an NFS or iSCSI volume that goes away forever. What if the app keeps write()ing in the hopes it'll come back, and by the time the kernel starts reporting EIO for write(), it's already saddled with a huge volume of dirty writeback buffers it can't get rid of because someone, one day, might want to know about them?
You could make the argument that it's OK to forget if the entire file system goes away. But actually, why is that ok? What if it's remounted again? That'd be really bad too, for someone expecting write reliability.
You can coarsen from dirty buffer tracking to marking the FD(s) bad, but what if there's no FD to mark because the file isn't open at the moment?
You can mark the inode cache entry and pin it, I guess. But what if your app triggered I/O errors over vast numbers of small files? Again, the kernel's left holding the ball.
It doesn't know if/when an app will return to check. It doesn't know how long to remember the failure for. It doesn't know when all interested clients have been informed and it can treat the fault as cleared/repaired, either, so it'd have to
keep on reporting EIO for PostgreSQL's own writes and fsyncs() indefinitely
, even once we do recovery.
The only way it could avoid that would be to keep the dirty writeback pages around and flagged bad, then clear the flag when a new write() replaces the same file range. I can't imagine that being practical.
Blaming the kernel for this sure is the easy way out.
But IMO we cannot rationally expect the kernel to remember error state forever for us, then forget it when we expect, all without actually telling it anything about our activities or even that we still exist and are still interested in the files/writes. We've closed the files and gone away.
Whatever we do, it's likely going to have to involve not doing that anymore.
Even if we can somehow convince the kernel folks to add a new interface for us that reports I/O errors to some listener, like an inotify/fnotify/dnotify/whatever-it-is-today-notify extension reporting errors in buffered async writes, we won't be able to rely on having it for 5-10 years, and only on Linux.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-09 01:35:06
On 9 April 2018 at 06:29, Bruce Momjian
wrote:
I think the big problem is that we don't have any way of stopping Postgres at the time the kernel reports the errors to the kernel log, so we are then returning potentially incorrect results and committing transactions that might be wrong or lost.
Right.
Specifically, we need a way to ask the kernel at checkpoint time "was everything written to [this set of files] flushed successfully since the last time I asked, no matter who did the writing and no matter how the writes were flushed?"
If the result is "no" we PANIC and redo. If the hardware/volume is screwed, the user can fail over to a standby, do PITR, etc.
But we don't have any way to ask that reliably at present.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 01:55:10
Hi,
On 2018-04-08 16:27:57 -0700, Christophe Pettus wrote:
On Apr 8, 2018, at 16:16, Andres Freund
wrote: We don't panic that way when getting IO errors during reads either, and they're more likely to be persistent than errors during writes (because remapping on storage layer can fix issues, but not during reads).
There is a distinction to be drawn there, though, because we immediately pass an error back to the client on a read, but a write problem in this situation can be masked for an extended period of time.
Only if you're "lucky" enough that your clients actually read that data, and then you're somehow able to figure out across the whole stack that these 0.001% of transactions that fail are due to IO errors. Or you also need to do log analysis.
If you want to solve things like that you need regular reads of all your data, including verifications etc.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-09 02:00:41
On 9 April 2018 at 07:16, Andres Freund
wrote:
I think the danger presented here is far smaller than some of the statements in this thread might make one think.
Clearly it's not happening a huge amount or we'd have a lot of noise about Pg eating people's data, people shouting about how unreliable it is, etc. We don't. So it's not some earth shattering imminent threat to everyone's data. It's gone unnoticed, or the root cause unidentified, for a long time.
I suspect we've written off a fair few issues in the past as "it'd bad hardware" when actually, the hardware fault was the trigger for a Pg/kernel interaction bug. And blamed containers for things that weren't really the container's fault. But even so, if it were happening tons, we'd hear more noise.
I've already been very surprised there when I learned that PostgreSQL completely ignores wholly absent relfilenodes. Specifically, if you unlink() a relation's backing relfilenode while Pg is down and that file has writes pending in the WAL. We merrily re-create it with uninitalized pages and go on our way. As Andres pointed out in an offlist discussion, redo isn't a consistency check, and it's not obliged to fail in such cases. We can say "well, don't do that then" and define away file losses from FS corruption etc as not our problem, the lower levels we expect to take care of this have failed.
We have to look at what checkpoints are and are not supposed to promise, and whether this is a problem we just define away as "not our problem, the lower level failed, we're not obliged to detect this and fail gracefully."
We can choose to say that checkpoints are required to guarantee crash/power loss safety ONLY and do not attempt to protect against I/O errors of any sort. In fact, I think we should likely amend the documentation for release versions to say just that.
In all likelihood, once you've got an IO error that kernel level retries don't fix, your database is screwed.
Your database is going to be down or have interrupted service. It's possible you may have some unreadable data. This could result in localised damage to one or more relations. That could affect FK relationships, indexes, all sorts. If you're really unlucky you might lose something critical like pg_clog/ contents.
But in general your DB should be repairable/recoverable even in those cases.
And in many failure modes there's no reason to expect any data loss at all, like:
Local disk fills up (seems to be safe already due to space reservation at write() time)
Thin-provisioned storage backing local volume iSCSI or paravirt block device fills up
NFS volume fills up
Multipath I/O error
Interruption of connectivity to network block device
Disk develops localized bad sector where we haven't previously written data
Except for the ENOSPC on NFS, all the rest of the cases can be handled by expecting the kernel to retry forever and not return until the block is written or we reach the heat death of the universe. And NFS, well...
Part of the trouble is that the kernel
won't
retry forever in all these cases, and doesn't seem to have a way to ask it to in all cases.
And if the user hasn't configured it for the right behaviour in terms of I/O error resilience, we don't find out about it.
So it's not the end of the world, but it'd sure be nice to fix.
Whether fsync reports that or not is really somewhat besides the point. We don't panic that way when getting IO errors during reads either, and they're more likely to be persistent than errors during writes (because remapping on storage layer can fix issues, but not during reads).
That's because reads don't make promises about what's committed and synced. I think that's quite different.
We should fix things so that reported errors are treated with crash recovery, and for the rest I think there's very fair arguments to be made that that's far outside postgres's remit.
Certainly for current versions.
I think we need to think about a more robust path in future. But it's certainly not "stop the world" territory.
The docs need an update to indicate that we explicitly disclaim responsibility for I/O errors on async writes, and that the kernel and I/O stack must be configured never to give up on buffered writes. If it does, that's not our problem anymore.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 02:06:12
On 2018-04-09 10:00:41 +0800, Craig Ringer wrote:
I suspect we've written off a fair few issues in the past as "it'd bad hardware" when actually, the hardware fault was the trigger for a Pg/kernel interaction bug. And blamed containers for things that weren't really the container's fault. But even so, if it were happening tons, we'd hear more noise.
Agreed on that, but I think that's FAR more likely to be things like multixacts, index structure corruption due to logic bugs etc.
I've already been very surprised there when I learned that PostgreSQL completely ignores wholly absent relfilenodes. Specifically, if you unlink() a relation's backing relfilenode while Pg is down and that file has writes pending in the WAL. We merrily re-create it with uninitalized pages and go on our way. As Andres pointed out in an offlist discussion, redo isn't a consistency check, and it's not obliged to fail in such cases. We can say "well, don't do that then" and define away file losses from FS corruption etc as not our problem, the lower levels we expect to take care of this have failed.
And it'd be a realy bad idea to behave differently.
And in many failure modes there's no reason to expect any data loss at all, like:
Local disk fills up (seems to be safe already due to space reservation at write() time)
That definitely should be treated separately.
Thin-provisioned storage backing local volume iSCSI or paravirt block device fills up
NFS volume fills up
Those should be the same as the above.
I think we need to think about a more robust path in future. But it's certainly not "stop the world" territory.
I think you're underestimating the complexity of doing that by at least two orders of magnitude.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-09 03:15:01
On 9 April 2018 at 10:06, Andres Freund
wrote:
And in many failure modes there's no reason to expect any data loss at all, like:
Local disk fills up (seems to be safe already due to space reservation at write() time)
That definitely should be treated separately.
It is, because all the FSes I looked at reserve space before returning from write(), even if they do delayed allocation. So they won't fail with ENOSPC at fsync() time or silently due to lost errors on background writeback. Otherwise we'd be hearing a LOT more noise about this.
Thin-provisioned storage backing local volume iSCSI or paravirt block device fills up
NFS volume fills up
Those should be the same as the above.
Unfortunately, they aren't.
AFAICS NFS doesn't reserve space with the other end before returning from write(), even if mounted with the sync option. So we can get ENOSPC lazily when the buffer writeback fails due to a full backing file system. This then travels the same paths as EIO: we fsync(), ERROR, retry, appear to succeed, and carry on with life losing the data. Or we never hear about the error in the first place.
(There's a proposed extension that'd allow this, see
https://tools.ietf.org/html/draft-iyer-nfsv4-space-reservation-ops-02#page-5
, but I see no mention of it in fs/nfs. All the reserve_space / xdr_reserve_space stuff seems to be related to space in protocol messages at a quick read.)
Thin provisioned storage could vary a fair bit depending on the implementation. But the specific failure case I saw, prompting this thread, was on a volume using the stack:
xfs -> lvm2 -> multipath -> ??? -> SAN
(the HBA/iSCSI/whatever was not recorded by the looks, but IIRC it was iSCSI. I'm checking.)
The SAN ran out of space. Due to use of thin provisioning, Linux
thought
there was plenty of space on the volume; LVM thought it had plenty of physical extents free and unallocated, XFS thought there was tons of free space, etc. The space exhaustion manifested as I/O errors on flushes of writeback buffers.
The logs were like this:
kernel: sd 2:0:0:1: [sdd] Unhandled sense code
kernel: sd 2:0:0:1: [sdd]
kernel: Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
kernel: sd 2:0:0:1: [sdd]
kernel: Sense Key : Data Protect [current]
kernel: sd 2:0:0:1: [sdd]
kernel: Add. Sense: Space allocation failed write protect
kernel: sd 2:0:0:1: [sdd] CDB:
kernel: Write(16): **HEX-DATA-CUT-OUT**
kernel: Buffer I/O error on device dm-0, logical block 3098338786
kernel: lost page write due to I/O error on dm-0
kernel: Buffer I/O error on device dm-0, logical block 3098338787
The immediate cause was that Linux's multipath driver didn't seem to recognise the sense code as retryable, so it gave up and reported it to the next layer up (LVM). LVM and XFS both seem to think that the lower layer is responsible for retries, so they toss the write away, and tell any interested writers if they feel like it, per discussion upthread.
In this case Pg did get the news and reported fsync() errors on checkpoints, but it only reported an error once per relfilenode. Once it ran out of failed relfilenodes to cause the checkpoint to ERROR, it "completed" a "successful" checkpoint and kept on running until the resulting corruption started to manifest its self and it segfaulted some time later. As we've now learned, there's no guarantee we'd even get the news about the I/O errors at all.
WAL was on a separate volume that didn't run out of room immediately, so we didn't PANIC on WAL write failure and prevent the issue.
In this case if Pg had PANIC'd (and been able to guarantee to get the news of write failures reliably), there'd have been no corruption and no data loss despite the underlying storage issue.
If, prior to seeing this, you'd asked me "will my PostgreSQL database be corrupted if my thin-provisioned volume runs out of space" I'd have said "Surely not. PostgreSQL won't be corrupted by running out of disk space, it orders writes carefully and forces flushes so that it will recover gracefully from write failures."
Except not. I was very surprised.
BTW, it also turns out that the
default
for multipath is to give up on errors anyway; see the queue_if_no_path option and no_path_retries options. (Hint: run PostgreSQL with no_path_retries=queue). That's a sane default if you use O_DIRECT|O_SYNC, and otherwise pretty much a data-eating setup.
I regularly see rather a lot of multipath systems, iSCSI systems, SAN backed systems, etc. I think we need to be pretty clear that we expect them to retry indefinitely, and if they report an I/O error we cannot reliably handle it. We need to patch Pg to PANIC on any fsync() failure and document that Pg won't notice some storage failure modes that might otherwise be considered nonfatal or transient, so very specific storage configuration and testing is required. (Not that anyone will do it). Also warn against running on NFS even with "hard,sync,nointr".
It'd be interesting to have a tool that tested error handling, allowing people to do iSCSI plug-pull tests, that sort of thing. But as far as I can tell nobody ever tests their storage stack anyway, so I don't plan on writing something that'll never get used.
I think we need to think about a more robust path in future. But it's certainly not "stop the world" territory.
I think you're underestimating the complexity of doing that by at least two orders of magnitude.
Oh, it's just a minor total rewrite of half Pg, no big deal ;)
I'm sure that no matter how big I think it is, I'm still underestimating it.
The most workable option IMO would be some sort of fnotify/dnotify/whatever that reports all I/O errors on a volume. Some kind of error reporting handle we can keep open on a volume level that we can check for each volume/tablespace after we fsync() everything to see if it all really worked. If we PANIC if that gives us a bad answer, and PANIC on fsync errors, we guard against the great majority of these sorts of should-be-transient-if-the-kernel-didn't-give-up-and-throw-away-our-data errors.
Even then, good luck getting those events from an NFS volume in which the backing volume experiences an issue.
And it's kind of moot because AFAICS no such interface exists.
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-09 08:45:40
On 8 April 2018 at 22:47, Anthony Iliopoulos
wrote:
On Sun, Apr 08, 2018 at 10:23:21PM +0100, Greg Stark wrote:
On 8 April 2018 at 04:27, Craig Ringer
wrote:
On 8 April 2018 at 10:16, Thomas Munro
The question is, what should the kernel and application do in cases where this is simply not possible (according to freebsd that keeps dirty pages around after failure, for example, -EIO from the block layer is a contract for unrecoverable errors so it is pointless to keep them dirty). You'd need a specialized interface to clear-out the errors (and drop the dirty pages), or potentially just remount the filesystem.
Well firstly that's not necessarily the question. ENOSPC is not an unrecoverable error. And even unrecoverable errors for a single write doesn't mean the write will never be able to succeed in the future. But secondly doesn't such an interface already exist? When the device is dropped any dirty pages already get dropped with it. What's the point in dropping them but keeping the failing device?
But just to underline the point. "pointless to keep them dirty" is exactly backwards from the application's point of view. If the error writing to persistent media really is unrecoverable then it's all the more critical that the pages be kept so the data can be copied to some other device. The last thing user space expects to happen is if the data can't be written to persistent storage then also immediately delete it from RAM. (And the
really
last thing user space expects is for this to happen and return no error.)
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-09 10:50:41
On Mon, Apr 09, 2018 at 09:45:40AM +0100, Greg Stark wrote:
On 8 April 2018 at 22:47, Anthony Iliopoulos
wrote:
On Sun, Apr 08, 2018 at 10:23:21PM +0100, Greg Stark wrote:
On 8 April 2018 at 04:27, Craig Ringer
wrote:
On 8 April 2018 at 10:16, Thomas Munro
The question is, what should the kernel and application do in cases where this is simply not possible (according to freebsd that keeps dirty pages around after failure, for example, -EIO from the block layer is a contract for unrecoverable errors so it is pointless to keep them dirty). You'd need a specialized interface to clear-out the errors (and drop the dirty pages), or potentially just remount the filesystem.
Well firstly that's not necessarily the question. ENOSPC is not an unrecoverable error. And even unrecoverable errors for a single write doesn't mean the write will never be able to succeed in the future.
To make things a bit simpler, let us focus on EIO for the moment. The contract between the block layer and the filesystem layer is assumed to be that of, when an EIO is propagated up to the fs, then you may assume that all possibilities for recovering have been exhausted in lower layers of the stack. Mind you, I am not claiming that this contract is either documented or necessarily respected (in fact there have been studies on the error propagation and handling of the block layer, see [1]). Let us assume that this is the design contract though (which appears to be the case across a number of open-source kernels), and if not - it's a bug. In this case, indeed the specific write()s will never be able to succeed in the future, at least not as long as the BIOs are allocated to the specific failing LBAs.
But secondly doesn't such an interface already exist? When the device is dropped any dirty pages already get dropped with it. What's the point in dropping them but keeping the failing device?
I think there are degrees of failure. There are certainly cases where one may encounter localized unrecoverable medium errors (specific to certain LBAs) that are non-maskable from the block layer and below. That does not mean that the device is dropped at all, so it does make sense to continue all other operations to all other regions of the device that are functional. In cases of total device failure, then the filesystem will prevent you from proceeding anyway.
But just to underline the point. "pointless to keep them dirty" is exactly backwards from the application's point of view. If the error writing to persistent media really is unrecoverable then it's all the more critical that the pages be kept so the data can be copied to some other device. The last thing user space expects to happen is if the data can't be written to persistent storage then also immediately delete it from RAM. (And the
really
last thing user space expects is for this to happen and return no error.)
Right. This implies though that apart from the kernel having to keep around the dirtied-but-unrecoverable pages for an unbounded time, that there's further an interface for obtaining the exact failed pages so that you can read them back. This in turn means that there needs to be an association between the fsync() caller and the specific dirtied pages that the caller intents to drain (for which we'd need an fsync_range(), among other things). BTW, currently the failed writebacks are not dropped from memory, but rather marked clean. They could be lost though due to memory pressure or due to explicit request (e.g. proc drop_caches), unless mlocked.
There is a clear responsibility of the application to keep its buffers around until a successful fsync(). The kernels do report the error (albeit with all the complexities of dealing with the interface), at which point the application may not assume that the write()s where ever even buffered in the kernel page cache in the first place.
What you seem to be asking for is the capability of dropping buffers over the (kernel) fence and idemnifying the application from any further responsibility, i.e. a hard assurance that either the kernel will persist the pages or it will keep them around till the application recovers them asynchronously, the filesystem is unmounted, or the system is rebooted.
[1]
https://www.usenix.org/legacy/event/fast08/tech/full_papers/gunawi/gunawi.pdf
From:Geoff Winkless <pgsqladmin(at)geoff(dot)dj>
Date:2018-04-09 12:03:28
On 9 April 2018 at 11:50, Anthony Iliopoulos
wrote:
What you seem to be asking for is the capability of dropping buffers over the (kernel) fence and idemnifying the application from any further responsibility, i.e. a hard assurance that either the kernel will persist the pages or it will keep them around till the application recovers them asynchronously, the filesystem is unmounted, or the system is rebooted.
That seems like a perfectly reasonable position to take, frankly.
The whole
point
of an Operating System should be that you can do exactly that. As a developer I should be able to call write() and fsync() and know that if both calls have succeeded then the result is on disk, no matter what another application has done in the meantime. If that's a "difficult" problem then that's the OS's problem, not mine. If the OS doesn't do that, it's _not_doing_its
job
.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-09 12:16:38
On 9 April 2018 at 18:50, Anthony Iliopoulos
wrote:
There is a clear responsibility of the application to keep its buffers around until a successful fsync(). The kernels do report the error (albeit with all the complexities of dealing with the interface), at which point the application may not assume that the write()s where ever even buffered in the kernel page cache in the first place.
What you seem to be asking for is the capability of dropping buffers over the (kernel) fence and idemnifying the application from any further responsibility, i.e. a hard assurance that either the kernel will persist the pages or it will keep them around till the application recovers them asynchronously, the filesystem is unmounted, or the system is rebooted.
That's what Pg appears to assume now, yes.
Whether that's reasonable is a whole different topic.
I'd like a middle ground where the kernel lets us register our interest and tells us if it lost something, without us having to keep eight million FDs open for some long period. "Tell us about anything that happens under pgdata/" or an inotify-style per-directory-registration option. I'd even say that's ideal.
In the mean time, I propose that we fsync() on close() before we age FDs out of the LRU on backends. Yes, that will hurt throughput and cause stalls, but we don't seem to have many better options. At least it'll only flush what we actually wrote to the OS buffers not what we may have in shared_buffers. If the bgwriter does the same thing, we should be 100% safe from this problem on 4.13+, and it'd be trivial to make it a GUC much like the fsync or full_page_writes options that people can turn off if they know the risks / know their storage is safe / don't care.
Some keen person who wants to later could optimise it by adding a fsync worker thread pool in backends, so we don't block the main thread. Frankly that might be a nice thing to have in the checkpointer anyway. But it's out of scope for fixing this in durability terms.
I'm partway through a patch that makes fsync panic on errors now. Once that's done, the next step will be to force fsync on close() in md and see how we go with that.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-09 12:31:27
On Mon, Apr 09, 2018 at 01:03:28PM +0100, Geoff Winkless wrote:
On 9 April 2018 at 11:50, Anthony Iliopoulos
wrote:
What you seem to be asking for is the capability of dropping buffers over the (kernel) fence and idemnifying the application from any further responsibility, i.e. a hard assurance that either the kernel will persist the pages or it will keep them around till the application recovers them asynchronously, the filesystem is unmounted, or the system is rebooted.
That seems like a perfectly reasonable position to take, frankly.
Indeed, as long as you are willing to ignore the consequences of this design decision: mainly, how you would recover memory when no application is interested in clearing the error. At which point other applications with different priorities will find this position rather unreasonable since there can be no way out of it for them. Good luck convincing any OS kernel upstream to go with this design.
The whole
point
of an Operating System should be that you can do exactly that. As a developer I should be able to call write() and fsync() and know that if both calls have succeeded then the result is on disk, no matter what another application has done in the meantime. If that's a "difficult" problem then that's the OS's problem, not mine. If the OS doesn't do that, it's _not_doing_its
job
.
No OS kernel that I know of provides any promises for atomicity of a write()+fsync() sequence, unless one is using O_SYNC. It doesn't provide you with isolation either, as this is delegated to userspace, where processes that share a file should coordinate accordingly.
It's not a difficult problem, but rather the kernels provide a common denominator of possible interfaces and designs that could accommodate a wider range of potential application scenarios for which the kernel cannot possibly anticipate requirements. There have been plenty of experimental works for providing a transactional (ACID) filesystem interface to applications. On the opposite end, there have been quite a few commercial databases that completely bypass the kernel storage stack. But I would assume it is reasonable to figure out something between those two extremes that can work in a "portable" fashion.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-09 12:54:16
On Mon, Apr 09, 2018 at 08:16:38PM +0800, Craig Ringer wrote:
I'd like a middle ground where the kernel lets us register our interest and tells us if it lost something, without us having to keep eight million FDs open for some long period. "Tell us about anything that happens under pgdata/" or an inotify-style per-directory-registration option. I'd even say that's ideal.
I see what you are saying. So basically you'd always maintain the notification descriptor open, where the kernel would inject events related to writeback failures of files under watch (potentially enriched to contain info regarding the exact failed pages and the file offset they map to). The kernel wouldn't even have to maintain per-page bits to trace the errors, since they will be consumed by the process that reads the events (or discarded, when the notification fd is closed).
Assuming this would be possible, wouldn't Pg still need to deal with synchronizing writers and related issues (since this would be merely a notification mechanism - not prevent any process from continuing), which I understand would be rather intrusive for the current Pg multi-process design.
But other than that, similarly this interface could in principle be similarly implemented in the BSDs via kqueue(), I suppose, to provide what you need.
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 13:33:18
On 04/09/2018 02:31 PM, Anthony Iliopoulos wrote:
On Mon, Apr 09, 2018 at 01:03:28PM +0100, Geoff Winkless wrote:
On 9 April 2018 at 11:50, Anthony Iliopoulos
wrote:
What you seem to be asking for is the capability of dropping buffers over the (kernel) fence and idemnifying the application from any further responsibility, i.e. a hard assurance that either the kernel will persist the pages or it will keep them around till the application recovers them asynchronously, the filesystem is unmounted, or the system is rebooted.
That seems like a perfectly reasonable position to take, frankly.
Indeed, as long as you are willing to ignore the consequences of this design decision: mainly, how you would recover memory when no application is interested in clearing the error. At which point other applications with different priorities will find this position rather unreasonable since there can be no way out of it for them.
Sure, but the question is whether the system can reasonably operate after some of the writes failed and the data got lost. Because if it can't, then recovering the memory is rather useless. It might be better to stop the system in that case, forcing the system administrator to resolve the issue somehow (fail-over to a replica, perform recovery from the last checkpoint, ...).
We already have dirty_bytes and dirty_background_bytes, for example. I don't see why there couldn't be another limit defining how much dirty data to allow before blocking writes altogether. I'm sure it's not that simple, but you get the general idea - do not allow using all available memory because of writeback issues, but don't throw the data away in case it's just a temporary issue.
Good luck convincing any OS kernel upstream to go with this design.
Well, there seem to be kernels that seem to do exactly that already. At least that's how I understand what this thread says about FreeBSD and Illumos, for example. So it's not an entirely insane design, apparently.
The question is whether the current design makes it any easier for user-space developers to build reliable systems. We have tried using it, and unfortunately the answers seems to be "no" and "Use direct I/O and manage everything on your own!"
The whole
point
of an Operating System should be that you can do exactly that. As a developer I should be able to call write() and fsync() and know that if both calls have succeeded then the result is on disk, no matter what another application has done in the meantime. If that's a "difficult" problem then that's the OS's problem, not mine. If the OS doesn't do that, it's _not_doing_its
job
.
No OS kernel that I know of provides any promises for atomicity of a write()+fsync() sequence, unless one is using O_SYNC. It doesn't provide you with isolation either, as this is delegated to userspace, where processes that share a file should coordinate accordingly.
We can (and do) take care of the atomicity and isolation. Implementation of those parts is obviously very application-specific, and we have WAL and locks for that purpose. I/O on the other hand seems to be a generic service provided by the OS - at least that's how we saw it until now.
It's not a difficult problem, but rather the kernels provide a common denominator of possible interfaces and designs that could accommodate a wider range of potential application scenarios for which the kernel cannot possibly anticipate requirements. There have been plenty of experimental works for providing a transactional (ACID) filesystem interface to applications. On the opposite end, there have been quite a few commercial databases that completely bypass the kernel storage stack. But I would assume it is reasonable to figure out something between those two extremes that can work in a "portable" fashion.
Users ask us about this quite often, actually. The question is usually about "RAW devices" and performance, but ultimately it boils down to buffered vs. direct I/O. So far our answer was we rely on kernel to do this reliably, because they know how to do that correctly and we simply don't have the manpower to implement it (portable, reliable, handling different types of storage, ...).
One has to wonder how many applications actually use this correctly, considering PostgreSQL cares about data durability/consistency so much and yet we've been misunderstanding how it works for 20+ years.
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 13:42:35
On 04/09/2018 12:29 AM, Bruce Momjian wrote:
An crazy idea would be to have a daemon that checks the logs and stops Postgres when it seems something wrong.
That doesn't seem like a very practical way. It's better than nothing, of course, but I wonder how would that work with containers (where I think you may not have access to the kernel log at all). Also, I'm pretty sure the messages do change based on kernel version (and possibly filesystem) so parsing it reliably seems rather difficult. And we probably don't want to PANIC after I/O error on an unrelated device, so we'd need to understand which devices are related to PostgreSQL.
From:Abhijit Menon-Sen <ams(at)2ndQuadrant(dot)com>
Date:2018-04-09 13:47:03
At 2018-04-09 15:42:35 +0200, tomas(dot)vondra(at)2ndquadrant(dot)com wrote:
On 04/09/2018 12:29 AM, Bruce Momjian wrote:
An crazy idea would be to have a daemon that checks the logs and stops Postgres when it seems something wrong.
That doesn't seem like a very practical way.
Not least because Craig's tests showed that you can't rely on
always
getting an error message in the logs.
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 13:54:19
On 04/09/2018 04:00 AM, Craig Ringer wrote:
On 9 April 2018 at 07:16, Andres Freund <andres(at)anarazel(dot)de
I think the danger presented here is far smaller than some of the statements in this thread might make one think.
Clearly it's not happening a huge amount or we'd have a lot of noise about Pg eating people's data, people shouting about how unreliable it is, etc. We don't. So it's not some earth shattering imminent threat to everyone's data. It's gone unnoticed, or the root cause unidentified, for a long time.
Yeah, it clearly isn't the case that everything we do suddenly got pointless. It's fairly annoying, though.
I suspect we've written off a fair few issues in the past as "it'd bad hardware" when actually, the hardware fault was the trigger for a Pg/kernel interaction bug. And blamed containers for things that weren't really the container's fault. But even so, if it were happening tons, we'd hear more noise.
Right. Write errors are fairly rare, and we've probably ignored a fair number of cases demonstrating this issue. It kinda reminds me the wisdom that not seeing planes with bullet holes in the engine does not mean engines don't need armor [1].
[1]
https://medium.com/@penguinpress/an-excerpt-from-how-not-to-be-wrong-by-jordan-ellenberg-664e708cfc3d
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-09 14:22:06
On Mon, Apr 09, 2018 at 03:33:18PM +0200, Tomas Vondra wrote:
We already have dirty_bytes and dirty_background_bytes, for example. I don't see why there couldn't be another limit defining how much dirty data to allow before blocking writes altogether. I'm sure it's not that simple, but you get the general idea - do not allow using all available memory because of writeback issues, but don't throw the data away in case it's just a temporary issue.
Sure, there could be knobs for limiting how much memory such "zombie" pages may occupy. Not sure how helpful it would be in the long run since this tends to be highly application-specific, and for something with a large data footprint one would end up tuning this accordingly in a system-wide manner. This has the potential to leave other applications running in the same system with very little memory, in cases where for example original application crashes and never clears the error. Apart from that, further interfaces would need to be provided for actually dealing with the error (again assuming non-transient issues that may not be fixed transparently and that temporary issues are taken care of by lower layers of the stack).
Well, there seem to be kernels that seem to do exactly that already. At least that's how I understand what this thread says about FreeBSD and Illumos, for example. So it's not an entirely insane design, apparently.
It is reasonable, but even FreeBSD has a big fat comment right there (since 2017), mentioning that there can be no recovery from EIO at the block layer and this needs to be done differently. No idea how an application running on top of either FreeBSD or Illumos would actually recover from this error (and clear it out), other than remounting the fs in order to force dropping of relevant pages. It does provide though indeed a persistent error indication that would allow Pg to simply reliably panic. But again this does not necessarily play well with other applications that may be using the filesystem reliably at the same time, and are now faced with EIO while their own writes succeed to be persisted.
Ideally, you'd want a (potentially persistent) indication of error localized to a file region (mapping the corresponding failed writeback pages). NetBSD is already implementing fsync_ranges(), which could be a step in the right direction.
One has to wonder how many applications actually use this correctly, considering PostgreSQL cares about data durability/consistency so much and yet we've been misunderstanding how it works for 20+ years.
I would expect it would be very few, potentially those that have a very simple process model (e.g. embedded DBs that can abort a txn on fsync() EIO). I think that durability is a rather complex cross-layer issue which has been grossly misunderstood similarly in the past (e.g. see [1]). It seems that both the OS and DB communities greatly benefit from a periodic reality check, and I see this as an opportunity for strengthening the IO stack in an end-to-end manner.
[1]
https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-pillai.pdf
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-09 15:29:36
On 9 April 2018 at 15:22, Anthony Iliopoulos
wrote:
On Mon, Apr 09, 2018 at 03:33:18PM +0200, Tomas Vondra wrote:
Sure, there could be knobs for limiting how much memory such "zombie" pages may occupy. Not sure how helpful it would be in the long run since this tends to be highly application-specific, and for something with a large data footprint one would end up tuning this accordingly in a system-wide manner.
Surely this is exactly what the kernel is there to manage. It has to control how much memory is allowed to be full of dirty buffers in the first place to ensure that the system won't get memory starved if it can't clean them fast enough. That isn't even about persistent hardware errors. Even when the hardware is working perfectly it can only flush buffers so fast. The whole point of the kernel is to abstract away shared resources. It's not like user space has any better view of the situation here. If Postgres implemented all this in DIRECT_IO it would have exactly the same problem only with less visibility into what the rest of the system is doing. If every application implemented its own buffer cache we would be back in the same boat only with a fragmented memory allocation.
This has the potential to leave other applications running in the same system with very little memory, in cases where for example original application crashes and never clears the error.
I still think we're speaking two different languages. There's no application anywhere that's going to "clear the error". The application has done the writes and if it's calling fsync it wants to wait until the filesystem can arrange for the write to be persisted. If the application could manage without the persistence then it wouldn't have called fsync.
The only way to "clear out" the error would be by having the writes succeed. There's no reason to think that wouldn't be possible sometime. The filesystem could remap blocks or an administrator could replace degraded raid device components. The only thing Postgres could do to recover would be create a new file and move the data (reading from the dirty buffer in memory!) to a new file anyways so we would "clear the error" by just no longer calling fsync on the old file.
We always read fsync as a simple write barrier. That's what the documentation promised and it's what Postgres always expected. It sounds like the kernel implementors looked at it as some kind of communication channel to communicate status report for specific writes back to user-space. That's a much more complex problem and would have entirely different interface. I think this is why we're having so much difficulty communicating.
It is reasonable, but even FreeBSD has a big fat comment right there (since 2017), mentioning that there can be no recovery from EIO at the block layer and this needs to be done differently. No idea how an application running on top of either FreeBSD or Illumos would actually recover from this error (and clear it out), other than remounting the fs in order to force dropping of relevant pages. It does provide though indeed a persistent error indication that would allow Pg to simply reliably panic. But again this does not necessarily play well with other applications that may be using the filesystem reliably at the same time, and are now faced with EIO while their own writes succeed to be persisted.
Well if they're writing to the same file that had a previous error I doubt there are many applications that would be happy to consider their writes "persisted" when the file was corrupt. Ironically the earlier discussion quoted talked about how applications that wanted more granular communication would be using O_DIRECT -- but what we have is fsync trying to be
too
granular such that it's impossible to get any strong guarantees about anything with it.
One has to wonder how many applications actually use this correctly, considering PostgreSQL cares about data durability/consistency so much and yet we've been misunderstanding how it works for 20+ years.
I would expect it would be very few, potentially those that have a very simple process model (e.g. embedded DBs that can abort a txn on fsync() EIO).
Honestly I don't think there's
any
way to use the current interface to implement reliable operation. Even that embedded database using a single process and keeping every file open all the time (which means file descriptor limits limit its scalability) can be having silent corruption whenever some other process like a backup program comes along and calls fsync (or even sync?).
From:Robert Haas <robertmhaas(at)gmail(dot)com>
Date:2018-04-09 16:45:00
On Mon, Apr 9, 2018 at 8:16 AM, Craig Ringer
wrote:
In the mean time, I propose that we fsync() on close() before we age FDs out of the LRU on backends. Yes, that will hurt throughput and cause stalls, but we don't seem to have many better options. At least it'll only flush what we actually wrote to the OS buffers not what we may have in shared_buffers. If the bgwriter does the same thing, we should be 100% safe from this problem on 4.13+, and it'd be trivial to make it a GUC much like the fsync or full_page_writes options that people can turn off if they know the risks / know their storage is safe / don't care.
Ouch. If a process exits -- say, because the user typed \q into psql -- then you're talking about potentially calling fsync() on a really large number of file descriptor flushing many gigabytes of data to disk. And it may well be that you never actually wrote any data to any of those file descriptors -- those writes could have come from other backends. Or you may have written a little bit of data through those FDs, but there could be lots of other data that you end up flushing incidentally. Perfectly innocuous things like starting up a backend, running a few short queries, and then having that backend exit suddenly turn into something that could have a massive system-wide performance impact.
Also, if a backend ever manages to exit without running through this code, or writes any dirty blocks afterward, then this still fails to fix the problem completely. I guess that's probably avoidable -- we can put this late in the shutdown sequence and PANIC if it fails.
I have a really tough time believing this is the right way to solve the problem. We suffered for years because of ext3's desire to flush the entire page cache whenever any single file was fsync()'d, which was terrible. Eventually ext4 became the norm, and the problem went away. Now we're going to deliberately insert logic to do a very similar kind of terrible thing because the kernel developers have decided that fsync() doesn't have to do what it says on the tin? I grant that there doesn't seem to be a better option, but I bet we're going to have a lot of really unhappy users if we do this.
From:"Joshua D(dot) Drake" <jd(at)commandprompt(dot)com>
Date:2018-04-09 17:26:24
On 04/09/2018 09:45 AM, Robert Haas wrote:
On Mon, Apr 9, 2018 at 8:16 AM, Craig Ringer
wrote:
In the mean time, I propose that we fsync() on close() before we age FDs out of the LRU on backends. Yes, that will hurt throughput and cause stalls, but we don't seem to have many better options. At least it'll only flush what we actually wrote to the OS buffers not what we may have in shared_buffers. If the bgwriter does the same thing, we should be 100% safe from this problem on 4.13+, and it'd be trivial to make it a GUC much like the fsync or full_page_writes options that people can turn off if they know the risks / know their storage is safe / don't care.
I have a really tough time believing this is the right way to solve the problem. We suffered for years because of ext3's desire to flush the entire page cache whenever any single file was fsync()'d, which was terrible. Eventually ext4 became the norm, and the problem went away. Now we're going to deliberately insert logic to do a very similar kind of terrible thing because the kernel developers have decided that fsync() doesn't have to do what it says on the tin? I grant that there doesn't seem to be a better option, but I bet we're going to have a lot of really unhappy users if we do this.
I don't have a better option but whatever we do, it should be an optional (GUC) change. We have plenty of YEARS of people not noticing this issue and Robert's correct, if we go back to an era of things like stalls it is going to look bad on us no matter how we describe the problem.
From:Gasper Zejn <zejn(at)owca(dot)info>
Date:2018-04-09 18:02:21
On 09. 04. 2018 15:42, Tomas Vondra wrote:
On 04/09/2018 12:29 AM, Bruce Momjian wrote:
An crazy idea would be to have a daemon that checks the logs and stops Postgres when it seems something wrong.
That doesn't seem like a very practical way. It's better than nothing, of course, but I wonder how would that work with containers (where I think you may not have access to the kernel log at all). Also, I'm pretty sure the messages do change based on kernel version (and possibly filesystem) so parsing it reliably seems rather difficult. And we probably don't want to PANIC after I/O error on an unrelated device, so we'd need to understand which devices are related to PostgreSQL.
regards
For a bit less (or more) crazy idea, I'd imagine creating a Linux kernel module with kprobe/kretprobe capturing the file passed to fsync or even byte range within file and corresponding return value shouldn't be that hard. Kprobe has been a part of Linux kernel for a really long time, and from first glance it seems like it could be backported to 2.6 too.
Then you could have stable log messages or implement some kind of "fsync error log notification" via whatever is the most sane way to get this out of kernel.
If the kernel is new enough and has eBPF support (seems like >=4.4), using bcc-tools[1] should enable you to write a quick script to get exactly that info via perf events[2].
Obviously, that's a stopgap solution ...
[1]
https://github.com/iovisor/bcc
[2]
https://blog.yadutaf.fr/2016/03/30/turn-any-syscall-into-event-introducing-ebpf-kernel-probes/
From:Mark Dilger <hornschnorter(at)gmail(dot)com>
Date:2018-04-09 18:29:42
On Apr 9, 2018, at 10:26 AM, Joshua D. Drake
wrote:
We have plenty of YEARS of people not noticing this issue
I disagree. I have noticed this problem, but blamed it on other things. For over five years now, I have had to tell customers not to use thin provisioning, and I have had to add code to postgres to refuse to perform inserts or updates if the disk volume is more than 80% full. I have lost count of the number of customers who are running an older version of the product (because they refuse to upgrade) and come back with complaints that they ran out of disk and now their database is corrupt. All this time, I have been blaming this on virtualization and thin provisioning.
From:Robert Haas <robertmhaas(at)gmail(dot)com>
Date:2018-04-09 19:02:11
On Mon, Apr 9, 2018 at 12:45 PM, Robert Haas
wrote:
Ouch. If a process exits -- say, because the user typed \q into psql -- then you're talking about potentially calling fsync() on a really large number of file descriptor flushing many gigabytes of data to disk. And it may well be that you never actually wrote any data to any of those file descriptors -- those writes could have come from other backends. Or you may have written a little bit of data through those FDs, but there could be lots of other data that you end up flushing incidentally. Perfectly innocuous things like starting up a backend, running a few short queries, and then having that backend exit suddenly turn into something that could have a massive system-wide performance impact.
Also, if a backend ever manages to exit without running through this code, or writes any dirty blocks afterward, then this still fails to fix the problem completely. I guess that's probably avoidable -- we can put this late in the shutdown sequence and PANIC if it fails.
I have a really tough time believing this is the right way to solve the problem. We suffered for years because of ext3's desire to flush the entire page cache whenever any single file was fsync()'d, which was terrible. Eventually ext4 became the norm, and the problem went away. Now we're going to deliberately insert logic to do a very similar kind of terrible thing because the kernel developers have decided that fsync() doesn't have to do what it says on the tin? I grant that there doesn't seem to be a better option, but I bet we're going to have a lot of really unhappy users if we do this.
What about the bug we fixed in
https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=2ce439f3379aed857517c8ce207485655000fc8e
? Say somebody does something along the lines of:
ps uxww | grep postgres | grep -v grep | awk '{print $2}' | xargs kill -9
...and then restarts postgres. Craig's proposal wouldn't cover this case, because there was no opportunity to run fsync() after the first crash, and there's now no way to go back and fsync() any stuff we didn't fsync() before, because the kernel may have already thrown away the error state, or may lie to us and tell us everything is fine (because our new fd wasn't opened early enough). I can't find the original discussion that led to that commit right now, so I'm not exactly sure what scenarios we were thinking about. But I think it would at least be a problem if full_page_writes=off or if you had previously started the server with fsync=off and now wish to switch to fsync=on after completing a bulk load or similar. Recovery can read a page, see that it looks OK, and continue, and then a later fsync() failure can revert that page to an earlier state and now your database is corrupted -- and there's absolute no way to detect this because write() gives you the new page contents later, fsync() doesn't feel obliged to tell you about the error because your fd wasn't opened early enough, and eventually the write can be discarded and you'll revert back to the old page version with no errors ever being reported anywhere.
Another consequence of this behavior that initdb -S is never reliable, so pg_rewind's use of it doesn't actually fix the problem it was intended to solve. It also means that initdb itself isn't crash-safe, since the data file changes are made by the backend but initdb itself is doing the fsyncs, and initdb has no way of knowing what files the backend is going to create and therefore can't -- even theoretically -- open them first.
What's being presented to us as the API contract that we should expect from buffered I/O is that if you open a file and read() from it, call fsync(), and get no error, the kernel may nevertheless decide that some previous write that it never managed to flush can't be flushed, and then revert the page to the contents it had at some point in the past. That's mostly or less equivalent to letting a malicious adversary randomly overwrite database pages plausible-looking but incorrect contents without notice and hoping you can still build a reliable system. You can avoid the problem if you can always open an fd for every file you want to modify before it's written and hold on to it until after it's fsync'd, but that's pretty hard to guarantee in the face of kill -9.
I think the simplest technological solution to this problem is to rewrite the entire backend and all supporting processes to use O_DIRECT everywhere. To maintain adequate performance, we'll have to write a complete I/O scheduling system inside PostgreSQL. Also, since we'll now have to make shared_buffers much larger -- since we'll no longer be benefiting from the OS cache -- we'll need to replace the use of malloc() with an allocator that pulls from shared_buffers. Plus, as noted, we'll need to totally rearchitect several of our critical frontend tools. Let's freeze all other development for the next year while we work on that, and put out a notice that Linux is no longer a supported platform for any existing release. Before we do that, we might want to check whether fsync() actually writes the data to disk in a usable way even with O_DIRECT. If not, we should just de-support Linux entirely as a hopelessly broken and unsupportable platform.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 19:13:14
Hi,
On 2018-04-09 15:02:11 -0400, Robert Haas wrote:
I think the simplest technological solution to this problem is to rewrite the entire backend and all supporting processes to use O_DIRECT everywhere. To maintain adequate performance, we'll have to write a complete I/O scheduling system inside PostgreSQL. Also, since we'll now have to make shared_buffers much larger -- since we'll no longer be benefiting from the OS cache -- we'll need to replace the use of malloc() with an allocator that pulls from shared_buffers. Plus, as noted, we'll need to totally rearchitect several of our critical frontend tools. Let's freeze all other development for the next year while we work on that, and put out a notice that Linux is no longer a supported platform for any existing release. Before we do that, we might want to check whether fsync() actually writes the data to disk in a usable way even with O_DIRECT. If not, we should just de-support Linux entirely as a hopelessly broken and unsupportable platform.
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
We're talking about the storage layer returning an irresolvable error. You're hosed even if we report it properly. Yes, it'd be nice if we could report it reliably. But that doesn't change the fact that what we're doing is ensuring that data is safely fsynced unless storage fails, in which case it's not safely fsynced anyway.
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 19:22:58
On 04/09/2018 08:29 PM, Mark Dilger wrote:
On Apr 9, 2018, at 10:26 AM, Joshua D. Drake
wrote: We have plenty of YEARS of people not noticing this issue
I disagree. I have noticed this problem, but blamed it on other things. For over five years now, I have had to tell customers not to use thin provisioning, and I have had to add code to postgres to refuse to perform inserts or updates if the disk volume is more than 80% full. I have lost count of the number of customers who are running an older version of the product (because they refuse to upgrade) and come back with complaints that they ran out of disk and now their database is corrupt. All this time, I have been blaming this on virtualization and thin provisioning.
Yeah. There's a big difference between not noticing an issue because it does not happen very often vs. attributing it to something else. If we had the ability to revisit past data corruption cases, we would probably discover a fair number of cases caused by this.
The other thing we probably need to acknowledge is that the environment changes significantly - things like thin provisioning are likely to get even more common, increasing the incidence of these issues.
From:Peter Geoghegan <pg(at)bowt(dot)ie>
Date:2018-04-09 19:25:33
On Mon, Apr 9, 2018 at 12:13 PM, Andres Freund
wrote:
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
+1
We're talking about the storage layer returning an irresolvable error. You're hosed even if we report it properly. Yes, it'd be nice if we could report it reliably. But that doesn't change the fact that what we're doing is ensuring that data is safely fsynced unless storage fails, in which case it's not safely fsynced anyway.
Right. We seem to be implicitly assuming that there is a big difference between a problem in the storage layer that we could in principle detect, but don't, and any other problem in the storage layer. I've read articles claiming that technologies like SMART are not really reliable in a practical sense [1], so it seems to me that there is reason to doubt that this gap is all that big.
That said, I suspect that the problems with running out of disk space are serious practical problems. I have personally scoffed at stories involving Postgres databases corruption that gets attributed to running out of disk space. Looks like I was dead wrong.
[1]
https://danluu.com/file-consistency/
-- "Filesystem correctness"
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-09 19:26:21
On Mon, Apr 09, 2018 at 04:29:36PM +0100, Greg Stark wrote:
Honestly I don't think there's
any
way to use the current interface to implement reliable operation. Even that embedded database using a single process and keeping every file open all the time (which means file descriptor limits limit its scalability) can be having silent corruption whenever some other process like a backup program comes along and calls fsync (or even sync?).
That is indeed true (sync would induce fsync on open inodes and clear the error), and that's a nasty bug that apparently went unnoticed for a very long time. Hopefully the errseq_t linux 4.13 fixes deal with at least this issue, but similar fixes need to be adopted by many other kernels (all those that mark failed pages as clean).
I honestly do not expect that keeping around the failed pages will be an acceptable change for most kernels, and as such the recommendation will probably be to coordinate in userspace for the fsync().
What about having buffered IO with implied fsync() atomicity via O_SYNC? This would probably necessitate some helper threads that mask the latency and present an async interface to the rest of PG, but sounds less intrusive than going for DIO.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 19:29:16
On 2018-04-09 21:26:21 +0200, Anthony Iliopoulos wrote:
What about having buffered IO with implied fsync() atomicity via O_SYNC?
You're kidding, right? We could also just add sleep(30)'s all over the tree, and hope that that'll solve the problem. There's a reason we don't permanently fsync everything. Namely that it'll be way too slow.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 19:37:03
On April 9, 2018 12:26:21 PM PDT, Anthony Iliopoulos
wrote:
I honestly do not expect that keeping around the failed pages will be an acceptable change for most kernels, and as such the recommendation will probably be to coordinate in userspace for the fsync().
Why is that required? You could very well just keep per inode information about fatal failures that occurred around. Report errors until that bit is explicitly cleared. Yes, that keeps some memory around until unmount if nobody clears it. But it's orders of magnitude less, and results in usable semantics.
From:Justin Pryzby <pryzby(at)telsasoft(dot)com>
Date:2018-04-09 19:41:19
On Mon, Apr 09, 2018 at 09:31:56AM +0800, Craig Ringer wrote:
You could make the argument that it's OK to forget if the entire file system goes away. But actually, why is that ok?
I was going to say that it'd be okay to clear error flag on umount, since any opened files would prevent unmounting; but, then I realized we need to consider the case of close()ing all FDs then opening them later..in another process.
I was going to say that's fine for postgres, since it chdir()s into its basedir, but actually not fine for nondefault tablespaces..
On Mon, Apr 09, 2018 at 02:54:16PM +0200, Anthony Iliopoulos wrote:
notification descriptor open, where the kernel would inject events related to writeback failures of files under watch (potentially enriched to contain info regarding the exact failed pages and the file offset they map to).
For postgres that'd require backend processes to open() an file such that, following its close(), any writeback errors are "signalled" to the checkpointer process...
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-09 19:44:31
On Mon, Apr 09, 2018 at 12:29:16PM -0700, Andres Freund wrote:
On 2018-04-09 21:26:21 +0200, Anthony Iliopoulos wrote:
What about having buffered IO with implied fsync() atomicity via O_SYNC?
You're kidding, right? We could also just add sleep(30)'s all over the tree, and hope that that'll solve the problem. There's a reason we don't permanently fsync everything. Namely that it'll be way too slow.
I am assuming you can apply the same principle of selectively using O_SYNC at times and places that you'd currently actually call fsync().
Also assuming that you'd want to have a backwards-compatible solution for all those kernels that don't keep the pages around, irrespective of future fixes. Short of loading a kernel module and dealing with the problem directly, the only other available options seem to be either O_SYNC, O_DIRECT or ignoring the issue.
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 19:47:44
On 04/09/2018 04:22 PM, Anthony Iliopoulos wrote:
On Mon, Apr 09, 2018 at 03:33:18PM +0200, Tomas Vondra wrote:
We already have dirty_bytes and dirty_background_bytes, for example. I don't see why there couldn't be another limit defining how much dirty data to allow before blocking writes altogether. I'm sure it's not that simple, but you get the general idea - do not allow using all available memory because of writeback issues, but don't throw the data away in case it's just a temporary issue.
Sure, there could be knobs for limiting how much memory such "zombie" pages may occupy. Not sure how helpful it would be in the long run since this tends to be highly application-specific, and for something with a large data footprint one would end up tuning this accordingly in a system-wide manner. This has the potential to leave other applications running in the same system with very little memory, in cases where for example original application crashes and never clears the error. Apart from that, further interfaces would need to be provided for actually dealing with the error (again assuming non-transient issues that may not be fixed transparently and that temporary issues are taken care of by lower layers of the stack).
I don't quite see how this is any different from other possible issues when running multiple applications on the same system. One application can generate a lot of dirty data, reaching dirty_bytes and forcing the other applications on the same host to do synchronous writes.
Of course, you might argue that is a temporary condition - it will resolve itself once the dirty pages get written to storage. In case of an I/O issue, it is a permanent impact - it will not resolve itself unless the I/O problem gets fixed.
Not sure what interfaces would need to be written? Possibly something that says "drop dirty pages for these files" after the application gets killed or something. That makes sense, of course.
Well, there seem to be kernels that seem to do exactly that already. At least that's how I understand what this thread says about FreeBSD and Illumos, for example. So it's not an entirely insane design, apparently.
It is reasonable, but even FreeBSD has a big fat comment right there (since 2017), mentioning that there can be no recovery from EIO at the block layer and this needs to be done differently. No idea how an application running on top of either FreeBSD or Illumos would actually recover from this error (and clear it out), other than remounting the fs in order to force dropping of relevant pages. It does provide though indeed a persistent error indication that would allow Pg to simply reliably panic. But again this does not necessarily play well with other applications that may be using the filesystem reliably at the same time, and are now faced with EIO while their own writes succeed to be persisted.
In my experience when you have a persistent I/O error on a device, it likely affects all applications using that device. So unmounting the fs to clear the dirty pages seems like an acceptable solution to me.
I don't see what else the application should do? In a way I'm suggesting applications don't really want to be responsible for recovering (cleanup or dirty pages etc.). We're more than happy to hand that over to kernel, e.g. because each kernel will do that differently. What we however do want is reliable information about fsync outcome, which we need to properly manage WAL, checkpoints etc.
Ideally, you'd want a (potentially persistent) indication of error localized to a file region (mapping the corresponding failed writeback pages). NetBSD is already implementing fsync_ranges(), which could be a step in the right direction.
One has to wonder how many applications actually use this correctly, considering PostgreSQL cares about data durability/consistency so much and yet we've been misunderstanding how it works for 20+ years.
I would expect it would be very few, potentially those that have a very simple process model (e.g. embedded DBs that can abort a txn on fsync() EIO). I think that durability is a rather complex cross-layer issue which has been grossly misunderstood similarly in the past (e.g. see [1]). It seems that both the OS and DB communities greatly benefit from a periodic reality check, and I see this as an opportunity for strengthening the IO stack in an end-to-end manner.
Right. What I was getting to is that perhaps the current fsync() behavior is not very practical for building actual applications.
Best regards, Anthony
[1]
https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-pillai.pdf
Thanks. The paper looks interesting.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-09 19:51:12
On Mon, Apr 09, 2018 at 12:37:03PM -0700, Andres Freund wrote:
On April 9, 2018 12:26:21 PM PDT, Anthony Iliopoulos
wrote:
I honestly do not expect that keeping around the failed pages will be an acceptable change for most kernels, and as such the recommendation will probably be to coordinate in userspace for the fsync().
Why is that required? You could very well just keep per inode information about fatal failures that occurred around. Report errors until that bit is explicitly cleared. Yes, that keeps some memory around until unmount if nobody clears it. But it's orders of magnitude less, and results in usable semantics.
As discussed before, I think this could be acceptable, especially if you pair it with an opt-in mechanism (only applications that care to deal with this will have to), and would give it a shot.
Still need a way to deal with all other systems and prior kernel releases that are eating fsync() writeback errors even over sync().
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 19:54:05
On 04/09/2018 09:37 PM, Andres Freund wrote:
On April 9, 2018 12:26:21 PM PDT, Anthony Iliopoulos
wrote:
I honestly do not expect that keeping around the failed pages will be an acceptable change for most kernels, and as such the recommendation will probably be to coordinate in userspace for the fsync().
Why is that required? You could very well just keep per inode information about fatal failures that occurred around. Report errors until that bit is explicitly cleared. Yes, that keeps some memory around until unmount if nobody clears it. But it's orders of magnitude less, and results in usable semantics.
Isn't the expectation that when a fsync call fails, the next one will retry writing the pages in the hope that it succeeds?
Of course, it's also possible to do what you suggested, and simply mark the inode as failed. In which case the next fsync can't possibly retry the writes (e.g. after freeing some space on thin-provisioned system), but we'd get reliable failure mode.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 19:59:34
On 2018-04-09 14:41:19 -0500, Justin Pryzby wrote:
On Mon, Apr 09, 2018 at 09:31:56AM +0800, Craig Ringer wrote:
You could make the argument that it's OK to forget if the entire file system goes away. But actually, why is that ok?
I was going to say that it'd be okay to clear error flag on umount, since any opened files would prevent unmounting; but, then I realized we need to consider the case of close()ing all FDs then opening them later..in another process.
On Mon, Apr 09, 2018 at 02:54:16PM +0200, Anthony Iliopoulos wrote:
notification descriptor open, where the kernel would inject events related to writeback failures of files under watch (potentially enriched to contain info regarding the exact failed pages and the file offset they map to).
For postgres that'd require backend processes to open() an file such that, following its close(), any writeback errors are "signalled" to the checkpointer process...
I don't think that's as hard as some people argued in this thread. We could very well open a pipe in postmaster with the write end open in each subprocess, and the read end open only in checkpointer (and postmaster, but unused there). Whenever closing a file descriptor that was dirtied in the current process, send it over the pipe to the checkpointer. The checkpointer then can receive all those file descriptors (making sure it's not above the limit, fsync(), close() ing to make room if necessary). The biggest complication would presumably be to deduplicate the received filedescriptors for the same file, without loosing track of any errors.
Even better, we could do so via a dedicated worker. That'd quite possibly end up as a performance benefit.
I was going to say that's fine for postgres, since it chdir()s into its basedir, but actually not fine for nondefault tablespaces..
I think it'd be fair to open PG_VERSION of all created tablespaces. Would require some hangups to signal checkpointer (or whichever process) to do so when creating one, but it shouldn't be too hard. Some people would complain because they can't do some nasty hacks anymore, but it'd also save peoples butts by preventing them from accidentally unmounting.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 20:04:20
Hi,
On 2018-04-09 21:54:05 +0200, Tomas Vondra wrote:
Isn't the expectation that when a fsync call fails, the next one will retry writing the pages in the hope that it succeeds?
Some people expect that, I personally don't think it's a useful expectation.
We should just deal with this by crash-recovery. The big problem I see is that you always need to keep an file descriptor open for pretty much any file written to inside and outside of postgres, to be guaranteed to see errors. And that'd solve that. Even if retrying would work, I'd advocate for that (I've done so in the past, and I've written code in pg that panics on fsync failure...).
What we'd need to do however is to clear that bit during crash recovery... Which is interesting from a policy perspective. Could be that other apps wouldn't want that.
I also wonder if we couldn't just somewhere read each relevant mounted filesystem's errseq value. Whenever checkpointer notices before finishing a checkpoint that it has changed, do a crash restart.
From:Mark Dilger <hornschnorter(at)gmail(dot)com>
Date:2018-04-09 20:25:54
On Apr 9, 2018, at 12:13 PM, Andres Freund
wrote:
Hi,
On 2018-04-09 15:02:11 -0400, Robert Haas wrote:
I think the simplest technological solution to this problem is to rewrite the entire backend and all supporting processes to use O_DIRECT everywhere. To maintain adequate performance, we'll have to write a complete I/O scheduling system inside PostgreSQL. Also, since we'll now have to make shared_buffers much larger -- since we'll no longer be benefiting from the OS cache -- we'll need to replace the use of malloc() with an allocator that pulls from shared_buffers. Plus, as noted, we'll need to totally rearchitect several of our critical frontend tools. Let's freeze all other development for the next year while we work on that, and put out a notice that Linux is no longer a supported platform for any existing release. Before we do that, we might want to check whether fsync() actually writes the data to disk in a usable way even with O_DIRECT. If not, we should just de-support Linux entirely as a hopelessly broken and unsupportable platform.
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
We're talking about the storage layer returning an irresolvable error. You're hosed even if we report it properly. Yes, it'd be nice if we could report it reliably. But that doesn't change the fact that what we're doing is ensuring that data is safely fsynced unless storage fails, in which case it's not safely fsynced anyway.
I was reading this thread up until now as meaning that the standby could receive corrupt WAL data and become corrupted. That seems a much bigger problem than merely having the master become corrupted in some unrecoverable way. It is a long standing expectation that serious hardware problems on the master can result in the master needing to be replaced. But there has not been an expectation that the one or more standby servers would be taken down along with the master, leaving all copies of the database unusable. If this bug corrupts the standby servers, too, then it is a whole different class of problem than the one folks have come to expect.
Your comment reads as if this is a problem isolated to whichever server has the problem, and will not get propagated to other servers. Am I reading that right?
Can anybody clarify this for non-core-hacker folks following along at home?
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 20:30:00
On 04/09/2018 10:04 PM, Andres Freund wrote:
Hi,
On 2018-04-09 21:54:05 +0200, Tomas Vondra wrote:
Isn't the expectation that when a fsync call fails, the next one will retry writing the pages in the hope that it succeeds?
Some people expect that, I personally don't think it's a useful expectation.
Maybe. I'd certainly prefer automated recovery from an temporary I/O issues (like full disk on thin-provisioning) without the database crashing and restarting. But I'm not sure it's worth the effort.
And most importantly, it's rather delusional to think the kernel developers are going to be enthusiastic about that approach ...
We should just deal with this by crash-recovery. The big problem I see is that you always need to keep an file descriptor open for pretty much any file written to inside and outside of postgres, to be guaranteed to see errors. And that'd solve that. Even if retrying would work, I'd advocate for that (I've done so in the past, and I've written code in pg that panics on fsync failure...).
Sure. And it's likely way less invasive from kernel perspective.
What we'd need to do however is to clear that bit during crash recovery... Which is interesting from a policy perspective. Could be that other apps wouldn't want that.
IMHO it'd be enough if a remount clears it.
I also wonder if we couldn't just somewhere read each relevant mounted filesystem's errseq value. Whenever checkpointer notices before finishing a checkpoint that it has changed, do a crash restart.
Hmmmm, that's an interesting idea, and it's about the only thing that would help us on older kernels. There's a wb_err in adress_space, but that's at inode level. Not sure if there's something at fs level.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 20:34:15
Hi,
On 2018-04-09 13:25:54 -0700, Mark Dilger wrote:
I was reading this thread up until now as meaning that the standby could receive corrupt WAL data and become corrupted.
I don't see that as a real problem here. For one the problematic scenarios shouldn't readily apply, for another WAL is checksummed.
There's the problem that a new basebackup would potentially become corrupted however. And similarly pg_rewind.
Note that I'm not saying that we and/or linux shouldn't change anything. Just that the apocalypse isn't here.
Your comment reads as if this is a problem isolated to whichever server has the problem, and will not get propagated to other servers. Am I reading that right?
I think that's basically right. There's cases where corruption could get propagated, but they're not straightforward.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 20:37:31
Hi,
On 2018-04-09 22:30:00 +0200, Tomas Vondra wrote:
Maybe. I'd certainly prefer automated recovery from an temporary I/O issues (like full disk on thin-provisioning) without the database crashing and restarting. But I'm not sure it's worth the effort.
Oh, I agree on that one. But that's more a question of how we force the kernel's hand on allocating disk space. In most cases the kernel allocates the disk space immediately, even if delayed allocation is in effect. For the cases where that's not the case (if there are current ones, rather than just past bugs), we should be able to make sure that's not an issue by pre-zeroing the data and/or using fallocate.
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 20:43:03
On 04/09/2018 10:25 PM, Mark Dilger wrote:
On Apr 9, 2018, at 12:13 PM, Andres Freund
wrote:
Hi,
On 2018-04-09 15:02:11 -0400, Robert Haas wrote:
I think the simplest technological solution to this problem is to rewrite the entire backend and all supporting processes to use O_DIRECT everywhere. To maintain adequate performance, we'll have to write a complete I/O scheduling system inside PostgreSQL. Also, since we'll now have to make shared_buffers much larger -- since we'll no longer be benefiting from the OS cache -- we'll need to replace the use of malloc() with an allocator that pulls from shared_buffers. Plus, as noted, we'll need to totally rearchitect several of our critical frontend tools. Let's freeze all other development for the next year while we work on that, and put out a notice that Linux is no longer a supported platform for any existing release. Before we do that, we might want to check whether fsync() actually writes the data to disk in a usable way even with O_DIRECT. If not, we should just de-support Linux entirely as a hopelessly broken and unsupportable platform.
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
We're talking about the storage layer returning an irresolvable error. You're hosed even if we report it properly. Yes, it'd be nice if we could report it reliably. But that doesn't change the fact that what we're doing is ensuring that data is safely fsynced unless storage fails, in which case it's not safely fsynced anyway.
I was reading this thread up until now as meaning that the standby could receive corrupt WAL data and become corrupted. That seems a much bigger problem than merely having the master become corrupted in some unrecoverable way. It is a long standing expectation that serious hardware problems on the master can result in the master needing to be replaced. But there has not been an expectation that the one or more standby servers would be taken down along with the master, leaving all copies of the database unusable. If this bug corrupts the standby servers, too, then it is a whole different class of problem than the one folks have come to expect.
Your comment reads as if this is a problem isolated to whichever server has the problem, and will not get propagated to other servers. Am I reading that right?
Can anybody clarify this for non-core-hacker folks following along at home?
That's a good question. I don't see any guarantee it'd be isolated to the master node. Consider this example:
(0) checkpoint happens on the primary
(1) a page gets modified, a full-page gets written to WAL
(2) the page is written out to page cache
(3) writeback of that page fails (and gets discarded)
(4) we attempt to modify the page again, but we read the stale version
(5) we modify the stale version, writing the change to WAL
The standby will get the full-page, and then a WAL from the stale page version. That doesn't seem like a story with a happy end, I guess. But I might be easily missing some protection built into the WAL ...
From:Mark Dilger <hornschnorter(at)gmail(dot)com>
Date:2018-04-09 20:55:29
On Apr 9, 2018, at 1:43 PM, Tomas Vondra
wrote:
On 04/09/2018 10:25 PM, Mark Dilger wrote:
On Apr 9, 2018, at 12:13 PM, Andres Freund
wrote:
Hi,
On 2018-04-09 15:02:11 -0400, Robert Haas wrote:
I think the simplest technological solution to this problem is to rewrite the entire backend and all supporting processes to use O_DIRECT everywhere. To maintain adequate performance, we'll have to write a complete I/O scheduling system inside PostgreSQL. Also, since we'll now have to make shared_buffers much larger -- since we'll no longer be benefiting from the OS cache -- we'll need to replace the use of malloc() with an allocator that pulls from shared_buffers. Plus, as noted, we'll need to totally rearchitect several of our critical frontend tools. Let's freeze all other development for the next year while we work on that, and put out a notice that Linux is no longer a supported platform for any existing release. Before we do that, we might want to check whether fsync() actually writes the data to disk in a usable way even with O_DIRECT. If not, we should just de-support Linux entirely as a hopelessly broken and unsupportable platform.
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
We're talking about the storage layer returning an irresolvable error. You're hosed even if we report it properly. Yes, it'd be nice if we could report it reliably. But that doesn't change the fact that what we're doing is ensuring that data is safely fsynced unless storage fails, in which case it's not safely fsynced anyway.
I was reading this thread up until now as meaning that the standby could receive corrupt WAL data and become corrupted. That seems a much bigger problem than merely having the master become corrupted in some unrecoverable way. It is a long standing expectation that serious hardware problems on the master can result in the master needing to be replaced. But there has not been an expectation that the one or more standby servers would be taken down along with the master, leaving all copies of the database unusable. If this bug corrupts the standby servers, too, then it is a whole different class of problem than the one folks have come to expect.
Your comment reads as if this is a problem isolated to whichever server has the problem, and will not get propagated to other servers. Am I reading that right?
Can anybody clarify this for non-core-hacker folks following along at home?
That's a good question. I don't see any guarantee it'd be isolated to the master node. Consider this example:
(0) checkpoint happens on the primary
(1) a page gets modified, a full-page gets written to WAL
(2) the page is written out to page cache
(3) writeback of that page fails (and gets discarded)
(4) we attempt to modify the page again, but we read the stale version
(5) we modify the stale version, writing the change to WAL
The standby will get the full-page, and then a WAL from the stale page version. That doesn't seem like a story with a happy end, I guess. But I might be easily missing some protection built into the WAL ...
I can also imagine a master and standby that are similarly provisioned, and thus hit an out of disk error at around the same time, resulting in corruption on both, even if not the same corruption. When choosing to have one standby, or two standbys, or ten standbys, one needs to be able to assume a certain amount of statistical independence between failures on one server and failures on another. If they are tightly correlated dependent variables, then the conclusion that the probability of all nodes failing simultaneously is vanishingly small becomes invalid.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-09 21:08:29
Hi,
On 2018-04-09 13:55:29 -0700, Mark Dilger wrote:
I can also imagine a master and standby that are similarly provisioned, and thus hit an out of disk error at around the same time, resulting in corruption on both, even if not the same corruption.
I think it's a grave mistake conflating ENOSPC issues (which we should solve by making sure there's always enough space pre-allocated), with EIO type errors. The problem is different, the solution is different.
From:Tomas Vondra <tomas(dot)vondra(at)2ndquadrant(dot)com>
Date:2018-04-09 21:25:52
On 04/09/2018 11:08 PM, Andres Freund wrote:
Hi,
On 2018-04-09 13:55:29 -0700, Mark Dilger wrote:
I can also imagine a master and standby that are similarly provisioned, and thus hit an out of disk error at around the same time, resulting in corruption on both, even if not the same corruption.
I think it's a grave mistake conflating ENOSPC issues (which we should solve by making sure there's always enough space pre-allocated), with EIO type errors. The problem is different, the solution is different.
In any case, that certainly does not count as data corruption spreading from the master to standby.
From:Mark Dilger <hornschnorter(at)gmail(dot)com>
Date:2018-04-09 21:33:29
On Apr 9, 2018, at 2:25 PM, Tomas Vondra
wrote:
On 04/09/2018 11:08 PM, Andres Freund wrote:
Hi,
On 2018-04-09 13:55:29 -0700, Mark Dilger wrote:
I can also imagine a master and standby that are similarly provisioned, and thus hit an out of disk error at around the same time, resulting in corruption on both, even if not the same corruption.
I think it's a grave mistake conflating ENOSPC issues (which we should solve by making sure there's always enough space pre-allocated), with EIO type errors. The problem is different, the solution is different.
I'm happy to take your word for that.
In any case, that certainly does not count as data corruption spreading from the master to standby.
Maybe not from the point of view of somebody looking at the code. But a user might see it differently. If the data being loaded into the master and getting replicated to the standby "causes" both to get corrupt, then it seems like corruption spreading. I put "causes" in quotes because there is some argument to be made about "correlation does not prove cause" and so forth, but it still feels like causation from an arms length perspective. If there is a pattern of standby servers tending to fail more often right around the time that the master fails, you'll have a hard time comforting users, "hey, it's not technically causation." If loading data into the master causes the master to hit ENOSPC, and replicating that data to the standby causes the standby to hit ENOSPC, and if the bug abound ENOSPC has not been fixed, then this looks like corruption spreading.
I'm certainly planning on taking a hard look at the disk allocation on my standby servers right soon now.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-09 22:33:16
On Tue, Apr 10, 2018 at 2:22 AM, Anthony Iliopoulos
wrote:
On Mon, Apr 09, 2018 at 03:33:18PM +0200, Tomas Vondra wrote:
Well, there seem to be kernels that seem to do exactly that already. At least that's how I understand what this thread says about FreeBSD and Illumos, for example. So it's not an entirely insane design, apparently.
It is reasonable, but even FreeBSD has a big fat comment right there (since 2017), mentioning that there can be no recovery from EIO at the block layer and this needs to be done differently. No idea how an application running on top of either FreeBSD or Illumos would actually recover from this error (and clear it out), other than remounting the fs in order to force dropping of relevant pages. It does provide though indeed a persistent error indication that would allow Pg to simply reliably panic. But again this does not necessarily play well with other applications that may be using the filesystem reliably at the same time, and are now faced with EIO while their own writes succeed to be persisted.
Right. For anyone interested, here is the change you mentioned, and an interesting one that came a bit earlier last year:
Retrying may well be futile, but at least future fsync() calls won't report success bogusly. There may of course be more space-efficient ways to represent that state as the comment implies, while never lying to the user -- perhaps involving filesystem level or (pinned) inode level errors that stop all writes until unmounted. Something tells me they won't resort to flakey fsync() error reporting.
I wonder if anyone can tell us what Windows, AIX and HPUX do here.
[1]
https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-pillai.pdf
Very interesting, thanks.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-10 00:32:20
On Tue, Apr 10, 2018 at 10:33 AM, Thomas Munro
wrote:
I wonder if anyone can tell us what Windows, AIX and HPUX do here.
I created a wiki page to track what we know (or think we know) about fsync() on various operating systems:
https://wiki.postgresql.org/wiki/Fsync_Errors
If anyone has more information or sees mistakes, please go ahead and edit it.
From:Andreas Karlsson <andreas(at)proxel(dot)se>
Date:2018-04-10 00:41:10
On 04/09/2018 02:16 PM, Craig Ringer wrote:
I'd like a middle ground where the kernel lets us register our interest and tells us if it lost something, without us having to keep eight million FDs open for some long period. "Tell us about anything that happens under pgdata/" or an inotify-style per-directory-registration option. I'd even say that's ideal.
Could there be a risk of a race condition here where fsync incorrectly returns success before we get the notification of that something went wrong?
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-10 01:44:59
On 10 April 2018 at 03:59, Andres Freund
wrote:
On 2018-04-09 14:41:19 -0500, Justin Pryzby wrote:
On Mon, Apr 09, 2018 at 09:31:56AM +0800, Craig Ringer wrote:
You could make the argument that it's OK to forget if the entire file system goes away. But actually, why is that ok?
I was going to say that it'd be okay to clear error flag on umount, since any opened files would prevent unmounting; but, then I realized we need to consider the case of close()ing all FDs then opening them later..in another process.
On Mon, Apr 09, 2018 at 02:54:16PM +0200, Anthony Iliopoulos wrote:
notification descriptor open, where the kernel would inject events related to writeback failures of files under watch (potentially enriched to contain info regarding the exact failed pages and the file offset they map to).
For postgres that'd require backend processes to open() an file such that, following its close(), any writeback errors are "signalled" to the checkpointer process...
I don't think that's as hard as some people argued in this thread. We could very well open a pipe in postmaster with the write end open in each subprocess, and the read end open only in checkpointer (and postmaster, but unused there). Whenever closing a file descriptor that was dirtied in the current process, send it over the pipe to the checkpointer. The checkpointer then can receive all those file descriptors (making sure it's not above the limit, fsync(), close() ing to make room if necessary). The biggest complication would presumably be to deduplicate the received filedescriptors for the same file, without loosing track of any errors.
Yep. That'd be a cheaper way to do it, though it wouldn't work on Windows. Though we don't know how Windows behaves here at all yet.
Prior discussion upthread had the checkpointer open()ing a file at the same time as a backend, before the backend writes to it. But passing the fd when the backend is done with it would be better.
We'd need a way to dup() the fd and pass it back to a backend when it needed to reopen it sometimes, or just make sure to keep the oldest copy of the fd when a backend reopens multiple times, but that's no biggie.
We'd still have to fsync() out early in the checkpointer if we ran out of space in our FD list, and initscripts would need to change our ulimit or we'd have to do it ourselves in the checkpointer. But neither seems insurmountable.
FWIW, I agree that this is a corner case, but it's getting to be a pretty big corner with the spread of overcommitted, dedupliating SANs, cloud storage, etc. Not all I/O errors indicate permanent hardware faults, disk failures, etc, as I outlined earlier. I'm very curious to know what AWS EBS's error semantics are, and other cloud network block stores. (I posted on Amazon forums
https://forums.aws.amazon.com/thread.jspa?threadID=279274&tstart=0
but nothing so far).
I'm also not particularly inclined to trust that all file systems will always reliably reserve space without having some cases where they'll fail writeback on space exhaustion.
So we don't need to panic and freak out, but it's worth looking at the direction the storage world is moving in, and whether this will become a bigger issue over time.
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-10 01:52:21
On Tue, Apr 10, 2018 at 1:44 PM, Craig Ringer
wrote:
On 10 April 2018 at 03:59, Andres Freund
wrote:
I don't think that's as hard as some people argued in this thread. We could very well open a pipe in postmaster with the write end open in each subprocess, and the read end open only in checkpointer (and postmaster, but unused there). Whenever closing a file descriptor that was dirtied in the current process, send it over the pipe to the checkpointer. The checkpointer then can receive all those file descriptors (making sure it's not above the limit, fsync(), close() ing to make room if necessary). The biggest complication would presumably be to deduplicate the received filedescriptors for the same file, without loosing track of any errors.
Yep. That'd be a cheaper way to do it, though it wouldn't work on Windows. Though we don't know how Windows behaves here at all yet.
Prior discussion upthread had the checkpointer open()ing a file at the same time as a backend, before the backend writes to it. But passing the fd when the backend is done with it would be better.
How would that interlock with concurrent checkpoints?
I can see how to make that work if the share-fd-or-fsync-now logic happens in smgrwrite() when called by FlushBuffer() while you hold io_in_progress, but not if you defer it to some random time later.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-10 01:54:30
On 10 April 2018 at 04:25, Mark Dilger
wrote:
I was reading this thread up until now as meaning that the standby could receive corrupt WAL data and become corrupted.
Yes, it can, but not directly through the first error.
What can happen is that we think a block got written when it didn't.
If our in memory state diverges from our on disk state, we can make subsequent WAL writes based on that wrong information. But that's actually OK, since the standby will have replayed the original WAL correctly.
I think the only time we'd run into trouble is if we evict the good (but not written out) data from s_b and the fs buffer cache, then later read in the old version of a block we failed to overwrite. Data checksums (if enabled) might catch it unless the write left the whole block stale. In that case we might generate a full page write with the stale block and propagate that over WAL to the standby.
So I'd say standbys are relatively safe - very safe if the issue is caught promptly, and less so over time. But AFAICS WAL-based replication (physical or logical) is not a perfect defense for this.
However, remember, if your storage system is free of any sort of overprovisioning, is on a non-network file system, and doesn't use multipath (or sets it up right) this issue
is exceptionally unlikely to affect you
.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-10 01:59:03
On 10 April 2018 at 04:37, Andres Freund
wrote:
Hi,
On 2018-04-09 22:30:00 +0200, Tomas Vondra wrote:
Maybe. I'd certainly prefer automated recovery from an temporary I/O issues (like full disk on thin-provisioning) without the database crashing and restarting. But I'm not sure it's worth the effort.
Oh, I agree on that one. But that's more a question of how we force the kernel's hand on allocating disk space. In most cases the kernel allocates the disk space immediately, even if delayed allocation is in effect. For the cases where that's not the case (if there are current ones, rather than just past bugs), we should be able to make sure that's not an issue by pre-zeroing the data and/or using fallocate.
Nitpick: In most cases the kernel reserves disk space immediately, before returning from write(). NFS seems to be the main exception here.
EXT4 and XFS don't allocate until later, it by performing actual writes to FS metadata, initializing disk blocks, etc. So we won't notice errors that are only detectable at actual time of allocation, like thin provisioning problems, until after write() returns and we face the same writeback issues.
So I reckon you're safe from space-related issues if you're not on NFS (and whyyy would you do that?) and not thinly provisioned. I'm sure there are other corner cases, but I don't see any reason to expect space-exhaustion-related corruption problems on a sensible FS backed by a sensible block device. I haven't tested things like quotas, verified how reliable space reservation is under concurrency, etc as yet.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-10 02:00:59
On April 9, 2018 6:59:03 PM PDT, Craig Ringer
wrote:
On 10 April 2018 at 04:37, Andres Freund
wrote:
Hi,
On 2018-04-09 22:30:00 +0200, Tomas Vondra wrote:
Maybe. I'd certainly prefer automated recovery from an temporary I/O issues (like full disk on thin-provisioning) without the database crashing and restarting. But I'm not sure it's worth the effort.
Oh, I agree on that one. But that's more a question of how we force the kernel's hand on allocating disk space. In most cases the kernel allocates the disk space immediately, even if delayed allocation is in effect. For the cases where that's not the case (if there are current ones, rather than just past bugs), we should be able to make sure that's not an issue by pre-zeroing the data and/or using fallocate.
Nitpick: In most cases the kernel reserves disk space immediately, before returning from write(). NFS seems to be the main exception here.
EXT4 and XFS don't allocate until later, it by performing actual writes to FS metadata, initializing disk blocks, etc. So we won't notice errors that are only detectable at actual time of allocation, like thin provisioning problems, until after write() returns and we face the same writeback issues.
So I reckon you're safe from space-related issues if you're not on NFS (and whyyy would you do that?) and not thinly provisioned. I'm sure there are other corner cases, but I don't see any reason to expect space-exhaustion-related corruption problems on a sensible FS backed by a sensible block device. I haven't tested things like quotas, verified how reliable space reservation is under concurrency, etc as yet.
How's that not solved by pre zeroing and/or fallocate as I suggested above?
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-10 02:02:48
On 10 April 2018 at 08:41, Andreas Karlsson
wrote:
On 04/09/2018 02:16 PM, Craig Ringer wrote:
I'd like a middle ground where the kernel lets us register our interest and tells us if it lost something, without us having to keep eight million FDs open for some long period. "Tell us about anything that happens under pgdata/" or an inotify-style per-directory-registration option. I'd even say that's ideal.
Could there be a risk of a race condition here where fsync incorrectly returns success before we get the notification of that something went wrong?
We'd examine the notification queue only once all our checkpoint fsync()s had succeeded, and before we updated the control file to advance the redo position.
I'm intrigued by the suggestion upthread of using a kprobe or similar to achieve this. It's a horrifying unportable hack that'd make kernel people cry, and I don't know if we have any way to flush buffered probe data to be sure we really get the news in time, but it's a cool idea too.
From:Michael Paquier <michael(at)paquier(dot)xyz>
Date:2018-04-10 05:04:13
On Mon, Apr 09, 2018 at 03:02:11PM -0400, Robert Haas wrote:
Another consequence of this behavior that initdb -S is never reliable, so pg_rewind's use of it doesn't actually fix the problem it was intended to solve. It also means that initdb itself isn't crash-safe, since the data file changes are made by the backend but initdb itself is doing the fsyncs, and initdb has no way of knowing what files the backend is going to create and therefore can't -- even theoretically -- open them first.
And pg_basebackup. And pg_dump. And pg_dumpall. Anything using initdb -S or fsync_pgdata would enter in those waters.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-10 05:37:19
On 10 April 2018 at 13:04, Michael Paquier
wrote:
On Mon, Apr 09, 2018 at 03:02:11PM -0400, Robert Haas wrote:
Another consequence of this behavior that initdb -S is never reliable, so pg_rewind's use of it doesn't actually fix the problem it was intended to solve. It also means that initdb itself isn't crash-safe, since the data file changes are made by the backend but initdb itself is doing the fsyncs, and initdb has no way of knowing what files the backend is going to create and therefore can't -- even theoretically -- open them first.
And pg_basebackup. And pg_dump. And pg_dumpall. Anything using initdb -S or fsync_pgdata would enter in those waters.
... but
only if they hit an I/O error
or they're on a FS that doesn't reserve space and hit ENOSPC.
It still does 99% of the job. It still flushes all buffers to persistent storage and maintains write ordering. It may not detect and report failures to the user how we'd expect it to, yes, and that's not great. But it's hardly throw up our hands and give up territory either. Also, at least for initdb, we can make initdb fsync() its own files before close(). Annoying but hardly the end of the world.
From:Michael Paquier <michael(at)paquier(dot)xyz>
Date:2018-04-10 06:10:21
On Tue, Apr 10, 2018 at 01:37:19PM +0800, Craig Ringer wrote:
On 10 April 2018 at 13:04, Michael Paquier
wrote:
And pg_basebackup. And pg_dump. And pg_dumpall. Anything using initdb -S or fsync_pgdata would enter in those waters.
... but
only if they hit an I/O error
or they're on a FS that doesn't reserve space and hit ENOSPC.
Sure.
It still does 99% of the job. It still flushes all buffers to persistent storage and maintains write ordering. It may not detect and report failures to the user how we'd expect it to, yes, and that's not great. But it's hardly throw up our hands and give up territory either. Also, at least for initdb, we can make initdb fsync() its own files before close(). Annoying but hardly the end of the world.
Well, I think that there is place for improving reporting of failure in file_utils.c for frontends, or at worst have an exit() for any kind of critical failures equivalent to a PANIC.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-10 12:15:15
On 10 April 2018 at 14:10, Michael Paquier
wrote:
Well, I think that there is place for improving reporting of failure in file_utils.c for frontends, or at worst have an exit() for any kind of critical failures equivalent to a PANIC.
Yup.
In the mean time, speaking of PANIC, here's the first cut patch to make Pg panic on fsync() failures. I need to do some closer review and testing, but it's presented here for anyone interested.
I intentionally left some failures as ERROR not PANIC, where the entire operation is done as a unit, and an ERROR will cause us to retry the whole thing.
For example, when we fsync() a temp file before we move it into place, there's no point panicing on failure, because we'll discard the temp file on ERROR and retry the whole thing.
I've verified that it works as expected with some modifications to the test tool I've been using (pushed).
The main downside is that if we panic in redo, we don't try again. We throw our toys and shut down. But arguably if we get the same I/O error again in redo, that's the right thing to do anyway, and quite likely safer than continuing to ERROR on checkpoints indefinitely.
Patch attached.
To be clear, this patch only deals with the issue of us retrying fsyncs when it turns out to be unsafe. This does NOT address any of the issues where we won't find out about writeback errors at all.
AttachmentContent-TypeSize v1-0001-PANIC-when-we-detect-a-possible-fsync-I-O-error-i.patchtext/x-patch10.3 KB
From:Robert Haas <robertmhaas(at)gmail(dot)com>
Date:2018-04-10 15:15:46
On Mon, Apr 9, 2018 at 3:13 PM, Andres Freund
wrote:
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
Well, I admit that I wasn't entirely serious about that email, but I wasn't entirely not-serious either. If you can't find reliably find out whether the contents of the file on disk are the same as the contents that the kernel is giving you when you call read(), then you are going to have a heck of a time building a reliable system. If the kernel developers are determined to insist on these semantics (and, admittedly, I don't know whether that's the case - I've only read Anthony's remarks), then I don't really see what we can do except give up on buffered I/O (or on Linux).
We're talking about the storage layer returning an irresolvable error. You're hosed even if we report it properly. Yes, it'd be nice if we could report it reliably. But that doesn't change the fact that what we're doing is ensuring that data is safely fsynced unless storage fails, in which case it's not safely fsynced anyway.
I think that reliable error reporting is more than "nice" -- I think it's essential. The only argument for the current Linux behavior that has been so far advanced on this thread, at least as far as I can see, is that if it kept retrying the buffers forever, it would be pointless and might run the machine out of memory, so we might as well discard them. But previous comments have already illustrated that the kernel is not really up against a wall there -- it could put individual inodes into a permanent failure state when it discards their dirty data, as you suggested, or it could do what others have suggested, and what I think is better, which is to put the whole filesystem into a permanent failure state that can be cleared by remounting the FS. That could be done on an as-needed basis -- if the number of dirty buffers you're holding onto for some filesystem becomes too large, put the filesystem into infinite-fail mode and discard them all. That behavior would be pretty easy for administrators to understand and would resolve the entire problem here provided that no PostgreSQL processes survived the eventual remount.
I also don't really know what we mean by an "unresolvable" error. If the drive is beyond all hope, then it doesn't really make sense to talk about whether the database stored on it is corrupt. In general we can't be sure that we'll even get an error - e.g. the system could be idle and the drive could be on fire. Maybe this is the case you meant by "it'd be nice if we could report it reliably". But at least in my experience, that's typically not what's going on. You get some I/O errors and so you remount the filesystem, or reboot, or rebuild the array, or ... something. And then the errors go away and, at that point, you want to run recovery and continue using your database. In this scenario, it matters
quite a bit
what the error reporting was like during the period when failures were occurring. In particular, if the database was allowed to think that it had successfully checkpointed when it didn't, you're going to start recovery from the wrong place.
I'm going to shut up now because I'm telling you things that you obviously already know, but this doesn't sound like a "near irresolvable corner case". When the storage goes bonkers, either PostgreSQL and the kernel can interact in such a way that a checkpoint can succeed without all of the relevant data getting persisted, or they don't. It sounds like right now they do, and I'm not really clear that we have a reasonable idea how to fix that. It does not sound like a PANIC is sufficient.
From:Robert Haas <robertmhaas(at)gmail(dot)com>
Date:2018-04-10 15:28:07
On Tue, Apr 10, 2018 at 1:37 AM, Craig Ringer
wrote:
... but
only if they hit an I/O error
or they're on a FS that doesn't reserve space and hit ENOSPC.
It still does 99% of the job. It still flushes all buffers to persistent storage and maintains write ordering. It may not detect and report failures to the user how we'd expect it to, yes, and that's not great. But it's hardly throw up our hands and give up territory either. Also, at least for initdb, we can make initdb fsync() its own files before close(). Annoying but hardly the end of the world.
I think we'd need every child postgres process started by initdb to do that individually, which I suspect would slow down initdb quite a lot. Now admittedly for anybody other than a PostgreSQL developer that's only a minor issue, and our regression tests mostly run with fsync=off anyway. But I have a strong suspicion that our assumptions about how fsync() reports errors are baked into an awful lot of parts of the system, and by the time we get unbaking them I think it's going to be really surprising if we haven't done real harm to overall system performance.
BTW, I took a look at the MariaDB source code to see whether they've got this problem too and it sure looks like they do. os_file_fsync_posix() retries the fsync in a loop with an 0.2 second sleep after each retry. It warns after 100 failures and fails an assertion after 1000 failures. It is hard to understand why they would have written the code this way unless they expect errors reported by fsync() to continue being reported until the underlying condition is corrected. But, it looks like they wouldn't have the problem that we do with trying to reopen files to fsync() them later -- I spot checked a few places where this code is invoked and in all of those it looks like the file is already expected to be open.
From:Anthony Iliopoulos <ailiop(at)altatus(dot)com>
Date:2018-04-10 15:40:05
Hi Robert,
On Tue, Apr 10, 2018 at 11:15:46AM -0400, Robert Haas wrote:
On Mon, Apr 9, 2018 at 3:13 PM, Andres Freund
wrote:
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
Well, I admit that I wasn't entirely serious about that email, but I wasn't entirely not-serious either. If you can't find reliably find out whether the contents of the file on disk are the same as the contents that the kernel is giving you when you call read(), then you are going to have a heck of a time building a reliable system. If the kernel developers are determined to insist on these semantics (and, admittedly, I don't know whether that's the case - I've only read Anthony's remarks), then I don't really see what we can do except give up on buffered I/O (or on Linux).
I think it would be interesting to get in touch with some of the respective linux kernel maintainers and open up this topic for more detailed discussions. LSF/MM'18 is upcoming and it would have been the perfect opportunity but it's past the CFP deadline. It may still worth contacting the organizers to bring forward the issue, and see if there is a chance to have someone from Pg invited for further discussions.
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-10 16:38:27
On 9 April 2018 at 11:50, Anthony Iliopoulos
wrote:
On Mon, Apr 09, 2018 at 09:45:40AM +0100, Greg Stark wrote:
On 8 April 2018 at 22:47, Anthony Iliopoulos
wrote:
To make things a bit simpler, let us focus on EIO for the moment. The contract between the block layer and the filesystem layer is assumed to be that of, when an EIO is propagated up to the fs, then you may assume that all possibilities for recovering have been exhausted in lower layers of the stack.
Well Postgres is using the filesystem. The interface between the block layer and the filesystem may indeed need to be more complex, I wouldn't know.
But I don't think "all possibilities" is a very useful concept. Neither layer here is going to be perfect. They can only promise that all possibilities that have actually been implemented have been exhausted. And even among those only to the degree they can be done automatically within the engineering tradeoffs and constraints. There will always be cases like thin provisioned devices that an operator can expand, or degraded raid arrays that can be repaired after a long operation and so on. A network device can't be sure whether a remote server may eventually come back or not and have to be reconfigured by a human or system automation tool to point to the new server or new network configuration.
Right. This implies though that apart from the kernel having to keep around the dirtied-but-unrecoverable pages for an unbounded time, that there's further an interface for obtaining the exact failed pages so that you can read them back.
No, the interface we have is fsync which gives us that information with the granularity of a single file. The database could in theory recognize that fsync is not completing on a file and read that file back and write it to a new file. More likely we would implement a feature Oracle has of writing key files to multiple devices. But currently in practice that's not what would happen, what would happen would be a human would recognize that the database has stopped being able to commit and there are hardware errors in the log and would stop the database, take a backup, and restore onto a new working device. The current interface is that there's one error and then Postgres would pretty much have to say, "sorry, your database is corrupt and the data is gone, restore from your backups". Which is pretty dismal.
There is a clear responsibility of the application to keep its buffers around until a successful fsync(). The kernels do report the error (albeit with all the complexities of dealing with the interface), at which point the application may not assume that the write()s where ever even buffered in the kernel page cache in the first place.
Postgres cannot just store the entire database in RAM. It writes things to the filesystem all the time. It calls fsync only when it needs a write barrier to ensure consistency. That's only frequent on the transaction log to ensure it's flushed before data modifications and then periodically to checkpoint the data files. The amount of data written between checkpoints can be arbitrarily large and Postgres has no idea how much memory is available as filesystem buffers or how much i/o bandwidth is available or other memory pressure there is. What you're suggesting is that the application should have to babysit the filesystem buffer cache and reimplement all of it in user-space because the filesystem is free to throw away any data any time it chooses?
The current interface to throw away filesystem buffer cache is unmount. It sounds like the kernel would like a more granular way to discard just part of a device which makes a lot of sense in the age of large network block devices. But I don't think just saying that the filesystem buffer cache is now something every application needs to re-implement in user-space really helps with that, they're going to have the same problems to solve.
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-10 16:54:40
On 10 April 2018 at 02:59, Craig Ringer
wrote:
Nitpick: In most cases the kernel reserves disk space immediately, before returning from write(). NFS seems to be the main exception here.
I'm kind of puzzled by this. Surely NFS servers store the data in the filesystem using write(2) or the in-kernel equivalent? So if the server is backed by a filesystem where write(2) preallocates space surely the NFS server must behave as if it'spreallocating as well? I would expect NFS to provide basically the same set of possible failures as the underlying filesystem (as long as you don't enable nosync of course).
From:"Joshua D(dot) Drake" <jd(at)commandprompt(dot)com>
Date:2018-04-10 18:58:37
-hackers,
I reached out to the Linux ext4 devs, here is tytso(at)mit(dot)edu response:
""" Hi Joshua,
This isn't actually an ext4 issue, but a long-standing VFS/MM issue.
There are going to be multiple opinions about what the right thing to do. I'll try to give as unbiased a description as possible, but certainly some of this is going to be filtered by my own biases no matter how careful I can be.
First of all, what storage devices will do when they hit an exception condition is quite non-deterministic. For example, the vast majority of SSD's are not power fail certified. What this means is that if they suffer a power drop while they are doing a GC, it is quite possible for data written six months ago to be lost as a result. The LBA could potentialy be far, far away from any LBA's that were recently written, and there could have been multiple CACHE FLUSH operations in the since the LBA in question was last written six months ago. No matter; for a consumer-grade SSD, it's possible for that LBA to be trashed after an unexpected power drop.
Which is why after a while, one can get quite paranoid and assume that the only way you can guarantee data robustness is to store multiple copies and/or use erasure encoding, with some of the copies or shards written to geographically diverse data centers.
Secondly, I think it's fair to say that the vast majority of the companies who require data robustness, and are either willing to pay $$$ to an enterprise distro company like Red Hat, or command a large enough paying customer base that they can afford to dictate terms to an enterprise distro, or hire a consultant such as Christoph, or have their own staffed Linux kernel teams, have tended to use O_DIRECT. So for better or for worse, there has not been as much investment in buffered I/O and data robustness in the face of exception handling of storage devices.
Next, the reason why fsync() has the behaviour that it does is one ofhe the most common cases of I/O storage errors in buffered use cases, certainly as seen by the community distros, is the user who pulls out USB stick while it is in use. In that case, if there are dirtied pages in the page cache, the question is what can you do? Sooner or later the writes will time out, and if you leave the pages dirty, then it effectively becomes a permanent memory leak. You can't unmount the file system --- that requires writing out all of the pages such that the dirty bit is turned off. And if you don't clear the dirty bit on an I/O error, then they can never be cleaned. You can't even re-insert the USB stick; the re-inserted USB stick will get a new block device. Worse, when the USB stick was pulled, it will have suffered a power drop, and see above about what could happen after a power drop for non-power fail certified flash devices --- it goes double for the cheap sh*t USB sticks found in the checkout aisle of Micro Center.
So this is the explanation for why Linux handles I/O errors by clearing the dirty bit after reporting the error up to user space. And why there is not eagerness to solve the problem simply by "don't clear the dirty bit". For every one Postgres installation that might have a better recover after an I/O error, there's probably a thousand clueless Fedora and Ubuntu users who will have a much worse user experience after a USB stick pull happens.
I can think of things that could be done --- for example, it could be switchable on a per-block device basis (or maybe a per-mount basis) whether or not the dirty bit gets cleared after the error is reported to userspace. And perhaps there could be a new unmount flag that causes all dirty pages to be wiped out, which could be used to recover after a permanent loss of the block device. But the question is who is going to invest the time to make these changes? If there is a company who is willing to pay to comission this work, it's almost certainly soluble. Or if a company which has a kernel on staff is willing to direct an engineer to work on it, it certainly could be solved. But again, of the companies who have client code where we care about robustness and proper handling of failed disk drives, and which have a kernel team on staff, pretty much all of the ones I can think of (e.g., Oracle, Google, etc.) use O_DIRECT and they don't try to make buffered writes and error reporting via fsync(2) work well.
In general these companies want low-level control over buffer cache eviction algorithms, which drives them towards the design decision of effectively implementing the page cache in userspace, and using O_DIRECT reads/writes.
If you are aware of a company who is willing to pay to have a new kernel feature implemented to meet your needs, we might be able to refer you to a company or a consultant who might be able to do that work. Let me know off-line if that's the case...
- Ted
"""
From:"Joshua D(dot) Drake" <jd(at)commandprompt(dot)com>
Date:2018-04-10 19:51:01
-hackers,
The thread is picking up over on the ext4 list. They don't update their archives as often as we do, so I can't link to the discussion. What would be the preferred method of sharing the info?
Thanks,
From:"Joshua D(dot) Drake" <jd(at)commandprompt(dot)com>
Date:2018-04-10 20:57:34
On 04/10/2018 12:51 PM, Joshua D. Drake wrote:
-hackers,
The thread is picking up over on the ext4 list. They don't update their archives as often as we do, so I can't link to the discussion. What would be the preferred method of sharing the info?
Thanks to Anthony for this link:
http://lists.openwall.net/linux-ext4/2018/04/10/33
It isn't quite real time but it keeps things close enough.
From:Jonathan Corbet <corbet(at)lwn(dot)net>
Date:2018-04-11 12:05:27
On Tue, 10 Apr 2018 17:40:05 +0200 Anthony Iliopoulos
wrote:
LSF/MM'18 is upcoming and it would have been the perfect opportunity but it's past the CFP deadline. It may still worth contacting the organizers to bring forward the issue, and see if there is a chance to have someone from Pg invited for further discussions.
FWIW, it is my current intention to be sure that the development community is at least aware of the issue by the time LSFMM starts.
The event is April 23-25 in Park City, Utah. I bet that room could be found for somebody from the postgresql community, should there be somebody who would like to represent the group on this issue. Let me know if an introduction or advocacy from my direction would be helpful.
From:Greg Stark <stark(at)mit(dot)edu>
Date:2018-04-11 12:23:49
On 10 April 2018 at 19:58, Joshua D. Drake
wrote:
You can't unmount the file system --- that requires writing out all of the pages such that the dirty bit is turned off.
I always wondered why Linux didn't implement umount -f. It's been in BSD since forever and it's a major annoyance that it's missing in Linux. Even without leaking memory it still leaks other resources, causes confusion and awkward workarounds in UI and automation software.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-11 14:29:09
Hi,
On 2018-04-11 06:05:27 -0600, Jonathan Corbet wrote:
The event is April 23-25 in Park City, Utah. I bet that room could be found for somebody from the postgresql community, should there be somebody who would like to represent the group on this issue. Let me know if an introduction or advocacy from my direction would be helpful.
If that room can be found, I might be able to make it. Being in SF, I'm probably the physically closest PG dev involved in the discussion.
Thanks for chiming in,
From:Jonathan Corbet <corbet(at)lwn(dot)net>
Date:2018-04-11 14:40:31
On Wed, 11 Apr 2018 07:29:09 -0700 Andres Freund
wrote:
If that room can be found, I might be able to make it. Being in SF, I'm probably the physically closest PG dev involved in the discussion.
OK, I've dropped the PC a note; hopefully you'll be hearing from them.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-17 21:19:53
On Tue, Apr 10, 2018 at 05:54:40PM +0100, Greg Stark wrote:
On 10 April 2018 at 02:59, Craig Ringer
wrote:
Nitpick: In most cases the kernel reserves disk space immediately, before returning from write(). NFS seems to be the main exception here.
I'm kind of puzzled by this. Surely NFS servers store the data in the filesystem using write(2) or the in-kernel equivalent? So if the server is backed by a filesystem where write(2) preallocates space surely the NFS server must behave as if it'spreallocating as well? I would expect NFS to provide basically the same set of possible failures as the underlying filesystem (as long as you don't enable nosync of course).
I don't think the write is
sent
to the NFS at the time of the write, so while the NFS side would reserve the space, it might get the write request until after we return write success to the process.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-17 21:29:17
On Mon, Apr 9, 2018 at 03:42:35PM +0200, Tomas Vondra wrote:
On 04/09/2018 12:29 AM, Bruce Momjian wrote:
An crazy idea would be to have a daemon that checks the logs and stops Postgres when it seems something wrong.
That doesn't seem like a very practical way. It's better than nothing, of course, but I wonder how would that work with containers (where I think you may not have access to the kernel log at all). Also, I'm pretty sure the messages do change based on kernel version (and possibly filesystem) so parsing it reliably seems rather difficult. And we probably don't want to PANIC after I/O error on an unrelated device, so we'd need to understand which devices are related to PostgreSQL.
My more-considered crazy idea is to have a postgresql.conf setting like archive_command that allows the administrator to specify a command that will be run
after
fsync but before the checkpoint is marked as complete. While we can have write flush errors before fsync and never see the errors during fsync, we will not have write flush errors
after
fsync that are associated with previous writes.
The script should check for I/O or space-exhaustion errors and return false in that case, in which case we can stop and maybe stop and crash recover. We could have an exit of 1 do the former, and an exit of 2 do the later.
Also, if we are relying on WAL, we have to make sure WAL is actually safe with fsync, and I am betting only the O_DIRECT methods actually are safe:
#wal_sync_method = fsync                # the default is the first option
                                            # supported by the operating system:
                                            #   open_datasync
                                     -->    #   fdatasync (default on Linux)
                                     -->    #   fsync
                                     -->    #   fsync_writethrough
                                            #   open_sync
I am betting the marked wal_sync_method methods are not safe since there is time between the write and fsync.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-17 21:32:45
On Mon, Apr 9, 2018 at 03:42:35PM +0200, Tomas Vondra wrote:
On 04/09/2018 12:29 AM, Bruce Momjian wrote:
An crazy idea would be to have a daemon that checks the logs and stops Postgres when it seems something wrong.
That doesn't seem like a very practical way. It's better than nothing, of course, but I wonder how would that work with containers (where I think you may not have access to the kernel log at all). Also, I'm pretty sure the messages do change based on kernel version (and possibly filesystem) so parsing it reliably seems rather difficult. And we probably don't want to PANIC after I/O error on an unrelated device, so we'd need to understand which devices are related to PostgreSQL.
Replying to your specific case, I am not sure how we would use a script to check for I/O errors/space-exhaustion if the postgres user doesn't have access to it. Does O_DIRECT work in such container cases?
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-17 21:34:53
On 2018-04-17 17:29:17 -0400, Bruce Momjian wrote:
Also, if we are relying on WAL, we have to make sure WAL is actually safe with fsync, and I am betting only the O_DIRECT methods actually are safe:
> #wal_sync_method = fsync                # the default is the first option
    >                                         # supported by the operating system:
    >                                         #   open_datasync
    >                                  -->    #   fdatasync (default on Linux)
    >                                  -->    #   fsync
    >                                  -->    #   fsync_writethrough
    >                                         #   open_sync
I am betting the marked wal_sync_method methods are not safe since there is time between the write and fsync.
Hm? That's not really the issue though? One issue is that retries are not necessarily safe in buffered IO, the other that fsync might not report an error if the fd was closed and opened.
O_DIRECT is only used if wal archiving or streaming isn't used, which makes it pretty useless anyway.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-17 21:41:42
On 2018-04-17 17:32:45 -0400, Bruce Momjian wrote:
On Mon, Apr 9, 2018 at 03:42:35PM +0200, Tomas Vondra wrote:
That doesn't seem like a very practical way. It's better than nothing, of course, but I wonder how would that work with containers (where I think you may not have access to the kernel log at all). Also, I'm pretty sure the messages do change based on kernel version (and possibly filesystem) so parsing it reliably seems rather difficult. And we probably don't want to PANIC after I/O error on an unrelated device, so we'd need to understand which devices are related to PostgreSQL.
You can certainly have access to the kernel log in containers. I'd assume such a script wouldn't check various system logs but instead tail /dev/kmsg or such. Otherwise the variance between installations would be too big.
There's not
that
many different type of error messages and they don't change that often. If we'd just detect error for the most common FSs we'd probably be good. Detecting a few general storage layer message wouldn't be that hard either, most things have been unified over the last ~8-10 years.
Replying to your specific case, I am not sure how we would use a script to check for I/O errors/space-exhaustion if the postgres user doesn't have access to it.
Not sure what you mean?
Space exhaustiion can be checked when allocating space, FWIW. We'd just need to use posix_fallocate et al.
Does O_DIRECT work in such container cases?
Yes.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-17 21:49:42
On Mon, Apr 9, 2018 at 12:25:33PM -0700, Peter Geoghegan wrote:
On Mon, Apr 9, 2018 at 12:13 PM, Andres Freund
wrote:
Let's lower the pitchforks a bit here. Obviously a grand rewrite is absurd, as is some of the proposed ways this is all supposed to work. But I think the case we're discussing is much closer to a near irresolvable corner case than anything else.
+1
We're talking about the storage layer returning an irresolvable error. You're hosed even if we report it properly. Yes, it'd be nice if we could report it reliably. But that doesn't change the fact that what we're doing is ensuring that data is safely fsynced unless storage fails, in which case it's not safely fsynced anyway.
Right. We seem to be implicitly assuming that there is a big difference between a problem in the storage layer that we could in principle detect, but don't, and any other problem in the storage layer. I've read articles claiming that technologies like SMART are not really reliable in a practical sense [1], so it seems to me that there is reason to doubt that this gap is all that big.
That said, I suspect that the problems with running out of disk space are serious practical problems. I have personally scoffed at stories involving Postgres databases corruption that gets attributed to running out of disk space. Looks like I was dead wrong.
Yes, I think we need to look at user expectations here.
If the device has a hardware write error, it is true that it is good to detect it, and it might be permanent or temporary, e.g. NAS/NFS. The longer the error persists, the more likely the user will expect corruption. However, right now, any length outage could cause corruption, and it will not be reported in all cases.
Running out of disk space is also something you don't expect to corrupt your database --- you expect it to only prevent future writes. It seems NAS/NFS and any thin provisioned storage will have this problem, and again, not always reported.
So, our initial action might just be to educate users that write errors can cause silent corruption, and out-of-space errors on NAS/NFS and any thin provisioned storage can cause corruption.
Kernel logs (not just Postgres logs) should be monitored for these issues and fail-over/recovering might be necessary.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-18 09:52:22
On Tue, Apr 17, 2018 at 02:34:53PM -0700, Andres Freund wrote:
On 2018-04-17 17:29:17 -0400, Bruce Momjian wrote:
Also, if we are relying on WAL, we have to make sure WAL is actually safe with fsync, and I am betting only the O_DIRECT methods actually are safe:
> > #wal_sync_method = fsync                # the default is the first option
> >                                         # supported by the operating system:
> >                                         #   open_datasync
> >                                  -->    #   fdatasync (default on Linux)
> >                                  -->    #   fsync
> >                                  -->    #   fsync_writethrough
> >                                         #   open_sync
I am betting the marked wal_sync_method methods are not safe since there is time between the write and fsync.
Hm? That's not really the issue though? One issue is that retries are not necessarily safe in buffered IO, the other that fsync might not report an error if the fd was closed and opened.
Well, we have have been focusing on the delay between backend or checkpoint writes and checkpoint fsyncs. My point is that we have the same problem in doing a write,
then
fsync for the WAL. Yes, the delay is much shorter, but the issue still exists. I realize that newer Linux kernels will not have the problem since the file descriptor remains open, but the problem exists with older/common linux kernels.
O_DIRECT is only used if wal archiving or streaming isn't used, which makes it pretty useless anyway.
Uh, as doesn't 'open_datasync' and 'open_sync' fsync as part of the write, meaning we can't lose the error report like we can with the others?
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-18 10:04:30
On 18 April 2018 at 05:19, Bruce Momjian
wrote:
On Tue, Apr 10, 2018 at 05:54:40PM +0100, Greg Stark wrote:
On 10 April 2018 at 02:59, Craig Ringer
wrote:
Nitpick: In most cases the kernel reserves disk space immediately, before returning from write(). NFS seems to be the main exception here.
I'm kind of puzzled by this. Surely NFS servers store the data in the filesystem using write(2) or the in-kernel equivalent? So if the server is backed by a filesystem where write(2) preallocates space surely the NFS server must behave as if it'spreallocating as well? I would expect NFS to provide basically the same set of possible failures as the underlying filesystem (as long as you don't enable nosync of course).
I don't think the write is
sent
to the NFS at the time of the write, so while the NFS side would reserve the space, it might get the write request until after we return write success to the process.
It should be sent if you're using sync mode.
From my reading of the docs, if you're using async mode you're already open to so many potential corruptions you might as well not bother.
I need to look into this more re NFS and expand the tests I have to cover that properly.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-18 10:19:28
On 10 April 2018 at 20:15, Craig Ringer
wrote:
On 10 April 2018 at 14:10, Michael Paquier
wrote:
Well, I think that there is place for improving reporting of failure in file_utils.c for frontends, or at worst have an exit() for any kind of critical failures equivalent to a PANIC.
Yup.
In the mean time, speaking of PANIC, here's the first cut patch to make Pg panic on fsync() failures. I need to do some closer review and testing, but it's presented here for anyone interested.
I intentionally left some failures as ERROR not PANIC, where the entire operation is done as a unit, and an ERROR will cause us to retry the whole thing.
For example, when we fsync() a temp file before we move it into place, there's no point panicing on failure, because we'll discard the temp file on ERROR and retry the whole thing.
I've verified that it works as expected with some modifications to the test tool I've been using (pushed).
The main downside is that if we panic in redo, we don't try again. We throw our toys and shut down. But arguably if we get the same I/O error again in redo, that's the right thing to do anyway, and quite likely safer than continuing to ERROR on checkpoints indefinitely.
Patch attached.
To be clear, this patch only deals with the issue of us retrying fsyncs when it turns out to be unsafe. This does NOT address any of the issues where we won't find out about writeback errors at all.
Thinking about this some more, it'll definitely need a GUC to force it to continue despite a potential hazard. Otherwise we go backwards from the status quo if we're in a position where uptime is vital and correctness problems can be tolerated or repaired later. Kind of like zero_damaged_pages, we'll need some sort of continue_after_fsync_errors .
Without that, we'll panic once, enter redo, and if the problem persists we'll panic in redo and exit the startup process. That's not going to help users.
I'll amend the patch accordingly as time permits.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-18 11:46:15
On Wed, Apr 18, 2018 at 06:04:30PM +0800, Craig Ringer wrote:
On 18 April 2018 at 05:19, Bruce Momjian
wrote:
On Tue, Apr 10, 2018 at 05:54:40PM +0100, Greg Stark wrote:
On 10 April 2018 at 02:59, Craig Ringer
wrote:
Nitpick: In most cases the kernel reserves disk space immediately, before returning from write(). NFS seems to be the main exception here.
I'm kind of puzzled by this. Surely NFS servers store the data in the filesystem using write(2) or the in-kernel equivalent? So if the server is backed by a filesystem where write(2) preallocates space surely the NFS server must behave as if it'spreallocating as well? I would expect NFS to provide basically the same set of possible failures as the underlying filesystem (as long as you don't enable nosync of course).
I don't think the write is
sent
to the NFS at the time of the write, so while the NFS side would reserve the space, it might get the write request until after we return write success to the process.
It should be sent if you're using sync mode.
From my reading of the docs, if you're using async mode you're already open to so many potential corruptions you might as well not bother.
I need to look into this more re NFS and expand the tests I have to cover that properly.
So, if sync mode passes the write to NFS, and NFS pre-reserves write space, and throws an error on reservation failure, that means that NFS will not corrupt a cluster on out-of-space errors.
So, what about thin provisioning? I can understand sharing
free
space among file systems, but once a write arrives I assume it reserves the space. Is the problem that many thin provisioning systems don't have a sync mode, so you can't force the write to appear on the device before an fsync?
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-18 11:56:57
On Tue, Apr 17, 2018 at 02:41:42PM -0700, Andres Freund wrote:
On 2018-04-17 17:32:45 -0400, Bruce Momjian wrote:
On Mon, Apr 9, 2018 at 03:42:35PM +0200, Tomas Vondra wrote:
That doesn't seem like a very practical way. It's better than nothing, of course, but I wonder how would that work with containers (where I think you may not have access to the kernel log at all). Also, I'm pretty sure the messages do change based on kernel version (and possibly filesystem) so parsing it reliably seems rather difficult. And we probably don't want to PANIC after I/O error on an unrelated device, so we'd need to understand which devices are related to PostgreSQL.
You can certainly have access to the kernel log in containers. I'd assume such a script wouldn't check various system logs but instead tail /dev/kmsg or such. Otherwise the variance between installations would be too big.
I was thinking 'dmesg', but the result is similar.
There's not
that
many different type of error messages and they don't change that often. If we'd just detect error for the most common FSs we'd probably be good. Detecting a few general storage layer message wouldn't be that hard either, most things have been unified over the last ~8-10 years.
It is hard to know exactly what the message format should be for each operating system because it is hard to generate them on demand, and we would need to filter based on Postgres devices.
The other issue is that once you see a message during a checkpoint and exit, you don't want to see that message again after the problem has been fixed and the server restarted. The simplest solution is to save the output of the last check and look for only new entries. I am attaching a script I run every 15 minutes from cron that emails me any unexpected kernel messages.
I am thinking we would need a contrib module with sample scripts for various operating systems.
Replying to your specific case, I am not sure how we would use a script to check for I/O errors/space-exhaustion if the postgres user doesn't have access to it.
Not sure what you mean?
Space exhaustiion can be checked when allocating space, FWIW. We'd just need to use posix_fallocate et al.
I was asking about cases where permissions prevent viewing of kernel messages. I think you can view them in containers, but in virtual machines you might not have access to the host operating system's kernel messages, and that might be where they are.
AttachmentContent-TypeSize
    dmesg_checktext/plain574 bytes
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-18 12:45:53
wrOn 18 April 2018 at 19:46, Bruce Momjian
wrote:
So, if sync mode passes the write to NFS, and NFS pre-reserves write space, and throws an error on reservation failure, that means that NFS will not corrupt a cluster on out-of-space errors.
Yeah. I need to verify in a concrete test case.
The thing is that write() is allowed to be asynchronous anyway. Most file systems choose to implement eager reservation of space, but it's not mandated. AFAICS that's largely a historical accident to keep applications happy, because FSes used to
allocate
the space at write() time too, and when they moved to delayed allocations, apps tended to break too easily unless they at least reserved space. NFS would have to do a round-trip on write() to reserve space.
The Linux man pages (
http://man7.org/linux/man-pages/man2/write.2.html
) say:
A successful return from write() does not make any guarantee that data has been committed to disk. On some filesystems, including NFS, it does not even guarantee that space has successfully been reserved for the data. In this case, some errors might be delayed until a future write(2), fsync(2), or even close(2). The only way to be sure is to call fsync(2) after you are done writing all your data.
... and I'm inclined to believe it when it refuses to make guarantees. Especially lately.
So, what about thin provisioning? I can understand sharing
free
space among file systems
Most thin provisioning is done at the block level, not file system level. So the FS is usually unaware it's on a thin-provisioned volume. Usually the whole kernel is unaware, because the thin provisioning is done on the SAN end or by a hypervisor. But the same sort of thing may be done via LVM - see lvmthin. For example, you may make 100 different 1TB ext4 FSes, each on 1TB iSCSI volumes backed by SAN with a total of 50TB of concrete physical capacity. The SAN is doing block mapping and only allocating storage chunks to a given volume when the FS has written blocks to every previous free block in the previous storage chunk. It may also do things like block de-duplication, compression of storage chunks that aren't written to for a while, etc.
The idea is that when the SAN's actual physically allocate storage gets to 40TB it starts telling you to go buy another rack of storage so you don't run out. You don't have to resize volumes, resize file systems, etc. All the storage space admin is centralized on the SAN and storage team, and your sysadmins, DBAs and app devs are none the wiser. You buy storage when you need it, not when the DBA demands they need a 200% free space margin just in case. Whether or not you agree with this philosophy or think it's sensible is kind of moot, because it's an extremely widespread model, and servers you work on may well be backed by thin provisioned storage
even if you don't know it
.
Think of it as a bit like VM overcommit, for storage. You can malloc() as much memory as you like and everything's fine until you try to actually use it. Then you go to dirty a page, no free pages are available, and
boom
.
The thing is, the SAN (or LVM) doesn't have any idea about the FS's internal in-memory free space counter and its space reservations. Nor does it understand any FS metadata. All it cares about is "has this LBA ever been written to by the FS?". If so, it must make sure backing storage for it exists. If not, it won't bother.
Most FSes only touch the blocks on dirty writeback, or sometimes lazily as part of delayed allocation. So if your SAN is running out of space and there's 100MB free, each of your 100 FSes may have decremented its freelist by 2MB and be happily promising more space to apps on write() because, well, as far as they know they're only 50% full. When they all do dirty writeback and flush to storage, kaboom, there's nowhere to put some of the data.
I don't know if posix_fallocate is a sufficient safeguard either. You'd have to actually force writes to each page through to the backing storage to know for sure the space existed. Yes, the docs say
After a successful call to posix_fallocate(), subsequent writes to bytes in the specified range are guaranteed not to fail because of lack of disk space.
... but they're speaking from the filesystem's perspective. If the FS doesn't dirty and flush the actual blocks, a thin provisioned storage system won't know.
It's reasonable enough to throw up our hands in this case and say "your setup is crazy, you're breaking the rules, don't do that". The truth is they AREN'T breaking the rules, but we can disclaim support for such configurations anyway.
After all, we tell people not to use Linux's VM overcommit too. How's that working for you? I see it enabled on the great majority of systems I work with, and some people are very reluctant to turn it off because they don't want to have to add swap.
If someone has a 50TB SAN and wants to allow for unpredictable space use expansion between various volumes, and we say "you can't do that, go buy a 100TB SAN instead" ... that's not going to go down too well either. Often we can actually say "make sure the 5TB volume PostgreSQL is using is eagerly provisioned, and expand it at need using online resize if required. We don't care about the rest of the SAN.".
I guarantee you that when you create a 100GB EBS volume on AWS EC2, you don't get 100GB of storage preallocated. AWS are probably pretty good about not running out of backing store, though.
There
are
file systems optimised for thin provisioning, etc, too. But that's more commonly done by having them do things like zero deallocated space so the thin provisioning system knows it can return it to the free pool, and now things like DISCARD provide much of that signalling in a standard way.
From:Mark Kirkwood <mark(dot)kirkwood(at)catalyst(dot)net(dot)nz>
Date:2018-04-18 23:31:50
On 19/04/18 00:45, Craig Ringer wrote:
I guarantee you that when you create a 100GB EBS volume on AWS EC2, you don't get 100GB of storage preallocated. AWS are probably pretty good about not running out of backing store, though.
Some db folks (used to anyway) advise dd'ing to your freshly attached devices on AWS (for performance mainly IIRC), but that would help prevent some failure scenarios for any thin provisioned storage (but probably really annoy the admins' thereof).
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-19 00:44:33
On 19 April 2018 at 07:31, Mark Kirkwood
wrote:
On 19/04/18 00:45, Craig Ringer wrote:
I guarantee you that when you create a 100GB EBS volume on AWS EC2, you don't get 100GB of storage preallocated. AWS are probably pretty good about not running out of backing store, though.
Some db folks (used to anyway) advise dd'ing to your freshly attached devices on AWS (for performance mainly IIRC), but that would help prevent some failure scenarios for any thin provisioned storage (but probably really annoy the admins' thereof).
This still makes a lot of sense on AWS EBS, particularly when using a volume created from a non-empty snapshot. Performance of S3-snapshot based EBS volumes is spectacularly awful, since they're copy-on-read. Reading the whole volume helps a lot.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-20 20:49:08
On Wed, Apr 18, 2018 at 08:45:53PM +0800, Craig Ringer wrote:
wrOn 18 April 2018 at 19:46, Bruce Momjian
wrote:
So, if sync mode passes the write to NFS, and NFS pre-reserves write space, and throws an error on reservation failure, that means that NFS will not corrupt a cluster on out-of-space errors.
Yeah. I need to verify in a concrete test case.
Thanks.
The thing is that write() is allowed to be asynchronous anyway. Most file systems choose to implement eager reservation of space, but it's not mandated. AFAICS that's largely a historical accident to keep applications happy, because FSes used to
allocate
the space at write() time too, and when they moved to delayed allocations, apps tended to break too easily unless they at least reserved space. NFS would have to do a round-trip on write() to reserve space.
The Linux man pages (
http://man7.org/linux/man-pages/man2/write.2.html
) say:
" A successful return from write() does not make any guarantee that data has been committed to disk. On some filesystems, including NFS, it does not even guarantee that space has successfully been reserved for the data. In this case, some errors might be delayed until a future write(2), fsync(2), or even close(2). The only way to be sure is to call fsync(2) after you are done writing all your data. "
... and I'm inclined to believe it when it refuses to make guarantees. Especially lately.
Uh, even calling fsync after write isn't 100% safe since the kernel could have flushed the dirty pages to storage, and failed, and the fsync would later succeed. I realize newer kernels have that fixed for files open during that operation, but that is the minority of installs.
The idea is that when the SAN's actual physically allocate storage gets to 40TB it starts telling you to go buy another rack of storage so you don't run out. You don't have to resize volumes, resize file systems, etc. All the storage space admin is centralized on the SAN and storage team, and your sysadmins, DBAs and app devs are none the wiser. You buy storage when you need it, not when the DBA demands they need a 200% free space margin just in case. Whether or not you agree with this philosophy or think it's sensible is kind of moot, because it's an extremely widespread model, and servers you work on may well be backed by thin provisioned storage
even if you don't know it
.
Most FSes only touch the blocks on dirty writeback, or sometimes lazily as part of delayed allocation. So if your SAN is running out of space and there's 100MB free, each of your 100 FSes may have decremented its freelist by 2MB and be happily promising more space to apps on write() because, well, as far as they know they're only 50% full. When they all do dirty writeback and flush to storage, kaboom, there's nowhere to put some of the data.
I see what you are saying --- that the kernel is reserving the write space from its free space, but the free space doesn't all exist. I am not sure how we can tell people to make sure the file system free space is real.
You'd have to actually force writes to each page through to the backing storage to know for sure the space existed. Yes, the docs say
" After a successful call to posix_fallocate(), subsequent writes to bytes in the specified range are guaranteed not to fail because of lack of disk space. "
... but they're speaking from the filesystem's perspective. If the FS doesn't dirty and flush the actual blocks, a thin provisioned storage system won't know.
Frankly, in what cases will a write fail
for
lack of free space? It could be a new WAL file (not recycled), or a pages added to the end of the table.
Is that it? It doesn't sound too terrible. If we can eliminate the corruption due to free space exxhaustion, it would be a big step forward.
The next most common failure would be temporary storage failure or storage communication failure.
Permanent storage failure is "game over" so we don't need to worry about that.
From:Gasper Zejn <zejn(at)owca(dot)info>
Date:2018-04-21 19:21:39
Just for the record, I tried the test case with ZFS on Ubuntu 17.10 host with ZFS on Linux 0.6.5.11.
ZFS does not swallow the fsync error, but the system does not handle the error nicely: the test case program hangs on fsync, the load jumps up and there's a bunch of z_wr_iss and z_null_int kernel threads belonging to zfs, eating up the CPU.
Even then I managed to reboot the system, so it's not a complete and utter mess.
The test case adjustments are here:
https://github.com/zejn/scrapcode/commit/e7612536c346d59a4b69bedfbcafbe8c1079063c
Kind regards,
On 29. 03. 2018 07:25, Craig Ringer wrote:
On 29 March 2018 at 13:06, Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com
On Thu, Mar 29, 2018 at 6:00 PM, Justin Pryzby
> The retries are the source of the problem ; the first fsync() can return EIO,
> and also *clears the error* causing a 2nd fsync (of the same data) to return
> success.

> What I'm failing to grok here is how that error flag even matters,
> whether it's a single bit or a counter as described in that patch.  If
> write back failed, *the page is still dirty*.  So all future calls to
> fsync() need to try to try to flush it again, and (presumably) fail
> again (unless it happens to succeed this time around).
You'd think so. But it doesn't appear to work that way. You can see yourself with the error device-mapper destination mapped over part of a volume.
I wrote a test case here.
https://github.com/ringerc/scrapcode/blob/master/testcases/fsync-error-clear.c
I don't pretend the kernel behaviour is sane. And it's possible I've made an error in my analysis. But since I've observed this in the wild, and seen it in a test case, I strongly suspect that's what I've described is just what's happening, brain-dead or no.
Presumably the kernel marks the page clean when it dispatches it to the I/O subsystem and doesn't dirty it again on I/O error? I haven't dug that deep on the kernel side. See the stackoverflow post for details on what I found in kernel code analysis.
From:Andres Freund <andres(at)anarazel(dot)de>
Date:2018-04-23 20:14:48
Hi,
On 2018-03-28 10:23:46 +0800, Craig Ringer wrote:
TL;DR: Pg should PANIC on fsync() EIO return. Retrying fsync() is not OK at least on Linux. When fsync() returns success it means "all writes since the last fsync have hit disk" but we assume it means "all writes since the last SUCCESSFUL fsync have hit disk".
But then we retried the checkpoint, which retried the fsync(). The retry succeeded, because the prior fsync()
cleared the AS_EIO bad page flag
.
Random other thing we should look at: Some filesystems (nfs yes, xfs ext4 no) flush writes at close(2). We check close() return code, just log it... So close() counts as an fsync for such filesystems().
I'm LSF/MM to discuss future behaviour of linux here, but that's how it is right now.
From:Bruce Momjian <bruce(at)momjian(dot)us>
Date:2018-04-24 00:09:23
On Mon, Apr 23, 2018 at 01:14:48PM -0700, Andres Freund wrote:
Hi,
On 2018-03-28 10:23:46 +0800, Craig Ringer wrote:
TL;DR: Pg should PANIC on fsync() EIO return. Retrying fsync() is not OK at least on Linux. When fsync() returns success it means "all writes since the last fsync have hit disk" but we assume it means "all writes since the last SUCCESSFUL fsync have hit disk".
But then we retried the checkpoint, which retried the fsync(). The retry succeeded, because the prior fsync()
cleared the AS_EIO bad page flag
.
Random other thing we should look at: Some filesystems (nfs yes, xfs ext4 no) flush writes at close(2). We check close() return code, just log it... So close() counts as an fsync for such filesystems().
Well, that's interesting. You might remember that NFS does not reserve space for writes like local file systems like ext4/xfs do. For that reason, we might be able to capture the out-of-space error on close and exit sooner for NFS.
From:Craig Ringer <craig(at)2ndquadrant(dot)com>
Date:2018-04-26 02:16:52
On 24 April 2018 at 04:14, Andres Freund
wrote:
I'm LSF/MM to discuss future behaviour of linux here, but that's how it is right now.
Interim LWN.net coverage of that can be found here:
https://lwn.net/Articles/752613/
From:Thomas Munro <thomas(dot)munro(at)enterprisedb(dot)com>
Date:2018-04-27 01:18:55
On Tue, Apr 24, 2018 at 12:09 PM, Bruce Momjian
wrote:
On Mon, Apr 23, 2018 at 01:14:48PM -0700, Andres Freund wrote:
Hi,
On 2018-03-28 10:23:46 +0800, Craig Ringer wrote:
TL;DR: Pg should PANIC on fsync() EIO return. Retrying fsync() is not OK at least on Linux. When fsync() returns success it means "all writes since the last fsync have hit disk" but we assume it means "all writes since the last SUCCESSFUL fsync have hit disk".
But then we retried the checkpoint, which retried the fsync(). The retry succeeded, because the prior fsync()
cleared the AS_EIO bad page flag
.
Random other thing we should look at: Some filesystems (nfs yes, xfs ext4 no) flush writes at close(2). We check close() return code, just log it... So close() counts as an fsync for such filesystems().
Well, that's interesting. You might remember that NFS does not reserve space for writes like local file systems like ext4/xfs do. For that reason, we might be able to capture the out-of-space error on close and exit sooner for NFS.
It seems like some implementations flush on close and therefore discover ENOSPC problem at that point, unless they have NVSv4 (RFC 3050) "write delegation" with a promise from the server that a certain amount of space is available. It seems like you can't count on that in any way though, because it's the server that decides when to delegate and how much space to promise is preallocated, not the client. So in userspace you always need to be able to handle errors including ENOSPC returned by close(), and if you ignore that and you're using an operating system that immediately incinerates all evidence after telling you that (so that later fsync() doesn't fail), you're in trouble.
Some relevant code:
It looks like the bleeding edge of the NFS spec includes a new ALLOCATE operation that should be able to support posix_fallocate() (if we were to start using that for extending files):
https://tools.ietf.org/html/rfc7862#page-64
I'm not sure how reliable [posix_]fallocate is on NFS in general though, and it seems that there are fall-back implementations of posix_fallocate() that write zeros (or even just feign success?) which probably won't do anything useful here if not also flushed (that fallback strategy might only work on eager reservation filesystems that don't have direct fallocate support?) so there are several layers (libc, kernel, nfs client, nfs server) that'd need to be aligned for that to work, and it's not clear how a humble userspace program is supposed to know if they are.
I guess if you could find a way to amortise the cost of extending (like Oracle et al do by extending big container datafiles 10MB at a time or whatever), then simply writing zeros and flushing when doing that might work out OK, so you wouldn't need such a thing? (Unless of course it's a COW filesystem, but that's a different can of worms.)
This thread continues on the
ext4
mailing list:
From:   "Joshua D. Drake" <jd@...mandprompt.com>
Subject: fsync() errors is unsafe and risks data loss
Date:   Tue, 10 Apr 2018 09:28:15 -0700
-ext4,
If this is not the appropriate list please point me in the right direction. I am a PostgreSQL contributor and we have come across a reliability problem with writes and fsync(). You can see the thread here:
https://www.postgresql.org/message-id/flat/20180401002038.GA2211%40paquier.xyz#20180401002038.GA2211@paquier.xyz
The tl;dr; in the first message doesn't quite describe the problem as we started to dig into it further.
From:   "Darrick J. Wong" <darrick.wong@...cle.com>
Date:   Tue, 10 Apr 2018 09:54:43 -0700
On Tue, Apr 10, 2018 at 09:28:15AM -0700, Joshua D. Drake wrote:
-ext4,
If this is not the appropriate list please point me in the right direction. I am a PostgreSQL contributor and we have come across a reliability problem with writes and fsync(). You can see the thread here:
https://www.postgresql.org/message-id/flat/20180401002038.GA2211%40paquier.xyz#20180401002038.GA2211@paquier.xyz
The tl;dr; in the first message doesn't quite describe the problem as we started to dig into it further.
You might try the XFS list (linux-xfs@...r.kernel.org) seeing as the initial complaint is against xfs behaviors...
From:   "Joshua D. Drake" <jd@...mandprompt.com>
Date:   Tue, 10 Apr 2018 09:58:21 -0700
On 04/10/2018 09:54 AM, Darrick J. Wong wrote:
On Tue, Apr 10, 2018 at 09:28:15AM -0700, Joshua D. Drake wrote:
-ext4,
If this is not the appropriate list please point me in the right direction. I am a PostgreSQL contributor and we have come across a reliability problem with writes and fsync(). You can see the thread here:
https://www.postgresql.org/message-id/flat/20180401002038.GA2211%40paquier.xyz#20180401002038.GA2211@paquier.xyz
The tl;dr; in the first message doesn't quite describe the problem as we started to dig into it further.
You might try the XFS list (linux-xfs@...r.kernel.org) seeing as the initial complaint is against xfs behaviors...
Later in the thread it becomes apparent that it applies to ext4 (NFS too) as well. I picked ext4 because I assumed it is the most populated of the lists since its the default filesystem for most distributions.
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Tue, 10 Apr 2018 14:43:56 -0400
Hi Joshua,
This isn't actually an ext4 issue, but a long-standing VFS/MM issue.
There are going to be multiple opinions about what the right thing to do. I'll try to give as unbiased a description as possible, but certainly some of this is going to be filtered by my own biases no matter how careful I can be.
First of all, what storage devices will do when they hit an exception condition is quite non-deterministic. For example, the vast majority of SSD's are not power fail certified. What this means is that if they suffer a power drop while they are doing a GC, it is quite possible for data written six months ago to be lost as a result. The LBA could potentialy be far, far away from any LBA's that were recently written, and there could have been multiple CACHE FLUSH operations in the since the LBA in question was last written six months ago. No matter; for a consumer-grade SSD, it's possible for that LBA to be trashed after an unexpected power drop.
Which is why after a while, one can get quite paranoid and assume that the only way you can guarantee data robustness is to store multiple copies and/or use erasure encoding, with some of the copies or shards written to geographically diverse data centers.
Secondly, I think it's fair to say that the vast majority of the companies who require data robustness, and are either willing to pay $$$ to an enterprise distro company like Red Hat, or command a large enough paying customer base that they can afford to dictate terms to an enterprise distro, or hire a consultant such as Christoph, or have their own staffed Linux kernel teams, have tended to use O_DIRECT. So for better or for worse, there has not been as much investment in buffered I/O and data robustness in the face of exception handling of storage devices.
Next, the reason why fsync() has the behaviour that it does is one ofhe the most common cases of I/O storage errors in buffered use cases, certainly as seen by the community distros, is the user who pulls out USB stick while it is in use. In that case, if there are dirtied pages in the page cache, the question is what can you do? Sooner or later the writes will time out, and if you leave the pages dirty, then it effectively becomes a permanent memory leak. You can't unmount the file system --- that requires writing out all of the pages such that the dirty bit is turned off. And if you don't clear the dirty bit on an I/O error, then they can never be cleaned. You can't even re-insert the USB stick; the re-inserted USB stick will get a new block device. Worse, when the USB stick was pulled, it will have suffered a power drop, and see above about what could happen after a power drop for non-power fail certified flash devices --- it goes double for the cheap sh*t USB sticks found in the checkout aisle of Micro Center.
So this is the explanation for why Linux handles I/O errors by clearing the dirty bit after reporting the error up to user space. And why there is not eagerness to solve the problem simply by "don't clear the dirty bit". For every one Postgres installation that might have a better recover after an I/O error, there's probably a thousand clueless Fedora and Ubuntu users who will have a much worse user experience after a USB stick pull happens.
I can think of things that could be done --- for example, it could be switchable on a per-block device basis (or maybe a per-mount basis) whether or not the dirty bit gets cleared after the error is reported to userspace. And perhaps there could be a new unmount flag that causes all dirty pages to be wiped out, which could be used to recover after a permanent loss of the block device. But the question is who is going to invest the time to make these changes? If there is a company who is willing to pay to comission this work, it's almost certainly soluble. Or if a company which has a kernel on staff is willing to direct an engineer to work on it, it certainly could be solved. But again, of the companies who have client code where we care about robustness and proper handling of failed disk drives, and which have a kernel team on staff, pretty much all of the ones I can think of (e.g., Oracle, Google, etc.) use O_DIRECT and they don't try to make buffered writes and error reporting via fsync(2) work well.
In general these companies want low-level control over buffer cache eviction algorithms, which drives them towards the design decision of effectively implementing the page cache in userspace, and using O_DIRECT reads/writes.
If you are aware of a company who is willing to pay to have a new kernel feature implemented to meet your needs, we might be able to refer you to a company or a consultant who might be able to do that work. Let me know off-line if that's the case...
From:   Andreas Dilger <adilger@...ger.ca>
Date:   Tue, 10 Apr 2018 13:44:48 -0600
On Apr 10, 2018, at 10:50 AM, Joshua D. Drake
jd@...mandprompt.com
wrote:
-ext4,
If this is not the appropriate list please point me in the right direction. I am a PostgreSQL contributor and we have come across a reliability problem with writes and fsync(). You can see the thread here:
https://www.postgresql.org/message-id/flat/20180401002038.GA2211%40paquier.xyz#20180401002038.GA2211@paquier.xyz
The tl;dr; in the first message doesn't quite describe the problem as we started to dig into it further.
Yes, this is a very long thread. The summary is Postgres is unhappy that fsync() on Linux (and also other OSes) returns an error once if there was a prior write() failure, instead of keeping dirty pages in memory forever and trying to rewrite them.
This behaviour has existed on Linux forever, and (for better or worse) is the only reasonable behaviour that the kernel can take. I've argued for the opposite behaviour at times, and some subsystems already do limited retries before finally giving up on a failed write, though there are also times when retrying at lower levels is pointless if a higher level of code can handle the failure (e.g. mirrored block devices, filesystem data mirroring, userspace data mirroring, or cross-node replication).
The confusion is whether fsync() is a "level" state (return error forever if there were pages that could not be written), or an "edge" state (return error only for any write failures since the previous fsync() call).
I think Anthony Iliopoulos was pretty clear in his multiple descriptions in that thread of why the current behaviour is needed (OOM of the whole system if dirty pages are kept around forever), but many others were stuck on "I can't believe this is happening??? This is totally unacceptable and every kernel needs to change to match my expectations!!!" without looking at the larger picture of what is practical to change and where the issue should best be fixed.
Regardless of why this is the case, the net is that PG needs to deal with all of the systems that currently exist that have this behaviour, even if some day in the future it may change (though that is unlikely). It seems ironic that "keep dirty pages in userspace until fsync() returns success" is totally unacceptable, but "keep dirty pages in the kernel" is fine. My (limited) understanding of databases was that they preferred to cache everything in userspace and use O_DIRECT to write to disk (which returns an error immediately if the write fails and does not double buffer data).
From: Martin Steigerwald
martin@...htvoll.de
Date: Tue, 10 Apr 2018 21:47:21 +0200
Hi Theodore, Darrick, Joshua.
CC´d fsdevel as it does not appear to be Ext4 specific to me (and to you as well, Theodore).
Theodore Y. Ts'o - 10.04.18, 20:43:
This isn't actually an ext4 issue, but a long-standing VFS/MM issue. […] First of all, what storage devices will do when they hit an exception condition is quite non-deterministic. For example, the vast majority of SSD's are not power fail certified. What this means is that if they suffer a power drop while they are doing a GC, it is quite possible for data written six months ago to be lost as a result. The LBA could potentialy be far, far away from any LBA's that were recently written, and there could have been multiple CACHE FLUSH operations in the since the LBA in question was last written six months ago. No matter; for a consumer-grade SSD, it's possible for that LBA to be trashed after an unexpected power drop.
Guh. I was not aware of this. I knew consumer-grade SSDs often do not have power loss protection, but still thought they´d handle garble collection in an atomic way. Sometimes I am tempted to sing an "all hardware is crap" song (starting with Meltdown/Spectre, then probably heading over to storage devices and so on… including firmware crap like Intel ME).
Next, the reason why fsync() has the behaviour that it does is one ofhe the most common cases of I/O storage errors in buffered use cases, certainly as seen by the community distros, is the user who pulls out USB stick while it is in use. In that case, if there are dirtied pages in the page cache, the question is what can you do? Sooner or later the writes will time out, and if you leave the pages dirty, then it effectively becomes a permanent memory leak. You can't unmount the file system --- that requires writing out all of the pages such that the dirty bit is turned off. And if you don't clear the dirty bit on an I/O error, then they can never be cleaned. You can't even re-insert the USB stick; the re-inserted USB stick will get a new block device. Worse, when the USB stick was pulled, it will have suffered a power drop, and see above about what could happen after a power drop for non-power fail certified flash devices --- it goes double for the cheap sh*t USB sticks found in the checkout aisle of Micro Center.
From the original PostgreSQL mailing list thread I did not get on how exactly FreeBSD differs in behavior, compared to Linux. I am aware of one operating system that from a user point of view handles this in almost the right way IMHO: AmigaOS.
When you removed a floppy disk from the drive while the OS was writing to it it showed a "You MUST insert volume somename into drive somedrive:" and if you did, it just continued writing. (The part that did not work well was that with the original filesystem if you did not insert it back, the whole disk was corrupted, usually to the point beyond repair, so the "MUST" was no joke.)
In my opinion from a user´s point of view this is the only sane way to handle the premature removal of removable media. I have read of a GSoC project to implement something like this for NetBSD but I did not check on the outcome of it. But in MS-DOS I think there has been something similar, however MS-DOS is not an multitasking operating system as AmigaOS is.
Implementing something like this for Linux would be quite a feat, I think, cause in addition to the implementation in the kernel, the desktop environment or whatever other userspace you use would need to handle it as well, so you´d have to adapt udev / udisks / probably Systemd. And probably this behavior needs to be restricted to anything that is really removable and even then in order to prevent memory exhaustion in case processes continue to write to an removed and not yet re-inserted USB harddisk the kernel would need to halt I/O processes which dirty I/O to this device. (I believe this is what AmigaOS did. It just blocked all subsequent I/O to the device still it was re-inserted. But then the I/O handling in that OS at that time is quite different from what Linux does.)
So this is the explanation for why Linux handles I/O errors by clearing the dirty bit after reporting the error up to user space. And why there is not eagerness to solve the problem simply by "don't clear the dirty bit". For every one Postgres installation that might have a better recover after an I/O error, there's probably a thousand clueless Fedora and Ubuntu users who will have a much worse user experience after a USB stick pull happens.
I was not aware that flash based media may be as crappy as you hint at.
From my tests with AmigaOS 4.something or AmigaOS 3.9 + 3rd Party Poseidon USB stack the above mechanism worked even with USB sticks. I however did not test this often and I did not check for data corruption after a test.
From:   Andres Freund <andres@...razel.de>
Date:   Tue, 10 Apr 2018 15:07:26 -0700
(Sorry if I screwed up the thread structure - I'd to reconstruct the reply-to and CC list from web archive as I've not found a way to properly download an mbox or such of old content. Was subscribed to fsdevel but not ext4 lists)
Hi,
2018-04-10 18:43:56 Ted wrote:
I'll try to give as unbiased a description as possible, but certainly some of this is going to be filtered by my own biases no matter how careful I can be.
Same ;)
2018-04-10 18:43:56 Ted wrote:
So for better or for worse, there has not been as much investment in buffered I/O and data robustness in the face of exception handling of storage devices.
That's a bit of a cop out. It's not just databases that care. Even more basic tools like SCM, package managers and editors care whether they can proper responses back from fsync that imply things actually were synced.
2018-04-10 18:43:56 Ted wrote:
So this is the explanation for why Linux handles I/O errors by clearing the dirty bit after reporting the error up to user space. And why there is not eagerness to solve the problem simply by "don't clear the dirty bit". For every one Postgres installation that might have a better recover after an I/O error, there's probably a thousand clueless Fedora and Ubuntu users who will have a much worse user experience after a USB stick pull happens.
I don't think these necessarily are as contradictory goals as you paint them. At least in postgres' case we can deal with the fact that an fsync retry isn't going to fix the problem by reentering crash recovery or just shutting down - therefore we don't need to keep all the dirty buffers around. A per-inode or per-superblock bit that causes further fsyncs to fail would be entirely sufficent for that.
While there's some differing opinions on the referenced postgres thread, the fundamental problem isn't so much that a retry won't fix the problem, it's that we might NEVER see the failure. If writeback happens in the background, encounters an error, undirties the buffer, we will happily carry on because we've never seen that. That's when we're majorly screwed.
Both in postgres,
and
a lot of other applications, it's not at all guaranteed to consistently have one FD open for every file writtten. Therefore even the more recent per-fd errseq logic doesn't guarantee that the failure will ever be seen by an application diligently fsync()ing.
You'd not even need to have per inode information or such in the case that the block device goes away entirely. As the FS isn't generally unmounted in that case, you could trivially keep a per-mount (or superblock?) bit that says "I died" and set that instead of keeping per inode/whatever information.
2018-04-10 18:43:56 Ted wrote:
If you are aware of a company who is willing to pay to have a new kernel feature implemented to meet your needs, we might be able to refer you to a company or a consultant who might be able to do that work.
I find it a bit dissapointing response. I think it's fair to say that for advanced features, but we're talking about the basic guarantee that fsync actually does something even remotely reasonable.
2018-04-10 19:44:48 Andreas wrote:
The confusion is whether fsync() is a "level" state (return error forever if there were pages that could not be written), or an "edge" state (return error only for any write failures since the previous fsync() call).
I don't think that's the full issue. We can deal with the fact that an fsync failure is edge-triggered if there's a guarantee that every process doing so would get it. The fact that one needs to have an FD open from before any failing writes occurred to get a failure,
THAT'S
the big issue.
Beyond postgres, it's a pretty common approach to do work on a lot of files without fsyncing, then iterate over the directory fsync everything, and
then
assume you're safe. But unless I severaly misunderstand something that'd only be safe if you kept an FD for every file open, which isn't realistic for pretty obvious reasons.
2018-04-10 18:43:56 Ted wrote:
I think Anthony Iliopoulos was pretty clear in his multiple descriptions in that thread of why the current behaviour is needed (OOM of the whole system if dirty pages are kept around forever), but many others were stuck on "I can't believe this is happening??? This is totally unacceptable and every kernel needs to change to match my expectations!!!" without looking at the larger picture of what is practical to change and where the issue should best be fixed.
Everone can participate in discussions...
From:   Andreas Dilger <adilger@...ger.ca>
Date:   Wed, 11 Apr 2018 15:52:44 -0600
On Apr 10, 2018, at 4:07 PM, Andres Freund
andres@...razel.de
wrote:
2018-04-10 18:43:56 Ted wrote:
So for better or for worse, there has not been as much investment in buffered I/O and data robustness in the face of exception handling of storage devices.
That's a bit of a cop out. It's not just databases that care. Even more basic tools like SCM, package managers and editors care whether they can proper responses back from fsync that imply things actually were synced.
Sure, but it is mostly PG that is doing (IMHO) crazy things like writing to thousands(?) of files, closing the file descriptors, then expecting fsync() on a newly-opened fd to return a historical error. If an editor tries to write a file, then calls fsync and gets an error, the user will enter a new pathname and retry the write. The package manager will assume the package installation failed, and uninstall the parts of the package that were already written.
There is no way the filesystem can handle the package manager failure case, and keeping the pages dirty and retrying indefinitely may never work (e.g. disk is dead or disconnected, is a sparse volume without any free space, etc). This (IMHO) implies that the higher layer (which knows more about what the write failure implies) needs to deal with this.
2018-04-10 18:43:56 Ted wrote:
So this is the explanation for why Linux handles I/O errors by clearing the dirty bit after reporting the error up to user space. And why there is not eagerness to solve the problem simply by "don't clear the dirty bit". For every one Postgres installation that might have a better recover after an I/O error, there's probably a thousand clueless Fedora and Ubuntu users who will have a much worse user experience after a USB stick pull happens.
I don't think these necessarily are as contradictory goals as you paint them. At least in postgres' case we can deal with the fact that an fsync retry isn't going to fix the problem by reentering crash recovery or just shutting down - therefore we don't need to keep all the dirty buffers around. A per-inode or per-superblock bit that causes further fsyncs to fail would be entirely sufficent for that.
While there's some differing opinions on the referenced postgres thread, the fundamental problem isn't so much that a retry won't fix the problem, it's that we might NEVER see the failure. If writeback happens in the background, encounters an error, undirties the buffer, we will happily carry on because we've never seen that. That's when we're majorly screwed.
I think there are two issues here - "fsync() on an fd that was just opened" and "persistent error state (without keeping dirty pages in memory)".
If there is background data writeback
without an open file descriptor
, there is no mechanism for the kernel to return an error to any application which may exist, or may not ever come back.
Consider if there was a per-inode "there was once an error writing this inode" flag. Then fsync() would return an error on the inode forever, since there is no way in POSIX to clear this state, since it would need to be kept in case some new fd is opened on the inode and does an fsync() and wants the error to be returned.
IMHO, the only alternative would be to keep the dirty pages in memory until they are written to disk. If that was not possible, what then? It would need a reboot to clear the dirty pages, or truncate the file (discarding all data)?
Both in postgres,
and
a lot of other applications, it's not at all guaranteed to consistently have one FD open for every file written. Therefore even the more recent per-fd errseq logic doesn't guarantee that the failure will ever be seen by an application diligently fsync()ing.
... only if the application closes all fds for the file before calling fsync. If any fd is kept open from the time of the failure, it will return the original error on fsync() (and then no longer return it).
It's not that you need to keep every fd open forever. You could put them into a shared pool, and re-use them if the file is "re-opened", and call fsync on each fd before it is closed (because the pool is getting too big or because you want to flush the data for that file, or shut down the DB). That wouldn't require a huge re-architecture of PG, just a small library to handle the shared fd pool.
That might even improve performance, because opening and closing files is itself not free, especially if you are working with remote filesystems.
You'd not even need to have per inode information or such in the case that the block device goes away entirely. As the FS isn't generally unmounted in that case, you could trivially keep a per-mount (or superblock?) bit that says "I died" and set that instead of keeping per inode/whatever information.
The filesystem will definitely return an error in this case, I don't think this needs any kind of changes:
int ext4_sync_file(struct file *file, loff_t start, loff_t end, int datasync) { if (unlikely(ext4_forced_shutdown(EXT4_SB(inode->i_sb)))) return -EIO;
2018-04-10 18:43:56 Ted wrote:
If you are aware of a company who is willing to pay to have a new kernel feature implemented to meet your needs, we might be able to refer you to a company or a consultant who might be able to do that work.
I find it a bit dissapointing response. I think it's fair to say that for advanced features, but we're talking about the basic guarantee that fsync actually does something even remotely reasonable.
Linux (as PG) is run by people who develop it for their own needs, or are paid to develop it for the needs of others. Everyone already has too much work to do, so you need to find someone who has an interest in fixing this (IMHO very peculiar) use case. If PG developers want to add a tunable "keep dirty pages in RAM on IO failure", I don't think that it would be too hard for someone to do. It might be harder to convince some of the kernel maintainers to accept it, and I've been on the losing side of that battle more than once. However, like everything you don't pay for, you can't require someone else to do this for you. It wouldn't hurt to see if Jeff Layton, who wrote the errseq patches, would be interested to work on something like this.
That said,
even
if a fix was available for Linux tomorrow, it would be
years
before a majority of users would have it available on their system, that includes even the errseq mechanism that was landed a few months ago. That implies to me that you'd want something that fixes PG
now
so that it works around whatever (perceived) breakage exists in the Linux fsync() implementation. Since the thread indicates that non-Linux kernels have the same fsync() behaviour, it makes sense to do that even if the Linux fix was available.
2018-04-10 19:44:48 Andreas wrote:
The confusion is whether fsync() is a "level" state (return error forever if there were pages that could not be written), or an "edge" state (return error only for any write failures since the previous fsync() call).
I don't think that's the full issue. We can deal with the fact that an fsync failure is edge-triggered if there's a guarantee that every process doing so would get it. The fact that one needs to have an FD open from before any failing writes occurred to get a failure,
THAT'S
the big issue.
Beyond postgres, it's a pretty common approach to do work on a lot of files without fsyncing, then iterate over the directory fsync everything, and
then
assume you're safe. But unless I severaly misunderstand something that'd only be safe if you kept an FD for every file open, which isn't realistic for pretty obvious reasons.
I can't say how common or uncommon such a workload is, though PG is the only application that I've heard of doing it, and I've been working on filesystems for 20 years. I'm a bit surprised that anyone expects fsync() on a newly-opened fd to have any state from write() calls that predate the open. I can understand fsync() returning an error for any IO that happens within the context of that fsync(), but how far should it go back for reporting errors on that file? Forever? The only way to clear the error would be to reboot the system, since I'm not aware of any existing POSIX code to clear such an error
From:   Dave Chinner <david@...morbit.com>
Date:   Thu, 12 Apr 2018 10:09:16 +1000
On Wed, Apr 11, 2018 at 03:52:44PM -0600, Andreas Dilger wrote: > On Apr 10, 2018, at 4:07 PM, Andres Freund
andres@...razel.de
wrote: > > 2018-04-10 18:43:56 Ted wrote: > >> So for better or for worse, there has not been as much investment in > >> buffered I/O and data robustness in the face of exception handling of > >> storage devices. > > > > That's a bit of a cop out. It's not just databases that care. Even more > > basic tools like SCM, package managers and editors care whether they can > > proper responses back from fsync that imply things actually were synced. > > Sure, but it is mostly PG that is doing (IMHO) crazy things like writing > to thousands(?) of files, closing the file descriptors, then expecting > fsync() on a newly-opened fd to return a historical error.
Yeah, this seems like a recipe for disaster, especially on cross-platform code where every OS platform behaves differently and almost never to expectation.
And speaking of "behaving differently to expectations", nobody has mentioned that close() can also return write errors. Hence if you do write - close - open - fsync the the write error might get reported on close, not fsync. IOWs, the assumption that "async writeback errors will persist across close to open" is fundamentally broken to begin with. It's even documented as a slient data loss vector in the close(2) man page:
$ man 2 close
.....
   Dealing with error returns from close()

	  A careful programmer will check the return value of
	  close(), since it is quite possible that  errors  on  a
	  previous  write(2)  operation  are reported  only on the
	  final close() that releases the open file description.
	  Failing to check the return value when closing a file may
	  lead to silent loss of data.  This can especially be
	  observed with NFS and with disk quota.
Yeah, ensuring data integrity in the face of IO errors is a really hard problem. :/
To pound the broken record: there are many good reasons why Linux filesystem developers have said "you should use direct IO" to the PG devs each time we have this "the kernel doesn't do [complex things PG needs]" discussion.
In this case, robust IO error reporting is easy with DIO. It's one of the reasons most of the high performance database engines are either using or moving to non-blocking AIO+DIO (RWF_NOWAIT) and use O_DSYNC/RWF_DSYNC for integrity-critical IO dispatch. This is also being driven by the availability of high performance, high IOPS solid state storage where buffering in RAM to optimise IO patterns and throughput provides no real performance benefit.
Using the AIO+DIO infrastructure ensures errors are reported for the specific write that fails at failure time (i.e. in the aio completion event for the specific IO), yet high IO throughput can be maintained without the application needing it's own threading infrastructure to prevent blocking.
This means the application doesn't have to guess where the write error occurred to retry/recover, have to handle async write errors on close(), have to use fsync() to gather write IO errors and then infer where the IO failure was, or require kernels on every supported platform to jump through hoops to try to do exactly the right thing in error conditions for everyone in all circumstances at all times....
From:   Andres Freund <andres@...razel.de>
Date:   Wed, 11 Apr 2018 19:17:52 -0700
On 2018-04-11 15:52:44 -0600, Andreas Dilger wrote:
On Apr 10, 2018, at 4:07 PM, Andres Freund
andres@...razel.de
wrote:
2018-04-10 18:43:56 Ted wrote:
So for better or for worse, there has not been as much investment in buffered I/O and data robustness in the face of exception handling of storage devices.
That's a bit of a cop out. It's not just databases that care. Even more basic tools like SCM, package managers and editors care whether they can proper responses back from fsync that imply things actually were synced.
Sure, but it is mostly PG that is doing (IMHO) crazy things like writing to thousands(?) of files, closing the file descriptors, then expecting fsync() on a newly-opened fd to return a historical error.
It's not just postgres. dpkg (underlying apt, on debian derived distros) to take an example I just randomly guessed, does too:
/* We want to guarantee the extracted files are on the disk, so that the
   * subsequent renames to the info database do not end up with old or zero
   * length files in case of a system crash. As neither dpkg-deb nor tar do
   * explicit fsync()s, we have to do them here.
   * XXX: This could be avoided by switching to an internal tar extractor. */
  dir_sync_contents(cidir);
(a bunch of other places too)
Especially on ext3 but also on newer filesystems it's performancewise entirely infeasible to fsync() every single file individually - the performance becomes entirely attrocious if you do that.
I think there's some legitimate arguments that a database should use direct IO (more on that as a reply to David), but claiming that all sorts of random utilities need to use DIO with buffering etc is just insane.
If an editor tries to write a file, then calls fsync and gets an error, the user will enter a new pathname and retry the write. The package manager will assume the package installation failed, and uninstall the parts of the package that were already written.
Except that they won't notice that they got a failure, at least in the dpkg case. And happily continue installing corrupted data
There is no way the filesystem can handle the package manager failure case, and keeping the pages dirty and retrying indefinitely may never work (e.g. disk is dead or disconnected, is a sparse volume without any free space, etc). This (IMHO) implies that the higher layer (which knows more about what the write failure implies) needs to deal with this.
Yea, I agree that'd not be sane. As far as I understand the dpkg code (all of 10min reading it), that'd also be unnecessary. It can abort the installation, but only if it detects the error. Which isn't happening.
While there's some differing opinions on the referenced postgres thread, the fundamental problem isn't so much that a retry won't fix the problem, it's that we might NEVER see the failure. If writeback happens in the background, encounters an error, undirties the buffer, we will happily carry on because we've never seen that. That's when we're majorly screwed.
I think there are two issues here - "fsync() on an fd that was just opened" and "persistent error state (without keeping dirty pages in memory)".
If there is background data writeback
without an open file descriptor
, there is no mechanism for the kernel to return an error to any application which may exist, or may not ever come back.
And that's
horrible
. If I cp a file, and writeback fails in the background, and I then cat that file before restarting, I should be able to see that that failed. Instead of returning something bogus.
Or even more extreme, you untar/zip/git clone a directory. Then do a sync. And you don't know whether anything actually succeeded.
Consider if there was a per-inode "there was once an error writing this inode" flag. Then fsync() would return an error on the inode forever, since there is no way in POSIX to clear this state, since it would need to be kept in case some new fd is opened on the inode and does an fsync() and wants the error to be returned.
The data in the file also is corrupt. Having to unmount or delete the file to reset the fact that it can't safely be assumed to be on disk isn't insane.
Both in postgres,
and
a lot of other applications, it's not at all guaranteed to consistently have one FD open for every file written. Therefore even the more recent per-fd errseq logic doesn't guarantee that the failure will ever be seen by an application diligently fsync()ing.
... only if the application closes all fds for the file before calling fsync. If any fd is kept open from the time of the failure, it will return the original error on fsync() (and then no longer return it).
It's not that you need to keep every fd open forever. You could put them into a shared pool, and re-use them if the file is "re-opened", and call fsync on each fd before it is closed (because the pool is getting too big or because you want to flush the data for that file, or shut down the DB). That wouldn't require a huge re-architecture of PG, just a small library to handle the shared fd pool.
Except that postgres uses multiple processes. And works on a lot of architectures. If we started to fsync all opened files on process exit our users would
lynch
us. We'd need a complicated scheme that sends processes across sockets between processes, then deduplicate them on the receiving side, somehow figuring out which is the oldest filedescriptors (handling clockdrift safely).
Note that it'd be perfectly fine that we've "thrown away" the buffer contents if we'd get notified that the fsync failed. We could just do WAL replay, and restore the contents (just was we do after crashes and/or for replication).
That might even improve performance, because opening and closing files is itself not free, especially if you are working with remote filesystems.
There's already a per-process cache of open files.
You'd not even need to have per inode information or such in the case that the block device goes away entirely. As the FS isn't generally unmounted in that case, you could trivially keep a per-mount (or superblock?) bit that says "I died" and set that instead of keeping per inode/whatever information.
The filesystem will definitely return an error in this case, I don't think this needs any kind of changes:
int ext4_sync_file(struct file *file, loff_t start, loff_t end, int datasync) { if (unlikely(ext4_forced_shutdown(EXT4_SB(inode->i_sb)))) return -EIO;
Well, I'm making that argument because several people argued that throwing away buffer contents in this case is the only way to not cause OOMs, and that that's incompatible with reporting errors. It's clearly not...
2018-04-10 18:43:56 Ted wrote:
If you are aware of a company who is willing to pay to have a new kernel feature implemented to meet your needs, we might be able to refer you to a company or a consultant who might be able to do that work.
I find it a bit dissapointing response. I think it's fair to say that for advanced features, but we're talking about the basic guarantee that fsync actually does something even remotely reasonable.
Linux (as PG) is run by people who develop it for their own needs, or are paid to develop it for the needs of others.
Sure.
Everyone already has too much work to do, so you need to find someone who has an interest in fixing this (IMHO very peculiar) use case. If PG developers want to add a tunable "keep dirty pages in RAM on IO failure", I don't think that it would be too hard for someone to do. It might be harder to convince some of the kernel maintainers to accept it, and I've been on the losing side of that battle more than once. However, like everything you don't pay for, you can't require someone else to do this for you. It wouldn't hurt to see if Jeff Layton, who wrote the errseq patches, would be interested to work on something like this.
I don't think this is that PG specific, as explained above.
From:   Andres Freund <andres@...razel.de>
Date:   Wed, 11 Apr 2018 19:32:21 -0700
Hi,
On 2018-04-12 10:09:16 +1000, Dave Chinner wrote:
To pound the broken record: there are many good reasons why Linux filesystem developers have said "you should use direct IO" to the PG devs each time we have this "the kernel doesn't do [complex things PG needs]" discussion.
I personally am on board with doing that. But you also gotta recognize that an efficient DIO usage is a metric ton of work, and you need a large amount of differing logic for different platforms. It's just not realistic to do so for every platform. Postgres is developed by a small number of people, isn't VC backed etc. The amount of resources we can throw at something is fairly limited. I'm hoping to work on adding linux DIO support to pg, but I'm sure as hell not going to do be able to do the same on windows (solaris, hpux, aix, ...) etc.
And there's cases where that just doesn't help at all. Being able to untar a database from backup / archive / timetravel / whatnot, and then fsyncing the directory tree to make sure it's actually safe, is really not an insane idea. Or even just cp -r ing it, and then starting up a copy of the database. What you're saying is that none of that is doable in a safe way, unless you use special-case DIO using tooling for the whole operation (or at least tools that fsync carefully without ever closing a fd, which certainly isn't the case for cp et al).
In this case, robust IO error reporting is easy with DIO. It's one of the reasons most of the high performance database engines are either using or moving to non-blocking AIO+DIO (RWF_NOWAIT) and use O_DSYNC/RWF_DSYNC for integrity-critical IO dispatch. This is also being driven by the availability of high performance, high IOPS solid state storage where buffering in RAM to optimise IO patterns and throughput provides no real performance benefit.
Using the AIO+DIO infrastructure ensures errors are reported for the specific write that fails at failure time (i.e. in the aio completion event for the specific IO), yet high IO throughput can be maintained without the application needing it's own threading infrastructure to prevent blocking.
This means the application doesn't have to guess where the write error occurred to retry/recover, have to handle async write errors on close(), have to use fsync() to gather write IO errors and then infer where the IO failure was, or require kernels on every supported platform to jump through hoops to try to do exactly the right thing in error conditions for everyone in all circumstances at all times....
Most of that sounds like a good thing to do, but you got to recognize that that's a lot of linux specific code.
From:   Andres Freund <andres@...razel.de>
Date:   Wed, 11 Apr 2018 19:51:13 -0700
Hi,
On 2018-04-11 19:32:21 -0700, Andres Freund wrote:
And there's cases where that just doesn't help at all. Being able to untar a database from backup / archive / timetravel / whatnot, and then fsyncing the directory tree to make sure it's actually safe, is really not an insane idea. Or even just cp -r ing it, and then starting up a copy of the database. What you're saying is that none of that is doable in a safe way, unless you use special-case DIO using tooling for the whole operation (or at least tools that fsync carefully without ever closing a fd, which certainly isn't the case for cp et al).
And before somebody argues that that's a too small window to trigger the problem realistically: Restoring large databases happens pretty commonly (for new replicas, testcases, or actual fatal issues), takes time, and it's where a lot of storage is actually written to for the first time in a while, so it's far from unlikely to trigger bad block errors or such.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Wed, 11 Apr 2018 20:02:48 -0700
On Wed, Apr 11, 2018 at 07:17:52PM -0700, Andres Freund wrote:
While there's some differing opinions on the referenced postgres thread, the fundamental problem isn't so much that a retry won't fix the problem, it's that we might NEVER see the failure. If writeback happens in the background, encounters an error, undirties the buffer, we will happily carry on because we've never seen that. That's when we're majorly screwed.
I think there are two issues here - "fsync() on an fd that was just opened" and "persistent error state (without keeping dirty pages in memory)".
If there is background data writeback
without an open file descriptor
, there is no mechanism for the kernel to return an error to any application which may exist, or may not ever come back.
And that's
horrible
. If I cp a file, and writeback fails in the background, and I then cat that file before restarting, I should be able to see that that failed. Instead of returning something bogus.
At the moment, when we open a file, we sample the current state of the writeback error and only report new errors. We could set it to zero instead, and report the most recent error as soon as anything happens which would report an error. That way err = close(open("file")); would report the most recent error.
That's not going to be persistent across the data structure for that inode being removed from memory; we'd need filesystem support for persisting that. But maybe it's "good enough" to only support it for recent files.
Jeff, what do you think?
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Thu, 12 Apr 2018 01:09:24 -0400
On Wed, Apr 11, 2018 at 07:32:21PM -0700, Andres Freund wrote:
Most of that sounds like a good thing to do, but you got to recognize that that's a lot of linux specific code.
I know it's not what PG has chosen, but realistically all of the other major databases and userspace based storage systems have used DIO precisely
because
it's the way to avoid OS-specific behavior or require OS-specific code. DIO is simple, and pretty much the same everywhere.
In contrast, the exact details of how buffered I/O workrs can be quite different on different OS's. This is especially true if you take performance related details (e.g., the cleaning algorithm, how pages get chosen for eviction, etc.)
As I read the PG-hackers thread, I thought I saw acknowledgement that some of the behaviors you don't like with Linux also show up on other Unix or Unix-like systems?
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Thu, 12 Apr 2018 01:34:45 -0400
On Wed, Apr 11, 2018 at 07:17:52PM -0700, Andres Freund wrote:
If there is background data writeback
without an open file descriptor
, there is no mechanism for the kernel to return an error to any application which may exist, or may not ever come back.
And that's
horrible
. If I cp a file, and writeback fails in the background, and I then cat that file before restarting, I should be able to see that that failed. Instead of returning something bogus.
If there is no open file descriptor, and in many cases, no process (because it has already exited), it may be horrible, but what the h*ll else do you expect the OS to do?
The solution we use at Google is that we watch for I/O errors using a completely different process that is responsible for monitoring machine health. It used to scrape dmesg, but we now arrange to have I/O errors get sent via a netlink channel to the machine health monitoring daemon. If it detects errors on a particular hard drive, it tells the cluster file system to stop using that disk, and to reconstruct from erasure code all of the data chunks on that disk onto other disks in the cluster. We then run a series of disk diagnostics to make sure we find all of the bad sectors (every often, where there is one bad sector, there are several more waiting to be found), and then afterwards, put the disk back into service.
By making it be a separate health monitoring process, we can have HDD experts write much more sophisticated code that can ask the disk firmware for more information (e.g., SMART, the grown defect list), do much more careful scrubbing of the disk media, etc., before returning the disk back to service.
Everyone already has too much work to do, so you need to find someone who has an interest in fixing this (IMHO very peculiar) use case. If PG developers want to add a tunable "keep dirty pages in RAM on IO failure", I don't think that it would be too hard for someone to do. It might be harder to convince some of the kernel maintainers to accept it, and I've been on the losing side of that battle more than once. However, like everything you don't pay for, you can't require someone else to do this for you. It wouldn't hurt to see if Jeff Layton, who wrote the errseq patches, would be interested to work on something like this.
I don't think this is that PG specific, as explained above.
The reality is that recovering from disk errors is tricky business, and I very much doubt most userspace applications, including distro package managers, are going to want to engineer for trying to detect and recover from disk errors. If that were true, then Red Hat and/or SuSE have kernel engineers, and they would have implemented everything everything on your wish list. They haven't, and that should tell you something.
The other reality is that once a disk starts developing errors, in reality you will probably need to take the disk off-line, scrub it to find any other media errors, and there's a good chance you'll need to rewrite bad sectors (incluing some which are on top of file system metadata, so you probably will have to run fsck or reformat the whole file system). I certainly don't think it's realistic to assume adding lots of sophistication to each and every userspace program.
If you have tens or hundreds of thousands of disk drives, then you will need to do tsomething automated, but I claim that you really don't want to smush all of that detailed exception handling and HDD repair technology into each database or cluster file system component. It really needs to be done in a separate health-monitor and machine-level management system.
From:   Dave Chinner <david@...morbit.com>
Date:   Thu, 12 Apr 2018 15:45:36 +1000
On Wed, Apr 11, 2018 at 07:32:21PM -0700, Andres Freund wrote:
Hi,
On 2018-04-12 10:09:16 +1000, Dave Chinner wrote:
To pound the broken record: there are many good reasons why Linux filesystem developers have said "you should use direct IO" to the PG devs each time we have this "the kernel doesn't do
" discussion.
I personally am on board with doing that. But you also gotta recognize that an efficient DIO usage is a metric ton of work, and you need a large amount of differing logic for different platforms. It's just not realistic to do so for every platform. Postgres is developed by a small number of people, isn't VC backed etc. The amount of resources we can throw at something is fairly limited. I'm hoping to work on adding linux DIO support to pg, but I'm sure as hell not going to do be able to do the same on windows (solaris, hpux, aix, ...) etc.
And there's cases where that just doesn't help at all. Being able to untar a database from backup / archive / timetravel / whatnot, and then fsyncing the directory tree to make sure it's actually safe, is really not an insane idea.
Yes it is.
This is what syncfs() is for - making sure a large amount of of data and metadata spread across many files and subdirectories in a single filesystem is pushed to stable storage in the most efficient manner possible.
Or even just cp -r ing it, and then starting up a copy of the database. What you're saying is that none of that is doable in a safe way, unless you use special-case DIO using tooling for the whole operation (or at least tools that fsync carefully without ever closing a fd, which certainly isn't the case for cp et al).
No, Just saying fsyncing individual files and directories is about the most inefficient way you could possible go about doing this.
From:   Lukas Czerner <lczerner@...hat.com>
Date:   Thu, 12 Apr 2018 12:19:26 +0200
On Wed, Apr 11, 2018 at 07:32:21PM -0700, Andres Freund wrote:
And there's cases where that just doesn't help at all. Being able to untar a database from backup / archive / timetravel / whatnot, and then fsyncing the directory tree to make sure it's actually safe, is really not an insane idea. Or even just cp -r ing it, and then starting up a copy of the database. What you're saying is that none of that is doable in a safe way, unless you use special-case DIO using tooling for the whole operation (or at least tools that fsync carefully without ever closing a fd, which certainly isn't the case for cp et al).
Does not seem like a problem to me, just checksum the thing if you really need to be extra safe. You should probably be doing it anyway if you backup / archive / timetravel / whatnot.
From:   Jeff Layton <jlayton@...hat.com>
Date:   Thu, 12 Apr 2018 07:09:14 -0400
On Wed, 2018-04-11 at 20:02 -0700, Matthew Wilcox wrote:
On Wed, Apr 11, 2018 at 07:17:52PM -0700, Andres Freund wrote:
While there's some differing opinions on the referenced postgres thread, the fundamental problem isn't so much that a retry won't fix the problem, it's that we might NEVER see the failure. If writeback happens in the background, encounters an error, undirties the buffer, we will happily carry on because we've never seen that. That's when we're majorly screwed.
I think there are two issues here - "fsync() on an fd that was just opened" and "persistent error state (without keeping dirty pages in memory)".
If there is background data writeback
without an open file descriptor
, there is no mechanism for the kernel to return an error to any application which may exist, or may not ever come back.
And that's
horrible
. If I cp a file, and writeback fails in the background, and I then cat that file before restarting, I should be able to see that that failed. Instead of returning something bogus.
What are you expecting to happen in this case? Are you expecting a read error due to a writeback failure? Or are you just saying that we should be invalidating pages that failed to be written back, so that they can be re-read?
At the moment, when we open a file, we sample the current state of the writeback error and only report new errors. We could set it to zero instead, and report the most recent error as soon as anything happens which would report an error. That way err = close(open("file")); would report the most recent error.
That's not going to be persistent across the data structure for that inode being removed from memory; we'd need filesystem support for persisting that. But maybe it's "good enough" to only support it for recent files.
Jeff, what do you think?
I hate it :). We could do that, but....yecchhhh.
Reporting errors only in the case where the inode happened to stick around in the cache seems too unreliable for real-world usage, and might be problematic for some use cases. I'm also not sure it would really be helpful.
I think the crux of the matter here is not really about error reporting, per-se. I asked this at LSF last year, and got no real answer:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
One possibility would be to invalidate the range that failed to be written (or the whole file) and force the pages to be faulted in again on the next access. It could be surprising for some applications to not see the results of their writes on a subsequent read after such an event.
Maybe that's ok in the face of a writeback error though? IDK.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Thu, 12 Apr 2018 04:19:48 -0700
On Thu, Apr 12, 2018 at 07:09:14AM -0400, Jeff Layton wrote:
On Wed, 2018-04-11 at 20:02 -0700, Matthew Wilcox wrote:
At the moment, when we open a file, we sample the current state of the writeback error and only report new errors. We could set it to zero instead, and report the most recent error as soon as anything happens which would report an error. That way err = close(open("file")); would report the most recent error.
That's not going to be persistent across the data structure for that inode being removed from memory; we'd need filesystem support for persisting that. But maybe it's "good enough" to only support it for recent files.
Jeff, what do you think?
I hate it :). We could do that, but....yecchhhh.
Reporting errors only in the case where the inode happened to stick around in the cache seems too unreliable for real-world usage, and might be problematic for some use cases. I'm also not sure it would really be helpful.
Yeah, it's definitely half-arsed. We could make further changes to improve the situation, but they'd have wider impact. For example, we can tell if the error has been sampled by any existing fd, so we could bias our inode reaping to have inodes with unreported errors stick around in the cache for longer.
I think the crux of the matter here is not really about error reporting, per-se. I asked this at LSF last year, and got no real answer:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
I suspect it isn't. If there's a transient error then we should reattempt the write. OTOH if the error is permanent then reattempting the write isn't going to do any good and it's just going to cause the drive to go through the whole error handling dance again. And what do we do if we're low on memory and need these pages back to avoid going OOM? There's a lot of options here, all of them bad in one situation or another.
One possibility would be to invalidate the range that failed to be written (or the whole file) and force the pages to be faulted in again on the next access. It could be surprising for some applications to not see the results of their writes on a subsequent read after such an event.
Maybe that's ok in the face of a writeback error though? IDK.
I don't know either. It'd force the application to face up to the fact that the data is gone immediately rather than only finding it out after a reboot. Again though that might cause more problems than it solves. It's hard to know what the right thing to do is.
From:   Jeff Layton <jlayton@...hat.com>
Date:   Thu, 12 Apr 2018 07:24:12 -0400
On Thu, 2018-04-12 at 15:45 +1000, Dave Chinner wrote:
On Wed, Apr 11, 2018 at 07:32:21PM -0700, Andres Freund wrote:
Hi,
On 2018-04-12 10:09:16 +1000, Dave Chinner wrote:
To pound the broken record: there are many good reasons why Linux filesystem developers have said "you should use direct IO" to the PG devs each time we have this "the kernel doesn't do
" discussion.
I personally am on board with doing that. But you also gotta recognize that an efficient DIO usage is a metric ton of work, and you need a large amount of differing logic for different platforms. It's just not realistic to do so for every platform. Postgres is developed by a small number of people, isn't VC backed etc. The amount of resources we can throw at something is fairly limited. I'm hoping to work on adding linux DIO support to pg, but I'm sure as hell not going to do be able to do the same on windows (solaris, hpux, aix, ...) etc.
And there's cases where that just doesn't help at all. Being able to untar a database from backup / archive / timetravel / whatnot, and then fsyncing the directory tree to make sure it's actually safe, is really not an insane idea.
Yes it is.
This is what syncfs() is for - making sure a large amount of of data and metadata spread across many files and subdirectories in a single filesystem is pushed to stable storage in the most efficient manner possible.
Just note that the error return from syncfs is somewhat iffy. It doesn't necessarily return an error when one inode fails to be written back. I think it mainly returns errors when you get a metadata writeback error.
Or even just cp -r ing it, and then starting up a copy of the database. What you're saying is that none of that is doable in a safe way, unless you use special-case DIO using tooling for the whole operation (or at least tools that fsync carefully without ever closing a fd, which certainly isn't the case for cp et al).
No, Just saying fsyncing individual files and directories is about the most inefficient way you could possible go about doing this.
You can still use syncfs but what you'd probably have to do is call syncfs while you still hold all of the fd's open, and then fsync each one afterward to ensure that they all got written back properly. That should work as you'd expect.
From:   Dave Chinner <david@...morbit.com>
Date:   Thu, 12 Apr 2018 22:01:22 +1000
On Thu, Apr 12, 2018 at 07:09:14AM -0400, Jeff Layton wrote:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
There isn't a right thing. Whatever we do will be wrong for someone.
One possibility would be to invalidate the range that failed to be written (or the whole file) and force the pages to be faulted in again on the next access. It could be surprising for some applications to not see the results of their writes on a subsequent read after such an event.
Not to mention a POSIX IO ordering violation. Seeing stale data after a "successful" write is simply not allowed.
Maybe that's ok in the face of a writeback error though? IDK.
No matter what we do for async writeback error handling, it will be slightly different from filesystem to filesystem, not to mention OS to OS. The is no magic bullet here, so I'm not sure we should worry too much. There's direct IO for anyone who cares that need to know about the completion status of every single write IO....
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Thu, 12 Apr 2018 11:16:46 -0400
On Thu, Apr 12, 2018 at 10:01:22PM +1000, Dave Chinner wrote:
On Thu, Apr 12, 2018 at 07:09:14AM -0400, Jeff Layton wrote:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
There isn't a right thing. Whatever we do will be wrong for someone.
That's the problem. The best that could be done (and it's not enough) would be to have a mode which does with the PG folks want (or what they
think
they want). It seems what they want is to have an error result in the page being marked clean. When they discover the outcome (OOM-city and the unability to unmount a file system on a failed drive), then they will complain to us
again
, at which point we can tell them that want they really want is another variation on O_PONIES, and welcome to the real world and real life.
Which is why, even if they were to pay someone to implement what they want, I'm not sure we would want to accept it upstream --- or distro's might consider it a support nightmare, and refuse to allow that mode to be enabled on enterprise distro's. But at least, it will have been some PG-based company who will have implemented it, so they're not wasting other people's time or other people's resources...
We could try to get something like what Google is doing upstream, which is to have the I/O errors sent to userspace via a netlink channel (without changing anything else about how buffered writeback is handled in the face of errors). Then userspace applications could switch to Direct I/O like all of the other really serious userspace storage solutions I'm aware of, and then someone could try to write some kind of HDD health monitoring system that tries to do the right thing when a disk is discovered to have developed some media errors or something more serious (e.g., a head failure). That plus some kind of RAID solution is I think the only thing which is really realistic for a typical PG site.
It's certainly that's what
I
would do if I didn't decide to use a hosted cloud solution, such as Cloud SQL for Postgres, and let someone else solve the really hard problems of dealing with real-world HDD failures. :-)
From:   Jeff Layton <jlayton@...hat.com>
Date:   Thu, 12 Apr 2018 11:08:50 -0400
On Thu, 2018-04-12 at 22:01 +1000, Dave Chinner wrote:
On Thu, Apr 12, 2018 at 07:09:14AM -0400, Jeff Layton wrote:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
There isn't a right thing. Whatever we do will be wrong for someone.
One possibility would be to invalidate the range that failed to be written (or the whole file) and force the pages to be faulted in again on the next access. It could be surprising for some applications to not see the results of their writes on a subsequent read after such an event.
Not to mention a POSIX IO ordering violation. Seeing stale data after a "successful" write is simply not allowed.
I'm not so sure here, given that we're dealing with an error condition. Are we really obligated not to allow any changes to pages that we can't write back?
Given that the pages are clean after these failures, we aren't doing this even today:
Suppose we're unable to do writes but can do reads vs. the backing store. After a wb failure, the page has the dirty bit cleared. If it gets kicked out of the cache before the read occurs, it'll have to be faulted back in. Poof -- your write just disappeared.
That can even happen before you get the chance to call fsync, so even a write()+read()+fsync() is not guaranteed to be safe in this regard today, given sufficient memory pressure.
I think the current situation is fine from a "let's not OOM at all costs" standpoint, but not so good for application predictability. We should really consider ways to do better here.
Maybe that's ok in the face of a writeback error though? IDK.
No matter what we do for async writeback error handling, it will be slightly different from filesystem to filesystem, not to mention OS to OS. The is no magic bullet here, so I'm not sure we should worry too much. There's direct IO for anyone who cares that need to know about the completion status of every single write IO....
I think we we have an opportunity here to come up with better defined and hopefully more useful behavior for buffered I/O in the face of writeback errors. The first step would be to hash out what we'd want it to look like.
Maybe we need a plenary session at LSF/MM?
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 12:46:27 -0700
Hi,
On 2018-04-12 12:19:26 +0200, Lukas Czerner wrote:
On Wed, Apr 11, 2018 at 07:32:21PM -0700, Andres Freund wrote:
And there's cases where that just doesn't help at all. Being able to untar a database from backup / archive / timetravel / whatnot, and then fsyncing the directory tree to make sure it's actually safe, is really not an insane idea. Or even just cp -r ing it, and then starting up a copy of the database. What you're saying is that none of that is doable in a safe way, unless you use special-case DIO using tooling for the whole operation (or at least tools that fsync carefully without ever closing a fd, which certainly isn't the case for cp et al).
Does not seem like a problem to me, just checksum the thing if you really need to be extra safe. You should probably be doing it anyway if you backup / archive / timetravel / whatnot.
That doesn't really help, unless you want to sync() and then re-read all the data to make sure it's the same. Rereading multi-TB backups just to know whether there was an error that the OS knew about isn't particularly fun. Without verifying after sync it's not going to improve the situation measurably, you're still only going to discover that $data isn't available when it's needed.
What you're saying here is that there's no way to use standard linux tools to manipulate files and know whether it failed, without filtering kernel logs for IO errors. Or am I missing something?
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 12:55:36 -0700
Hi,
On 2018-04-12 01:34:45 -0400, Theodore Y. Ts'o wrote:
The solution we use at Google is that we watch for I/O errors using a completely different process that is responsible for monitoring machine health. It used to scrape dmesg, but we now arrange to have I/O errors get sent via a netlink channel to the machine health monitoring daemon.
Any pointers to that the underling netlink mechanism? If we can force postgres to kill itself when such an error is detected (via a dedicated monitoring process), I'd personally be happy enough. It'd be nicer if we could associate that knowledge with particular filesystems etc (which'd possibly hard through dm etc?), but this'd be much better than nothing.
The reality is that recovering from disk errors is tricky business, and I very much doubt most userspace applications, including distro package managers, are going to want to engineer for trying to detect and recover from disk errors. If that were true, then Red Hat and/or SuSE have kernel engineers, and they would have implemented everything everything on your wish list. They haven't, and that should tell you something.
The problem really isn't about
recovering
from disk errors.
Knowing
about them is the crucial part. We do not want to give back clients the information that an operation succeeded, when it actually didn't. There could be improvements above that, but as long as it's guaranteed that "we" get the error (rather than just some kernel log we don't have access to, which looks different due to config etc), it's ok. We can throw our hands up in the air and give up.
The other reality is that once a disk starts developing errors, in reality you will probably need to take the disk off-line, scrub it to find any other media errors, and there's a good chance you'll need to rewrite bad sectors (incluing some which are on top of file system metadata, so you probably will have to run fsck or reformat the whole file system). I certainly don't think it's realistic to assume adding lots of sophistication to each and every userspace program.
If you have tens or hundreds of thousands of disk drives, then you will need to do tsomething automated, but I claim that you really don't want to smush all of that detailed exception handling and HDD repair technology into each database or cluster file system component. It really needs to be done in a separate health-monitor and machine-level management system.
Yea, agreed on all that. I don't think anybody actually involved in postgres wants to do anything like that. Seems far outside of postgres' remit.
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 13:13:22 -0700
Hi,
On 2018-04-12 11:16:46 -0400, Theodore Y. Ts'o wrote:
That's the problem. The best that could be done (and it's not enough) would be to have a mode which does with the PG folks want (or what they
think
they want). It seems what they want is to have an error result in the page being marked clean. When they discover the outcome (OOM-city and the unability to unmount a file system on a failed drive), then they will complain to us
again
, at which point we can tell them that want they really want is another variation on O_PONIES, and welcome to the real world and real life.
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient. I don't see that that'd realistically would trigger OOM or the inability to unmount a filesystem. If the drive is entirely gone there's obviously no point in keeping per-file information around, so per-blockdev/fs information suffices entirely to return an error on fsync (which at least on ext4 appears to happen if the underlying blockdev is gone).
Have fun making up things we want, but I'm not sure it's particularly productive.
Which is why, even if they were to pay someone to implement what they want, I'm not sure we would want to accept it upstream --- or distro's might consider it a support nightmare, and refuse to allow that mode to be enabled on enterprise distro's. But at least, it will have been some PG-based company who will have implemented it, so they're not wasting other people's time or other people's resources...
Well, that's why I'm discussing here so we can figure out what's acceptable before considering wasting money and revew cycles doing or paying somebody to do some crazy useless shit.
We could try to get something like what Google is doing upstream, which is to have the I/O errors sent to userspace via a netlink channel (without changing anything else about how buffered writeback is handled in the face of errors).
Ah, darn. After you'd mentioned that in an earlier mail I'd hoped that'd be upstream. And yes, that'd be perfect.
Then userspace applications could switch to Direct I/O like all of the other really serious userspace storage solutions I'm aware of, and then someone could try to write some kind of HDD health monitoring system that tries to do the right thing when a disk is discovered to have developed some media errors or something more serious (e.g., a head failure). That plus some kind of RAID solution is I think the only thing which is really realistic for a typical PG site.
As I said earlier, I think there's good reason to move to DIO for postgres. But to keep that performant is going to need some serious work.
But afaict such a solution wouldn't really depend on applications using DIO or not. Before finishing a checkpoint (logging it persistently and allowing to throw older data away), we could check if any errors have been reported and give up if there have been any. And after starting postgres on a directory restored from backup using $tool, we can fsync the directory recursively, check for such errors, and give up if there've been any.
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 13:24:57 -0700
On 2018-04-12 07:09:14 -0400, Jeff Layton wrote:
On Wed, 2018-04-11 at 20:02 -0700, Matthew Wilcox wrote:
On Wed, Apr 11, 2018 at 07:17:52PM -0700, Andres Freund wrote:
While there's some differing opinions on the referenced postgres thread, the fundamental problem isn't so much that a retry won't fix the problem, it's that we might NEVER see the failure. If writeback happens in the background, encounters an error, undirties the buffer, we will happily carry on because we've never seen that. That's when we're majorly screwed.
I think there are two issues here - "fsync() on an fd that was just opened" and "persistent error state (without keeping dirty pages in memory)".
If there is background data writeback
without an open file descriptor
, there is no mechanism for the kernel to return an error to any application which may exist, or may not ever come back.
And that's
horrible
. If I cp a file, and writeback fails in the background, and I then cat that file before restarting, I should be able to see that that failed. Instead of returning something bogus.
What are you expecting to happen in this case? Are you expecting a read error due to a writeback failure? Or are you just saying that we should be invalidating pages that failed to be written back, so that they can be re-read?
Yes, I'd hope for a read error after a writeback failure. I think that's sane behaviour. But I don't really care
that
much.
At the very least
some
way to
know
that such a failure occurred from userland without having to parse the kernel log. As far as I understand, neither sync(2) (and thus sync(1)) nor syncfs(2) is guaranteed to report an error if it was encountered by writeback in the background.
If that's indeed true for syncfs(2), even if the fd has been opened before (which I can see how it could happen from an implementation POV, nothing would associate a random FD with failures on different files), it's really impossible to detect this stuff from userland without text parsing.
Even if it'd were just a perf-fs /sys/$something file that'd return the current count of unreported errors in a filesystem independent way, it'd be better than what we have right now.
1) figure out /sys/$whatnot $directory belongs to
2) oldcount=$(cat /sys/$whatnot/unreported_errors)
3) filesystem operations in $directory
4) sync;sync;
5) newcount=$(cat /sys/$whatnot/unreported_errors)
6) test "$oldcount" -eq "$newcount" || die-with-horrible-message
Isn't beautiful to script, but it's also not absolutely terrible.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Thu, 12 Apr 2018 13:28:30 -0700
On Thu, Apr 12, 2018 at 01:13:22PM -0700, Andres Freund wrote:
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient.
Ah; this was my suggestion to Jeff on IRC. That we add a per-superblock wb_err and then allow syncfs() to return it. So you'd open an fd on a directory (for example), and call syncfs() which would return -EIO or -ENOSPC if either of those conditions had occurred since you opened the fd.
I don't see that that'd realistically would trigger OOM or the inability to unmount a filesystem.
Ted's referring to the current state of affairs where the writeback error is held in the inode; if we can't evict the inode because it's holding the error indicator, that can send us OOM. If instead we transfer the error indicator to the superblock, then there's no problem.
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 14:11:45 -0700
On 2018-04-12 07:24:12 -0400, Jeff Layton wrote:
On Thu, 2018-04-12 at 15:45 +1000, Dave Chinner wrote:
On Wed, Apr 11, 2018 at 07:32:21PM -0700, Andres Freund wrote:
Hi,
On 2018-04-12 10:09:16 +1000, Dave Chinner wrote: > To pound the broken record: there are many good reasons why Linux > filesystem developers have said "you should use direct IO" to the PG > devs each time we have this "the kernel doesn't do
PG needs>" discussion.
I personally am on board with doing that. But you also gotta recognize that an efficient DIO usage is a metric ton of work, and you need a large amount of differing logic for different platforms. It's just not realistic to do so for every platform. Postgres is developed by a small number of people, isn't VC backed etc. The amount of resources we can throw at something is fairly limited. I'm hoping to work on adding linux DIO support to pg, but I'm sure as hell not going to do be able to do the same on windows (solaris, hpux, aix, ...) etc.
And there's cases where that just doesn't help at all. Being able to untar a database from backup / archive / timetravel / whatnot, and then fsyncing the directory tree to make sure it's actually safe, is really not an insane idea.
Yes it is.
This is what syncfs() is for - making sure a large amount of of data and metadata spread across many files and subdirectories in a single filesystem is pushed to stable storage in the most efficient manner possible.
syncfs isn't standardized, it operates on an entire filesystem (thus writing out unnecessary stuff), it has no meaningful documentation of it's return codes. Yes, using syncfs() might better performancewise, but it doesn't seem like it actually solves anything, performance aside:
Just note that the error return from syncfs is somewhat iffy. It doesn't necessarily return an error when one inode fails to be written back. I think it mainly returns errors when you get a metadata writeback error.
You can still use syncfs but what you'd probably have to do is call syncfs while you still hold all of the fd's open, and then fsync each one afterward to ensure that they all got written back properly. That should work as you'd expect.
Which again doesn't allow one to use any non-bespoke tooling (like tar or whatnot). And it means you'll have to call syncfs() every few hundred files, because you'll obviously run into filehandle limitations.
From:   Jeff Layton <jlayton@...hat.com>
Date:   Thu, 12 Apr 2018 17:14:54 -0400
On Thu, 2018-04-12 at 13:28 -0700, Matthew Wilcox wrote:
On Thu, Apr 12, 2018 at 01:13:22PM -0700, Andres Freund wrote:
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient.
Ah; this was my suggestion to Jeff on IRC. That we add a per- superblock wb_err and then allow syncfs() to return it. So you'd open an fd on a directory (for example), and call syncfs() which would return -EIO or -ENOSPC if either of those conditions had occurred since you opened the fd.
Not a bad idea and shouldn't be too costly. mapping_set_error could flag the superblock one before or after the one in the mapping.
We'd need to define what happens if you interleave fsync and syncfs calls on the same inode though. How do we handle file->f_wb_err in that case? Would we need a second field in struct file to act as the per-sb error cursor?
I don't see that that'd realistically would trigger OOM or the inability to unmount a filesystem.
Ted's referring to the current state of affairs where the writeback error is held in the inode; if we can't evict the inode because it's holding the error indicator, that can send us OOM. If instead we transfer the error indicator to the superblock, then there's no problem.
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Thu, 12 Apr 2018 17:21:44 -0400
On Thu, Apr 12, 2018 at 01:28:30PM -0700, Matthew Wilcox wrote:
On Thu, Apr 12, 2018 at 01:13:22PM -0700, Andres Freund wrote:
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient.
Ah; this was my suggestion to Jeff on IRC. That we add a per-superblock wb_err and then allow syncfs() to return it. So you'd open an fd on a directory (for example), and call syncfs() which would return -EIO or -ENOSPC if either of those conditions had occurred since you opened the fd.
When or how would the per-superblock wb_err flag get cleared?
Would all subsequent fsync() calls on that file system now return EIO? Or would only all subsequent syncfs() calls return EIO?
I don't see that that'd realistically would trigger OOM or the inability to unmount a filesystem.
Ted's referring to the current state of affairs where the writeback error is held in the inode; if we can't evict the inode because it's holding the error indicator, that can send us OOM. If instead we transfer the error indicator to the superblock, then there's no problem.
Actually, I was referring to the pg-hackers original ask, which was that after an error, all of the dirty pages that couldn't be written out would stay dirty.
If it's only as single inode which is pinned in memory with the dirty flag, that's bad, but it's not as bad as pinning all of the memory pages for which there was a failed write. We would still need to invent some mechanism or define some semantic when it would be OK to clear the per-inode flag and let the memory associated with that pinned inode get released, though.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Thu, 12 Apr 2018 14:24:32 -0700
On Thu, Apr 12, 2018 at 05:21:44PM -0400, Theodore Y. Ts'o wrote:
On Thu, Apr 12, 2018 at 01:28:30PM -0700, Matthew Wilcox wrote:
On Thu, Apr 12, 2018 at 01:13:22PM -0700, Andres Freund wrote:
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient.
Ah; this was my suggestion to Jeff on IRC. That we add a per-superblock wb_err and then allow syncfs() to return it. So you'd open an fd on a directory (for example), and call syncfs() which would return -EIO or -ENOSPC if either of those conditions had occurred since you opened the fd.
When or how would the per-superblock wb_err flag get cleared?
That's not how errseq works, Ted ;-)
Would all subsequent fsync() calls on that file system now return EIO? Or would only all subsequent syncfs() calls return EIO?
Only ones which occur after the last sampling get reported through this particular file descriptor.
From:   Jeff Layton <jlayton@...hat.com>
Date:   Thu, 12 Apr 2018 17:27:54 -0400
On Thu, 2018-04-12 at 13:24 -0700, Andres Freund wrote:
On 2018-04-12 07:09:14 -0400, Jeff Layton wrote:
On Wed, 2018-04-11 at 20:02 -0700, Matthew Wilcox wrote:
On Wed, Apr 11, 2018 at 07:17:52PM -0700, Andres Freund wrote:
While there's some differing opinions on the referenced postgres thread, the fundamental problem isn't so much that a retry won't fix the problem, it's that we might NEVER see the failure. If writeback happens in the background, encounters an error, undirties the buffer, we will happily carry on because we've never seen that. That's when we're majorly screwed.
I think there are two issues here - "fsync() on an fd that was just opened" and "persistent error state (without keeping dirty pages in memory)".
If there is background data writeback
without an open file descriptor
, there is no mechanism for the kernel to return an error to any application which may exist, or may not ever come back.
And that's
horrible
. If I cp a file, and writeback fails in the background, and I then cat that file before restarting, I should be able to see that that failed. Instead of returning something bogus.
What are you expecting to happen in this case? Are you expecting a read error due to a writeback failure? Or are you just saying that we should be invalidating pages that failed to be written back, so that they can be re-read?
Yes, I'd hope for a read error after a writeback failure. I think that's sane behaviour. But I don't really care
that
much.
I'll have to respectfully disagree. Why should I interpret an error on a read() syscall to mean that writeback failed? Note that the data is still potentially intact.
What
might
make sense, IMO, is to just invalidate the pages that failed to be written back. Then you could potentially do a read to fault them in again (i.e. sync the pagecache and the backing store) and possibly redirty them for another try.
Note that you can detect this situation by checking the return code from fsync. It should report the latest error once per file description.
At the very least
some
way to
know
that such a failure occurred from userland without having to parse the kernel log. As far as I understand, neither sync(2) (and thus sync(1)) nor syncfs(2) is guaranteed to report an error if it was encountered by writeback in the background.
If that's indeed true for syncfs(2), even if the fd has been opened before (which I can see how it could happen from an implementation POV, nothing would associate a random FD with failures on different files), it's really impossible to detect this stuff from userland without text parsing.
syncfs could use some work.
I'm warming to willy's idea to add a per-sb errseq_t. I think that might be a simple way to get better semantics here. Not sure how we want to handle the reporting end yet though...
We probably also need to consider how to better track metadata writeback errors (on e.g. ext2). We don't really do that properly at quite yet either.
Even if it'd were just a perf-fs /sys/$something file that'd return the current count of unreported errors in a filesystem independent way, it'd be better than what we have right now.
1) figure out /sys/$whatnot $directory belongs to 2) oldcount=$(cat /sys/$whatnot/unreported_errors) 3) filesystem operations in $directory 4) sync;sync; 5) newcount=$(cat /sys/$whatnot/unreported_errors) 6) test "$oldcount" -eq "$newcount" || die-with-horrible-message
Isn't beautiful to script, but it's also not absolutely terrible.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Thu, 12 Apr 2018 14:31:10 -0700
On Thu, Apr 12, 2018 at 05:14:54PM -0400, Jeff Layton wrote:
On Thu, 2018-04-12 at 13:28 -0700, Matthew Wilcox wrote:
On Thu, Apr 12, 2018 at 01:13:22PM -0700, Andres Freund wrote:
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient.
Ah; this was my suggestion to Jeff on IRC. That we add a per- superblock wb_err and then allow syncfs() to return it. So you'd open an fd on a directory (for example), and call syncfs() which would return -EIO or -ENOSPC if either of those conditions had occurred since you opened the fd.
Not a bad idea and shouldn't be too costly. mapping_set_error could flag the superblock one before or after the one in the mapping.
We'd need to define what happens if you interleave fsync and syncfs calls on the same inode though. How do we handle file->f_wb_err in that case? Would we need a second field in struct file to act as the per-sb error cursor?
Ooh. I hadn't thought that through. Bleh. I don't want to add a field to struct file for this uncommon case.
Maybe O_PATH could be used for this? It gets you a file descriptor on a particular filesystem, so syncfs() is defined, but it can't report a writeback error. So if you open something O_PATH, you can use the file's f_wb_err for the mapping's error cursor.
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 14:37:56 -0700
On 2018-04-12 17:21:44 -0400, Theodore Y. Ts'o wrote:
On Thu, Apr 12, 2018 at 01:28:30PM -0700, Matthew Wilcox wrote:
On Thu, Apr 12, 2018 at 01:13:22PM -0700, Andres Freund wrote:
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient.
Ah; this was my suggestion to Jeff on IRC. That we add a per-superblock wb_err and then allow syncfs() to return it. So you'd open an fd on a directory (for example), and call syncfs() which would return -EIO or -ENOSPC if either of those conditions had occurred since you opened the fd.
When or how would the per-superblock wb_err flag get cleared?
I don't think unmount + resettable via /sys would be an insane approach. Requiring explicit action to acknowledge data loss isn't a crazy concept. But I think that's something reasonable minds could disagree with.
Would all subsequent fsync() calls on that file system now return EIO? Or would only all subsequent syncfs() calls return EIO?
If it were tied to syncfs, I wonder if there's a way to have some errseq type logic. Store a per superblock (or whatever equivalent thing) errseq value of errors. For each fd calling syncfs() report the error once, but then store the current value in a separate per-fd field. And if that's considered too weird, only report the errors to fds that have been opened from before the error occurred.
I can see writing a tool 'pg_run_and_sync /directo /ries -- command' which opens an fd for each of the filesystems the directories reside on, and calls syncfs() after. That'd allow to use backup/restore tools at least semi safely.
I don't see that that'd realistically would trigger OOM or the inability to unmount a filesystem.
Ted's referring to the current state of affairs where the writeback error is held in the inode; if we can't evict the inode because it's holding the error indicator, that can send us OOM. If instead we transfer the error indicator to the superblock, then there's no problem.
Actually, I was referring to the pg-hackers original ask, which was that after an error, all of the dirty pages that couldn't be written out would stay dirty.
Well, it's an open list, everyone can argue. And initially people at first didn't know the OOM explanation, and then it takes some time to revise ones priors :). I think it's a design question that reasonable people can disagree upon (if "hot" removed devices are handled by throwing data away regardless, at least). But as it's clearly not something viable, we can move on to something that can solve the problem.
If it's only as single inode which is pinned in memory with the dirty flag, that's bad, but it's not as bad as pinning all of the memory pages for which there was a failed write. We would still need to invent some mechanism or define some semantic when it would be OK to clear the per-inode flag and let the memory associated with that pinned inode get released, though.
Yea, I agree that that's not obvious. One way would be to say that it's only automatically cleared when you unlink the file. A bit heavyhanded, but not too crazy.
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Thu, 12 Apr 2018 17:52:52 -0400
On Thu, Apr 12, 2018 at 12:55:36PM -0700, Andres Freund wrote:
Any pointers to that the underling netlink mechanism? If we can force postgres to kill itself when such an error is detected (via a dedicated monitoring process), I'd personally be happy enough. It'd be nicer if we could associate that knowledge with particular filesystems etc (which'd possibly hard through dm etc?), but this'd be much better than nothing.
Yeah, sorry, it never got upstreamed. It's not really all that complicated, it was just that there were some other folks who wanted to do something similar, and there was a round of bike-sheddingh several years ago, and nothing ever went upstream. Part of the problem was that our orignial scheme sent up information about file system-level corruption reports --- e.g, those stemming from calls to ext4_error() --- and lots of people had different ideas about how tot get all of the possible information up in some structured format. (Think something like uerf from Digtial's OSF/1.)
We did something
really
simple/stupid. We just sent essentially an ascii test string out the netlink socket. That's because what we were doing before was essentially scraping the output of dmesg (e.g. /dev/kmssg).
That's actually probably the simplest thing to do, and it has the advantage that it will work even on ancient enterprise kernels that PG users are likely to want to use. So you will need to implement the dmesg text scraper anyway, and that's probably good enough for most use cases.
The problem really isn't about
recovering
from disk errors.
Knowing
about them is the crucial part. We do not want to give back clients the information that an operation succeeded, when it actually didn't. There could be improvements above that, but as long as it's guaranteed that "we" get the error (rather than just some kernel log we don't have access to, which looks different due to config etc), it's ok. We can throw our hands up in the air and give up.
Right, it's a little challenging because the actual regexp's you would need to use do vary from device driver to device driver. Fortunately nearly everything is a SCSI/SATA device these days, so there isn't
that
much variability.
Yea, agreed on all that. I don't think anybody actually involved in postgres wants to do anything like that. Seems far outside of postgres' remit.
Some people on the pg-hackers list were talking about wanting to retry the fsync() and hoping that would cause the write to somehow suceed. It's
possible
that might help, but it's not likely to be helpful in my experience.
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 14:53:19 -0700
On 2018-04-12 17:27:54 -0400, Jeff Layton wrote:
On Thu, 2018-04-12 at 13:24 -0700, Andres Freund wrote:
At the very least
some
way to
know
that such a failure occurred from userland without having to parse the kernel log. As far as I understand, neither sync(2) (and thus sync(1)) nor syncfs(2) is guaranteed to report an error if it was encountered by writeback in the background.
If that's indeed true for syncfs(2), even if the fd has been opened before (which I can see how it could happen from an implementation POV, nothing would associate a random FD with failures on different files), it's really impossible to detect this stuff from userland without text parsing.
syncfs could use some work.
It's really too bad that it doesn't have a flags argument.
We probably also need to consider how to better track metadata writeback errors (on e.g. ext2). We don't really do that properly at quite yet either.
Even if it'd were just a perf-fs /sys/$something file that'd return the current count of unreported errors in a filesystem independent way, it'd be better than what we have right now.
1) figure out /sys/$whatnot $directory belongs to 2) oldcount=$(cat /sys/$whatnot/unreported_errors) 3) filesystem operations in $directory 4) sync;sync; 5) newcount=$(cat /sys/$whatnot/unreported_errors) 6) test "$oldcount" -eq "$newcount" || die-with-horrible-message
Isn't beautiful to script, but it's also not absolutely terrible.
ext4 seems to have something roughly like that (/sys/fs/ext4/$dev/errors_count), and by my reading it already seems to be incremented from the necessary places. By my reading XFS doesn't seem to have something similar.
Wouldn't be bad to standardize...
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Thu, 12 Apr 2018 17:57:56 -0400
On Thu, Apr 12, 2018 at 02:53:19PM -0700, Andres Freund wrote:
Isn't beautiful to script, but it's also not absolutely terrible.
ext4 seems to have something roughly like that (/sys/fs/ext4/$dev/errors_count), and by my reading it already seems to be incremented from the necessary places.
This is only for file system inconsistencies noticed by the kernel. We don't bump that count for data block I/O errors.
The same idea could be used on a block device level. It would be pretty simple to maintain a counter for I/O errors, and when the last error was detected on a particular device. You could evne break out and track read errors and write errors eparately if that would be useful.
If you don't care what block was bad, but just that
some
I/O error had happened, a counter is definitely the simplest approach, and less hair to implemnet and use than something like a netlink channel or scraping dmesg....
From:   Andres Freund <andres@...razel.de>
Date:   Thu, 12 Apr 2018 15:03:59 -0700
Hi,
On 2018-04-12 17:52:52 -0400, Theodore Y. Ts'o wrote:
We did something
really
simple/stupid. We just sent essentially an ascii test string out the netlink socket. That's because what we were doing before was essentially scraping the output of dmesg (e.g. /dev/kmssg).
That's actually probably the simplest thing to do, and it has the advantage that it will work even on ancient enterprise kernels that PG users are likely to want to use. So you will need to implement the dmesg text scraper anyway, and that's probably good enough for most use cases.
The worst part of that is, as you mention below, needing to handle a lot of different error message formats. I guess it's reasonable enough if you control your hardware, but no such luck.
Aren't there quite realistic scenarios where one could miss kmsg style messages due to it being a ringbuffer?
Right, it's a little challenging because the actual regexp's you would need to use do vary from device driver to device driver. Fortunately nearly everything is a SCSI/SATA device these days, so there isn't
that
much variability.
There's also SAN / NAS type stuff - not all of that presents as a SCSI/SATA device, right?
Yea, agreed on all that. I don't think anybody actually involved in postgres wants to do anything like that. Seems far outside of postgres' remit.
Some people on the pg-hackers list were talking about wanting to retry the fsync() and hoping that would cause the write to somehow suceed. It's
possible
that might help, but it's not likely to be helpful in my experience.
Depends on the type of error and storage. ENOSPC, especially over NFS, has some reasonable chances of being cleared up. And for networked block storage it's also not impossible to think of scenarios where that'd work for EIO.
But I think besides hope of clearing up itself, it has the advantage that it trivially can give
some
feedback to the user. The user'll get back strerror(ENOSPC) with some decent SQL error code, which'll hopefully cause them to investigate (well, once monitoring detects high error rates). It's much nicer for the user to type COMMIT; get an appropriate error back etc, than if the database just commits suicide.
From:   Dave Chinner <david@...morbit.com>
Date:   Fri, 13 Apr 2018 08:44:04 +1000
On Thu, Apr 12, 2018 at 11:08:50AM -0400, Jeff Layton wrote:
On Thu, 2018-04-12 at 22:01 +1000, Dave Chinner wrote:
On Thu, Apr 12, 2018 at 07:09:14AM -0400, Jeff Layton wrote:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
There isn't a right thing. Whatever we do will be wrong for someone.
One possibility would be to invalidate the range that failed to be written (or the whole file) and force the pages to be faulted in again on the next access. It could be surprising for some applications to not see the results of their writes on a subsequent read after such an event.
Not to mention a POSIX IO ordering violation. Seeing stale data after a "successful" write is simply not allowed.
I'm not so sure here, given that we're dealing with an error condition. Are we really obligated not to allow any changes to pages that we can't write back?
Posix says this about write():
After a write() to a regular file has successfully returned:

     Any successful read() from each byte position in the file that
     was modified by that write shall return the data specified by
     the write() for that position until such byte positions are
     again modified.
IOWs, even if there is a later error, we told the user the write was successful, and so according to POSIX we are not allowed to wind back the data to what it was before the write() occurred.
Given that the pages are clean after these failures, we aren't doing this even today:
Suppose we're unable to do writes but can do reads vs. the backing store. After a wb failure, the page has the dirty bit cleared. If it gets kicked out of the cache before the read occurs, it'll have to be faulted back in. Poof -- your write just disappeared.
Yes - I was pointing out what the specification we supposedly conform to says about this behaviour, not that our current behaviour conforms to the spec. Indeed, have you even noticed xfs_aops_discard_page() and it's surrounding context on page writeback submission errors?
To save you looking, XFS will trash the page contents completely on a filesystem level ->writepage error. It doesn't mark them "clean", doesn't attempt to redirty and rewrite them - it clears the uptodate state and may invalidate it completely. IOWs, the data written "sucessfully" to the cached page is now gone. It will be re-read from disk on the next read() call, in direct violation of the above POSIX requirements.
This is my point: we've done that in XFS knowing that we violate POSIX specifications in this specific corner case - it's the lesser of many evils we have to chose between. Hence if we chose to encode that behaviour as the general writeback IO error handling algorithm, then it needs to done with the knowledge it is a specification violation. Not to mention be documented as a POSIX violation in the various relevant man pages and that this is how all filesystems will behave on async writeback error.....
From:   Jeff Layton <jlayton@...hat.com>
Date:   Fri, 13 Apr 2018 08:56:38 -0400
On Thu, 2018-04-12 at 14:31 -0700, Matthew Wilcox wrote:
On Thu, Apr 12, 2018 at 05:14:54PM -0400, Jeff Layton wrote:
On Thu, 2018-04-12 at 13:28 -0700, Matthew Wilcox wrote:
On Thu, Apr 12, 2018 at 01:13:22PM -0700, Andres Freund wrote:
I think a per-file or even per-blockdev/fs error state that'd be returned by fsync() would be more than sufficient.
Ah; this was my suggestion to Jeff on IRC. That we add a per- superblock wb_err and then allow syncfs() to return it. So you'd open an fd on a directory (for example), and call syncfs() which would return -EIO or -ENOSPC if either of those conditions had occurred since you opened the fd.
Not a bad idea and shouldn't be too costly. mapping_set_error could flag the superblock one before or after the one in the mapping.
We'd need to define what happens if you interleave fsync and syncfs calls on the same inode though. How do we handle file->f_wb_err in that case? Would we need a second field in struct file to act as the per-sb error cursor?
Ooh. I hadn't thought that through. Bleh. I don't want to add a field to struct file for this uncommon case.
Maybe O_PATH could be used for this? It gets you a file descriptor on a particular filesystem, so syncfs() is defined, but it can't report a writeback error. So if you open something O_PATH, you can use the file's f_wb_err for the mapping's error cursor.
That might work.
It'd be a syscall behavioral change so we'd need to document that well. It's probably innocuous though -- I doubt we have a lot of callers in the field opening files with O_PATH and calling syncfs on them.
From:   Jeff Layton <jlayton@...hat.com>
Date:   Fri, 13 Apr 2018 09:18:56 -0400
On Fri, 2018-04-13 at 08:44 +1000, Dave Chinner wrote:
On Thu, Apr 12, 2018 at 11:08:50AM -0400, Jeff Layton wrote:
On Thu, 2018-04-12 at 22:01 +1000, Dave Chinner wrote:
On Thu, Apr 12, 2018 at 07:09:14AM -0400, Jeff Layton wrote:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
There isn't a right thing. Whatever we do will be wrong for someone.
One possibility would be to invalidate the range that failed to be written (or the whole file) and force the pages to be faulted in again on the next access. It could be surprising for some applications to not see the results of their writes on a subsequent read after such an event.
Not to mention a POSIX IO ordering violation. Seeing stale data after a "successful" write is simply not allowed.
I'm not so sure here, given that we're dealing with an error condition. Are we really obligated not to allow any changes to pages that we can't write back?
Posix says this about write():
After a write() to a regular file has successfully returned:
Any successful read() from each byte position in the file that
 was modified by that write shall return the data specified by
 the write() for that position until such byte positions are
 again modified.
IOWs, even if there is a later error, we told the user the write was successful, and so according to POSIX we are not allowed to wind back the data to what it was before the write() occurred.
Given that the pages are clean after these failures, we aren't doing this even today:
Suppose we're unable to do writes but can do reads vs. the backing store. After a wb failure, the page has the dirty bit cleared. If it gets kicked out of the cache before the read occurs, it'll have to be faulted back in. Poof -- your write just disappeared.
Yes - I was pointing out what the specification we supposedly conform to says about this behaviour, not that our current behaviour conforms to the spec. Indeed, have you even noticed xfs_aops_discard_page() and it's surrounding context on page writeback submission errors?
To save you looking, XFS will trash the page contents completely on a filesystem level ->writepage error. It doesn't mark them "clean", doesn't attempt to redirty and rewrite them - it clears the uptodate state and may invalidate it completely. IOWs, the data written "sucessfully" to the cached page is now gone. It will be re-read from disk on the next read() call, in direct violation of the above POSIX requirements.
This is my point: we've done that in XFS knowing that we violate POSIX specifications in this specific corner case - it's the lesser of many evils we have to chose between. Hence if we chose to encode that behaviour as the general writeback IO error handling algorithm, then it needs to done with the knowledge it is a specification violation. Not to mention be documented as a POSIX violation in the various relevant man pages and that this is how all filesystems will behave on async writeback error.....
Got it, thanks.
Yes, I think we ought to probably do the same thing globally. It's nice to know that xfs has already been doing this. That makes me feel better about making this behavior the gold standard for Linux filesystems.
So to summarize, at this point in the discussion, I think we want to consider doing the following:
better reporting from syncfs (report an error when even one inode failed to be written back since last syncfs call). We'll probably implement this via a per-sb errseq_t in some fashion, though there are some implementation issues to work out.
invalidate or clear uptodate flag on pages that experience writeback errors, across filesystems. Encourage this as standard behavior for filesystems and maybe add helpers to make it easier to do this.
Did I miss anything? Would that be enough to help the Pg usecase?
I don't see us ever being able to reasonably support its current expectation that writeback errors will be seen on fd's that were opened after the error occurred. That's a really thorny problem from an object lifetime perspective.
From:   Andres Freund <andres@...razel.de>
Date:   Fri, 13 Apr 2018 06:25:35 -0700
Hi,
On 2018-04-13 09:18:56 -0400, Jeff Layton wrote:
Yes, I think we ought to probably do the same thing globally. It's nice to know that xfs has already been doing this. That makes me feel better about making this behavior the gold standard for Linux filesystems.
So to summarize, at this point in the discussion, I think we want to consider doing the following:
better reporting from syncfs (report an error when even one inode failed to be written back since last syncfs call). We'll probably implement this via a per-sb errseq_t in some fashion, though there are some implementation issues to work out.
invalidate or clear uptodate flag on pages that experience writeback errors, across filesystems. Encourage this as standard behavior for filesystems and maybe add helpers to make it easier to do this.
Did I miss anything? Would that be enough to help the Pg usecase?
I don't see us ever being able to reasonably support its current expectation that writeback errors will be seen on fd's that were opened after the error occurred. That's a really thorny problem from an object lifetime perspective.
It's not perfect, but I think the amount of hacky OS specific code should be acceptable. And it does allow for a wrapper tool that can be used around backup restores etc to syncfs all the necessary filesystems. Let me mull with others for a bit.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Fri, 13 Apr 2018 07:02:32 -0700
On Fri, Apr 13, 2018 at 09:18:56AM -0400, Jeff Layton wrote:
On Fri, 2018-04-13 at 08:44 +1000, Dave Chinner wrote:
To save you looking, XFS will trash the page contents completely on a filesystem level ->writepage error. It doesn't mark them "clean", doesn't attempt to redirty and rewrite them - it clears the uptodate state and may invalidate it completely. IOWs, the data written "sucessfully" to the cached page is now gone. It will be re-read from disk on the next read() call, in direct violation of the above POSIX requirements.
This is my point: we've done that in XFS knowing that we violate POSIX specifications in this specific corner case - it's the lesser of many evils we have to chose between. Hence if we chose to encode that behaviour as the general writeback IO error handling algorithm, then it needs to done with the knowledge it is a specification violation. Not to mention be documented as a POSIX violation in the various relevant man pages and that this is how all filesystems will behave on async writeback error.....
Got it, thanks.
Yes, I think we ought to probably do the same thing globally. It's nice to know that xfs has already been doing this. That makes me feel better about making this behavior the gold standard for Linux filesystems.
So to summarize, at this point in the discussion, I think we want to consider doing the following:
better reporting from syncfs (report an error when even one inode failed to be written back since last syncfs call). We'll probably implement this via a per-sb errseq_t in some fashion, though there are some implementation issues to work out.
invalidate or clear uptodate flag on pages that experience writebackerrors, across filesystems. Encourage this as standard behavior for filesystems and maybe add helpers to make it easier to do this.
Did I miss anything? Would that be enough to help the Pg usecase?
I don't see us ever being able to reasonably support its current expectation that writeback errors will be seen on fd's that were opened after the error occurred. That's a really thorny problem from an object lifetime perspective.
I think we can do better than XFS is currently doing (but I agree that we should have the same behaviour across all Linux filesystems!)
If we get an error while wbc->for_background is true, we should not clear uptodate on the page, rather SetPageError and SetPageDirty.
Background writebacks should skip pages which are PageError.
for_sync writebacks should attempt one last write. Maybe it'll succeed this time. If it does, just ClearPageError. If not, we have somebody to report this writeback error to, and ClearPageUptodate.
I think kupdate writes are the same as for_background writes. for_reclaim is tougher. I don't want to see us getting into OOM because we're hanging onto stale data, but we don't necessarily have an open fd to report the error on. I think I'm leaning towards behaving the same for for_reclaim as for_sync, but this is probably a subject on which reasonable people can disagree.
And this logic all needs to be on one place, although invoked from each filesystem.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Fri, 13 Apr 2018 07:48:07 -0700
On Tue, Apr 10, 2018 at 03:07:26PM -0700, Andres Freund wrote:
I don't think that's the full issue. We can deal with the fact that an fsync failure is edge-triggered if there's a guarantee that every process doing so would get it. The fact that one needs to have an FD open from before any failing writes occurred to get a failure,
THAT'S
the big issue.
Beyond postgres, it's a pretty common approach to do work on a lot of files without fsyncing, then iterate over the directory fsync everything, and
then
assume you're safe. But unless I severaly misunderstand something that'd only be safe if you kept an FD for every file open, which isn't realistic for pretty obvious reasons.
While accepting that under memory pressure we can still evict the error indicators, we can do a better job than we do today. The current design of error reporting says that all errors which occurred before you opened the file descriptor are of no interest to you. I don't think that's necessarily true, and it's actually a change of behaviour from before the errseq work.
Consider Stupid Task A which calls open(), write(), close(), and Smart Task B which calls open(), write(), fsync(), close() operating on the same file. If A goes entirely before B and encounters an error, before errseq_t, B would see the error from A's write.
If A and B overlap, even a little bit, then B still gets to see A's error today. But if writeback happens for A's write before B opens the file then B will never see the error.
B doesn't want to see historical errors that a previous invocation of B has already handled, but we know whether
anyone
has seen the error or not. So here's a patch which restores the historical behaviour of seeing old unhandled errors on a fresh file descriptor:
Signed-off-by: Matthew Wilcox
mawilcox@...rosoft.com
diff --git a/lib/errseq.c b/lib/errseq.c
index df782418b333..093f1fba4ee0 100644
--- a/lib/errseq.c
+++ b/lib/errseq.c
@@ -119,19 +119,11 @@ EXPORT_SYMBOL(errseq_set);
 errseq_t errseq_sample(errseq_t *eseq)
 {
 	errseq_t old = READ_ONCE(*eseq);
-	errseq_t new = old;
 
-	/*
-	 * For the common case of no errors ever having been set, we can skip
-	 * marking the SEEN bit. Once an error has been set, the value will
-	 * never go back to zero.
-	 */
-	if (old != 0) {
-		new |= ERRSEQ_SEEN;
-		if (old != new)
-			cmpxchg(eseq, old, new);
-	}
-	return new;
+	/* If nobody has seen this error yet, then we can be the first. */
+	if (!(old & ERRSEQ_SEEN))
+		old = 0;
+	return old;
 }
 EXPORT_SYMBOL(errseq_sample);
From:   Dave Chinner <david@...morbit.com>
Date:   Sat, 14 Apr 2018 11:47:52 +1000
On Fri, Apr 13, 2018 at 07:02:32AM -0700, Matthew Wilcox wrote:
On Fri, Apr 13, 2018 at 09:18:56AM -0400, Jeff Layton wrote:
On Fri, 2018-04-13 at 08:44 +1000, Dave Chinner wrote:
To save you looking, XFS will trash the page contents completely on a filesystem level ->writepage error. It doesn't mark them "clean", doesn't attempt to redirty and rewrite them - it clears the uptodate state and may invalidate it completely. IOWs, the data written "sucessfully" to the cached page is now gone. It will be re-read from disk on the next read() call, in direct violation of the above POSIX requirements.
This is my point: we've done that in XFS knowing that we violate POSIX specifications in this specific corner case - it's the lesser of many evils we have to chose between. Hence if we chose to encode that behaviour as the general writeback IO error handling algorithm, then it needs to done with the knowledge it is a specification violation. Not to mention be documented as a POSIX violation in the various relevant man pages and that this is how all filesystems will behave on async writeback error.....
Got it, thanks.
Yes, I think we ought to probably do the same thing globally. It's nice to know that xfs has already been doing this. That makes me feel better about making this behavior the gold standard for Linux filesystems.
So to summarize, at this point in the discussion, I think we want to consider doing the following:
better reporting from syncfs (report an error when even one inode failed to be written back since last syncfs call). We'll probably implement this via a per-sb errseq_t in some fashion, though there are some implementation issues to work out.
invalidate or clear uptodate flag on pages that experience writeback errors, across filesystems. Encourage this as standard behavior for filesystems and maybe add helpers to make it easier to do this.
Did I miss anything? Would that be enough to help the Pg usecase?
I don't see us ever being able to reasonably support its current expectation that writeback errors will be seen on fd's that were opened after the error occurred. That's a really thorny problem from an object lifetime perspective.
I think we can do better than XFS is currently doing (but I agree that we should have the same behaviour across all Linux filesystems!)
If we get an error while wbc->for_background is true, we should not clear uptodate on the page, rather SetPageError and SetPageDirty.
So you're saying we should treat it as a transient error rather than a permanent error.
Background writebacks should skip pages which are PageError.
That seems decidedly dodgy in the case where there is a transient error - it requires a user to specifically run sync to get the data to disk after the transient error has occurred. Say they don't notice the problem because it's fleeting and doesn't cause any obvious problems?
e.g. XFS gets to enospc, runs out of reserve pool blocks so can't allocate space to write back the page, then space is freed up a few seconds later and so the next write will work just fine.
This is a recipe for "I lost data that I wrote /days/ before the system crashed" bug reports.
for_sync writebacks should attempt one last write. Maybe it'll succeed this time. If it does, just ClearPageError. If not, we have somebody to report this writeback error to, and ClearPageUptodate.
Which may well be unmount. Are we really going to wait until unmount to report fatal errors?
We used to do this with XFS metadata. We'd just keep trying to write metadata and keep the filesystem running (because it's consistent in memory and it might be a transient error) rather than shutting down the filesystem after a couple of retries. the result was that users wouldn't notice there were problems until unmount, and the most common sympton of that was "why is system shutdown hanging?".
We now don't hang at unmount by default:
$ cat /sys/fs/xfs/dm-0/error/fail_at_unmount 
1
$
And we treat different errors according to their seriousness. EIO and device ENOSPC we default to retry forever because they are often transient, but for ENODEV we fail and shutdown immediately (someone pulled the USB stick out). metadata failure behaviour is configured via changing fields in /sys/fs/xfs/
/error/metadata/
/...
We've planned to extend this failure configuration to data IO, too, but never quite got around to it yet. this is a clear example of "one size doesn't fit all" and I think we'll end up doing the same sort of error behaviour configuration in XFS for these cases. (i.e. /sys/fs/xfs/
/error/writeback/
/....)
And this logic all needs to be on one place, although invoked from each filesystem.
Perhaps so, but as there's no "one-size-fits-all" behaviour, I really want to extend the XFS error config infrastructure to control what the filesystem does on error here.
From:   Andres Freund <andres@...razel.de>
Date:   Fri, 13 Apr 2018 19:04:33 -0700
Hi,
On 2018-04-14 11:47:52 +1000, Dave Chinner wrote:
And we treat different errors according to their seriousness. EIO and device ENOSPC we default to retry forever because they are often transient, but for ENODEV we fail and shutdown immediately (someone pulled the USB stick out). metadata failure behaviour is configured via changing fields in /sys/fs/xfs/
/error/metadata/
/...
We've planned to extend this failure configuration to data IO, too, but never quite got around to it yet. this is a clear example of "one size doesn't fit all" and I think we'll end up doing the same sort of error behaviour configuration in XFS for these cases. (i.e. /sys/fs/xfs/
/error/writeback/
/....)
Have you considered adding an ext/fat/jfs errors=remount-ro/panic/continue style mount parameter?
From:   Matthew Wilcox <willy@...radead.org>
Date:   Fri, 13 Apr 2018 19:38:14 -0700
On Sat, Apr 14, 2018 at 11:47:52AM +1000, Dave Chinner wrote:
On Fri, Apr 13, 2018 at 07:02:32AM -0700, Matthew Wilcox wrote:
If we get an error while wbc->for_background is true, we should not clear uptodate on the page, rather SetPageError and SetPageDirty.
So you're saying we should treat it as a transient error rather than a permanent error.
Yes, I'm proposing leaving the data in memory in case the user wants to try writing it somewhere else.
Background writebacks should skip pages which are PageError.
That seems decidedly dodgy in the case where there is a transient error - it requires a user to specifically run sync to get the data to disk after the transient error has occurred. Say they don't notice the problem because it's fleeting and doesn't cause any obvious problems?
That's fair. What I want to avoid is triggering the same error every 30 seconds (or whatever the periodic writeback threshold is set to).
e.g. XFS gets to enospc, runs out of reserve pool blocks so can't allocate space to write back the page, then space is freed up a few seconds later and so the next write will work just fine.
This is a recipe for "I lost data that I wrote /days/ before the system crashed" bug reports.
So ... exponential backoff on retries?
for_sync writebacks should attempt one last write. Maybe it'll succeed this time. If it does, just ClearPageError. If not, we have somebody to report this writeback error to, and ClearPageUptodate.
Which may well be unmount. Are we really going to wait until unmount to report fatal errors?
Goodness, no. The errors would be immediately reportable using the wb_err mechanism, as soon as the first error was encountered.
From:   bfields@...ldses.org (J. Bruce Fields)
Date:   Wed, 18 Apr 2018 12:52:19 -0400
Theodore Y. Ts'o - 10.04.18, 20:43:
First of all, what storage devices will do when they hit an exception condition is quite non-deterministic. For example, the vast majority of SSD's are not power fail certified. What this means is that if they suffer a power drop while they are doing a GC, it is quite possible for data written six months ago to be lost as a result. The LBA could potentialy be far, far away from any LBA's that were recently written, and there could have been multiple CACHE FLUSH operations in the since the LBA in question was last written six months ago. No matter; for a consumer-grade SSD, it's possible for that LBA to be trashed after an unexpected power drop.
Pointers to documentation or papers or anything? The only google results I can find for "power fail certified" are your posts.
I've always been confused by SSD power-loss protection, as nobody seems completely clear whether it's a safety or a performance feature.
From:   bfields@...ldses.org (J. Bruce Fields)
Date:   Wed, 18 Apr 2018 14:09:03 -0400
On Wed, Apr 11, 2018 at 07:17:52PM -0700, Andres Freund wrote:
Hi,
On 2018-04-11 15:52:44 -0600, Andreas Dilger wrote:
On Apr 10, 2018, at 4:07 PM, Andres Freund
andres@...razel.de
wrote:
2018-04-10 18:43:56 Ted wrote:
So for better or for worse, there has not been as much investment in buffered I/O and data robustness in the face of exception handling of storage devices.
That's a bit of a cop out. It's not just databases that care. Even more basic tools like SCM, package managers and editors care whether they can proper responses back from fsync that imply things actually were synced.
Sure, but it is mostly PG that is doing (IMHO) crazy things like writing to thousands(?) of files, closing the file descriptors, then expecting fsync() on a newly-opened fd to return a historical error.
It's not just postgres. dpkg (underlying apt, on debian derived distros) to take an example I just randomly guessed, does too: /* We want to guarantee the extracted files are on the disk, so that the * subsequent renames to the info database do not end up with old or zero * length files in case of a system crash. As neither dpkg-deb nor tar do * explicit fsync()s, we have to do them here. * XXX: This could be avoided by switching to an internal tar extractor. */ dir_sync_contents(cidir);
(a bunch of other places too)
Especially on ext3 but also on newer filesystems it's performancewise entirely infeasible to fsync() every single file individually - the performance becomes entirely attrocious if you do that.
Is that still true if you're able to use some kind of parallelism? (async io, or fsync from multiple processes?)
From:   Dave Chinner <david@...morbit.com>
Date:   Thu, 19 Apr 2018 09:59:50 +1000
On Fri, Apr 13, 2018 at 07:04:33PM -0700, Andres Freund wrote:
Hi,
On 2018-04-14 11:47:52 +1000, Dave Chinner wrote:
And we treat different errors according to their seriousness. EIO and device ENOSPC we default to retry forever because they are often transient, but for ENODEV we fail and shutdown immediately (someone pulled the USB stick out). metadata failure behaviour is configured via changing fields in /sys/fs/xfs/
/error/metadata/
/...
We've planned to extend this failure configuration to data IO, too, but never quite got around to it yet. this is a clear example of "one size doesn't fit all" and I think we'll end up doing the same sort of error behaviour configuration in XFS for these cases. (i.e. /sys/fs/xfs/
/error/writeback/
/....)
Have you considered adding an ext/fat/jfs errors=remount-ro/panic/continue style mount parameter?
That's for metadata writeback error behaviour, not data writeback IO errors.
We are definitely not planning to add mount options to configure IO error behaviors. Mount options are a horrible way to configure filesystem behaviour and we've already got other, fine-grained configuration infrastructure for configuring IO error behaviour. Which, as I just pointed out, was designed to be be extended to data writeback and other operational error handling in the filesystem (e.g. dealing with ENOMEM in different ways).
From:   Dave Chinner <david@...morbit.com>
Date:   Thu, 19 Apr 2018 10:13:43 +1000
On Fri, Apr 13, 2018 at 07:38:14PM -0700, Matthew Wilcox wrote:
On Sat, Apr 14, 2018 at 11:47:52AM +1000, Dave Chinner wrote:
On Fri, Apr 13, 2018 at 07:02:32AM -0700, Matthew Wilcox wrote:
If we get an error while wbc->for_background is true, we should not clear uptodate on the page, rather SetPageError and SetPageDirty.
So you're saying we should treat it as a transient error rather than a permanent error.
Yes, I'm proposing leaving the data in memory in case the user wants to try writing it somewhere else.
And if it's getting IO errors because of USB stick pull? What then?
Background writebacks should skip pages which are PageError.
That seems decidedly dodgy in the case where there is a transient error - it requires a user to specifically run sync to get the data to disk after the transient error has occurred. Say they don't notice the problem because it's fleeting and doesn't cause any obvious problems?
That's fair. What I want to avoid is triggering the same error every 30 seconds (or whatever the periodic writeback threshold is set to).
So if kernel ring buffer overflows and so users miss the first error report, they'll have no idea that the data writeback is still failing?
e.g. XFS gets to enospc, runs out of reserve pool blocks so can't allocate space to write back the page, then space is freed up a few seconds later and so the next write will work just fine.
This is a recipe for "I lost data that I wrote /days/ before the system crashed" bug reports.
So ... exponential backoff on retries?
Maybe, but I don't think that actually helps anything and adds yet more "when should we write this" complication to inode writeback....
for_sync writebacks should attempt one last write. Maybe it'll succeed this time. If it does, just ClearPageError. If not, we have somebody to report this writeback error to, and ClearPageUptodate.
Which may well be unmount. Are we really going to wait until unmount to report fatal errors?
Goodness, no. The errors would be immediately reportable using the wb_err mechanism, as soon as the first error was encountered.
But if there are no open files when the error occurs, that error won't get reported to anyone. Which means the next time anyone accesses that inode from a user context could very well be unmount or a third party sync/syncfs()....
From:   Eric Sandeen <esandeen@...hat.com>
Date:   Wed, 18 Apr 2018 19:23:46 -0500
On 4/18/18 6:59 PM, Dave Chinner wrote:
On Fri, Apr 13, 2018 at 07:04:33PM -0700, Andres Freund wrote:
Hi,
On 2018-04-14 11:47:52 +1000, Dave Chinner wrote:
And we treat different errors according to their seriousness. EIO and device ENOSPC we default to retry forever because they are often transient, but for ENODEV we fail and shutdown immediately (someone pulled the USB stick out). metadata failure behaviour is configured via changing fields in /sys/fs/xfs/
/error/metadata/
/...
We've planned to extend this failure configuration to data IO, too, but never quite got around to it yet. this is a clear example of "one size doesn't fit all" and I think we'll end up doing the same sort of error behaviour configuration in XFS for these cases. (i.e. /sys/fs/xfs/
/error/writeback/
/....)
Have you considered adding an ext/fat/jfs errors=remount-ro/panic/continue style mount parameter?
That's for metadata writeback error behaviour, not data writeback IO errors.
/me points casually at data_err=abort & data_err=ignore in ext4...
data_err=ignore
              Just print an error message if an error occurs in a file data buffer in ordered mode.

       data_err=abort
              Abort the journal if an error occurs in a file data buffer in ordered mode.
Just sayin'
We are definitely not planning to add mount options to configure IO error behaviors. Mount options are a horrible way to configure filesystem behaviour and we've already got other, fine-grained configuration infrastructure for configuring IO error behaviour. Which, as I just pointed out, was designed to be be extended to data writeback and other operational error handling in the filesystem (e.g. dealing with ENOMEM in different ways).
I don't disagree, but there are already mount-option knobs in ext4, FWIW.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Wed, 18 Apr 2018 17:40:37 -0700
On Thu, Apr 19, 2018 at 10:13:43AM +1000, Dave Chinner wrote:
On Fri, Apr 13, 2018 at 07:38:14PM -0700, Matthew Wilcox wrote:
On Sat, Apr 14, 2018 at 11:47:52AM +1000, Dave Chinner wrote:
On Fri, Apr 13, 2018 at 07:02:32AM -0700, Matthew Wilcox wrote:
If we get an error while wbc->for_background is true, we should not clear uptodate on the page, rather SetPageError and SetPageDirty.
So you're saying we should treat it as a transient error rather than a permanent error.
Yes, I'm proposing leaving the data in memory in case the user wants to try writing it somewhere else.
And if it's getting IO errors because of USB stick pull? What then?
I've been thinking about this. Ideally we want to pass some kind of notification all the way up to the desktop and tell the user to plug the damn stick back in. Then have the USB stick become the same blockdev that it used to be, and complete the writeback. We are so far from being able to do that right now that it's not even funny.
Background writebacks should skip pages which are PageError.
That seems decidedly dodgy in the case where there is a transient error - it requires a user to specifically run sync to get the data to disk after the transient error has occurred. Say they don't notice the problem because it's fleeting and doesn't cause any obvious problems?
That's fair. What I want to avoid is triggering the same error every 30 seconds (or whatever the periodic writeback threshold is set to).
So if kernel ring buffer overflows and so users miss the first error report, they'll have no idea that the data writeback is still failing?
I wasn't thinking about kernel ringbuffer based reporting; I was thinking about errseq_t based reporting, so the application can tell the fsync failed and maybe does something application-level to recover like send the transactions across to another node in the cluster (or whatever this hypothetical application is).
for_sync writebacks should attempt one last write. Maybe it'll succeed this time. If it does, just ClearPageError. If not, we have somebody to report this writeback error to, and ClearPageUptodate.
Which may well be unmount. Are we really going to wait until unmount to report fatal errors?
Goodness, no. The errors would be immediately reportable using the wb_err mechanism, as soon as the first error was encountered.
But if there are no open files when the error occurs, that error won't get reported to anyone. Which means the next time anyone accesses that inode from a user context could very well be unmount or a third party sync/syncfs()....
Right. But then that's on the application.
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Wed, 18 Apr 2018 21:08:19 -0400
On Wed, Apr 18, 2018 at 05:40:37PM -0700, Matthew Wilcox wrote:
I've been thinking about this. Ideally we want to pass some kind of notification all the way up to the desktop and tell the user to plug the damn stick back in. Then have the USB stick become the same blockdev that it used to be, and complete the writeback. We are so far from being able to do that right now that it's not even funny.o
Maybe we shouldn't be trying to do any of this in the kernel, or at least as little as possible in the kernel? Perhaps it would be better to do most of this as a device mapper hack; I suspect we'll need userspace help to igure out whether the user has plugged the same USB stick in, or a different USB stick, anyway.
From:   Christoph Hellwig <hch@...radead.org>
Date:   Thu, 19 Apr 2018 01:39:04 -0700
On Wed, Apr 18, 2018 at 12:52:19PM -0400, J. Bruce Fields wrote:
Theodore Y. Ts'o - 10.04.18, 20:43:
First of all, what storage devices will do when they hit an exception condition is quite non-deterministic. For example, the vast majority of SSD's are not power fail certified. What this means is that if they suffer a power drop while they are doing a GC, it is quite possible for data written six months ago to be lost as a result. The LBA could potentialy be far, far away from any LBA's that were recently written, and there could have been multiple CACHE FLUSH operations in the since the LBA in question was last written six months ago. No matter; for a consumer-grade SSD, it's possible for that LBA to be trashed after an unexpected power drop.
Pointers to documentation or papers or anything? The only google results I can find for "power fail certified" are your posts.
I've always been confused by SSD power-loss protection, as nobody seems completely clear whether it's a safety or a performance feature.
Devices from reputable vendors should always be power fail safe, bugs notwithstanding. What power-loss protection in marketing slides usually means is that an SSD has a non-volatile write cache. That is once a write is ACKed data is persisted and no additional cache flush needs to be sent. This is a feature only available in expensive eterprise SSDs as the required capacitors are expensive. Cheaper consumer or boot driver SSDs have a volatile write cache, that is we need to do a separate cache flush to persist data (REQ_OP_FLUSH in Linux). But a reasonable implementation of those still won't corrupt previously written data, they will just lose the volatile write cache that hasn't been flushed. Occasional bugs, bad actors or other issues might still happen.
From:   "J. Bruce Fields" <bfields@...ldses.org>
Date:   Thu, 19 Apr 2018 10:10:16 -0400
On Thu, Apr 19, 2018 at 01:39:04AM -0700, Christoph Hellwig wrote:
On Wed, Apr 18, 2018 at 12:52:19PM -0400, J. Bruce Fields wrote:
Theodore Y. Ts'o - 10.04.18, 20:43:
First of all, what storage devices will do when they hit an exception condition is quite non-deterministic. For example, the vast majority of SSD's are not power fail certified. What this means is that if they suffer a power drop while they are doing a GC, it is quite possible for data written six months ago to be lost as a result. The LBA could potentialy be far, far away from any LBA's that were recently written, and there could have been multiple CACHE FLUSH operations in the since the LBA in question was last written six months ago. No matter; for a consumer-grade SSD, it's possible for that LBA to be trashed after an unexpected power drop.
Pointers to documentation or papers or anything? The only google results I can find for "power fail certified" are your posts.
I've always been confused by SSD power-loss protection, as nobody seems completely clear whether it's a safety or a performance feature.
Devices from reputable vendors should always be power fail safe, bugs notwithstanding. What power-loss protection in marketing slides usually means is that an SSD has a non-volatile write cache. That is once a write is ACKed data is persisted and no additional cache flush needs to be sent. This is a feature only available in expensive eterprise SSDs as the required capacitors are expensive. Cheaper consumer or boot driver SSDs have a volatile write cache, that is we need to do a separate cache flush to persist data (REQ_OP_FLUSH in Linux). But a reasonable implementation of those still won't corrupt previously written data, they will just lose the volatile write cache that hasn't been flushed. Occasional bugs, bad actors or other issues might still happen.
Thanks! That was my understanding too. But then the name is terrible. As is all the vendor documentation I can find:
https://insights.samsung.com/2016/03/22/power-loss-protection-how-ssds-are-protecting-data-integrity-white-paper/
"Power loss protection is a critical aspect of ensuring data integrity, especially in servers or data centers."
https://www.intel.com/content/.../ssd-320-series-power-loss-data-protection-brief.pdf
"Data safety features prepare for unexpected power-loss and protect system and user data."
Why do they all neglect to mention that their consumer drives are also perfectly capable of well-defined behavior after power loss, just at the expense of flush performance? It's ridiculously confusing.
From:   Matthew Wilcox <willy@...radead.org>
Date:   Thu, 19 Apr 2018 10:40:10 -0700
On Wed, Apr 18, 2018 at 09:08:19PM -0400, Theodore Y. Ts'o wrote:
On Wed, Apr 18, 2018 at 05:40:37PM -0700, Matthew Wilcox wrote:
I've been thinking about this. Ideally we want to pass some kind of notification all the way up to the desktop and tell the user to plug the damn stick back in. Then have the USB stick become the same blockdev that it used to be, and complete the writeback. We are so far from being able to do that right now that it's not even funny.o
Maybe we shouldn't be trying to do any of this in the kernel, or at least as little as possible in the kernel? Perhaps it would be better to do most of this as a device mapper hack; I suspect we'll need userspace help to igure out whether the user has plugged the same USB stick in, or a different USB stick, anyway.
The device mapper target (dm-removable?) was my first idea too, but I kept thinking through use cases and I think we end up wanting this functionality in the block layer. Let's try a story.
Stephen the PFY goes into the data centre looking to hotswap a failed drive. Due to the eight pints of lager he had for lunch, he pulls out the root drive instead of the failed drive. The air raid siren warbles and he realises his mistake, shoving the drive back in.
CYOA:
Currently: All writes are lost, calamities ensue. The PFY is fired.
With dm-removable: Nobody thought to set up dm-removable on the root drive. Calamities still ensue, but now it's the BOFH's fault instead of the PFY's fault.
Built into the block layer: After a brief hiccup while we reattach the drive to its block_device, the writes resume and nobody loses their job.
From:   "Theodore Y. Ts'o" <tytso@....edu>
Date:   Thu, 19 Apr 2018 19:27:15 -0400
On Thu, Apr 19, 2018 at 10:40:10AM -0700, Matthew Wilcox wrote:
With dm-removable: Nobody thought to set up dm-removable on the root drive. Calamities still ensue, but now it's the BOFH's fault instead of the PFY's fault.
Built into the block layer: After a brief hiccup while we reattach the drive to its block_device, the writes resume and nobody loses their job.
What you're talking about is a deployment issue, though. Ultimately the distribution will set up dm-removable automatically if the user requests it, much like it sets up dm-crypt automatically for laptop users upon request.
My concern is that not all removable devices have a globally unique id number available in hardware so the kernel can tell whether or not it's the same device that has been plugged in. There are hueristics you could use -- for example, you could look at the file system uuid plus the last fsck time. But they tend to be very file system specific, and not things we would want ot have in the kernel.
From:   Dave Chinner <david@...morbit.com>
Date:   Fri, 20 Apr 2018 09:28:59 +1000
On Wed, Apr 18, 2018 at 05:40:37PM -0700, Matthew Wilcox wrote:
On Thu, Apr 19, 2018 at 10:13:43AM +1000, Dave Chinner wrote:
On Fri, Apr 13, 2018 at 07:38:14PM -0700, Matthew Wilcox wrote:
On Sat, Apr 14, 2018 at 11:47:52AM +1000, Dave Chinner wrote:
On Fri, Apr 13, 2018 at 07:02:32AM -0700, Matthew Wilcox wrote:
If we get an error while wbc->for_background is true, we should not clear uptodate on the page, rather SetPageError and SetPageDirty.
So you're saying we should treat it as a transient error rather than a permanent error.
Yes, I'm proposing leaving the data in memory in case the user wants to try writing it somewhere else.
And if it's getting IO errors because of USB stick pull? What then?
I've been thinking about this. Ideally we want to pass some kind of notification all the way up to the desktop and tell the user to plug the damn stick back in. Then have the USB stick become the same blockdev that it used to be, and complete the writeback. We are so far from being able to do that right now that it's not even funny.
nod
But in the meantime, device unplug (should give ENODEV, not EIO) is a fatal error and we need to toss away the data.
Background writebacks should skip pages which are PageError.
That seems decidedly dodgy in the case where there is a transient error - it requires a user to specifically run sync to get the data to disk after the transient error has occurred. Say they don't notice the problem because it's fleeting and doesn't cause any obvious problems?
That's fair. What I want to avoid is triggering the same error every 30 seconds (or whatever the periodic writeback threshold is set to).
So if kernel ring buffer overflows and so users miss the first error report, they'll have no idea that the data writeback is still failing?
I wasn't thinking about kernel ringbuffer based reporting; I was thinking about errseq_t based reporting, so the application can tell the fsync failed and maybe does something application-level to recover like send the transactions across to another node in the cluster (or whatever this hypothetical application is).
But if it's still failing, then we should be still trying to report the error. i.e. if fsync fails and the page remains dirty, then the next attmept to write it is a new error and fsync should report that. IOWs, I think we should be returning errors at every occasion errors need to be reported if we have a persistent writeback failure...
for_sync writebacks should attempt one last write. Maybe it'll succeed this time. If it does, just ClearPageError. If not, we have somebody to report this writeback error to, and ClearPageUptodate.
Which may well be unmount. Are we really going to wait until unmount to report fatal errors?
Goodness, no. The errors would be immediately reportable using the wb_err mechanism, as soon as the first error was encountered.
But if there are no open files when the error occurs, that error won't get reported to anyone. Which means the next time anyone accesses that inode from a user context could very well be unmount or a third party sync/syncfs()....
Right. But then that's on the application.
Which we know don't do the right thing. Seems like a lot of hoops to jump through given it still won't work if the appliction isn't changed to support linux specific error handling requirements...
From:   Jan Kara <jack@...e.cz>
Date:   Sat, 21 Apr 2018 18:59:54 +0200
On Fri 13-04-18 07:48:07, Matthew Wilcox wrote:
On Tue, Apr 10, 2018 at 03:07:26PM -0700, Andres Freund wrote:
I don't think that's the full issue. We can deal with the fact that an fsync failure is edge-triggered if there's a guarantee that every process doing so would get it. The fact that one needs to have an FD open from before any failing writes occurred to get a failure,
THAT'S
the big issue.
Beyond postgres, it's a pretty common approach to do work on a lot of files without fsyncing, then iterate over the directory fsync everything, and
then
assume you're safe. But unless I severaly misunderstand something that'd only be safe if you kept an FD for every file open, which isn't realistic for pretty obvious reasons.
While accepting that under memory pressure we can still evict the error indicators, we can do a better job than we do today. The current design of error reporting says that all errors which occurred before you opened the file descriptor are of no interest to you. I don't think that's necessarily true, and it's actually a change of behaviour from before the errseq work.
Consider Stupid Task A which calls open(), write(), close(), and Smart Task B which calls open(), write(), fsync(), close() operating on the same file. If A goes entirely before B and encounters an error, before errseq_t, B would see the error from A's write.
If A and B overlap, even a little bit, then B still gets to see A's error today. But if writeback happens for A's write before B opens the file then B will never see the error.
B doesn't want to see historical errors that a previous invocation of B has already handled, but we know whether
anyone
has seen the error or not. So here's a patch which restores the historical behaviour of seeing old unhandled errors on a fresh file descriptor:
Signed-off-by: Matthew Wilcox
mawilcox@...rosoft.com
So I agree with going to the old semantics of reporting errors from before a file was open at least once to someone. As the PG case shows apps are indeed relying on the old behavior. As much as it is unreliable, it ends up doing the right thing for these apps in 99% of cases and we shouldn't break them (BTW IMO the changelog should contain a note that this fixes a regression of PostgreSQL, a reference to this thread and CC to stable). Anyway feel free to add:
Reviewed-by: Jan Kara
jack@...e.cz
Oh, and to make myself clear I do think we need to find a better way of reporting IO errors. I consider this just an immediate band-aid to avoid userspace regressions.
diff --git a/lib/errseq.c b/lib/errseq.c index df782418b333..093f1fba4ee0 100644 --- a/lib/errseq.c +++ b/lib/errseq.c @@ -119,19 +119,11 @@ EXPORT_SYMBOL(errseq_set); errseq_t errseq_sample(errseq_t *eseq) { errseq_t old = READ_ONCE(*eseq); - errseq_t new = old;
/*
* For the common case of no errors ever having been set, we can skip
* marking the SEEN bit. Once an error has been set, the value will
* never go back to zero.
*/
if (old != 0) {
new |= ERRSEQ_SEEN;
if (old != new)
cmpxchg(eseq, old, new);
}
return new;
/* If nobody has seen this error yet, then we can be the first. */
if (!(old & ERRSEQ_SEEN))
old = 0;
return old;
From:   Jan Kara <jack@...e.cz>
Date:   Sat, 21 Apr 2018 20:14:29 +0200
On Thu 12-04-18 07:09:14, Jeff Layton wrote:
On Wed, 2018-04-11 at 20:02 -0700, Matthew Wilcox wrote:
At the moment, when we open a file, we sample the current state of the writeback error and only report new errors. We could set it to zero instead, and report the most recent error as soon as anything happens which would report an error. That way err = close(open("file")); would report the most recent error.
That's not going to be persistent across the data structure for that inode being removed from memory; we'd need filesystem support for persisting that. But maybe it's "good enough" to only support it for recent files.
Jeff, what do you think?
I hate it :). We could do that, but....yecchhhh.
Reporting errors only in the case where the inode happened to stick around in the cache seems too unreliable for real-world usage, and might be problematic for some use cases. I'm also not sure it would really be helpful.
So this is never going to be perfect but I think we could do good enough by: 1) Mark inodes that hit IO error. 2) If the inode gets evicted from memory we store the fact that we hit an error for this IO in a more space efficient data structure (sparse bitmap, radix tree, extent tree, whatever). 3) If the underlying device gets destroyed, we can just switch the whole SB to an error state and forget per inode info. 4) If there's too much of per-inode error info (probably per-fs configurable limit in terms of number of inodes), we would yell in the kernel log, switch the whole fs to the error state and forget per inode info.
This way there won't be silent loss of IO errors. Memory usage would be reasonably limited. It could happen the whole fs would switch to error state "prematurely" but if that's a problem for the machine, admin could tune the limit for number of inodes to keep IO errors for...
I think the crux of the matter here is not really about error reporting, per-se.
I think this is related but a different question.
I asked this at LSF last year, and got no real answer:
When there is a writeback error, what should be done with the dirty page(s)? Right now, we usually just mark them clean and carry on. Is that the right thing to do?
One possibility would be to invalidate the range that failed to be written (or the whole file) and force the pages to be faulted in again on the next access. It could be surprising for some applications to not see the results of their writes on a subsequent read after such an event.
Maybe that's ok in the face of a writeback error though? IDK.
I can see the admin wanting to rather kill the machine with OOM than having to deal with data loss due to IO errors (e.g. if he has HA server fail over set up). Or retry for some time before dropping the dirty data. Or do what we do now (possibly with invalidating pages as you say). As Dave said elsewhere there's not one strategy that's going to please everybody. So it might be beneficial to have this configurable like XFS has it for metadata.
OTOH if I look at the problem from application developer POV, most apps will just declare game over at the face of IO errors (if they take care to check for them at all). And the sophisticated apps that will try some kind of error recovery have to be prepared that the data is just gone (as depending on what exactly the kernel does is rather fragile) so I'm not sure how much practical value the configurable behavior on writeback errors would bring.
