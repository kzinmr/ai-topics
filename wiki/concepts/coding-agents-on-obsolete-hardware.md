---
title: "Coding agents on obsolete and exotic hardware"
created: 2026-11-23
updated: 2026-11-23
type: concept
tags: [coding-agent, ai-hardware, retro-computing, vibe-coding, agent-skills]
sources:
  - raw/articles/2026-11-21_ricapar_clawdos.md
  - raw/articles/2026-11-20_ankitg_vibecoding-an-inference-chip.md
  - raw/articles/jayd.ml--2026-11-01-llms-are-going-to-crush-every-bug-html--b5609894.md
---

# Coding agents on obsolete and exotic hardware

**One-line summary**: Three Nov 2026 projects put coding agents on hardware they were never meant to touch — a 4.77 MHz 8088, an FPGA inference chip, a 9-year-old tablet — and all three succeeded, with the agent's cross-domain fluency (Verilog, kernel C, Turbo C) as the common variable.

## Thesis

The limiting factor for "what can an agent build" has shifted from the agent's domain knowledge to the human's choice of problem. In all three cases the author had little or no expertise in the target domain (the FPGA author had "never written Verilog"; the DOS harness is 100% agent-written) yet shipped working systems. The recurring pattern: agents handle exploration and low-level codegen; humans still define the correctness contract and the iteration loop ("the humans are still useful at defining how to iterate fast and what correctness looks like, and the agents are great to manage the exploration" — ankitg).

## ClawDOS — an agent harness on an IBM PC 5160 (Nov 21, 2026, HN 84)

Ricapar's [ClawDOS](http://ricapar.net/ClawDOS/) runs an AI coding agent natively on DOS on a real 8088 at 4.77 MHz, 640 KB RAM, CGA. Key design facts:

- `HARNESS.EXE` is a 176 KB DOS program that speaks the Claude Messages API itself — writes requests, parses streamed replies, runs tools, keeps conversations on disk. "The 8088 does everything but TLS."
- A "bridge" PC (`tunnel/tunnel.py`, socat/stunnel) terminates TLS — an 8088 cannot do it — and can hold the API key so it never touches the PC's disk.
- 18 tools including `peek`/`poke`/`port` (memory and I/O), a `run` tool that hands the machine to Turbo C with ~450K free, timer-interrupt CGA screenshots that the 8088 encodes as PNG and sends to Claude with the tool result, and on-disk memories/skills in `C:\MEMORY` listed in the system prompt.
- Agent-built demos: `PRIMES.C` written, compiled and run 64 s after one prompt (26 s of it compiling); a WarGames tribute (5 files Turbo C, 15 KB source, <10 KB EXE) with CGA vector map and PC-speaker music.
- Repo is 100% Claude-written except the author's backstory box; the author's test question was "can that something it built then build other somethings?"
- Safe mode on by default: every file/memory/port write asks `Allow ...? (y/n)`.

## Vibecoding an inference chip (Nov 20, 2026, HN 152)

Ankit Goyal vibe-coded an AWS F2 FPGA into running an LLM: a DeepGrove ternary-weight model on 16 GB FPGA HBM. Numbers:

- Cloud agent (Conductor) ran for days, ~3M lines of experiment history, parsed 30M lines of output, ~$10,000 in Claude/OpenAI tokens, hundreds of experiments. Mostly C++ and Verilog — the author had written neither in a decade / ever.
- Optimization trajectory: 6 → 213 tok/s, **33x** the bit-exact baseline (burst attention, parallel MoE router with exact GCC-sort tie-breaker, head loader dual-bank read +17.3%, clock stepping to 225/425 MHz after a soak test found faults at 231.25).
- Router precision is a real constraint: kept in FP32 because lower precision changed expert selection.
- Verification ladder kept publication-grade: per-block cocotb unit tests → one layer co-simulated against the real checkpoint → multi-token 24-layer decode compared token-for-token with a reference oracle; sim results, timing signoff, and board results never claimed from one another.
- Prompting was mostly encouragement ("you're a superintelligent model, time to be more creative"); process advice (e.g. a pasted 4,741-char external writeup) sorted into 10 adopt / 5 reject ideas within 70 s but moved the speed line less than autonomous exploration did. Astra and Opus 5 were interchangeable for this work.

## Claude vs. neglected open-source bugs on a 9-year-old tablet (Nov 1, 2026)

Jayd Milne used Claude to bring modern Linux up on a Galaxy Tab S3: in a single one-hour exchange Claude backported an unmerged WIP GPU patch from LKML, fixed a freedreno driver bug existing since 2018, found two Kwin bugs and an Alpine file-capabilities packaging bug, and prepared forks + MR descriptions. His thesis: even accepting the "stochastic averages" framing, most code mostly works, so average-quality generation compounds against a huge backlog of neglected OSS bugs. See [[entities/jayden-milne]].

## Assessment

Confidence is high on the observed artifacts (screenshots, benchmark tables, MRs are published) and medium on the economics claims (the $10K/3M-line figures are self-reported single-run numbers with no independent reproduction). The cluster's value is not novelty per stunts — retro-agent demos recur yearly — but the convergence: three independent authors, three unrelated hardware domains, one workflow (agent explores, human pins correctness), each reporting the agent cleared a domain-skill wall the author did not have.

## Related

- [[concepts/ai-engineering-dekilling]] — the counter-argument: cross-domain agent fluency may also erode the very comprehension needed to define correctness contracts
- [[concepts/agent-skills]] — ClawDOS memories/skills and the design-agent briefs are the same plain-text-context pattern
- [[concepts/openai-jalapeno-inference-chip]] — model-assisted chip design at the frontier end; ankitg is the hobbyist mirror
- [[concepts/modest-success-software-boom]] — Milne's compounding-against-backlog thesis
- [[concepts/vibe-coding]] — origin term; ankitg is the hardware-domain extension
