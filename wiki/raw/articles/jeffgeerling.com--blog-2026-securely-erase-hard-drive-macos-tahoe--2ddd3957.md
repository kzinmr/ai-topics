---
title: "How to Securely Erase an old Hard Drive on macOS Tahoe"
url: "https://www.jeffgeerling.com/blog/2026/securely-erase-hard-drive-macos-tahoe/"
fetched_at: 2026-04-28T07:02:53.099944+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# How to Securely Erase an old Hard Drive on macOS Tahoe

Source: https://www.jeffgeerling.com/blog/2026/securely-erase-hard-drive-macos-tahoe/

Apparently Apple thinks nobody with a modern Mac uses spinning rust (hard drives with platters) anymore.
I plugged in a hard drive from an old iMac into my Mac Studio using my
Sabrent USB to SATA Hard Drive
enclosure, and opened up Disk Utility, clicked on the top-level disk in the sidebar, and clicked 'Erase'.
Lo and behold, there's no 'Security Options' button on there, as there had been since—I believe—the very first version of Disk Utility in Mac OS X!
It seems like
this option may have been dropped in macOS 15 Sequoia
, but regardless, if you want to write 1s, 0s, or do a
DOE-compliant 3-pass erase
, you have to hop over to Terminal now.
Apple apparently hasn't gotten the memo, as
their macOS 26 Tahoe Disk Utility User Guide
currently states
:
(Optional) If available, click Security Options, use the slider to choose how many times to write over the erased data, then click OK.
Secure erase options are available only for some types of storage devices. If the Security Options button is not available, Disk Utility cannot perform a secure erase on the storage device.
Secure Erase with
diskutil
in Terminal
First, find your disk using
diskutil list
:
$ diskutil list
/dev/disk0 (internal, physical):
#:                       TYPE NAME                    SIZE       IDENTIFIER
0:      GUID_partition_scheme                        *1.0 TB     disk0
1:             Apple_APFS_ISC Container disk1         524.3 MB   disk0s1
2:                 Apple_APFS Container disk3         994.7 GB   disk0s2
3:        Apple_APFS_Recovery Container disk2         5.4 GB     disk0s3
...
/dev/disk9 (external, physical):
#:                       TYPE NAME                    SIZE       IDENTIFIER
0:     FDisk_partition_scheme                        *1.0 TB     disk9
1:                  Apple_HFS Macintosh HD            1.0 TB     disk9s1
Mine is
/dev/disk9
. Run the command
diskutil secureErase
on that disk, providing an integer for the secure option:
0 - Single-pass erase resulting in a zero fill.
1 - Single-pass erase resulting in a random-number fill.
2 - Seven-pass "secure" erase.
3 - Gutmann algorithm 35-pass "secure" erase.
4 - Three-pass "secure" erase.
For example:
$ diskutil secureErase 1 /dev/disk9
Started erase on disk9
[ / 0%..10%.............................................. ] 10.5%
diskutil
's docs warn
Level 2, 3, or 4 secure erases can take an extremely long time
, but even a single pass takes a while on older drives, or some of the largest modern drives with 16+ TB. SATA performance has sadly not kept up with the times.
