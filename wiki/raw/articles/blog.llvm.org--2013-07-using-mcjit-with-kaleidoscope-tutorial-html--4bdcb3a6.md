---
title: "Using MCJIT with the Kaleidoscope Tutorial"
url: "https://blog.llvm.org/2013/07/using-mcjit-with-kaleidoscope-tutorial.html"
fetched_at: 2026-05-05T07:01:43.168038+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Using MCJIT with the Kaleidoscope Tutorial

Source: https://blog.llvm.org/2013/07/using-mcjit-with-kaleidoscope-tutorial.html

Using MCJIT with the Kaleidoscope Tutorial
By Andy Kaylor
Jul 22, 2013
#MC
,
#jit
15 minute read
You may have noticed that there are two different JIT execution engines in the LLVM project.  The older implementation (llvm::JIT) is a sort of ad hoc implementation that brings together various pieces of the LLVM code generation and adds its own glue to get dynamically generated code into memory one function at a time.  The newer implementation (llvm::MCJIT) is heavily based on the core MC library and emits complete object files into memory then prepares them for execution.
MCJIT has several advantages, including broader platform support and better tool integration.  However, because it is designed to compile entire modules into object images the MCJIT engine doesn’t directly support some key features of the older JIT implementation, such as lazy compilation.  By lazy compilation, I mean deferring compilation of individual functions until just before the function is going to be executed.
At this point you may find yourself saying, “Wait a minute?  Are you saying MC
JIT
doesn’t do ‘just-in-time’ compilation?!?”  Well…sort of.  It’s more of a dynamic code emitter than a true just-in-time compiler.  That said we’d like it to become a long term replacement for the old JIT so that we can reap the benefits of ongoing development in core MC code generation.
So the question becomes, can we make MCJIT do what the older JIT engine does?  The current answer is, “I hope so.”  As a means of exploring this question, I decided to try to convert the Kaleidoscope tutorial to use MCJIT.
The Kaleidoscope tutorial demonstrates a simple interactive interpreter (“toy”) designed to teach developers how to implement a simple programming language using LLVM.  Kaleidoscope is presented as a procedural language that supports floating point variables, function calls and a few basic operators.  The tutorial uses the JIT execution engine to produce executable code from user input.
Since MCJIT was conceived as a drop in replacement for the older JIT engine, putting it into the Kaleidoscope tutorial should be easy, right?  Eh….keep reading and you can judge for yourself.  Along the way, you’ll see firsthand some of the key differences between these two engines.
First Steps
I’ll be starting where the Kaleidoscope tutorial ends.  If you want to follow along, you can grab the final Kaleidoscope source code from the LLVM source tree at
<llvm_root>/examples/Kaleidoscope/Chapter7/toy.cpp
There’s a Makefile there too, but it is intended to build the program in place as part of a complete LLVM build, so we’ll be using a command line approach.  For now, you can just type the build command in the Kaleidoscope tutorial:
clang++ -g toy.cpp `llvm-config --cppflags --ldflags --libs core jit native` -O3 –o toy
If you have the right tools in your path, that should build the tutorial for you.
The first change we’ll need to make is to create an MCJIT execution engine instead of a JIT execution engine.  This is pretty simple.  The ExecutionEngine gets created in the main() function in toy.cpp using an EngineBuilder object with a call that looks like this:
TheExecutionEngine = EngineBuilder(TheModule).setErrorStr(&ErrStr).create();
EngineBuilder creates a JIT engine by default, but you can request an MCJIT engine instead by calling the setUseMCJIT() function, as such:
TheExecutionEngine = EngineBuilder(TheModule).setErrorStr(&ErrStr)
.setUseMCJIT(true)
.create();
You’ll also need to include ‘MCJIT.h’ to get the MCJIT static constructor linked in properly (you can replace ‘JIT.h’) and add two new lines of component initialization at the top of main().
IntializeNativeTargetAsmPrinter();
InitializeNatureTargetAsmParser();
Another feature of MCJIT that I should mention at this point is that it is designed to allow generated code to be remapped for execution in external processes or even on remote systems.  As such, it requires that we call ExecutionEngine::finalizeObject() to let it know we’re ready for the generated object to be put in its executable state.  We can do that just before calling getPointerToFunction() in HandleTopLevelExpression:
TheExecutionEngine->finalizeObject();
Now build with the command above, substituting ‘mcjit’ for ‘jit’ in the library list.
clang++ -g toy.cpp `llvm-config --cppflags --ldflags --libs core mcjit native` -O3 –o toy
Handling Function Names
At this point, you’re up and running with MCJIT.  Unfortunately, nothing will work because the interpreter uses unnamed functions to evaluate immediate expressions and MCJIT doesn’t like that.
For the purposes of this experiment, I’m going to work around that with a quick and dirty hack that generates a simple unique name for such anonymous functions, and while I’m at it I’ll make sure any function names would be legal in C, because that we need that to handle the way our interpreter names operators.  My hack looks like this:
//===----------------------------------------------------------------------===//
// Quick and dirty hack
//===----------------------------------------------------------------------===//
// FIXME: Obviously we can do better than this
std::string GenerateUniqueName(const char *root)
{
static int i = 0;
char s[16];
sprintf(s, "%s%d", root, i++);
std::string S = s;
return S;
}
std::string MakeLegalFunctionName(std::string Name)
{
std::string NewName;
if (!Name.length())
return GenerateUniqueName("anon_func_");
// Start with what we have
NewName = Name;
// Look for a numberic first character
if (NewName.find_first_of("0123456789") == 0) {
NewName.insert(0, 1, 'n');
}
// Replace illegal characters with their ASCII equivalent
std::string legal_elements = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
size_t pos;
while ((pos = NewName.find_first_not_of(legal_elements)) != std::string::npos) {
char old_c = NewName.at(pos);
char new_str[16];
sprintf(new_str, "%d", (int)old_c);
NewName = NewName.replace(pos, 1, new_str);
}
return NewName;
}
We need to use this in three places.  First, in PrototypeAST::Codegen() just before the call to Function::Create()
std::string FnName = MakeLegalFunctionName(Name);
Also replace subsequent references to ‘Name’ with ‘FnName’ in this function.  Changing the ‘Name’ member of the PrototypeAST object would have other unintended consequences, so here we’re just changing the name by which LLVM will know the function.  To that end, we also need to update calls to getFunction in UnaryExprAST::Codegen() and BinaryExprAST::Codegen().
Function *F = TheModule->getFunction(MakeLegalFunctionName(std::string("unary")+Opcode));
and
Function *F = TheModule->getFunction(MakeLegalFunctionName(std::string("binary")+Opcode));
A new member variable wouldn’t be a bad idea, but we won’t have to think about this again, so for now let’s just leave it simple.
Adding Multiple Module Support
Now let’s compile again using the command line above and give this a try.
ready> def add(x y) x+y;
[output omitted]
ready> add(1, 2);
ready> Evaluated to 3.000000
Hurray! It’s working!  Let’s keep playing with it.
ready> add(3, 4);
ready> Segmentation fault (core dumped)
Oops!  What happened?  Well, here’s the thing.  Our ‘toy’ program creates a single module, uses that to create an execution engine, then keeps adding all the functions it creates to that same module.  This works with JIT, which is just generating code for one function at a time.  MCJIT, on the other hand, compiles the entire module and expects it to stay compiled.  When you add something to it and call finalizeObject() again it will skip the compilation phase (because it thinks the module has already been compiled) and attempt to re-apply relocations.  Since the MCJIT memory manager marked the code sections for this object as R-X in the previous call to finalizeObject, the attempt to re-write the relocation crashes.  MCJIT should obviously handle this case more gracefully, but the relevant point here is that MCJIT won’t let you continue to modify a module after it’s been compiled.
We’ll need to modify our program to spin off a new module and execution engine every time it compiles a previous module, but as it turns out that’s not as painful to implement as it might sound.  Our ‘toy’ program uses three global variables (TheModule, TheFPM and TheExecutionEngine) to handle all the functionality we’re interested in.  We’ll create a helper class to replace those three objects and coordinate their behavior.
The class will look like this:
//===----------------------------------------------------------------------===//
// MCJIT helper class
//===----------------------------------------------------------------------===//
class MCJITHelper
{
public:
MCJITHelper(LLVMContext& C) : Context(C), OpenModule(NULL) {}
~MCJITHelper();
Function *getFunction(const std::string FnName);
Module *getModuleForNewFunction();
void *getPointerToFunction(Function* F);
void dump();
private:
typedef std::vector<Module*> ModuleVector;
typedef std::vector<ExecutionEngine*> EngineVector;
LLVMContext  &Context;
Module       *OpenModule;
ModuleVector  Modules;
EngineVector  Engines;
};
MCJITHelper::~MCJITHelper()
{
if (OpenModule)
delete OpenModule;
EngineVector::iterator begin = Engines.begin();
EngineVector::iterator end = Engines.end();
EngineVector::iterator it;
for (it = begin; it != end; ++it)
delete *it;
}
Function *MCJITHelper::getFunction(const std::string FnName) {
ModuleVector::iterator begin = Modules.begin();
ModuleVector::iterator end = Modules.end();
ModuleVector::iterator it;
for (it = begin; it != end; ++it) {
Function *F = (*it)->getFunction(FnName);
if (F) {
if (*it == OpenModule)
return F;
assert(OpenModule != NULL);
// This function is in a module that has already been JITed.
// We need to generate a new prototype for external linkage.
// Look for a prototype in the current module.
Function *PF = OpenModule->getFunction(FnName);
if (PF && !PF->empty()) {
ErrorF("redefinition of function across modules");
return 0;
}
// If we don't have a prototype yet, create one.
if (!PF)
PF = Function::Create(F->getFunctionType(),
Function::ExternalLinkage,
FnName,
OpenModule);
return PF;
}
}
return NULL;
}
Module *MCJITHelper::getModuleForNewFunction() {
// If we have a Module that hasn't been JITed, use that.
if (OpenModule)
return OpenModule;
// Otherwise create a new Module.
std::string ModName = GenerateUniqueName("mcjit_module_");
Module *M = new Module(ModName, Context);
Modules.push_back(M);
OpenModule = M;
return M;
}
void *MCJITHelper::getPointerToFunction(Function* F) {
// See if an existing instance of MCJIT has this function.
EngineVector::iterator begin = Engines.begin();
EngineVector::iterator end = Engines.end();
EngineVector::iterator it;
for (it = begin; it != end; ++it) {
void *P = (*it)->getPointerToFunction(F);
if (P)
return P;
}
// If we didn't find the function, see if we can generate it.
if (OpenModule) {
std::string ErrStr;
ExecutionEngine *NewEngine = EngineBuilder(OpenModule)
.setErrorStr(&ErrStr)
.setUseMCJIT(true)
.create();
if (!NewEngine) {
fprintf(stderr, "Could not create ExecutionEngine: %s\n", ErrStr.c_str());
exit(1);
}
OpenModule = NULL;
Engines.push_back(NewEngine);
NewEngine->finalizeObject();
return NewEngine->getPointerToFunction(F);
}
return NULL;
}
void MCJITHelper::dump()
{
ModuleVector::iterator begin = Modules.begin();
ModuleVector::iterator end = Modules.end();
ModuleVector::iterator it;
for (it = begin; it != end; ++it)
(*it)->dump();
}
The one thing here that might require explanation is the implementation of getFunction.  This is used when the interpreter wants to call an existing function.  Since we’re dealing with multiple modules now, we need to look for this function in all of the modules our helper class is handling.  If we find it in the module we’re currently working with, we can just use it, but if we find it in another module we need to create a prototype in the current module.  The function declaration we found in the other module will provide the function type.
We’ll create a new global variable (TheHelper) and get rid of the three previously mentioned.  In main() we’ll replace the code that creates and initializes those three objects with a single line of code:
TheHelper = new MCJITHelper(Context);
Now we just need to go through the code and replace uses of those three global objects with calls to our helper.  There aren’t as many as you might expect.  You can find references to TheModule in UnaryExprAST::Codegen(), BinaryExprAST::Codegen(), CallExprAST::Codegen(), and PrototypeAST::Codegen().  All of these except the last are just drop-in replacements.  In PrototypeAST::Codegen() we need to add a call to TheHelper->getModuleForNewFunction() to get the last argument to Function::Create().
Module* M = TheHelper->getModuleForNewFunction();
Function *F = Function::Create(FT, Function::ExternalLinkage, Name, M);
TheExecutionEngine is used only in HandleTopLevelExpression() and a direct replacement is suitable there, plus we can eliminate the call to finalizeObject since that will happen inside MCJITHelper::getPointerToFunction.
TheFPM is used in FunctionAST::Codegen() but that’s not where we’ll want it for MCJIT purposes.  Since we aren’t creating an ExecutionEngine until we need to compile a Module, I’m also going to put the FunctionPassManager creation there and optimize all the functions in a Module just before code generation.  This isn’t strictly necessary, but it makes the code generation phase go a bit faster.  We can put the following in MCJITHelper::getPointerToFunction() just after the execution engine is created:
// Create a function pass manager for this engine
FunctionPassManager *FPM = new FunctionPassManager(OpenModule);
// Set up the optimizer pipeline.  Start with registering info about how the
// target lays out data structures.
FPM->add(new DataLayout(*NewEngine->getDataLayout()));
// Provide basic AliasAnalysis support for GVN.
FPM->add(createBasicAliasAnalysisPass());
// Promote allocas to registers.
FPM->add(createPromoteMemoryToRegisterPass());
// Do simple "peephole" optimizations and bit-twiddling optzns.
FPM->add(createInstructionCombiningPass());
// Reassociate expressions.
FPM->add(createReassociatePass());
// Eliminate Common SubExpressions.
FPM->add(createGVNPass());
// Simplify the control flow graph (deleting unreachable blocks, etc).
FPM->add(createCFGSimplificationPass());
FPM->doInitialization();
// For each function in the module
Module::iterator it;
Module::iterator end = OpenModule->end();
for (it = OpenModule->begin(); it != end; ++it) {
// Run the FPM on this function
FPM->run(*it);
}
// We don't need this anymore
delete FPM;
Cross Module Linking
Let’s try what we have now.  Recompile using the command line above and start the program:
ready> def add(x y) x+y;
[output omitted]
ready> add(1, 2);
ready> Evaluated to 3.000000
ready> add(3, 4);
ready> LLVM ERROR: Program used external function ‘add’ which could not be resolved!
Do you see what happened there?  Our program created a module, added the function ‘add’ to it and then added a call to that function.  At this point, the MCJITHelper compiled that module and started a new module.  When we tried to call ‘add’ a second time, the generated call went into the new module, which doesn’t have a definition for ‘add’ – only a prototype.
To make this work we’re going to need some way to link our dynamic code against previously generated modules.
Here’s how linking works in MCJIT.  When code is generated from a Module, a complete object file image is generated into memory.  As MCJIT’s runtime loader is preparing this object for execution, it will create a list of external symbols that need to be resolved.  It will then call the MCJIT memory manager’s getPointerToNamedFunction method in an attempt to resolve these external symbols.  (Why the memory manager? Because that’s the component that knows which address space the JITed code will be running in.)  The default memory manager (SectionMemoryManager) uses sys::DynamicLibrary::SearchForAddressOfSymbol() to try to link this symbol against the current process.  If it can’t find the symbol, the symbol gets reported as unresolved.
We could solve the problem of linking dynamically generated objects by iterating through all the symbols in an object as it is loaded and calling sys::DynamicLibrary::AddSymbol() for each one.  In some circumstances that might be a good solution (as long as you aren’t worried about name conflicts).  However, I’d like to demonstrate an alternative solution which can be adapted to more general purposes.  I’m going to create a custom memory manager for linking purposes.
My new memory manager will inherit from SectionMemoryManager and use the base implementation for the actual memory management.  It will also attempt to reuse the base symbol resolution, but if a symbol is not found, it will delegate symbol resolution to our MCJITHelper class, which can search other loaded objects.
Here’s the code for the new memory manager:
class HelpingMemoryManager : public SectionMemoryManager
{
HelpingMemoryManager(const HelpingMemoryManager&) LLVM_DELETED_FUNCTION;
void operator=(const HelpingMemoryManager&) LLVM_DELETED_FUNCTION;
public:
HelpingMemoryManager(MCJITHelper *Helper) : MasterHelper(Helper) {}
virtual ~HelpingMemoryManager() {}
/// This method returns the address of the specified function.
/// Our implementation will attempt to find functions in other
/// modules associated with the MCJITHelper to cross link functions
/// from one generated module to another.
///
/// If \p AbortOnFailure is false and no function with the given name is
/// found, this function returns a null pointer. Otherwise, it prints a
/// message to stderr and aborts.
virtual void *getPointerToNamedFunction(const std::string &Name,
bool AbortOnFailure = true);
private:
MCJITHelper *MasterHelper;
};
void *HelpingMemoryManager::getPointerToNamedFunction(const std::string &Name,
bool AbortOnFailure)
{
// Try the standard symbol resolution first, but ask it not to abort.
void *pfn = SectionMemoryManager::getPointerToNamedFunction(Name, false);
if (pfn)
return pfn;
pfn = MasterHelper->getPointerToNamedFunction(Name);
if (!pfn && AbortOnFailure)
report_fatal_error("Program used external function '" + Name +
"' which could not be resolved!");
return pfn;
}
(Don’t forget to add this to the class definition if you’re coding along.)
Finally, we need to set the memory manager in MCJITHelper::getPointerToFunction where we use EngineBuilder to create a new execution engine.
ExecutionEngine *NewEngine = EngineBuilder(OpenModule)
.setErrorStr(&ErrStr)
.setUseMCJIT(true)
.setMCJITMemoryManager(new HelpingMemoryManager(this))
.create();
If you’re building against the LLVM 3.3 release, you need to use setJITMemoryManager instead of the more recently added setMCJITMemoryManager call.
Finally, chances are you’ve built LLVM with the default settings, which means you built it without runtime type information (RTTI).  If that is the case, you’ll also need to start building the sample program without RTTI to get the inheritance from SectionMemoryManager to link properly. If you do that, there’s a place in BinaryExprAST::Codegen where you’ll need to change a ‘dynamic_cast’ to a ‘reinterpret_cast’ to keep things working.  You lose a little automatic error checking that way, but since this is just a demo program I think we can live with that.  Alternatively, you could rebuild LLVM with RTTI enabled.
Here’s the new command line we’ll use for building our program:
clang++ -g -fno-rtti toy.cpp `llvm-config --cppflags --ldflags --libs core mcjit native` -O3 –o toy
Trying it out one more time:
ready> def add(x y) x+y;
[output omitted]
ready> add(1, 2);
ready> Evaluated to 3.000000
ready> add(3, 4);
ready> Evaluated to 7.000000
ready> def mul(x y) x*y;
[output omitted]
ready> mul(5, 6);
ready> Evaluated to 30.000000
ready> mul(7, add(8, 9));
ready> Evaluated to 119.000000
ready> extern exit();
[output omitted]
ready> exit();
Woo hoo!  It’s really working this time.
BTW, you see how that call to exit() got linked against our app, right?  The Kaleidoscope tutorial shows you something like that, but the tutorial is a bit out of date.  You can link against symbols in shared libraries that our program uses this way, but to link against symbols defined in the main program module you’ll need to build with the ‘-rdynamic’ flag.
clang++ -g -fno-rtti -rdynamic toy.cpp `llvm-config --cppflags --ldflags --libs core mcjit native` -O3 –o toy
Anyway, now we’ve got a functional Kaleidoscope interpreter built using MCJIT.  In the next installment I’ll do some crude performance analysis and look at ways that we can make it a little better.
The full source code listing for this post is available in the trunk of the LLVM source tree at <llvm_root>/examples/Kaleidoscope/MCJIT.
