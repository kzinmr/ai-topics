# Same Substrate, Different Problems: Analytical Template

## When to Use This Pattern

Two independently-evolved concepts share a technical substrate (e.g., both use sandboxed code execution) but solve fundamentally different problems. The user asks: *"Does Concept A incorporate Concept B? Can they be combined?"*

**Signal phrases from the user:**
- "あらためてXってYの概念を陽に取り込んでいる？"
- "関係性を吟味して解説して"
- "Does X explicitly incorporate Y's approach?"

**Symptom**: The concepts *look* similar because they share infrastructure patterns (e.g., "LLM writes code in sandbox"), but their *purpose* differs (e.g., context management vs. tool orchestration).

## Detection Criteria

Before concluding "same substrate, different problems," verify both:

### A. Shared Substrate ✓
- Both use the same execution model (e.g., code in sandbox → results filtered)
- Both involve LLM writing structured code
- Both reduce round trips / context bloat
- Both emerged around the same time

### B. Different Problem ✓
- **Search space differs**: What is the LLM exploring? (documents vs. API endpoints vs. code files)
- **Built-in tools differ**: What primitives does each provide? (llm_query vs. async tool calls)
- **Recursion exists in one but not the other**: Is sub-LLM calling a core feature or absent?
- **Security model differs**: Are there access-control mechanisms like allowed_callers?
- **Origin story differs**: What paper/doc introduced each? Do they cite each other?

## Workflow

### 1. Read Both Original Sources
Don't rely on summary pages — read the canonical sources:
- Original paper / arXiv for research concepts
- Official API docs for platform mechanisms
- First-party engineering blogs for architectural patterns
- README for open-source projects

