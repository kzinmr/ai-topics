# Beehiiv 403 → AINews Content Substitution Pattern

## Problem
When beehiiv tracking URLs return HTTP 403 (expired tracking tokens, ~12-24h after send), you lose access to the newsletter's curated article content. The inbox pre-triage summary provides estimated topics but lacks the technical depth needed for triage accuracy.

## Solution (validated July 2026)
When a beehiiv newsletter's links are all 403, check if **AINews** (pub_id=1084089, swyx's daily bulletin) from the **same cron batch** covers the same topic. AINews is a daily curation that often covers the same major stories as other newsletters with more technical detail.

**Detection**: Search other newsletters in the same batch for the topic keyword (e.g., "Tencent", "Hy3", "Hunyuan"). If AINews is present, extract the topic coverage from its resolved body.

**Concrete example**: July 7, 2026 batch — "Tencent's Open Model Crashes the Frontier" (beehiiv, all 403) and "AINews: The Field Guide to Fable" had substantial Tencent Hy3 coverage including:
- Exact model specs (295B MoE, 21B active, 192 experts, 256K context)
- vLLM day-0 support with upstreamed Tencent kernels
- 2.95x mixed-length decode gain, 24% TTFT / 17% TPOT improvements
- Nous Portal free access announcement
- Comparison vs GLM-5.2

## When this works
- The target topic is a **major AI event** (model release, policy change, benchmark milestone)
- AINews is in the **same batch time window** (AINews publishes daily ~04:00 UTC)
- The topic is technical enough that AINews's detail-oriented curation covers the relevant specifics

## When this does NOT work
- Obscure or niche topics that only the beehiiv newsletter covers
- AINews is absent from the batch
- The beehiiv topic is a personal essay, interview, or opinion piece unlikely to appear in AINews

## Integration with existing 403 handling
Use this **after** the inbox summary check (the inbox summary is still the primary source for topic identification). AINews substitution provides the **content depth** that the inbox summary's estimated-topics-only report cannot.

## Pitfall
AINews may not name the specific beehiiv publication. The substitution is for **topic content** not **attribution**. In the triage JSON, use the beehiiv newsletter's raw_path as source and note "content verified via AINews cross-reference" in the reason_ja.
