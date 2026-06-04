# LongCoT RLM Tips Structure (Alex Zhang, April 2026)

Extracted from `alexzhang13/longcot-mini-rlm-results` trajectories/math/results.jsonl.
Blog post: https://alexzhang13.github.io/blog/2026/longcot-rlm/

## Three Layers of the `<env_tips>` Section

### Layer 1: Graph Dependency Directive Catalog
An exhaustive list of ALL verbatim directive types that LongCoT problems use to pass values between nodes:

- "use the answer from node_X and subtract K"
- "use the numerator / denominator of the reduced form of the fraction from node_Y"
- "use the integer answer from node_Z" (the rational/integer summand, NOT floor of radical)
- "use the largest / smallest integer from the answer list of node_W"
- "the coefficient of sqrt(k) from node_V"
- "the exponent of p in the m-th pair / factor of node_U"
- "the x-coordinate / y-coordinate of the n-th ordered pair in the answer of node_T"
- "the integer part of the answer from node_S" (floor — different from 'integer term')
- "the base of the power from node_R" (k in k^e)
- "[If node_K == V, then A, otherwise B]" (conditional)
- "a number such that <constraint involving later nodes>" (cyclic — seed-and-search)

### Layer 2: Two-Pass Workflow

**Pass 1 — Map & Solve:**
1. Record graph as Python data in turn 1 (do NOT solve yet):
   ```python
   nodes = {"node_0": {"q": "<verbatim>", "deps": [], "refs": []}, ...}
   final_order = ["node_14", "node_3", "node_0", "node_11"]
   answers = {}
   ```
2. Scan for cycles (forward refs). Cycles always have a numeric constraint.
3. Solve node by node in topological order. Print EVERY variable before using it.
4. NEVER inline parent values from memory — always round-trip through `answers[...]`.

**Pass 2 — Independent Re-derivation (MANDATORY before storing final answer):**
Run a SEPARATE REPL cell for each node using a different method:
- Closed-form primary → brute-force verify
- Brute-force primary → closed-form verify
- sympy solve → substitute back
- Combinatorial identity → generating-function reformulation

Print both values and MATCH/DIFFER marker. Only store after agreement.

### Layer 3: General Principles (Anti-Brute-Force)

- **Time budget**: Each REPL cell < 60s wall clock. Cap loops/itertools at 10M operations.
- **No float for exact answers**: `sp.Rational`, `Fraction`, sympy expressions only.
- **No exponential blowup**: Avoid `a**b` when either side is large; use `sp.log` space.
- **Memoize bounded**: `lru_cache(maxsize=10**6)`. Bail on unbounded state space.
- **Seed-and-search for cycles**: Enumerate 1..40 candidates, solve downstream for each.
- **Double-derive everything**: A single-method computation is a guess.
- **No memorized answers**: Even for recognized IMO/Putnam problems, re-derive.
- **Elegance check**: Competition answers are small integers, simple fractions, or clean closed forms. Ugly output = upstream misreading.
- **Best-effort ship**: A blank answer.txt scores 0. Ship your best values even if uncertain.

## Key Insight for Harness Engineering

The tips exploit the RLM's REPL environment specifically — the Two-Pass workflow, symbolic computation, and double-derivation instructions only work because the model has a persistent Python REPL. Giving the same tips to a non-RLM LM (without REPL) degrades performance, proving that RLM's recursive decomposition is essential.
