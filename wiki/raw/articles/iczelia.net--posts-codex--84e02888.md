---
title: "Dissecting a CODEX crack"
url: "https://iczelia.net/posts/codex/"
fetched_at: 2026-05-05T07:01:23.445911+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Dissecting a CODEX crack

Source: https://iczelia.net/posts/codex/

Today I got my hands on a CODEX crack for Europa Universalis IV. Of course, I’m well known for not using things for their intended purpose, so I decided to dissect it and see what’s inside. This short post will describe my thought process and workflow.
First steps
⌗
This is how the directory with all the files inside it looks like:
Because Windows Defender seems to complain, I disable it and proceed to mount the ISO. There are a bunch of files here, but we’re interested mainly in
setup.exe
and
setup-1.bin
.
The CODEX directory seems to contain some game-related files that aren’t really relevant to our topic. I start by launching the crack inside a sandbox, inside of a virtual machine:
Wow!
It looks really good. It also bundles really good music (for keygen standards, anyway). Let’s dig deeper then. After dropping the binary inside a bunch of tools, I concluded that it’s a binary produced by Inno Setup.
We can see a bunch of interesting things here. The string table values oddly remind me of Borland RTL. The second and third screens zoom on the
DVCLAL
resource (which is embedded by Borland tools into every binary as a form of checking if they were made using a legimiate version of the tooling). Finally,
PACKAGEINFO
makes it clear that this is a VCL application.
The manifest also says something about InnoSetup. Let’s verify if this file is an InnoSetup installer:
Scanning -> E:\setup.exe
File Type : 32-Bit Exe (Subsystem : Win GUI / 2), Size : 7372832 (0708020h) Byte(s) | Machine: 0x14C (I386)
Compilation TimeStamp : 0x506A75C4 -> Tue 02nd Oct 2012 05:04:04 (GMT)
[TimeStamp] 0x506A75C4 -> Tue 02nd Oct 2012 05:04:04 (GMT) | PE Header | - | Offset: 0x00000108 | VA: 0x00400108 | -
-> File has 7204384 (06DEE20h) bytes of appended data starting at offset 029200h
[LoadConfig] CodeIntegrity -> Flags 0xA3F0 | Catalog 0x46 (70) | Catalog Offset 0x2000001 | Reserved 0x46A4A0
[LoadConfig] GuardAddressTakenIatEntryTable 0x8000011 | Count 0x46A558 (4629848)
[LoadConfig] GuardLongJumpTargetTable 0x8000001 | Count 0x46A5F8 (4630008)
[LoadConfig] HybridMetadataPointer 0x8000011 | DynamicValueRelocTable 0x46A66C
[LoadConfig] FailFastIndirectProc 0x8000011 | FailFastPointer 0x46C360
[LoadConfig] UnknownZero1 0x8000011
[File Heuristics] -> Flag #1 : 00000000000001001100000000100101 (0x0004C025)
[Entrypoint Section Entropy] : 6.04 (section #1) ".itext  " | Size : 0xBE8 (3048) byte(s)
[DllCharacteristics] -> Flag : (0x8000) -> TSA
[SectionCount] 8 (0x8) | ImageSize 0x33000 (208896) byte(s)
[VersionInfo] Product Name : Europa Universalis IV Leviathan                             
[VersionInfo] File Description : Europa Universalis IV Leviathan Setup                       
[VersionInfo] Version Comments : This installation was built with Inno Setup.
[ModuleReport] [IAT] Modules -> oleaut32.dll | advapi32.dll | user32.dll | kernel32.dll | kernel32.dll | user32.dll | kernel32.dll | advapi32.dll | comctl32.dll | kernel32.dll | advapi32.dll | oleaut32.dll
[-= Installer =-] Inno Setup v5.5.0 Module
[CompilerDetect] -> Borland Delphi
- Scan Took : 0.141 Second(s) [00000008Dh (141) tick(s)] [566 of 580 scan(s) done]
Seems like I was right. Let’s unpack the installer then:
C:\codex>inno_unpacker -v D:\setup.exe
; Version detected: 5500 (Unicode) (Custom)
Size        Time              Filename
--------------------------------------
    456704  2011.12.31 16:01  {tmp}\ISDone.dll
     15808  2015.03.09 16:40  {tmp}\english.ini
     45725  2015.02.25 20:15  {tmp}\Style.vsf
   2039808  2015.09.30 05:32  {tmp}\VclStylesinno.dll
    110207  2014.12.22 16:54  {tmp}\BASS.dll
    132608  2013.11.22 16:09  {tmp}\bp.dll
     28160  2012.04.30 01:49  {tmp}\wintb.dll
   5528548  2020.06.08 15:33  {tmp}\Music.ogg
       540  2015.03.11 08:27  {tmp}\Play1.bmp
       540  2015.03.11 08:28  {tmp}\Play2.bmp
       540  2015.03.11 08:28  {tmp}\Play3.bmp
       540  2015.03.11 08:24  {tmp}\Pause1.bmp
       540  2015.03.11 08:24  {tmp}\Pause2.bmp
       540  2015.03.11 08:24  {tmp}\Pause3.bmp
       776  2015.03.11 08:30  {tmp}\trackBkg.bmp
       344  2015.03.11 08:30  {tmp}\trackbtn1.bmp
       344  2015.03.11 08:30  {tmp}\trackbtn2.bmp
       344  2015.03.11 08:29  {tmp}\trackbtn3.bmp
    376832  2015.03.02 13:42  {tmp}\unarc.dll
      4948  2021.06.20 14:17  install_script.iss
--------------------------------------

C:\codex>inno_unpacker -x D:\setup.exe
Let’s check the contents of the install script. We’re just looking around with no real goal, so it won’t hurt to check it:
;InnoSetupVersion=5.5.0 (Unicode)

[Setup]
AppName=Europa Universalis IV Leviathan
AppVerName=Europa Universalis IV Leviathan
AppId=Europa Universalis IV Leviathan
DefaultDirName={code:DefDirWiz}
DefaultGroupName=Europa Universalis IV Leviathan
OutputBaseFilename=setup
Compression=lzma
Uninstallable=Unnin
AllowNoIcons=yes
WizardImageFile=embedded\WizardImage0.bmp
WizardSmallImageFile=embedded\WizardSmallImage0.bmp

[Files]
Source: "{tmp}\ISDone.dll"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\english.ini"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Style.vsf"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\VclStylesinno.dll"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\BASS.dll"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\bp.dll"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\wintb.dll"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Music.ogg"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Play1.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Play2.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Play3.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Pause1.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Pause2.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\Pause3.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\trackBkg.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\trackbtn1.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\trackbtn2.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\trackbtn3.bmp"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 
Source: "{tmp}\unarc.dll"; DestDir: "{tmp}"; MinVersion: 0.0,5.0; Flags: deleteafterinstall dontcopy 

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"; ValueName: "{app}\eu4.exe"; ValueType: String; ValueData: "RUNASADMIN"; Check: "CheckError"; MinVersion: 0.0,5.0; Flags: uninsdeletevalue uninsdeletekeyifempty 

[Icons]
Name: "{group}\{cm:UninstallProgram,Europa Universalis IV Leviathan}"; Filename: "{uninstallexe}"; Check: "Unnin and Start and CheckError"; MinVersion: 0.0,5.0; 
Name: "{userdesktop}\Europa Universalis IV Leviathan"; Filename: "{app}\eu4.exe"; Check: "Icon and CheckError"; MinVersion: 0.0,5.0; 
Name: "{group}\Europa Universalis IV Leviathan"; Filename: "{app}\eu4.exe"; Check: "Start and CheckError"; MinVersion: 0.0,5.0; 

[UninstallDelete]
Type: filesandordirs; Name: "{app}"; 

[CustomMessages]
English.NameAndVersion=%1 version %2
English.AdditionalIcons=Additional icons:
[...]
MemoReady=Waiting for Input...
InteProc=Cancel extraction?
Success=Successfully Installed
Fail=Installation Failed

[Languages]
; These files are stubs
; To achieve better results after recompilation, use the real language files
Name: "English"; MessagesFile: "embedded\English.isl";
Just about what I expected. The
{tmp}
directory is more interesting:
Here are my initial guesses for what each of these files are:
BASS.dll
- an audio library used for playing this sick tune in the background
bp.dll
- judging by exports, it’s an InnoSetup plugin that integrates music into the installers
ISDone.dll
- a library for unpacking things
Music.ogg
- the music we were looking for :)
Style.vsf
- VCL control styles used in the installer (I’m probably going to steal these for my future projects)
unarc.dll
- an unpacker for some archiving format? Seems to export
FreeArcExtract
.
VclStylesinno.dll
- an InnoSetup plugin that allows using custom VCL styles inside installers.
wintb.dll
- according to the exports, it’s something related to the taskbar.
You can download the VCL styles
here
, and the music
here
.
After copying the music over to my phone, I noticed that VLC labeled it as
Master Boot Record - ANSI.SYS
. I guess I’ll be listening to MBR more often.
Anyways, now that we have a big part of the entire process sorted out, there’s still the
setup-1.bin
file left. After opening it in a hex editor, we notice that it has a very specific header:
After looking for some clues online, it turns out that it’s a FreeArc archive. This would make a ton of sense, because we’ve seen a FreeArc decompressor earlier. Let’s try opening this file inside FreeArc then!
Oops. Well, if FreeArc doesn’t want to open this file, then surely we can open it using the libraries attached… But how? Because the file format already seems modified to me, I won’t trust any exising FreeArc source listings. Let’s drop the DLL inside Ghidra instead:
This function is really messy. And digging deeper doesn’t help! It seems like I’ll have to resort to online resources.
This
and
this
look like a good start. Turns out that my initial idea was right - and we just pass arguments to the unarchiver! Let’s quickly sketch up a tiny wrapper over this library.
To recap, the
FreeArcExtract
function takes a callback and a bunch of varargs that are later passed to the unarchiver as argv. The callback is called like so:
… so our callback is expected to take a string, two numbers and a string. As i’m not willing to dig deeper into this codebase, we will just print these and see what happens. We take the definition of the callback and function from the headers, alongside a simple main function:
Of course, since this is a vararg function, I’d have to whip out assembly to make it accept an arbitrary amount of parameters. But I don’t need to support that, so this chain of
if
s is fine. I tried to list the contents of the archive using
main l d:\setup-1.bin
, but this didn’t yield anything interesting, so i decided to test it instead.
read, 76, 80663645,
read, 76, 80663649,
write, 408, 428709076,
filename, 1, 1770550, map\random\tiles\data\tilepoh15_r.bmp
write, 410, 430479626,
filename, 1, 1770550, map\random\tiles\data\tilepoh28_h.bmp
write, 412, 432250176,
filename, 1, 1770550, map\random\tiles\data\tilepoh28_r.bmp
write, 413, 434020726,
filename, 5, 5308470, map\random\tiles\data\tilepoh15_p.bmp
write, 416, 436208347,
read, 77, 80744995,
read, 77, 80744999,
read, 77, 80745003,
read, 77, 80984329,
read, 77, 80984333,
read, 77, 80984337,
write, 418, 439329196,
filename, 5, 5308470, map\random\tiles\data\tilepoh28_p.bmp
write, 424, 444637666,
filename, 0, 885882, map\random\tiles\data\tilepoh16_h.bmp
read, 77, 81192459,
read, 77, 81192463,
read, 77, 81192467,
read, 77, 81276060,
read, 77, 81276064,
read, 77, 81276068,
write, 424, 445523548,
Okay, we need to filter out everything that doesn’t have the 4th argument out. It seemed to work, and we got a lot of output on stdout:
filename, 0, 16512, gfx\interface\achievements\achievement_colonial_management.dds
filename, 0, 16512, gfx\interface\achievements\achievement_cowardly_tactics.dds
filename, 0, 16512, gfx\interface\achievements\achievement_czechs_and_balances.dds
filename, 0, 16512, gfx\interface\achievements\achievement_dar_al_islam.dds
filename, 0, 16512, gfx\interface\achievements\achievement_david_the_builder.dds
filename, 0, 16512, gfx\interface\achievements\achievement_defender_of_the_faith.dds
filename, 0, 16512, gfx\interface\achievements\achievement_definitely_the_sultan_of_rum.dds
filename, 0, 16512, gfx\interface\achievements\achievement_die_please_die.dds
filename, 0, 16512, gfx\interface\achievements\achievement_disciples_of_enlightenment.dds
filename, 0, 16512, gfx\interface\achievements\achievement_dont_be_cilli.dds
Using the
x
flag, I decided to uncompress everything into the current directory. The entire process took a while.
The end
⌗
There’s nothing much left for me to explore. I believe that a different compression algorithm would work much better on this data, though. But since it takes quite a while to compress, and the data is around 5.1 GB, I gave up.
