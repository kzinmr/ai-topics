---
title: "Object Caching with the Kaleidoscope Example Program"
url: "https://blog.llvm.org/2013/08/object-caching-with-kaleidoscope.html"
fetched_at: 2026-05-05T07:01:43.025645+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Object Caching with the Kaleidoscope Example Program

Source: https://blog.llvm.org/2013/08/object-caching-with-kaleidoscope.html

Object Caching with the Kaleidoscope Example Program
By Andy Kaylor
Aug 2, 2013
#MC
,
#jit
9 minute read
In previous posts I described the process of porting the LLVM Kaleidoscope tutorial program to use MCJIT as its execution engine and introduced a lazy compilation implementation with the MCJIT engine.  The lazy implementation produced similar, and in some cases better, performance when compared with an implementation based on the older JIT execution engine, but it used more memory.
In this post, I’m going to extend the new implementation to use MCJIT’s object caching interface.  This will give our interpreter a way to store pre-compiled versions of previously used function and retrieve them for execution in later runs of the program.
Adding a Library Parsing Mechanism
I’m going to base the object caching on a library loading model.  In theory we could cache any object that the execution engine generates, but to make effective use of the cache we need some way of knowing that what we’re loading matches something we previously stored.  For simplicity, I’m going to extend the Kaleidoscope tutorial to accept a command line argument that references an LLVM IR file to be loaded as a library.  Once that’s working, I’ll introduce the object caching mechanism.
The IR loading is a fairly easy thing to add.  We’ll use a standard LLVM command line parsing template:
cl::opt<std::string>
InputIR("input-IR",
cl::desc("Specify the name of an IR file to load for function definitions"),
cl::value_desc("input IR file name"));
Then in the main() function, we’ll add argc and argv parameters along with a call to parse the command line options.
int main(int argc, char **argv) {
InitializeNativeTarget();
InitializeNativeTargetAsmPrinter();
InitializeNativeTargetAsmParser();
LLVMContext &Context = getGlobalContext();
cl::ParseCommandLineOptions(argc, argv,
"Kaleidoscope example program\n");
if (!InputIR.empty()) {
parseInputIR(InputIR);
}
...
}
Happily, LLVM also gives us what we need to parse an IR file into a module:
bool parseInputIR(std::string InputFile) {
SMDiagnostic Err;
Module *M = ParseIRFile(InputFile, Err, getGlobalContext());
if (!M) {
Err.print("IR parsing failed: ", errs());
return false;
}
char ModID[256];
sprintf(ModID, "IR:%s", InputFile.c_str());
M->setModuleIdentifier(ModID);
TheHelper->addModule(M);
return true;
}
I’m setting an identifier that we can use to recognize that this module was loaded as an IR file.  We’ll use that later for object caching, but right now it also lets us skip the function optimization passes when we compile this module.
// Get the ModuleID so we can identify IR input files
const std::string ModuleID = M->getModuleIdentifier();
// If we've flagged this as an IR file, it doesn't need function passes run.
if (0 != ModuleID.compare(0, 3, "IR:")) {
// Create a function pass manager for this engine
FunctionPassManager *FPM = new FunctionPassManager(M);
...
}
Finally, we need to provide a function to add the newly created module to the list of modules handled by MCJITHelper.
void MCJITHelper::addModule(Module* M) {
Modules.push_back(M);
}
Our lazy compilation mechanism will take care of compiling this module when any function it contains is called.
When we build the program now, we need to add ‘irreader’ to the list of libraries on the compile line.
At this point, we can provide a complete IR file as input to our Kaleidoscope interpreter.  You can generate an IR file by capturing the ‘dump’ output of a module that has been created by our interpreter.  It’s easiest to do this using the old JIT-based implementation, since it keeps everything in one module.  Because the particulars of where an input file will come from are likely to be implementation specific, I’ll just leave it at that for now.
Implementing Object Cache
The mechanism above to load IR files can be used with either the JIT or MCJIT implementations of the Kaleidoscope interpreter.  With the MCJIT implementation, there is a significant time hit for compilation the first time a library is accessed, but subsequent references will be very fast.  With the JIT implementation, the module parsed from IR is compiled lazily and so its responsiveness will be more uniform.
However, MCJIT provides a mechanism for caching generated object images.  Once we’ve compiled a module, we can store the image and never have to compile it again.  This is not available with the JIT execution engine and gives MCJIT a significant performance advantage when a library is used in multiple invocations of the program.
MCJIT uses a callback mechanism to allow clients to register a custom cache handler.  The handler must be a subclass of the ObjectCache class defined in ‘llvm/ExecutionEngine/ObjectCache.h.”  For this example, I’m going to use a very simple scheme that uses the input IR filename as a key and stores cached files in a subdirectory relative to the current working directory.  Obviously in a real product you’d want something more sophisticated, but for demonstration purposes this will work.
Here’s the implementation:
//===----------------------------------------------------------------------===//
// MCJIT object cache class
//===----------------------------------------------------------------------===//
class MCJITObjectCache : public ObjectCache {
public:
MCJITObjectCache() {
// Set IR cache directory
sys::fs::current_path(CacheDir);
sys::path::append(CacheDir, "toy_object_cache");
}
virtual ~MCJITObjectCache() {
}
virtual void notifyObjectCompiled(const Module *M, const MemoryBuffer *Obj) {
// Get the ModuleID
const std::string ModuleID = M->getModuleIdentifier();
// If we've flagged this as an IR file, cache it
if (0 == ModuleID.compare(0, 3, "IR:")) {
std::string IRFileName = ModuleID.substr(3);
SmallString<128>IRCacheFile = CacheDir;
sys::path::append(IRCacheFile, IRFileName);
if (!sys::fs::exists(CacheDir.str()) && sys::fs::create_directory(CacheDir.str())) {
fprintf(stderr, "Unable to create cache directory\n");
return;
}
std::string ErrStr;
raw_fd_ostream IRObjectFile(IRCacheFile.c_str(), ErrStr, raw_fd_ostream::F_Binary);
IRObjectFile << Obj->getBuffer();
}
}
// MCJIT will call this function before compiling any module
// MCJIT takes ownership of both the MemoryBuffer object and the memory
// to which it refers.
virtual MemoryBuffer* getObject(const Module* M) {
// Get the ModuleID
const std::string ModuleID = M->getModuleIdentifier();
// If we've flagged this as an IR file, cache it
if (0 == ModuleID.compare(0, 3, "IR:")) {
std::string IRFileName = ModuleID.substr(3);
SmallString<128> IRCacheFile = CacheDir;
sys::path::append(IRCacheFile, IRFileName);
if (!sys::fs::exists(IRCacheFile.str())) {
// This file isn't in our cache
return NULL;
}
OwningPtr<MemoryBuffer> IRObjectBuffer;
MemoryBuffer::getFile(IRCacheFile.c_str(), IRObjectBuffer, -1, false);
// MCJIT will want to write into this buffer, and we don't want that
// because the file has probably just been mmapped.  Instead we make
// a copy.  The filed-based buffer will be released when it goes
// out of scope.
return MemoryBuffer::getMemBufferCopy(IRObjectBuffer->getBuffer());
}
return NULL;
}
private:
SmallString<128> CacheDir;
};
I’m going to instantiate this cache as a member variable of the MCJITHelper class.  I’m also adding a command line option to enable cache use.
cl::opt<bool>
UseObjectCache("use-object-cache",
cl::desc("Enable use of the MCJIT object caching"),
cl::init(false));
Activating the cache simply requires a single call to the ExecutionEngine object after it has been created in MCJITHelper::compileModule():
if (UseObjectCache)
NewEngine->setObjectCache(&OurObjectCache);
At this point the MCJIT engine itself manages use of the cache.  When the MCJIT engine is about to compile a module, it will call the cache’s getObject method.  If this method returns an object image, MCJIT will prepare that object for execution rather than compiling a new version.  When MCJIT does compile a module it calls the cache’s NotifyObjectCompiled method, giving the cache a chance to store the object image.
The implementation above uses the Module identifier as a key to identify matching modules, but clients are free to use any mechanism to make this identification.
Cache Performance
Now that we have the object caching mechanism in place, let’s take a look and see how it impacts our performance.
I’ve created a new set of test inputs based on the inputs I used for previous measurements, but I separated the function definitions and the immediate function calls into separate script files and then generated an IR file from the function definitions.  I’ll use these files to execute a workload that is equivalent to the previous workload while using an IR input file and loading the resultant object from cache when possible.
There is obviously some performance benefit just from having a ready-made IR file rather than having to parse Kaleidoscope input, so I also created a version of the JIT-based implementation which accepts the IR input library to provide a meaningful point of comparison.
The chart below shows the 5000-function workloads I’ve been using run with multiple implementations of the Kaleidoscope interpreter.  The first three bars in each group show the “lazy” MCJIT implementation, the original JIT implementation and our first working MCJIT implementation with the original workload file.  The next three bars show the new implementations using an IR input file for function definitions.
As you can see, the non-cached run of the library-based MCJIT implementation is slightly faster than our first working implementation (because the IR is pre-made), but significantly slower than the “lazy” MCJIT implementation.  However, this performance hit is only incurred the first time the workload is run.  When the workload is run with this same MCJIT implementation a second time the function library is loaded from cache and the performance is far and away better than any of the other implementations.
Conclusions
So where does this leave us?  Did you ever have one of those math professors in college who would get halfway through a tricky proof and then write “QED” on the board even though it wasn’t at all obvious how he would finish it?  That’s the part we’re at now.
I began this exercise in an attempt to either prove or disprove that the MCJIT execution engine was suitable for use in a program that relied on true just-in-time compilation.  I came up with a reference implementation that does that, though with a few lingering questions – particularly regarding memory consumption.
At this point, I’m satisfied that MCJIT is up to the task.
Quod erat demonstratum
.
Of course, there’s more work to be done.  Any serious implementation using the techniques I’ve shown would require a lot of fine tuning.  Some of what I’ve done, such as the multiple module management, can and should be moved into the MCJIT component itself.  No doubt many of the opportunities for performance improvements and more efficient memory use will also be within the MCJIT component.  Nevertheless, I think the way forward is reasonably well defined.
Several active LLVM developers are committed to making MCJIT a top notch execution engine.  I hope that the exploration I’ve presented here will help more developers make use of it now and will generate momentum to iron out whatever additional shortcomings remain.
The full source code listing for this post along with the scripts for generating test input are available in the trunk of the LLVM source tree at <llvm_root>/examples/Kaleidoscope/MCJIT.
