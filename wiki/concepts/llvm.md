---
title: "LLVM"
type: concept
created: 2026-04-25
updated: 2026-08-01
tags:
  - compiler
  - programming-language
  - open-source
  - infrastructure
aliases:
  - llvm
  - low-level-virtual-machine
related:
  - concepts/programming-languages
  - concepts/compiler-construction
  - concepts/compiler-explorer
  - entities/modular
sources:
  - https://blog.llvm.org/posts/2025-03-11-flang-new/
  - raw/articles/blog.llvm.org--posts-2025-03-11-flang-new--8f37a052.md
---

# LLVM

**LLVM** (historically "Low Level Virtual Machine") is an open-source compiler infrastructure project that provides a modular collection of reusable compiler and toolchain technologies. It is the backbone of modern compilation: the LLVM Intermediate Representation (LLVM IR) serves as a common backend target for languages including C/C++ (Clang), Rust, Swift, Julia, and increasingly Fortran (Flang), and the **MLIR** framework built on top of it underpins AI compiler stacks.

## Core Components

- **LLVM IR** — A low-level, language-agnostic intermediate representation. All compilers using LLVM as a backend eventually emit LLVM IR; its drawback is that it discards language-specific information (e.g., Fortran array semantics), which motivated higher-level IRs.
- **Clang** — The C/C++/Objective-C frontend; the reference model for how a frontend feeds LLVM IR.
- **MLIR (Multi-Level Intermediate Representation)** — Introduced to the LLVM community in 2019. Makes it cheap to define and introduce new abstraction levels with in-the-box compiler-engineering infrastructure, solving the "high-level language details don't map cleanly to LLVM IR" problem without each language building bespoke IR infrastructure (as Swift and Rust originally did).
- **Flang** — The Fortran frontend/compiler (see below).

## Flang: LLVM's Fortran Compiler

Flang is a case study in decade-long compiler incubation and open-source community building. Fortran (created in the 1950s as "Formula Translation") remains dominant in scientific computing — over **80% of applications on ARCHER2**, the UK national supercomputer (750,000-core Cray EX), are written in Fortran — and has seen a modern resurgence (package manager `fpm`, unofficial standard library, LFortran).

**Why build another Fortran compiler?** The US National Labs (LANL, led by Pat McCormick) and NVIDIA partnered because GFortran alone is a single point of failure for the US scientific mission; multiple independent open-source implementations reduce that risk and uncover standard ambiguities.

### Timeline highlights

| Year | Milestone |
|------|-----------|
| 1989 | Portland Group (PGI) formed — C, Fortran 77, C++ compilers for Intel i860 |
| 2000 | PGI becomes STMicroelectronics subsidiary |
| Aug 2011 | Bill Wendling starts LLVM-based Fortran compiler "Flang" (later renamed "Fort") |
| Jul 2013 | PGI sold to NVIDIA |
| Nov 2015 | NVIDIA joins DOE Exascale Computing Project; commits to open-sourcing PGI Fortran frontend + runtime to LLVM |
| May 2017 | First release of "Classic Flang" (PGI frontend + LLVM IR backend) as separate repo |
| Apr 2018 | Steve Scalpone (NVIDIA) announces frontend rewrite → "F18" |
| Aug 2018 | Eric Schweitz begins "FIR" (Fortran Intermediate Representation), later reimplemented as an **MLIR dialect** |
| Apr 2019 | F18 approved for migration into the LLVM Project monorepo |
| 2019 | MLIR debuts; FIR adopts it — likely the first "serious project" outside Google to use MLIR |
| Oct 2024 | `flang-new` renamed to `flang` via the LLVM proposal process (Brad Richardson; Chris Lattner weighed in) |
| Nov 2024 | AMD announces next-gen Fortran compiler based on LLVM Flang; Arm ships experimental toolchain with Flang |
| Mar 2025 | LLVM 20.1.0 — first release including the `flang` binary |

### Technical highlights

- **HLFIR** (High Level Fortran IR) addressed many performance/correctness issues pre-rename.
- Cross-company team (Arm, Huawei, Linaro, NVIDIA, Qualcomm) made SPEC 2017 buildable with Flang; OpenMP support to 2.5; Linaro showed Flang performance near GFortran; the GFortran test suite was added to the LLVM Test Suite; Fujitsu's and IBM's test suites were opened up.
- Renaming criteria (agreed by community): document known limitations, complete expected bug fixes, fail loudly on unimplemented features, competitive performance, public test-suite pass rates, and prevent Classic Flang confusion.

## AI Relevance

MLIR is central to AI infrastructure: it underpins accelerator compiler stacks (NVIDIA, AMD), TensorFlow, and torch-mlir, and its multi-level dialect design is the standard approach for mapping high-level model graphs to hardware. LLVM/MLIR therefore sit directly beneath the inference/training compilation layer of modern AI systems. Chris Lattner, LLVM co-founder, went on to found [[entities/modular]] (Mojo language, MAX AI platform). [[concepts/compiler-explorer]] is the web playground where Flang and other LLVM-based compilers can be tried interactively.

## Related Concepts

- [[concepts/programming-languages]] — Language adoption dynamics (see Paul Graham's "Being Popular" theory)
- [[concepts/compiler-construction]] — General compiler construction methodologies
- [[concepts/compiler-explorer]] — Interactive compiler playground supporting Flang
- [[entities/modular]] — Chris Lattner's AI infrastructure company (LLVM lineage)

## Sources

- [LLVM Blog: "LLVM Fortran Levels Up: Goodbye flang-new, Hello flang!" (Mar 2025)](https://blog.llvm.org/posts/2025-03-11-flang-new/)
- Raw: `raw/articles/blog.llvm.org--posts-2025-03-11-flang-new--8f37a052.md`
