---
title: "macOS 27.3 includes new privacy controls for Full Disk Access and more"
url: "https://9to5mac.com/2026/11/16/macos-27-3-includes-new-privacy-controls-for-full-disk-access-and-more/"
fetched_at: 2026-11-17T10:00:44.776726+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# macOS 27.3 includes new privacy controls for Full Disk Access and more

Source: https://9to5mac.com/2026/11/16/macos-27-3-includes-new-privacy-controls-for-full-disk-access-and-more/

Last month, Apple
announced
its plans to tighten macOS privacy controls around Full Disk Access amid the rise of “increasingly capable and autonomous” AI agents.
With today’s new macOS 27.3 beta, Apple is implementing several changes as part of this.
In a post on its
developer website last month
, Apple said some developers are “using Full Disk Access in ways that could put users at risk, exposing everything on their systems.” As such, it said that it would “introduce additional controls to ensure that users who genuinely wish to grant an app this extraordinary level of access can only do so with very explicit user action.”
What’s changing in macOS 27.3
In macOS 27.2, “Device Control and Data Access” is a unified toggle in System Settings, where Apple says that apps with that level of access can “view and send email, edit contacts and photos, monitor your keyboard, track websites, record your screen, control any app on your Mac, and more.”
In macOS 27.3, Apple is splitting “Device Control and Data Access” into two categories:
Accessibility: Intended specifically for assistive technologies, with permissions handled through an entitlement process.
System and App Protection Override: A new category for apps that need to bypass certain macOS protections to control other apps or perform automated tasks.
For the latter, users will be able to specify which apps an automation tool can access rather than granting it unrestricted control. For instance, you could give an app access to the Mail app, but not Messages.
macOS 27.3 also adds an option for users to require an app to request permission every time it needs access, rather than granting it access indefinitely.
Apple is also introducing a new menu bar indicator that will provide additional transparency when an app is controlling another app with System and App Protection Override. This is designed to let users know when an automation tool is interacting with apps and information in the background.
Full Disk Access isn’t going away
Crucially, Apple isn’t removing the ability to give an app Full Disk Access. If you deem it necessary, you can still give an app Full Disk Access. However, Apple is redesigning the approval process to make the implications of that decision more obvious.
macOS 27.3 will display a more detailed explanation about the protections being bypassed and the types of personal information that could be exposed.
Users can also choose to grant an app access to specific folders instead of their entire Mac. For example, an app that only needs to work with files in a particular folder won’t get unrestricted access to everything else.
Any app you’ve already given Full Disk Access will still have that access. Previously granted permissions will remain in effect, and those apps will continue functioning as they do today without any approval required.
Apple has
published a new support document
detailing the Full Disk Access updates.
For developers
Apple says the underlying APIs aren’t changing, but developers will need to update their apps to account for situations where users grant limited access rather than unrestricted permissions.
Finally, Apple says developers of backup apps and assistive technologies can request entitlements that allow them to maintain the same experience for new installations as before macOS 27.3. Apple has already identified popular apps that rely on these permissions, and those apps will continue working as expected without requiring an entitlement.
Developers can read more on
Apple’s Developer website.
My favorite Apple deals right now:
Follow Chance
:
Threads
,
X
, and
Instagram
FTC: We use income earning auto affiliate links.
More.
