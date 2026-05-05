---
title: "Filesystem error handling"
url: "https://danluu.com/filesystem-errors/"
fetched_at: 2026-05-05T07:01:31.796034+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Filesystem error handling

Source: https://danluu.com/filesystem-errors/

We’re going to reproduce some
results from papers on filesystem robustness that were written up roughly a decade ago
:
Prabhakaran et al. SOSP 05 paper
, which injected errors below the filesystem and
Gunawi et al. FAST 08
, which looked at how often filesystems failed to check return codes of functions that can return errors.
Prabhakaran et al.
injected errors at the block device level (just underneath the filesystem) and found that
ext3
,
resierfs
,
ntfs
, and
jfs
mostly handled read errors reasonbly but
ext3
,
ntfs
, and
jfs
mostly ignored write errors. While the paper is interesting, someone installing Linux on a system today is much more likely to use
ext4
than any of the now-dated filesystems tested by Prahbhakaran et al. We’ll try to reproduce some of the basic results from the paper on more modern filesystems like
ext4
and
btrfs
, some legacy filesystems like
exfat
,
ext3
, and
jfs
, as well as on
overlayfs
.
Gunawi et al.
found that errors weren’t checked most of the time. After we look at error injection on modern filesystems, we’ll look at how much (or little) filesystems have improved their error handling code.
Error injection
A cartoon view of a file read might be:
pread syscall -> OS generic filesystem code -> filesystem specific code -> block device code -> device driver -> device controller -> disk
. Once the disk gets the request, it sends the data back up:
disk -> device controller -> device driver -> block device code -> filesystem specific code -> OS generic filesystem code -> pread
. We’re going to look at error injection at the block device level, right below the file system.
Let’s look at what happened when we injected errors in 2017 vs. what Prabhakaran et al. found in 2005.
2005
2017
read
write
silent
read
write
silent
read
write
silent
file
mmap
btrfs
prop
prop
prop
prop
prop
prop
exfat
prop
prop
ignore
prop
prop
ignore
ext3
prop
ignore
ignore
prop
prop
ignore
prop
prop
ignore
ext4
prop
prop
ignore
prop
prop
ignore
fat
prop
prop
ignore
prop
prop
ignore
jfs
prop
ignore
ignore
prop
ignore
ignore
prop
prop
ignore
reiserfs
prop
prop
ignore
xfs
prop
prop
ignore
prop
prop
ignore
Each row shows results for one filesystem.
read
and
write
indicating reading and writing data, respectively, where the block device returns an error indicating that the operation failed.
silent
indicates a read failure (incorrect data) where the block device didn’t indicate an error. This could happen if there’s disk corruption, a transient read failure, or a transient write failure silently caused bad data to be written.
file
indicates that the operation was done on a file opened with
open
and
mmap
indicates that the test was done on a file mapped with
mmap
.
ignore
(red) indicates that the error was ignored,
prop
(yellow) indicates that the error was propagated and that the
pread
or
pwrite
syscall returned an error code, and
fix
(green) indicates that the error was corrected. No errors were corrected. Grey entries indicate configurations that weren’t tested.
From the table, we can see that, in 2005,
ext3
and
jfs
ignored write errors even when the block device indicated that the write failed and that things have improved, and that any filesystem you’re likely to use will correctly tell you that a write failed.
jfs
hasn’t improved, but
jfs
is now rarely used outside of legacy installations.
No tested filesystem other than
btrfs
handled silent failures correctly. The other filesystems tested neither duplicate nor checksum data, making it impossible for them to detect silent failures.
zfs
would probably also handle silent failures correctly but wasn’t tested.
apfs
, despite post-dating
btrfs
and
zfs
, made the explicit decision to not checksum data and silently fail on silent block device errors. We’ll discuss this more later.
In all cases tested where errors were propagated, file reads and writes returned
EIO
from
pread
or
pwrite
, respectively;
mmap
reads and writes caused the process to receive a
SIGBUS
signal.
The 2017 tests above used an 8k file where the first block that contained file data either returned an error at the block device level or was corrupted, depending on the test. The table below tests the same thing, but with a 445 byte file instead of an 8k file. The choice of 445 was arbitrary.
2005
2017
read
write
silent
read
write
silent
read
write
silent
file
mmap
btrfs
fix
fix
fix
fix
fix
fix
exfat
prop
prop
ignore
prop
prop
ignore
ext3
prop
ignore
ignore
prop
prop
ignore
prop
prop
ignore
ext4
prop
prop
ignore
prop
prop
ignore
fat
prop
prop
ignore
prop
prop
ignore
jfs
prop
ignore
ignore
prop
ignore
ignore
prop
prop
ignore
reiserfs
prop
prop
ignore
xfs
prop
prop
ignore
prop
prop
ignore
In the small file test table, all the results are the same, except for
btrfs
, which returns correct data in every case tested. What’s happening here is that the filesystem was created on a rotational disk and, by default,
btrfs
duplicates filesystem metadata on rotational disks (it can be configured to do so on SSDs, but that’s not the default). Since the file was tiny,
btrfs
packed the file into the metadata and the file was duplicated along with the metadata, allowing the filesystem to fix the error when one block either returned bad data or reported a failure.
Overlay
Overlayfs
allows one file system to be “overlaid” on another.
As explained in the initial commit
, one use case might be to put an (upper) read-write directory tree on top of a (lower) read-only directory tree, where all modifications go to the upper, writable layer.
Although not listed on the tables, we also tested every filesystem other than
fat
as the lower filesystem with overlay fs (ext4 was the upper filesystem for all tests). Every filessytem tested showed the same results when used as the bottom layer in
overlay
as when used alone.
fat
wasn’t tested because mounting
fat
resulted in a
filesystem not supported
error.
Error correction
btrfs
doesn’t, by default, duplicate metadata on SSDs because the developers believe that redundancy wouldn’t provide protection against errors on SSD (which is the same reason
apfs
doesn’t have redundancy). SSDs do a kind of write coalescing, which is likely to cause writes which happen consecutively to fall into the same block. If that block has a total failure, the redundant copies would all be lost, so redundancy doesn’t provide as much protection against failure as it would on a rotational drive.
I’m not sure that this means that redundancy wouldn’t help -- Individual flash cells degrade with operation and lose charge as they age. SSDs have built-in
wear-leveling
and
error-correction
that’s designed to reduce the probability that a block returns bad data, but over time, some blocks will develop so many errors that the error-correction won’t be able to fix the error and the block will return bad data. In that case, a read should return some bad bits along with mostly good bits. AFAICT, the publicly available data on SSD error rates seems to line up with this view.
Error detection
Relatedly, it appears that
apfs
doesn’t checksum data because “[apfs] engineers contend that Apple devices basically don’t return bogus data”
. Publicly available studies on SSD reliability have not found that there’s a model that doesn’t sometimes return bad data. It’s a common conception that SSDs are less likely to return bad data than rotational disks, but when Google studied this across their drives, they found:
The annual replacement rates of hard disk drives have previously been reported to be 2-9% [19,20], which is high compared to the 4-10% of flash drives we see being replaced in a 4 year period. However, flash drives are less attractive when it comes to their error rates. More than 20% of flash drives develop uncorrectable errors in a four year period, 30-80% develop bad blocks and 2-7% of them develop bad chips. In comparison, previous work [1] on HDDs reports that only 3.5% of disks in a large population developed bad sectors in a 32 months period – a low number when taking into account that the number of sectors on a hard disk is orders of magnitudes larger than the number of either blocks or chips on a solid state drive, and that sectors are smaller than blocks, so a failure is less severe.
While there is one sense in which SSDs are more reliable than rotational disks, there’s also a sense in which they appear to be less reliable. It’s not impossible that Apple uses some kind of custom firmware on its drive that devotes more bits to error correction than you can get in publicly available disks, but even if that’s the case, you might plug a non-apple drive into your apple computer and want some kind of protection against data corruption.
Internal error handling
Now that we’ve reproduced some tests from Prabhakaran et al., we’re going to move on to
Gunawi et al.
. Since the paper is fairly involved, we’re just going to look at one small part of the paper, the part where they examined three function calls,
filemap_fdatawait
,
filemap_fdatawrite
, and
sync_blockdev
to see how often errors weren’t checked for these functions.
Their justification for looking at these function is given as:
As discussed in Section 3.1, a function could return more than one error code at the same time, and checking only one of them suffices. However, if we know that a certain function only returns a single error code and yet the caller does not save the return value properly, then we would know that such call is really a flaw. To find real flaws in the file system code, we examined three important functions that we know only return single error codes: sync_blockdev, filemap_fdatawrite, and filemap_fdatawait. A file system that does not check the returned error codes from these functions would obviously let failures go unnoticed in the upper layers.
Ignoring errors from these functions appears to have fairly serious consequences. The documentation for
filemap_fdatawait
says:
filemap_fdatawait — wait for all under-writeback pages to complete
...
Walk the list of under-writeback pages of the given address space and wait for all of them. Check error status of the address space and return it.
Since the error status of the address space is cleared by this function, callers are responsible for checking the return value and handling and/or reporting the error.
The comment next to the code for
sync_blockdev
reads:
Write out and wait upon all the dirty data associated with a block device via its mapping.  Does not take the superblock lock.
In both of these cases, it appears that ignoring the error code could mean that data would fail to get written to disk without notifying the writer that the data wasn’t actually written?
Let’s look at  how often calls to these functions didn’t completely ignore the error code:
fn
2008
'08 %
2017
'17 %
filemap_fdatawait
7 / 29
24
12 / 17
71
filemap_fdatawrite
17 / 47
36
13 / 22
59
sync_blockdev
6 / 21
29
7 / 23
30
This table is for all code in linux under
fs
. Each row shows data for calls of one function. For each year, the leftmost cell shows the number of calls that do something with the return value over the total number of calls. The cell to the right shows the percentage of calls that do something with the return value. “Do something” is used very loosely here -- branching on the return value and then failing to handle the error in either branch, returning the return value and having the caller fail to handle the return value, as well as saving the return value and then ignoring it are all considered doing something for the purposes of this table.
For example Gunawi et al. noted that
cifs/transport.c
had
int SendReceive () { 
    int rc;
    rc = cifs_sign_smb(); // 
    ... 
    rc = smb_send();
}
Although
cifs_sign_smb
returned an error code, it was never checked before being overwritten by
smb_send
, which counted as being used for our purposes even though the error wasn’t handled.
Overall, the table appears to show that many more errors are handled now than were handled in 2008 when Gunawi et al. did their analysis, but it’s hard to say what this means from looking at the raw numbers because it might be ok for some errors not to be handled and different lines of code are executed with different probabilities.
Conclusion
Filesystem error handling seems to have improved. Reporting an error on a
pwrite
if the block device reports an error is perhaps the most basic error propagation a robust filesystem should do; few filesystems reported that error correctly in 2005. Today, most filesystems will correctly report an error when the simplest possible error condition that doesn’t involve the entire drive being dead occurs if there are no complicating factors.
Most filesystems don’t have checksums for data and leave error detection and correction up to userspace software. When I talk to server-side devs at big companies, their answer is usually something like “who cares? All of our file accesses go through a library that checksums things anyway and redundancy across machines and datacenters takes care of failures, so we only need error detection and not correction”. While that’s true for developers at certain big companies, there’s a lot of software out there that isn’t written robustly and just assumes that filesystems and disks don’t have errors.
This was a joint project with Wesley Aptekar-Cassels; the vast majority of the work for the project was done while pair programming at
RC
. We also got
a lot
of help from Kate Murphy. Both Wesley (w.aptekar@gmail.com) and Kate (hello@kate.io) are looking for work. They’re great and I highly recommend talking to them if you’re hiring!
Appendix: error handling in C
A fair amount of effort has been applied to get error handling right. But C makes it very easy to get things wrong, even when you apply a fair amount effort and even apply extra tooling. One example of this in the code is the
submit_one_bio
function. If you look at the definition, you can see that it’s annotated with
__must_check
, which will cause a compiler warning when the result is ignored. But if you look at calls of
submit_one_bio
, you’ll see that its callers aren’t annotated and can ignore errors. If you dig around enough you’ll find one path of error propagation that looks like:
submit_one_bio
submit_extent_page
__extent_writepage
extent_write_full_page
write_cache_pages
generic_writepages
do_writepages
__filemap_fdatawrite_range
__filemap_fdatawrite
filemap_fdatawrite
Nine levels removed from
submit_one_bio
, we see our old friend, `filemap_fdatawrite, which we know often doesn’t get checked for errors.
There's a very old debate over how to prevent things like this from accidentally happening. One school of thought, which I'll call the Uncle Bob (UB) school believes that
we can't fix these kinds of issues with tools or processes and simply need to be better programmers in order to avoid bugs
. You'll often hear people of the UB school say things like, "you can't get rid of all bugs with better tools (or processes)". In his famous and well-regarded talk,
Simple Made Easy
, Rich Hickey says
What's true of every bug found in the field?
[Audience reply: Someone wrote it?] [Audience reply: It got written.]
It got written. Yes. What's a more interesting fact about it? It passed the type checker.
[Audience laughter]
What else did it do?
[Audience reply: (Indiscernible)]
It passed all the tests. Okay. So now what do you do? Right? I think we're in this world I'd like to call guardrail programming. Right? It's really sad. We're like: I can make change because I have tests. Who does that? Who drives their car around banging against the guardrail saying, "Whoa! I'm glad I've got these guardrails because I'd never make it to the show on time."
[Audience laughter]
If you watch the talk, Rich uses "simplicity" the way Uncle Bob uses "discipline". They way these statements are used, they're roughly equivalent to Ken Thompson saying "
Bugs are bugs. You write code with bugs because you do
". The UB school throws tools and processes under the bus, saying that it's unsafe to rely solely on tools or processes.
Rich's rhetorical trick is brilliant -- I've heard that line quoted tens of times since the talk to argue against tests or tools or types. But, like guardrails, most tools and processes aren't about eliminating all bugs, they're about reducing the severity or probability of bugs. If we look at this particular function call, we can see that a static analysis tool failed to find this bug. Does that mean that we should give up on static analysis tools? A static analysis tool could look for all calls of
submit_one_bio
and show you the cases where the error is propagated up N levels only to be dropped. Gunawi et al. did exactly that and found
a lot
of bugs. A person basically can't do the same thing without tooling. They could try, but people are lucky if they get 95% accuracy when manually digging through things like this. The sheer volume of code guarantees that a human doing this by hand would make mistakes.
Even better than a static analysis tool would be a language that makes it harder to accidentally forget about checking for an error. One of the issues here is that it's sometimes valid to drop an error. There are a number of places where there's no interace that allows an error to get propagated out of the filesystem, making it correct to drop the error, modulo changing the interface. In the current situation, as an outsider reading the code, if you look at a bunch of calls that drop errors, it's very hard to say, for all of them, which of those is a bug and which of those is correct. If the default is that we have a kind of guardrail that says "this error must be checked", people can still incorrectly ignore errors, but you at least get an annotation that the omission was on purpose. For example, if you're forced to specifically write code that indicates that you're ignoring an error, and in code that's inteded to be robust, like filesystem code, code that drops an error on purpose is relatively likely to be accompanied by a comment explaining why the error was dropped.
Appendix: why wasn't this done earlier?
After all, it would be nice if we knew if modern filesystems could do basic tasks correctly. Filesystem developers probably know this stuff, but since I don't
follow LKML
, I had no idea whether or not things had improved since 2005 until we ran the experiment.
The papers we looked at here came out of Andrea and Remzi Arpaci-Dusseau's research lab. Remzi has a talk where he mentioned that grad students don't want to reproduce and update old work. That's entirely reasonable, given the incentives they face. And I don't mean to pick on academia here -- this work came out of academia, not industry. It's possible this kind of work simply wouldn't have happened if not for the academic incentive system.
In general, it seems to be quite difficult to fund work on correctness. There are a fair number of papers on new ways to find bugs, but that's relatively little work on applying existing techniques to existing code. In academia, that seems to be hard to get a good publication out of, in the open source world, that seems to be less interesting to people than writing new code. That's also entirely reasonable -- people should work on what they want, and even if they enjoy working on correctness, that's probably not a great career decision in general. I was at the
RC
career fair the other night and my badge said I was interested in testing. The first person who chatted me up opened with "do you work in QA?". Back when I worked in hardware, that wouldn't have been a red flag, but in software, "QA" is code for a low-skill, tedious, and poorly paid job. Much of industry considers testing and QA to be an afterthought. As a result, open source projects that companies rely on are often
woefully underfunded
. Google funds some great work (like afl-fuzz), but that's the exception and not the rule, even within Google, and most companies don't fund any open source work. The work in this post was done by a few people who are intentionally temporarily unemployed, which isn't really a scalable model.
Occasionally, you'll see someone spend a lot of effort on immproving correctness, but that's usually done as a massive amount of free labor. Kyle Kingsbury might be the canonical example of this -- my understanding is that he worked on the
Jepsen distributed systems testing tool
on nights and weekends for years before turning that into a consulting business. It's great that he did that -- he showed that almost every open source distributed system had serious data loss or corruption bugs. I think that's great, but stories about heoric effort like that always worry me because heroism doesn't scale. If Kyle hadn't come along, would most of the bugs that he and his tool found still plague open source distributed systems today? That's a scary thought.
If I knew how to fund more work on correctness, I'd try to convince you that we should switch to this new model, but I don't know of a funding model that works. I've set up a
patreon (donation account)
, but it would be quite extraordinary if that was sufficient to actually fund a signifcant amount of work. If you look at how much programmers make off of donations, if I made two order of magnitude less than I could if I took a job in industry, that would already put me in the top 1% of programmers on patreon. If I made one order of magnitude less than I'd make in industry, that would be extraordinary. Off the top of my head, the only programmers who make more than that off of patreon either make something with much broader appeal (like games) or are Evan You, who makes one of the most widely use front-end libraries in existence. And if I actually made as much as I can make in industry, I suspect that would make me the highest grossing programmer on patreon, even though, by industry standards, my compensation hasn't been anything special.
If I had to guess, I'd say that part of the reason it's hard to fund this kind of work is that consumers don't incentivize companies to fund this sort of work. If you look at "big" tech companies, two of them are substantially more serious about correctness than their competitors. This results in many fewer horror stories about lost emails and documents as well as lost entire accounts. If you look at the impact on consumers, it might be something like the difference between 1% of people seeing lost/corrupt emails vs. 0.001%. I think that's pretty significant if you multiply that cost across all consumers, but the vast majority of consumers aren't going to make decisions based on that kind of difference. If you look at an area where correctness problems are much more apparent, like databases or backups, you'll find that even the worst solutions have defenders who will pop into any dicussions and say "works for me". A backup solution that works 90% of the time is quite bad, but if you have one that works 90% of the time, it will still have staunch defenders who drop into discussions to say things like "I've restored from backup three times and it's never failed! You must be making stuff up!". I don't blame companies for rationally responding to consumers, but I do think that the result is unfortunate for consumers.
Just as an aside, one of the great wonders of doing open work for free is that the more free work you do, the more people complain that you didn't do enough free work. As David MacIver has said,
doing open source work is like doing normal paid work, except that you get paid in complaints instead of cash
. It's basically guaranteed that the most common comment on this post, for all time, will be that didn't test someone's pet filesystem because we're
btrfs
shills or just plain lazy, even though we include a link to a repo that lets anyone add tests as they please. Pretty much every time I've done any kind of free experimental work, people who obvously haven't read the experimental setup or the source code complain that the experiment couldn't possibly be right because of [thing that isn't true that anyone could see by looking at the setup] and that it's absolutely inexcusable that I didn't run the experiment on the exact pet thing they wanted to see. Having played video games competitively in the distant past, I'm used to much more intense internet trash talk, but in general, this incentive system seems to be backwards.
Appendix: experimental setup
For the error injection setup, a high-level view of the experimental setup is that
dmsetup
was used to simulate bad blocks on the disk.
A list of the commands run looks something like:
cp images/btrfs.img.gz /tmp/tmpeas9efr6.gz
gunzip -f /tmp/tmpeas9efr6.gz
losetup -f
losetup /dev/loop19 /tmp/tmpeas9efr6
blockdev --getsize /dev/loop19
#        0 74078 linear /dev/loop19 0
#        74078 1 error
#        74079 160296 linear /dev/loop19 74079
dmsetup create fserror_test_1508727591.4736078
mount /dev/mapper/fserror_test_1508727591.4736078 /mnt/fserror_test_1508727591.4736078/
mount -t overlay -o lowerdir=/mnt/fserror_test_1508727591.4736078/,upperdir=/tmp/tmp4qpgdn7f,workdir=/tmp/tmp0jn83rlr overlay /tmp/tmpeuot7zgu/
./mmap_read /tmp/tmpeuot7zgu/test.txt
umount /tmp/tmpeuot7zgu/
rm -rf /tmp/tmp4qpgdn7f
rm -rf /tmp/tmp0jn83rlr
umount /mnt/fserror_test_1508727591.4736078/
dmsetup remove fserror_test_1508727591.4736078
losetup -d /dev/loop19
rm /tmp/tmpeas9efr6
See this github repo for the exact set of commands run to execute tests
.
Note that all of these tests were done on linux, so
fat
means the linux
fat
implementation, not the windows
fat
implementation.
zfs
and
reiserfs
weren’t tested because they couldn’t be trivially tested in the exact same way that we tested other filesystems (one of us spent an hour or two trying to get
zfs
to work, but its configuration interface is inconsistent with all of the filesystems tested;
reiserfs
appears to have a consistent interface but testing it requires doing extra work for a filesystem that appears to be dead).
ext3
support is now provided by the
ext4
code, so what
ext3
means now is different from what it meant in 2005.
All tests were run on both ubuntu 17.04, 4.10.0-37, as well as on arch, 4.12.8-2. We got the same results on both machines. All filesystems were configured with default settings. For
btrfs
, this meant duplicated metadata without duplicated data and, as far as we know, the settings wouldn't have made a difference for other filesystems.
The second part of this doesn’t have much experimental setup to speak of. The setup was to grep the linux source code for the relevant functions.
Thanks to Leah Hanson, David Wragg, Ben Kuhn, Wesley Aptekar-Cassels, Joel Borggrén-Franck, Yuri Vishnevsky, and Dan Puttick for comments/corrections on this post.
