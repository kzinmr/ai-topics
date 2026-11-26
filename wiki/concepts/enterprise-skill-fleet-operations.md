---
title: "Enterprise Skill Fleet Operations (Uber aifx Case)"
created: 2026-11-26
updated: 2026-11-26
type: concept
tags: [agent-skills, enterprise-agents, harness-engineering, agent-observability, evaluation, developer-tooling]
confidence: high
sources:
  - raw/articles/2026-11-23_ubereng_how-uber-evals-1-million-agent-skill-invocations-a-month.md
related:
  - concepts/agent-skills
  - concepts/agent-skill-ecosystem-missing-package-manager
  - concepts/code-mode
  - concepts/dark-factory-software-factory
  - concepts/enterprise-ai-cost-management
---

# Enterprise Skill Fleet Operations

How a large enterprise runs thousands of [[concepts/agent-skills|agent skills]] as a managed fleet: distribution, tiering, discovery, telemetry, evaluation, cost control, and self-service bug reporting. The canonical public case is **Uber** (X Article "How Uber Evals 1 Million Agent Skill Invocations a Month", 2026-11-23, 21.5K bookmarks).

## Scale (Uber, Oct 2025 → Nov 2026)

- Skills marketplace: **1 skill → 5,000+ in one year**; thousands of authors; **>1M skill invocations/month**.
- Follows the Aug 2026 "Software Factory" report (~3,600 skills, 30K executions/day) — see [[concepts/dark-factory-software-factory]].

## Architecture: One Repo, One CLI, Three Tiers

- **One Git repository** as the marketplace: version control supplies owner, review, history — partially answering the missing-registry problem identified in [[concepts/agent-skill-ecosystem-missing-package-manager]].
- **`aifx` CLI**: installs skills/plugins per-agent (Claude Code, Codex, OpenCode all keep the same skills), layered config merge (company → team → repo → directory → user → local override, additive only), role-based personas, MCP calls, observability.
- **Three tiers with rising quality bar**: Domain (team-owned, 1 peer approval + CI) → Core (platform-reviewed) → Always-on (~100 skills for every employee's first run).

## Telemetry & Cost Accounting

- OpenTelemetry hooks emit skill/tool events (skill, version, agent-chosen vs user-typed; no prompt text/file contents) → **12 per-skill measures** (users, retention, cost, latency, errors).
- **Cost per invocation** = session cost-total snapshot before the call minus after it; includes reading the skill and downstream turns.
- Cost-reduction levers (measured): Code Mode scripting (below), cheaper-model worker subagents (tracing skill −46%/invocation), run-script-at-load-time (search skill −32%), moving polling to a background agent (~1/3 of spend in top-20 sessions).

## Evaluation System

- Eval suite composition: **~5% golden cases** (fixed input/output, tool mocks), **~80% real prompts graded on trajectory**, **~15% author-judged**.
- Runs in clean rooms (Minion, AES sandbox, devpods) — catches "works on my machine" dependencies.
- Counterintuitive finding: **70–90% pass rate can be more useful than 100%** — a 100%-passing eval may be too weak to detect regressions.
- **Ablation**: replay real prompts with/without the skill (or parts), blind judge picks the winner. Warehouse-query skill ablation: without it, +13% tool calls, 6× tool errors, +31% time; skill-side answer won 87% of comparisons.
- **Linter** of distilled code smells: numbered one-objective steps, concrete command + result check per step, mandatory error-recovery table.

## Code Mode Adoption

Uber independently arrived at [[concepts/code-mode]] (after Cloudflare's post): deterministic flows moved to gateway scripts; >100 MCP tool preloads (50–70K tokens before the first user message) eliminated; `.mcp.json` files blocked in skills/plugins; code-mode skills became named packages other skills reference.

## Agents Filing Their Own Bugs: Papercuts

- Always-on `log-papercut` skill lets agents file structured friction reports unasked (tried / expected / happened / fix). Thousands filed in 3 months; hundreds fixed.
- Example fixes: commit-message race via shared temp file, epoch-seconds-vs-milliseconds unit bug, silent wrong-key config lookup, CI-wait-on-repo-with-no-CI 404 loop.
- Human signals (Fawkes maintenance PRs: comments/rejections) feed back into eval sets.

## Relation to the "Missing Package Manager" Debate

Uber's answer to the ecosystem's missing npm/cargo primitives (registry, pinning, provenance, dependency resolution) is **internalization**: one Git repo + aifx + platform-team review + KPI'd ownership. It reproduces package-manager properties inside one org, but confirms the public-ecosystem gap — nothing here helps skills installed from outside the marketplace.

## Open Problems / Roadmap (Uber)

A/B testing skills; per-model SKILL.md compilation (phrasing/length works differently per model family); indexed trace collection; skill recommendations; a single task router across agents.

## See Also

- [[concepts/agent-skills]] — the SKILL.md open standard itself
- [[concepts/agent-skill-ecosystem-missing-package-manager]] — the public-ecosystem counterpart
- [[concepts/code-mode]] — deterministic flows as code
- [[concepts/dark-factory-software-factory]] — Uber factory case study (Aug 2026)
- [[concepts/enterprise-ai-cost-management]] — Uber's broader cost-equation work
