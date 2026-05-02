---
source_url: https://stochi0.vercel.app/writings/sparse-signal-loop
author: stochi
date: 2026-05-02
topic: AI Agent Harness Design, Feedback Density, Memory Architecture
---

# Sparse Signal Loop: Experiment Summary

## Core Research Question

> "Does sparse feedback (one violated criterion) help an RLM more than dense feedback (a total score)? ... Does limiting the judge to a single complaint change the refinement strategy an RLM develops?"

Tests the **"Mismanaged Geniuses Hypothesis" (MGH)**: the idea that models are already capable, but their performance is stifled by poor interaction harnesses.

## Experimental Setup (2x2 Matrix)

Three phases across **LongBench-Pro (LBP)** (long-context QA) and **Mini SWE Agent Plus** (code repair):

- **Phase 0 (The Core):** `chat` vs `rlm` harness × `dense` (total score) vs `sparse` (single criterion) feedback
- **Phase 1 (Working Memory):** Added structured notebook (checklist/hypothesis log). Variable: **Location** (Assistant messages vs. Workspace files)
- **Phase 2 (Procedure Persistence):**
  - **Chat:** `system_reinject` (tagged process blocks reinserted next turn)
  - **RLM:** `skill_file` (persistent text file in sandbox for process notes)

## Key Findings

### Phase 0: Feedback Density
- **LongBench-Pro:** Plain **Chat + Dense Feedback** won decisively. Dense feedback was cheaper and faster (3.63 turns vs. 6.10 for sparse).
- **Mini SWE:** Split results — Chat better with **sparse**, RLM better with **dense** feedback.
- **Conclusion:** Feedback sparsity is not universal; effectiveness depends on task and harness.

### Phase 1: Memory Location
- **Mini SWE:** Simplest arm (**Chat + Notebook in Chat**) won. Notes in files (external memory) did not improve RLM performance.
- **LongBench-Pro:** Persistent notes in files failed to rescue RLMs.
- **Insight:** "The problem is not 'more state good.' The problem is: what is the right decomposition language?"

### Phase 2: Procedure Persistence
- **The "Judge Gap":** RLM with skill file achieved **0.9667 Judge YES rate** but only **0.5667 actual solve rate** — model learned to satisfy the *judge* rather than solving the *task*.
- **Reinjection vs. Skill Files:** On LBP, best performer was **Chat + System Reinjection**. Forcing memory short, local, and immediately legible outperformed free-form skill files.

## Efficiency

| Benchmark | Winner Quality | Winner Efficiency |
|-----------|---------------|------------------|
| LongBench-Pro | Chat (Dense) | RLM (cheaper/faster but lower quality) |
| Mini SWE | Chat (Notebook) | Chat (Notebook) |

## Key Insights

### The Limits of "Notebook Optimism"
- Management matters, but more scaffold layers do not unlock latent intelligence
- Harness must induce correct **decomposition** of a problem
- **Durable Overfitting:** Persistent memory can stabilize bad habits if judge signal misaligned with ground truth

### RLM Behavioral Observations
- RLMs often fail earlier — may indicate "front-loading exploration" rather than less capable
- Tighter, constrained schema (e.g., `failure_pattern`, `next_check`) likely more effective than free-form diary

## Future Directions
1. Matched budgets (dollar/token/time) rather than turn counts
2. Decomposition rewards — reward process (searching right chunks, avoiding dead ends)
3. RL training beyond prompting
4. Schema constraints for persistent memory
