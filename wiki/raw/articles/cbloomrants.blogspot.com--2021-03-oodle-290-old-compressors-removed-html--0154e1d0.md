---
title: "Oodle 2.9.0 : old compressors removed"
url: "http://cbloomrants.blogspot.com/2021/03/oodle-290-old-compressors-removed.html"
fetched_at: 2026-05-05T07:01:47.875819+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Oodle 2.9.0 : old compressors removed

Source: http://cbloomrants.blogspot.com/2021/03/oodle-290-old-compressors-removed.html

Oodle 2.9.0 is now out.  The full changelog is :
## Release 2.9.0 - March 23, 2021

$* *fix* : OodleLZ_Compress had an encoder crash bug in the Optimal level encodes on data in sizes just slightly over a 256KB chunk (eg. 262145) with a repeated substring at the very end

$* *change* : Mac libs and dylibs are now fat binaries with x64 and ARM64
$* *change* : Tex : Oodle Texture no longer checks for license file
$* *change* : defining OODLE_IMPORT_LIB / OODLE_IMPORT_DLL is no longer needed; you can link with either type of lib without setting a define
$* *change* : Oodle public headers no longer define types like U8, SINTa, they are instead OO_U8, OO_SINTa, etc.
$* *change* : Oodle public headers now require stdint.h which on Windows/MSVC means VC2010 or higher

$* *change* : Net : OODLE_PLATFORM_HAS_SELECTDICTIONARYANDTRAIN define removed.  Call OodleNetwork1_SelectDictionarySupported instead.

$* *removed* : Core : support for the deprecated LZ compressors is now removed (LZH,LZA,etc.).  Only newlz (Kraken,Mermaid,Selkie,Leviathan,Hydra) and LZB16 are supported.
$* *removed* : Core : OodleLZ_CompressContext_* functions removed; streaming encoders no longer supported
$* *removed* : Ext : OODLEX_PATH_* public defines removed.
$* *removed* : Ext : OODLEX_WCHAR_SIZE public define removed.
$* *removed* : Tex : OodleTex_CheckLicense func removed ; Oodle Texture no longer checks for license files

$* *deprecation* : OodleConfigValues::m_OodleLZ_Small_Buffer_LZ_Fallback_Size no longer used; newlz compressors no longer ever drop down to LZB16 (default behavior unchanged)
The biggest change is the removal of all deprecated pre-Kraken compressors (LZH,LZHLW,LZNA,LZNIB,BitKnit,etc.) except for LZB16 which stays for the moment (but is also
deprecated).  Data compressed with the old codecs cannot be decoded by Oodle 2.9.0 ; up to Oodle 2.8.14 data
made by any earlier version can always be decoded by later versions.
Note that old versions of the Kraken-family of compressors still be decoded (Oodle 2.9.0 will read data written by Oodle 2.3 Kraken), and that will
always be the case, we never break reading old data (made by the supported codecs).
So if you are using the Kraken-family of compressors, you can always update to newer versions and your old data
will be readable.
If you were using one of the old codecs, we recommend changing to one of the Oceanic Cryptozoology codecs (Kraken, Mermaid, Selkie, Leviathan).
They are better in every way.  To do this, you need to decode that data with the old version of Oodle you have (or any version up through 2.8.14)
because 2.9.0 cannot decode the old codecs.  Assuming your old version is post-Kraken (2.1.5), you can re-encode to Kraken with your old sdk
and the current version (2.9.0) will be able to load that data.
If you can't switch codecs for some reason, you can always keep using the old version of Oodle you are currently on.
We have also designated the last version before 2.9.0 (which was 2.8.14) as a "long term support" release.  We will continue to push
critical bug fixes to 2.8.14.lts for people who need to stay on old codecs.
(2.8.14.lts has already received a bug fix since the 2.8.14 first release; clients on 2.8.14 should update to the latest version)
If at all possible we recommend everyone to get on the Oceanic Cryptozoology codecs and update to 2.9.0 ; if you need the old codecs we
recommend 2.8.14 for long term support.
LZB16 is still supported in 2.9.0 because some data may need it, but we strongly discourage its use.
