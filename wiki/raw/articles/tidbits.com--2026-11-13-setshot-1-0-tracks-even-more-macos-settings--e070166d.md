---
title: "SetShot 1.0 Tracks Even More macOS Settings"
url: "https://tidbits.com/2026/11/13/setshot-1-0-tracks-even-more-macos-settings/"
fetched_at: 2026-11-18T10:01:22.514690+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# SetShot 1.0 Tracks Even More macOS Settings

Source: https://tidbits.com/2026/11/13/setshot-1-0-tracks-even-more-macos-settings/

This past August, I did something I had never done before: released a full-fledged Mac app. Prompted by tech ghost stories about settings mysteriously changing during operating system updates, I spent months working with Claude Code to create a utility called SetShot that would reveal what settings change during macOS updates (see “
SetShot Tracks macOS Settings Changes
,” 19 August 2026). So far, I haven’t caught Apple red-handed, although I still hear chatter about configuration changes after users install updates.
Practically speaking, SetShot offers something never previously available to Mac users: the capability to identify and log settings changes over time, whether made by you, macOS, or some app. To that end, it takes and compares snapshots of numerous settings deep within macOS, reporting on what changed between them. It never changes any settings, so the worst it can do is tell you something you didn’t want to know.
I wasn’t confident enough to call that first version 1.0, so, like countless developers before me, I hedged by releasing 1.0b26 alongside that article. Since then, I have been adding to and refining SetShot, and although there is plenty more that could be done, I encourage you to download and try the official
SetShot 1.0
, which is free and
open source
. Cue the confetti and balloons!
What SetShot Does
When you take a snapshot, SetShot scans 20 sources of macOS system data, including over 500 preference files. It currently recognizes over 830 settings and knows to ignore as background noise over 1750 other items that macOS changes on its own. You can compare any two snapshots—usually the most recent two—to see what changed between them, or compare a snapshot against a built-in baseline captured from a clean install of macOS 15 Sequoia, macOS 26 Tahoe, or macOS 27 Golden Gate.
Each comparison lists every recognized change with its title, its location in System Settings, and its before-and-after values. Where possible, an Open in Settings button takes you directly to the appropriate pane in System Settings. If something seems off about the setting’s title, path, or values, you can click Submit Feedback to help me improve the SetShot knowledge base. Changes that SetShot doesn’t yet recognize appear in a separate section with their raw technical names and values. If you think one is a real setting, click Submit to send it to me for addition to the knowledge base.
Along the way, SetShot maintains the Journal, which is a chronological log of all recognized changes across your comparisons. Because your first snapshot is compared against the baseline, the Journal starts out with all your existing customizations. You can even export the Journal to HTML or Markdown to use as a checklist when setting up a new Mac to match your current one. (SetShot doesn’t write settings, so you’ll still be flipping switches by hand.)
You can take snapshots manually whenever you like, but SetShot can also take them automatically on a schedule you set in its Settings view. By default, SetShot deletes scheduled snapshots that contain no changes. When a scheduled snapshot finds a recognized change, SetShot displays a notification that you can click to run the comparison. I run snapshots frequently throughout the day for testing, but for most people, a daily check is sufficient.
If you’re running one of the betas, choose
SetShot > Check for Updates
to get 1.0. Versions before 1.0b32 biffed their automatic update checks, so they won’t find it on their own.
What’s New in 1.0
I have released eight beta updates since 1.0b26 with a slew of new features, interface tweaks, and bug fixes. You can read the gory details in the
release notes
, but the highlights include:
An actual
SetShot website
, wordy though it may be (so sue me)
Distribution via a disk image and a prompt to move the app to the Applications folder if it’s launched elsewhere to avoid macOS translocation, a security feature that runs newly downloaded apps from a hidden, randomly located copy and breaks some SetShot features (see “
Move Downloaded Mac Apps Before Initial Launch
,” 6 September 2022)
Faster snapshots, comparisons, and Journal display, plus the option to cancel a capture or comparison in progress
Support for macOS 27 Golden Gate, including a baseline snapshot
A
Help > Contact Support
option that makes it easy to report bugs or request features, plus a
SetShot > Settings
menu item, after John Gruber and others pointed out that an app about settings should probably have one
The option to ignore certain legitimate but chatty changes: audio devices, screenshot settings, and DNS changes
A bundled copy of the knowledge base so SetShot can describe changes even when it can’t reach the Internet on its first launch
Oodles of persnickety changes in the knowledge base, including tracking of login items, background activity, privacy permissions, security settings, wallpaper and screen saver changes, audio input and output devices, VPN and network connections, and much else (some of which require Full Disk Access)
VoiceOver support, Markdown export, and many other interface refinements and bug fixes, including the elimination of the vestigial View menu
What SetShot Has Turned Up So Far
Although I haven’t caught Apple changing a setting behind my back during an update, the betas have produced a few stories that show how macOS stores settings and just how much is going on in the background on our Macs.
When Mark Nagata, the coordinator of our Japanese translation team, first ran SetShot, his initial comparison reported 33,000 changes. Nearly all of them came from one file,
com.apple.audio.InfoHelper.plist
, which caches what each installed Audio Unit plug-in can do. Macs without audio plug-ins, like all of mine, lack that file, so SetShot didn’t know about it beforehand. Once I trained SetShot to ignore that file as noise, those changes disappeared from the comparison.
macOS did silently change one setting, although it wasn’t during an update. One day back in September, SetShot’s scheduled comparison reported that my default Web browser had changed from Arc to Safari. I had not made that change, but clicking links in other apps did in fact open them in Safari, even though
System Settings > Desktop & Dock
still reported Arc as the default Web browser. I don’t understand what happened here, but changing the default in System Settings to Brave and back to Arc fixed it.
When I upgraded to the beta of macOS 27.3, my first comparison in SetShot revealed hundreds of changes relating to Siri as Apple moved settings between preference files. I have marked them all as noise now, so you won’t see them, but it was interesting to get a glimpse of Apple moving things around in preparation for new features.
SetShot also featured in an amusing archaeological settings dig. While doing some testing, John Gruber of Daring Fireball changed his highlight color from the very specific blue he chose decades ago, but he was dismayed to discover he couldn’t restore his custom color because Apple had changed how the color picker works. SetShot showed his old RGB string changing to the word “Other,” which confirmed the change but didn’t help him undo it. He suggested that SetShot should report the
defaults
key so he didn’t have to figure out the appropriate
defaults write
command. It’s now on the list to look into.
Plans for Future Updates
I have various ideas for features to add, and several more have come from early users. In no particular order, they include:
Calculating statistics about the number of settings, how many have changed from defaults, and so on
Support for hidden
defaults write
settings that have no visible interface and can be changed only in Terminal or with utilities like
TinkerTool
or
Cocktail
Bob Harris’s suggestion of tracking the settings inside MDM configuration profiles so users on organization-managed Macs can tell what settings changes have been pushed by IT administrators
On the other side of the equation, a background-only version of SetShot that IT admins and Apple consultants could install on client machines to monitor changes and help troubleshoot problems
Scott-H5’s suggestion of tracking settings from VoiceOver Utility, which exposes hundreds of options that shape the VoiceOver experience
More generally, tracking settings for non-Apple apps that users choose
A gentle in-app nudge to support SetShot’s development by becoming a TidBITS member
Siri AI support
, once macOS 27.3 ships, so you can have it explain settings changes in more detail, answer questions about the Journal, and send comparison results to other apps
Some way to compare snapshots between Macs to make it easier to implement matching settings
Tweaks that make SetShot more fun, such as a quiz mode that challenges you to identify where certain settings live
Reading iOS settings from Finder backups so SetShot can support iPhones and iPads as well—the Holy Grail!
My enthusiasm for adding new features will be proportional to how much input and support I get from users. SetShot is free and open source because I harbor no illusions about its commercial potential, but I’m more likely to keep working on it if people who find it useful become
TidBITS members
and share their thoughts with me.
Give it a try
!
