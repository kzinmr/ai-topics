---
title: "Fuzzing"
type: concept
aliases:
  - fuzzing
  - fuzz testing
created: 2026-04-25
updated: 2026-11-18
tags:
  - concept
  - security
  - cybersecurity
  - software-quality
  - testing
  - vulnerability-discovery
  - vulnerability
sources:
  - https://en.wikipedia.org/wiki/Fuzzing
  - https://llvm.org/docs/LibFuzzer.html
  - https://google.github.io/oss-fuzz/
---

# Fuzzing

**Fuzzing** (fuzz testing) is the automated technique of feeding a program **malformed, random, or semi-structured inputs** at volume, watching for crashes, hangs, assertion failures, or sanitizer reports — and then minimizing the failing input (test-case reduction) into a reproducible bug. It is the most successful marriage of brute force and engineering in security: most memory-safety vulnerabilities in mature C/C++ codebases (browsers, kernels, parsers, compilers) were found by fuzzers, not by humans reading code.

## The taxonomy

| Class | Input strategy | Representative |
|-------|---------------|----------------|
| **Mutation-based (dumb→smart)** | Bit-flips, splices, dictionary tokens over seed corpus | zzuf, AFL, libFuzzer |
| **Generation-based** | Grammar-aware input synthesis | grammar fuzzers, protocol fuzzers |
| **Coverage-guided (grey-box)** | Evolutionary loop: inputs that reach new code branches are kept as seeds | **AFL/AFL++**, libFuzzer, honggfuzz |
| **White-box / symbolic** | Solve path constraints to reach deep branches | KLEE, SymQEMU |
| **Structure-aware** | Understand the input format (protobuf, ELF, images, SQL) | custom harnesses, libprotobuf-mutator |
| **Differential** | Fuzz *two* implementations, flag disagreements | compiler miscompile hunting, crypto cross-checks |

### Coverage-guided fuzzing, in one paragraph

The 2013 **American Fuzzy Lop** (AFL, Michal Zalewski) innovation was **instrument the program with edge coverage, then treat input generation as evolution**: programs are compiled with an instrumentation shim; a shared bitmap records which control-flow edges were hit; inputs that hit *new* edges become seeds and get mutated harder (with an scheduler overhavoc/splicing strategies). [[concepts/american-fuzzy-lop]] covers AFL specifically. Modern practice is **AFL++** (community fork with modular mutators, CmpLog, launchpad-style fuzzing) and **libFuzzer** (in-process, harness-driven, Sanitizer-integrated).

## Industrialization

- **OSS-Fuzz** (Google, 2016→): continuous fuzzing of ~1,000 critical open-source projects at scale, with ClusterFuzz fleets, auto-triage, and 90-day disclosure. Its results reshaped expectations: it is now normal that "every parser had crashes" — CVEs like Heartbleed-adjacent memory bugs, ImageMagick sagas, and OpenSSH/XZ supply-chain incidents all intersect the fuzzing ecosystem.
- **ClusterFuzzLite / CIFuzz**: fuzzing as CI, so regressions are caught per-PR.
- **Kernel/OS fuzzing**: syzkaller (Linux kernel, syzbot dashboard), Windows equivalent (Project Fuzz), hypervisor fuzzing.
- **Harness engineering** is the real skill: fuzzing a library requires a *crash-free, stateless entrypoint* (e.g. `LLVMFuzzerTestOneInput`); most fuzzing productivity is harness quality, corpus seeding, and dictionary/structure knowledge.

## Fuzzing in the LLM/agent era (this wiki's angle)

1. **LLMs writing fuzzing harnesses.** The bottleneck to fuzzing coverage has always been harness authoring. LLM agents that can read a library's API and emit correct harnesses + seed corpora collapse that cost — a direct line into [[concepts/ai-vulnerability-discovery]] and [[concepts/ai-vulnerability-detection-at-scale]].
2. **Agents as the fuzzing loop.** Differential-testing compilers for miscompiles (see [[concepts/ai-agent-compiler-bug-finding]], [[concepts/carlini-c-compiler-agents]]) is fuzzing where the agent generates programs, runs them across compiler versions ([[concepts/compiler-explorer]] as the interactive ancestor), and treats divergence as the oracle. The agent replaces the mutation engine with *semantic* generation.
3. **Fuzzing the LLM itself.** Prompt-injection and jailbreak research is effectively **adversarial input search over natural language** — automated red-teaming frameworks (GCG suffixes,PAIR-style jailbreak generation, cf. [[concepts/x-agentred-multi-service-red-teaming]]) are fuzzers whose mutation operator is an LLM. See [[concepts/ai-preflight-safety-testing]], [[concepts/ai-pre-release-testing]].
4. **Fuzzing agent toolchains**: MCP servers, sandbox escapes ([[concepts/agent-sandbox-patterns]]), and parsers in agent harnesses are the new C parsers — structure-aware fuzzing is being pointed at them.

## Sanitizers & oracles

Fuzzers are only as good as their crash detectors: **AddressSanitizer** (memory errors), **UBSan** (undefined behavior), **MSan** (uninitialized reads), plus differential oracles (output mismatch between implementations) and timeout/hang detection. ASan + libFuzzer + OSS-Fuzz is the canonical triad.

## Related Concepts

- [[concepts/american-fuzzy-lop]] — the founding coverage-guided fuzzer
- [[concepts/ai-vulnerability-discovery]] / [[concepts/ai-vulnerability-detection-at-scale]] — LLM-augmented fuzzing
- [[concepts/ai-agent-compiler-bug-finding]] — differential fuzzing of compilers by agents
- [[concepts/software-supply-chain-security]] — xz-utils, log4shell-era context
- [[concepts/threat-modeling]] — decides *what* to fuzz
- [[concepts/property-based-testing]] — the design-for-failure sibling in app land
- [[concepts/formal-methods]] — exhaustive vs probabilistic verification

## Sources

- Barton Miller's original fuzzing work (1988, University of Wisconsin)
- [OSS-Fuzz](https://google.github.io/oss-fuzz/)
- [libFuzzer documentation](https://llvm.org/docs/LibFuzzer.html)
- Zalewski, "American Fuzzy Lop" (2013)
