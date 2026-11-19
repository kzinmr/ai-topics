---
title: "If the Windows documentation doesn't list a particular technology as supporting an operation, does that mean that it doesn't support it?"
url: "https://devblogs.microsoft.com/oldnewthing/20261118-00/?p=112870/"
fetched_at: 2026-11-19T10:01:32.889039+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# If the Windows documentation doesn't list a particular technology as supporting an operation, does that mean that it doesn't support it?

Source: https://devblogs.microsoft.com/oldnewthing/20261118-00/?p=112870/

In the Windows documentation for various file system operations, you will often find a section in the Remarks that says
This function is supported by the following technologies.
Technology
Supported
Server Message Block (SMB) 3.0 protocol
Yes
SMB 3.0 Transparent Failover (TFO)
Yes
SMB 3.0 with Scale-out File Shares (SO)
Yes
Cluster Shared Volume File System (CsvFS)
Yes
Resilient File System (ReFS)
Yes
But what about network protocols that aren’t on the list? Does their absence mean that they aren’t supported?
The table lists the file systems and network protocols that we has information for. If something is not on the list, that doesn’t mean that it doesn’t support it. It just means that we don’t know whether it supports it.
If it definitely didn’t support it, then it would have been in the table with a “No”, like this one for
Get­File­Information­By­Handle
:
Technology
Supported
Server Message Block (SMB) 3.0 protocol
No
SMB 3.0 Transparent Failover (TFO)
No
SMB 3.0 with Scale-out File Shares (SO)
No
Cluster Shared Volume File System (CsvFS)
Yes
Resilient File System (ReFS)
Yes
Since third parties can implement their own network protocols,¹ the Windows documentation cannot be comprehensive. It just documents what it knows. If you want information about some other network protocol or file system driver, you’ll have to consult the documentation for the product that implements the protocol or file system you are interested in.
¹ I noticed
AFS
and
APFS
and I didn’t even make it to the letter B.
