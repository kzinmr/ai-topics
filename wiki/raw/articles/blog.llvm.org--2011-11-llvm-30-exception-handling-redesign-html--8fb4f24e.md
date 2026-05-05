---
title: "LLVM 3.0 Exception Handling Redesign"
url: "https://blog.llvm.org/2011/11/llvm-30-exception-handling-redesign.html"
fetched_at: 2026-05-05T07:01:43.653266+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM 3.0 Exception Handling Redesign

Source: https://blog.llvm.org/2011/11/llvm-30-exception-handling-redesign.html

LLVM 3.0 Exception Handling Redesign
One of the biggest IR changes in the LLVM 3.0 release is a redesign and reimplementation of the LLVM IR exception handling model. The old model, while it worked for most cases, fell over in some key situations, leading to obscure miscompilations, missed optimizations, and poor compile time. This post talks about the changes in LLVM 3.0 and how to move an existing LLVM front-end to the new design. It assumes some familiarity with the Itanium C++ ABI for exception handling.
Goals of the exception handling system
Exception handling needs to be a first-class citizen of the LLVM IR. This allows us to manipulate the exception handling information in an intelligent fashion (e.g., during inlining). Also, code generation needs to be able to reliably find a variety of information associated specific
invoke
call (e.g. the personality function for use with a call). Finally, we need to follow the established exception handling ABI to ensure binary compatibility with other compilers.
While there are a lot of details to get right for exception handling to work (with regards to the ABI), our goal is to keep LLVM IR as simple to generate and manipulate as possible. By making EH a first-class citizen, the new instructions will have a simple, easily understood syntax and constraints which can be tested to ensure that the IR is correct after each code transformation.
The old exception handling system
The old system used LLVM intrinsics to convey the exception handling information to the code generator. The primary problem with the old system is that there was nothing that bound these intrinsics to the invoke calls that could be unwound through, making code generation fragile, and optimizations like inlining impossible to represent (in the general case).
Further, the intrinsics were very difficult for code transformations to maintain and update correctly: we would frequently get exception tables which had incorrect information in them (e.g., specifying that a specific type couldn't propagate past that point when it wasn't specified in the original program). It also couldn't handle "cleanup" situations without a lot of work.
Because of normal code motion, the intrinsics, which held the information that the code generator needed to generate the correct tables, could be moved far away from the
invoke
instruction they were associated with. I.e., they could be moved out of the
invoke
's landingpad. This made code generation of the previous exception handling constructs fragile, and sometimes caused miscompilations of exception handling code, which wasn't acceptable.
A final (somewhat theoretical) issue is that the old system only worked with standard personality functions. It would be nearly impossible to use custom personality functions (e.g. that returned 3 registers in a landing pad instead of 2) with it. While we had no specific use case for this, we were unable to use custom personality functions to optimize code size or performance of C++ exceptions.
The LLVM 3.0 Exception Handling System
The backbone of the new exception handling system are the two new instructions
landingpad
and
resume
:
landingpad
Defines a landing pad basic block. It contains all of the information that's needed by the code generator to generate the correct EH tables. It's also required to be the first non-
PHI
instruction in the unwind destination of an invoke instruction. In addition, a landing pad may
only
be jumped to by the unwind edge of an
invoke
instruction. These constraints ensure that it is always possible to accurately match up the unwind information with an invoke call. It replaces the
@llvm.eh.exception
and
@llvm.eh.selector
intrinsics.
resume
Causes the current exception to resume propagation up the stack. It replaces the
@llvm.eh.resume
intrinsic.
Here is a simple example of what the new syntax looks like. For this program:
void bar();
void foo() throw (const char *) {
try {
bar();
} catch (int) {
}
}
The IR looks like this:
@_ZTIPKc = external constant i8*
@_ZTIi = external constant i8*
define void @_Z3foov() uwtable ssp {
entry:
invoke void @_Z3barv()
to label %try.cont unwind label %lpad
lpad:
%0 = landingpad { i8*, i32 } personality i8* bitcast (i32 (...)* @__gxx_personality_v0 to i8*)
catch i8* bitcast (i8** @_ZTIi to i8*)
filter [1 x i8*] [i8* bitcast (i8** @_ZTIPKc to i8*)]
%1 = extractvalue { i8*, i32 } %0, 0
%2 = extractvalue { i8*, i32 } %0, 1
%3 = tail call i32 @llvm.eh.typeid.for(i8* bitcast (i8** @_ZTIi to i8*)) nounwind
%matches = icmp eq i32 %2, %3
br i1 %matches, label %catch, label %filter.dispatch
filter.dispatch:
%ehspec.fails = icmp slt i32 %2, 0
br i1 %ehspec.fails, label %ehspec.unexpected, label %eh.resume
ehspec.unexpected:
tail call void @__cxa_call_unexpected(i8* %1) no return
unreachable
catch:
%4 = tail call i8* @__cxa_begin_catch(i8* %1) nounwind
tail call void @__cxa_end_catch() nounwind
br label %try.cont
try.cont:
ret void
eh.resume:
resume { i8*, i32 } %0
}
The
landingpad
instruction specifies the
personality function
the EH runtime uses, a list of types which it can catch (
int
), and a list of types which
foo
is allowed to throw (
const char *
).
The
resume
instruction resumes propagation of the exception if it's not caught and of an allowed type.
Converting to the LLVM 3.0 exception handling system
Converting from the old EH API to the new EH API is rather simple because a lot of complexity has been removed. To generate the EH code in LLVM 2.9, you would have to do something akin to this:
Function *ExcIntr =
Intrinsic::getDeclaration(TheModule, Intrinsic::eh_exception);
Function *SlctrIntr =
Intrinsic::getDeclaration(TheModule, Intrinsic::eh_selector);
Function *PersonalityFn =
Function::Create(FunctionType::get(Type::getInt32Ty(Context), true),
Function::ExternalLinkage,
"__gxx_personality_v0", TheModule);
// The exception pointer.
Value *ExnPtr = Builder.CreateCall(ExcIntr, "exn");
// The arguments to the @llvm.eh.selector instruction.
std::vector<Value*> Args;  Args.push_back(ExnPtr);
Args.push_back(Builder.CreateBitCast(PersonalityFn,
Type::getInt8PtrTy(Context)));
// ... Complex code to add catch types, filters, cleanups, and catch-alls to Args ...
// The selector call.
Value *Sel = Builder.CreateCall(SlctrIntr, Args, "exn.sel");
You should instead generate a
landingpad
instruction, that returns an exception object and selector value:
LandingPadInst *LPadInst =
Builder.CreateLandingPad(StructType::get(Int8PtrTy, Int32Ty, NULL),
PersonalityFn, 0);
Value *ExnPtr = Builder.CreateExtractValue(LPadInst, 0);
Value *Sel = Builder.CreateExtractValue(LPadInst, 1);
It's now trivial to add the individual clauses to the
landingpad
instruction.
// Adding a catch clause
Constant *TypeInfo = getTypeInfo();
LPadInst->addClause(TypeInfo);
// Adding a C++ catch-all
LPadInst->addClause(Constant::getNullValue(Builder.getInt8PtrTy()));
// Adding a cleanup
LPadInst->setCleanup(true);
// Adding a filter clause
std::vector<Value*> TypeInfos;
Constant *TypeInfo = getFilterTypeInfo();
TypeInfos.push_back(Builder.CreateBitCast(TypeInfo, Builder.getInt8PtrTy()));
ArrayType *FilterTy = ArrayType::get(Int8PtrTy, TypeInfos.size());
LPadInst-<addClause(ConstantArray::get(FilterTy, TypeInfos));
Converting from using the
@llvm.eh.resume
intrinsic to the
resume
instruction is trivial. It takes the exception pointer and exception selector values returned by the
landingpad
instruction:
Type *UnwindDataTy = StructType::get(Builder.getInt8PtrTy(),
Builder.getInt32Ty(), NULL);
Value *UnwindData = UndefValue::get(UnwindDataTy);
Value *ExcPtr = Builder.CreateLoad(getExceptionObjSlot());
Value *ExcSel = Builder.CreateLoad(getExceptionSelSlot());
UnwindData = Builder.CreateInsertValue(UnwindData, ExcPtr, 0, "exc_ptr");
UnwindData = Builder.CreateInsertValue(UnwindData, ExcSel, 1, "exc_sel");
Builder.CreateResume(UnwindData);
Conclusion
The new EH system now works much better than the old system. It is much less fragile and complex. This makes it easier to understand when you have to read the IR to figure out what's going on. More importantly, it allows us to follow the ABI more closely than before.
Better yet, it's rather straight-forward to convert from the old system to the new one. In fact, you may see your code become much simpler! If you're interested in more details and reference information, please see the
Exception Handling in LLVM IR
document.
