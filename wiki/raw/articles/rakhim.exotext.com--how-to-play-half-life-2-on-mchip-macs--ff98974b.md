---
title: "How to play Half Life 1 and 2 on M-chip Macs"
url: "https://rakhim.exotext.com/how-to-play-half-life-2-on-mchip-macs"
fetched_at: 2026-04-29T07:01:21.012856+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# How to play Half Life 1 and 2 on M-chip Macs

Source: https://rakhim.exotext.com/how-to-play-half-life-2-on-mchip-macs

Half Life and Half Life 2 are my favorite games. I've played them through multiple times. I played Half Life 1 for the first time in 1999 or 2000, can't remember. My computer at the time could barely run it.
Nowadays, it's a struggle to play older PC games on a Mac. There are two fundamental issues:
A while ago macOS had dropped support for 32-bit applications.
Recently, Apple hardware migrated from Intel x86 to Arm architecture.
My machine is Mac Studio 2023 M2 Max 64GB RAM, running macOS 15.3.2.
In general, these are the options:
Try Wine, or wine-based tools like
Whisky
(free) or
Crossover
(paid).
Install Windows in a VM like Parallels.
Try to build a mac-native version.
Just buy a cheap PC and stop torturing yourself.
I did not have any success with barebones Wine or Whisky for Half Life 1 or 2. Crossover on the other hand — everything worked! HL1 runs great (look ma, maximum settings!). Can't believe that games is 27 years old. Wtf. Is this retro now?
Half Life 2 runs great too... I thought. You see, even with max settings, it's buttery-smooth until it's not. The first 10-20 minutes of the game there's little very action, and everything is good. But once explosions start happening, fps drops to single digits, and it's very annoying. Hard to enjoy it.
I've tried changing settings, and installing "DirectX for Modern Games", like someone recommended. Frames drop less, but still pretty badly.
Next I tried Parallels Desktop. It's a full-blown VM with an ARM-version of Windows 11. The OS itself runs without issues, it seems. I installed Steam into it, then installed Half Life 2, and it just runs fine! It's amazing because there are 2 layers of simulation happening. First there's the virtual machine, next there's x86 instruction set simulated on the ARM architecture. The amount of computation happening is staggering!
FPS is not great at max settings, but at least it's stable. You can probably get much better results with Parallels Pro, which does not limit VRAM to 8GB.
Parallels is not cheap though, and I'm not sure I need it for anything else. But hey, maybe play other games. And it's a subscription (of course), the Pro version is currently at €119.99 per year.
So I decided to try another way: you can actually build a version of HL2 natively on Mac thanks to the fact that Valve's Source engine has been leaked in the past. There's a
guide here
, but I faced some issues, so below is my updated guide.
Install Homebrew.
Install Xcode Command Line Tools
xcode-select --install
Install dependencies:
brew install sdl2 freetype2 fontconfig pkg-config opus jpeg jpeg-turbo libpng libedit python3
(you may already have
python3
though)
Clone source engine code
git clone --recursive https://github.com/nillerusr/source-engine
and cd into it.
Configure and build:
python3 waf configure -T release --prefix='' --build-games=hl2
python3 waf build
(there may be numerous warnings, it's ok)
Install into some directory:
python3 waf install --destdir='/users/<YOUR_USERNAME>/Games/Gaming/Half Life 2'
Now the tricky part. If you just install Half Life 2 from steam, you'll get the latest version, which does not work with this method. The game loads, but all fonts and textures are corrupted. You need to get specifically a "Pre-20th Anniversary build". So, buy the game if you haven't done it yet, then in your library press the gear icon → Properties → Betas and select this build.
Now download the game normally via Steam. Once donwload is complete, click on the gear icon again → Manage → Browse Local Files. This will open a directory where Steam had installed the game. Now perform the following file manipulations:
Move the
platform
directory to
~/Games/Gaming/Half Life 2
.
Move everything from
hl2
directory to
~/Games/Gaming/Half Life 2/hl2
except for the
bin
directory (it already exists in
~/Games/Gaming/Half Life 2/hl2/bin
).
Move
run.sh
file to
~/Games/Gaming/Half Life 2
.
Delete everything remaining in the Steam game directory.
Move everything from
~/Games/Gaming/Half Life 2
to the Steam game directory.
Rename
hl2_launcher
to
hl2_osx
.
This is how the final structure looks like:
├── bin
├── engine.log
├── ep2
├── episodic
├── hl2
│   ├── bin
│   ├── cfg
│   ├── demoheader.tmp
│   ├── downloadlists
│   ├── gameinfo.txt
│   ├── gamepadui
│   ├── ...
├── hl2.sh
├── hl2_osx
├── lostcoast
├── platform
└── steam_appid.txt
That's it. You should be able to run the game normally via Steam. I only played about 45 minutes so far, and it works without any issues. But I suspect something will break at some point.
