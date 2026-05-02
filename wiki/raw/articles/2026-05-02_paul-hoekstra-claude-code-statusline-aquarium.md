# I turned my Claude Code statusline into an aquarium

**Author:** Paul Hoekstra | **Source:** Paul's Pipeline (Substack)
**URL:** https://paulhoekstra.substack.com/p/i-turned-my-claude-code-statusline
**Published:** April 29, 2026

## Summary

Guide to customizing the Claude Code statusline — a shell script receiving JSON via stdin that runs after every assistant reply, capable of displaying real-time metrics and creative visualizations.

## Key Concepts

### Mechanism
- Claude Code passes JSON blob to shell script via stdin
- Script processes data, prints output to stdout
- Runs after every assistant reply
- `refreshInterval` setting enables timer-based re-runs

### Recommended Setup
- `/statusline build` command auto-generates scripts
- Saves to `~/.claude/`, updates settings automatically

### Data Density ("All the Bells and Whistles")
- Core: model name, directory, git worktree, active agent
- Usage: context window %, session cost, duration, prompt cache reads
- Advanced: rate limit bars (5h/7d), cache TTL proxy

### Infrastructure/Ops
- Vercel deploy boards, AWS spend monitoring, PagerDuty status
- GitHub PRs awaiting review, Kubernetes context/pod readiness

### Personal Assistant
- Next meeting display, currently playing music, weather

### Visual Tools
- `npx ccstatusline` — widget picker with live preview
- Powerline mode, clickable PR links, skill names

### Creative
- Doom HUD (health bar bleeding as context fills)
- Aquarium (rate limits/system health as animated fish)
