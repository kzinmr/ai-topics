---
title: "30% faster Windows builds with clang-cl and the new /Zc:dllexportInlines- flag"
url: "https://blog.llvm.org/2018/11/30-faster-windows-builds-with-clang-cl_14.html"
fetched_at: 2026-05-05T07:01:37.966737+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# 30% faster Windows builds with clang-cl and the new /Zc:dllexportInlines- flag

Source: https://blog.llvm.org/2018/11/30-faster-windows-builds-with-clang-cl_14.html

30% faster Windows builds with clang-cl and the new /Zc:dllexportInlines- flag
Background
In the course of adding Microsoft Visual C++ (MSVC) compatible Windows support to Clang, we worked hard to make sure the
dllexport and dllimport declspecs
are handled the same way by Clang as by MSVC.
dllexport and dllimport are used to specify what functions and variables should be externally accessible ("exported") from the currently compiled Dynamic-Link Library (DLL), or should be accessed ("imported") from another DLL. In the class declaration below,
S::foo()
will be exported when building a DLL:
struct __declspec(dllexport) S {
void foo() {}
};
and code using that DLL would typically see a declaration like this:
struct __declspec(dllimport) S {
void foo() {}
};
to indicate that the function is defined in and should be accessed from another DLL.
Often the same declaration is used along with a
preprocessor macro
to flip between dllexport and dllimport, depending on whether a DLL is being built or consumed.
The basic idea of dllexport and dllimport is simple, but the semantics get more complicated as they interact with more facets of the C++ language: templates, inheritance, different kinds of instantiation, redeclarations with different declspecs, and so on. Sometimes the semantics are surprising, but by now we think clang-cl gets most of them right. And as the old maxim goes, once you know the rules well, you can start tactfully breaking them.
One issue with dllexport is that for inline functions such as
S::foo()
above, the compiler must emit the definition
even if it's not used in the translation unit
. That's because the DLL must export it, and the compiler cannot know if any other translation unit will provide a definition.
This is very inefficient. A dllexported class with inline members in a header file will cause definitions of those members to be emitted in
every translation unit that includes the header
, directly or indirectly. And as we know, C++ source files often end up including a lot of headers. This behaviour is also different from non-Windows systems, where inline function definitions are not emitted unless they're used, even in shared objects and dynamic libraries.
/Zc:dllexportInlines-
To address this problem, clang-cl recently gained a new command-line flag,
/Zc:dllexportInlines-
(MSVC uses the /Zc: prefix for
language conformance options
). The basic idea is simple: since the definition of an inline function is available along with its declaration, it's not necessary to import or export it from a DLL — the inline definition can be used directly. The effect of the flag is to not apply class-level dllexport/dllimport declspecs to inline member functions. In the two examples above, it means
S::foo()
would not be dllexported or dllimported, even though the
S
class is declared as such.
This is very similar to the
-fvisibility-inlines-hidden
Clang and GCC flag used on non-Windows. For C++ projects with many inline functions, it can significantly reduce the set of exported functions, and thereby the symbol table and file size of the shared object or dynamic library, as well as program load time.
On Windows however, the main benefit is not having to emit the unused inline function definitions. This means the compiler has to do much less work, and reduces object file size which in turn reduces the work for the linker. For Chrome, we
saw 30 % faster full builds
, 30 % shorter link times for blink_core.dll, and 40 % smaller total .obj file size.
The reduction in .obj file size, combined with the enormous reduction in .lib files allowed by previously switching linkers to lld-link which uses thin archives, means that a typical Chrome build directory is now 60 % smaller than it would have been just a year ago.
(Some of the same benefit can be had without this flag if the dllexport inline function comes from a pre-compiled header (PCH) file. In that case, the definition will be emitted in the object file when building the PCH, and so is not emitted elsewhere unless it's used.)
Compatibility
Using /Zc:dllexportInlines- is "half ABI incompatible". If it's used to build a DLL, inline members will no longer be exported, so any code using the DLL must use the same flag to not dllimport those members. However, the reverse scenario generally works: a DLL compiled without the flag (such as a system DLL built with MSVC) can be referenced from code that uses the flag, meaning that the referencing code will use the inline definitions instead of importing them from the DLL.
Like -fvisibility-inlines-hidden, /Zc:dllexportInlines- breaks the C++ language guarantee that (even an inline) function has a unique address within the program. When using these flags, an inline function will have a different address when used inside the library and outside.
Also, these flags can lead to link errors when inline functions, which would normally be dllimported, refer to internal symbols of a DLL:
void internal();
struct __declspec(dllimport) S {
void foo() { internal(); }
}
Normally, references to
S::foo()
would use the definition in the DLL, which also contains the definition of
internal()
, but when using /Zc:dllexportInlines-, the inline definition of
S::foo()
is used directly, resulting in a link error since no definition of
internal()
can be found.
Even worse, if there is an inline definition of
internal()
containing a static local variable, the program will now refer to a different instance of that variable than in the DLL:
inline int internal() { static int x; return x++; }
struct __declspec(dllimport) S {
int foo() { return internal(); }
}
This could lead to very subtle bugs. However, since Chrome already uses -fvisibility-inlines-hidden, which has the same potential problem, we believe this is not a common issue.
Summary
/Zc:dllexportInlines- is like -fvisibility-inlines-hidden for DLLs and significantly reduces build times. We're excited that using Clang on Windows allows us to benefit from new features like this.
More information
For more information, see the
User's Manual for /Zc:dllexportInlines-
.
The flag was added in Clang
r346069
, which will be part of the Clang 8 release expected in March 2019. It's also available in the
Windows Snapshot Build
.
Acknowledgements
/Zc:dllexportInlines- was implemented by Takuto Ikuta based on a prototype by Nico Weber.
