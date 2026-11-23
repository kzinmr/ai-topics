---
title: "Moving LLVM's llvm::cl options to TableGen"
url: "https://maskray.me/blog/moving-llvm-cl-options-to-tablegen"
fetched_at: 2026-11-23T10:10:16.637677+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# Moving LLVM's llvm::cl options to TableGen

Source: https://maskray.me/blog/moving-llvm-cl-options-to-tablegen

Since September, the number of
llvm::cl::
option definitions in
llvm/lib
dropped from about 2,860 on release/23.x to about 1,070 on main.
Most of the difference moved from global
llvm::cl::opt
objects into per-library structs declared in TableGen and stored per
LLVMContext
; the rest were deleted.
This post covers why, the design, what it cost, what embedders need to change, and what is left before the LLVM 24 branch.
What is wrong with
llvm::cl::opt
A developer knob in an LLVM library is a namespace-scope global:
static
cl
::opt
<bool>
EnableCmovConverter
(
"x86-cmov-converter"
,
cl
::
desc
(
"Enable the X86 cmov-to-branch optimization."
),
cl
::
init
(
true
),
cl
::Hidden);
Each one is a dynamic initializer that registers the option into a
StringMap
.
It costs about 200 bytes of
.bss
, a couple of dynamic relocations, and about 1K instructions at startup and exit.
Multiplied by a few thousand options, every tool that links LLVM pays this before
main
, whether or not it parses a command line.
The values are process-wide.
Two
LLVMContext
s in one process cannot use different values, which matters to every embedder that compiles more than one thing at a time:
rustc's per-session
-Cllvm-args
, JITs that compile modules in parallel (Intel's graphics compiler, raised in the RFC thread), and NVIDIA, for whom removing global state was "the most important thing" (Reid Kleckner).
Options also leak across library boundaries: 48
extern cl::opt
declarations read another library's option, some through a public header.
2,589 of the 2,939 options (88%) were already
cl::Hidden
: they are developer knobs, not user-facing options, and nothing outside the library needs to see them as globals.
An
llvm/Option
based RFC
On 2026-09-20 I posted
[RFC] Declare library command line options in TableGen, one struct per library
.
The idea is to reuse
llvm/Option
, the OptTable library behind the clang, lld, and llvm-objcopy drivers.
LLVMOption is both a data representation and a parsing library; this design uses the data representation.
Steffen Larsen was "preliminarily fine" with it.
James Henderson and Jan Svoboda preferred it; Jan noted that clang's own option structs duplicate defaults between a header and the marshalling
.td
, and generating the struct from TableGen removes that.
Alexis Engelke asked for compile-time tracker numbers before going further.
If OptTable is to replace
cl::opt
, it has to be cheaper, not just tidier.
Four patches starting with
#218845
shrank
OptTable::Info
from 88 to 16 bytes with no dynamic relocations, by replacing string pointers with
StringTable
offsets and moving rarely used fields into a deduplicated side table.
clang's
DriverOptions.cpp.o
went from 96,968 to 72,400 bytes at the last step alone.
Declaring options
Each library owns a
.td
file in its own directory.
A target usually has two: one for the code generator, bound by its
TargetMachine
, and one in
MCTargetDesc/
for the MC layer, which llvm-mc and
clang -cc1as
use without a
TargetMachine
.
Here are excerpts of X86's,
llvm/lib/Target/X86/X86Options.td
:
include "llvm/Option/LibraryOptions.td"
def X86Options : OptionsStruct<prefix = "x86-">;
...
// X86CmovConversion.cpp
defm : BoolField<"x86-cmov-converter", "true",
"Enable the X86 cmov-to-branch optimization">;
defm : BoolField<"x86-cmov-converter-force-all", "false",
"Convert all cmovs to branches">;
defm : BoolField<"x86-cmov-converter-force-mem-operand", "true",
"Convert cmovs to branches whenever they have memory operands">;
defm : ValueField<"x86-cmov-converter-threshold", "unsigned", "4",
"Minimum gain per loop (in cycles) threshold">;
...
and
llvm/lib/Target/X86/MCTargetDesc/X86MCOptions.td
:
include "llvm/Option/LibraryOptions.td"
def X86MCOptions : OptionsStruct<prefix = "x86-">;
...
defm : ValueField<"x86-pad-max-prefix-size", "std::optional<unsigned>", "std::nullopt",
"Maximum number of prefixes to use for padding">;
// MCTargetDesc/X86MCAsmInfo.cpp
defm : EnumField<"x86-asm-syntax", "X86::AsmWriterFlavorTy", "X86::ATT",
"att,intel", ["X86::ATT", "X86::Intel"],
"Select the assembly style for input">;
llvm-min-tblgen -gen-opt-parser-defs
emits the option table, a struct with default member initializers, and an
apply
function that sets the member an argument names:
struct
X86MCOptions
{
bool
experimental_lvi_inline_asm_hardening{
false
};
std
::
optional
<
StringRef
> align_branch{
std
::nullopt};
std
::
optional
<
unsigned
> align_branch_boundary{
std
::nullopt};
bool
branches_within_32B_boundaries{
false
};
bool
pad_for_align{
false
};
bool
pad_for_branch_align{
true
};
std
::
optional
<
unsigned
> pad_max_prefix_size{
std
::nullopt};
X86
::
AsmWriterFlavorTy
asm_syntax{
X86
::ATT};
bool
mark_data_regions{
true
};
static const
llvm
::
opt
::
OptTable
&
optTable
();
bool
apply
(
const
llvm
::
opt
::
Arg
&
A
,
llvm
::
BumpPtrAllocator
&
Alloc
);
private:
friend class
llvm
::
cl
::
LibraryOptionsContext
;
friend class
llvm
::
opt
::
LibraryOptionsParser
;
static const
X86MCOptions
Default;
};
Member names are snake_case spellings with the struct's
prefix
stripped.
A
std::optional
member replaces a
getNumOccurrences()
check:
x86-pad-max-prefix-size
is unset unless given.
Default
is constant-initialized and private, so code cannot read options without going through a context.
There are also list fields, whose members are
ArrayRef
s so the structs stay trivially destructible.
let Condition = AssertsOnly in
declares options that exist only in assertion builds.
The full vocabulary is in
CommandLine.md
, section "Declaring a Library's Options in TableGen".
A library's struct is private: the
.td
and the header live in
lib/X
, never in
include/
.
Another library that needs a value calls a function or takes a parameter, and an embedder gets knobs through API structs (
PipelineTuningOptions
,
TargetOptions
,
lto::Config
).
Targets register their structs from
LLVMInitializeXXXTarget()
and
LLVMInitializeXXXTargetMC()
with a function-local static, so a target's options cost no dynamic initializer:
extern
"C"
LLVM_C_ABI
void
LLVMInitializeX86TargetMC
() {
static
opt
::RegisterLibraryOptions
<
X86MCOptions
>
O;
...
Reading options: the owner binds once
Values live in
cl::LibraryOptionsContext
.
Each layer reaches it through an object it already has, and an owner binds the struct once:
IR passes ask the function's context:
F.getContext().getLibraryOptions().get<InstCombineCLOptions>()
.
A
TargetMachine
binds its struct in the constructor, and subtargets and passes read it through
getCLOpts()
.
MC goes through
MCTargetOptions::LibraryOptions
, because
MCAsmInfo
and
MCAsmBackend
are created before any
MCContext
.
The X86 port turns the global above into a reference bound by the
TargetMachine
:
X86TargetMachine
::
X86TargetMachine
(...)
: ...,
CLOpts
(
cl
::
LibraryOptionsContext
::
get
<
X86Options
>(
Options.MCOptions.LibraryOptions)),
and
X86CmovConversion.cpp
reads it through the subtarget, replacing
EnableCmovConverter
,
ForceAll
and the other globals:
const
X86Options
&
CLOpts
=
STI->
getCLOpts
();
if
(
!
CLOpts.cmov_converter)
return
false
;
The MC struct is reached from
MCTargetOptions
, which
MCAsmInfo
, the asm backend and the asm parser all receive:
inline const
X86MCOptions
&
getCLOpts
(
const
MCTargetOptions
&
Options
) {
return
cl
::
LibraryOptionsContext
::
get
<
X86MCOptions
>(Options.LibraryOptions);
}
AssemblerDialect
=
X86_MC
::
getCLOpts
(Options).asm_syntax;
Larger libraries bind a reference in their central objects (
LSRInstance
,
GVNPassImpl
,
ScheduleDAGInstrs
) and pass it to static helpers.
A lookup is a hash probe at bind time, not on every read; converting four libraries to per-context reads measured within ±0.02% instructions:u on the compile-time tracker.
Parsing into a context
A tool parses into the context it will compile with:
LLVMContext Context;
...
cl
::
parseCommandLineOptions
(Context.
getLibraryOptions
(),
codegen
::
getToolOptions
(),
ArrayRef
(argv, argc),
"llvm system compiler
\n
"
);
Library options go to the context, and everything else still goes to
cl::
.
Option spellings do not change, so
clang -mllvm
,
ld.lld -mllvm
, opt and llc work as before.
Two contexts in one process can now differ.
This program compiles the same function on two threads, with
-x86-asm-syntax=intel
(the
X86MCOptions
field above) parsed into only one of the contexts:
static
std
::
string compile
(
LLVMContext
&
Ctx
) {
SMDiagnostic
Err;
std
::
unique_ptr
<
Module
> M
=
parseAssemblyString
(IR, Err, Ctx);
std
::
string
Error;
const
Target
*
T
=
TargetRegistry
::
lookupTarget
(M->
getTargetTriple
(), Error);
TargetOptions
Opts;
Opts.MCOptions.LibraryOptions
= &
Ctx.
getLibraryOptions
();
std
::
unique_ptr
<
TargetMachine
>
TM
(T->
createTargetMachine
(
M->
getTargetTriple
(),
""
,
""
, Opts,
std
::nullopt));
M->
setDataLayout
(TM->
createDataLayout
());
SmallString
<
0
> S;
raw_svector_ostream OS
(S);
legacy
::
PassManager
PM;
TM->
addPassesToEmitFile
(PM, OS,
nullptr
,
CodeGenFileType
::AssemblyFile);
PM.
run
(
*
M);
return
std
::
string
(S);
}
int
main
() {
InitializeNativeTarget
();
InitializeNativeTargetAsmPrinter
();
LLVMContext
A, B;
const char *
ArgsA[]
=
{
"demo"
,
"-x86-asm-syntax=intel"
};
const char *
ArgsB[]
=
{
"demo"
};
cl
::
parseCommandLineOptions
(A.
getLibraryOptions
(), ArgsA);
cl
::
parseCommandLineOptions
(B.
getLibraryOptions
(), ArgsB);
std
::
string
OutA, OutB;
std
::
thread TA
([
&
] { OutA
=
compile
(A); });
std
::
thread TB
([
&
] { OutB
=
compile
(B); });
TA.
join
();
TB.
join
();
outs
()
<<
"=== A
\n
"
<<
OutA
<<
"=== B
\n
"
<<
OutB;
}
% ./demo | grep -E '===|syntax|lea|ret'
=== A
.intel_syntax noprefix
lea	eax, [rdi + rsi]
ret
=== B
.att_syntax
leal	(%rdi,%rsi), %eax
retq
With release/23.x's global options, both threads would read the same value.
Initialize targets before parsing, since targets register their options in
LLVMInitializeXXXTarget()
, and parse before starting threads: the parser itself still has global state.
The legacy
cl::ParseCommandLineOptions
now rejects library options (
#242689
), so a tool that has not been ported fails loudly instead of silently ignoring an option:
% llvm-dwarfdump -x86-cmov-converter=false /dev/null
llvm-dwarfdump: Unknown command line argument '-x86-cmov-converter=false'.  Try: 'llvm-dwarfdump --help'
Library options are never serialized into bitcode.
A setting that must survive LTO belongs in an IR attribute or a module flag; developer knobs are passed again at link time with
-mllvm
.
What embedders need to change
LLVM 24 is the first release with this API.
A tool or embedder that forwards developer options to LLVM, such as rustc's
-Cllvm-args
, Julia, Zig, or an out-of-tree compiler driver, needs these changes:
Replace
cl::ParseCommandLineOptions(argc, argv)
with
cl::parseCommandLineOptions(Store, ArrayRef(argv, argc))
, where
Store
is the
LLVMContext
's
getLibraryOptions()
or a standalone
cl::LibraryOptionsContext
. Otherwise most CodeGen, MC, target, and optimization options become "Unknown command line argument".
With a standalone store, copy it into each
LLVMContext
with
Ctx.getLibraryOptions().assign(Store)
. Parse once, before creating threads.
Point
TargetOptions::MCOptions.LibraryOptions
at the store when creating a
TargetMachine
.
codegen::getTargetOptions
and
mc::getMCTargetOptions
do this for tools that use them.
codegen::RegisterCodeGenFlags
and
mc::RegisterMCTargetOptionsFlags
are gone. Pass
codegen::getToolOptions()
or
mc::getToolOptions()
to
cl::parseCommandLineOptions
instead.
C API users keep calling
LLVMParseCommandLineOptions
, before creating any context: contexts, target machines, MCJIT and ORC created through the C API read the options it parsed (
#234820
,
#242692
). Per-context C APIs wait until the migration ends; Nikita Popov considered them too early for the stable C API.
Spellings may have changed. Library options carry no stability promise; a renamed option that tests use keeps its old spelling as an alias for about six months.
How the design changed
The first version (
#226087
, 2026-09-30) gave each struct a process-wide
T::Global
, so a library could be ported before its readers had a context.
Per-context storage, originally a later step of the plan, was moved up and landed on 2026-10-14 (
#231407
), and
T::Global
was deleted on 2026-11-15 (
#242854
).
Nothing writes a process-wide library option any more.
The temporary global made the first ports cheap.
But once contexts existed, every reader still bound to the global was a silent-ignore bug.
For example, an early version of the per-context patch dropped target
-mllvm
options in clang's distributed ThinLTO backend, because that path built its
TargetMachine
without the context's options.
Spellings
Each port normalizes spellings: one prefix per library, and positive booleans with
enable-
and
disable-
dropped (
-cgp-branch-opts=0
, not
-disable-cgp-branch-opts
).
This matches what most options already looked like: 1,360 of the 1,808 booleans in llc and opt's
-help-hidden
had neither prefix.
Old spellings that tests or users rely on are kept as aliases for a while (
#232174
):
def : AliasOf<"hoist-const-loads", "machine-licm-hoist-const-loads">;
def : AliasOf<"disable-ifcvt-diamond", "ifcvt-diamond=false">;
A boolean accepts
-x
and
-x=true|false|1|0
.
I
proposed
accepting
-no-x
and eventually rejecting
-x=false
.
Hans Wennborg pointed out that countless build configurations pass
-x=false
, and James Y Knight and Nikita Popov saw no value in a second spelling, so I withdrew it.
Cleaning up
cl::
first
Before porting, I removed
cl::
features that have no
.td
equivalent:
cl::Sink
,
cl::multi_val
,
cl::Grouping
,
cl::DefaultOption
, and
cl::callback
in libraries.
A callback becomes a plain field plus code that inspects the state after parsing.
Pass plugins no longer put their options into the global namespace;
-plugin-arg=<plugin>,<arg>
(
#227414
) routes arguments to the plugin.
The tool-level registries in
CommandFlags.cpp
and
MCTargetOptionsCommandFlags.cpp
became opt-in TableGen structs too.
Cost and benefit
The first prototype ported LLVMPasses and LLVMCGData.
On the compile-time tracker, instructions:u stayed within ±0.02% on all configurations,
PassBuilderPipelines.cpp.o
shrank by 75.8 KB (7.9%), and clang's
.bss
by 1.5%.
Larger ports saved startup work: Scalar (214 options) −0.06% to −0.10% instructions:u on O0-g.
One measurement trap: removing
.bss
objects moves the addresses of the
AnalysisKey
statics.
DenseMapInfo<T *>
hashes the pointer, so probe lengths in
AnalysisManager
maps change, and an Analysis port showed +0.15% instructions on
opt -O3
with no real cost.
Pinning the keys' addresses with
--symbol-ordering-file
and
--section-start=.bss
made it disappear.
Where it stands
36
.td
files on main declare about 1,880 fields, covering 14 generic libraries (including Analysis, CodeGen, IR, MC, Passes and the Transforms libraries) and 15 targets.
Others have ported options too: Meredith Julian ported NVPTX, Simon Pilgrim SelectionDAG, and Maksim Shelegov and Rahman Lavaee smaller groups.
On 2026-11-06 I posted a
help wanted
call to library maintainers.
-Werror=global-constructors
is on for
llvm/lib
(
#239678
), with 62 libraries still opted out.
Once a library reaches zero dynamic initializers it leaves the opt-out list and cannot regain a global
cl::opt
.
What is left:
Transforms/Utils, the rest of CodeGen, ARM, PowerPC, Hexagon, LoongArch, BPF, ProfileData and LTO.
-print-options
and "Did you mean" suggestions do not see library options yet.
Global constructors that are not options: pass registries,
DEBUG_COUNTER
, and the GlobalISel combiner's rule lists.
LLVM 24 branches on 2027-01-12, and I want most of
llvm/
done by then.
MLIR, Polly, BOLT and clang-tools-extra will follow later.
Acknowledgments
Alexis Engelke reviewed most of this work: he approved 57 of the 91 framework and port patches I landed.
His reviews shaped the design, including trivially destructible structs and a constant-initialized
T::Default
in place of seeding each context.
Nikita Popov steered the C API toward one global store until the migration ends and reviewed the C API changes and the removal of
T::Global
.
Reid Kleckner pushed for per-context storage on behalf of embedders and reviewed the framework, the MC port, per-context storage and
AliasOf
, which grew out of his alias patches.
