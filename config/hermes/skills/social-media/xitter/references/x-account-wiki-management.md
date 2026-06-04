# X Account & Wiki Entity Management

## Workflow
1. Add to `config/feeds/x-accounts.yaml`
2. Generate skeleton: `cd ~/ai-topics && ~/.hermes/hermes-agent/venv/bin/python ~/scripts/build_x_wiki.py --handle @Username`
3. Enrich: research person's X activity, blog posts, open source, key ideas
4. Remove `status: skeleton`, add detailed bio, cross-links, quality target: match antirez-com.md depth
5. Update index.md under entities section
6. Commit: `cd ~/ai-topics && git add wiki/ config/feeds/x-accounts.yaml && git commit && git push`

## Key Concepts to Cross-Link
- Multi-agent patterns → `[[back-of-house-multi-agent-patterns]]`
- Single-agent limitations → `[[single-agent-ceiling]]`
- Orchestration → `[[session-hierarchy-management]]`

## Pitfalls
- Do NOT add duplicate entries to x-accounts.yaml — always search first
- Skeleton pages have TODO markers — must fill during enrichment
- YAML folded scalars in x-accounts.yaml are fragile with patch — use execute_code + yaml.safe_load
