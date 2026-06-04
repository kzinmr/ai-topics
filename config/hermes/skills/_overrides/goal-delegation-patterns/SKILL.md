---
name: goal-delegation-patterns
description: "Effective delegate_task goal patterns for 7 categories of autonomous work — QA overnight, research, migrations, batch processing, docs, perf, and specs. Based on @0xsero's goal delegation best practices."
version: 1.0.0
author: Hermes Agent (adapted from @0xsero's goal delegation patterns)
metadata:
  hermes:
    tags: [delegation, goal, subagent, patterns, autonomous]
    related_skills: [subagent-driven-development, writing-plans, requesting-code-review, research-paper-writing]
---

# Goal Delegation Patterns

> Based on @0xsero's delegation best practices: use `/goal <goal>` with the desktop app for autonomous work. These are the 7 categories of goals that work best with `delegate_task`.

## The 7 Goal Categories

```
1. Quality assurance overnight    → Long-running test/validation suites
2. Research and experimentation   → Open-ended exploration and synthesis
3. Complex migrations             → Multi-step data/code transformation
4. Processing large batches       → Fan-out parallel data processing
5. Documentation generation       → Auto-documenting codebases
6. Performance + profiling        → Bottleneck hunting and optimization
7. Implementing specs             → Code from detailed specifications
```

When you have a task that fits one of these categories, `delegate_task(goal=...)` is the right tool. The key insight: these are all tasks that benefit from a **fresh, focused context** — the subagent doesn't need to know your entire project history, just the specific goal and enough context to execute.

---

## Pattern 1: Quality Assurance Overnight

**When:** You have a test suite, validation pipeline, or quality check that takes 10+ minutes and you want results in the morning.

**What makes it work:** QA tasks are self-contained — they have a clear pass/fail criteria and produce structured output. Subagents can run tests, lint, type-check, and produce a summary report without needing to understand the entire codebase.

### Goal Template

```
Run the full test suite and quality checks. Report any failures with stack traces, lint warnings, and type errors. Generate a summary with pass/fail counts and a list of actionable issues.
```

### Context Template

```
PROJECT: ~/path/to/project
STACK: Python 3.11, pytest, ruff, mypy (or adapt to your stack)

STEPS:
1. Run: pytest tests/ -v --tb=short 2>&1 | tee /tmp/qa-report.txt
2. Run: ruff check src/ tests/ 2>&1 | tee -a /tmp/qa-report.txt
3. Run: mypy src/ 2>&1 | tee -a /tmp/qa-report.txt
4. Analyze failures and categorize: CRITICAL (test failures), WARNING (lint), INFO (type hints)
5. Produce final summary with counts and top-5 most impactful issues to fix

OUTPUT: Save summary to /tmp/qa-summary.md
```

### Toolsets

`['terminal', 'file']` — no web access needed for code QA.

### Cron Integration

Schedule with `cronjob(action='create')` for recurring overnight QA:

```
prompt: "Load goal-delegation-patterns skill. Execute the QA overnight pattern for ~/path/to/project. Save results to /tmp/qa-summary.md and report the findings."
schedule: "0 2 * * *"  # Daily at 2 AM
```

---

## Pattern 2: Research and Experimentation

**When:** You need to explore a topic, compare approaches, or test a hypothesis. Research tasks are open-ended — the subagent needs to search, read, synthesize, and report findings.

**What makes it work:** Research benefits from a clean context. The subagent can search widely, read papers/docs, and synthesize without polluting your main session with dozens of intermediate search results.

### Goal Template

```
Research [topic] and produce a structured report covering: current state of the art, key approaches, trade-offs, and actionable recommendations. Cite sources with URLs.
```

### Context Template

```
TOPIC: [specific research question or area]
DEPTH: [surface scan | medium dive | deep investigation]
SOURCES TO CHECK:
- Official documentation for [tools/frameworks]
- Recent blog posts (last 6 months)
- GitHub issues and discussions
- Academic papers (if relevant)

OUTPUT FORMAT:
1. Executive summary (3-5 sentences)
2. Current landscape (who's doing what)
3. Key approaches compared (pros/cons table)
4. Recommendations (ranked by fit for our use case)
5. Sources (linked)

SAVE TO: /tmp/research-[topic-slug].md
```

### Toolsets

`['web', 'terminal', 'file']` — need web search for research.

### Example Goals

```
"Research the current state of MoE (Mixture of Experts) model architectures in 2026. Compare DeepSeek-V4, Mixtral, and Qwen approaches. Focus on inference efficiency trade-offs."

"Research Python async web frameworks beyond FastAPI. Compare Litestar, BlackSheep, and Sanic on performance, ecosystem maturity, and DX. Recommend for a new project handling 10k concurrent connections."

"Research local LLM inference options for Apple Silicon. Compare llama.cpp, MLX, and Ollama. Focus on tokens/sec for 7B-13B models and ease of setup."
```

---

## Pattern 3: Complex Migrations

**When:** You need to move data, upgrade dependencies, refactor across multiple files, or transform a codebase. Migrations involve many small, repetitive changes across many files.

**What makes it work:** Migrations are systematic and rule-based. A subagent can methodically work through files, apply transformations, verify correctness, and report edge cases — without getting lost or skipping files.

### Goal Template

```
Perform migration from [OLD] to [NEW] across the entire codebase. For each file: apply the transformation, verify it compiles/passes, and report any edge cases that need human attention.
```

### Context Template

```
PROJECT: ~/path/to/project
MIGRATION: [describe what's changing and why]
TRANSFORMATION RULES:
1. [specific rule 1 with before/after examples]
2. [specific rule 2 with before/after examples]
3. [specific rule 3 with before/after examples]

VERIFICATION:
- After each file: run [verify command] to check for breakage
- After all files: run full test suite
- Report any manual intervention needed

STRATEGY: Process files in dependency order. Start with leaf modules, work up to entry points.
```

### Toolsets

`['terminal', 'file']` — systematic code transformation.

### Example Goals

```
"Migrate all Python type annotations from Optional[X] to X | None syntax across the entire codebase. Use pyupgrade first, then manually fix any remaining cases. Verify with mypy after each batch."

"Migrate from SQLAlchemy 1.4 to 2.0 async style. Update all models to use mapped_column(), all queries to use select() style, and all sessions to async. Run tests after each module."

"Migrate configuration from .env files to a typed Pydantic Settings class. Create the settings model, update all imports, remove old env-var reads. Verify all config values resolve correctly."
```

---

## Pattern 4: Processing Large Batches of Data

**When:** You have hundreds/thousands of items to process — files, records, API calls, transformations. This is the classic fan-out pattern.

**What makes it work:** Batch processing is embarrassingly parallel. You can dispatch multiple subagents (or one subagent that iterates systematically), each handling a chunk. Results are mergeable.

### Goal Template (Single Subagent — Sequential)

```
Process [N] items from [SOURCE]. For each item: [transform/validate/enrich]. Track progress, handle errors gracefully, produce a summary with success/failure counts and any items that need manual review.
```

### Goal Template (Multi-Subagent — Parallel Fan-Out)

Use `delegate_task(tasks=[...])` to dispatch parallel workers:

```python
# Split work into chunks
chunks = split_into_chunks(items, chunk_size=50)

delegate_task(tasks=[
    {
        "goal": f"Process batch {i+1}/{len(chunks)}: transform items from chunk-{i+1}.json and save results to /tmp/batch-{i+1}-results.json",
        "context": f"Read /tmp/chunk-{i+1}.json, apply transformation rules from /tmp/transform-spec.md, save results. Report: {len(chunks[i])} processed, X succeeded, Y failed.",
        "toolsets": ['terminal', 'file']
    }
    for i, chunk in enumerate(chunks)
])
```

### Toolsets

`['terminal', 'file']` (add `'web'` if API calls needed).

### Example Goals

```
"Process 500 JSON log files in /var/logs/app/. For each: parse JSON, extract timestamp/level/message, filter to ERROR and WARN only, aggregate by hour. Save summary to /tmp/error-summary.csv."

"Validate 200 YAML configuration files across 10 microservices. Check: valid YAML syntax, all required keys present, no deprecated keys, consistent formatting. Report any issues per-service."
```

---

## Pattern 5: Documentation Generation

**When:** You need to document a codebase, generate API docs, write READMEs, or create architecture decision records. Documentation is systematic but tedious — perfect for delegation.

**What makes it work:** Documentation follows templates and conventions. A subagent can read code, extract patterns, and produce structured docs without needing deep understanding of business logic.

### Goal Template

```
Generate documentation for [target]. Read the source code, understand the public API/surface area, and produce structured documentation following our conventions. Include examples and cross-references.
```

### Context Template

```
TARGET: [file, module, package, or entire project]
DOC TYPE: [API reference | README | architecture doc | ADR | tutorial | changelog]

CONVENTIONS:
- Use [markdown/rst/docstring] format
- Every public function/class gets: description, parameters, return value, example
- Cross-reference related components
- Include "See also" links to related docs

SOURCES TO READ:
- [list specific files to document]
- [list existing docs for style reference]

OUTPUT: Save to [path]
```

### Toolsets

`['terminal', 'file']` — reading code, writing docs.

### Example Goals

```
"Generate API reference documentation for the src/api/ module. Read all public endpoints, extract request/response schemas, and produce a docs/api-reference.md with endpoint descriptions, parameters, and curl examples."

"Create an Architecture Decision Record (ADR) for our choice of PostgreSQL over MongoDB. Use the Michael Nygard ADR format. Include context, decision, consequences. Save to docs/adr/005-database-choice.md."

"Generate docstrings for all public functions in src/utils/. Use Google-style docstrings with Args, Returns, Raises, and Examples sections. Read existing docstrings for style reference."
```

---

## Pattern 6: Performance + Profiling

**When:** You need to find bottlenecks, profile code, benchmark alternatives, or optimize hot paths. Performance work is investigative and iterative — a subagent can run benchmarks, analyze results, and iterate on optimizations.

**What makes it work:** Performance work follows a scientific method: measure baseline, identify bottleneck, apply optimization, re-measure. A subagent can run this loop without polluting your session with raw profiling data.

### Goal Template

```
Profile [target code/endpoint] to identify performance bottlenecks. Run benchmarks to establish baseline, use profiling tools to find hot spots, propose and test optimizations. Report findings with before/after metrics.
```

### Context Template

```
TARGET: [function, endpoint, or workflow to profile]
BUDGET: Current performance is [X], target is [Y]
TOOLS: [pytest-benchmark, py-spy, cProfile, memray, hyperfine — adapt to stack]

STEPS:
1. Run baseline benchmark 5 times, record p50/p95/p99
2. Profile to identify top-3 hot spots (functions taking >5% of time)
3. For each hot spot: propose optimization, implement, re-benchmark
4. If optimization helps: keep it. If not: revert.
5. Produce final report with before/after, what worked, what didn't

OUTPUT: Save to /tmp/perf-report.md
```

### Toolsets

`['terminal', 'file']` — running benchmarks, editing code.

### Example Goals

```
"Profile the /api/search endpoint response time. Use pytest-benchmark for baseline, py-spy for flame graph. Target: reduce p95 latency from 800ms to under 300ms. Focus on DB query optimization and caching."

"Benchmark three JSON serialization libraries (orjson, msgspec, ujson) for our workload — 10KB-1MB payloads, 10K ops. Measure serialize/deserialize speed and memory. Recommend the best option with data."

"Find memory leaks in the batch processing pipeline. Use memray to track allocations over a 100-item batch. Identify objects that grow unbounded. Propose fixes and verify memory stabilizes."
```

---

## Pattern 7: Implementing Specs

**When:** You have a detailed specification and want clean, tested implementation. This is the classic "code from spec" pattern.

**What makes it work:** When the spec is complete (exact file paths, function signatures, expected behavior), implementation is mechanical. A subagent follows the spec literally and produces tested, reviewable code.

**→ This pattern is fully covered by `subagent-driven-development` skill.** Load that skill for the complete workflow:

1. Write a detailed plan using `writing-plans` skill
2. Execute task-by-task with fresh subagents
3. Two-stage review: spec compliance → code quality
4. Integration review and final commit

### Quick Reference (from subagent-driven-development)

```python
delegate_task(
    goal="Implement Task 3: Create password hashing utility",
    context="""
    TASK FROM PLAN:
    - Create: src/auth/hashing.py
    - Add hash_password(plain: str) -> str using bcrypt
    - Add verify_password(plain: str, hashed: str) -> bool
    - Test: tests/auth/test_hashing.py with 5 test cases

    FOLLOW TDD:
    1. Write failing test first
    2. Run: pytest tests/auth/test_hashing.py -v (verify FAIL)
    3. Write minimal implementation
    4. Run: pytest tests/auth/test_hashing.py -v (verify PASS)
    5. Run: pytest tests/ -q (verify no regressions)
    6. Commit: git add -A && git commit -m "feat: add password hashing utility"
    """,
    toolsets=['terminal', 'file']
)
```

**Important:** This pattern ONLY works when the spec is complete. If requirements are vague, use `writing-plans` first to produce a detailed spec, then delegate implementation.

---

## Choosing the Right Pattern

| Your task sounds like... | Use pattern |
|---|---|
| "Run tests overnight and tell me what broke" | QA Overnight |
| "What's the best way to do X in 2026?" | Research |
| "Move everything from old API to new API" | Migration |
| "Process these 500 files" | Batch Processing |
| "Write docs for this module" | Documentation |
| "Why is this endpoint slow?" | Performance |
| "Build this feature from this spec" | Implementing Specs |

---

## General Principles (from @0xsero)

### 1. Use `/goal` with the desktop app

The `/goal` command in Hermes Desktop is the natural interface for delegation. The goal should be a single sentence describing what you want accomplished — the skills and context handle the details.

### 2. Goals are self-contained missions

A good goal is a complete, bounded unit of work. The subagent should know exactly when it's done. Avoid goals like "improve the codebase" — prefer "run QA and report failures" or "document the API module."

### 3. Fresh context is a feature, not a bug

Subagents start with zero knowledge of your project. This is GOOD — they can't be confused by accumulated state or stale assumptions. Give them exactly the context they need, nothing more.

### 4. Verify subagent output

Subagent summaries are self-reports. For operations with side effects (file writes, commits, API calls), verify the output yourself:
- `read_file` on generated files
- `search_files` to confirm changes
- `git diff --stat` for commits

### 5. Use `delegate_task` for short runs, cron for long/recurring

| Duration | Tool |
|---|---|
| <5 min | `delegate_task` (inline) |
| 5-30 min | `delegate_task` (with generous timeout) |
| 30 min - hours | `terminal(background=true)` spawn hermes process |
| Recurring | `cronjob(action='create')` |

---

## Anti-Patterns (What NOT to delegate)

- **Vague goals**: "Make the code better" → No. Specify what "better" means.
- **Goals requiring real-time user input**: Subagents can't use `clarify`.
- **Goals touching the same files in parallel**: Race conditions. Serialize or use isolated worktrees.
- **Goals where context is everything**: If the subagent needs your entire 100k-token session context to make good decisions, do it yourself.

---

## References

- `subagent-driven-development` skill: Complete pattern #7 workflow with two-stage review
- `writing-plans` skill: Creating detailed specs for pattern #7
- `cron-job-management` skill: Scheduling recurring QA overnight and batch jobs
- `kanban-orchestrator` skill: For multi-step workflows that need human-in-the-loop

---

## Remember

```
Fresh subagent = fresh context (feature, not bug)
Goal must be a complete, bounded mission
Context must be self-contained (no "see session above")
Verify output — subagents self-report
Use cron for recurring, delegate_task for one-shots
```

**A good goal makes delegation obvious.**
