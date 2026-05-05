---
title: "LLVM integrated assembler: Improving MCExpr and MCValue"
url: "https://maskray.me/blog/2025-04-06-llvm-integrated-assembler-improving-mcexpr-mcvalue"
fetched_at: 2026-05-05T07:01:45.593732+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# LLVM integrated assembler: Improving MCExpr and MCValue

Source: https://maskray.me/blog/2025-04-06-llvm-integrated-assembler-improving-mcexpr-mcvalue

In my previous post,
Relocation
Generation in Assemblers
, I explored some key concepts behind
LLVM’s integrated assemblers. This post dives into recent improvements
I’ve made to refine that system.
The LLVM integrated assembler handles fixups and relocatable
expressions as distinct entities. Relocatable expressions, in
particular, are encoded using the
MCValue
class, which
originally looked like this:
1
2
3
4
5
class
MCValue
{
const
MCSymbolRefExpr *SymA =
nullptr
, *SymB =
nullptr
;
int64_t
Cst =
0
;
uint32_t
RefKind =
0
;
};
In this structure:
RefKind
acts as an optional relocation specifier,
though only a handful of targets actually use it.
SymA
represents an optional symbol reference (the
addend).
SymB
represents another optional symbol reference (the
subtrahend).
Cst
holds a constant value.
While functional, this design had its flaws. For one, the way
relocation specifiers were encoded varied across architectures:
Targets like COFF, Mach-O, and ELF's PowerPC, SystemZ, and X86 embed
the relocation specifier within
MCSymbolRefExpr *SymA
as
part of
SubclassData
.
Conversely, ELF targets such as AArch64, MIPS, and RISC-V store it
as a target-specific subclass of
MCTargetExpr
, and convert
it to
MCValue::RefKind
during
MCValue::evaluateAsRelocatable
.
Another issue was with
SymB
. Despite being typed as
const MCSymbolRefExpr *
, its
MCSymbolRefExpr::VariantKind
field went unused. This is
because expressions like
add - sub@got
are not
relocatable.
Over the weekend, I tackled these inconsistencies and reworked the
representation into something cleaner:
1
2
3
4
5
6
class
MCValue
{
const
MCSymbol *SymA =
nullptr
, *SymB =
nullptr
;
int64_t
Cst =
0
;
uint32_t
Specifier =
0
;
};
This updated design not only aligns more closely with the concept of
relocatable expressions but also shaves off some compiler time in LLVM.
The ambiguous
RefKind
has been renamed to
Specifier
for clarity. Additionally, targets that
previously encoded the relocation specifier within
MCSymbolRefExpr
(rather than using
MCTargetExpr
) can now access it directly via
MCValue::Specifier
.
To support this change, I made a few adjustments:
Streamlining Mach-O support
Mach-O assembler support in LLVM has accumulated significant
technical debt, impacting both target-specific and generic code. One
particularly nagging issue was the
const SectionAddrMap *Addrs
parameter in
MCExpr::evaluateAs*
functions. This parameter existed to
handle cross-section label differences, primarily for generating
(compact) unwind information in Mach-O. A typical example of this can be
seen in assembly like:
1
2
3
4
5
6
.section        __TEXT,__text,regular,pure_instructions
Leh_func_begin0:
.section        __TEXT,__eh_frame,coalesced,no_toc+strip_static_syms+live_support
Ltmp3:
Ltmp4 = Leh_func_begin0-Ltmp3
.long   Ltmp4
The
SectionAddrMap *Addrs
parameter always felt like a
clunky workaround to me. It wasn’t until I dug into the
Mach-O
AArch64 object writer
that I realized this hack wasn't necessary for
that writer. This discovery prompted a cleanup effort to remove the
dependency on
SectionAddrMap
for ARM and X86 and eliminate
the parameter:
While I was at it, I also tidied up
MCSymbolRefExpr
by
removing
the clunky
HasSubsectionsViaSymbolsBit
, further
simplifying the codebase.
Stremlining InstPrinter
The MCExpr code also determines how expression operands in assembly
instructions are printed. I have made improvements in this area as
well:
