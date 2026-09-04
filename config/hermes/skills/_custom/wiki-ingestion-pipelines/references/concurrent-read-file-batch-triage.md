# Concurrent read_file for Batch Triage

## Pattern

When triaging 15-20+ raw articles in a dreaming or blog triage session, reading them sequentially with `read_file` is slow. The tool supports parallel invocation — call multiple `read_file` in a single function_calls block.

## Example (3 concurrent reads)

```xml
<function_calls>
<invoke name="read_file">
<parameter name="path">~/wiki/raw/articles/article-1.md