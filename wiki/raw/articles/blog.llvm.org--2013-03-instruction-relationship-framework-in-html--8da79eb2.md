---
title: "Instruction Relationship Framework in LLVM"
url: "https://blog.llvm.org/2013/03/instruction-relationship-framework-in.html"
fetched_at: 2026-05-05T07:01:43.452631+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Instruction Relationship Framework in LLVM

Source: https://blog.llvm.org/2013/03/instruction-relationship-framework-in.html

Instruction Relationship Framework in LLVM
By Jyotsna Verma
Mar 20, 2013
#codegen
,
#MC
9 minute read
The article provides an overview of the new Relationship framework of TableGen. This TableGen feature is used to describe user defined relationships between instructions. It was added to LLVM in October 2012.
Motivation:
The motivation for this feature stemmed from the Hexagon backend. Much like other processors, Hexagon provides multiple variations for many instructions. It is a common requirement in machine instruction passes to switch between various formats of the same instruction. For example, consider an
Add
instruction with predicated true (
Add_pt
) and predicated false (
Add_pf
) forms. Let's assume that a non-predicated
Add
instruction is selected during target lowering. However, during if-conversion, the optimization pass might decide to change the non-predicated
Add
into the predicated true
Add_pt
form. These transformations require a framework to relate non-predicated forms to the respective predicated forms. In the absence of such a framework, this transformation is typically achieved using large switch cases. There are many deficiencies in using a switch case based approach. The manual implementation of switch case clauses requires a very high maintenance cost. It also results in lost optimization opportunities due to incomplete implementation of switch cases. The lack of a relationship model resulted in around 15% of Hexagon backend code dedicated to switch cases with several of those functions growing to over thousands of lines of code.
This problem inspired us to explore some alternatives. We started to look for a framework that was easy to maintain, flexible, scalable, and less error prone. After some initial discussions and brainstorming in the Hexagon group, we decided to modify TableGen to express instruction relations. The initial design was submitted to the LLVM-dev mailing list for review. Jakob Stoklund gave valuable suggestions and helped with the design of the relationship framework. The idea was to add a query language that can be used to define different kind of relationships between instructions. TableGen was extended to parse relationship models. It uses the information to construct tables which are queried to determine new opcodes corresponding to a relationship. The Hexagon backend relies heavily on the relationship framework and it has significantly improved the code quality of our target.
Before getting into the implementation details, let's consider an API that takes an instruction opcode as input and returns its predicated true/false form. We'll first look at the switch-case based solution and then compare it with the relationship based implementation.
short getPredicatedTrue(short opcode) {
switch (opcode) {
default:
return -1;
case Hexagon::Add:
return Hexagon::Add_pt;
case Hexagon::Sub:
return Hexagon::Sub_pt;
case Hexagon::And:
return Hexagon::And_pt;
case Hexagon::Or:
return Hexagon::Or_pt;
case ... :
return ...
}
short getPredicatedFalse(short opcode) {
switch (opcode) {
default:
return -1;
case Hexagon::Add:
return Hexagon::Add_pf;
case Hexagon::Sub:
return Hexagon::Sub_pf;
case Hexagon::And:
return Hexagon::And_pf;
case Hexagon::Or:
return Hexagon::Or_pf;
case ... :
return ...
}
short getPredicatedOpcode(short opcode, bool predSense) {
return predSense ? getPredicatedTrue(opcode)
: getPredicatedFlase(opcode);
}
The switch-case based approach becomes quite unwieldy because of the large number of cases. Also, it requires continuous maintenance as new instructions are added. The problem becomes more demanding when an instruction has multiple relations since each of these APIs must be updated.
The relationship framework offers a very systematic solution to this problem. It requires instructions to model their attributes and categorize their groups. For instance, a field called 'PredSense' can be used to record whether an instruction is predicated or not and its sense of predication. Each instruction in the group has to be unique such that no two instructions can share all the same attributes. There must be at least one field with different value. The instruction groups are modeled by assigning a common base name to all the instructions in the group. One of the biggest advantages of this approach is that, by modeling these attributes and groups once, we can define multiple relationships with very little effort.
With the relationship framework, the
getPredicatedOpcode
API can be implemented as below:
short getPredicatedOpcode(short opcode, bool predSense) {
return predSense ? getPredicated(opcode, PredSenseTrue)
: getPredicated(opcode, PredSenseFalse);
}
Here,
getPredicated()
function is automatically generated by the relationship framework. It performs a query into the corresponding relationship table, also generated by the framework, and returns the matching predicated opcode if found.
Architecture:
The entire framework is driven by a class called
InstrMapping
. The TableGen back-end has been extended to include a new parser for the relationship models implemented using
InstrMapping
class. Any relationship model must derive from this class and assign all the class members to the appropriate values. This is how the class looks like:
class InstrMapping {
// Used to reduce search space only to the instructions using this relation model
string FilterClass;
// List of fields/attributes that should be same for all the instructions in
// a row of the relation table. Think of this as a set of properties shared
// by all the instructions related by this relationship.
list
RowFields = [];
// List of fields/attributes that are same for all the instructions
// in a column of the relation table.
list
ColFields = [];
// Values for the fields/attributes listed in 'ColFields' corresponding to
// the key instruction. This is the instruction that will be transformed
// using this relation model.
list
KeyCol = [];
// List of values for the fields/attributes listed in 'ColFields', one for
// each column in the relation table. These are the instructions a key
// instruction will be transformed into.
list
> ValueCols = [];
}
Now, let's revisit the
getPredicated
API. As mentioned earlier, this function can be auto-generated by the relationship framework. It requires us to define a relationship model that can relate non-predicated instructions with their predicated forms:
def getPredicated : InstrMapping {
// Choose a FilterClass that is used as a base class for all the instructions modeling
// this relationship. This is done to reduce the search space only to these set of instructions.
let FilterClass = "PredRel";
// Instructions with same values for all the fields in RowFields form a row in the resulting
// relation table.
// For example, if we want to relate 'Add' (non-predicated) with 'Add_pt'
// (predicated true) and 'Add_pf' (predicated false), then all 3
// instructions need to have a common base name, i.e., same value for BaseOpcode here. It can be
// any unique value (Ex: XYZ) and should not be shared with any other instruction not related to 'Add'.
let RowFields = ["BaseOpcode"];
// List of attributes that can be used to define key and column instructions for a relation.
// Here, key instruction is passed as an argument to the function used for querying relation tables.
// Column instructions are the instructions they (key) can transform into.
//
// Here, we choose 'PredSense' as ColFields since this is the unique attribute of the key
// (non-predicated) and column (true/false) instructions involved in this relationship model.
let ColFields = ["PredSense"];
// The key column contains non-predicated instructions.
let KeyCol = ["none"];
// Two value columns - first column contains instructions with PredSense=true while the second
// column has instructions with PredSense=false.
let ValueCols = [["true"], ["false"]];
}
This relationship model is processed and the information is used to construct a table along with the API to query. All this is emitted in the
XXXInstrInfo.inc
file. However, with the changes made so far, we may end up with an empty relation table since we haven't defined
PredSense
and
BaseOpcode
for any of the instructions yet.
multiclass ALU32_Pred
{
let
PredSense = !if(PredNot, "false", "true")
, isPredicated = 1 in
def NAME : ALU32_rr<(outs IntRegs:$dst),
(ins PredRegs:$src1, IntRegs:$src2, IntRegs: $src3),
!if(PredNot, "if (!$src1)", "if ($src1)")#
" $dst = "#mnemonic#"($src2, $src3)",
[]>;
}
multiclass ALU32_base
{
let
BaseOpcode = BaseOp
in {
let isPredicable = 1 in
def NAME : ALU32_rr<(outs IntRegs:$dst),
(ins IntRegs:$src1, IntRegs:$src2),
"$dst = "#mnemonic#"($src1, $src2)",
[(set (i32 IntRegs:$dst), (OpNode (i32 IntRegs:$src1),
(i32 IntRegs:$src2)))]>;
defm pt : ALU32_Pred
; // Predicate true
defm pf : ALU32_Pred
; // Predicate false
}
}
let isCommutable = 1 in {
defm Add : ALU32_base<"add", "ADD", add>,
PredRel
;
defm And : ALU32_base<"and", "AND", and>,
PredRel
;
defm Xor: ALU32_base<"xor", "XOR", xor>,
PredRel
;
defm Or  : ALU32_base<"or", "OR", or>,
PredRel
;
}
defm Sub : ALU32_base<"sub", "SUB", sub>,
PredRel
;
Fields highlighted in blue are solely for the purpose of Relationship framework. Here,
PredRel
is a filter class used to extract instructions that may be related using
getPredicated
relationship model. All the instructions using this model are expected to derive from
PreRel
class.
BaseOpcode
is used to group related instructions together. In the above example, all the variants of
Add
instruction,
Add, Add_pt, Add_pf
will have their BaseOpcode set to
ADD
. Similarly,
BaseOpcode
for all the variants for
Sub
is set to
SUB
. It can be any string unique across all groups.
PredSense
is used to identify instructions within each group.
With the help of this extra information, TableGen is able to construct the following API. It offers the same functionality as switch-case based approach and significantly reduces the maintenance overhead:
int getPredicated(uint16_t Opcode, enum PredSense inPredSense) {
static const uint16_t getPredicatedTable[][3] = {
{ Hexagon::Add, Hexagon::Add_pt, Hexagon::Add_pf },
{ Hexagon::And, Hexagon::And_pt, Hexagon::And_pf },
{ Hexagon::Or, Hexagon::Or_pt, Hexagon::Or_pf },
{ Hexagon::Sub, Hexagon::Sub_pt, Hexagon::Sub_pf },
{ Hexagon::Xor, Hexagon::Xor_pt, Hexagon::Xor_pf },
}; // End of getPredicatedTable
unsigned mid;
unsigned start = 0;
unsigned end = 5;
while (start < end) {
mid = start + (end - start)/2;
if (Opcode == getPredicatedTable[mid][0]) {
break;
}
if (Opcode < getPredicatedTable[mid][0])
end = mid;
else
start = mid + 1;
}
if (start == end)
return -1; // Instruction doesn't exist in this table.
if (inPredSense == PredSense_true)
return getPredOpcodeTable[mid][1];
if (inPredSense == PredSense_false)
return getPredicatedTable[mid][2];
return -1;
}
Once instructions have been defined to appropriately model their properties, defining new instruction mappings become extremely easy. Now, say we want to have an API that allows us to transform a
predicate-true
instruction into its
predicate-false
form. This can be done by defining a new relationship model. For this model, we don't have to modify any of the instruction definitions as they already have all the necessary information present.
//===------------------------------------------------------------------===//
// Generate mapping table to relate predicate-true instructions with their
// predicate-false forms
//
def getFalsePredOpcode : InstrMapping {
let FilterClass = "PredRel";
let RowFields = ["BaseOpcode"];
let ColFields = ["PredSense"];
let KeyCol = ["true"];
let ValueCols = [["false"]];
}
Conclusion:
I hope this article succeeds in providing some useful information about the framework. The Hexagon backend makes extensive use of this feature and can be used as a reference for getting started on relationship framework.
