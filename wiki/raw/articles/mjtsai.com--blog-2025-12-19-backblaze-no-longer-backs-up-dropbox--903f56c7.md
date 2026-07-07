---
title: "Backblaze No Longer Backs Up Dropbox"
url: "https://mjtsai.com/blog/2025/12/19/backblaze-no-longer-backs-up-dropbox/"
fetched_at: 2026-07-07T07:01:42.447049+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Backblaze No Longer Backs Up Dropbox

Source: https://mjtsai.com/blog/2025/12/19/backblaze-no-longer-backs-up-dropbox/

Rob Halliday
:
It appeared that Backblaze was now just not backing up Dropbox AT ALL, and was discarding (without warning) existing backups of Dropbox folders.
I contacted Backlbaze tech support. Janet their ‘AI Agent’ who is “well-trained to answer your questions” (!!), responded an hour or so later saying that Backblaze now basically do not back up Dropbox as of a recent update to the Mac Backup software.
[…]
Working back through the Backblaze release notes, this change happened in 9.2.2.878. The release notes page does not include release dates for software versions, so there is no way of telling when this change happened.
[…]
If I hadn’t discovered this by accident today, I might not have found out until too late. I suspect this is why I haven’t managed to find more outcry about it on the web today - I suspect this applies to a lot of people, who know this has been working fine and haven’t yet noticed that it’s now broken. Yes, it’s in the release notes, but a change like this should, I feel, be displayed VERY PROMINENTLY as part of an update, or an update causing a change this dramatic should not be forced on users automatically.
I’ve had
concerns about Backblaze
for a long time, but this is a new low.
Previously:
Update (
2025-12-22
): It seems like Backblaze now also excludes
iCloud
Drive
and
OneDrive
but not
Dropbox via Maestral
. This seems to
not
be due to Dropbox using the File Provider Extension framework, and it’s not overridable at the user level, so I guess there’s some sort of built-in exclusion.
CrashPlan
also no longer backs up Dropbox. Arq can still back up all this stuff.
Update (
2026-04-08
):
Backblaze
:
Recent updates to macOS and iCloud prevent us from backing up files that remain iCloud-managed, even if they appear “downloaded” in Finder.
This change affects files stored in iCloud Drive folders that macOS controls via cloud sync, including the ~/Library/Mobile Documents directory. Simply disabling “Optimize Mac Storage” alone is not sufficient anymore - files that remain inside iCloud-managed folders cannot be backed up due to Apple’s iCloud architecture restrictions.
[…]
This limitation is caused by Apple’s recent iCloud updates that restrict third-party backup access to cloud-managed locations. We can only back up local data and cannot override Apple’s iCloud controls.
I don’t understand why they are saying that the change is due to Apple and that it affects even files that
are
locally cached. Other apps are able to read the files, and other backup apps such as Arq are even able to temporarily materialize files that are not locally cached.
Update (
2026-04-09
): This claim is now in the
Backblaze documentation
:
iCloud’s most recent update prevents Backblaze from backing up files that iCloud synced.
To back up these files, download them to another local location where Backblaze can read them.
Update (
2026-04-14
):
Robert Reese
(via
Hacker News
):
No problem I thought, I’ll just restore this from Backblaze. Sadly it was not to be. At some point Backblaze had started to ignore
.git
folders.
This annoyed me. Firstly I needed that folder and Backblaze had let me down. Secondly within the Backblaze preferences I could find no way to re-enable this. In fact looking at the list of exclusions I could find no mention of
.git
whatsoever.
[…]
Well lesson learned I guess, but then a week ago I came across this thread on reddit: “
Doesn’t back up Dropbox folder??
”. A user was surprised to find their Dropbox folder no longer being backed up. Alarmed I logged into Backblaze, and lo and behold, my OneDrive folder was missing.
He’s a Windows user—so the change can’t be blamed on Apple—and quotes the
Backblaze release notes
as saying that cloud files are excluded to prevent “performance issues” and “excessive data usage.”
Update (
2026-04-21
):
natasha_backblaze
:
To give a bit more context on the “why”: these cloud storage providers now rely heavily on OS-level frameworks to manage sync state. On Windows, for example, files are often represented as reparse points via the Cloud Files API. While they can appear local, they are still system-managed placeholders, which makes it difficult to reliably back them up as standard on-disk files.
Moreover, we built our product in a way to not backup reparse points for two reasons:
We wanted the backup client to be light on the system and only back up needed user-generated files.
We wanted the service to be unlimited, so following reparse points would lead to us backing up tons of data in the cloud
We’ve made targeted investments where we can, for example, adding support for iCloud Drive by working within Apple’s model and supporting Google Drive, but extending that same level of support to third-party providers like Dropbox or OneDrive is more complex and not included in the current version.
Jim-From-Backblaze
:
First and foremost, Backblaze Computer Backup was built with one overarching goal in mind: to back up all of your data on Mac and Windows computers. To do it simply, easily, and without much user interaction needed.
This backup covers unlimited data on the computer itself as well as internal drives and external drives that are physically connected to the computer.
That part has not changed.
What has changed is how some third-party cloud-sync tools store files on your computer.
Modern tools like OneDrive and Dropbox don’t always keep full files locally anymore. A lot of the time, what you’re seeing in Explorer/Finder is a placeholder, basically a pointer back to the cloud, not the actual file sitting on disk.
This seems completely at odds with Backblaze excluding even files in cloud folders that are
not
pointers back to the cloud.
Update (
2026-05-01
):
Natasha Rabinov
:
We’ve successfully added support for iCloud Drive and Google Drive by working within those platforms’ models. Extending the same support to every sync provider is more complex, but it’s something we’re actively exploring.
Christian Selig
:
Dang Backblaze is memory hungry on Tahoe, what are we using 33 GB of RAM for?
See also:
Accidental Tech Podcast
.
Update (
2026-05-04
):
zkarj
:
I and others have checked and confirmed that stuff in Documents (and Desktop)
is
being backed up, but stuff in all other parts of iCloud Drive (e.g. the default folders for Pages, Numbers, etc) is
not
being backed up.
David Carlton
:
As per an interaction I had with Backblaze support, they’re intentionally not backing up files that are in directories under
com~apple~CloudDocs
, which is where standalone iCloud Drive directories live.
Ivan Drucker
:
I just discovered ~/Library/CloudDocs and ~/Library/Mobile Documents missing from a BackBlaze backup. Not happy. Using client 9.2.2.898.
[…]
Also, on their “Back Up iCloud Drive” support page, they now have a banner at the top which says “iCloud’s most recent update prevents Backblaze from backing up files that iCloud synced. To back up these files, download them to another local location where Backblaze can read them.” That seems to suggest no iCloud Drive support at all, and the whole thing reeks of nonsense, and it contradicts the rest of the page and the blog post saying they have iCloud Drive working. “iCloud’s most recent update?” What does that even mean?
Update (
2026-05-25
):
mikebhm
:
After setting it all up I remembered the Dropbox thread and asked Backblaze support for a clear statement about whether BB backs up iCloud Drive (assuming full size local copies present). The unequivocal answer is NO. You have to relocate the contents of iCloud Drive to a different location, which of course destroys the point of iCloud Drive.
Backblaze
Backup
Datacide
Dropbox
File Provider Extensions
Git
iCloud Drive
Mac
Mac App
macOS Tahoe 26
Microsoft OneDrive
24 Comments
