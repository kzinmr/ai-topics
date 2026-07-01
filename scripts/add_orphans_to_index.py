#!/usr/bin/env python3
"""
Add 20 orphan concept pages to index.md in alphabetical order.
"""
import os, re, sys

wiki = '/opt/data/ai-topics/wiki'
index_path = os.path.join(wiki, 'index.md')

with open(index_path) as f:
    lines = f.readlines()
lines = [l.rstrip('\n') for l in lines]

# Entries to add: (slug, display_line)
# Description is extracted from the page's title + first meaningful line
entries_to_add = [
    ('concepts/agent-harnesses', '- [[concepts/agent-harnesses]] — Agent Harnesses — Design patterns and runtime infrastructure for building reliable, long-running AI agents'),
    ('concepts/agentic-rag', '- [[concepts/agentic-rag]] — Agentic RAG — Retrieval-augmented generation with autonomous agent-driven search and synthesis'),
    ('concepts/ai-alignment', '- [[concepts/ai-alignment]] — AI Alignment — Ensuring AI systems act in accordance with human values and intentions'),
    ('concepts/chain-of-thought', '- [[concepts/chain-of-thought]] — Chain-of-Thought Reasoning — Step-by-step reasoning technique that improves LLM performance on complex tasks'),
    ('concepts/continual-learning', '- [[concepts/continual-learning]] — Continual Learning — Continuous improvement in AI systems via on-policy distillation, RLVR, and dreaming'),
    ('concepts/cpu-inference-llm', '- [[concepts/cpu-inference-llm]] — CPU Inference for LLMs — Running LLMs on consumer/edge CPUs via quantization (llama.cpp, Ollama)'),
    ('concepts/deep-research', '- [[concepts/deep-research]] — Deep Research — Autonomous multi-step research agents that synthesize findings from web search and document analysis'),
    ('concepts/durable-execution', '- [[concepts/durable-execution]] — Durable Execution — Fault-tolerant, stateful execution model for long-running agent workflows'),
    ('concepts/edge-ai', '- [[concepts/edge-ai]] — Edge AI — On-device AI inference via NPU accelerators; Apple Intelligence, Gemini Nano, llama.cpp'),
    ('concepts/inference', '- [[concepts/inference]] — Inference — LLM inference engine comparison; vLLM, SGLang, TGI, llama.cpp, and their trade-offs'),
    ('concepts/kv-cache', '- [[concepts/kv-cache]] — KV Cache — Key-Value caching in Transformer inference; eliminates redundant recomputation during autoregressive generation'),
    ('concepts/llm-security', '- [[concepts/llm-security]] — LLM Security — Security vulnerabilities in LLM applications including prompt injection, data leakage, and jailbreaking'),
    ('concepts/model-context-protocol-mcp', '- [[concepts/model-context-protocol-mcp]] — Model Context Protocol (MCP) — Open protocol for connecting LLMs to external tools, data sources, and services'),
    ('concepts/open-source-ai', '- [[concepts/open-source-ai]] — Open-Source AI Strategy — Strategic use of open-source AI for rapid iteration and global adoption; 3-category open model makers framework'),
    ('concepts/prompt-caching', '- [[concepts/prompt-caching]] — Prompt Caching — Paged attention and API-level caching strategies for reducing LLM inference costs'),
    ('concepts/rag-systems', '- [[concepts/rag-systems]] — RAG Systems — Retrieval-Augmented Generation architectures, from naive RAG to advanced agentic retrieval patterns'),
    ('concepts/sandbox', '- [[concepts/sandbox]] — Sandbox (Agent Sandboxing) — Isolated execution environments for running untrusted AI agent code in production'),
    ('concepts/scaling-laws', '- [[concepts/scaling-laws]] — Scaling Laws — Empirical power-law relationships for loss vs model size, data, and compute'),
    ('concepts/speculative-decoding', '- [[concepts/speculative-decoding]] — Speculative Decoding — Accelerating LLM inference by using draft models to predict multiple tokens per forward pass'),
    ('concepts/test-time-scaling', '- [[concepts/test-time-scaling]] — Test-Time Scaling — Techniques for improving LLM output quality by allocating more compute at inference time'),
]

# Find the Concepts section boundaries
concept_start = None
concept_end = None
for i, line in enumerate(lines):
    if line.startswith('## Concepts'):
        concept_start = i + 1
    elif concept_start and line.startswith('## '):
        concept_end = i
        break

if concept_start is None or concept_end is None:
    print("ERROR: Could not find Concepts section")
    sys.exit(1)

print(f"Concepts section: lines {concept_start} to {concept_end-1}")

# Extract existing concept slugs from the section
concept_section = lines[concept_start:concept_end]
existing_slugs = set()
for line in concept_section:
    m = re.search(r'\[\[concepts/([^\]|]+)', line)
    if m:
        existing_slugs.add(m.group(1))

# Filter out already-indexed entries
to_insert = [(slug, entry) for slug, entry in entries_to_add if slug.split('/')[1] not in existing_slugs]
print(f"Already indexed: {len(entries_to_add) - len(to_insert)}")
print(f"New entries to add: {len(to_insert)}")

# Find alphabetical insertion points
def find_insertion_idx(section_lines, new_slug, extract_pattern=r'\[\[concepts/([^\]|]+)\]\]'):
    """Find the index where new_slug should be inserted in the section."""
    for i, line in enumerate(section_lines):
        m = re.search(extract_pattern, line)
        if m:
            existing = m.group(1)
            if new_slug.lower() < existing.lower():
                return i
    return len(section_lines)

# Sort entries alphabetically by slug
to_insert.sort(key=lambda x: x[0])

# Build the ordered insertion list with indices
actions = []
for slug, entry in to_insert:
    bare_slug = slug.split('/')[1]
    idx = find_insertion_idx(concept_section, bare_slug)
    actions.append((idx, slug, entry))

# Sort bottom-up to preserve line numbers
actions.sort(key=lambda x: x[0], reverse=True)

# Insert
for idx, slug, entry in actions:
    concept_section.insert(idx, entry)

# Reconstruct the full file
new_lines = lines[:concept_start] + concept_section + lines[concept_end:]

# Update header counts
concept_count = len([l for l in concept_section if l.startswith('- [[concepts/')])
for i, line in enumerate(new_lines):
    m = re.match(r'^## Concepts \((\d+) pages\)', line)
    if m:
        new_lines[i] = f'## Concepts ({concept_count} pages)'
        break

# Update total pages
total_indexed = sum(1 for l in new_lines if l.startswith('- [['))
for i, line in enumerate(new_lines):
    if 'Total pages:' in line:
        m = re.search(r'Total pages: (\d+)', line)
        if m:
            new_lines[i] = line.replace(f'Total pages: {m.group(1)}', f'Total pages: {total_indexed}')
        m2 = re.search(r'Indexed entries: (\d+)', line)
        if m2:
            new_lines[i] = new_lines[i].replace(f'Indexed entries: {m2.group(1)}', f'Indexed entries: {total_indexed}')
        break

with open(index_path, 'w') as f:
    f.write('\n'.join(new_lines) + '\n')

print(f"Done. Added {len(to_insert)} orphan pages to index.md")
print(f"New concept section count: {concept_count}")
print(f"Total indexed entries: {total_indexed}")
