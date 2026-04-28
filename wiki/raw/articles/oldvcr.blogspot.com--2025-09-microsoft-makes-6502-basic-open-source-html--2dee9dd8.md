---
title: "Microsoft makes 6502 BASIC open source"
url: "https://oldvcr.blogspot.com/2025/09/microsoft-makes-6502-basic-open-source.html"
fetched_at: 2026-04-28T07:02:04.617886+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Microsoft makes 6502 BASIC open source

Source: https://oldvcr.blogspot.com/2025/09/microsoft-makes-6502-basic-open-source.html

It was probably going to happen sooner or later, but Microsoft has
officially released the source code for 6502 BASIC
. The specific revision is very Commodore-centric: it's the 1977 "8K" BASIC variant "1.1," which Commodore users know better as BASIC V2.0, the same BASIC used in the early PET and with later spot changes from Commodore (including removing Bill Gates'
famous Easter egg
) in the VIC-20 and Commodore 64. I put "8K" in quotes because the 40-bit Microsoft Binary Format version, which is most familiar as the native floating point format for most 8-bit BASICs derived from Microsoft's and all Commodore BASICs from the PET on up, actually starts at 9K in size. In the C64, because there is RAM and I/O between the BASIC ROM and the Kernal ROM, there is an extra
JMP
at the end of the BASIC ROM to continue to the routine in the lowest portions of the Kernal ROM. The jump doesn't exist in the VIC-20 where the ROM is contiguous and as a result everything past that point is shifted by three bytes on the C64, the length of the instruction.
This is, of course, the same BASIC that Gates wanted a percentage of but Jack Tramiel famously refused to budge on the $25,000 one-time fee, claiming "I'm already married." Gates yielded to Tramiel, as most people did then, but I suspect the slight was never forgotten. Not until the 128 did Microsoft officially appear in the credits for Commodore BASIC, and then likely only as a way to push its bona fides as a low-end business computer. Microsoft's source release also includes changes from Commodore's own John Feagans, who rewrote the garbage collection routine, and was the original developer of the Commodore Kernal
and later Magic Desk
.
The source code is all in
one big file
(typical for the time) and supports
six machine models
, the first most likely a vapourware 6502 system never finished by Canadian company Semi-Tech Microelectronics (
STM
) better known for the CP/M-based Pied Piper, then the Apple II, the Commodore (in this case PET 2001), the Ohio Scientific (OSI) Challenger,
the Commodore/MOS KIM-1
, and most intriguingly a PDP-10-based simulator written by Paul Allen. The source code, in fact, was cross-assembled on a PDP-10 using MACRO-10, and when assembled for the PDP-10 emulator it actually emits a PDP-10 executable that traps on every instruction into the simulator linked with it — an interesting way of effectively accomplishing threaded code. A similar setup was used for their 8080 emulator. Unfortunately, I don't believe Allen's code has been released anywhere, though I'd love to be proven wrong if people know otherwise. Note that they presently don't even mention the STM port in
the Github README
, possibly because no one was sure what it did.
While MACRO-10 source for 6502 BASIC has circulated before and been analysed in detail,
most notably by Michael Steil
, this is nevertheless the first official release where it is truly open-source
under the MIT license
and Microsoft should be commended for doing so. This also makes it much easier to pull a BASIC up for your own 6502 homebrew system — there's nothing like the original.
