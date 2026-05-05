---
title: "LLVM 3.1 vector changes"
url: "https://blog.llvm.org/2011/12/llvm-31-vector-changes.html"
fetched_at: 2026-05-05T07:01:43.634269+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM 3.1 vector changes

Source: https://blog.llvm.org/2011/12/llvm-31-vector-changes.html

LLVM 3.1 vector changes
Intel uses the Low-Level Virtual Machine (LLVM) in a number of products, including the
Intel® OpenCL SDK
. The SDK's implicit vectorization module generates LLVM-IR (intermediate representation) which uses vector types.
LLVM-IR supports operations that use vector data types, and the LLVM code generator needs to do non-trivial work in order to efficiently compile vector operations into SIMD instructions. Recently, there were changes to the LLVM code generation that enabled better code generation for vector operations. In addition to many low level optimizations, this post talks about two major changes: the implementation of vector-select, and the support for vectors-of-pointers.
The LLVM-IR select instruction
The LLVM IR 'select' instruction is used to choose one value based on a condition. If the condition evaluates to 'True', the instruction returns the first value argument; otherwise, it returns the second value argument. For example:
%X = select i1 true, i8 17, i8 42          ; yields i8:17
The 'select' instruction also supports vector data types, where the condition is a vector of boolean data type. If the condition is a vector of booleans (see above), then the selection is done per element.
Vector-select instructions are very useful for vectorizing compilers, which use them to 'mask-out' inactive SIMD lanes. Until recently, the LLVM code generator did not support conditions with vector data types. Enabling them required enhancing several other areas of the code generator.
SSE blends
Intel's SSE4.1 instruction set features the PBLENDVB instruction. This instruction selects byte values from registers XMM1 and XMM2, using a mask specified in the high bit of each byte in XMM0, and stores the values into XMM1. There are also other instructions for handling larger data types, such as 32-bit integers, etc. It may seem odd for the selector bits to be the high bit, but the vector-compare machine instructions also set the high bits, so that the compare and blend instructions can work together efficiently.
As mentioned earlier, the LLVM-IR 'select' instruction represents the mask as a vector of booleans, which need to be translated into the high-bit of each SIMD vector element. This translation is done by the Type-Legalizer phase in the LLVM code generator.
Type Legalization
The Type Legalizer is a code generation phase that converts operations of any arbitrary data type which is represented by the LLVM-IR, into operations that use types which are supported by the target machine. For example, on x86 architecture, general purpose registers support the types i8, i16, i32 and i64. These types are 'Legal' because they fit into a machine register. The type i24 is 'Illegal' because it does not match a native x86 machine register. The Type-Legalizer has a complex set of rules for legalizing different types, and in many cases the type legalization takes multiple steps.The Type-Legalizer has a number of strategies for handling illegal vector types:
Widening - The type-legalizer can widen vectors by adding additional elements. For example, the type <3 x float> would be widened to the legal type '<4 x float>'.
Splitting - The type-legalizer can split large vectors into smaller types. For example, a value of type <8 x float> can be split into two values of the legal type '<4 x float>'.
Scalarizing - The type-legalizer can break a vector into multiple scalars. For example, an operation of type <2 x i64> can be done on two 64-bit scalars using general purpose registers.
Notice that none of the strategies above can translate the type '<4 x i1>' into the register-sized type '<4 x i32>'. To support the code-generation of vector-select, we added a new legalization kind which can support the promotion of each element in the vector, rather than increasing the number of elements in the vector.
LLVM already promotes small scalar integers into larger integers. For example, the type i8 is promoted to i32 on processors that do not support types smaller than 32 bits. Once the new type legalization technique was implemented, adding support for the select instruction was easy. Much like other instructions, a simple pattern in the TD file added support for different 'blend' instructions for different generations of the Intel Architecture (SSE4.1, AVX and AVX2). Processors that do not support the 'blend' instruction, lower the vector-select IR into a sequence of AND,XOR,OR with acceptable performance.
Optimizations for Element Promotion
The new type-legalization method for vectors and the new vector-select implementation is open for new optimizations. For example, consider the problem of saving a vector of type '<4 x i8>' into memory. The in-memory representation of this type is that of four consecutive bytes, but the vector's in-register representation is '<4 x i32>'. Without any additional optimizations, the naive way of saving the vector would be to extract each one of the bytes into a general purpose register and to save them one by one into memory. One of the optimizations that we added recently is to shuffle all of the saved bytes into the lower part of the vector and save the four bytes into memory using a single scalar 32 bit store.
Vectors of pointers
Until recently, LLVM's vector type only contained elements which were integers or floating point. This abstraction matched the common SIMD instruction sets and enabled efficient code generation for many processors. In many cases vectorizing compilers wish to represent a vector of pointers, mainly for implementing scatter/gather memory operations. The lack of support in the IR made some vectorizing compilers worke around limitation by converting pointers to integers. This solution required the vectorizing compiler to implement address calculation manually, and added complexity to the software.
To solve this, LLVM now supports the pointer-vector type, as well as the instructions to manipulate it. Much like other vector instructions, the pointer-vector can be created and modified using the instructions 'insertelement', 'extractelement' and 'shufflevector'. However, pointer-vector types would not be so useful without vector 'getelementptr' instructions. We extended LLVM's GEP instruction to support vectors of pointers. The new pointer-vector abstraction enables better code generation, even for processors which do not support explicit gather/scatter instructions, since address calculation is now done on vectors.The following code is now legal in LLVM:
define i32 @foo(<4 x i32*> %base, <4 x i32> %offset) nounwind {
entry:
%A2 = getelementptr <4 x i32*> %base, <4 x i32> %offset
%k = extractelement <4 x i32*> %A2, i32 3
%v = load i32* %k
ret i32 %v
}
We currently support only vectors of pointers to primitive types. In the future we may add additional capabilities and optimizations.
Conclusion
Intel® OpenCL SDK features an implicit vectorization module which uses the LLVM compiler toolkit for code generation. We are continuing to improve LLVM's code generation support for vectors, in order to support future Intel Architectures.
LLVM 3.1 will feature a number of changes that will enable vectorizing compilers to generate better code.
