---
title: "TextArena"
type: entity
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - reinforcement-learning
  - multi-agent
  - game-based
  - open-source
aliases:
  - textarena
status: active
sources:
  - https://github.com/LeonGuertler/TextArena
  - https://www.textarena.ai/
  - https://www.textarena.ai/blog
  - https://arxiv.org/abs/2504.11442
related:
  - "[[concepts/evaluation/ai-benchmarks-and-evals]]"
  - "[[concepts/ai-benchmarks/unstable-baselines]]"
---

# TextArena

A collection of **100+ competitive text-based games** for benchmarking and training Large Language Models, developed by Leon Guertler, Bobby Cheng, Simon Yu, Bo Liu, Leshem Choshen, and Cheston Tan. Provides an OpenAI Gym-style interface for training, evaluating, and benchmarking models in interactive text environments.

**GitHub**: [LeonGuertler/TextArena](https://github.com/LeonGuertler/TextArena) (401+ stars) | **Website**: [textarena.ai](https://textarena.ai) | **Paper**: [arXiv 2504.11442](https://arxiv.org/abs/2504.11442) | **PyPI**: [textarena](https://pypi.org/project/textarena/)

---

## What It Provides

TextArena offers a comprehensive platform with three key components:

### 1. 100+ Text-Based Games

A diverse suite of games spanning single-player, two-player, and multi-player formats:
- **Board games**: TicTacToe, Chess (text-based), Go, SettlersOfCatan
- **Card games**: KuhnPoker, TexasHold'em (text-based variants)
- **Puzzle games**: SimpleTak, FifteenPuzzle, RushHour
- **Strategy games**: Negotiation, Diplomacy variants

Each game follows the **OpenAI Gym interface**: `env.reset()` → `env.step()` → `env.close()`, making it trivial to integrate with existing RL and LLM frameworks.

### 2. Online Evaluation Platform

A hosted leaderboard at textarena.ai where researchers can:
- Submit models for automated evaluation against other models
- Participate in multiplayer game tournaments
- Track TrueSkill-based rankings over time

### 3. Python SDK (pip package)

```python
import textarena as ta

agents = {
    0: ta.agents.OpenRouterAgent(model_name="GPT-4o-mini"),
    1: ta.agents.OpenRouterAgent(model_name="anthropic/claude-3.5-haiku"),
}

env = ta.make(env_id="TicTacToe-v0")
env = ta.wrappers.SimpleRenderWrapper(env=env)
env.reset(num_players=len(agents))

done = False
while not done:
    player_id, observation = env.get_observation()
    action = agents[player_id](observation)
    done, step_info = env.step(action=action)

rewards, game_info = env.close()
```

---

## Architecture

### Backend Evolution

The platform evolved through three versions:

| Version | Date | Key Features |
|---------|------|-------------|
| **v1 (Early release)** | Jan 2025 | Basic API + polling, Supabase database, Vercel frontend, ngrok backend |
| **v2 (Sleepless fixes)** | Feb 2025 | Improved scalability, better matchmaking |
| **v3 (Good enough)** | Jul 2025 | 100+ games, simplified states, observation wrappers |

Key architectural decisions:
- **Supabase** for database (recommended by Henry Mao)
- **Vercel** for frontend deployment (recommended by Henry Mao)
- **WebSocket vs. API polling**: Started with API polling for simplicity, acknowledged scalability limits
- **MIT license** for both backend and frontend code (open-sourced for researchers)

### Matchmaking Flow

1. Client calls `register_online_model()` → adds to Supabase
2. Client calls `make_online()` → enters matchmaking queue
3. Client **polls** every n seconds for match found
4. Matched → server sends observation → client returns action
5. Repeat until game ends → rewards computed → TrueSkill updated

---

## Key Research Initiatives

### SPIRAL (Jul 2025)

**SPIRAL**: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning.

Introduces RL via self-play on TextArena games as a training paradigm. Demonstrates that multi-agent, multi-turn reinforcement learning on competitive text-based games can improve LLM reasoning capabilities.

### MindGames Competition (NeurIPS 2025)

Announced Jul 14, 2025: a NeurIPS 2025 competition for training LLMs on TextArena games that require **theory of mind** — games where players must model and predict opponent behavior.

### UnstableBaselines (Jun 2025)

A lightweight async online RL library specifically built for training LLMs on TextArena games. See [[concepts/ai-benchmarks/unstable-baselines]].

---

## Timeline

| Date | Event |
|------|-------|
| Sep 2024 | Repository created |
| Jan 31, 2025 | Initial demo release, highlighted by **Andrej Karpathy** (crashed servers) |
| Feb 14, 2025 | New stable version for pip and website |
| Apr 16, 2025 | TextArena paper released (arXiv 2504.11442) |
| Jun 22, 2025 | UnstableBaselines released |
| Jul 1, 2025 | v0.6.9: 100 games, simplified states, observation wrappers |
| Jul 1, 2025 | SPIRAL paper released |
| Jul 14, 2025 | MindGames NeurIPS 2025 competition announced |
| Jul 31, 2025 | SettlersOfCatan added |

---

## Relationship to Benchmark Ecosystem

TextArena sits at the intersection of **game-based agent evaluation** and **reinforcement learning training**. Unlike static benchmarks (MMLU, GPQA), it provides:

1. **Dynamic evaluation**: Models interact in real-time with opponents
2. **Multi-agent setting**: Natural testbeds for agent-agent interaction
3. **Theory of mind**: Games require modeling opponent behavior
4. **Training signal**: Games provide natural reward signals for RL
5. **TrueSkill ranking**: Continuous competitive evaluation rather than one-off scores

Complements other game-based benchmarks like [[concepts/ai-benchmarks/factorio-learning-environment]] (single-agent factory building) and [[concepts/ai-benchmarks/agent-survival-benchmark]] (PvP survival).

---

## Team

| Member | Role |
|--------|------|
| **Leon Guertler** | Co-founder, primary developer |
| **Bobby Cheng** | Co-founder |
| **Simon Yu** | Co-author |
| **Bo Liu** | Co-author |
| **Leshem Choshen** | Co-author |
| **Cheston Tan** | Co-author |

---

## Related Pages

- [[concepts/ai-benchmarks/unstable-baselines]] — UnstableBaselines RL library for TextArena
- [[concepts/ai-benchmarks/factorio-learning-environment]] — Another game-based agent evaluation
- [[concepts/ai-benchmarks/agent-survival-benchmark]] — PvP agent survival
- [[concepts/evaluation/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[entities/florian-brand]] — @xeophon, benchmark analyst who tracks game-based evals

## Sources

1. Guertler, L., Cheng, B., Yu, S., Liu, B., Choshen, L., Tan, C. (2025). "TextArena." arXiv:2504.11442. https://arxiv.org/abs/2504.11442
2. TextArena GitHub. https://github.com/LeonGuertler/TextArena
3. TextArena Website. https://textarena.ai/
4. TextArena Blog: "How we built TextArena." https://www.textarena.ai/blog
5. UnstableBaselines. https://github.com/TextArena/UnstableBaselines
6. SPIRAL Paper. https://github.com/LeonGuertler/TextArena (announced Jul 2025)
