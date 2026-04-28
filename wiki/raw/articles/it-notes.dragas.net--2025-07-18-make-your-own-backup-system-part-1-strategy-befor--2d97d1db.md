---
title: "Make Your Own Backup System - Part 1: Strategy Before Scripts"
url: "https://it-notes.dragas.net/2025/07/18/make-your-own-backup-system-part-1-strategy-before-scripts/"
fetched_at: 2026-04-28T07:02:49.833609+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Make Your Own Backup System - Part 1: Strategy Before Scripts

Source: https://it-notes.dragas.net/2025/07/18/make-your-own-backup-system-part-1-strategy-before-scripts/

Backup: Beyond the Simple Copy
For as long as I can remember, backup is something that has been underestimated by far too many people. Between flawed techniques, "Schrödinger's backups" (i.e., never tested, thus both valid and invalid at the same time), and conceptual errors about what they are and how they work (RAID is not a backup!), too much data has been lost due to deficiencies in this area.
Nowadays, backup is often an afterthought. Many rely entirely on "the cloud" without ever asking how - or if - their data is actually protected. It's a detail many overlook, but even major cloud providers operate on a shared responsibility model. Their terms often clarify that while they secure the infrastructure, the ultimate responsibility for protecting and backing up your data lies with you. By putting everything "in the cloud", on clusters owned by other companies, or on distributed Kubernetes systems, backup seems unnecessary. When I sometimes ask developers or colleagues how they handle backups for all this, they look at me as if I'm speaking an archaic, unknown, and indecipherable language. The thought has simply never crossed their minds. But data is not ephemeral; it must be preserved in every way possible.
I've always had a philosophy: data must always be restorable (and as quickly as possible), in an open format (meaning you shouldn't have to buy anything to restore or consult it), and consistent. These points may seem obvious, but they are not.
I have encountered various scenarios of data loss:
Datacenters destroyed by fire
– I had 142 servers there, but they were all restored in just a few hours.
Server rooms flooded.
Servers destroyed in earthquakes, often due to collapsing walls.
Increasing incidents of various ransomware attacks.
Intentional damage by entities seeking to create problems.
Mistakes made by administrators, which can happen to anyone.
The risk escalates for servers connected to the internet, like e-commerce and email servers. Here, not only is data integrity crucial, but so is the uninterrupted operation of services. This series of posts will revisit some of my old articles to explain my core ideas on the subject and describe, at least in part, my primary techniques.
Many consider a backup to be a simple copy. I often hear people say they have backups because they "copy the data", but this is often wrong and extremely dangerous, providing a false sense of security. Copying the files of a live database is an almost useless operation, as the result will nearly always be impossible to restore. It is essential to at least perform a proper dump and then transfer that file. Yet, many people do this and will only realize their mistake when they face an emergency and need to restore.
The Backup Plan: Asking the Right Questions
Before touching a single file, you must start with a plan, and that plan starts with asking the right questions:
"How much risk am I willing to take? What data do I need to protect? What downtime can I tolerate in case of data loss? What type and amount of storage space do I have available?"
The first question is particularly critical. A common but risky approach is to store a backup on the same machine that requires backing up. While convenient, this method fails in the event of a machine failure. Even relying on a classic USB drive for daily backups is not foolproof, as these devices are as susceptible to failure as any other hardware component. And contrary to popular belief, even high-end uninterruptible power supplies (UPS) are not immune to catastrophic failures.
Thus, the initial step is to establish a management plan, balancing security and cost. The safest backup is often the one stored farthest from the source machine. However, this approach introduces challenges related to space and bandwidth. While local area network (LAN) backups are relatively straightforward, off-network backups involve additional connectivity considerations. This might lead to a compromise on the amount of data backed up to maintain operational speed during both backup and recovery processes.
Safety doesn't always equate to practicality. For instance, with a 200 MBit/sec connection and 2 TB of backup data, the recovery time could be significant. However, if the goal is not rapid restorability but simply ensuring the data is available, the safest backup is often the one closest to us. That is, a backup we can "touch", disconnect, and consult even when offline.
Therefore, it is essential to develop a backup policy tailored to specific needs, keeping in mind that no 'perfect' solution exists.
The Core Decision: Full Disk vs. Individual Files
When planning a backup strategy, one key decision is whether to back up the entire disk or just individual files. Or both of them. Each approach has its pros and cons.
Entire Disk (or Storage) Backup
Advantages:
Complete Recovery: Restoring a full disk backup can quickly revert a system to its exact previous state, boot loader included.
Integration in Virtualization Systems: If your VM is a single file on a filesystem like ZFS or btrfs, you can simply copy that file (after taking a snapshot) to get a complete backup of the VM. Solutions like Proxmox offer easy management of full disk backups, accessible via command line or web interface.
Flexibility in Virtual Environments: Products like the Proxmox Backup Server offer the ability to recover individual files from a full backup, combining the benefits of both approaches.
Disadvantages:
Downtime for Physical Machines: Often, it's necessary to shut down the machine to create a full disk backup, leading to operational interruptions. A hybrid approach, if the physical host is running FreeBSD for example, is to take a snapshot and copy all the host's datasets. The restore process, however, will require some manual operations.
Large Space Requirements: Full disk backups can consume substantial space, including unnecessary data.
Potential Slowdowns and Compatibility Issues: The backup process can be slow and may encounter issues with non-standard file system configurations.
Individual File Backup
While it might seem simpler, backing up individual files can get complicated.
Advantages:
Basic Utility Use: Possible with standard system utilities like tar, cp, rsync, etc.
Granular Backups: Allows for backing up specific files and comparing them to previous versions.
Delta Copying: Only modified parts of the files are backed up, saving space and reducing data transfer.
Portability and Partial Recovery: Files can be moved individually and partially restored as needed.
Compression and Deduplication: These features are often available at the file or block level.
Operational Continuity: Can be done without shutting down the machine.
Disadvantages:
Storage Space Requirements: Simple copy solutions might require significant storage.
Need for File System Snapshot: For efficient and consistent backups, a snapshot (like native ZFS snapshots, btrfs, LVM Volume snapshots, or Microsoft's VSS) is highly recommended before copying.
Hidden Pitfalls: Issues may not become apparent until a backup is needed. And by then, it may be too late.
The Key to Consistency: The Power of Snapshots
Backing up a "live" file system involves a "start" and an "end" moment. During this time, the data can change, leading to fatal inconsistencies. I've encountered such issues in the past: a large MySQL database was compromised, and I was tasked with its recovery. I confidently took the client's last file-based backup and restored various files (not a native dump). Unsurprisingly, the database failed to restart. The large data file had changed too much between the start and end of the copy, rendering it inconsistent. Fortunately, I also had a proper dump, so I managed to recover from that.
The issue is evident: backing up a live file system is risky. An open database, even a basic one like a browser's history, is highly likely to get corrupted, making the backup useless.
The solution is to create a snapshot of the entire file system before beginning the backup. This approach freezes a consistent "point-in-time" view of the data. To date, using snapshots, I have managed to recover everything.
Here are the methods I've explored over the years:
Native File System Snapshot (e.g.,
BTRFS
or
ZFS
): If your file system inherently supports snapshots, it's wise to use this feature. It's likely to be the most efficient and technically sound option.
LVM Snapshot: For those using LVM, creating a snapshot of the logical volume is a viable approach. This method can lead to some space wastage and, while I still use it, has occasionally caused the file system to freeze during the snapshot's destruction, necessitating a reboot. This has been a rare but recurring issue across different hardware setups, especially under high I/O load.
DattoBD: I've tracked this tool since its inception. I used it extensively in the past, but I sometimes faced stability issues (kernel panics or the inability to delete snapshots, forcing a reboot). For snapshots with Datto, I often use UrBackup scripts, which are convenient and efficient.
The Architecture: Push or Pull?
A longstanding debate among experts is whether backups should be initiated by the client (push) or requested by the server (pull). In my view, it depends.
Generally, I prefer centralized backup systems on dedicated servers, maintained in highly secure environments with minimal services running. Therefore, I lean towards the "pull" method, where the server connects to the client to initiate the backup.
Ideally, the backup server should not be reachable from the outside. It should be protected, hardened, and only be able to reach the setups it needs to back up. The goal is to minimize the possibility that the backup data could be compromised or deleted in case the client machine itself is attacked (which, unfortunately, is not so rare).
This is not always possible, but there are ways to mitigate this problem. One way is to ensure that machines that must be backed up via "push" (i.e., by contacting the backup server themselves) can only access their own space. More importantly, the backup server, for security reasons, should maintain its own filesystem snapshots for a certain period. In this way, even in the worst-case scenario (workload compromised -> connection to backup server -> deletion of backups to demand a ransom), the backup server has its own snapshots. These server-side snapshots should not be accessible from the client host and should be kept long enough to ensure any compromise can be detected in time.
My Guiding Principles for a Good Backup System
Over the years, I've favored having granular control over backups, often finding the need to recover specific files or emails accidentally deleted by clients. A good backup system, in my opinion, should possess these key features:
Instant Recovery and Speed: The system should enable quick recovery and operate at a high processing speed.
External Storage: Backups must be stored externally, not on the same system being backed up. Still, local snapshots are a good idea for immediate rollbacks.
Security: I avoid using mainstream cloud storage services like Dropbox or Google Drive for primary backups. Own your data!
Efficient Space Management: This includes features like compression and deduplication.
Minimal Invasiveness: The system should require minimal additional components to function.
Conclusion: What's Next
The approach to backup is varied, and in this series, I will describe the main scenarios I usually face. I will start with the backup servers and their primary configurations, then move on to the various software and techniques I use.
But that will begin with
the next post, where I'm talk about building the backup server which, of course, will be powered by FreeBSD
- like all my backup servers for the last 20 years.
