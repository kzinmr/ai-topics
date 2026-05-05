---
title: "LLVM integrated assembler: Improving expressions and relocations"
url: "https://maskray.me/blog/2025-05-26-llvm-integrated-assembler-improving-expressions-and-relocations"
fetched_at: 2026-05-05T07:01:45.624405+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# LLVM integrated assembler: Improving expressions and relocations

Source: https://maskray.me/blog/2025-05-26-llvm-integrated-assembler-improving-expressions-and-relocations

In my previous post,
LLVM
integrated assembler: Improving MCExpr and MCValue
delved into
enhancements made to LLVM's internal MCExpr and MCValue representations.
This post covers recent refinements to MC, focusing on expression
resolving and relocation generation.
Preventing cyclic
dependencies
Equated
symbols
may form a cycle, which is not allowed.
1
2
3
4
5
6
7
8
9
# CHECK: [[#@LINE+2]]:7: error: cyclic dependency detected for symbol 'a'
# CHECK: [[#@LINE+1]]:7: error: expression could not be evaluated
a = a + 1
# CHECK: [[#@LINE+3]]:6: error: cyclic dependency detected for symbol 'b1'
# CHECK: [[#@LINE+1]]:6: error: expression could not be evaluated
b0 = b1
b1 = b2
b2 = b0
Previously, LLVM's interated assembler used an occurs check to detect
these cycles when parsing symbol equating directives.
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
bool
parseAssignmentExpression
(StringRef Name,
bool
allow_redef,
MCAsmParser &Parser, MCSymbol *&Sym,
const
MCExpr *&Value)
{
...
Sym = Parser.
getContext
().
lookupSymbol
(Name);
if
(Sym) {
if
(Value->
isSymbolUsedInExpression
(Sym))
return
Parser.
Error
(EqualLoc,
"Recursive use of '"
+ Name +
"'"
);
...
}
isSymbolUsedInExpression
implemented occurs check as a
tree (or more accurately, a DAG) traversal.
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
24
25
26
27
28
bool
MCExpr::isSymbolUsedInExpression
(
const
MCSymbol *Sym)
const
{
switch
(
getKind
()) {
case
MCExpr::Binary: {
const
MCBinaryExpr *BE =
static_cast
<
const
MCBinaryExpr *>(
this
);
return
BE->
getLHS
()->
isSymbolUsedInExpression
(Sym) ||
BE->
getRHS
()->
isSymbolUsedInExpression
(Sym);
}
case
MCExpr::Target: {
const
MCTargetExpr *TE =
static_cast
<
const
MCTargetExpr *>(
this
);
return
TE->
isSymbolUsedInExpression
(Sym);
}
case
MCExpr::Constant:
return
false
;
case
MCExpr::SymbolRef: {
const
MCSymbol &S =
static_cast
<
const
MCSymbolRefExpr *>(
this
)->
getSymbol
();
if
(S.
isVariable
() && !S.
isWeakExternal
())
return
S.
getVariableValue
()->
isSymbolUsedInExpression
(Sym);
return
&S == Sym;
}
case
MCExpr::Unary: {
const
MCExpr *SubExpr =
static_cast
<
const
MCUnaryExpr *>(
this
)->
getSubExpr
();
return
SubExpr->
isSymbolUsedInExpression
(Sym);
}
}
llvm_unreachable
(
"Unknown expr kind!"
);
}
While generally effective, this routine wasn't universally applied
across all symbol equating scenarios, such as with
.weakref
or some target-specific parsing code, leading to potential undetected
cycles, and therefore infinite loop in assembler execution.
To address this, I adopted a 2-color depth-first search (DFS)
algorithm. While a 3-color DFS is typical for DAGs, a 2-color approach
suffices for our trees, although this might lead to more work when a
symbol is visited multiple times. Shared subexpressions are very rare in
LLVM.
Here is the relevant change to
evaluateAsRelocatableImpl
. I also need a new bit from
MCSymbol
.
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
24
25
26
27
@@ -497,13 +498,25 @@
bool MCExpr::evaluateAsRelocatableImpl(MCValue &Res, const MCAssembler *Asm,
case SymbolRef: {
const MCSymbolRefExpr *SRE = cast<MCSymbolRefExpr>(this);
-    const MCSymbol &Sym = SRE->getSymbol();
+    MCSymbol &Sym = const_cast<MCSymbol &>(SRE->getSymbol());
const auto Kind = SRE->getKind();
bool Layout = Asm && Asm->hasLayout();
// Evaluate recursively if this is a variable.
+    if (Sym.isResolving()) {
+      if (Asm && Asm->hasFinalLayout()) {
+        Asm->getContext().reportError(
+            Sym.getVariableValue()->getLoc(),
+            "cyclic dependency detected for symbol '" + Sym.getName() + "'");
+        Sym.IsUsed = false;
+        Sym.setVariableValue(MCConstantExpr::create(0, Asm->getContext()));
+      }
+      return false;
+    }
if (Sym.isVariable() && (Kind == MCSymbolRefExpr::VK_None || Layout) &&
canExpand(Sym, InSet)) {
+      Sym.setIsResolving(true);
+      auto _ = make_scope_exit([&] { Sym.setIsResolving(false); });
bool IsMachO =
Asm && Asm->getContext().getAsmInfo()->hasSubsectionsViaSymbols();
if (Sym.getVariableValue()->evaluateAsRelocatableImpl(Res, Asm,
Unfortunately, I cannot remove
MCExpr::isSymbolUsedInExpression
, as it is still used by
AMDGPU (
[AMDGPU] Avoid
resource propagation for recursion through multiple functions
).
Revisiting the
.weakref
directive
The .weakref directive had intricate impact on the expression
resolving framework.
.weakref
enables the creation of weak aliases without
directly modifying the target symbol's binding. This allows a header
file in library A to optionally depend on symbols from library B. When
the target symbol is otherwise not referenced, the object file affected
by the weakref directive will include an undefined weak symbol. However,
when the target symbol is defined or referenced (by the user), it can
retain STB_GLOBAL binding to support archive member extraction. GCC's
[[gnu::weakref]]
attribute, as used in runtime library
headers like
libgcc/gthr-posix.h
, utilizes this
feature.
I've noticed a few issues:
Unreferenced
.weakref alias, target
created undefined
target
.
Crash when
alias
was already defined.
VK_WEAKREF
was mis-reused by the
alias
directive of llvm-ml (MASM replacement).
And addressed them with
Expression resolving and
reassignments
=
and its equivalents (
.set
,
.equ
) allow a symbol to be
equated
multiple times. This means when a symbol is referenced, its current
value is captured at that moment, and subsequent reassignments do not
alter prior references.
1
2
3
4
5
6
7
.data
.set x, 0
.long x         // reference the first instance
x = .-.data
.long x         // reference the second instance
.set x,.-.data
.long x         // reference the third instance
The assembly code evaluates to
.long 0; .long 4; .long 8
.
Historically, the LLVM integrated assembler restricted reassigning
symbols whose value wasn't a parse-time integer constant
(
MCConstExpr
). This was a safeguard against potentially
unsafe reassignments, as an old value might still be referenced.
1
2
3
4
% clang -c g.s
g.s:6:8: error: invalid reassignment of non-absolute variable 'x'
.set x,.-.data
^
The safeguard was implemented with multiple conditions, aided by a
mysterious
IsUsed
variable.
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
if
(Value->
isSymbolUsedInExpression
(Sym))
return
Parser.
Error
(EqualLoc,
"Recursive use of '"
+ Name +
"'"
);
else
if
(Sym->
isUndefined
(
false
) && !Sym->
isUsed
() &&
!Sym->
isVariable
())
;
else
if
(Sym->
isVariable
() && !Sym->
isUsed
() && allow_redef)
;
else
if
(!Sym->
isUndefined
() && (!Sym->
isVariable
() || !allow_redef))
return
Parser.
Error
(EqualLoc,
"redefinition of '"
+ Name +
"'"
);
else
if
(!Sym->
isVariable
())
return
Parser.
Error
(EqualLoc,
"invalid assignment to '"
+ Name +
"'"
);
else
if
(!
isa
<MCConstantExpr>(Sym->
getVariableValue
()))
return
Parser.
Error
(EqualLoc,
"invalid reassignment of non-absolute variable '"
+
Name +
"'"
);
Over the past few years, during our work on porting Clang to Linux
kernel ports, we worked around this by modifying the assembly code
itself:
This prior behavior wasn't ideal. I've since enabled proper
reassignment by implementing a system where the symbol is cloned upon
redefinition, and the symbol table is updated accordingly. Crucially,
any existing references to the original symbol remain unchanged, and the
original symbol is no longer included in the final emitted symbol
table.
Before rolling out this improvement, I discovered problematic uses in
the AMDGPU and ARM64EC backends that required specific fixes or
workarounds. This is a common challenge when making general improvements
to LLVM's MC layer: you often need to untangle and resolve individual
backend-specific "hacks" before a more generic interface enhancement can
be applied.
For the following assembly, newer Clang emits relocations referencing
foo, foo, bar, foo
like GNU Assembler.
1
2
3
4
5
6
7
b = a
a = foo
call a
call b
a = bar
call a
call b
Relocation generation
For a deeper dive into the concepts of relocation generation, you
might find my previous post,
Relocation
generation in assemblers
, helpful.
Driven by the need to support new RISC-V vendor relocations (e.g.,
Xqci extensions from Qualcomm) and my preference against introducing an
extra
MCAsmBackend
hook, I've significantly refactored
LLVM's relocation generation framework. This effort generalized existing
RISC-V/LoongArch ADD/SUB relocation logic and enabled its customization
for other targets like AVR and PowerPC.
The linker relaxation framework sometimes generated redundant
relocations that could have been resolved. This occurred in several
scenarios, including:
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
.option norelax
j label
// For assembly input, RISCVAsmParser::ParseInstruction sets ForceRelocs (https://reviews.llvm.org/D46423).
// For direct object emission, RISCVELFStreamer sets ForceRelocs (#77436)
.option relax
call foo  // linker-relaxable
.option norelax
j label   // redundant relocation due to ForceRelocs
.option relax
label:
And also with label differences within a section without
linker-relaxable instructions:
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
call foo
.section .text1,"ax"
# No linker-relaxable instruction. Label differences should be resolved.
w1:
nop
w2:
.data
# Redundant R_RISCV_SET32 and R_RISCV_SUB32
.long w2-w1
These issues have now been resolved through a series of patches,
significantly revamping the target-neutral relocation generation
framework. Key contributions include:
I've also streamlined relocation generation within the SPARC backend.
Given its minimal number of relocations, the SPARC implementation could
serve as a valuable reference for downstream targets seeking to
customize their own relocation handling.
Simplification
to assembly and machine code emission
For a dive into the core classes involved in LLVM's assembly and
machine code emission, you might read my
Notes
on LLVM assembly and machine code emission
.
The
MCAssembler
class orchestrates the emission process,
managing
MCAsmBackend
,
MCCodeEmitter
, and
MCObjectWriter
. In turn,
MCObjectWriter
oversees
MCObjectTargetWriter
.
Historically, many member functions within the subclasses of
MCAsmBackend
,
MCObjectWriter
, and
MCObjectTargetWriter
accepted a
MCAssembler *
argument. This was often redundant, as it was typically only used to
access the
MCContext
instance. To streamline this, I've
added a
MCAssembler *
member variable directly to
MCAsmBackend
,
MCObjectWriter
, and
MCObjectTargetWriter
, along with convenient helper
functions like
getContext
. This change cleans up the
interfaces and improves code clarity.
Previously, the ARM, Hexagon, and RISC-V backends had unique
requirements that led to extra arguments being passed to MCAsmBackend
hooks. These arguments were often unneeded by other targets. I've since
refactored these interfaces, replacing those specialized arguments with
more generalized and cleaner approaches.
Future plan
The assembler's ARM port has a limitation where only relocations with
implicit addends (REL) are handled. For
CREL
, we
aim to use explicit addends across all targets to simplify
linker/tooling implementation, but this is incompatible with
ARMAsmBackend
's current design. See this ARM CREL assembler
issue
https://github.com/llvm/llvm-project/issues/141678
.
To address this issue, we should
In
MCAssembler::evaluateFixup
, generalize
MCFixupKindInfo::FKF_IsAlignedDownTo32Bits
(ARM hack, also
used by other backends) to support more fixups, including
ARM::fixup_arm_uncondbl
(
R_ARM_CALL
). Create a
new hook in
MCAsmBackend
.
In
ARMAsmBackend
, move the
Value -= 8
code
from
adjustFixupValue
to the new hook.
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
unsigned
ARMAsmBackend::adjustFixupValue
(
const
MCAssembler &Asm,
...
case
ARM::fixup_arm_condbranch:
case
ARM::fixup_arm_uncondbranch:
case
ARM::fixup_arm_uncondbl:
case
ARM::fixup_arm_condbl:
case
ARM::fixup_arm_blx:
Value -=
8
;
if
(!isInt<
26
>(Value)) {
Ctx.reportError(Fixup.getLoc(),
"Relocation out of range"
);
return
0
;
Enabling RELA/CREL support requires significant effort and exceeds my
expertise or willingness to address for AArch32. However, I do want to
add a new MCAsmBackend hook to minimize AArch32's invasive modifications
to the generic relocation generation framework.
For reference, the arm-vxworks port in binutils
introduced
RELA support in 2006
.
