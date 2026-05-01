---
title: "Windows 11 after two decades of macOS: okay, but also awful"
url: "https://rakhim.exotext.com/windows-11-experience"
fetched_at: 2026-05-01T07:01:22.779050+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# Windows 11 after two decades of macOS: okay, but also awful

Source: https://rakhim.exotext.com/windows-11-experience

Recently my partner's trusty old 5K iMac died after 8.5 years of service (Radeon gpu is fried). At first I thought it was finally time to get one of those cool little M4 Mac Minis, but then decided to conduct an experiment. I gave up my Mac Studio M2 Max (64 Gb unified memory and 1 Tb storage) and tried to use my Windows PC as the main machine.
I originally purchased it to learn Unreal Engine and to play games. Let's try to use it for everything else: programming (Rust, TypeScript, Node), music production, photo editing, paperwork, general web browsing, writing.
Long story short: it's not as bad as I thought, but it's still painful. I can totally be productive and, in some areas, even more so than in macOS. Given choice, I'd still pick a Mac though (but
Tahoe
is making things harder).
The other parts of the setup are:
Lenovo Y32p-30, kinda meh 32" 4K display with 144Hz refresh rate. The software is atrocious btw.
Logitech Ergo K860 keyboard
Wired Corsair mouse (I feel like a crazy person, but I cannot use a wireless mouse with macOS since forever; more on that later)
ADAM Audio D3V studio speakers
Universal Audio Volt 1 interface
My Windows PC is pretty beefy for my needs, and in most aspects more powerful than Mac Studio:
Ryzen 5 9600X CPU
GeForce RTX 5070 Ti GPU
WD Blue NVMe SSD 1TB
32 GB DDR5 RAM
packed in a very nice white Deepcool CH160 case
But macOS is also bad
Before I continue rambling about the good and the bad parts of Windows, let me clarify: I don't think macOS is perfect or even excellent. It's
pretty good
. Over the years, I've had a lot of issues, including:
When suing wireless mice (2.4 ghz),
cursor regularly stutters
and jumps. This started with a 2010 Macbook Pro, and I could never fix it. I've tried multiple brands of mice, I've tried different USB extenders and docks, I've tried putting the receiver literally within 10 cm from the mouse. Multiple macbooks, mac mini, iMac, it doesn't matter. I hate the feeling of bluetooth mice, so for years now I'm using a wired gaming mouse.
All desktop macs I had would randomly
refuse to sleep
on first try. Sometimes it takes 3-4 attempts to make it actually sleep.
Network SMB shares
don't stay connected consistently, especially after reboots. (it's the opposite on Windows, works very reliably there)
Time Machine
(local usb drive, not even a network share) would silently stop backing up files, with zero indication of any issue. I stopped trusting it altogether.
Finder UI is slow
and often has a delay, e.g. press enter to rename a file, start typing immediately, and first 1-2 characters are not registered.
Tahoe
looks like a cheap knock off toy
Even after significant time spent in Windows doing regular things, I find myself deeply uncomfortable mainly due to two aspects: Things 3 app and keyboard bindings.
Things 3
is the best todo app in the world, for me. I've purchased it almost a decade ago and have been using it every day. It is complete, and no other app comes close to the level of usability and polish. Also, it was a one-time purchase, not a subscription, even though it comes with cloud syncing feature.
The biggest challenge that cannot be resolved ever is keyboard bindings. It's one of the best usability features of macOS: most operations are done with
cmd
key,
opt
is consistently used for additional level of options, and neither one interferes with
ctrl
. GUI and Terminal bindings co-exist nicely.
Navigating text with
cmd
and
alt
and
shift
became very natural to me. And yes, before you say anything: I've used vim for about a year in the past (it was before nvim existed!), and I've used Emacs for couple of years, even made a Mac-centric distribution called
Castlemacs
. I dislike modal editing, and I'm not a fan of Emacs-style bindings. Yes, moving by word and by line is not very efficient, but I don't care. I'm fast enough, speed of typing and jumping was never a bottleneck for me.
Here are some common keyboard shortcuts across the two OSes. Notice how consistently
cmd
is utilized.
Action
macOS
Windows
Start of line
cmd ←
home
End of line
cmd →
end
Word back
opt ←
ctrl ←
Word forward
opt →
ctrl →
Top of file
cmd ↑
ctrl home
End of file
cmd ↓
ctrl end
Switch windows
cmd tab
alt tab
Copy/paste
cmd c
/
cmd v
ctrl c
/
ctrl v
Open file
cmd ↓
enter
Up directory
cmd ↑
alt ↑
Close tab
cmd w
ctrl w
Close app
cmd q
alt f4
Minimize window
cmd m
win ↓
Hide window
cmd h
win d
The first week in Windows I decided to not go against the flow and try to adapt to the native bindings. I have a full-size keyboard, so I do have those
home
and
end
keys handy. But I couldn't. It's just not comfortable to reach for 4 different buttons.
Having to use
ctrl
for clipboard and
alt
for switching between windows also felt very unnatural. It's a very common action: copy, switch to another app, paste. In macOS, this can be done with the thumb sitting on
cmd
and quickly firing three presses:
cmd c
,
cmd tab
,
cmd v
. In Windows, you have to switch between two buttons which aren't even next to each other.
I've switched
ctrl
and
alt
using SharpKeys (also, CapsLock to Control):
And added a custom shortcut
ctrl tab
to act like
alt tab
using
PowerToys
, a nice collection of small utilities.
This way muscle memory is intact, but I lose the existing
ctrl tab
combo for switching between browser or text editor tabs. In addition, some Windows 2000 style apps and windows don't register this new mapping. Sometimes I'd switch to another app and won't be able to switch back until I reach for the actual
alt
key.
So it's all very finnicky.
There's a powerful scripting platform called
AutoHotKey
. Someone had shared a pretty feature-rich
script
that brings most mac-style key bindings to Windows. It mostly works, but the devil is in the details. For example, in macOS I can be in the middle of the line of text, press
cmd shift →
(select until the end of line), then while keeping
shift
press
alt ←
twice (unselect two words back). This isn't an artificial example, I do stuff like this all the time. This ahk script works for the first back-word jump, but on the second jump it removes the selection. The cursor moves as expected, but the selection is lost even though
shift
is still down. I've seemingly fixed this issue, but something else broke. In addition, my new obsession (
Arc Raiders
) treats AutoHotKey as a weapon of cheaters (which it can be), so I have to disable it before running the game. I wrote a
.bat
file (yeah, those are totally a thing still!) that shuts down AutoHotKey, runs the game, stays in the background, and restarts AutoHotKey after the game shuts down.
At this point I realized I'm fiddling with the computer just like I did with FreeBSD and Linux back in high school in early 2000s. Back then it was fun, but now it feels like wasted time.
The good
Let's start with the good stuff.
Windows Explorer
The file explorer is for the most part much better than Mac's Finder. It's easier to navigate, create new files, switch views. Unlike mac, Windows can remember and mount network SMB shares consistently.
Task bar
Windows task bar still feels like home. It makes sense, it's easy to see windows of running apps, and you get automatic shortcuts with
Win+1
,
Win+2
, etc. to either run or switch to running apps at the corresponding location in the task bar.
winget
Winget is a native package manager. Windows has a package manager! That's very cool. I found 95% of software I needed in the winget registry. It's easy:
winget install -e --id SublimeHQ.SublimeText.4
winget install -e --id Valve.Steam
Unlike apt or brew, most software is installed via the same old "Installer" msi, a fully GUI-driven process. Winget just makes it easier to get to that point, so you don't have to fish out the file download links from various websites.
Third-party software
There are some excellent pieces of software that only exist for Windows.
File Pilot
is an amazing file explorer. I would pay a lot of money to have this on mac. Luckily, the author actually wants to bring it to macOS at some point.
Everything
is a file search utility that feels like magic, especially compared to the built-in search in Windows. Think of it as visual fzf. It's extremely fast.
There are some apps I no longer use, but still worth to mention:
MusicBee
and
foobar 2000
.
It's nice too see some old-school whimsy, too.
Native screen resolution scaling
Windows can scale the monitor resolution to arbitrary percent, and things
generally
looks okay. On macOS, when using a 4K monitor you have these options:
Enjoy sharp text but huge UI by selecting 1080 logical resolution.
Tolerate awful text rendering by selecting any other resolution.
Install
BetterDisplay
.
I can't go back to under 120Hz screens, and don't want to pay so much for a 5K 120+Hz screen, so 4K it is. Windows does not require any 3rd party software to make things scale, but... Oh wait, this is the "Good" section. Let me explain what's wrong with monitors and scaling later.
Customizability
Lots of people dislike the new UI of Windows 11, and there are ways to heavily customize it with 3rd party solutions. I haven't tried any, because I think the UI is fine (the bigger problem is that the UI is inconsistent to a fault). But it's nice to know there are ways to change things. With macOS, I'm afraid there is no way but to eat (liquid) glass.
Window management
Built-in window management and tiling is pretty good. Or at least much better than macOS, which I can't use without 3rd party software like
Moom
,
Rectangle
, or
Better Touch Tool
.
Unreal Engine
Windows is the main platform for Unreal Engine, so unsurprisingly it works best there. I've tried running it on both macOS and Linux (Ubuntu and Fedora), and it never works well on either of those. On macOS it's noticeably slower (but sure, maybe M2 Max with 64 gigs is too weak). On Linux it's just buggy as hell (like, left mouse click requiring two clicks to register, and dropdown menus appearing with 500+ pixel offset from the click origin).
I've been learning Unreal and following some courses no problem. Like always, the worst part of any complex software project is a web view. The Epic Game Store which you are forced to use to get assets from Fab, is one of the worst pieces of software I had a displeasure of interacting with. It's amazing how in the background there is a fully-rendered high-resolution 3D world with particle effects and real-time shadows and reflections, and in the foreground a HTML page with some compressed jpegs struggles to scroll at 10 fps.
This feels exactly like Nintendo eShop on the Switch. Games run great even, eShop barely moves.
Anyway, Unreal Engine on Windows is a fine experience.
Gaming
I've been playing a lot of Arc Raiders lately, and never had any problems. This is my first PC since, gosh, 2008 or so, and it's absolutely mindblowing to me that I can alt+tab from a game with zero issues!
Phone link
Phone link is a way to connect a smartphone to the PC via Bluetooth to get notifications and share files. It works surprisingly well, BUT my iPhone did not like it. After few hours, airpods connected to the iPhone would start crackling like crazy. I had to disable Phone link to fix it.
WSL
Windows Subsystem for Linux is a very interesting technology. With WSL2, we basically get light-weight virtual machines with automatic cross-platform sharing of certain resources. In a few minutes, I was able to set up an instance of Ubuntu and run several projects, including Rust and TypeScript+Cloudflare Workers setups.
Linux's filesystem is mounted to Windows, so you can access them just like any other drive in File explorer. And vice-versa, the C drive of Windows is mounted into Linux. But this link is slow. So, to work on my projects with Sublime or VS Code, I could open the files directly, but searching and other operations across multiple files feel sluggish. Microsoft made it easy with VS Code though: if you open a directory from within Linux with
code .
, the Windows version of VS Code will start and connect to the (essentially) remote Linux file system. It all feels a bit convoluted, but just works.
By default, all Windows apps are added to
PATH
. You can run
notepad.exe
from the Linux terminal, for example, and even pass parameters or files to supported apps. As a result, my
PATH
would grow uncontrollably. Also, stuff like
git
or
node
would be found twice, because I had them installed on both sides.
In the spirit of coming back to Windows, I decided to try a full-blown IDE: JetBrains WebStorm. I didn't find an equivalent "remote" connection, so I just opened the project as is, by pointing the Windows-based IDE to the mounted Linux fs. It started indexing files, choked, and froze. After disabling indexing, I was able to use the IDE and make the edits, and even take advantage of nice refactoring tools, but then faced another issue: WebStorm's git feature would error out. I later found out that having git installed in Windows while also having another instance installed in WSL would cause issues.
I backup my machines with Backblaze. It would backup the vhdx file, but naturally you won't see the actual contents unless you mount it back. This means all of my programming projects files are jailed behind that abstraction of WSL. You can run whatever backup software inside the WSL instance, of course.
Some modern CLI tools want you to login with a web-browser (like Cloudflare's Wrangler or any coding LLM). This flow sometimes wouldn't work, and the solution that keeps coming up in discussions online is...
install a browser
inside WSL.
WSL can actually run GUI apps!
You can run that WebStorm or whatever editor/IDE from inside the Linux VM, and it would render into Windows just like any other app. GUI Linux apps appear in the Windows start menu as if they are native. It's mind-blowing, and a tremendous technological achievement. I had no other choice but to use it for
Sublime Merge
, my favorite git client. It works, but it needs a separate config for scaling, otherwise on my 4K monitor at 150% scaling all those Linux GUI apps look tiny.
WSL's filesystem is stored in a
vhdx
file. It can grow dynamically, but as far as I understand it can't shrink automatically. So it may take up more space than needed. There are ways to compact it but this requires shutting down the WSL instance and running some commands or software.
And this was the theme of the next few weeks: WSL works fine, but issues keep coming up. Nothing catastrophic, and most things can be solved with some googling. Though at some point I rememberd the feeling I had while using Windows 95 through 7 (the last one I had on my personal computer before switching to Macs). Tinkering, Googling, reading obscure forums, editing the registry... WSL tries very hard to maintain an illusion of complete smooth integration between the two worlds, but these issues break immersion and distract from work.
The bad
Well, I knew it, you knew it, everybody knows it. Windows is not a high quality product. I really wanted to like it, and I geniunely loved some aspects of it. But there are so, so many bugs and bad design decisions, it's a death by twenty thousand cuts.
Installation
You must login into your Microsoft account during installation. There are still ways around it, and I was able to take advantage of one, but it's utterly ridiculous.
Funny thing is: I was also installing the same copy of Windows on an older laptop, and the installer didn't recognize the WiFi card, so it simply allowed to continue because there is no internet. But if it recognizes your WiFi card (or the network card with an active ethernet connection), then you have no choice but to authenticate.
Honestly, I don't care that much. I'm signed into my Apple account on all Apple devices. The reason I hate this so much in Windows is that it assigns the username and home folder from the Microsoft account email. So, my home directory was
windo
because those are the first 5 letters of the email address I'd used for my Microsoft account. What the hell is that?!
Keyboard layouts
I live in Finland. I speak English. I need two keyboard layouts: US English and Finnish. I spent about two hours trying to achieve this.
The starting point is that I have a single "Language" pack on the system, with a single keyboard layout (US English).
Now, go to "Keyboards", click "Add a keyboard" (strange wording, but ok), add "Finnish QWERTY". The result: 4 keyboard layouts.
By the way, I have no idea what those words mean: ENG, English, Finnish. Which one indicates the layout?!
OK now delete the Finnish keyboard. The result: 3 English keyboard layouts remain.
Here's the best part: there is no simple way to remove those 2 additional layouts. You are stuck with three variants of English.
There is a registry edit trick and alternatively a PowerShell comamnd that can help get rid of everything except for one layout:
Set-WinUserLanguageList -LanguageList (New-WinUserLanguageList -Language -en-US) -Force
This requires a system restart, by the way. But how do normal people solve this? And also how do normal people get exactly two or three layouts that they need? (like those weird foreigners who speak multiple languages.)
This is the algorithm:
Add "keyboards" that you need.
Look at the resulting list of layouts and remember the ones you don't need.
Add "keyboard" that corresponds to those. You have to choose exactly the same wording as in those extra layouts. Adding them will not create additional layouts.
Now go and delete those newly added keyboards.
In my case, I had to add "English (United States) United States-international" and "English (United Kingdom) Finnish" and then delete them. Only this way I ended up with exactly two layouts.
I'm not making this shit up. Forums and full of discussions about this issue.
Scaling issues
As I mentioned in the good part, native screen resolution scaling is mostly good. But in some UI elements and on some websites the text is horribly rendered. Turns out selecting 150% scaling and selecing custom scaling set to the same 150% yield very different results. The latter fixes the majority of blurry fonts. Interestingly, if you choose custom scaling, the menu setting shows 350% regardless of your custom value. That is not true value, but some sort of buggy placeholder.
Ugly font rendering
I use a
simple css rule
on my homepage that aims to utilize system fonts whenever possible. This way the text should look decent enough on any platform. It looks great on macOS and major Linux distros, but it looks horrible on Windows 11.
Here are the fonts stacks I use:
ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

Iowan Old Style, Apple Garamond, Baskerville, Times New Roman, Droid Serif, Times, Source Serif Pro, serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol;
This is how my homepage looks on Windows 11:
And in macOS Sequoia:
You can improve this by selecting a different stack.
modernfontstacks.com
has a nice collection, and
their github page
has screenshots from various platforms, making it easier to make the best choice.
It's not fair to blame Windows for the choice of CSS that I made myself, but this kind of caught me off guard. My other projects (
minifeed.net
and
exotext.com
where you are reading this blog) look like ass on Windows, too, even though they are utilizing a different set of fonts. Whatever I choose looks wrong.
Browsing the web in general, lots of sites look unpleasant unless they use 3rd party fonts. Even good old verdana on HackerNews renders ugly. But this is a niche, personal problem. Most people don't care and I'm not being dismissive here, I think it's absolutely ok not to care.
Display brightness (DDC/CI) issues
After many attempts I gave up trying to make Windows' native brighntess control buttons work for my external display. On macOS, fantastic
Better Display
takes care of it. Every single Linux distro I've tried (Ubuntu, Fedora, PopOS, Bazzite, Mint) just works out of the box. Windows is the only system for which the actual Lenovo software and drivers exist.
(By the way, that
Lenovo software
is comically bad. The 1.6/5 rating on Windows store feels too genorous.)
I settled with
twinkletray
, a little tray app that detects DDC/CI capabilities of the monitor and allows you adjust brighntess with a slider or by scrolling up and down on the icon. You can setup custom key bindings, but unfortunately there is no simple way to re-bind Windows' native brighntess keys (F1-F2). They just show the native brighntess bar, but have no effect on the actual brightess.
UI inconsistencies and layers
Each new version of Windows adds a new UI framework and updates
some
parts of the system. By now, in Windows 11, there are at least half dozen different UI conventions. It's a mess, and it's jarring.
For example, the old control panel exists alognside the new Settings app. They are not equivalent: some things can only be configured in one, some in the other. Some links from the control panel open sections of the Settings app; and vice versa.
The list of installed apps in the Control panel shows more apps than Settings. Resizing the Settings app horizontally results in a horrible stutter at 5fps.
Some windows got the new headers but kept Windows 7 (?) era buttons.
Some go all the way to 2000.
The newly designed context (right click) menu is very limited. The actual full menu is behind an additional click ("Show more options").
That full menu is from another century (but at least it renders faster).
After diggin into the control panel, I'd find things I never knew existed.
Third party software is also like that. The Windows experience throughout the day feels like switching between multiple virtual machines running different operating systems. UI, fonts, sizes: anything can be anything.
Disk labels
Windows uses letter labels for mounted disks. I still remember having
A
drive for a floppy disk in my first Windows 95 machine! By default, labels are assigned automatically as you mount devices. I have an external SSD which got the letter
D
. I set up some programs to use it for storage. Later that week I had to disconnect it. Later still I had mounted an encrypted volume (via
Cryptomator
) and it got assigned the same label
D
because at the time it was the next available letter. The programs that expected my external SSD started re-downloading files they couldn't find and saving them into my encrypted volume.
There are ways to assign permanent labels, but the default behavior is not good.
Start menu confusion
The start menu is just weird now. It's a dynamic collection of stuff, but also allows you to search for anything, and even includes web search by default. It also shows "Recommendations" which you cannot disable in settings (only with a registry hack). Here I have them disabled because what is this, a restaurant? Recommending apps is an alient concept that doesn't make sense. It's not like I open the Start menu and look for interesting apps to run.
"Is this Notepad.exe any good? Okay then, I'll take it, with a side of Calculator, please"
There is a separate Search menu (Win+S). It looks very similar and typing stuff there shows almost the same results.
Just... bugs
Sometimes after sleeping some taskbar icons disappear. Doesn't matter if the app is running or not. I have found bug reports on forums dating to 2021.
Window resize targets are competing with
Tahoe
.
Switching to/from dark mode sometimes doesn't render fully.
Updates just fail with no explanation. Then succeed after a dozen attempts.
I now dual-boot Windows 11 and Fedora Linux on that PC, but unfortunately Linux cannot be my main machine either. Unreal Engine does not work properly, and Ableton Live simply does not exist for Linux.
In the end, I decided to stop forcing myself and purchased a used M1 Macbook Air (16 Gb version, luckily), from which I am typing this. I'll keep an eye on the upcoming M5 models for the main workstation, but for occasional mobile use this "old" little M1 laptop is great.
Windows 11 could've been a fantastic OS. Instead of pushing AI crap and adding Copilot to Notepad (
I kid you not
), Microsoft could focus on fixing multi-year bugs and cleaning up the UI mess. There is so much good stuff in there, so much potential. There is so many talented programmers creating fantastic software.
Curious to see how this platform evolves further. But I don't have high hopes, neither for Windows nor for macOS. The world runs on desktops, but both Apple and Microsoft seem to actively despise it.
