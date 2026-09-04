#!/usr/bin/env python3
"""Translate all Japanese text in log.md body (skip YAML frontmatter)."""
import re

with open('/opt/data/ai-topics/wiki/log.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Find YAML frontmatter boundaries (first two --- markers)
first_dashes = None
second_dashes = None
for i, line in enumerate(lines):
    if line.strip() == '---':
        if first_dashes is None:
            first_dashes = i
        elif second_dashes is None:
            second_dashes = i
            break

print(f"Frontmatter: lines {first_dashes+1} to {second_dashes+1}")

# Define translations for each line with Japanese
# Index is 0-based
translations = {
    42: '- **Source**: X Article by North (@anorth_chen) — "Why is it always difficult to land your agent projects?"',
    
    57: '- All 5 skipped: susam.net (Math Notes), danluu.com (Physics Archive), Karpathy (PhD Program Guide + AI Creative Fiction), filfre.net (Historical Mystery) — none contain AI/LLM technology content',
    
    278: '## [2026-05-29] raw-backlog-ingest | 5 items backlog processed — 0 take, 2 reference, 3 skip',
    
    280: '- **AINews Kimi K2.5 Digest** → `reference` — Includes Kimi K2.5/MoonViT/Agent Swarm/Trinity Large (Arcee/Prime Intellect 400B MoE), but Kimi-related content already covered up to K2.6 in entities/kimi.md',
    
    281: '- **SemiAnalysis GPU TCO Analysis** → `reference` — GPU cluster TCO analysis including ClusterMAX/Goodput calculator. AI infrastructure related but already processed in newsletter pipeline',
    
    282: '- **Ed Zitron "AI Is Too Expensive"** → `skip` — Already processed in 5/28 backlog',
    
    285: '- Archive: `wiki/raw/archived/triage/backlog/2026-05-29_20260529T160100Z.json`',
    
    344: '## [2026-05-29] raw-backlog-ingest | 5 items backlog processed — all skip (0 takes)',
    
    345: '- paulgraham.com "How to Start a Startup" (2005) → skip: general startup theory, not AI-related',
    
    346: '- Miguel Grinberg "SQLAlchemy 2 In Practice" → skip: database tutorial, not AI-related',
    
    347: '- Dan Luu "Some thoughts on writing" → skip: writing style essay, not AI-related',
    
    348: '- SemiAnalysis "How Much Do GPU Clusters Really Cost?" (2 items, same post_id) → skip: already covered in concepts/gpu-cluster-tco-goodput.md + entities/semianalysis.md',
    
    349: '- Archive: `wiki/raw/archived/triage/backlog/2026-05-29_20260529T080055Z.json`',
    
    350: '- Triage JSON: `.hermes/cron/data/backlog/triage_latest.json`',
    
    442: '- [[concepts/orchestration-tax]] — New concept page created: Named by Richard Seroter at Google I/O 2026 panel, expanded by Addy Osmani. "Humans as GIL (Global Interpreter Lock)" structure in AI agent development. Application of Amdahl\'s Law, Busy ≠ Productive, 5 attention design strategies (backpressure, sort work, batch reviews, spend attention only on judgment, protect serial time). Cross-referenced with [[concepts/cognitive-surrender]], [[concepts/cognitive-debt]], [[concepts/harness-engineering]].',
    
    443: '  - [[entities/addy-osmani]] — Added "The Orchestration Tax" section, updated sources/description/Related Pages',
    
    448: '- [[concepts/gpu-cluster-tco-goodput]] — New concept page created: SemiAnalysis GPU cluster TCO framework. 8 cost elements (GPU/Storage/Network/Control Plane/Support/Goodput/Setup/Debugging), comparison of 3 fault-tolerant training methods (TorchFT vs AWS Checkpointless vs TorchPass), 3 workload scenario analysis (LLM Pretrain/RL Research/Inference). Goodput Expense formula and TCO comparison by provider tier.',
    
    449: '  - [[entities/semianalysis]] — Added GPU Cluster TCO & Goodput Framework section, updated related/sources',
    
    450: '  - [[concepts/gpu-cloud-rankings]] — Updated related/sources',
    
    451: '  - 3 items skipped: Paul Graham (startup advice), Miguel Grinberg (SQLAlchemy tutorial), Dan Luu (writing philosophy) — outside AI scope',
    
    452: '  - 1 item deduped: SemiAnalysis duplicate file (different substack app-link, same post)',
    
    884: '- [[concepts/bitsandbytes.md]] — `Benchmark on T4 16GB GPU:` (was: `T4 16GB GPUでのベンチマーク:`)',
    
    887: '- [[concepts/code-execution-with-mcp.md]] — `★ this page` (was: `★ このページ`)',
    
    888: '- [[concepts/code-mode.md]] — `★ this page` (was: `★ このページ`)',
    
    928: '- concepts/skill-retrieval-augmentation.md — `Concept Cluster Map (Parent Page)` (was: `概念クラスターマップ(親ページ)`)',
    
    929: '- concepts/skill-architecture-patterns.md — `Concept Cluster Map (Parent Page)` (was: `概念クラスターマップ(親ページ)`)',
    
    930: '- concepts/agentic-ai-skills.md — `Concept Cluster Map (Parent Page)` (was: `概念クラスターマップ(親ページ)`)',
    
    933: '- concepts/memory-scaling.md — `Memory Scaling` (was: `メモリスケーリング`)',
    
    936: '- concepts/hierarchy-to-intelligence-block-organization-model-transformation.md — duplicate stub (superseded by concepts/ai-organization/ai-org-from-hierarchy-to-intelligence.md)',
    
    940: '- concepts/thin-bi.md raw article path — 7 JP chars in immutable raw/ file reference (2033336956961308721_bi-tool-becoming-thinner.md)',
    
    958: '- `concepts/proprietary-context-ai-era-governance-diamond-chart.md` (was: `concepts/proprietary-context-ai時代の組織ガバナンスとdiamond型組織図.md`) → `proprietary-context-ai-era-governance-diamond-chart.md`',
    
    959: '- `concepts/ai-benchmarks-and-community.md` (was: `concepts/aiベンチマークとコミュニティ.md`) → `ai-benchmarks-and-community.md`',
    
    994: '- concepts/ai-memory-systems-chat-vs-coding-agent-design-philosophy-comparison.md — removed 44 JP chars, title + stub text',
}

# Apply translations
for line_num, new_text in translations.items():
    lines[line_num] = new_text

new_content = '\n'.join(lines)

# Verify no Japanese kana remain in body
body_start = second_dashes + 1  # After the --- at line 109 (index 108)
body = '\n'.join(lines[body_start:])
jp_kana = re.compile(r'[\u3040-\u309F\u30A0-\u30FF]')
remaining = jp_kana.findall(body)
print(f"Remaining Japanese kana in body: {len(remaining)}")
if remaining:
    print(f"Remaining chars: {set(remaining)}")
    for i, line in enumerate(lines[body_start:]):
        if jp_kana.search(line):
            print(f"  Body line {i+body_start+1}: {line[:150]}")

# Write back
with open('/opt/data/ai-topics/wiki/log.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! File written.")
