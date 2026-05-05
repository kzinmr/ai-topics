---
title: "Interactive programming in C++ internships - LLVM Blog Post"
url: "https://blog.llvm.org/posts/2022-12-21-compiler-research-internships/"
fetched_at: 2026-05-05T07:01:36.999279+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Interactive programming in C++ internships - LLVM Blog Post

Source: https://blog.llvm.org/posts/2022-12-21-compiler-research-internships/

Interactive programming in C++ internships — LLVM Blog Post
Another program year is ending and our
Compiler Research
team is extremely happy to share the hard work and the results of our interns
contributors!
The Compiler Research team includes researchers located at Princeton University
and CERN.
Our primary goal is research into foundational software tools helping scientists
to program for speed, interoperability, interactivity, flexibility, and
reproducibility. We work in various fields of science such as high energy
physics, where research is fundamentally connected to software at exabyte scale.
We develop computational methods and research software for scientific
exploration and discovery. Our current research focuses on three main topics:
interpretative C/C++/CUDA
, automatic differentiation tools, and C++ language interoperability with Python
and D.
This year, we had six participants who worked on seven projects, covering a wide
range of topics, from LLVM’s new JIT linker
(
JITLink
) to
Clang-Repl
,
an interactive C++ interpreter for incremental compilation integrated
in
Clang
. All projects rise toward a
common, ambitious goal:
to establish a proficient workflow in LLVM,
where
interactive
development in C++
is possible, and exploratory C++ becomes an accessible
experience to a wider audience.
Below you can find the list of projects from our interns, an overview of the
objectives and results. We invite you to follow the links to access a more
detailed description of each project.
Developer:
Sunho Kim
(
Computer Science, De Anza College, Cupertino, California
)
Mentors:
Stefan Gränitz
(
Freelance Compiler Developer, Berlin,
Deutschland
),
Lang Hames
(
Apple
),
Vassil Vassilev
(
Princeton University/CERN
)
Funding:
Google Summer of Code 2022
Suhno developed a
JITLink
specialization that extends JITLink’s generic linker algorithm, allowing
JITLink to support ELF/aarch64 target and provides full support of all advanced
PE/COFF object file features. By supporting the ELF/aarch64 target, JITLink can
now be used in Julia, while COFF/X86_64 enables Microsoft Visual C++ (MSCV)
target in
Clang-Repl
.
Here you can find Sunho’s GSoC
final report
.
Hurray!
This project has been accepted as a Tutorial at the
2022 LLVM Developers’ Meeting
!
The conference took place in San Jose, California, from 7th to 10th November
2022.
Here you can find the
video
and the
slides
of Sunho’s presentation.
The project was also presented at the Compiler As a Service (CaaS) monthly
meeting. Here you can find the
video
and the
slides
of Sunho’s presentation.
Developer:
Matheus Izvekov
Mentors:
Richard Smith
(
Google
),
Vassil Vassilev
(
Princeton
University/CERN
)
Funding:
Google Summer of Code 2022
Clang
’s type system was optimized by
pushing type-syntactic-sugar on the arguments of a template specialization into
those member accesses. This was achieved by: 1. creating a new type node into
the Abstract Syntax Tree (AST) that represents the sugar of a member access in
a template specialization; and 2. implementing single step desugaring logic
which will perform the substitution of template parameter sugar into the
corresponding specialization argument sugar. As a result, we improved Clang’s
diagnostic system by enabling other constructs to preserve type sugar, allowing
both for their representation when present in the specialization argument.
Here you can find Matheus’ GSoC
final report
.
Hurray!
This project has been accepted as a Lightning Talk at the
2022 LLVM Developers’ Meeting
!
The conference took place in San Jose, California, from 7th to 10th November
2022.
Here you can find the
video
and the
slides
of Matheus’ presentation.
Developers:
Jun Zhang
(
Software Engineering, Anhui Normal University, WuHu, China
) and
Purva Chaudhari
(
California State University Northridge, Northridge CA, USA
)
Mentors:
Vassil Vassilev
(
Princeton University/CERN
)
Clang-Repl
is an
interactive C++ interpreter integrated in Clang, which enables incremental
compilation. It supports interactive programming for C++ in a
Read-Eval_Print Loop
(
REPL
)
style, compiling the code just-in-time with a JIT approach that reduces the
compile-run cycles. We added the “undo” functionality to Clang-REPL, and we
improved error-recovery by adding the possibility to recover the low-level
execution infrastructure. As a result, Clang-REPL now supports reversal
execution and recovery actions on behalf of a user in an automatic and
convenient way.
Hurray!
This project has been accepted as a Lightning Talk at the
2022 LLVM Developers’ Meeting
!
The conference took place in San Jose, California, from 7th to 10th November
2022.
Here you can find the
video
and the
slides
of Purva and Jun’s presentation.
Developer:
Anubhab Ghosh
(
Computer Science and Engineering, Indian Institute of Information Technology, Kalyani, India
)
Mentors:
Stefan Gränitz
(
Freelance Compiler Developer, Berlin, Deutschland
),
Lang Hames
(
Apple
),
Vassil Vassilev
(
Princeton University/CERN
)
Funding:
Google Summer of Code 2022
Anubhab introduced a new
JITLinkMemoryManager
based on a MemoryMapper abstraction that is capable of allocating JIT code
(and data) using shared memory. The following advantages should arise from the
implemented strategy: 1. a faster transport (and access) for code and data when
running JIT’d code in a separate process on the same machine, and 2. the
guarantee that all allocations are close together in memory and meet the
constraints of the default code model allowing the use of outputs from regular
compilers.
Here you can find Anubhab’s GSoC
final report
.
Hurray!
This project has been accepted as a Lightning Talk at the
2022 LLVM Developers’ Meeting
!
The conference took place in San Jose, California, from 7th to 10th November
2022.
Here you can find the
video
and the
slides
of Anubhab’s presentation.
Developer:
Jun Zhang
(
Software Engineering, Anhui Normal University, WuHu, China
)
Mentors:
David Lange
(
Princeton University
),
Alexander Penev
(
University of Plovdiv Paisii Hilendarski, Bulgaria
),
Vassil Vassilev
(
Princeton University/CERN
)
Funding:
Google Summer of Code 2022
The current performance of the modules usage in
ROOT
was evaluated, and a strategy for optimizing the memory footprint was developed.
This strategy includes reducing unnecessary symbol-lookups and module-loading,
and is especially useful for very large codebases like
CMSSW
,
where Jun reduced the amount of memory by half (from 1.1GB to 600MB) for simple
workflows like hsimple.C, and the number of loaded from 180 to 52.
Here you can find Jun’s GSoC
final report
.
Developer:
Manish Kausik H
(
.Tech and M.Tech in Computer Science and Engineering(Dual Degree),
Indian Institute of Technology Bhubaneswar
)
Mentors:
David Lange
(
Princeton University
),
William Moses
(
Massachusetts Institute of Technology
),
Vassil Vassilev
(
Princeton University/CERN
)
Funding:
Google Summer of Code 2022
Clad
is an open
source plugin to the Clang compiler that enables
Automatic Differentiation
for C++. Clad receives an Abstract Syntax Tree (AST) from the underlying
compiler platform (Clang), decides whether a derivative is requested and
produces it, and modifies the AST to insert the generated code.
Enzyme AD
is an LLVM based AD plugin.
It works by taking existing code as LLVM IR and computing the derivative
(and gradient) of that function.
In this project, Manish integrated Enzyme within Clad, giving a Clad user the
option of selecting Enzyme for Automatic Differentiation on demand. The
integration of Clad and Enzyme t results in a new tool that offers an optimized
and flexible implementation of automatic differentiation.
Here you can find Manish’s GSoC
final report
.
Thank you, developers!
We hope our interns contributors enjoyed our community. Our best reward is to
know that we supported your early steps into the world of open-source software
development and compiler construction. We hope that this experience motivated
you to continue to be involved with the broad LLVM ecosystem.
We express our gratitude to the
Google Summer of Code
Program and to the Institute for Research and Innovation in Software for High
Energy Physics (
IRIS-HEP
) for supporting our
research and providing six young developers this wonderful opportunity.
A special thanks goes to the LLVM community for being supportive and for sharing
their knowledge and introducing our community to the new contributors. Thank you
so much!
Thanks for choosing Compiler-Research for your internship! We were lucky to
have you!
