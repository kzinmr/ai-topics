# Hermes Skill Lifecycle — Maintenance & Optimization Roadmap

Created: 2026-04-12

## Background

Hermes Agent generates local skills on demand (`~/.hermes/skills/`). Project-specific
skills are version-controlled in `config/hermes/skills/` and loaded via `skills.external_dirs`.

Currently 5 managed skills, 10 unmanaged local skills, 63 builtin skills.
No automated quality feedback exists. Skills degrade silently when wiki structure
or workflow changes underneath them.

## Phase 1: Manual (current)

- Skills are created by Hermes in `~/.hermes/skills/` during conversations
- Useful ones are manually reviewed and moved to `config/hermes/skills/`
- One-off skills (e.g. claude-mythos-model) are periodically deleted
- Skill edits happen when something visibly breaks or the wiki structure changes

**Sufficient for**: <10 managed skills, infrequent structural changes

**Gaps**:
- No visibility into which skills are actually used or how often
- No detection of skill rot (e.g. SKILL.md references paths that moved)
- No mechanism to notice when a Hermes-generated skill is worth promoting

## Phase 2: Observability + Triage

### 2a. New skill notification

Cron job or hook that diffs `~/.hermes/skills/` against a known baseline
and notifies (Slack/Discord) when new local skills appear:

```
Baseline: snapshot of skill dirs at last review
Trigger: daily or post-session
Output: "New local skill: <name> (category: <cat>) — review for promotion?"
```

Low effort, high signal. Prevents useful skills from being forgotten in
`~/.hermes/skills/` while only throwaway ones pile up.

### 2b. Skill lint

Static analysis of managed skills in `config/hermes/skills/`:
- Path references still valid? (e.g. `~/wiki/raw/` → was it renamed?)
- Referenced tools/commands still exist?
- SKILL.md frontmatter complete?
- Cross-references to other skills still resolve?

Could run as part of wiki lint (llm-wiki skill §3) or as a separate cron job.

### 2c. Usage tracking

Requires o11y integration (→ see `hermes-o11y-strategy.md`).

When Hermes activates a skill, log:
- Skill name
- Trigger context (user query, cron, triage)
- Outcome (success, partial, failure, abandoned)
- Duration / token cost

Even coarse metrics ("skill X activated 12 times this month, 3 failures")
enable prioritized maintenance.

## Phase 3: Eval-driven feedback loop

Bridge from o11y data to skill improvement.

### 3a. Skill evals

For each managed skill, define eval criteria:

```yaml
# Example: wiki-entity-upgrade
evals:
  - name: output_quality
    metric: "upgraded page ≥ 8KB with Timeline, Core Ideas, Key Quotes sections"
    method: llm-as-judge (binary pass/fail)
  - name: path_correctness
    metric: "all files written to ~/ai-topics/wiki/, not ~/.hermes/hermes-agent/wiki/"
    method: post-run filesystem check
  - name: index_updated
    metric: "wiki/index.md modified in same commit"
    method: git diff check
```

Eval results accumulate in Braintrust (or equivalent). Dashboard shows
skill health over time.

### 3b. Automated skill improvement proposals

When a skill's eval pass rate drops below threshold:
1. Gather recent failure traces from o11y
2. Hermes (or Shelley) analyzes failure patterns
3. Generate a proposed SKILL.md diff
4. Human reviews and merges (or auto-merge if confidence is high)

This is not RL in the traditional sense — it's **eval-driven prompt engineering**
with a human-in-the-loop gate. The "reward signal" is eval pass/fail, the "policy
update" is a SKILL.md edit.

### 3c. Skill promotion pipeline

Formalize the `~/.hermes/skills/` → `config/hermes/skills/` flow:

```
Hermes creates skill → usage tracked → passes quality threshold
  → auto-PR to ai-topics with SKILL.md + eval definition
  → human approval → merged to config/hermes/skills/
  → original removed from ~/.hermes/skills/
```

## Phase 4: Autonomous skill evolution (speculative)

Full closed loop. Hermes proposes new skills based on:
- Repeated patterns in conversation that aren't covered by existing skills
- inbox/ triage finding recurring article themes without matching wiki workflows
- Skill eval failures suggesting a skill should be split or merged

The agent generates candidate SKILL.md, runs synthetic evals against recent
wiki data, and promotes if above threshold. Human oversight shifts from
per-skill approval to periodic audit of the promotion pipeline itself.

This is where it starts resembling RL:
- **State**: current skill set + wiki structure + recent usage logs
- **Action**: create/modify/merge/delete skill
- **Reward**: downstream eval scores + usage frequency + user satisfaction signals
- **Policy**: the meta-prompt or framework that decides when to propose skill changes

Major open question: how to get reliable reward signal. User explicit feedback
("file this" / "this was useful") is sparse. Proxy metrics (skill activation
frequency, wiki page quality scores, time-to-completion) may be noisy.
This connects directly to the `queries/` issue (#1) — if we solve the
"when is output worth keeping" problem for queries, the same signal
works for skill quality.

## Dependencies

| Phase | Depends on |
|-------|------------|
| 2a | Cron job (trivial) |
| 2b | Skill lint script (medium) |
| 2c | o11y integration (hermes-o11y-strategy.md) |
| 3a | Eval framework + o11y |
| 3b | 3a + LLM-as-judge pipeline |
| 3c | 3b + GitHub PR automation |
| 4 | All of the above + meta-prompt research |

## Related

- `shelley/hermes-o11y-strategy.md` — Braintrust/Phoenix integration for trace logging
- GitHub issue #1 — queries/ directory semantics (reward signal problem)
- llm-wiki SKILL.md §2 (Query) — "painful to re-derive" judgment
