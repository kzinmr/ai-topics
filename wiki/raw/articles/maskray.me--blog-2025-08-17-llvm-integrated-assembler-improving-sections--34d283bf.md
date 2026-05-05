---
title: "LLVM integrated assembler: Improving sections and symbols"
url: "https://maskray.me/blog/2025-08-17-llvm-integrated-assembler-improving-sections-and-symbols"
fetched_at: 2026-05-05T07:01:45.263599+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# LLVM integrated assembler: Improving sections and symbols

Source: https://maskray.me/blog/2025-08-17-llvm-integrated-assembler-improving-sections-and-symbols

In my previous post,
LLVM
integrated assembler: Improving expressions and relocations
delved
into enhancements made to LLVM's expression resolving and relocation
generation. This post covers recent refinements to MC, focusing on
sections and symbols.
Sections
Sections are named, contiguous blocks of code or data within an
object file. They allow you to logically group related parts of your
program. The assembler places code and data into these sections as it
processes the source file.
1
2
3
4
5
6
7
8
9
10
11
12
class
MCSection
{
...
enum
SectionVariant
{
SV_COFF =
0
,
SV_ELF,
SV_GOFF,
SV_MachO,
SV_Wasm,
SV_XCOFF,
SV_SPIRV,
SV_DXContainer,
};
In LLVM 20, the
MCSection
class
used an enum called
SectionVariant
to
differentiate between various object file formats, such as ELF, Mach-O,
and COFF. These subclasses are used in contexts where the section type
is known at compile-time, such as in
MCStreamer
and
MCObjectTargetWriter
.
This change eliminates the need for runtime type information (RTTI)
checks, simplifying the codebase and improving efficiency.
Additionally, the storage for fragments' fixups (adjustments to
addresses and offsets) has been moved into the
MCSection
class.
Symbols
Symbols are names that represent memory addresses or values.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
class
MCSymbol
{
protected
:
enum
SymbolKind
{
SymbolKindUnset,
SymbolKindCOFF,
SymbolKindELF,
SymbolKindGOFF,
SymbolKindMachO,
SymbolKindWasm,
SymbolKindXCOFF,
};
enum
Contents
:
uint8_t
{
SymContentsUnset,
SymContentsOffset,
SymContentsVariable,
SymContentsCommon,
SymContentsTargetCommon,
};
Similar to sections, the
MCSymbol
class
also used a discriminator enum, SymbolKind, to distinguish
between object file formats. This enum has also been removed.
Furthermore, the
MCSymbol
class had an
enum Contents
to specify the kind of symbol. This name was
a bit confusing, so it has been
renamed
to
enum Kind
for clarity.
A special enumerator,
SymContentsTargetCommon
, which was
used by AMDGPU for a specific type of common symbol, has also been
removed
.
The functionality it provided is now handled by updating
ELFObjectWriter
to respect the symbol's section index
(
SHN_AMDGPU_LDS
for this special AMDGPU symbol).
sizeof(MCSymbol)
has been reduced to 24 bytes on 64-bit
systems.
The previous blog post
LLVM
integrated assembler: Improving expressions and relocations
describes other changes:
The
MCSymbol::IsUsed
flag was a workaround for
detecting a subset of invalid reassignments and is
removed
.
The
MCSymbol::IsResolving
flag is added to detect
cyclic dependencies of equated symbols.
