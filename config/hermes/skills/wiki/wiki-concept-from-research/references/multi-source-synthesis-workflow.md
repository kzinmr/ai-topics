# Multi-Source Synthesis Workflow

When enriching a concept page from **multiple heterogeneous sources** (e.g., an article + YouTube talk + Google Slides + X thread, all on the same topic), or when doing deep-dive enrichment across linked materials (see the Scaling Hypothesis session for a worked example):

## Workflow Steps

1. **Process each source independently first** — extract content, save as separate raw articles with correct filenames. Don't skip this step even if you'll synthesize later.
2. **Synthesize in the concept page** — add one coherent section per source, not one paragraph per source. Each section should have its own framing:
   - "Architectural Case Study" for an engineering talk
   - "Theoretical Perspective" for a founder's essay  
   - "Post-Pretraining Analysis" for a practitioner's thread
3. **Build a narrative arc** across sections — connect them explicitly:
   - "This talk addresses a core question Gwern raised in his original essay..."
   - "Daniel Han's analysis operationalizes this claim into concrete technical directions..."
4. **Update frontmatter sources LAST** — add all sources to the `sources:` list after the body content is finalized.
5. **Update log.md with a comprehensive entry** — list each source and section added.

## Pitfalls

### Patch Tool: read_file Line Number Prefixes

When `read_file` outputs a file, it prepends line numbers to each line (e.g., `   503|   500|- [[concepts/...]]`). **These line numbers are NOT part of the file content.** If you use them in `patch`'s `old_string`, you will get corrupted output with duplicate prefixes.

**Correct approach:**
- **For small edits**: Write `patch` `old_string` matching the ACTUAL file content (without read_file's line number prefix). Verify by searching for the exact text first.
- **For large edits**: Use a tool that shows content without line prefixes, or use `write_file` with the full new content.
- **For append-only**: Use `patch` with a unique `old_string` from the last line, then add your new content.

### Frontmatter Source Update Order

- **Do NOT patch `sources:` in the frontmatter first** — the line positions may shift as you add body content
- **Add body sections first** (after the frontmatter, they're stable)
- **Update frontmatter `sources:` LAST** — after all body edits are done

### Index.md Line Count Drift

The `wiki/index.md` concepts section shows concept numbers (e.g., `|   500|- [[concepts/...]]`). These are position markers. If you delete or insert an entry, re-verify that the remaining entries' position numbers are sequential. The index is maintained manually — there's no auto-renumbering.

## Example: Scaling Hypothesis Deep-Dive

The 2026-05-07 session enriched `concepts/scaling-hypothesis.md` from 4 sources:

| Source | Type | Section Created |
|--------|------|----------------|
| gwern.net/scaling-hypothesis | Article (2020) | Core thesis, strong/weak, last bits, emergent agency |
| Stanford CS25 (Hyung Won Chung) | YouTube + Slides (2024) | Architectural Case Study: structure paradox, encoder-decoder→decoder-only |
| NeurIPS 2024 (Ilya Sutskever) | YouTube (2024) | End of Pretraining: 2014 recipe, deep learning dogma, superintelligence |
| Daniel Han analysis | X thread (2024) | Post-Pretraining Playbook: 5 approaches, Memory+, Data Wall |

**Narrative arc**: Gwern framed the hypothesis → Chung showed it applies to architecture design → Sutskever declared pretraining will end → Han operationalized the post-pretraining roadmap.

## Related

- [wiki-entity-enrichment-from-article](../wiki-entity-enrichment-from-article/SKILL.md) — entity-side enrichment (broader but entity-focused)