### 2. Check for Explicit References
Search each concept's documentation for mentions of the other:
- Does RLM paper mention "programmatic tool calling" or "allowed_callers"? (usually no — it predates PTC)
- Does PTC documentation mention "recursive sub-LM queries"? (no — PTC doesn't have recursion)

### 3. Build the Comparison Table

| Dimension | Concept A | Concept B |
|-----------|-----------|-----------|
| **Problem** | What specific challenge? | What specific challenge? |
| **Search space** | What's being explored? | What's being explored? |
| **Model's behavior** | Code does what? (explore → llm_query) | Code does what? (tool_a → tool_b → print) |
| **Recursion** | Essential or absent? | Essential or absent? |
| **Security** | allowed_callers / blanket access? | allowed_callers / blanket access? |
| **Async wrapping** | Automatic or not? | Automatic or not? |
| **Tool origin** | MCP/API definition or Python Callable? | MCP/API definition or Python Callable? |

### 4. Draw the "Evolved Independently" Conclusion

The correct conclusion is rarely "A incorporates B" — it's usually one of:

| Relationship | Description | Example |
|-------------|-------------|---------|
| **Same substrate, different problems** | Share code-execution foundation, different purpose | RLM × PTC |
| **Parallel solutions** | Same problem, different mechanism | RLM × Context Folding |
| **Vertical hierarchy** | Same org, different abstraction levels | PTC → Code Exec MCP → CodeMode |
| **One implements the other** | B is a concrete implementation of A's mechanism | Monty implements PTC |

### 5. Check for "Accidental Extensibility"

The most subtle finding: A has a general parameter (e.g., `tools: list[Callable]`) that *technically accepts* B-style functions. This is **not designed integration** — it's accidental extensibility. Document the limitations:

1. No security boundary (allowed_callers absent)
2. No async auto-wrapping
3. No caller tracking
4. No context-exclusion guarantee

### 6. Write the Analysis

Structure:

```
## Concept A × Concept B: Independent Paradigms

### A does NOT explicitly incorporate B

### Problem Difference (table)

### Shared Substrate

### Accidental Extensibility (if applicable)

### Conclusion: Independent Paradigms
  A: [purpose] → how A achieves it
  B: [purpose] → how B achieves it
```

## Reference Example

See the analysis added to `dspy-rlm.md` in the 2026-05-01 session:

**RLM × Programmatic Tool Calling:**
- RLM does NOT explicitly incorporate PTC
- RLM's `llm_query` is recursive sub-LM calling, not external tool calling
- RLM's `tools` parameter is accidental extensibility, not designed integration
- 4 specific limitations of the accidental extensibility
- Both use sandboxed code execution as substrate, but:
  - RLM solves context rot (document decomposition)
  - PTC solves tool definition bloat (API orchestration)

## Extended Pattern: The 2-Axis Complementarity Model

When two concepts share a common substrate but the user's follow-up reveals they actually operate on **orthogonal axes**, the "same substrate, different problems" model is necessary but not sufficient. The concepts are not just different — they are **complementary** along independent dimensions.

### Detection

The user offers a framing like "X is tool/function-centric, Y is data/context-centric" or "X optimizes execution, Y optimizes selection." This is the signal that a 2-axis model is needed.

### Workbook

1. **Identify each concept's center**: What is the primary object the concept manipulates?
   - PTC → tools (functions): orchestrates execution of external APIs
   - RLM → data (context): explores and decomposes documents
   - RAG → data retrieval: selects chunks from a vector store

2. **Identify each concept's LLM alternative**: What is the standard approach being optimized?
   - PTC → sequential tool calling (N round trips → 1 code execution)
   - RLM → long-context prompting / RAG (all data pushed in → code selectively reads)

3. **Identify the determinism/freedom tradeoff on each axis**:
   - PTC: more deterministic execution order than tool calling (code fixes the sequence); more freedom (conditionals, parallelism)
   - RLM: more deterministic exploration strategy than RAG (code fixes the filter); more freedom (arbitrary decomposition depth)

4. **Draw the axis diagram** (ASCII):
   ```
                   ↑ RLM (データ軸: 何を分析するか)
                   │   context[start:end], llm_query()
                   │
                   │   ★ Integrated design
                   │   context探索 + await tool() + llm_query()
                   │
       ────────────┼─────────────────────────→ PTC (関数軸: どう実行するか)
                   │   await tool(), asyncio.gather()
   ```

5. **Write concrete code examples for each axis and their integration**:
   - Pure PTC: `await tool_a()`, `asyncio.gather()`
   - Pure RLM: `context[start:end]`, `llm_query()`, `SUBMIT()`
   - Integrated: `relevant = context[:100]`, `data = await api({"ids": ...})`, `analysis = llm_query(f"...")`

### Section Structure

When adding to the wiki, use this hierarchy:

```
## Concept A × Concept B: 補完する2軸（X軸 vs Y軸）

### 根本的なフレーミング
[Comparison table: center, LLM alternative, problem, determinism dimension, freedom dimension]

### 補完関係の図示
[ASCII axis diagram]

### 具体例で見る違い
[Code examples for each axis + integrated]

### なぜこのフレーミングが重要か
[Why collapsing into "common substrate" loses the point; why treating as "completely different" misses synergy]

### [Implementation analysis]
[Then the existing "does NOT explicitly incorporate" + accidental extensibility + first-principles design sections]
```

### Methodological Note: Iterative Refinement

The correct framing often emerges through **user correction**, not a single analytical pass. Expect 2-3 iterations:

| Phase | Trap | Correction | What it becomes |
|-------|------|------------|-----------------|
| 1 | Implementation-specific conclusion ("DSPy.RLM does NOT incorporate PTC") | User says "look at the original paper, not the implementation" | First-principles architectural analysis |
| 2 | Architecture analysis shows compatibility | User says "but are they really the same category?" | 2-axis complementarity framing |
| 3 | 2-axis model validated | User refines the axes (function-axis vs data-axis) | Final framing with concrete code examples |

**Key pitfall to avoid**: Don't jump to "they're the same thing" because they share infrastructure. The **problem** they solve is the defining characteristic, not the mechanism. When the user challenges a conclusion, go back to the **original source document** (paper, API spec, first-party blog) — not the implementation wrapper — to re-examine the architecture from first principles.

### Extended Analysis: Merge/Split Symmetry

When the 2-axis model is validated, check for a directionality symmetry — one concept operates in the **merge** direction (collapsing N discrete items into 1 code block) while the other operates in the **split** direction (decomposing 1 large item into N pieces).

| Direction | Characteristic | Example (PTC) | Example (RLM) |
|-----------|---------------|---------------|----------------|
| **Merge** | Bundle N things -> 1 code block | N tool calls -> 1 `asyncio.gather()` | -- |
| **Split** | Decompose 1 thing -> N pieces | -- | 1 huge context -> `re.findall()` + `llm_query()` |
| **Bottleneck** | What limits performance | Round trips (model back-and-forth) | Context size (what fits in window) |
| **Optimization** | How it speeds up | Parallel execution, native control flow | Selective loading, recursive analysis |

### Extended Analysis: Soft MapReduce

When one concept (typically RLM) operates on the data/context axis, it can be understood as a **soft MapReduce** — the LLM dynamically implements MAP (exploration/decomposition), SHUFFLE (intermediate analysis via `llm_query`), and REDUCE (aggregation via `SUBMIT`) operations through code.

**Contrast with traditional MapReduce:**

| Aspect | Traditional MapReduce | Soft MapReduce (RLM) |
|--------|---------------------|---------------------|
| **Split function** | Fixed partitioner | Code-defined (regex, slicing, semantic boundary) |
| **Map** | Same function on each shard | Flexible per-shard strategy |
| **Shuffle/Combine** | Key-based sorting | `llm_query()` -- semantic analysis |
| **Reduce** | Same aggregation function | `llm_query()` + `SUBMIT()` -- dynamic synthesis |
| **Strategy** | Pre-defined by developer | Chosen by LLM at runtime (RLM paper section 5) |

Document this analogy when the concept's code examples naturally follow the Map-Reduce pattern (explore -> extract -> aggregate).
