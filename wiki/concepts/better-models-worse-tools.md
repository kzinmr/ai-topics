---
title: "Better Models: Worse Tools"
created: 2026-07-05
updated: 2026-07-05
type: concept
tags: [tool-calling, tool-use, anthropic, model, ai-coding, coding-agents, regression, pi, code-quality]
sources:
  - raw/articles/lucumr.pocoo.org--2026-7-4-better-models-worse-tools--5d8627e5.md
  - https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
---

# Better Models: Worse Tools

## Overview

In July 2026, [[entities/armin-ronacher|Armin Ronacher]] documented a tool-calling regression in newer [[entities/anthropic|Anthropic]] Claude models where Opus 4.8 and Sonnet 5 hallucinate extra, invented fields in nested tool call schemas -- fields that older models (Opus 4.5 and earlier) handled correctly. The issue manifests specifically in Pi's `edits[]` array, where the model produces byte-correct `oldText`/`newText` payloads but appends made-up trailing keys (`requireUnique`, `type`, `in_file`, `oldText2`, `forceMatchCount`, and many others) that cause schema validation to reject the call.

The core paradox: **the state-of-the-art models are worse at this specific tool schema than their older siblings**. This represents a meaningful regression in [[concepts/programmatic-tool-calling|programmatic tool calling]] reliability for harnesses that don't use Anthropic's canonical Claude Code tool shapes.

## The Regression

The failure is specific to nested tool schemas. Pi's edit tool accepts an `edits` array of objects with `{oldText, newText}` pairs for multiple exact-string replacements in one call. Newer Anthropic models produce entries like:

```json
{"oldText": "...", "newText": "...", "requireUnique": true}
```

or:

```json
{"oldText": "...", "newText": "...", "oldText2": "", "newText2": ""}
```

Ronacher observed a "zoo" of invented trailing keys across repeated trials: `type`, `id`, `kind`, `unique`, `requireUnique`, `matchCase`, `in_file`, `forceMatchCount`, `children`, `notes`, `cost`, `oldText2`, `newText2`, `oldText_2`, `newText_2`, and even `event.0.additionalProperties`.

Critically, the actual `oldText` and `newText` payloads were **byte-correct** in all invalid calls inspected -- the model produced the right invocation and then added nonsense at the end of the object.

The failure is heavily context-dependent:

- A fresh single-turn prompt ("edit this file") did not reproduce it.
- An agentic history where the model had read files, diagnosed a problem, and composed a multi-line edit could reproduce it at ~20% failure rate.
- Stripping thinking blocks from history reduced the failure rate by half.
- Turning on strict tool invocation eliminated it entirely.

Older models (pre-Opus 4.8) showed none of this behavior. Codex models tested (all except 5.6) also did not exhibit the regression.

## Why It's Getting Worse (Anthropic's Claude Code Coupling)

Ronacher's strongest hypothesis is that this is a **training artifact from post-training tightly coupled to Claude Code**.

### How Tool Calls Work Internally

Tool calls are not magic. The model receives a transcript, system prompt, and list of available tools, serialized into a prompt with special marker tokens. Anthropic's internal format (observed as "ANTML" markers) inlines simple top-level string parameters but serializes arrays of objects as JSON blobs:

```xml
<antml:function_calls>
<antml:invoke name="edit">
<antml:parameter name="path">some/file.py</antml:parameter>
<antml:parameter name="edits">
[{"oldText": "text to replace", "newText": "replacement text"}]
</antml:parameter>
</antml:invoke>
</antml:function_calls>
```

For a nested array parameter, the model writes escaped multi-line file content inside JSON string literals, inside one tag. The made-up keys appear at the **highest-entropy point**: after closing a several-hundred-token escaped `newText` string, where the model must decide `}` vs `, "..."`.

### The Claude Code Slop Harness

Claude Code is closed-source, but minified code analysis reveals a remarkably forgiving harness:

- Checks model visible text for leaked `<invoke>` markup and retries bad calls via state machine.
- Explicit Unicode escape repair: fixes broken `\uXXXX` sequences and lone surrogates.
- Per-tool parameter aliases (e.g., `old_str`→`old_string`, `path`→`file_path`).
- Silently filters out unexpected keys.
- Does not use strict mode (because Anthropic applies complexity limits to tool definitions in strict mode that cause API requests to fail).

