---
title: "Claude Code's source code has been leaked via a map file in their NPM registry"
url: "https://substack.com/redirect/e0cfc9bd-db50-4c4f-b454-0d11ae24f988?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-09T16:28:25.458647+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# Claude Code's source code has been leaked via a map file in their NPM registry

Source: https://substack.com/redirect/e0cfc9bd-db50-4c4f-b454-0d11ae24f988?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Intersected available info on the web with the source for this list of new features:
UNRELEASED PRODUCTS & MODES
1. KAIROS -- Persistent autonomous assistant mode driven by periodic <tick> prompts. More autonomous when terminal unfocused. Exclusive tools: SendUserFileTool, PushNotificationTool, SubscribePRTool. 7 sub-feature flags.
2. BUDDY -- Tamagotchi-style virtual companion pet. 18 species, 5 rarity tiers, Mulberry32 PRNG, shiny variants, stat system (DEBUGGING/PATIENCE/CHAOS/WISDOM/SNARK). April 1-7 2026 teaser window.
3. ULTRAPLAN -- Offloads planning to a remote 30-minute Opus 4.6 session. Smart keyword detection, 3-second polling, teleport sentinel for returning results locally.
4. Dream System -- Background memory consolidation (Orient -> Gather -> Consolidate -> Prune). Triple trigger gate: 24h + 5 sessions + advisory lock. Gated by tengu_onyx_plover.
INTERNAL-ONLY TOOLS & SYSTEMS
5. TungstenTool -- Ant-only tmux virtual terminal giving Claude direct keystroke/screen-capture control. Singleton, blocked from async agents.
6. Magic Docs -- Ant-only auto-documentation. Files starting with "# MAGIC DOC:" are tracked and updated by a Sonnet sub-agent after each conversation turn.
7. Undercover Mode -- Prevents Anthropic employees from leaking internal info (codenames, model versions) into public repo commits. No force-OFF; dead-code-eliminated from external builds.
ANTI-COMPETITIVE & SECURITY DEFENSES
8. Anti-Distillation -- Injects anti_distillation: ['fake_tools'] into every 1P API request to poison model training from scraped traffic. Gated by tengu_anti_distill_fake_tool_injection.
UNRELEASED MODELS & CODENAMES
9. opus-4-7, sonnet-4-8 -- Confirmed as planned future versions (referenced in undercover mode instructions).
10. "Capybara" / "capy v8" -- Internal codename for the model behind Opus 4.6. Hex-encoded in the BUDDY system to avoid build canary detection.
11. "Fennec" -- Predecessor model alias. Migration: fennec-latest -> opus, fennec-fast-latest -> opus[1m] + fast mode.
UNDOCUMENTED BETA API HEADERS
12. afk-mode-2026-01-31 -- Sticky-latched when auto mode activates
15. fast-mode-2026-02-01 -- Opus 4.6 fast output
16. task-budgets-2026-03-13 -- Per-task token budgets
17. redact-thinking-2026-02-12 -- Thinking block redaction
18. token-efficient-tools-2026-03-28 -- JSON tool format (~4.5% token saving)
19. advisor-tool-2026-03-01 -- Advisor tool
20. cli-internal-2026-02-09 -- Ant-only internal features
200+ SERVER-SIDE FEATURE GATES
21. tengu_penguins_off -- Kill switch for fast mode
22. tengu_scratch -- Coordinator mode / scratchpad
23. tengu_hive_evidence -- Verification agent
24. tengu_surreal_dali -- RemoteTriggerTool
25. tengu_birch_trellis -- Bash permissions classifier
26. tengu_amber_json_tools -- JSON tool format
27. tengu_iron_gate_closed -- Auto-mode fail-closed behavior
28. tengu_amber_flint -- Agent swarms killswitch
29. tengu_onyx_plover -- Dream system
30. tengu_anti_distill_fake_tool_injection -- Anti-distillation
31. tengu_session_memory -- Session memory
32. tengu_passport_quail -- Auto memory extraction
33. tengu_coral_fern -- Memory directory
34. tengu_turtle_carbon -- Adaptive thinking by default
35. tengu_marble_sandcastle -- Native binary required for fast mode
YOLO CLASSIFIER INTERNALS (previously only high-level known)
36. Two-stage system: Stage 1 at max_tokens=64 with "Err on the side of blocking"; Stage 2 at max_tokens=4096 with <thinking>
37. Three classifier modes: both (default), fast, thinking
38. Assistant text stripped from classifier input to prevent prompt injection
39. Denial limits: 3 consecutive or 20 total -> fallback to interactive prompting
40. Older classify_result tool schema variant still in codebase
COORDINATOR MODE & FORK SUBAGENT INTERNALS
41. Exact coordinator prompt: "Every message you send is to the user. Worker results are internal signals -- never thank or acknowledge them."
42. Anti-pattern enforcement: "Based on your findings, fix the auth bug" explicitly called out as wrong
43. Fork subagent cache sharing: Byte-identical API prefixes via placeholder "Fork started -- processing in background" tool results
44. <fork-boilerplate> tag prevents recursive forking
45. 10 non-negotiable rules for fork children including "commit before reporting"
DUAL MEMORY ARCHITECTURE
46. Session Memory -- Structured scratchpad for surviving compaction. 12K token cap, fixed sections, fires every 5K tokens + 3 tool calls.
47. Auto Memory -- Durable cross-session facts. Individual topic files with YAML frontmatter. 5-turn hard cap. Skips if main agent already wrote to memory.
48. Prompt cache scope "global" -- Cross-org caching for the static system prompt prefix