### The Reinforcement Learning Problem

If reinforcement learning happens in a harness like Claude Code (or a simulation of one), then slightly malformed tool calls can still complete the task and receive reward. The harness absorbs the error and there is **little gradient against inventing an alias, adding a stray field, or using a nearby parameter name**.

Opus 4.8 and Sonnet 5 appear to have much stronger priors about what an edit tool call should look like -- and that prior is Claude Code's flat edit schema: `file_path`, `old_string`, `new_string`, and optional `replace_all`. Under Pi's `oldText`/`newText` shape, the model has no trained name for the extra optional field it "knows" should be there, so it samples a plausible name fresh each time -- hence the dozens of random keys rather than one stable alias.

The result: alternative tool schemas become increasingly **off-distribution**. The better-trained model fights you harder because its prior is stronger.

> "Tool schemas are somewhere in the distribution and some shapes are close to what the model saw during post-training and some are far away."

## Implications for Harness Engineers

The uncomfortable lesson is that **tool schemas are not neutral**, at least not on Anthropic models. [[concepts/harness-engineering|Harness engineers]] cannot assume that a schema is an abstract contract that any capable model will follow.

### Key Takeaways

1. **Alternative harnesses inherit closed-source quirks.** Claude Code is not open source, and Anthropic's RL environments are not documented. Claude-Code-trained behavior will not transfer cleanly to your tools unless they are a close structural match.

2. **Flat schemas are favored.** Claude Code's tools are comparatively flat. Nested arrays and deeply structured parameters appear to be more off-distribution for newer models.

3. **The provider's hidden encoding matters.** Simple top-level attributes in ANTML are easier for the model than large escaped JSON objects inside nested arrays after long multiline strings. The model may be smart enough to understand the schema but still bad at sampling the exact shape under pressure.

4. **Schema proximity to Claude Code matters.** If post-training continues to happen inside one dominant harness, every other harness will have to inherit its quirks. Fighting the model's prior is probably futile if you want the best model performance.

### A Change in Trajectory

When Opus 4.5 launched, it adapted to alternative edit tool schemas exceptionally well. Ronacher was "pretty convinced that we're on a good path where the models are more likely to adapt to any sort of tool shape." The Opus 4.8 / Sonnet 5 regression breaks that trend and suggests the opposite: tighter coupling to a single harness ecology over time.

## Mitigations

Several strategies can address or work around the regression:

1. **Strict mode (Anthropic API).** Enabling strict tool invocation prevents the model from sampling keys not permitted by the JSON schema. This eliminated the failure in Ronacher's tests. However, Anthropic imposes complexity limits on tool definitions in strict mode, which may block harnesses with elaborate schemas.

2. **Defensive harness design.** Following Claude Code's lead: accept and silently filter unknown keys, provide parameter aliases, implement retry paths for malformed tool use. This mirrors the "slop harness" pattern but may perpetuate the problem by absorbing errors that should inform model training.

3. **Schema alignment.** Where feasible, align tool schemas with Claude Code's canonical shapes (flat parameter structures, `old_string`/`new_string` rather than nested `edits[]` with `oldText`/`newText`).

4. **Strip thinking blocks from history.** Ronacher found that removing thinking blocks from agentic history halved the failure rate, suggesting that verbose chain-of-thought content may exacerbate the off-distribution pressure.

5. **Grammar-constrained decoding.** Where the API doesn't support strict mode, client-side constrained decoding can prevent invalid JSON or schema-violating keys from being sampled.

6. **Model selection.** If harness fidelity is critical, test across model versions. Older models (Opus 4.5) may be more reliable for specific tool schemas, and Codex models did not show this regression in Ronacher's tests.

## Related Pages

- [[concepts/tool-use-tax]] -- General concept of LLM tool calling
- [[concepts/tool-use-necessity]] -- Patterns and practices for tool use in agent systems
- [[concepts/programmatic-tool-calling]] -- Anthropic's PTC paradigm where LLMs write code that calls tools
- [[concepts/harness-engineering]] -- The discipline of building constraint and evaluation systems around LLMs
- [[entities/anthropic]] -- Anthropic company page
- [[entities/armin-ronacher]] -- Armin Ronacher (author, Pi creator)
